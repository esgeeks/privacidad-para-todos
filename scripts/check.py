#!/usr/bin/env python3
"""Verifica las herramientas listadas en README.md.

- Para cada URL de GitHub: consulta la API pública (repos/{owner}/{repo}) y
  reporta último push, estrellas y licencia. Marca como inactivo si no hay
  push en los últimos 12 meses, o si el repo está archivado.
- Para URLs que no son de GitHub (tiendas, sitios oficiales): comprueba que
  respondan con código 200.
- Si encuentra repos inactivos, los mueve (no los borra) a la tabla
  "En observación" / "Under review" de README.md y README.en.md.

Uso:
    python3 scripts/check.py [--token TOKEN] [--no-write]

Variables de entorno:
    GITHUB_TOKEN  Token opcional para subir el límite de la API de GitHub
                  (60 peticiones/hora sin token, 5000/hora con token).
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
README_ES = REPO_ROOT / "README.md"
README_EN = REPO_ROOT / "README.en.md"

SYSTEM_SECTIONS = {
    "Android": "Android",
    "iPhone / iOS": "iPhone / iOS",
    "Windows": "Windows",
    "macOS": "macOS",
    "Linux": "Linux",
    "Multiplataforma y navegador": "Multiplataforma y navegador",
}

INACTIVE_MONTHS_THRESHOLD = 12
USER_AGENT = "privacidad-para-todos-check-script (+https://github.com)"
HTTP_TIMEOUT = 12

LINK_RE = re.compile(r"^\|\s*(?:\[([^\]]+)\]\((https?://[^\)]+)\)|([^|]+?))\s*\|")
GITHUB_RE = re.compile(r"^https?://github\.com/([^/]+)/([^/#?]+)")


@dataclass
class ToolRow:
    system: str
    raw_line: str
    name: str
    url: str | None


@dataclass
class GithubResult:
    owner: str
    repo: str
    url: str
    pushed_at: str | None = None
    stars: int | None = None
    license: str | None = None
    archived: bool = False
    months_since_push: float | None = None
    inactive: bool = False
    error: str | None = None


@dataclass
class UrlResult:
    url: str
    status: int | None = None
    ok: bool = False
    error: str | None = None


def parse_rows(readme_path: Path) -> list[ToolRow]:
    """Extrae filas de tablas de herramientas, agrupadas por sección de sistema."""
    rows: list[ToolRow] = []
    current_system: str | None = None
    in_table = False

    for line in readme_path.read_text(encoding="utf-8").splitlines():
        header_match = re.match(r"^##\s+(.*)$", line)
        if header_match:
            title = header_match.group(1).strip()
            # README.en.md usa headers distintos; mapeamos por índice de orden.
            current_system = title if title in SYSTEM_SECTIONS else _map_en_header(title)
            in_table = False
            continue

        if not line.startswith("|"):
            in_table = False
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or all(c == "" for c in cells):
            continue
        if set(cells[0]) <= {"-", " "}:
            # fila separadora `|---|---|...`
            continue
        if cells[0] in ("Herramienta", "Tool"):
            in_table = True
            continue
        if not in_table or current_system is None:
            continue

        m = LINK_RE.match(line)
        if not m:
            continue
        name = (m.group(1) or m.group(3) or "").strip()
        url = m.group(2)
        if not name:
            continue
        rows.append(ToolRow(system=current_system, raw_line=line, name=name, url=url))

    return rows


def _map_en_header(title: str) -> str | None:
    en_to_es = {
        "Android": "Android",
        "iPhone / iOS": "iPhone / iOS",
        "Windows": "Windows",
        "macOS": "macOS",
        "Linux": "Linux",
        "Cross-platform and browser": "Multiplataforma y navegador",
    }
    return en_to_es.get(title)


def github_api_get(path: str, token: str | None) -> dict:
    req = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/vnd.github+json",
            **({"Authorization": f"Bearer {token}"} if token else {}),
        },
    )
    with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
        return json.loads(resp.read().decode("utf-8"))


def check_github(url: str, token: str | None, cache: dict[str, GithubResult]) -> GithubResult:
    m = GITHUB_RE.match(url)
    owner, repo = m.group(1), m.group(2)
    repo = re.sub(r"\.git$", "", repo)
    key = f"{owner}/{repo}".lower()
    if key in cache:
        return cache[key]

    result = GithubResult(owner=owner, repo=repo, url=url)
    try:
        data = github_api_get(f"/repos/{owner}/{repo}", token)
        result.pushed_at = data.get("pushed_at")
        result.stars = data.get("stargazers_count")
        license_info = data.get("license") or {}
        result.license = license_info.get("spdx_id") or license_info.get("name")
        result.archived = bool(data.get("archived"))
        if result.pushed_at:
            pushed = datetime.strptime(result.pushed_at, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )
            delta_days = (datetime.now(timezone.utc) - pushed).days
            result.months_since_push = round(delta_days / 30, 1)
            result.inactive = result.months_since_push > INACTIVE_MONTHS_THRESHOLD or result.archived
    except urllib.error.HTTPError as e:
        if e.code == 404:
            result.error = "404 (repo no encontrado / posiblemente renombrado o eliminado)"
        elif e.code == 403:
            result.error = "403 (límite de la API de GitHub alcanzado; usa --token)"
        else:
            result.error = f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        result.error = str(e)

    cache[key] = result
    time.sleep(0.2)
    return result


def check_url(url: str, cache: dict[str, UrlResult]) -> UrlResult:
    if url in cache:
        return cache[url]
    result = UrlResult(url=url)
    for method in ("HEAD", "GET"):
        try:
            req = urllib.request.Request(url, method=method, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=HTTP_TIMEOUT) as resp:
                result.status = resp.status
                result.ok = 200 <= resp.status < 300
            break
        except urllib.error.HTTPError as e:
            result.status = e.code
            result.ok = 200 <= e.code < 300
            if e.code in (405, 403) and method == "HEAD":
                continue
            break
        except Exception as e:  # noqa: BLE001
            result.error = str(e)
    cache[url] = result
    time.sleep(0.1)
    return result


def sync_en_observacion(readme_path: Path, inactive_rows: list[tuple[ToolRow, GithubResult]], lang: str) -> None:
    """Mueve filas inactivas de sus tablas a la sección En observación / Under review."""
    if not inactive_rows:
        return

    text = readme_path.read_text(encoding="utf-8")

    for row, gh in inactive_rows:
        if row.raw_line in text:
            text = text.replace(row.raw_line + "\n", "")

    today = datetime.now(timezone.utc).date().isoformat()
    if lang == "es":
        header = "| Sistema | Herramienta | Último push detectado | Verificado el |\n|---|---|---|---|\n"
        section_title = "## En observación"
    else:
        header = "| System | Tool | Last detected push | Checked on |\n|---|---|---|---|\n"
        section_title = "## Under review"

    new_rows = ""
    for row, gh in inactive_rows:
        pushed = gh.pushed_at.split("T")[0] if gh.pushed_at else "?"
        new_rows += f"| {row.system} | [{row.name}]({row.url}) | {pushed} | {today} |\n"

    marker = section_title + "\n"
    idx = text.find(marker)
    if idx == -1:
        return
    insert_at = idx + len(marker)
    # salta el párrafo introductorio hasta la línea en blanco siguiente
    next_blank = text.find("\n\n", insert_at)
    if next_blank == -1:
        return
    insert_at = next_blank + 2
    text = text[:insert_at] + header + new_rows + "\n" + text[insert_at:]
    readme_path.write_text(text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    parser.add_argument("--no-write", action="store_true", help="No modificar los README, solo reportar.")
    args = parser.parse_args()

    if not README_ES.exists():
        print(f"No se encontró {README_ES}", file=sys.stderr)
        return 1

    rows = parse_rows(README_ES)

    gh_cache: dict[str, GithubResult] = {}
    url_cache: dict[str, UrlResult] = {}

    per_system_counts: dict[str, int] = {s: 0 for s in SYSTEM_SECTIONS}
    inactive: list[tuple[ToolRow, GithubResult]] = []
    failed_urls: list[UrlResult] = []
    github_checked = 0
    url_checked = 0
    no_link = 0

    for row in rows:
        if row.system in per_system_counts:
            per_system_counts[row.system] += 1

        if row.url is None:
            no_link += 1
            continue

        if GITHUB_RE.match(row.url):
            gh = check_github(row.url, args.token, gh_cache)
            github_checked += 1
            if gh.error:
                print(f"[GITHUB ERROR] {row.system} · {row.name} · {row.url} · {gh.error}")
            elif gh.inactive:
                print(
                    f"[INACTIVO] {row.system} · {row.name} · último push {gh.pushed_at} "
                    f"(~{gh.months_since_push} meses) · estrellas={gh.stars} · licencia={gh.license}"
                )
                inactive.append((row, gh))
            else:
                print(
                    f"[OK] {row.system} · {row.name} · último push {gh.pushed_at} "
                    f"(~{gh.months_since_push} meses) · estrellas={gh.stars} · licencia={gh.license}"
                )
        else:
            ur = check_url(row.url, url_cache)
            url_checked += 1
            if ur.ok:
                print(f"[OK] {row.system} · {row.name} · {row.url} · HTTP {ur.status}")
            else:
                reason = ur.error or f"HTTP {ur.status}"
                print(f"[FALLO] {row.system} · {row.name} · {row.url} · {reason}")
                failed_urls.append(ur)

    if not args.no_write:
        sync_en_observacion(README_ES, inactive, "es")
        if README_EN.exists():
            en_rows = parse_rows(README_EN)
            en_by_url = {r.url: r for r in en_rows if r.url}
            en_inactive = []
            for row, gh in inactive:
                en_row = en_by_url.get(row.url)
                if en_row:
                    en_inactive.append((en_row, gh))
            sync_en_observacion(README_EN, en_inactive, "en")

    print("\n" + "=" * 70)
    print("RESUMEN")
    print("=" * 70)
    total = sum(per_system_counts.values())
    for system, count in per_system_counts.items():
        print(f"  {system}: {count} herramientas")
    print(f"  TOTAL: {total} herramientas")
    print(f"\n  Repos de GitHub verificados: {github_checked}")
    print(f"  URLs no-GitHub verificadas: {url_checked}")
    print(f"  Entradas sin URL (ajustes nativos, etc.): {no_link}")
    print(f"\n  En observación (>{INACTIVE_MONTHS_THRESHOLD} meses sin push o archivado): {len(inactive)}")
    for row, gh in inactive:
        print(f"    - {row.system} · {row.name} · {row.url}")
    print(f"\n  URLs que no respondieron 200: {len(failed_urls)}")
    for ur in failed_urls:
        print(f"    - {ur.url} · {ur.error or ur.status}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
