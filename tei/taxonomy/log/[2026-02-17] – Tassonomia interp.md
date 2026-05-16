### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-17] – Tassonomia interpretativa prudenziale
# Consolidamento degli Attributi e Stabilizzazione del Sistema

### Added
- **Stabilizzazione del sistema annotativo**: Fissato l'uso combinato degli attributi `@ana` (per il puntamento alle categorie tassonomiche) e `@subtype` (per la specificazione tipologica locale), garantendo una granularità a due livelli nella marcatura dei segmenti.
- **Definizione delle gerarchie**: Implementata la logica per cui `@ana` gestisce l'asse semantico universale del progetto, mentre `@subtype` accoglie le variazioni contestuali interne ai singoli libri.

### Changed
- **Revisione complessiva degli attributi**: Eseguito un audit integrale su tutte le unità annotate per verificare la coerenza tra l'intento interpretativo e la codifica tecnica.
- **Rimozione degli attributi provvisori**: Eliminati tutti i tag e gli attributi temporanei utilizzati durante la fase di bozza e i test di marcatura automatica, lasciando il codice pulito e pronto per la pubblicazione.

### Documentation
- Aggiornate le linee guida nella sezione **"Sintassi della Marcatura"** per riflettere l'uso normativo della coppia `@ana`/`@subtype`.
- Documentata la procedura di pulizia dei metadati per i futuri revisori del corpus.

### Fixed
- Risolte le ambiguità derivanti dall'uso di attributi non standard o ridondanti che interferivano con la validazione ODD.
- Bonificati i residui di marcatura sperimentale che appesantivano il `body` del testo.

### Notes
- Questa fase segna il passaggio definitivo della **prototipazione**. 
- Il sistema annotativo è ora considerato **congelato** per le verifiche e lo stess test AI.