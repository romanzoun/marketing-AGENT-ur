# RV-DV-20260917-R13 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschließlich die zwei unveränderten Markertexte aus
`team/copywriter/collected/document-validator-two-2026-09-17-r13.md`. Der
Stilnachweis liegt mit **0,82/0,88 BESTANDEN** vor. Maßgeblich für das
Reviewer-Urteil sind die Kampagne und die aktuelle vollständige Dublettenlage;
eine bestandene Stilprüfung ist keine inhaltliche Freigabe.

## Textidentität und deterministische Prüfung

Die Hashes beziehen sich jeweils auf den exakten UTF-8-Text zwischen Start- und
Endmarker, ohne Marker und ohne den trennenden LF vor dem Endmarker.

| Prüfung | POST 1 | POST 2 |
|---|---:|---:|
| Unicode-Codepoints | **1.214** | **1.135** |
| Kampagnenlimit | 1.300 | 1.300 |
| UTF-8-Bytes | 1.230 | 1.152 |
| interne LF | 16 | 16 |
| SHA-256 | `50ab6e47aab469294a6c3043a07c6925cb49297adfc817acd3d2bb65b1bb67fc` | `71fbf21de4cdefd743d2377073408b1e513307c4f30a91c6681a04d0a7f49cf5` |
| vollständiger exakter CTA inkl. UTM-Link | 1-mal, bestanden | 1-mal, bestanden |
| URLs | genau der zulässige CTA-Link | genau der zulässige CTA-Link |
| Pflicht-Hashtags | alle je 1-mal | alle je 1-mal |
| weitere Hashtags | keine | keine |
| exakte Dublette in Approval/Schedule/Log | keine | keine |

Beide Texte enthalten damit exakt `#Compliance #eIDAS #RecordsManagement`,
keinen weiteren Hashtag und liegen unter dem Zeichenlimit.

## POST 1 — ABGELEHNT

### Bestandene Prüfpunkte

- Deutsch und enger ICP: IT/Security als konkreter Blocker sowie
  Records/Posteingang, Vertragsadministration und Compliance Ops im Prüfprozess
  vor Freigabe oder Archivierung.
- Stimme: persönliche Ich-Perspektive, verständliches Diagrammbild, trockenes
  Augenzwinkern und keine Corporate- oder Spam-Dramaturgie.
- Fakten und Produktrolle: Der Document Validator wird korrekt der Prüfung von
  ZertES-/eIDAS-signierten PDFs sowie Signatur- und Zertifikatsinformationen
  zugeordnet. PDF in eigener Umgebung und lokal gebildeter Hash sind korrekt
  formuliert; es wird nicht behauptet, ausschließlich der Hash verlasse die
  Umgebung.
- Die menschliche Beurteilung/Freigabe/Rechtsprüfung bleibt ausdrücklich beim
  zuständigen Menschen. Keine Rechts-, Sicherheits-, Compliance-, Revisions-
  oder Wirkgarantie, kein Konkurrenten-Bashing und keine erfundene Biografie.
- CTA, UTM-Link, Hashtags, Spam- und Brand-Safety-Prüfung sind bestanden.

### Ablehnungsgrund

**Funktionale Dublette.** Der tragende Nutzenkern ist erneut: Eine sensible
vollständige PDF soll nicht in eine unbekannte beziehungsweise Fremd-Cloud
getragen werden; beim Document Validator bleibt sie in der eigenen Umgebung
und ihr Hash wird lokal gebildet. Genau dieser Datenweg-/Fremd-Cloud-Nutzen ist
bereits Kern von `post-2026-09-11-0001` im Log und im Approved-Korpus. Der
aktuelle Schluss fragt wieder, wohin die vollständige PDF im Prüfprozess geht.

Zusätzlich deckt `post-2026-09-13-0002` im Schedule/Approved-Korpus den
gemeinsamen Datenweg-Test für IT/Security, Records und Legal Ops bereits ab:
Wo liegt die PDF, was verlässt die Umgebung, welche Prüfinformationen entstehen
und wer entscheidet danach? Das Architekturdiagramm und der zu streichende
Pfeil ändern das Bild, aber nicht die Funktion oder den Entscheidungsnutzen.

### Pflichtänderung vor einer erneuten Prüfung

Den Fremd-Cloud-/lokaler-Datenweg-/Hash-Nutzen nicht erneut zum Hook,
Hauptargument und zur Schlussfrage machen. POST 1 braucht einen nachweislich
queuefreien funktionalen Nutzen für den engen ICP; ein neues Diagramm- oder
Pfeilbild allein genügt nicht. Der überarbeitete Text muss anschließend als
tatsächlich geänderter Finalstand erneut durch Stil- und Reviewer-Prüfung.

## POST 2 — ABGELEHNT

### Bestandene Prüfpunkte

- Deutsch und enger ICP: Records/Posteingang, Vertragsadministration und
  Compliance Ops mit einer eingehenden signierten PDF vor Freigabe oder
  Archivierung.
- Stimme: konkrete Alltagsszene, starke Ich-Perspektive, Selbstironie und
  verständliche Bilder ohne Werbe- oder Spamton.
- Fakten und Produktrolle: Prüfung von ZertES-/eIDAS-signierten PDFs sowie
  Signatur- und Zertifikatsinformationen, PDF in eigener Umgebung und lokal
  gebildeter Hash sind korrekt. Das technische Ergebnis wird nicht mit einer
  fachlichen Freigabe oder Rechtsprüfung gleichgesetzt.
- Keine Rechts-, Sicherheits-, Compliance-, Revisions- oder Wirkgarantie,
  keine erfundene Biografie und kein markensicherheitsrelevanter Inhalt.
- CTA, UTM-Link und Hashtags sind vollständig und exakt; die formale und
  Brand-Safety-Prüfung ist bestanden.

### Ablehnungsgrund

**Funktionale Dublette.** Der neue Zeitpunkt „Freitag, 16:58 Uhr“ ist eine neue
Szene, der funktionale Nutzen bleibt jedoch der bereits veröffentlichte
Robustheits-/Kontrollpunkt-Test: Ein Prüfprozess soll auch unter einer
alltäglichen Belastung zuverlässig als fester Schritt vor Freigabe oder
Archivierung funktionieren. `post-2026-09-15-0002` im Schedule und
Approved-Korpus prüft dieselbe Prozessrobustheit bereits über die
Urlaubsvertretung und denselben wiederholbaren Prüfbaustein. Uhrzeit und
Kaffeebecher ersetzen Ferienvertretung und Escape Room, ohne die Funktion zu
ändern.

Der zweite Kern — Prüfinformationen sind noch keine Freigabe, der Mensch
entscheidet beziehungsweise holt die Rechtsprüfung hinzu — ist zudem bereits
expliziter Gegenstand von `post-2026-09-16-0002` im Schedule/Approved-Korpus
(`technisch geprüft` versus `fachlich freigegeben`, Prüfinformationen versus
menschliche Entscheidung). Damit entsteht auch aus dieser Abgrenzung kein
neuer funktionaler Nutzen.

### Pflichtänderung vor einer erneuten Prüfung

Nicht nur die Belastungsszene austauschen. POST 2 braucht einen funktionalen
Mehrwert, der weder den bestehenden Robustheits-/Vertretungstest und festen
Kontrollpunkt noch die bereits belegte Trennung von technischer Prüfung und
menschlicher Freigabe erneut trägt. Der überarbeitete Text muss anschließend
als tatsächlich geänderter Finalstand erneut durch Stil- und Reviewer-Prüfung.

## Gesamtergebnis

| Text | Stilstatus | Reviewer-Urteil | Pflichtänderung |
|---|---:|---|---|
| POST 1 | 0,82 BESTANDEN | **ABGELEHNT** | neuer queuefreier Funktionskern statt Fremd-Cloud-/Datenweg-Wiederholung |
| POST 2 | 0,88 BESTANDEN | **ABGELEHNT** | neuer queuefreier Funktionskern statt Robustheits-/Kontrollpunkt- und Mensch-entscheidet-Wiederholung |

Beide Texte sind an den Copywriter zurückzugeben. Dieses interne
Reviewer-Urteil ist keine Nutzerfreigabe und berechtigt nicht zu Queue-,
Checkbox-, Planungs-, Operator- oder Veröffentlichungsaktionen. Texte, Queue,
Planung, Profil und Lernstand wurden nicht verändert.
