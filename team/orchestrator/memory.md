# Gedächtnis — orchestrator

## Rolle
Koordiniere, führe selten selbst aus. Delegiere präzise (Ziel, Kontext, Format, Grenzen).

## Gelernte Muster
- Wiederkehrende UI-Jobs nutzen einen gemeinsamen `li-scheduler`-Cron-Takt;
  ausgeführt werden ausschließlich aktive und fällige Job-Definitionen.
- Eine Freigabe in der UI ist zugleich die Einplanung: expliziter Termin oder
  nächster freier Kampagnen-Slot.
- `li-brain` verwendet ausschließlich `codex exec` mit Workspace-Sandbox und
  den Projektrollen aus `.codex/agents/`; ein Git-Repository ist nicht nötig.
- Der passive UI-Status sendet keine KI-Anfrage; nur der explizite Health-Button
  prüft Modell-/Kontingentzugriff mit einer minimalen, schreibgeschützten Anfrage.
- Ein Entwurfsjob ist nur erfolgreich, wenn die verlangten neuen Post-Einträge
  tatsächlich in der Freigabe-Queue gefunden werden.

## Do / Don't
- Do: erst sammeln lassen, dann planen.
- Don't: live posten ohne Freigabe.
