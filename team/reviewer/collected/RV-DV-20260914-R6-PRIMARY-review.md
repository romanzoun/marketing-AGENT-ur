# Reviewer-Prüfung RV-DV-20260914-R6-PRIMARY

## Prüfrahmen und Snapshot

Geprüft wurden ausschliesslich die zwei unveränderten reinen Texte zwischen
`POST-1-START/END` und `POST-2-START/END` in
`team/copywriter/collected/document-validator-two-2026-09-14-r6-primary.md`.
Marker und die direkt angrenzenden Zeilenumbrüche gehören nicht zum Text;
interne Zeilenumbrüche zählen als Unicode-Codepoint. SHA-256 wurde über die
UTF-8-Bytes des jeweiligen reinen Markertexts gebildet.

Die vorangegangene Stilprüfung ist mit `0,88` für POST 1 und `0,95` für
POST 2 bestanden. Ihre Text-Hashes stimmen mit den unten unabhängig ermittelten
Hashes überein. Eine Stil- oder Reviewer-Prüfung ist keine Nutzerfreigabe.

Reproduzierbarer Datei-Snapshot beim Abschlussabgleich:

- Ausgangsdatei: `2091274ffebe815a7a4b85b7e334064132b56fe26028fd7ca432908e141a938b`
- Stilbericht: `8234c0c4090eeac7f8ba42a833ec733ad52dab3f06cde56854a4df485b7a8b29`
- `approvals.md`: `c204e9afcd466fe88be1c99dedce02ac4750d417a037db8cdb734d2360963fd1`
- `schedule.md`: `c0a544065e0e9b507ae6b7b9328da844bd71393f22b20fc1876fbad4d89e11df`
- `log.md`: `0519c350812a3cd0f62deac5b4ed9c87b5ffe9cd60f211f0e8d35e4c5ef08122`

## Deterministische Pflichtprüfung

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | Rest bis 1.300 | SHA-256 |
|---|---:|---:|---:|---:|---|
| POST 1 | 1.276 | 1.287 | 18 | 24 | `2a3bb5af37117dd409c052eb0f19f238fd6c65d563949e51e82e97bf36c3be3c` |
| POST 2 | 1.284 | 1.299 | 21 | 16 | `a42b6ddb1049f7b0a1b2b48d2c70b79e1e867578033cb4418dc6b0ac80553797` |

Beide Texte bestehen das Limit von 1.300 Unicode-Codepoints.

In jedem Text kommen ausschliesslich die drei Pflicht-Hashtags `#Compliance`,
`#eIDAS` und `#RecordsManagement` vor, jeweils genau einmal. Der folgende
Kampagnen-CTA steht in jedem Text genau einmal, vollständig sowie wort-,
zeichen- und zeilenumbruchgetreu:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

Jeder Text enthält genau diesen einen Link. Zeichenlimit, CTA und
Pflicht-Hashtags sind damit für beide Texte bestanden.

## Fakten- und Produktgrenzen

Als aktuelle Primärquellen wurden am 2026-09-14 die offiziellen Swisscom-Seiten
zum [Document Validator](https://trustservices.swisscom.com/de/products/validator/document-validator)
und zum [Business Identity Validator](https://trustservices.swisscom.com/de/products/validator/business-identity-validator)
gegengeprüft.

- Der Document Validator unterstützt ZertES-/eIDAS-signierte PDFs, erstellt den
  Hash lokal beziehungsweise im eigenen Workflow und sendet nicht die
  vollständige PDF. Die Formulierung, die PDF bleibe in der eigenen Umgebung und
  ihr Hash werde lokal gebildet, ist damit gedeckt.
- Swisscom beschreibt die Validierung der Signaturdaten und die Rückgabe eines
  Ergebnisses an den Prozess. Beide Posts bleiben vorsichtig bei einer
  belastbareren Signatur- und Zertifikatsauswertung und behaupten weder eine
  Offline-Lösung noch, dass überhaupt keine Daten an Swisscom gehen.
- Der BIV prüft Unternehmensdaten und Zeichnungsberechtigungen und validiert
  Dokumente. POST 2 beschränkt ihn zutreffend auf möglichen Kontext zu Zeichner,
  Unternehmen und Berechtigung.

## Inhaltliche Prüfung

### POST 1 — Flughafen-Ausnahmeweg

- **Sprache, ICP und Thema:** Klares Deutsch; Records/Posteingang,
  Vertragsadministration und Compliance/Legal Ops sind eng adressiert. Die
  Situation liegt konkret vor Freigabe oder Archivierung einer signierten PDF.
- **Stimme:** Flughafen-Schale, Piepen und das kurze Zuständigkeitszögern ergeben
  einen nahbaren, trockenen Bildbogen. Die Ich-Perspektive und die Praxisfrage
  passen zum Stilprofil; kein Corporate- oder Buzzword-Sprech.
- **Prozess-, Rechts- und Revisionsgrenze:** Die Auswertung wird ausdrücklich
  nicht mit dem organisatorischen Ausnahmeweg verwechselt. Der Text verneint
  Rechtsgarantie sowie automatisch entstehende Compliance, Freigabe und
  Revisionssicherheit und ordnet die Entscheidung einem Menschen zu.
- **Fakten und Brand-Safety:** Keine erfundene Fehlerklasse, automatische Sperre,
  Kundengeschichte oder Biografie. Keine Konkurrenzabwertung, kein
  Heilsversprechen, keine Politik oder Religion.
- **Spam:** Ein sachlicher Produktlink, genau drei einschlägige Pflicht-Hashtags
  und eine passende Gesprächsfrage; keine Link-, Hashtag- oder CTA-Häufung.

### POST 2 — Agenten-Handover und Mandat

- **Sprache, ICP und Thema:** Klares Deutsch. AI-Agent, Browser,
  signierte PDF, Prüfauswertung und nächster Prozessschritt sind konkret
  verbunden; der Text weitet die Zielgruppe nicht pauschal auf alle
  Backoffice-Tätigkeiten aus.
- **Stimme:** Angeklebter Schnurrbart, Staffelstab und Übergabezettel bilden
  eine konsistente, persönliche Metapher mit Augenzwinkern. Die Schlussfrage
  lädt zu einem echten Praxisvergleich ein.
- **Produktrollen:** Document Validator und BIV bleiben sauber getrennt. Keines
  der Produkte wird als Entscheider, Freigabestelle oder Mandatsgeber dargestellt.
- **Mensch-/Agent-Erkennung und Berechtigung:** Der Text sagt explizit, dass
  weder Document Validator noch BIV erkennen, ob ein Mensch oder Agent den
  Browser bedient. Ebenso explizit erteilen sie keinem Agenten Mandat oder
  Berechtigung und ersetzen keine menschliche Freigabe. Die geforderte
  Spezialgrenze ist damit vollständig erfüllt.
- **Rechts-, Compliance- und Revisionsgrenze:** Es gibt keine juristische
  Garantie und keine Behauptung automatischer Compliance, Freigabe,
  Ablehnung oder Revisionssicherheit. Ziel und Prozessverantwortung bleiben
  menschlich.
- **Fakten, Spam und Brand-Safety:** Keine erfundene Produktfunktion,
  Kundengeschichte oder Biografie; keine Konkurrenzabwertung, verbotenen Themen
  oder Heilsversprechen. Link und Hashtags sind unauffällig.

## Dublettenabgleich

Der aktuelle Bestand enthält keine Posts in `approvals.md`, sieben Posts in
`schedule.md` und zwei Posts in `log.md`. Die neun Bestandswinkel sind
Fremd-Cloud/Garderobe, Audit/Detektiv, LKW/API-Workflow,
15-Minuten-Datenweg-Test, Regionalzug/stille Post, grüner Haken im Nebel,
Outlook-Integration, BIV-Namensschild sowie grüner Haken/Gepäckmarke.

- **POST 1** ist durch den organisatorischen Ausnahmeweg bei fehlender Klarheit
  und die Frage nach Stoppen, Beurteilen und Dokumentieren eigenständig. Die
  Flughafenmetapher allein macht ihn nicht zur Wiederholung des alten
  Gepäckmarken-/grüner-Haken-Winkels.
- **POST 2** ist durch den konkreten Agenten-Übergabezettel und die expliziten
  Grenzen zu Bedienererkennung, Mandat, Berechtigung und Freigabe eigenständig.
  Thematisch verwandte Agenten-Kommentare sind weder exakte noch funktionale
  Dubletten dieses eigenständigen Postwinkels.

Keiner der beiden Markertexte ist byte- oder textidentisch in `approvals.md`,
`schedule.md` oder `log.md` vorhanden. Der Dublettencheck ist für beide bestanden.

## Urteile und Pflichtänderungen

### POST 1 — `FREIGEGEBEN`

Zeichenlimit, Hash-Identität, exakter CTA, Pflicht-Hashtags, Sprache, enger ICP,
Kampagnenthema, persönliche Stimme, Produktrolle, Datenfluss, menschliche
Entscheidung, Rechts-/Compliance-/Freigabe-/Revisionsgrenzen, Fakten, Spam,
Brand-Safety und Dublettenabgrenzung bestehen.

**Pflichtänderung:** keine.

### POST 2 — `FREIGEGEBEN`

Zeichenlimit, Hash-Identität, exakter CTA, Pflicht-Hashtags, Sprache, enger ICP,
Kampagnenthema, persönliche Stimme, Produktrollentrennung, Datenfluss,
Mensch-/Agent-Erkennung, Mandat/Berechtigung, menschliche Freigabe,
Rechts-/Compliance-/Revisionsgrenzen, Fakten, Spam, Brand-Safety und
Dublettenabgrenzung bestehen.

**Pflichtänderung:** keine.

## Prozessgrenze

Diese Reviewer-Freigaben sind ausdrücklich keine Nutzerfreigaben und berechtigen
weder zum Einreihen noch zum Planen oder Veröffentlichen. `posts_per_run: 1`
bleibt die operative Veröffentlichungsgrenze pro Zyklus.

Ausgangstexte, Queue, Checkboxen, Freigaben, Termine, Planung und LinkedIn wurden
durch diesen Review nicht verändert. Es gab keine `li-jobs`-, Operator-,
Veröffentlichungs- oder LinkedIn-Aktion.
