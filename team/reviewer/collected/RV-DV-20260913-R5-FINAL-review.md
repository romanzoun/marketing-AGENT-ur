# Reviewer-Prüfung RV-DV-20260913-R5-FINAL

## Prüfrahmen

- Geprüft wurden ausschließlich die unveränderten Texte zwischen `POST 1 BEGIN/END` und `POST 2 BEGIN/END` in `team/copywriter/collected/document-validator-two-2026-09-13-r5-final.md`.
- Maßstab: aktive Kampagne `Kampagnen/document validator/kampagne.yaml`, persönliches Profil, Stilprofil, Reviewer-Rolle, Stilbericht `SE-DV-20260913-R5-FINAL-review.md` sowie sämtliche acht bestehenden Posttexte in `approvals.md`, `schedule.md` und `log.md`.
- Deterministische Zählweise: Unicode-Codepoints einschließlich interner Zeilenumbrüche, ohne Markerzeilen und ohne abschließenden Zeilenumbruch.
- `schedule.md` enthält keinen Post. Der Vergleichsbestand umfasst sechs offene Posts in `approvals.md` und zwei veröffentlichte Posts in `log.md`.

## POST 1 — FREIGEGEBEN

**Zeichenzahl:** 1.144 von maximal 1.300 Unicode-Zeichen.

**Deterministische Prüfung:**

- Deutsch: bestanden.
- Pflicht-Hashtags: `#Compliance`, `#eIDAS` und `#RecordsManagement` jeweils genau einmal vorhanden.
- CTA: der Kampagnen-CTA einschließlich vollständigem UTM-Link ist exakt und genau einmal vorhanden.
- Identität der geprüften Fassung: SHA-256 `097ee9bfbab1dce74ce735a17d16f088768fc87b0f523796475ec804ebf28b97`; stimmt mit dem Stilbericht überein.

**Begründung:**

- Zielgruppe und Themenfit sind klar: Records-/Posteingang- und Compliance-Prozess, eingehende signierte PDFs, Kontrollpunkt vor Freigabe oder Archivierung sowie nachvollziehbare Übergaben.
- Produktrolle und Datenfluss sind kampagnenkonform beschrieben: Der Document Validator prüft bei ZertES-/eIDAS-signierten PDFs Signatur und Zertifikatsinformationen belastbarer; die PDF bleibt in der eigenen Umgebung und ihr Hash wird lokal gebildet.
- Keine unbelegte Garantie: Der Text verspricht weder rechtliche Gültigkeit noch Sicherheit, Revisionssicherheit oder automatische Freigabe. Er stellt ausdrücklich klar, dass das Prüfergebnis nur unterstützt und der zuständige Mensch entscheidet.
- Stimme bestanden: Regionalzug, Stationsfolge und „stille Post“ sind persönlich, anschaulich und trocken-witzig; der Text bleibt fachlich und vermeidet Marketing-Sprech. Der Stilbericht bestätigt dies mit 0,94.
- Abgrenzung zum Bestand ist ausreichend klar: Der neue Kernwinkel ist der Vertrauensverlust des Prüfstatus an mehreren organisatorischen Übergaben. Er wiederholt weder Fremd-Cloud/Datenweg, Audit-Detektiv, LKW/API-Prüfschritt, Agent-vs.-Mensch, Paketsiegel/Berechtigung, Grünhaken/Nebel, Namensschild/BIV noch Gepäckmarke/Grünhaken als Leitidee. Die sprachliche Nähe zur bestehenden Audit-Rückfrage bleibt eine unterstützende Pointe, nicht derselbe Postwinkel.
- Keine banned topics, Konkurrentenabwertung, erfundene Biografie, Spam-Mechanik oder sonstiges Brand-Safety-Risiko erkennbar.

**Pflichtänderungen:** Keine.

## POST 2 — FREIGEGEBEN

**Zeichenzahl:** 1.203 von maximal 1.300 Unicode-Zeichen.

**Deterministische Prüfung:**

- Deutsch: bestanden.
- Pflicht-Hashtags: `#Compliance`, `#eIDAS` und `#RecordsManagement` jeweils genau einmal vorhanden.
- CTA: der Kampagnen-CTA einschließlich vollständigem UTM-Link ist exakt und genau einmal vorhanden.
- Identität der geprüften Fassung: SHA-256 `6c53ea9137ac2f56509ac486ba8da6e44327077e50001ea9f9e51adc2e73c030`; stimmt mit dem Stilbericht überein.

**Begründung:**

- Zielgruppe und Themenfit sind klar: IT/Security, Records und Legal Ops prüfen gemeinsam Datenweg, Auswertungsumfang und menschliche Entscheidung vor Freigabe oder Archivierung.
- Produktrollen sind sauber getrennt: Der Document Validator prüft ZertES-/eIDAS-signierte PDFs beziehungsweise Signatur- und Zertifikatsinformationen belastbarer; der Business Identity Validator kann Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen.
- Der lokale Datenfluss ist korrekt beschrieben: Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet.
- Keine unbelegte Garantie: „Die Stoppuhr misst den Datenweg, nicht juristische Sicherheit“ grenzt die Übung ausdrücklich von einer Rechts- oder Sicherheitszusage ab. Die Produkte liefern Prüfinformationen; Freigabe oder Ablehnung bleibt beim zuständigen Menschen. Auch eine Revisionsgarantie wird nicht behauptet.
- Stimme bestanden: „Folienschlacht“, Test-PDF, Stoppuhr und Klemmbrett erzeugen eine persönliche, bildhafte und leicht witzige Szene ohne erfundene Kundenerfahrung. Die vier Fragen sind konkret statt werblich. Der Stilbericht bestätigt dies mit 0,92.
- Abgrenzung zum Bestand ist ausreichend klar: Der neue Kernwinkel ist ein gemeinsamer, zeitlich begrenzter 15-Minuten-Praxistest vor einer Demo. Trotz Berührungspunkten zu Datenweg und Workflow ist er weder der Fremd-Cloud-/Mantel-Post noch der LKW-/API-Automationspost und wiederholt auch keinen der übrigen sechs Leitwinkel.
- Keine banned topics, Konkurrentenabwertung, erfundene Biografie, Spam-Mechanik oder sonstiges Brand-Safety-Risiko erkennbar.

**Pflichtänderungen:** Keine.

## Operative Grenze

Beide Texte dürfen ausschließlich als zwei getrennte, noch nicht nutzerfreigegebene Kandidaten behandelt werden. Wegen `limits.posts_per_run: 1` dürfen sie niemals im selben Veröffentlichungszyklus veröffentlicht werden. Diese Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zur Einplanung noch zur Veröffentlichung.

Durch diese Prüfung wurden Ausgangstexte, Queue-Dateien, Checkboxen, Freigaben und Termine nicht verändert. Es erfolgte keine `add`-, `schedule`-, `run-due`-, Operator-, Veröffentlichungs- oder LinkedIn-Aktion.
