# SE-DV-NP-20260926-R22 — einmalige reguläre Stilrunde

Bewertet wurden in genau einer regulären Stilrunde ausschliesslich die zwei
unveränderten `text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-26-r22.md`. Massgeblich waren
Romans Stilprofil, der vollständige Lernstand mit den konkreten
Nutzerkorrekturen, der vollständige aktuelle Approved-Korpus, das persönliche
Profil und die Kampagne. Schwelle: **BESTANDEN ab 0,70**; darunter wäre eine
Pflichtrevision durch den Copywriter erforderlich.

## Textidentität

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Textidentität bestätigt | Text unverändert |
|---|---:|---:|---:|---|---|---|
| Post 1 | 1.255 | 1.273 | 26 | `0d4029383c37260ff1a85293ba44b6629364411a4826f55d64cb2d95a1e28c56` | ja | ja |
| Post 2 | 1.290 | 1.304 | 22 | `e048c6ca33d901a84f8b6e4857a7cc203824339e5a6153e2a335f071d566fa32` | ja | ja |

Beide Texte liegen unter dem Kampagnenlimit von 1.300 Unicode-Codepoints. Die
Quelldatei enthält exakt zwei `text`-Blöcke; der Style-Evaluator hat keinen
Text verändert.

## Post 1 — drei Uhren und drei verschiedene Zeitpunkte

- **Score: 0,86**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette**

Bahnhofsuhren, Ortsangaben und der „Fahrplanstress“ des inneren
Ordnungsmenschen machen die abstrakte Zeitfrage sofort greifbar. Die
Ich-Perspektive, die trockene Pointe und die kurzen Übergänge treffen Romans
persönliche, gesprochene Stimme. Die Dreierliste ist für Records/ECM und Legal
Ops konkret nutzbar; die Schlussfrage greift das Bild sauber wieder auf. Der
Produktblock bleibt sachlich, ohne Heilsversprechen oder Marketing-Sprech.

Leichten Abzug gibt es für den vergleichsweise prozessualen Mittelteil sowie
die zwei Zuordnungssätze „soweit die Informationen verfügbar sind“ und „macht
der eigene Prozess sichtbar“. Direkte Nutzerkorrekturen zeigen, dass Roman
solche Detailabgrenzungen auf LinkedIn oft kürzt und den Produktmehrwert in den
Vordergrund stellt. Hier sind sie knapp, für die korrekte Aussage wesentlich
und bremsen den Text nicht genug für eine Pflichtrevision.

### Dublettenabgleich

Die nächsten Familien sind `post-2026-09-25-0001` zur Version des angewendeten
internen Regelsets am Entscheidungszeitpunkt, `post-2026-09-16-0002` zu den zwei
Zuständen „technisch geprüft“ und „fachlich freigegeben“ sowie ältere allgemeine
Audit-Rückschauen. Der neue Funktionskern ist anders: Er trennt
**Signaturzeitpunkt, technischen Prüfzeitpunkt und fachlichen
Entscheidungszeitpunkt** als drei verschiedenartige Prozessinformationen. Keine
der Vergleichsfassungen behandelt diese Drei-Zeitpunkte-Zuordnung. Damit liegt
trotz thematischer Familiennähe keine funktionale Dublette vor.

## Post 2 — Namensschild, Vertragswert und interne Kompetenzgrenze

- **Score: 0,78**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette; deutliche Motivnähe zur historischen Namensschild-Familie**

Der Hook ist knapp, verständlich und bildhaft. Der Sprung von 5'000 zu fünf
Millionen gibt dem Bild einen trockenen, konkreten Zug. Die drei Fragen trennen
technische Validität, verfügbaren BIV-Kontext und die organisationsseitige
Einordnung verständlich. „Das weiss weder der grüne Haken noch das
Namensschild“ bringt Romans Haltung mit einer kleinen Pointe zurück; die
Schlussfrage bleibt freundlich und fachlich relevant.

Der Score-Abzug ist bewusst deutlicher: Im historischen Log-Post
`post-2026-09-10-0002` steht bereits ein Namensschild für die Trennung von Name
und geschäftlicher Zeichnungsberechtigung. Auch die Rollenverteilung zwischen
Document Validator und BIV ist vertraut. Zudem ist der Absatz zur internen
Kompetenzgrenze sachlicher als Romans stärkste Approved-Beispiele. Der neue
Text bleibt dennoch oberhalb der Schwelle, weil er die bekannte Familie auf
einen materiell engeren, neuen Entscheidungsfall zuspitzt.

### Dublettenabgleich

`post-2026-09-10-0002` fragt allgemein, ob die identifizierte Person für ein
Unternehmen zeichnen darf. Der neue Text fragt enger, ob der verfügbare Kontext
**für diesen konkreten Vorgang und diesen Vertragswert** innerhalb der eigenen
internen Kompetenzregeln genügt. Auch `post-2026-09-22-0002` zum
Vier-Augen-Prinzip, `post-2026-09-23-0002` zu mehreren Signaturen und die
allgemeinen DocVal-/BIV-Rollentexte decken diesen wert- und vorgangsgebundenen
Kern nicht ab. Deshalb ist die Motivwiederholung deutlich, aber keine
funktionale Dublette.

## Umfang der Queue-Dublettenprüfung

Vollständig geprüft wurden die Posttexte in `approvals.md`, `schedule.md` und
`log.md` beider DocVal-Kampagnenpfade. Aktuell enthalten die vorhandenen Dateien
35 Posteinträge beziehungsweise 34 unterschiedliche exakte Textstände; die
einzige interne exakte Wiederholung ist ein doppelt vorhandener historischer
Schedule-Eintrag und betrifft keinen der beiden R22-Texte. Im Pfad
`Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/` existiert derzeit keine
`log.md`; im Pfad `Kampagnen/document validator/queue/` ist `approvals.md` leer.

## Ergebnis

| Text | Score | Urteil | Pflichtrevision | Exakte Dublette | Funktionale Dublette | Text unverändert |
|---|---:|---|---|---|---|---|
| Post 1 | 0,86 | **BESTANDEN** | nein | nein | nein | ja |
| Post 2 | 0,78 | **BESTANDEN** | nein | nein | nein | ja |

Beide Texte überschreiten die Schwelle. Es erfolgt keine Rückgabe an den
Copywriter, keine Umschreibung und keine zusätzliche Stil- oder Kontrollrunde.
Dieses Stilurteil ist keine Nutzerfreigabe und löst keine Queue-, Checkbox-,
Termin-, Schedule-, Log-, Profil-, Lern-, Approved-, Operator-, Browser-,
LinkedIn- oder Veröffentlichungsaktion aus.
