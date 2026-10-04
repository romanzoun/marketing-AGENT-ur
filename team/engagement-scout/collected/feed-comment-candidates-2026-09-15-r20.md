# Feed-Kommentarkandidaten — 2026-09-15 — R20

## Lauf

- Exakter Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Sandbox-Versuch: lokaler CDP-Zugriff mit `EPERM` blockiert; keine Queue-Änderung.
- Wiederholung mit freigegebenem lokalem CDP-Zugriff: erfolgreich; CLI meldete 2 Kandidaten.
- Queue-Diff: exakt zwei neue, zunächst leere Kommentarblöcke 0001 und 0002.
- IDs, URLs und Original-`note:` wurden für die Prüfung unverändert übernommen. Eine separate Source-URN war in keinem Block vorhanden und wurde nicht erfunden.

## Semantische Einordnung

### Verworfen: comment-2026-09-15-0001

- URL: https://lnkd.in/p/eGBW3aTx
- Autor: Joerg Lenz
- Urteil: **UNPASSEND**
- Grund: Die Trefferwörter elektronische Identität/eIDAS sind nur eine Vorauswahl. Der vollständige Post ist eine politisch-historische Keynote-Zusammenfassung über Ministerin, sowjetische Besatzung, Freiheit, Staat und internationale Governance. Damit berührt er das Kampagnen-No-Go Politik und hat keinen belastbaren Anschluss an eingehende signierte PDFs, Zertifikatsprüfung vor Archiv/Freigabe, Records-/ECM-Workflows oder den engen ICP. Ein Kommentar müsste die Kampagnenperspektive künstlich aufsetzen.
- Queue-Folge: Der ausschließlich durch diesen Lauf neu angelegte Block wurde nach der dokumentierten Prüfung wieder entfernt; keine Checkbox, Planung oder Veröffentlichung.

### Behalten: comment-2026-09-15-0002

- URL: https://lnkd.in/p/eMEnq-m7
- Autor: Lissi GmbH
- Scout-Vorprüfung: **PASSEND**; unabhängige Strategieprüfung anschließend **BEDINGT PASSEND**
- Zielsprache: Englisch
- Grund: Der vollständige Post behandelt eIDAS-2.0-Interoperabilität, Wallet-to-Verifier-Kommunikation, Access-/Registration-Certificate-Lifecycle, browsernahe Verifikation sowie wiederholbare Produktionstests statt einmaliger Compliance-Prüfung. Das passt fachlich zu belastbarer Zertifikatsauswertung, digitaler Identität, Auditierbarkeit und integrierten Prüfprozessen. Der Bezug bleibt eine persönliche fachliche Perspektive; keine aufgesetzte Produktwerbung und kein schlechtredender Wettbewerbsvergleich.
- Queue-Folge: Der Block bleibt mit leerer Freigabe-Checkbox in `approvals.md` und wird nur textlich/Stil/Review bearbeitet.

## Rohblöcke unmittelbar nach Sammlung

### Treffer 1 — unverändert

```yaml
### comment-2026-09-15-0001 — comment
- [ ] freigeben

```yaml
id: comment-2026-09-15-0001
kind: comment
campaign: DocVal + BIV — vor Archiv / vor Freigabe
campaign_version: 1
source_job_id: job-0003
text: ''
url: https://lnkd.in/p/eGBW3aTx
author: Joerg Lenz
note: "Feed post\n\nJoerg Lenz\n\n \n • 1st\n\nWorking on simplicity meeting compliance\
  \ in combining artificial intelligence and digital trust services. Driving adoption\
  \ of trustworthy identity proofing, electronic signature, verifiable credentials\
  \ & more \n\n14h • Edited • \n\n\U0001F1EA\U0001F1FA\U0001F194 Dignity before technology:\
  \ The theme of the opening keynote of ENISA Trust Services and eID Forum 2026 in\
  \ Tallinn \U0001F1EA\U0001F1EA \n\nThe 12th European Union Agency for Cybersecurity\
  \ (ENISA) Trust Services and eID Forum opened at Kultuurikatel with a keynote by\
  \ Liisa Pakosta, Estonia's Minister of Justice and Digital Affairs, who reframed\
  \ electronic identity not as an engineering achievement but as a question of human\
  \ dignity and freedom.\n\nPakosta grounded her argument in lived history. Under\
  \ Soviet occupation, obtaining a passport to travel meant applying to Moscow for\
  \ an exemption - an experience she described as a humiliation she hopes few in the\
  \ room have known. Where people are not free, she noted, they have no identity of\
  \ their own. \n\nAfter Estonia regained independence in 1991, the country set out\
  \ to do everything differently: democracy requires trust, trust requires transparency,\
  \ and digital systems make it possible to see who did what, when and how.\n\nPakosta\
  \ mentioned this was the real driver of Estonia's digital journey: The aim was never\
  \ to become the world's most technological country, but to give people back the\
  \ dignity and freedom associated with an identity they control.\n\nShe also offered\
  \ a market lesson relevant to the eIDAS 2.0 debate: it was not the state that made\
  \ Estonian eID successful, but the banking sector, which built electronic identity\
  \ to move money and lent it credibility. \n\nGovernment ran joint campaigns with\
  \ banks - if you trust your money to this identity, why not public services? Voluntary\
  \ uptake alone did not work; adoption came once use became mandatory.\n\nThe unfinished\
  \ business, Pakosta said, is international recognition. \n\nTravelling to a United\
  \ Nations event in Geneva this July, she used mobile electronic identity throughout\
  \ and was asked for no documents - until she reached UN headquarters, where she\
  \ had to have her embassy produce a printed copy of her paper passport. \n\nHumanity\
  \ already recognises each other's paper passports, she observed; the question is\
  \ why the digital equivalent remains unresolved. Estonia has raised this with ICAO\
  \ and the UN for years, and she welcomed the EU's current seriousness on the file.\n\
  \nPakosta concluded : the remaining obstacles are cultural and governance-related,\
  \ not technological. Fraud with paper documents and AI-driven attacks on systems\
  \ are manageable problems. \n\nWhat is needed is cooperation between human beings\
  \ (and their organizations they work for)- regulation, international agreements\
  \ and workable global governance - so that trusted identity delivers what it should:\
  \ the freedom to travel, build companies, research and create.\n\nIf you are on\
  \ site in Tallinn: feel free to (re-) connect with Luigi-Enrico Tomasini and myself\
  \ - engaging here on behalf of Namirial catching up with progress being made and\
  \ pick up intelligence to be shared with our customers and partners . \n… more\n\
  \nMichał Tabor and 13 others reacted\nMichał Tabor and 13 others\n\n1 repost\n1\
  \ repost\n\nLike\nComment\nRepost\nSend"
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
```

### Treffer 2 — unverändert

```yaml
### comment-2026-09-15-0002 — comment
- [ ] freigeben

```yaml
id: comment-2026-09-15-0002
kind: comment
campaign: DocVal + BIV — vor Archiv / vor Freigabe
campaign_version: 1
source_job_id: job-0003
text: ''
url: https://lnkd.in/p/eMEnq-m7
author: Lissi GmbH
note: "Feed post\n\nLissi GmbH\n\n \n\nVisit website\n\n3w • \n\n\U0001F1EA\U0001F1FA\
  \ \U0001F4F2 The EUDI Wallet regulation is standardized. So why isn't the wallet\
  \ integration plug-and-play? ⬇️\n\nWelcome to our new monthly format: Sales Question\
  \ of the Month, answered by Martin Schmid, Head of Sales at Lissi.\n\nThis month's\
  \ question comes up in almost every technical scoping call:\n\"If eIDAS 2.0 is a\
  \ standardized regulation, why isn't interoperability between wallets simply plug-and-play?\"\
  \n\nMartin's answer:\n\nAchieving cross-border interoperability introduces real\
  \ integration complexity. All wallets conform to a common regulatory standard —\
  \ but implementation across 30+ national ecosystems remains fragmented. Each member\
  \ state interprets configurations slightly differently. Standards-compliant on paper\
  \ does not mean interoperable in practice.\n\nThree reasons why:\n\n➡️ Protocol\
  \ churn management — platforms must continuously track and maintain low-level protocol\
  \ updates, including the High Assurance Interoperability Profile (HAIP) and advanced\
  \ querying mechanics driven by OpenID4VP (the protocol family behind wallet-to-verifier\
  \ communication).\n\n➡️ Automated certificate handling — relying parties must manage\
  \ the full lifecycle of Access and Registration Certificates, dynamically routing\
  \ requests to national registrars for every downstream client transaction.\n\n➡️\
  \ Evolving core APIs — platforms need built-in support for next-generation frameworks\
  \ like the W3C Digital Credentials API (DC API), which eliminates QR code vulnerabilities\
  \ and enables native browser-to-wallet bridging.\n\nIn a nutshell: validating production\
  \ flows requires rigorous testing against dynamic sandboxes — not a one-time compliance\
  \ check.\n\n\U0001FAC6 This is exactly the layer of complexity Lissi's Connector\
  \ is built to absorb, so your teams don't have to track every national implementation\
  \ quirk themselves.\n\nWhat's the question you keep getting asked about EUDI Wallet\
  \ integration? Drop it below — it might be next month's feature. \U0001F91D\n\n\
  … more\n\nMonthly Sales Question\n\n·\n\n2 pages\n\nHelge Michael and 17 others\
  \ reacted\nHelge Michael and 17 others\n\n2 reposts\n2 reposts\n\nLike\nComment\n\
  Repost\nSend"
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
```
