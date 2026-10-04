# SE-DV-NP-20261001-R26 — einmalige reguläre Stilrunde

Bewertet wurden genau einmal und ausschliesslich die zwei unveränderten
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-10-01-r26.md`. Massgeblich waren
Romans Stilprofil, der vollständige Lernstand mit den konkreten
Nutzerkorrekturen, der vollständige aktuelle Approved-Korpus, das persönliche
Profil, die verbindliche R26-Strategie und die Kampagne. Die ausdrückliche
Auftragszahl von zwei Texten gilt trotz `posts_per_run: 1`. Schwelle:
**BESTANDEN ab 0,70**; darunter wäre eine konkrete Pflichtrevision durch den
Copywriter erforderlich.

## Identität und Prüfumfang

- Auftrag: `SE-DV-NP-20261001-R26`
- Rolle: `style-evaluator`
- Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`
- Strategie: `team/content-strategist/collected/docval-biv-ideas-2026-10-01-r26.md`
- Eingabe: `team/copywriter/collected/docval-biv-two-2026-10-01-r26.md`
- Bewertete Textstände: exakt zwei unveränderte `text`-Blöcke, je einmal
- Dublettenbestand: alle aktuellen `kind: post`-Texte in `approvals.md`,
  `schedule.md` und `log.md` der Kampagne

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | NFC | SHA-256 | Textidentität bestätigt | Text unverändert |
|---|---:|---:|---:|---|---|---|---|
| Post 1 | 999 | 1.015 | 12 | ja | `db19d8f91fa8a48eb0e52747ce1a66a62e308e63616462d6806e0cb4932a0f2f` | ja | ja |
| Post 2 | 1.103 | 1.120 | 12 | ja | `dbcd5c96df8dd7f97986243cdb97daf526719990385fe7805954a41b45e9fc9f` | ja | ja |

Die Quelldatei enthält exakt zwei `text`-Blöcke. Zeichenanzahl und SHA-256
stimmen bei beiden exakt mit den Angaben im Copywriter-Artefakt überein. Beide
liegen unter dem Kampagnenlimit von 1.300 Unicode-Codepoints. Der
Style-Evaluator hat keinen Eingabetext verändert.

## Post 1 — das Prüfergebnis muss den Systemwechsel überleben

- **Score: 0,90**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette**

Der verblassende Kassenbon macht die abstrakte Gefahr eines nur in der heutigen
Oberfläche verständlichen Prüfergebnisses sofort greifbar. „Ein weisses
Andenken“ und die spätere Tapeten-/Umbau-Pointe setzen Romans trockenen,
leicht schmunzelnden Ton. Die Ich-Sätze formulieren eine klare Haltung, ohne
eine erfundene Praxis- oder Kundengeschichte zu behaupten. Kurze Einstiegszeilen,
ein sachlicher Mittelteil und die offene Schlussfrage ergeben den bewährten
Rhythmus Bild → fachlicher Punkt → Einladung.

Der Produktabsatz bleibt positiv und faktisch: Der Document Validator liefert
Signatur- und Zertifikatsinformationen. Die anschliessende Zuständigkeit des
eigenen Records-/ECM-Prozesses ist hier keine bremsende allgemeine Negativliste,
sondern der eigentliche Systemwechsel-Kern. Damit wahrt der Text die
Produktgrenze und zugleich Romans konkrete Lernpräferenz, LinkedIn-Texte nicht
mit langen Rechts-, Freigabe- oder Garantiedisclaimern zu überladen. Der Wechsel
vom Thermopapier zur Tapete ist ein kleiner zweiter Bildimpuls, bleibt aber im
gemeinsamen Motiv „Information darf den Trägerwechsel nicht verlieren“ und
senkt die Freigabewahrscheinlichkeit nur geringfügig.

### Funktionaler Dublettenabgleich

Die grösste Nähe besteht zu `post-2026-09-25-0001`, der Regelset,
Regelversion und Entscheidungszeitpunkt festhält, sowie zum historischen
`post-2026-09-22-0001` in `log.md`, der Prüfinformationen von der späteren
Records-Entscheidung trennt. R26 Post 1 behandelt jedoch einen anderen
operativen Bruch: Ob Signatur- und Zertifikatsinformationen nach einem Wechsel
von DMS, Workflow oder Oberfläche weiterhin eindeutig zur geprüften PDF gehören
und ohne das Altsystem verständlich bleiben. Auch die bestehenden Posts zu
Dokumentfassung, Batch-Korrelation und zentralem Klärdatensatz decken diese
Migration der Bedeutungsbeziehung nicht ab.

## Post 2 — der verwendete Identitätskontext braucht einen Zeitpunkt

- **Score: 0,87**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette**

Restaurantrechnung und heutige Speisekarte bilden ein einziges, konsequent
geführtes Bild. Die kurzen „Vielleicht“-Sätze sprechen locker, der Satz „Bei
einer Entscheidung zu einer signierten PDF sehe ich das ähnlich“ setzt die
persönliche Haltung klar, und die spätere Menü-Pointe schliesst den Bogen. Der
Produktabsatz ordnet Document Validator und BIV knapp und ohne Marketing-Sprech
ein; die Schlussfrage übersetzt den Gedanken direkt in den Prozess des
Publikums.

Etwas sachlicher als Romans stärkste Approved-Beispiele ist der Absatz zum
tatsächlich herangezogenen Informationsstand. Besonders „Nicht als Behauptung,
der Kontext habe sich verändert“ ist eine defensive Absicherung und bremst den
gesprochenen Rhythmus leicht. Sie bleibt hier jedoch kurz, verhindert eine
unbelegte Veränderungsbehauptung und wird sofort wieder auf den positiven Nutzen
der Erklärbarkeit einer früheren Entscheidung zurückgeführt. Deshalb mindert sie
den Score, löst aber keine Pflichtrevision aus.

### Funktionaler Dublettenabgleich

Die nächste Bestandsfamilie bilden `post-2026-09-25-0001` mit der bei einer
Entscheidung geltenden Regelversion, `post-2026-09-26-0001` mit drei getrennten
Zeitpunkten sowie `post-2026-09-28-0002` mit der Zuordnung eines Unternehmens-
und Rollenkontexts zum konkreten Prozessschritt. R26 Post 2 wiederholt keinen
dieser Funktionskerne. Er fragt spezifisch, welcher **damals tatsächlich
verwendete verfügbare Identitäts- und Berechtigungskontext** die frühere
Entscheidung getragen hat, und warnt davor, einen heutigen Abruf stillschweigend
an dessen Stelle zu setzen. Weder die allgemeine Zeitpunktstrennung noch die
Regelversion oder die Auswahl unter mehreren aktuellen Kontexten behandeln diese
zeitliche Bindung des verwendeten Informationsstands.

## Vollständiger Abgleich mit dem aktuellen Queue-Bestand

Geprüft wurden 14 Posttexte in `approvals.md`, ein Posttext in `schedule.md` und
ein Posttext in `log.md`, insgesamt 16 aktuelle Posteinträge. Beide R26-Hashes
sind in diesem Bestand nicht vorhanden. Der Einzelabgleich der Funktionskerne
ergibt ebenfalls keine Dublette.

| Text | Score | Urteil | Pflichtrevision | Exakte Dublette | Funktionale Dublette | Text unverändert |
|---|---:|---|---|---|---|---|
| Post 1 | 0,90 | **BESTANDEN** | nein | nein | nein | ja |
| Post 2 | 0,87 | **BESTANDEN** | nein | nein | nein | ja |

## Ergebnis

Beide unveränderten Texte überschreiten die Schwelle von 0,70. Es besteht
ausdrücklich **keine Pflichtrevision**. Es erfolgt keine Rückgabe an den
Copywriter, keine Umschreibung und keine zweite Stilrunde. Dieses Stilurteil ist
keine Nutzerfreigabe und löst keine Queue-, Freigabe-, Planungs-, Bild-,
Profil-, Lern-, Approved-, Operator-, Browser-, LinkedIn- oder
Veröffentlichungsaktion aus.
