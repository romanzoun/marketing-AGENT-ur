# Feed-Kommentarkandidaten — 2026-09-13 — R12

## Lauf

- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Exakter Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Erster Sandbox-Versuch: wegen `EPERM ::1:9222` ohne Queue-Änderung abgebrochen.
- Erfolgreiche Wiederholung mit lokalem Chrome-CDP-Zugriff: zwei Feedposts gesammelt. Die CLI meldete `kandidaten: 1`; der Vorher/Nachher-Abgleich der Queue belegt zwei tatsächlich neu persistierte Blöcke (`0005`, `0006`).
- Queue: `Kampagnen/document validator/queue/approvals.md`

## Tatsächlich neue Kandidaten

### `comment-2026-09-13-0005`

- LinkedIn-ID des Feedpost-DOM-Eintrags: vom Werkzeug nicht exponiert
- URN: vom Werkzeug nicht exponiert; nicht erfunden oder abgeleitet
- URL: `https://lnkd.in/p/ekbPXqmf`
- Autor: `Followed by Petar Chardakov`
- `source_job_id`: `job-0003`
- Zielsprache: Englisch
- Ausgangszustand `text:`: leer
- Relevanzindikatoren: eIDAS 2.0, EU Digital Identity Wallet, PID als Identitätsschicht, grenzüberschreitende Attributprüfung, kontrollierte Offenlegung.
- Vollständige unveränderte `note:` und alle Metadaten stehen im Queue-Block dieser ID.

### `comment-2026-09-13-0006`

- LinkedIn-ID des Feedpost-DOM-Eintrags: vom Werkzeug nicht exponiert
- URN: vom Werkzeug nicht exponiert; nicht erfunden oder abgeleitet
- URL: `https://lnkd.in/p/eNKteCgy`
- Autor: `Enclave`
- `source_job_id`: `job-0003`
- Zielsprache: Englisch
- Ausgangszustand `text:`: leer
- Relevanzindikatoren: eIDAS, EU Digital Identity Wallet, Akzeptanzpflichten, starke Authentisierung, souveräne Identitätsschicht.
- Vollständige unveränderte `note:` und alle Metadaten stehen im Queue-Block dieser ID.

## Schutzgrenzen

- IDs, URLs, Autoren, `note:`, `source_job_id`, Metadaten und Checkboxen unverändert lassen.
- Copywriter darf ausschließlich die beiden leeren `text:`-Felder befüllen.
- Keine Freigabe, keine Planung/Verschiebung, keine Operator-Aktion und keine Veröffentlichung.
alidator/queue/approvals.md`.
- Ausgangszustand des `text:`-Felds: leer.

## Schutzgrenzen

- IDs, URLs, Autoren, `note:`, `source_job_id` und Checkboxen bleiben unverändert.
- Ausschließlich die leeren `text:`-Felder dürfen vom Copywriter befüllt werden.
- Keine Freigabe, keine Planung/Verschiebung, keine Operator-Aktion und keine Veröffentlichung.
