# Guida alla Navigazione del *teiHeader*

### Edizione digitale TEI + IA — *Castello dell'anima*

---
## Indice

1. [Cos'è questo file](#1-cosè-questo-file)
2. [Struttura generale del teiHeader](#2-struttura-generale-del-teiheader)
3. [Mappa rapida della navigazione](#3-mappa-rapida-della-navigazione)
4. [Che cosa contiene ogni sezione](#4-che-cosa-contiene-ogni-sezione)
5. [Come cercare velocemente nel teiHeader](#5-come-cercare-velocemente-nel-teiheader)
6. [Come usare il teiHeader per il riuso](#6-come-usare-il-teiheader-per-il-riuso)
7. [Esempio di percorso tipico](#7-esempio-di-percorso-tipico)
8. [Riferimenti utili](#8-riferimenti-utili)
9. [Contatti](#9-contatti)
***

## 1. Cos'è questo file

Questo documento è una **guida operativa** per orientarsi all'interno del *teiHeader* dell'edizione digitale del *Castello dell'anima*.  
Serve a:

*   capire come è organizzata la struttura
*   trovare rapidamente le sezioni rilevanti
*   riutilizzare tassonomie, metodo, modelli editoriali
*   navigare gli ID, le mani, le tassonomie e il revision log

***

## 2. Struttura generale del teiHeader

Il teiHeader è composto da cinque blocchi diretti:

*   **`<fileDesc>`** — Identità, provenienza, responsabilità
*   **`<encodingDesc>`** — Metodo editoriale, tassonomie (`classDecl`)
*   **`<profileDesc>`** — Lingue, persone, contesto storico
*   **`<xenoData>`** — Pipeline IA (specifica machine-readable) e puntatore METS; è un blocco a sé, non annidato in `encodingDesc`
*   **`<revisionDesc>`** — Log completo della lavorazione

***

## 3. Mappa rapida della navigazione

### 🔹 **Per trovare i dati materiali del manoscritto**

Vai in:

*   `fileDesc` → `sourceDesc` → `msDesc` → `physDesc` → `handDesc`
*   `fileDesc` → `sourceDesc` → `listWit`

### 🔹 **Per capire i criteri editoriali**

Vai in:

*   `encodingDesc`
*   `editorialDecl`
*   `projectDesc`
*   `tagsDecl`

### 🔹 **Per capire le categorie usate in @ana**

Vai in:

*   `encodingDesc` → `classDecl`
*   ogni `<taxonomy xml:id="...">`

### 🔹 **Per ricostruire il workflow editoriale**

Vai in:

*   `revisionDesc`

### 🔹 **Per studiare la rete delle persone**

Vai in:

*   `profileDesc` → `listPerson`
*   `profileDesc` → `listOrg`

***

## 4. Che cosa contiene ogni sezione

### **`<fileDesc>`**

*   informazioni su titolo, autore, editor
*   provenienza del manoscritto
*   bibliografia primaria
*   identificazioni archivistiche

### **`<encodingDesc>`**

*   principi di trascrizione
*   apparato critico in *parallel segmentation*
*   definizione delle mani e dei layer
*   tassonomie utilizzate nell'attributo `@ana` (in `classDecl`)

### **`<profileDesc>`**

*   lingue
*   profilo sociolinguistico
*   lista delle persone coinvolte
*   istituzioni religiose e inquisitoriali

### **`<xenoData>`**

*   specifica machine-readable della pipeline IA (modello, vincoli, operazioni controfattuali, audit trail)
*   puntatore METS

### **`<revisionDesc>`**

*   lista cronologica delle operazioni editoriali
*   scenari IA
*   validazioni
*   note di correzione

### **`<classDecl>`** (dentro `encodingDesc`)

*   il modello concettuale dell'intera edizione, articolato in otto assi interpretativi: funzioni retoriche (`func`), rischio dottrinale (`risk`), impatto interpretativo (`impact`), stati mistici (`mystic_state`), operazioni discorsive (`operation`), livelli di esposizione (`exposition`), fasi discorsive (`phase`), relazioni semantiche (`relation`)
*   più due assi di processo editoriale (`fase`, `workflow`)

***

## 5. Come cercare velocemente nel teiHeader

### 🔍 *Cerchi una categoria @ana?*

Cerca:

    taxonomy xml:id="..."

### 🔍 *Cerchi come trattare glosse, aggiunte, cancellature?*

Controlla:

    encodingDesc → editorialDecl

### 🔍 *Cerchi come funzionano i testimoni?*

Controlla:

    fileDesc → sourceDesc → listWit

### 🔍 *Cerchi cosa indica un certo xml:id?*

Cerca:

    xml:id="..."

### 🔍 *Cerchi l'elenco delle mani scriventi?*

Controlla:

    fileDesc → sourceDesc → msDesc → physDesc → handDesc

### 🔍 *Cerchi come è stata gestita l'IA?*

Controlla:

    xenoData (specifica machine-readable)
    projectDesc (descrizione discorsiva)
    revisionDesc (scenari applicati)

***

## 6. Come usare il teiHeader per il riuso

### ✅ *Importare le tassonomie*

Puoi copiare direttamente l'intero `<classDecl>` nel tuo progetto.

### ✅ *Replicare il metodo editoriale*

La sezione `<encodingDesc>` è pensata per essere usata come modello.

### ✅ *Estrarre l'ontologia del testo*

Le tassonomie non sono attualmente esportate in formati Linked Open Data, ma la loro struttura (categorie con `xml:id` stabile e `catDesc`) le rende adattabili, con lavoro aggiuntivo, a formati come SKOS, RDF, JSON-LD o OntoLex-Lemon.

### ✅ *Creare documentazione FAIR*

`revisionDesc` fornisce provenance completa per depositi in piattaforme.

***

## 7. Esempio di percorso tipico

### 🔹 Per capire "cos'è `risk-dottrinale`"

1.  Cerca `risk-dottrinale` in `classDecl` (tassonomia `risk`)
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

## 8. Riferimenti utili

Per una completa interoperabilità:

*   TEI P5 Guidelines
*   ODD customization
*   Modello TEI + IA documentato in `xenoData` e `projectDesc`
*   Tassonomie descritte in `classDecl`

***

##  9. Contatti

Luciano Longo — `luciano.longo@dedalus.com`  
ORCID: [0009-0005-7557-7546](https://orcid.org/0009-0005-7557-7546)
