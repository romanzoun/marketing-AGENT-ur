# Reviewer-Prüfung RV-DV-20260912-R3-CLOSE

Geprüft wurden ausschließlich die beiden Textblöcke zwischen
`POST-1-START/END` und `POST-2-START/END` in
`team/copywriter/collected/document-validator-two-2026-09-12-r3-close.md`.
Maßstab waren die aktive Kampagne, das persönliche Profil, das Stilprofil und
die Reviewer-Regeln. Der vorgelagerte Stilbericht wurde berücksichtigt, ersetzt
aber nicht diese unabhängige Prüfung.

## Deterministische Pflichtprüfung

Die Unicode-Zeichen wurden direkt aus den markierten Textblöcken inklusive
interner Zeilenumbrüche und ohne Markierungszeilen gezählt.

| Text | Unicode-Zeichen | Maximum | Rest | Pflicht-Hashtags | Weitere Hashtags | Exakter UTM-Link | Vollständiger CTA |
|---|---:|---:|---:|---|---:|---:|---:|
| POST 1 | 1.244 | 1.300 | 56 | `#Compliance`, `#eIDAS`, `#RecordsManagement` je 1× | 0 | 1× | 1× |
| POST 2 | 1.277 | 1.300 | 23 | `#Compliance`, `#eIDAS`, `#RecordsManagement` je 1× | 0 | 1× | 1× |

Beide Texte bestehen Zeichenlimit, die Vorgabe **genau der drei**
Pflicht-Hashtags sowie den vollständigen Kampagnen-CTA einschließlich dieses
exakten Links:

`https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice`

## POST 1 — Der feste Prüfschalter

**Urteil: freigegeben**

- **Thema und enger ICP:** Der Text behandelt wiederholbare Prüfung signierter
  PDFs vor Freigabe/Archivierung im Records-/ECM-Workflow. Records-,
  Posteingang- und Vertragsadmin-Teams werden konkret angesprochen; keine
  pauschale Backoffice-Zielgruppe.
- **Sprache und Stimme:** Deutsch, persönliche Ich-Haltung, gut geführtes
  LKW-Bild und zurückhaltender Humor. Fachlicher Mittelteil bleibt verständlich
  und frei von Buzzword-Bingo.
- **Fakten und Produktrollen:** Die Aussagen zu API-Einbindung,
  ZertES-/eIDAS-Signatur- und Zertifikatsauswertung, lokaler Hashbildung und dem
  Verbleib der PDF in der eigenen Umgebung sind von der Kampagne gedeckt. Der
  Document Validator wird nicht als Rechtsentscheider oder Freigabeinstanz
  dargestellt; die menschliche Verantwortung ist ausdrücklich abgegrenzt.
- **CTA, Spam und Markensicherheit:** Konkrete Publikumsfrage plus vollständiger
  Pflicht-CTA wirken einladend und nicht drängend. Keine Garantien,
  Heilsversprechen, Konkurrenzangriffe, politischen oder religiösen Inhalte.

**Pflichtänderungen:** keine.

## POST 2 — Wer klickt da?

**Urteil: freigegeben**

- **Thema und enger ICP:** Der Kampagnentopik AI-Agent-vs.-Mensch wird direkt
  mit Nachweisen, Verantwortlichkeit sowie Freigabe-/Archivierungsprozessen für
  Records- und Compliance-Teams verbunden. Die Ansprache bleibt damit eng genug.
- **Sprache und Stimme:** Deutsch, klare persönliche Haltung, kurze Fragen und
  ein zusammenhängendes Cursor-/Ausweis-/Schnurrbart-Bild mit glaubwürdigem
  Augenzwinkern.
- **Fakten und Produktrollentrennung:** Der Document Validator ist korrekt der
  signierten PDF und Zertifikatsauswertung zugeordnet; BIV ergänzt Zeichner-,
  Unternehmens- und Berechtigungskontext. Der Text behauptet ausdrücklich
  nicht, dass eines der Produkte den Browserbediener erkennt oder die
  menschliche Freigabe ersetzt. Keine unbelegte Biografie oder Kundengeschichte.
- **CTA, Spam und Markensicherheit:** Konkrete Fachfrage plus vollständiger
  Pflicht-CTA; keine aggressive Wiederholung, keine verbotenen Themen und keine
  juristische Garantie oder sonstige Produktüberhöhung.

**Pflichtänderungen:** keine.

## Abschluss

Beide Posts sind reviewer-seitig **freigegeben**. Diese Freigabe ist
ausdrücklich **keine Nutzerfreigabe** und berechtigt weder zur Planung noch zur
Veröffentlichung. Bei `posts_per_run: 1` dürfte operativ ohnehin höchstens ein
Post je Zyklus veröffentlicht werden. Ausgangstexte, Queue-Dateien, Checkboxen,
Stilprofil, `learning.json` und Approved-Korpus blieben unverändert.
