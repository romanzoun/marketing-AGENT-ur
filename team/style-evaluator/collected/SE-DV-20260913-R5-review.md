# Stilprüfung SE-DV-20260913-R5

## Prüfumfang und Bewertungsbasis

Geprüft wurden ausschliesslich die Texte zwischen `POST 1 BEGIN/END` und
`POST 2 BEGIN/END` in
`team/copywriter/collected/document-validator-two-2026-09-13-r5.md`.
Bewertet wurde die geschätzte Freigabewahrscheinlichkeit anhand von persönlicher
Stimme, Haltung, Wortwahl und Rhythmus. Schwelle: ab `0,70` **BESTANDEN**,
darunter **REVISION** und Rückgabe an den Copywriter.

`team/style/learning.json` enthält keine Nutzerkorrekturen, Muster oder
Freigaben. Unter `team/style/approved/` liegt nur die README; ein empirischer
Approved-Korpus fehlt noch. Auch `config/personal_profile.yaml` enthält keine
biografischen Angaben. Die Bewertung stützt sich deshalb auf das explizite
Stilprofil und die Kampagnenstimme, ohne Erfahrungen oder biografische Details
zu unterstellen.

## Deterministische Textidentität

Gezählt wurden Unicode-Codepoints des reinen Textes zwischen den Markern.
Interne Zeilenumbrüche zählen mit; Marker und die direkt angrenzenden
Zeilenumbrüche zählen nicht.

| Text | Unicode-Codepoints | interne Zeilenumbrüche | SHA-256 des reinen Textes |
|---|---:|---:|---|
| POST 1 | 1.144 | 16 | `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97` |
| POST 2 | 1.203 | 19 | `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030` |

## POST 1 — Regionalzug und stille Post

**Score: 0,94 — BESTANDEN**

- **Persönliche Stimme:** Regionalzug und «stille Post» machen einen abstrakten
  Kontrollprozess sofort greifbar. «Mein Lieblingssatz ... Also: überhaupt
  nicht.» bringt die geforderte Ich-Stimme und trockene Selbstironie klar ein.
- **Haltung:** «Für mich gehört der Kontrollpunkt ...» ist eine konkrete,
  pragmatische Position. Die Entscheidung bleibt ausdrücklich beim zuständigen
  Menschen; der Text verspricht keine rechtliche Automatik.
- **Wortwahl:** Die Staffelung von «Signatur geprüft» zu «hat sicher jemand
  gemacht» klingt mündlich und nahbar. Der Produktabsatz ist sachlicher, bleibt
  aber konkret und frei von Buzzword-Bingo.
- **Rhythmus:** Kurzer Bild-Hook, Viererfolge, zugespitzte Mini-Erzählung,
  fachliche Einordnung und offene Frage ergeben einen sehr sauberen gesprochenen
  Bogen.

**Pflichtrevision:** keine.

Optionale Verdichtung, nicht erforderlich:

> Das Ergebnis hilft Records- und Compliance-Teams beim Prüfen. Entscheiden tut
> es nicht, freigeben auch nicht. Das bleibt beim zuständigen Menschen.

Diese Variante verdichtet lediglich den etwas sachlicheren Grenzabsatz; der
vorliegende Text besteht bereits ohne Änderung.

## POST 2 — 15-Minuten-Test mit Stoppuhr und Klemmbrett

**Score: 0,92 — BESTANDEN**

- **Persönliche Stimme:** «Vor einer Demo würde ich ...» und «Meine
  Generalprobe» setzen Roman sichtbar ins Geschehen, ohne eine tatsächlich
  durchgeführte Demo zu behaupten. Folienschlacht, Stoppuhr und Klemmbrett sind
  eigenständige, merkfähige Bilder.
- **Haltung:** Der Text plädiert für einen kleinen, nachvollziehbaren Prozesstest
  statt Show. Die klare Grenze zwischen Datenweg, Prüfinformation und
  menschlicher Entscheidung wirkt glaubwürdig und verantwortungsvoll.
- **Wortwahl:** Die vier Fragen sind konkret und zielgruppennah. Der Produktabsatz
  ist technisch dichter und etwas weniger mündlich, wird aber durch «Die
  Stoppuhr misst den Datenweg, nicht juristische Sicherheit» stark aufgefangen.
- **Rhythmus:** Hook, nummerierte Generalprobe, Produktantwort, Grenzziehung und
  Schlussfrage funktionieren klar. Der lange Satz zur Auswertung der Signatur-
  und Zertifikatsinformationen bremst den Takt leicht; das bleibt ein kleiner,
  nicht revisionspflichtiger Abzug.

**Pflichtrevision:** keine.

Optionale Verdichtung, nicht erforderlich:

> Beim Swisscom Document Validator bleibt die PDF in der eigenen Umgebung, ihr
> Hash wird lokal gebildet. Er prüft Signatur und Zertifikatsinformationen bei
> ZertES-/eIDAS-signierten PDFs belastbarer. Der Business Identity Validator
> kann Zeichner, Unternehmen und Berechtigung ergänzen.

Die Fassung teilt den technisch dichten Satz in einen mündlicheren Rhythmus;
der vorliegende Text besteht bereits ohne Änderung.

## Ergebnis

| Text | Score | Urteil | Rückgabe an Copywriter |
|---|---:|---|---|
| POST 1 | 0,94 | BESTANDEN | nein |
| POST 2 | 0,92 | BESTANDEN | nein |

Kein Text liegt unter `0,70`; daher ist keine Pflichtrevision und keine erneute
Stilbewertung vor der Freigabe-Queue erforderlich. Die optionalen
Umschreibungen sind keine Auflagen.

Die Ausgangstexte, Queue, Checkboxen, Freigaben, Stilprofil, `learning.json`,
Approved-Korpus, Planung und LinkedIn blieben unverändert. Es wurde nichts
freigegeben oder veröffentlicht.
