### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-07] – Tassonomia interpretativa prudenziale
# Consolidamento Architetturale e Armonizzazione Identificatori

### Added
- **Creazione del primo sistema combinato per annotazioni multiple**: implementata la logica di stratificazione che permette l'applicazione simultanea di più categorie (es. `risk` + `operation` + `impact`) su un singolo attributo `@ana`.
- Sviluppata la struttura per la gestione delle del set tag interpretativo, garantendo che ogni segmento testuale possa essere interrogato su più assi contemporaneamente.

### Changed
- **Revisione del set di categorie**: raffinamento delle definizioni esistenti per eliminare sovrapposizioni semantiche e migliorare la precisione della marcatura durante la codifica manuale.
- **Armonizzazione degli identificatori XML**: normalizzazione di tutti gli `xml:id` delle categorie tassonomiche per garantire una nomenclatura coerente (es. passaggio a nomi standardizzati e rimozione di discrepanze lessicali).

### Documentation
- Aggiornate la documentazione sulla sintassi degli identificatori per riflettere le nuove regole di armonizzazione.
- Inseriti esempi pratici di "annotazione combinata" nel manuale di codifica per illustrare la corretta gestione degli spazi tra gli ID all'interno di `@ana`.

### Fixed
- Risolti i conflitti di naming negli ID delle categorie che causavano errori durante il parsing automatico delle relazioni tra gli assi.
- Eliminati i riferimenti incrociati orfani nati durante le prime fasi di definizione delle categorie.

### Notes
- L'armonizzazione degli identificatori è un passo cruciale per la validità dello Schematron e per la futura stabilità delle query di analisi dei dati.
