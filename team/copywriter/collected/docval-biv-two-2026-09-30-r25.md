# CW-DV-NP-20260930-R25 — finale Posttexte

## POST 1 — Technisch nicht geprüft ist nicht ungültig

```text
Wenn die Gepäckwaage streikt, wiegt mein Koffer nicht plötzlich null Kilo.

Er ist auch nicht automatisch zu schwer. Ich habe schlicht kein Messergebnis.

Genau diese unspektakuläre dritte Spur ist mir in automatisierten Prüfprozessen wichtig: technisch nicht geprüft.

Denn «technisch nicht geprüft» ist nicht dasselbe wie «Signatur ungültig». Wer beides in dasselbe rote Feld kippt, macht aus einem Messproblem eine fachliche Aussage. Praktisch, kompakt – und leider falsch etikettiert.

Der Swisscom Document Validator liefert Signatur- und Zertifikatsinformationen. Wie der eigene Workflow einen technisch unterbrochenen Prüfschritt sichtbar macht und welchen nächsten Schritt er vorsieht, gehört in die Prozesslogik von Records/ECM und Compliance Operations.

Ich mag solche dritten Zustände. Sie wirken wenig glamourös, verhindern aber, dass Rot so tut, als hätte wirklich jemand gewogen.

Unterscheidet euer Workflow sauber zwischen «technisch nicht geprüft» und «ungültig»?
```

- Unicode-Codepoints: `981`
- SHA-256 (reiner Text): `d1b88d59654de555f2cffe38fcd3eebf4b0f42f018cdd1e16d08ed425232397e`

## POST 2 — Das PDF bleibt geschützt, die Ergebnisse brauchen trotzdem eine Zwecklogik

```text
Mein Koffer bleibt im Schliessfach. Sein Namensetikett hänge ich trotzdem nicht ans schwarze Brett.

Das ist für mich die zweite Hälfte einer guten Datenschutzfrage.

Beim Swisscom Document Validator bleibt die PDF in der eigenen Umgebung; für die Validierung wird ihr Hash verwendet. Das ist wichtig. Danach arbeitet der Prüfprozess aber weiterhin mit Informationen: Der Document Validator liefert Signatur- und Zertifikatsinformationen. Der Business Identity Validator kann Kontext zu Zeichner, Unternehmen und verfügbaren Berechtigungsinformationen ergänzen.

Und dann wird es sehr praktisch:

Wer braucht welche Signatur-, Zertifikats-, Identitäts-, Unternehmens- oder verfügbare Berechtigungsinformation für die Prüfung?

Wer braucht was für einen Klärfall oder eine Entscheidung?

Nicht jede Rolle braucht automatisch die ganze Auslage. Die Sichtbarkeit sollte zum Zweck des jeweiligen Prozessschritts passen – auch wenn das PDF selbst in der eigenen Umgebung bleibt.

Datenschutz endet für mich also nicht an der Schliessfachtür. Dort wechselt nur die Frage: vom Dokument zum Ergebnis.

Ist in eurem Prüfprozess geregelt, wer welches Ergebnis sehen muss – und wofür?
```

- Unicode-Codepoints: `1173`
- SHA-256 (reiner Text): `d75b05db13c525563b8301fb36f55984fe48a9be77145fc25f4723858e6e1016`

## Prüfung

- Exakt zwei deutsche LinkedIn-Posttexte; keine Hashtags und kein Produktlink.
- Post 1 trennt einen technisch nicht zustande gekommenen Prüfschritt ausdrücklich von einer ungültigen Signatur. Es enthält keine Ausfallquote, keine konkrete Produktfehlerbehauptung und keinen Produktstatuscode.
- Post 2 behandelt ausschließlich die nachgelagerte Sichtbarkeits- und Zwecklogik der verfügbaren Prüf- und Kontextinformationen. Es enthält keine Aussage zu Speicherung, Aufbewahrungsdauer oder Produktzugriffsrollen und keine BIV-Garantie.
- Keine exakte Textdublette zu den zwölf aktuellen Queue-Posts. Funktional eigenständig gegenüber Klärdatensatz, allgemeiner Statussemantik, Datenweg, Unternehmens-/Rollenkontext und fehlender Berechtigungsinformation: Post 1 behandelt Messausfall versus fachliches Ergebnis; Post 2 die zweckgebundene Sichtbarkeit der nachgelagerten Ergebnisarten.
- Keine Queue-, Freigabe-, Planungs-, Bild- oder Veröffentlichungsaktion.
