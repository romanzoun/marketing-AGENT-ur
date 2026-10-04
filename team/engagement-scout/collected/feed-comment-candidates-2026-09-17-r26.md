# Feed-Kommentarkandidaten — Document Validator — 2026-09-17 — R26

## Suchlauf

Exakt ausgeführt:

`./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`

- Sandbox-Versuch: lokaler CDP-Zugriff mit `EPERM` blockiert.
- Derselbe exakte Befehl mit freigegebenem Zugriff auf den bereits laufenden lokalen Chrome-Debug-Port wiederholt.
- Browser-Vorauswahl: `2 Beitrag/Beiträge gesammelt (new-feed)`.
- CLI-Ergebnis: `kandidaten: 2`.
- Tatsächlich neu persistiert: genau ein ID/URL/`note:`-Block. Ein zweiter belastbarer Block war nicht vorhanden; wegen der bekannten ID-Kollision wurde nichts rekonstruiert.

## Rohfund — vollständig und unverändert aus der Queue gesichert

```yaml
id: comment-2026-09-17-0003
kind: comment
campaign: DocVal + BIV — vor Archiv / vor Freigabe
campaign_version: 1
source_job_id: job-0003
text: ''
url: https://lnkd.in/p/eYqf7Fv7
author: Timo Behrmann
note: "Feed post\n\nTimo Behrmann\n\n \n • 1st\n\nIndustry Lead - Public Sector |\
  \ Digital Identity, GovTech & eGovernment @ Nect GmbH | M.Sc. Leadership & Change\
  \ Management Graduate\n\nBook an appointment\n\n20h • \n\nSmart Country Convention\
  \ 2026: Das Klassentreffen. \n\nVom 13. bis 15. Oktober 2026 trifft sich die Public‑Sector‑Community\
  \ wieder in Berlin zur Smart Country Convention. \n\nAuch ich freue mich gemeinsam\
  \ mit dem Team von Nect auf viele Gespräche rund um: \n\U0001F449 Digitale Identitäten\L\
  \U0001F449 EUDI‑Wallet & digitale Nachweise\L\U0001F449 Registermodernisierung\L\
  \U0001F449 Ende‑zu‑Ende‑Digitalisierung\L\U0001F449 Nutzerfreundliche Verwaltungsprozesse\
  \ \n\nBesonders spannend wird aus meiner Sicht die Frage sein, wie Verwaltungen\
  \ heute bereits konkrete Schritte in Richtung EUDI‑Wallet 2027 gehen können, ohne\
  \ auf den offiziellen Rollout warten zu müssen. \n\nMit eIDAS‑konformen Identitäts-\
  \ und Signaturdiensten sowie dem EUDI-ConNECTor beschäftigen wir uns täglich mit\
  \ der Frage, wie digitale Identitäten nicht nur verfügbar, sondern auch tatsächlich\
  \ genutzt werden. \n\n\U0001F4CD Ihr findet uns: \n- im Wallet‑Forum (Halle 25,\
  \ Stand 205)\L- sowie am VISA‑Gemeinschaftsstand (hub27, Stand 316)\n\nIch freue\
  \ mich auf viele bekannte und neue Gesichter in Berlin.\n\n#SCCON26 #SmartCountryConvention\
  \ #DigitaleIdentität #EUDIWallet #GovTech #Verwaltungsdigitalisierung #DigitaleVerwaltung\
  \ #eGovernment #Digitalisierung\n\n… more\n\nShow translation\n\nMichail Wolochonskij\
  \ and 39 others reacted\nMichail Wolochonskij and 39 others\n\n1 comment\n1 comment\n\
  \n•\n\n1 repost\n1 repost\n\nLike\nComment\nRepost\nSend"
user_memory_note: ''
reshare_with_comment: false
image_path: null
image_source: null
image_origin: null
image_prompt: ''
image_auto_selected: null
image_error: ''
published_url: null
published_at: null
publish_at: null
generated_text: null
evaluation_score: null
evaluation_note: ''
evaluated_at: null
approval_origin: null
auto_approval_threshold: null
```

## Semantische Entscheidung

**VERWORFEN / nicht kampagnenrelevant genug.** Der Beitrag enthält echte Digital-Identity-, EUDI-Wallet-, eIDAS- und Signaturdienst-Begriffe und ist damit ein Keyword-Treffer. Inhaltlich ist er jedoch eine Messe- und Standankündigung. Er enthält keinen konkreten Anschluss an eingehende signierte PDFs, Prüfung vor Archiv/Freigabe, Zertifikatsauswertung, lokalen Hash/Datenfluss, Audit-Trail, Records-/ECM-Prozesse oder die Produktrollen von Document Validator und BIV. Der enge ICP der Kampagne wird nicht adressiert. Die Pflicht-Tags `#Compliance` und `#RecordsManagement` sowie eine DocVal-/PDF-/Archivbrücke wären aufgesetzt.

Folge: Rohfund gesichert, leerer ungekreuzter Queue-Block entfernt, kein Kommentar erzwungen. Kein geeigneter Kandidat zur Übergabe an Content-Stratege, Copywriter, Style-Evaluator oder Reviewer.
