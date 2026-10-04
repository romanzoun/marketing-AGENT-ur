# SE-DV-NP-20260930-R25 — einmalige reguläre Stilrunde

Bewertet wurden genau einmal und ausschliesslich die zwei unveränderten
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-30-r25.md`. Massgeblich waren
Romans Stilprofil, der vollständige Lernstand mit den konkreten
Nutzerkorrekturen, der vollständige aktuelle Approved-Korpus, das persönliche
Profil, die R25-Strategie und die Kampagne. Schwelle: **BESTANDEN ab 0,70**;
darunter wäre eine konkrete Pflichtrevision durch den Copywriter erforderlich.

## Textidentität

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch. Beide Texte sind NFC-normalisiert.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Textidentität bestätigt | Text unverändert |
|---|---:|---:|---:|---|---|---|
| Post 1 | 981 | 1.006 | 12 | `d1b88d59654de555f2cffe38fcd3eebf4b0f42f018cdd1e16d08ed425232397e` | ja | ja |
| Post 2 | 1.173 | 1.194 | 16 | `d75b05db13c525563b8301fb36f55984fe48a9be77145fc25f4723858e6e1016` | ja | ja |

Die Quelldatei enthält exakt zwei `text`-Blöcke. Zeichenanzahl und SHA-256
stimmen bei beiden exakt mit den Angaben im Copywriter-Artefakt überein. Beide
liegen unter dem Kampagnenlimit von 1.300 Unicode-Codepoints. Der
Style-Evaluator hat keinen Eingabetext verändert.

## Post 1 — technisch nicht geprüft ist nicht ungültig

- **Score: 0,91**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette zu den zwölf aktuellen Queue-Posts**

Die streikende Gepäckwaage übersetzt die abstrakte Statussemantik sofort in
eine konkrete Alltagssituation. Die ersten drei Absätze sind gesprochen,
persönlich und rhythmisch klar. „Praktisch, kompakt – und leider falsch
etikettiert“ sowie das Schlussbild, in dem Rot so tut, als hätte jemand
gewogen, setzen Romans typischen trockenen Witz. Die Ich-Haltung ist nicht nur
dekorativ: „Diese unspektakuläre dritte Spur ist mir ... wichtig“ formuliert
eine klare fachliche Position für Records/ECM und Compliance Operations.

Der Produktabsatz bleibt sachlich und ordnet die anschliessende Prozesslogik
dem eigenen Workflow zu. Er vermeidet lange Rechts- oder
Freigabeabgrenzungen, die Roman in direkten Korrekturen mehrfach aus
LinkedIn-Texten entfernt hat. Damit bleibt der praktische Nutzen vor der
Defensivklärung. Die Schlussfrage greift den Kern präzise auf und lädt ohne
Verkaufsdruck zur Antwort ein.

### Funktionaler Dublettenabgleich

Die nächste Queue-Familie ist `post-2026-09-29-0002`: Dort bedeutet eine
**nicht verfügbare Berechtigungsinformation** weder „nicht berechtigt“ noch
„wird schon passen“. R25 Post 1 behandelt dagegen einen anderen Gegenstand und
einen anderen Prozessfehler: Ein **technisch nicht zustande gekommenes
Prüfergebnis** darf nicht als ungültige Signatur umgedeutet werden.
`post-2026-09-28-0001` beschreibt die Führung eines bereits vorhandenen
Klärfalls, nicht die vorgelagerte Statusunterscheidung. Die übrigen zehn
Queue-Posts behandeln Mehrfachprüfung, Mehrfachsignaturen, Dokumentfassung,
Browser/API-Semantik, Regelversion, Stapelzuordnung, Zeitpunkte,
Berechtigungskontext, Ergebniszuordnung oder Vorgangsvollständigkeit. Der neue
Messproblem-versus-Messergebnis-Kern ist funktional eigenständig.

## Post 2 — Ergebnisdaten brauchen eine Zwecklogik

- **Score: 0,89**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette zu den zwölf aktuellen Queue-Posts**

Schliessfach, Namensetikett und schwarzes Brett bilden ein einziges,
konsequent geführtes Bild für Datenminimierung nach der technischen Prüfung.
„Das ist für mich die zweite Hälfte einer guten Datenschutzfrage“ setzt eine
klare persönliche Haltung und erweitert den bekannten Produktvorteil um eine
praktische Anschlussfrage. Die beiden kurzen Fragen in der Mitte brechen den
dichten Fachabsatz gut auf. „Nicht jede Rolle braucht automatisch die ganze
Auslage“ und „Dort wechselt nur die Frage: vom Dokument zum Ergebnis“ geben
dem Text Romans anschaulichen, leicht schmunzelnden Rhythmus.

Der längere Katalog der Ergebnisarten ist fachlich nötig und macht den
Mittelteil etwas sachlicher als Romans stärkste Approved-Beispiele; deshalb
liegt der Score knapp unter Post 1. Er kippt aber weder in Marketing-Sprech
noch in Rechtsbelehrung. Besonders passend zu den Lernsignalen ist, dass der
Text den konkreten Prozessnutzen und eine verständliche Frage in den
Vordergrund stellt, statt eine lange Liste dessen anzuhängen, was die Produkte
nicht entscheiden oder garantieren.

### Funktionaler Dublettenabgleich

Die grösste thematische Nähe besteht zu `post-2026-09-28-0002` und
`post-2026-09-26-0002`. Der erste fragt, welcher verfügbare Unternehmens- und
Rollenkontext dem konkreten Vorgang zugeordnet wird; der zweite, wie Kontext
mit Vorgang und internen Kompetenzregeln verbunden wird. R25 Post 2 fragt
hingegen nach **Sichtbarkeit und Zweckbindung**: Welche Rolle darf beziehungsweise
soll welche Ergebnisart für Prüfung, Klärung oder Entscheidung sehen? Auch
`post-2026-09-23-0001` verteilt Entscheidungen auf Rollen, behandelt aber
weder Zugriff noch Datenminimierung. Der Koffer-/Etikett-Winkel ist daher keine
funktionale Wiederholung des Datenweg-Themas oder der bestehenden
Kontextzuordnungs-Posts.

## Exakter Abgleich mit den zwölf aktuellen Queue-Posts

Die zwölf `kind: post`-Einträge in der aktuellen `approvals.md` wurden als
reine Textwerte gegen beide R25-Texte verglichen. Es gibt keine exakte
Textübereinstimmung. Auch der inhaltliche Einzelabgleich ergibt keine
funktionale Dublette.

| Text | Score | Urteil | Pflichtrevision | Exakte Dublette | Funktionale Dublette | Text unverändert |
|---|---:|---|---|---|---|---|
| Post 1 | 0,91 | **BESTANDEN** | nein | nein | nein | ja |
| Post 2 | 0,89 | **BESTANDEN** | nein | nein | nein | ja |

## Ergebnis

Beide unveränderten Texte überschreiten die Schwelle von 0,70. Es besteht
ausdrücklich **keine Pflichtrevision**. Es erfolgt keine Rückgabe an den
Copywriter, keine Umschreibung und keine weitere Stilrunde. Dieses Stilurteil
ist keine Nutzerfreigabe und löst keine Queue-, Freigabe-, Planungs-, Bild-,
Profil-, Lern-, Approved-, Operator-, Browser-, LinkedIn- oder
Veröffentlichungsaktion aus.
