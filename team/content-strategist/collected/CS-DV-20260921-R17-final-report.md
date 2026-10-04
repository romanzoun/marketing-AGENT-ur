# CS-DV-20260921-R17 — Abschluss

- Wiederaufnahme: **nein**. R16 war vollständig abgeschlossen; keine zwei
  neueren stilbestandenen, queuefreien Texte vorhanden.
- POST 1: „Garderobenzettel — Prüfinformation und PDF-Version zusammenhalten“;
  Stil **0,82 BESTANDEN**, Reviewer **FREIGEGEBEN**; Queue-ID
  `post-2026-09-21-0001`, 1.125 Codepoints, SHA-256
  `fa4f3399a2135c62f1215b3ee4c1911d47b3b5631442296f6985ae8f181b3d47`.
- Ursprünglicher POST 2: Stil **0,90 BESTANDEN**, Reviewer **ABGELEHNT** als
  funktionale Dublette; nicht gequeuet und nicht erneut geprüft.
- Ersatz POST 2-I2: „Klingelbeschriftung — Eingangskanal ist keine
  Signaturprüfung“; Stil **0,88 BESTANDEN**, Reviewer **FREIGEGEBEN**; Queue-ID
  `post-2026-09-21-0002`, 1.278 Codepoints, SHA-256
  `61afa5d75a2e5eabe4590f8b7b645220b69a067a7475dd2b6ef67e28430a6eb8`.
- Ausgeführte Queue-Schreibvorgänge: zweimal
  `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" add --kind post --text "…"`.
- Nachweis: `approvals.md` vor Lauf 0 Posts, nach Lauf exakt 2 Posts; beide
  Checkboxen leer, `approval_origin: null`, `text == generated_text`, Hashes
  identisch mit den reviewer-freigegebenen Fassungen. Beide IDs fehlen in
  `schedule.md` und `log.md`.
- Die automatische optionale Bildgenerierung für 0002 scheiterte; der
  Text-Queue-Eintrag blieb erfolgreich und unverändert. Nichts freigegeben,
  angekreuzt, geplant oder veröffentlicht.
