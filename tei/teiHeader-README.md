# Castello dell'anima — teiHeader dell'edizione digitale TEI + IA

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0  
**Stato**: Working Draft (25 luglio 2026)  

---
## Indice

1. [Definizione e Perimetro del File](#1-definizione-e-perimetro-del-file)
2. [Architettura dei Blocchi Metatestuali](#2-architettura-dei-blocchi-metatestuali)
3. [Sistema Tassonomico (`classDecl`)](#3-sistema-tassonomico-classdecl)
4. [Dichiarazione del Tagset (`tagsDecl`)](#4-dichiarazione-del-tagset-tagsdecl)
   - A. [Struttura Core e Contesto](#a-struttura-core-e-contesto)
   - B. [Descrizione del Manoscritto](#b-descrizione-del-manoscritto)
   - C. [Trascrizione e Correzioni Autoriali](#c-trascrizione-e-correzioni-autoriali)
   - D. [Apparato Critico e Annotazione Analitica](#d-apparato-critico-e-annotazione-analitica)
   - E. [Collegamenti e Citazioni](#e-collegamenti-e-citazioni)
   - F. [Entità Nominate e Note](#f-entità-nominate-e-note)
5. [Protocollo IA (`xenoData` + `projectDesc`)](#5-protocollo-ia-xenodata--projectdesc)
6. [Validazione e Qualità del Dato](#6-validazione-e-qualità-del-dato)
7. [Citazione](#7-citazione)
8. [Contatti](#8-contatti)

---

## 1. Definizione e Perimetro del File

Questo file costituisce l'architettura metatestuale e il modello computazionale completo (`teiHeader`) per l'edizione digitale del *Castello dell'anima* (Palermo, Biblioteca Comunale, ms. 2 Qq E 29).

Come **dispositivo di rappresentazione scientifica**, il file racchiude l'infrastruttura d'inquadramento e audit dell'edizione: metadati bibliografici e codicologici, apparato critico, sistema tassonomico, protocollo di simulazione IA e tracciabilità del workflow. Non contiene il testo del manoscritto (collocato in un file TEI separato), garantendo la netta separazione tra **testo-oggetto** e **modello di descrizione**.

---

## 2. Architettura dei Blocchi Metatestuali

Il `teiHeader` è strutturato in cinque moduli operativi, concepiti per garantire il rispetto dei principi **FAIR** (*Findable, Accessible, Interoperable, Reusable*).

```
                  ┌─────────────────────────────────────────┐
                  │                teiHeader                │
                  └────────────────────┬────────────────────┘
                                        │
     ┌──────────────────┬──────────────┴───────┬──────────────────┐
     │                   │                      │                  │
┌────┴────────────┐┌─────┴───────────┐ ┌────────┴──────────┐┌──────┴─────────┐
│    fileDesc      ││  encodingDesc   │ │   profileDesc      ││   xenoData     │
├──────────────────┤├─────────────────┤ ├────────────────────┤├────────────────┤
│ • Titolo & Auth  ││ • Criteri Ecd.  │ │ • Sociolinguistica ││ • JSON IA      │
│ • Codicologia    ││ • classDecl(10) │ │ • listPerson       ││ • METS Link    │
│ • Apparati       ││ • tagsDecl (46) │ │ • listOrg          ││                │
└──────────────────┘└─────────────────┘ └────────────────────┘└────────────────┘
                                        │
                             ┌──────────┴──────────┐
                             │    revisionDesc     │
                             ├──────────────────────┤
                             │ • Audit Log (>70)   │
                             └──────────────────────┘
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

Il sistema si fonda su **10 tassonomie**, suddivise in due famiglie distinte per evitare sovrapposizioni tra il piano ermeneutico sul testo e il piano gestionale del lavoro editoriale.

```
                     classDecl (10 Tassonomie)
                                │
     ┌──────────────────────────┴──────────────────────────┐
     ▼                                                      ▼
8 Tassonomie Interpretative                    2 Tassonomie di Processo
(Annotazione sul testo via @ana)               (Tracciamento in revisionDesc)
├── func (Funzioni retoriche, 16)              ├── fase (Fasi lavoro, 42)
├── risk (Rischio dottrinale, 5)                └── workflow (Scenari IA, 4)
├── impact (Impatto interpretativo, 4)
├── mystic_state (Stati mistici, 5)
├── operation (Operazioni discorsive, 5)
├── exposition (Livelli esposizione, 4)
├── phase (Fasi discorsive, 4)
└── relation (Intertestualità, 10)
```

### Regole di Formattazione e Integrità
- **Separazione d'uso:** Le 8 tassonomie interpretative si applicano al testo tramite `@ana`. Le 2 di processo sono riservate al `revisionDesc`.
- **Integrità dei Dati:** Ogni categoria possiede obbligatoriamente un `xml:id` e un elemento `catDesc` compilato e non vuoto. L'`xml:id` deve rispettare il prefisso della tassonomia radice — **eccetto l'asse `func`**, esplicitamente esente per consentire ai suoi assi di primo livello (`legittimazione`, `pedagogia`, `rischio`, `ethos`) di non portare il prefisso `func-`.

---

## 4. Dichiarazione del Tagset (`tagsDecl`)

Il tagset disciplina **46 elementi TEI**, raggruppati per macro-funzione.

### A. Struttura Core e Contesto
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `TEI`, `teiHeader`, `fileDesc` | Struttura radice e contenitori dei metadati. |
| `sourceDesc`, `msDesc`, `msIdentifier` | Identificazione archivistica e descrizione del testimone. |
| `div`, `p`, `seg`, `head` | Struttura del testo (Libri, Capitoli) e unità interpretative. |
| `pb` | Foliazione originale (recto/verso) per il controllo della materialità. |

### B. Descrizione del Manoscritto
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `msContents`, `msItem` | Contenuto e articolazione interna (Libri I–III). |
| `physDesc`, `handDesc`, `handNote` | Descrizione materiale, mani e inchiostri. |
| `layoutDesc`, `layout` | *Mise en page* e rigatura. |

### C. Trascrizione e Correzioni Autoriali
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `add`, `del`, `subst` | Tracciamento di aggiunte, cancellature e sostituzioni autoriali. |
| `abbr`, `expan` | Abbreviazioni e relativi scioglimenti editoriali. |
| `sic`, `corr` | Distinzione tra errori materiali del ms. e correzioni editoriali. |
| `gap`, `supplied`, `unclear` | Lacune fisiche, integrazioni congetturali e grafie illeggibili. |
| `lb` | Interruzioni di riga rilevanti. |

### D. Apparato Critico e Annotazione Analitica
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `app`, `lem`, `rdg` | Apparato *in situ*: lezioni base e varianti d'autore (`Tb0`, `Tb1`, `T1`…). |
| `spanGrp`, `span` | Annotazioni analitiche su nuclei concettuali. |

### E. Collegamenti e Citazioni
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `ref`, `ptr` | Rinvii interni, esterni e intertestuali. |
| `cit`, `quote`, `bibl` | Citazioni bibliche, liturgiche, mistiche e riferimenti bibliografici. |

### F. Entità Nominate e Note
| Elemento | Uso Ecdotico / Computazionale |
| :--- | :--- |
| `persName`, `placeName`, `orgName` | Tagging di persone, luoghi e istituzioni. |
| `date`, `term`, `lang` | Date, termini tecnici mistici e indicazioni di lingua. |
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
1. **Human-in-the-Loop:** Nessuna variante generata dall'IA viene incorporata nel testo base. Ogni evento è verificato ed espresso come lettura alternativa (`<app>/<lem>/<rdg>`).
2. **Auditability:** Parametri, vincoli e campi obbligatori dell'audit trail sono formalizzati in sintassi JSON all'interno di `xenoData`.

---

## 6. Validazione e Qualità del Dato

- **Validazione Strutturale:** Schema **RelaxNG** generato dall'ODD di progetto (`taxonomy.odd`).
- **Validazione Semantica (ISO Schematron):**
  - Presenza e non-vacuità di `catDesc`.
  - Coerenza del prefisso `xml:id` rispetto alla tassonomia radice (asse `func` esente).
  - Unicità globale degli `xml:id` su `taxonomy` e `category`.

La risoluzione dei puntatori interni (`@ana`, `@ref`, `@who`, `@corresp`) è verificata separatamente, non fa parte delle regole Schematron del progetto.

---

## 7. Citazione

Longo, Luciano (2026). *Castello dell'anima — teiHeader dell'edizione digitale TEI + IA*. Working draft, 25 luglio 2026. CC BY 4.0.

## 8. Contatti

Luciano Longo — `luciano.longo@dedalus.com`  
ORCID: [0009-0005-7557-7546](https://orcid.org/0009-0005-7557-7546)
