# SE-DV-20260917-R14 — einmalige Stilprüfung

Geprüft wurden genau einmal ausschliesslich die zwei unveränderten R14-Markertexte aus `team/copywriter/collected/document-validator-two-2026-09-17-r14.md`. Massgeblich waren Romans Stilprofil, der vollständige Lernstand, alle freigegebenen Beispiele, die R14-Ideen und die aktuellen Posttexte in `approvals.md`, `schedule.md` und `log.md`. Schwelle: **BESTANDEN ab 0,70**.

## Textidentität

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Identität |
|---|---:|---:|---:|---|---|
| POST 1 | 1.166 | 1.181 | 16 | `39c6748c9cc105d4a4682e707bd4f7d229122f7a396aa7dc8b623d968ff4cf05` | bestätigt |
| POST 2 | 1.144 | 1.163 | 20 | `41df29d212d95621f67c737279f8f7bfa59700ff2bbac92d2ef1d327e9954df4` | bestätigt |

Die Hashes beziehen sich auf den exakten UTF-8-Text zwischen Start- und Endmarker, ohne Marker und ohne den trennenden LF vor dem Endmarker. Beide Texte sind NFC-normalisiert und stimmen mit den im Eingabeartefakt angegebenen Längen und Hashes überein.

## POST 1 — Cursor ohne Pass

- **Score: 0,93**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**

Der Hook ist bildhaft, trocken und sofort persönlich: Der höflich klickende Cursor macht die Mensch-vs.-Agent-Grenze ohne Zukunftspathos greifbar. Kurze Sätze, Ich-Perspektive und die konkrete Schlussfrage treffen Romans Rhythmus. Die beiden knappen Produktgrenzen wirken nicht wie ein ausführlicher Disclaimer, sondern sichern den eigenständigen Gedanken sauber ab. Leichter Abzug für die etwas abstrakte Passage zu "belastbaren Informationen" und "Vertrauenssignal".

Keine exakte Dublette unter den aktuell 3 Approval-, 12 Schedule- und 4 Log-Posts. Auch keine funktionale Dublette: Der Browser kommt zwar bereits als Arbeitsort vor, dort geht es aber um Kontextwechsel und integrierte PDF-Prüfung. Hier trägt die Erkennbarkeitsgrenze der Oberfläche und die Frage, welches prüfbare Signal neben dem Cursor zählt.

## POST 2 — innere Nebelmaschine

- **Score: 0,92**
- **Urteil: BESTANDEN**
- **Pflichtrevision: nein**

"Meine innere Nebelmaschine" ist ein starker selbstironischer Marker. "Grosser Auftritt. Schlechte Sicht." und "Weniger Nebel, mehr Substantive" geben dem Text einen klaren gesprochenen Takt. Die Beschaffungsszene übersetzt ein grosses Rechtswort in zwei konkrete Prüffragen und bleibt damit fachlich, menschlich und ohne Werbesprech. Die knappe Grenze zur automatischen rechtlichen Würdigung ist sachlich nötig, kostet gegenüber Romans jüngster Kürzungspräferenz aber einen kleinen Anteil.

Keine exakte Dublette. Die Nebel-Metapher berührt den geplanten "grünen Haken im Nebel"; DocVal-/BIV-Rollen und fehlende Rechtsgarantie erscheinen auch in bestehenden Posts. Funktional bleibt R14 eigenständig: Der tragende Nutzen ist eine Beschaffungs- und Sprachregel für den Umgang mit der Behauptung "juristisch sicher", nicht die Sicht hinter einem Statussignal, die technische/fachliche Freigabetrennung oder der BIV-Kontext als solcher.

## Ergebnis

| Text | Score | Urteil | Pflichtrevision |
|---|---:|---|---|
| POST 1 | 0,93 | **BESTANDEN** | nein |
| POST 2 | 0,92 | **BESTANDEN** | nein |

Beide Texte überschreiten die Schwelle von 0,70. Es erfolgt keine Rückgabe an den Copywriter und keine Textänderung. Dieses Urteil ist keine Nutzerfreigabe und löst keine Queue-, Checkbox-, Planungs-, Profil-, Lern-, Korpus-, Operator- oder Veröffentlichungsaktion aus.
