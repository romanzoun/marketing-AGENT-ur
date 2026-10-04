# Reviewer-Prüfung RV-DV-20260913-R5-PRIMARY

## Prüfrahmen und Snapshot

Geprüft wurden ausschliesslich die unveränderten reinen Texte zwischen
`POST 1 BEGIN/END` und `POST 2 BEGIN/END` in
`team/copywriter/collected/document-validator-two-2026-09-13-r5-primary.md`.
Marker und direkt angrenzende Zeilenumbrüche gehören nicht zum Text. Unicode-
Zeichenzahl bedeutet Anzahl Unicode-Codepoints; interne Zeilenumbrüche zählen.
SHA-256 wurde über die UTF-8-Bytes des jeweiligen reinen Texts gebildet.

Verglichen wurde mit allen zum Prüfzeitpunkt vorhandenen Posts: acht in
`approvals.md` und zwei in `log.md`. Reproduzierbarer Datei-Snapshot:

- Ausgangsdatei: `ad931c3d31dc1942776325fe2306661da620a59e0adca59bbba6163c418b00f9`
- Stilbericht: `2bfdef63e6f833b6ee95a9017504c5505fad20d2ad4920226bfab451d3dd5f43`
- `approvals.md`: `804693f48639193ac7ed7db972281e826a1459e55d2f973518add115ec9a2e47`
- `log.md`: `253fa2bfb2b4ba2ad2385cea5abf1a11cc08fc23cbd59acf292b1fc67e607fc5`

Während der Abschlusskontrolle wurde `approvals.md` parallel und ohne Zutun
des Reviewers neu gespeichert (vorheriger Hash:
`23ec3f00300b5d47dfd31529ba8a86a202851efcc5fb8cfdadcbfb15154b7d7e`).
Der aktuelle Stand wurde deshalb erneut vollständig auf alle acht Post-Blöcke
geprüft. Beide unten genannten ID-/Text-/Hash-Treffer bestehen unverändert.
Auch die Ausgangsdatei wurde parallel um einen Identitätsnachweis ausserhalb
der Marker ergänzt (vorheriger Hash:
`9b50c4a2b5935ccdd79a2ab834043976d637ccbd007b8716eba39789cf9a9029`).
Beide reinen Markertexte blieben bei der erneuten Prüfung bytegenau unverändert;
massgeblich sind ihre separat ausgewiesenen Text-Hashes.

Die vorangegangene Stilprüfung ist bestanden: POST 1 mit `0,94`, POST 2 mit
`0,92`. Eine Stilfreigabe oder Reviewer-Bewertung ist keine Nutzerfreigabe.

## Deterministische Pflichtprüfung

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | Rest bis 1.300 | SHA-256 |
|---|---:|---:|---:|---:|---|
| POST 1 | 1.144 | 1.172 | 16 | 156 | `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97` |
| POST 2 | 1.203 | 1.217 | 19 | 97 | `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030` |

Beide Texte bestehen das Zeichenlimit von 1.300 Unicode-Codepoints.

In jedem Text kommen `#Compliance`, `#eIDAS` und `#RecordsManagement` jeweils
genau einmal vor. Der folgende CTA steht in jedem Text genau einmal, wort-,
zeichen- und zeilenumbruchgetreu:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

## Fakten- und Sicherheitsprüfung

Als aktuelle Primärquellen wurden am 2026-09-13 die offiziellen Swisscom-Seiten
zum [Document Validator](https://trustservices.swisscom.com/de/products/validator/document-validator)
und zum [Business Identity Validator](https://trustservices.swisscom.com/de/products/validator/business-identity-validator)
herangezogen.

- **Document Validator:** Die Aussagen zum lokal gebildeten Dokument-Hash, zum
  Verbleib der PDF in der eigenen Umgebung, zur Prüfung von Signaturdaten sowie
  zur Unterstützung ZertES-/eIDAS-signierter PDFs sind belegt. Die Texte behaupten
  weder Offline-Verarbeitung noch, dass gar keine Daten an Swisscom gehen.
- **BIV in POST 2:** Die vorsichtige Formulierung, BIV könne Kontext zu Zeichner,
  Unternehmen und Berechtigung ergänzen, passt zur offiziellen Rolle mit
  Unternehmensdaten, Zeichnungsberechtigten und unterzeichneten Dokumenten.
- **Menschliche Entscheidung:** Beide Texte trennen Prüfinformationen von der
  anschliessenden Entscheidung. Kein Produkt wird als rechtlicher Entscheider
  oder automatische Freigabeinstanz dargestellt.
- **Rechts-, Sicherheits-, Revisions- und Freigabegrenzen:** Keine Rechtsgarantie,
  keine Sicherheitsgarantie, keine automatische Revisionssicherheit und keine
  automatische Freigabe werden versprochen. POST 2 verneint juristische Sicherheit
  ausdrücklich; POST 1 beschränkt das Ergebnis auf Unterstützung.
- **Thema und enger ICP:** Signierte PDFs vor Freigabe/Archivierung, Records,
  Compliance sowie IT/Security und Legal Ops liegen innerhalb der Kampagne.
- **Stimme und CTA:** Persönliche Ich-Haltung, Regionalzug/stille Post sowie
  Stoppuhr/Klemmbrett sind bildhaft, nahbar und ohne Corporate-Heilsversprechen.
  Frage-CTA und Pflicht-CTA konkurrieren nicht problematisch miteinander.
- **Spam und Markensicherheit:** Ein sachlicher Produktlink, drei einschlägige
  Pflicht-Hashtags, keine Konkurrenzabwertung, keine erfundene Kundenerfahrung
  oder Biografie, keine Politik oder Religion. Bestanden.

## Dublettenabgleich mit allen Queue-/Log-Posts

Die acht älteren Bestandswinkel sind inhaltlich unterscheidbar: Fremd-Cloud/
Garderobe, Audit/Detektiv, LKW/API-Workflow, Browser-Cursor/Agent, Paketsiegel/
Berechtigung, grüner Haken im Nebel, BIV-Namensschild und grüner Haken/
Gepäckmarke. Gegen diese acht Winkel wären Regionalzug/stille Post und der
15-Minuten-Datenweg-Test ausreichend eigenständig.

Der aktuelle Gesamtbestand enthält jedoch zusätzlich zwei exakte Dubletten:

| Markertext | Exakter Treffer in `approvals.md` | Zeichenzahl | SHA-256 | Befund |
|---|---|---:|---|---|
| POST 1 | `post-2026-09-13-0001` | 1.144 | `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97` | byte- und textidentisch |
| POST 2 | `post-2026-09-13-0002` | 1.203 | `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030` | byte- und textidentisch |

Es gibt keine exakten Treffer in `log.md`. Weil beide Texte bereits als offene
Post-Jobs in `approvals.md` stehen, würde eine erneute Weitergabe oder Einreihung
denselben Inhalt doppelt in die Freigabe-Pipeline bringen.

## Urteile und Pflichtänderungen

### POST 1 — `abgelehnt`

Form, Kampagnenfit, Fakten, Produktrolle, Datenfluss, menschliche Entscheidung,
Grenzziehung, Stimme, CTA, Hashtags, Spam und Markensicherheit bestehen. Das
Gesamturteil lautet dennoch zwingend **`abgelehnt`**, weil der Text bereits exakt
als `post-2026-09-13-0001` in `approvals.md` vorhanden ist.

**Pflichtänderung:** Keine Textkorrektur. Nicht erneut einreichen oder per
`li-jobs add` einreihen. Den bereits bestehenden Queue-Job als alleinigen
Kandidaten behandeln. Falls ausdrücklich ein weiterer Kandidat benötigt wird,
muss der Copywriter einen tatsächlich neuen Winkel und neuen Text erstellen und
erneut durch Stil- und Reviewer-Prüfung geben.

### POST 2 — `abgelehnt`

Form, Kampagnenfit, Fakten, Produktrollentrennung, Datenfluss, menschliche
Entscheidung, Grenzziehung, Stimme, CTA, Hashtags, Spam und Markensicherheit
bestehen. Das Gesamturteil lautet dennoch zwingend **`abgelehnt`**, weil der Text
bereits exakt als `post-2026-09-13-0002` in `approvals.md` vorhanden ist.

**Pflichtänderung:** Keine Textkorrektur. Nicht erneut einreichen oder per
`li-jobs add` einreihen. Den bereits bestehenden Queue-Job als alleinigen
Kandidaten behandeln. Falls ausdrücklich ein weiterer Kandidat benötigt wird,
muss der Copywriter einen tatsächlich neuen Winkel und neuen Text erstellen und
erneut durch Stil- und Reviewer-Prüfung geben.

## Verbleibende Risiken und Prozessgrenzen

- Der Dublettenbefund ist an die oben dokumentierten Queue-/Log-Hashes gebunden.
  Eine parallele Neuspeicherung wurde bereits beobachtet. Vor jeder späteren
  Aktion muss der dann aktuelle Queue-Stand erneut gelesen werden.
- Die offiziellen Produktseiten belegen den beschriebenen Datenfluss und die
  Produktrollen, ersetzen aber keine anwendungsfallspezifische Rechts-, Security-
  oder Revisionsprüfung. Die Texte versprechen eine solche Garantie nicht.
- `posts_per_run: 1` bleibt die operative Veröffentlichungsgrenze. Dieses Review
  erteilt weder eine Nutzerfreigabe noch eine Publikationsberechtigung.

Ausgangstext, Queue, Checkboxen, Freigaben, Planung und LinkedIn wurden durch
diesen Review nicht verändert. Die beobachtete parallele Queue-Neuspeicherung
wurde nicht zurückgesetzt. Es wurde nichts veröffentlicht.
