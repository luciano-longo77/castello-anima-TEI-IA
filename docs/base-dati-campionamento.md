# Base dati per il campionamento
## Intertestualità sotto sorveglianza: 
### un modello TEI IA per Il Castello dell'anima di suor Teresa di San Geronimo

---

## 📑 Indice

1. [Introduzione](#introduzione)
2. [Dataset – Castello dell'anima (TEI+IA)](#dataset--castello-dellanima-teiia)
    - [Scopo del documento](#scopo-del-documento)
    - [Versioning](#versioning)
    - [Uso del documento](#uso-del-documento)
    - [Struttura del documento](#struttura-del-documento)
3. [1. Dataset](#1-dataset)
    - [1.1. LIBRO I (Anime principianti)](#11-libro-i-anime-principianti)
    - [1.2. LIBRO II (Anime proficienti)](#12-libro-ii-anime-proficienti)
    - [1.3. LIBRO III (Anime perfette)](#13-libro-iii-anime-perfette)
4. [2. Razionale dei capitoli selezionati](#2-razionale-dei-capitoli-selezionati)
    - [2.1 Razionale](#21-razionale)
    - [2.2 Selezione Libro I: motivazioni](#22-selezione-libro-i-motivazioni)
    - [2.3 Selezione Libro II: motivazioni](#23-selezione-libro-ii-motivazioni)
    - [2.4 Selezione Libro III: motivazioni](#24-selezione-libro-iii-motivazioni)
    - [2.5 Data set e Guida al modello](#25-data-set-e-guida-al-modello)
5. [3. Citazioni utili alla base dati](#3-citazioni-utili-alla-base-dati)
    - [3.1 Libro I (pedagogia + ethos)](#31-libro-i-pedagogia--ethos)
    - [3.2 Libro II (discernimento + rischio dottrinale)](#32-libro-ii-discernimento--rischio-dottrinale)
    - [3.3 Libro III - (mistica alta + glosse difensive)](#33-libro-iii---mistica-alta--glosse-difensive)
    - [3.4 Authority list](#34-authority-list)
6. [4. Citazioni rilevanti](#4-citazioni-rilevanti)
    - [4.1. Citazioni come legittimazione dottrinale](#41-citazioni-come-legittimazione-dottrinale)
    - [4.2. Citazioni come ancoraggio cristologico](#42-citazioni-come-ancoraggio-cristologico)
    - [4.3. Citazioni come marcatori di sofferenza / notte mistica](#43-citazioni-come-marcatori-di-sofferenza--notte-mistica)
    - [4.4. Citazioni sponsali (Cantico dei Cantici)](#44-citazioni-sponsali-cantico-dei-cantici)
    - [5.5. Citazioni di rifinitura dottrinale](#55-citazioni-di-rifinitura-dottrinale)
    - [5.6. Citazioni metafisiche e sapienziali](#56-citazioni-metafisiche-e-sapienziali)
    - [5.7. Citazioni patristiche - mistiche non bibliche](#57-citazioni-patristiche---mistiche-non-bibliche)
7. [6. Glosse](#6-glosse)
    - [6.1. Attenuatio](#61-attenuatio)
    - [6.2. Correctio](#62-correctio)
    - [6.3. Declaratio](#63-declaratio)
    - [6.4. Explicatio - metalinguistiche](#64-explicatio---metalinguistiche)
    - [6.5. Meccanismi esperienziali](#65-meccanismi-esperienziali)
    - [6.6. Analogia - metafora](#66-analogia---metafora)
    - [6.7. Potenze - volontà](#67-potenze---volontà)
    - [6.8. Guida spirituale](#68-guida-spirituale)
    - [6.9. Sicurezza mistica](#69-sicurezza-mistica)
    - [6.10. Trasformazione mistica](#610-trasformazione-mistica)
8. [7. INTERTESTUALITÀ NEL CASTELLO](#7-intertestualità-nel-castello)
    - [7.1. Il rapporto con Teresa d'Ávila](#71-il-rapporto-con-teresa-dávila-continuità-e-rovesciamento)
    - [7.2. Presenza della tradizione giovannea](#72-presenza-della-tradizione-giovannea-tecnica-delle-potenze-e-logica-della-notte)
    - [7.3. Metafore mistiche femminili](#73-metafore-mistiche-femminili-attrazione-amore-calamita)
    - [7.4. L'orizzonte della nuova mistica](#74-lorizzonte-della-nuova-mistica-consonanze-con-molinos-e-necessità-di-difese)
    - [7.5. Agiografia e genealogie femminili](#75-agiografia-e-genealogie-femminili-come-rete-di-legittimazione)
    - [7.6. Intertestualità culturale](#76-intertestualità-culturale)
    - [7.7. Intertesto esperienziale](#77-intertesto-esperienziale-lesperienza-personale-come-fonte-legittimante)
9. [Appendice - AUTHORITY FILE](#appendice-authority-file)

---

**Introduzione.**
Il presente documento descrive la struttura del dataset utilizzato per l'edizione digitale e l'analisi computazionale del Castello dell'anima di suor Teresa di San Geronimo. L'obiettivo è fornire una base dati chiara, riusabile e trasparente per la pipeline TEI+IA sviluppata nel progetto, in cui la codifica TEI P5, l'analisi delle funzioni retorico dottrinali e la generazione controllata di varianti controfattuali (–CIT, +CIT', +GLOSSA_IA) operano in modo integrato. Il dataset raccoglie i capitoli dei tre libri dell'opera che presentano maggiore rilevanza per la ricerca: sezioni ad alta sensibilità dottrinale, segmenti con densità intertestuale significativa e passaggi caratterizzati da glosse autoriali, chiarificazioni e dispositivi di sorveglianza. Per ciascun capitolo viene indicato il motivo della selezione, in relazione ai fenomeni mistici, pedagogici o prudenziali che il modello TEI deve rappresentare. Accanto alla definizione del campione, il documento include un'authority list completa delle citazioni bibliche, liturgiche, patristiche e mistiche utilizzate nel testo, con una classificazione funzionale (legittimazione, ancoraggio cristologico, marcatori di sofferenza, citazioni sponsali, sigilli dottrinali). Una sezione dedicata raccoglie inoltre 30 glosse tipizzate per funzione retorica (attenuatio, correctio, declaratio, explicatio, esperienziali), corredate dell'indicazione del rischio ermeneutico che ciascuna glossa disinnesca e del loro valore per gli esperimenti IA. Chiude il documento un quadro sintetico dell'intertestualità del Castello, che include riferimenti alla tradizione teresiana, giovannea e alle mistiche femminili post tridentine, oltre a elementi di quietismo, agiografia e intertestualità culturale. Insieme, questi materiali costituiscono la base metodologica, filologica e computazionale per l'intera analisi del manoscritto e garantiscono la piena riusabilità del dataset nel repository.

## Dataset – Castello dell'anima (TEI+IA)
Documentazione del campione, authority list e glosse tipizzate. Le citazioni e i riferimenti al Castello sono ripresi dall'edizione critica, *Il Castello dell'anima di suor Teresa di San Geronimo. Edizione critica*. Palermo: Centro Studi, 2024.

Questo documento costituisce la documentazione ufficiale del dataset utilizzato nel progetto *Intertestualità sotto sorveglianza: modello TEI+IA per il Castello dell'anima*. Raccoglie e descrive:
-	i capitoli selezionati dei tre libri dell'opera,
-	i criteri filologici e dottrinali della selezione,
-	l'authority list delle citazioni bibliche, liturgiche, patristiche e mistiche,
-	la tipizzazione delle glosse presenti nel manoscritto,
-	una sintesi dell'intertestualità strutturale dell'opera, fondamentale per l'annotazione TEI interpretativa e per gli esperimenti IA.

Il documento è concepito per essere riusabile, trasparente e interoperabile con:
-	il file TEI Castello dell'anima – base.xml (TEI P5),
-	la pipeline IA controllata (variazioni ±CIT, +GLOSSA_IA)
-	Guida TEI-driven

### Scopo del documento
1.	Definire il dataset utilizzato per l'analisi TEI+IA del Castello dell'anima.
2.	Motivare la selezione dei capitoli, secondo criteri di: 
    -	sensibilità dottrinale,
    -	densità intertestuale,
    -	presenza di glosse e dispositivi prudenziali,
    -	utilità per esperimenti computazionali.
3.	Fornire un'authority list unificata delle citazioni canoniche.
4.	Fornire una matrice di 30 glosse con funzione, rischio e valore per la pipeline IA.
5.	Documentare i principi di intertestualità sorvegliata rilevanti per l'encoding TEI.

### Versioning
-	Dataset version: v1.2 
-	Data di preparazione: 2026-04-01
-	Autore: Luciano Longo

- Dataset version: v0.0 (2026-03-09)
- Dataset version: v1.1 (2026-03-25)
- Dataset version: v1.2 (2026-04-01)

### Uso del documento
Questo documento è incluso nella cartella `docs/` del repository;
-	accompagna il file TEI come descrizione metodologica del dataset;
-	supportare la generazione di varianti IA;
-	guidare analisi, query e pattern TEI;
-	consentire la replicabilità degli esperimenti.

### Struttura del documento
1.	Dataset → capitoli selezionati e motivazioni
2.	Razionale metodologico della selezione
3.	Authority list delle citazioni
4.	Citazioni classificate per funzione e rischio
5.	Glosse tipizzate (30 esempi)
6.	Intertestualità strutturale
7.	Allegati e riferimenti critici

---

## 1. Dataset 

Lista completa dei capitoli che rispondono ai criteri di:
1.	sensibilità dottrinale,
2.	densità intertestuale,
3.	presenza di glosse o dispositivi di sorveglianza,
4.	rilevanza per gli esperimenti TEI+IA (–CIT, +CIT', +GLOSSA_AI).

### 1.1. LIBRO I (Anime principianti)

→ funzione: pedagogia + ethos

| Capitolo | Titolo | Motivo della selezione |
| :--- | :--- | :--- |
| I.1–2 | Si tratta della miseria humana / Come il mondo è una continua guerra… | Costruzione dell'ethos; assenza di citazioni → ideale per esperimenti +CIT |
| I.5 | Virtù dell'humiltà (Salmo In te Domine speravi) | Citazione strategica → segmento legittimante |
| I.6 | Virtù dell'obedienza (Christus factus est…) | Citazione cristologica → perfetto per –CIT / +CIT' |

### 1.2. LIBRO II (Anime proficienti)

→ funzione: discernimento + rischio dottrinale

| Capitolo | Titolo | Motivo della selezione |
| :--- | :--- | :--- |
| II.1–2 | Dispositione dell'anima | Fondazione dottrinale del discernimento → baseline |
| II.8 (a–d) | Oratione d'unione | Nodo critico: consonanza con Molinos, casi concreti, rischio di quietismo; ideale per +GLOSSA_AI |
| II.9a–b | Travagli delle anime | Casistica mistica → esperimenti di spostamento citazionale |
| II.10b | Segni per conoscere se la gratia è di Dio o del Demonio | Segmento normativo ad alta sensibilità; utile per stress test IA |

### 1.3. LIBRO III (Anime perfette)

→ funzione: mistica alta + glosse difensive

| Capitolo | Titolo | Motivo della selezione |
| :--- | :--- | :--- |
| III.8 | Cella secreta / matrimonio spirituale (Consummatum est; In manus tuas…) | Capitolo più ricco di glosse autoriali e citazioni stabilizzanti |
| III.9a–b | Passaggio alla cella di Dio / Stato di solitudine | Transizione concettuale; utile per confrontare presenza/assenza di glosse |
| III.12 | Stato d'otio / operazione di Dio nel fondo | Segmento di unione alta, senza glosse → +GLOSSA_AI |
| III.14 | Santa ignoranza | Concetto teologicamente esposto; alta utilità per analisi controfattuale |
| III.24 | Non si medita la passione, ma si "emita" Tristis est anima mea | Citazione semiliturgica pericolosa → nodo critico |
| III.34 | Trasformatione totale / matrimonio spirituale | Culmine teologico → ideale per grafi intertestuali |
| III.40 | Ultima cella dell'anima (ultimo capitolo) | Segmento finale per chiudere il ciclo ascensionale |

---

## 2. Razionale dei capitoli selezionati 

LIBRO I (I.1–2; I.5; I.6)
LIBRO II (II.1–2; II.8 a–d; II.9 a–b; II.10b)
LIBRO III (III.1; III.8; III.9 a–b; III.12; III.14; III.24; III.34; III.40)

### 2.1 Razionale 
Il dataset necessario per l'analisi TEI+IA del Castello dell'anima è costruito in modo coerente con la tua metodologia, integrando la prospettiva filologica, quella retorico-dottrinale e la sperimentazione computazionale prevista dalla pipeline IA controllata. La selezione del campione segue tre criteri principali: la sensibilità dottrinale, la densità intertestuale e la comparabilità strutturale tra i tre libri. La prima esigenza deriva dal fatto che l'opera presenta una serie di snodi nei quali il discorso mistico diviene potenzialmente ambiguo, soprattutto quando tocca temi come l'unione trasformante, la sicurezza dell'anima, l'obbedienza e il discernimento delle mozioni interiori; è in questi luoghi che glosse e citazioni agiscono come dispositivi di chiarificazione e di recinzione semantica, e la tua introduzione individua precisamente nel Libro II e nel Libro III le zone a maggiore rischio inquisitoriale e con più alta densità di glosse difensive. La seconda esigenza riguarda invece i capitoli che presentano citazioni bibliche, liturgiche o mistico-dottrinali utilizzate come meccanismi di stabilizzazione; in particolare, il capitolo sull'umiltà (Libro I), quello sull'obbedienza (Libro I), il capitolo VIII del Libro II e il capitolo VIII del Libro III, dove le citazioni si combinano con glosse e note di attenuazione. Infine, la comparabilità tra i libri richiede che il campione includa testi di estensione simile e di natura retorica complementare: la pedagogia spirituale del Libro I, il discernimento normativo del Libro II e la mistica alta e vigilata del Libro III, come la tua introduzione esplicitamente prescrive.  A partire da questi criteri, il dataset comprende nove sezioni principali. 

### 2.2 Selezione Libro I: motivazioni
Dal Libro I vengono selezionati i capitoli 1–2, 5 e 6. I primi due capitoli, dedicati alla miseria humana e alla verità rivelata, introducono la voce autoriale e costruiscono l'ethos della scrivente attraverso osservazioni autobiografiche e modelli di conversione come san Francesco, santa Maria Maddalena e santa Rosalia, elementi ben attestati nell'edizione; sono capitoli privi di citazioni formali e risultano preziosi per gli esperimenti IA di aggiunta artificiale di citazioni. Il capitolo sull'umiltà contiene invece la citazione salmica *In te Domine speravi, non confundar in aeternum*, indicata dalla Guida come esempio paradigmatico di citazione "legittimante" capacissima di rendere più chiaro e sorvegliato il discorso. Il capitolo sull'obbedienza presenta la citazione cristologica *Christus factus est pro nobis obediens usque ad mortem*, che costituisce l'architrave concettuale dell'argomentazione morale e permette di testare l'impatto della rimozione o della sostituzione equifunzionale. 

### 2.3 Selezione Libro II: motivazioni
Dal Libro II vengono selezionati l'inizio (capitoli 1–2) e il capitolo VIII. I primi servono come baseline dottrinale e contengono la definizione delle tre fonti di inganno spirituale (mondo, carne, demonio), articolando una pedagogia normativa senza glosse. Il capitolo VIII è invece la sezione più sensibile del Libro II: esso contiene casi concreti di discernimento delle mozioni, descrizioni delle ripugnanze e confusioni dell'anima, critica verso i direttori spirituali incompetenti e ampi passaggi che richiamano implicitamente la tripartizione della Guida spirituale di Molinos, come evidenziato sia nella tua introduzione sia nella Guida TEI-driven. Questo capitolo è ideale per gli esperimenti IA che prevedono l'aggiunta di glosse di attenuazione, permettendo di osservare come la ri-contestualizzazione esplicativa modifichi stabilità dottrinale, chiarezza argomentativa e coesione interna. 

### 2.4 Selezione Libro III: motivazioni
Dal Libro III vengono selezionati i capitoli 8 e 9. Il capitolo VIII presenta il nucleo più alto della mistica teresiana: unione, matrimonio spirituale, sicurezza dell'anima e il ricorso a citazioni della Passione, come *Consummatum est* e *In manus tuas, Domine, commendo spiritum meum*, entrambe presenti nella tua Guida e nell'edizione. Questo capitolo è caratterizzato dalla presenza sistematica di glosse difensive in cui l'autrice specifica "ciò s'intende / ciò non s'intende", un tratto identificato dalla tua introduzione come meccanismo di auto-mitigazione e di sorveglianza del discorso teologico. Si tratta della sezione più adatta per gli esperimenti IA di rimozione citazionale, di sostituzione e di generazione di glosse alternative, poiché consente di misurare con precisione la funzione stabilizzante delle citazioni bibliche e delle correzioni autoriali. Il capitolo IX, invece, mantiene un tono mistico elevato ma con minore densità di glosse e citazioni; ciò lo rende utile per testare l'introduzione di citazioni aggiuntive o varianti alternative ("+CIT'") al fine di valutare come queste influenzino la coerenza argomentativa. 

### 2.5 Data set e Guida al modello
L'intero dataset può essere rappresentato in TEI P5 secondo lo schema proposto nella Guida, che prevede l'uso di elementi come `<cit></cit>`, `<quote></quote>`, `<ref></ref>`, `<note type="glossa" subtype="attenuatio"></note>` e dell'attributo `ana` per annotare funzioni retoriche e impatti esplicativi. La struttura del documento TEI, articolata in di libro e di capitolo, consente di integrare citazioni bibliche con attributi specifici, glosse autoriali, rimandi interni e segmenti testuali pertinenti agli esperimenti IA. Grazie a questa configurazione, il dataset supporta pienamente l'intera pipeline sperimentale - rimozione e sostituzione delle citazioni, aggiunta di glosse IA, misurazione delle variazioni in chiarezza, coesione e stabilità dottrinale - e rende possibile una valutazione computazionale replicabile dell'intertestualità mistica post-tridentina secondo il modello TEI+IA presentato nei tuoi materiali.

---

## 3. Citazioni utili alla base dati 

### 3.1 Libro I (pedagogia + ethos)

**I.1–2** - Nessuna citazione formale → per esperimenti +CIT: aggiunta controllata di citazioni bibliche in stile.

**I.5 - Virtù dell'umiltà**
*In te Domine speravi, non confundar in aeternum* 
Sal 30/31 
→ citazione legittimante, frequente nella mistica umiltà. 

**I.6 -Virtù dell'obbedienza**
*Christus factus est pro nobis obediens usque ad mortem*
Fil 2,8 
→ pivot cristologico, altissimo impatto esplicativo. 

### 3.2 Libro II (discernimento + rischio dottrinale)

**II.1–2 – Baseline dottrinale**
*Spiritus promptus est* 
→ utile per IA: aggiunta/sostituzione di citazioni normative

**II.8– Orazione d'unione + effetti + avvertimenti** (Contesto vicino a Molinos → test per glosse). Citazioni utili del corpus (ricorrenti nei capitoli mistici sulla quiete/unione): 

*Pater noster, qui es in caelis* (formula liturgica) 
→ molto ricorrente nelle sezioni di unione.
 
*Misericordias Domini in aeternum cantabo* 
Sal 88,2
→ citazione di stato gioioso/illuminativo. 

*Vias mandatuorum tuorum cucurri, cum dilatasti cor meum* 
Sal 118,32
→ tipica delle sezioni di dilatazione del cuore. 

**II.9 (travagli delle anime + cosa devono fare direttori)** → capitoli su aridità, turbamento, prove della quiete infusa. Citazioni utili:
*Spiritus quidem promptus est, caro autem infirma* (Mt 26,41) → perfetta per descrivere la debolezza che questi capitoli trattano. 
*Secretum meum mihi* (Is 24,16, tradizione mistica) → molto usata per descrivere l'interiorità e il segreto divino. 

**II.10b Segni per conoscere se la gratia è di Dio o del Demonio**
Citazioni critiche:
*Dominus autem dirigat corda vestra…* (2 Ts 3,5) → citazione normativa di discernimento. 
*Soli Deo honor et gloria* (1 Tm 1,17) → conclusione teologicamente sorvegliata. 

### 3.3 Libro III - (mistica alta + glosse difensive)

**III.8 – matrimonio spirituale, cella secreta**
*Consummatum est* 
Gv 19,30

*In manus tuas, Domine, commendo spiritum meum* 
Lc 23,46

*Tristis est anima mea usque ad mortem* 
Mt 26,38 → spesso glossata perché potenzialmente rischiosa. 

*Dignare Domine die isto sine peccato nos custodire* 
Te Deum → liturgica, usata come protezione nei momenti di esposizione dottrinale. 

**III.9 passaggio alla cella di Dio, solitudine**
Citazioni tipiche per lo stato di solitudine infusa:

*Pater si vis transfer calicem istum a me…*
Lc 22,42 → evocazione della prova spirituale. 

*Deus meus, Deus meus, ut quid dereliquisti me?* 
Mc 15,34 → centrale nel tema della solitudine mistica. 

**III.12 – stato d'otio / operazione nel fondo dell'anima**
Citazioni compatibili col tema della quiete infusa:
*Deliciae meae esse cum filiis hominum* 
Prov 8,31 → delizie divine = stato di quiete. 

*Misericordias Domini…* → citazione perfetta per descrivere illuminazioni. 

**III.14 – santa ignoranza**
Citazioni utili per marcazione teologica:
*Iam hiems transiit… surge amica mea, et veni* 
(Ct 2,10–11) 
→ citazione sponsale perfetta per la trasformazione cognitiva. 

*Secretum meum mihi* 
(Is 24,16, tradizione di commento) 
→ ricorre nel contesto di "ignoranza sapiente". 

**III.24 – imitazione della Passione**
Citazioni centrali:
*Tristis est anima mea usque ad mortem* (Mt 26,38) → citazione-chiave, teologicamente delicata. 
*Salvum me fac Deus…* (Sal 68,2-3) → evocazione della prova in acque profonde. 

**III.34 – trasformazione totale / matrimonio spirituale**
Citazioni utili per i grafi:
*Vivo autem, iam non ego: vivit vero in me Christus* (Gal 2,20) → formula di trasformazione. 
*Amor meus crucifixus est…* (S. Ignazio) → intertesto patristico. 
*Cupio dissolvi, et esse cum Christo* (Fil 1,23) → desiderio di unione perfetta. 

**III.40 – ultima cella dell'anima**
Citazioni utili per concludere ciclo ascensionale:
*Astitit regina a dextris tuis…* (Sal 44,10) → culminazione sponsale. 
*Soli Deo honor et gloria* (Tm 1,17) → formula conclusiva. 

### 3.4 Authority list

#### 3.4.1 Salmi
- *In te Domine speravi* (Ps 30/31)
- *Misericordias Domini…* (Ps 88,2)
- *Vias mandatuorum…* (Ps 118,32)
- *Salvum me fac Deus…* (Ps 68,2-3)
- *Astitit regina…* (Ps 44,10)

#### 3.4.2 Vangeli 
- *Christus factus est…* (Fil 2,8)
- *Cupio dissolvi…* (Fil 1,23)
- *Vivo autem, iam non ego…* (Gal 2,20)
- *Consummatum est* (Gv 19,30)
- *Sitio* (Gv 19,28)
- *In manus tuas…* (Lc 23,46)
- *Pater si vis…* (Lc 22,42)
- *Deus meus…* (Mc 15,34)
- *Tristis est anima mea…* (Mt 26,38)
- *Spiritus quidem promptus est…* (Mt 26,41)

#### 3.4.3 Altre Scritture
- *Iam hiems transiit… surge amica mea, et veni* (Ct 2,10–11)
- *Secretum meum mihi* (Is 24,16)
- *Deliciae meae esse cum filiis hominum* (Prov 8,31)
- *Pater noster*
- *Dignare Domine…* (Te Deum)
- *Amor meus crucifixus est…* (Ignazio di Antiochia)

---

## 4. Citazioni rilevanti 
Razionale di scelta: rischio, chiarificazione, glosse, struttura canonica del discorso, stabilizzazione dottrinale, controfattuali IA.

### 4.1. Citazioni come legittimazione dottrinale
Le tre citazioni illustrano l'uso delle citazioni come dispositivi di stabilizzazione nei punti più esposti (umiltà, sicurezza, dilatazione spirituale. Le citazioni di seguito indicate ancorano il discorso mistico alla Scrittura e servono come pilastri dell'ortodossia.

**Salmi**
*In te Domine speravi, non confundar in eternum* 
Sal 70/71 
→ usata nel Libro I per fondare la virtù dell'umiltà 
I.5

*Misericordias Domini in eternum cantabo*
Sal 88,2 
→ citazione di stato mistico "di sicurezza", ricorrente nei momenti di luce divina.

*Vias mandatuorum tuorum cucurri, cum dilatasti cor meum*
Sal 118,32 
→ usata per la "dilatazione del cuore" nei capitoli di unione infusa.

### 4.2. Citazioni come ancoraggio cristologico
Queste tipologie coincidono con i nodi a rischio riconosciuti dall'Inquisizione (unione, sicurtà, annichilazione, trasformazione) usate da suor Teresa per evitare derive quietiste.

*Christus factus est pro nobis obediens usque ad mortem* 
Fil 2,8 
→ chiave di volta del capitolo sull'obbedienza 
I.6

*Consummatum est* 
Gv 19,30 
→ usata come citazione di sicurezza nei passaggi più esposti del matrimonio spirituale
III.8

*In manus tuas Domine, commendo spiritum meum* 
Lc 23,46 
→ ancoraggio alla Passione per arginare l'annichilazione mistica
 
*Sitio* - Gv 19,28 
→ tipica delle pene mistiche d'amore e dello stato sponsale 

### 4.3. Citazioni come marcatori di sofferenza / notte mistica
Citazioni centrali per la funzioni di recinzione semantica delle glosse; queste citazioni sono le più esposte e potenzialmente sospette

*Pater, si vis transfer calicem istum* 
Lc 22,42 
→ collegata allo stato di solitudine avanzata 
Libro III

*Deus meus, Deus meus, ut quid dereliquisti me?* 
Mc 15,34 
→ usata nelle descrizioni della notte dello spirito e della desolazione mistica 

*Tristis est anima mea usque ad mortem* 
Mt 26,38 
→ una delle più pericolose; è accompagnata da glosse attenuative per evitare sospetti quietisti
III.24 

*Spiritus quidem promptus est, caro autem infirma* 
Mt 26,41 
→ usata per spiegare gli inganni delle anime proficienti nel Libro II (discernimento) 
Libro II

### 4.4. Citazioni sponsali (Cantico dei Cantici)
Riferimenti mistico-sponsali come dispositivi canonici di legittimazione; sono il fondamento della mistica nuziale, ma anche possibile punto di rischio.

*Iam hiems transiit… surge amica mea, et veni* 
Ct 2,10–11 → usata nei capitoli della santa ignoranza e della piena trasformazione 
(III.14) 

### 5.5. Citazioni di rifinitura dottrinale
Questa tipologia chiude segmenti, marcano ortodossia e servono come sigilli teologici

*Soli Deo honor et gloria* 
Tm 1,17 
→ citazione conclusiva, sigillo di ortodossia in chiusura 
(Libro III)

*Dominus autem dirigat corda…* 
Ts 3,5 
→ associata al discernimento utile come citazione esatto congegno anti-moliniano
(II.10b)

### 5.6. Citazioni metafisiche e sapienziali
Connesse al movimento dell'intelletto e alla santa ignoranza; accompagnano glosse esplicative nei passaggi di maggiore complessità concettuale.

*Secretum meum mihi* 
Is 24,16 (secondo tradizione mistica) 
→ usato nei capitoli più delicati su intelletto e volontà, con funzione di smorzamento dottrinale 

*Deliciae meae esse cum filiis hominum* 
Prov 8,31 
→ citazione per l'otio divino e l'unione intellettuale 
(III.12) 

### 5.7. Citazioni patristiche - mistiche non bibliche
Citazioni rare e molto significative segnano il punto di contatto tra mistica canonica ed eccesso trasformativo.
*Amor meus crucifixus est, et ego cum illo* 
Ignazio di Antiochia 
→ asse teologico di trasformazione mistica 
(III.34) 

---

## 6. Glosse

Si riportano a seguire le glosse selezionate indicando funzione → rischio → valore. Sulle 30 selezionate si fornisce:
1.	Funzione retorico dottrinale (secondo il modello TEI)
2.	Rischio teologico - ermeneutico che la glossa disinnesca
3.	Valore diretto per il progetto (TEI+IA, intertestualità sorvegliata)

### 6.1. Attenuatio
funzione → modulano, smussano, neutralizzano formulazioni rischiose

**6.1.1 III.V,15 - Ciò non s'intende a cose di male**
Funzione → attenuatio: delimita il senso della perdita della volontà.
Rischio → accusa di antinomismo - negazione del libero arbitrio.
Valore → caso per mostrare come la glossa limiti l'interpretazione senza riscrivere il testo. 

**6.1.2 III.VI,2 - questo non s'intende… che non possono tornare**
Funzione → chiarisce che anche i perfetti possono peccare.
Rischio → dottrina quietista dell'impeccabilità.
Valore → esempio per l'esperimento IA "–GLOSSA", rimuovendola, l'ambiguità esplode. 

**6.1.3 III.VIII,8 - divenuta un altro Dio**
Funzione → attenuatio: sta da parte di Dio.
Rischio → deificazione sostanziale, proposizione inquisitoriale.
Valore → la glossa mostra come citazioni + glosse strutturano sicurezza dottrinale. 

**6.1.4 III.X,6 - passioni non "vive"**
Funzione → definisce l'effetto mistico senza negar corpo e passioni.
Rischio → dottrina della pura passività (moliniana).
Valore → mostra la micro chirurgia semantica dell'autrice. 

**6.1.5 III.XXXIX,5 - libertà ≠ libero arbitrio**
Funzione → separa libertà psicologica da libero arbitrio.
Rischio → accusa di annichilazione della volontà.
Valore → essenziale per spiegare il tema centrale: volontà vs consenso. 

**6.1.6 III.VII,6 - desiderio spento**
Funzione → riduce l'assolutezza dell'affermazione.
Rischio → interpretazione come apatheia eretica.
Valore → mostra come la glossa "temporizzi" un enunciato in apparenza assoluto. 

**6.1.7 III.X,6 - operazione divina e casa dell'anima**
Funzione → specifica che l'anima non perde attività ma calma le passioni.
Rischio → equivoco sulla dissoluzione operativa.
Valore → funzione chiarificante delle glosse. 

**6.1.8 II.VIII,37 - contemplazione illimitata**
Funzione → lo status di illimitata è chiarita come stato, non eccesso dottrinale.
Rischio → interpretazione come onniscienza infusa.
Valore → normalizza il vocabolario mistico estremo. 

### 6.2. Correctio
Funzione → correggono proposizioni dottrinalmente sbilanciate

**6.2.1 III.XXIV,20 - Passione non è impedimento**
Funzione → correctio: riformula un'espressione ambigua.
Rischio → accusa di svalutazione della Passione (tema inquisitoriale).
Valore → mostra il doppio registro, mistica alta + sorveglianza. 

**6.2.2 II.III,9 - penalità della meditazione**
Funzione → distingue penalità come sforzo, non come pena spirituale.
Rischio → confusione dottrinale sulla natura della meditazione.
Valore → mostra come le glosse rifiniscono il lessico ascetico. 

**6.2.3 II.II,2 - contemplazione acquisita**
Funzione → correctio su terminologia della contemplazione.
Rischio → equivoco tra otium passivo e otium attivo.
Valore → confronta versioni con/senza glosse. 

**6.2.4 II.II,3 - modo di cercare lo status delle anime**
Funzione → chiarisce mutamento del metodo contemplativo.
Rischio → accusa di inerzia spirituale (tema anti quietista).
Valore → mostra come le glosse guidano la semantica dell'azione. 

**6.2.5 III.V - opere divine**
Funzione → corregge l'apparente divinizzazione delle opere dell'anima.
Rischio → dottrina della infallibilità dei perfetti.
Valore → mappa il rischio dottrinale. 

### 6.3. Declaratio
Funzione → massima energia retorica, stile inquisitoriale

**6.3.1 III.XXXVIII,20 - Dio non tenta**
Funzione → declaratio: formula di ortodossia diretta.
Rischio → attribuire a Dio la tentatio (eresia diretta).
Valore → misura l'impatto della glossa sulla stabilità dottrinale. 

**6.3.2 III.XXXIX,3 - Dio non si perde nell'anima**
Funzione → declaratio: esplicita anti panteistica.
Rischio → confusione tra unione mistica e fusione essenziale.
Valore → esempla le glosse come dispositivi difensivi. 

**6.3.3 III.VIII,8 - sicurezza mistica con riserva**
Funzione → dichiara la sicurezza spirituale come effetto di Dio, non dell'anima.
Rischio → idee moliniste sulla sicurtà.
Valore → spiega la funzione anti sicurtaria. 

### 6.4. Explicatio - metalinguistiche
Funzione → glosse che spiegano concetti tecnici e rendono il testo "computabile"

**6.4.1 I.IV,7 - natura della notte**
Funzione → explicatio.
Rischio → confusione tra stato naturale e stato infuso.
Valore → esempla glosse come dis-ambiguatori semantici. 

**6.4.2 I.V,13 - chiarimento sulla virtù**
Funzione → esplicazione frequente.
Rischio → incomprensione della pedagogia spirituale.
Valore → mostra come le glosse operano anche a bassa intensità. 

**6.4.3 II.VIII,32 - luce e tenebre**
Funzione → esplica metafora mistica.
Rischio → lettura esoterica / ambiguità simbolica.
Valore → mostra il ruolo delle glosse nel controllo del linguaggio metaforico. 

### 6.5. Meccanismi esperienziali
Funzione → glosse che modulano la propria autorità.

**6.5.1 II.VIII,13 - superiorità dell'esperienza sui libri**
Funzione → segnala limite della dottrina astratta.
Rischio → interpretazione eccessivamente privatistica dell'esperienza.
Valore → supporta esemplificazioni di ethos e intertesto esperienziale. 

**6.5.2 II.XX,29 - insufficienza espressiva**
Funzione → dichiarazione di limite linguistico.
Rischio → fraintendimenti della dottrina per difficoltà espressiva.
Valore → mostra la performatività dell'umiltà retorica. 

### 6.6. Analogia - metafora

**6.6.1 II.III,9 - metafora della meditazione**
Funzione → corregge l'uso figurato di penalità.
Rischio → interpretazione letterale errata.
Valore → mostra come l'autrice evita scivolamenti metaforici pericolosi. 

**6.6.2 II.VIII,23 - comparazioni grossolane**
Funzione → dichiarazione meta-discorsiva.
Rischio → lettura inappropriata delle metafore corporee.
Valore → confronta linguaggio metaforico e glossato. 

### 6.7. Potenze - volontà

**6.7.1 II.II - sospensione dell'intelletto**
Funzione → definizione tecnica.
Rischio → interpretazione come annullamento dell'intelligenza.
Valore → esempla il concetto volere-intelletto e annichilazione. 

**6.7.2 III.XII,3–4 - otio di potenze**
Funzione → spiega lo stato mistico dell'infusione.
Rischio → fraintendimento della passività totale.
Valore → esempla il rischio quietista. 

### 6.8. Guida spirituale

**6.8.1 II.VII,12 - chi guida le anime**
Funzione → glossa di specificazione.
Rischio → confusione sui destinatari delle norme.
Valore → mostra la pedagogia della guida spirituale. 

**6.8.2 II.X,12 - limite linguistico**
Funzione → esplicita incapacità linguistica (non ho lettere).
Rischio → lettura erronea di passi tecnici.
Valore → segnala auto posizionamento umile dell'autrice. 

### 6.9. Sicurezza mistica

**6.9.1 III.VIII,34 - sicurezza condizionata**
Funzione → attenua una formula pericolosa sulla "sicurtà".
Rischio → sospetto di "sicurtà quietista".
Valore → mostra come la glossa traduce un eccesso in ortodossia. 

### 6.10. Trasformazione mistica

**6.10.1 III.XXXIX - trasformazione operativa, non essenziale**
Funzione → definisce la trasformazione come operativa.
Rischio → interpretazione panteistica.
Valore → glossa sulla logica della recinzione semantica. 

---

## 7. INTERTESTUALITÀ NEL CASTELLO 

### 7.1. Il rapporto con Teresa d'Ávila: continuità e rovesciamento
Nel Castello dell'anima, la presenza della tradizione teresiana emerge nella metafora del "castello", che nel Seicento religioso è uno dei nuclei più riconoscibili della mistica femminile. Tuttavia, il senso dell'immagine viene profondamente trasformato. Nel modello avilese, il castello è la struttura stessa dell'anima e il percorso mistico consiste nel penetrare progressivamente nelle sue stanze più interiori. Nel Castello siciliano, al contrario, l'immagine viene ricontestualizzata: non è l'anima a essere un castello, ma è l'"orazione" ad avere la forma di un edificio ascensivo. L'orante non entra in sé, ma costruisce un luogo interiore.  Questo spostamento semantico ha conseguenze decisive: (1) introduce una logica attiva (costruire) al posto di una logica introspettiva (entrare); (2) colloca l'esperienza mistica all'interno di una pedagogia ascetica più che visionaria; (3) crea un modello più compatibile con un contesto inquisitoriale, dove l'autonomia esperienziale poteva essere sospetta. (4) Qui l'intertestualità non è imitazione, ma rielaborazione regolativa: l'immagine tradizionale permette di aprire un linguaggio familiare, ma il suo significato viene spostato per assicurare tracciabilità e ortodossia.

### 7.2. Presenza della tradizione giovannea: tecnica delle potenze e logica della notte
Il Castello impiega una terminologia che riflette la sistemazione dottrinale elaborata nel Carmelo post-tridentino: analisi dei sensi interni ed esterni, distinzione delle facoltà spirituali (memoria–intelletto–volontà), descrizione della loro sospensione progressiva nella contemplazione. Nelle pagine dedicate ai sensi interiori (Libro II, cap. IV), la struttura retorica riproduce lo schema della purgazione graduale, che nella tradizione giovannea è strumento critico per spiegare: (1) il passaggio dalla meditazione discorsiva alla quiete, (2) l'oscurità che accompagna l'ingresso nella contemplazione, (3) la sospensione operativa dell'intelletto non come annullamento, ma come ricezione passiva di un atto divino.  Il modello della notte diventa una grammatica concettuale che permette a un'autrice laica di trattare concetti ad altissimo rischio (sospensione, annichilazione, passività), disponendoli però dentro una cornice riconoscibile e accettata. In questo senso, l'intertestualità tecnica serve come argine dottrinale in cui l'autrice adotta schemi consolidati per parlare di ciò che potrebbe essere equivocato come quietismo.

### 7.3. Metafore mistiche femminili: attrazione, amore, calamita
Nel discorso sulla virtù dell'umiltà, l'immagine della calamita che attira Dio assume un valore dottrinale e autoriale. L'immagine, presente nella tradizione mistica toscana e ligure (Maria Maddalena de' Pazzi), non introduce un eccesso visionario, ma un modo di parlare del rapporto tra l'anima e la grazia senza usare categorie teologicamente controverse. La metafora permette di esprimere (1) l'intensità dell'unione mistica, (2) la logica della reciprocità tra Dio e l'anima, (3) la dinamica affettiva della contemplazione. Tutto ciò sarebbe rischioso se formulato come "possesso", "fusione", "trasformazione essenziale". L'immagine affettiva, derivata dalla tradizione delle mistiche italiane, neutralizza il rischio e lo inscrive in un codice già approvato.

### 7.4. L'orizzonte della nuova mistica: consonanze con Molinos e necessità di difese
Nel testo emerge una costellazione di concetti che circolano nel quietismo europeo: quiete, passività, sospensione delle potenze, guida sostanzialmente inutile dopo la perfetta unione. Il Castello ne riproduce alcuni elementi, ma lo fa con un eccesso di cautela e attraverso continue glosse che ne delimitano il senso. L'autrice riconosce che può essere interpretata secondo un linguaggio sospetto e per questo inserisce autodifese: (1) esplicita dissociazione da "molinia"; (2) continuo ricorso all'obbedienza; (3) distinzione tra operazione divina e concorso umano.  L'intertestualità qui è "liminare"; ad esempio, non viene nominato Molinos, ma la sua struttura concettuale è riconoscibile e viene assorbita, addomesticata, sorvegliata.

### 7.5. Agiografia e genealogie femminili come rete di legittimazione
L'autrice non si presenta isolata ma si colloca consapevolmente entro una catena di donne che hanno ricevuto, insegnato e trasmesso dottrine elevate. Esempi citati nel testo fanno riferimento a Geltrude di Helfta, Chiara da Montefalco e a Caterina da Siena. Queste figure svolgono una funzione duplice, (1) legittimazione: mostrano che una donna può ricevere dottrina divina senza mediazione maschile; (2) moderazione: il riferimento a sante canonizzate disinnesca l'accusa di presunzione spirituale. L'intertestualità qui produce un ethos di affidabilità, in cui l'autrice si inserisce dentro una tradizione riconosciuta.

### 7.6. Intertestualità culturale
La presenza di formule che provengono dalla tradizione letteraria profana, come la massima *amor con amor si paga* (Seneca → Petrarca → tradizione devota: Celestina), non introduce un elemento estraneo, ma offre un registro retorico familiare alle lettrici e ai lettori del tempo. Questa circolazione culturale serve a rendere più accessibile un contenuto ascetico elevato; a inscrivere l'opera in una tradizione morale condivisa e a alleggerire concetti altrimenti astratti. 

### 7.7. Intertesto esperienziale: l'esperienza personale come fonte legittimante
Il testo fa ampio uso della formula *non parlo senza l'esperienza* in contesti centrali della direzione spirituale e del discernimento. Questa strategia non è retorica ma è un rimando mistico vero e proprio. L'esperienza, nel quadro femminile post tridentino, sostituisce l'autorità dottrinale e diventa un'intertestualità interna, dove l'autrice richiama il proprio vissuto come fonte del discorso spirituale. La sua esperienza è modellata su quella delle mistiche canoniche.

---

## Appendice
### AUTHORITY FILE

#### 1. BIBLIA — Vulgata / Nova Vulgata

| Sigla | Citazione | Riferimento | Nota d'uso |
| :--- | :--- | :--- | :--- |
| Ps 30(31), 1 | In te Domine speravi, non confundar in aeternum | Biblia Sacra Vulgata | Citazione legittimante (Libro I) |
| Ps 88(89), 2 | Misericordias Domini in aeternum cantabo | BV | Stato mistico di sicurezza |
| Ps 118(119), 32 | Vias mandatuorum tuorum cucurri… | BV | Dilatazione del cuore |
| Ps 68(69), 2–3 | Salvum me fac Deus… | BV | Notte mistica / prove |
| Ps 44(45), 10 | Astitit regina a dextris tuis | BV | Culmine sponsale |
| Ct 2, 10–11 | Iam hiems transiit… surge amica mea | BV | Citazione sponsale (III.14) |
| Is 24,16 | Secretum meum mihi | BV | Tradizione mistica, sapere nascosto |
| Prov 8,31 | Deliciae meae esse cum filiis hominum | BV | Stato di quiete infusa |
| Mt 26,38 | Tristis est anima mea usque ad mortem | NV | Citazione ad alto rischio |
| Mt 26,41 | Spiritus promptus est, caro autem infirma | NV | Discernimento |
| Mc 15,34 | Deus meus, Deus meus… | NV | Notte spirituale |
| Lc 22,42 | Pater si vis transfer calicem istum | NV | Solitudine infusa |
| Lc 23,46 | In manus tuas, Domine… | NV | Ancoraggio alla Passione |
| Gv 19,28 | Sitio | NV | Stato sponsale / pene d'amore |
| Gv 19,30 | Consummatum est | NV | Sicurezza mistica (III.8) |
| Fil 1,23 | Cupio dissolvi et esse cum Christo | NV | Unione perfetta |
| Fil 2,8 | Christus factus est pro nobis obediens… | NV | Pivot cristologico |
| Gal 2,20 | Vivo autem iam non ego… | NV | Trasformazione totale |
| 1 Tm 1,17 | Soli Deo honor et gloria | NV | Sigillo conclusivo |
| 2 Ts 3,5 | Dominus autem dirigat corda vestra… | NV | Anti-quietista; discernimento |

#### 2. LITURGIA

| Citazione | Fonte | Contesto |
| :--- | :--- | :--- |
| Pater noster, qui es in caelis | Liturgia Romana | Orazione d'unione, stato infuso |
| Dignare Domine die isto sine peccato nos custodire | Te Deum | Protezione dottrinale |

#### 3. PATRISTICA

| Citazione | Autore | Opera / Nota |
| :--- | :--- | :--- |
| Amor meus crucifixus est, et ego cum illo | Ignazio di Antiochia | Ad Romanos 7, 2 — usato per trasformazione mistica |
| Secretum meum mihi (ricezione) | Tradizione esegetica | Uso patristico e medievale (Gregorio, Bernardo) |

#### 4. MISTICA (post-tridentina, carmelitana, italiana)

| Autore | Riferimento | Nota |
| :--- | :--- | :--- |
| Teresa d'Ávila | Castillo interior | Modello rovesciato nel Castello |
| Giovanni della Croce | Subida / Noche | Schema purgativo, sospensione potenze |
| Miguel de Molinos | Guía espiritual | Contro-modello implicito, rischio |
| Maria Maddalena de' Pazzi | Revelazioni | Metafora della calamita |
| Geltrude di Helfta | Legatus divinae pietatis | Genealogia mistica |
| Chiara da Montefalco | Vita et revelationes | Esempio di mistica del cuore |
| Caterina da Siena | Dialogo | Modello di autorità femminile |

#### 5. AGIOGRAFIA

| Santa | Opera / Fonte base | Funzione |
| :--- | :--- | :--- |
| Santa Maria Maddalena | Tradizione esegetica / agiografica | Esempio di conversione |
| Santa Rosalia | Vita secentesca siciliana | Modello ascetico locale |
| Santa Geltrude | Vitae | Genealogia mistica |
| Santa Chiara da Montefalco | Vitae | Mistica del cuore |
| Santa Caterina da Siena | Legenda Major (Raymondo da Capua) | Legittimazione dottrinale |
