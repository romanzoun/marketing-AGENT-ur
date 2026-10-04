# SE-DV-NP-20260929-R24 — einmalige reguläre Stilrunde

Bewertet wurden genau einmal und ausschliesslich die zwei unveränderten
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-29-r24.md`. Massgeblich waren
Romans Stilprofil, der vollständige Lernstand mit den konkreten
Nutzerkorrekturen, der vollständige aktuelle Approved-Korpus, das persönliche
Profil, die R24-Strategie und die Kampagne. Schwelle: **BESTANDEN ab 0,70**;
darunter wäre eine konkrete Pflichtrevision durch den Copywriter erforderlich.

## Textidentität

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch. Beide Texte sind NFC-normalisiert.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Textidentität bestätigt | Text unverändert |
|---|---:|---:|---:|---|---|---|
| Post 1 | 1.146 | 1.157 | 21 | `114239efad93c06f4f0ea149c8a67725d4259a10c634b5a11d27b7b1896d7765` | ja | ja |
| Post 2 | 1.232 | 1.250 | 22 | `3e9f89dbfd18b1ea6ccc36754901e9de0839a62aa397229935f3ff5d89c4085e` | ja | ja |

Die Quelldatei enthält exakt zwei `text`-Blöcke. Beide liegen unter dem
Kampagnenlimit von 1.300 Unicode-Codepoints. Der Style-Evaluator hat keinen
Eingabetext verändert.

## Post 1 — intaktes Siegel, unvollständiger Vorgang

- **Score: 0,87**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette**

Umzugskarton, Siegel, Packliste und fehlende Schrauben geben der abstrakten
Trennung zwischen Signaturprüfung und Vorgangsvollständigkeit ein einziges,
konsequent geführtes Bild. „Die Packliste hat trotzdem schlechte Laune“ und
„Ein intaktes Siegel zählt eben keine Schrauben“ setzen den für Roman typischen
trockenen Witz. Die Ich-Haltung ist klar, die kurzen Einstiegs- und
Pointe-Sätze sorgen für gesprochenen Rhythmus, und die nummerierten Schritte
machen den Records-/ECM- und Legal-Ops-Nutzen konkret. Der Produktabsatz bleibt
sachlich und frei von Buzzwords, Heilsversprechen oder künstlichem Druck; nur
der standardisierte CTA klingt naturgemäss etwas formeller als der Haupttext.

Das passt zu den Approved- und Lernmustern „bildhafter Alltagsgegenstand →
konkrete operative Trennung → kurze Frage“. Zugleich bleibt der Kundennutzen im
Vordergrund. Die direkte Nutzerpräferenz, lange Rechts- und
Freigabeabgrenzungen aus LinkedIn-Posts zu entfernen, wird eingehalten: Der
Satz zum eigenen Vollständigkeitsprozess ist keine defensive Nebenbelehrung,
sondern der Funktionskern dieses Posts.

### Funktionaler Dublettenabgleich

Die nächste bestehende Familie ist `post-2026-09-16-0002` mit den zwei
Zuständen „technisch geprüft“ und „fachlich freigegeben“. Hinzu kommen Posts zu
Mehrfachsignaturen, Dokumentversionen, Stapelkorrelation und
Records-Klassifikation. R24 Post 1 erzählt jedoch einen anderen operativen
Fall: Die signierte **Hauptdatei** kann technisch geprüft sein, während zum
gesamten Geschäftsvorgang erwartete Beilagen, Anlagen oder Unterlagen fehlen.
Kein bestehender Post behandelt diese Packlisten-/Vorgangsvollständigkeit.

## Post 2 — „nicht verfügbar“ ist kein negativer Nachweis

- **Score: 0,82**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**
- **Dublettenurteil: keine exakte und keine funktionale Dublette; erkennbare Nähe zur historischen Berechtigungsfamilie**

Die leere Schublade und der Hammer machen eine semantische Datenlücke sofort
verständlich. „Für ein Statusfeld ist das etwas unromantisch. Aber ehrlich.“
trifft Romans kurzen, leicht selbstironischen Rhythmus; die Ich-Perspektive und
die konkrete Dreiertrennung halten den Text persönlich und operativ. Der
Produktteil ist verständlich, fachlich zurückhaltend und ohne
Marketing-Sprech. Die Schlussfrage nimmt das eigentliche Risiko einer
vorschnellen Ja-/Nein-Deutung sauber wieder auf.

Der etwas niedrigere Score folgt aus dem sachlicheren zweiten Teil. Die Sätze
zur fehlenden Information, zur BIV-Grenze und zum organisationsinternen Prozess
bremsen den Rhythmus stärker als Romans beste Approved-Beispiele. Direkte
Nutzerkorrekturen bevorzugen meist den sichtbaren Produktmehrwert vor längeren
Negativabgrenzungen. Hier bleibt die Abgrenzung dennoch knapp und ist für den
neuen semantischen Kern notwendig; sie kippt weder in Rechtsbelehrung noch in
Corporate-Sprache.

### Funktionaler Dublettenabgleich

Die historische Familie um `post-2026-09-10-0002` trennt Name und allgemeine
geschäftliche Zeichnungsberechtigung. `post-2026-09-26-0002` verbindet
verfügbaren Kontext mit Vertragswert und interner Kompetenzgrenze;
`post-2026-09-28-0002` behandelt die Auswahl eines passenden Unternehmens- und
Rollenkontexts unter mehreren Treffern. R24 Post 2 setzt einen neuen, engeren
Kern: **Eine nicht verfügbare Berechtigungsinformation ist weder positiver noch
negativer Berechtigungsnachweis.** Diese Statussemantik ist in keinem
bestehenden Post der beiden Queue-Historien oder im Approved-Korpus behandelt.

## Umfang der Dublettenprüfung

Vollständig geprüft wurden die Posttexte in `approvals.md`, `schedule.md` und
`log.md` beider DocVal-Kampagnenpfade sowie der vollständige aktuelle
Approved-Korpus. Die sechs Queue-Dateien enthalten aktuell 37 Posteinträge und
36 unterschiedliche exakte Textstände; die einzige interne exakte Wiederholung
ist der doppelt vorhandene historische Schedule-Text
`post-2026-09-17-0003`. Keiner der beiden R24-Texte ist exakt oder funktional
damit oder mit einem anderen Bestandsbeitrag identisch.

## Ergebnis

| Text | Score | Urteil | Pflichtrevision | Exakte Dublette | Funktionale Dublette | Text unverändert |
|---|---:|---|---|---|---|---|
| Post 1 | 0,87 | **BESTANDEN** | nein | nein | nein | ja |
| Post 2 | 0,82 | **BESTANDEN** | nein | nein | nein | ja |

Beide Texte überschreiten die Schwelle. Es erfolgt keine Rückgabe an den
Copywriter, keine Umschreibung und ohne tatsächliche Textänderung keine zweite
Stil- oder Kontrollrunde. Dieses Stilurteil ist keine Nutzerfreigabe und löst
keine Queue-, Checkbox-, Termin-, Schedule-, Log-, Kampagnen-, Profil-, Lern-,
Approved-, Operator-, Browser-, LinkedIn- oder Veröffentlichungsaktion aus.
