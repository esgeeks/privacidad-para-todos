# Contribuir / Contributing

## Español

Gracias por querer mejorar esta lista. Antes de abrir un issue o un pull request, revisa el criterio de entrada — así evitamos ida y vuelta innecesaria.

### Criterio de entrada

Una herramienta entra en la lista solo si cumple **las cuatro** condiciones:

1. **Sin root, sin jailbreak, sin compilar.** Debe instalarse desde una tienda oficial, un instalador, un paquete (`.deb`/`.rpm`/Flatpak/AppImage) o un script de un clic que cualquier persona sin conocimientos técnicos pueda ejecutar.
2. **Mantenida.** Tiene que mostrar actividad (commit, release o versión en tienda) en los últimos 12 meses. `scripts/check.py` verifica esto automáticamente para los repos de GitHub.
3. **Gratuita, o con una versión gratuita real y usable.** No vale un trial de 7 días disfrazado de "versión gratis". El plan gratuito tiene que servir para algo por sí solo.
4. **Protege el propio dispositivo.** Fuera de alcance: pentesting, auditoría de redes ajenas, OSINT sobre terceros, exploits, herramientas de ataque WiFi/Bluetooth, phishing, C2, o cualquier cosa pensada para intervenir un sistema que no es el tuyo.

### Cómo proponer una herramienta

Abre un issue con la plantilla **"Proponer herramienta"** ([.github/ISSUE_TEMPLATE/proponer-herramienta.yml](.github/ISSUE_TEMPLATE/proponer-herramienta.yml)) o directamente un pull request añadiendo la fila a la tabla correspondiente, respetando el formato de columnas existente:

```
| Nombre | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
```

- Enlaza el nombre a la URL oficial.
- "Qué hace" en una sola frase, sin superlativos de marketing.
- Indica la fecha o versión más reciente que puedas verificar, no una fecha aproximada inventada.
- Si la herramienta requiere terminal o pasos técnicos, márcala como `Intermedio`.

### Reportar una herramienta abandonada

Si detectas que una herramienta lleva más de 12 meses sin actividad, abre un issue con la plantilla **"Herramienta abandonada"** ([.github/ISSUE_TEMPLATE/herramienta-abandonada.yml](.github/ISSUE_TEMPLATE/herramienta-abandonada.yml)). La moveremos a la sección "En observación" con la fecha, no la borraremos de inmediato — puede que solo esté en pausa.

### Lo que no aceptamos

- Herramientas de pentesting, OSINT ofensivo, hacking de redes o cuentas ajenas, exploits.
- Enlaces de afiliados o con parámetros de tracking.
- Software de pago sin versión gratuita real.
- Herramientas que requieran root/jailbreak persistente o compilar desde código fuente.
- Traducciones de nombres de menús nativos de Android/iOS/Windows en la versión en español — se dejan en su idioma original porque así aparecen en la pantalla del usuario.

---

## English

Thanks for wanting to improve this list. Before opening an issue or pull request, check the entry criteria below — it saves everyone a back-and-forth.

### Entry criteria

A tool is added to the list only if it meets **all four** conditions:

1. **No root, no jailbreak, no compiling.** It must install from an official store, an installer, a package (`.deb`/`.rpm`/Flatpak/AppImage), or a one-click script that anyone without technical knowledge can run.
2. **Maintained.** It must show activity (a commit, release, or store version) within the last 12 months. `scripts/check.py` verifies this automatically for GitHub repos.
3. **Free, or with a real, usable free tier.** A 7-day trial disguised as a "free version" doesn't count. The free tier has to be genuinely useful on its own.
4. **Protects the user's own device.** Out of scope: pentesting, auditing other people's networks, OSINT on third parties, exploits, WiFi/Bluetooth attack tools, phishing, C2, or anything meant to compromise a system that isn't yours.

### How to propose a tool

Open an issue using the **"Propose a tool"** template ([.github/ISSUE_TEMPLATE/proponer-herramienta.yml](.github/ISSUE_TEMPLATE/proponer-herramienta.yml)), or submit a pull request adding the row directly to the relevant table, matching the existing column format:

```
| Name | What it does | Install | Spanish UI? | License | Last updated | Level |
```

- Link the name to the official URL.
- "What it does" in a single sentence, no marketing superlatives.
- Give the most recent date or version you can verify — not a made-up approximate date.
- If the tool requires a terminal or technical steps, mark it as `Intermediate`.

### Reporting an abandoned tool

If you notice a tool has had no activity for more than 12 months, open an issue using the **"Abandoned tool"** template ([.github/ISSUE_TEMPLATE/herramienta-abandonada.yml](.github/ISSUE_TEMPLATE/herramienta-abandonada.yml)). We'll move it to the "Under review" section with the date rather than deleting it outright — it might just be paused.

### What we don't accept

- Pentesting tools, offensive OSINT, hacking other people's networks or accounts, exploits.
- Affiliate links or links with tracking parameters.
- Paid software with no real free tier.
- Tools that require persistent root/jailbreak or compiling from source.
- Translated native menu names for Android/iOS/Windows in the Spanish version — they stay in their original language because that's how they appear on the user's screen.
