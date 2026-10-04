# RV-DV-NP-20260923-R19 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschliesslich die zwei unveränderten `text`-Blöcke
aus `team/copywriter/collected/docval-biv-two-2026-09-23-r19.md`. Grundlage
waren Kampagne, persönliches Profil, Stilprofil, verbindliches Briefing, das
bestandene Stilurteil sowie die vollständigen aktuellen beziehungsweise
historischen Approval-, Schedule- und Log-Texte der neuen und alten
DocVal-Kampagne. Texte und Queues blieben unverändert.

## Textidentität und deterministische Vorprüfung

Die Hashes beziehen sich auf den exakten Inhalt des jeweiligen `text`-Blocks
ohne Marker und ohne den trennenden Zeilenumbruch vor dem Endmarker.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Limit | CTA/UTM | Hashtags |
|---|---:|---:|---:|---|---|---|---|
| Post 1 | 1.122 | 1.137 | 20 | `0a540dd84e43568474baf959cfb12a64093ab5dd6a421b2c35be8f3979a0563a` | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA und exakter UTM-Link je 1× | keine Pflicht-Hashtags; `#Compliance`, `#eIDAS`, `#RecordsManagement` passend und je 1× |
| Post 2 | 1.297 | 1.318 | 23 | `ffb9c833ae3180a5691057796ec970c96375716af68d2cf63616a750a12126cd` | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA und exakter UTM-Link je 1× | keine Pflicht-Hashtags; `#Compliance`, `#eIDAS`, `#RecordsManagement` passend und je 1× |

Beide Texte sind NFC-normalisiert. Codepointzahlen und SHA-256 stimmen exakt
mit dem Stilbericht überein; die dort bewerteten Fassungen sind unverändert.
`required_hashtags` ist leer. Der jeweils einzige Link ist der
kampagnendefinierte Produktlink mit `utm_source=linkedin`,
`utm_medium=social` und `utm_campaign=docval_biv_backoffice`.

## Dublettenlage

- In den geparsten `text`-Feldern von Approvals, Schedule und Log beider
  DocVal-Kampagnen liegt für keinen R19-Text eine exakte Dublette vor.
- Post 1 ist keine Wiederaufnahme des verworfenen Kontrollpunkt-Winkels. Sein
  Kern ist die redundante technische Neuprüfung derselben PDF durch
  Posteingang, Vertragsadministration und Compliance Ops; ein klar verorteter
  technischer Prüfschritt liefert gemeinsame Prüfinformationen, während die
  Fachrollen weiterhin ihre unterschiedlichen Entscheidungen treffen. Das ist
  ausreichend verschieden von festem Kontrollpunkt, Urlaubsvertretung,
  Zwei-Status- und Vier-Augen-Posts.
- Post 2 ist ebenfalls eigenständig: Er behandelt erstmals die Zuordnung und
  fachliche Betrachtung mehrerer Signaturen innerhalb derselben PDF statt
  eines pauschalen Dokumentstatus. Die vorhandenen Posts zu grünem Haken,
  Signatur/Identität/Berechtigung allgemein, Namensschild/Paketsiegel,
  Zwei-Status-Trennung und Vier-Augen-Prinzip decken diesen Mehrfachsignatur-
  Prozesskern nicht ab.

## Post 1 — eine technische Prüfung, mehrere Fachentscheidungen

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch, Kampagnenobjective und enger ICP sind erfüllt: konkrete Rollen
  prüfen dieselbe eingehende signierte PDF vor Archivierung.
- Der eigenständige operative Kern ist klar und funktional: unnötige
  technische Wiederholungsprüfungen werden von getrennten fachlichen
  Entscheidungen unterschieden. Weder automatische Freigabe noch
  Archivierung oder Workflowsteuerung wird behauptet.
- Die Produkt- und Datengrenzen sind korrekt: Der Document Validator liefert
  bei ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen;
  die PDF bleibt in der eigenen Umgebung und ihr Hash wird lokal gebildet.
  Beurteilung, Freigabe und Archivierung bleiben beim eigenen Prozess.
- Kaffeetassen-Hook, kurze gesprochene Sätze, Ich-Haltung und konkrete
  Schlussfrage entsprechen Romans persönlicher Stimme; Stilscore 0,86
  **BESTANDEN**.
- Keine Rechts-, Compliance-, Revisions-, Berechtigungs- oder
  Sicherheitsgarantie, keine erfundene Biografie, Kundengeschichte,
  Statistik oder regulatorische Pflicht; kein Angstmarketing,
  Wettbewerber-Bashing oder Spam.
- CTA, UTM-Link, Themen und Markensicherheit sind bestanden.

**Pflichtänderung:** keine.

## Post 2 — mehrere Signaturen sind kein gemeinsames Ampelsignal

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch, Kampagnenobjective und enger ICP sind erfüllt: Records/ECM und
  Compliance/Legal Ops betrachten eine mehrfach signierte PDF vor Freigabe
  oder Archivierung.
- Der Text formuliert mehrere Signaturen ausschliesslich als
  Prozesssituation. „Jede Unterschrift einzeln im Blick behalten“ und die
  anschliessenden Fragen sind eine fachliche Arbeitsanforderung; es wird keine
  konkrete Mehrfachsignatur-UI, automatische Einzelbewertung oder besondere
  Zuordnungsfunktion von Document Validator oder BIV behauptet.
- Die Produktrollen bleiben korrekt: Der Document Validator liefert
  Signatur- und Zertifikatsinformationen; BIV ergänzt Kontext zu Zeichner,
  Unternehmen und verfügbaren Berechtigungsinformationen. Freigabe und
  Archivierungsentscheid bleiben beim Team; der BIV-Kontext wird ausdrücklich
  nicht als juristische Garantie dargestellt.
- Drehtür-/Eintrittsmarkenbild, Pointe, kurze Struktur und Schlussfrage passen
  zur persönlichen Stimme; Stilscore 0,82 **BESTANDEN**.
- Keine pauschale Zeichnungsberechtigung, automatische Freigabe oder
  Archivierung und keine Rechts-, Compliance-, Revisions-, Berechtigungs- oder
  Sicherheitsgarantie; keine erfundene Biografie, Kundengeschichte, Statistik
  oder regulatorische Pflicht; kein Angstmarketing, Wettbewerber-Bashing oder
  Spam.
- CTA, UTM-Link, Themen und Markensicherheit sind bestanden.

**Pflichtänderung:** keine.

## Ergebnis und Prozessgrenze

| Text | Stilstatus | Reviewer-Urteil | Textidentität |
|---|---|---|---|
| Post 1 | 0,86 BESTANDEN | **FREIGEGEBEN** | 1.122 Codepoints; Hash bestätigt; unverändert |
| Post 2 | 0,82 BESTANDEN | **FREIGEGEBEN** | 1.297 Codepoints; Hash bestätigt; unverändert |

Das Kampagnenlimit `posts_per_run: 1` verhindert eine gemeinsame spätere
Veröffentlichung, nicht die getrennte Prüfung dieser zwei Entwürfe. Diese
Urteile sind interne Reviewer-Freigaben, keine Nutzerfreigaben. Sie berechtigen
weder zum Einreihen, Ankreuzen, Planen noch zum Veröffentlichen. Es erfolgte
keine Text-, Queue-, Checkbox-, Schedule-, Log-, Stil-, Lern-, Approved-,
Operator-, Browser-, LinkedIn- oder Veröffentlichungsaktion. Ohne tatsächliche
Textänderung erfolgt keine weitere Reviewer-Runde.
