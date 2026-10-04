# Abschlussbericht — ES-FC-DV-20260915-R20

## Ergebnis

Der exakt beauftragte Feed-Lauf wurde ausgeführt, beide vollständigen Originalposts wurden semantisch geprüft und nur ein fachlich tragfähiger Kandidat behalten. Nichts wurde freigegeben, angekreuzt, eingeplant oder veröffentlicht.

## Sammlung

- Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Versuch: ausschließlich wegen Sandbox-`EPERM` am lokalen Chrome-CDP-Port ohne Queue-Änderung abgebrochen.
- Identische Wiederholung mit freigegebenem lokalem CDP-Zugriff: erfolgreich.
- CLI-Ergebnis: `ok: true`, `kandidaten: 2`.
- Queue-Diff bestätigte exakt die zwei neuen leeren Rohblöcke 0001 und 0002.
- Beide unveränderten Rohblöcke einschließlich vollständiger `note:` sind in `team/engagement-scout/collected/feed-comment-candidates-2026-09-15-r20.md` gesichert.
- Eine separate URN war bei keinem Treffer vorhanden und wurde nicht erfunden.

## Kandidatenentscheidung

### Verworfen — comment-2026-09-15-0001

- URL: https://lnkd.in/p/eGBW3aTx
- Autor: Joerg Lenz
- Status: **UNPASSEND**
- Grund: Der eID/eIDAS-Treffer stammt aus einer politisch-historischen Keynote-Zusammenfassung über Ministerin, sowjetische Besatzung, Freiheit, Staat und internationale Governance. Das berührt das No-Go Politik. Zudem fehlen eingehende signierte PDFs, Zertifikatsprüfung vor Archiv/Freigabe, Records-/ECM-Ablauf, lokaler Datenfluss und enger ICP. Eine Kampagnenbrücke wäre konstruiert.
- Folge: ausschließlich der durch diesen Lauf neu erzeugte Queue-Block wurde entfernt; ID, URL und vollständiger Originalpost bleiben unverändert im Sammelartefakt dokumentiert.

### Behalten — comment-2026-09-15-0002

- URL: https://lnkd.in/p/eMEnq-m7
- Autor: Lissi GmbH
- Scout-Vorprüfung: passend als fachlich angrenzender Anlass.
- Content-Stratege: **BEDINGT PASSEND**, Zielsprache Englisch.
- Tragfähige Anker: eIDAS 2.0, Wallet-to-Verifier-Kommunikation, Lifecycle von Access-/Registration-Zertifikaten, wiederholbare Produktionstests und die Differenz zwischen formaler Standardkonformität und praktisch nachvollziehbarer Verifikation.
- Grenze: kein künstlicher DocVal-/BIV-, PDF-, Archiv-, ECM-, lokaler-Hash- oder Produktpitch; keine Wettbewerberabwertung.

## Finaler Kommentar

> “Standards-compliant on paper” is exactly where the easy part ends for me. The real test is whether certificate lifecycles and verification flows can be rerun, traced and explained when national implementations keep moving. Otherwise, interoperability is a railway map with thirty slightly different track gauges. #Compliance #eIDAS #RecordsManagement

- Sprache/Sätze: Englisch, 3 Sätze
- Unicode-Codepoints: 351 von maximal 500
- UTF-8-Bytes: 355
- SHA-256: `9da70bb953b862f3f9bcfaad645d5882900ebdbfd9cf848fd4def6a9b63d9145`
- Links: 0
- Pflicht-Hashtags: `#Compliance`, `#eIDAS`, `#RecordsManagement` jeweils exakt einmal
- Produktnennung/Werbung: keine
- Erfundene biografische oder fachliche Fakten: keine

## Agentenprüfungen

- Content-Stratege: **BEDINGT PASSEND**; organischer Awareness-Kommentar nur innerhalb der oben genannten Grenze.
- Copywriter: exakter hashgebundener Textstand erstellt.
- Style-Evaluator, Iteration 1: **0,95 — BESTANDEN**; keine Pflichtrevision, daher keine zweite Copywriter-Runde.
- Reviewer: **FREIGEGEBEN**, keine Pflichtänderung; Limit, Hashtags, Zielpostbezug, Fakten, Sprache, Stimme, CTA-/Link-Ausnahme, Banned Topics, Wettbewerb, Spam und Brand-Safety bestanden.
- Reviewer-Freigabe ist ausdrücklich keine Nutzerfreigabe.

## Queue-Race und finaler Zustand

Zwei unmittelbar ID-/URL-/Note-/Leertext-gebundene Copywriter-Patches änderten nachweislich nur die `text:`-Zeile, wurden aber um 23:56:01 und 23:58:27 durch einen parallelen Queue-Writer mitsamt dem Block entfernt. Es entstand dabei kein neuer Rejection-/Nutzerablehnungs-Eintrag für diesen Kandidaten. Cron meldete um 23:55:01 keinen fälligen Job; die gleichzeitig sichtbare fremde Anlage von `job-0007` wurde nicht verändert.

Nach Stil- und Reviewerprüfung wurde ausschließlich der unverändert gesicherte Rohblock 0002 einmalig mit dem exakt geprüften Text wiederhergestellt. Abschließende Kontrolle:

- `approvals.md`: genau der ID-/URL-gebundene Kandidat 0002 mit obigem Text
- Checkbox: `- [ ] freigeben`
- `publish_at`, `published_at`, `published_url`, `approval_origin`: `null`
- `generated_text`, `evaluation_score`, `evaluated_at`: `null`
- Original-`note:`, ID, URL, Autor und `source_job_id`: unverändert
- Queue-Datei SHA-256: `ca6ae45a5dddd7f25729d8b429ee4c92a82c1132c675186ed46bf0a9a5adad44`
- Stabilitätskontrolle nach finalem Restore: 45 Sekunden ohne erneuten Rewrite
- Kandidaten-ID und URL fehlen in `schedule.md` und `log.md`
- Verworfenes URL-Ziel 0001 fehlt in approvals/schedule/log

## Geänderte R20-Dateien

- `Kampagnen/document validator/queue/approvals.md`
- `team/engagement-scout/collected/feed-comment-candidates-2026-09-15-r20.md`
- `team/engagement-scout/collected/ES-FC-DV-20260915-R20-final-report.md`
- `team/engagement-scout/inbox.md`
- `team/engagement-scout/todo.md`
- `team/engagement-scout/outbox.md`
- `team/engagement-scout/memory.md`
- `team/content-strategist/collected/comment-candidates-2026-09-15-r20.md`
- `team/content-strategist/inbox.md`
- `team/content-strategist/outbox.md`
- `team/copywriter/collected/document-validator-comments-2026-09-15-r20.md`
- `team/copywriter/inbox.md`
- `team/copywriter/todo.md`
- `team/copywriter/outbox.md`
- `team/style-evaluator/collected/SE-FC-DV-20260915-R20-review.md`
- `team/style-evaluator/inbox.md`
- `team/reviewer/collected/RV-FC-DV-20260915-R20-review.md`
- `team/reviewer/inbox.md`
- `team/board.md`

Keine Änderung an `schedule.md`, `log.md`, Stilprofil, `learning.json` oder Approved-Korpus durch den R20-Agentenlauf.
