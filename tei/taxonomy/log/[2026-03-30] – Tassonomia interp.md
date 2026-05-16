### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-03-30] – Tassonomia interpretativa prudenziale
# Raffinamento Semantico e Potenziamento delle Tassonomie Epistemiche

### Added
- **Tassonomia `risk`**: Introdotta la categoria specifica `risk-quietismo`. Questa aggiunta permette di isolare il rischio storico-dottrinale legato alle controversie del XVII secolo dal `risk-dottrinale` generico, aumentando la granularità analitica nelle sezioni a massima esposizione.
- **Tassonomia `impact`**: Introdotti i livelli funzionali `impact-critical` (impatto strutturale) e `impact-supportive` (impatto locale). L'estensione è mirata a migliorare le correlazioni statistiche con l'indice numerico N/A/F (Nulla/Adeguata/Forte).

### Changed
- **Tassonomia `operation`**: Eseguita una normalizzazione concettuale sulle categorie `attenuatio`, `precisatio` e `declaratio`. Le descrizioni sono state riscritte per rendere computabile la distinzione tra le diverse "mosse discorsive" autoriali e facilitare l'estrazione automatica delle strategie prudenziali.
- **Riorganizzazione delle Classi**: Tutte le modifiche sono state applicate e stabilizzate all'interno del `<classDecl>` nel `teiHeader`.

### Documentation
- Aggiornata la documentazione metodologica per riflettere la distinzione tra **tassonomie epistemiche** (7 attive) e **tassonomie procedurali** (ora separate nel modello e non utilizzate in `@ana`).
- Formalizzata la motivazione scientifica per il passaggio a una classificazione più granulare del rischio (distinzione tra rischio generico e specifico).

### Fixed
- Riallineamento dei pesi di impatto: la nuova distinzione tra `critical` e `supportive` risolve le ambiguità nella valutazione della "tenuta teologica" dei singoli segmenti.
- Armonizzazione delle descrizioni per garantire che le operazioni prudenziali non siano sovrapponibili tra loro.

### Notes
- **Stato della Tassonomia**: Il sistema conta ora **42 categorie** totali.
- Le modifiche apportate oggi agli assi `risk`, `operation` e `impact` sono considerate **stabili**.
- È stata confermata la scelta metodologica di non utilizzare tassonomie di processo per la marcatura diretta sul testo, mantenendo la pulizia semantica dell'attributo `@ana`.