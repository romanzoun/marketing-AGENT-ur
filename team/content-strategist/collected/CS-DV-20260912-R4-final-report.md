# Abschlussbericht CS-DV-20260912-R4

Kampagne: `Kampagnen/document validator/kampagne.yaml`

## Ergebnis

- Exakt zwei neue, klar getrennte Post-Ideen entwickelt und durch die Pflichtkette geführt.
- Copywriter-Endtexte: 1.233 / 1.278 Unicode-Zeichen.
- Style-Evaluator: POST 1 `0,91 — BESTANDEN`; POST 2 `0,87 — BESTANDEN`; keine Revision erforderlich.
- Reviewer: beide `FREIGEGEBEN`; keine Pflichtänderungen.
- Queue-Postbestand unmittelbar vor den Adds: 4.
- Queue-Postbestand nach beiden einzelnen Adds: 6.
- Verifiziertes Delta: exakt `+2` neue Post-Einträge.
- Neue IDs: `post-2026-09-12-0003`, `post-2026-09-12-0004`.
- Beide neuen Freigabe-Checkboxen sind leer. Die IDs stehen weder in `schedule.md` noch in `log.md`; deren SHA-256-Werte blieben über die Queue-Aktion unverändert.

## Finaltext 1 — Style 0,91 — Reviewer FREIGEGEBEN

Ein unversehrtes Paketsiegel beruhigt. Nur: Es sagt nicht, ob der Absender fürs Unternehmen überhaupt bestellen durfte.

Bei signierten PDFs ist es ähnlich: Der Klebestreifen kann tadellos sein, und trotzdem fehlt die geschäftliche Einordnung.

Ich würde im Records-/Posteingang, in der Vertragsadministration oder in Compliance Ops deshalb zwei Fragen sauber trennen:

1. Ist die ZertES-/eIDAS-Signatur technisch belastbar geprüft?
2. Wer hat für welches Unternehmen gezeichnet – und welche Berechtigungsinformationen liegen vor?

Der Swisscom Document Validator prüft die Signatur und wertet Zertifikatsinformationen belastbarer aus. Der Business Identity Validator ergänzt Kontext zu Zeichner, Unternehmen und Berechtigung.

Das sind zwei Produktrollen, nicht ein Zauberstempel. Sie liefern Prüfinformationen. Die rechtliche Würdigung und die Freigabe bleiben beim zuständigen Team.

Prüft euer Prozess nur das Siegel – oder auch, wer dahintersteht?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement

Queue-Nachweis: einzelner `li-jobs add`-Aufruf meldete `ok: true`, `added: post-2026-09-12-0003`, interne Evaluation `0.83`, Vorschlag `2026-09-13T16:00`; keine Nutzerfreigabe.

## Finaltext 2 — Style 0,87 — Reviewer FREIGEGEBEN

Ein grüner Haken im Nebel ist wie eine Ampel, von der ich nur die Farbe sehe. Beruhigend? Ja. Genug für eine belastbare Entscheidung? Eher nicht.

Für Records-Teams, Vertragsadministration und Compliance Ops mit regelmässig eingehenden signierten PDFs steckt die Arbeit hinter dem Haken:

- Welche ZertES-/eIDAS-Signatur wurde geprüft?
- Welche Zertifikatsinformationen tragen das Ergebnis?
- Was muss dokumentiert sein, damit die Entscheidung Monate später nachvollziehbar bleibt?

Der Swisscom Document Validator prüft die Signatur und wertet Zertifikatsinformationen belastbarer aus. Die PDF bleibt in der eigenen Umgebung; lokal wird ihr Hash gebildet.

Ich mag dieses Bild: Der Haken ist der Wegweiser, nicht das Ziel. Das Prüfergebnis unterstützt den Prozess, ersetzt aber weder die rechtliche Würdigung noch die menschliche Freigabe. Auch Revisionssicherheit entsteht nicht automatisch.

Welche Details müssen bei euch sichtbar bleiben, damit aus dem grünen Licht kein späteres Rätsel wird?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement

Queue-Nachweis: einzelner `li-jobs add`-Aufruf meldete `ok: true`, `added: post-2026-09-12-0004`, interne Evaluation `0.83`, Vorschlag `2026-09-14T09:00`; keine Nutzerfreigabe.

## Sicherheits- und Betriebsnachweis

Keine Freigabe-Checkbox gesetzt, nichts nach `schedule.md` verschoben, kein
`schedule`, `run-due`, `post` oder Operator-Aufruf ausgeführt und nichts auf
LinkedIn veröffentlicht. `posts_per_run: 1` bleibt die operative Grenze für
einen späteren Veröffentlichungszyklus; die zwei neuen Einträge sind nur
ungeprüfte Nutzerfreigabe-Kandidaten in `approvals.md`.

Bei einer nachgelagerten Parallelitätskontrolle wurde kurzzeitig eine exakte
Dubletten-ID `post-2026-09-12-0005` erzeugt, weil die bereits vorhandene
YAML-Darstellung den Text umgebrochen hatte. Ausschliesslich dieser leere,
ungeprüfte Dublettenblock wurde wieder aus `approvals.md` entfernt; eine
Sicherung des Zustands vor der Korrektur liegt unter
`/private/tmp/document-validator-approvals-before-remove-0005-20260912-1530.md`.
Die finale semantische Prüfung bestätigt genau je einen Treffer der beiden
freigegebenen Texte unter `0003` und `0004`, sechs Posts insgesamt (Ausgang vier,
Delta exakt zwei) und null gesetzte Freigabe-Checkboxen.
