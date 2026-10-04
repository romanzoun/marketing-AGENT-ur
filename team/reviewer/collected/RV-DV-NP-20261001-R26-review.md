# RV-DV-NP-20261001-R26 — einmalige reguläre Reviewer-Schlussprüfung

Geprüft wurden genau einmal und ausschliesslich die zwei unveränderten finalen
`text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-10-01-r26.md`. Massgeblich waren
die aktive Kampagne
`Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`, das persönliche
Profil, das Stilprofil, die verbindlichen R26-Ideen, der bestandene Stilbericht
`team/style-evaluator/collected/SE-DV-NP-20261001-R26-review.md` sowie sämtliche
aktuellen Posttexte in `approvals.md`, `schedule.md` und `log.md` der aktiven
Kampagne. Die ausdrückliche Auftragszahl von zwei Texten gilt für diese Prüfung
trotz `posts_per_run: 1`. Es wurde kein Text geändert.

Hashbasis: UTF-8-Bytes des reinen Inhalts im jeweiligen `text`-Block, ohne
Marker und ohne abschliessenden Zeilenumbruch.

## Deterministische Vorprüfung

| Text | Unicode-Codepoints | UTF-8-Bytes | Limit | Pflicht-Hashtags | SHA-256 | Textidentität |
|---|---:|---:|---:|---|---|---|
| Post 1 | 999 | 1.015 | 1.300 | keine (`required_hashtags: []`) | `db19d8f91fa8a48eb0e52747ce1a66a62e308e63616462d6806e0cb4932a0f2f` | bestätigt |
| Post 2 | 1.103 | 1.120 | 1.300 | keine (`required_hashtags: []`) | `dbcd5c96df8dd7f97986243cdb97daf526719990385fe7805954a41b45e9fc9f` | bestätigt |

Die Quelldatei enthält exakt zwei `text`-Blöcke. Beide haben je 12 interne
Zeilenumbrüche und liegen in NFC vor. Zeichenwerte und Hashes stimmen exakt mit
dem Copywriter-Artefakt und dem Stilbericht überein; damit ist die unveränderte
Textidentität bestätigt. Beide Texte enthalten weder Hashtag noch Link. Das ist
zulässig: Die Kampagne verlangt keine Hashtags, und die verbindliche Strategie
sieht für diese fachlichen Awareness-Posts jeweils eine offene Prozessfrage statt
Produktlink oder Verkaufs-CTA vor.

Der aktuelle Dublettenbestand umfasst 16 Posts: 14 in `approvals.md`, einen in
`schedule.md` und einen in `log.md`. Keiner der beiden R26-Hashes ist dort
vorhanden.

## Post 1 — Das Prüfergebnis muss den Systemwechsel überleben

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Stimme/CTA: Der Beitrag trifft Records Management,
  ECM/DMS-Verantwortliche, Compliance Operations und Prozessverantwortliche
  direkt. Er behandelt die nachvollziehbare Verbindung von Signatur- und
  Zertifikatsinformationen mit der geprüften PDF über einen DMS-, Workflow- oder
  Oberflächenwechsel hinweg. Kassenbon, Tapete und Umbau bilden einen
  verständlichen, leicht humorvollen Rahmen; Ich-Haltung und offene Schlussfrage
  entsprechen Romans persönlicher Stimme. Die Frage nach der Verständlichkeit
  ohne Altsystem ist ein präziser Awareness-CTA.
- Fakten und Produktrollen: Dem Swisscom Document Validator wird ausschliesslich
  die Lieferung von Signatur- und Zertifikatsinformationen zugeschrieben.
  Verständliche Verknüpfung, Aufbewahrung und Migration ordnet der Text
  ausdrücklich dem eigenen Records-/ECM-Prozess zu. Er behauptet kein
  Exportformat, keine Speicher- oder Migrationsfunktion des Produkts, keine
  garantierte Langzeitprüfbarkeit und keine vollständige Revisionssicherheit.
- Rechts-/Sicherheitsgrenzen, Spam und Brand-Safety: Keine Rechts-, Freigabe-,
  Revisions- oder Sicherheitsgarantie, keine erfundene Pflicht, Biografie,
  Kundengeschichte, Statistik oder Produkteigenschaft. Kein Angstmarketing,
  Wettbewerberbezug, Spam oder Banned Topic.
- Dubletten: Keine exakte und keine funktionale Dublette. Die grösste Nähe haben
  `post-2026-09-25-0001` mit Regelset, Regelversion und Entscheidungszeitpunkt
  sowie `post-2026-09-22-0001` in `log.md` mit der Trennung von
  Prüfinformationen und Records-Entscheidung. Dieser Post behandelt dagegen
  eigenständig, ob die Bedeutungs- und Zuordnungsbeziehung zwischen
  Prüfinformationen und genau der geprüften PDF einen Systemwechsel überlebt.
  Auch Dokumentfassung, Batch-Korrelation und zentraler Klärdatensatz im übrigen
  Bestand decken diesen Funktionskern nicht ab.

## Post 2 — Der verwendete Identitätskontext braucht einen Zeitpunkt

**Urteil: FREIGEGEBEN**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Stimme/CTA: Der Beitrag adressiert Vertragsadministration,
  Compliance/Legal Ops, Records/ECM und Prozessverantwortliche. Restaurantrechnung
  und heutige Speisekarte machen den Unterschied zwischen aktuellem Abruf und
  damaliger Entscheidungsgrundlage greifbar; Ich-Perspektive, kurze Pointe und
  offene Schlussfrage passen zur persönlichen Stimme. Die Frage nach dem damals
  verwendeten Kontext ist ein klarer fachlicher Awareness-CTA.
- Fakten und Produktrollen: Der Document Validator bleibt korrekt auf Signatur-
  und Zertifikatsinformationen begrenzt. BIV **kann** Kontext zu Zeichner,
  Unternehmen und verfügbaren Berechtigungsinformationen ergänzen. Der Text
  behauptet weder historische BIV-Daten noch unveränderliche Snapshots,
  Speicher-, Aufbewahrungs- oder Zeitstempelfunktionen. Er sagt ausdrücklich
  nicht, dass sich der Kontext verändert habe, und schreibt die Sichtbarkeit der
  tatsächlich herangezogenen Informationen dem eigenen Prozess zu. Keine
  konkrete oder juristisch garantierte Zeichnungsberechtigung wird behauptet.
- Rechts-/Sicherheitsgrenzen, Spam und Brand-Safety: Keine Rechtsberatung,
  regulatorische Pflicht, automatische Freigabe, Revisions- oder
  Sicherheitsgarantie und keine erfundene Produktfunktion, Biografie,
  Kundengeschichte oder Statistik. Kein Angstmarketing, Wettbewerberbezug,
  Spam oder Banned Topic.
- Dubletten: Keine exakte und keine funktionale Dublette. Die grösste Nähe haben
  `post-2026-09-25-0001` mit der geltenden Regelversion,
  `post-2026-09-26-0001` mit drei unterschiedlichen Ereigniszeitpunkten und
  `post-2026-09-28-0002` mit der Zuordnung eines Unternehmens- und
  Rollenkontexts zu einem Prozessschritt. Dieser Post fokussiert eigenständig,
  welcher damals tatsächlich verwendete verfügbare Identitäts- und
  Berechtigungskontext die frühere Entscheidung getragen hat und warum ein
  heutiger Abruf ihn nicht stillschweigend ersetzt.

## Gesamtergebnis

| Text | Style-Status | Reviewer-Urteil | Pflichtänderung | Exakte Dublette | Funktionale Dublette |
|---|---:|---|---|---|---|
| Post 1 | 0,90 BESTANDEN | **FREIGEGEBEN** | nein | nein | nein |
| Post 2 | 0,87 BESTANDEN | **FREIGEGEBEN** | nein | nein | nein |

Dies ist genau eine interne Reviewer-Prüfung des unveränderten R26-Textstands.
Die Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zur
Queue-Aufnahme oder -Verschiebung noch zu Planung, Bildaktion oder
Veröffentlichung. Es wurde keine Queue-, Freigabe-, Planungs-, Bild-, Profil-,
Lern-, Approved-, Operator-, Browser- oder Veröffentlichungsaktion ausgeführt.
Ohne tatsächliche Textänderung ist keine weitere Reviewer-, Hash- oder
Statusrunde erforderlich.
