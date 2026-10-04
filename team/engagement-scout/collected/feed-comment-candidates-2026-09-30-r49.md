# Feed-Kommentarkandidaten — 2026-09-30 — R49

## Lauf

- Befehl: `./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-comments --limit 3`
- Erster Aufruf: technisch vor Sammlung mit `BrowserType.connect_over_cdp: connect EPERM ::1:9222` im Workspace-Sandbox abgebrochen.
- Unveränderter Wiederholungsaufruf mit genehmigtem Zugriff auf den lokalen Chrome-CDP-Port: erfolgreich; 3 Feed-Beiträge gesammelt, 1 neuer belastbarer Queue-Kandidat.
- Queue-Datei: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md`
- Keine Checkbox angekreuzt, nichts geplant, verschoben oder veröffentlicht.

## Neue Kandidaten, absteigend nach fit_score

### comment-2026-09-30-0001 — Playable — fit_score 0.0

- Permalink: https://lnkd.in/p/epM_tMcS
- Originalpost: vollständig im unveränderten `note:` des Queue-Blocks gespeichert; beworbene englische Anzeige für ein Lookbook mit 21 Marketing-Gamification-Kampagnen, Game-Typen, Zielgruppen-Incentives und Marketingzielen.
- Fit: `0.0`
- Sperre: beworbene generische Marketing-Gamification-Anzeige mit Lookbook-CTA und Kampagnenbeispielen, ohne Bezug zu signierten PDFs, Signatur-/Zertifikatsprüfung, Identität/Berechtigung, Records/Archiv, Audit, ECM/DMS oder einem konkreten Backoffice-/Browserprozess; damit generischer Digital-Marketing-Post ohne konkreten Kampagnenbezug.
- Text: exakt leer (`text: ''`, 0 Codepoints).
- Status: sichtbar behalten und ungekreuzt. Copywriter bestätigte die Sperre; der Style-Evaluator stellte mangels Text korrekt keinen Style-Score und keine Revision fest; Reviewer urteilte `ABGELEHNT/GESPERRT`. Mangels geeigneten Kandidaten keine Übergabe an content-strategist.

## Folgeprüfungen

- Copywriter: Sperre bestätigt; `text: ''`, 0 Codepoints; Bericht `team/copywriter/collected/CW-FC-DV-20260930-R49-AUDIT-report.md`.
- Style-Evaluator: Score nicht anwendbar/keiner, keine Revision; `evaluation_score: null`; Bericht `team/style-evaluator/collected/SE-FC-DV-20260930-R49-AUDIT-review.md`.
- Reviewer: `ABGELEHNT/GESPERRT`; Bericht `team/reviewer/collected/RV-FC-DV-20260930-R49-review.md`.
- Der Zieljob bleibt mit leerer Checkbox in `approvals.md` und fehlt in `schedule.md` sowie `log.md`.
