---
name: linkedin-actions
description: Wie das Team LinkedIn-Aktionen über die deterministischen Python-Werkzeuge ausführt (sammeln, posten, kommentieren, antworten, teilen, Bild generieren).
---

# Skill: LinkedIn-Aktionen

Alle LinkedIn-Aktionen laufen über ein einziges Python-Tool mit JSON-Ausgabe.
Wrapper: `./bin/li <command> ...` (setzt `PYTHONPATH=src` selbst).

## Voraussetzungen

- Microsoft Edge mit offenem Debug-Port und eingeloggter LinkedIn-Session:
  ```bash
  /Applications/Microsoft\ Edge.app/Contents/MacOS/Microsoft\ Edge \
      --remote-debugging-port=9222 --user-data-dir="$HOME/edge-linkedin"
  ```
- Abhängigkeiten installiert: `pip install -r requirements.txt`.
- Prüfe die Session zuerst: `./bin/li check`.

## Befehle

| Aktion | Befehl | Ausgabe |
|--------|--------|---------|
| Wall sammeln | `./bin/li wall --keywords a,b --limit 10 [--with-urls]` | `{ok, count, posts:[{id,author,text,url}]}` |
| Feed sammeln | `./bin/li feed --keywords a,b --limit 15 [--with-urls]` | wie oben |
| Posten | `./bin/li post --text "..." [--image PFAD]` | `{ok, command:"post"}` |
| Kommentieren (Feed-Node) | `./bin/li comment --post-id URN --text "..."` | `{ok, command:"comment"}` |
| **Kommentieren (per URL)** | `./bin/li comment-url --url <permalink> --text "..."` | `{ok, command:"comment-url"}` |
| Reply | `./bin/li reply --post-id URN --text "..."` | `{ok, command:"reply"}` |
| Reshare | `./bin/li reshare --post-id URN [--thoughts "..."]` | `{ok, command:"reshare"}` |
| Personen suchen | `./bin/li-jobs --campaign C find-connections --query "CIO Dokumentenmanagement" --limit 5` | legt noch nicht vernetzte Profile in `approvals.md` ab |
| Bild | `./bin/li image --prompt "..." --name post_1` | `{ok, image_path}` |
| Kampagne | `./bin/li campaign --campaign Kampagnen/x.yaml` | `{ok, campaign:{...}}` |

## Freigabe → Einplanung → automatisches Posten (`./bin/li-jobs`)

Nichts wird sofort veröffentlicht. Ablauf pro Kampagne, Dateien liegen in
`Kampagnen/<x>/queue/`:

`approvals.md` (warten auf Freigabe) → `schedule.md` (mit Zeitpunkt) → `log.md` (erledigt).

| Job | Befehl | Zweck |
|-----|--------|-------|
| Entwurf anlegen | `./bin/li-jobs --campaign C add --kind post --text "..."` | Post-Vorschlag zur Freigabe |
| Kommentar-Kandidaten | `./bin/li-jobs --campaign C find-comments --limit 5` | Feed-Posts + Permalink-URLs sammeln |
| Kommentartext ergänzen | direkt in `approvals.md` im `text:`-Feld schreiben | Meinung formulieren |
| Vernetzungskandidaten | `./bin/li-jobs --campaign C find-connections --query "<Rolle>" --limit 5` | Profile mit sichtbarer Vernetzen-Aktion sammeln |
| Bild setzen | `./bin/li-jobs --campaign C image --id <id> --query "..." --source web\|gen` | Web-Bild **mit Quelle** oder KI-Bild |
| Einplanen | `./bin/li-jobs --campaign C schedule --slots 09:00,13:00` | nur `- [x]`-Angekreuztes bekommt Termin |
| Veröffentlichen | `./bin/li-jobs --campaign C run-due` | **Cron-Job**: postet, was fällig ist |
| Übersicht | `./bin/li-jobs --campaign C status` | Zahlen + nächste Termine |

**Freigabe** = in `approvals.md` die Checkbox auf `- [x] freigeben` setzen. Texte
dürfen dort direkt editiert werden. Kommentare ohne Text werden nicht eingeplant.
Vernetzungsanfragen benötigen immer eine manuelle Freigabe und eine persönliche
Notiz mit höchstens 300 Zeichen. Pro Tag werden maximal fünf versendet.

**Bildquelle:** Bei `--source web` (Openverse, CC-lizenziert) wird die Attribution
in `image_source` gespeichert und beim Posten **automatisch an den Text angehängt**.

**Cron** (alle 15 Min prüfen, ob etwas fällig ist):
```cron
*/15 * * * * cd /Users/romanzoun/linkedin-automation && ./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" run-due >> .runs/cron.log 2>&1
```
Voraussetzung: Edge läuft mit `--remote-debugging-port=9222` und ist eingeloggt.
Test ohne Veröffentlichen: `run-due --dry-run`.

## Weboberfläche — Sara's Marketing AGENT-ur (`./bin/li-ui`)

`./bin/li-ui` startet die UI auf http://127.0.0.1:8765. Sie arbeitet auf denselben
MD-Queues (keine eigene Datenbank). Im Tab **Jobs** werden wiederkehrende Aufgaben
mit Alltagssprache angelegt (`jeden Tag um 15 Uhr`, `alle 30 Minuten`,
`werktags um 09:00`). Nur Jobs mit aktivem Schalter laufen. Der gemeinsame
System-Cron-Takt wird dort einmalig über **Automatik aktivieren** eingerichtet.
Im Tab **Freigaben** verschiebt **Freigeben** einen Eintrag direkt mit manuellem
oder automatisch gewähltem Termin nach **Planung**. Weitere Tabs: **Cron**,
**Historie** und **Kampagnen**.

## Gehirn & Betriebsbereitschaft

| Zweck | Befehl |
|-------|--------|
| Content über Copilot/Codex erzeugen | `./bin/li-brain --campaign C draft-posts --count 2` |
| Kandidaten sammeln + Kommentare texten | `./bin/li-brain --campaign C find-and-write --count 5` |
| Personen finden + Vernetzungsnotizen texten | `./bin/li-brain --campaign C find-and-write-connections --count 5` |
| verfügbare KI-CLI prüfen | `./bin/li-brain --campaign C check` |
| echten Modell-/Kontingentzugriff prüfen | `./bin/li-brain --campaign C probe` |
| Browser/Session/KI-CLI prüfen | `./bin/li-health [--no-start] [--quiet]` |

`li-brain` ruft bevorzugt die Copilot Custom Agents headless auf. Fehlt Copilot
oder schlägt sein Lauf fehl, übernimmt Codex CLI mit `codex exec` und
Workspace-Sandbox. Mit `BRAIN_CLI=codex` kann Codex fest gewählt werden. Beide
Wege legen Vorschläge in `approvals.md` ab und veröffentlichen **nichts**.
`li-health` startet Edge bei Bedarf und meldet fehlenden Login per Notification.
Der **Health Check**-Button der Weboberfläche prüft zusätzlich per minimaler
`HEALTH_OK`-Anfrage, ob die ausgewählte KI-CLI tatsächlich Modellzugriff bzw.
Kontingent hat. Dieser aktive Test läuft nur auf Klick und nutzt eine kleine
Menge KI-Kontingent; der normale Status bleibt passiv.

**Vollständige Crontab-Vorlage:**
```cron
# 07:30 werktags: Ideen erzeugen (Copilot CLI)
30 7 * * 1-5 cd /Users/romanzoun/linkedin-automation && ./bin/li-health --quiet && ./bin/li-brain --campaign "Kampagnen/document validator/kampagne.yaml" draft-posts --count 2 >> .runs/cron.log 2>&1
45 7 * * 1-5 cd /Users/romanzoun/linkedin-automation && ./bin/li-brain --campaign "Kampagnen/document validator/kampagne.yaml" find-and-write --count 5 >> .runs/cron.log 2>&1
# alle 10 Min: Betriebsbereitschaft prüfen
*/10 * * * * cd /Users/romanzoun/linkedin-automation && ./bin/li-health --quiet >> .runs/cron.log 2>&1
# alle 15 Min: nur posten, wenn Health ok
*/15 * * * * cd /Users/romanzoun/linkedin-automation && ./bin/li-health --quiet --no-start && ./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" run-due >> .runs/cron.log 2>&1
```

## Wichtige Hinweise

- Die `id`/URN aus `wall`/`feed` unverändert an `comment`/`reply`/`reshare` weitergeben.
- Zum Testen ohne Veröffentlichen: `--dry-run` an Schreibbefehle anhängen.
- Ausgaben sind JSON auf stdout; Logs gehen auf stderr.
- Selektoren können sich ändern — bei Fehlern `src/linkedin_agents/browser/linkedin.py` prüfen.

## Verifizierte Fakten (Discovery 2026-09-09)

Ausführbar: `PYTHONPATH=src python scripts/discover.py` (read-only, 9/9 Checks ok).

- **Zwei Feed-Varianten:**
  - **Wall** (`/in/me/recent-activity/all/`): klassisch, `data-urn="urn:li:activity:..."`
    → stabile IDs, ideal für `comment`/`reply`/`reshare`.
  - **Haupt-Feed** (`/feed/`): neue React-Variante, Container
    `div[role="listitem"][componentkey^="update-card-focus"]`, **ohne `data-urn`**.
    Die gesammelte `id` ist der `componentkey` und **nur pro Seiten-Render stabil**,
    nicht über Reloads/Aufrufe hinweg.
- **Konsequenz:** Für Engagement auf **Feed**-Posts nicht auf eine später wieder
  auffindbare URN verlassen. Zuverlässig sind: eigene **Posts** (`post`) und
  Engagement auf **Wall**-Beiträgen. Für Feed-Kommentare im selben Lauf agieren.
- **Empfohlener Weg (stabil): URL speichern, später per URL kommentieren.**
  Beim Sammeln `--with-urls` nutzen → jeder Beitrag bekommt eine Permalink-URL
  (via „Copy link to post“). Später jederzeit: `./bin/li comment-url --url <permalink> --text "..."`.
  Der Feed mischt sich ständig um; eine gespeicherte URL zeigt dagegen stabil auf
  den Einzelpost. `--with-urls` öffnet je Beitrag das „…“-Menü → nur für kleine
  Kandidaten-Listen verwenden, nicht für 40+.
- **Composer:** Submit-Button heißt **`Post`**, Medien/Bild-Button heißt **`Add media`**
  (englische UI); Buttons rendern leicht verzögert.
