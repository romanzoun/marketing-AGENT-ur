# Reviewer-Prüfung RV-DV-20260913-R5

Geprüft wurden ausschließlich die unveränderten Texte zwischen `POST 1
BEGIN/END` und `POST 2 BEGIN/END` in
`team/copywriter/collected/document-validator-two-2026-09-13-r5.md`.
Maßstab waren die aktive Kampagne, das persönliche Profil, das Stilprofil, der
leere Lernstand, der aktuelle Approved-Korpus, die Reviewer-Regeln sowie alle
acht bestehenden Posttexte in `approvals.md` und `log.md`. Die Stilvorprüfung
mit 0,94 beziehungsweise 0,92 wurde berücksichtigt, ersetzt aber nicht diese
unabhängige Prüfung.

## Deterministische Pflichtprüfung

Gezählt wurden Unicode-Codepoints des reinen Markertexts inklusive interner
Zeilenumbrüche; Marker und die direkt angrenzenden Trenn-Zeilenumbrüche wurden
nicht mitgezählt.

| Text | Unicode-Codepoints | Interne Zeilenumbrüche | Limit | Rest | Pflicht-Hashtags | Vollständiger CTA | Exakter UTM-Link | SHA-256 |
|---|---:|---:|---:|---:|---|---:|---:|---|
| POST 1 | 1.144 | 16 | 1.300 | 156 | `#Compliance`, `#eIDAS`, `#RecordsManagement` je genau 1× | 1× | 1× | `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97` |
| POST 2 | 1.203 | 19 | 1.300 | 97 | `#Compliance`, `#eIDAS`, `#RecordsManagement` je genau 1× | 1× | 1× | `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030` |

Beide Hashes stimmen mit dem Stilbericht überein. Beide Texte sind gültiges
UTF-8 und enthalten weder CR-Zeichen, Unicode-Ersatzzeichen, nachlaufende
Leerzeichen noch zusätzliche Vorkommen des UTM-Links. Der vollständige
Kampagnen-CTA steht in beiden Texten exakt einmal in dieser dreizeiligen Form:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

## Abgleich gegen die acht bestehenden Postwinkel

| Bestands-ID | Bestandswinkel | Abgrenzung POST 1 | Abgrenzung POST 2 |
|---|---|---|---|
| `post-2026-09-10-0001` (Log) | grüner Haken/Gepäckmarke, Audit-Trail | Übergabeverlust statt Statussignal | zeitlich begrenzte Prozess-Generalprobe statt Haken/Audit-Trail |
| `post-2026-09-10-0002` (Log) | Namensschild, BIV und geschäftlicher Kontext | keine Identitäts-/Berechtigungsmetapher | BIV nur als eine von vier Prüffragen, Hauptwinkel ist der gemeinsame Prozesstest |
| `post-2026-09-11-0001` | Fremd-Cloud und erlaubter Datenweg | Übergaben und Bedeutungsverlust statt Cloudziel | inhaltliche Berührung beim Datenweg, aber eigenständige Demo-/Prüfmethode mit vier Rollenfragen statt Cloudwarnung |
| `post-2026-09-11-0002` | höflicher Audit-Detektiv, spätere Erklärbarkeit | inhaltliche Berührung bei Nachvollziehbarkeit, aber Fokus auf Vertrauensverlust an aktuellen Übergaben statt Rückschau im Audit | Generalprobe vor Einsatz statt rückblickende Audit-Erklärung |
| `post-2026-09-12-0001` | LKW, fester API-Prüfschritt | keine API-/Skalierungs- oder LKW-Erzählung | kein Integrations- oder API-Winkel |
| `post-2026-09-12-0002` | Browser-Cursor, AI-Agent versus Mensch | keine Agentenfrage | menschliche Entscheidung als Guardrail, aber kein Agent-/Browser-Identitätswinkel |
| `post-2026-09-12-0003` | Paketsiegel, Signatur versus Berechtigung | keine Siegel-/BIV-Rollentrennung | BIV-Kontext wird korrekt erwähnt, aber nur innerhalb eines breiteren End-to-End-Tests |
| `post-2026-09-12-0004` | grüner Haken im Nebel, sichtbare Prüftiefe | Übergabekette statt Haken/Prüfdetails | vier konkrete Prozessfragen statt Statussignal-/Revisionswinkel |

Es liegt weder eine Text-/Hash-Dublette noch eine bloße Neuverpackung eines
einzelnen Bestandswinkels vor. POST 1 führt den eigenständigen, in der Kampagne
ausdrücklich vorgesehenen „stille Post“-Winkel an System- und
Organisationsübergaben aus. POST 2 verbindet die fachlichen Prüfpunkte als
konkrete 15-Minuten-Generalprobe für IT/Security, Records und Legal Ops. Die
inhaltlichen Berührungen mit Datenweg, Nachvollziehbarkeit und BIV sind für die
Kampagnenkonsistenz nötig und kippen nicht in eine Dublette.

## POST 1 — Regionalzug und stille Post

**Urteil: FREIGEGEBEN**

**Zwingende Änderungen: keine.**

- **Deutsch, enger ICP und Thema:** Der Text adressiert einen Kontrollpunkt vor
  Freigabe oder Archivierung und nennt Records- und Compliance-Teams. Er bleibt
  bei eingehenden signierten PDFs und weitet die Zielgruppe nicht pauschal auf
  alle Backoffice-Teams aus.
- **Persönliche Stimme:** Regionalzug, „stille Post“, die zugespitzte
  Bedeutungsverschiebung und „Mein Lieblingssatz ... Also: überhaupt nicht“
  ergeben eine erkennbare Ich-Stimme mit trockenem Humor, ohne Werbesprech.
- **Fakten und Datenfluss:** Der Swisscom Document Validator wird korrekt der
  belastbareren Prüfung von Signatur- und Zertifikatsinformationen bei
  ZertES-/eIDAS-signierten PDFs zugeordnet. Die PDF bleibt in der eigenen
  Umgebung; ihr Hash wird lokal gebildet.
- **Menschliche und rechtliche Grenze:** Das Prüfergebnis unterstützt Teams,
  trifft ausdrücklich keine rechtliche Entscheidung und gibt nichts
  automatisch frei. Der zuständige Mensch entscheidet. Es wird weder
  Revisionssicherheit noch eine juristische Garantie versprochen.
- **CTA, Spam und Markensicherheit:** Die Publikumsfrage und der einmalige
  Pflicht-CTA sind sachlich und einladend. Keine erfundene Biografie oder
  Kundengeschichte, keine Konkurrenzabwertung, keine Politik oder Religion.

## POST 2 — 15-Minuten-Prozesstest

**Urteil: FREIGEGEBEN**

**Zwingende Änderungen: keine.**

- **Deutsch, enger ICP und Thema:** IT/Security, Records und Legal Ops werden
  konkret über PDF-Ablage, Datenfluss, Signatur-/Zertifikatsauswertung und
  Entscheidungsverantwortung angesprochen. Der Test liegt eng auf dem
  Prüfprozess vor Freigabe oder Archivierung.
- **Persönliche Stimme:** „Ich würde“, „Meine Generalprobe“, Folienschlacht,
  Stoppuhr und Klemmbrett bilden eine persönliche, greifbare und leicht
  selbstironische Erzählung. Der 15-Minuten-Rahmen beschreibt die vorgeschlagene
  Beobachtungsdauer, nicht eine unbelegte Produktleistung.
- **Fakten, Produktrollen und Datenfluss:** Beim Document Validator bleibt die
  PDF in der eigenen Umgebung und ihr Hash wird lokal gebildet. DocVal wird
  korrekt der belastbareren Prüfung von ZertES-/eIDAS-signierten PDFs sowie
  ihrer Signatur- und Zertifikatsinformationen zugeordnet. BIV kann getrennt
  davon Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen.
- **Menschliche und rechtliche Grenze:** Die Stoppuhr misst ausdrücklich den
  Datenweg und keine juristische Sicherheit. Die Produkte liefern
  Prüfinformationen; Freigabe oder Ablehnung bleibt beim zuständigen Menschen.
  Keine automatische Freigabe, Rechtsgarantie oder behauptete
  Revisionssicherheit.
- **CTA, Spam und Markensicherheit:** Die Schlussfrage und der einmalige CTA
  sind relevant und nicht drängend. Keine erfundene Demo-Erfahrung, keine
  Konkurrenzabwertung und keine verbotenen Themen.

## Abschluss

- POST 1: **FREIGEGEBEN**, keine zwingende Änderung.
- POST 2: **FREIGEGEBEN**, keine zwingende Änderung.

Diese Reviewer-Freigaben sind ausdrücklich **keine Nutzerfreigaben** und
berechtigen weder zum Einplanen noch zum Veröffentlichen. `posts_per_run: 1`
bleibt die spätere operative Obergrenze je Lauf/Zyklus. Entwurfsdatei, Queue,
Checkboxen, Freigaben, Planung, Operator und LinkedIn blieben unverändert.
