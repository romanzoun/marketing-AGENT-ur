# Reviewer-Prüfung RV-DV-20260912-R4-FINAL

Geprüft wurden ausschließlich die beiden Texte zwischen
`POST-1-START/END` und `POST-2-START/END` in
`team/copywriter/collected/document-validator-two-2026-09-12-r4-final.md`.
Maßstab waren die aktive Kampagne, das persönliche Profil, das Stilprofil,
der leere Lernstand, der aktuelle Approved-Korpus und die Reviewer-Regeln. Die
Stilvorprüfung mit 0,91 beziehungsweise 0,87 wurde berücksichtigt, ersetzt aber
nicht diese unabhängige Prüfung.

## Deterministische Pflichtprüfung

Gezählt wurden Unicode-Codepoints des reinen Markertexts inklusive interner
Zeilenumbrüche; Marker und der unmittelbar vor dem END-Marker stehende
Trenn-Zeilenumbruch wurden nicht mitgezählt.

| Text | Unicode-Codepoints | Interne Zeilenumbrüche | Limit | Rest | Pflicht-Hashtags | Vollständiger exakter CTA | Exakter UTM-Link |
|---|---:|---:|---:|---:|---|---:|---:|
| POST 1 | 1.233 | 19 | 1.300 | 67 | alle drei, je genau 1× | 1× | 1× |
| POST 2 | 1.278 | 18 | 1.300 | 22 | alle drei, je genau 1× | 1× | 1× |

Die drei Pflicht-Hashtags sind in beiden Texten exakt `#Compliance`, `#eIDAS`
und `#RecordsManagement`. Der vollständige Kampagnen-CTA steht jeweils exakt
einmal im Text:

```text
Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.
```

Die unabhängig ermittelten SHA-256-Werte der reinen Texte sind:

- POST 1: `e3cd17a2864d844f30a586004892bbda1061efbab0adf50610c30baea3270e6c`
- POST 2: `c8ccdb1e1675f0e58a28a89f18493d7d049f4ef35093ef2ba8374ebeadbe281d`

Beide Werte stimmen mit der Stilprüfung überein. Beide Texte sind gültiges UTF-8
und enthalten weder CR-Zeichen, Unicode-Ersatzzeichen noch nachlaufende
Leerzeichen.

## POST 1 — Paketsiegel und Berechtigung

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

- **Sprache, Thema und enger ICP:** Der Text ist deutsch und richtet sich
  konkret an Records-/Posteingang, Vertragsadministration und Compliance Ops
  bei der Prüfung signierter PDFs. Er weitet die Zielgruppe nicht pauschal auf
  alle Backoffice-Teams aus.
- **Blickwinkel und Stimme:** Paketsiegel und Klebestreifen tragen einen klaren,
  eigenständigen Blickwinkel. Die Ich-Formulierung, die zwei konkreten Fragen
  und der „Zauberstempel“ ergeben eine persönliche, nahbare und fachlich
  glaubwürdige Stimme ohne Werbesprech.
- **Fakten und Produktrollentrennung:** Der Document Validator ist korrekt der
  Signaturprüfung und belastbareren Auswertung von Zertifikatsinformationen
  zugeordnet. BIV ergänzt Zeichner-, Unternehmens- und
  Berechtigungsinformationen. Der Text behauptet weder, dass DocVal die
  Berechtigung klärt, noch dass BIV die Signatur prüft.
- **Hash/PDF-Datenfluss:** Der Text macht hierzu keine Aussage und erzeugt damit
  keinen Widerspruch zur Kampagnenvorgabe. Dieser Post fokussiert zulässig die
  getrennten Produktrollen; die Kampagne schreibt den Datenfluss nicht als
  Pflichtsatz für jeden einzelnen Post vor.
- **Menschliche und rechtliche Grenzen:** Produkte liefern ausdrücklich nur
  Prüfinformationen. Rechtliche Würdigung und Freigabe bleiben beim zuständigen
  Team. Es gibt keine juristische Garantie und kein Heilsversprechen.
- **CTA, Spam und Brand-Safety:** Die Publikumsfrage und der einmalige
  Pflicht-CTA sind einladend, nicht drängend. Keine erfundene Biografie oder
  Kundengeschichte, keine Konkurrenzabwertung und keine verbotenen Themen.

## POST 2 — Grüner Haken im Nebel

**Urteil: FREIGEGEBEN**

**Pflichtänderungen: keine.**

- **Sprache, Thema und enger ICP:** Der Text ist deutsch und adressiert
  Records-Teams, Vertragsadministration und Compliance Ops mit regelmäßig
  eingehenden signierten PDFs. Signaturprüfung, Zertifikatsinformationen und
  spätere Nachvollziehbarkeit liegen eng auf den Kampagnenthemen.
- **Blickwinkel und Stimme:** Grüner Haken, Nebel und Wegweiser vermitteln die
  Grenze eines oberflächlichen Statussignals bildhaft. „Ich mag dieses Bild“,
  kurze Fragen und das „spätere Rätsel“ geben dem Text einen persönlichen,
  zurückhaltend humorvollen Ton. Die leichte Mischung der Verkehrsbilder ist
  eine optionale Stilfrage, keine Pflichtänderung.
- **Fakten, Produktrolle und Datenfluss:** Der Document Validator ist korrekt
  der Signatur- und Zertifikatsauswertung zugeordnet. Die Aussage, dass die PDF
  in der eigenen Umgebung bleibt und ihr Hash lokal gebildet wird, entspricht
  exakt dem Kampagnen-Datenfluss. BIV wird nicht erwähnt und daher auch nicht
  fälschlich mit DocVal vermischt.
- **Menschliche und rechtliche Grenzen:** Das Prüfergebnis unterstützt den
  Prozess, ersetzt aber ausdrücklich weder rechtliche Würdigung noch menschliche
  Freigabe. Dass Revisionssicherheit nicht automatisch entsteht, verhindert
  eine unzulässige Garantie.
- **CTA, Spam und Brand-Safety:** Fachfrage, einmaliger Pflicht-CTA und drei
  Pflicht-Hashtags sind angemessen. Keine aggressive Wiederholung, erfundene
  Erfahrung, Konkurrenzabwertung, Politik oder Religion.

## Abschluss

- POST 1: **FREIGEGEBEN**, keine Pflichtänderung.
- POST 2: **FREIGEGEBEN**, keine Pflichtänderung.

Diese Reviewer-Freigaben sind ausdrücklich **keine Nutzerfreigaben** und
berechtigen weder zum Einplanen noch zum Veröffentlichen. `posts_per_run: 1`
bleibt die operative Obergrenze je Lauf/Zyklus. Ausgangstexte, Queue,
Checkboxen, Stilprofil, `learning.json`, Approved-Korpus, Planung und LinkedIn
blieben unverändert.
