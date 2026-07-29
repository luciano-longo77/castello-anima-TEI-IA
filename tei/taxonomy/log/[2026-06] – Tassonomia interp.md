### 📝 Change Log: Progetto "Castello dell'anima"

## [2026-06-03] – Normalizzazione riferimenti @ana

### Changed
- Normalizzati 64 valori `@ana` in `revisionDesc` e `projectDesc` del `teiHeader`, allineandoli ai nuovi identificatori delle tassonomie `fase` e `workflow` e aggiungendo il carattere `#` iniziale mancante.

### Notes
- Intervento sul `teiHeader`; nessuna modifica a `tassonomia-gh.xml`.

---

## [2026-06-17] – Rimozione riferimenti orfani

### Fixed
- Rimossi undici riferimenti `@ana` orfani privi di categoria dichiarata in `classDecl` (`diario-mistico` e le sue tre partizioni, `model-constraints`, `workflow-2`, quattro fasi editoriali non dichiarate), senza alterare il testo associato.

### Notes
- Intervento sul `teiHeader`; nessuna modifica a `tassonomia-gh.xml`.
