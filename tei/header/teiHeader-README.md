# teiHeader
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0  

---
## Indice

1. [Definizione e perimetro del file](#1-definizione-e-perimetro-del-file)
2. [Architettura dei Blocchi Metatestuali](#2-architettura-dei-blocchi-metatestuali)
3. [Sistema Tassonomico (`classDecl`)](#3-sistema-tassonomico-classdecl)
4. [Dichiarazione del Tagset (`tagsDecl`)](#4-dichiarazione-del-tagset-tagsdecl)
   - A. [Struttura Radice e Metadati](#a-struttura-radice-e-metadati)
   - B. [Descrizione del Manoscritto](#b-descrizione-del-manoscritto)
   - C. [Struttura del Testo](#c-struttura-del-testo)
   - D. [Trascrizione Interpretativa e Integrazioni](#d-trascrizione-interpretativa-e-integrazioni)
   - E. [Genetica d'Autrice (nell'apparato)](#e-genetica-dautrice-nellapparato)
   - F. [Apparato Critico](#f-apparato-critico)
   - G. [Annotazione Interpretativa e Stand-off](#g-annotazione-interpretativa-e-stand-off)
   - H. [Indice d'Impatto (Feature Structures)](#h-indice-dimpatto-feature-structures)
   - I. [Collegamenti e Citazioni](#i-collegamenti-e-citazioni)
   - J. [Entità Nominate, Termini e Note](#j-entità-nominate-termini-e-note)
5. [Protocollo IA (`xenoData` + `projectDesc`)](#5-protocollo-ia-xenodata--projectdesc)
6. [Validazione e Qualità del Dato](#6-validazione-e-qualità-del-dato)
7. [Citazione](#7-citazione)
8. [Contatti](#8-contatti)

---

## 1. Definizione e perimetro del file

Questo file costituisce l'architettura metatestuale e il modello computazionale completo (`teiHeader`) per l'edizione digitale del *Castello dell'anima* (Palermo, Biblioteca Comunale, ms. 2 Qq E 29).

Come **dispositivo di rappresentazione scientifica**, il file racchiude l'infrastruttura d'inquadramento e audit dell'edizione: metadati bibliografici e codicologici, apparato critico, sistema tassonomico, protocollo di simulazione IA e tracciabilità del workflow. Non contiene il testo del manoscritto (collocato in un file TEI separato), garantendo la netta separazione tra **testo-oggetto** e **modello di descrizione**.

---

## 2. Architettura dei Blocchi Metatestuali

Il `teiHeader` è strutturato in cinque moduli operativi, concepiti per garantire il rispetto dei principi **FAIR** (*Findable, Accessible, Interoperable, Reusable*).

```
                  ┌─────────────────────────────────────────┐
                  │                teiHeader                │
                  └────────────────────┬────────────────────┘
     ┌──────────────────┬──────────────┴──────┬────────────────────┐
     │                  │                     │                    │
┌────┴────────────┐┌────┴───────────┐ ┌───────┴────────────┐┌──────┴─────────┐
│    fileDesc     ││  encodingDesc  │ │   profileDesc      ││   xenoData     │
├─────────────────┤├────────────────┤ ├────────────────────┤├────────────────┤
│ • Titolo & Auth ││ • Criteri Ecd. │ │ • Sociolinguistica ││ • JSON IA      │
│ • Codicologia   ││ • classDecl(12)│ │ • listPerson       ││ • METS Link    │
│ • Apparati      ││ • tagsDecl (70)│ │ • listOrg          ││                │
│                 ││                │ │ • textClass        ││                │
└─────────────────┘└────────────────┘ └────────────────────┘└────────────────┘
                                        │
                             ┌──────────┴──────────┐
                             │    revisionDesc     │
                             ├─────────────────────┤
                             │ • Audit Log (>70)   │
                             └─────────────────────┘
```

| Blocco XML | Funzione Ecdotica e Computazionale |
| :--- | :--- |
| **`fileDesc`** | **Descrizione bibliografica e materiale.** Include dati di titolarità, licenza, 6 tipologie di note critiche, descrizione codicologica analitica (mani, inchiostri, layout), bibliografia e testimoni. |
| **`encodingDesc`** | **Modello formale ed ecdotico.** Contiene l'abstract del modello, i criteri editoriali (`projectDesc`, `refsDecl`, `editorialDecl`), il tagset dichiarato (`tagsDecl`) e le tassonomie (`classDecl`). |
| **`profileDesc`** | **Inquadramento storico e sociolinguistico.** Traccia il contesto di produzione del testo mistico secentesco: analisi sociolinguistica della lingua, prosopografia (`listPerson`) e istituzioni (`listOrg`: Carmelo, Inquisizione). |
| **`xenoData` (×2)** | **Dati non-TEI e interoperabilità.** Ospita la specifica JSON del protocollo di simulazione IA e il puntatore ai metadati METS. |
| **`revisionDesc`** | **Audit trail della lavorazione.** Log cronologico decrescente (>70 voci) che traccia ogni modifica, revisione e decisione editoriale. |

---

## 3. Sistema Tassonomico (`classDecl`)

Il sistema si fonda su **12 tassonomie** (8+2+2): **8 interpretative** applicate al testo via `@ana`, **2 ausiliarie** (`impact-band-N`, `impact-band-A` — i vocabolari-banda usati nei `symbol` delle `fs` dell'indice d'impatto, non applicate via `@ana`) e **2 di processo** (`fase`, `workflow`) riservate al `revisionDesc`.

```
                     classDecl (12 Tassonomie)
                                │
   ┌─────────────────────────────┼─────────────────────────────┐
   ▼                             ▼                             ▼
8 Interpretative (via @ana)   2 Ausiliarie (symbol fs)    2 di Processo (revisionDesc)
├── func (4 rami)             ├── impact-band-N (4)        ├── fase (42)
├── risk (5)                  └── impact-band-A (3)        └── workflow (4)
├── impact (4)
├── mystic_state (5)
├── operation (5)
├── exposition (4)
├── phase (4)
└── relation (10)
```

### Regole di Formattazione e Integrità
- **Separazione d'uso:** Le 8 tassonomie interpretative si applicano al testo tramite `@ana`; le 2 ausiliarie `impact-band-N`/`impact-band-A` forniscono i valori-banda dei `symbol` nelle `fs`; le 2 di processo sono riservate al `revisionDesc`.
- **Integrità dei Dati:** Ogni categoria possiede obbligatoriamente un `xml:id` e un elemento `catDesc` compilato e non vuoto. L'`xml:id` deve rispettare il prefisso della tassonomia radice — **eccetto l'asse `func`**, esplicitamente esente per consentire ai suoi assi di primo livello (`legittimazione`, `pedagogia`, `rischio`, `ethos`) di non portare il prefisso `func-`.

---

## 4. Dichiarazione del Tagset (`tagsDecl`)

Il tagset disciplina **70 elementi TEI**, dichiarati nel `tagsDecl` in un unico ordinamento logico dal contenitore al dettaglio e qui raggruppati per macro-funzione (A–J). Il modello editoriale è la **trascrizione interpretativa** a normalizzazione grafica **silenziosa e dichiarata** ([`docs/criteri-trascrizione.md`](../../docs/criteri-trascrizione.md) + `editorialDecl`): alcuni elementi restano *dichiarati* nel tagset per compatibilità e riuso, ma **non compaiono** nel testo di lettura (vedi D–E).

### A. Struttura Radice e Metadati
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `TEI`, `teiHeader` | Radice della codifica e testata descrittiva del modulo. |
| `fileDesc`, `sourceDesc` | Metadati editoriali e descrizione del manoscritto autografo. |

### B. Descrizione del Manoscritto
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `msDesc`, `msIdentifier` | Descrizione strutturata e identificazione archivistica del testimone. |
| `msContents`, `msItem` | Contenuto e articolazione interna (Libri I–III). |
| `physDesc`, `handDesc`, `handNote` | Descrizione materiale, mani scriventi e inchiostri/matita. |
| `layoutDesc`, `layout` | *Mise en page* e rigatura. |

### C. Struttura del Testo
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `div`, `head`, `argument` | Partizione (Libri, Capitoli), rubriche/titoli e sommari argomentativi. |
| `titlePage`, `titlePart` | Frontespizio e sue porzioni (titolo, formula, responsabilità). |
| `p`, `seg` | Unità minima del discorso e unità di struttura/interpretative. |
| `pb`, `lb` | Foliazione originale (recto/verso) e interruzioni di riga. |
| `fw`, `anchor` | Elementi di cornice (richiami, segnature) e punti d'ancoraggio per lo stand-off. |

### D. Trascrizione Interpretativa e Integrazioni

> La grafia (accenti, abbreviazioni, divisione delle parole, refusi di copia) è regolarizzata **silenziosamente** e dichiarata una volta per tutte. Gli elementi diplomatici di normalizzazione — `choice`, `orig`/`reg`, `sic`/`corr`, `abbr`/`expan` — restano **dichiarati nel tagset** ma **non compaiono** nel testo di lettura. Attivi i soli marcatori di integrazione e incertezza materiale.

| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `abbr`, `expan` | Abbreviazioni e scioglimenti — *dichiarati, non usati* (scioglimento silenzioso). |
| `choice`, `orig`, `reg` | Alternative editoriali, forma originale vs normalizzata — *dichiarati, non usati* (normalizzazione silenziosa). |
| `sic`, `corr` | Errori del ms. vs correzioni editoriali — *dichiarati, non usati* (correzione silenziosa). |
| `foreign` | Segmenti in lingua diversa **non** citazionali (nel corpus attuale: nessuno; il latino citazionale è `cit`/`quote`, vedi I). |
| `gap`, `supplied`, `unclear` | **Attivi:** lacune fisiche, integrazioni congetturali/su guasto (le parentesi quadre `[ ]`) e grafie illeggibili. |

### E. Genetica d'Autrice (nell'apparato)

> Le varianti **sostanziali** d'autrice — aggiunte, cassature, sostituzioni — si registrano **solo dentro `<app>`/`<rdg>`** (apparato sostanziale, F); le correzioni puramente grafiche non si marcano (silenziose). Restano inline le sole ritracciature/ripristini.

| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `add`, `del`, `subst` | Aggiunte, cancellature e sostituzioni autoriali — **dentro `<rdg>`** dell'apparato. |
| `restore` | Ripristino di una porzione cancellata e poi confermata. |
| `retrace` | Ripasso/rinforzo del tratto da parte della stessa mano (strato prudenziale tardivo `#ink_3-dark`). |
| `metamark` | Segni operativi d'autore (richiami, segni di spostamento). |

### F. Apparato Critico
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `app`, `lem`, `rdg` | Apparato *in situ*: lezione base e varianti d'autore (`Tb0`, `Tb1`, `T1`…). |

### G. Annotazione Interpretativa e Stand-off
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `spanGrp`, `span` | Gruppi e singole annotazioni analitiche su nuclei concettuali. |
| `interp`, `interpGrp` | Voci e gruppi di vocabolario interpretativo (figure retoriche). |
| `link`, `linkGrp` | Associazioni esplicite fra segmenti e annotazioni. |
| `rs`, `hi` | Stringhe referenziali generiche ed evidenziazioni grafiche. |

### H. Indice d'Impatto (Feature Structures)
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `standOff` | Contenitore di annotazioni non in linea (indice d'impatto, figure). |
| `fs`, `f`, `symbol`, `numeric` | Struttura di tratti, tratto singolo, valore-banda (`symbol`: N_band/A_band) e valore numerico (`numeric`: N/A/F/Fnorm/I) dell'indice. |

### I. Collegamenti e Citazioni
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `ref`, `ptr` | Rinvii interni/esterni/intertestuali e puntatori strutturali. |
| `cit`, `quote`, `bibl` | Citazioni bibliche/liturgiche/mistiche e riferimenti bibliografici. |

### J. Entità Nominate, Termini e Note
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `persName`, `placeName`, `orgName` | Tagging di persone, luoghi e istituzioni. |
| `date`, `term` | Date storiche/redazionali e termini tecnici o mistici. |
| `note` | Note editoriali, dottrinali e contestuali. |

---

## 5. Protocollo IA (`xenoData` + `projectDesc`)

L'edizione integra un **protocollo IA per la generazione di eventi controfattuali** (Claude Sonnet 5, fallback Gemini), formalizzato nel blocco `xenoData` e nei criteri di `projectDesc`.

### Codici delle Operazioni Controfattuali
| Codice | Operazione |
| :--- | :--- |
| `-CIT` | Soppressione di una glossa o citazione dal testo |
| `+TEXTsub` | Recupero di una cancellatura autoriale |
| `+CIT` | Integrazione per esteso di una citazione richiamata |

### Principi di Controllo Filologico
1. **Expert-in-the-Loop:** Nessuna variante generata dall'IA viene incorporata nel testo base. Ogni evento è verificato ed espresso come lettura alternativa (`<app>/<lem>/<rdg>`).
2. **Auditability:** Parametri, vincoli e campi obbligatori dell'audit trail sono formalizzati in sintassi JSON all'interno di `xenoData`.

---

## 6. Validazione e Qualità del Dato

- **Validazione strutturale:** l'header è validato contro **`tei_all.rng`** (RelaxNG
  completo TEI P5), dichiarato nel file tramite `<?xml-model?>`.
- **Governance della tassonomia:** le tassonomie interpretative sono definite nella
  fonte normativa `tei/taxonomy/tassonomia-gh.xml`, validata a parte contro il proprio
  ODD (`taxonomy-odd.odd` → RelaxNG + Schematron: presenza/non-vacuità di `catDesc`,
  coerenza del prefisso `xml:id`, unicità globale). L'header ne incorpora una copia
  allineata; la coerenza della copia con la fonte è garantita da controllo separato.
- **Integrità referenziale:** la risoluzione dei puntatori interni (`@ana`, `@ref`,
  `@who`, `@corresp`) è verificata separatamente e non fa parte delle regole Schematron.

---

## 7. Citazione

Longo, Luciano (2026). *Castello dell'anima — teiHeader dell'edizione digitale TEI + IA*. Working draft, 25 luglio 2026. CC BY 4.0.

## 8. Contatti

Luciano Longo — `luciano.longo@dedalus.com`  
ORCID: [0009-0005-7557-7546](https://orcid.org/0009-0005-7557-7546)
