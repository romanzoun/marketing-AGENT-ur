# RV-FR-DV-20261003-R5 — einmalige Reviewer-Prüfung

- Datum: 2026-10-03
- Kampagne: `DocVal + BIV — vor Archiv / vor Freigabe`, Version 2
- Scope: ausschließlich `reshare-2026-10-03-0001` und `reshare-2026-10-03-0002`
- Charakter: interne Reviewer-Entscheidung; keine Nutzerfreigabe und keine Veröffentlichungsberechtigung

## Deterministische Vorprüfung

Kampagnenregeln: `max_post_chars: 1300`, `required_hashtags: []`,
`reshares_per_run: 1`.

| ID | Text | SHA-256 | Pflicht-Hashtags | Checkbox | Statusfelder |
|---|---:|---|---|---|---|
| `reshare-2026-10-03-0001` | 439 Unicode-Codepoints / 446 UTF-8-Bytes | `d887fb22c99e97c16f80a66983a2a3f1d8f0987a2b851bc47f594bc26e2e889f` | keine; erfüllt | `- [ ] freigeben` | `approval_origin:null`, `publish_at:null`, `published_at:null`, `published_url:null` |
| `reshare-2026-10-03-0002` | exakt leer, 0 Unicode-Codepoints | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | keine; erfüllt | `- [ ] freigeben` | `approval_origin:null`, `publish_at:null`, `published_at:null`, `published_url:null` |

Beide IDs kommen in `approvals.md` jeweils genau einmal vor. Beide Ziel-IDs
fehlen vollständig in `schedule.md` und `log.md`. Das identische URL-Feld
`https://lnkd.in/p/eCxssRD5` kommt zweimal vor und ist bei 0002 technisch
verdächtig; es wurde weder korrigiert noch als Beleg für den Bloomberg-Post
behandelt. Die Entscheidungen sind deshalb zusätzlich an Autor und vollständige
`note` gebunden.

## `reshare-2026-10-03-0001`

**Interne Reviewer-Entscheidung: FREIGEGEBEN**

Bindung bestätigt:

- URL: `https://lnkd.in/p/eCxssRD5`
- Autor: `HSLU – Hochschule Luzern – Informatik`
- vollständige `note`: HSLU-Ankündigung des Digital Sovereignty Index 2026 mit
  Strategie/Governance, praktischer Umsetzung sowie Daten-, technologischer und
  operativer Souveränität; keine veröffentlichten Studienresultate
- `reshare_with_comment:true`
- `fit_score:0.76` und inhaltlich passende Fit-Note
- Style: `evaluation_score:0.88`, **BESTANDEN**, keine Pflichtrevision

Gründe:

- Der Originalbeitrag ist für DocVal/BIV allein breit, aber als strategischer
  Rahmen belastbar relevant: Er behandelt ausdrücklich die Lücke zwischen
  Strategie/Governance und operativer Umsetzung digitaler Souveränität.
- Der Begleittext liefert den erforderlichen engen Mehrwert für den ICP: ein
  sensibles signiertes PDF vor Freigabe oder Archivierung, die konkrete Frage
  nach dem Verlassen der eigenen Umgebung und die hash-basierte Validierung als
  kleinen operativen Baustein.
- Audience und Topics passen zu Records/ECM, Compliance, IT, Security und
  Datenschutz in konkreten Dokumentprüfprozessen. Damit ist es kein verbotener
  generischer Digitalisierungspost.
- Die Produktfakten bleiben innerhalb der Kampagne: Das PDF bleibt in der
  eigenen Umgebung; für die Validierung wird der Hash verwendet. Der Text
  behauptet weder Studienergebnisse noch Teilnahme/Partnerschaft, Kundenfälle,
  regulatorische Pflichten oder Rechts-, Sicherheits- bzw. Revisionsgarantien.
  BIV wird nicht künstlich angehängt.
- Stimme und Form sind persönlich, nahbar, konkret und nicht werblich. Die drei
  kurzen Absätze beginnen mit einer Ich-Perspektive und enden in einer sachlichen
  Einordnung; kein Spam, kein Competitor-Bashing und kein Angstmarketing.
- CTA ist passend zur Awareness-Strategie: kein eigener Produkt-, Demo-, DM-
  oder Link-CTA. Der Originalpost enthält bereits die natürliche
  Veranstaltungs-/Anmeldehandlung; ein zusätzlicher Conversion-CTA würde den
  fachlichen Reshare unnötig kapern. Die Kampagne verlangt den Standard-CTA nur
  bei klar sinnvoller Conversion-Nähe und hält ausdrücklich fest, dass nicht
  jeder Beitrag verkaufen muss.
- Keine exakte Textdubletten-Spur im Approved-Korpus, in `schedule.md` oder
  `log.md`; der wiederkehrende Hash-/Umgebungs-Fakt ist durch den spezifischen
  Souveränitätswinkel funktional eigenständig.

Keine Pflichtänderung. Diese Reviewer-Freigabe lässt Checkbox, Queue und
Planungsstatus ausdrücklich unverändert.

## `reshare-2026-10-03-0002`

**Interne Reviewer-Entscheidung: ABGELEHNT/GESPERRT**

Bindung bestätigt:

- unverändert verdächtige Doppel-URL: `https://lnkd.in/p/eCxssRD5`
- Autor: `Bloomberg Professional Services`
- vollständige `note`: beworbener Global Index Outlook zu Verteidigung,
  Energiesicherheit, AI, Fixed Income, Märkten und Portfolios
- `reshare_with_comment:false`
- `fit_score:0.0` und konkrete Sperr-Note
- Style: N/A (`evaluation_score:null`, `evaluation_note:''`,
  `evaluated_at:null`), da `text:''`

Gründe:

- Der Originalbeitrag hat keinen semantischen Kampagnenfit: keine signierten
  PDFs, ZertES/eIDAS, Signatur-/Zertifikatsauswertung, Hash-Prüfung,
  Freigabe/Archivierung, Records/ECM/DMS, Audit-Trail, Identitäts- oder
  Berechtigungsprüfung.
- Audience und Objective richten sich an Markt-/Portfoliointeressierte, nicht an
  den engen DocVal-/BIV-ICP in einer Dokumentprüfsituation.
- `AI` und `security` sind nur Randbegriffe des Markt-Ausblicks. Eine eigene
  Brücke zu DocVal/BIV wäre die verbotene generische Digitalisierung ohne
  konkreten Kernbezug und ein künstlicher Produkt-Pitch.
- Weder eigener Begleittext noch CTA sind zulässig. Auch ein ausdrücklicher
  Awareness-Reshare ohne Text scheidet aus, weil schon der Originalbeitrag nicht
  kampagnenrelevant ist.
- Der Leertext muss exakt leer bleiben. Keine Copywriter-Rückgabe zur bloßen
  Umschreibung; für eine spätere Prüfung wäre ein anderer, natürlich passender
  Originalbeitrag erforderlich.

## Queue-Schutz und Dateistand

- `approvals.md`, `schedule.md` und `log.md` wurden durch den Reviewer nicht
  verändert.
- Beide Checkboxen blieben offen; keine Nutzerfreigabe, kein Termin, keine
  Verschiebung, keine Veröffentlichung.
- Keine Browser-, LinkedIn-, Operator- oder Folgeagentenaktion.
- Queue-Hashes am Prüfstand:
  - `approvals.md`: `360a59c0b23122176c2e491de26b3b762843d79c9866267bb59f1b9fe688aac7`
  - `schedule.md`: `7740777329c3eea295e99cdc4b9fc898af31da802226b210061a470cf3c90c75`
  - `log.md`: `eebd33040ddca17ace7d8487182c9ace31ef22fa3cd5873284fe5fa670c3afce`

Ergebnis des Limits `reshares_per_run:1`: Genau 0001 ist der verbleibende intern
freigegebene Kandidat; 0002 bleibt sichtbar gesperrt. Eine Reviewer-Freigabe ist
keine Nutzerfreigabe und berechtigt nie zum Veröffentlichen.
