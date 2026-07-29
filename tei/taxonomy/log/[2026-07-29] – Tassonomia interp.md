### 📝 Change Log: Progetto "Castello dell'anima"

## [2026-07-29] – Verifica di coerenza sistematica: XML, schema, esempi, CI, documentazione

### Documentation

- **`tassonomia-gh.xml` vs `teiHeader`**: verificata la coerenza integrale — le 8 tassonomie interpretative (`func`, `risk`, `impact`, `mystic_state`, `operation`, `exposition`, `phase`, `relation`) risultano identiche negli `xml:id` e nel testo delle `catDesc` in entrambi i file. Unica differenza rilevata: convenzione tipografica dell'apostrofo (curvo in `tassonomia-gh.xml`, dritto nel `teiHeader`) — nessuna divergenza di contenuto.
- **Licenza**: verificata coerente in CC BY 4.0 su `tassonomia-gh.xml`, `teiHeader`, `SPDX-License-Identifier CC-BY-4.0.md`, `Sistema Tassonomico.md` — stesso titolare, stesso URL target, nessuna restrizione NC residua.
- **Regole Schematron**: verificato il funzionamento reale (non per lettura) delle 4 regole — `category-catdesc-present`, `category-catdesc-not-empty`, `category-prefix-consistency` (con esenzione dell'asse `func`), `taxonomy-category-xmlid-unique` — tramite esecuzione diretta con `lxml.isoschematron` contro `tassonomia-gh.xml`.
- **`Sistema Tassonomico.md`**: rivisto interamente; corretti nome file ODD (`taxonomy-odd.odd` → `taxonomy.odd`, 4 occorrenze) e formula dell'indice N–A–F (allineata a quella reale del `teiHeader`: `I = 0.40N + 0.35A + 0.25F`, valori continui 0–1, non binari).
- **Widget `Interpretive_Taxonomy` (HTML)**: verificato che il fix precedente (`desc`→`catDesc`) fosse stato applicato correttamente; aggiunta sezione Schematron reale (prima assente nonostante il tag dichiarato); corretto tag `encodingDesc` da `schematron` a `standard` con nota esplicativa (elemento TEI non personalizzato dal progetto).
- **Guida di navigazione del `teiHeader`**: verificata e corretta (posizione di `xenoData` come fratello di `encodingDesc`, non suo contenuto; elenco tassonomie completato con le 4 mancanti; sintassi esempio `risk:risk-dottrinale` → `risk-dottrinale`).
- **README del `teiHeader`** (più versioni successive): riviste e allineate a licenza CC BY 4.0, protocollo IA a 3 procedure reali, struttura a 5 blocchi diretti, conteggio tassonomie corretto.
- **Diagramma Mermaid** (`rng-taxonomy-diagram.md`): corretta l'etichetta del nodo `catDesc` (prima ambigua, mostrata come "descNode"); corretto il collegamento del vincolo Schematron dal nodo `catDesc` al nodo `category` corretto (context reale delle regole); aggiunta dichiarazione di linguaggio `mermaid` al blocco di codice per renderizzazione corretta su GitHub.
- **Capitoli 1 e 2 del paper accademico**: verificati contro `tassonomia-gh.xml` — capitolo 2 pienamente coerente; capitolo 1 richiedeva allineamento terminologico sul protocollo controfattuale (vedi Fixed).

### Fixed

- **`taxonomy-sch.sch`**: corretto `queryBinding="xslt2"` → `queryBinding="xslt"` — il motore di validazione `lxml` usato in CI supporta solo Schematron XSLT 1.0; le 4 regole del progetto non richiedono funzioni XPath 2.0.
- **`tei/taxonomy/esempio/taxonomy-text-model.xml`**: rimossi 6 riferimenti `@ana` a categorie inesistenti (`relation-premessa-conseguenza`, `impact-supportive` ×2, `relation-analogia`, `relation-causa-effetto`, `relation-contrasto`), rimossi senza sostituzione su richiesta esplicita.
- **Paper accademico, capitolo 1** (§1.1, §1.2, §1.4): sostituita la vecchia triade "rimozione/ricollocazione/aggiunta" (e varianti a 4 operazioni in §1.2) con le tre procedure reali del protocollo IA (`-CIT` rimozione, `+TEXTsub` recupero di cancellature autoriali, `+CIT` integrazione di citazioni), coerenti con `projectDesc` e `xenoData` del `teiHeader`.
- **Indice dei log tassonomici**: corretta la data `[2026-03-28]` → `[2026-02-28]` (refuso di mese); rimosse due voci `[2026-04-08]` erroneamente aggiunte e non corrispondenti a file realmente presenti nella cartella; aggiunte le tre voci mensili `[2026-05]`, `[2026-06]`, `[2026-07]` mancanti dall'indice.
- **Log `[2026-02-28]`**: ammorbidito il linguaggio assoluto ("tutti i puntatori orfani", "assenza di refusi") non più coerente con i riferimenti inventati trovati oggi in `taxonomy-text-model.xml`; aggiunta nota di rimando alla verifica odierna.
- **Log `[2026-04-22]`**: corrette le categorie della tassonomia `phase` erroneamente indicate come `development`/`conclusion` — le categorie reali sono `phase-mediana`/`phase-conclusive`; aggiunta menzione del marcatore trasversale `phase-critical`, assente dalla voce originale; corretto il nome del file da `tassonomia.xml` a `tassonomia-gh.xml`.

### Added

- **`.github/workflows/main.yml`**: creato e attivato il workflow di validazione automatica GitHub Actions. Verifica, a ogni push su `tei/taxonomy/**`: buona formazione XML, conformità RelaxNG, conformità Schematron (4 regole reali), presenza delle 8 tassonomie core, e validità referenziale di ogni `@ana` nei file dentro `tei/taxonomy/esempio/` contro gli `xml:id` realmente dichiarati in `tassonomia-gh.xml`.
- **Guida CI/CD** (`docs/guida-ci-cd.html`): creata versione corretta con nomi file reali, sostituendo i tre file doppioni malposizionati in `tei/taxonomy/workflows/` (non eseguibili da GitHub Actions per posizione errata).
- **README `tei/taxonomy/schema/`**: creato, con distinzione esplicita tra file sorgente (`taxonomy.odd`, scritto a mano) e file generati (`taxonomy-rng.rng`, `taxonomy-sch.sch`) e avviso esplicito di non modificare questi ultimi a mano.
- **README `tei/taxonomy/esempio/taxonomy-text-model.xml`**: creato, breve guida di lettura del file esempio per il lettore non specialista.
- **Visualizzazione HTML** (`taxonomy-text-model.html`): creata pagina statica che mostra il testo annotato con evidenziazione per asse tassonomico e legenda colore.

### Notes

- **Verifica empirica del workflow**: testato end-to-end, inclusi due cicli di correzione in diretta (fallimento su `queryBinding`, poi su assenza del controllo referenziale @ana) fino a esecuzione con esito `Success` (run #6, 9 secondi, zero errori).
- **Limite tecnico documentato**: un vincolo Schematron dichiarativo che referenzi un documento esterno (`document()`) non è realizzabile in modo affidabile con `lxml.isoschematron`, per un problema di risoluzione dell'URI di base nella compilazione interna dello Schematron. Il controllo referenziale `@ana` è stato quindi implementato in Python nello script di CI, non in Schematron.
- **Nessuna modifica a `tassonomia-gh.xml`** in questa sessione: tutte le correzioni hanno riguardato file collegati (esempio, schema, documentazione, log), su richiesta esplicita di non intervenire sul file normativo stesso.
