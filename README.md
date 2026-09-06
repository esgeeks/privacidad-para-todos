# Privacidad para todos · el repositorio de Anonimato Platino (EsGeeks)

Español · [English](README.en.md)

Herramientas de privacidad y anonimato para gente normal, organizadas por sistema: Android, iPhone, Windows, Mac y Linux. Sin root, sin jerga técnica, y con criterio: solo herramientas mantenidas y gratuitas (o con versión gratuita real) que protegen tu propio dispositivo.

Está pensada para alguien sin conocimientos técnicos que quiere dejar de regalar sus datos sin tener que aprender a programar ni tocar la terminal (salvo que quiera).

## 📘 Este repositorio es el bono del manual «Anonimato Platino»

Este repo es el complemento vivo del manual **Anonimato Platino**: el manual te enseña el método (qué ajustar, en qué orden, por qué importa cada paso) y este repositorio lleva la lista de herramientas, que cambia cada pocos meses. Así no te quedas con una guía desactualizada en un PDF fijo.

👉 [ALEXIS: URL de la landing]

## Cómo usar esta lista

- **Nivel**: cada herramienta está marcada como `Principiante` o `Intermedio`. Si vas empezando, quédate en `Principiante` — es suficiente para el 90% de la gente.
- **¿En español?**: si dice "No", la herramienta funciona igual pero su interfaz está en inglés (nombres de menú, botones). No afecta lo que hace.
- **Cómo se instala**: preferimos tiendas oficiales (App Store, Play, F-Droid, Flathub) o instaladores directos del sitio oficial. Cuando una herramienta requiere terminal, se avisa en la columna y el nivel sube a `Intermedio`.
- No necesitas instalar todo. Con 3-4 herramientas bien elegidas por sistema ya cubres el 80% del riesgo cotidiano. La sección "Cómo elegir" te ayuda a priorizar.

## Índice

- [Android](#android)
- [iPhone / iOS](#iphone--ios)
- [Windows](#windows)
- [macOS](#macos)
- [Linux](#linux)
- [Multiplataforma y navegador](#multiplataforma-y-navegador)
- [Cómo elegir](#cómo-elegir)
- [Qué NO está aquí y por qué](#qué-no-está-aquí-y-por-qué)
- [Cómo contribuir](#cómo-contribuir)
- [En observación](#en-observación)
- [Licencia y créditos](#licencia-y-créditos)

---

## Android

### Antes de instalar nada: los 3 ajustes nativos que más importan

1. **Elimina el ID de publicidad**: `Ajustes → Seguridad y privacidad → Privacidad → Anuncios → Eliminar ID de publicidad`.
2. **Pausa "Actividad en la web y en las apps" de Google**: `Ajustes → Google → Gestionar tu cuenta → Datos y privacidad → Actividad en la web y en las apps` → Pausar / Auto-eliminar.
3. **Activa DNS privado cifrado**: `Ajustes → Red e internet → DNS privado → Nombre de host` → `dns.adguard-dns.com` o `dns.cloudflare.com`.

> En Android no existe un interruptor único de "telemetría": la fuga principal es Google Services + el fabricante (Samsung, Xiaomi, etc.). Estos tres ajustes cubren la mayor parte.

#### Rastreadores

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [TrackerControl](https://trackercontrol.org) | Monitoriza y bloquea trackers de apps con listas actualizadas y control por app (VPN local). | F-Droid o GitHub APK | Sí | GPL-3.0 | 2026-08-05 | Principiante |
| [Exodus Privacy](https://exodus-privacy.eu.org) | Analiza las apps instaladas y muestra qué trackers y permisos peligrosos usan. | F-Droid | Sí | AGPL | 2025-2026 (sin fecha exacta) | Principiante |
| [AdAway](https://adaway.org) (modo no-root) | Bloquea anuncios y trackers vía hosts (VPN local). | F-Droid | Sí | GPLv3 | 2025-2026 (sin fecha exacta) | Principiante |

#### Firewall / DNS

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [RethinkDNS](https://rethinkdns.com) | Firewall por app + DNS cifrado + bloqueo de malware/trackers (VPN local). | F-Droid | Parcial | Apache-2.0 | 2026-08 | Principiante |
| [NetGuard](https://www.netguard.me) | Firewall simple por app (Wi-Fi/móvil), sin root, con bloqueo de anuncios opcional. | F-Droid o Play | Sí | GPL-3.0 | 2026-08-01 (v2.337) | Principiante |
| personalDNSfilter | Filtro DNS local con listas de hosts para bloquear ads/trackers sin root. | F-Droid | Sí | GPL | 2025-2026 (sin fecha exacta) | Principiante |
| BlockAds | Bloqueo de ads/trackers en todo el sistema + firewall y perfiles. | F-Droid | Sí | GPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |
| DNS privado (sistema) + NextDNS / AdGuard DNS | DNS cifrado nativo de Android (DoH/DoT) con listas de bloqueo. | `Ajustes → Red e internet → DNS privado` | Sí | Nativo | Nativo (integrado) | Principiante |

#### Permisos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [App Manager](https://muntashirakon.github.io/AppManager) | Gestiona permisos, componentes, trackers y backup de apps (modo no-root limitado). | F-Droid | Sí | GPL-3.0 | 2026-06 (v4.1) | Intermedio |
| Shelter / Insular | Crea un perfil de trabajo para aislar apps no confiables. | F-Droid | Sí | Apache-2.0 | 2025-2026 (sin fecha exacta) | Principiante |
| Gestor de permisos nativo | Control granular de permisos por app. | Ya viene en `Ajustes` | Sí | Nativo | Nativo (integrado) | Principiante |

#### Spyware / stalkerware

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [PCAPdroid](https://github.com/emanuele-f/pcapdroid) | Monitoriza las conexiones de cada app y permite bloquear comportamiento sospechoso. | F-Droid | Sí | GPL | 2025-2026 (sin fecha exacta) | Intermedio |
| TrackerControl + Exodus (combinados) | Detectan y bloquean spyware/stalkerware analizando trackers y conexiones. | F-Droid | Sí | — | 2025-2026 (sin fecha exacta) | Principiante |

#### Metadatos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [ExifEraser](https://github.com/Tommy-Geenexus/exif-eraser) | Elimina EXIF/metadatos de fotos (JPEG/PNG/WebP) sin permisos extra. | F-Droid / IzzyOnDroid / GitHub | Sí | MIT | 2026-07 (v6.5.1) | Principiante |
| Scrambled Exif | Quita metadatos de imágenes al compartirlas. | F-Droid | Sí | GPL | 2025-2026 (sin fecha exacta, v1.8) | Principiante |
| Metadata Remover | Muestra y borra metadatos de fotos antes de compartir. | F-Droid | Sí | Apache-2.0 | 2024-04 (mantenida) | Principiante |
| Secure Camera (GrapheneOS) | Cámara que elimina EXIF automáticamente al disparar. | Obtainium / GrapheneOS Store | Sí | MIT | 2025-2026 (sin fecha exacta) | Principiante |

#### General (tienda y base)

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Obtainium](https://github.com/ImranR98/Obtainium) | Instala y actualiza apps directo desde GitHub/releases, evitando tiendas con tracking. | GitHub APK / F-Droid | Sí | GPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Aurora Store](https://auroraoss.com) | Cliente de Play Store anónimo, sin cuenta de Google. | F-Droid | Sí | GPL | 2025-2026 (sin fecha exacta) | Principiante |
| [F-Droid](https://f-droid.org) | Catálogo de apps FOSS orientadas a privacidad. | Sitio oficial | Sí | GPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Orbot](https://orbot.app) | Proxy Tor para todo el sistema (VPN local). | F-Droid | Sí | BSD | 2025-2026 (sin fecha exacta) | Principiante |

[↑ Volver al índice](#índice)

---

## iPhone / iOS

### Antes de instalar nada: los 3 ajustes nativos que más importan

1. **Desactiva el rastreo entre apps (ATT)**: `Ajustes → Privacidad y seguridad → Rastreo → Permitir que las apps soliciten seguimiento` → Desactivar.
2. **Apaga Apple Intelligence y el envío de datos a la nube**: `Ajustes → Apple Intelligence y Siri` → desactivar Apple Intelligence, procesamiento en la nube, "Mejorar Siri y Dictado", sugerencias.
3. **Desactiva la publicidad personalizada de Apple**: `Ajustes → Privacidad y seguridad → Publicidad de Apple → Anuncios personalizados` → Desactivar.

> En iOS no hay equivalente gratuito a un "ShutUp10" — cualquier app que diga "desactiva la telemetría del sistema" es marketing. Lo que sí puedes hacer son estos ajustes nativos y usar perfiles DNS.

#### Rastreadores (Safari)

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [AdGuard](https://adguard.com) | Bloquea anuncios y rastreadores en Safari (gratis); a nivel sistema vía DNS/VPN local en la versión Pro. | App Store → activa el bloqueador en `Ajustes → Safari` | Sí | Propietaria (núcleo abierto en partes) | Actualizado 2026 | Principiante |
| [1Blocker](https://1blocker.com) | Bloquea anuncios, rastreadores y elementos molestos en Safari con listas actualizadas. | App Store → activa en `Ajustes → Safari → Extensiones` | Sí | Propietaria | Ago 2026 | Principiante |
| Wipr / Filtr | Bloquea anuncios en Safari; Filtr (pago extra) usa los filtros de URL de iOS 26 para bloquear dentro de apps. | App Store | Parcial | Propietaria | 2026 | Principiante |

#### Permisos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| App Privacy Report + Rastreo (nativo) | Informe de privacidad de apps + denegar el rastreo a todas las apps de golpe. | `Ajustes → Privacidad y seguridad` | Sí | Nativo Apple | Nativo (integrado) | Principiante |

#### Spyware

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [iMazing](https://imazing.com) (Spyware Analyzer) | Escanea el backup del iPhone en busca de indicadores de Pegasus, Predator, stalkerware y watchware (función gratis). | Descarga para Mac/Windows → conecta el iPhone → "Detect Spyware" | Sí | Propietaria (detección basada en MVT) | 2026 | Principiante |

> Categoría limitada por diseño: el sandbox de iOS hace casi imposible escanear spyware directamente desde el propio iPhone. iMazing analiza el backup desde un ordenador.

#### DNS cifrado / perfiles

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [1.1.1.1 (Cloudflare)](https://1.1.1.1) | DNS cifrado + WARP opcional para proteger consultas y tráfico. | App Store → instala perfil VPN/DNS | Sí | Propietaria | Ago 2026 | Principiante |
| [NextDNS](https://nextdns.io) | DNS cifrado personalizable que bloquea anuncios, rastreadores y malware a nivel sistema. | App Store → configura perfil | Sí | Propietaria (configuración abierta) | Actualizado 2026 | Principiante |
| AdGuard DNS | DNS cifrado con bloqueo de anuncios/rastreadores/malware. | App Store (AdGuard o app DNS) | Sí | Propietaria | 2025-2026 | Principiante |
| Perfiles DNS (Quad9, AdGuard DNS...) | Perfiles `.mobileconfig` para DNS cifrado (DoH/DoT). | Safari → descarga perfil → `Ajustes → General → VPN y gestión de dispositivos` | — | Varía | Continuo | Principiante |

#### Metadatos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| Metadata Remover / EXIF Eraser / ExifGuard | Elimina GPS, EXIF, fechas y datos de cámara de fotos antes de compartirlas (on-device). | App Store (busca "Metadata Remover", "EXIF Eraser" o "ExifGuard") | Variable | Propietaria | 2026 | Principiante |

[↑ Volver al índice](#índice)

---

## Windows

### Antes de instalar nada: los 3 ajustes nativos que más importan

1. **Desactiva diagnósticos opcionales**: `Configuración → Privacidad y seguridad → Diagnósticos y comentarios` → desactivar datos opcionales y experiencias personalizadas; pulsa "Eliminar datos de diagnóstico".
2. **Apaga Recall si tienes un PC Copilot+**: `Privacidad y seguridad → Recall e instantáneas → Guardar instantáneas` → Desactivar y "Eliminar todas".
3. **Elimina el ID de publicidad**: `Privacidad y seguridad → General` → desactivar ID de publicidad y contenido sugerido.

#### Telemetría y debloat

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [O&O ShutUp10++](https://www.oo-software.com/en/shutup10) | Desactiva telemetría, Copilot, Recall, anuncios y cientos de opciones de privacidad de Windows 10/11 con un clic, de forma reversible. | Descarga el `.exe` portable y ejecútalo | Sí | Freeware | Sep 2026 (v3.5.1130) | Principiante |
| [privacy.sexy](https://privacy.sexy) | Genera y ejecuta scripts transparentes y reversibles para desactivar telemetría, bloat, Copilot, Recall y endurecer la privacidad. | Web o descarga de escritorio y ejecuta scripts | No | AGPL-3.0 | Mar 2026 (v0.13.8) | Principiante |
| [Win11Debloat](https://github.com/Raphire/Win11Debloat) | Script de PowerShell ligero que elimina bloatware y desactiva telemetría, Copilot y Recall. | `irm https://debloat.raphi.re/ \| iex` en PowerShell como admin | No | MIT | Ago 2026 | Principiante |
| [Chris Titus WinUtil](https://github.com/ChrisTitusTech/winutil) | Utilidad todo-en-uno con interfaz gráfica para debloat, telemetría y optimización. | `irm christitus.com/win \| iex` en PowerShell | No | MIT | 2025-2026 (sin fecha exacta) | Principiante |
| [Winhance](https://github.com/memstechtips/Winhance) | App para optimizar, personalizar, debloatear y mejorar la privacidad en Windows 10/11. | Descarga el release | No | MIT | 2025-2026 (sin fecha exacta) | Principiante |
| [Windows-Privacy-Toolkit](https://github.com/NX1X/Windows-Privacy-Toolkit) | Toolkit de PowerShell ligero para auditar y desactivar telemetría, Recall, Copilot y tracking. | Script vía PowerShell | No | MIT | 2025-2026 (sin fecha exacta) | Intermedio |
| [Sophia Script for Windows](https://github.com/farag2/Sophia-Script-for-Windows) | Módulo de PowerShell potente para ajuste fino, debloat y privacidad avanzada. | Descarga y ejecuta en PowerShell | No | MIT | 2025-2026 (sin fecha exacta) | Intermedio |
| [WindowsSpyBlocker](https://github.com/crazy-max/WindowsSpyBlocker) | Bloquea el envío de datos de Windows mediante hosts, firewall y reglas. | Descarga el ejecutable | No | MIT | 2025-2026 (sin fecha exacta) | Intermedio |
| [WPD](https://wpd.app/) | Dashboard portátil para configurar la privacidad de Windows (telemetría, servicios, etc.). | `.exe` portable | No | Freeware | 2025-2026 (sin fecha exacta) | Principiante |

#### Rastreadores

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [uBlock Origin](https://github.com/gorhill/uBlock) | El bloqueador de anuncios y trackers más efectivo para navegadores. | Extensión desde la tienda del navegador | Sí | GPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |
| [AdGuard (free)](https://adguard.com) | Bloqueador de anuncios/trackers a nivel sistema y navegador (versión gratuita real). | Instalador oficial | Sí | Freemium | 2025-2026 (sin fecha exacta) | Principiante |

#### Firewall / DNS

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Portmaster](https://safing.io) | Firewall de aplicaciones open-source que monitoriza y bloquea conexiones, trackers y anuncios + DNS filtrado. | Instalador oficial o `winget` | No | GPL-3.0 | Ago 2026 (v2.2.x) | Principiante |
| [simplewall](https://github.com/henrypp/simplewall) | Firewall ligero basado en WFP que controla qué apps pueden salir a internet. | Portable o instalador | Sí (interfaz local) | GPL-3.0 | 2025/2026 (v3.8.7+) | Intermedio |
| NextDNS / AdGuard DNS / Quad9 / Mullvad DNS | DNS cifrado (DoH/DoT) con bloqueo de trackers/malware. | Configúralo en `Ajustes de red` de Windows o su app | Sí (web) | Gratis | 2025-2026 (sin fecha exacta) | Principiante |

#### Permisos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| Configuración de privacidad nativa | Revisa y revoca permisos de cámara, micrófono, ubicación, etc. por app. | `Configuración → Privacidad y seguridad` | Sí | Nativo | Nativo (integrado) | Principiante |

#### Spyware

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| Windows Defender + SmartScreen | Detección y protección nativa contra malware/spyware. | Activado por defecto; mantenlo actualizado | Sí | Nativo | Nativo (integrado) | Principiante |
| [Malwarebytes (free)](https://www.malwarebytes.com) | Escáner gratuito de malware/spyware/stalkerware. | Instalador oficial | Sí | Freemium | 2025-2026 (sin fecha exacta) | Principiante |

#### Metadatos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [ExifCleaner](https://github.com/szTheory/exifcleaner) | App gráfica para eliminar metadatos (EXIF, GPS, etc.) de fotos, vídeos y PDFs con arrastrar y soltar. | Descarga `.exe` portable o instalador | No | MIT | 2025-2026 (sin fecha exacta) | Principiante |
| [BleachBit](https://www.bleachbit.org) | Limpia cachés, logs, historiales y metadatos de apps/sistema de forma segura. | Instalador o portable | Sí | GPL-3.0 | Jul-Sep 2026 (v6.0.x) | Principiante |
| [MetaPurge](https://github.com/XORD-AI/MetaPurge) | Sanitiza EXIF, metadatos de PDF y timestamps en Windows (portable). | ZIP portable | No | MIT | 2025-2026 (sin fecha exacta) | Principiante |

[↑ Volver al índice](#índice)

---

## macOS

### Antes de instalar nada: los 3 ajustes nativos que más importan

1. **Desactiva analíticas y mejoras**: `Ajustes del Sistema → Privacidad y seguridad → Analíticas y mejoras` → desactiva todo.
2. **Apaga Apple Intelligence y Siri en la nube**: `Apple Intelligence y Siri` → desactivar Apple Intelligence, nube, "Mejorar Siri y Dictado" y sugerencias.
3. **Desactiva la publicidad personalizada de Apple**: `Privacidad y seguridad → Publicidad de Apple` → anuncios personalizados desactivados.

#### Telemetría

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [privacy.sexy](https://privacy.sexy) | Genera y aplica scripts transparentes y reversibles para desactivar telemetría de macOS, Siri, Apple Intelligence, analíticas y bloat. | Web (genera script) o descarga de escritorio | No | AGPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |
| Ajustes del sistema (Apple Intelligence & Siri + Analíticas) | Desactiva Apple Intelligence, Siri, analíticas y anuncios personalizados desde Ajustes. | `System Settings → Apple Intelligence & Siri` / `Privacy & Security → Analytics` | Sí | Nativo | Nativo (integrado) | Principiante |

#### Firewall / DNS / rastreadores

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [LuLu](https://objective-see.org/products/lulu.html) | Firewall de conexiones salientes gratuito que alerta y permite bloquear cualquier app que intente conectar a internet. | DMG desde objective-see.org | No | GPL-3.0 | 2026 (v4.x) | Principiante |
| [Cloudflare WARP (1.1.1.1)](https://developers.cloudflare.com/warp-client/) | Cifra el DNS (y opcionalmente todo el tráfico) con 1.1.1.1, sin logs permanentes. | PKG/DMG oficial | Parcial | Gratuita (Cloudflare) | 2025-2026 (sin fecha exacta) | Principiante |
| [NextDNS](https://nextdns.io) | DNS cifrado personalizable con bloqueo de trackers, anuncios y malware. | App o `System Settings → Network → DNS` | Sí (web/app) | Freemium (gratis real) | 2025-2026 (sin fecha exacta) | Principiante |
| AdGuard DNS / Home | DNS cifrado con bloqueo de anuncios/trackers; versión gratuita usable. | App o configuración DNS | Sí | Freemium | 2025-2026 (sin fecha exacta) | Principiante |
| [Radio Silence](https://radiosilenceapp.com) | Bloquea apps de internet de forma simple (lista negra, sin pop-ups constantes). | DMG oficial | No | Pago único bajo (~$9, con prueba) | Mantenida | Principiante |
| [Little Snitch](https://www.obdev.at/products/littlesnitch) | Firewall avanzado de conexiones salientes con reglas detalladas y monitor en tiempo real. | DMG oficial | Sí | Comercial | 2025-2026 (sin fecha exacta) | Intermedio |

#### Spyware

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [OverSight](https://objective-see.org/products/oversight.html) | Alerta cuando cualquier proceso activa el micrófono o la cámara. | ZIP/DMG desde objective-see | No | GPL-3.0 | 2024-2026 (v2.4+) | Principiante |
| [KnockKnock](https://objective-see.org/products/knockknock.html) | Escanea y muestra software persistente instalado (LaunchAgents, login items, etc.). | ZIP desde objective-see (sin instalación) | No | GPL-3.0 | Dic 2025 (v4.0.3) | Principiante |
| [BlockBlock](https://objective-see.org/products/blockblock.html) | Monitorea ubicaciones de persistencia y alerta ante cualquier componente nuevo. | Instalador desde objective-see | No | GPL-3.0 | 2025-2026 (v2.5) | Principiante |
| [ReiKey](https://objective-see.org/products/reikey.html) | Detecta y monitorea "event taps" de teclado (keyloggers). | Instalador desde objective-see | No | GPL-3.0 | 2025-2026 (v1.4) | Intermedio |
| [TaskExplorer](https://objective-see.org/products/taskexplorer.html) | Explora procesos en ejecución, firmas, librerías y conexiones de red. | Desde objective-see | No | GPL-3.0 | 2025-2026 (sin fecha exacta) | Intermedio |
| [Pareto Security](https://paretosecurity.com) | Auditoría automática de higiene de seguridad básica (FileVault, Firewall, Gatekeeper, actualizaciones...). | DMG oficial | No | GPL-3.0 (app gratuita) | 2026 (v1.35+) | Principiante |

#### Permisos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| Pareto Security (ver spyware) | Además de detección, audita permisos y configuración de seguridad. | DMG oficial | No | GPL-3.0 | 2026 (v1.35+) | Principiante |

#### Metadatos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [ImageOptim](https://imageoptim.com/mac) | Optimiza imágenes y elimina metadatos EXIF/GPS/perfiles de color en lote, arrastrando y soltando. | DMG oficial o Homebrew | Parcial | GPL-2.0 | 2026 (v1.8+) | Principiante |
| [ExifTool](https://exiftool.org) | Herramienta de línea de comandos para leer/eliminar cualquier metadato de fotos, PDFs y documentos. | `brew install exiftool` | No | Artistic/GPL | 2026 (v13.x) | Intermedio |

#### Borrar rastro

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [PureMac](https://github.com/momenbasel/PureMac) | Limpiador nativo open-source de cachés, residuos y datos temporales. | DMG/Homebrew | No | MIT | 2026 | Principiante |
| [AppCleaner](https://freemacsoft.net/appcleaner) | Desinstala apps eliminando todos sus residuos y preferencias. | DMG oficial | Sí | Gratuita | Mantenida | Principiante |
| privacy.sexy (scripts de limpieza) | Scripts para borrar historiales, cachés de apps, logs y rastros de uso. | Genera y ejecuta scripts en privacy.sexy | No | AGPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |

[↑ Volver al índice](#índice)

---

## Linux

*Probado en Ubuntu, Linux Mint, Fedora y derivadas.*

### Antes de instalar nada: los 3 ajustes nativos que más importan

1. **Desactiva la telemetría de Firefox**: `about:config` → `toolkit.telemetry.enabled = false`, `toolkit.telemetry.unified = false`, `datareporting.healthreport.uploadEnabled = false`.
2. **Apaga los informes de fallos (Apport)**: `Ajustes → Privacidad` → desactiva el envío automático de informes de errores.
3. **Configura DNS cifrado (DoH/DoT)** en el gestor de red de tu distro, con NextDNS, Mullvad DNS o Quad9.

#### Telemetría

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [privacy.sexy](https://privacy.sexy) | Scripts con interfaz gráfica para desactivar telemetría, informes, bloat y configuraciones invasivas del sistema. | AppImage o versión web + ejecuta los scripts | No | MIT | 2026 (AppImage activo) | Principiante |

#### Firewall / DNS / rastreadores

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Portmaster](https://safing.io) | Firewall de aplicaciones + bloqueo de trackers/anuncios + DNS cifrado (DoH/DoT), con control por app. | `.deb`/`.rpm` oficial o script de un clic desde safing.io | Parcial | AGPL-3.0 | 2026 (v2 activo) | Principiante |
| [OpenSnitch](https://github.com/evilsocket/opensnitch) | Firewall interactivo de aplicaciones que pregunta por cada conexión saliente y bloquea trackers. | `.deb`/`.rpm` desde releases o repos (`apt`/`dnf`) | No | GPL-3.0 | 2025-12 (v1.8.0) | Intermedio |
| [Gufw](https://gufw.org) | Interfaz gráfica simple para el firewall UFW. | `sudo apt/dnf install gufw` | Sí | GPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |
| [AdGuard Home](https://adguard.com/adguard-home.html) / [Pi-hole](https://pi-hole.net) | DNS sinkhole local para bloquear anuncios/trackers en toda la red. | Docker o script de un clic | Sí (parcial) | GPL | 2026 | Intermedio |
| NextDNS / Mullvad DNS / Quad9 | DNS cifrado con bloqueo de trackers (configurable en NetworkManager o Portmaster). | Configuración nativa de red o GUI de Portmaster | Sí | Varias | 2026 | Principiante |

#### Permisos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Flatseal](https://github.com/tchx84/Flatseal) | Interfaz para revisar y restringir permisos de apps Flatpak (red, archivos, dispositivos...). | `flatpak install flathub com.github.tchx84.Flatseal` | Sí (parcial) | GPL-3.0 | 2025-26 | Principiante |
| [Firejail](https://firejail.wordpress.com) | Sandbox ligero para restringir apps nativas. | `sudo apt/dnf install firejail` | No | GPL-2.0 | 2025-26 | Intermedio |
| AppArmor / SELinux | Sistemas de control de acceso obligatorio ya incluidos (SELinux en Fedora, AppArmor en Ubuntu/Mint). | Ya vienen instalados | — | GPL | Nativo (integrado) | Intermedio |

#### Metadatos

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Metadata Cleaner](https://flathub.org/apps/fr.romainvigier.MetadataCleaner) | Interfaz basada en MAT2 para ver y eliminar metadatos de fotos, documentos, audio y vídeos. | `flatpak install flathub fr.romainvigier.MetadataCleaner` | Sí | GPL-3.0 | 2025-26 | Principiante |
| [MAT2](https://0xacab.org/jvoisin/mat2) | Herramienta de línea de comandos (con integración en gestores de archivos) para eliminar metadatos. | `sudo apt/dnf install mat2` o `pip` | No | LGPL-3.0 | 2025-26 (PyPI 0.15) | Intermedio |

#### Borrar rastro / cifrado

| Herramienta | Qué hace | Instalación | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [BleachBit](https://www.bleachbit.org) | Limpia cachés, cookies, historiales, temporales y rastros de aplicaciones; incluye borrado seguro. | `.deb`/`.rpm` oficial o repos | Sí | GPL-3.0 | 2026 (v6.0) | Principiante |
| secure-delete / srm (paquete) | Herramientas de línea de comandos para borrado seguro de archivos y espacio libre. | `sudo apt/dnf install secure-delete` | No | GPL | 2025-2026 (sin fecha exacta) | Intermedio |
| [OnionShare](https://onionshare.org) | Comparte archivos de forma anónima vía Tor, sin dejar rastro en servidores. | Flatpak Flathub o `pip` | Sí | GPL-3.0 | 2026 | Intermedio |
| [Cryptomator](https://cryptomator.org) | Cifra carpetas locales o en la nube. | Flatpak Flathub o AppImage | Sí | GPL-3.0 | 2026 | Principiante |
| [VeraCrypt](https://www.veracrypt.fr) / LUKS (nativo) | Contenedores y cifrado de volúmenes (LUKS viene de fábrica en la mayoría de instaladores). | Flatpak/AppImage VeraCrypt o instalador de la distro (LUKS) | Sí | Apache-2.0 / GPL | 2026 / nativo | Intermedio |
| [Syncthing](https://syncthing.net) | Sincroniza archivos entre tus dispositivos sin pasar por una nube central. | Flatpak o repos | Sí | MPL-2.0 | 2026 | Principiante |

[↑ Volver al índice](#índice)

---

## Multiplataforma y navegador

Herramientas que no dependen de un sistema concreto — funcionan igual (o casi) en varios de los sistemas de arriba. Instálalas desde la tienda o el sitio correspondiente a tu sistema.

#### Navegador

| Herramienta | Qué hace | Disponible en | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Tor Browser](https://www.torproject.org) | Navegador basado en Firefox que enruta el tráfico por la red Tor para anonimato real. | Android, Windows, macOS, Linux (en iPhone: Onion Browser) | Sí | MPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Brave](https://brave.com) | Navegador basado en Chromium con bloqueo de anuncios/trackers por defecto. | Android, iPhone, Windows, macOS, Linux | Sí | MPL | 2025-2026 (sin fecha exacta) | Principiante |
| [LibreWolf](https://librewolf.net) | Fork de Firefox endurecido por defecto: sin telemetría, con anti-fingerprinting. | Windows, macOS, Linux | Sí | MPL-2.0 | 2025-2026 (sin fecha exacta) | Principiante |
| [Mullvad Browser](https://mullvad.net/browser) | Basado en Tor Browser pero sin red Tor; pensado para usarse junto a una VPN. | Windows, macOS, Linux | No | MPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Firefox](https://www.mozilla.org/firefox) (configurado con ETP estricto) | Navegador con Enhanced Tracking Protection estricto + soporte de extensiones como uBlock Origin. | Android, iPhone, Windows, macOS, Linux | Sí | MPL | 2025-2026 (sin fecha exacta) | Principiante |
| [uBlock Origin](https://github.com/gorhill/uBlock) | El bloqueador de anuncios y trackers más efectivo, como extensión de navegador. | Firefox/Chrome/Edge/Brave en cualquier sistema | Sí | GPL-3.0 | 2025-2026 (sin fecha exacta) | Principiante |

#### Mensajería

| Herramienta | Qué hace | Disponible en | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Signal](https://signal.org) | Mensajería y llamadas cifradas de extremo a extremo (protocolo Signal). | Android, iPhone, Windows, macOS, Linux | Sí | AGPL/GPL | 2025-2026 (sin fecha exacta) | Principiante |
| [SimpleX Chat](https://simplex.chat) | Mensajería descentralizada sin identificadores (ni número de teléfono ni usuario). | Android, iPhone, Windows, macOS, Linux | Sí | AGPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Session](https://getsession.org) | Mensajería descentralizada y privada sin número de teléfono. | Android, iPhone, Windows, macOS, Linux | Sí | GPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Element](https://element.io) (Matrix) | Cliente de Matrix para chats cifrados y federados. | Android, Windows, macOS, Linux | Sí | Apache-2.0 | 2025-2026 (sin fecha exacta) | Intermedio |
| [Molly](https://molly.im) | Fork endurecido de Signal (cifrado local, borrado de RAM, Tor opcional, sin Google). | Android | Sí | AGPL | 2025-2026 (sin fecha exacta) | Intermedio |
| [Briar](https://briarproject.org) | Mensajería P2P que funciona incluso offline (Tor/Bluetooth). | Android | Sí | GPL | 2025-2026 (sin fecha exacta) | Intermedio |

#### Contraseñas y 2FA

| Herramienta | Qué hace | Disponible en | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [Bitwarden](https://bitwarden.com) | Gestor de contraseñas open-source con autofill, generador y sincronización (freemium real). | Android, iPhone, Windows, macOS, Linux | Sí | GPL | 2026-08/09 | Principiante |
| KeePass (KeePassXC en escritorio, KeePassDX en Android, KeePassium en iPhone) | Gestor de contraseñas offline con base de datos local cifrada (`.kdbx`). | Android, iPhone, Windows, macOS, Linux | Sí | GPL-3.0 | 2026 | Principiante |
| [Proton Pass](https://proton.me/pass) | Gestor de contraseñas cifrado de extremo a extremo, con alias de correo integrados. | Android, iPhone, Windows, macOS, Linux | Sí | Open-source (parcial) | 2025-2026 (sin fecha exacta) | Principiante |
| [Aegis](https://getaegis.app) (Android) / [2FAS Auth](https://2fas.com) / [Ente Auth](https://ente.io/auth) | Apps de autenticación 2FA (TOTP) open-source, cifradas y exportables. | Android, iPhone, Windows, macOS, Linux (según app) | Sí | GPL/AGPL | 2026-02 (Aegis v3.4.2) | Principiante |

#### Correo y alias

| Herramienta | Qué hace | Disponible en | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [SimpleLogin](https://simplelogin.io) | Crea alias de email que reenvían a tu bandeja real, protegiéndote del spam y el tracking. | Web + extensión, apps Android/iPhone | Sí | AGPL | 2025-2026 (sin fecha exacta) | Principiante |
| [addy.io](https://addy.io) (AnonAddy) | Alias de correo open-source con un plan gratuito generoso y soporte PGP. | Web + extensión, apps Android/iPhone | Sí | AGPL | 2025-2026 (sin fecha exacta) | Principiante |
| [Proton Mail](https://proton.me/mail) / [Tuta](https://tuta.com) | Correo cifrado de extremo a extremo con alias, plan gratuito real. | Web, Android, iPhone, Windows, macOS, Linux | Sí | Open-source (clientes) | 2025-2026 (sin fecha exacta) | Principiante |
| [Thunderbird](https://www.thunderbird.net) | Cliente de correo open-source con soporte OpenPGP. | Windows, macOS, Linux | Sí | MPL-2.0 | 2025-2026 (sin fecha exacta) | Principiante |

#### Borrar rastro

| Herramienta | Qué hace | Disponible en | ¿Español? | Licencia | Última actualización | Nivel |
|---|---|---|---|---|---|---|
| [BleachBit](https://www.bleachbit.org) | Limpia cachés, cookies, historiales, temporales y rastros de aplicaciones; incluye borrado seguro. | Windows, Linux (macOS: alternativas nativas de la sección macOS) | Sí | GPL-3.0 | 2026 (v6.0) | Principiante |

[↑ Volver al índice](#índice)

---

## Cómo elegir

No necesitas instalar toda la lista. Reglas prácticas:

1. **En Android**, usa una sola VPN local a la vez (TrackerControl, RethinkDNS o NetGuard compiten por el mismo "slot" de VPN del sistema — elige una).
2. **En iPhone**, la mayor parte del trabajo son ajustes nativos, no apps. Empieza por los 3 ajustes de arriba antes de instalar nada.
3. **En Windows**, empieza por O&O ShutUp10++ o privacy.sexy (elige uno, no los dos a la vez) y añade un firewall de aplicaciones (Portmaster o simplewall) después.
4. **En macOS**, activa FileVault + el Firewall nativo (entrante) y súmales LuLu (saliente) — con eso cubres la mayoría del riesgo cotidiano.
5. **En cualquier sistema**, un gestor de contraseñas (Bitwarden o KeePass) + 2FA (Aegis/2FAS/Ente Auth) hacen más por tu seguridad que cualquier otra herramienta de esta lista. Empieza por ahí si solo vas a hacer una cosa.

[↑ Volver al índice](#índice)

## Qué NO está aquí y por qué

Este repositorio se queda deliberadamente corto en algunos temas porque no son para "gente normal" o se salen del criterio de entrada (ver [CONTRIBUTING.md](CONTRIBUTING.md)):

- **Pentesting y hacking ofensivo**: escáneres de vulnerabilidades, frameworks de explotación, herramientas de ataque WiFi, phishing, C2. Sirven para atacar sistemas de otros, no para proteger el tuyo.
- **OSINT ofensivo sobre terceros**: buscadores de personas, scrapers de redes sociales ajenas, herramientas de rastreo de teléfonos o cuentas de otras personas.
- **Exploits y 0-days**: fuera de alcance total; este repo protege dispositivos, no los compromete.
- **Tails, Qubes OS, Whonix**: son sistemas operativos completos orientados a un modelo de amenaza alto (activismo en riesgo, periodismo en países represivos). Excelentes herramientas, pero no son "instalables hoy sin conocimientos" sobre tu sistema actual — requieren aprender un flujo de trabajo distinto. Si tu modelo de amenaza los necesita, empieza en [privacyguides.org](https://www.privacyguides.org).
- **Cripto/blockchain**: monederos, mezcladores, exchanges. No es el enfoque de este repositorio.
- **Root/jailbreak**: cualquier herramienta que exija romper las protecciones del fabricante queda fuera; el riesgo para un usuario no técnico supera el beneficio.

[↑ Volver al índice](#índice)

## Cómo contribuir

¿Conoces una herramienta que falta o una que ya no se mantiene? Lee [CONTRIBUTING.md](CONTRIBUTING.md) y abre un issue o un pull request.

Criterio de entrada resumido:
1. Sin root, sin jailbreak, sin compilar.
2. Mantenida (actividad en los últimos 12 meses).
3. Gratuita, o con una versión gratuita real y usable (no un trial disfrazado).
4. Protege el propio dispositivo — nada de pentesting, OSINT ofensivo, exploits o hacking de redes/cuentas ajenas.

[↑ Volver al índice](#índice)

## En observación

Herramientas que en algún momento cumplieron el criterio pero cuyo repositorio de GitHub lleva más de 12 meses sin actividad detectada por `scripts/check.py`. No se borran directamente — se mueven aquí con la fecha de la última verificación, y se revisan antes de cada actualización.

*(`scripts/check.py` rellena esta sección automáticamente en cada ejecución; ver el reporte de verificación en cada release. Vacía en el lanzamiento inicial: todas las herramientas de la lista pasaron la comprobación en la fecha de publicación — ver commit inicial.)*

[↑ Volver al índice](#índice)

---

## 📘 ¿Quieres el método completo, no solo las herramientas?

Este repositorio se actualiza, pero **el manual Anonimato Platino** te explica el por qué de cada ajuste y en qué orden hacerlos, paso a paso.

👉 [ALEXIS: URL de la landing]

## Licencia y créditos

Este proyecto se publica bajo licencia [CC-BY-SA-4.0](LICENSE): puedes copiar, adaptar y redistribuir esta lista, incluso con fines comerciales, siempre que menciones la fuente y compartas bajo la misma licencia.

Fuentes y proyectos que sirvieron de referencia para el criterio de curación:

- [privacyguides.org](https://www.privacyguides.org)
- [awesome-privacy](https://github.com/pluja/awesome-privacy)
- [F-Droid](https://f-droid.org)

Gracias también a los mantenedores de cada una de las herramientas listadas — este repositorio no sería posible sin su trabajo.

[↑ Volver al índice](#índice)
