# CW-DV-NP-20260924-R20 — finale Posttexte

Hashbasis: UTF-8-Bytes des reinen Posttexts im jeweiligen `text`-Block, ohne abschliessenden Zeilenumbruch.

## Post 1 — Eingangsoriginal vor Vorverarbeitung prüfen

```text
Bei einer signierten PDF würde ich nicht zuerst die Möbel umstellen und danach den Grundriss prüfen.

Im Posteingang passiert sinngemäss genau das: Erst OCR, PDF/A-Konvertierung, Stempelung oder eine andere Vorverarbeitung. Danach soll die eingegangene Signatur geprüft werden.

Nur kann die Vorverarbeitung eine andere Datei- oder Bytefassung erzeugen. Das heisst nicht pauschal, dass jede Transformation jede Signatur ungültig macht. Es heisst etwas viel Praktischeres: Der Prozess muss klar benennen, welche Fassung geprüft wird und welche Fassung ins Archiv geht.

Für Records/ECM gehört der technische Prüfschritt für mich deshalb möglichst nah an den Eingang des signierten Originals.

Der Swisscom Document Validator liefert bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Prüft ihr das eingegangene Original – oder eine Fassung, die schon durch die Dokumentenküche gelaufen ist?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice

Für eine kurze Demo oder einen Austausch:
DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement
```

- Unicode-Codepoints: `1275`
- SHA-256: `913db9fa9b695f9b2ebafd3f59e808e0ba137c0f74bd9d4e090c094dc3310d7e`
- Fakten-/Grenzencheck: Enger Records-/ECM-/Posteingang-Bezug; Vorverarbeitung nur als mögliche Änderung der Datei-/Bytefassung beschrieben, ausdrücklich keine pauschale Aussage, dass jede Transformation jede Signatur ungültig macht. Document Validator ausschliesslich mit den belegten Aussagen zu Signatur-/Zertifikatsinformationen, Verbleib der PDF in der eigenen Umgebung und lokaler Hash-Bildung beschrieben. Keine Rechts-, Sicherheits-, Revisions- oder Archivierungsgarantie; kein BIV-Bezug.
- Dublettencheck: Gegen sämtliche Posttexte in Approvals/Schedule/Log beider Kampagnen sowie die relevanten freigegebenen und gesammelten DocVal-Posts geprüft. Keine exakte oder funktionale Dublette: Bestandsbeiträge behandeln den Kontrollpunkt vor Archivierung allgemein, Versionszuordnung oder Prüfinformation versus Records-Entscheid, nicht die konkrete Reihenfolge vor OCR/PDF/A/Stempelung und die Festlegung der geprüften sowie archivierten Fassung.

## Post 2 — Browser und API, eine Prüfsprache

```text
Der Browser ist der Vordereingang. Die API ist die Lieferantentür.

Wenn dahinter zwei verschiedene Wörterbücher liegen, hat Records/ECM trotzdem zwei Prüfprozesse.

Genau das würde ich bei der Abnahme testen: Eine signierte PDF wird einzeln im Browser geprüft. Derselbe definierte Fall kommt über die API in den Workflow. Danach vergleicht das Team nicht nur Farben, sondern:

- Werden Signatur- und Zertifikatsinformationen gleich benannt?
- Bedeutet «geprüft» auf beiden Wegen dasselbe?
- Führt derselbe Fall zur selben vorgesehenen Folgeentscheidung?

Der Swisscom Document Validator prüft bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen und kann in Records-/ECM-Abläufe eingebunden werden. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Für mich ist das die nützliche Abnahmefrage: zwei Eingangstüren, aber eine fachliche Sprache.

Sprechen Browser-Einzelprüfung und API-Workflow bei euch dieselbe Prüfsprache?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice

Für eine kurze Demo oder einen Austausch:
DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement
```

- Unicode-Codepoints: `1256`
- SHA-256: `43caa131bce7c308949cdcad09c46d1f833d68bf43b070b0148ae745e11b38df`
- Fakten-/Grenzencheck: Enger Records-/ECM-Abnahmefall; Browser und API nur als zwei belegte Zugangswege, die gemeinsame Prüfsprache und Folgeentscheidung ausdrücklich als Prozess-/Abnahmekriterium formuliert. Document Validator nur mit belegter Prüfung von Signatur-/Zertifikatsinformationen, Einbindbarkeit in Records-/ECM-Abläufe, Verbleib der PDF in der eigenen Umgebung und lokaler Hash-Bildung beschrieben. Keine Gleichheits-, Sicherheits-, Rechts-, Revisions- oder Freigabegarantie; keine erfundene Produktfunktion und kein BIV-Bezug.
- Dublettencheck: Der ursprünglich vorgegebene Datenfluss-/Beschaffungswinkel ist funktional bereits durch `post-2026-09-13-0002` belegt und wurde deshalb in derselben Copywriter-Runde verworfen. Der Ersatzwinkel ist gegen sämtliche Posttexte in Approvals/Schedule/Log beider Kampagnen sowie relevante freigegebene und gesammelte DocVal-Posts geprüft. Keine exakte oder funktionale Dublette: Anders als API-Kontrollpunkt, Browser-Medienbruch, Urlaubsvertretung und allgemeiner Workflow-Test geht es ausschliesslich um Kanalparität von Begriffen und vorgesehener Folgeentscheidung bei der Abnahme von Browser-Einzelprüfung und API-Workflow.
