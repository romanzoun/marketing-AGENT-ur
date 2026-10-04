# Reviewer-Schlussprüfung RV-DV-20260915-R8

## Prüfgrundlage und Bindung

- Geprüft wurden ausschließlich die zwei unveränderten reinen Markertexte aus
  `team/copywriter/collected/document-validator-two-2026-09-15-r8.md` gegen
  `Kampagnen/document validator/kampagne.yaml`, `config/personal_profile.yaml`,
  die zugehörigen R8-Ideen und die Stilprüfung `SE-DV-20260915-R8`.
- Jedes Marker-Paar `=== POST n START ===` / `=== POST n END ===` kommt genau
  einmal vor. Codepoints und SHA-256 beziehen sich auf den reinen Text zwischen
  den Markern, ohne abschließenden Zeilenumbruch.
- Die Stilprüfung bindet dieselben Texte und bewertet POST 1 mit **0,91** sowie
  POST 2 mit **0,94** jeweils als **BESTANDEN**.
- `config/personal_profile.yaml` enthält keine biografischen Angaben. Keiner der
  Texte erfindet Rolle, Unternehmen, Erfahrung, Kundenhistorie oder persönliche
  Episode.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Hashbindung |
|---|---:|---:|---:|---|---|
| POST 1 | 1.163 | 1.174 | 18 | `87f678be67aa9cb87a686584b5d11dbadcc6b9fa0a791a5246b267fa2b7dfb57` | Sollwert und Stilbericht bestätigt |
| POST 2 | 1.214 | 1.229 | 19 | `66f97623948804d2b40f73a0e6c0c06543dc13424c7195b9765dc50c054b32f7` | Sollwert und Stilbericht bestätigt |

## Deterministische Pflichtprüfung

| Kriterium | POST 1 | POST 2 |
|---|---|---|
| Limit `max_post_chars: 1300` | bestanden: 1.163 | bestanden: 1.214 |
| Vollständiger Kampagnen-CTA | exakt 1-mal | exakt 1-mal |
| Exakter UTM-Link | exakt 1-mal; keine weitere URL | exakt 1-mal; keine weitere URL |
| `#Compliance` | exakt 1-mal | exakt 1-mal |
| `#eIDAS` | exakt 1-mal | exakt 1-mal |
| `#RecordsManagement` | exakt 1-mal | exakt 1-mal |
| Weitere Hashtags | keine | keine |

Der vollständige Kampagnen-CTA ist in beiden Texten exakt und in der
vorgeschriebenen Zeilenfolge enthalten:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

## Aktueller Dubletten-Snapshot

Read-only-Snapshot zum Prüfzeitpunkt `2026-09-15T20:10:25+0200`:

| Queue-Stufe | Datei-SHA-256 | Post-Blöcke |
|---|---|---:|
| `approvals.md` | `c204e9afcd466fe88be1c99dedce02ac4750d417a037db8cdb734d2360963fd1` | 0 |
| `schedule.md` | `217291a6120a45b6c79a76d68099ac02fcd7ce6201cbb52de712b1cc055e8077` | 6 |
| `log.md` | `df22c177c4ad07910fa1d204a3a30bedee0e65676d461cb5eca3cc783e1a9ffd` | 3 |

Geprüfte Bestands-IDs: `post-2026-09-11-0001`,
`post-2026-09-11-0002`, `post-2026-09-13-0002`,
`post-2026-09-13-0001`, `post-2026-09-12-0004`,
`post-2026-09-12-0003`, `post-2026-09-10-0002`,
`post-2026-09-10-0001` und `post-2026-09-12-0001`.

- **Exakte Dubletten:** keine. Kein Bestands-Post ist text- oder hashidentisch
  mit einem der beiden R8-Markertexte.
- **Funktionale Dublette POST 1:** keine. Der eigenständige Nutzenkern ist der
  benannte und menschlich verantwortete Ausnahmeweg bei unklarer Auswertung.
  Bestandswinkel zu Datenweg/Fremd-Cloud, Audit-Nachweis, Demo-Test,
  Übergabeverlust, grünem Haken, Outlook-Integration, BIV-Kontext oder
  LKW/API-Workflow beantworten diese Zuständigkeitsfrage nicht.
- **Funktionale Dublette POST 2:** keine. Kein Bestands-Post behandelt den
  konkreten Browser-Agenten-Handover samt Übergabezettel und ausdrücklicher
  Mensch-vs.-Agent-, Mandats- und Produktgrenze. Allgemeine BIV-, Freigabe- oder
  Workflow-Themen sind nur benachbart.

## POST 1

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch und enger ICP: Records/Posteingang, Vertragsadministration sowie
  Compliance/Legal Ops bei signierten PDFs vor Freigabe oder Archivierung sind
  ausdrücklich adressiert.
- Themen- und Kampagnenfit: Der Text fokussiert den operativen Ausnahmeweg bei
  unklarer Signatur-/Zertifikatsauswertung und damit einen relevanten
  Prüf-, Records- und Compliance-Prozess.
- Stimme: Flughafenschale, Piepen und die kurz wartenden Zuständigen ergeben ein
  verständliches, trocken humorvolles Bild. Die Ich-Perspektive und offene
  Praxisfrage wirken persönlich; kein Marketing-Sprech oder Buzzword-Bingo.
- Fakten und Produktrolle: Der Swisscom Document Validator bleibt korrekt auf
  ZertES-/eIDAS-signierte PDFs sowie Signatur- und Zertifikatsinformationen
  begrenzt. Die PDF bleibt in der eigenen Umgebung; ihr Hash wird lokal
  gebildet.
- Entscheidungs-, Freigabe- und Rechtsgrenze: Der Text sagt ausdrücklich, dass
  das Ergebnis keine menschliche Beurteilung, Freigabe oder Rechtsprüfung
  ersetzt. Er verspricht weder automatische Compliance noch Revisionssicherheit
  oder einen automatisch erzeugten Ausnahmeprozess.
- CTA und Publikumsfrage sind passend und nicht drängend. Keine erfundene
  Biografie oder Kundengeschichte, keine Konkurrentenabwertung, keine Politik,
  Religion, Garantie, Täuschung oder Spam; keine relevante Brand-Safety-Gefahr.

**Pflichtänderungen:** Keine.

## POST 2

**Urteil: FREIGEGEBEN**

Begründung:

- Deutsch und enger ICP: Browser-Agent, signierte PDF, Signatur-/
  Zertifikatsauswertung, geschäftlicher Kontext und menschlich verantworteter
  nächster Schritt sind direkt an einen Records-/Compliance-Workflow gebunden.
- Themen- und Kampagnenfit: Der Text trifft die Kampagnenthemen AI-Agent im
  Browser, digitale Identität, nachvollziehbarer Handover und menschliche
  Verantwortung, ohne das Produkt als Agentensteuerung darzustellen.
- Stimme: Der angeklebte Schnurrbart, Staffelstab und Übergabezettel bilden ein
  konsistentes, persönliches und humorvolles Bild. Die Vierer-Liste ist konkret;
  kein Klamauk, Marketing-Sprech oder Spam.
- Fakten und Produktrollen: Der Document Validator bleibt auf signierte PDFs
  sowie Signatur- und Zertifikatsinformationen begrenzt; PDF und lokaler Hash
  sind kampagnenkonform beschrieben. Der Business Identity Validator kann
  ausschließlich Kontext zu Zeichner, Unternehmen und Berechtigung ergänzen.
- Mensch-vs.-Agent- und Mandatsgrenze: ausdrücklich und unmissverständlich.
  Weder Document Validator noch BIV erkennen, ob Mensch oder Agent den Browser
  bedient, oder erteilen einem Agenten Mandat. Das Ergebnis ersetzt keine
  menschliche Beurteilung, Freigabe oder Rechtsprüfung; der verantwortliche
  nächste Schritt bleibt beim Menschen.
- CTA und Publikumsfrage sind passend und nicht drängend. Keine Rechtsgarantie,
  automatische Compliance/Freigabe, erfundene Biografie oder Kundengeschichte,
  Konkurrentenabwertung, Politik, Religion, Täuschung oder Brand-Safety-Gefahr.

**Pflichtänderungen:** Keine.

## Gesamtergebnis und Freigabegrenze

Beide exakt hashgebundenen R8-Markertexte sind **FREIGEGEBEN**. Diese
Reviewer-Freigaben sind **keine Nutzerfreigaben** und berechtigen nicht zur
Queue-Aufnahme, Checkbox-Änderung, Planung oder Veröffentlichung. Die zwei Texte
sind getrennte Kandidaten; `posts_per_run: 1` begrenzt eine spätere Ausführung
auf höchstens einen Post pro Lauf/Zyklus. Entwürfe, Queue, Checkboxen, Termine,
Schedule und Log blieben unverändert; keine Operator-, Browser-, Bild-,
LinkedIn- oder Veröffentlichungsaktion wurde ausgeführt.
