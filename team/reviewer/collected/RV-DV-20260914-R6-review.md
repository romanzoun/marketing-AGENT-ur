# Reviewer-Prüfung RV-DV-20260914-R6

## Prüfrahmen und Snapshot

Geprüft wurden ausschliesslich die zwei reinen Texte zwischen
`POST-1-START/END` und `POST-2-START/END` in
`team/copywriter/collected/document-validator-two-2026-09-14-r6.md`.
Marker und die direkt angrenzenden Zeilenumbrüche gehören nicht zum Text.
Unicode-Zeichenzahl bedeutet Anzahl Unicode-Codepoints; interne Zeilenumbrüche
zählen. SHA-256 wurde über die UTF-8-Bytes des jeweiligen reinen Textes
gebildet.

Massgebliche Dateien beim Abschlussabgleich:

- Ausgangsdatei: `4cb730a2846d228b57bcb267fee44387d86ff237c282f87e2543b413fa56d10d`
- R6-Ideen: `63e3156d5e870662cd651fc56ca290abb7fb419ad4752a5270ee5a90fdb71147`
- Stilbericht: `2bf86bd3134fbd1d494dba93d9dfeb9c8c8ab0b64f62c55f8c6d71d807816e4e`
- `approvals.md`: `4c5879893f1c2b7163cdf2d2731f7f15034e43bbf295454145cf02857462843b`
- `schedule.md`: `77058f6ecf5f46538f41abc67f607caea2d3600bf7f29cd2e3b90a2da360f1f3`
- `log.md`: `0519c350812a3cd0f62deac5b4ed9c87b5ffe9cd60f211f0e8d35e4c5ef08122`

Während des Reviews wurde `approvals.md` parallel und ohne Zutun des Reviewers
von 829 auf 942 Zeilen erweitert; der SHA-256 änderte sich von
`63b07c68c85968ef71070c7c12bdbbc315ef08a79a36cc689ee62d3ef67e294e`
auf den oben ausgewiesenen aktuellen Wert. Die Ergänzung betraf neue
Kommentar-Kandidaten; die vier offenen Post-Blöcke blieben bestehen. Der
Dublettenabgleich wurde deshalb gegen den aktuellen Gesamtbestand wiederholt.

Die vorangegangene Stilprüfung ist bestanden: POST 1 mit `0,95`, POST 2 mit
`0,94`. Ein Stilurteil oder Reviewer-Urteil ist keine Nutzerfreigabe.

## Deterministische Pflichtprüfung

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | Rest bis 1.300 | SHA-256 |
|---|---:|---:|---:|---:|---|
| POST 1 | 1.260 | 1.272 | 16 | 40 | `9eca69480571dead35940a5820f2601bde31b07dfcdf0a0b543becae234f1c47` |
| POST 2 | 1.258 | 1.270 | 14 | 42 | `22a16907a568e82026d6ac1b4836d5b4797f6a37dc3529a49405c6addead18c6` |

Beide Texte bestehen das Limit von 1.300 Unicode-Codepoints. Die im Auftrag
erwarteten Textidentitäten sind exakt bestätigt.

In jedem Text kommen `#Compliance`, `#eIDAS` und `#RecordsManagement` jeweils
genau einmal vor. Der folgende Kampagnen-CTA steht in jedem Text genau einmal,
vollständig sowie wort-, zeichen- und zeilenumbruchgetreu:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

Jeder Text enthält genau diesen einen Link. Die deterministischen Pflichtpunkte
Zeichenlimit, CTA und Pflicht-Hashtags sind damit für beide Texte bestanden.

## Inhaltliche Prüfung

### POST 1 — Flughafen-Sicherheitskontrolle und Ausnahmeweg

- **Sprache und Stimme:** Klares Deutsch, persönliche Ich-Perspektive,
  anschauliche Sicherheitskontrolle und trockene Pointe. Kein Marketing-Sprech.
- **Enger ICP und Kampagnenthema:** Regelmässig eingehende signierte PDFs,
  Records-/Posteingang, Vertragsadministration und Compliance/Legal Ops sowie
  der Ausnahmeweg vor Freigabe oder Archivierung sind klar benannt.
- **Produktrolle und Datenfluss:** Der Document Validator wird auf die Prüfung
  ZertES-/eIDAS-signierter PDFs sowie Signatur- und Zertifikatsinformationen
  begrenzt. Die PDF bleibt in der eigenen Umgebung; ihr Hash wird lokal
  gebildet. Weder Offline-Verarbeitung noch ein vollständig lokales Produkt
  werden behauptet.
- **Menschliche, rechtliche und automatische Grenze:** Der Text verneint eine
  juristische Garantie und eine automatische Sperre des Archivschritts. Er
  ordnet Stoppen, Beurteilen, Dokumentieren sowie Freigabe/Archivierung dem Team
  beziehungsweise einem verantwortlichen Menschen zu.
- **Fakten, Biografie und Sicherheit:** Keine erfundene Fehlerklasse, keine
  Kundengeschichte oder unbelegte biografische Behauptung. Keine Rechts-,
  Compliance-, Sicherheits- oder Revisionsgarantie. Keine Konkurrenzabwertung,
  Politik oder Religion.
- **Spam:** Ein sachlicher Kampagnenlink, drei vorgeschriebene Hashtags und eine
  passende Gesprächsfrage; keine Link- oder Hashtag-Häufung.

### POST 2 — Agenten-Handover, Mandat und menschliche Verantwortung

- **Enger ICP und Kampagnenthema:** Der Text bindet AI-Agenten konkret an die
  Prüfung einer signierten PDF, die Auswertung und den nächsten Prozessschritt.
  Der Nachweis vor dem Weiterhandeln adressiert Records-/Compliance-Prozesse,
  nicht pauschal alle Backoffice-Tätigkeiten.
- **Produktrollen und Datenfluss:** Der Document Validator bleibt auf signierte
  PDFs sowie Signatur- und Zertifikatsinformationen begrenzt. Der BIV kann nur
  Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen. PDF-Verbleib in
  der eigenen Umgebung und lokal gebildeter Hash sind korrekt und ohne
  weitergehende Datenflussgarantie formuliert.
- **Mensch-/Agent-/Mandatsgrenze:** Der Text behauptet ausdrücklich nicht, die
  Produkte könnten den Browser-Bediener als Mensch oder Agent erkennen. Sie
  erteilen dem Agenten weder Mandat noch Berechtigung und ersetzen keine
  menschliche Freigabe. Die Verantwortung für den nächsten Schritt bleibt beim
  Menschen.
- **Juristische und automatische Grenze:** Es gibt keine Rechtsgarantie und
  keine Behauptung automatischer Freigabe, Ablehnung, Compliance oder
  Revisionssicherheit. Die Produkte liefern Prüfinformationen beziehungsweise
  Kontext, nicht die Prozessentscheidung.
- **Stimme, Biografie, Spam und Brand-Safety:** Schnurrbart, Übergabezettel und
  Staffelstab ergeben einen persönlichen, eigenständigen Bildbogen. Keine
  erfundene Erfahrung oder Biografie, keine Konkurrenzabwertung, kein
  Heilsversprechen und keine verbotenen Themen. Link- und Hashtag-Einsatz sind
  unauffällig.
- **Deutsch:** Die Kongruenz in `Weder der Document Validator noch der BIV
  erkennt, ob ...` ist kein Pflichtfehler. Bei zwei singularischen, mit
  `weder ... noch` verbundenen Subjektteilen sind nach der deutschen
  Referenzgrammatik Singular und Plural möglich. `erkennen` wäre eine mögliche
  stilistische Glättung, `erkennt` ist aber grammatisch zulässig und erzwingt
  keine Textrevision.

## Dublettenabgleich

Der aktuelle Bestand enthält neun Posts: vier in `approvals.md`, drei in
`schedule.md` und zwei in `log.md`. Ihre Winkel sind BIV-Namensschild,
grüner Haken/Gepäckmarke, Fremd-Cloud/Garderobe, Audit/Detektiv,
LKW/API-Workflow, Paketsiegel/Berechtigung, grüner Haken im Nebel,
Regionalzug/stille Post und 15-Minuten-Datenweg-Test.

- **POST 1** ist mit der Flughafen-Sicherheitskontrolle und dem ausdrücklich
  organisatorischen Ausnahmeweg bei unklarem Prüfergebnis eigenständig. Es
  wiederholt weder den grünen-Haken- noch den Audit- oder Datenweg-Winkel.
- **POST 2** ist mit angeklebtem Schnurrbart, Übergabezettel, konkreter
  Mensch-/Agent-Erkennbarkeitsgrenze und Mandatsübergabe eigenständig. Der
  allgemeine Agentenbezug einzelner Kommentare macht ihn nicht zur Dublette
  eines vorhandenen Postwinkels.

Keiner der beiden Markertexte ist als Posttext im aktuellen Queue-/Schedule-/
Log-Bestand vorhanden. Der Dublettencheck ist für beide bestanden.

## Urteile und Pflichtänderungen

### POST 1 — `FREIGEGEBEN`

Zeichenlimit, Textidentität, exakter CTA, Pflicht-Hashtags, Sprache, enger ICP,
Kampagnenthema, Produktrolle, lokaler Hash/PDF-Verbleib, menschliche und
juristische Grenzen, Stimme, Fakten, Biografie, Spam, Brand-Safety und
Dublettenabgrenzung bestehen.

**Pflichtänderung:** keine.

### POST 2 — `FREIGEGEBEN`

Zeichenlimit, Textidentität, exakter CTA, Pflicht-Hashtags, Sprache, enger ICP,
Kampagnenthema, Produktrollentrennung, Datenfluss, Mensch-/Agent-/Mandatsgrenze,
menschliche Freigabe, Fakten, Biografie, Stimme, Spam, Brand-Safety und
Dublettenabgrenzung bestehen.

**Pflichtänderung:** keine. Die Pluralform `erkennen` wäre rein optional; sie
ist keine Voraussetzung für dieses Urteil, das für die unveränderte Fassung mit
1.258 Codepoints und SHA-256
`22a16907a568e82026d6ac1b4836d5b4797f6a37dc3529a49405c6addead18c6` gilt.

## Prozessgrenze

Diese Reviewer-Freigabe ist ausdrücklich keine Nutzerfreigabe und berechtigt
weder zum Einreihen noch zum Planen oder Veröffentlichen. `posts_per_run: 1`
bleibt die operative Veröffentlichungsgrenze pro Zyklus.

Ausgangstexte, Queue, Checkboxen, Freigaben, Termine, Planung und LinkedIn
wurden durch diesen Review nicht verändert. Es gab keine `li-jobs`-, Operator-,
Veröffentlichungs- oder LinkedIn-Aktion.
