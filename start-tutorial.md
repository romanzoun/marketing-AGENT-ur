# Start-Tutorial für macOS und Windows

Diese Anleitung startet Sara's Marketing AGENT-ur lokal ohne Docker.
Die Oberfläche läuft danach unter [http://127.0.0.1:8765](http://127.0.0.1:8765).

Voraussetzung ist eine persönlich von Roman Zoun unterschriebene Nutzungserlaubnis.
Lizenzanfragen: roman.zoun@gmail.com.

## 1. Programme installieren

Auf beiden Systemen werden benötigt:

- Git
- Python 3.11 oder neuer
- Microsoft Edge oder Google Chrome
- Node.js mit npm, weil darüber die KI-CLI installiert wird

Unter Windows zusätzlich die App **Git Credential Manager** verwenden, die mit
Git for Windows mitgeliefert wird.

## 2. Repository holen

Im Terminal beziehungsweise in PowerShell:

```bash
git clone https://github.com/romanzoun/marketing-AGENT-ur.git
cd marketing-AGENT-ur
```

Das Repository ist öffentlich. Für das Herunterladen und für automatische Updates
wird kein GitHub-Token benötigt.

## 3. Python-Umgebung einrichten

### macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
```

### Windows (PowerShell)

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
Copy-Item .env.example .env
```

Falls PowerShell das Aktivieren blockiert, einmalig in derselben Sitzung
ausführen:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

## 4. Lokale Zugangsdaten eintragen

Die Datei `.env` bleibt lokal und darf niemals committed werden. Für die
Update-Prüfung muss dort nichts eingetragen werden, weil das Repository
öffentlich ist.

`OPENAI_API_KEY` nur eintragen, wenn Bilder erzeugt werden sollen. Dafür
zusätzlich `IMAGE_PROVIDER=openai` setzen. Ohne Key bleibt `IMAGE_PROVIDER=none`.

## 5. KI-CLI konfigurieren

Für Content-Jobs muss eine KI-CLI installiert, angemeldet und in `.env`
ausgewählt werden. Dafür wird zuerst Node.js installiert, weil es `npm` mitbringt.

### Node.js installieren

#### macOS

Falls Homebrew noch nicht installiert ist:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Danach Node.js installieren und prüfen:

```bash
brew install node
node --version
npm --version
```

#### Windows

PowerShell als normaler Benutzer öffnen und ausführen:

```powershell
winget install --id OpenJS.NodeJS.LTS -e
```

PowerShell danach schließen und neu öffnen. Dann prüfen:

```powershell
node --version
npm --version
```

Beide Befehle müssen eine Versionsnummer anzeigen. Falls `npm` nicht gefunden
wird, Windows neu starten und die Prüfung wiederholen.

Standard in `.env` ist:

```text
BRAIN_ENGINE=copilot
```

Nur wenn ausdrücklich Codex verwendet werden soll, diese Zeile setzen:

```text
BRAIN_ENGINE=codex
```

`auto` bevorzugt ebenfalls Copilot und nutzt Codex nur, wenn Copilot nicht
verfügbar ist.

### GitHub Copilot CLI

```bash
npm install -g @github/copilot
copilot login
```

### Codex CLI

```bash
npm install -g @openai/codex
codex login
```

Copilot verwendet die Rollen aus `.github/agents/`, Codex die Rollen aus
`.codex/agents/`.

## 6. LinkedIn-Browser einmal anmelden

Die App verwendet ein separates Browserprofil. Alle bereits geöffneten Edge-
oder Chrome-Fenster mit diesem Profil vorher schließen.

### macOS

```bash
./scripts/start-linkedin-browser-macos.sh
```

### Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\start-linkedin-browser-windows.ps1
```

Im geöffneten Fenster bei LinkedIn anmelden. Dieses Fenster während der Nutzung
offen lassen. Die Anmeldung bleibt im separaten Profil gespeichert.

## 7. App starten

### macOS

Doppelklick auf `LinkedIn Automation.command` oder im Terminal:

```bash
./bin/li-desktop
```

### Windows

In PowerShell im Projektordner:

```powershell
.\.venv\Scripts\python.exe -m linkedin_agents.desktop
```

Es öffnet sich das Fenster **Sara's Marketing AGENT-ur**. Beim Öffnen wird
geprüft, ob auf GitHub eine neuere Version vorliegt. Danach **Starten** drücken.
Der Browser öffnet [http://127.0.0.1:8765](http://127.0.0.1:8765).

**Aktualisieren** prüft GitHub jederzeit manuell. Ein Update wird nur übernommen,
wenn keine lokalen Änderungen überschrieben würden.

## 8. Verbindung prüfen

Mit aktivierter Python-Umgebung:

### macOS

```bash
./bin/li check
```

### Windows

```powershell
$env:PYTHONPATH = "src"
python -m linkedin_agents.cli check
```

Erwartet wird eine Ausgabe mit `"ok": true` und `"logged_in": true`.

## Tägliche Nutzung

1. LinkedIn-Browser über das passende Skript aus Schritt 6 öffnen.
2. Desktop-App starten.
3. Im Fenster **Starten** drücken.
4. In der Oberfläche Entwürfe prüfen und ausdrücklich freigeben.

Nichts wird ohne Freigabe veröffentlicht. Automatische Jobs laufen nur zwischen
08:00 und 17:00 Uhr.

## Probleme

- **Update schlägt fehl:** Internetverbindung und die Adresse in `config/update.yaml` prüfen. Ein GitHub-Token wird für dieses öffentliche Repository nicht benötigt.
- **Lokale Änderungen blockieren das Update:** Änderungen sichern oder verwerfen,
  danach erneut aktualisieren.
- **LinkedIn nicht verbunden:** Browserfenster aus Schritt 6 muss offen und
  angemeldet sein. Port `9222` darf nicht durch einen anderen Browser belegt sein.
- **Fenster öffnet sich nicht:** Prüfen, ob `.venv` existiert und die Pakete aus
  `requirements.txt` installiert wurden.
