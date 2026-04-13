# Intertestualità sotto sorveglianza  
### Modello TEI-driven e AI-assisted per l’analisi di citazioni, glosse e rimandi nel *Castello dell’anima*

Questo repository documenta un progetto che integra **TEI interpretativo** e **Intelligenza Artificiale controllata** per lo studio delle funzioni intertestuali nel *Castello dell’anima* (1692–1693) di suor Teresa di San Geronimo. La ricerca si concentra sul modo in cui citazioni, glosse autoriali e rimandi mistici contribuiscono alla costruzione di chiarezza, coesione e stabilità dottrinale all’interno di un testo caratterizzato da forte vigilanza teologica.  

---
## 📑 Indice

* [Intertestualità sotto sorveglianza](#intertestualità-sotto-sorveglianza)

  * [Obiettivi](#-obiettivi)
  * [Struttura del repository](#-struttura-del-repository)
  * [Modello TEI](#-modello-tei)
  * [Pipeline AI](#-pipeline-ai)
  * [Il campione](#-il-campione)
  * [Stato dell’arte e ragioni del modello](#-stato-dellarte-e-ragioni-del-modello)
  * [Contributo del progetto](#-contributo-del-progetto)
  * [Licenza](#-licenza)
  * [Autore](#-autore)

---

##  🎯 Obiettivi

- Rappresentare in TEI citazioni bibliche, liturgiche, mistiche e proverbiali come **oggetti analitici** dotati di fonte, funzione retorica e impatto esplicativo.  

- Modellare **glosse autoriali** (attenuatio, precisatio, declaratio) come dispositivi di chiarificazione e delimitazione dottrinale.  

- Strutturare un **campione di 14 capitoli** selezionati per sensibilità dottrinale, densità intertestuale e presenza di fenomeni di revisione.  

- Implementare una **pipeline AI controllata** che consente:
  - rimozione di citazioni (–CIT),  
  - sostituzione con citazioni equifunzionali (+CIT’),  
  - aggiunta di glosse IA coerenti con lo stile autoriale (+GLOSSA_AI),  
  con successiva valutazione degli effetti su chiarezza, coesione e stabilità dottrinale.  

---

## 📁 Struttura del repository

### `/data`
- **base-dati**: contiene il set dei 14 capitoli utilizzati per l’analisi, insieme alle motivazioni della selezione (sensibilità, glosse, citazioni, articolazione tematica).  

### `/tei`
Modellazione secondo TEI P5 con:
- struttura gerarchica in `div` per Libri e capitoli;  
- citazioni annotate con `cit/quote/ref/bibl`;  
- glosse rappresentate tramite `note type="glossa"` e `subtype="attenuatio|precisatio|declaratio"`;  
- segmentazione retorica con `seg`;  
- funzioni e impatto tramite `@ana` e `@n_imp`;  
- gestione di varianti e fenomeni grafici con `add`, `del`, `subst`, `app`.

### 📘 Documentazione del teiHeader
Per consultare la documentazione completa del **teiHeader**  
(criteri editoriali, tassonomie, modello genetico, pipeline IA):  

➡️ **[Leggi il README del teiHeader](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/readme-teiHeader_v1.md)**  

### `/analysis`
Strumenti per:
- generazione controllata di varianti tramite IA (–CIT, +CIT’, +GLOSSA_AI),  
- ricalcolo di funzioni retoriche e impatto,  
- analisi comparativa fra testo base e varianti.  

### `/documentation`
Materiale di lavoro, linee guida di codifica e articolazione metodologica.

---

## 🧩 Modello TEI

### Citazioni
Rappresentate come entità autonome con:
- testo citato,  
- origine canonica o mistica,  
- riferimento normalizzato,  
- funzione retorica (legittimazione, pedagogia, gestione del rischio, ethos).  

### Glosse
Annotate come glosse esplicative, attenuative o dichiarative, collocate nei punti a maggiore esposizione dottrinale del testo.  

### Segmenti retorici
Porzioni di testo rilevanti, classificate tramite `@ana` secondo la funzione che svolgono nel discorso.

### Indice di impatto
Valore (alto, medio, basso) assegnato a citazioni e glosse in base a:
- necessità interpretativa,  
- capacità di ridurre ambiguità,  
- ruolo nel chiarire o delimitare concetti teologici complessi.  

---

## 🤖 Pipeline AI

La pipeline opera su varianti generate automaticamente in tre modalità:

- **–CIT**: rimozione di una citazione per valutare perdita di chiarezza o coesione;  
- **+CIT’**: sostituzione con una citazione equivalente per funzione;  
- **+GLOSSA_AI**: glosse IA in stile autoriale destinate a modulare il rischio esegetico.  

Ogni variante è sottoposta a:
1. generazione controllata,  
2. verifica esperta,  
3. rianalisi TEI con misurazione dell’impatto.

---

## 🔬 Il campione

Il dataset include **14 capitoli** distribuiti nei tre Libri dell’opera.  
I segmenti selezionati presentano:

- nodi dottrinali sensibili (contemplazione, unione, sicurezza spirituale, discernimento),  
- elevata densità di citazioni o rimandi,  
- glosse autoriali impiegate per chiarificazione o attenuazione,  
- estensione comparabile e equilibrio fra fenomeni retorici.  

Questo campione costituisce la base per l’annotazione TEI e per la sperimentazione AI.

---
## 📌 Stato dell’arte e ragioni del modello

Dalle linee di ricerca degli studi attuali emerge che:
- la scrittura mistica femminile post tridentina è caratterizzata da forte pressione normativa e sorveglianza dottrinale;  
- citazioni e glosse formano **una infrastruttura di controllo** che stabilizza il discorso nei punti ad alta esposizione;  
- mancano strumenti replicabili per misurare il ruolo dell’intertestualità in contesti analoghi;  

Su questa base
- 📡 il progetto propone un modello computazionale TEI+IA che colma questo vuoto metodologico.  

---

## 🌐 Contributo del progetto

Il modello permette di:

- analizzare in modo sistematico il rapporto fra citazione, glossa e costruzione del discorso mistico;  
- rendere osservabili e misurabili fenomeni normalmente affidati alla sola interpretazione qualitativa;  
- verificare l’effetto delle varianti tramite scenari controfattuali controllati;  
- fornire un protocollo replicabile per lo studio di testi mistici post tridentini e materiali prodotti in contesti di sorveglianza dottrinale.  

---

## 📄 Licenza
Da definire.

---

## 👤 Autore
**Luciano Longo**  
Filologia digitale e Digital Humanities  
Contatti: 
luciano.longo@dedalus.com
/ 
https://orcid.org/0009-0005-7557-7546
/
https://github.com/luciano-longo77
