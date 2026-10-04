# Installation auf einem anderen Mac oder Windows-PC

Die empfohlene Variante ist **Docker Desktop**. Dadurch müssen Python, Node.js,
Playwright und Codex nicht einzeln auf dem Zielrechner installiert werden. Benötigt
werden nur:

- Docker Desktop
- Microsoft Edge oder Google Chrome
- ein OpenAI-API-Key
- ein LinkedIn-Login

Die Oberfläche ist anschließend nur lokal unter `http://127.0.0.1:8765`
erreichbar. Der Scheduler läuft in einem zweiten Container und prüft jede Minute
die aktiven Jobs.

## 1. Projekt auf den Zielrechner kopieren

Den **gesamten** Ordner `linkedin-automation` kopieren. Wichtig sind auch die
versteckten Ordner und Dateien wie `.codex`, `.github`, `.env.example` und `.runs`.

Empfohlene Zielordner:

- macOS: `/Users/DEINNAME/linkedin-automation`
- Windows: `C:\linkedin-automation`

Bei einem Umzug von einem bereits laufenden Rechner zuerst dort stoppen:

```bash
docker compose down
```

Nur ein Rechner sollte denselben LinkedIn-Account und dieselben Queue-Dateien
automatisch bearbeiten. Zwei gleichzeitig laufende Scheduler können sonst dieselbe
Aktion doppelt ausführen.

Für einen vollständigen Umzug müssen insbesondere diese Daten mitkopiert werden:

- `Kampagnen/` – Kampagnen, Versionen, Freigaben, Planung, Historie und Analytics
- `team/` – Stilprofil und gelernte Freigabemuster
- `ideas/` – Ideen
- `automation/` – Jobs und Automatik-Einstellungen
- `config/` – persönliches Profil/CV
- `.runs/` – erzeugte und hochgeladene Bilder

### Wo die dauerhaften Daten liegen

Es muss **kein zusätzlicher Datenordner innerhalb von Docker** angelegt werden. Der
kopierte Projektordner auf dem Mac oder Windows-PC ist gleichzeitig die dauerhafte,
menschenlesbare Datenablage:

```text
linkedin-automation/
├── Kampagnen/
│   └── <kampagne>/
│       ├── kampagne.yaml
│       ├── versions/
│       └── queue/
│           ├── approvals.md
│           ├── schedule.md
│           ├── log.md
│           └── analytics.yaml
├── team/
│   ├── board.md
│   ├── <agent>/
│   │   ├── memory.md
│   │   ├── todo.md
│   │   ├── inbox.md
│   │   ├── outbox.md
│   │   └── collected/
│   └── style/
│       ├── profile.md
│       ├── learning.json
│       └── approved/
├── ideas/ideas.yaml
├── automation/jobs.yaml
├── config/
│   ├── personal_profile.yaml
│   └── timeouts.yaml
└── .runs/images/
```

`docker-compose.yml` bindet genau diese Host-Ordner in **beide** Container ein:

| Ordner auf dem Rechner | Pfad im Container | Inhalt |
|---|---|---|
| `./Kampagnen` | `/app/Kampagnen` | Kampagnen, Freigaben, Planung, Historie, Analytics |
| `./team` | `/app/team` | Agenten-Memory, Stil-Lernen, Board und Arbeitsdateien |
| `./ideas` | `/app/ideas` | Ideen |
| `./automation` | `/app/automation` | Jobdefinitionen und Ausführungszustand |
| `./config` | `/app/config` | persönliches Profil/CV |
| `./.runs` | `/app/.runs` | Bilder und technische Logs |

Das bedeutet: Wenn ein Agent beispielsweise `/app/team/copywriter/memory.md`
aktualisiert, steht die Änderung sofort als
`team/copywriter/memory.md` im normalen Projektordner des Rechners. Ein Neubau,
Update oder Löschen des Containers entfernt diese Dateien nicht.

Nur der technische Codex-Login-Cache liegt im benannten Docker-Volume
`codex-home`. Darin befinden sich **keine** Kampagnen, Entwürfe oder Lern-Memories.
Dieser Cache wird beim Rechnerwechsel bewusst nicht kopiert, sondern per API-Key
neu erzeugt. Dadurch landet `auth.json` nicht zwischen den normalen Projektdateien.

## 2. Docker Desktop installieren

- [Docker Desktop für macOS](https://docs.docker.com/desktop/setup/install/mac-install/)
- [Docker Desktop für Windows](https://docs.docker.com/desktop/setup/install/windows-install/)

Docker Desktop einmal öffnen und die Ersteinrichtung abschließen. Unter Windows ist
die WSL-2-Variante normalerweise die einfachste Wahl.

## 3. `.env` mit dem OpenAI-Key anlegen

Der API-Key gehört im Projekt-Hauptordner in die Datei `.env` – direkt neben
`docker-compose.yml`. Er gehört **nicht** in `Dockerfile`, YAML-Kampagnen oder den
Programmcode.

API-Key im [OpenAI-Dashboard](https://platform.openai.com/api-keys) erzeugen. Codex
unterstützt für lokale und automatisierte Abläufe die Anmeldung per API-Key; diese
Nutzung wird über das API-Konto abgerechnet. Siehe
[OpenAI: Codex-Authentifizierung](https://developers.openai.com/codex/auth).

### macOS (Terminal)

```bash
cd /Users/DEINNAME/linkedin-automation
cp .env.example .env
open -e .env
```

### Windows (PowerShell)

```powershell
cd C:\linkedin-automation
Copy-Item .env.example .env
notepad .env
```

Für OpenAI-Bilder und Codex sollte `.env` so aussehen:

```dotenv
CDP_ENDPOINT=http://localhost:9222
LOG_LEVEL=INFO
IMAGE_PROVIDER=openai
OPENAI_API_KEY=HIER_DEINEN_OPENAI_KEY_EINTRAGEN
IMAGE_MODEL=gpt-image-1
```

Hinweise:

- Den echten Key nur hinter `OPENAI_API_KEY=` einsetzen.
- Keine Leerzeichen vor oder nach dem `=` einfügen.
- Wenn keine Bilder erzeugt werden sollen, `IMAGE_PROVIDER=none` setzen.
- Docker ersetzt `CDP_ENDPOINT` intern automatisch durch
  `http://host.docker.internal:9222`. Der Wert in `.env` bleibt für einen möglichen
  lokalen Betrieb korrekt.
- `.env` ist bereits von Git und vom Docker-Build ausgeschlossen. Trotzdem niemals
  verschicken, committen oder in Screenshots zeigen.

## 4. Separaten LinkedIn-Browser starten

Die Automation verwendet bewusst ein eigenes Browserprofil. Dort einmal bei
LinkedIn anmelden; die Sitzung bleibt danach in diesem Profil gespeichert.

Das separate `--user-data-dir` ist zwingend: Aktuelle Chrome-Versionen akzeptieren
Remote Debugging beim normalen Standardprofil nicht mehr. Außerdem erhält die
Automation dadurch keinen Zugriff auf das private Alltagsprofil.

### macOS

Im Projekt ist ein Startskript enthalten:

```bash
cd /Users/DEINNAME/linkedin-automation
chmod +x scripts/start-linkedin-browser-macos.sh
./scripts/start-linkedin-browser-macos.sh
```

Das Skript verwendet zuerst Microsoft Edge und andernfalls Google Chrome.

### Windows

In PowerShell:

```powershell
cd C:\linkedin-automation
powershell -ExecutionPolicy Bypass -File .\scripts\start-linkedin-browser-windows.ps1
```

Das Skript sucht zuerst Microsoft Edge und danach Google Chrome.

Im geöffneten Fenster zu LinkedIn gehen und anmelden. Dieses Browserfenster während
der Automation geöffnet lassen. Den Debug-Port `9222` in Router oder Firewall
niemals für andere Rechner oder das Internet freigeben.

Optionaler Browser-Test:

macOS:

```bash
curl http://127.0.0.1:9222/json/version
```

Windows PowerShell:

```powershell
Invoke-RestMethod http://127.0.0.1:9222/json/version
```

## 5. Anwendung erstmals starten

Im Projektordner:

```bash
docker compose up --build -d
docker compose ps
```

Die erste Erstellung dauert länger, weil das Image Python, Node.js und Codex CLI
installiert. Danach Codex einmal mit dem Key aus `.env` anmelden:

```bash
docker compose exec app sh -lc 'printenv OPENAI_API_KEY | codex login --with-api-key'
docker compose exec app codex login status
```

Der Login wird im Docker-Volume `codex-home` gespeichert und von Web-App und
Scheduler gemeinsam verwendet. Der Key wird bei diesem Befehl nicht im Terminal
ausgegeben. Das Volume enthält danach Anmeldedaten und sollte weder exportiert noch
an andere Personen weitergegeben werden.

Nun `http://127.0.0.1:8765` öffnen und oben **Health Check** anklicken. Erfolgreich
sind diese drei Punkte:

- Browser/CDP erreichbar
- LinkedIn eingeloggt
- Codex eingeloggt und eine minimale Modellanfrage erfolgreich

Logs bei Problemen:

```bash
docker compose logs --tail=200 app
docker compose logs --tail=200 scheduler
```

## 6. Autostart auf macOS und Windows

Für die Anwendung selbst ist kein zusätzlicher Cronjob und kein weiteres
Autostart-Skript nötig:

1. Docker Desktop öffnen.
2. **Settings → General** öffnen.
3. **Start Docker Desktop when you sign in to your computer** aktivieren.
4. Den Stack mindestens einmal mit `docker compose up -d` erstellt haben.

Beide Services besitzen bereits `restart: unless-stopped`. Sobald Docker Desktop
nach der Anmeldung läuft, startet es daher Web-App und Scheduler wieder. Wenn der
Stack absichtlich mit `docker compose stop` angehalten wurde, mit
`docker compose up -d` wieder aktivieren.

Zusätzlich muss der LinkedIn-Browser beim Benutzer-Login starten.

### Browser-Autostart auf macOS

Die Datei
`autostart/macos/com.linkedin-automation.browser.plist.example` öffnen und darin
`__PROJECT_DIR__` durch den absoluten Projektpfad ersetzen, zum Beispiel
`/Users/roman/linkedin-automation`. Danach:

```bash
mkdir -p "$HOME/Library/LaunchAgents"
cp autostart/macos/com.linkedin-automation.browser.plist.example \
  "$HOME/Library/LaunchAgents/com.linkedin-automation.browser.plist"
launchctl bootstrap "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.linkedin-automation.browser.plist"
```

Nach der nächsten macOS-Anmeldung startet der separate LinkedIn-Browser automatisch.
Zum Entfernen:

```bash
launchctl bootout "gui/$(id -u)" \
  "$HOME/Library/LaunchAgents/com.linkedin-automation.browser.plist"
```

### Browser-Autostart auf Windows

1. Im Startmenü **Aufgabenplanung** öffnen.
2. Rechts **Aufgabe erstellen…** wählen.
3. Name: `LinkedIn Automation Browser`.
4. Unter **Trigger**: **Bei Anmeldung** des eigenen Benutzers.
5. Unter **Aktionen**: **Programm starten**.
6. Programm/Skript: `powershell.exe`.
7. Argumente hinzufügen (Projektpfad anpassen):

```text
-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File "C:\linkedin-automation\scripts\start-linkedin-browser-windows.ps1"
```

8. Aufgabe speichern und über **Ausführen** einmal testen.

Docker Desktop und der Browser starten damit nach der Benutzeranmeldung. Der Rechner
muss eingeschaltet, angemeldet und darf nicht im Ruhezustand sein, wenn LinkedIn-
Aktionen genau zum vorgesehenen Zeitpunkt ausgeführt werden sollen.

## 7. Updates und Neustart

Nach Änderungen am Programmcode:

```bash
docker compose up --build -d
```

Nur nach Änderungen an `.env` reicht ebenfalls dieser Befehl; ein bloßes
`docker compose restart` übernimmt geänderte Umgebungsvariablen nicht zuverlässig.

Manuell stoppen und wieder starten:

```bash
docker compose down
docker compose up -d
```

`docker compose down` löscht weder die gemounteten Projektordner noch das benannte
`codex-home`-Volume. Nicht `docker compose down -v` verwenden, wenn der gespeicherte
Codex-Login erhalten bleiben soll.

## 8. Backup

Für ein Backup Docker kurz stoppen und den gesamten Projektordner sichern. Die
Datei `.env` separat und verschlüsselt sichern oder auf dem Zielrechner neu anlegen.
Das Docker-Volume mit dem Codex-Login muss nicht übertragen werden; die Anmeldung
kann mit dem obigen `codex login --with-api-key`-Befehl wiederholt werden.

## 9. Häufige Fehler

### Oberfläche öffnet nicht

```bash
docker compose ps
docker compose logs --tail=200 app
```

Prüfen, ob bereits ein anderes Programm Port `8765` verwendet.

### LinkedIn ist im Health Check rot

- Separaten Browser mit dem mitgelieferten Skript starten.
- In genau diesem Browserprofil bei LinkedIn anmelden.
- Prüfen, ob `http://127.0.0.1:9222/json/version` antwortet.
- Containerzugriff testen:

```bash
docker compose exec app python -c "import httpx; print(httpx.get('http://host.docker.internal:9222/json/version').status_code)"
```

### Codex ist im Health Check rot

```bash
docker compose exec app codex login status
docker compose exec app sh -lc 'printenv OPENAI_API_KEY | codex login --with-api-key'
```

Wenn das weiterhin fehlschlägt, API-Key, API-Guthaben/Abrechnung und den
Internetzugang von Docker prüfen.

### Bilder werden nicht erzeugt

In `.env` müssen `IMAGE_PROVIDER=openai` und ein gültiger `OPENAI_API_KEY` stehen.
Danach die Container neu erstellen:

```bash
docker compose up -d --force-recreate
```
