# CS-DV-20260918-R15 — exakt zwei neue Post-Ideen

## Wiederaufnahme- und Dublettenprüfung

- Frühere offene Team-Checkboxen zu R6/R8 sind kein Wiederaufnahmefall: Die
  zugehörigen Flughafen-/Ausnahmeweg- und Browser-Agent-/Übergabezettel-Texte
  liegen bereits als frühere Jobs in `schedule.md`.
- Ausgangsbestand in `approvals.md`: 1 Post und 2 Kommentare; SHA-256
  `7e21db06ffea3542941df49835cb3f706f2952a3e231045629a0925f33f414ff`.
- Die folgenden Blickwinkel sind weder exakte noch funktionale Dubletten der
  aktuellen Posttexte in `approvals.md`, `schedule.md` oder `log.md`.

## Idee 1 — Zu selten für Routine, zu wichtig fürs Bauchgefühl

**Blickwinkel:** Der besonders interessante Bereich liegt nicht erst bei hunderten
Prüfungen. Schon etwa 10–50 eingehende signierte PDFs pro Monat können bei
sensiblen Daten oder Audit-Druck einen klaren Kontrollpunkt brauchen. Gerade weil
eine solche Prüfung nicht jeden Morgen vorkommt, entsteht oft keine verlässliche
Routine: Menschen improvisieren, verschieben oder erinnern sich unterschiedlich.
Der Post soll diese „gefährliche Mitte“ greifbar machen und für einen festgelegten
Prüfschritt vor Freigabe oder Archivierung argumentieren.

**Hook/Bild:** Ein Prozess, der nur alle paar Tage klingelt, wird nicht automatisch
zur Gewohnheit. Eher zu einem Klingelton, bei dem kurz alle überlegen, wem das
Telefon gehört. Trocken und persönlich, ohne Kundengeschichte.

**Fachlicher Kern:** Nicht behaupten, dass eine bestimmte Menge automatisch einen
Business Case, Rechtswirkung oder Compliance erzeugt. Die kampagneninterne
Faustformel als Orientierung formulieren: Bei ungefähr 10+ Prüfungen pro Monat plus
Sensitivität/Audit-Druck lohnt sich ein definierter Kontrollpunkt. Document
Validator prüft ZertES-/eIDAS-signierte PDFs sowie Signatur- und
Zertifikatsinformationen; die PDF bleibt in der eigenen Umgebung, der Hash wird
lokal gebildet. Der Mensch beurteilt und entscheidet.

**Schlussfrage:** Ab welchem Volumen wird aus einer gelegentlichen Prüfung bei euch
ein definierter Prozess?

## Idee 2 — „Bei Bedarf prüfen“ ist ein Horoskop

**Blickwinkel:** Viele Prozessbeschreibungen sagen nur, dass signierte PDFs „bei
Bedarf“ geprüft werden. Das ist für Records/Posteingang, Vertragsadministration
oder Compliance Ops kein belastbarer Auslöser. Der neue Nutzenkern ist eine klare,
vorab definierte Trigger-Regel: Welche eingehenden signierten PDFs müssen vor
Freigabe oder Archivierung in den Prüfschritt, wer beurteilt das Ergebnis und wo
landet die Entscheidung? Der Validator liefert Prüfinformationen; er erfindet
weder die interne Policy noch klassifiziert oder genehmigt er automatisch.

**Hook/Bild:** „Bei Bedarf prüfen“ ist für Roman ungefähr so präzise wie ein
Horoskop: klingt erstaunlich passend, hilft aber am Dienstag um 16:40 Uhr nicht bei
der nächsten PDF. Humorvoll, nicht abwertend.

**Fachlicher Kern:** Den Trigger konkret, aber organisationsneutral machen, etwa
„eingehende signierte PDF + vorgesehene Freigabe/Archivierung + sensible oder
auditrelevante Unterlagen“. Keine automatische Erkennung, Rechtsprüfung,
Freigabe, Revisionssicherheit oder Vollständigkeit behaupten. Document Validator
bleibt bei Signatur-/Zertifikatsinformationen; BIV darf nur optional und korrekt
als Kontext zu Zeichner, Unternehmen und Berechtigung genannt werden.

**Schlussfrage:** Ist euer Prüfauslöser eine klare Regel oder ein freundliches „bei
Bedarf“?

## Verbindliche Leitplanken für beide Texte

- Sprache Deutsch; persönliche Ich-Perspektive, kurzer gesprochener Rhythmus,
  trockener Humor; keine erfundene Biografie, Rolle, Kundenepisode oder Kennzahl.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance/Legal Ops;
  eingehende signierte PDFs vor Freigabe oder Archivierung.
- Je Text höchstens 1.300 Unicode-Codepoints, genau ein zulässiger Link, exakt der
  vollständige Kampagnen-CTA und exakt `#Compliance #eIDAS #RecordsManagement`.
- Keine Konkurrentenabwertung, Politik, Religion, Rechtsgarantie,
  Compliance-/Freigabe-/Revisionsautomatik oder Produkterweiterung.
- Bestehende Bildfelder und Hauptwinkel nicht wiederholen: grüner Haken,
  Detektiv/Audit, Garderobe/Cloud, LKW/Werkstor, stille Post/Regionalzug,
  Flughafen/Ausnahmeweg, Schnurrbart/Übergabezettel, Cursor/Pass,
  Gefrierschrank, Aufzugknopf/zwei Stempel, Gäste/Schuhe, Besteckkasten,
  Dateiname, Escape Room, Nebelmaschine und Demo/Stoppuhr.
- Keine Queue-, Freigabe-, Checkbox-, Schedule-, Operator- oder
  Veröffentlichungsaktion durch den copywriter.

## Zielgerichteter Ersatzkern für abgelehnte Idee 1 (Iteration 2)

Der Reviewer hat die ursprüngliche Volumen-/Routine-Idee als funktionale
Dublette des bestehenden 10+-Fälle-/Urlaubsvertretungs-Posts abgelehnt. Sie wird
nicht gequeut und nicht nur umformuliert.

**Neuer Funktionskern:** Ein AI-Agent braucht im agentischen Ablauf manchmal
vor dem nächsten Tool-Schritt eine explizite Compliance-Entscheidung. Deshalb
wird MCP-Zugriff rund um Business Identity Validator und Document Validator
aufgebaut: Signatur-/Zertifikatsinformationen und Kontext zu Zeichner,
Unternehmen und Berechtigung können als klarer Prüfpunkt in einem agentischen
Workflow angefragt werden, bevor der Agent fortfährt. Der Nutzen ist die
explizite Prüfunterbrechung im Tool-Ablauf, nicht Mensch-vs.-Agent-Erkennung,
Browser-Cursor, Mandatserteilung, allgemeiner Handover, Volumen, Routine oder
ein bloss fester Records-Kontrollpunkt.

**Hook/Bild:** Ein guter AI-Agent sollte nicht nur wissen, welches Tool er als
Nächstes aufrufen kann. Er sollte auch wissen, wann er kurz die Hände von der
Tastatur nehmen muss. Bildhaft und trocken, aber ohne bereits belegten Cursor,
Schnurrbart, Schlüssel, Staffelstab oder Übergabezettel.

**Harte Grenzen:** Die Aussage „wir bauen MCP-Zugriff rund um BIV und Document
Validator“ ist durch das freigegebene Lern-/Approved-Beispiel
`2026-09-17-comment-2026-09-16-0001.md` gedeckt. Nicht behaupten, die Produkte
erkennen Mensch versus Agent, geben dem Agenten Identität/Mandat/Berechtigung,
treffen selbst eine Compliance-/Rechts-/Freigabeentscheidung oder erlauben dem
Agenten automatisch weiterzumachen. Document Validator bleibt bei
ZertES-/eIDAS-signierten PDFs sowie Signatur-/Zertifikatsinformationen; BIV
kann Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen. Ein
zuständiger Mensch beziehungsweise die organisationsseitige Policy entscheidet
über den nächsten Schritt. Alle übrigen gemeinsamen Leitplanken bleiben
unverändert.
