# CS-DV-NP-20260922-R18 — exakt zwei neue Post-Ideen

Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`

## Wiederaufnahme- und Queue-Prüfung

- In der neuen Kampagnen-Queue existieren null Post-Einträge; vorhanden sind nur
  Kommentar-Kandidaten. In den jüngsten Copywriter-/Style-/Reviewer-Artefakten
  existiert kein Paar fertiger, stilbestandener Posts für diesen Kampagnenpfad,
  das noch auf Reviewer oder Queue wartet. Daher Neuanlage, keine Fortsetzung.
- Exakt zwei neue Posts sind der ausdrückliche Laufauftrag. Die Kampagnenbegrenzung
  `posts_per_run: 1` wird für diesen expliziten Zweierauftrag nicht als
  Redaktionsvorgabe missverstanden; es werden trotzdem exakt zwei neue
  Nutzerfreigabe-Einträge erzeugt, aber nichts veröffentlicht oder geplant.

## Idee 1 — Der Validator ist Türsteher, nicht Bibliothekar

**Neuer Funktionskern:** Vor der Archivierung ist die Prüfung einer signierten
PDF wichtig, aber Signatur- und Zertifikatsinformationen beantworten nicht
automatisch, zu welcher Records-Klasse das Dokument gehört, wie lange es
aufbewahrt wird oder ob es archiviert werden darf. Der Post trennt erstmals die
technische Prüfinformation von Klassifikation und Retention; er ist kein weiterer
allgemeiner Zwei-Status- oder Freigabe-Post.

**Hook/Bild:** Ein Türsteher kann den Ausweis prüfen. Er entscheidet deshalb noch
lange nicht, in welches Regal die Akte gehört. Das wäre ein sehr eigenwilliger
Bibliotheksbetrieb.

**Fachlicher Kern:** Der Swisscom Document Validator prüft bei ZertES-/eIDAS-
signierten PDFs Signatur- und Zertifikatsinformationen; die PDF bleibt in der
eigenen Umgebung, ihr Hash wird lokal gebildet. Keine automatische
Records-Klassifikation, Aufbewahrungsfrist, Archivierungsentscheidung,
Rechtsprüfung oder Revisionssicherheit behaupten. Die Organisation beziehungsweise
zuständige Menschen ordnen Prüfinformationen in Ablageklasse, Retention und
Archivierungsentscheid ein.

**Schlussfrage:** Trennt euer Prozess sichtbar zwischen Signaturprüfung und der
Frage, wo und wie lange das Dokument aufbewahrt wird?

## Idee 2 — Vier Augen dürfen nicht zweimal nur denselben Haken anschauen

**Neuer Funktionskern:** Ein Vier-Augen-Prinzip wird nicht automatisch belastbar,
wenn zwei Personen nacheinander nur denselben visuellen Status bestätigen. Für
Records/ECM, Vertragsadministration und Compliance/Legal Ops sollte klar sein,
welche Prüfinformationen die zweite Person sieht und welche fachliche Entscheidung
sie unabhängig trifft. Dies ist ein Governance-Winkel zur Qualität des
Vier-Augen-Schritts, nicht die bereits verwendete allgemeine Trennung von
«technisch geprüft» und «fachlich freigegeben».

**Hook/Bild:** Zwei Paar Augen auf demselben grünen Haken sind noch kein
Vier-Augen-Prinzip. Manchmal ist es einfach nur sehr konzentriertes gemeinsames
Anstarren.

**Fachlicher Kern:** Der Document Validator liefert bei ZertES-/eIDAS-signierten
PDFs Signatur- und Zertifikatsinformationen. BIV darf ergänzend nur als Kontext
zu Zeichner, Unternehmen und verfügbaren Informationen zur Berechtigung genannt
werden; keine Aussage, dass BIV jede Zeichnungsberechtigung abschliessend oder
juristisch garantiert. Die Organisation gestaltet das Vier-Augen-Prinzip und
die Entscheidungsrollen; die Produkte erteilen keine Freigabe und ersetzen keine
rechtliche Beurteilung.

**Schlussfrage:** Was prüft das zweite Augenpaar bei euch wirklich – Evidenz und
Entscheidung oder nur die Farbe des Hakens?

## Verbindliche Textgrenzen

- Exakt zwei deutsche LinkedIn-Posts, je maximal 1.300 Unicode-Codepoints.
- Roman als Mensch: Ich-Perspektive, kurzer gesprochener Rhythmus, trockener Witz,
  bildhafte Vergleiche; kein Marketing-Sprech, keine erfundene Biografie,
  Kundengeschichte, Kennzahl oder regulatorische Pflicht.
- Enger ICP und konkrete Situation: eingehende signierte PDFs vor Freigabe oder
  Archivierung in Records/Posteingang, Vertragsadministration, ECM oder
  Compliance/Legal Ops.
- Vollständiger produktnaher Kampagnen-CTA mit exakt dem UTM-Link; sparsame,
  passende Hashtags. Laut Kampagne sind keine Hashtags zwingend vorgeschrieben;
  zur Korpusnähe bevorzugt `#Compliance #eIDAS #RecordsManagement`.
- Produktgrenzen strikt: keine automatische Auswahl, Freigabe, Archivierung,
  Rechtsprüfung, Identitäts-/Berechtigungsgarantie, Revisionssicherheit oder
  Audit-Trail-Funktion erfinden. BIV nur in Post 2 und sauber begrenzt.
- Nicht auf belegte Hauptwinkel zurückfallen: Fremd-Cloud/Datenweg, Audit-
  Rückschau, LKW, stille Post, Ausnahmeweg, Urlaubsvertretung, allgemeiner
  Zwei-Status-Post, Trigger-Regel, Version-Zuordnung, Eingangskanal,
  Prozess-Testfälle oder sichtbare Unterschrift.
- Folgeagenten ändern Queue, Checkboxen, Schedule/Log, Lernstand, Stilprofil und
  Approved-Korpus nicht und veröffentlichen nichts.
