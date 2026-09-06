# Privacidad para todos · the Anonimato Platino repository (EsGeeks)

[Español](README.md) · English

Privacy and anonymity tools for regular people, organized by system: Android, iPhone, Windows, Mac and Linux. No root, no technical jargon, and with a clear bar: only maintained, free (or with a genuinely usable free tier) tools that protect your own device.

Built for someone with no technical background who wants to stop giving away their data without having to learn to code or touch a terminal (unless they want to).

## 📘 This repository is the bonus for the "Anonimato Platino" manual

This repo is the living companion to the **Anonimato Platino** manual: the manual teaches you the method (what to change, in what order, why each step matters), and this repository carries the list of tools, which changes every few months. That way you're not stuck with an outdated PDF guide.

👉 [ALEXIS: landing page URL]

## How to use this list

- **Level**: each tool is marked `Principiante` (Beginner) or `Intermedio` (Intermediate). If you're just starting out, stick to `Principiante` — that covers 90% of people.
- **Spanish UI?**: if it says "No", the tool works the same but its interface is in English (menu names, buttons). It doesn't affect what it does.
- **Install**: we prefer official stores (App Store, Play, F-Droid, Flathub) or direct installers from the official site. When a tool needs a terminal, that's noted in the column and the level moves up to `Intermedio`.
- You don't need to install everything. 3-4 well-chosen tools per system already cover 80% of everyday risk. The "How to choose" section helps you prioritize.

## Table of contents

- [Android](#android)
- [iPhone / iOS](#iphone--ios)
- [Windows](#windows)
- [macOS](#macos)
- [Linux](#linux)
- [Cross-platform and browser](#cross-platform-and-browser)
- [How to choose](#how-to-choose)
- [What's NOT here and why](#whats-not-here-and-why)
- [How to contribute](#how-to-contribute)
- [Under review](#under-review)
- [License and credits](#license-and-credits)

---

## Android

### Before installing anything: the 3 native settings that matter most

1. **Delete your advertising ID**: `Settings → Security & privacy → Privacy → Ads → Delete advertising ID`.
2. **Pause Google's "Web & App Activity"**: `Settings → Google → Manage your Google Account → Data & privacy → Web & App Activity` → Pause / Auto-delete.
3. **Turn on encrypted private DNS**: `Settings → Network & internet → Private DNS → Private DNS provider hostname` → `dns.adguard-dns.com` or `dns.cloudflare.com`.

> Android has no single "telemetry" switch: the main leak is Google Services plus the manufacturer (Samsung, Xiaomi, etc.). These three settings cover most of it.

#### Trackers

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [TrackerControl](https://trackercontrol.org) | Monitors and blocks app trackers with updated lists and per-app control (local VPN). | F-Droid or GitHub APK | Yes | GPL-3.0 | 2026-08-05 | Beginner |
| [Exodus Privacy](https://exodus-privacy.eu.org) | Analyzes installed apps and shows which trackers and dangerous permissions they use. | F-Droid | Yes | AGPL | 2025-2026 (no exact date) | Beginner |
| [AdAway](https://adaway.org) (non-root mode) | Blocks ads and trackers via hosts (local VPN). | F-Droid | Yes | GPLv3 | 2025-2026 (no exact date) | Beginner |

#### Firewall / DNS

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [RethinkDNS](https://rethinkdns.com) | Per-app firewall + encrypted DNS + malware/tracker blocking (local VPN). | F-Droid | Partial | Apache-2.0 | 2026-08 | Beginner |
| [NetGuard](https://www.netguard.me) | Simple per-app firewall (Wi-Fi/mobile), no root, with optional ad blocking. | F-Droid or Play | Yes | GPL-3.0 | 2026-08-01 (v2.337) | Beginner |
| personalDNSfilter | Local DNS filter using hosts lists to block ads/trackers without root. | F-Droid | Yes | GPL | 2025-2026 (no exact date) | Beginner |
| BlockAds | System-wide ad/tracker blocking + firewall and profiles. | F-Droid | Yes | GPL-3.0 | 2025-2026 (no exact date) | Beginner |
| Private DNS (system) + NextDNS / AdGuard DNS | Android's native encrypted DNS (DoH/DoT) with blocklists. | `Settings → Network & internet → Private DNS` | Yes | Native | Native (built-in) | Beginner |

#### Permissions

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [App Manager](https://muntashirakon.github.io/AppManager) | Manages permissions, components, trackers and app backups (limited non-root mode). | F-Droid | Yes | GPL-3.0 | 2026-06 (v4.1) | Intermediate |
| Shelter / Insular | Creates a work profile to isolate untrusted apps. | F-Droid | Yes | Apache-2.0 | 2025-2026 (no exact date) | Beginner |
| Native permission manager | Granular per-app permission control. | Already in `Settings` | Yes | Native | Native (built-in) | Beginner |

#### Spyware / stalkerware

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [PCAPdroid](https://github.com/emanuele-f/pcapdroid) | Monitors each app's connections and lets you block suspicious behavior. | F-Droid | Yes | GPL | 2025-2026 (no exact date) | Intermediate |
| TrackerControl + Exodus (combined) | Detect and block spyware/stalkerware by analyzing trackers and connections. | F-Droid | Yes | — | 2025-2026 (no exact date) | Beginner |

#### Metadata

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [ExifEraser](https://github.com/Tommy-Geenexus/exif-eraser) | Strips EXIF/metadata from photos (JPEG/PNG/WebP) with no extra permissions. | F-Droid / IzzyOnDroid / GitHub | Yes | MIT | 2026-07 (v6.5.1) | Beginner |
| Scrambled Exif | Removes image metadata when sharing. | F-Droid | Yes | GPL | 2025-2026 (no exact date, v1.8) | Beginner |
| Metadata Remover | Shows and deletes photo metadata before sharing. | F-Droid | Yes | Apache-2.0 | 2024-04 (maintained) | Beginner |
| Secure Camera (GrapheneOS) | Camera that strips EXIF automatically on capture. | Obtainium / GrapheneOS Store | Yes | MIT | 2025-2026 (no exact date) | Beginner |

#### General (store and base)

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Obtainium](https://github.com/ImranR98/Obtainium) | Installs and updates apps straight from GitHub/releases, avoiding tracking-heavy stores. | GitHub APK / F-Droid | Yes | GPL | 2025-2026 (no exact date) | Beginner |
| [Aurora Store](https://auroraoss.com) | Anonymous Play Store client, no Google account needed. | F-Droid | Yes | GPL | 2025-2026 (no exact date) | Beginner |
| [F-Droid](https://f-droid.org) | Catalog of privacy-focused FOSS apps. | Official site | Yes | GPL | 2025-2026 (no exact date) | Beginner |
| [Orbot](https://orbot.app) | System-wide Tor proxy (local VPN). | F-Droid | Yes | BSD | 2025-2026 (no exact date) | Beginner |

[↑ Back to top](#table-of-contents)

---

## iPhone / iOS

### Before installing anything: the 3 native settings that matter most

1. **Turn off cross-app tracking (ATT)**: `Settings → Privacy & Security → Tracking → Allow Apps to Request to Track` → Off.
2. **Turn off Apple Intelligence and cloud data upload**: `Settings → Apple Intelligence & Siri` → disable Apple Intelligence, cloud processing, "Improve Siri and Dictation", suggestions.
3. **Turn off Apple's personalized advertising**: `Settings → Privacy & Security → Apple Advertising → Personalized Ads` → Off.

> There's no free equivalent to a "ShutUp10" on iOS — any app claiming to "disable system telemetry" is marketing. What you can actually do is these native settings plus DNS profiles.

#### Trackers (Safari)

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [AdGuard](https://adguard.com) | Blocks ads and trackers in Safari (free); system-wide via DNS/local VPN in the Pro version. | App Store → enable the blocker in `Settings → Safari` | Yes | Proprietary (parts open-core) | Updated 2026 | Beginner |
| [1Blocker](https://1blocker.com) | Blocks ads, trackers and clutter in Safari with updated filter lists. | App Store → enable in `Settings → Safari → Extensions` | Yes | Proprietary | Aug 2026 | Beginner |
| Wipr / Filtr | Blocks ads in Safari; Filtr (paid add-on) uses iOS 26's URL filters to block inside apps too. | App Store | Partial | Proprietary | 2026 | Beginner |

#### Permissions

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| App Privacy Report + Tracking (native) | App privacy report + deny tracking to all apps at once. | `Settings → Privacy & Security` | Yes | Native Apple | Native (built-in) | Beginner |

#### Spyware

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [iMazing](https://imazing.com) (Spyware Analyzer) | Scans an iPhone backup for indicators of Pegasus, Predator, stalkerware and watchware (free feature). | Download for Mac/Windows → connect the iPhone → "Detect Spyware" | Yes | Proprietary (MVT-based detection) | 2026 | Beginner |

> Deliberately limited category: iOS's sandbox makes it nearly impossible to scan for spyware directly from the iPhone itself. iMazing analyzes the backup from a computer instead.

#### Encrypted DNS / profiles

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [1.1.1.1 (Cloudflare)](https://1.1.1.1) | Encrypted DNS + optional WARP to protect queries and traffic. | App Store → install VPN/DNS profile | Yes | Proprietary | Aug 2026 | Beginner |
| [NextDNS](https://nextdns.io) | Customizable encrypted DNS that blocks ads, trackers and malware system-wide. | App Store → configure profile | Yes | Proprietary (open configuration) | Updated 2026 | Beginner |
| AdGuard DNS | Encrypted DNS with ad/tracker/malware blocking. | App Store (AdGuard or DNS app) | Yes | Proprietary | 2025-2026 | Beginner |
| DNS profiles (Quad9, AdGuard DNS...) | `.mobileconfig` profiles for encrypted DNS (DoH/DoT). | Safari → download profile → `Settings → General → VPN & Device Management` | — | Varies | Ongoing | Beginner |

#### Metadata

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| Metadata Remover / EXIF Eraser / ExifGuard | Removes GPS, EXIF, dates and camera data from photos before sharing (on-device). | App Store (search "Metadata Remover", "EXIF Eraser" or "ExifGuard") | Variable | Proprietary | 2026 | Beginner |

[↑ Back to top](#table-of-contents)

---

## Windows

### Before installing anything: the 3 native settings that matter most

1. **Turn off optional diagnostics**: `Settings → Privacy & security → Diagnostics & feedback` → disable optional data and tailored experiences; hit "Delete diagnostic data".
2. **Turn off Recall if you have a Copilot+ PC**: `Privacy & security → Recall & snapshots → Save snapshots` → Off, then "Delete all".
3. **Delete your advertising ID**: `Privacy & security → General` → turn off advertising ID and suggested content.

#### Telemetry and debloat

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) | Disables telemetry, Copilot, Recall, ads and hundreds of Windows 10/11 privacy options with one click, reversibly. | Download the portable `.exe` and run it | Yes | Freeware | Sep 2026 (v3.5.1130) | Beginner |
| [privacy.sexy](https://privacy.sexy) | Generates and runs transparent, reversible scripts to disable telemetry, bloat, Copilot, Recall and harden privacy. | Web or desktop download, then run the scripts | No | AGPL-3.0 | Mar 2026 (v0.13.8) | Beginner |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) | Lightweight PowerShell script that removes bloatware and disables telemetry, Copilot and Recall. | `irm https://debloat.raphi.re/ \| iex` in PowerShell as admin | No | MIT | Aug 2026 | Beginner |
| [Chris Titus WinUtil](https://github.com/ChrisTitusTech/winutil) | All-in-one GUI utility for debloat, telemetry and optimization. | `irm christitus.com/win \| iex` in PowerShell | No | MIT | 2025-2026 (no exact date) | Beginner |
| [Winhance](https://github.com/memstechtips/Winhance) | App to optimize, customize, debloat and improve privacy on Windows 10/11. | Download the release | No | MIT | 2025-2026 (no exact date) | Beginner |
| [Windows-Privacy-Toolkit](https://github.com/NX1X/Windows-Privacy-Toolkit) | Lightweight PowerShell toolkit to audit and disable telemetry, Recall, Copilot and tracking. | Script via PowerShell | No | MIT | 2025-2026 (no exact date) | Intermediate |
| [Sophia Script for Windows](https://github.com/farag2/Sophia-Script-for-Windows) | Powerful PowerShell module for fine-tuning, debloat and advanced privacy. | Download and run in PowerShell | No | MIT | 2025-2026 (no exact date) | Intermediate |
| [WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker) | Blocks Windows data collection via hosts, firewall and rules. | Download the executable | No | MIT | 2025-2026 (no exact date) | Intermediate |
| [WPD](https://wpd.app/) | Portable dashboard for configuring Windows privacy (telemetry, services, etc.). | Portable `.exe` | No | Freeware | 2025-2026 (no exact date) | Beginner |

#### Trackers

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [uBlock Origin](https://github.com/gorhill/uBlock) | The most effective ad and tracker blocker for browsers. | Extension from the browser's store | Yes | GPL-3.0 | 2025-2026 (no exact date) | Beginner |
| [AdGuard (free)](https://adguard.com) | System- and browser-level ad/tracker blocker (real free version). | Official installer | Yes | Freemium | 2025-2026 (no exact date) | Beginner |

#### Firewall / DNS

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Portmaster](https://safing.io) | Open-source application firewall that monitors and blocks connections, trackers and ads + filtered DNS. | Official installer or `winget` | No | GPL-3.0 | Aug 2026 (v2.2.x) | Beginner |
| [simplewall](https://github.com/henrypp/simplewall) | Lightweight WFP-based firewall controlling which apps can reach the internet. | Portable or installer | Yes (local UI) | GPL-3.0 | 2025/2026 (v3.8.7+) | Intermediate |
| NextDNS / AdGuard DNS / Quad9 / Mullvad DNS | Encrypted DNS (DoH/DoT) with tracker/malware blocking. | Configure in Windows' `Network settings` or their app | Yes (web) | Free | 2025-2026 (no exact date) | Beginner |

#### Permissions

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| Native privacy settings | Review and revoke camera, microphone, location, etc. permissions per app. | `Settings → Privacy & security` | Yes | Native | Native (built-in) | Beginner |

#### Spyware

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| Windows Defender + SmartScreen | Native malware/spyware detection and protection. | Enabled by default; keep it updated | Yes | Native | Native (built-in) | Beginner |
| [Malwarebytes (free)](https://www.malwarebytes.com) | Free malware/spyware/stalkerware scanner. | Official installer | Yes | Freemium | 2025-2026 (no exact date) | Beginner |

#### Metadata

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [ExifCleaner](https://github.com/szTheory/exifcleaner) | GUI app to remove metadata (EXIF, GPS, etc.) from photos, videos and PDFs via drag-and-drop. | Download portable `.exe` or installer | No | MIT | 2025-2026 (no exact date) | Beginner |
| [BleachBit](https://www.bleachbit.org) | Cleans caches, logs, histories and app/system metadata securely. | Installer or portable | Yes | GPL-3.0 | Jul-Sep 2026 (v6.0.x) | Beginner |
| [MetaPurge](https://github.com/XORD-AI/MetaPurge) | Sanitizes EXIF, PDF metadata and timestamps on Windows (portable). | Portable ZIP | No | MIT | 2025-2026 (no exact date) | Beginner |

[↑ Back to top](#table-of-contents)

---

## macOS

### Before installing anything: the 3 native settings that matter most

1. **Turn off analytics and improvements**: `System Settings → Privacy & Security → Analytics & Improvements` → disable everything.
2. **Turn off Apple Intelligence and Siri cloud processing**: `Apple Intelligence & Siri` → disable Apple Intelligence, cloud, "Improve Siri and Dictation" and suggestions.
3. **Turn off Apple's personalized advertising**: `Privacy & Security → Apple Advertising` → personalized ads off.

#### Telemetry

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [privacy.sexy](https://privacy.sexy) | Generates and applies transparent, reversible scripts to disable macOS telemetry, Siri, Apple Intelligence, analytics and bloat. | Web (generates script) or desktop download | No | AGPL-3.0 | 2025-2026 (no exact date) | Beginner |
| System Settings (Apple Intelligence & Siri + Analytics) | Disable Apple Intelligence, Siri, analytics and personalized ads from Settings. | `System Settings → Apple Intelligence & Siri` / `Privacy & Security → Analytics` | Yes | Native | Native (built-in) | Beginner |

#### Firewall / DNS / trackers

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [LuLu](https://objective-see.org/products/lulu.html) | Free outbound-connection firewall that alerts and lets you block any app trying to reach the internet. | DMG from objective-see.org | No | GPL-3.0 | 2026 (v4.x) | Beginner |
| [Cloudflare WARP (1.1.1.1)](https://developers.cloudflare.com/warp-client/) | Encrypts DNS (and optionally all traffic) via 1.1.1.1, with no permanent logs. | Official PKG/DMG | Partial | Free (Cloudflare) | 2025-2026 (no exact date) | Beginner |
| [NextDNS](https://nextdns.io) | Customizable encrypted DNS with tracker, ad and malware blocking. | App or `System Settings → Network → DNS` | Yes (web/app) | Freemium (real free tier) | 2025-2026 (no exact date) | Beginner |
| AdGuard DNS / Home | Encrypted DNS with ad/tracker blocking; usable free tier. | App or DNS configuration | Yes | Freemium | 2025-2026 (no exact date) | Beginner |
| [Radio Silence](https://radiosilenceapp.com) | Blocks apps from reaching the internet in a simple way (blocklist, no constant pop-ups). | Official DMG | No | Low one-time payment (~$9, with trial) | Maintained | Beginner |
| [Little Snitch](https://www.obdev.at/products/littlesnitch) | Advanced outbound firewall with detailed rules and a real-time monitor. | Official DMG | Yes | Commercial | 2025-2026 (no exact date) | Intermediate |

#### Spyware

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [OverSight](https://objective-see.org/products/oversight.html) | Alerts when any process activates the microphone or camera. | ZIP/DMG from objective-see | No | GPL-3.0 | 2024-2026 (v2.4+) | Beginner |
| [KnockKnock](https://objective-see.org/products/knockknock.html) | Scans and shows persistent installed software (LaunchAgents, login items, etc.). | ZIP from objective-see (no install needed) | No | GPL-3.0 | Dec 2025 (v4.0.3) | Beginner |
| [BlockBlock](https://objective-see.org/products/blockblock.html) | Monitors persistence locations and alerts on any new component. | Installer from objective-see | No | GPL-3.0 | 2025-2026 (v2.5) | Beginner |
| [ReiKey](https://objective-see.org/products/reikey.html) | Detects and monitors keyboard "event taps" (keyloggers). | Installer from objective-see | No | GPL-3.0 | 2025-2026 (v1.4) | Intermediate |
| [TaskExplorer](https://objective-see.org/products/taskexplorer.html) | Explores running processes, signatures, libraries and network connections. | From objective-see | No | GPL-3.0 | 2025-2026 (no exact date) | Intermediate |
| [Pareto Security](https://paretosecurity.com) | Automatic audit of basic security hygiene (FileVault, Firewall, Gatekeeper, updates...). | Official DMG | No | GPL-3.0 (free app) | 2026 (v1.35+) | Beginner |

#### Permissions

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| Pareto Security (see spyware) | Besides detection, audits permissions and security configuration. | Official DMG | No | GPL-3.0 | 2026 (v1.35+) | Beginner |

#### Metadata

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [ImageOptim](https://imageoptim.com/mac) | Optimizes images and strips EXIF/GPS/color-profile metadata in bulk via drag-and-drop. | Official DMG or Homebrew | Partial | GPL-2.0 | 2026 (v1.8+) | Beginner |
| [ExifTool](https://exiftool.org) | Command-line tool to read/remove any metadata from photos, PDFs and documents. | `brew install exiftool` | No | Artistic/GPL | 2026 (v13.x) | Intermediate |

#### Erasing traces

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [PureMac](https://github.com/momenbasel/PureMac) | Native open-source cleaner for caches, leftovers and temp data. | DMG/Homebrew | No | MIT | 2026 | Beginner |
| [AppCleaner](https://freemacsoft.net/appcleaner) | Uninstalls apps along with all their leftover files and preferences. | Official DMG | Yes | Free | Maintained | Beginner |
| privacy.sexy (cleanup scripts) | Scripts to erase histories, app caches, logs and usage traces. | Generate and run scripts at privacy.sexy | No | AGPL-3.0 | 2025-2026 (no exact date) | Beginner |

[↑ Back to top](#table-of-contents)

---

## Linux

*Tested on Ubuntu, Linux Mint, Fedora and derivatives.*

### Before installing anything: the 3 native settings that matter most

1. **Disable Firefox telemetry**: `about:config` → `toolkit.telemetry.enabled = false`, `toolkit.telemetry.unified = false`, `datareporting.healthreport.uploadEnabled = false`.
2. **Turn off crash reports (Apport)**: `Settings → Privacy` → disable automatic error report submission.
3. **Set up encrypted DNS (DoH/DoT)** in your distro's network manager, using NextDNS, Mullvad DNS or Quad9.

#### Telemetry

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [privacy.sexy](https://privacy.sexy) | GUI scripts to disable telemetry, reports, bloat and invasive system settings. | AppImage or web version, then run the scripts | No | MIT | 2026 (active AppImage) | Beginner |

#### Firewall / DNS / trackers

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Portmaster](https://safing.io) | Application firewall + tracker/ad blocking + encrypted DNS (DoH/DoT), with per-app control. | Official `.deb`/`.rpm` or one-click script from safing.io | Partial | AGPL-3.0 | 2026 (v2 active) | Beginner |
| [OpenSnitch](https://github.com/evilsocket/opensnitch) | Interactive application firewall that prompts for every outbound connection and blocks trackers. | `.deb`/`.rpm` from releases or repos (`apt`/`dnf`) | No | GPL-3.0 | 2025-12 (v1.8.0) | Intermediate |
| [Gufw](https://gufw.org) | Simple GUI for the UFW firewall. | `sudo apt/dnf install gufw` | Yes | GPL-3.0 | 2025-2026 (no exact date) | Beginner |
| [AdGuard Home](https://adguard.com/adguard-home.html) / [Pi-hole](https://pi-hole.net) | Local DNS sinkhole to block ads/trackers network-wide. | Docker or one-click script | Yes (partial) | GPL | 2026 | Intermediate |
| NextDNS / Mullvad DNS / Quad9 | Encrypted DNS with tracker blocking (configurable in NetworkManager or Portmaster). | Native network settings or Portmaster GUI | Yes | Various | 2026 | Beginner |

#### Permissions

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Flatseal](https://github.com/tchx84/Flatseal) | GUI to review and restrict Flatpak app permissions (network, files, devices...). | `flatpak install flathub com.github.tchx84.Flatseal` | Yes (partial) | GPL-3.0 | 2025-26 | Beginner |
| [Firejail](https://firejail.wordpress.com) | Lightweight sandbox to restrict native apps. | `sudo apt/dnf install firejail` | No | GPL-2.0 | 2025-26 | Intermediate |
| AppArmor / SELinux | Mandatory access control systems already included (SELinux on Fedora, AppArmor on Ubuntu/Mint). | Already installed | — | GPL | Native (built-in) | Intermediate |

#### Metadata

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Metadata Cleaner](https://flathub.org/apps/fr.romainvigier.MetadataCleaner) | MAT2-based interface to view and remove metadata from photos, documents, audio and video. | `flatpak install flathub fr.romainvigier.MetadataCleaner` | Yes | GPL-3.0 | 2025-26 | Beginner |
| [MAT2](https://0xacab.org/jvoisin/mat2) | Command-line tool (with file-manager integration) to remove metadata. | `sudo apt/dnf install mat2` or `pip` | No | LGPL-3.0 | 2025-26 (PyPI 0.15) | Intermediate |

#### Erasing traces / encryption

| Tool | What it does | Install | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [BleachBit](https://www.bleachbit.org) | Cleans caches, cookies, histories, temp files and app traces; includes secure deletion. | Official `.deb`/`.rpm` or repos | Yes | GPL-3.0 | 2026 (v6.0) | Beginner |
| secure-delete / srm (package) | Command-line tools for securely wiping files and free space. | `sudo apt/dnf install secure-delete` | No | GPL | 2025-2026 (no exact date) | Intermediate |
| [OnionShare](https://onionshare.org) | Shares files anonymously over Tor, with no server-side trace. | Flatpak Flathub or `pip` | Yes | GPL-3.0 | 2026 | Intermediate |
| [Cryptomator](https://cryptomator.org) | Encrypts local or cloud folders. | Flatpak Flathub or AppImage | Yes | GPL-3.0 | 2026 | Beginner |
| [VeraCrypt](https://www.veracrypt.fr) / LUKS (native) | Encrypted containers and volumes (LUKS ships out of the box on most distro installers). | Flatpak/AppImage VeraCrypt or your distro's installer (LUKS) | Yes | Apache-2.0 / GPL | 2026 / native | Intermediate |
| [Syncthing](https://syncthing.net) | Syncs files between your own devices without a central cloud. | Flatpak or repos | Yes | MPL-2.0 | 2026 | Beginner |

[↑ Back to top](#table-of-contents)

---

## Cross-platform and browser

Tools that aren't tied to one system — they work the same (or almost) across several of the systems above. Install them from the store or site that matches your system.

#### Browser

| Tool | What it does | Available on | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Tor Browser](https://www.torproject.org) | Firefox-based browser that routes traffic through the Tor network for real anonymity. | Android, Windows, macOS, Linux (on iPhone: Onion Browser) | Yes | MPL | 2025-2026 (no exact date) | Beginner |
| [Brave](https://brave.com) | Chromium-based browser with ad/tracker blocking on by default. | Android, iPhone, Windows, macOS, Linux | Yes | MPL | 2025-2026 (no exact date) | Beginner |
| [LibreWolf](https://librewolf.net) | Hardened Firefox fork: no telemetry by default, with anti-fingerprinting. | Windows, macOS, Linux | Yes | MPL-2.0 | 2025-2026 (no exact date) | Beginner |
| [Mullvad Browser](https://mullvad.net/browser) | Based on Tor Browser but without the Tor network; meant to be used alongside a VPN. | Windows, macOS, Linux | No | MPL | 2025-2026 (no exact date) | Beginner |
| [Firefox](https://www.mozilla.org/firefox) (configured with strict ETP) | Browser with strict Enhanced Tracking Protection + support for extensions like uBlock Origin. | Android, iPhone, Windows, macOS, Linux | Yes | MPL | 2025-2026 (no exact date) | Beginner |
| [uBlock Origin](https://github.com/gorhill/uBlock) | The most effective ad and tracker blocker, as a browser extension. | Firefox/Chrome/Edge/Brave on any system | Yes | GPL-3.0 | 2025-2026 (no exact date) | Beginner |

#### Messaging

| Tool | What it does | Available on | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Signal](https://signal.org) | End-to-end encrypted messaging and calls (Signal protocol). | Android, iPhone, Windows, macOS, Linux | Yes | AGPL/GPL | 2025-2026 (no exact date) | Beginner |
| [SimpleX Chat](https://simplex.chat) | Decentralized messaging with no identifiers (no phone number or username). | Android, iPhone, Windows, macOS, Linux | Yes | AGPL | 2025-2026 (no exact date) | Beginner |
| [Session](https://getsession.org) | Decentralized, private messaging with no phone number. | Android, iPhone, Windows, macOS, Linux | Yes | GPL | 2025-2026 (no exact date) | Beginner |
| [Element](https://element.io) (Matrix) | Matrix client for encrypted, federated chats. | Android, Windows, macOS, Linux | Yes | Apache-2.0 | 2025-2026 (no exact date) | Intermediate |
| [Molly](https://molly.im) | Hardened Signal fork (local encryption, RAM wipe, optional Tor, no Google). | Android | Yes | AGPL | 2025-2026 (no exact date) | Intermediate |
| [Briar](https://briarproject.org) | P2P messaging that works even offline (Tor/Bluetooth). | Android | Yes | GPL | 2025-2026 (no exact date) | Intermediate |

#### Passwords and 2FA

| Tool | What it does | Available on | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [Bitwarden](https://bitwarden.com) | Open-source password manager with autofill, generator and sync (real freemium). | Android, iPhone, Windows, macOS, Linux | Yes | GPL | 2026-08/09 | Beginner |
| KeePass (KeePassXC on desktop, KeePassDX on Android, KeePassium on iPhone) | Offline password manager with a local encrypted database (`.kdbx`). | Android, iPhone, Windows, macOS, Linux | Yes | GPL-3.0 | 2026 | Beginner |
| [Proton Pass](https://proton.me/pass) | End-to-end encrypted password manager with built-in email aliases. | Android, iPhone, Windows, macOS, Linux | Yes | Open-source (partial) | 2025-2026 (no exact date) | Beginner |
| [Aegis](https://getaegis.app) (Android) / [2FAS Auth](https://2fas.com) / [Ente Auth](https://ente.io/auth) | Open-source, encrypted, exportable 2FA (TOTP) apps. | Android, iPhone, Windows, macOS, Linux (varies by app) | Yes | GPL/AGPL | 2026-02 (Aegis v3.4.2) | Beginner |

#### Email and aliasing

| Tool | What it does | Available on | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [SimpleLogin](https://simplelogin.io) | Creates email aliases that forward to your real inbox, shielding you from spam and tracking. | Web + extension, Android/iPhone apps | Yes | AGPL | 2025-2026 (no exact date) | Beginner |
| [addy.io](https://addy.io) (AnonAddy) | Open-source email aliasing with a generous free plan and PGP support. | Web + extension, Android/iPhone apps | Yes | AGPL | 2025-2026 (no exact date) | Beginner |
| [Proton Mail](https://proton.me/mail) / [Tuta](https://tuta.com) | End-to-end encrypted email with aliases, real free plan. | Web, Android, iPhone, Windows, macOS, Linux | Yes | Open-source (clients) | 2025-2026 (no exact date) | Beginner |
| [Thunderbird](https://www.thunderbird.net) | Open-source email client with OpenPGP support. | Windows, macOS, Linux | Yes | MPL-2.0 | 2025-2026 (no exact date) | Beginner |

#### Erasing traces

| Tool | What it does | Available on | Spanish UI? | License | Last updated | Level |
|---|---|---|---|---|---|---|
| [BleachBit](https://www.bleachbit.org) | Cleans caches, cookies, histories, temp files and app traces; includes secure deletion. | Windows, Linux (macOS: see native alternatives in the macOS section) | Yes | GPL-3.0 | 2026 (v6.0) | Beginner |

[↑ Back to top](#table-of-contents)

---

## How to choose

You don't need to install the whole list. Practical rules:

1. **On Android**, use only one local VPN at a time (TrackerControl, RethinkDNS and NetGuard all compete for the same system VPN "slot" — pick one).
2. **On iPhone**, most of the work is native settings, not apps. Start with the 3 settings above before installing anything.
3. **On Windows**, start with either O&O ShutUp10++ or privacy.sexy (pick one, not both at once) and add an application firewall (Portmaster or simplewall) afterward.
4. **On macOS**, turn on FileVault + the native (inbound) Firewall and add LuLu (outbound) — that covers most everyday risk.
5. **On any system**, a password manager (Bitwarden or KeePass) + 2FA (Aegis/2FAS/Ente Auth) do more for your security than anything else on this list. Start there if you're only going to do one thing.

[↑ Back to top](#table-of-contents)

## What's NOT here and why

This repository deliberately stays short on some topics because they're not for "regular people" or fall outside the entry criteria (see [CONTRIBUTING.md](CONTRIBUTING.md)):

- **Pentesting and offensive hacking**: vulnerability scanners, exploitation frameworks, WiFi attack tools, phishing kits, C2 frameworks. These attack other people's systems, not protect your own.
- **Offensive OSINT on third parties**: people-search engines, scrapers for other people's social media, tools for tracking other people's phones or accounts.
- **Exploits and 0-days**: completely out of scope; this repo protects devices, it doesn't compromise them.
- **Tails, Qubes OS, Whonix**: full operating systems designed for a high threat model (at-risk activism, journalism in repressive countries). Excellent tools, but not something you can "install today with no background" on your current system — they require learning a different workflow entirely. If your threat model needs them, start at [privacyguides.org](https://www.privacyguides.org).
- **Crypto/blockchain**: wallets, mixers, exchanges. Not the focus of this repository.
- **Root/jailbreak**: any tool that requires breaking the manufacturer's protections is out of scope; the risk for a non-technical user outweighs the benefit.

[↑ Back to top](#table-of-contents)

## How to contribute

Know a tool that's missing, or one that's no longer maintained? Read [CONTRIBUTING.md](CONTRIBUTING.md) and open an issue or pull request.

Entry criteria, summarized:
1. No root, no jailbreak, no compiling.
2. Maintained (activity within the last 12 months).
3. Free, or with a real, usable free tier.
4. Protects your own device — no pentesting, offensive OSINT, exploits, or hacking other people's networks/accounts.

[↑ Back to top](#table-of-contents)

## Under review

Tools that once met the entry criteria but whose GitHub repository has shown no activity for over 12 months, as detected by `scripts/check.py`. They aren't deleted outright — they're moved here with the date of the last check, and reviewed before every update.

*(`scripts/check.py` fills this section in automatically on every run; see the verification report for each release. Empty at initial launch: every tool in the list passed the check on the publication date — see the initial commit.)*

[↑ Back to top](#table-of-contents)

---

## 📘 Want the full method, not just the tools?

This repository gets updated, but **the Anonimato Platino manual** explains the why behind every setting and the order to do them in, step by step.

👉 [ALEXIS: landing page URL]

## License and credits

This project is published under the [CC-BY-SA-4.0](LICENSE) license: you can copy, adapt and redistribute this list, even commercially, as long as you credit the source and share it under the same license.

Sources and projects used as a reference for the curation criteria:

- [privacyguides.org](https://www.privacyguides.org)
- [awesome-privacy](https://github.com/pluja/awesome-privacy)
- [F-Droid](https://f-droid.org)

Thanks also to the maintainers of every tool listed here — this repository wouldn't be possible without their work.

[↑ Back to top](#table-of-contents)
