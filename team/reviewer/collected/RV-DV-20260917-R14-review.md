# RV-DV-20260917-R14 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschließlich die zwei unveränderten Markertexte
aus `team/copywriter/collected/document-validator-two-2026-09-17-r14.md`.
Der gebundene Stilnachweis liegt mit **0,93/0,92 BESTANDEN** vor. Maßgeblich
für das Reviewer-Urteil sind die vollständige Kampagne, der persönliche
Faktenrahmen und die aktuelle Dublettenlage. Eine Reviewer-Freigabe ist keine
Nutzerfreigabe und berechtigt nicht zum Veröffentlichen.

## Textidentität und deterministische Prüfung

Die Hashes beziehen sich auf den exakten UTF-8-Text zwischen Start- und
Endmarker, ohne Marker und ohne den trennenden LF vor dem Endmarker.

| Prüfung | POST 1 | POST 2 |
|---|---:|---:|
| Unicode-Codepoints | **1.166** | **1.144** |
| Kampagnenlimit | 1.300 | 1.300 |
| UTF-8-Bytes | 1.181 | 1.163 |
| interne LF | 16 | 20 |
| SHA-256 | `39c6748c9cc105d4a4682e707bd4f7d229122f7a396aa7dc8b623d968ff4cf05` | `41df29d212d95621f67c737279f8f7bfa59700ff2bbac92d2ef1d327e9954df4` |
| Stilstatus | 0,93 BESTANDEN | 0,92 BESTANDEN |
| vollständiger exakter CTA inkl. UTM-Link | 1-mal, bestanden | 1-mal, bestanden |
| URLs | genau der zulässige CTA-Link | genau der zulässige CTA-Link |
| Pflicht-Hashtags | alle je 1-mal | alle je 1-mal |
| weitere Hashtags | keine | keine |
| exakte Dublette im Prüfkorpus | keine | keine |

Beide Texte sind NFC-normalisiert, enthalten damit jeweils genau
`#Compliance #eIDAS #RecordsManagement` und liegen unter dem Zeichenlimit.

## POST 1 — FREIGEGEBEN

- **Sprache, ICP und Thema:** Deutsch; Records/Posteingang,
  Vertragsadministration und Compliance Ops werden konkret im Umgang mit
  eingehenden signierten PDFs adressiert. Die gesellschaftlich-technische
  Frage nach Mensch oder Agent am Browser ist ausdrücklich Kampagnenthema.
- **Stimme:** Der höflich klickende Cursor ist ein eigenständiges, bildhaftes
  und trockenes Opening. Ich-Perspektive, kurze Sätze und die offene
  Schlussfrage passen zum Stilprofil; kein Werbe- oder Spamton.
- **Fakten und Produktrollen:** Der Document Validator wird korrekt der Prüfung
  von Signatur- und Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs
  zugeordnet. Der Business Identity Validator ergänzt nur möglichen Kontext zu
  Zeichner, Unternehmen und Berechtigung. Der Text grenzt ausdrücklich und
  korrekt ab, dass beide Produkte weder Mensch versus Agent erkennen noch
  einem Agenten ein Mandat erteilen.
- **Rechts-/Garantiegrenzen und Brand-Safety:** Keine Rechts-, Sicherheits-,
  Compliance-, Revisions- oder Wirkgarantie; keine erfundene Biografie oder
  Kundengeschichte, kein Konkurrenten-Bashing und kein verbotenes Thema.
- **Dublettenprüfung:** Keine exakte Dublette in `approvals.md`, `schedule.md`,
  `log.md`, im freigegebenen Korpus oder in R11/R13. Auch funktional
  eigenständig: Bestehende Browser-/Workflow-Texte behandeln Kontextwechsel,
  integrierte Prüfung, technische versus fachliche Zustände oder sichtbare
  Prüfinformationen. R11 behandelt die Sichtbarkeit am Prozessziel. R13
  behandelt Datenweg beziehungsweise Prozessrobustheit. POST 1 trägt dagegen
  die Erkennbarkeitsgrenze der Oberfläche und fragt nach einem prüfbaren
  Vertrauenssignal neben dem Cursor. Das ist weder der vorhandene
  Handover-/Freigabe- noch der Datenwegkern.

**Pflichtänderung: keine.**

## POST 2 — FREIGEGEBEN

- **Sprache, ICP und Thema:** Deutsch; Beschaffung, Records-, Vertragsadmin-
  und Compliance-Teams werden mit einer konkreten Prüfsituation adressiert.
  Der Text passt insbesondere zur kampagnendefinierten Buyer-/Blocker-Frage,
  ob ein Angebot „juristisch genug“ ist.
- **Stimme:** „Innere Nebelmaschine“, „Grosser Auftritt. Schlechte Sicht.“ und
  „mehr Substantive“ ergeben einen persönlichen, selbstironischen und
  gesprochenen Rhythmus ohne Marketing-Sprech.
- **Fakten und Produktrollen:** Der Document Validator liefert korrekt
  Prüfinformationen zu Signatur und Zertifikat; der Business Identity
  Validator kann ergänzenden geschäftlichen Kontext zu Zeichner, Unternehmen
  und Berechtigung liefern. Die Rollen werden weder vertauscht noch zu einer
  rechtlichen Entscheidung erweitert.
- **Rechts-/Garantiegrenzen und Brand-Safety:** Die ausdrückliche Grenze, dass
  beide Produkte keine automatische rechtliche Würdigung liefern, verhindert
  eine Rechtsgarantie. Keine Compliance-, Sicherheits-, Revisions- oder
  Wirkgarantie, keine erfundene Biografie oder Kundengeschichte, kein
  Konkurrenten-Bashing und kein verbotenes Thema.
- **Dublettenprüfung:** Keine exakte Dublette. Die Nebel-Metapher und die
  DocVal-/BIV-Rollen berühren vorhandenes Vokabular, aber nicht denselben
  funktionalen Nutzen. Der bestehende „grüne Haken im Nebel“ fragt nach
  sichtbaren technischen Details; der veröffentlichte Namensschild-/
  Kristallkugel-Text erklärt primär den ergänzenden BIV-Kontext. R11 wiederholt
  genau diese Produktrollentrennung als Hauptnutzen, R13 Datenweg und
  Prozessrobustheit. POST 2 macht dagegen aus der pauschalen Beschaffungsphrase
  „juristisch sicher“ zwei konkrete Prüffragen und etabliert damit eine neue
  Sprach- und Kaufregel. Diese Beschaffungsfunktion ist im Prüfkorpus nicht
  belegt.

**Pflichtänderung: keine.**

## Gesamtergebnis

| Text | SHA-256 | Länge | Reviewer-Urteil | Pflichtänderung |
|---|---|---:|---|---|
| POST 1 | `39c6748c9cc105d4a4682e707bd4f7d229122f7a396aa7dc8b623d968ff4cf05` | 1.166 Codepoints | **FREIGEGEBEN** | keine |
| POST 2 | `41df29d212d95621f67c737279f8f7bfa59700ff2bbac92d2ef1d327e9954df4` | 1.144 Codepoints | **FREIGEGEBEN** | keine |

Dies ist die einzige reguläre Reviewer-Runde für diese unveränderten Entwürfe.
Es erfolgte keine Text-, Queue-, Checkbox-, Freigabe-, Planungs-, Profil-,
Operator- oder Veröffentlichungsaktion. Die interne Reviewer-Freigabe ersetzt
keine Nutzerfreigabe.
