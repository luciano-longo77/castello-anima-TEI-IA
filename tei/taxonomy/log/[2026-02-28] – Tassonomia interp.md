### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-28] – Tassonomia interpretativa prudenziale
# – Normalizzazione Semantica e Validazione delle Co-occorrenze

### Added
- **Verifica della co-occorrenza dei valori**: implementato un protocollo di controllo per garantire la stabilità semantica tra assi diversi (es. assicurare che un `risk-high` sia coerentemente supportato da un'adeguata `operation` di riequilibrio).
- **Verifica della corrispondenza funzioni/valori**: accertata la coerenza logica tra le funzioni retoriche dichiarate e i valori annotativi applicati, eliminando discrepanze tra l'intento comunicativo e la marcatura tecnica.

### Changed
- **Normalizzazione dell'attributo `@ana`**: eseguita la pulizia e standardizzazione di tutti i valori annotati in ogni unità del testo (`seg`, `cit`), garantendo l'assenza di refusi o stringhe non autorizzate.
- **Riallineamento alle tassonomie**: forzato il matching speculare tra i valori usati nel corpo del testo e le definizioni strutturali presenti nel `<classDecl>` del `teiHeader`.
- **Armonizzazione terminologica**: completata l'unificazione del linguaggio tecnico tra i cinque assi principali (`func`, `operation`, `risk`, `exposition`, `relation`), stabilizzando il vocabolario controllato del progetto.

### Documentation
- Aggiornata la matrice di co-occorrenza nel documento metodologico per guidare i futuri inserimenti ed evitare accoppiamenti di metadati logicamente inconsistenti.
- Formalizzate le regole di armonizzazione terminologica per mantenere la coerenza tra i diversi livelli di analisi (retorico, tattico e dottrinale).

### Fixed
- Corretti tutti i puntatori orfani o residui di vecchie nomenclature che impedivano il perfetto allineamento tra testo e tassonomia.
- Risolte le ambiguità definitorie tra "funzione" e "operazione", stabilendo una gerarchia chiara tra l'obiettivo strategico e l'azione testuale concreta.

### Notes
- La stabilità semantica raggiunta permette ora l'estrazione di dati statistici per una prima analisi dell'intertestualità sotto sorveglianza.