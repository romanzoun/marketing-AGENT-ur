# Reviewer-Prüfung — RV-FC-DV-20260921-R37

Datum: 2026-09-21  
Kampagne: `Kampagnen/docval-biv-vor-archiv-vor-freigabe/kampagne.yaml`  
Prüfumfang: einmalige Abschlussprüfung ausschließlich der Queue-Kandidaten `comment-2026-09-21-0001` und `comment-2026-09-21-0002`

## Geprüfter Queue-Zustand

- `approvals.md` enthält genau zwei YAML-Blöcke, in dieser Reihenfolge: `comment-2026-09-21-0001`, danach `comment-2026-09-21-0002`.
- Beide Einträge sind vom Typ `comment`, vollständig sichtbar und ungekreuzt; es gibt **2** leere Freigabe-Checkboxen und **0** gesetzte.
- Die `fit_score`-Werte sind `0.02` und `0.01` und damit korrekt absteigend sortiert.
- Beide `text:`-Werte sind exakt leer: jeweils **0 Unicode-Codepoints**. `generated_text`, `evaluation_score`, `evaluation_note`, `evaluated_at`, `publish_at`, `published_at` und `published_url` sind ebenfalls leer beziehungsweise `null`.
- Queue-SHA-256 zum Prüfzeitpunkt: `ab2bfcea14dd5b79b64fa9c044780f1b68839b9c7f71c95770de9c564fada51f`.
- Im Kampagnenordner existieren keine `schedule.md`- oder `log.md`-Dateien; keiner der beiden Kandidaten ist geplant oder protokolliert veröffentlicht.

## Deterministische Vorprüfung

Die Kampagne definiert `max_comment_chars: 500` und `required_hashtags: []`.

- `comment-2026-09-21-0001`: **0 / 500** Codepoints; keine Pflicht-Hashtags gefordert.
- `comment-2026-09-21-0002`: **0 / 500** Codepoints; keine Pflicht-Hashtags gefordert.

Das Zeichenlimit und die leere Pflicht-Hashtag-Liste erzeugen bei einem leeren Feld keinen formalen Verstoß. Sie machen daraus jedoch keinen freigabefähigen Entwurf: Es liegt bewusst kein Kommentartext vor. CTA, Stimme, Textfakten und Spam sind daher auf Textebene nicht anwendbar; eine Style-Evaluator-Runde wäre ohne finalen Text gegenstandslos.

## `comment-2026-09-21-0001` — **ABGELEHNT (SPERRE BESTÄTIGT)**

- Der vollständige Originalpost behandelt den METR-Bericht zum Hugging-Face-/OpenAI-Vorfall als allgemeine KI-News. Das trifft das No-Go `beliebige KI-News ohne Verbindung zum Kernthema`.
- Die ausdrückliche Einordnung über UN-Generalversammlung und ein separates US-China-Treffen trifft zusätzlich das No-Go `Politik`.
- Es fehlt ein belastbarer Anschluss an die Prüfung **signierter** PDFs, Archivierung oder Freigabe, Records/ECM, Audit-Trail, ZertES/eIDAS-Signaturprüfung oder BIV. Dass der verlinkte Bericht selbst als PDF vorliegt, schafft keinen Kampagnenbezug.
- `fit_score: 0.02` ist als nahezu null und im Vergleich zu 0002 minimal höher vertretbar, weil der Post zumindest `digital trust` nennt; daraus darf dennoch keine künstliche Produkt- oder Prozessbrücke gebaut werden.
- Die vorhandene `fit_note` benennt beide konkreten Sperrgründe und die fehlenden Kernthema-Anker korrekt und ausreichend.
- Das leere `text:`-Feld ist folgerichtig. Ein Kommentar würde entweder am Kampagnenziel vorbeigehen oder eine unbelegte Brücke erfinden. Das schützt vor Politikbezug, Faktenrisiko und markenfremdem Opportunismus.

## `comment-2026-09-21-0002` — **ABGELEHNT (SPERRE BESTÄTIGT)**

- Der vollständige Originalpost ist ein beworbener allgemeiner AI-/Digital-Workspace-Report zu Observability, Risiko, Experience und Security. Das trifft die No-Gos `generische Digitalisierungsposts ohne konkreten Bezug` und `beliebige KI-News ohne Verbindung zum Kernthema`.
- Es fehlt jeder konkrete Bezug zu signierten PDFs, Prüfung vor Archivierung oder Freigabe, Records/ECM, Signaturvalidierung, Audit-Trail oder BIV.
- `fit_score: 0.01` bildet den praktisch fehlenden Kampagnenfit korrekt ab und steht zu Recht nach `0.02`.
- Die vorhandene `fit_note` ist konkret, sachlich und deckungsgleich mit Kampagnen-No-Gos und Originalpost.
- Das leere `text:`-Feld ist folgerichtig. Ein Kommentar wäre ein generischer Werbe-/Report-Anschluss oder müsste einen nicht belegten Kampagnenbezug konstruieren; beides wäre weder thematisch noch markensicher.

## Gesamturteil

**Beide Kandidaten sind ABGELEHNT; beide Sperren sind korrekt.** Scores, konkrete `fit_note`-Begründungen, absteigende Sortierung, leere Texte, ungekreuzte sichtbare Queue-Einträge und das Auslassen einer Style-Evaluator-Runde sind kampagnen- und prozesskonform. Es gibt keine Textrevision an den Copywriter: Die Ablehnung beruht auf den Originalposts und den harten Kampagnen-No-Gos, nicht auf einer reparierbaren Formulierung.

Die beiden final übergebenen Zustände wurden genau einmal geprüft. Queue, Texte, Metadaten und Checkboxen wurden nicht verändert. Es wurde nichts nutzerfreigegeben, geplant, verschoben oder veröffentlicht. Dieses Urteil ist ausschließlich intern und berechtigt nicht zur Veröffentlichung.
