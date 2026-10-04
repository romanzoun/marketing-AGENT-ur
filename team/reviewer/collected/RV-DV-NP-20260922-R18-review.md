# RV-DV-NP-20260922-R18 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschliesslich die zwei unveränderten reinen
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-22-r18.md`. Grundlage waren
die aktive Kampagne, das persönliche Profil, das Stilprofil, das bestandene
Stilurteil, der vollständige Approved-Korpus, die aktuelle Postlage der neuen
Kampagne sowie die relevanten jüngsten R14–R17-Artefakte. Texte und Queue
blieben unverändert.

## Textidentität und deterministische Vorprüfung

Die Hashes beziehen sich jeweils auf den exakten Text im `text`-Block ohne
Marker und ohne den trennenden Zeilenumbruch vor dem Endmarker.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Limit | CTA/UTM | Hashtags |
|---|---:|---:|---:|---|---|---|---|
| Post 1 | 1.222 | 1.235 | 20 | `40f225091c910408718f017f53fef27983b4b824a5874989dad92838659b7098` | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA und einziger Link exakt 1× | keine Pflicht-Hashtags; `#Compliance`, `#eIDAS`, `#RecordsManagement` passend und je 1× |
| Post 2 | 1.291 | 1.300 | 22 | `ff62a690e9d8a1941913b3437a703c2c93a13fcfc116e7b33c42f8e6549c57e4` | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA und einziger Link exakt 1× | keine Pflicht-Hashtags; `#Compliance`, `#eIDAS`, `#RecordsManagement` passend und je 1× |

Beide Texte sind NFC-normalisiert. Codepointzahlen und SHA-256-Hashes stimmen
exakt mit dem Stilurteil überein; die dort bewerteten Fassungen sind damit
unverändert. `required_hashtags` ist in der Kampagne leer. Der verwendete Link
ist jeweils exakt der kampagnendefinierte Link mit
`utm_source=linkedin`, `utm_medium=social` und
`utm_campaign=docval_biv_backoffice`.

## Aktuelle Dublettenlage

- In `Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md`
  stehen aktuell null Posttexte; vorhanden sind nur Kommentar-Kandidaten.
  `schedule.md` und `log.md` sind in dieser neuen Kampagne nicht vorhanden.
- Der vollständige Approved-Korpus wurde geprüft. Zusätzlich wurden die
  jüngsten R14–R17-Post- und Reviewer-Artefakte mit den dort bereits
  belegten beziehungsweise abgelehnten Funktionskernen abgeglichen.
- Für keinen der beiden R18-Texte liegt eine exakte Dublette vor. Auch die
  unten begründeten Funktionskerne sind ausreichend eigenständig.

## Post 1 — Der Validator ist Türsteher, nicht Bibliothekar

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch, enger ICP und konkrete Situation sind klar: Records-/ECM-Teams
  prüfen eingehende signierte PDFs vor der Archivierung.
- Der eigenständige Funktionskern ist die Grenze zwischen technischer
  Signatur-/Zertifikatsprüfung und den nachgelagerten Records-Aufgaben
  Ablageklasse, Aufbewahrungsfrist und Archivierungsentscheid. Der bereits
  freigegebene Zwei-Stempel-Post trennt allgemein „technisch geprüft“ von
  „fachlich freigegeben“; R18 macht dagegen erstmals Klassifikation und
  Retention zum konkreten Gegenstand. Auch Audit-Rückschau,
  Urlaubsvertretung, Trigger-Regel und Ergebnis-/Versionszuordnung werden
  nicht wiederholt.
- Türsteher/Bibliothekar, der trockene Organisationswitz, Ich-Perspektive und
  Schlussfrage entsprechen der persönlichen, konkreten Stimme. Das
  Stilurteil liegt bei 0,84 **BESTANDEN**.
- Die Produktrolle bleibt korrekt begrenzt: Der Document Validator prüft bei
  ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen; die
  PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.
  Klassifikation, Aufbewahrungsfrist und Archivierungsentscheid werden
  ausdrücklich nicht dem Produkt zugeschrieben.
- Keine automatische Archivierung oder Freigabe, keine Rechts-, Compliance-,
  Revisions-, Berechtigungs- oder Sicherheitsgarantie, keine erfundene
  Biografie, Kundengeschichte, Statistik oder regulatorische Pflicht.
- CTA, UTM, Themen, Ton, Spam-Prüfung und Markensicherheit sind bestanden;
  keine gesperrten Themen und kein Wettbewerber-Bashing.

**Pflichtänderung:** keine.

## Post 2 — Vier Augen brauchen zwei Prüfblicke

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch, enger ICP und konkrete Situation sind klar: Records/ECM,
  Vertragsadministration und Compliance/Legal Ops prüfen signierte PDFs vor
  Freigabe oder Archivierung.
- Der eigenständige Funktionskern ist die Qualität und Unabhängigkeit des
  Vier-Augen-Schritts: Die zweite Person soll konkrete Prüfinformationen und
  Kontext sehen und eine eigene fachliche Entscheidung treffen. Das ist mehr
  als die bestehende allgemeine Zwei-Status-Logik und mehr als ein erneuter
  Post zur begrenzten Aussagekraft eines grünen Hakens. Audit-Rückschau,
  mündliche Übergabe und Urlaubsvertretung sind ebenfalls nicht der Kern.
- Der Hook mit zwei Augenpaaren auf demselben Haken, das „gemeinsame
  Anstarren“, die Ich-Haltung und die drei praktischen Fragen passen zur
  persönlichen Stimme. Das Stilurteil liegt bei 0,87 **BESTANDEN**.
- Die Produktrollen sind sauber getrennt: Der Document Validator liefert
  Signatur- und Zertifikatsinformationen; der Business Identity Validator
  kann ergänzend Kontext zu Zeichner, Unternehmen und verfügbaren
  Informationen zur Berechtigung liefern. Die fachliche Folgerung bleibt
  ausdrücklich beim zuständigen Team.
- Keine Behauptung einer abschliessenden Zeichnungsberechtigung, automatischen
  Freigabe oder Archivierung und keine Rechts-, Compliance-, Revisions-,
  Berechtigungs- oder Sicherheitsgarantie. Keine erfundene Biografie,
  Kundengeschichte, Statistik oder regulatorische Pflicht.
- CTA, UTM, Themen, Ton, Spam-Prüfung und Markensicherheit sind bestanden;
  keine gesperrten Themen und kein Wettbewerber-Bashing.

**Pflichtänderung:** keine.

## Ergebnis und Prozessgrenze

| Text | Stilstatus | Reviewer-Urteil | Textidentität |
|---|---|---|---|
| Post 1 | 0,84 BESTANDEN | **FREIGEGEBEN** | Hash und Länge bestätigt; unverändert |
| Post 2 | 0,87 BESTANDEN | **FREIGEGEBEN** | Hash und Länge bestätigt; unverändert |

Dies sind interne Reviewer-Urteile, keine Nutzerfreigaben. Sie berechtigen
weder zum Einreihen, Ankreuzen, Planen noch zum Veröffentlichen. Es erfolgte
keine Text-, Queue-, Checkbox-, Schedule-, Log-, Stil-, Lern-, Approved-,
Operator-, Browser-, LinkedIn- oder Veröffentlichungsaktion. Ohne tatsächliche
Textänderung erfolgt keine weitere Reviewer-Runde.
