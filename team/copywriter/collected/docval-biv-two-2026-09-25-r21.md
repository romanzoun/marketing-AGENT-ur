# CW-DV-NP-20260925-R21 — zwei finale LinkedIn-Posttexte

Hashbasis: UTF-8-Bytes des reinen Texts im jeweiligen `text`-Block, ohne abschliessenden Zeilenumbruch.

## Post 1 — Die Prüfentscheidung braucht eine Versionsnummer

```text
Die Prüfentscheidung braucht eine Versionsnummer.

Ein Fahrplan sagt mir nicht nur, wann der Zug fährt. Ich muss auch wissen, welcher Fahrplan gilt. Sonst war 09:12 vielleicht gestern noch richtig und heute nur noch sportlich.

Bei eingehenden signierten PDFs ist es ähnlich: Derselbe technische Befund kann je nach Dokumentart, internem Regelset und Prozessschritt anders weiterbehandelt werden.

Darum würde ich neben den Prüfinformationen im eigenen Records-/ECM-Prozess festhalten:

- welches Regelset oder Prozessschema angewendet wurde
- in welcher Version
- zu welchem Entscheidungszeitpunkt

Der Swisscom Document Validator prüft bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Die Prüfinformationen kommen vom Validator. Welche interne Regel gilt und wie entschieden wird, bestimmt die Organisation.

Kann euer Team später noch sagen, nach welcher Regelversion es entschieden hat?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice

Für eine kurze Demo oder einen Austausch:
DM oder Kommentar.

#eIDAS #RecordsManagement
```

- Unicode-Codepoints: `1266`
- SHA-256: `1d6900030293edc4017166bbbc7896d8e6c76f06a65411fb43f7bb4ab37d7d3d`
- Fakten-/Grenzencheck: Der Document Validator wird ausschliesslich mit der Prüfung von Signatur- und Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs, dem Verbleib der PDF in der eigenen Umgebung und der lokalen Hash-Bildung beschrieben. Regelset, Prozessschema, Version und Entscheidung sind ausdrücklich organisationsseitig; keine automatische Policy-, Rechts-, Freigabe-, Archivierungs- oder Revisionsfunktion wird behauptet. Keine Biografie, Kundensituation, Statistik oder Garantie erfunden; kein BIV-Bezug.
- Konkrete Dublettenabgrenzung: Der Text behandelt weder die Zuordnung eines Prüfergebnisses zur geprüften PDF-Version noch allgemeine Audit-Rückschau oder die Zwei-Status-Trennung. Sein eigener Funktionskern ist die zum Entscheidungszeitpunkt angewendete **Version des internen Regelsets/Prozessschemas**, durch die derselbe technische Befund je nach Dokumentart und Prozess anders weiterbehandelt werden kann. Dieser Kern ist in den Posttexten beider Queues und den relevanten Entwürfen nicht belegt; der Ausgangswinkel wurde daher nicht ersetzt.

## Post 2 — Ein Stapel bekommt keinen Sammelhaken

```text
Ein Stapel bekommt keinen Sammelhaken.

Ein Gesamtstatus für einen PDF-Stapel wäre wie ein Lieferschein ohne Positionsnummern: «Alles da» klingt gut. Bis jemand wissen will, welche Kiste gemeint war.

Wenn der Records-/ECM-Prozess mehrere signierte PDFs automatisiert zur Prüfung führt, muss das Ergebnis pro Datei zuordenbar bleiben.

Ich würde deshalb pro Dokument zusammenhalten:

- die eindeutige Dateireferenz
- die zugehörigen Signatur- und Zertifikatsinformationen
- die zugehörige Prozessentscheidung

Erst danach darf eine Übersicht zusammenfassen. Sonst verdeckt der Sammelhaken die Information, die beim einzelnen Dokument gebraucht wird.

Der Swisscom Document Validator prüft bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Die dokumentweise Korrelation ist dabei eine Aufgabe des eigenen Records-/ECM-Prozesses.

Zeigt eure Übersicht nur «alles geprüft» – oder welches Ergebnis zu welcher PDF gehört?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice

Für eine kurze Demo oder einen Austausch:
DM oder Kommentar.

#eIDAS #RecordsManagement
```

- Unicode-Codepoints: `1291`
- SHA-256: `fcf81add3e41f4f517e18f120a96efeeac9da62b4d5a3364fe56ed149557d4f6`
- Fakten-/Grenzencheck: Die automatisierte Zuführung mehrerer Dateien und die dokumentweise Korrelation sind ausdrücklich Anforderungen an den eigenen Records-/ECM-Prozess; keine Batch-, Sammelstatus-, Mapping-, Archivierungs- oder Workflowfunktion des Produkts wird behauptet. Der Document Validator wird nur mit den belegten Signatur-/Zertifikatsinformationen, dem Verbleib der PDF in der eigenen Umgebung und lokaler Hash-Bildung beschrieben. Keine Rechts-, Sicherheits- oder Revisionsgarantie, keine Biografie, Kundensituation oder Statistik; kein BIV-Bezug.
- Konkrete Dublettenabgrenzung: Anders als der bestehende Mehrfachsignatur-Post ordnet dieser Text nicht mehrere Unterschriften innerhalb einer PDF einzeln zu, sondern die Prüfinformationen mehrerer **verschiedener Dateien** im eigenen Volumenprozess. Er behandelt auch nicht Urlaubsvertretung, allgemeine Volumenschwelle/Routine, Browser-/API-Parität, Testsets, Dokumentversionierung oder eine allgemeine Statuslogik. Der dokumentweise Korrelationskern ist in den Posttexten beider Queues und den relevanten Entwürfen nicht belegt; der Ausgangswinkel wurde daher nicht ersetzt.
