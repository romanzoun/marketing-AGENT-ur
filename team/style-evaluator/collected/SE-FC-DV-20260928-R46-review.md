# Stilprüfung — SE-FC-DV-20260928-R46

Datum: 2026-09-28  
Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`  
Schwelle: **BESTANDEN** nur bei Score `>= 0.70`

## Prüfumfang und Integrität

- Bewertet wurden ausschliesslich die finalen Texte von `comment-2026-09-28-0001` und `comment-2026-09-28-0003`, jeweils gebunden an ID, URL, vollständige Original-Note, Codepoint-Zahl und SHA-256.
- Massstab: Romans aktuelle persönliche Stimme, Ich-Haltung, Wortwahl, Satzrhythmus, bildhafter Vergleich, fachliche Natürlichkeit sowie Nähe zu genehmigten und abgelehnten Mustern. Exakte und funktionale Dubletten wurden gegen Approved-Korpus, Lernstand und aktuelle Queue geprüft.
- `comment-2026-09-28-0002` wurde wegen Banned Topic nicht stilbewertet. Sein `text:` ist und bleibt exakt leer; kein Style-Score wurde vergeben.
- In der Queue wurden nur `evaluation_score`, `evaluation_note` und `evaluated_at` der beiden bewerteten Blöcke aktualisiert. Kein Kommentartext und kein anderes Queue-Feld wurde verändert.

## comment-2026-09-28-0001

- URL: `https://lnkd.in/p/eerZ9VNn`
- Unicode-Codepoints: **342** — bestätigt
- SHA-256: `74bb46ed8a1b68572d4bc79f96e0f1fba9ded98e1b0e2be9e119e958cc983d14` — bestätigt
- Score: **0.55**
- Urteil: **NICHT BESTANDEN — REVISION ERFORDERLICH**

### Stimme und fachliche Natürlichkeit

Der Einstieg „I like this distinction“ und „In practice“ geben eine klare persönliche Haltung. Drei Sätze führen sauber von Identifikation über Organisation und authority zur bildhaften Pointe. Der Text reagiert direkt auf den Originalpost, bleibt unter 500 Zeichen und behauptet weder juristische Garantie noch abschliessende Zeichnungsberechtigung. Das ist fachlich natürlich und grundsätzlich nah an Romans englischer Stimme.

### Dublettenprüfung

- Keine exakte Volltext- oder Hash-Dublette.
- **Starke funktionale und lexikalische Dublette.** „A name badge“ wiederholt den freigegebenen Kommentar `2026-09-13-comment-2026-09-12-0003.md` mit dessen „name badge written in pencil“.
- „office keys“, „on whose authority“ und Mandat wiederholen die freigegebenen Kommentare `2026-09-13-comment-2026-09-12-0005.md` und `2026-09-14-comment-2026-09-13-0003.md` nahezu als gemeinsame Schlussfigur.
- Der funktionale Kern „Identität allein reicht nicht; Organisation, Mandat, Rechte und Verantwortung müssen vor dem Handeln prüfbar sein“ wurde bereits in `SE-FC-DV-20260917-R23-review.md` als belegte Badge-/Office-Keys-/Mandatsfamilie abgelehnt. Eine Kombination bekannter Bilder schafft keinen neuen Blickwinkel.

### Konkrete Umschreibeanweisung

Den Text nicht erneut um Badge, Schlüssel, Tür, Mandat oder den Empfänger-Checkpoint bauen. Stattdessen die Identität als **Bündel einzelner attestierter Fakten** behandeln und konkret fragen, welcher Nachweis welchen Entscheidungsschritt trägt und wie unterschiedliche Nachweise auseinandergehalten werden. Auch „office keys“, „on whose authority“ und die bereits belegte Dreierfolge Mandat/Rechte/Verantwortung vermeiden.

Arbeitsrichtung, nicht freigegebener Ersatztext:

> What makes this distinction useful for me is that identity is not one portable label. It is a bundle of claims from different sources, and each decision should show which claim it relied on. Otherwise, the wallet may travel well while the reason for trusting a specific fact gets lost in the luggage.

## comment-2026-09-28-0003

- URL: `https://www.linkedin.com/feed/update/urn:li:ugcPost:7509281736724357120/`
- Unicode-Codepoints: **374** — bestätigt
- SHA-256: `3f09c7933e53db080a5e9e5c47577f84a2aece5880e0f03346e0485a1b80c722` — bestätigt
- Score: **0.58**
- Urteil: **NICHT BESTANDEN — REVISION ERFORDERLICH**

### Stimme und fachliche Natürlichkeit

„I would want“ schafft eine persönliche Position. Der Dreisatz ist gut geführt: These, operative Bedingung, trockene Pointe. „collection of local surprises“ ist ein verständliches Bild ohne Competitor-Bashing. Der Text bleibt eng bei nationalen Umgebungen und Interoperabilität, vermeidet Produktpitch, Rechtsbehauptung und künstliche PDF-/BIV-Brücke.

### Dublettenprüfung

- Keine exakte Volltext- oder Hash-Dublette.
- **Funktionale Dublette zur aktuellen Queue:** `comment-2026-09-23-0001` beginnt bereits mit „The happy path is the easy part“ und testet dieselbe Übergabe anhand nicht verfügbarer oder nicht unterstützter Credentials sowie eines brauchbaren Ausnahmewegs.
- Der neue Text übernimmt davon „happy path“, testbare handover, „unavailable“ und den definierten Fallback. Der nationale Rahmen ändert die Oberfläche, nicht die Funktion des Kommentars.
- „Interoperability becomes real“ und das Bild eines europäischen Rahmens mit lokalen Abweichungen liegen zusätzlich nahe an freigegebenen Island-/Bridge-/different-ruler-Kommentaren. Diese Nähe wäre für sich allein tragbar; zusammen mit der Queue-Dublette fehlt aber ein neuer Beitrag.

### Konkrete Umschreibeanweisung

Happy Path, Handover, Fallback, unavailable/unsupported und allgemeine Explainability vollständig verlassen. Aus dem Originalpost stattdessen einen eigenständigen operativen Winkel machen: eine **lebende, datierte Testmatrix** je Land, Wallet, Credential-Typ, Version und letztem erfolgreichen Lauf. Die Pointe darf zeigen, wie schnell eine undatierte Europakarte zur Dekoration altert.

Arbeitsrichtung, nicht freigegebener Ersatztext:

> For me, the useful deliverable is not one integration diagram but a living test matrix: country, wallet, credential, version and last successful run. National environments keep moving, so every green field needs a date beside it. An interoperability map without test dates ages into wall decoration surprisingly quickly.

## Kontrollkandidat comment-2026-09-28-0002

- URL: `https://www.linkedin.com/company/shopify/posts/`
- Status: **GESPERRT wegen Banned Topic**
- `text:`: exakt `''`
- SHA-256 des Leertexts: `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`
- **Kein Style-Score vergeben.**

## Grenzen

- Keine Nutzerfreigabe gesetzt, keine Checkbox angekreuzt, nichts geplant, verschoben oder veröffentlicht.
- `team/style/profile.md`, `team/style/learning.json` und `team/style/approved/` unverändert; es liegt keine Nutzerfreigabe vor.
- Keine Folgeagenten gestartet.
