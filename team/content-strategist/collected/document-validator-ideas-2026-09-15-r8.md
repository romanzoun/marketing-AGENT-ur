# CS-DV-20260915-R8 — exakt zwei Post-Ideen

Kampagne: `Kampagnen/document validator/kampagne.yaml`

Queue-Ausgangsstand: `approvals.md` enthält 0 Posts; SHA-256
`4254f974cd4e013ef0eeb34039f1e1a6531911cf4d90782a1c6c55e85aaccd60`.

## Idee 1 — Wenn die PDF-Prüfung „piept“

- Blickwinkel: Nicht der reibungslose Standardfall zeigt die Qualität eines
  Records-/Compliance-Prozesses, sondern der verantwortete Ausnahmeweg bei einer
  unklaren Signatur- oder Zertifikatsauswertung.
- Bild/Hook: Flughafenkontrolle — interessant wird es, wenn es piept und kurz alle
  sehr professionell auf die Zuständigkeit des anderen warten.
- Fachlicher Kern: Document Validator prüft ZertES-/eIDAS-signierte PDFs sowie
  Signatur- und Zertifikatsinformationen belastbarer; die PDF bleibt in der
  eigenen Umgebung, ihr Hash wird lokal gebildet. Die Auswertung ersetzt weder
  Zuständigkeiten noch menschliche Beurteilung, Freigabe oder Rechtsprüfung.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance/Legal Ops.
- Diskussionsfrage: Wer besitzt den Ausnahmeweg vor Archivierung oder Freigabe?

## Idee 2 — Übergabezettel für den Browser-Agenten

- Blickwinkel: Wenn ein AI-Agent im Browser einen Prüfschritt übernimmt, braucht
  der menschlich verantwortete Workflow einen nachvollziehbaren Handover statt
  einer Verwechslung von technischer Prüfung und Mandat.
- Bild/Hook: Ein AI-Agent mit angeklebtem Schnurrbart ist noch kein Kollege mit
  Mandat; beim Staffelstab gehört ein Übergabezettel dazu.
- Fachlicher Kern: Document Validator liefert Signatur-/Zertifikatsauswertung;
  BIV kann Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen. Keines der
  Produkte erkennt Mensch versus Agent, erteilt einem Agenten Mandat oder ersetzt
  die menschliche Freigabe.
- Enger ICP: Teams mit signierten PDFs in Records-/Freigabeprozessen und
  auditierbaren Browser-/Backoffice-Abläufen.
- Diskussionsfrage: Welche Angaben muss der Handover enthalten, bevor der nächste
  Schritt angestossen wird?

## Verbindliche Leitplanken für beide Texte

- Deutsch, jeweils höchstens 1.300 Unicode-Zeichen.
- Persönlich, trocken witzig und bildhaft; kein Marketing-Sprech, keine
  erfundene Biografie, kein Heilsversprechen.
- Vollständiger Kampagnen-CTA samt exaktem UTM-Link und alle drei Pflicht-Hashtags
  `#Compliance`, `#eIDAS`, `#RecordsManagement` in jedem Post.
- Beide sind getrennte Freigabekandidaten. Wegen `posts_per_run: 1` darf später
  höchstens einer pro Veröffentlichungszyklus ausgeführt werden.
- Keine Queue-, Checkbox-, Planungs- oder Veröffentlichungsaktion durch
  delegierte Agenten.
