# 📘 Guida alla Navigazione del *teiHeader*

### Edizione digitale TEI + IA — *Castello dell’anima*

***

## ✅ 1. Cos’è questo file

Questo documento è una **guida operativa** per orientarsi all’interno del *teiHeader* dell’edizione digitale del *Castello dell’anima*.  
Serve a:

*   capire come è organizzata la struttura
*   trovare rapidamente le sezioni rilevanti
*   riutilizzare tassonomie, metodo, modelli editoriali
*   navigare gli ID, le mani, le tassonomie e il revision log

***

## ✅ 2. Struttura generale del teiHeader

Il teiHeader è composto da quattro grandi blocchi:

*   **`<fileDesc>`** — Identità, provenienza, responsabilità
*   **`<encodingDesc>`** — Metodo editoriale, tassonomie, pipeline IA
*   **`<profileDesc>`** — Lingue, persone, contesto storico
*   **`<revisionDesc>`** — Log completo della lavorazione

***

## ✅ 3. Mappa rapida della navigazione

### 🔹 **Per trovare i dati materiali del manoscritto**

Vai in:

*   `fileDesc`
*   `sourceDesc`
*   `handDesc`
*   `listWit`

### 🔹 **Per capire i criteri editoriali**

Vai in:

*   `encodingDesc`
*   `editorialDecl`
*   `projectDesc`
*   `tagsDecl`

### 🔹 **Per capire le categorie usate in @ana**

Vai in:

*   `classDecl`
*   ogni `<taxonomy xml:id="...">`

### 🔹 **Per ricostruire il workflow editoriale**

Vai in:

*   `revisionDesc`

### 🔹 **Per studiare la rete delle persone**

Vai in:

*   `profileDesc` → `listPerson`
*   `profileDesc` → `listOrg`

***

## ✅ 4. Che cosa contiene ogni sezione

### ### **`<fileDesc>`**

*   informazioni su titolo, autore, editor
*   provenienza del manoscritto
*   bibliografia primaria
*   identificazioni archivistiche

### **`<encodingDesc>`**

*   principi di trascrizione
*   apparato critico in *parallel segmentation*
*   definizione delle mani e dei layer
*   pipeline IA documentata (xenoData)
*   tassonomie utilizzate nell’attributo `@ana`

### **`<profileDesc>`**

*   lingue
*   profilo sociolinguistico
*   lista delle persone coinvolte
*   istituzioni religiose e inquisitoriali

### **`<revisionDesc>`**

*   lista cronologica delle operazioni editoriali
*   scenari IA
*   validazioni
*   note di correzione

### **`<classDecl>`**

*   il modello concettuale dell’intera edizione
*   funzioni retoriche
*   stati mistici
*   categorie di rischio
*   posizioni materiali
*   fasi discorsive

***

## ✅ 5. Come cercare velocemente nel teiHeader

### 🔍 *Cerchi una categoria @ana?*

Cerca:

    taxonomy xml:id="..."

### 🔍 *Cerchi come trattare glosse, aggiunte, cancellature?*

Controlla:

    encodingDesc → editorialDecl

### 🔍 *Cerchi come funzionano i testimoni?*

Controlla:

    listWit

### 🔍 *Cerchi cosa indica un certo xml:id?*

Cerca:

    xml:id="..."

### 🔍 *Cerchi l’elenco delle mani scriventi?*

Controlla:

    handDesc

### 🔍 *Cerchi come è stata gestita l’IA?*

Controlla:

    xenoData
    projectDesc
    revisionDesc (scenari)

***

## ✅ 6. Come usare il teiHeader per il riuso

### ✅ *Importare le tassonomie*

Puoi copiare direttamente l’intero `<classDecl>` nel tuo progetto.

### ✅ *Replicare il metodo editoriale*

La sezione `<encodingDesc>` è pensata per essere usata come modello.

### ✅ *Estrarre l’ontologia del testo*

Le tassonomie sono pronte per essere esportate in:

*   SKOS
*   RDF
*   JSON-LD
*   OntoLex-Lemon

### ✅ *Creare documentazione FAIR*

`revisionDesc` fornisce provenance completa per depositi in piattaforme.

***

## ✅ 7. Esempio di percorso tipico

### 🔹 Per capire “cos’è risk:risk-dottrinale”

1.  Cerca `risk-dottrinale` in `classDecl`
2.  Vedi la sua definizione e il dominio semantico
3.  Torna nel testo e leggi i segmenti che lo usano

### 🔹 Per sapere cosa significa `hand="ink_1"`

1.  Vai in `handDesc`
2.  Leggi la descrizione paleografica
3.  Trova i segmenti del testo che la usano

### 🔹 Per vedere come è arrivato un certo valore

1.  Cerca il suo `xml:id`
2.  Trova la voce corrispondente in `revisionDesc`

***

## ✅ 8. Riferimenti utili

Per una completa interoperabilità:

*   TEI P5 Guidelines
*   ODD customization
*   Modello TEI + IA documentato in `encodingDesc`
*   Tassonomie descritte in `classDecl`

***

## ✅ 9. Contatti

Per assistenza, consultare la sezione “Contatti” nel README principale.
