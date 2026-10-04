# Agent-Anweisungen: LinkedIn-Marketing-Team

Dieses Repository wird über **GitHub Copilot CLI oder Codex CLI** gesteuert.
`li-brain` bevorzugt Copilot und nutzt Codex automatisch als Fallback. Python
liefert nur deterministische Werkzeuge.

## Grundregeln (immer gültig)

- Die **Kampagne** in `Kampagnen/<name>.yaml` ist die einzige Quelle der Wahrheit.
  Halte dich **strikt** an Ziel, Zielgruppe, Tonalität, erlaubte/verbotene Themen,
  Pflicht-Hashtags, CTA, Zeichenlimits und Mengen-Limits.
- **Nichts wird ohne Freigabe veröffentlicht.** Standard ist ein Vorschlag/Entwurf.
  Erst auf ausdrückliche Anweisung (oder `--allow-all-tools` im Headless-Betrieb)
  darf der Operator live posten/kommentieren/teilen.
- Vernetzungsanfragen benötigen immer eine einzelne manuelle Freigabe, eine persönliche
  Notiz mit höchstens 300 Zeichen und bleiben auf maximal fünf Sendungen pro Tag begrenzt.
- Respektiere die LinkedIn-Nutzungsbedingungen. Konservative Frequenzen, keine
  Spam-Muster, keine automatisierte Massenaktion.
- Kein Erfinden von Fakten. Wenn Kontext fehlt, sammle ihn erst mit den Tools.
- **Persönlicher Touch:** Texte sollen nach dem Nutzer klingen. Das gelernte
  Stilprofil `team/style/profile.md` ist dafür maßgeblich; der `style-evaluator`
  aktualisiert es bei jeder Freigabe (nur aus freigegebenen Posts lernen).

## Werkzeuge (deterministisch, JSON-Ausgabe)

Alle Aktionen laufen über das Python-Tool. Wrapper: `./bin/li <command> ...`.

| Zweck | Befehl |
|-------|--------|
| Eigene Wall/Aktivität sammeln | `./bin/li wall --keywords <a,b> --limit 10` |
| Feed sammeln | `./bin/li feed --keywords <a,b> --limit 15` |
| Beitrag posten | `./bin/li post --text "..." [--image PFAD]` |
| Kommentieren | `./bin/li comment --post-id <urn> --text "..."` |
| Auf Kommentar antworten | `./bin/li reply --post-id <urn> --text "..."` |
| Beitrag teilen | `./bin/li reshare --post-id <urn> [--thoughts "..."]` |
| Vernetzungskandidaten suchen | `./bin/li-jobs --campaign <pfad> find-connections --query "<rolle>" --limit 5` |
| Bild generieren | `./bin/li image --prompt "..." --name post_1` |
| Kampagne prüfen | `./bin/li campaign --campaign Kampagnen/<name>.yaml` |
| Session prüfen | `./bin/li check` |

Voraussetzung: Chrome läuft mit `--remote-debugging-port=9222` und ist bei
LinkedIn eingeloggt (siehe `README.md`). Zum reinen Entwerfen ohne Veröffentlichen
`--dry-run` an Schreibbefehle anhängen.

@AGENTS.md
