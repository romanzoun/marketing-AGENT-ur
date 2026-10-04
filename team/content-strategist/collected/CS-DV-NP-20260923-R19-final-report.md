# CS-DV-NP-20260923-R19 — Abschlussbericht

## Ergebnis

- Laufart: **Neuentwicklung**, keine Wiederaufnahme. Der jüngste Zweierlauf R18
  war bereits vollständig reviewed und gequeut; danach lag kein Paar neuer,
  fertiger und stilbestandener Posttexte ohne Queue-Eintrag vor.
- Copywriter: exakt zwei neue Endtexte in einer regulären Runde. Der ursprünglich
  vorgesehene Kontrollpunkt-Winkel für Post 1 war funktional belegt und wurde
  innerhalb derselben Runde durch den freien Kern „eine technische Prüfung,
  mehrere Fachentscheidungen“ ersetzt. Post 2 blieb beim neuen
  Mehrfachsignatur-Winkel.
- Style-Evaluator: Post 1 **0,86 BESTANDEN**, Post 2 **0,82 BESTANDEN**;
  keine Pflichtrevision und keine zweite Stilrunde.
- Reviewer, einmalige reguläre Runde: Post 1 **FREIGEGEBEN**, Post 2
  **FREIGEGEBEN**; keine Pflichtänderung und keine weitere Reviewer-Runde.

## Queue-Belege

Beide Texte wurden nach dem Reviewer-Ergebnis ausschliesslich mit
`./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" add --kind post --text "..."`
in `approvals.md` abgelegt. `li-jobs` meldete für beide `adjusted: false`.

| ID | Reviewer-Länge | Checkbox | Publish-Beleg | li-jobs Evaluation |
|---|---:|---|---|---:|
| `post-2026-09-23-0001` | 1.122 | leer | `published_url: null`, `published_at: null`, `approval_origin: null` | 0,84 |
| `post-2026-09-23-0002` | 1.297 | leer | `published_url: null`, `published_at: null`, `approval_origin: null` | 0,93 |

- Queue-Postbestand vorher: **2**.
- Queue-Postbestand nachher: **4**.
- Neue Posts dieses Laufs: **exakt 2**.
- Neue IDs dieses Laufs: `post-2026-09-23-0001` und
  `post-2026-09-23-0002`.
- Beide Freigabe-Checkboxen sind leer. Es wurde nichts nutzerfreigegeben,
  verschoben, veröffentlicht oder aktiv eingeplant; die von `li-jobs`
  gespeicherten editierbaren Terminvorschläge sind keine Schedule-Einträge.

