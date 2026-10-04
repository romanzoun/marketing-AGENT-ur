# CW-DV-NP-20261001-R26 — finale Posttexte

## POST 1 — Das Prüfergebnis muss den Systemwechsel überleben

```text
Ein Kassenbon auf Thermopapier ist beim Kauf wunderbar lesbar.

Jahre später ist er manchmal nur noch ein weisses Andenken. Man weiss: Da stand etwas. Nur leider nicht mehr was.

So möchte ich mit Prüfergebnissen signierter PDFs nicht enden.

Ein grüner Status in der heutigen Oberfläche hilft heute. Nach einem Wechsel von DMS oder Workflow sollte aber weiterhin verständlich sein, welche Signatur- und Zertifikatsinformationen zu genau dieser geprüften PDF gehörten.

Der Swisscom Document Validator liefert Signatur- und Zertifikatsinformationen. Wie diese Informationen im eigenen Records-/ECM-Prozess verständlich mit der geprüften PDF verbunden und bei einer Migration mitgenommen werden, ist Aufgabe der Organisation.

Für mich darf ein Prüfergebnis nicht an der Tapete des heutigen Systems kleben. Sonst bleibt nach dem Umbau vielleicht noch die Farbe im Gedächtnis, aber nicht mehr ihre Bedeutung.

Wären eure Prüfinformationen nach einem DMS-Wechsel noch ohne das alte System verständlich?
```

- Unicode-Codepoints: `999`
- SHA-256 (reiner Text): `db19d8f91fa8a48eb0e52747ce1a66a62e308e63616462d6806e0cb4932a0f2f`

## POST 2 — Der verwendete Identitätskontext braucht einen Zeitpunkt

```text
Eine alte Restaurantrechnung prüfe ich nicht mit der heutigen Speisekarte.

Vielleicht steht das Gericht noch darauf. Vielleicht auch nicht. Beides sagt mir nicht, welcher Preis damals auf der Karte stand.

Bei einer Entscheidung zu einer signierten PDF sehe ich das ähnlich. Wer sie später nachvollzieht, sollte den heute verfügbaren Identitätskontext nicht stillschweigend an die Stelle des damals verwendeten setzen.

Der Swisscom Document Validator liefert Signatur- und Zertifikatsinformationen. Der Business Identity Validator kann Kontext zu Zeichner, Unternehmen und verfügbaren Berechtigungsinformationen ergänzen.

Für mich sollte im eigenen Prozess deshalb sichtbar bleiben, welche verfügbaren Informationen zum Entscheidungszeitpunkt tatsächlich herangezogen wurden. Nicht als Behauptung, der Kontext habe sich verändert. Sondern damit eine frühere Entscheidung auch auf ihrer damaligen Grundlage erklärt wird.

Die heutige Speisekarte kann nützlich sein. Sie ist nur kein Beleg für das Menü von damals.

Ist bei euch später sichtbar, welcher Kontext der damaligen Entscheidung zugrunde lag?
```

- Unicode-Codepoints: `1103`
- SHA-256 (reiner Text): `dbcd5c96df8dd7f97986243cdb97daf526719990385fe7805954a41b45e9fc9f`

## Grenz- und Dublettenprüfung

- Exakt zwei deutsche LinkedIn-Posttexte; keine Hashtags und kein Produktlink.
- Post 1 schreibt dem Document Validator nur Signatur- und Zertifikatsinformationen zu. Verständliche Verknüpfung, Aufbewahrung und Migration liegen ausdrücklich beim eigenen Records-/ECM-Prozess; keine Aussage zu Exportformat, Speicherfunktion, garantierter Langzeitprüfbarkeit oder vollständiger Revisionssicherheit.
- Post 2 beschreibt BIV nur als möglichen Kontext zu Zeichner, Unternehmen und verfügbaren Berechtigungsinformationen. Keine Behauptung zu historischen Daten, unveränderlichen Snapshots, Speicher-/Zeitstempelfunktionen, Kontextänderung oder juristisch garantierter Zeichnungsberechtigung.
- Funktional eigenständig gegenüber allen aktuellen Posts in `approvals.md`, `schedule.md` und `log.md`: Post 1 behandelt allein die Verständlichkeit des Prüfergebnisses über die Lebensdauer der heutigen Oberfläche hinaus; Post 2 allein die zeitliche Bindung des tatsächlich verwendeten Identitätskontexts. Keine Wiederholung von Dokument-/Regelversion, drei Zeitpunkten, Batch-Korrelation, Rollenentscheidung, Namensgleichheit, Kompetenzgrenzen oder fehlender Berechtigungsinformation.
- Keine Queue-, Freigabe-, Planungs-, Bild- oder Veröffentlichungsaktion.
