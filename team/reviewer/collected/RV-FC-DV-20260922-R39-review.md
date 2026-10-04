# Reviewer-Prüfung — RV-FC-DV-20260922-R39

Datum: 2026-09-22  
Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`  
Prüfumfang: einmalige Prüfung der unveränderten Queue-Kandidaten `comment-2026-09-22-0004` und `comment-2026-09-22-0005`

## Deterministische Vorprüfung

Die Kampagne erlaubt maximal **500 Unicode-Codepoints** pro Kommentar und verlangt
**keine Pflicht-Hashtags** (`required_hashtags: []`).

| Kandidat | Codepoints | SHA-256 des exakten UTF-8-Texts | Hashtags | Links | Ergebnis |
|---|---:|---|---:|---:|---|
| `comment-2026-09-22-0004` | 336/500 | `82607584150656fe51e93033e87ea6c6d4ac6102ce5d92e8c3f8738cb83eadd4` | 0 | 0 | bestanden |
| `comment-2026-09-22-0005` | 0/500 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | 0 | Leertext bestätigt |

Der Text von 0004 ist inhaltsidentisch mit dem finalen Text im Copywriter-Bericht
und dem exakt bewerteten Text der Stilprüfung. Der Stilstatus **0,88 BESTANDEN**,
ohne Pflichtrevision, ist bestätigt. 0005 enthält bewusst keinen Entwurf; das
formale Limit macht den gesperrten Kandidaten nicht freigabefähig.

## `comment-2026-09-22-0004`

- URL: `https://lnkd.in/p/eVSaN-CY`
- Separate URN: keine vorhanden; keine abgeleitet oder erfunden
- `fit_score`: `0.28`
- Einzelurteil: **FREIGEGEBEN**
- Pflichtänderung: **keine**

### Begründung

- **Objective und Themenfit:** Der Kommentar bleibt im engen, zulässigen
  Awareness-Winkel zu digitaler Identität, digitalem Vertrauen und verständlicher
  Trust-Kommunikation. Er verkauft nicht und erfindet keine Brücke zu signierten
  PDFs, Archivierung/Freigabe, Records/ECM, Audit-Trail, Signaturvalidierung,
  Document Validator oder BIV. Der niedrige Teilfit `0.28` ist deshalb angemessen,
  aber nicht null.
- **Audience:** Der Originalpost behandelt Verbraucherwahrnehmung und erreicht
  nicht den engen Records-/ECM-/Compliance-ICP. Der Kommentar behauptet diesen
  Zielgruppenbezug jedoch nicht, sondern beschränkt sich auf eine fachliche
  Awareness-Einordnung. Das ist für diesen Randthemen-Kommentar vertretbar.
- **Sprache und Stimme:** Englisch folgt dem englischen Originalpost und der
  sichtbaren Diskussion. Die persönliche Einleitung „What stands out to me“, die
  verständliche Erklärung von selective disclosure und die nüchterne Grenze
  gegen Sicherheitsversprechen sind nahbar, fachlich und nicht werblich. Der
  bestätigte Stilscore `0.88` ist plausibel.
- **Studien- und Faktengrenzen:** Der Text begrenzt den Befund ausdrücklich auf
  Frankreich und Deutschland. Er übernimmt weder die Prozentwerte noch behauptet
  er EU-Repräsentativität, tatsächliche Adoption oder eine kausal bewiesene
  Wirkung. Die Kommunikationslücke ist als persönliche Einordnung formuliert.
  Selective disclosure wird nicht mit Signaturvalidierung, Identitäts- oder
  Berechtigungsprüfung gleichgesetzt.
- **Sicherheits-, Rechts- und Produktgrenzen:** Keine Hacking-Prävention,
  Datenschutz-, Sicherheits- oder Rechtsgarantie; vielmehr grenzt der Schlusssatz
  ein pauschales Sicherheitsversprechen ausdrücklich aus. Keine Swisscom- oder
  Produktbehauptung, keine Aussage zu BIV-Berechtigungen und keine erfundene
  Praxis-, Kunden- oder Biografieangabe.
- **CTA und Links:** Kein Link und kein Conversion-CTA. Das ist bei diesem bewusst
  nicht produktnahen Awareness-Kommentar korrekt; Website-, Demo-, DM- oder
  Produkt-CTA wären konstruiert und spamartig. Ein CTA ist für diesen Kommentar
  nicht verpflichtend.
- **Spam, Konkurrenz und Brand-Safety:** Keine werbliche Wiederholung, kein
  Competitor-Bashing, keine negative IDnow-/Namirial-Darstellung, kein
  Angstmarketing, keine Politik oder Religion.
- **Dubletten:** Keine exakte Dublette in Queue, Planung, Log oder Approved-Korpus.
  Die Stilprüfung bestätigt trotz thematischer Nähe zu früheren
  selective-disclosure-/Wallet-Kommentaren auch keine funktionale Dublette: Der
  eigenständige Kern ist das Verständnis des Offenlegungsumfangs und die Grenze
  zwischen einer Datenschutzfunktion und einem allgemeinen Sicherheitsversprechen.

## `comment-2026-09-22-0005`

- URL: `https://lnkd.in/p/eQgvWeW8`
- Separate URN: keine vorhanden; keine abgeleitet oder erfunden
- `fit_score`: `0.0`
- Einzelurteil: **ABGELEHNT**
- Pflichtänderung: **keinen Kommentar für diese Kampagne verfassen; `text: ''` beibehalten**

### Begründung

Der vollständige Originalpost ist eine beworbene Download-Anzeige zu einer
TikTok-/Instagram-Strategie. Er hat keinen konkreten Bezug zu digitaler Identität,
elektronischen oder digitalen Signaturen, signierten PDFs, Prüfung vor Archivierung
oder Freigabe, Records/ECM, Compliance Operations, Audit-Trail, Zertifikaten,
Signaturvalidierung oder BIV. Damit ist er ein generischer Social-Media-/Marketing-
und Digitalisierungstreffer ohne Kernthema-Verbindung und fällt unter die
Kampagnensperre für generische Digitalisierungsposts ohne konkreten Bezug.

Ein Kommentar könnte den Kampagnenfit nur erfinden oder ausserhalb der Kampagne
bleiben. Die konkrete `fit_note`, `fit_score: 0.0` und der exakte Leertext sind
daher richtig. Auf Textebene sind Stimme, CTA und Fakten nicht anwendbar; die
Sperre des Originalbeitrags ist nicht durch Umschreiben reparierbar. Der sichtbare
Queue-Block bleibt zu Recht als transparenter, ungekreuzter Sammelkandidat
erhalten, ohne daraus eine Freigabe oder Veröffentlichung abzuleiten.

## Queue-, Sortierungs- und Schutzstatus

- Die neuen Kandidaten stehen korrekt absteigend: `0.28 > 0.0`.
- IDs, URLs, Autoren, vollständige Notes, `fit_score` und `fit_note` stimmen mit
  den geprüften Übergaben überein; beide IDs und URLs kommen in der Queue jeweils
  genau einmal vor.
- Für beide Kandidaten ist keine separate URN vorhanden.
- Beide Freigabe-Checkboxen sind leer.
- 0004: **kampagnen-, fakten- und markensicher; intern FREIGEGEBEN**.
- 0005: **kampagnenseitig gesperrt; ABGELEHNT und leer zu belassen**.
- Gesamtstatus: **SICHER**, sofern Texte, Metadaten, Reihenfolge und Checkboxen
  unverändert bleiben.

Diese Reviewer-Freigabe ist **keine Nutzerfreigabe**. Sie berechtigt weder zum
Ankreuzen einer Queue-Checkbox noch zu Planung, Verschiebung, Operator-Aktion oder
Veröffentlichung. Queue, Texte, Scores, Notes, Checkboxen, Stil-/Lerndateien und
Planung wurden durch diese Prüfung nicht verändert.
