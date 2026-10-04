# Copywriter-Bericht — CW-FC-DV-20260912-R6

- Datum: 2026-09-12
- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Queue: `Kampagnen/document validator/queue/approvals.md`
- Umfang: ausschliesslich die `text:`-Felder von `comment-2026-09-12-0003` und `comment-2026-09-12-0004`
- Status: beide Texte eingetragen; keine Freigabe, Planung, Verschiebung oder Veröffentlichung

## comment-2026-09-12-0003

- Sprache: Englisch, entsprechend dem Zielpost im vollständigen `note:`-Feld
- Unicode-Zeichenzahl: 347
- Sätze: 2
- Link: keiner
- Pflicht-Hashtags: `#Compliance #eIDAS #RecordsManagement`

> A sales agent can sound wonderfully human, but the interesting part begins when it is allowed to act. For me, the business case is incomplete until identity, permissions and a traceable handover are as clear as the conversion target—otherwise the shiny new colleague is wearing a name badge written in pencil. #Compliance #eIDAS #RecordsManagement

## comment-2026-09-12-0004

- Sprache: Englisch, entsprechend dem Zielpost im vollständigen `note:`-Feld
- Unicode-Zeichenzahl: 307
- Sätze: 2
- Link: keiner
- Pflicht-Hashtags: `#Compliance #eIDAS #RecordsManagement`

> Keeping people in a familiar interface sounds like the quiet kind of progress I like: less wallet tourism, more useful workflow. The real test, for me, is whether issuer, verifier and permission context remain just as clear when the plumbing disappears behind the wall. #Compliance #eIDAS #RecordsManagement

## Integritäts- und Konfliktprotokoll

- Der Copywriter änderte in der Queue ausschliesslich die beiden Ziel-`text:`-Felder. Job-IDs, URLs, Autoren, vollständige `note:`-Felder und Checkboxen blieben auch in der Endkontrolle unverändert.
- Beim ersten Patch trafen die zwei nicht kontextualisierten Ersetzungen vorübergehend die ebenfalls leeren `text:`-Felder der Jobs `comment-2026-09-12-0001` und `comment-2026-09-12-0002`. Der unmittelbare Blockabgleich erkannte dies; beide Felder wurden exakt auf `text: ''` zurückgesetzt, bevor die Zielblöcke 0003/0004 ID-gebunden befüllt wurden. Die Endkontrolle findet beide neuen Texte ausschliesslich in 0003/0004.
- Konflikt: Eine parallele Queue-Neuspeicherung änderte nach der Copywriter-Füllung in beiden Zielblöcken `source_job_id` von `job-0003` auf `job-0001`, ergänzte `publish_at` (`2026-09-13T12:00` / `2026-09-13T14:00`), kopierte die Texte nach `generated_text` und schrieb Evaluationsdaten (0,73 / 0,83; `evaluated_at: 2026-09-12T15:20`). Diese fremden Änderungen wurden nicht zurückgesetzt; beide Zieltexte blieben inhaltlich exakt erhalten.
- Die Stil- und Reviewer-Kette wird gemäss Auftrag durch den Engagement Scout gesteuert; keine Weiterdelegation durch den Copywriter.
