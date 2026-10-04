# RV-DV-NP-20260926-R22 — einmalige reguläre Reviewer-Runde

Geprüft wurden genau einmal ausschließlich die zwei unveränderten `text`-Blöcke
aus `team/copywriter/collected/docval-biv-two-2026-09-26-r22.md`. Maßgeblich
waren die Kampagne `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`,
das persönliche Profil, das Stilprofil und der bestandene Stilbericht
`team/style-evaluator/collected/SE-DV-NP-20260926-R22-review.md`.

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschließenden Zeilenumbruch.

## Deterministische Vorprüfung

| Text | Unicode-Codepoints | Limit | Pflicht-Hashtags | CTA/UTM | SHA-256 |
|---|---:|---:|---|---|---|
| Post 1 | 1.255 | 1.300 | keine (`required_hashtags: []`) | vollständiger Kampagnen-CTA; exakter UTM-Link einmal | `0d4029383c37260ff1a85293ba44b6629364411a4826f55d64cb2d95a1e28c56` |
| Post 2 | 1.290 | 1.300 | keine (`required_hashtags: []`) | vollständiger Kampagnen-CTA; exakter UTM-Link einmal | `e048c6ca33d901a84f8b6e4857a7cc203824339e5a6153e2a335f071d566fa32` |

Die Textidentität stimmt bei beiden Posts mit Copywriter-Artefakt und
Stilbericht überein. Die vorhandenen optionalen Hashtags sind thematisch
vertretbar.

## Post 1 — Drei Uhren, drei Aussagen

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit: Deutsch, enger Records-/ECM-/Legal-Ops-ICP, Prüfung signierter
  PDFs vor Archivierung/Freigabe sowie nachvollziehbare Prozessdokumentation
  sind klar getroffen. Die Uhren-/Fahrplanmetapher, Ich-Perspektive und knappe
  Schlussfrage entsprechen der persönlichen Stimme; kein Spam oder
  Angstmarketing.
- Fakten und Produktgrenzen: Der Document Validator wird nur mit der Prüfung
  von Signatur- und Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs
  sowie dem Datenfluss „PDF in der eigenen Umgebung, Hash lokal gebildet“
  beschrieben. Die Trennung und Festhaltung von Signaturzeitpunkt,
  technischem Prüfzeitpunkt und fachlichem Entscheidungszeitpunkt wird
  ausdrücklich dem **eigenen Prozess** zugeordnet und durch „soweit die
  Informationen verfügbar sind“ begrenzt. Es wird keine Zeitstempel-,
  Zeitfeld-, Archivierungs-, Freigabe-, Rechts- oder Revisionsfunktion des
  Validators behauptet. Keine erfundene Biografie, Kundensituation,
  regulatorische Pflicht, Statistik oder Garantie.
- Dubletten: Gegen alle 35 vorhandenen Posteinträge beziehungsweise 34
  unterschiedlichen Textstände in `approvals.md`, `schedule.md` und `log.md`
  beider DocVal-Kampagnenpfade besteht keine exakte Dublette. Auch keine
  funktionale Dublette: `post-2026-09-25-0001` dokumentiert die Version eines
  internen Regelsets am Entscheidungszeitpunkt; `post-2026-09-16-0002` trennt
  technischen Prüfstatus und fachliche Freigabe. Der vorliegende Kern trennt
  dagegen drei verschiedenartige Zeitpunkte beziehungsweise Ereignisse. Die
  thematische Nähe ersetzt diesen neuen Funktionskern nicht.

## Post 2 — Ein Namensschild kennt keinen Betrag

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit: Deutsch, Vertragsadministration und Compliance/Legal Ops sowie
  die Trennung von technischer Signaturprüfung, Identitäts-/Unternehmenskontext
  und organisationsseitiger Entscheidung sind exakt kampagnenrelevant. Hook,
  trockener Betragskontrast und Schlussfrage sind persönlich und verständlich;
  kein Spam, Druck oder Heilsversprechen.
- Fakten und Produktgrenzen: Der Document Validator bleibt auf Signatur- und
  Zertifikatsinformationen begrenzt. Der BIV **kann** Kontext zu Zeichner,
  Unternehmen und verfügbaren Informationen zur Berechtigung liefern. Ob
  5'000 oder 5 Millionen innerhalb einer internen Kompetenzgrenze liegen, wird
  ausdrücklich dem zuständigen Team und seinen Regeln zugeordnet. Die beiden
  Beträge sind erkennbar illustrative Kontrastwerte, keine Statistik oder
  Aussage über eine konkrete Organisation. Dem BIV werden weder interne
  Kompetenzgrenzen noch automatische Wertprüfung, abschließende
  Zeichnungsberechtigung oder rechtliche Garantie zugeschrieben. Keine
  erfundene Biografie, Kundensituation oder regulatorische Pflicht.
- Dubletten: Keine exakte Dublette in den 35 Posteinträgen beider Queue-Pfade.
  Deutliche Motivnähe besteht zum historischen `post-2026-09-10-0002`, der das
  Namensschild allgemein für Name versus geschäftliche
  Zeichnungsberechtigung nutzt. Der neue Funktionskern ist jedoch materiell
  enger: verfügbarer Kontext wird mit **diesem konkreten Vorgang und
  Vertragswert** sowie organisationsinternen Kompetenzregeln verknüpft. Auch
  Vier-Augen-, Mehrfachsignatur- und allgemeine DocVal-/BIV-Rollentexte decken
  diesen wert- und vorgangsgebundenen Entscheidungsfall nicht ab. Daher keine
  funktionale Dublette.

## Ergebnis

| Text | Urteil | Pflichtänderung | Exakte Dublette | Funktionale Dublette |
|---|---|---|---|---|
| Post 1 | **FREIGEGEBEN** | nein | nein | nein |
| Post 2 | **FREIGEGEBEN** | nein | nein | nein |

Die Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zur
Queue-Verschiebung noch zu Planung oder Veröffentlichung. Ohne tatsächliche
Textänderung ist keine weitere Reviewer-, Hash- oder Kontrollrunde erforderlich.
