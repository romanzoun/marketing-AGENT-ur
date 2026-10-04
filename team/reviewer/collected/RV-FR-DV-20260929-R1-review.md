# Reviewer-Bericht — RV-FR-DV-20260929-R1

Datum: 2026-09-29  
Kampagne: `DocVal + BIV — vor Archiv / vor Freigabe` (Version 2)  
Prüfumfang: ausschließlich `reshare-2026-09-29-0001` und `reshare-2026-09-29-0002` in `approvals.md`

## Gesamturteil

Beide Kandidaten sind **ABGELEHNT/GESPERRT**. Keiner der Originalbeiträge hat den erforderlichen konkreten Bezug zum engen ICP, zu eingehenden signierten PDFs, Signatur-/Zertifikatsprüfung, Records/Archiv, Audit/ECM, Document Validator oder BIV. Die leeren Begleittexte dürfen nicht als Awareness-Ausnahme verstanden werden: Beide Jobs sind ausdrücklich verworfene Treffer, keine kampagnenrelevanten Awareness-Reshares.

## Deterministische Vorprüfung

- Beide `text:`-Werte sind exakt `''` und haben 0 Unicode-Codepoints. Damit werden `max_post_chars: 1300` und `max_comment_chars: 500` nicht überschritten.
- `required_hashtags: []`; es fehlen daher keine Pflicht-Hashtags.
- Beide Freigabe-Checkboxen sind leer.
- Je Job: `reshare_with_comment: false`, `fit_score: 0.0`, `publish_at: null`, `published_at: null`, `published_url: null`, `approval_origin: null`.
- Beide Blöcke enthalten keine URN; es wurde keine URN ergänzt oder erfunden.
- Beide IDs kommen in `approvals.md` jeweils genau in Überschrift und `id:` vor und sind weder in `schedule.md` noch in `log.md` vorhanden. Auch beide URLs fehlen dort.
- Die deterministischen Textregeln sind wegen des bewusst leeren Begleittexts formal erfüllt; sie begründen keine Reshare-Freigabe. CTA und Stil-Score sind ohne Begleittext nicht anwendbar.

## Einzelurteile

### reshare-2026-09-29-0001 — ABGELEHNT/GESPERRT

- Bindung: ID, URL `https://lnkd.in/p/ex-iKWdW`, Autor `Michael Muoghalu`, Volltext unter `note:` und konkrete `fit_note` passen zusammen. Der geparste Queue-Volltext ist mit dem Scout-Artefakt exakt identisch (1.645 Codepoints; SHA-256 `2a816d0d59402ce022d81fa5063997c00e290e322d3f1fb795e527f57ced5dbe`).
- Semantik: Der Originalbeitrag behandelt Tokenisierung/RWA, GTM, Branchenwissen und die Rolle von Mittelsleuten. Er nennt weder signierte PDFs noch Signatur-/Zertifikatsprüfung, Records/Archiv, Audit, ECM, BIV oder einen konkreten Backoffice-/Browser-Prüfprozess.
- Kampagnenbezug: Ein abstrakter Vertrauens- oder Technologiewandel-Anklang reicht nicht. Der Beitrag fällt unter das verbotene Muster `generische Digitalisierungsposts ohne konkreten Bezug` und adressiert weder den engen ICP noch Produkte oder Kampagnen-CTA.
- Stimme/Fakten/Spam/Markensicherheit: Kein eigener Text zu prüfen; der Originalpost enthält keinen tragfähigen fachlichen Anker für Romans Positionierung. Ein Reshare würde die Kampagne thematisch verwässern. Die konkrete Sperrnotiz und Fit 0,0 sind korrekt.

### reshare-2026-09-29-0002 — ABGELEHNT/GESPERRT

- Bindung: ID, URL `https://lnkd.in/p/eZ25MYbB`, Autor `Realize`, Volltext unter `note:` und konkrete `fit_note` passen zusammen. Alle 16 nichtleeren Textzeilen stehen vollständig und in derselben Reihenfolge in Queue und Scout-Artefakt. Der YAML-geparste Queue-Wert faltet gegenüber der Scout-Darstellung lediglich zwei Leerzeilen; es fehlt kein inhaltlicher Text. Queue-Notiz: 432 Codepoints; SHA-256 `e0fd4f60951dc9e546a12ef0be4b6e918963d5d002dac8a5702901e7853550f9`.
- Semantik: Es handelt sich um eine beworbene Growth-Marketing-Anzeige zu Targeting, Launches, Placements und Account Management. Sie enthält keinen Bezug zum Objective, engen ICP, zu Kampagnenthemen, Document Validator, BIV oder dem Kampagnen-CTA.
- Stimme/Fakten/Spam/Markensicherheit: Ein Reshare der Promotion wäre werblich, fachlich beliebig und für Romans Positionierung off-brand bzw. spamnah. Die konkrete Sperrnotiz und Fit 0,0 sind korrekt.

## Queue-Schutzstatus

Die beiden Queue-Blöcke wurden nicht geändert. Keine Checkbox wurde gesetzt, kein Text erzeugt, keine Freigabe erteilt, kein Termin gesetzt, nichts nach `schedule.md` oder `log.md` verschoben und nichts veröffentlicht. Es gab keinen Operator-, Browser- oder LinkedIn-Aufruf. Dieses Reviewer-Urteil ist keine Nutzerfreigabe.
