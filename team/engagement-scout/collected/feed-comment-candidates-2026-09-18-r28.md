# Feed-Kommentarkandidaten — 2026-09-18 — R28

## Suchlauf

- Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Versuch im Workspace-Sandbox: fehlgeschlagen (`connect EPERM ::1:9222`).
- Identischer Wiederholungsversuch mit freigegebenem Zugriff auf den lokalen Chrome-Debug-Port: erfolgreich.
- Browser: `2 Beitrag/Beiträge gesammelt (new-feed)`.
- CLI: `kandidaten: 2`, Zieldatei `Kampagnen/document validator/queue/approvals.md`.
- Tatsächlich persistiert: zwei neue vollständige, leere und ungekreuzte Kommentarblöcke.

## Semantische Entscheidung

### 1. VERWORFEN

- ID: `comment-2026-09-18-0001`
- URL: `https://lnkd.in/p/e9QZwXwg`
- URN: im Originalblock nicht vorhanden; keine erfunden.
- Autor: `Viky Manaila 💯`
- Textfeld: leer geblieben.
- Begründung: Der Originalpost behandelt Fristen, Zertifizierung und gestaffelte Einführung der EUDI Wallet. Das ist ein echter Treffer für `eIDAS` und digitale Identität, aber kein enger Fit für Objective, ICP oder Produkte der Kampagne: kein eingehendes signiertes PDF, keine ZertES-/eIDAS-Signaturprüfung, kein Records-/Archiv-/Freigabeprozess, kein Audit-Trail/ECM und kein DocVal-/BIV-Anwendungsfall. Ein Kommentar müsste die PDF-/Records-Brücke künstlich ergänzen und die Pflicht-Tags `#Compliance` und `#RecordsManagement` würden den Originalpost überdehnen.

Vollständiger Originalpost aus `note:`:

```text
Feed post

Viky Manaila 💯

 
 • Following

eIDAS, Digital Identity, Digital Signatures & PKI expert

1w • 

2026 is the year the European Digital Identity (EUDI) Wallet becomes a legal reality. Under Regulation (EU) 2024/1183, every Member State must make at least one certified wallet available to its citizens, residents and businesses by 24 December 2026, with mandatory acceptance by regulated private-sector players following in late 2027. Will all 27 Member States cross that line with a fully functional, certified national solution? Almost certainly not, and for good reasons. This is not a story of failure. It is a reality check on what “ready” actually means, and why a pragmatic, phased approach may be the wisest path forward.

https://lnkd.in/dUbUZkdw

#eIDAS #EUDI #digitalwallets
… more

EUDI Wallets: The Deadline is not the finish line
EUDI Wallets: The Deadline is not the finish line

medium.com

Petar Chardakov and 83 others reacted
Petar Chardakov and 83 others

9 comments
9 comments

•

5 reposts
5 reposts

Like
Comment
Repost
Send

Adrian Doerk 🇪🇺 📲 Premium Profile 1st
Adrian Doerk 🇪🇺 📲 
 • 1st

Co-Founder Lissi GmbH | EUDI Wallet infrastructure for banks & regulated industries | Winner, SPRIND EUDI Wallet Challenge | eIDAS 2.0, KYC, SCA, QES

1w

As always a great read Viky. There is little transparent communication about the topic you're raising. I think we will get a comprehensive overview at the Trust Service forum / CA day next week in Tallin. Your post provides a excellent starting point for this important discussion. 
… more

3 reactions
3

1
1

See 8 more comments
```

### 2. VERWORFEN

- ID: `comment-2026-09-18-0002`
- URL: `https://lnkd.in/p/e-8FXAXJ`
- URN: im Originalblock nicht vorhanden; keine erfunden.
- Autor: `Joerg Lenz`
- Textfeld: leer geblieben.
- Begründung: Der Originalpost ist ein knapper Event-/Sessionhinweis über die Komplexität der EU Digital Identity Wallet, Konformitätsbewertung und Trust-Service-Zertifizierung. Trotz echter `eIDAS`-/Trust-/Compliance-Nähe fehlt der operative Anschluss an den engen ICP und die Kampagnenthemen: kein signiertes PDF, keine Signatur- oder Zertifikatsauswertung im Dokumentenworkflow, keine Archiv-/Freigabeentscheidung, kein Audit-Trail/Records/ECM und keine Identitäts-/Berechtigungsprüfung per BIV. Ein Produkt- oder Records-Bezug wäre aufgesetzt.

Vollständiger Originalpost aus `note:`:

```text
Feed post

Joerg Lenz

 
 • 1st

Working on simplicity meeting compliance in combining artificial intelligence and digital trust services. Driving adoption of trustworthy identity proofing, electronic signature, verifiable credentials & more 

2d • Edited • 

Joris Minolla mapping out the complexity of the EU Digital Identity Wallet and the best approach from a conformity assessment body.

For himself he is attempting to catch up with acronyms in mapping them on the wall in his home office to gain an in-depth understanding over time as well as to stay on top of the increasing complexity and the various national specifics. 

That sounds a bit familiar to my approaches … 

He is yet covering the aspects of Trust Service Certification as a contribution to 18th CA Day in Tallinn. 

Today’s sessions are also streamed online. 
… more

Franziska Granc and 6 others reacted
Franziska Granc and 6 others

1 comment
1 comment

•

1 repost
1 repost

Like
Comment
Repost
Send
```

## Folgeworkflow

- Behalten: `0`.
- Verworfen: `2`.
- Kein Kandidat an `content_strategist`, `copywriter`, `style_evaluator` oder `reviewer` übergeben, weil kein Originalpost die verlangte Schwelle „wirklich passend“ erfüllt.
- Deshalb keine finalen `text:`-Inhalte, keine Style-Scores und keine Reviewer-Entscheidungen.
- Die beiden leeren, ungekreuzten Neufundblöcke wurden nach dieser vollständigen Rohsicherung aus `approvals.md` entfernt. Bestehende Einträge und parallele Änderungen wurden erhalten.
- Nichts veröffentlicht, freigegeben, angekreuzt, eingeplant oder in `schedule.md` verschoben; kein fälliger Job ausgeführt.
