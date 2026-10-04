# ES-CONN-DV-20260923-R2 — LinkedIn-Personensuche

## Auftrag und Grenzen

- Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`
- Genau ein Personensuchlauf, Limit 2.
- Keine Vernetzungsanfrage senden, nichts freigeben, planen oder veroeffentlichen.
- Neue Kandidaten in `approvals.md` behalten, anhand des gespeicherten Profiltexts bewerten und nur bei belegbarer Passung texten und pruefen.

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

Die Kampagne nennt als Buyer/Champion insbesondere Teamleads Records/ECM und Compliance Leads; der Branchenfokus liegt auf regulierten Schweizer Organisationen. Fuer den genau einen Lauf wurde deshalb diese einzelne konkrete Champion-Suche gewaehlt:

`Teamlead Records Management ECM Compliance Schweiz`

## Exakter einmaliger Befehl und Ausgang

```text
$ ./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-connections --query "Teamlead Records Management ECM Compliance Schweiz" --limit 2
14:47:19 | INFO    | browser.linkedin       | Verbinde mit Chrome via CDP: http://localhost:9222
{
  "ok": true,
  "kandidaten": 0,
  "query": "Teamlead Records Management ECM Compliance Schweiz",
  "file": "Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md"
}
```

Exit-Code: `0`. Es wurde kein zweiter, alternativer oder Retry-Suchlauf ausgefuehrt.

## Kandidaten, Bewertung und Folgepruefungen

- Gefundene/neue Kandidaten: `0` / `0`.
- Daher keine neuen IDs, URNs, URLs oder gespeicherten Profiltexte vorhanden.
- Daher keine belastbare Grundlage fuer `fit_score`, `fit_note` oder `text`; die Kandidatenliste ist leer und damit bereits absteigend sortiert.
- Copywriter nicht gestartet: kein passender Kandidat und kein Profiltext.
- Style-Evaluator nicht gestartet: keine neue Vernetzungsnotiz zu pruefen.
- Reviewer nicht gestartet: keine neue Vernetzungsnotiz und kein neuer Kandidat zu pruefen.

## Queue-Verifikation

- Vor dem Lauf: SHA-256 `b5dfe151235e93aa540a4c2ca3001e1c829c02735b871083dd4cf4be9a47779c`.
- Nach dem Lauf: SHA-256 `b7e168522930dff964c8df1b12d97f4987c7c1ea217a18eff52c8c4f8b31eae4`.
- Der Diff enthaelt ausschliesslich die vom CLI normalisierte Hinweiszeile am Dateikopf (`Danach li-jobs schedule ...`); es wurde kein Connection-Block angelegt, veraendert oder entfernt.
- Alle vorhandenen Checkboxen blieben leer; bestehende fremde Inhalte und Aenderungen wurden nicht zurueckgesetzt.

## Ergebnis und Sicherheitsbestaetigung

Der exakt einmalige Suchlauf war technisch erfolgreich, lieferte aber keine Kandidaten. Es wurde nichts veroeffentlicht, keine Vernetzungsanfrage gesendet, nichts geplant und keine Freigabe gesetzt. Es wurde kein Operator-, Schedule-, Run-Due-, Send- oder Publish-Befehl ausgefuehrt.
