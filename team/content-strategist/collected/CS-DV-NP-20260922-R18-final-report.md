# CS-DV-NP-20260922-R18 — Abschlussbericht

## Ergebnis

- Laufart: **Neuanlage**, keine Fortsetzung. Vor Beginn lagen im neuen
  Kampagnenpfad null Posts und kein Paar fertiger, stilbestandener, ungequeuter
  Posttexte vor.
- Copywriter: exakt zwei neue Texte, 1.222 / 1.291 Unicode-Codepoints.
- Style-Evaluator: Post 1 **0,84 BESTANDEN**, Post 2 **0,87 BESTANDEN**;
  keine Pflichtrevision, Texte unverändert.
- Reviewer, einmalige reguläre Runde: Post 1 **FREIGEGEBEN**, Post 2
  **FREIGEGEBEN**; keine Pflichtänderung.

## Queue-Belege

Beide Texte wurden unmittelbar nach dem Reviewer-Ergebnis ausschliesslich mit
`./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" add --kind post --text "..."`
abgelegt.

| ID | Zeichen | SHA-256 des gespeicherten Texts | Checkbox | Publish-Beleg |
|---|---:|---|---|---|
| `post-2026-09-22-0001` | 1.222 | `40f225091c910408718f017f53fef27983b4b824a5874989dad92838659b7098` | leer | `published_url: null`, `published_at: null`, `approval_origin: null` |
| `post-2026-09-22-0002` | 1.291 | `ff62a690e9d8a1941913b3437a703c2c93a13fcfc116e7b33c42f8e6549c57e4` | leer | `published_url: null`, `published_at: null`, `approval_origin: null` |

- Queue-Postbestand vorher: **0**.
- Queue-Postbestand nachher: **2**.
- Neue Posts dieses Laufs: **exakt 2**.
- Beide gespeicherten Texte stimmen hash- und längengleich mit den stil- und
  reviewer-geprüften Fassungen überein; `generated_text` entspricht jeweils
  `text`, `li-jobs` meldete `adjusted: false`. Daher keine erneute Kontrollrunde.
- `schedule.md` und `log.md` sind in diesem Kampagnenpfad nicht vorhanden.
- Für Post 1 scheiterte der automatische Bildversuch wegen fehlender
  Generator-/Netzkonfiguration; der Post wurde trotzdem ohne Bildpfad korrekt in
  approvals.md abgelegt. Es erfolgte kein separater Bild- oder Publish-Schritt.

Es wurde nichts veröffentlicht, nicht geschedult, nicht freigegeben und keine
Freigabe-Checkbox angekreuzt.
