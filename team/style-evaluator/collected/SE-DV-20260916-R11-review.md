# SE-DV-20260916-R11 — eine reguläre Stilrunde

Bewertungsgrundlage: `config/personal_profile.yaml`, `team/style/profile.md`,
der vollständige Stand von `team/style/learning.json`, alle freigegebenen
Beispiele unter `team/style/approved/`, die Kampagne sowie die aktuellen
Kampagnenwinkel. Schwelle: **BESTANDEN ab 0,70**, darunter **NICHT BESTANDEN**
mit Pflichtrevision.

Die Hashbindung bezieht sich jeweils auf den unveränderten exakten Text zwischen
`POST START` und `POST END`, ohne Marker und ohne den trennenden LF direkt vor
dem Endmarker. SHA-256 wurde über die UTF-8-Bytes dieses Texts gebildet.

## POST 1

- Codepoints: **1.093 — bestätigt**
- SHA-256: **`e8d51d4f268729eb5b714cff0d62453fae4dd5f6c462f7be501c85a2c5efa5bc` — bestätigt**
- Score: **0,66**
- Urteil: **NICHT BESTANDEN**

### Begründung

„Pendelstrecke mit Monatsabo“ ist ein starkes, trocken komisches Bild. Die
kurzen Sätze, „Ich würde deshalb nicht schneller klicken“ und die offene
Schlussfrage treffen Romans gesprochene, persönliche Haltung sehr gut. Der
Produktabsatz bleibt konkret und ohne Heilsversprechen oder Marketing-Sprech.

Die Freigabewahrscheinlichkeit fällt dennoch unter die Schwelle, weil der Text
funktional nicht eigenständig genug ist. Sein Kern — aus wiederholten manuellen
Einzelprüfungen wird ab ungefähr zehn Vorgängen ein Prozessproblem; deshalb den
Prüfschritt fest in Records/ECM integrieren, auch per API — ist bereits nahezu
deckungsgleich im freigegebenen LKW-/Werkstor-Post
`2026-09-14-post-2026-09-12-0001.md` enthalten. Download, Prüfung und Rückweg in
den Prozess liegen zusätzlich sehr nah am freigegebenen Browser-/Kontextwechsel-
Post `2026-09-15-post-2026-09-15-0002.md`. Das neue Verkehrsbild allein schafft
keinen neuen funktionalen Kampagnenwinkel.

### Pflichtrevision

Den Monatsabo-Hook nur behalten, wenn der fachliche Kern vollständig von
„Wiederholung wird Prozess + API-Integration“ weggeführt wird. Konkrete
Umschreibung für den Mittelteil:

> Bei signierten PDFs interessiert mich deshalb nicht nur, wie oft jemand
> klickt. Mich interessiert, ob am Ende noch sichtbar ist, welche
> Signatur- und Zertifikatsinformationen geprüft wurden — genau dort, wo danach
> freigegeben oder archiviert wird.
>
> Der Swisscom Document Validator liefert diese Prüfinformationen für
> ZertES-/eIDAS-signierte PDFs. Die PDF bleibt in der eigenen Umgebung, ihr Hash
> wird lokal gebildet.
>
> Wo endet eure Prüfstrecke heute: bei einem Ergebnis im Workflow oder bei
> einer Notiz, die wieder jemand zurücktragen muss?

Damit würde der Text vom bereits freigegebenen Volumen-/API-Winkel auf die
Sichtbarkeit des konkreten Prüfergebnisses am Prozessziel wechseln. Der
Copywriter muss die Gesamtfassung anschließend erneut auf Eigenständigkeit
prüfen lassen.

## POST 2

- Codepoints: **1.079 — bestätigt**
- SHA-256: **`e2f119d685b56c40b97805425761d13601c27b04973c2633f30ad4443928213e` — bestätigt**
- Score: **0,64**
- Urteil: **NICHT BESTANDEN**

### Begründung

„Eine einseitige PDF kann mehr wiegen als ein 300-seitiger Bericht“ und „Im
Bauch von Legal und Security“ sind persönlich, bildhaft und merkfähig. Der
Rhythmus ist kurz und gesprochen; „falscher Türsteher“ bringt ein zweites
Augenzwinkern, ohne albern zu wirken. Auch hier fehlen Buzzwords,
Corporate-Sprech und erfundene Biografie.

Funktional wiederholt der Text jedoch den bereits freigegebenen
Gepäckkontroll-Post `2026-09-15-post-2026-09-15-0001.md`: Dort lautet die
Kernaussage ausdrücklich, dass Dokumentengröße den Prüfprozess nicht bestimmen
soll, sensible Inhalte nicht von Dritten eingesehen werden sollen und die PDF in
der eigenen Umgebung bleibt. Die Fremd-Cloud-Frage überschneidet sich außerdem
mit dem freigegebenen Garderoben-/Datenweg-Post
`2026-09-13-post-2026-09-11-0001.md`. Der neue Gewichtsvergleich ändert damit
die Verpackung, nicht den funktionalen Winkel.

### Pflichtrevision

Den Gewichts-Hook auf geschäftliche Tragweite statt erneut auf Dateigröße plus
Cloud-Datenweg zuspitzen. Konkrete Umschreibung für den Kern:

> Eine Seite kann geschäftlich schwer wiegen, weil nicht nur zählt, ob eine
> Signatur technisch geprüft wurde. Es zählt auch, wer gezeichnet hat und in
> welchem Unternehmenskontext.
>
> Der Swisscom Document Validator liefert bei ZertES-/eIDAS-signierten PDFs
> Signatur- und Zertifikatsinformationen. Der Business Identity Validator kann
> ergänzenden Kontext zu Zeichner, Unternehmen und Berechtigung liefern.
>
> Welche kurze PDF bekommt bei euch heute den längeren Blick: die mit vielen
> Seiten oder die mit der größeren geschäftlichen Tragweite?

So würde aus dem bereits freigegebenen Größen-/Fremd-Cloud-Winkel ein klar
anderer Blick auf technische Signaturprüfung versus geschäftlichen Kontext.
Auch diese revidierte Gesamtfassung muss vor der Freigabe-Queue erneut bewertet
werden.

## Ergebnis der Runde

| Text | Score | Urteil | Pflichtrevision |
|---|---:|---|---|
| POST 1 | 0,66 | NICHT BESTANDEN | ja |
| POST 2 | 0,64 | NICHT BESTANDEN | ja |

Beide Texte gehen wegen Scores unter 0,70 an den Copywriter zurück. Diese
Stilrunde verändert weder die beiden Ausgangstexte noch Queue, Checkboxen,
Evaluationen, Stil-/Lerndateien oder Freigabebeispiele und setzt keine
Freigabe, Planung oder Veröffentlichung.
