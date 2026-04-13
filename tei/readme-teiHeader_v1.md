# Castello dell’anima — Edizione Digitale TEI + IA (teiHeader)
### Autrice: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
### Editor: Luciano Longo  
### Versione: 1.0 — 13 aprile 2026  

---
## 📘 Navigazione

- [1. Descrizione del progetto](#1-descrizione-del-progetto)
- [2. Standard utilizzati](#2-standard-utilizzati)
- [3. Struttura del teiHeader](#3-struttura-del-teiheader)
- [4. Pipeline TEI + IA](#4-pipeline-tei--ia)
- [5. Contenuti principali](#5-contenuti-principali)
- [6. Conformità](#6-conformità)
- [7. Contatti](#7-contatti)
- [8. Citazione](#8-citazione)
---

## 1. Descrizione del progetto
Questo deposito contiene il **teiHeader completo** dell’edizione digitale del *Castello dell’anima* (Palermo, Biblioteca Comunale, ms. 2 Qq E 29), progettata come **edizione critica, diplomatica, genetica e interpretativa** secondo gli standard **TEI P5**.

Il teiHeader documenta in modo esaustivo:

- la **descrizione materiale** del manoscritto (mani, inchiostri, ductus, glosse, sostituzioni, cancellature);  
- la **strutturazione genetica** (Tb0–Tb3, T4) e il modello dei testimoni;  
- l’**apparato critico** in *parallel segmentation*;  
- un **sistema tassonomico multilivello** (funzioni, rischio, esposizione, prudenza, mistica, relazione, posizione, fase, layer);  
- la **governance IA** per la produzione di scenari controllati expert‑in‑the‑loop;  
- un **indice d’impatto numerico (N/A/F)** per la valutazione computazionale delle zone critiche;  
- un **revision log completo** (>70 entries) per garantire auditabilità e trasparenza.

Il file costituisce un **metadataset FAIR** autonomo, riusabile e interoperabile.

---

## 2. Standard utilizzati
- **TEI P5** — moduli: core, msdescription, transcr, textcrit, linking, analysis  
- **ODD customization** specifica del progetto  
- **Proprietà FAIR**:  
  - *Findable*: xml:id persistenti e univoci  
  - *Accessible*: TEI P5 aperto  
  - *Interoperable*: tassonomie documentate in `<classDecl>`, ODD  
  - *Reusable*: documentazione completa del metodo  

Licenza: **CC BY-NC 4.0**

---

## 3. Struttura del teiHeader
Il file include:

- **fileDesc**: provenienza, responsabilità, identificazione del manoscritto  
- **encodingDesc**: criteri editoriali, tassonomie, pipeline IA, apparato critico  
- **profileDesc**: lingue, profilo sociolinguistico, prosopografia, istituzioni  
- **revisionDesc**: audit trail completo  
- **classDecl**: modello concettuale multilivello (retorica, teologia, rischio, mistica)  
- **handDesc**: mani scriventi e analisi paleografica  
- **biblStruct e listBibl**: fonti dottrinali e scritturali  

---

## 4. Pipeline TEI + IA
La sezione `<xenoData>` documenta una pipeline IA controllata:

- generazione di varianti scenariali (–CIT, +CIT’, +GLOSSA_IA, RIC)  
- seed deterministici per replicabilità  
- validazione umana (`expert‑in‑the‑loop`)  
- audit trail con hash input/output  
- nessuna modifica sul testo base  

Gli scenari sono codificati come `<rdg ana="scenario:*">`.

---

## 5. Contenuti principali
- descrizione materiale completa  
- modellizzazione genetica Tb0–Tb3/T4  
- apparato critico in *parallel segmentation*  
- tassonomie semantiche multilivello  
- prosopografia e contesto istituzionale (Carmelo, Inquisizione)  
- catene intertestuali, dottrinali, mistiche, retoriche, epistemiche (`<linkGrp>`)  

---

## 6. Conformità e qualità
Il teiHeader rispetta:

- **TEI Scholarly Editions Guidelines**  
- **sshOC/DARIAH Data Stewardship Guidelines**  
- **FAIR Data Principles**  
- **Provenance & Versioning Best Practices**  
- **Interoperability principles for semantic TEI**  

La sezione `<revisionDesc>` garantisce una tracciabilità completa del workflow editoriale.

---

## 7. Contatti
**Editor**: Luciano Longo  
Email: luciano.longo@dedalus.com  
ORCID: https://orcid.org/0009-0005-7557-7546

---

## 8. Citazione consigliata
Longo, Luciano (2026), *Castello dell’anima — teiHeader dell’edizione digitale TEI + IA*, v.1.0.
