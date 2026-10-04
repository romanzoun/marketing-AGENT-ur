# RV-DV-NP-20260929-R24 — einmalige Reviewer-Schlussprüfung

Geprüft wurden genau einmal die zwei unveränderten finalen `text`-Blöcke aus
`team/copywriter/collected/docval-biv-two-2026-09-29-r24.md` gegen
`Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`.

Prüfgrundlagen waren ausserdem das persönliche Profil, das Stilprofil, die bindende
R24-Strategie, der bestandene Stilbericht
`team/style-evaluator/collected/SE-DV-NP-20260929-R24-review.md` sowie sämtliche
Posttexte in `approvals.md`, `schedule.md` und `log.md` der Kampagnenpfade
`Kampagnen/docval-biv-vor-archiv-vor-freigabe/` und
`Kampagnen/document validator/`.

## Textidentität und deterministische Gesamtprüfung

Die Quelldatei enthält exakt zwei `text`-Blöcke. Hashbasis sind die UTF-8-Bytes des
reinen Blockinhalts ohne Marker und ohne abschliessenden Zeilenumbruch. Beide Texte
sind NFC-normalisiert und stimmen unverändert mit dem bestandenen Stilbericht überein.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Identität bestätigt |
|---|---:|---:|---:|---|---|
| Post 1 | 1.146 | 1.157 | 21 | `114239efad93c06f4f0ea149c8a67725d4259a10c634b5a11d27b7b1896d7765` | ja |
| Post 2 | 1.232 | 1.250 | 22 | `3e9f89dbfd18b1ea6ccc36754901e9de0839a62aa397229935f3ff5d89c4085e` | ja |

- Zeichenlimit: **bestanden** — beide Texte liegen unter maximal 1.300
  Unicode-Codepoints.
- Pflicht-Hashtags: **bestanden** — `required_hashtags` ist leer; beide Texte
  enthalten keine Hashtags.
- CTA/UTM: **bestanden** — beide Beiträge sind klar produkt- und lösungsnah. Beide
  enthalten den vollständigen Conversion-Abschluss mit „Vor dem Archivieren prüfen
  statt hoffen“, der Demo-/Austausch-Einladung und genau einer Document-Validator-URL.
  Die UTM-Parameter sind jeweils exakt
  `utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice`.
- Exakte Dublette: **nein** — in den sechs Queue-Dateien liegen 37 Posteinträge mit
  36 unterschiedlichen exakten Textständen; die einzige interne Wiederholung ist
  der historische Schedule-Text `post-2026-09-17-0003`. Keiner der beiden R24-Texte
  stimmt mit einem Bestandsbeitrag überein.

## Post 1 — Signaturprüfung der Hauptdatei vs. Vorgangsvollständigkeit

**Urteil: FREIGEGEBEN**  
**Aufnahme in `approvals.md`: zulässig**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Sprache: Der deutsche Text adressiert mit Vertragsadministration,
  Records/ECM und Legal Ops den engen ICP in der konkreten Situation vor Freigabe
  oder Archivierung. Der Umzugskarton, die Packliste und die fehlenden Schrauben
  machen den Prozessunterschied greifbar.
- Stimme: Ich-Perspektive, gesprochener Rhythmus, trockene Pointe, klare Zweiteilung
  und offene Workflow-Frage entsprechen Kampagne und Stilprofil. Der Stil-Score
  0,87 ist dem unveränderten Hash eindeutig zugeordnet.
- Produkt- und Faktengrenzen: Der Document Validator wird nur mit Signatur- und
  Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs sowie dem belegten
  Datenfluss „PDF bleibt in der eigenen Umgebung, Hash wird lokal gebildet“
  beschrieben. Keine erfundene Biografie, Kundenreferenz, Statistik,
  regulatorische Pflicht oder Produktfunktion.
- Pflichtschwerpunkt Trennung: **bestanden** — Schritt 1 betrifft ausdrücklich die
  technische Prüfung der signierten Hauptdatei. Schritt 2 betrifft erwartete
  Beilagen, Anlagen und weitere Vorgangsunterlagen. Der Text ordnet die Beurteilung
  und Dokumentation der Geschäftsvorgangs-Vollständigkeit ausdrücklich dem eigenen
  Prozess zu. Er behauptet nicht, der Document Validator prüfe Beilagen, Inhalt,
  Vorgangszuordnung, Vollständigkeit oder Freigabereife.
- Rechts-/Sicherheits-/Brand-Safety: Keine Rechts-, Sicherheits-, Revisions- oder
  Vollständigkeitsgarantie, kein automatischer Freigabeentscheid, kein
  Angstmarketing, Competitor-Bashing oder Banned Topic. Der einmalige Produktblock
  mit CTA ist nicht spamartig.
- Funktionale Dublette: **nein** — der nächstliegende Bestandsbeitrag
  `post-2026-09-16-0002` trennt „technisch geprüft“ von „fachlich freigegeben“;
  `post-2026-09-22-0001` trennt technische Prüfinformationen von
  Records-Klassifikation und Archivierungsentscheid. R24 Post 1 hat einen anderen
  operativen Kern: Eine technisch geprüfte signierte Hauptdatei sagt nichts darüber
  aus, ob alle erwarteten Unterlagen des gesamten Geschäftsvorgangs vorliegen.

## Post 2 — Nicht verfügbare Information vs. negativer Berechtigungsnachweis

**Urteil: FREIGEGEBEN**  
**Aufnahme in `approvals.md`: zulässig**  
**Pflichtänderung: nein**

- Kampagnenfit/ICP/Sprache: Der deutsche Text adressiert Vertragsadministration und
  Compliance/Legal Ops mit einem konkreten Status- und Entscheidungsproblem im
  Freigabeworkflow. Die Schubladen-/Hammer-Metapher macht die abstrakte Semantik
  einer Datenlücke verständlich.
- Stimme: Ich-Perspektive, kurze Pointe, operative Dreiertrennung und offene
  Workflow-Frage passen zur persönlichen Stimme. Der Stil-Score 0,82 ist dem
  unveränderten Hash eindeutig zugeordnet.
- Produktrollen: Der Document Validator bleibt auf Signatur- und
  Zertifikatsinformationen begrenzt. Der Business Identity Validator **kann** nur
  Kontext zu Zeichner, Unternehmen und verfügbaren Berechtigungsinformationen
  ergänzen. Der Text schreibt BIV weder einen Freigabeentscheid noch die Ermittlung
  oder Garantie einer konkreten rechtlichen Zeichnungsberechtigung zu.
- Pflichtschwerpunkt Statussemantik/BIV-Grenze: **bestanden** — „Information nicht
  verfügbar“ wird weder als Berechtigungs-Ja noch als Nachweis fehlender
  Berechtigung ausgelegt. Die ausdrückliche Aussage, dass BIV keine konkrete oder
  rechtliche Zeichnungsberechtigung garantiert, zieht die Kampagnengrenze klar.
  Klärung und Entscheidung bleiben ausdrücklich beim organisationsinternen Prozess.
- Fakten/Recht/Brand-Safety: Keine erfundene Pflicht, Biografie, Kundengeschichte,
  Zahl oder Statistik; keine Rechts-, Sicherheits- oder Revisionsgarantie, kein
  Angstmarketing, Wettbewerberbezug oder Banned Topic. CTA und Produktnennung sind
  einmalig und nicht spamartig.
- Funktionale Dublette: **nein** — `post-2026-09-10-0002` trennt Name allgemein von
  geschäftlicher Zeichnungsberechtigung, `post-2026-09-26-0002` verknüpft verfügbaren
  Kontext mit Vertragswert und interner Kompetenzgrenze, und
  `post-2026-09-28-0002` behandelt die Auswahl des passenden Unternehmens- oder
  Rollenkontexts. R24 Post 2 behandelt eigenständig die engere Statussemantik, dass
  das Fehlen einer Berechtigungsinformation kein negativer Berechtigungsnachweis ist.

## Bindendes Reviewer-Ergebnis

| Text | Urteil | Aufnahme in `approvals.md` | Pflichtänderung |
|---|---|---|---|
| Post 1 | **FREIGEGEBEN** | zulässig | nein |
| Post 2 | **FREIGEGEBEN** | zulässig | nein |

Dies war die einzige reguläre Reviewer-Runde für diese unveränderten R24-Texte.
Ohne tatsächliche Textänderung ist keine weitere Reviewer-, Hash- oder Statusrunde
nötig. Die Urteile sind interne Reviewer-Freigaben, keine Nutzerfreigaben, und
berechtigen weder zur Planung noch zur Veröffentlichung. Es wurden keine Eingabetexte,
Queues, Checkboxen, Kampagnen-, Stil-, Lern- oder Approved-Dateien sowie keine
Schedule-/Log-Daten geändert und keine Veröffentlichungsaktion ausgeführt.
