# Reviewer-Schlussprüfung RV-DV-20260915-R9-QUEUE-REPAIR

## Prüfgrundlage und Textbindung

- Geprüft wurden ausschließlich die zwei finalen Markertexte aus
  `team/copywriter/collected/document-validator-two-2026-09-15-r9-queue-repair.md`
  und die geparsten tatsächlichen `text:`-Werte der Queue-IDs
  `post-2026-09-15-0001` und `post-2026-09-15-0002` in `approvals.md`.
- Markertext und geparster Queue-Text sind je ID exakt identisch. Codepoints,
  Bytes, interne LF und SHA-256 beziehen sich auf den exakten UTF-8-Text ohne
  zusätzlichen Schluss-LF.
- Die unabhängige Stilprüfung bindet dieselben Texte und bewertet POST 1 mit
  **0,95** sowie POST 2 mit **0,96** jeweils als **BESTANDEN**. Es erfolgte
  keine weitere Textänderung.
- `config/personal_profile.yaml` enthält keine biografischen Angaben. Keiner der
  Texte erfindet Rolle, Unternehmen, Erfahrung, Kundenhistorie oder eine
  persönliche Episode.

| Text / Queue-ID | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Bindung |
|---|---:|---:|---:|---|---|
| POST 1 / `post-2026-09-15-0001` | 1.120 | 1.136 | 16 | `ba66a282cdb923f560bc3eb4a380aa05ed1b3a555d7fc9003d78f35cf6f2d286` | Marker = Queue = Sollwert |
| POST 2 / `post-2026-09-15-0002` | 1.158 | 1.176 | 14 | `2bd48362539c01c396f52557e00359cfa3d83a7b45a982985d26a53673a223d8` | Marker = Queue = Sollwert |

## Deterministische Pflichtprüfung

| Kriterium | POST 1 | POST 2 |
|---|---|---|
| Limit `max_post_chars: 1300` | bestanden: 1.120 | bestanden: 1.158 |
| Vollständiger exakter Kampagnen-CTA | exakt 1-mal | exakt 1-mal |
| Exakter UTM-Link | exakt 1-mal; keine weitere URL | exakt 1-mal; keine weitere URL |
| `#Compliance` | exakt 1-mal | exakt 1-mal |
| `#eIDAS` | exakt 1-mal | exakt 1-mal |
| `#RecordsManagement` | exakt 1-mal | exakt 1-mal |
| Weitere Hashtags | keine | keine |

Der vollständige CTA ist in beiden Texten exakt und in der vorgeschriebenen
Zeilenfolge enthalten:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

## Dublettenprüfung gegen `approvals.md`, `schedule.md` und `log.md`

- Bestand: 2 Post-Blöcke in `approvals.md`, 8 in `schedule.md` und 3 in
  `log.md`. Beim Vergleich in `approvals.md` wurde die jeweils eigene gebundene
  Textinstanz nicht als Dublette gegen sich selbst gezählt.
- **Exakte Dubletten:** keine. Die beiden Reparaturtexte sind untereinander und
  gegenüber allen anderen Posttexten weder text- noch normalisierungsidentisch.
- **Funktionale Dublette POST 1:** keine. Der eigenständige Nutzenkern ist die
  Warnung, einen amtlich klingenden Dateinamen oder ein Label nicht mit einem
  Prüfergebnis zu verwechseln. Die Bestandswinkel zu Datenweg, Audit-Nachweis,
  Demo-Test, Übergaben, grünem Haken, Outlook-Integration, BIV-Kontext,
  Ausnahmeweg, Browser-Prozess und LKW/API-Workflow behandeln diesen
  Dateiname-als-Scheinbeleg-Winkel nicht.
- **Funktionale Dublette POST 2:** keine. Der Urlaubsvertretungs-Test prüft, ob
  ein wiederholbarer Prüfprozess ohne geheimes Personenwissen funktioniert.
  Der benachbarte LKW/API-Workflow-Post fokussiert manuelle Einzelaktionen und
  einen festen Prüfschalter; kein Bestands-Post behandelt Vertretbarkeit,
  implizites Wissen oder den Ferien-/Escape-Room-Test.

## POST 1 — Der Dateiname ist kein Prüfbericht

**Urteil: freigegeben**

- Deutsch und enger ICP: Records- und Vertragsadmin-Teams mit regelmäßig
  eingehenden signierten PDFs sind konkret adressiert; kein pauschales „alle
  Backoffice“.
- Themen und Stimme: Der amtlich klingende Dateiname und der selbst gemalte
  Reisepass-Stempel machen den Unterschied zwischen Label und Prüfung greifbar.
  „Für mich“, die knappe Pointe und die offene Praxisfrage wirken persönlich,
  humorvoll und fachlich; kein Buzzword- oder Marketing-Sprech.
- Fakten und Produktrollen: Der Swisscom Document Validator bleibt korrekt auf
  ZertES-/eIDAS-signierte PDFs sowie Signatur- und Zertifikatsinformationen
  begrenzt. PDF und lokaler Hash sind kampagnenkonform beschrieben. Der
  Business Identity Validator ergänzt ausschließlich Kontext zu Zeichner,
  Unternehmen und Berechtigung.
- Menschliche Zuständigkeit und Rechtsgrenze: Freigabe,
  Archivierungsentscheidung und rechtliche Beurteilung bleiben ausdrücklich
  beim zuständigen Team. Keine Rechtsgarantie, automatische Compliance,
  Freigabe oder Revisionssicherheitsbehauptung.
- CTA und Publikumsfrage sind passend und nicht drängend. Keine erfundene
  Biografie oder Kundengeschichte, Konkurrenzabwertung, Politik, Religion,
  Täuschung, Spam oder Brand-Safety-Gefahr.

**Pflichtänderungen:** keine.

## POST 2 — Der Urlaubsvertretungs-Test

**Urteil: freigegeben**

- Deutsch und enger ICP: Die Schwelle von 10+ signierten PDFs pro Monat, der
  Records-/ECM-Workflow und der Schritt vor Freigabe oder Archivierung treffen
  den definierten operativen ICP direkt.
- Themen und Stimme: Geheimes Klopfmuster, Escape Room mit Ferienplan und
  Urlaubsvertretungs-Test bilden einen konsistenten, nahbaren Vergleich. Die
  Ich-Haltung, konkreten Prozessfragen und Schlussfrage sind persönlich und
  fachlich; kein Klamauk, Buzzword-Bingo oder Werbesprech.
- Fakten und Produktrolle: Der Swisscom Document Validator ist korrekt als per
  API einbindbarer, wiederholbarer Prüfbaustein für Signatur- und
  Zertifikatsinformationen bei ZertES-/eIDAS-signierten PDFs beschrieben. Die
  PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet. Dem Produkt
  werden keine BIV-, Agentensteuerungs- oder Entscheidungsfunktionen
  zugeschrieben.
- Menschliche Zuständigkeit und Rechtsgrenze: Zuständigkeit,
  Ausnahmebehandlung, Freigabe und Rechtsprüfung bleiben ausdrücklich beim
  Team. Der Text verspricht weder eine juristische Garantie noch automatische
  Compliance oder Revisionssicherheit.
- CTA und Publikumsfrage sind passend und nicht drängend. Keine erfundene
  Biografie oder Kundengeschichte, Konkurrenzabwertung, Politik, Religion,
  Täuschung, Spam oder Brand-Safety-Gefahr.

**Pflichtänderungen:** keine.

## Gesamtergebnis und Freigabegrenze

Beide exakt hashgebundenen R9-QUEUE-REPAIR-Texte sind **freigegeben**.
`posts_per_run: 1` begrenzt eine spätere Veröffentlichung pro Lauf/Zyklus und
nicht die Zahl dieser zwei getrennten Nutzerfreigabe-Kandidaten. Diese
Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zu
Checkbox-, Termin-, Schedule-, Operator-, Browser-, LinkedIn- noch
Veröffentlichungsaktionen. Texte und Queue blieben unverändert.
