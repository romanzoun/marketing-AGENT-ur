# Reviewer-Prüfung — RV-FC-DV-20260923-R41

Datum: 2026-09-23  
Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`  
Prüfumfang: einmalige Prüfung der finalen Queue-Kandidaten `comment-2026-09-23-0004` und `comment-2026-09-23-0005`

## Deterministische Vorprüfung

Die Kampagne erlaubt maximal **500 Unicode-Codepoints** pro Kommentar und verlangt
**keine Pflicht-Hashtags** (`required_hashtags: []`).

| Kandidat | Codepoints | SHA-256 des exakten UTF-8-Texts | Hashtags | Links | Ergebnis |
|---|---:|---|---:|---:|---|
| `comment-2026-09-23-0004` | 255/500 | `b7f44df58b6218c54d8e500c50f8ede77402d5d8cb08f115de25af3bd88fefe3` | 0 | 0 | bestanden |
| `comment-2026-09-23-0005` | 0/500 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | 0 | 0 | Leertext bestätigt |

Der Text von 0004 ist identisch mit dem finalen Copywriter-Text und dem exakt
bewerteten Text der Stilprüfung. Der Stilstatus **0,84 BESTANDEN**, ohne
Pflichtrevision, ist bestätigt. 0005 enthält bewusst keinen Entwurf; das
eingehaltene Zeichenlimit und die leere Hashtag-Pflicht machen den gesperrten
Originalbeitrag nicht freigabefähig.

## `comment-2026-09-23-0004`

- URL: `https://lnkd.in/p/eXaGqFQk`
- `fit_score`: `0.34`
- Einzelurteil: **FREIGEGEBEN**
- Pflichtänderung: **keine**

### Begründung

- **Themenfit und Objective:** Der Kommentar bleibt im engen, zulässigen
  Awareness-Anschluss des Originalposts: Day-1-Readiness, technische Akzeptanz,
  QES und Governance werden direkt aufgegriffen; Zuständigkeiten und
  Ausnahmefälle sind eine plausible operative Einordnung. Der Text baut
  ausdrücklich keine künstliche Brücke zu signierten PDFs, Prüfung vor
  Archivierung/Freigabe, Records/ECM, Audit-Trail, Zertifikatsauswertung,
  Document Validator oder BIV. Der niedrige Teilfit `0.34` bleibt damit korrekt,
  aber nicht null.
- **Audience:** Finanzinstitute und Governance-/Compliance-/Digitalisierungsrollen
  überschneiden sich mit einem Teil der Kampagnenzielgruppe. Der Kommentar gibt
  nicht vor, den engeren Records-/Posteingang-/ECM-ICP oder einen konkreten
  Dokumentenprüfprozess abzudecken.
- **Sprache und Stimme:** Deutsch folgt dem deutschen Original. „für mich“ macht
  die Aussage persönlich, ohne eine unbelegte Kunden-, Praxis- oder
  Biografieerfahrung zu behaupten. Zwei verständliche Sätze, ein natürlicher
  Gedankenstrich und die nüchterne Prozessperspektive passen zur persönlichen,
  fachlichen und nicht werblichen Stimme. Der bestätigte Stilscore `0.84` ist
  plausibel.
- **CTA:** Kein Link und kein Conversion-CTA. Das ist für diesen nur bedingt
  passenden Awareness-Kommentar korrekt; Produkt-, Website-, Demo- oder DM-CTA
  würden eine nicht vorhandene DocVal-/BIV-Brücke konstruieren und spamartig
  wirken. Ein CTA ist hier nicht verpflichtend.
- **Fakten und Recht:** Der Kommentar behauptet weder eine gesetzliche
  2027-Frist noch eine regulatorische Pflicht, rechtliche Wirkung,
  Zeichnungsberechtigung, Datenschutz- oder Sicherheitsgarantie. Er setzt QES
  nicht mit Identitäts-, Berechtigungs-, SCA-, Transaktionsfreigabe- oder
  Signaturvalidierungsfunktionen gleich. Zuständigkeiten und Ausnahmefälle sind
  als persönliche Prozessbewertung formuliert, nicht als belegtes Ergebnis des
  Webcasts.
- **Produktgrenzen:** Keine Swisscom-, Document-Validator-, BIV-, Hash-,
  Fremd-Cloud- oder sonstige Produktbehauptung. Insbesondere werden keine
  Funktionen des Originalthemas auf DocVal/BIV übertragen.
- **Spam und Markensicherheit:** Kein Pitch, keine werbliche Wiederholung, kein
  Angstmarketing, keine Heils- oder Rechtsversprechen, kein Competitor-Bashing,
  keine Politik oder Religion. Der Kommentar ergänzt den Originalbeitrag um
  einen konkreten operativen Gedanken.
- **Dubletten:** Keine exakte Dublette im Lernstand oder Approved-Korpus. Die
  vorhandene allgemeine Themenfamilie „Technik allein reicht nicht“ wird hier
  eigenständig auf die Day-1-Betriebsreife von QES-Akzeptanz, Zuständigkeiten,
  Governance und Ausnahmewegen bezogen. Keine funktionale Dublette mit den
  nächstliegenden Governance-, Wallet- oder Records-Beispielen.

## `comment-2026-09-23-0005`

- URL: `https://lnkd.in/p/ePPZJmVe`
- `fit_score`: `0.0`
- Einzelurteil: **ABGELEHNT**
- Pflichtänderung: **keinen Kommentar für diese Kampagne verfassen; `text: ''` beibehalten**

### Begründung

Der vollständige Originalbeitrag ist eine beworbene Download-Anzeige zu
TikTok-ROI und Creator-First-Marketing. Er hat keinen konkreten Bezug zu digitaler
Identität, elektronischen oder digitalen Signaturen, QES, signierten PDFs,
Prüfung vor Archivierung oder Freigabe, Records/ECM, Compliance Operations,
Audit-Trail, Zertifikaten, Signaturvalidierung, Document Validator oder BIV.
Damit fällt er ausdrücklich unter das Kampagnen-No-Go **„generische
Digitalisierungsposts ohne konkreten Bezug“**.

Ein Kommentar könnte den Themen- und Audience-Fit nur erfinden oder ausserhalb
der Kampagne bleiben. `fit_score: 0.0`, die konkrete Sperrbegründung und der
exakte Leertext sind richtig. Stimme, CTA, Fakten und Produktgrenzen sind auf
Textebene nicht anwendbar; die Sperre des Originalbeitrags ist nicht durch eine
Textrevision reparierbar. Der sichtbare ungekreuzte Queue-Block bleibt zu Recht
als transparenter Sammelkandidat erhalten.

## Queue-, Sortierungs- und Schutzstatus

- Die beiden neuen Kandidaten stehen korrekt absteigend: `0.34 > 0.0`.
- IDs und URLs kommen in der Queue jeweils genau einmal vor; beide Blöcke
  enthalten genau ein `text:`-Feld.
- Beide Freigabe-Checkboxen sind leer.
- 0004: **kampagnen-, fakten- und markensicher; intern FREIGEGEBEN**.
- 0005: **kampagnenseitig gesperrt; ABGELEHNT und leer zu belassen**.

Diese Reviewer-Freigabe ist **keine Nutzerfreigabe**. Sie berechtigt weder zum
Ankreuzen einer Queue-Checkbox noch zu Planung, Verschiebung, Operator-Aktion
oder Veröffentlichung. Queue, Texte, IDs, URLs, Notes, Scores, Checkboxen,
Termine, Stil-/Lerndateien und Planung wurden durch diese Prüfung nicht verändert.
