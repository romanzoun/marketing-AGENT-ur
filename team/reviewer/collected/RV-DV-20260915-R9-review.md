# Reviewer-Schlussprüfung RV-DV-20260915-R9

## Prüfgrundlage und Textbindung

- Geprüft wurden ausschließlich die zwei unveränderten Markertexte aus
  `team/copywriter/collected/document-validator-two-2026-09-15-r9.md` gegen die
  aktive Kampagne, das persönliche Profil, das Stilprofil, die bestandene
  Stilprüfung `SE-DV-20260915-R9` und den aktuellen Kampagnen-Queue-Bestand.
- Jedes Marker-Paar kommt genau einmal vor. Codepoints, Bytes, interne LF und
  SHA-256 beziehen sich auf den exakten UTF-8-Text zwischen den Markern, ohne
  zusätzlichen Schluss-LF.
- Die Stilprüfung bindet dieselben Texte und bewertet POST 1 mit **0,95** sowie
  POST 2 mit **0,96** jeweils als **BESTANDEN**. Es gab keine Textänderung und
  deshalb keine erneute Copywriter-, Stil- oder Hashrunde.
- `config/personal_profile.yaml` enthält keine biografischen Angaben. Keiner der
  Texte erfindet Rolle, Unternehmen, Erfahrung, Kundenhistorie oder persönliche
  Episode.

| Text | Unicode-Codepoints | UTF-8-Bytes | interne LF | SHA-256 | Hashbindung |
|---|---:|---:|---:|---|---|
| POST 1 | 1.128 | 1.145 | 16 | `1ec10ba95e8cae298cdf54b556905c90cb9b19a834d3a3abaf61f9daa45438c2` | Sollwert und Stilbericht bestätigt |
| POST 2 | 1.158 | 1.176 | 14 | `2bd48362539c01c396f52557e00359cfa3d83a7b45a982985d26a53673a223d8` | Sollwert und Stilbericht bestätigt |

## Deterministische Pflichtprüfung

| Kriterium | POST 1 | POST 2 |
|---|---|---|
| Limit `max_post_chars: 1300` | bestanden: 1.128 | bestanden: 1.158 |
| Vollständiger Kampagnen-CTA | exakt 1-mal | exakt 1-mal |
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

## Aktueller Dubletten-Snapshot

Read-only-Snapshot zum Prüfzeitpunkt `2026-09-15T22:30:17+0200`:

| Queue-Stufe | Datei-SHA-256 | Post-Blöcke |
|---|---|---:|
| `approvals.md` | `c204e9afcd466fe88be1c99dedce02ac4750d417a037db8cdb734d2360963fd1` | 0 |
| `schedule.md` | `ff6dac784e358f27b1b1eec22d3e7b22c1a3a69115d552e99728e8e69a4fa8ab` | 8 |
| `log.md` | `df22c177c4ad07910fa1d204a3a30bedee0e65676d461cb5eca3cc783e1a9ffd` | 3 |

Geprüfte Bestands-IDs: `post-2026-09-11-0001`,
`post-2026-09-11-0002`, `post-2026-09-13-0002`,
`post-2026-09-13-0001`, `post-2026-09-12-0004`,
`post-2026-09-12-0003`, `post-2026-09-15-0001`,
`post-2026-09-15-0002`, `post-2026-09-10-0002`,
`post-2026-09-10-0001` und `post-2026-09-12-0001`.

- **Exakte Dubletten:** keine. Kein aktueller Bestands-Post ist text-,
  normalisierungs- oder hashidentisch mit einem der beiden R9-Texte.
- **Funktionale Dublette POST 1:** keine. Der eigenständige Nutzenkern ist die
  Warnung, einen amtlich klingenden Dateinamen oder ein Label nicht mit einem
  Prüfergebnis zu verwechseln. Bestandswinkel zu Datenweg, Audit-Nachweis,
  Demo-Test, Übergaben, grünem Haken, Outlook-Integration, BIV-Kontext,
  Ausnahmeweg, Agenten-Handover oder LKW/API-Workflow behandeln diesen
  Dateiname-als-Scheinbeleg-Winkel nicht.
- **Funktionale Dublette POST 2:** keine. Der Urlaubsvertretungs-Test prüft als
  eigener operativer Winkel, ob ein wiederholbarer Prüfprozess ohne geheimes
  Personenwissen funktioniert. Der vorhandene LKW/API-Workflow-Post ist
  benachbart, fokussiert aber manuelle Einzelaktionen und den festen
  Prüfschalter; kein Bestands-Post behandelt Vertretbarkeit, implizites Wissen
  oder den Ferien-/Escape-Room-Test.

## POST 1 — Der Dateiname ist kein Prüfbericht

**Urteil: freigegeben**

- Deutsch und enger ICP: Records- und Vertragsadmin-Teams mit regelmäßig
  eingehenden signierten PDFs vor Freigabe oder Archivierung sind konkret
  adressiert; kein pauschales „alle Backoffice“.
- Themen und Stimme: Der amtlich klingende Dateiname und der selbst gemalte
  Reisepass-Stempel machen den Unterschied zwischen Label und Prüfung
  verständlich. „Für mich“, die knappe Pointe und die offene Praxisfrage wirken
  persönlich, humorvoll und fachlich; kein Buzzword- oder Marketing-Sprech.
- Fakten und Produktrollen: Der Swisscom Document Validator bleibt korrekt auf
  ZertES-/eIDAS-signierte PDFs sowie Signatur- und Zertifikatsinformationen
  begrenzt. PDF und lokaler Hash sind kampagnenkonform beschrieben. Der Business
  Identity Validator kann ausschließlich Kontext zu Zeichner, Unternehmen und
  Berechtigung ergänzen.
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

Beide exakt hashgebundenen R9-Texte sind **freigegeben**. Diese
Reviewer-Freigaben sind keine Nutzerfreigaben und berechtigen weder zur
Queue-Aufnahme noch zu Checkbox-, Termin-, Planungs-, Operator-, Browser-,
LinkedIn- oder Veröffentlichungsaktionen. Die zwei Texte bleiben getrennte
Kandidaten; `posts_per_run: 1` begrenzt eine spätere Veröffentlichung auf
höchstens einen Post pro Lauf/Zyklus. Ausgangstexte, Queue, Checkboxen,
Schedule und Log blieben unverändert.
