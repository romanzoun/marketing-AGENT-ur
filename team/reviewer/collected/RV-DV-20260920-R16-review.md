# RV-DV-20260920-R16 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschliesslich die zwei unveränderten Markertexte
aus `team/copywriter/collected/document-validator-two-2026-09-20-r16.md`.
Grundlage waren die aktive Kampagne, persönliches Profil, Rollen- und
Teamkontext, die R16-Ideen, das bestandene Stilurteil sowie alle aktuell in
`approvals.md`, `schedule.md` und `log.md` enthaltenen Posttexte. Es erfolgte
keine Text-, Queue-, Checkbox-, Schedule-, Bild-, Operator- oder
Veröffentlichungsaktion.

## Textidentität und deterministische Pflichtprüfung

Die Hashes beziehen sich jeweils auf den exakten UTF-8-Text zwischen Start- und
Endmarker, ohne Marker und ohne den trennenden LF vor dem Endmarker.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | NFC | Limit | CTA / Link | Pflicht-Hashtags |
|---|---:|---:|---:|---|---|---|---|---|
| POST 1 | 1.219 | 1.240 | 16 | `0623b974ff7582d0e5ea24a5637e108a449442dae331d3d264f65731c8e2d9d2` | ja | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA exakt einmal; einziger Link ist der korrekte UTM-Link | `#Compliance`, `#eIDAS`, `#RecordsManagement` je exakt einmal; keine weiteren Hashtags |
| POST 2 | 1.187 | 1.201 | 20 | `dea44c4b3050e3c592212777888e32ab4e2c23a3b551950132c9c0d9d7c8a7da` | ja | bestanden (≤ 1.300) | vollständiger Kampagnen-CTA exakt einmal; einziger Link ist der korrekte UTM-Link | `#Compliance`, `#eIDAS`, `#RecordsManagement` je exakt einmal; keine weiteren Hashtags |

Beide Identitäten stimmen exakt mit Auftrag und Stilurteil überein.

## Aktueller Dublettenstand

- Vollständig geprüft: 23 aktuelle Posttexte — 3 in `approvals.md`, 14 in
  `schedule.md`, 6 in `log.md`.
- Exakte Dubletten: keine für POST 1 oder POST 2.
- POST 1 ist trotz benachbarter Bestandsmotive eigenständig. Der vorhandene
  Dateinamen-/Label-Post fragt, warum eine amtlich klingende Bezeichnung kein
  Prüfnachweis ist; der vorhandene Haken-Post fragt nach Details hinter einem
  angezeigten Prüfergebnis. R16 fragt früher und anders: ob hinter einem bloss
  sichtbaren Namenszug überhaupt eine technisch prüfbare elektronische Signatur
  mit auswertbaren Signatur- und Zertifikatsinformationen liegt. Das ist ein
  eigener Eingangsunterscheidungs- und kein allgemeiner Kontrollpunkt.
- POST 2 ist trotz benachbartem Demo-/Stoppuhr- und Ausnahmeweg-Bestand
  eigenständig. Der bestehende 15-Minuten-Demotest verfolgt einen einzelnen
  Datenweg und fragt nach Ort, Abfluss, Auswertung und Entscheidung. R16
  empfiehlt dagegen einen vom Team zusammengestellten Sollfallsatz samt
  erwartetem Ergebnis und Negativfall, um Integration, Weiterleitung und
  menschliche Entscheidung als End-to-End-Prozess abzunehmen. Das wiederholt
  weder Urlaubsvertretung/Volumen noch Ausnahmebehandlung als Funktionskern.

## POST 1 — Kringel / sichtbarer Eindruck

**Urteil: FREIGEGEBEN**

Begründung:

- Kampagnenthema und enger ICP sind klar: Records/Posteingang und
  Vertragsadministration unterscheiden vor Freigabe oder Archivierung zwischen
  optischem Unterschriftseindruck und technisch prüfbarer elektronischer
  Signatur.
- Die Aussage bleibt fachlich begrenzt. Der Text behauptet weder, dass ein
  sichtbarer oder eingescannter Namenszug generell unwirksam sei, noch dass nur
  eine ZertES-/eIDAS-Signatur rechtliche Wirkung habe. Er sagt präzise, dass aus
  dem sichtbaren Bild allein keine ZertES-/eIDAS-Prüfbarkeit ableitbar ist.
- Die Produktrolle ist korrekt: Der Document Validator prüft bei entsprechend
  elektronisch signierten PDFs Signatur- und Zertifikatsinformationen; PDF in
  eigener Umgebung und lokale Hashbildung sind kampagnengedeckt. Fachliche
  Beurteilung und Freigabe bleiben ausdrücklich beim zuständigen Team.
- Persönliche Ich-Spur, trockener Einkaufszettel-Humor, konkrete Schlussfrage
  und enger Produktbezug entsprechen Stimme und bestandenem Stilurteil. Keine
  erfundene Biografie, Kundengeschichte, Rechtsgarantie, Herabsetzung,
  Spam-Mechanik oder sonstiges Brand-Safety-Risiko.

Pflichtänderung: keine.

## POST 2 — organisatorischer End-to-End-Abnahmetest

**Urteil: FREIGEGEBEN**

Begründung:

- Kampagnenthema und enger ICP sind klar: Vor dem produktiven Records-/ECM-
  Einsatz wird der gesamte Prüfprozess mit bekannten Sollfällen, erwartetem
  Ergebnis, Negativfall, Weiterleitung und menschlicher Entscheidung getestet.
- Der Testsatz ist eindeutig eine organisatorische Empfehlung an das Team. Der
  Text erfindet keine Validator-Funktion für Testdaten, automatische
  Klassifikation, fest definierte Ergebnisstatus, Workflow-Stopp oder
  automatische Freigabe. Besonders sauber ist die Formulierung „der eigene
  Workflow“ und „wie vorgesehen“.
- Die Produktrolle bleibt korrekt und begrenzt: Prüfung von ZertES-/eIDAS-
  signierten PDFs sowie Signatur- und Zertifikatsinformationen, Einbindung in
  Records-/ECM-Abläufe, PDF in eigener Umgebung und lokale Hashbildung. Wer
  beurteilt und freigibt, bleibt ausdrücklich menschlich/organisatorisch
  geklärt.
- Der Rauchmelder-Hook, die Ich-Haltung, die drei praktischen Prüffragen und die
  Schlussfrage entsprechen Stimme und bestandenem Stilurteil. Keine Garantie,
  kein erfundener Produktstatus, keine Kundengeschichte, kein Konkurrenzangriff,
  keine Spam- oder Brand-Safety-Auffälligkeit.

Pflichtänderung: keine.

## Gesamtergebnis

| Text | Urteil | Blocker |
|---|---|---|
| POST 1 | **FREIGEGEBEN** | keine |
| POST 2 | **FREIGEGEBEN** | keine |

Die Reviewer-Freigaben sind ausschliesslich interne Kampagnenurteile. Sie sind
keine Nutzerfreigabe und berechtigen weder zur Planung noch zur Veröffentlichung.
