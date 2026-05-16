### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-04-22] – Stabilizzazione e Uniformazione

### Added
- Implementata la versione **v2.1 della tassonomia core**, con passaggio alla nomenclatura tecnica internazionale (inglese accademico) per gli assi `exposition`, `phase` e `impact`.
- Inserite nuove categorie granulari nell'asse `exposition`: `low`, `medium`, `high`, `critical` (in sostituzione della precedente terminologia italiana).
- Definito l'asse cronologico `phase` con i nuovi identificatori: `introduction`, `development`, `conclusion`.

### Changed
- **Uniformazione Totale**: Allineati i puntatori `@ana` nel file di esempio `taxonomy-text-model.xml` con le definizioni contenute in `tassonomia.xml`.
- **Risoluzione Incongruenze**: Eliminati tutti i riferimenti "orfani" (es. `#expo-media`, `#phase-fase-iniziale`) a favore della nomenclatura rigorosa richiesta dallo Schematron (`#exposition-medium`, `#phase-introduction`).
- **Precisione Terminologica**: Sostituiti i termini descrittivi generici con identificatori univoci per garantire la stabilità delle query XPath e delle analisi computazionali.

### Documentation
- Aggiornato il paragrafo relativo alla **"Coerenza di Stringa"** nel manuale di codifica: ora è esplicitamente richiesto il matching letterale tra `@xml:id` della tassonomia e valore di `@ana` nel testo.
- Verificato il log di validazione: il sistema ora restituisce `0 errori` nel confronto incrociato tra i file allegati.

### Fixed
- - **Drift analitico verso versioni tassonomiche legacy**:
  risolto un problema di persistenza di riferimenti a versioni obsolete della tassonomia
  nei processi di analisi automatica; forzata la validazione esclusiva sugli allegati correnti.
- **Validazione Schematron**: Ripristinata la "tenuta" scientifica del prefisso obbligatorio (es. ogni categoria dell'esposizione deve tassativamente iniziare con `exposition-`).

### Notes
- La tassonomia è ora considerata **stabile (v2.2)**.