<!--
Documento metodologico.

Questo paper descrive la tassonomia interpretativa prudenziale
implementata in `tassonomia-gh.xml` e governata tramite schema TEI,
Relax NG e Schematron.

Il documento non introduce categorie nuove né propone estensioni
del modello: costituisce la descrizione formale e critica
della tassonomia così come implementata nel repository.
-->

# Una tassonomia interpretativa prudenziale per l'annotazione TEI  
## Statuto, architettura e governo di un modello ermeneutico

## Abstract

Il contributo presenta una **tassonomia interpretativa prudenziale** progettata a partire dal *Castello dell'anima* di Teresa di San Geronimo (secolo XVII), come modello per la formalizzazione e il governo dell'annotazione interpretativa in ambiente TEI. La tassonomia è concepita come un **oggetto ermeneutico autonomo**, formalizzato nel `teiHeader` e governato mediante vincoli strutturali (Relax NG) e semantici (Schematron). L'obiettivo non è classificare contenuti tematici, ma rendere **esplicite, verificabili e controllabili** le categorie interpretative che presiedono all'annotazione di testi ad alta densità ermeneutica. Il modello si fonda su un'architettura multi‑asse, distingue nettamente la definizione delle categorie dal loro uso nel testo e costituisce un'infrastruttura metodologica verificabile e riproducibile.

## Indice

- [Abstract](#abstract)
1. [Oggetto e statuto della tassonomia interpretativa](#1-oggetto-e-statuto-della-tassonomia-interpretativa)
2. [Architettura della tassonomia interpretativa prudenziale](#2-architettura-della-tassonomia-interpretativa-prudenziale)
   - 2.1 [Razionale della struttura multi-asse](#21-razionale-della-struttura-multi-asse)
   - 2.2 [Le tassonomie core](#22-le-tassonomie-core)
   - 2.3 [Categorie e descrizioni](#23-categorie-e-descrizioni)
3. [Implementazione TEI e governo formale](#3-implementazione-tei-e-governo-formale)
   - 3.1 [Collocazione nel `teiHeader`](#31-collocazione-nel-teiheader)
   - 3.2 [Vincoli strutturali e semantici](#32-vincoli-strutturali-e-semantici)
   - 3.3 [Separazione tra definizione e uso](#33-separazione-tra-definizione-e-uso)
   - 3.4 [Robustezza del modello: verifica empirica dei vincoli](#34-robustezza-del-modello-verifica-empirica-dei-vincoli)
4. [Uso controllato della tassonomia](#4-uso-controllato-della-tassonomia)
- [Conclusione](#conclusione)
---

## 1. Oggetto e statuto della tassonomia interpretativa

La tassonomia qui presentata non è una ontologia tematica del contenuto testuale, né un apparato descrittivo del lessico o dei concetti dottrinali. Essa nasce come **dispositivo di governo dell'interpretazione**, progettato per rendere esplicite le categorie attraverso cui un testo viene letto, segmentato e annotato.

Nel contesto del *Castello dell'anima*, l'annotazione comporta necessariamente l'attivazione di categorie interpretative non neutre: funzioni retoriche, strategie prudenziali, livelli di rischio dottrinale, gradi di esposizione concettuale. La tassonomia assume come principio di base che tali categorie **non possano rimanere implicite**, né essere affidate a etichette estemporanee o a note discorsive non formalizzate.

Per questo motivo la tassonomia è modellizzata come **oggetto TEI autonomo**, collocato nel `teiHeader` e separato dal corpo del testo. Essa non descrive il testo, ma **dichiara le condizioni interpretative del suo trattamento**. Il suo statuto è quindi metatestuale ed ermeneutico: la tassonomia non è un supporto dell'edizione, ma una infrastruttura concettuale che precede e governa l'annotazione.

---

## 2. Architettura della tassonomia interpretativa prudenziale

### 2.1 Razionale della struttura multi‑asse

L'interpretazione di un testo mistico non è riducibile a una singola dimensione semantica. Una stessa unità testuale può, simultaneamente, svolgere una funzione retorica, attivare un rischio dottrinale, richiedere un'operazione prudenziale e avere un impatto interpretativo differente sul contesto immediato e sull'opera nel suo complesso.

Per rispondere a questa complessità, la tassonomia adotta una **architettura multi‑asse**, articolata in tassonomie distinte, ciascuna dedicata a una specifica dimensione dell'atto interpretativo. Questa separazione impedisce la sovrapposizione di categorie eterogenee e garantisce la leggibilità e l'interrogabilità del modello.

### 2.2 Le tassonomie core

Il modello definisce otto tassonomie principali, ciascuna formalizzata come elemento `<taxonomy>` dotato di identificatore stabile:

- **Funzioni interpretative (`func`)**  
  Modella il ruolo discorsivo e retorico dei segmenti testuali (legittimazione, pedagogia, gestione del rischio, ethos).  
  Non descrive contenuti, ma funzioni svolte nel discorso.

- **Rischio dottrinale (`risk`)**  
  Esplicita i punti di possibile ambiguità o criticità interpretativa (quietismo, panteismo, impeccabilità, ambiguità).  
  Svolge una funzione eminentemente prudenziale.

- **Impatto interpretativo (`impact`)**  
  Indica il peso interpretativo di un segmento sul contesto esegetico, distinguendo nodi portanti da passaggi di supporto.

- **Stati mistici (`mystic_state`)**  
  Modella gli stati dell'esperienza mistica non come temi, ma come categorie operative dell'interpretazione.

- **Operazioni prudenziali (`operation`)**  
  Rende esplicite le strategie testuali di controllo e mitigazione del rischio (`attenuatio`, `delimitazione`, `precisatio`, `declaratio`, `riequilibrio`).

- **Livello di esposizione (`exposition`)**  
  Descrive il grado di esplicitazione concettuale, indipendentemente dal contenuto teologico.

- **Fase discorsiva (`phase`)**  
  Colloca i segmenti all'interno della progressione argomentativa dell'opera.

- **Relazioni (`relation`)**  
  Formalizza legami intertestuali, analogici e argomentativi.

### 2.3 Categorie e descrizioni

Ogni categoria è identificata da un `xml:id` stabile ed è obbligatoriamente accompagnata da un elemento `<catDesc>`. La descrizione non ha valore meramente documentativo, ma costituisce il **luogo in cui l'interpretazione viene resa esplicita**. Una categoria priva di `<catDesc>`, o con `<catDesc>` vuoto, è considerata metodologicamente invalida — vincolo imposto non solo a livello editoriale, ma verificato meccanicamente dal content model Relax NG e dai controlli Schematron dedicati. Questa scelta trasforma la tassonomia in uno spazio di responsabilità ermeneutica, impedendo l'uso di etichette prive di fondamento interpretativo dichiarato.

---

## 3. Implementazione TEI e governo formale

### 3.1 Collocazione nel `teiHeader`

La tassonomia è implementata nel `teiHeader`, all'interno di `<encodingDesc>/<classDecl>`. Questa collocazione sancisce la sua funzione di **metamodello interpretativo**, distinto dal testo e dichiarato prima di ogni annotazione.

Il file `tassonomia-gh.xml` è concepito come documento TEI completo e autosufficiente, dotato di statuto scientifico autonomo, e costituisce l'**unica fonte normativa** delle categorie interpretative del progetto. Eventuali altre occorrenze di `classDecl` presenti altrove nel repository (ad esempio in file di metadati del manoscritto) non hanno statuto normativo proprio e devono essere mantenute allineate a questa fonte, o preferibilmente sostituite da un riferimento (`xi:include`) ad essa.

### 3.2 Vincoli strutturali e semantici

Il governo della tassonomia è garantito da due livelli di validazione:

- **Relax NG**, che definisce la struttura ammessa e l'obbligatorietà degli elementi;
- **Schematron**, che impone regole semantiche, tra cui l'obbligo di `<catDesc>`, la non vacuità delle descrizioni, la coerenza degli identificatori rispetto alla tassonomia di appartenenza e l'unicità degli `xml:id`.

Questi vincoli trasformano la tassonomia in un oggetto formalmente sorvegliato e sottratto a modifiche arbitrarie.

### 3.3 Separazione tra definizione e uso

Un principio centrale del modello è la separazione rigorosa tra definizione delle categorie interpretative e loro uso nel testo. I file testuali non sono validati contro lo schema della tassonomia, ma utilizzano le categorie esclusivamente tramite riferimenti `@ana`. Questa separazione evita la confusione tra fenomeno testuale e apparato interpretativo e garantisce la stabilità ontologica delle categorie.

### 3.4 Robustezza del modello: verifica empirica dei vincoli

La solidità di un modello tassonomico governato non si misura solo dalla coerenza del suo disegno, ma dalla sua capacità di **resistere a scostamenti reali** nel corso dello sviluppo. Il presente modello è stato sottoposto a verifica empirica sistematica, non solo a validazione formale: ogni vincolo dichiarato in Relax NG e Schematron è stato testato attivamente, introducendo deliberatamente violazioni (categoria priva di descrizione, descrizione vuota, identificatore non coerente con il prefisso della tassonomia radice, `xml:id` duplicato) per confermare che il sistema le intercetti correttamente prima che vengano committate.

Questa verifica ha inoltre messo in luce un rischio strutturale rilevante: la separazione tra definizione e uso della tassonomia (§3.3), pur essendo un principio metodologico solido, **non previene da sola la duplicazione della definizione stessa**. Nel corso dello sviluppo si è riscontrata una divergenza reale tra la tassonomia normativa e una sua copia parallela, embedded in un file di metadati del manoscritto, evolutasi indipendentemente fino a includere categorie assenti dalla fonte primaria e a usare un elemento di descrizione non conforme allo schema. La divergenza è stata rilevata e corretta solo grazie a un confronto sistematico, non a un controllo automatico integrato nella pipeline di validazione.

Questo caso mostra un limite intrinseco della governance dichiarativa: uno schema, per quanto rigoroso, vincola solo i documenti che vengono effettivamente validati contro di esso. La robustezza del modello dipende quindi non solo dalla qualità delle regole formali, ma dalla disciplina con cui ogni istanza della tassonomia viene tenuta sotto lo stesso regime di validazione — idealmente tramite un meccanismo di inclusione (`xi:include`) che renda strutturalmente impossibile la duplicazione, piuttosto che affidarsi al solo allineamento manuale.
---

## 4. Uso controllato della tassonomia

L'uso della tassonomia avviene attraverso l'attributo `@ana`, inteso come riferimento a categorie già dichiarate e governate. Ogni unità testuale può attivare simultaneamente più categorie appartenenti a tassonomie diverse, riflettendo la natura multidimensionale dell'interpretazione.

L'annotazione non mira a classificare il testo, ma a **rendere visibile la stratificazione ermeneutica** che presiede alla sua lettura. In questo senso, la tassonomia non riduce la complessità interpretativa, ma la esplicita e la rende governabile.

---

## Conclusione

La tassonomia interpretativa prudenziale qui presentata propone un modello alternativo all'annotazione tematica tradizionale. Formalizzando l'interpretazione come livello ontologico separato e governato, il modello consente di affrontare testi ad alta densità ermeneutica senza rinunciare al controllo metodologico.

La TEI è utilizzata non solo come linguaggio di rappresentazione del testo, ma come **strumento di governo dell'atto interpretativo**. In questo senso, la tassonomia non è un complemento dell'edizione, ma una sua condizione epistemica dichiarata.
