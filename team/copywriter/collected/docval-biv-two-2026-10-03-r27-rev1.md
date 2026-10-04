# CW-DV-NP-20261003-R27-REV1 — Pflichtrevision Post 1

Hashbasis: UTF-8-Bytes des reinen Posttexts im jeweiligen `text`-Block, ohne abschliessenden Zeilenumbruch.

## POST 1 — Ein Testsatz mit Staubschicht ist ein Museumsstück

```text
Ein Testsatz mit Staubschicht ist für mich eher Museumsstück als Sicherheitsnetz.

Nach der Einführung bleibt der Posteingang schliesslich nicht stehen. Irgendwann taucht eine neue Dokumentart oder Signaturkonstellation auf, die das Records-/ECM- oder Compliance-Team erst klären muss.

Genau danach wird es interessant: Wer macht aus diesem geklärten Fall einen zulässigen internen Testfall? Und bei welchem nächsten Anlass wird der aktualisierte Testsatz wieder genutzt?

Der konkrete Nutzen ist für mich simpel: Aus einer einmal geklärten Überraschung wird ein künftig wiederholbarer interner Testfall.

Der Swisscom Document Validator prüft ZertES-/eIDAS-signierte PDFs sowie Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.

Welche Fälle in den internen Testsatz gehören und wann er erneut genutzt wird, verantwortet der eigene Prozess. So bleibt der Testsatz Arbeitsmittel statt Ausstellungsstück.

Wer hält euren Testsatz aktuell, wenn im Posteingang etwas Neues auftaucht?
```

- Unicode-Codepoints: `1041`
- SHA-256 (reiner Text): `9a1339b16deeae999b4832b70a815466ee2d211fe5f47c9f28af4a20f63c00cf`
- Dubletten-/Faktengrenze: Materiell neuer Kern ist ausschliesslich der Lebenszyklus des zulässigen internen Testsatzes nach der Einführung: Ein geklärter neuer Fall wird zum künftig wiederholbaren Testfall; der eigene Prozess bestimmt Verantwortlichkeit und nächsten Einsatz. Keine einmalige Abnahme, makellose Demo-PDF, Randfallliste, Übergabeprüfung, Browser-/API-Prüfsprache oder allgemeiner Unhappy-Path-Test. Keine Speicherung, Verwaltung oder automatische erneute Ausführung eines Testsatzes durch den Document Validator behauptet.

## POST 2 — Ein erneuter Eingang ist kein Radiergummi — bereits stilbestanden, bytegenau unverändert

```text
Auf einer Restaurantrechnung kann ich eine falsche Position stornieren.

Was nicht geht: so tun, als sei sie nie auf dem Bon gewesen.

Wenn nach einem unklaren oder abgelehnten Prüffall eine neu signierte PDF eingeht, ist sie für mich deshalb kein Radiergummi.

Im Records-/ECM-Prozess würde ich beide Vorgänge unterscheidbar halten:

- die zuerst eingegangene Dateifassung mit ihrem Prüfereignis
- die damalige Klärung oder Prozessentscheidung
- die neu eingereichte Dateifassung mit ihrem neuen Prüfereignis
- die Beziehung «erneut eingereicht» oder «ersetzt»

Sonst sieht die jüngste Fassung ordentlich aus, während der Weg dorthin still vom Bon verschwindet.

Der Swisscom Document Validator liefert Signatur- und Zertifikatsinformationen. Welche Information zu welcher Dateifassung gehört, wie beide Vorgänge verbunden werden und was danach freigegeben oder archiviert wird, legt der zuständige Prozess fest.

Kann euer Team eine Neueinreichung erkennen, ohne dass die frühere Entscheidung ausradiert wird?
```

- Stilstatus: `0,81 — BESTANDEN`; keine Revision.
- Unicode-Codepoints: `1011`
- SHA-256 (reiner Text): `5f70474088960d8c3af0201675c1e8e75ba5ce9ea46f9b243e43747614644589`
- Bestätigung: bytegenau unverändert gegenüber dem Erstlauf.

## Abschlussprüfung

- Ausschliesslich Post 1 materiell revidiert.
- Post 2 bytegenau unverändert übernommen.
- Keine Queue-, Freigabe-, Planungs-, Stil-, Lern- oder Approved-Änderung; keine Veröffentlichung und kein Folgeagent.
