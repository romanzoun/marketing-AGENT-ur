# CS-DV-20260920-R16 — exakt zwei neue Post-Ideen

## Wiederaufnahme- und Queue-Prüfung

- Der jüngste Lauf `CS-DV-20260918-R15` ist vollständig abgeschlossen. Seine zwei
  reviewer-freigegebenen Texte liegen bereits als `post-2026-09-18-0001/0002`
  ungekreuzt in `approvals.md`; es gibt keine zwei neueren stilbestandenen Texte
  ohne Queue-Eintrag.
- Baseline für diesen Lauf: drei Post-Blöcke in `approvals.md`.
- Die folgenden Ideen erhalten neue Funktionskerne und dürfen weder als Variante
  eines vorhandenen grünen Hakens noch als allgemeiner Kontrollpunkt geschrieben
  werden.

## Idee 1 — Sichtbare Unterschrift ist noch kein prüfbarer Nachweis

**Blickwinkel:** Im Posteingang sieht eine PDF mit Namenszug oder eingescanntem
Kringel schnell «unterschrieben» aus. Für Records/Posteingang und
Vertragsadministration ist das aber nicht dieselbe Frage wie: Liegt eine technisch
prüfbare ZertES-/eIDAS-Signatur samt auswertbaren Zertifikatsinformationen vor?
Der neue Nutzenkern ist die saubere Eingangsunterscheidung zwischen optischem
Eindruck und technisch prüfbarer elektronischer Signatur — noch bevor Freigabe oder
Archivierung beginnen.

**Hook/Bild:** Ein Kringel unten rechts macht aus einer PDF noch keinen geprüften
Vertrag. Romans Einkaufszettel hat schliesslich auch eine Unterschrift — meistens
«Milch nicht vergessen».

**Fachlicher Kern:** Keine pauschale Aussage zur Rechtswirkung sichtbarer,
eingescannter oder elektronischer Unterschriften. Nur sagen: Aus dem sichtbaren Bild
allein lässt sich keine ZertES-/eIDAS-Prüfung ableiten. Der Swisscom Document
Validator prüft bei entsprechend elektronisch signierten PDFs Signatur- und
Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird
lokal gebildet. Fachliche Einordnung und Freigabe bleiben beim zuständigen Team.

**Schlussfrage:** Woran erkennt euer Posteingang heute, ob eine PDF nur
unterschrieben aussieht oder technisch geprüft werden kann?

## Idee 2 — Den Prüfprozess mit Testfällen prüfen

**Blickwinkel:** Eine Validator-Integration sollte nicht nur im freundlichen
Happy Path vorgeführt werden. Vor dem produktiven ECM-/Records-Einsatz braucht der
gesamte Ablauf einige bekannte Testfälle: Kommt das Prüfergebnis am richtigen Ort
an? Stoppt der Workflow, wenn eine vorgegebene Bedingung nicht erfüllt ist? Bleibt
klar, wer beurteilt und freigibt? Der neue Nutzenkern ist ein wiederholbarer
Abnahmetest des Prüfprozesses, nicht die tägliche Prüfung, der Ausnahmeweg oder eine
Volumenargumentation.

**Hook/Bild:** Einen Rauchmelder nur mit frischer Zimmerluft zu testen, ist sehr
harmonisch. Nur leider kein besonders ehrlicher Test. Trocken, nicht dramatisch.

**Fachlicher Kern:** Keine Produktfunktion für Testdatensätze, automatische
Klassifikation oder fest definierte Ergebnisstatus erfinden. Als organisatorische
Empfehlung formulieren: Teams stellen selbst einen kleinen, datenschutzkonformen
Testsatz mit vorab erwarteten Prüfergebnissen zusammen und testen Integration,
Weiterleitung und menschliche Entscheidung. Der Document Validator prüft
ZertES-/eIDAS-signierte PDFs sowie Signatur- und Zertifikatsinformationen und kann
in Records-/ECM-Abläufe eingebunden werden; die PDF bleibt in der eigenen Umgebung,
der Hash wird lokal gebildet.

**Schlussfrage:** Wann habt ihr zuletzt nicht das PDF, sondern euren Prüfprozess
getestet?

## Verbindliche Leitplanken für beide Texte

- Deutsch; Roman in Ich-Perspektive, persönlich, trocken-witzig, bildhaft,
  gesprochen und ohne Marketing-Sprech oder erfundene Biografie/Kundengeschichte.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance/Legal Ops;
  eingehende signierte PDFs vor Freigabe oder Archivierung.
- Je Text höchstens 1.300 Unicode-Codepoints; vollständiger Kampagnen-CTA samt
  einzigem UTM-Link; mindestens die drei Pflicht-Hashtags
  `#Compliance #eIDAS #RecordsManagement` (zusätzliche passende Hashtags sind laut
  jüngstem Lernsignal erlaubt, aber nicht nötig).
- Produkte strikt trennen; BIV nur nennen, wenn Zeichner, Unternehmen oder
  Berechtigung inhaltlich nötig sind. Keine automatische Freigabe, Rechts-,
  Compliance-, Revisions- oder Wirkgarantie.
- Keine Wiederholung vorhandener Funktionskerne: Datenweg/Fremd-Cloud, grüner
  Haken/Zertifikatsdetails, Audit-Rückschau, BIV-Zeichnungsberechtigung,
  Ausnahmeweg, Volumen/Urlaubsvertretung, allgemeiner Kontrollpunkt,
  technische vs. fachliche Freigabe, Trigger-Regel, Browser-Agent-Erkennung oder
  MCP-Prüfunterbrechung.
- Keine Queue-, Checkbox-, Schedule-, Operator-, Bild- oder
  Veröffentlichungsaktion durch Folgeagenten.
