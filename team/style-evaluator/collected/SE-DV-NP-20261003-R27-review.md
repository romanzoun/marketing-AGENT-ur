# SE-DV-NP-20261003-R27 — einmalige Stilbewertung

Bewertet wurden genau einmal und ausschliesslich die beiden unveränderten
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-10-03-r27.md`. Massgeblich waren
Romans persönliches Profil, Stilprofil, der vollständige Lernstand mit den
konkreten Nutzerkorrekturen, die relevanten freigegebenen Postbeispiele, die
vollständige Kampagne und der aktuelle Queue-Bestand. Schwelle:
**BESTANDEN ab 0,70**; darunter ist eine Copywriter-Revision zwingend.

## Identität und Prüfumfang

- Auftrag: `SE-DV-NP-20261003-R27`
- Eingabe: `team/copywriter/collected/docval-biv-two-2026-10-03-r27.md`
- Datei-SHA-256: `ebd09253e9be8d96598401f4198eb48e398918b10df0b87b8eced2e5d1e2defe`
- Bewertete Textstände: exakt zwei unveränderte `text`-Blöcke, je einmal
- Hashbasis: UTF-8-Bytes des reinen Posttexts ohne Marker und ohne
  abschliessenden Zeilenumbruch
- Queue-Abgleich: alle 16 Posts in `approvals.md`, der eine Post in
  `schedule.md` und der eine Post in `log.md`; ergänzend der relevante
  Approved-Korpus

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | NFC | SHA-256 | Text unverändert |
|---|---:|---:|---:|---|---|---|
| Post 1 | 1.028 | 1.041 | 14 | ja | `0b049de685c0ba41716db2195f603b579aac2daadf4f8b3568a42c28f3b92a93` | ja |
| Post 2 | 1.011 | 1.028 | 17 | ja | `5f70474088960d8c3af0201675c1e8e75ba5ce9ea46f9b243e43747614644589` | ja |

Beide Zeichenangaben und Text-Hashes stimmen exakt mit dem Copywriter-Artefakt
überein. Beide Texte liegen unter dem Kampagnenlimit von 1.300
Unicode-Codepoints. Der Style-Evaluator hat keinen Eingabetext verändert.

## Post 1 — Regenschirm / Abnahmetest

- **Score: 0,66**
- **Urteil: NICHT BESTANDEN**
- **Copywriter-Revision zwingend: ja**
- **Exakte Dublette: nein**
- **Funktionale Dublette: ja, zum freigegebenen Rauchmelder-Post**
- **Text-SHA-256:** `0b049de685c0ba41716db2195f603b579aac2daadf4f8b3568a42c28f3b92a93`

Der Text trifft Romans Stimme für sich betrachtet sehr gut. Der
Wohnzimmer-Regenschirm ist sofort verständlich, „Grün rein, grün raus,
Applaus“ setzt ein glaubwürdiges Augenzwinkern, und „So wirkt auf mich“ sowie
„Dabei interessiert mich“ geben dem fachlichen Teil eine persönliche
Ich-Haltung. Die kurzen Fragen, die konkrete Liste und die Schlussfrage ergeben
einen gesprochenen Rhythmus. Es gibt kein Buzzword-Bingo, kein Angstmarketing
und kein steifes Produktlob.

Die geschätzte Freigabewahrscheinlichkeit bleibt trotzdem unter 0,70, weil der
praktische Kern bereits sehr eng im freigegebenen Post
`2026-09-21-post-2026-09-20-0002.md` erzählt wurde. Dort wird ein Rauchmelder
nicht nur mit frischer Zimmerluft und der Prozess nicht nur mit einer
freundlichen Beispiel-PDF getestet; ein datenschutzkonformer Testsatz mit
bekannten Fällen prüft Ergebnisübergabe, Verhalten bei einer nicht erfüllten
Bedingung und menschliche Zuständigkeit. R27 Post 1 ersetzt Rauchmelder durch
Regenschirm und konkretisiert mehrere Signaturen, unklaren Befund sowie
grosse/sensitive Dateien, erzählt funktional aber erneut: keine makellose
Demo-PDF als alleinige Abnahme, repräsentative Randfälle durch den ganzen
Records-/ECM-Ablauf schicken, Übergaben prüfen und Zuständigkeit klären. Auch
die Nähe zum Queue-Post `post-2026-09-24-0002` über Browser-/API-Abnahme und
gleiche Prüfsprache verstärkt die Wiederholung. Die neuen Beispiele sind eine
Nuance, kein ausreichend neuer Funktionskern.

### Zwingende Änderungen für die Copywriter-Revision

1. Nicht nur Regenschirm oder einzelne Testfälle umformulieren. Der gesamte
   Funktionskern „nicht nur perfekte Beispiel-PDF, sondern repräsentative
   Randfälle und den ganzen Ablauf testen“ muss ersetzt werden.
2. Den neuen Text von beiden bereits belegten Testfamilien lösen: weder erneut
   den allgemeinen Rauchmelder-/Unhappy-Path-Prozesstest noch den
   Browser-/API-Prüfsprache-Abgleich erzählen.
3. Einen materiell anderen operativen Nutzen wählen und ihn in einem Satz klar
   benennen, bevor die Metapher gebaut wird. Falls das Abnahmethema erhalten
   bleibt, muss ein bislang unbehandelter einzelner Abnahmepunkt im Zentrum
   stehen; die jetzige Dreierliste plus Übergabe-/Entscheidungsfragen darf nicht
   erneut die Geschichte bilden.
4. Die gelungenen Stilmerkmale erhalten: persönliche Ich-Haltung, eine neue
   bildhafte Pointe, kurze gesprochene Sätze, knapper positiver Produktbezug und
   eine konkrete Schlussfrage. Keine zusätzliche Rechts- oder
   Produktgrenzenliste ergänzen.

Eine konkrete mögliche Neuausrichtung, ohne sie hier in den Entwurf
einzuarbeiten: statt der einmaligen Abnahme den **Lebenszyklus des internen
Testsatzes nach der Einführung** erzählen. Eine neue Leitzeile könnte lauten:
„Ein Testsatz mit Staubschicht ist für mich eher Museumsstück als
Sicherheitsnetz.“ Der operative Kern wäre dann ausschliesslich, wer bei neuen
Dokumentarten oder Signaturkonstellationen den zulässigen Testsatz ergänzt und
wann er erneut durchlaufen wird. Eine passende Schlussfrage wäre: „Wer hält
euren Testsatz aktuell, wenn im Posteingang ein neuer Fall auftaucht?“ Diese
Richtung ist materiell neu; sie darf nicht wieder in die bestehende Geschichte
vom einmaligen Test des gesamten Ablaufs zurückfallen.

Kampagnen- und Faktenbegrenzung sind im vorliegenden Text ansonsten eingehalten:
Die Produktaussagen zu ZertES/eIDAS, Signatur- und Zertifikatsinformationen,
lokaler Hashbildung und PDF in eigener Umgebung sind von der Kampagne gedeckt.
Testauswahl, Klärweg, Übergaben und fachliche Entscheidung werden zutreffend dem
eigenen Prozess zugeordnet. Es werden keine Testfunktion, Kennzahl oder
Unterstützung bestimmter fehlerhafter PDFs behauptet.

## Post 2 — Neueinreichung ist kein Radiergummi

- **Score: 0,81**
- **Urteil: BESTANDEN**
- **Copywriter-Revision zwingend: nein**
- **Exakte Dublette: nein**
- **Funktionale Dublette: nein**
- **Text-SHA-256:** `5f70474088960d8c3af0201675c1e8e75ba5ce9ea46f9b243e43747614644589`

Restaurantrechnung, Storno, Bon und Radiergummi führen ein durchgehendes,
greifbares Bild. Die zwei kurzen Eröffnungssätze sprechen locker; „ist sie für
mich deshalb kein Radiergummi“ setzt eine klare persönliche Haltung. Die Liste
übersetzt das Bild präzise in Dateifassung, Prüfereignis, frühere Entscheidung
und Beziehung zur Neueinreichung. „Ordentlich“, während der Weg „still vom Bon
verschwindet“, bringt das fachliche Risiko mit einem trockenen Augenzwinkern auf
den Punkt. Der Text ist fachlich klar, ohne Marketing-Sprech oder
Heilsversprechen, und die Schlussfrage bleibt einladend statt verkäuferisch.

Die Bildwelt liegt erkennbar nahe am aktuellen Queue-Post
`post-2026-10-01-0002`, der ebenfalls mit einer Restaurantrechnung beginnt.
Das kostet Freigabewahrscheinlichkeit, ist aber keine funktionale Dublette: Der
Bestandspost vergleicht den damals verwendeten Identitätskontext mit einer
heutigen Speisekarte. R27 Post 2 behandelt dagegen die erneute Einreichung
einer neu signierten Dateifassung nach einem unklaren oder abgelehnten Fall und
fordert, frühere Fassung, früheres Prüfereignis, damalige Entscheidung, neue
Fassung und ihre Beziehung unterscheidbar zu halten. Auch die Queue-Posts zu
Dokumentfassung (`post-2026-09-24-0001`), Regelversion
(`post-2026-09-25-0001`), Dateikorrelation (`post-2026-09-25-0002`) und
Klärdatensatz (`post-2026-09-28-0001`) decken diesen Neueinreichungs-
beziehungsweise Nicht-Überschreibungs-Kern nicht ab.

Der Produktabsatz bleibt innerhalb der Faktenbegrenzung: Der Document Validator
liefert Signatur- und Zertifikatsinformationen; Zuordnung, Historie, Verbindung
der Vorgänge sowie Freigabe und Archivierung werden ausdrücklich dem
zuständigen Prozess zugewiesen. Es wird keine Versionierungs-, Speicher-,
Archivierungs- oder Aufbewahrungsfunktion des Produkts und keine konkrete
Aufbewahrungspflicht behauptet. Wegen des Scores über 0,70 ist keine unnötige
Revision zu verlangen.

## Dublettencheck und Ergebnis

Keiner der beiden Text-Hashes kommt als Queue-Text in `approvals.md`,
`schedule.md` oder `log.md` vor. Post 1 ist jedoch funktional zu einem
freigegebenen Bestandsbeitrag doppelt; Post 2 bleibt trotz ähnlicher
Restaurant-Bildwelt funktional eigenständig.

| Text | Score | Urteil | Copywriter-Revision zwingend | Exakte Dublette | Funktionale Dublette |
|---|---:|---|---|---|---|
| Post 1 | **0,66** | **NICHT BESTANDEN** | **ja** | nein | ja |
| Post 2 | **0,81** | **BESTANDEN** | nein | nein | nein |

Damit geht ausschliesslich Post 1 an den Copywriter zurück und muss nach einer
tatsächlichen Textänderung vor der Freigabe-Queue erneut bewertet werden. Post 2
benötigt keine Revision. Dieses Stilurteil ist keine Nutzerfreigabe und löst
keine Queue-, Checkbox-, Termin-, Schedule-, Log-, Profil-, Lern-, Approved-,
Operator-, Browser-, LinkedIn- oder Veröffentlichungsaktion aus.
