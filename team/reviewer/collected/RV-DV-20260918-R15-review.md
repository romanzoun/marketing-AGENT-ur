# RV-DV-20260918-R15 — einmalige Reviewer-Prüfung

Geprüft wurden genau einmal ausschließlich die zwei unveränderten Markertexte
aus `team/copywriter/collected/document-validator-two-2026-09-18-r15.md`.
Der gebundene Stilnachweis liegt mit **0,91/0,88 BESTANDEN** vor. Maßgeblich
für das Reviewer-Urteil sind die vollständige Kampagne, der persönliche
Faktenrahmen und die aktuellen Posttexte in `approvals.md`, `schedule.md` und
`log.md`. Eine Reviewer-Freigabe ist keine Nutzerfreigabe und berechtigt nicht
zum Veröffentlichen.

## Textidentität und deterministische Prüfung

Die Hashes beziehen sich auf den exakten UTF-8-Text zwischen Start- und
Endmarker, ohne Marker und ohne den trennenden LF vor dem Endmarker.

| Prüfung | POST 1 | POST 2 |
|---|---:|---:|
| Unicode-Codepoints | **1.187** | **1.219** |
| Kampagnenlimit | 1.300 | 1.300 |
| UTF-8-Bytes | 1.207 | 1.239 |
| interne LF | 16 | 20 |
| SHA-256 | `a0c7d07c263625a9e827fc5399bb3f190e66bc2c5fca9f0e0084f3c37374b13d` | `0734ba7afc650f6caa283bf6f2c46fa60bb11b3fd423d9645723a0be9780551d` |
| Stilstatus | 0,91 BESTANDEN | 0,88 BESTANDEN |
| vollständiger exakter CTA inkl. UTM-Link | 1-mal, bestanden | 1-mal, bestanden |
| URLs | genau der zulässige CTA-Link | genau der zulässige CTA-Link |
| Pflicht-Hashtags | alle je 1-mal | alle je 1-mal |
| weitere Hashtags | keine | keine |
| exakte Dublette in Approval/Schedule/Log | keine | keine |

Beide Texte enthalten damit genau `#Compliance #eIDAS #RecordsManagement`,
liegen unter dem Zeichenlimit und enthalten jeweils exakt einen Link. Der
geprüfte Queue-Snapshot umfasst 1/14/6 Posttexte in Approval/Schedule/Log;
seine Datei-Hashes lauten `7e21db06…`, `9c07932b…` und `0a7ddab6…`.

## POST 1 — ABGELEHNT

### Bestandene Prüfpunkte

- **Sprache, ICP und Thema:** Deutsch; Records/Posteingang,
  Vertragsadministration und Compliance Ops werden für eingehende signierte
  PDFs vor Freigabe oder Archivierung konkret adressiert. Die Größenordnung ist
  als persönliche Orientierung und nicht als garantierter Business Case
  formuliert.
- **Stimme:** Klingelton, kurze Gegensätze und Ich-Perspektive ergeben einen
  persönlichen, verständlichen Rhythmus ohne Corporate- oder Spamton.
- **Fakten, Produktrolle und Datenfluss:** Der Document Validator wird korrekt
  der Prüfung von ZertES-/eIDAS-signierten PDFs sowie Signatur- und
  Zertifikatsinformationen zugeordnet. PDF in eigener Umgebung und lokal
  gebildeter Hash sind korrekt formuliert.
- **Entscheidungs-, Rechts- und Compliance-Grenzen:** Der Mensch beurteilt das
  Ergebnis und entscheidet. Es gibt keine Rechts-, Compliance-, Freigabe-,
  Revisions- oder Wirkgarantie und keine erfundene Biografie oder
  Kundengeschichte. Banned Topics, Konkurrentenabwertung und Brand-Safety-
  Risiken liegen nicht vor.

### Ablehnungsgrund

**Funktionale Dublette.** Der tragende Nutzenkern lautet erneut: Ab ungefähr
10 eingehenden signierten PDFs pro Monat soll aus einer gelegentlichen oder
personenabhängigen Prüfung ein definierter Kontrollpunkt vor Freigabe oder
Archivierung werden. Genau diese Schwelle und Funktion trägt bereits der
eingeplante `post-2026-09-15-0002` (Escape Room/Urlaubsvertretung): Bei 10+
signierten PDFs soll die spontane Einzelaktion durch einen wiederholbaren
Prüfbaustein vor Freigabe oder Archivierung ersetzt werden.

Der Klingelton und die fehlende tägliche Routine setzen ein neues Bild, ändern
aber weder Prozessnutzen noch Handlungsempfehlung. Auch die vorhandenen Posts
`post-2026-09-16-0001` und `post-2026-09-16-0002` im Schedule besetzen bereits
den festen Kontrollpunkt beziehungsweise die getrennte menschliche
Entscheidung. Damit ist POST 1 nicht funktional eigenständig.

### Pflichtänderung

Nicht erneut Volumen, fehlende Routine oder Personenabhängigkeit als Begründung
für denselben festen Kontrollpunkt verwenden. Der Text braucht einen
nachweislich queuefreien Funktionskern für den engen ICP; ein anderes
Alltagsbild oder eine andere Spanne allein genügt nicht. Nur ein tatsächlich
geänderter Finalstand dürfte erneut durch Stil- und Reviewer-Prüfung gehen.

## POST 2 — FREIGEGEBEN

- **Sprache, ICP und Thema:** Deutsch; Records/Posteingang,
  Vertragsadministration und Compliance Ops werden mit einer konkreten
  Vorabregel für eingehende signierte PDFs vor Freigabe oder Archivierung
  adressiert.
- **Stimme:** Horoskopvergleich, konkrete Uhrzeit, Ich-Haltung und knappe
  Dreierliste sind persönlich, bildhaft und gesprochen, ohne Werbe- oder
  Spamdramaturgie.
- **Fakten, Produktrolle und Datenfluss:** Der Document Validator wird korrekt
  auf ZertES-/eIDAS-signierte PDFs sowie Signatur- und
  Zertifikatsinformationen begrenzt. PDF in eigener Umgebung und lokal
  gebildeter Hash stimmen mit der Kampagne überein.
- **Menschliche Entscheidung und Grenzen:** Die Organisation legt vorab fest,
  welche Dokumente geprüft werden, wer das Ergebnis beurteilt und wo die
  Entscheidung festgehalten wird. Der Text grenzt ausdrücklich ab, dass das
  Produkt weder die interne Policy erfindet noch automatisch klassifiziert
  oder freigibt und dass Revisionssicherheit nicht automatisch entsteht. Keine
  Rechts-, Compliance-, Freigabe-, Revisions- oder Wirkgarantie.
- **Banned Topics und Brand-Safety:** Keine erfundene Biografie oder
  Kundengeschichte, keine Konkurrentenabwertung, keine Politik oder Religion
  und kein aggressiver CTA.
- **Dublettenprüfung:** Keine exakte Dublette. Funktional ist die
  **Auslöseregel vor Eingang des Einzelfalls** eigenständig: Bestehende Posts
  behandeln Datenweg, Prüfinformationen, technischen versus fachlichen Status,
  dokumentierte Entscheidung oder Robustheit eines bereits gesetzten
  Kontrollpunkts. POST 2 definiert dagegen erstmals, anhand welcher
  vorab festgelegten Kriterien ein Dokument überhaupt in den Prüfschritt
  gelangt. Das ist weder nur eine neue Metapher noch dieselbe Nutzenfunktion.

## Gesamtergebnis

| Text | SHA-256 | Länge | Reviewer-Urteil |
|---|---|---:|---|
| POST 1 | `a0c7d07c263625a9e827fc5399bb3f190e66bc2c5fca9f0e0084f3c37374b13d` | 1.187 Codepoints | **ABGELEHNT** |
| POST 2 | `0734ba7afc650f6caa283bf6f2c46fa60bb11b3fd423d9645723a0be9780551d` | 1.219 Codepoints | **FREIGEGEBEN** |

Dies ist die einzige reguläre Reviewer-Runde für diese unveränderten
Textstände. Es erfolgte keine Text-, Queue-, Checkbox-, Nutzerfreigabe-,
Planungs-, Profil-, Operator-, Browser-, LinkedIn- oder
Veröffentlichungsaktion. Die interne Reviewer-Freigabe von POST 2 ersetzt
keine Nutzerfreigabe.
