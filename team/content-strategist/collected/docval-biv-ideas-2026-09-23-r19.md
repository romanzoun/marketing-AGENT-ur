# CS-DV-NP-20260923-R19 — exakt zwei neue Post-Ideen

Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`

## Wiederaufnahme- und Queue-Prüfung

- Der jüngste Postlauf `CS-DV-NP-20260922-R18` wurde vollständig abgeschlossen:
  beide Texte bestanden den Stilcheck und Reviewer und liegen bereits als
  `post-2026-09-22-0001` / `post-2026-09-22-0002` in dieser Queue.
- Nach diesem Abschluss existiert kein Paar neuer fertiger, stilbestandener
  Posttexte, das noch auf Reviewer oder Queue wartet. Daher **Neuentwicklung**,
  keine Fortsetzung.
- Ausgangsbestand dieser Queue: exakt zwei ungekreuzte Posts. Dieser Lauf soll
  exakt zwei weitere ungekreuzte Posts ergänzen. Es wird nichts freigegeben,
  geplant oder veröffentlicht.
- Der explizite Auftrag über zwei Freigabe-Entwürfe ist bindend. Das Kampagnenlimit
  `posts_per_run: 1` betrifft die spätere Ausführung; beide Entwürfe dürfen nie
  im selben Veröffentlichungszyklus publiziert werden.

## Idee 1 — Der Prüfpunkt hinter der Ausfahrt ist nur Dekoration

**Neuer Blickwinkel:** Nicht nur *ob*, sondern *wann* eine eingehende signierte
PDF geprüft wird, entscheidet über den Nutzen des Kontrollpunkts. Erfolgt die
Prüfung erst nachdem ein Records-/ECM-, Vertrags- oder Compliance-Prozess bereits
freigegeben, weiterverarbeitet oder archiviert hat, kommt die Information zu
spät. Der Post macht die Reihenfolge zum konkreten Governance-Thema: erst
Prüfinformationen sichtbar machen, dann lässt der zuständige Mensch den nächsten
Prozessschritt zu.

**Hook/Bild:** Eine Schranke fünf Meter hinter der Autobahnausfahrt ist technisch
vorhanden und praktisch sehr dekorativ. Beim Prüfpunkt für signierte PDFs ist die
Position ähnlich wichtig.

**Fachlicher Kern:** Der Swisscom Document Validator liefert bei ZertES-/eIDAS-
signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der
eigenen Umgebung; ihr Hash wird lokal gebildet. Das Produkt erteilt keine
Freigabe, archiviert nichts automatisch und ersetzt weder Rechtsprüfung noch
fachlichen Entscheid. Der Prozessverantwortliche definiert, dass die relevanten
Prüfinformationen *vor* Freigabe, Archivierung oder Weiterverarbeitung vorliegen.

**Abgrenzung:** Kein allgemeiner Zwei-Status-/Zwei-Stempel-Post, keine Trigger-
Regel für einzelne Dokumentarten, kein Happy-Path-/Ausnahmeweg, keine
Versionszuordnung. Der eigenständige Kern ist die Position des Kontrollpunkts
vor dem ersten nachgelagerten Entscheidungsschritt.

**Schlussfrage:** An welcher Stelle kann euer Prozess heute noch stoppen — bevor
oder erst nachdem das Dokument weitergewandert ist?

## Idee 2 — Drei Unterschriften passen nicht in eine einzige Ampel

**Neuer Blickwinkel:** Bei einer PDF mit mehreren Signaturen ist ein pauschales
„Dokument geprüft“ zu grob. Records-/Vertragsadmin- und Compliance-/Legal-Ops-
Teams müssen nachvollziehen können, welche Signatur- und Zertifikatsinformationen
zu welcher unterzeichnenden Person gehören und welche fachlichen Fragen danach
noch offen sind. Der Business Identity Validator darf ergänzend Kontext zu
Person, Unternehmen und verfügbaren Informationen zur Berechtigung liefern,
aber keine pauschale Zeichnungsberechtigung garantieren.

**Hook/Bild:** Wenn drei Personen an der Tür stehen, klebe ich nicht eine
Eintrittsmarke auf die Drehtür und erkläre damit alle drei für geprüft. Eine
einzige Ampel für mehrere Unterschriften ist ähnlich gesprächig.

**Fachlicher Kern:** Der Document Validator liefert bei ZertES-/eIDAS-signierten
PDFs Signatur- und Zertifikatsinformationen. BIV ergänzt ausschliesslich Kontext
zu Zeichner, Unternehmen und verfügbaren Berechtigungsinformationen. Keine
Behauptung, dass eine Ampel, DocVal oder BIV das Dokument automatisch freigibt,
jede Signatur pauschal gleich bewertet oder rechtliche Zeichnungsberechtigung
abschliessend garantiert. Zuständige Menschen beurteilen die einzelnen
Informationen und treffen den Freigabe-/Archivierungsentscheid.

**Abgrenzung:** Kein allgemeiner „Signatur, Identität und Berechtigung sind drei
Fragen“-Post und keine Wiederholung des einzelnen Paketsiegels/Namensschilds.
Der eigenständige operative Kern ist die Granularität bei *mehreren* Signaturen
in derselben PDF.

**Schlussfrage:** Sieht euer Prozess bei mehrfach signierten PDFs jede Signatur —
oder nur eine gemeinsame Ampelfarbe?

## Verbindliche Textgrenzen

- Exakt zwei deutsche LinkedIn-Posts, je höchstens 1.300 Unicode-Codepoints.
- Roman als Mensch: persönlich, locker, witzig, bildhafte Vergleiche, kurze
  gesprochene Sätze; kein Marketing-Sprech und keine erfundene Biografie,
  Kundengeschichte, Kennzahl oder regulatorische Pflicht.
- Enger ICP und konkrete Situation vor Freigabe/Archivierung; keine pauschalen
  Backoffice-Aussagen.
- Produktnah, daher vollständiger Kampagnen-CTA mit exakt dem UTM-Link und dem
  Demo-/Austausch-Satz. Keine Pflicht-Hashtags laut Kampagne; für Korpusnähe
  sparsam `#Compliance #eIDAS #RecordsManagement` verwenden.
- Produktgrenzen strikt: keine automatische Freigabe, Archivierung, Rechtsprüfung,
  Identitäts-/Berechtigungsgarantie, Revisionssicherheit, Audit-Trail- oder
  Workflowfunktion erfinden. Bei Idee 2 Mehrfachsignaturen als Prozesssituation
  behandeln; keine unbelegte Detailfunktion des Produkts behaupten.
- Vor Finalisierung gegen aktuelle Queue sowie vorhandene Copywriter-, Schedule-
  und Log-Texte der neuen und alten DocVal-Kampagne auf exakte und funktionale
  Dubletten prüfen. Falls einer der beiden Winkel funktional belegt ist, innerhalb
  derselben einen Copywriter-Runde auf einen nachweislich freien konkreten Winkel
  wechseln und dies im Bericht nennen.
- Copywriter ändert weder Queue noch Checkboxen, Schedule/Log, Lernstand,
  Stilprofil oder Approved-Korpus und startet keine Folgeagenten.

