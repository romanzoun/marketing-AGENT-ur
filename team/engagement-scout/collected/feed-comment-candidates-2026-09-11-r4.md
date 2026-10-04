# Feed-Kommentarkandidaten — 2026-09-11 — R4

## Sammellauf

- Befehl: `./bin/li-jobs --campaign "Kampagnen/document validator/kampagne.yaml" find-comments --limit 2`
- Ergebnis des erfolgreichen Laufs: `ok: true`, `kandidaten: 2`, Zieldatei `Kampagnen/document validator/queue/approvals.md`
- Der erste Sandbox-Versuch endete vor der Sammlung mit `EPERM` am lokalen Chrome-CDP-Port; der identische berechtigte Wiederholungslauf war erfolgreich.

## Tatsächlich neu persistierter Queue-Eintrag

- Job-ID: `comment-2026-09-11-0006`
- Source-Job-ID: `job-0003`
- URL: `https://lnkd.in/p/e_PvJmYJ`
- Autor-Feld: `Alex Rada commented`
- Ausgangszustand: `text: ''`, `- [ ] freigeben`, keine Evaluation, keine Planung
- Zielpost-Sprache: Englisch
- Zielpost-Kontext: Charly Wargnier postet „trillion dollar company btw“; das sichtbare Profil nennt LLMs, AI agents und Data Science, Alex Radas sichtbarer Kommentar fragt nach dem Hintergrund.

## Integritätsbefund

Vor dem Lauf enthielt die Queue vier Kommentar-IDs (`0001`, `0002`, `0005`, `0004`). Der Generator `next_id` zählt Einträge statt die höchste Nummer zu bestimmen. Deshalb erhielt der erste der zwei intern gefundenen Beiträge erneut die bereits vorhandene ID `comment-2026-09-11-0005` und wurde beim anschliessenden ID-Deduplizieren nicht persistiert; nur der zweite Beitrag blieb als `0006` erhalten. Der CLI-Ergebniswert `kandidaten: 2` zählt die interne Liste vor dieser Deduplizierung. Für den verlorenen ersten Treffer lagen nach dem Befehl weder URL noch Note im Queue-Artefakt vor; er wird nicht geraten oder rekonstruiert.

IDs, URL und Queue-Felder des tatsächlich persistierten Kandidaten wurden unverändert übernommen. Es wurde nichts angekreuzt, freigegeben, geplant, verschoben oder veröffentlicht.
