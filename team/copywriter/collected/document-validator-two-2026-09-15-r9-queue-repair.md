# CW-DV-20260915-R9-QUEUE-REPAIR — Queue-Endtexte

Quelle: tatsächlich gespeicherte `text:`-Werte der Queue-IDs `post-2026-09-15-0001` und `post-2026-09-15-0002` in `Kampagnen/document validator/queue/approvals.md`.

## POST 1 — post-2026-09-15-0001 — minimal repariert

- Unicode-Codepoints: `1120`
- UTF-8-Bytes: `1136`
- Interne LF: `16`
- SHA-256 (exakter Text, UTF-8, ohne zusätzlichen Schluss-LF): `ba66a282cdb923f560bc3eb4a380aa05ed1b3a555d7fc9003d78f35cf6f2d286`

<!-- QUEUE TEXT 1 START -->
`Vertrag_final_SIGNIERT_v7.pdf` klingt schon ziemlich amtlich.

Für mich ist der Dateiname trotzdem ungefähr so beweiskräftig wie ein selbst gemalter Stempel auf einem Reisepass. Hübsch beschriftet ist noch nicht geprüft.

Gerade in Records- oder Vertragsadmin-Teams mit regelmässig eingehenden signierten PDFs darf «ist signiert» nicht das Prüfergebnis sein.

Der Swisscom Document Validator prüft bei ZertES-/eIDAS-signierten PDFs die Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Mit dem Business Identity Validator kommt Kontext zu Zeichner, Unternehmen und Berechtigung hinzu. Die Freigabe, der Archivierungsentscheid und die rechtliche Beurteilung bleiben beim zuständigen Team.

Welche Dateinamen oder Labels gelten bei euch im Alltag noch unbewusst als Prüfnachweis?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement
<!-- QUEUE TEXT 1 END -->

## POST 2 — post-2026-09-15-0002 — byte-identisch zur Queue

- Unicode-Codepoints: `1158`
- UTF-8-Bytes: `1176`
- Interne LF: `14`
- SHA-256 (exakter Text, UTF-8, ohne zusätzlichen Schluss-LF): `2bd48362539c01c396f52557e00359cfa3d83a7b45a982985d26a53673a223d8`

<!-- QUEUE TEXT 2 START -->
Wenn ein Prüfprozess nur funktioniert, weil eine Person das geheime Klopfmuster kennt, ist das für mich kein Prozess. Das ist ein Escape Room mit Ferienplan.

Bei 10+ signierten PDFs im Monat wird spätestens die Urlaubsvertretung zum Realitätstest: Kann sie denselben Prüfschritt vor Freigabe oder Archivierung durchführen? Und dieselben relevanten Prüfinformationen nachvollziehen – ohne auf Zuruf zu arbeiten?

Der Swisscom Document Validator kann als wiederholbarer Prüfbaustein in den Records-/ECM-Workflow eingebunden werden, auch per API. Er prüft bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Das Produkt liefert Prüfinformationen. Zuständigkeit, Ausnahmebehandlung, Freigabe und Rechtsprüfung bleiben beim Team.

Besteht euer heutiger Ablauf den Urlaubsvertretungs-Test?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement
<!-- QUEUE TEXT 2 END -->

## Änderungsnachweis

- POST 1, ausschließlich ein Satz ersetzt:
  - Queue-Ist: `Der Business Identity Validator zusätzlichen Kontext zu Zeichner, Unternehmen und Berechtigung liefern.`
  - Reparatur: `Mit dem Business Identity Validator kommt Kontext zu Zeichner, Unternehmen und Berechtigung hinzu.`
- Die Triggerphrase `kann zusätzlich` kommt in POST 1 nicht vor. Die Produktrolle bleibt fachlich auf Kontext zu Zeichner, Unternehmen und Berechtigung begrenzt.
- POST 2 ist byte-identisch zum geparsten Queue-Text; Queue-SHA-256 und Endtext-SHA-256 sind identisch.
- Beide Texte bleiben unter 1.300 Unicode-Codepoints und enthalten den vollständigen exakten CTA/UTM-Link sowie ausschließlich `#Compliance #eIDAS #RecordsManagement` je genau einmal.
- Keine Queue-, Checkbox-, Schedule-, Operator-, Browser- oder Veröffentlichungsaktion.
