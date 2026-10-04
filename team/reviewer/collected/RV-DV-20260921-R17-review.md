# RV-DV-20260921-R17 — einmalige abschliessende Reviewer-Prüfung

Geprüft wurden genau einmal ausschliesslich die zwei unveränderten reinen
Markertexte aus
`team/copywriter/collected/document-validator-two-2026-09-21-r17.md` gegen die
aktive Kampagne, das Strategiebriefing, das persönliche Profil, das Stilprofil,
den Stilbericht und den aktuellen Postbestand in `approvals.md`, `schedule.md`
und `log.md`.

## Deterministische Vorprüfung

| Text | Unicode-Codepoints | Limit | SHA-256 | Pflicht-Hashtags | CTA/UTM-Link | Exakte Dublette |
|---|---:|---|---|---|---|---|
| POST 1 | 1.125 | bestanden | `fa4f3399a2135c62f1215b3ee4c1911d47b3b5631442296f6985ae8f181b3d47` | alle drei, je 1× | vollständig und exakt, 1× | keine |
| POST 2 | 1.189 | bestanden | `f46a3161d485a336eb5cb04604c04c6bfd63bd76ba68a87fa807ef1a878d9cd7` | alle drei, je 1× | vollständig und exakt, 1× | keine |

Bestätigt sind je Text `#Compliance`, `#eIDAS` und `#RecordsManagement` sowie
genau der zulässige Kampagnenlink
`https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice`.
Der aktuelle Bestand umfasst 0 Posts in `approvals.md`, 20 Posts in
`schedule.md` und 6 Posts in `log.md`.

## POST 1 — **FREIGEGEBEN**

**Begründung:**

- Deutsch, enger ICP und klares Kampagnenthema: signierte PDFs in
  Records/Posteingang, Vertragsadministration und Compliance Ops vor Freigabe
  oder Archivierung.
- Persönliche, trockene Stimme mit verständlicher Garderobenzettel-/Konfetti-
  Metapher; Stilprüfung mit 0,82 **BESTANDEN**.
- Vollständiger Kampagnen-CTA mit exakt zulässigem UTM-Link; alle drei
  Pflicht-Hashtags vorhanden.
- Fakten und Produktgrenzen eingehalten: Der Document Validator wird auf
  Signatur- und Zertifikatsinformationen sowie lokalen Hash/Dokumentverbleib in
  der eigenen Umgebung begrenzt. Die eindeutige Zuordnung zur geprüften
  PDF-Version ist ausdrücklich als organisatorische Aufgabe des eigenen
  Records-/ECM-Prozesses formuliert.
- Keine Behauptung automatischer Versionierung, Archivierung, Freigabe,
  Rechtswirkung, Revisionssicherheit oder eines vollständigen Audit-Trails.
- Kein Spam- oder Markensicherheitsproblem, kein Wettbewerber-Bashing und keine
  gesperrten Themen.
- Keine exakte oder funktionale Dublette. Der vorhandene
  `Vertrag_final_SIGNIERT_v7.pdf`-Post behandelt Dateinamen/Labels als
  unzureichenden Prüfnachweis; dieser Text behandelt dagegen die mögliche
  Fehlzuordnung eines Prüfergebnisses zu einer anderen PDF-Version. Auch die
  bestehende Garderoben-Metapher betrifft den Datenweg/Fremd-Cloud-Risiko und
  nicht die Ergebnis-Version-Zuordnung.

**Pflichtänderung:** keine.

## POST 2 — **ABGELEHNT**

**Begründung:**

- Die deterministischen Anforderungen, deutsche Sprache, enger ICP,
  Kampagnenthema, CTA, UTM-Link, Pflicht-Hashtags, Fakten- und Produktgrenzen,
  Spam- und Markensicherheit sind bestanden. Die Stilprüfung liegt mit 0,90 bei
  **BESTANDEN**.
- Dennoch besteht eine **funktionale Dublette** zum aktuellen Queue-/Log-Bestand.
  Der neue Kern „Prüfinformationen, Einordnung und Entscheidung so
  dokumentieren, dass die nächste zuständige Person sie ohne mündliche
  Übersetzung versteht“ wiederholt in Kombination bereits belegte Funktionen:
  - `post-2026-09-11-0002` in `log.md`: Signatur, Zertifikatsinformationen und
    Entscheidungsgrundlage nachvollziehbar festhalten, damit eine Entscheidung
    später erklärt werden kann.
  - `post-2026-09-15-0002` in `schedule.md`: Die nächste/vertretende Person soll
    denselben Prüfschritt und dieselben relevanten Prüfinformationen ohne Zuruf
    nachvollziehen können.
  - `post-2026-09-16-0002` in `schedule.md`: Prüfinformation und fachliche
    Entscheidung getrennt sichtbar machen.
- Schatzkarten-Hook, Dreierliste und Formulierungen sind neu, ändern aber den
  bereits mehrfach vorhandenen operativen Nutzenkern nicht ausreichend. Nach
  der strikten Kampagnenvorgabe genügt eine neue Metapher nicht zur funktionalen
  Abgrenzung.

**Rückgabegrund an den Copywriter:** Erst eine tatsächlich geänderte Fassung mit
einem materiell neuen operativen Kern darf erneut geprüft werden; keine reine
Hook-, Metaphern- oder Synonymrevision.

## Schlussvermerk

Dies ist eine interne Reviewer-Freigabe bzw. -Ablehnung, keine Nutzerfreigabe.
Sie berechtigt weder zum Einreihen, Ankreuzen, Planen noch zum Veröffentlichen.
Texte, Queue, Checkboxen, `schedule.md`, `log.md`, Profil-, Lern- und
Approved-Dateien blieben unverändert. Ohne tatsächliche Textänderung erfolgt
keine weitere Reviewer-Runde.
