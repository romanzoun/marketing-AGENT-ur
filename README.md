# Sara's Marketing AGENT-ur

Lokale Anwendung zur Planung, Freigabe und Ausführung von LinkedIn-Kampagnen.
Die Weboberfläche läuft unter `http://127.0.0.1:8765`. Nichts wird ohne Freigabe
veröffentlicht.

## Lizenz

Copyright (c) 2026 Roman Zoun (romanzoun). Alle Rechte vorbehalten.

Jegliche Nutzung ist nur mit einer persönlich von Roman Zoun unterschriebenen
Erlaubnis zulässig. Der vollständige Text steht in [LICENSE.md](LICENSE.md).

## Für Teammitglieder

1. Roman Zoun erteilt GitHub-Zugriff auf das private Repository.
2. Das Repository wird einmalig ausgecheckt:

```bash
git clone https://github.com/romanzoun/marketing-AGENT-ur.git
cd marketing-AGENT-ur
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

3. In `.env` werden die persönlichen Zugangsdaten lokal eingetragen. Diese Datei
   wird niemals ins Repository übernommen.
4. Der LinkedIn-Browser wird mit dem mitgelieferten Startskript geöffnet und die
   eigene LinkedIn-Sitzung einmal angemeldet.
5. Danach genügt ein Doppelklick auf `LinkedIn Automation.command`.

Das Fenster bietet **Starten**, **Aktualisieren** und **Beenden**. Beim Öffnen
prüft es automatisch, ob auf GitHub eine neuere Version vorliegt. Ein Update
wird nur übernommen, wenn keine lokalen Änderungen überschrieben würden, und die
App wird danach neu gestartet.

Die Repository-Adresse steht in [config/update.yaml](config/update.yaml).

## LinkedIn Marketing Team — mit Codex CLI

Ein Team spezialisierter CLI-Agenten, das LinkedIn-Kampagnen managt:
Content ausdenken, schreiben, prüfen und über eine **laufende Chrome/LinkedIn-Session**
(Playwright) **posten, kommentieren, antworten und teilen**.

`li-brain` verwendet ausschließlich Codex CLI. Python liefert die
deterministischen Werkzeuge; die Rollen sind projektbezogene Codex-Agenten.

## Das Team (`.codex/agents/*.toml`)

| Agent | Rolle |
|-------|-------|
| `orchestrator` | Plant den Lauf, entscheidet was posten/replyen/teilen, delegiert |
| `campaign-manager` | Lädt/prüft Kampagne, wacht über Limits & Guardrails |
| `engagement-scout` | Sammelt Beiträge von der eigenen Wall und aus dem Feed |
| `content-strategist` | Entwickelt Content-Ideen (Posts, Kommentare, Reshares) |
| `copywriter` | Schreibt finale Texte in der Markenstimme |
| `art-director` | Entwirft Bild-Prompts und rendert Bilder |
| `reviewer` | Prüft strikt gegen die Kampagne (Freigabe/Ablehnung) |
| `operator` | Führt Aktionen über die Playwright-Werkzeuge aus |

Jeder Agent hat unter `team/<agent>/` eine eigene **Ablage**, ein **Gedächtnis**
(`memory.md`, v. a. Schreibstil), eine **Todo-Liste** (`todo.md`) sowie
**inbox/outbox** zur Delegation. Der geteilte Überblick liegt in `team/board.md`.
Das Betriebshandbuch und die gemeinsamen Grundregeln stehen in `AGENTS.md`.

## Setup

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python -m playwright install chromium   # optional (für CDP nicht zwingend)
cp .env.example .env

# Codex CLI installieren und einloggen:
npm install -g @openai/codex
codex login
```

### Laufende LinkedIn-Session (CDP)

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --remote-debugging-port=9222 --user-data-dir="$HOME/chrome-linkedin"
```

Fenster offen lassen und einmal bei LinkedIn einloggen. Danach sollte
`./bin/li check` `{"ok": true, "logged_in": true}` liefern.

## Steuerung über Codex

Im Projektordner:

```bash
codex          # interaktive Session

# Beispiel-Prompts:
#   "Starte einen Kampagnenlauf für Kampagnen/example_campaign.yaml"
#   "Sammle meine Wall zu den Kampagnen-Keywords und schlage 3 Kommentare vor"
```

Den Orchestrator interaktiv verwenden:

```bash
codex
# Prompt: "Nutze den Agenten orchestrator und plane den heutigen Lauf für Kampagnen/example_campaign.yaml"
```

Headless/automatisch für einen Entwurfsjob:

```bash
./bin/li-brain --campaign Kampagnen/example_campaign.yaml draft-posts --count 2
```

Für Jobs und Cron verwendet `./bin/li-brain` `codex exec` mit den Agenten unter
`.codex/agents/`. Der Git-Check wird bewusst übersprungen, weil die Queue-Dateien
selbst die überprüfbaren Artefakte sind:

```bash
./bin/li-brain --campaign Kampagnen/example_campaign.yaml check
```

Die Aufgaben unter `PROMPTS` in `src/linkedin_agents/brain.py` sind Basis-Prompts.
Zur Laufzeit werden der konkrete Kampagnenpfad, der vollständige Originalbeitrag,
das persönliche Profil, das jeweilige Agenten-Memory, das Stilprofil, die
Lernhistorie und freigegebene Beispiele injiziert. Kommentar-, Reshare- und
Vernetzungsjobs behalten technisch lesbare Kandidaten zunächst bei. Codex bewertet
sie anschließend semantisch gegen Ziel, Zielgruppe, Rollen, Themen und Ausschlüsse
der Kampagne. Die Freigabeansicht sortiert nach dem niedrigeren Wert aus
Kampagnenpassung und Text-/Stilscore.

### Job-Abläufe und Zeitbudgets

| Job im Menü | Verarbeitung | Zeitbudget |
|-------------|--------------|------------|
| Posts entwerfen (Codex) | Kampagnenidee → Copywriter → Style-Evaluator → optionaler Rewrite → Reviewer → Freigabe-Queue | 25 Minuten Agentenzeit |
| Kommentare finden + texten (Codex) | LinkedIn-Feed → Passungsscore des vollständigen Originalposts → Copywriter → Style-Evaluator → optionaler Rewrite → Reviewer → Freigabe-Queue | 35 Minuten Agentenzeit |
| Reshares finden + texten (Codex) | LinkedIn-Suche → Kampagnenrelevanz → Entscheidung mit/ohne Begleittext → Copywriter → Style-Evaluator → optionaler Rewrite → Reviewer → Freigabe-Queue | 35 Minuten Agentenzeit |
| Kontakte finden + Notizen (Codex) | Personensuche aus Zielgruppe/Personas → Rollen-Passung → persönliche Notiz → Reviewer → Freigabe-Queue | 35 Minuten Agentenzeit |
| Nur Kandidaten sammeln | LinkedIn-Suche und Keyword-Vorauswahl, ohne Codex-Textkette | kein langes Agentenzeitbudget |
| Fällige veröffentlichen | Bereits freigegebene und fällige Queue-Einträge über den Operator ausführen | kein Content-Agent |

Das äußere Job-Zeitbudget beträgt 50 Minuten und umfasst zusätzlich Browserarbeit,
lokale Evaluation, Planung und gegebenenfalls Bildgenerierung. Die Stufen laufen
größtenteils nacheinander, weil jede die Ausgabe der vorherigen benötigt. Eine
zweite Text-/Bewertungsrunde findet nur statt, wenn der Style-Score unter `0.70`
liegt. Abgebrochene Post-Läufe werden anhand fertiger Artefakte fortgesetzt, statt
dieselben Ideen erneut zu erzeugen.

Der Button **Health Check** in der Kopfzeile prüft gemeinsam:

- Erreichbarkeit des LinkedIn-Browsers und den LinkedIn-Login,
- Installation und Login der Codex CLI,
- den tatsächlichen Modell-/Kontingentzugriff über eine minimale Testfrage.

Die Testfrage wird nur beim Klick gesendet und verbraucht eine kleine Menge
KI-Kontingent. Der laufende Status in der Kopfzeile bleibt passiv.

## Werkzeuge (deterministisch, JSON)

Wrapper `./bin/li` (setzt `PYTHONPATH=src`):

| Aktion | Befehl |
|--------|--------|
| Wall sammeln | `./bin/li wall --keywords a,b --limit 10` |
| Feed sammeln | `./bin/li feed --keywords a,b --limit 15` |
| Posten | `./bin/li post --text "..." [--image PFAD]` |
| Kommentieren | `./bin/li comment --post-id URN --text "..."` |
| Reply | `./bin/li reply --post-id URN --text "..."` |
| Reshare | `./bin/li reshare --post-id URN [--thoughts "..."]` |
| Bild | `./bin/li image --prompt "..." --name post_1` |
| Kampagne prüfen | `./bin/li campaign --campaign Kampagnen/x.yaml` |
| Session prüfen | `./bin/li check` |

Zum Entwerfen ohne Veröffentlichen: `--dry-run` an Schreibbefehle anhängen.
Beim tatsächlichen Veröffentlichen setzt der Browser-Operator Post-, Kommentar-,
Reply- und Reshare-Texte in einem Schritt in den LinkedIn-Editor ein. Er tippt nicht
mehr Zeichen für Zeichen; ein CDP-`insert_text` dient als Fallback und verändert
nicht die persönliche Zwischenablage.

## Standard-Kampagnenlauf

1. `campaign-manager` prüft die Kampagne und meldet die Rest-Limits.
2. `engagement-scout` sammelt Wall + Feed → `team/engagement-scout/collected/`.
3. `content-strategist` plant Ideen (Posts/Kommentare/Reshares) im Rahmen der Limits.
4. `copywriter` schreibt die Texte (Stil aus `memory.md`).
5. `art-director` erzeugt bei Bedarf ein Bild.
6. `reviewer` prüft strikt; nur Freigegebenes geht weiter.
7. `operator` veröffentlicht — nur nach Freigabe.

## Jobs, Freigaben und automatische Planung

Die Weboberfläche startet mit `./bin/li-ui`. Im Tab **Jobs** lassen sich
wiederkehrende Aufgaben mit einem Zeitplan in Alltagssprache anlegen, zum
Beispiel `jeden Tag um 15 Uhr`, `alle 30 Minuten`, `werktags um 09:00` oder
`montags und mittwochs um 15:30`.

- Der Schalter **Aktiv** entscheidet, ob ein Job vom Scheduler berücksichtigt wird.
- Die einmalige Schaltfläche **Automatik aktivieren** installiert den gemeinsamen
  System-Cron-Takt. Danach prüft `li-scheduler` alle fünf Minuten alle UI-Jobs.
- Im Tab **Freigaben** verschiebt **Freigeben** den bearbeiteten Inhalt direkt in
  **Planung**. Ohne manuell gewählten Termin wird automatisch der nächste freie
  Kampagnen-Slot vergeben.
- Jede Freigabekarte besitzt eine optionale **Notiz fürs Lernen**. Sie verändert
  den LinkedIn-Text nicht. Bei **Freigeben** wird sie als bestätigtes positives
  Nutzersignal, bei **Ablehnen & lernen** als negatives Signal in
  `team/style/learning.json` gespeichert und künftig zusammen mit Kampagne,
  Memory und Beispielen in Codex-Prompts injiziert.
- Oben im Tab **Freigaben** kann eine absolute Score-Schwelle gewählt werden.
  Die Grenzen 70, 75, 80, 85, 90 und 95 Prozent sind als Toggle-Buttons verfügbar.
  **Passende automatisch freigeben** verschiebt alle Entwürfe ab dem gewählten Score in
  die Planung. Automatische Freigaben werden nur Montag bis Freitag und höchstens
  viermal pro Tag eingeplant. Ein dauerhafter Counter zeigt die bisherigen
  Auto-Freigaben. Manuelle Freigaben bleiben davon unberührt und dürfen auch am
  Wochenende oder zusätzlich zu diesen vier Slots geplant werden.
- Pro Content-Job bleibt die Freigabe zunächst manuell. Nach zehn Entwürfen dieses
  Jobs, die nacheinander ohne Textänderung manuell freigegeben wurden, kann im
  Jobs-Tab eine Auto-Freigabe für die historischen oberen 20, 15, 10 oder 5 Prozent
  der Scores per Toggle gewählt werden. Neben dem aktiven Toggle stehen die daraus
  berechnete Mindest-Score-Grenze und die Zahl der bisherigen Auto-Freigaben dieses
  Jobs. Sie gilt nur für neue Entwürfe dieses Jobs und verschiebt sie in **Planung**;
  sie veröffentlicht nicht sofort.
- Erst der aktive Job **Fällige veröffentlichen** publiziert eingeplante Inhalte,
  sobald deren Zeitpunkt erreicht ist.
- Vernetzungskandidaten werden nach Rollen- und Zielgruppenpassung sortiert. Sie
  können nie automatisch freigegeben werden. Erst eine manuelle Freigabe plant die
  Anfrage; beim Versand wird erneut geprüft, ob „Vernetzen“ noch verfügbar ist.
  Notizen sind Pflicht, maximal 300 Zeichen lang, und es werden höchstens fünf
  Vernetzungsanfragen pro Tag ausgeführt.

## Ideen und persönliches Profil

Im Tab **Ideen** können Stichpunkte oder fertige Rohtexte gesammelt werden. Eine
Kampagne ist optional: mit Zuordnung gelten deren Zielgruppe, Themen, CTA und
Grenzen; ohne Zuordnung entsteht ein persönlicher LinkedIn-Post ohne Produkt- oder
Kampagnenfilter. **Offene Ideen zu Posts (Codex)** kann als wiederkehrender Job
angelegt oder direkt im Ideen-Tab gestartet werden. Das Ergebnis durchläuft
Evaluator und Planer und landet immer zuerst unter **Freigaben**.

Der Tab **Konfiguration** enthält das persönliche Profil/CV des Account-Inhabers.
Rolle, Unternehmen, Kurzprofil, belegbare Erfahrung, Fachgebiete und persönliche
Perspektiven werden bei allen künftigen Posts und Kommentaren berücksichtigt.
Im selben Tab lassen sich die Zeitlimits für Post-, Kommentar-, Reshare-, Ideen-,
Rewrite- und Bildläufe in Minuten ändern. Sie stehen dauerhaft in
`config/timeouts.yaml`. Beim Ideen-Job gilt das sichtbare Limit pro Idee; die
Weboberfläche und der Scheduler berechnen für mehrere Ideen sowie eine mögliche
Stilüberarbeitung automatisch ein größeres Gesamtlimit.

## Bildgenerierung

`IMAGE_PROVIDER=none` (Standard) schreibt nur einen Bild-Brief als `.txt` nach
`.runs/images/`. Mit `IMAGE_PROVIDER=openai` + `OPENAI_API_KEY` werden echte Bilder
über die OpenAI Images API gerendert und beim Posten angehängt. Bei jedem neuen
eigenen Post wird `images.ratio` der Kampagne automatisch und stabil angewendet;
bei `0.5` kommt beispielsweise jeder zweite Post infrage. Automatisch gerendert
wird nur, wenn der sichtbare Evaluator-Score zusätzlich strikt über `0.85` liegt.
Der automatisch gebaute Prompt enthält den vollständigen finalen Posttext und
`images.style`; Schrift, Logos und Wasserzeichen im Motiv sind verboten.

Im Tab **Freigaben** gehört das Bild zur gemeinsamen Freigabe von Text und Motiv.
Dort kann pro Post ein KI-Bild erzeugt oder ersetzt, ein lizenzierbares Webbild
gesucht, ein eigenes PNG/JPEG hochgeladen oder das Bild entfernt werden. Nur bei
Webbildern wird die gespeicherte Quellenangabe automatisch an den LinkedIn-Text
angehängt. Kommentare und Reshares erhalten kein separates Bild.

## Kampagnen-Auswertung

Jede erfolgreich veröffentlichte Aktion wird zusätzlich dauerhaft in
`Kampagnen/<name>/queue/analytics.yaml` registriert. Gespeichert werden Kampagne,
Inhaltstyp, tatsächlicher Veröffentlichungszeitpunkt, Original-URL bei Kommentaren
und Reshares sowie der eigene LinkedIn-Permalink, sobald er gefunden wurde. Auch
ältere Einträge aus `log.md` werden automatisch in diese Ablage übernommen.

Der Tab **Auswertung** zeigt Posts, Kommentare, Reshares, Likes/Reaktionen,
Kommentare beziehungsweise Antworten, Reposts und sichtbare Impressionen. Mit
**Kennzahlen jetzt aktualisieren** wird LinkedIn erneut abgefragt und ein weiterer
Messpunkt gespeichert. Derselbe Lauf kann im Tab **Jobs** als
**Kampagnenzahlen aktualisieren** wiederkehrend geplant werden. Bei Kommentaren
wird nur der eigene Kommentar gemessen; Kennzahlen des fremden Originalposts
werden nicht als eigener Kampagnenerfolg summiert.

Der Tab **Historie** besitzt ebenfalls einen Monatskalender. Er verwendet bevorzugt
den tatsächlichen Veröffentlichungszeitpunkt und lässt sich auf einen einzelnen Tag
filtern.

## Kampagne

`Kampagnen/example_campaign.yaml` ist die Vorlage und die einzige Quelle der Wahrheit:
Ziel, Zielgruppe, Tonalität, erlaubte/verbotene Themen, Keywords, Hashtags, CTA,
Zeichenlimits, `limits`, `images`, `schedule`.

Im Tab **Kampagnen** kann jede Kampagne als YAML exportiert und eine YAML-Datei als
neue Kampagne importiert werden. Jeder Speichervorgang erhöht `version`; unveränderliche
Stände liegen unter `Kampagnen/<name>/versions/vNNNN.yaml`. Entwürfe, Planung und
Historie zeigen die Kampagnenversion, mit der der Inhalt erstellt wurde. Gleichzeitige
Bearbeitung mit einer veralteten Formularversion wird abgelehnt, statt Änderungen zu
überschreiben.

## Portabler Docker-Betrieb

Die vollständige Anleitung für Umzug, `.env`, OpenAI-Key, LinkedIn-Browser,
Windows/macOS und Autostart steht in **[INSTALLATION.md](INSTALLATION.md)**.

Auf dem Zielrechner Docker Desktop installieren, diesen Projektordner kopieren und
`.env` anlegen. Chrome muss mit einem eigenen LinkedIn-Profil und einem für Docker
erreichbaren Debug-Port laufen:

```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --remote-debugging-address=0.0.0.0 \
  --user-data-dir="$HOME/chrome-linkedin"
```

Danach einmal in diesem Browserfenster bei LinkedIn anmelden und den Stack starten:

```bash
docker compose up --build -d
docker compose logs -f app
```

Die Oberfläche läuft auf `http://127.0.0.1:8765`. Der zweite Container `scheduler`
prüft aktive Jobs jede Minute; ein Betriebssystem-Cronjob ist im Docker-Betrieb nicht
nötig. Kampagnen, Queues, Lernhistorie, Ideen, Bilder und Jobdefinitionen bleiben als
normale, lesbare Dateien in `Kampagnen/`, `team/`, `ideas/`, `automation/`, `config/`
und `.runs/` auf dem Host erhalten. Diese Ordner sind in beide Container gemountet;
sie liegen nicht im Container-Dateisystem. `OPENAI_API_KEY` wird über `.env` zur Laufzeit geladen
und nicht in das Image kopiert. Der CDP-Port 9222 darf nicht im Netzwerk oder Internet
freigegeben werden. Auf demselben Rechner nicht gleichzeitig den Docker-Scheduler und
einen bereits installierten Host-Cronjob für `li-scheduler` laufen lassen.

## Hinweise

- **Nichts wird ohne Freigabe veröffentlicht.** Standard ist manuell; eine
  Auto-Freigabe muss nach der Vertrauensphase ausdrücklich pro Job aktiviert werden.
- LinkedIn-Selektoren ändern sich häufig; ggf. `src/linkedin_agents/browser/linkedin.py` anpassen.
- LinkedIn-Nutzungsbedingungen beachten, konservative Frequenzen.
