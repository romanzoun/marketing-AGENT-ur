# CS-DV-20260921-R17 — exakt zwei neue Post-Ideen

## Wiederaufnahme- und Queue-Prüfung

- Wiederaufnahme: nein. Der jüngste Zweierlauf R16 ist vollständig abgeschlossen
  und liegt bereits in `schedule.md`; seitdem existieren keine neueren Copywriter-,
  Stil- oder Reviewer-Artefakte für zwei Posts.
- Baseline: `approvals.md` enthält null Post-Einträge.
- Beide folgenden Winkel müssen funktional von allen Posts in `approvals.md`,
  `schedule.md` und `log.md` abgegrenzt bleiben.

## Idee 1 — Prüfergebnis und exakte Dokumentversion zusammenhalten

**Blickwinkel:** In Vertragsadministration und Records reicht es nicht, dass
irgendwo ein Prüfergebnis liegt. Das Team muss organisatorisch sicherstellen, dass
es zur exakt geprüften PDF-Version gehört. Ein nachträglich neu gespeichertes oder
ausgetauschtes Dokument darf nicht versehentlich mit dem Ergebnis seines Vorgängers
weitergereicht werden. Der lokale Hash macht die Prüfung datensparsam; der Post
formuliert keine erfundete Produktfunktion zur automatischen Versionierung oder
Archivverknüpfung.

**Hook/Bild:** Ein Garderobenzettel ohne Mantelnummer ist hübsches Konfetti. Im
Records-Prozess ist ein Prüfergebnis ohne eindeutig zugehörige Dokumentversion
ähnlich dekorativ.

**Fachlicher Kern:** Der Swisscom Document Validator prüft bei ZertES-/eIDAS-
signierten PDFs Signatur- und Zertifikatsinformationen; die PDF bleibt in der
eigenen Umgebung, ihr Hash wird lokal gebildet. Als organisatorische Empfehlung
formulieren: Prüfinformation und geprüfte Version im eigenen Records-/ECM-Prozess
eindeutig zusammenhalten. Keine Behauptung, das Produkt archiviere, versioniere
oder garantiere Revisionssicherheit. Menschliche Beurteilung und Freigabe bleiben
beim zuständigen Team.

**Schlussfrage:** Wie verhindert ihr, dass Prüfergebnis und PDF-Version im Prozess
getrennte Wege nehmen?

## Idee 2 — Der Prüfbericht muss auch für die Vertretung verständlich sein

**Blickwinkel:** Der neue Kern ist nicht Urlaubsvertretung oder ein geheimer
Prozess, sondern die Lesbarkeit der Prüfinformationen für die nächste zuständige
Person. Ein binäres «okay» hilft wenig, wenn später niemand mehr nachvollziehen
kann, welche Signatur- und Zertifikatsinformationen vorlagen und welche fachliche
Entscheidung darauf folgte. Teams sollten ihre interne Darstellung und
Dokumentation so gestalten, dass technische Prüfinformation und menschliche
Entscheidung getrennt, aber gemeinsam verständlich bleiben.

**Hook/Bild:** Ein Prüfbericht, den nur sein Verfasser versteht, ist wie eine
Schatzkarte mit der Legende «weiss ich noch». Sehr persönlich, wenig
übergabefähig.

**Fachlicher Kern:** Document Validator liefert Signatur- und
Zertifikatsinformationen zu ZertES-/eIDAS-signierten PDFs; nicht behaupten, er
erzeuge automatisch einen vollständigen Audit-Trail, erkläre rechtliche Wirkung
oder treffe die Entscheidung. Organisatorische Empfehlung: interne Darstellung
und Dokumentation trennt Prüfinformation, Einordnung und Freigabe. Der Unterschied
zum vorhandenen Zwei-Stempel-Post muss klar sein: Hier geht es um verständliche
Übergabe/Lesbarkeit der Evidenz, nicht um Statuslogik oder Urlaubsvertretung.

**Schlussfrage:** Versteht die nächste zuständige Person eure Prüfdokumentation
ohne mündliche Übersetzung?

## Verbindliche Leitplanken

- Exakt zwei deutsche Posts, je maximal 1.300 Unicode-Codepoints.
- Roman spricht persönlich, trocken-witzig, bildhaft und ohne Marketing-Sprech;
  keine erfundene Biografie, Kundenstory oder Nutzungserfahrung.
- Enger ICP: Records/Posteingang, Vertragsadministration, Compliance/Legal Ops;
  signierte PDFs vor Freigabe oder Archivierung.
- Vollständiger Kampagnen-CTA mit exakt diesem UTM-Link und mindestens den drei
  Pflicht-Hashtags `#Compliance #eIDAS #RecordsManagement`.
- Produktgrenzen strikt einhalten: keine automatische Freigabe, Rechtswirkung,
  Revisionssicherheit, Archivierung, Versionierung oder Audit-Trail-Funktion
  erfinden. BIV nur nennen, wenn Zeichner, Unternehmen oder Berechtigung für den
  konkreten Winkel nötig sind.
- Keine funktionale Wiederholung bestehender Winkel wie grüner Haken,
  Fremd-Cloud/Datenweg, Audit-Rückschau, LKW, stille Post, Ausnahmeweg,
  Urlaubsvertretung, technische-vs.-fachliche Statuslogik, Trigger-Regel,
  Browser-Agenten, sichtbarer Kringel oder Prozess-Testfälle.
- Folgeagenten verändern weder Queue noch Checkboxen, Schedule/Log, Stilprofil,
  Lernstand oder Approved-Korpus und veröffentlichen nichts.

## Ersatzidee 2 nach Reviewer-Ablehnung — Eingangskanal ist kein Signaturprüfer

Der erste POST 2 wurde als funktionale Dublette verworfen. Sein Textstand bleibt
unverändert abgelehnt und wird nicht erneut geprüft.

**Neuer materieller Funktionskern:** Ein vertrauter Absendername, eine bekannte
E-Mail-Domain oder ein gewohntes Upload-Portal beantwortet nicht die Frage, welche
Signatur- und Zertifikatsinformationen in der eingegangenen PDF vorliegen. Der
Records-/Vertragsprozess darf Vertrauen in den Eingangskanal nicht mit der
Prüfung des Dokuments gleichsetzen. Der Document Validator prüft die entsprechend
elektronisch signierte PDF; er authentisiert weder den E-Mail-Absender noch das
Portal. Keine Behauptung, der Kanal sei unsicher oder eine Signatur sei allein
rechtlich ausreichend.

**Hook/Bild:** Der Absendername im Posteingang ist wie die Klingelbeschriftung:
nett zu wissen, wer läutet; noch kein Prüfbericht für das Paket.

**Schlussfrage:** Trennt euer Eingang heute klar zwischen «kam über einen
vertrauten Kanal» und «die signierte PDF wurde geprüft»?

Alle übrigen Leitplanken gelten unverändert. Dieser Ersatz darf nicht auf
Audit-Rückschau, Urlaubsvertretung, Zwei-Status-Logik, sichtbare Unterschrift,
Dateinamen oder Version-Zuordnung zurückfallen.
