# ES-CONN-DV-20260923-R1 — LinkedIn-Personensuche

## Auftrag und Grenzen

- Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`
- Genau ein Personensuchlauf, Limit 2.
- Keine Vernetzungsanfrage senden, nichts freigeben, planen oder veroeffentlichen.
- Neue Kandidaten sichtbar in `approvals.md` behalten, semantisch bewerten und nur bei belegbarer Passung texten/pruefen.

## Gelesene Quellen

- `AGENTS.md`
- `.codex/agents/engagement-scout.toml`
- `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`
- `config/personal_profile.yaml`
- `team/style/profile.md`
- `team/style/learning.json`
- `team/board.md`
- `team/engagement-scout/inbox.md`
- `team/engagement-scout/todo.md`
- `team/engagement-scout/memory.md`
- Ausgangszustand von `Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md`

## Herleitung und Suchquery

Die Kampagne nennt als Buyer/Champion insbesondere Teamleads Records/ECM und als Branchenfokus Banking, Versicherungen, Verwaltung und Grossunternehmen. Fuer den genau einen Lauf wurde deshalb eine einzelne, eng gefasste Champion-Suche gewaehlt:

`Head of Records Management ECM Banking Schweiz`

## Exakter einmaliger Befehl und Ausgang

```text
$ ./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-connections --query "Head of Records Management ECM Banking Schweiz" --limit 2
12:07:54 | INFO    | browser.linkedin       | Verbinde mit Chrome via CDP: http://localhost:9222
{
  "ok": true,
  "kandidaten": 0,
  "query": "Head of Records Management ECM Banking Schweiz",
  "file": "Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md"
}
```

Exit-Code: `0`. Es wurde kein zweiter, alternativer oder Retry-Suchlauf ausgefuehrt.

## Kandidaten und Folgepruefungen

- Neue Kandidaten: `0`.
- Daher keine gespeicherten neuen Profiltexte, IDs, URLs oder URNs vorhanden.
- Daher keine belastbare Grundlage fuer `fit_score`, `fit_note` oder eine individuelle Notiz.
- Copywriter nicht gestartet: kein geeigneter Kandidat und kein Profiltext.
- Style-Evaluator nicht gestartet: keine neue Notiz zu pruefen.
- Reviewer nicht gestartet: keine neue Notiz und kein neuer Kandidat zu pruefen.

## Verifikation

- `approvals.md` enthaelt nach dem Lauf keinen `connection`-Block.
- Damit sind alle neuen Kandidaten vorhanden (leere Menge); Sortierung und 300-Zeichen-Regel sind vacuous erfuellt.
- Es wurde keine Checkbox gesetzt und kein Approval-, Schedule-, Run-Due-, Send- oder Publish-Befehl ausgefuehrt.
- Fuer diese Kampagne existierten beim Baseline-Check keine `schedule.md`- oder `log.md`-Dateien; der Suchlauf hat keine angelegt.
- Baseline-SHA-256 von `approvals.md`: `e7769dd0425c815ac676aca7f0147086ac89ec7f377514205996fb8170a863db`.
- Nach dem Suchlauf: `352136b57e5db6f5ba24730a8247049f2e49d864ff7e0585b3b03454e5b80675`.
- Die Differenz stammt ausschliesslich aus parallelen, fremden `fit_score`-/`fit_note`-Ergaenzungen an zwei bestehenden Kommentar-Kandidaten; diese wurden respektiert und nicht rueckgaengig gemacht. Es gibt keine neue Connection-Differenz.

## Ergebnis

Der exakt einmalige Suchlauf war technisch erfolgreich, lieferte aber keine neuen Kandidaten. Keine externe Aktion wurde ausgeloest.
