### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-14] – Tassonomia interpretativa prudenziale
# Implementazione Livelli di Esposizione e Marcatura Critica

### Added
- **Introduzione dei livelli di esposizione dottrinale**: implementata la scala di intensità per l'asse `exposition`, necessaria a mappare la trasparenza o la prudenza del discorso mistico. Sono stati definiti i seguenti identificatori:
    - `expo-bassa`: Esposizione prudente, ampio uso di metafore e linguaggio piano.
    - `expo-media`: Presenza moderata di contenuti dottrinali con citazioni di supporto.
    - `expo-alta`: Trattazione intensa di materie mistiche che richiede glosse e cautele.
    - `expo-critica`: Livello massimo di esposizione, relativo a temi a forte rischio di censura (es. unione trasformativa).
- **Completamento dell’annotazione dei nodi ad alta esposizione**: terminata l'analisi sistematica delle sezioni del testo che presentano una densità dottrinale elevata, garantendo la copertura dei passaggi più sensibili del manoscritto.

### Changed
- Affinata la metodologia di rilevamento dei "punti di calore" del testo: l'asse `exposition` agisce ora in sinergia con l'asse `risk` per evidenziare le strategie di difesa dell'autrice.

### Documentation
- Inserite nella documentazione le definizioni qualitative per distinguere i quattro livelli di esposizione, fornendo criteri oggettivi per la scelta tra `expo-alta` e `expo-critica`.
- Documentata la correlazione statistica tra l'uso di glosse (`operation`) e l'aumento del livello di esposizione.

### Fixed
- Risolte le ambiguità nella classificazione dei segmenti intermedi, stabilizzando il confine tra esposizione "bassa" e "media" attraverso l'analisi dei tecnicismi teologici presenti.

### Notes
- L'introduzione di questa scala permette di visualizzare graficamente la "curva di rischio" dell'opera, identificando visivamente le aree dove il controllo istituzionale si faceva più pressante.
