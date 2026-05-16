### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-10] – Tassonomia interpretativa prudenziale
# [2026-04-22] – Riorganizzazione Strutturale e Consolidamento delle Tassonomie Core

### Added
- **Definizione formale delle tassonomie core**: stabilito il set definitivo degli 8 assi interpretativi per l'analisi del testo:
    - `func`: Funzioni retoriche e comunicative.
    - `risk`: Livelli e tipologie di rischio dottrinale.
    - `impact`: Impatto dell'affermazione sul sistema teologico.
    - `mystic_state`: Descrizione fenomenologica degli stati mistici.
    - `exposition`: Livello di chiarezza o cautela nell'esposizione.
    - `operation`: Manovre correttive e prudenziali (es. attenuatio).
    - `phase`: Collocazione del segmento nello sviluppo del libro.
    - `position`: Posizionamento del concetto rispetto all'ortodossia o alla tradizione.
- **Inserimento definitivo in `<classDecl>`**: codificata l'intera struttura tassonomica all'interno del `teiHeader`, rendendo il file un'unità autosufficiente per la validazione.

### Changed
- **Riorganizzazione del modello TEI**: ristrutturato il template del documento per accogliere una marcatura interpretativa sistematica, separando nettamente i metadati descrittivi da quelli analitici.
- Passaggio da una gestione "esterna" delle categorie a una gestione integrata nel file XML tramite l'uso rigoroso di `<taxonomy>` e `<category>`.

### Documentation
- Aggiornato l'elenco degli assi autorizzati nel documento metodologico.
- Specificate le descrizioni (`<desc>`) per ogni nuova categoria inserita per facilitare il lavoro dei codificatori e la supervisione dell'IA.

### Fixed
- Risolte le sovrapposizioni tra gli assi `operation` ed `exposition`, ora chiaramente distinti per funzione e ambito di applicazione.
- Normalizzati i prefissi degli `xml:id` per tutti gli assi definiti, eliminando le ambiguità che ostacolavano la validazione con Schematron.

### Notes
- Con questa riorganizzazione, l'architettura dei metadati è considerata stabile per la fase di codifica e verifica attuazione dei principi.