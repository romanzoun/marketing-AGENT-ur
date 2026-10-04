# AGENTS.md — Betriebshandbuch des Marketing-Teams

Dieses Team managt LinkedIn-Kampagnen über die Codex CLI. Es besteht aus
spezialisierten **Custom Agents** (`.codex/agents/*.toml`). Der
**Orchestrator** koordiniert; jeder Agent hat eine eigene Ablage, ein Gedächtnis
(v. a. Schreibstil), eine Todo-Liste und einen Ein-/Ausgang für Delegation.

Alle textenden und bewertenden Agenten lesen außerdem
`config/personal_profile.yaml`. Dort stehen Rolle, Unternehmen, CV, Expertise und
persönliche Perspektiven; nicht belegte biografische Angaben dürfen nie erfunden werden.

## Das Team

| Agent | Rolle | Ordner |
|-------|-------|--------|
| `orchestrator` | Plant die Kampagne, entscheidet was posten/replyen/teilen, delegiert Todos | `team/orchestrator/` |
| `campaign-manager` | Lädt/prüft Kampagne, wacht über Limits & Guardrails | `team/campaign-manager/` |
| `engagement-scout` | Sammelt Beiträge von der eigenen Wall und aus dem Feed | `team/engagement-scout/` |
| `content-strategist` | Entwickelt Content-Ideen (Posts, Kommentare, Reshares) | `team/content-strategist/` |
| `copywriter` | Schreibt finale Texte in der Markenstimme | `team/copywriter/` |
| `art-director` | Entwirft Bild-Prompts und rendert Bilder | `team/art-director/` |
| `style-evaluator` | Prüft persönlichen Touch/Stimme und lernt den Stil bei jeder Freigabe | `team/style-evaluator/` |
| `reviewer` | Prüft strikt gegen die Kampagne (Freigabe/Ablehnung) | `team/reviewer/` |
| `operator` | Führt Aktionen über die Playwright-Tools aus | `team/operator/` |

## Ablage, Gedächtnis, Todos (pro Agent)

Jeder Agent besitzt unter `team/<agent>/`:

- `memory.md` — dauerhaftes Wissen, v. a. **Schreibstil**, gelernte Muster, Do/Don't.
- `todo.md` — eigene offene Aufgaben (Markdown-Checkliste).
- `inbox.md` — Aufgaben, die **andere** an diesen Agenten delegiert haben.
- `outbox.md` — Aufgaben, die dieser Agent an **andere** delegiert hat.
- `collected/` — gesammelte/erzeugte Artefakte (z. B. Feed-Dumps, Entwürfe).

Der geteilte Überblick liegt in `team/board.md` (wer macht gerade was).

### Arbeitsprotokoll für jeden Agenten

1. **Start:** Lies `team/board.md`, das eigene `inbox.md`, `todo.md` und `memory.md`.
2. **Arbeiten:** Erledige Aufgaben mit den deterministischen `./bin/li*`-Werkzeugen
   und den Rollenanweisungen aus `.codex/agents/`.
3. **Delegieren:** Um X an Agent `Y` zu geben:
   - hänge einen Eintrag an `team/Y/inbox.md` an,
   - protokolliere ihn in deinem `team/<self>/outbox.md`,
   - aktualisiere `team/board.md`.
4. **Lernen:** Neue Stil-/Prozess-Erkenntnis → in das eigene `memory.md` schreiben.
5. **Abschluss:** Erledigte Punkte in `todo.md`/`inbox.md` abhaken, `board.md` updaten.

### Codex-Delegation

Beim Start einer spezialisierten Rolle aus `.codex/agents/` muss der aufrufende
Agent `fork_turns=none` zusammen mit dem gewünschten `agent_type` verwenden.
Der delegierte Auftrag enthält deshalb Ziel, Kampagnenpfad, Eingabedateien,
Ausgabeformat und Grenzen ausdrücklich. Danach wartet der Auftraggeber auf das
Ergebnis des Subagenten.

### Aufgaben-Format (für inbox/outbox/todo)

```
- [ ] <ID> | von:<agent> → an:<agent> | <kurze Aufgabe> | ctx:<pfad-oder-urn> | prio:<hoch|mittel|niedrig>
```

## Standard-Kampagnenlauf (vom Orchestrator gesteuert)

1. `campaign-manager`: `./bin/li campaign --campaign Kampagnen/<name>.yaml` → Guardrails feststellen.
2. `engagement-scout`: `./bin/li wall ...` und `./bin/li feed ...` → Beiträge nach `team/engagement-scout/collected/`.
3. `content-strategist`: schlägt konkrete Ideen vor (Posts / Kommentare / Reshares) im Rahmen der Limits.
4. `copywriter`: verfasst Texte gemäß `memory.md`-Stil + Kampagne + `team/style/profile.md`.
5. `art-director` (falls `images.enabled`): `./bin/li image --prompt "..." --name <id>`.
6. `style-evaluator`: bewertet persönlichen Touch/Stimme; bei Score < 0.7 zurück an `copywriter`.
7. `reviewer`: prüft jeden Entwurf strikt; nur Freigegebenes geht weiter.
8. `operator`: veröffentlicht via `./bin/li post|comment|reply|reshare` (nur nach Freigabe).

## Stil-Lernkreis (persönlicher Touch über die Zeit)

Das Stilprofil `team/style/profile.md` ist die Quelle der Wahrheit für die
**persönliche Stimme**; `team/style/approved/` ist der Korpus freigegebener Posts.

- **Vor Freigabe:** `style-evaluator` bewertet den Entwurf gegen das Stilprofil und
  liefert konkrete Umschreibungen, damit es nach dem Nutzer klingt.
- **Bei Freigabe durch den Nutzer:** `style-evaluator`
  1. speichert den finalen Text unter `team/style/approved/<YYYY-MM-DD>-<slug>.md`,
  2. destilliert 1–3 neue Stil-Signale in `team/style/profile.md`,
  3. ergänzt eine Changelog-Zeile (Datum + Quelle).

So schärft sich die Stimme mit jedem freigegebenen Post. Direkte Nutzeränderungen
in der Freigabe werden als konkrete Korrekturmuster gespeichert; freigegebene
Texte zählen zusätzlich als besonders starkes Stil-Signal.

## Freigabe- und Planungs-Workflow (`./bin/li-jobs`)

Nichts geht direkt live. Pro Kampagne liegen drei Dateien in `Kampagnen/<x>/queue/`:

`approvals.md` → `schedule.md` → `log.md`

1. **Vorschlagen:** `content-strategist`/`copywriter` legen Entwürfe ab
   (`li-jobs add --kind post --text "..."`), `engagement-scout` sammelt
   Kommentar-Kandidaten (`li-jobs find-comments`) und Reshare-Kandidaten
   (`li-jobs find-reshares`) inkl. Permalink-URL. Reshares können mit
   Begleittext/CTA oder bewusst ohne Text für Awareness freigegeben werden.
   Vernetzungskandidaten werden mit `li-jobs find-connections --query "<Rolle>"`
   gesammelt, nach Zielgruppenpassung bewertet und mit einer persönlichen Notiz
   von höchstens 300 Zeichen vorbereitet. Sie bleiben immer manuell freigabepflichtig.
2. **Bild:** `art-director` setzt ein Bild (`li-jobs image --id <id> --query "..."
   --source web|gen`); bei Web-Bildern wird die **Quelle** mitgespeichert und beim
   Posten automatisch an den Text angehängt.
3. **Evaluieren + vorplanen:** Jeder fertige Text erhält eine geschätzte
   Freigabewahrscheinlichkeit und einen editierbaren Terminvorschlag. Unter 0.70
   wird er anhand von `team/style/learning.json` und den freigegebenen Beispielen
   überarbeitet und erneut bewertet.
4. **Freigabe:** In der Weboberfläche verschiebt **Freigeben** den bearbeiteten
   Inhalt direkt nach `schedule.md` und übernimmt den vorgeschlagenen oder
   manuell geänderten Termin. Nutzeränderungen werden für kommende Texte gelernt.
   Alternativ kreuzt der Nutzer in `approvals.md` `- [x] freigeben` an.
   Nach zehn aufeinanderfolgenden unveränderten manuellen Freigaben desselben Jobs
   kann der Nutzer dort optional Auto-Freigabe für das historische obere
   Score-Perzentil (20/15/10/5 %) aktivieren. Auto-Freigaben zählen nicht selbst
   als Lern- oder Vertrauensfreigaben und verschieben nur nach `schedule.md`.
5. **Einplanen per CLI:** Für die Datei-Variante übernimmt `li-jobs schedule`
   vorhandene Vorschläge; ohne Vorschlag vergibt es mit `--slots 09:00,13:00`
   Termine im Aktivzeitfenster der Kampagne.
6. **Ausführen:** Der Cron-Job `li-jobs run-due` veröffentlicht, was fällig ist,
   und verschiebt es nach `log.md`. Der `operator` nutzt genau diesen Weg.

## Ideen-Inbox

`ideas/ideas.yaml` ist der Eingang für lose Ideen und Rohtexte. Der Job
`ideas-to-posts` verarbeitet offene Ideen einzeln. Mit `campaign` wird der Text
durch diese Kampagnenbrille entwickelt; ohne Kampagne gelten nur persönliches
Profil und Stil, die Ausgabe liegt technisch in `Kampagnen/persoenlich/`. Jeder
erzeugte Text geht durch Evaluator und Planer und anschließend in die Freigabe-Queue.

## Steuerung über Codex CLI

- Interaktiv im Ordner: `codex` → z. B. „Nutze den Agenten orchestrator und starte
  einen Kampagnenlauf für Kampagnen/example_campaign.yaml".
- Headless und für Jobs: `./bin/li-brain --campaign <pfad> <job> --count <n>`.
- `li-brain` startet `codex exec` mit Workspace-Sandbox und den Projekt-Agenten
  aus `.codex/agents/`; wegen `--skip-git-repo-check` ist kein Git-Repository nötig.
- Wiederkehrende Ausführung übernimmt `./bin/li-scheduler` aus dem Jobs-Menü.

## Kampagnen-Schema

Siehe `Kampagnen/example_campaign.yaml`. Relevante Felder: `objective`, `audience`,
`voice`, `topics`, `banned_topics`, `keywords_to_engage`, `required_hashtags`,
`cta`, `max_post_chars`, `max_comment_chars`, `limits`, `images`, `schedule`.
