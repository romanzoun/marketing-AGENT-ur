# Reshare-Kandidaten — 2026-09-30 — R2

## Lauf und Abgrenzung

- Auftrag: `ES-FR-DV-20260930-R2`
- Befehl: `./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-reshares --limit 2`
- Erster Sandbox-Versuch: vor LinkedIn-Zugriff mit lokalem CDP-`EPERM` beendet; Queue blieb byteidentisch.
- Unveränderter Wiederholungsaufruf mit lokalem Browserzugriff: `ok: true`, `kandidaten: 2`; Browser-Vorauswahl `2 Beitrag/Beiträge gesammelt (new-feed)`.
- Baseline `approvals.md`: SHA-256 `c817407dde4132588ec9aebb75a179491b8916310d53e95a685194154d573958`.
- Unmittelbar nach Suchlauf: SHA-256 `85256b29ffe6b168f8a9510372d5b3e5597897c0df3daf8bd2840973dcf66ff1`.
- Neu erzeugt: `reshare-2026-09-30-0001`, `reshare-2026-09-30-0002`.
- In beiden Blöcken ist kein URN-Feld vorhanden; keine URN wird ergänzt oder erfunden.
- Außer den beiden neuen Blöcken formatierte der CLI-Schreibvorgang im unmittelbar vorhergehenden Kommentarblock eine bestehende mehrzeilige `fit_note` semantisch unverändert um. Diese fremde Änderung wird nicht zurückgesetzt.

## reshare-2026-09-30-0001

- ID: `reshare-2026-09-30-0001`
- Autor: `EU Digital Identity Wallet`
- URL-Feld, exakt und unverändert:

```text
Freigabe, s.u. durch Isa/ Monika.
 
Bitte jeder selbständig den Flug im Intranet buchen (2 Steps):
1. Antrag Flugreise
Alles abfüllen und Email als Freigabe anhängen
Danach warten, bis Monika "OK" setzt
2. TravelMe (parallel)
Vorab Flug suchen und dann ebenso abfüllen
Hotel entweder ebenso hier oder eure präferierte Platform
Hotelsituation:
Kurt hat rechtzeitig gebucht im Q! (scheint ausgebucht zu sein, aber vllt. Hat ja jemand Glück)
Lindner ist eine Option
Ich habe noch gegenüber vom Q! – Media Hotel eine Option gefunden (ich reise am Mo Abend an und am Donnerstag ab, ergo 3 Nächte)
Grundsätzlich scheint es, dass es schwierig wird, alle in einem Hotel zu buchen.
Darum:
Bitte in/ um/ am K'damm prüfen entlang zu prüfen, entlang dem Bild 😉
Bild
Von dort ist es nur 1-2 S Bahn Stationen
 
```

- Technischer Befund: Das `url:`-Feld ist kein LinkedIn-Permalink, sondern ein sachfremder interner Reise-/Hoteltext. Es bleibt unverändert; es wird weder rekonstruiert noch als URL ausgegeben.
- Vollständiger Originalpost aus `note:`:

```text
Feed post

EU Digital Identity Wallet

18h • 

Launchpad 2026 is now exactly one month away! 🚀
 
On 29–30 October, the EUDI Wallets community gathers in Brussels, ready to Work it, Show it, Share it. 🚀 
 
Across two packed days, participants will test wallets, join hands-on workshops, hear inspiring keynotes and panels, see national wallet demos, and network with the wider EUDI ecosystem. 
 
Want to join? Here’s the good news: registrations are still open, but spaces are filling up fast!

👉 Register now: https://lnkd.in/ey7Nk8rN
… more

Joerg Lenz and 21 others reacted
Joerg Lenz and 21 others

1 repost
1 repost

Like
Comment
Repost
Send
```

## reshare-2026-09-30-0002

- ID: `reshare-2026-09-30-0002`
- Autor: `Realize`
- URL, exakt und unverändert: `https://lnkd.in/p/eZb9TZdV`
- Vollständiger Originalpost aus `note:`:

```text
Feed post

Realize

5,719 followers

Promoted

Follow

Deine Konkurrenz fischt immer noch im selben überfüllten Teich. Es ist Zeit, sie abzuhängen. 

Echtes inkrementelles Wachstum erfordert absolute Transparenz. Realize+ löst deine Abhängigkeit von den Walled Gardens und gibt dir mit der ersten agentenbasierten Werbeplattform die Kontrolle über deine Ads zurück. Keine Voreingenommenheit zugunsten eigener Lösungen, keine versteckten Kennzahlen – nur autonome Optimierung, die zu 100 % von deinen Ergebnissen bestimmt und auf die spezifischen Anforderungen deines Unternehmens zugeschnitten ist
… more

Show translation

Realize: Performance über Search & Social hinaus

Learn more

13 reactions
13

2 comments
2 comments

•

1 repost
1 repost

Like
Comment
Repost
Send
```

## Schutzgrenzen

- Nur diese zwei neuen Reshare-Blöcke dürfen im Prüfablauf bearbeitet werden.
- IDs, vorhandene URL-Werte, Autoren und vollständige Notes bleiben unverändert.
- Keine Checkbox ankreuzen, keine Freigabe setzen, nichts planen, verschieben oder veröffentlichen.
- `schedule.md`-Baseline: `7740777329c3eea295e99cdc4b9fc898af31da802226b210061a470cf3c90c75`.
- `log.md`-Baseline: `eebd33040ddca17ace7d8487182c9ace31ef22fa3cd5873284fe5fa670c3afce`.
