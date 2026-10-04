# Reviewer-Prüfung — RV-FR-DV-20261001-R4

- Datum: 2026-10-01
- Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`
- Zielblock: `reshare-2026-10-01-0002`
- URL: `https://www.linkedin.com/feed/update/urn:li:share:7510616066146955265/`
- Autorbindung: `Felix Wunderer, Dr. likes this`; Originalbeitrag von Michel
  Siegenthaler mit eingebettetem Swisscom-Beitrag
- Prüfumfang: einmalige Schlussprüfung des übergebenen finalen Text- und
  Queue-Stands

## Urteil

**ABGELEHNT/GESPERRT — nicht intern freigegeben.**

Die Content-Strategist-Sperre ist korrekt. Der Originalbeitrag behandelt den
Swisscom-Breitband-Hotline-/connect-Testsieg sowie Customer Experience,
Kundenservice, Qualität, Innovation und Teamwork. Er besitzt keinen belastbaren
Bezug zu Objective, engem ICP, Kernthemen oder Produkten dieser Kampagne.
`text: ''` muss exakt leer bleiben. Der Kandidat ist kein ausdrücklich
kampagnenrelevanter Awareness-Reshare ohne Begleittext, sondern ein verworfener
Keyword-Treffer.

## Deterministische Vorprüfung

- Zielblock genau einmal vorhanden; ID `reshare-2026-10-01-0002`,
  `kind: reshare`, `source_job_id: job-0011`, URL und Autorbindung stimmen mit
  dem Scout-Artefakt überein.
- Die vollständige rohe `note` ist zwischen Queue und Scout-Artefakt bytegleich.
  Der SHA-256 des YAML-Notiz-Payloads ist in beiden Darstellungen
  `15527b6a31acef442c15ef6e61e4f72cd6778d728931dd31e71ba3ac3bd4944f`;
  nach YAML-Dekodierung sind es jeweils 1.753 Bytes beziehungsweise 1.717
  Unicode-Codepoints mit SHA-256
  `34d0fadda32824af70e69d29bd8dbbf701fe105502e28438b72e56fc70335429`.
- `text: ''` ist exakt leer: **0 Unicode-Codepoints**. Das Limit
  `max_post_chars: 1300` ist formal eingehalten.
- `required_hashtags: []`: Es gibt keine Pflicht-Hashtags; der Leertext
  verletzt keine Hashtag-Pflicht.
- `reshare_with_comment: false`; es existieren weder Begleittext noch CTA.
- Stilprüfung ist mangels Text nicht anwendbar. Korrekt unverändert:
  `evaluation_score: null`, `evaluation_note: ''`, `evaluated_at: null`.
- `fit_score: 0.0`; die konkrete `fit_note` deckt Objective, Audience, Topics,
  Banned Topics, Products und CTA nachvollziehbar ab.
- Die Freigabe-Checkbox ist leer (`- [ ] freigeben`). `publish_at`,
  `published_at`, `published_url`, `approval_origin` und
  `auto_approval_threshold` sind `null`.
- ID und URL fehlen vollständig in `schedule.md` und `log.md`.

## Inhaltliche Prüfung

- **Objective:** Der Hotline-Testsieg schafft weder Problembewusstsein noch
  Expertise oder Vertrauen für die Prüfung digital signierter Dokumente vor
  Archivierung oder Freigabe. Profil-, Website-, Gesprächs- oder Demo-Ziel
  wären daraus nicht natürlich motiviert.
- **Audience:** Customer Experience und Breitband-Hotline adressieren nicht die
  enge Zielgruppe aus Records/Posteingang, Vertragsadministration, Compliance
  Operations, Records Management, ECM/DMS oder Legal Operations und keinen
  entsprechenden Prüfprozess.
- **Topics und Produkte:** Es fehlen signierte PDFs, ZertES/eIDAS,
  Signatur-/Zertifikatsauswertung, Identität/Berechtigung, Hash-Prüfung,
  Audit-Trail, Records/Archiv, ECM/DMS sowie konkrete Backoffice- oder
  Browser-Prüfprozesse. Document Validator und Business Identity Validator
  haben im Originalbeitrag keine natürliche fachliche Rolle.
- **Banned Topics:** Politik, Religion, Konkurrenz-Bashing, juristische
  Garantien und unbelegte Sicherheitsversprechen werden im Originalbeitrag
  nicht berührt. Eine nachträglich erfundene DocVal-/BIV-Brücke würde jedoch
  den Guardrail `generische Digitalisierungsposts ohne konkreten Bezug`
  verletzen. Die Begriffe `Innovation` und `Swisscom` allein schaffen keinen
  Kampagnenfit.
- **CTA:** Produktlink, Demo-CTA oder `DM oder Kommentar` wären künstlich. Auch
  ein kommentarloser Awareness-Reshare ist nicht zulässig, weil der
  Originalbeitrag selbst keinen Kampagnenkern trägt.
- **Fakten, Spam und Markensicherheit:** Der Leertext übernimmt oder bestätigt
  keine Angaben zu Testergebnis, Punktezahl, DACH-Sieg oder Servicequalität.
  Der Originalpost ist nicht als rechtswidrig, beleidigend oder anderweitig
  markenriskant auffällig; sein Reshare wäre in dieser Kampagne jedoch
  thematisch verwässernd und spamartig. Die Sperre schützt die fachliche
  Positionierung.
- **Stimme:** Mangels Begleittext nicht anwendbar. Es ist kein Text zu erzeugen
  und keine Copywriter-Rückgabe angezeigt, weil der Originalbeitrag selbst
  kampagnenfremd ist.

## Queue- und Veröffentlichungsschutz

`approvals.md`, `schedule.md`, `log.md` und alle Queue-Inhalte wurden vom
Reviewer nicht verändert. Keine Checkbox wurde gesetzt, kein Text erzeugt, kein
Termin gesetzt, nichts verschoben, freigegeben oder veröffentlicht. Es gab keine
LinkedIn-, Browser- oder Operator-Aktion und keine Folgeagenten. Dieses
Reviewer-Urteil ist keine Nutzerfreigabe und berechtigt nicht zum
Veröffentlichen.
