# Abschlussbericht ES-FC-DV-20260911

- Datum: 2026-09-11
- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Auftrag: exakt zwei Feed-Kommentarkandidaten sammeln, schreiben sowie durch
  Stil- und Kampagnenprüfung führen
- Veröffentlichungsstatus: nichts veröffentlicht, geplant oder nutzerfreigegeben

## Sammelbefehl und Ergebnis

Vorgeschriebener Befehl:

`./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`

Der Befehl wurde exakt ausgeführt. Der erste Versuch endete vor dem
LinkedIn-Zugriff mit `connect EPERM ::1:9222`, weil der lokale Chrome-CDP-Port
durch die Sandbox nicht erreichbar war. Der identische, für den lokalen
CDP-Zugriff freigegebene Wiederholungsversuch verband sich mit Chrome, endete
aber in `LinkedInClient.ensure_logged_in()` mit `Page.goto: Timeout 30000ms
exceeded` beim Aufruf von `https://www.linkedin.com/feed/`.

Der Trace belegt, dass der zweite Versuch vor `collect_feed()` und vor
`q.append()` abbrach. Diese beiden Befehlsversuche selbst konnten daher keinen
Queue-Eintrag schreiben. Parallel erschienen jedoch die zwei für diesen Lauf
dokumentierten Kandidaten in der Queue und wurden unverändert unter
`team/engagement-scout/collected/feed-comment-candidates-2026-09-11.md`
gesichert. Der Lauf lieferte keine URNs; es wurde keine URN ergänzt oder
abgeleitet.

## Die zwei dokumentierten Laufkandidaten

### comment-2026-09-11-0003

- ursprüngliche URL: `https://lnkd.in/p/eCA8Hjke`
- ursprünglicher Autor: `Timo Behrmann`
- Zielsprache: Deutsch
- Relevanz: EUDI-Wallet, digitale Identität, eIDAS, kommunale Standards und
  Schnittstellen
- final geprüfter Text: `11.000 Kommunen sollten wirklich nicht 11.000-mal
  dasselbe Rad erfinden – sonst wird aus der Wallet schnell ein Staffellauf mit
  11.000 verschiedenen Staffelstäben. Wiederverwendbare Standards und saubere
  Schnittstellen sind für mich deshalb nicht die technische Fußnote, sondern die
  eigentliche Startbedingung. Gute digitale Identität muss am Ende auch am
  Schalter funktionieren.`
- Umfang: 379 Unicode-Zeichen, 3 Sätze, kein Link

### comment-2026-09-11-0004

- ursprüngliche URL: `https://lnkd.in/p/ePwCJgU7`
- ursprünglicher Autorwert: `Lissi GmbH likes this`
- Quellbeitrag: Trusted Economy Forum
- Zielsprache: Englisch
- Relevanz: EUDI-Wallet, Identitätsprüfung auf Empfängerseite, Relying Parties,
  eIDAS
- final geprüfter Text: `A wallet experience has two front doors: the one on
  the phone and the one at the relying party. If verification on the receiving
  side feels like paperwork in disguise, even the smoothest tap cannot save it.
  I am looking forward to the practical view from both sides.`
- Umfang: 266 Unicode-Zeichen, 3 Sätze, kein Link

## Agenten-Prüfablauf

### Copywriter

Der Projekt-Agent `copywriter` wurde mit `agent_type=copywriter` und
`fork_turns=none` sowie vollständigen Pfaden, Zielpost-Kontexten und Grenzen
aufgerufen. Er bestätigte beide bereits parallel eingetragenen Texte als
konform und änderte sie nicht unnötig. Beide sind in der jeweiligen Zielsprache,
haben 2–4 Sätze, bleiben unter 500 Zeichen und enthalten weder Link, Produktpitch
noch erfundene persönliche Fakten.

### Style-Evaluator

Der Projekt-Agent `style_evaluator` wurde mit `fork_turns=none` aufgerufen und
prüfte gegen `team/style/profile.md`, `team/style/learning.json` und den
freigegebenen Korpus unter `team/style/approved/`.

- 0003: `0,88`, **BESTANDEN**. Persönlich, bildhaft, enger Originalbezug;
  kleiner Abzug wegen der doppelten Bildspur „Rad erfinden“/„Staffellauf“.
- 0004: `0,84`, **BESTANDEN**. Starkes „two front doors“-Bild und präziser
  Originalbezug; der Schlusssatz wirkt etwas formell.

Beide Scores liegen über 0,70. Es gab deshalb keine Pflichtrevision und keinen
Style-Rücklauf zum Copywriter. Die optionalen Umschreibungen stehen in
`team/style-evaluator/collected/SE-FC-DV-20260911-review.md`.

### Reviewer

Der Projekt-Agent `reviewer` wurde mit `fork_turns=none` aufgerufen und prüfte
Zeichenlimit, Zielsprache, Satzanzahl, Linkverzicht, Themen, Fakten, Spam und
Brand-Safety strikt gegen die Kampagne.

- 0003: **abgelehnt**. 379/500 Zeichen, 3 Sätze, Deutsch, kein Link. Inhalt,
  Stimme, Fakten, Spam und Brand-Safety bestanden. Einziger Ablehnungsgrund:
  `#Compliance`, `#eIDAS` und `#RecordsManagement` fehlen im eigenen Text.
- 0004: **abgelehnt**. 266/500 Zeichen, 3 Sätze, Englisch, kein Link. Inhalt,
  Stimme, Fakten, Spam und Brand-Safety bestanden. Einziger Ablehnungsgrund:
  dieselben drei fehlenden Pflicht-Hashtags.

Der Reviewer wertete die Link-CTA wegen der Kampagnenformulierung „Link im Post“
und der spezifischen Kommentarvorgabe „ohne Link“ als nicht anwendbar. Für
`required_hashtags` enthält die Kampagne dagegen keine Kommentar-Ausnahme.
Vorgeschlagene formale Korrektur: `#Compliance #eIDAS #RecordsManagement` am
Ende ergänzen. Damit lägen die Texte bei 418 beziehungsweise 305 Zeichen. Diese
Korrektur wurde wegen des nachfolgend beschriebenen Queue-Konflikts nicht
angewandt und nicht erneut geprüft.

## Queue-Konflikt und Blocker

Während der reinen Reviewer-Prüfung wurde `approvals.md` mehrfach von einem
parallelen Prozess neu geschrieben. Der Reviewer beobachtete den Hashwechsel
von `ff318b...` zu `7a3a3f...` und danach weitere Mutationen. Die ursprünglichen
Einträge 0003 und 0004 verschwanden dabei aus `approvals.md`; sie waren auch in
`schedule.md` und `log.md` nicht auffindbar. Anschließend wurde die ID
`comment-2026-09-11-0004` für einen anderen Beitrag (`iCOMPASS`,
`https://lnkd.in/p/evbbAWVa`) wiederverwendet.

Read-only-Snapshot 2026-09-11T15:28:07+0200:

- `approvals.md`: SHA-256
  `ffb5b8ec1ba89803793b0179f6960fdaec06a9f3a0bf00a833a00524b79edb90`,
  mtime 15:27:34
- `schedule.md`: SHA-256
  `89f11a51233e198b641c5c922d7d8d3adce5bcadfb0b24ba4cfdf3d9be732362`,
  mtime 13:50:28
- `log.md`: SHA-256
  `65faf60a90a3d648cffbc2836196dc212513b96433573151c154d3399577f832`,
  mtime 13:50:28

Das zeitgleich aktive Board protokollierte einen separaten R3-Post- und einen
weiteren Kommentar-Lauf. Das ist ein starker Hinweis auf konkurrierende
Read-Modify-Write-Zugriffe auf `approvals.md`, aber kein eindeutiger Beweis für
den konkreten Verursacher. `git status` war als weitere Belegquelle nicht
verfügbar, weil das Arbeitsverzeichnis kein Git-Repository ist; die Prozessliste
war in der Sandbox mit `operation not permitted` gesperrt.

Eine automatische Hashtag-Revision wäre dadurch unsicher: Die ursprüngliche ID
0004 adressiert jetzt einen anderen Zielpost, und 0003 fehlt. Deshalb wurden die
verschwundenen Einträge weder rekonstruiert noch anhand der wiederverwendeten ID
verändert. Der Reviewer-Rücklauf bleibt blockiert, bis die ursprünglichen
Kandidaten eindeutig und konfliktfrei wiederhergestellt oder mit neuen stabilen
IDs erneut gesammelt werden.

## Geänderte Dateien und Herkunft

Dem dokumentierten Kommentar-Lauf zuzuordnen sind:

- `Kampagnen/document validator/queue/approvals.md` — parallel mehrfach
  verändert; zunächst Kandidaten und Texte/Evaluationsfelder, später Verlust der
  ursprünglichen 0003/0004 und Wiederverwendung von 0004; nicht durch die hier
  ausgeführten Prüfagenten zurückgesetzt
- `team/engagement-scout/collected/feed-comment-candidates-2026-09-11.md`
- `team/engagement-scout/collected/ES-FC-DV-20260911-final-report.md`
- `team/engagement-scout/todo.md`
- `team/engagement-scout/outbox.md`
- `team/content-strategist/collected/comment-candidates-2026-09-11.md`
- `team/content-strategist/inbox.md`
- `team/copywriter/collected/document-validator-comments-2026-09-11.md`
- `team/copywriter/inbox.md`
- `team/style-evaluator/collected/SE-FC-DV-20260911-review.md`
- `team/style-evaluator/collected/SE-FC-DV-20260911-final-review.md`
- `team/style-evaluator/inbox.md`
- `team/style-evaluator/todo.md`
- `team/reviewer/collected/RV-FC-DV-20260911-review.md`
- `team/reviewer/inbox.md`
- `team/reviewer/memory.md`
- `team/board.md`

Parallel entstandene R2/R3-Artefakte und andere Post-Artefakte werden nicht als
Ergebnis dieses Zweierlaufs beansprucht.

## Sicherheitsbestätigung

In diesem Lauf wurde kein `operator`, `run-due`, `post`, `comment`, `reply`,
`reshare` oder `schedule` ausgeführt. Es wurde keine Checkbox angekreuzt, keine
Nutzerfreigabe erteilt und nichts veröffentlicht. Die Prüfagenten veränderten
weder Planung noch Log. Der aktuell sichtbare andere Eintrag 0004 wurde nicht als
der ursprünglich geprüfte Kandidat behandelt.
