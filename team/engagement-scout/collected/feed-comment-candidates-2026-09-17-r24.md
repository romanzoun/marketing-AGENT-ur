# Feed-Kommentarkandidaten — 2026-09-17 — R24

## Lauf

- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Exakter Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Versuch: fehlgeschlagen vor Sammlung (`EPERM ::1:9222`, Sandbox-Zugriff auf lokalen Chrome-CDP-Port); keine Queue-Änderung aus diesem Versuch.
- Wiederholung desselben Befehls mit freigegebenem lokalen CDP-Zugriff: erfolgreich; CLI meldete `2 Beitrag/Beiträge gesammelt (new-feed)` und `kandidaten: 2`.
- Persistenzkontrolle: Tatsächlich entstand genau ein neuer Approval-Block, `comment-2026-09-17-0003`. Ein zweiter belastbarer ID-/URL-/Note-Block ist nicht vorhanden; wegen der bekannten ID-Kollisionslogik wird nichts rekonstruiert oder erfunden.
- Queue-Zieldatei nach Lauf: `Kampagnen/document validator/queue/approvals.md`

## Tatsächlich persistierter Kandidat

### comment-2026-09-17-0003

- URL unverändert: `https://lnkd.in/p/eGJ3RzDT`
- Autor unverändert: `eID Easy`
- URN: im erzeugten Queue-Block nicht vorhanden; keine URN erfunden.
- Zielsprache: Englisch.
- Vorläufiges Scout-Urteil: **PASSEND**.
- Begründung: Der Originalpost behandelt EUDI Wallets, Relying-Party-Registrierung, Zweck und Empfänger von Kundendaten, Anzeige gegenüber Nutzern sowie die Rolle und Grenzen eines Intermediärs. Das passt direkt zu den Kampagnenthemen digitale Identität, verifizierbare Rollen/Berechtigungen, Compliance und Vertrauen. Der Kommentar darf daraus keinen PDF-, Archiv-, Hash-, ZertES-, Document-Validator- oder BIV-Produktbezug erfinden; sinnvoll ist eine persönliche Perspektive auf den Prüfpunkt vor der Integration: Wer fragt mit welchem Zweck und welcher Berechtigung welche Daten ab?
- Banned topics: keine Politik/Religion, kein Konkurrenten-Bashing, keine Rechtsgarantie. Event-/Registrierungscharakter ist zulässig, solange der Kommentar konkret auf die fachlichen Fragen antwortet und keine Werbung konstruiert.

### Unabhängige Strategieprüfung und Endentscheidung

- Content-Strategist-Bericht: `team/content-strategist/collected/comment-candidates-2026-09-17-r24.md`
- Content-Strategist-Urteil: **BEDINGT**, Zielsprache Englisch.
- Bestätigter Teilfit: EUDI Wallet, Relying-Party-Registrierung, Datenzweck, Intermediärsgrenzen und verifizierbare Berechtigung.
- Fehlender enger Anschluss: keine Records-/PDF-Prüf-/Archiv-/Audit-Situation und kein belegter DocVal-/BIV-Produktanschluss; es handelt sich primär um eine Eventankündigung.
- Scout-Endentscheidung unter der Vorgabe „nur wirklich passende Kandidaten“: **VERWORFEN**. Ein Kommentar samt Pflichtbezug `#RecordsManagement` wäre aufgesetzt; es wird keine Kampagnenbrücke und kein Kommentar erzwungen.
- Der weiterhin leere, ungekreuzte Approval-Block wurde nach vollständiger Rohsicherung entfernt. Es gab keinen Kommentartext, keine Evaluation und keine Nutzerfreigabe.

Vollständiger Originalpost aus `note:`:

```text
Feed post

eID Easy

3h • 

“Can we just integrate the wallet?”
Well… yes.
But also: not quite.

With EUDIW, the interesting questions often come before the integration:

• Who is asking for the customer’s data?
• Why do they need it?
• Where are they registered?
• What does the wallet show the user?
• And what can an intermediary (like eID Easy) actually handle?

In Explained by eID Easy S01E03, John Jolliffe, our Provider Relationships Manager, and Andrea Feliziani, our Chief Compliance Officer, will walk through the practical side of relying party registration and intermediaries.

Link to register in the comments.

Format: 30-minute live session | 15-minute live Q&A

See you on September 30, 11:00 CEST. 
Bring your questions (Q&A open to Community Members only)
… more

Explained by eID Easy S01E03

·

2 pages

Richard Oliphant and 9 others reacted
Richard Oliphant and 9 others

1 comment
1 comment

•

4 reposts
4 reposts

Like
Comment
Repost
Send
```

## Nicht belastbar persistierter CLI-Treffer

- Die CLI-Zahl `2` steht nur einem neuen Queue-Block gegenüber.
- Ohne einen unveränderten ID-/URL-/Note-Block kann der zweite Treffer weder semantisch geprüft noch an Textagenten übergeben werden.
- Entscheidung: **VERWORFEN / NICHT REKONSTRUIERT**, rein aus Prozess- und Datenintegritätsgründen; kein unbekannter Originalpost wird bewertet.

## Sicherheitsstatus

- Keine Checkbox angekreuzt.
- Keine Nutzerfreigabe erteilt.
- Nichts geplant oder veröffentlicht.
- Kein Operator gestartet.
