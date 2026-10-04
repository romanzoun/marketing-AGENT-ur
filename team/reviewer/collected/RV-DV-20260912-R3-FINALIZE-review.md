# Reviewer-Prüfung RV-DV-20260912-R3-FINALIZE

- Datum: 2026-09-12
- Kampagne und fachliche Quelle der Wahrheit: `Kampagnen/document validator/kampagne.yaml`
- Textquelle: `team/copywriter/collected/document-validator-two-2026-09-12-r3-finalize.md`
- Umfang: exakt die zwei unveränderten Texte zwischen `POST-1-START`/`POST-1-END` und `POST-2-START`/`POST-2-END`
- Stilvorprüfung: POST 1 mit 0,90, POST 2 mit 0,95; beide BESTANDEN
- Queue-Abgleich: aktueller Stand von `Kampagnen/document validator/queue/approvals.md`

## Deterministische Prüfung

Gezählt wurden Unicode-Zeichen innerhalb des jeweiligen Markerblocks. Alle
internen Zeilenumbrüche sind enthalten; die HTML-Marker sowie der unmittelbar
vor dem END-Marker stehende Trenn-Zeilenumbruch sind nicht Bestandteil des
Posttexts.

| Post | Unicode-Zeichen | Interne Zeilenumbrüche | Limit | Pflicht-Hashtags | Vollständiger CTA | Exakter UTM-Link |
|---|---:|---:|---:|---|---|---|
| POST 1 – Der feste Prüfschalter | 1.244 | 14 | 1.300 | alle drei, je genau 1× | genau 1× | genau 1× |
| POST 2 – Wer klickt da? | 1.277 | 16 | 1.300 | alle drei, je genau 1× | genau 1× | genau 1× |

Die drei Pflicht-Hashtags sind in beiden Texten exakt als `#Compliance`,
`#eIDAS` und `#RecordsManagement` vorhanden. Der vollständige Kampagnen-CTA
lautet jeweils:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

Beide Texte bestehen Zeichenlimit, Hashtag-, CTA- und Linkprüfung.

## Abgrenzung zur aktuellen Approval-Queue

In `approvals.md` befinden sich aktuell zwei Post-Kandidaten:

- `post-2026-09-11-0001` (1.097 Zeichen): Fremd-Cloud/Datenweg mit
  Garderoben-Metapher.
- `post-2026-09-11-0002` (1.127 Zeichen): Audit-Nachvollziehbarkeit mit
  Detektiv-/Alibi-Metapher.

Keiner der beiden hier geprüften Texte stimmt exakt mit einem dieser
Queue-Posts überein. POST 1 setzt mit LKW/Werkstor, festem Prüfschalter und
API-Einbindung einen klaren Workflow-Automatisierungswinkel; die lokale
Hash-Bildung ist eine notwendige gemeinsame Kampagnenfaktik, nicht das
Leitmotiv. POST 2 setzt mit Browser-Cursor, Agent-vs.-Mensch und abgegrenzter
Verantwortung einen klaren digitalen Identitätswinkel. Auch die beiden neuen
Kandidaten sind untereinander weder Text- noch Ideen-Dubletten.

## POST 1 – Der feste Prüfschalter

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

Begründung:

- Der Post ist deutsch und adressiert mit Records-, Posteingang- und
  Vertragsadmin-Teams sowie Records-/ECM-Workflows den engen ICP.
- Der LKW-/Werkstor-Vergleich, „Mir ist lieber“ und „Mensch am Steuer“ geben dem
  Text eine persönliche, nahbare Stimme mit angemessenem Humor. Der bestandene
  Stilscore von 0,90 ist damit auch inhaltlich plausibel.
- Das Thema passt eng zur Kampagne: wiederholbare Prüfung signierter PDFs vor
  Freigabe oder Archivierung, API-Integration, ZertES-/eIDAS-Prüfung,
  Zertifikatsauswertung und lokaler Hash.
- Die Produktrolle bleibt sauber: Der Swisscom Document Validator wird als
  einbindbarer Prüfschritt beschrieben. Archivierung und Freigabe sind Stellen
  im umgebenden Prozess, nicht Funktionen des Produkts.
- Der Text sagt ausdrücklich, dass die Technik weder rechtlich entscheidet noch
  das Dokument selbst freigibt. Er behauptet auch nicht, das Produkt archiviere.
- Es gibt keine erfundene Biografie, eigene Produkt- oder Kundenerfahrung,
  juristische Garantie, kein Heilsversprechen, keine Konkurrenzabwertung, keine
  Politik oder Religion. CTA, Link und drei Pflicht-Hashtags sind nicht
  spamartig.

## POST 2 – Wer klickt da?

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

Begründung:

- Der Post ist deutsch und bindet AI-Agenten eng an Prüf-, Freigabe- und
  Archivierungsprozesse von Records-/Compliance-Teams; er weitet den ICP nicht
  pauschal auf „alle Backoffice“-Teams aus.
- Browser-Cursor, Ausweis am Revers und der angeklebte Schnurrbart ergeben eine
  persönliche, verständliche und markensichere Bildsprache. Der Stilscore von
  0,95 ist damit auch inhaltlich plausibel.
- Die Produktrollen sind korrekt getrennt: Der Document Validator wertet die
  signierte PDF und Zertifikatsinformationen aus; der Business Identity
  Validator ergänzt Kontext zu Zeichner, Unternehmen und Berechtigung.
- Der Text erklärt ausdrücklich, dass keines der Produkte erkennt, wer den
  Browser bedient, und keines die menschliche Freigabe ersetzt. Er behauptet
  weder Erkennung noch Steuerung eines Browser-Agenten. Die Frage, unter welchen
  Nachweisen ein Agent einen Prozessschritt auslösen darf, weist die Entscheidung
  dem Team bzw. Prozess zu, nicht DocVal oder BIV.
- Es gibt keine erfundene Biografie, eigene Produkt- oder Kundenerfahrung,
  juristische Garantie, kein Heilsversprechen, keine Konkurrenzabwertung, keine
  Politik oder Religion. CTA, Link und drei Pflicht-Hashtags sind nicht
  spamartig.

## Gesamt- und Queue-Entscheidung

- POST 1: **FREIGEGEBEN**, 1.244 Unicode-Zeichen, keine Pflichtänderung.
- POST 2: **FREIGEGEBEN**, 1.277 Unicode-Zeichen, keine Pflichtänderung.

**Ja: Beide Texte dürfen unverändert und jeweils einzeln per `li-jobs add` als
zwei getrennte, noch nicht nutzerfreigegebene Kandidaten in `approvals.md`
gelegt werden.** Diese Aussage erlaubt nur das spätere Einreihen; im Rahmen
dieser Prüfung wurde keine Queue-Aktion ausgeführt.

`posts_per_run: 1` begrenzt eine spätere operative Veröffentlichung auf maximal
einen Post pro Lauf/Zyklus. Es begrenzt nicht die Zahl getrennt geprüfter
Kandidaten in `approvals.md`. Die Reviewer-Freigaben sind keine
Nutzerfreigaben und berechtigen weder zur Planung noch zur Veröffentlichung.
Keine Checkbox, kein Termin und keine Queue-, Bild-, Operator-, LinkedIn- oder
Veröffentlichungsaktion wurde ausgelöst.
