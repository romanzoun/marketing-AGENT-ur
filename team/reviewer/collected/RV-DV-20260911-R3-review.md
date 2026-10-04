# Reviewer-Prüfung RV-DV-20260911-R3

- Datum: 2026-09-11
- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Quelle: `team/copywriter/collected/document-validator-two-2026-09-11-r3.md`
- Umfang: genau die zwei unveränderten Posttexte zwischen ihren START-/END-Markern
- Stilvorprüfung: POST 1 mit 0,91 und POST 2 mit 0,94 bestanden
- Faktenabgleich: [Swisscom Document Validator](https://trustservices.swisscom.com/de/products/validator/document-validator) und [Swisscom Business Identity Validator](https://trustservices.swisscom.com/de/products/validator/business-identity-validator), abgerufen am 2026-09-11

## Deterministische Prüfung

Gezählt wurden Unicode-Zeichen innerhalb des jeweiligen Posttexts einschließlich
aller internen Zeilenumbrüche, jedoch ohne die HTML-Marker und ohne den
Zeilenumbruch vor dem END-Marker.

| Post | Unicode-Zeichen | Limit | Vollständiger CTA | Exakter UTM-Link | Hashtags |
|---|---:|---:|---|---|---|
| POST 1 – Der feste Prüfschalter | 1.244 | 1.300 | genau 1× | genau 1× | ausschließlich `#Compliance #eIDAS #RecordsManagement`, je genau 1× |
| POST 2 – Wer klickt da? | 1.277 | 1.300 | genau 1× | genau 1× | ausschließlich `#Compliance #eIDAS #RecordsManagement`, je genau 1× |

Beide Posts bestehen Zeichenlimit, CTA-, Link- und Hashtagprüfung.
POST 1 enthält 14, POST 2 enthält 16 interne Zeilenumbrüche; diese sind in den
ausgewiesenen Unicode-Zeichenzahlen enthalten.

## Dublettenabgleich

Die Queue-Dateien `approvals.md`, `schedule.md` und `log.md` sowie die drei
Vergleichsdateien vom 10.09., 11.09. und 11.09.-R2 wurden vollständig geprüft.
POST 1 ist durch LKW/Werkstor, festen Workflow und API-Prüfschritt klar von
Garderobe/Datenweg, grünem Haken/Gepäckmarke und Audit/Detektiv abgegrenzt.
POST 2 ist durch Cursor, Agent-vs-Mensch und digitale Verantwortungsnachweise
klar von Namensschild/BIV, Audit/Detektiv und den übrigen vorhandenen Posts
abgegrenzt. Es liegt keine Text- oder Ideen-Dublette vor.

## POST 1 – Der feste Prüfschalter

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

Begründung:

- Der Text ist vollständig deutsch und adressiert mit Records-, Posteingang- und
  Vertragsadmin-Teams sowie dem Records-/ECM-Workflow den engen ICP.
- Die Ich-Formulierungen transportieren eine persönliche Haltung, ohne
  Produktnutzung, Kundenerfahrung oder biografische Tatsachen zu behaupten.
- LKW, Werkstor, Ausladen, Kontrollzettel und „Mensch am Steuer“ bilden einen
  tragenden bildhaften Vergleich mit angemessenem, trockenem Witz.
- Der Swisscom Document Validator wird korrekt als per API einbindbarer
  Prüfschritt für ZertES-/eIDAS-Signatur und Zertifikatsinformationen beschrieben.
  Die PDF bleibt in der eigenen Umgebung; der Hash wird lokal gebildet.
- Archivierung und Freigabe sind eindeutig Prozesspositionen, keine dem Produkt
  zugeschriebenen Funktionen. Der Text sagt ausdrücklich, dass die Technik weder
  rechtlich entscheidet noch das Dokument selbst freigibt.
- Keine Rechtsgarantie, kein Heilsversprechen, keine Konkurrenzabwertung und
  keine Politik oder Religion. Ein Produktlink und drei vorgeschriebene Hashtags
  sind nicht spamartig.

## POST 2 – Wer klickt da?

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

Begründung:

- Der Text ist vollständig deutsch und bindet die Agentenfrage eng an Freigabe,
  Archivierung sowie Records-/Compliance-Teams statt an pauschale
  Backoffice-Automatisierung.
- „Für mich“ formuliert eine persönliche Haltung, ohne eigene Nutzung,
  Kundengeschichte oder unbelegte Biografie zu behaupten.
- Browser-Cursor, Ausweis am Revers und angeklebter Schnurrbart bilden einen
  durchgängigen, tragenden und markensicheren Vergleich.
- Die Produktrollen sind sauber getrennt: Document Validator wertet die signierte
  PDF und Zertifikatsinformationen aus; Business Identity Validator ergänzt
  Zeichner, Unternehmen und Berechtigung.
- Der Text grenzt ausdrücklich ab, dass keines der Produkte erkennt, wer den
  Browser bedient, und keines die menschliche Freigabe ersetzt. Er behauptet
  weder Erkennung noch Steuerung von Browser-Agenten.
- Keine Rechtsgarantie, kein Heilsversprechen, keine Konkurrenzabwertung und
  keine Politik oder Religion. Ein Produktlink und drei vorgeschriebene Hashtags
  sind nicht spamartig.

## Prozessgrenze

Diese Reviewer-Freigaben sind keine Nutzerfreigaben. Sie berechtigen weder zur
Planung noch zur Veröffentlichung. Entwürfe und Queue wurden nicht verändert;
keine Checkbox wurde gesetzt und keine Operator-Aktion ausgelöst.

## Gesamturteil

POST 1: **FREIGEGEBEN**, 1.244 Unicode-Zeichen, keine Pflichtänderung.

POST 2: **FREIGEGEBEN**, 1.277 Unicode-Zeichen, keine Pflichtänderung.

Bei `posts_per_run: 1` darf später höchstens einer der beiden Posts pro
Lauf/Zyklus veröffentlicht werden. Diese operative Grenze ändert nichts an der
getrennten Reviewer-Bewertung und erteilt keine Nutzerfreigabe.
