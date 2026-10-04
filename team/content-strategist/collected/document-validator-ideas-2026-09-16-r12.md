# CS-DV-20260916-R12 — zwei neue Ersatzideen nach Reviewer-Ablehnung von R11

Kampagne: `Kampagnen/document validator/kampagne.yaml`

## Abgrenzung

- R11 wurde einmal reviewed und wegen funktionaler Dubletten abgelehnt; diese
  Texte werden weder erneut geprüft noch gequeuet.
- Der aktuelle Approval-Stand enthält 0 Post-Einträge.
- Die folgenden Winkel vermeiden die bestehenden Familien Datenweg/Fremd-Cloud,
  grüner Haken/Zertifikatsdetails, Audit-Nachweis, LKW/API, stille Post,
  Outlook/Medienbruch, Dateiname/Stempel, Urlaubsvertretung, Ausnahmeweg,
  Browser-Agent, Archiv-Gefrierschrank und technische versus fachliche Freigabe.

## Idee 1 — Die Gegenpartei signiert, der Empfänger setzt den Kontrollpunkt

- **Blickwinkel:** Bei ausgehenden Dokumenten kann ein Unternehmen den eigenen
  Signaturprozess gestalten. Bei eingehenden signierten PDFs bestimmt dagegen
  die Gegenpartei, wie sie signiert. Records-, Vertragsadmin- und Compliance-
  Teams können trotzdem einen einheitlichen Prüfpunkt vor Annahme, Freigabe oder
  Archivierung setzen. Das ist weder ein Datenweg- noch ein API-/Volumenpost,
  sondern ein Beitrag über die asymmetrische Prozessverantwortung im Eingang.
- **Bild/Hook:** Gäste bringen ihre eigenen Schuhe mit. Ob sie damit ungeprüft
  über den frisch gewischten Boden laufen, entscheidet aber das Haus.
- **Fachkern:** Der Swisscom Document Validator liefert bei eingehenden
  ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Er
  standardisiert keine fremden Signaturprozesse und gibt nichts automatisch
  frei; er liefert dem empfangenden Team Prüfinformationen für seinen eigenen
  Kontrollpunkt. PDF bleibt in eigener Umgebung, Hash wird lokal gebildet.
- **Einladung:** Was ist bei euch standardisiert: wie andere signieren oder wie
  ihr eingehende signierte PDFs prüft?

## Idee 2 — Ein Posteingang, zwei Abkürzungen

- **Blickwinkel:** Im operativen Posteingang kommen Dokumente nicht in sauber
  beschrifteten Stapeln „ZertES“ und „eIDAS“ an. Der Prozess muss beide Arten
  eingehender signierter PDFs am selben Kontrollpunkt handhaben, ohne daraus
  eine Aussage über rechtliche Gleichwertigkeit oder Anerkennung abzuleiten.
  Dieser Winkel behandelt die gemischte regulatorische Herkunft, nicht erneut
  Datenweg, Audit-Trail, Freigaberolle oder BIV-Kontext.
- **Bild/Hook:** Ein Posteingang ist kein Besteckkasten. Die Gabeln aus der
  Schweiz und die Löffel aus der EU liegen nicht freiwillig in getrennten
  Fächern.
- **Fachkern:** Der Swisscom Document Validator prüft ZertES-/eIDAS-signierte
  PDFs und liefert Signatur- und Zertifikatsinformationen. Die PDF bleibt in
  eigener Umgebung, ihr Hash wird lokal gebildet. Keine Behauptung, ZertES und
  eIDAS seien rechtlich identisch; keine Rechts- oder Compliance-Garantie.
- **Einladung:** Muss euer Team beim Eingang erst die passende Prüfschublade
  suchen oder gibt es einen klaren Kontrollpunkt für beide?

## Verbindliche Leitplanken

- Genau zwei getrennte deutschsprachige Posts, je höchstens 1.300 Unicode-
  Codepoints inklusive Zeilenumbrüchen.
- Persönliche Ich-Stimme, trocken witzig, pro Text ein tragendes Bild, kurze
  gesprochene Sätze; kein Marketing-Sprech und keine erfundene Biografie oder
  Kundengeschichte.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance Ops in
  regulierten Organisationen mit regelmässig eingehenden signierten PDFs.
- Keine Heilsversprechen, automatische Compliance, Revisionssicherheits-,
  Zeitersparnis-, Sicherheits- oder Rechtsgarantie.
- Vollständiger Kampagnen-CTA mit exakt dem UTM-Link und je genau die drei
  Pflicht-Hashtags `#Compliance`, `#eIDAS`, `#RecordsManagement`.
- Keine Queue-, Checkbox-, Planungs-, Freigabe- oder Veröffentlichungsaktion
  durch delegierte Agenten.
