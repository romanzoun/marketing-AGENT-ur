# Feed-Kommentarkandidaten — 2026-09-22 — R38

## Lauf

- Befehl: `./bin/li-jobs --campaign "Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml" find-comments --limit 3`
- Erster Sandboxlauf: technisch vor Browserzugriff mit `EPERM ::1:9222` abgebrochen.
- Identischer Wiederholungslauf mit lokalem Chrome-CDP-Zugriff: `ok: true`, `kandidaten: 3`.
- Zielqueue: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/queue/approvals.md`
- Keine separate URN wurde vom Werkzeug ausgegeben; keine URN wurde ergänzt oder erfunden.

## Neue Kandidaten, absteigend nach Fit

### comment-2026-09-22-0001

- URL: `https://lnkd.in/p/ex2-tp5U`
- Autorin: Martina Knierim
- fit_score: `0.34`
- Status: bedingt passend, nicht durch `banned_topics` gesperrt
- fit_note: Digitale Identität, Trusted Lists, Trust Registries, grenzüberschreitendes Vertrauen und Nutzbarkeit treffen Kampagnenthemen. Der Originalpost behandelt jedoch Wallet-Infrastruktur und Standards, nicht signierte PDFs, Archivierung/Freigabe, Records/ECM, Audit-Trail oder BIV; deshalb ist nur eine enge, nicht werbliche Vertrauensperspektive zulässig.
- Vollständiger Originalpost: unverändert im `note:`-Feld des Queue-Eintrags gespeichert.

### comment-2026-09-22-0002

- URL: `https://lnkd.in/p/ey7Hz7CY`
- Autor: Lombard Odier Group
- fit_score: `0.01`
- Status: gesperrt
- fit_note: Beworbene Investment-Eventankündigung zu Geopolitik, Inflation und allgemeiner KI-Innovation; ausdrückliches Politik-No-Go und beliebige KI-News ohne Kernthema-Verbindung. Kein Bezug zu signierten PDFs, Archivierung/Freigabe, Records/ECM, Signaturprüfung oder BIV.
- Vollständiger Originalpost: unverändert im `note:`-Feld des Queue-Eintrags gespeichert.

### comment-2026-09-22-0003

- URL: `https://lnkd.in/p/edQ7QFFz`
- Autor: Andrea Frosinini
- fit_score: `0.0`
- Status: gesperrt
- fit_note: Stablecoin-, Zahlungsverkehrs- und Welthandelsreport ohne konkreten Bezug zur Prüfung signierter PDFs, Archivierung/Freigabe, Records/ECM, digitaler Signatur, Identität hinter einer Signatur oder BIV; generische Digitalisierung ohne Kernthema-Verbindung. Banking-/Compliance-Nähe allein reicht nicht.
- Vollständiger Originalpost: unverändert im `note:`-Feld des Queue-Eintrags gespeichert.

## Unveränderlichkeits- und Sicherheitsgrenzen

- IDs und URLs wurden exakt aus der Queue übernommen.
- Alle drei technisch belastbaren Kandidaten bleiben sichtbar und ungekreuzt in `approvals.md`.
- Für gesperrte Kandidaten bleibt `text: ''`.
- Keine Freigabe, keine Planung, keine Verschiebung nach `schedule.md`, keine Veröffentlichung.
