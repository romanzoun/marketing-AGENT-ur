# Stilprüfung SE-DV-20260913-R5-PRIMARY

## Prüfrahmen

Geprüft wurden ausschließlich die reinen Texte zwischen `POST 1 BEGIN/END`
und `POST 2 BEGIN/END` in
`team/copywriter/collected/document-validator-two-2026-09-13-r5-primary.md`.
Bewertet wurde die geschätzte Freigabewahrscheinlichkeit anhand persönlicher
Stimme, Haltung, Wortwahl und Rhythmus. Schwelle: ab `0,70` **BESTANDEN**,
darunter **REVISION** und Rückgabe an den Copywriter.

`team/style/learning.json` enthält keine Nutzerkorrekturen, Muster oder
Freigaben. Unter `team/style/approved/` liegt nur die README; ein empirischer
Approved-Korpus fehlt. `config/personal_profile.yaml` enthält ebenfalls keine
biografischen Angaben. Die Bewertung stützt sich daher auf das explizite
Stilprofil und die Kampagnenstimme, ohne Erfahrungen oder biografische Details
zu unterstellen.

## Deterministische Textidentität

Gezählt wurden Unicode-Codepoints des reinen Textes zwischen den Markern.
Interne Zeilenumbrüche zählen mit; Marker und die direkt angrenzenden
Zeilenumbrüche zählen nicht.

| Text | zugeordnete Queue-ID | Unicode-Codepoints | interne Zeilenumbrüche | SHA-256 des reinen Textes |
|---|---|---:|---:|---|
| POST 1 | `post-2026-09-13-0001` | 1.144 | 16 | `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97` |
| POST 2 | `post-2026-09-13-0002` | 1.203 | 19 | `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030` |

## POST 1 — Regionalzug und stille Post

**Score: 0,94 — BESTANDEN**

- **Persönliche Stimme:** Der Regionalzug und die stille Post machen den
  abstrakten Dokumentenweg sofort sichtbar. «Mein Lieblingssatz für spätere
  Rückfragen. Also: überhaupt nicht.» liefert Ich-Stimme, trockenen Witz und
  Selbstironie.
- **Haltung:** «Für mich gehört der Kontrollpunkt ...» ist eine klare,
  pragmatische Position. Die Entscheidung bleibt ausdrücklich beim zuständigen
  Menschen; der Text verspricht keine rechtliche Automatik.
- **Wortwahl:** Die Abstufung von «Signatur geprüft» über «müsste geprüft
  sein» bis «hat sicher jemand gemacht» klingt gesprochen und nahbar. Der
  Produktabsatz bleibt konkret und frei von Buzzword-Bingo.
- **Rhythmus:** Bild-Hook, kurze Viererfolge, Pointe, fachliche Einordnung und
  offene Frage bilden einen klaren gesprochenen Bogen.

Kleine Distanz zu `1,00`: Der Produktabsatz ist sachlicher und dichter als der
sehr persönliche Auftakt, kippt aber nicht in Corporate-Sprache.

**Pflichtrevision:** keine. Keine Umschreibung erforderlich.

## POST 2 — 15-Minuten-Test mit Stoppuhr und Klemmbrett

**Score: 0,92 — BESTANDEN**

- **Persönliche Stimme:** «Vor einer Demo würde ich ...» und «Meine
  Generalprobe» setzen Roman sichtbar ins Geschehen, ohne eine tatsächlich
  durchgeführte Demo zu behaupten. Folienschlacht, Stoppuhr und Klemmbrett sind
  eigenständige, merkfähige Bilder.
- **Haltung:** Der Text plädiert für einen kleinen, nachvollziehbaren Prozesstest
  statt Show. Datenweg, Prüfinformation und menschliche Entscheidung werden
  verantwortungsvoll voneinander abgegrenzt.
- **Wortwahl:** Die vier Fragen sind konkret und zielgruppennah. «Die Stoppuhr
  misst den Datenweg, nicht juristische Sicherheit» bringt die fachliche Grenze
  prägnant und bildhaft auf den Punkt.
- **Rhythmus:** Hook, nummerierte Generalprobe, Produktantwort, Grenzziehung und
  Schlussfrage funktionieren sauber. Der technisch dichte Produktabsatz bremst
  den Takt nur leicht.

Kleine Distanz zu `1,00`: Die Checkliste wirkt methodischer als spontan und der
mittlere Produktabsatz ist relativ dicht. Die Ich-Perspektive und die starken
Bilder halten den Text dennoch klar in Romans Stimme.

**Pflichtrevision:** keine. Keine Umschreibung erforderlich.

## Ergebnis

| Text | Score | Urteil | Rückgabe an Copywriter |
|---|---:|---|---|
| POST 1 | 0,94 | BESTANDEN | nein |
| POST 2 | 0,92 | BESTANDEN | nein |

Beide Texte liegen über `0,70`. Es gibt keine Pflichtrevision und keine
Rückgabe an den Copywriter. Entsprechend der Aufgabenbegrenzung wurde keine
Textrevision vorgenommen.

Die Ausgangstexte, Queue, Checkboxen, Freigaben, Planung, das Stilprofil,
`learning.json` und der Approved-Korpus blieben unverändert. Es wurde nichts
freigegeben oder veröffentlicht.
