# CW-DV-20260921-R17-I2 — materiell neuer Ersatzentwurf

## POST 2-I2 — Klingelbeschriftung: Eingangskanal ist keine Signaturprüfung

- Kurzthema: Vertrauen in Absendername, Domain oder Portal von der Prüfung der PDF trennen
- Unicode-Codepoints: 1278
- SHA-256: `61afa5d75a2e5eabe4590f8b7b645220b69a067a7475dd2b6ef67e28430a6eb8`

Hashbasis: UTF-8-Bytes des reinen Posttexts zwischen den Markern, ohne abschliessenden Zeilenumbruch.

=== POST 2-I2 START ===
Der Absendername im Posteingang ist wie die Klingelbeschriftung.

Nett zu wissen, wer läutet. Noch kein Prüfbericht für das Paket.

In Records/Posteingang, Vertragsadministration und Compliance Ops kommen signierte PDFs über bekannte Domains, vertraute E-Mail-Adressen oder gewohnte Portale an. Das sagt etwas über den Eingangskanal. Nicht aber, welche Signatur- und Zertifikatsinformationen in der PDF vorliegen.

Darum würde ich zwei Fragen nicht in denselben Briefkasten werfen:

Wie kam das Dokument an?
Was lässt sich an der signierten PDF prüfen?

Der Swisscom Document Validator prüft bei entsprechend ZertES-/eIDAS-signierten PDFs Signatur- und Zertifikatsinformationen. Die PDF bleibt in der eigenen Umgebung, ihr Hash wird lokal gebildet. Er authentisiert weder den E-Mail-Absender noch das Portal.

Ein vertrauter Bote und ein geprüftes Paket sind zwei verschiedene Dinge.

Trennt euer Eingang heute klar zwischen «kam über einen vertrauten Kanal» und «die signierte PDF wurde geprüft»?

Vor dem Archivieren prüfen statt hoffen:
https://trustservices.swisscom.com/de/products/validator/document-validator?utm_source=linkedin&utm_medium=social&utm_campaign=docval_biv_backoffice
— für eine kurze Demo/Beratung: DM oder Kommentar.

#Compliance #eIDAS #RecordsManagement
=== POST 2-I2 END ===

## Dublettenabgrenzung

Der Text behandelt die Trennung von Kanalvertrauen und Prüfung der Signatur-/Zertifikatsinformationen in der PDF. Er behandelt weder Outlook-Integration oder Datenweg noch sichtbare Unterschrift, Dateiname, Versionszuordnung, Audit-Rückschau, Urlaubsvertretung oder Zwei-Status-Logik.
