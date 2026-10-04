# CS-DV-20260917-R13 — exakt zwei neue Post-Ideen

Kampagne: `Kampagnen/document validator/kampagne.yaml`

## Wiederaufnahme- und Queue-Abgleich

- Aktuelle Baseline in `approvals.md`: **3** Post-Blöcke.
- Frühere stilbestandene Zweierpaare sind bereits in `schedule.md` vorhanden;
  insbesondere die Flughafen-/Browser-Agent-Texte sind dort enthalten und
  dürfen nicht erneut verwendet werden.
- Der einzelne Wallet-Text wurde am 2026-09-17 als eigener Vorlauf bereits in
  `approvals.md` aufgenommen und gehört nicht zu diesem Zweierauftrag.
- Es existiert daher kein queuefreies, fertiges Zweierpaar zur Wiederaufnahme.

## Idee 1 — Der beste Pfeil im Datenflussdiagramm fehlt

**Blickwinkel:** IT/Security und Records schauen auf denselben Prüfprozess aus
verschiedenen Richtungen. Der Post beginnt mit einem Architekturdiagramm: Viele
Pfeile wirken beeindruckend; bei einer sensiblen PDF ist der sympathischste
Pfeil aber der, der die vollständige Datei gerade nicht in eine Fremd-Cloud
trägt. Von dort eng zur belastbaren Kampagnenaussage: Beim Swisscom Document
Validator bleibt die PDF in der eigenen Umgebung, ihr Hash wird lokal gebildet;
geprüft werden ZertES-/eIDAS-Signatur und Zertifikatsinformationen. Abschluss
mit einer konkreten Frage an Teams: Welcher Pfeil verschwindet in ihrem heutigen
Prüfprozess, wenn die vollständige PDF lokal bleibt?

**Eigenständiger Nutzenkern:** gemeinsames Datenfluss-Gespräch zwischen dem
operativen Records-Team und dem Security-Blocker — nicht der schon verwendete
Garderoben-, Koffer-, Upload-/Download-, 15-Minuten-Test- oder Browser-
Kontextwechsel-Winkel.

**Ton:** Ich-Perspektive, trockenes Augenzwinkern über Architekturdiagramme,
kurze Sätze; kein Marketing-Sprech.

## Idee 2 — Freitag, 16:58 Uhr ist der beste Prozesstest

**Blickwinkel:** Eine eingehende signierte PDF kurz vor Feierabend zeigt, ob ein
Prüfschritt wirklich arbeitsfähig ist oder nur bei Sonnenschein funktioniert.
Nicht Geschwindigkeit versprechen, sondern den Prozess konkret machen: fester
Kontrollpunkt vor Freigabe/Archivierung, sichtbare Signatur- und
Zertifikatsinformationen, klar benannte menschliche Entscheidung. Der Swisscom
Document Validator liefert die technischen Prüfinformationen; der Mensch bleibt
für Beurteilung/Freigabe/Rechtsprüfung verantwortlich. Optional BIV nur dann
nennen, wenn der Text für den geschäftlichen Kontext zu Zeichner, Unternehmen
und Berechtigung wirklich Platz braucht. Abschlussfrage: Was muss um 16:58 Uhr
sichtbar sein, damit niemand aus Hoffnung auf „Archivieren“ klickt?

**Eigenständiger Nutzenkern:** Robustheit unter Zeitdruck und ein ruhiger,
klarer Feierabend-Prozess — nicht Urlaubsvertretung/Escape Room,
Ausnahmeweg/Flughafen-Piepen, Audit-Detektiv, Tiefkühldose oder doppelt
beschrifteter Statusknopf.

**Ton:** persönliche, leicht selbstironische Alltagsszene; bildhaft, knapp,
fachlich sauber, keine erfundene Kundengeschichte.

## Bindende Grenzen für beide Texte

- Deutsch; jeweils höchstens 1.300 Unicode-Codepoints.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance/Legal Ops
  bzw. IT/Security als konkreter Blocker dieses Prozesses.
- Vollständiger Kampagnen-CTA samt exaktem UTM-Link.
- Genau die drei Pflicht-Hashtags `#Compliance #eIDAS #RecordsManagement`, keine
  weiteren Hashtags.
- Keine Rechts-, Compliance-, Sicherheits-, Revisions- oder Wirkgarantie.
- Document Validator prüft ZertES-/eIDAS-signierte PDFs sowie Signatur- und
  Zertifikatsinformationen; PDF bleibt in eigener Umgebung, Hash wird lokal
  gebildet. Nicht behaupten, dass ausschliesslich der Hash das Unternehmen
  verlässt, wenn die Kampagnenquelle das nicht ausdrücklich sagt.
- BIV nur als ergänzender Kontext zu Zeichner, Unternehmen und Berechtigung;
  keine Gleichsetzung mit Signaturprüfung und keine Berechtigungs- oder
  Rechtsgarantie.
- Das Ergebnis ersetzt keine menschliche Beurteilung, Freigabe oder
  Rechtsprüfung.
- Keine biografischen Angaben ergänzen; `config/personal_profile.yaml` ist leer.
- Keine exakte oder funktionale Dublette zu Posts in `approvals.md`,
  `schedule.md`, `log.md`, zu abgelehnten R11-Texten oder zum Approved-Korpus.
- Copywriter schreibt exakt zwei klar markierte finale Texte und verändert keine
  Queue, keine Checkbox, keine Planung und keine Teamdateien ausser seinem
  eigenen Artefakt/Protokoll.
