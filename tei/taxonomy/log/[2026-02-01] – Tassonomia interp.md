### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-02-01] – Tassonomia interpretativa prudenziale
# Definizione Ontologica e Primi Set Semantici

### Added
- **Creazione del primo set di categorie semantiche**: implementata la struttura base per l'attributo `@ana`, permettendo il collegamento tra segmenti testuali e nodi interpretativi.
- **Definizione delle funzioni retoriche**: inserite le prime classi per mappare l'intenzionalità dell'autrice (asse `func`), con focus sulla postura narrativa e giustificativa.
- **Definizione degli stati mistici**: stabilite le categorie fondamentali per la descrizione dell'esperienza interiore (asse `mystic_state`), fornendo un vocabolario controllato per i fenomeni descritti nel testo.
- **Definizione delle categorie di rischio**: implementata la tassonomia per i livelli di criticità dottrinale (asse `risk`), essenziale per identificare i punti di frizione con la sorveglianza inquisitoriale.

### Changed
- Evoluzione dell'approccio di codifica: transizione da una marcatura puramente descrittiva a una **marcatura analitico-interpretativa**.
- Rafforzamento del legame tra il `teiHeader` (dove risiedono le definizioni) e il `body` (dove le categorie vengono applicate).

### Documentation
- Redazione delle prime note esplicative per ogni categoria aggiunta, propedeutiche alla compilazione della documentazione.
- Stabilito il principio di **univocità degli ID** per prevenire collisioni semantiche tra funzioni retoriche e stati mistici.

### Fixed
- Correzione delle prime ridondanze terminologiche tra le etichette di "funzione" ( `func` ) e "operazione".
- Allineamento formale degli identificatori (`xml:id`) alle convenzioni stabilite nel piano di lavoro.

### Notes
- Questo set rappresenta lo "scheletro" semantico del progetto.
- La distinzione tra *stato mistico* (fenomeno) e *rischio* (conseguenza esterna) è stata fissata come pilastro dell'architettura multi-asse.
