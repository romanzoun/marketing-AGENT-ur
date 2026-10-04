# CS-DV-NP-20260926-R22 — exakt zwei neue Post-Ideen

Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`

## Wiederaufnahme- und Queue-Prüfung

- Der jüngste Zweierlauf R21 ist vollständig abgeschlossen: Beide Texte wurden
  stilgeprüft, reviewer-freigegeben und liegen bereits als
  `post-2026-09-25-0001` / `post-2026-09-25-0002` in der Queue.
- Nach R21 existiert kein Paar neuer fertiger, stilbestandener Posttexte, das
  noch auf Reviewer oder Queue wartet. Daher Neuentwicklung, keine Fortsetzung.
- Ausgangsbestand: sechs Post-Einträge in `approvals.md`. Ziel dieses Auftrags:
  exakt zwei weitere ungekreuzte Post-Einträge; nichts freigeben, planen oder
  veröffentlichen.
- Der ausdrückliche Nutzerauftrag über zwei Entwürfe ist bindend. Das
  Kampagnenlimit `posts_per_run: 1` gilt für die spätere Veröffentlichung, nicht
  für das Erstellen zweier getrennter Freigabekandidaten.

## Idee 1 — Drei Uhren, drei Aussagen

**Neuer Blickwinkel:** In einem Records-/ECM-Prozess dürfen Signaturzeitpunkt,
technischer Prüfzeitpunkt und fachlicher Entscheidungszeitpunkt nicht in einem
unscharfen Feld wie „geprüft am“ verschwinden. Der Post macht die drei Zeitpunkte
als getrennte Prozessinformationen sichtbar, ohne dem Produkt eine Zeitstempel-,
Archiv- oder Entscheidungsfunktion zuzuschreiben.

**Hook/Bild:** Drei Uhren an einer Bahnhofswand sind nur hilfreich, wenn darunter
steht, welche davon Zürich, London und New York meint. Ein einziges „geprüft am“
für drei verschiedene Ereignisse ist ähnlich auskunftsfreudig.

**Fachlicher Kern:** Der Swisscom Document Validator prüft bei ZertES-/eIDAS-
signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der
eigenen Umgebung, ihr Hash wird lokal gebildet. Der eigene Prozess hält getrennt
fest, wann die Signatur angebracht, wann technisch geprüft und wann fachlich
entschieden wurde, soweit die jeweiligen Informationen verfügbar sind. Keine
Behauptung, der Validator liefere, qualifiziere oder garantiere alle drei Zeiten;
keine automatische Freigabe, Archivierung, Rechtsprüfung oder
Revisionssicherheit.

**Abgrenzung:** Nicht der bestehende Post zur Version eines internen Regelsets am
Entscheidungszeitpunkt. Hier geht es um die semantische Trennung dreier
Zeitangaben, nicht um Regelversionen, Dokumentversionen, Trigger oder
Audit-Rückschau allgemein.

**Schlussfrage:** Seht ihr später drei klare Zeitpunkte — oder nur ein Datum, das
alles und damit wenig sagt?

## Idee 2 — Ein Namensschild kennt keinen Betrag

**Neuer Blickwinkel:** Eine technisch valide Signatur und ein bekannter Name
beantworten noch nicht, ob der geschäftliche Kontext für genau diesen Vorgang
passt. Bei Verträgen kann derselbe Zeichner je nach Unternehmen, interner
Kompetenzgrenze oder Vorgang unterschiedlich eingeordnet werden. Der Post trennt
deshalb technische Validität, verfügbaren BIV-Kontext und die organisationsseitige
Entscheidung zu Betrag/Vorgang.

**Hook/Bild:** Ein Namensschild kennt keinen Betrag. Es sagt, wer vor mir steht —
nicht, ob diese Person über 5'000 oder 5 Millionen entscheiden darf.

**Fachlicher Kern:** Der Document Validator prüft Signatur- und
Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs. Der Business Identity
Validator kann ergänzend Kontext zu Zeichner, Unternehmen und verfügbaren
Informationen zur Berechtigung liefern. Nicht behaupten, BIV kenne interne
Kompetenzgrenzen, prüfe automatisch einen konkreten Vertragswert oder garantiere
eine rechtliche Zeichnungsberechtigung. Das zuständige Team gleicht den
verfügbaren Kontext mit seinen eigenen Regeln und dem konkreten Vorgang ab.

**Abgrenzung:** Kein allgemeiner „Signatur, Identität, Berechtigung sind drei
Fragen“-Post, kein Mehrfachsignatur-Post und kein blosses Namensschild-/Firmen-
Matching. Der eigenständige operative Kern ist, dass eine Berechtigungsfrage an
den konkreten Wert bzw. Vorgang gebunden sein kann und deshalb nicht aus einem
Namen oder grünen Status allein folgt.

**Schlussfrage:** Verknüpft euer Freigabeprozess den verfügbaren Kontext mit dem
konkreten Vorgang — oder bleibt es beim Namensschild?

## Verbindliche Textgrenzen

- Exakt zwei deutsche LinkedIn-Posts, je höchstens 1.300 Unicode-Codepoints.
- Romans Stimme: Ich-Perspektive, kurz und gesprochen, trockener Witz,
  bildhafte Vergleiche; kein Marketing-Sprech, keine erfundene Biografie,
  Kundengeschichte, Kennzahl oder regulatorische Pflicht.
- Enger ICP und klare Situation: eingehende signierte PDFs vor Freigabe oder
  Archivierung in Records/ECM, Vertragsadministration oder Compliance/Legal Ops.
- Produktnah; daher vollständiger Kampagnen-CTA mit exakt dem UTM-Link und
  Demo-/Austauschoption. `required_hashtags` ist leer; Hashtags sparsam.
- Produktgrenzen strikt. Besonders Idee 1 darf keine belegungslose Aussage zu
  qualifizierten Zeitstempeln oder konkreten vom Validator ausgegebenen
  Zeitfeldern enthalten. Idee 2 darf weder interne Kompetenzgrenzen als BIV-
  Funktion noch rechtliche Zeichnungsberechtigung als Garantie darstellen.
- Gegen sämtliche Posttexte in `approvals.md`, `schedule.md` und `log.md` beider
  DocVal-Kampagnenpfade auf exakte und funktionale Dubletten prüfen. Falls ein
  Winkel bereits funktional belegt ist, innerhalb derselben regulären
  Copywriter-Runde auf einen belegbar freien konkreten Winkel wechseln und die
  Abgrenzung dokumentieren.
- Copywriter ändert keine Queue, Checkbox, Planung, Lern-/Stildatei oder
  Approved-Datei, startet keine Folgeagenten und veröffentlicht nichts.
