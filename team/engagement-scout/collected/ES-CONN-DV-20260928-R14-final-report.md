# ES-CONN-DV-20260928-R14 — Abschlussbericht

Datum: 2026-09-28  
Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`

## Abgeleitete Personensuche

Query: `Leiter Vertragsmanagement Versicherungen Schweiz`

Herleitung: Die Kampagne nennt Vertragsadministration ausdrücklich in `audience` und als operative User-Persona. Versicherungen sind eine ausdrücklich genannte Zielbranche mit Audit-, Compliance- und Datenschutzanforderungen. Die Suche verbindet damit eine konkrete Rolle mit einer konkreten ICP-Branche.

## Exakter Suchlauf

Genau ein Aufruf wurde ausgeführt:

```text
./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-connections --query "Leiter Vertragsmanagement Versicherungen Schweiz" --limit 2
```

Ergebnis: Exit-Code `1`. Der Lauf scheiterte vor dem Laden der LinkedIn-Personensuche beim CDP-Verbindungsaufbau:

```text
11:27:09 | INFO    | browser.linkedin | Verbinde mit Chrome via CDP: http://localhost:9222
playwright._impl._errors.Error: BrowserType.connect_over_cdp: connect EPERM ::1:9222 - Local (:::0)
Call log:
  - <ws preparing> retrieving websocket url from http://localhost:9222
```

Auftragsgemäß wurde kein zweiter Lauf zur Wiederholung, Korrektur oder Ergänzung ausgeführt.

## Neue Kandidaten

Keine. Da die Personensuche nicht geladen wurde, existieren keine vom Werkzeug gespeicherten Profiltexte, IDs, URNs oder URLs. Ohne Profiltext sind weder Rollen-/Zielgruppenpassung noch `fit_score`, `fit_note` oder eine individuelle Vernetzungsnotiz belegbar. Es wurde nichts rekonstruiert oder erfunden. Die verlangte absteigende Sortierung ist für die leere Kandidatenmenge trivial erfüllt.

## Copywriter-, Stil- und Reviewer-Prüfung

Entfallen: Es gibt keinen neuen Kandidaten und keinen Text. Deshalb wurde kein leerer oder spekulativer Auftrag an `copywriter`, `style_evaluator`, `reviewer` oder `content_strategist` erzeugt. Zu prüfende Vernetzungsnotizen: `0`.

## Queue- und Aktionsverifikation

- `approvals.md` vor dem Suchlauf: SHA-256 `c18479f500861a218300e958de348a95656875a5d4efc2b1ce0ce213859a61fa`
- `approvals.md` nach dem Suchlauf: SHA-256 `c18479f500861a218300e958de348a95656875a5d4efc2b1ce0ce213859a61fa`
- Neue `CONNECTION`-/`connection-`-Blöcke: `0`
- `schedule.md` Abschluss-SHA-256: `c305e0babd6b00fe6232bd483016dff95d036bf64a31996467bb4c21b26b16ac`
- `log.md` Abschluss-SHA-256: `eebd33040ddca17ace7d8487182c9ace31ef22fa3cd5873284fe5fa670c3afce`
- Keine Vernetzungsanfrage gesendet.
- Nichts veröffentlicht.
- Nichts eingeplant.
- Keine Freigabe gesetzt und keine Checkbox angekreuzt.
- Bestehende Queue-Inhalte und fremde Änderungen wurden nicht überschrieben.

## Geänderte Dateien

- `team/engagement-scout/inbox.md`: R14-Auftrag protokolliert und abgeschlossen.
- `team/engagement-scout/todo.md`: R14-Arbeitspunkt protokolliert und abgeschlossen.
- `team/board.md`: Start und Abschluss des R14-Laufs protokolliert.
- `team/engagement-scout/collected/ES-CONN-DV-20260928-R14-final-report.md`: dieser datierte Abschlussbericht.

Unverändert durch diesen Lauf: Kampagnendatei, persönliches Profil, Stilprofil, Lernstand, Scout-Memory, Scout-Outbox sowie `approvals.md`, `schedule.md` und `log.md`.
