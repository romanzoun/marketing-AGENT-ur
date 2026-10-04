# Kampagnenrelevanz — Feed-Kommentarkandidat R4

- Auftrag: `CS-FC-DV-20260911-R4`
- Kampagne: `Kampagnen/document validator/kampagne.yaml`
- Bewerteter Queue-Job: `comment-2026-09-11-0006`
- URL: `https://lnkd.in/p/e_PvJmYJ`
- Autor-Feld: `Alex Rada commented`
- Urteil: **bedingt passend**

## Unmittelbare Integritätsprüfung vor dem Urteil

Der aktuelle Queue-Block wurde unmittelbar vor der Einstufung erneut gelesen. Job-ID,
URL und Autor-Feld entsprechen exakt den vorgegebenen Werten. Die Zielpost-Note nennt
Charly Wargnier mit sichtbarem Profilbezug zu „LLMs, AI agents & Data Science“, den
eigentlichen Posttext „trillion dollar company btw“ sowie Alex Radas Kommentar
„what's your background?“. Das Kommentartext-Feld war zu diesem Zeitpunkt leer, die
Freigabe-Checkbox nicht gesetzt; Evaluation und Planung waren ebenfalls leer.

## Begründung

**Themen und Keywords:** Der sichtbare Profiltext enthält mit „AI agents“ einen
expliziten Kampagnen-Keyword-Treffer und berührt damit das Kampagnenthema AI-Agenten.
Der eigentliche Zielpost behandelt jedoch weder Browser-Bedienung oder
Backoffice-Automatisierung noch die gesellschaftliche Frage Agent versus Mensch.
„trillion dollar company btw“ liefert dafür keinen belastbaren fachlichen Kontext.

**Kampagnenziel und ICP:** Es fehlt jeder direkte Bezug zu Document Validator, BIV,
signierten PDFs, ZertES/eIDAS, lokaler Hash-Prüfung, Archiv/Freigabe, Audit-Trail oder
Records-/Compliance-Prozessen. Auch der enge ICP aus Records, Vertragsadministration,
Compliance Ops, Banking, Versicherung, Verwaltung und Grossunternehmen ist im
Zielpost nicht erkennbar. Eine produktnahe Überleitung wäre daher konstruiert.

**Banned Topics:** Politik, Religion, Konkurrenzabwertung und juristische
Heilsversprechen kommen nicht vor. Auch die verbotene pauschale Ansprache „alle
Backoffice“ liegt nicht vor.

## Strategische Einordnung

Damit ist der Kandidat nicht stark genug für eine direkte DocVal-/BIV-Anknüpfung,
aber wegen des expliziten „AI agents“-Signals auch nicht vollständig ausserhalb der
Kampagne. Er ist **bedingt passend**: nur für einen eng am vorhandenen AI-Agenten-
Kontext bleibenden Beitrag denkbar; für Produkt-, Compliance- oder ICP-Nähe sollte
ein Kandidat mit konkretem Browser-, Identitäts-, Vertrauens- oder Prüfprozessbezug
bevorzugt werden.

Es wurde kein Kommentartext erstellt und keine Queue-Aktion ausgeführt.

## Abschlusskontrolle der Queue

Der unmittelbar vor dem Urteil gelesene Queue-Stand hatte den SHA-256-Hash
`2f59907c91426d2c7183e47493adc8ed01ac5603ec296cd6a4e1d8117ba78a9d`. Bei der
Abschlusskontrolle lautete er
`07141f0318194dddc1f2a9a2c04c56a3db4e6f7662e85d66e4ed39b8fa6f7977`, weil ein
paralleler Copywriter das zuvor leere `text:`-Feld von Job 0006 gefüllt hatte.
Diese Fremdänderung wurde weder veranlasst noch zurückgesetzt. Job-ID, URL,
Autor-Feld, vollständige Zielpost-Note, leere Checkbox, leere Planung und leere
Evaluation blieben in der Abschlusskontrolle unverändert. Der
content-strategist hat `approvals.md` nicht geschrieben.

Eine spätere reine Kontrolllesung ergab den Hash
`394a92e6184514441ff87c00f444a7491b677ae45edef42bd1a396783a4e74ca`:
Parallel waren nun zusätzlich `generated_text`, `evaluation_score: 0.83`,
Evaluationsnotiz/-zeitpunkt und `publish_at: 2026-09-13T10:00` eingetragen. Auch
diese Fremdänderungen wurden nicht veranlasst oder zurückgesetzt. ID, URL, Autor,
Zielpost-Note und die weiterhin leere Freigabe-Checkbox waren unverändert; der
content-strategist hat weiterhin keinen Queue-Schreibzugriff ausgeführt.
