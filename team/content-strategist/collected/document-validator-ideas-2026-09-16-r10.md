# CS-DV-20260916-R10 — exakt zwei neue Post-Ideen

Kampagne: `Kampagnen/document validator/kampagne.yaml`

## Wiederaufnahme- und Dublettenprüfung

- Ausgangsstand: `Kampagnen/document validator/queue/approvals.md` enthält 0
  Post-Blöcke.
- Die früheren R6-/R8-Paare sind keine abgebrochenen, queuefreien Aufträge: Sie
  wurden bereits stilistisch und durch Reviewer geprüft und ihre Winkel stehen
  inzwischen in `schedule.md`. Sie werden nicht erneut verwendet.
- Die neuen Winkel grenzen sich von bestehenden Posts zu grünem Haken,
  Datenweg/Fremd-Cloud, LKW/API, Audit-Detektiv, Outlook-Eingangskontrolle,
  Regionalzug/stiller Post, Gepäck/grossen Dateien, Browser-Kontextwechsel,
  Dateiname/Stempel, Urlaubsvertretung/Escape Room und „untraurig“ ab.

## Idee 1 — Das Archiv ist ein Gefrierschrank, keine Kläranlage

- **Blickwinkel:** Archivieren macht eine unklare Signaturprüfung nicht später
  belastbarer. Der Prüfpunkt gehört vor Archivierung oder Freigabe; sonst wird
  die Unsicherheit nur sehr ordentlich konserviert.
- **Bild/Hook:** Eine unbeschriftete Dose im Gefrierschrank wird nach drei Monaten
  nicht verständlicher. Sie bleibt ein brauner Block mit Vergangenheit.
- **Fachkern:** Der Swisscom Document Validator prüft bei ZertES-/eIDAS-
  signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der
  eigenen Umgebung, ihr Hash wird lokal gebildet. Das Ergebnis liefert
  Prüfinformationen; menschliche Beurteilung, Freigabe, Archivierungsentscheid
  und Rechtsprüfung bleiben beim zuständigen Team.
- **Enger ICP:** Records/Posteingang, Vertragsadministration und Compliance Ops,
  die signierte PDFs vor Freigabe oder Archiv prüfen.
- **Einladung:** Was muss vor dem Archivieren sichtbar geklärt sein, damit nicht
  nur Unsicherheit sauber abgelegt wird?

## Idee 2 — Zwei Stempel, nicht ein Knopf mit Doppelleben

- **Blickwinkel:** „Technisch geprüft“ und „fachlich freigegeben“ sind zwei
  verschiedene Prozesszustände. Wer beides in ein einziges Statusfeld presst,
  lässt später niemanden mehr erkennen, was das System geprüft und was ein
  verantwortlicher Mensch entschieden hat.
- **Bild/Hook:** Ein Knopf mit zwei Beschriftungen ist im Aufzug lustig, im
  Compliance-Prozess eher weniger. Besser sind zwei klar benannte Stempel:
  Prüfinformation vorhanden; fachliche Entscheidung getroffen.
- **Fachkern:** Document Validator liefert Signatur- und
  Zertifikatsinformationen zu ZertES-/eIDAS-signierten PDFs; BIV kann Kontext
  zu Zeichner, Unternehmen und Berechtigung ergänzen. Keines der Produkte gibt
  ein Dokument automatisch frei oder ersetzt menschliche/rechtliche
  Beurteilung. PDF bleibt in der eigenen Umgebung, Hash wird lokal gebildet.
- **Enger ICP:** Vertragsadministration, Records/ECM und Compliance/Legal Ops
  mit nachvollziehbaren Freigabe- und Archivierungsabläufen.
- **Einladung:** Zeigt euer Workflow getrennt, was geprüft wurde und wer danach
  entschieden hat?

## Verbindliche Leitplanken für beide Texte

- Deutsch; je höchstens 1.300 Unicode-Codepoints inklusive Zeilenumbrüchen.
- Persönliche Ich-Stimme, trocken witzig, ein tragendes Bild, kurze gesprochene
  Sätze; kein Marketing-Sprech und keine erfundene Biografie/Kundengeschichte.
- Fachlich eng und ohne Heilsversprechen, automatische Compliance,
  Revisionssicherheits- oder Rechtsgarantie.
- Vollständiger Kampagnen-CTA mit exakt dem UTM-Link und je genau die drei
  Pflicht-Hashtags `#Compliance`, `#eIDAS`, `#RecordsManagement`.
- Zwei getrennte Freigabekandidaten; `posts_per_run: 1` bleibt die spätere
  Veröffentlichungsgrenze pro Zyklus.
- Keine Queue-, Checkbox-, Planungs-, Freigabe- oder Veröffentlichungsaktion
  durch delegierte Agenten.
