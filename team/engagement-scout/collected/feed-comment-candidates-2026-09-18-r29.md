# Feed-Kommentarkandidaten — 2026-09-18 — R29

## Suchlauf

- Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Versuch im Workspace-Sandbox: fehlgeschlagen (`connect EPERM ::1:9222`), noch vor Daten- oder Queue-Änderungen.
- Identischer Wiederholungsversuch mit freigegebenem Zugriff auf den lokalen Chrome-Debug-Port: erfolgreich.
- Browser: `2 Beitrag/Beiträge gesammelt (new-feed)`.
- CLI: `kandidaten: 2`, Zieldatei `Kampagnen/document validator/queue/approvals.md`.
- Queue-Diff: zwei neue vollständige, leere und ungekreuzte Kommentarblöcke; `schedule.md` und `log.md` blieben unverändert.

## Semantische Entscheidung

### 1. VERWORFEN

- ID: `comment-2026-09-18-0001`
- URL: `https://lnkd.in/p/eihZJpzY`
- URN: im Originalblock nicht vorhanden; keine erfunden.
- Autor: `Joerg Lenz`
- Textfeld: leer geblieben.
- Begründung: Der deutschsprachige Webinarpost behandelt die ab 2027 erwartete Annahme von EUDI-Wallet-Nachweisen, Relying-Party-Registrierung, Datensparsamkeit, Datenschutz-Folgenabschätzung, Pseudonyme, Intermediäre und AMLR. Damit bestehen echte Treffer bei `eIDAS`, digitaler Identität, Compliance sowie Banken/Versicherern. Für den engen Objective-/Produkt-/ICP-Fit fehlt jedoch der operative Kern: kein eingehendes signiertes PDF, keine ZertES-/eIDAS-Signatur- oder Zertifikatsauswertung, kein Archiv-/Freigabe-/Records-/ECM-Prozess, kein Audit-Trail und keine konkrete BIV-Prüfung von Zeichner, Unternehmen oder Berechtigung. Ein DocVal-/Records-Bezug müsste erfunden werden; der Kommentar würde daher aufgesetzt wirken.

Vollständiger Originalpost aus `note:`:

```text
Feed post

Joerg Lenz

 
 • 1st

Working on simplicity meeting compliance in combining artificial intelligence and digital trust services. Driving adoption of trustworthy identity proofing, electronic signature, verifiable credentials & more 

4h • 

Muss Ihre Organisation ab dem 24.12.27 Nachweise aus EU Digital Identity Wallets - inkl. d-you -  akzeptieren?

Für den größten Teil des Finanzsektors - Banken, Versicherer und Zahlungsdienstleister -  lautet die Antwort: ja. Die Vorbereitung dafür muss jetzt beginnen um die Pflichtenkaskade des Art. 5f eIDAS-VO umzusetzen. Das betrifft alle privaten Diensteanbieter, die gesetzlich oder vertraglich zu einer Online-Identifizierung mit starker Kundenauthentifizierung verpflichtet sind. Ausgenommen sind nur Klein- und Kleinstunternehmen. 
 
Wir schauen um was man sich jetzt und was man sich demnächst kümmern kann und sollte: 
- Registrierung als vertrauende Beteiligte 
- Abfragebeschränkung und Datensparsamkeit: Welche Attribute darf ich überhaupt anfragen – und wie belege ich das?
- Datenschutz-Folgenabschätzung, Betroffenenrechte, Hinweispflichten
- Pseudonym-Akzeptanz und ihre Ausnahmen 
- Vertragsanpassungsbedarf bei Intermediären 
  
Wer parallel die Anforderungen der AMLR umsetzen muss die ab dem 10.07.27 greifen, kennt das Muster: zwei Fristen, ein Prozess, ein Team. 

Darüber sprechen wir mit Per Meyerdierks (GSK Stockmann) und Klaus Fellner (Geschäftsführer Namirial GmbH) - auch über die Erkenntnisse aus der ersten Lesung des  Digitale Identitäten-Gesetzes (#DIdG) im Bundestag am 23.09.26.

📅 Fr, 25.09.26, 10:00 Uhr · online via Zoom · kostenfrei · inkl. Live-Q&A
 🔗 Anmeldung: https://lnkd.in/d57xCAeP

#EUDIWallet #eIDAS2 #DigitaleIdentitäten #dyou #Namirial


… more

Show translation

Detlef Hühnlein and 11 others reacted
Detlef Hühnlein and 11 others

1 comment
1 comment

Like
Comment
Repost
Send
```

### 2. VERWORFEN

- ID: `comment-2026-09-18-0002`
- URL: `https://lnkd.in/p/emedu96a`
- URN: im Originalblock nicht vorhanden; keine erfunden.
- Autor: `Procivis • Securing Digital Trust`
- Textfeld: leer geblieben.
- Begründung: Der englische Eventrückblick enthält echte eIDAS-/Trust-Service-Anker und nennt qualifizierte Signaturen, Zeitstempel und Siegel. Inhaltlich geht es aber um eIDAS-2-Evolution, laufende Zertifizierung, QTSP-Geschäftsmodelle, Wallet-Chancen und Skalierung zwischen Mitgliedstaaten. Es fehlt jeder konkrete Bezug zu eingehenden signierten PDFs, Zertifikatsauswertung in einem Dokumentenworkflow, Records/Archiv/Freigabe, Audit-Trail/ECM oder BIV. Der Originalpost adressiert damit die Trust-Service-Branche, nicht den engen operativen Kampagnen-ICP; ein Kommentar mit DocVal-/Records-Brücke wäre künstlich.

Vollständiger Originalpost aus `note:`:

```text
Feed post

Procivis • Securing Digital Trust

 

23h • 

That's a wrap on the 12th Trust Services and eID Forum and CA-Day in Tallinn, organized by European Union Agency for Cybersecurity (ENISA). Two full days. A few things we're taking home:

Axel Rimkus joined the closing panel on the future of trust services alongside Nimbus Technologieberatung GmbH, TÜV TRUST IT | AT, Intesi Group, Namirial and Asseco, and set out a useful framing: eIDAS 2 is an evolution of eIDAS 1. Qualified signatures, timestamps and seals stay, and the EUDI Wallet adds a new layer of trust services around them.

What we heard from the room:

Timing. Several conformity assessment bodies admitted that certification work is still in progress, and the December deadline is getting tougher by the day. 

The business case. QTSPs are still asking where they fit when governments run the wallet and it's free for citizens. That perception is shifting, and the new trust services around the wallet are where the opportunities will come from.

Scale. Whether 27 Member States should each build the same thing came up repeatedly, and nobody has a final answer yet.

Ivan Marin and Jiri Zmelik represented Procivis in Tallinn across both days. Thank you to ENISA and everyone who contributed to the discussions.

#eIDAS2 #ProcivisOne #DigitalIdentity
… more

Désirée Heutschi and 14 others reacted
Désirée Heutschi and 14 others

Like
Comment
Repost
Send
```

## Folgeworkflow

- Behalten: `0`.
- Verworfen: `2`.
- Kein Kandidat an `content_strategist`, `copywriter`, `style_evaluator` oder `reviewer` übergeben: Keiner erfüllt die ausdrücklich verlangte Schwelle „wirklich passend“.
- Deshalb keine finalen Kommentartexte, keine Style-Scores und keine Reviewer-Urteile.
- Die beiden leeren, ungekreuzten Neufundblöcke wurden erst nach vollständiger Rohsicherung entfernt. Bestehende Jobs und fremde/parallele Änderungen blieben erhalten.
- Nichts veröffentlicht, freigegeben, angekreuzt, eingeplant oder nach `schedule.md` verschoben; kein Operator- oder `run-due`-Aufruf.

