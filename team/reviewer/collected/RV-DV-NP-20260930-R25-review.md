# RV-DV-NP-20260930-R25 — einmalige reguläre Reviewer-Schlussprüfung

Geprüft wurden genau einmal und ausschliesslich die zwei unveränderten finalen
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-30-r25.md`. Massgeblich waren
die aktive Kampagne
`Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`, das persönliche
Profil, das Stilprofil, die bindenden R25-Ideen, der bestandene Stilbericht
`team/style-evaluator/collected/SE-DV-NP-20260930-R25-review.md` sowie sämtliche
aktuellen Posttexte in `approvals.md`, `schedule.md` und `log.md` der aktiven
Kampagne. Es wurde kein Text geändert.

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch.

## Deterministische Vorprüfung

| Text | Unicode-Codepoints | Limit | Pflicht-Hashtags | SHA-256 | Textidentität |
|---|---:|---:|---|---|---|
| Post 1 | 981 | 1.300 | keine (`required_hashtags: []`) | `d1b88d59654de555f2cffe38fcd3eebf4b0f42f018cdd1e16d08ed425232397e` | bestätigt |
| Post 2 | 1.173 | 1.300 | keine (`required_hashtags: []`) | `d75b05db13c525563b8301fb36f55984fe48a9be77145fc25f4723858e6e1016` | bestätigt |

Die Quelldatei enthält exakt zwei `text`-Blöcke. Zeichenwerte und Hashes stimmen
bei beiden Texten exakt mit Copywriter-Artefakt, Stilbericht und Übergabe
überein. Beide enthalten weder Hashtag noch Link; das ist zulässig, weil keine
Pflicht-Hashtags bestehen und die Kampagne bei einem fachlichen Awareness-Post
keinen Produktlink oder Verkaufs-CTA verlangt.

## Post 1 — Technisch nicht geprüft ist nicht ungültig

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Stimme: Der Beitrag behandelt einen automatisierten
  Prüfprozess vor Freigabe oder Archivierung und adressiert Records/ECM sowie
  Compliance Operations ausdrücklich. Gepäckwaagenbild, Ich-Haltung, trockene
  Pointe und offene Prozessfrage passen zur persönlichen Stimme. Der CTA fragt
  präzise nach der Trennung von `technisch nicht geprüft` und `ungültig`.
- Fakten und Produktgrenzen: Der Text behauptet weder einen Ausfall noch eine
  Fehlerquote, einen Produktstatuscode oder einen aktuellen Fehlerzustand des
  Swisscom Document Validators. Der technische Unterbruch ist als allgemeiner
  Prüfschritt im eigenen Workflow formuliert. Der Document Validator bleibt
  korrekt auf die Lieferung von Signatur- und Zertifikatsinformationen begrenzt;
  Statussemantik und nächster Schritt werden ausdrücklich der eigenen
  Prozesslogik zugeordnet. `Nicht geprüft` wird sauber von einer fachlichen
  Aussage `Signatur ungültig` getrennt.
- Rechts-/Sicherheitsgrenzen und Brand-Safety: Keine Rechts-, Freigabe-,
  Revisions- oder Sicherheitsgarantie, keine erfundene Pflicht, Biografie,
  Kundengeschichte, Statistik oder Produkteigenschaft. Kein Angstmarketing,
  Wettbewerberbezug, Spam oder Banned Topic.
- Dubletten: Keine exakte Dublette unter den 15 aktuellen Posttexten in
  `approvals.md`, `schedule.md` und `log.md`. Auch keine funktionale Dublette:
  `post-2026-09-29-0002` trennt fehlende Berechtigungsinformation von negativer
  Berechtigungsentscheidung; `post-2026-09-28-0001` führt einen bereits
  vorhandenen Klärfall; `post-2026-09-24-0002` vergleicht die Semantik von
  Browser- und API-Ergebnissen. Dieser Text behandelt eigenständig das
  ausgebliebene technische Prüfergebnis gegenüber der Aussage `ungültig`.

## Post 2 — Ergebnisinformationen brauchen eine Zwecklogik

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Stimme: Der Beitrag trifft die Datenschutz-, Security- und
  Prozessperspektive des engen ICP. Schliessfach, Namensetikett und schwarzes
  Brett machen Datenminimierung und zweckgebundene Sichtbarkeit greifbar. Die
  offene Schlussfrage ist ein passender fachlicher Awareness-CTA ohne
  Verkaufsdruck.
- Fakten und Produktgrenzen: Der kampagnenbelegte Datenfluss ist korrekt
  wiedergegeben: Die PDF bleibt in der eigenen Umgebung; für die Validierung
  wird ihr Hash verwendet. Der Document Validator liefert Signatur- und
  Zertifikatsinformationen. BIV **kann** Kontext zu Zeichner, Unternehmen und
  verfügbaren Berechtigungsinformationen ergänzen. Der Text behauptet keine
  konkrete Speicherung oder Aufbewahrungsdauer, keine Produkt-Zugriffsrolle
  und keine technische Zugriffskontrollfunktion. Die Rollen-/Sichtbarkeitsfrage
  ist ausdrücklich eine Empfehlung für den nachgelagerten eigenen Prüfprozess.
  BIV wird weder eine konkrete noch eine rechtliche Zeichnungsberechtigung oder
  sonstige Garantie zugeschrieben.
- Rechts-/Sicherheitsgrenzen und Brand-Safety: Keine Rechtsberatung,
  regulatorische Pflicht, automatische Freigabe, Revisions- oder
  Sicherheitsgarantie und keine erfundene Produktfunktion, Biografie,
  Kundengeschichte oder Statistik. Kein Angstmarketing, Wettbewerberbezug,
  Spam oder Banned Topic.
- Dubletten: Keine exakte Dublette unter den 15 aktuellen Posttexten. Auch keine
  funktionale Dublette: `post-2026-09-28-0002` ordnet verfügbaren Unternehmens-
  und Rollenkontext einem Vorgang zu; `post-2026-09-26-0002` verbindet Kontext
  mit internen Kompetenzregeln; `post-2026-09-23-0001` trennt technische Prüfung
  von den Entscheidungen verschiedener Rollen. Dieser Text fokussiert dagegen
  eigenständig die zweckgebundene Sichtbarkeit und Datenminimierung für mehrere
  Arten nachgelagerter Ergebnisinformationen.

## Gesamtergebnis

| Text | Style-Status | Reviewer-Urteil | Pflichtänderung | Exakte Dublette | Funktionale Dublette |
|---|---:|---|---|---|---|
| Post 1 | 0,91 BESTANDEN | **FREIGEGEBEN** | nein | nein | nein |
| Post 2 | 0,89 BESTANDEN | **FREIGEGEBEN** | nein | nein | nein |

Dies ist genau eine interne Reviewer-Prüfung des unveränderten R25-Textstands.
Die Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zur
Queue-Aufnahme oder -Verschiebung noch zu Planung, Bildaktion oder
Veröffentlichung. Es wurde keine Queue-, Freigabe-, Planungs-, Bild-, Profil-,
Lern-, Approved-, Operator-, Browser- oder Veröffentlichungsaktion ausgeführt.
Ohne tatsächliche Textänderung ist keine weitere Reviewer-, Hash- oder
Statusrunde erforderlich.
