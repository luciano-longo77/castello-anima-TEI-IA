# Base dati per il campionamento
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

## Indice

1. [Dataset](#1-dataset)
   - 1.1 [Libro I (Anime principianti)](#11-libro-i-anime-principianti)
   - 1.2 [Libro II (Anime proficienti)](#12-libro-ii-anime-proficienti)
   - 1.3 [Libro III (Anime perfette)](#13-libro-iii-anime-perfette)
2. [Razionale dei capitoli selezionati](#2-razionale-dei-capitoli-selezionati)
   - 2.1 [Razionale](#21-razionale)
   - 2.2 [Selezione Libro I: motivazioni](#22-selezione-libro-i-motivazioni)
   - 2.3 [Selezione Libro II: motivazioni](#23-selezione-libro-ii-motivazioni)
   - 2.4 [Selezione Libro III: motivazioni](#24-selezione-libro-iii-motivazioni)
   - 2.5 [Dataset e Guida al modello](#25-dataset-e-guida-al-modello)
3. [Citazioni utili alla base dati](#3-citazioni-utili-alla-base-dati)
   - 3.1 [Libro I](#31-libro-i)
   - 3.2 [Libro II](#32-libro-ii)
   - 3.3 [Libro III](#33-libro-iii)
   - 3.4 [Authority list](#34-authority-list)
4. [Citazioni rilevanti](#4-citazioni-rilevanti)
   - 4.1 [Legittimazione dottrinale](#41-citazioni-come-legittimazione-dottrinale)
   - 4.2 [Ancoraggio cristologico](#42-citazioni-come-ancoraggio-cristologico)
   - 4.3 [Marcatori di sofferenza / notte mistica](#43-citazioni-come-marcatori-di-sofferenza--notte-mistica)
   - 4.4 [Citazioni sponsali (Cantico dei Cantici)](#44-citazioni-sponsali-cantico-dei-cantici)
   - 4.5 [Citazioni di rifinitura dottrinale](#45-citazioni-di-rifinitura-dottrinale)
   - 4.6 [Citazioni metafisiche e sapienziali](#46-citazioni-metafisiche-e-sapienziali)
   - 4.7 [Citazioni patristiche-mistiche non bibliche](#47-citazioni-patristiche-mistiche-non-bibliche)
6. [Glosse — matrice tipizzata sugli assi di tassonomia-gh.xml](#6-glosse--matrice-tipizzata-sugli-assi-di-tassonomia-ghxml)
7. [Intertestualità nel Castello](#7-intertestualità-nel-castello)
   - 7.1 [Teresa d'Ávila: continuità e rovesciamento](#71-il-rapporto-con-teresa-dávila-continuità-e-rovesciamento)
   - 7.2 [Tradizione giovannea: potenze e notte](#72-presenza-della-tradizione-giovannea-tecnica-delle-potenze-e-logica-della-notte)
   - 7.3 [Metafore mistiche femminili](#73-metafore-mistiche-femminili-attrazione-amore-calamita)
   - 7.4 [L'orizzonte della *nuova mistica*](#74-lorizzonte-della-nuova-mistica-consonanze-con-molinos-e-necessità-di-difese)
   - 7.5 [Agiografia e genealogie femminili](#75-agiografia-e-genealogie-femminili-come-rete-di-legittimazione)
   - 7.6 [Intertestualità culturale](#76-intertestualità-culturale)
   - 7.7 [Intertesto esperienziale](#77-intertesto-esperienziale-lesperienza-personale-come-fonte-legittimante)
- [Appendice — Authority File](#appendice--authority-file)

## Introduzione

Il presente documento descrive la struttura del dataset utilizzato per l'edizione digitale e l'analisi computazionale del *Castello dell'anima* di suor Teresa di San Geronimo. L'obiettivo è fornire una base dati chiara, riusabile e trasparente per la pipeline TEI+IA sviluppata nel progetto, in cui la codifica TEI P5, l'analisi delle funzioni retorico‑dottrinali e la generazione controllata di varianti controfattuali (-CIT, +TEXTsub, +CIT) operano in modo integrato. Il dataset raccoglie i capitoli dei tre libri dell'opera che presentano maggiore rilevanza per la ricerca: sezioni ad alta sensibilità dottrinale, segmenti con densità intertestuale significativa e passaggi caratterizzati da glosse autoriali, chiarificazioni e dispositivi di sorveglianza. Per ciascun capitolo viene indicato il motivo della selezione, in relazione ai fenomeni mistici, pedagogici o prudenziali che il modello TEI deve rappresentare. Accanto alla definizione del campione, il documento include un'authority list completa delle citazioni bibliche, liturgiche, patristiche e mistiche utilizzate nel testo, con una classificazione funzionale (legittimazione, ancoraggio cristologico, marcatori di sofferenza, citazioni sponsali, sigilli dottrinali). Una sezione dedicata raccoglie inoltre le glosse selezionate come **matrice tipizzata sugli assi della tassonomia** (`operation`+F, `func`, `risk`, `mystic_state`/`relation`, `impact`), con i valori N, A e I calcolati per ciascuna occorrenza. Chiude il documento un quadro sintetico dell'intertestualità del Castello, che include riferimenti alla tradizione teresiana, giovannea e alle mistiche femminili post‑tridentine, oltre a elementi di quietismo, agiografia e intertestualità culturale. Insieme, questi materiali costituiscono la base metodologica, filologica e computazionale per l'intera analisi del manoscritto e garantiscono la piena riusabilità del dataset nel repository.

Questo documento costituisce la documentazione ufficiale del dataset utilizzato nel progetto *Intertestualità sotto sorveglianza: modello TEI+IA per il Castello dell'anima*. Raccoglie e descrive:

- i capitoli selezionati dei tre libri dell'opera,
- i criteri filologici e dottrinali della selezione,
- l'authority list delle citazioni bibliche, liturgiche, patristiche e mistiche,
- la tipizzazione delle glosse presenti nel manoscritto,
- una sintesi dell'intertestualità strutturale dell'opera, fondamentale per l'annotazione TEI interpretativa e per gli esperimenti IA.

Il documento è concepito per essere riusabile, trasparente e interoperabile con:

- i file TEI *castello-anima-teiText.xml*, *castello-anima-teiHeader.xml* e *tassonomia-gh.xml* (TEI P5),
- la pipeline IA controllata (procedure -CIT, +TEXTsub, +CIT),
- *Guida TEI-driven*.

## Scopo del documento

1. Definire il dataset utilizzato per l'analisi TEI+IA del *Castello dell'anima*.
2. Motivare la selezione dei capitoli, secondo criteri di:
   - *sensibilità dottrinale,*
   - *densità intertestuale,*
   - *presenza di glosse e dispositivi prudenziali,*
   - *utilità per esperimenti computazionali.*
3. Fornire un'authority list unificata delle citazioni canoniche.
4. Fornire una matrice di glosse con funzione, rischio e valore per la pipeline IA.
5. Documentare i principi di intertestualità sorvegliata rilevanti per l'encoding TEI.

## Versioning
 **Dataset version**: v2.0
- **v0.0** (2026-03-09)
- **v1.1** (2026-03-25)
- **v1.2** (2026-04-01)
- **v1.3** (2026-08-07)
- **v1.9** (2026-08-12)
- **v2.0** (2026-08-12)

## Uso del documento

Questo documento è incluso nella cartella `docs/` del repository:

- accompagna il file TEI come descrizione metodologica del dataset;
- supporta la generazione di varianti IA;
- guida analisi, query e pattern TEI;
- consente la replicabilità degli esperimenti.

## Struttura del documento

1. *Dataset* → capitoli selezionati e motivazioni
2. *Razionale* metodologico della selezione
3. *Authority list* delle citazioni
4. *Citazioni* classificate per funzione e rischio
5. *Glosse* tipizzate
6. *Intertestualità* strutturale
7. *Allegati* e riferimenti critici

## 1. Dataset

Lista completa dei capitoli che rispondono ai criteri di:

1. sensibilità dottrinale,
2. densità intertestuale,
3. presenza di glosse o dispositivi di sorveglianza,
4. rilevanza per gli esperimenti TEI+IA (-CIT, +TEXTsub, +CIT).

Il campione consta di **29 loci di selezione** (corrispondenti a **36 capitoli**, poiché `I.1–2`, `II.1–2` e `II.4–5` raggruppano più capitoli e i capitoli `III.2–5` sono inclusi per intero come raccordo), distribuiti nei tre libri: 5 loci nel Libro I, 9 nel Libro II, 15 nel Libro III.

### 1.1. Libro I (Anime principianti)

**→ funzione**: pedagogia + ethos

| Capitolo | Titolo | Motivo della selezione |
|---|---|---|
| I.1–2 | Si tratta della miseria humana / Come il mondo è una continua guerra… | Costruzione dell'**ethos**; assenza di citazioni → ideale per esperimenti **+CIT** |
| I.4 | *Come per dar principio al Castello dell'anima è necessaria la notte de' sensi* (metafora del castello) | Fonda la **metafora-castello** (l'orazione come edificio ascensivo, rovesciamento avilese) e la notte dei sensi; glossa §6 6.4.1 → base testuale all'intertesto teresiano |
| I.5 | Virtù dell'humiltà (Salmo *In te Domine speravi*) | Citazione strategica → segmento **legittimante** |
| I.6 | Virtù dell'obedienza (*Christus factus est…*) | Citazione cristologica → perfetto per **-CIT / +CIT** |
| I.11 | *Virtù del distacco* | Snodo pedagogico con citazione → 2° sito **+CIT** di Libro I |

### 1.2. Libro II (Anime proficienti)

**→ funzione**: discernimento + rischio dottrinale

| Capitolo | Titolo | Motivo della selezione |
|---|---|---|
| II.1–2 | Dispositione dell'anima | Fondazione dottrinale del discernimento → baseline |
| II.3 | *Anime che incominciano ad entrare nella contemplatione* | Soglia dell'ingresso contemplativo; glosse §6 6.2.2/6.6.1 → fascia media dell'indice |
| II.4–5 | *Seconda notte / stati di notte oscura* | Intertesto **giovanneo** (Subida/Noche); catene notte→quiete |
| II.7 | *S'incomincia a trattare della contemplatione infusa (oratione di quiete)* | Cuore **quietista** (quiete ×16); glossa §6 6.8.1 → banco **−CIT** |
| II.8 (a–d) | Oratione d'unione | Nodo critico: consonanza con Molinos, casi concreti, rischio di quietismo; ideale per **-CIT / +CIT** |
| II.9a–b | Travagli delle anime | Casistica mistica → esperimenti di spostamento citazionale |
| II.10b | Segni per conoscere se la gratia è di Dio o del Demonio | Segmento normativo ad alta sensibilità; utile per **stress test IA** |
| II.20 | *Pene più dense* | Densità di glosse massima del blocco pene; glossa §6 6.5.2 |
| II.21 | *Pene doppo i sollievi* — «Mi dichiaro… se Dio l'abandonasse» (inchiostro scuro) | **Declaratio critica** (impeccabilità) §6 6.3.3 **e** strato **T3** ink_3-dark → primo `impact-critical` e primo T3 in Libro II |

### 1.3. Libro III (Anime perfette)

**→ funzione**: mistica alta + glosse difensive

| Capitolo | Titolo | Motivo della selezione |
|---|---|---|
| III.1 | *Si tratta della dispositione che lascia nell'anima la notte dello spirito* (c. 158r) | Soglia del Libro III: ingresso nella fase purgativa; baseline a bassa densità citazionale, comparabile a I.1–2 e II.1–2 → contrappunto strutturale |
| III.6 | *Nudità dell'anima e bacio* (c. 168v) | Preparazione al matrimonio spirituale; glossa §6 6.1.2 (impeccabilità) |
| III.7 | *Matrimonio spirituale che Dio fa con l'anima* (c. 173v) | Picco **panteismo**: «un altro Dio» ×3; glosse §6 6.1.3/6.1.6 |
| III.8 | *Cella secreta / matrimonio spirituale* (c. 175v) | Capitolo più ricco di glosse difensive: «l'anima divenuta un altro Dio» (c. 178v) mitigata da «totale sicurtà… non per fidar di sé stessa»; «una sicurtà… se Dio ci lasciasse potremo di nuovo cadire» (c. 178r) |
| III.10 | *Soggillo che Dio pone all'anima* (c. 182v) | *Annichilazione* ×4 (quietismo); glosse §6 6.1.4/6.1.7 |
| III.12 | *Stato d'otio / operazione di Dio nel fondo* | Segmento di unione alta, senza glosse → banco per **+CIT / +TEXTsub** |
| III.14 | *Santa ignoranza* | Concetto teologicamente esposto; alta utilità per analisi controfattuale |
| III.16 | *Certa sorte d'unione straordinaria* (c. 197v) | Alta densità glosse/rischio; impeccabilità |
| III.19 | *Molte sorte d'unione naturale e supernaturale* (c. 207v) | Distinzione naturale/**sovrannaturale** → punto più esposto al sospetto inquisitoriale |
| III.24 | *Non si medita la passione, ma si "emita" Tristis est anima mea* | Citazione semiliturgica pericolosa → nodo critico |
| III.32 | *Trasformatione nel crocefisso* (c. 241v) | Citazioni della **Passione** (*Consummatum est*, *In manus tuas*) → ancoraggio cristologico |
| III.34 | *Trasformatione totale / matrimonio spirituale* | Culmine teologico → ideale per grafi intertestuali |
| III.38 | *Sigillo d'ortodossia — «mi dichiaro»* (c. 256v) | **Declaratio critica** §6 6.3.1 |
| III.39 | *«Mi dichiaro» + annichilazione* (c. 259v) | **Declaratio critica** + *annichil* ×5; glosse §6 6.3.2/6.10.1 (panteismo) |
| III.40 | *Ultima cella dell'anima* (ultimo capitolo) | Segmento finale per chiudere il ciclo ascensionale |

## 2. Razionale dei capitoli selezionati

- **Libro I** — I.1–2; I.4; I.5; I.6; I.11
- **Libro II** — II.1–2; II.3; II.4–5; II.7; II.8 a–d; II.9 a–b; II.10b; II.20; II.21
- **Libro III** — III.1; III.6; III.7; III.8; III.10; III.12; III.14; III.16; III.19; III.24; III.32; III.34; III.38; III.39; III.40

### 2.1. Razionale

Il dataset necessario per l'analisi TEI+IA del *Castello dell'anima* è costruito in modo coerente con la metodologia del progetto, integrando la prospettiva filologica, quella retorico-dottrinale e la sperimentazione computazionale prevista dalla pipeline IA controllata. La selezione del campione segue tre criteri principali: la sensibilità dottrinale, la densità intertestuale e la comparabilità strutturale tra i tre libri. La prima esigenza deriva dal fatto che l'opera presenta una serie di snodi nei quali il discorso mistico diviene potenzialmente ambiguo, soprattutto quando tocca temi come l'unione trasformante, la sicurezza dell'anima, l'obbedienza e il discernimento delle mozioni interiori; è in questi luoghi che glosse e citazioni agiscono come dispositivi di chiarificazione e di recinzione semantica, e l'introduzione individua precisamente nel Libro II e nel Libro III le zone a maggiore rischio inquisitoriale e con più alta densità di glosse difensive. La seconda esigenza riguarda invece i capitoli che presentano citazioni bibliche, liturgiche o mistico-dottrinali utilizzate come meccanismi di stabilizzazione; in particolare, il capitolo sull'umiltà (Libro I), quello sull'obbedienza (Libro I), il capitolo VIII del Libro II e il capitolo VIII del Libro III, dove le citazioni si combinano con glosse e note di attenuazione. Infine, la comparabilità tra i libri richiede che il campione includa testi di estensione simile e di natura retorica complementare: la pedagogia spirituale del Libro I, il discernimento normativo del Libro II e la mistica alta e vigilata del Libro III, come l'introduzione esplicitamente prescrive. A partire da questi criteri, il dataset comprende **ventinove loci di selezione** (trentasei capitoli, poiché `I.1–2`, `II.1–2` e `II.4–5` raggruppano più capitoli e i capitoli `III.2–5` sono inclusi per intero come raccordo), così distribuiti: cinque nel Libro I, nove nel Libro II e quindici nel Libro III.

### 2.2. Selezione Libro I: motivazioni

Dal Libro I vengono selezionati i capitoli 1–2, 5 e 6. I primi due capitoli, dedicati alla *miseria humana* e alla verità rivelata, introducono la voce autoriale e costruiscono l'ethos della scrivente attraverso osservazioni autobiografiche e modelli di conversione come san Francesco, santa Maria Maddalena e santa Rosalia, elementi ben attestati nell'edizione; sono capitoli privi di citazioni formali e risultano preziosi per gli esperimenti IA di aggiunta artificiale di citazioni. Il capitolo sull'umiltà contiene invece la citazione salmica *In te Domine speravi, non confundar in aeternum*, indicata dalla Guida come esempio paradigmatico di citazione "legittimante" capace di rendere più chiaro e sorvegliato il discorso. Il capitolo sull'obbedienza presenta la citazione cristologica *Christus factus est pro nobis obediens usque ad mortem*, che costituisce l'architrave concettuale dell'argomentazione morale e permette di testare l'impatto della rimozione o della restituzione equifunzionale (+CIT).

L'ampliamento aggiunge i capitoli **4** e **11**. Il capitolo 4 — «Come per dar principio al Castello dell'anima è necessaria la notte de' sensi» — fonda la **metafora architettonica del castello** (l'orazione come edificio ascensivo, rovesciamento del modello avilese) e reca una glossa di delimitazione (§6 6.4.1): dà finalmente base testuale all'intertesto teresiano oggi solo argomentato. Il capitolo 11 (virtù del distacco) offre un secondo sito citazionale utile agli esperimenti **+CIT**.

### 2.3. Selezione Libro II: motivazioni

Dal Libro II vengono selezionati l'inizio (capitoli 1–2) e il capitolo VIII. I primi servono come baseline dottrinale e contengono la definizione delle tre fonti di inganno spirituale (mondo, carne, demonio), articolando una pedagogia normativa senza glosse. Il capitolo VIII è invece la sezione più sensibile del Libro II: esso contiene casi concreti di discernimento delle mozioni, descrizioni delle ripugnanze e confusioni dell'anima, critica verso i direttori spirituali incompetenti e ampi passaggi che richiamano implicitamente la tripartizione della *Guida spirituale* di Molinos, come evidenziato sia nell'introduzione sia nella Guida TEI-driven. Questo capitolo è ideale per gli esperimenti di rimozione (-CIT) e restituzione (+CIT) dei presìdi citazionali e glossematici, permettendo di osservare come la loro assenza modifichi stabilità dottrinale, chiarezza argomentativa e coesione interna.

L'ampliamento estende il Libro II alla **soglia contemplativa** e al **blocco delle pene**: il capitolo **3** documenta l'ingresso nella contemplazione infusa (glosse §6 6.2.2/6.6.1); i capitoli **4–5** portano l'intertesto **giovanneo** della notte oscura; il capitolo **7** («S'incomincia a trattare della contemplatione infusa, oratione di quiete») è il nucleo **quietista** più prossimo a Molinos (glossa §6 6.8.1); i capitoli **20–21** coprono il blocco delle pene, con il capitolo **21** che contiene la terza *declaratio* dell'opera — «Mi dichiaro… se Dio l'abandonasse», glossa tardiva a inchiostro scuro (strato **T3**) e sigillo d'ortodossia di banda **critica** sull'impeccabilità (§6 6.3.3).

### 2.4. Selezione Libro III: motivazioni

Dal Libro III vengono selezionati **quindici loci** — III.1, III.6, III.7, III.8, III.10, III.12, III.14, III.16, III.19, III.24, III.32, III.34, III.38, III.39, III.40 — che coprono l'intero arco della mistica alta e vigilata. I capitoli contigui III.2–III.5, inclusi per intero come raccordo, documentano la transizione osservabile fra la soglia (III.1) e il picco difensivo (III.8), rendendo continua — e non solo per estremi — la curva della densità prudenziale nel Libro III.

Il capitolo I (c. 158r) funge da **soglia purgativa** a bassa densità difensiva, contrappunto strutturale a I.1–2 e II.1–2; i capitoli **8 e 12** costituiscono i poli di massima e minima densità difensiva, attorno ai quali si organizza in profondità l'analisi controfattuale; i capitoli 14, 24, 34 e 40 scandiscono i nodi successivi dell'itinerario ascensionale (santa ignoranza, imitazione della Passione, trasformazione totale, sigillo conclusivo). 

Il capitolo VIII (c. 175v) presenta il nucleo più alto della mistica teresiana: unione, matrimonio spirituale, sicurezza dell'anima e la gestione dell'iperbole «l'anima divenuta un altro Dio» (c. 178v, §34), mitigata non per via sostanziale ma dal contesto prudenziale — «vedendosi tanto da lui fortificata», «totale sicurtà, e questo non per fidar di sé stessa» (c. 178v) — mentre il nodo della «sicurtà» è delimitato da «una sicurtà, però è di bene pensare, che se Dio ci lasciasse potremo di nuovo cadire» (c. 178r, §29). La formula anti-sostanziale «(un altro Dio) per particepatione» è invece il leitmotiv dei capitoli precedenti del blocco matrimoniale (III.5, c. 167v; III.6, c. 171v; III.7, c. 173r), e «per quanto sta da parte di Dio» appartiene a III.7 (c. 173v). Le citazioni cristologiche della Passione (*Consummatum est*, *In manus tuas, Domine, commendo spiritum meum*) non appartengono a questo capitolo ma ai capp. XXXI–XXXII (cc. 241v–243v). Il capitolo è caratterizzato inoltre dal ricorso prudenziale al refrain «dovemo sempre temere» / «mai fidarci di noi stessi» (§§28, 34), meccanismo di auto-mitigazione e di sorveglianza del discorso teologico. 

Si tratta della sezione più adatta per gli esperimenti di rimozione citazionale (-CIT), di restituzione (+CIT) e di recupero delle cancellature autoriali (+TEXTsub), poiché consente di misurare con precisione la funzione stabilizzante delle glosse e delle correzioni autoriali. Il capitolo XII, invece, espone l'ozio delle potenze al rischio quietista ma risulta strutturalmente privo di glosse difensive esplicite; questa minima densità difensiva ne fa il contrappunto ideale a III.8 e il banco di prova per la restituzione di citazioni (+CIT) e il recupero di eventuali cancellature (+TEXTsub), così da valutarne l'effetto sulla coerenza argomentativa.

L'ampliamento del Libro III chiude i vuoti rispetto alla **matrice glosse §6** e all'arco dottrinale. Il blocco del **matrimonio spirituale** — capitoli **6** (nudità/bacio, impeccabilità), **7** («un altro Dio» ×3, panteismo) e **10** (soggillo, annichilazione) — porta nel campione le glosse 6.1.2, 6.1.3, 6.1.6, 6.1.4 e 6.1.7, finora orfane; il capitolo **16** aggiunge una sorte straordinaria d'unione ad alta densità, il capitolo **19** la distinzione fra unione **naturale e sovrannaturale** (il punto più esposto al sospetto inquisitoriale), il capitolo **32** le citazioni cristologiche della **Passione** (*Consummatum est*, *In manus tuas*). Infine i capitoli **38** e **39** portano le due *declaratio* critiche restanti — le «mi dichiaro» di banda `impact-critical` (glosse 6.3.1, 6.3.2, 6.10.1) — che completano, con **II.21**, la copertura di **tutte e tre** le declaratio d'ortodossia dell'opera.

### 2.5. Dataset e Guida al modello

L'intero dataset può essere rappresentato in TEI P5 secondo lo schema proposto nella Guida, che prevede l'uso di elementi come `<cit></cit>`, `<quote></quote>`, `<ref></ref>`, `<note type="glossa" subtype="attenuatio"></note>` e dell'attributo `@ana` per annotare funzioni retoriche e impatti esplicativi. La struttura del documento TEI, articolata in unità di libro e di capitolo, consente di integrare citazioni bibliche con attributi specifici, glosse autoriali, rimandi interni e segmenti testuali pertinenti agli esperimenti IA. Grazie a questa configurazione, il dataset supporta pienamente l'intera pipeline sperimentale — rimozione (-CIT), restituzione delle citazioni (+CIT) e recupero delle cancellature autoriali (+TEXTsub), misurazione delle variazioni in chiarezza, coesione e stabilità dottrinale — e rende possibile una valutazione computazionale replicabile dell'intertestualità mistica post-tridentina secondo il modello TEI+IA.

## 3. Citazioni utili alla base dati

### 3.1. Libro I

*(pedagogia + ethos)*

**I.1–2** — Nessuna citazione formale → per esperimenti **+CIT**: aggiunta controllata di citazioni bibliche in stile.

**I.5** — Virtù dell'umiltà  
*In te Domine speravi, non confundar in aeternum* — Ps 70(71) (c. 13r)  
→ citazione legittimante, frequente nella mistica dell'umiltà; la stessa lezione ricorre in III.24 (cc. 220v-221r).

**I.6** — Virtù dell'obbedienza  
*Christus factus est pro nobis obediens usque ad mortem* — Fil 2,8 (c. 14r)  
→ pivot cristologico, altissimo impatto esplicativo.

### 3.2. Libro II

*(discernimento + rischio dottrinale)*

**II.1–2** — Baseline dottrinale  
*Spiritus promptus est* — Mt 26,41 (attestata a c. 25r)  
→ utile per IA: aggiunta/restituzione di citazioni normative (+CIT).

**II.8** — Orazione d'unione + effetti + avvertimenti *(contesto vicino a Molinos → test per glosse)*. Citazioni utili del corpus (ricorrenti nei capitoli mistici sulla quiete/unione):

- *Pater noster, qui es in caelis* (formula liturgica; c. 21r) → molto ricorrente nelle sezioni di unione.
- *Misericordias Domini in aeternum cantabo* — Sal 88,2 (cc. 92r, 182r, 203v) → citazione di stato gioioso/illuminativo.
- *Vias mandatuorum tuorum cucurri, cum dilatasti cor meum* — Sal 118,32 (c. 78r) → tipica delle sezioni di dilatazione del cuore.

**II.9** (travagli delle anime + cosa devono fare i direttori) → capitoli su aridità, turbamento, prove della quiete infusa. Citazioni utili:

- *Spiritus quidem promptus est, caro autem infirma* (Mt 26,41; c. 25r) → perfetta per descrivere la debolezza che questi capitoli trattano.
- *Secretum meum mihi* (Is 24,16, tradizione mistica; cc. 29v, 66v, 148v, 175v) → molto usata per descrivere l'interiorità e il segreto divino.

**II.10b** — Segni per conoscere se *la gratia è di Dio o del Demonio*. Citazioni critiche:

- *Dominus autem dirigat corda vestra...* (2 Ts 3,5; cc. 255v, 256r) → citazione normativa di discernimento.
- *Soli Deo honor et gloria* (1 Tm 1,17; cc. 253r, 263r) → conclusione teologicamente sorvegliata.

### 3.3. Libro III

*(mistica alta + glosse difensive)*

**III.8** — matrimonio spirituale, cella secreta (c. 175v). Dispositivi regolativi reali del capitolo (glosse, non citazioni latine):

- «l'anima **divenuta un altro Dio**» (c. 178v, §34) → mitigata dal contesto prudenziale «vedendosi tanto da lui fortificata» e «totale sicurtà… non per fidar di sé stessa» (178v).
- «una **sicurtà**, però è di bene pensare, che se Dio ci lasciasse potremo di nuovo cadire» (c. 178r, §29) → *attenuatio* del nodo della sicurezza.
- refrain prudenziale «dovemo sempre temere» / «mai fidarci di noi stessi» (178r–v, §§28, 34).

> **N.B. (attribuzione).** «(un altro Dio) **per particepatione**» è il leitmotiv del blocco **III.5–III.7** (cc. 167v, 171v, 173r), non di III.8; «**per quanto sta da parte di Dio**» è in **III.7** (c. 173v).

> **N.B. (citazioni).** *Consummatum est*, *In manus tuas* e *Tristis est anima mea* non sono in III.8: le prime due sono in III.XXXI–XXXII (cc. 241v–243v), la terza in III.24 (c. 219r).

- *Dignare Domine die isto sine peccato nos custodire* — Te Deum (cc. 100r, 216r) → liturgica, usata come protezione nei momenti di esposizione dottrinale.

**III.12** — stato d'otio / operazione nel fondo dell'anima. Citazioni compatibili col tema della quiete infusa:

- *Deliciae meae esse cum filiis hominum* — Prov 8,31 (c. 239r) → delizie divine = stato di quiete.
- *Misericordias Domini...* (Sal 88,2; cc. 92r, 182r, 203v) → citazione perfetta per descrivere illuminazioni.

**III.14** — santa ignoranza. Citazioni utili per marcazione teologica:

- *Iam hiems transiit... surge amica mea, et veni* (Ct 2,10-16; cc. 146r, 146v, 185r, 185v) → citazione sponsale perfetta per la trasformazione cognitiva.
- *Secretum meum mihi* (Is 24,16, tradizione di commento; cc. 148v, 175v) → ricorre nel contesto di "ignoranza sapiente".

**III.24** — imitazione della Passione. Citazioni centrali:

- *Tristis est anima mea usque ad mortem* (Mt 26,38; cc. 219r, 219v) → citazione-chiave, teologicamente delicata.
- *Salvum me fac Deus...* (Sal 68,2-3; c. 236r) → evocazione della prova in acque profonde.

**III.34** — trasformazione totale / matrimonio spirituale. Citazioni utili per i grafi:

- *Vivo autem, iam non ego: vivit vero in me Christus* (Gal 2,20; c. 173v) → formula di trasformazione.
- *Amor meus crucifissus est, et ego cum illo* (S. Ignazio, *Ad Romanos* 7) → intertesto patristico; **attestata a III.24** (c. 219v), non a III.34.
- *Cupio dissolvi, et esse cum Christo* (Fil 1,23; cc. 196r, 198v, 222r, 232v, 233r, 260r, 260v) → desiderio di unione perfetta.

**III.40** — ultima cella dell'anima. Citazioni utili per concludere il ciclo ascensionale:

- *Astitit regina a dextris tuis...* (Sal 44,10; attestata a c. 111r, Libro II) → culminazione sponsale.
- *Soli Deo honor et gloria* (Tm 1,17; cc. 253r, 263r) → formula conclusiva.

### 3.4. Authority list

*Anagrafe verificata sull'**apparato dell'edizione critica** (grafie volgarizzate come stampate; le carte indicano il folio dell'occorrenza). Tabella completa con occorrenze in [Appendice — Authority File](#appendice--authority-file).*

#### 3.4.1 Salmi
- *In te Domine speravi, non confundar in aeternum* — Ps 70(71),1 (cc. 13r, 220v, 221r)
- *Misericordias Domini in aeternum* — Ps 88,2 (cc. 92r, 182r, 203v)
- *Vias mandatorum tuorum cucurri* — Ps 118,32 (c. 78r)
- *Circumdederunt me dolores mortis* — Ps 114,3 (cc. 137v, 213r)
- *Salvum me fac Deus* — Ps 68,2-3 (c. 236r)
- *Astitit regina a dextris* — Ps 44,10 (c. 111r)

#### 3.4.2 Vangeli
- *Tristis est anima mea usque ad mortem* — Mt 26,38 (cc. 43r, 219r, 219v)
- *Spiritus promptus, caro autem infirma* — Mt 26,41 (c. 25r)
- *Deus meus… / Heloi Heloi lama sabacthani* — Mc 15,34 (cc. 213v, 219v, 220r, 243r)
- *(Getsemani)* — Mc 14,36 (c. 219v)
- *Pater dimitte illis, non enim sciunt* — Lc 23,24 (c. 220r)
- *In manus tuas, Domine* — Lc 23,46 (cc. 242r–243v)
- *Pater si vis, transfer calicem* — Lc 22,42 (cc. 25r, 25v, 219v)
- *Consummatum est* — Gv 19,30 (cc. 241v, 254v, 255r)
- *Sitio* — Gv 19,28 (cc. 241r, 241v)

#### 3.4.3 Epistole paoline
- *Cupio dissolvi et esse cum Christo* — Fil 1,23 (cc. 196r, 198v, 222r, 232v, 233r, 260r, 260v)
- *Christus factus est pro nobis obediens* — Fil 2,8 (c. 14r)
- *Vivo autem, iam non ego, vivit vero in me Christus* — Gal 2,20 (c. 173v)
- *Soli Deo sit honor et gloria* (Regi autem saeculorum…) — 1 Tm 1,17 (cc. 253r, 263r)
- *Dominus autem dirigat corda* — 2 Ts 3,5 (cc. 255v, 256r)

#### 3.4.4 Altre Scritture
- *Iam hiems transiit, imber abiit et recessit… surge amica mea et veni* — Ct 2,10-16 (cc. 146r, 146v, 185r, 185v)
- *Secretum meum mihi* — Is 24,16 (cc. 29v, 66v, 148v, 175v)
- *Deliciae meae esse cum filiis hominum* — Prov 8,31 (c. 239r)

#### 3.4.5 Patristica e scolastica
- *Amor meus crucifissus est, et ego cum illo* — S. Ignazio, *Ad Romanos* 7 (c. 219v, III.24)
- *De Civitate Dei* — S. Agostino (c. 248v)
- *Summa contra Gentiles* III.38 — S. Tommaso d'Aquino (cc. 133r, 160v)

#### 3.4.6 Liturgia
- *Pater noster, qui es in caelis* (c. 21r)
- *Te Deum* (*Dignare Domine / Pleni sunt caeli / Te Deum laudamus*) (cc. 100r, 100v, 113v, 114r, 216r, 252v)

**Totale attestato: 28 citazioni distinte** (23 bibliche + 2 patristiche + 1 scolastica + 2 liturgiche).

## 4. Citazioni rilevanti

Razionale di scelta: rischio, chiarificazione, glosse, struttura canonica del discorso, stabilizzazione dottrinale, controfattuali IA.

### 4.1. Citazioni come legittimazione dottrinale

Le citazioni illustrano l'uso delle citazioni come dispositivi di stabilizzazione nei punti più esposti (umiltà, sicurezza, dilatazione spirituale). Le citazioni di seguito indicate ancorano il discorso mistico alla Scrittura e servono come pilastri dell'ortodossia.

**Salmi**

- *In te Domine speravi, non confundar in aeternum* — Ps 70(71) → usata nel Libro I per fondare la virtù dell'umiltà (I.5, c. 13r); ripresa come ancoraggio in III.24 (cc. 220v-221r).
- *Misericordias Domini in aeternum cantabo* — Sal 88,2 → citazione di stato mistico "di sicurezza", ricorrente nei momenti di luce divina.
- *Vias mandatuorum tuorum cucurri, cum dilatasti cor meum* — Sal 118,32 → usata per la "dilatazione del cuore" nei capitoli di unione infusa.

### 4.2. Citazioni come ancoraggio cristologico

Queste tipologie coincidono con i nodi a rischio riconosciuti dall'Inquisizione (unione, sicurtà, annichilazione, trasformazione), usate da suor Teresa per evitare derive quietiste.

- *Christus factus est pro nobis obediens usque ad mortem* — Fil 2,8 → chiave di volta del capitolo sull'obbedienza (I.6).
- *Consummatum est* — Gv 19,30 → usata come citazione di ancoraggio nei passaggi di croce (III.XXXI–XXXII, cc. 241v–255r).
- *In manus tuas Domine, commendo spiritum meum* — Lc 23,46 → ancoraggio alla Passione per arginare l'annichilazione mistica (III.XXXII, cc. 241v–243v).
- *Sitio* — Gv 19,28 → tipica delle pene mistiche d'amore e dello stato sponsale.

### 4.3. Citazioni come marcatori di sofferenza / notte mistica

Citazioni centrali per la funzione di recinzione semantica delle glosse; sono le più esposte e potenzialmente sospette.

- *Pater, si vis transfer calicem istum* — Lc 22,42 → collegata allo stato di solitudine avanzata (Libro III).
- *Deus meus, Deus meus, ut quid dereliquisti me?* — Mc 15,34 → usata nelle descrizioni della *notte dello spirito* e della desolazione mistica.
- *Tristis est anima mea usque ad mortem* — Mt 26,38 → una delle più pericolose; è accompagnata da *glosse attenuative* per evitare sospetti quietisti (III.24).
- *Spiritus quidem promptus est, caro autem infirma* — Mt 26,41 → usata per spiegare gli inganni delle anime *proficienti* nel Libro II (discernimento).

### 4.4. Citazioni sponsali (Cantico dei Cantici)

Riferimenti mistico-sponsali come dispositivi canonici di legittimazione; sono il fondamento della mistica nuziale, ma anche possibile punto di rischio.

- *Iam hiems transiit... surge amica mea, et veni* — Ct 2,10–11 → usata nei capitoli della *santa ignoranza* e della piena trasformazione (III.14).

### 4.5. Citazioni di rifinitura dottrinale

Questa tipologia chiude i segmenti, marca l'ortodossia e serve come *sigillo teologico*.

- *Soli Deo honor et gloria* — Tm 1,17 → citazione conclusiva, sigillo di ortodossia in chiusura (Libro III).
- *Dominus autem dirigat corda...* — Ts 3,5 → associata al discernimento, utile come citazione *esatto congegno anti-moliniano* (II.10b).

### 4.6. Citazioni metafisiche e sapienziali

Connesse al movimento dell'intelletto e alla santa *ignoranza*; accompagnano glosse esplicative nei passaggi di maggiore complessità concettuale.

- *Secretum meum mihi* — Is 24,16 (secondo tradizione mistica) → usato nei capitoli più delicati su intelletto e volontà, con funzione di smorzamento dottrinale.
- *Deliciae meae esse cum filiis hominum* — Prov 8,31 → citazione per l'*otio divino* e l'unione intellettuale (III.12).

### 4.7. Citazioni patristiche-mistiche non bibliche

Citazioni rare e molto significative, segnano il punto di contatto tra mistica canonica ed eccesso trasformativo.

- *Amor meus crucifissus est, et ego cum illo* — Ignazio di Antiochia, *Ad Romanos* 7 → asse teologico di trasformazione mistica; **attestata a III.24** (c. 219v).

## 6. Glosse — matrice tipizzata sugli assi di tassonomia-gh.xml

Le 29 glosse selezionate sono tipizzate qui come **proiezione degli assi della tassonomia** (`operation`, `func`, `risk`, `mystic_state`/`relation`, `impact`): ogni etichetta è un `xml:id` dichiarato in `tassonomia-gh.xml`. La classe formale del marcatore **F** è derivata dal rango dell'asse `operation` — `delimitazione`→1, `attenuatio`/`precisatio`/`riequilibrio`→2, `declaratio`→3 — e normalizzata come `F/3`. I valori **N** (necessità interpretativa) e **A** (riduzione dell'ambiguità) sono giudizi *expert-in-the-loop* su scala 0–1; **I** è calcolato con la formula `I = (4·Fnorm + 2·N + 1·A)/7`. I valori N e A della matrice sono le stime **continue** (scala 0–1) usate per la calibrazione originaria delle soglie; il modello di produzione adotta poi le **bande-ancora** (N ∈ {0.90, 0.75, 0.55, 0.30}, A ∈ {0.85, 0.675, 0.40}), a soglie invariate.

Le **soglie** delle quattro classi non sono fissate a priori ma tagliate sulla distribuzione reale dei 29 valori di I (i confini low/medium e high/critical coincidono con ampi *natural breaks* — rispettivamente ~0.44→0.63 e ~0.77→0.95 — mentre la soglia medium/high a 0.66 separa valori contigui, 0.655 vs 0.661, ed è fissata per coerenza con la scala ordinale di F): **`impact-low` < 0.50 · `impact-medium` 0.50–0.66 · `impact-high` 0.66–0.82 · `impact-critical` ≥ 0.82**. 
La banda critica coincide con le tre *declaratio* (F=3), i sigilli performativi di ortodossia dell'autrice, coerentemente con il catDesc di `impact-critical`, che definisce la banda come «**massima forza regolativa del marcatore**»: nel campione le *declaratio*/sigilli d'ortodossia, collocati di norma nei nodi dottrinalmente più esposti (trasformazione, apparente impeccabilità, panteismo, sicurtà divina). La banda misura dunque la **forza (forma)** del presidio, non il solo rischio di contenuto: perciò anche una *professio fidei* proemiale, di forma performativa massima ma contenuto ortodosso, rientra legittimamente nella fascia critica.

**Frequenze dei marcatori seriali** (sull'edizione critica, testo normalizzato): *cioè* = 289; *s'intende* / *non s'intende* = 128 (di cui *non s'intende* = 16); *mi dichiaro* = 3 (famiglia *dichiar-* = 8); formule di riannodo del tipo «(come) ho detto» = 120 (di cui «come ho detto» = 32), oltre alle varianti «come dissi» = 73 e «come dissimo / habbiamo detto».

| Glossa | Operazione (F) | func | risk | N | A | I | impact |
|---|---|---|---|---|---|---|---|
| 6.1.1 · III.V,15 | attenuatio (2) | rischio | risk-quietismo | 0.85 | 0.76 | 0.732 | high |
| 6.1.2 · III.VI,2 | attenuatio (2) | rischio | risk-impeccabilita | 0.88 | 0.80 | 0.747 | high |
| 6.1.3 · III.VII,8 | attenuatio (2) | rischio | risk-panteismo | 0.95 | 0.85 | 0.774 | high |
| 6.1.4 · III.X,6 | attenuatio (2) | rischio | risk-quietismo | 0.75 | 0.68 | 0.692 | high |
| 6.1.5 · III.XXXIX,5 | attenuatio (2) | rischio | risk-quietismo | 0.88 | 0.82 | 0.750 | high |
| 6.1.6 · III.VII,6 | attenuatio (2) | rischio | risk-quietismo | 0.78 | 0.66 | 0.698 | high |
| 6.1.7 · III.X,6 | attenuatio (2) | rischio | risk-ambiguita | 0.70 | 0.62 | 0.670 | high |
| 6.1.8 · II.VIII,37 | attenuatio (2) | rischio | risk-ambiguita | 0.68 | 0.60 | 0.661 | high |
| 6.2.1 · III.XXIV,20 | riequilibrio (2) | rischio | risk-dottrinale | 0.82 | 0.72 | 0.718 | high |
| 6.2.2 · II.III,9 | riequilibrio (2) | rischio | risk-dottrinale | 0.62 | 0.58 | 0.641 | medium |
| 6.2.3 · II.II,2 | riequilibrio (2) | rischio | risk-quietismo | 0.66 | 0.60 | 0.655 | medium |
| 6.2.4 · II.II,3 | riequilibrio (2) | pedagogia | risk-quietismo | 0.64 | 0.58 | 0.647 | medium |
| 6.2.5 · III.V | riequilibrio (2) | rischio | risk-impeccabilita | 0.80 | 0.70 | 0.710 | high |
| 6.3.1 · III.XXXVIII,20 | declaratio (3) | rischio | risk-dottrinale | 0.90 | 0.85 | 0.950 | critical |
| 6.3.2 · III.XXXIX,3 | declaratio (3) | rischio | risk-panteismo | 0.94 | 0.88 | 0.966 | critical |
| 6.3.3 · II.XXI,16 | declaratio (3) | rischio | risk-impeccabilita | 0.92 | 0.85 | 0.956 | critical |
| 6.4.1 · I.IV,7 | delimitazione (1) | pedagogia | risk-ambiguita | 0.55 | 0.58 | 0.430 | low |
| 6.4.2 · I.V,13 | delimitazione (1) | pedagogia | risk-ambiguita | 0.48 | 0.52 | 0.402 | low |
| 6.4.3 · II.VIII,32 | delimitazione (1) | pedagogia | risk-ambiguita | 0.60 | 0.56 | 0.442 | low |
| 6.5.1 · II.VIII,13 | delimitazione (1) | ethos-esperienza | risk-dottrinale | 0.58 | 0.50 | 0.428 | low |
| 6.5.2 · II.XX,29 | delimitazione (1) | ethos-umilta | risk-ambiguita | 0.50 | 0.48 | 0.402 | low |
| 6.6.1 · II.III,9 | precisatio (2) | rischio | risk-ambiguita | 0.60 | 0.58 | 0.635 | medium |
| 6.6.2 · II.VIII,23 | delimitazione (1) | ethos-umilta | risk-ambiguita | 0.52 | 0.50 | 0.410 | low |
| 6.7.1 · II.II | precisatio (2) | rischio | risk-quietismo | 0.74 | 0.66 | 0.687 | high |
| 6.7.2 · III.XII,3-4 | precisatio (2) | rischio | risk-quietismo | 0.80 | 0.68 | 0.707 | high |
| 6.8.1 · II.VII,12 | delimitazione (1) | pedagogia-discernimento | risk-dottrinale | 0.56 | 0.55 | 0.429 | low |
| 6.8.2 · II.X,12 | delimitazione (1) | ethos-umilta | risk-ambiguita | 0.48 | 0.46 | 0.393 | low |
| 6.9.1 · III.VIII,34 | attenuatio (2) | rischio | risk-impeccabilita | 0.90 | 0.82 | 0.755 | high |
| 6.10.1 · III.XXXIX | riequilibrio (2) | rischio | risk-panteismo | 0.90 | 0.82 | 0.755 | high |

**Assi `mystic_state` / `relation` (dove pertinenti):** 6.1.3 (III.VII,8) → `relation-mistica-unione-sposalitio`; 6.1.6 (III.VII,6) → `mystic_state-otium`; 6.1.8 (II.VIII,37) → `mystic_state-illuminazione`; 6.2.1 (III.XXIV,20) → `relation-intertesto-biblico`; 6.2.3 (II.II,2) → `mystic_state-otium`; 6.7.1 (II.II) → `mystic_state-otium`; 6.7.2 (III.XII,3-4) → `mystic_state-otium`; 6.10.1 (III.XXXIX) → `relation-mistica-unione-sposalitio`.

**Nota `cert`.** Giudizio dell'annotatore *low* dove N/A restano incerti: 6.1.6, 6.1.7, 6.1.8, 6.2.2, 6.2.3, 6.2.4, 6.4.3, 6.6.1, 6.7.1 (da rivedere sul manoscritto in fase di validazione corpus).

**Nota loci (risolti — v1.8).** Le righe **6.1.3** e **6.3.3**, in precedenza etichettate `III.VIII,8`, sono state riassegnate sul riscontro delle trascrizioni: **6.1.3** («divenuta un altro Dio», panteismo, attenuatio) è a **III.VII,8** (c. 173r); **6.3.3** (impeccabilità, declaratio) è la terza «mi dichiaro» dell'opera — «Mi dichiaro però che resta nell'anima passiva capacetà… quando Dio l'abandonasse», glossa autoriale tardiva a inchiostro scuro — in **II.XXI** (c. 146r, § ≈ 16, da rifinire). La riga **6.9.1** (`III.VIII,34`, «totale sicurtà… non per fidar di sé stessa») è già corretta e resta la glossa anti-sostanziale propria di III.8.

## 7. Intertestualità nel Castello

### 7.1. Il rapporto con Teresa d'Ávila: continuità e rovesciamento

Nel *Castello dell'anima*, la presenza della tradizione teresiana emerge nella metafora del "castello", che nel Seicento religioso è uno dei nuclei più riconoscibili della mistica femminile. Tuttavia, il senso dell'immagine viene profondamente trasformato. Nel modello avilese, il castello è la struttura stessa dell'anima e il percorso mistico consiste nel penetrare progressivamente nelle sue stanze più interiori. Nel *Castello* siciliano, al contrario, l'immagine viene ricontestualizzata: non è l'anima a essere un castello, ma è l'"orazione" ad avere la forma di un edificio ascensivo. L'orante non entra in sé, ma *costruisce* un luogo interiore. Questo spostamento semantico ha conseguenze decisive: **(1)** introduce una logica attiva (costruire) al posto di una logica introspettiva (entrare); **(2)** colloca l'esperienza mistica all'interno di una pedagogia ascetica più che visionaria; **(3)** crea un modello più compatibile con un contesto inquisitoriale, dove l'autonomia esperienziale poteva essere sospetta; **(4)** qui l'intertestualità non è imitazione, ma rielaborazione regolativa: l'immagine tradizionale permette di aprire un linguaggio familiare, ma il suo significato viene spostato per assicurare tracciabilità e ortodossia.

### 7.2. Presenza della tradizione giovannea: tecnica delle potenze e logica della notte

Il *Castello* impiega una terminologia che riflette la sistemazione dottrinale elaborata nel Carmelo post-tridentino: analisi dei sensi interni ed esterni, distinzione delle facoltà spirituali (memoria–intelletto–volontà), descrizione della loro sospensione progressiva nella contemplazione. Nelle pagine dedicate ai sensi interiori (Libro II, cap. IV), la struttura retorica riproduce lo schema della purgazione graduale, che nella tradizione giovannea è strumento critico per spiegare: **(1)** il passaggio dalla meditazione discorsiva alla quiete, **(2)** l'oscurità che accompagna l'ingresso nella contemplazione, **(3)** la sospensione operativa dell'intelletto non come annullamento, ma come ricezione passiva di un atto divino. Il modello della *notte* diventa una grammatica concettuale che permette a un'autrice laica di trattare concetti ad altissimo rischio (sospensione, annichilazione, passività), disponendoli però dentro una cornice riconoscibile e accettata. In questo senso, l'intertestualità tecnica serve come argine dottrinale in cui l'autrice adotta schemi consolidati per parlare di ciò che potrebbe essere equivocato come quietismo.

### 7.3. Metafore mistiche femminili: attrazione, amore, calamita

Nel discorso sulla virtù dell'umiltà, l'immagine della *calamita* che attira Dio assume un valore dottrinale e autoriale. L'immagine, presente nella tradizione mistica toscana e ligure (Maria Maddalena de' Pazzi), non introduce un eccesso visionario, ma un modo di parlare del rapporto tra l'anima e la grazia senza usare categorie teologicamente controverse. La metafora permette di esprimere **(1)** l'intensità dell'unione mistica, **(2)** la logica della reciprocità tra Dio e l'anima, **(3)** la dinamica affettiva della contemplazione. Tutto ciò sarebbe rischioso se formulato come "possesso", "fusione", "trasformazione essenziale". L'immagine affettiva, derivata dalla tradizione delle mistiche italiane, neutralizza il rischio e lo inscrive in un codice già approvato.

### 7.4. L'orizzonte della *nuova mistica*: consonanze con Molinos e necessità di difese

Nel testo emerge una costellazione di concetti che circolano nel quietismo europeo: quiete, passività, sospensione delle potenze, guida sostanzialmente inutile dopo la perfetta unione. Il *Castello* ne riproduce alcuni elementi, ma lo fa con un eccesso di cautela e attraverso continue glosse che ne delimitano il senso. L'autrice riconosce che può essere interpretata secondo un linguaggio sospetto e per questo inserisce autodifese: **(1)** esplicita dissociazione da "molinia"; **(2)** continuo ricorso all'obbedienza; **(3)** distinzione tra operazione divina e concorso umano. L'intertestualità qui è "liminare": ad esempio, non viene nominato Molinos, ma la sua struttura concettuale è riconoscibile e viene assorbita, addomesticata, sorvegliata.

### 7.5. Agiografia e genealogie femminili come rete di legittimazione

L'autrice non si presenta isolata ma si colloca consapevolmente entro una catena di donne che hanno ricevuto, insegnato e trasmesso dottrine elevate. Esempi citati nel testo fanno riferimento a Geltrude di Helfta, Chiara da Montefalco e a Caterina da Siena. Queste figure svolgono una funzione duplice: **(1)** *legittimazione*: mostrano che una donna può ricevere dottrina divina senza mediazione maschile; **(2)** *moderazione*: il riferimento a sante canonizzate disinnesca l'accusa di presunzione spirituale. L'intertestualità qui produce un *ethos di affidabilità*, in cui l'autrice si inserisce dentro una tradizione riconosciuta.

### 7.6. Intertestualità culturale

La presenza di formule che provengono dalla tradizione letteraria profana, come la massima *amor con amor si paga* (Seneca → Petrarca → tradizione devota: Celestina), non introduce un elemento estraneo, ma offre un registro retorico familiare alle lettrici e ai lettori del tempo. Questa circolazione culturale serve a rendere più accessibile un contenuto ascetico elevato, a inscrivere l'opera in una tradizione morale condivisa e ad alleggerire concetti altrimenti astratti.

### 7.7. Intertesto esperienziale: l'esperienza personale come fonte legittimante

Il testo fa ampio uso della formula *non parlo senza l'esperienza* in contesti centrali della direzione spirituale e del discernimento. Questa strategia non è retorica ma è un rimando mistico vero e proprio. L'esperienza, nel quadro femminile post‑tridentino, sostituisce l'autorità dottrinale e diventa un'intertestualità interna, dove l'autrice richiama il proprio vissuto come fonte del discorso spirituale. La sua esperienza è modellata su quella delle mistiche canoniche.

## Appendice — Authority File

### 1. Biblia — Vulgata / Nova Vulgata

*Carte = folio dell'occorrenza sull'edizione critica (apparato).*

| Sigla | Citazione | Carte | Nota d'uso |
|---|---|---|---|
| Ps 70(71),1 | *In te Domine speravi, non confundar in aeternum* | 13r, 220v, 221r | Legittimante (I.5) e ancoraggio (III.24) |
| Ps 88(89),2 | *Misericordias Domini in aeternum cantabo* | 92r, 182r, 203v | Stato mistico di sicurezza |
| Ps 118(119),32 | *Vias mandatorum tuorum cucurri* | 78r | Dilatazione del cuore |
| Ps 114,3 | *Circumdederunt me dolores mortis* | 137v, 213r | Prova / desolazione |
| Ps 68(69),2-3 | *Salvum me fac Deus* | 236r | Notte mistica / prove |
| Ps 44(45),10 | *Astitit regina a dextris tuis* | 111r | Culmine sponsale |
| Mt 26,38 | *Tristis est anima mea usque ad mortem* | 43r, 219r, 219v | Alto rischio (III.24) |
| Mt 26,41 | *Spiritus promptus, caro autem infirma* | 25r | Discernimento |
| Mc 15,34 | *Deus meus… / Heloi Heloi lama sabacthani* | 213v, 219v, 220r, 243r | Notte spirituale |
| Mc 14,36 | *(Getsemani — conformità alla volontà)* | 219v | Passione |
| Lc 22,42 | *Pater si vis, transfer calicem istum* | 25r, 25v, 219v | Solitudine infusa |
| Lc 23,24 | *Pater dimitte illis, non enim sciunt* | 220r | Perdono / passione |
| Lc 23,46 | *In manus tuas, Domine* | 242r–243v | Ancoraggio alla Passione |
| Gv 19,28 | *Sitio* | 241r, 241v | Pene d'amore / sponsale |
| Gv 19,30 | *Consummatum est* | 241v, 254v, 255r | Sicurezza mistica |
| Ct 2,10-16 | *Iam hiems transiit… surge amica mea et veni* | 146r, 146v, 185r, 185v | Sponsale (III.14) |
| Is 24,16 | *Secretum meum mihi* | 29v, 66v, 148v, 175v | Sapere nascosto |
| Prov 8,31 | *Deliciae meae esse cum filiis hominum* | 239r | Quiete infusa |
| Fil 1,23 | *Cupio dissolvi et esse cum Christo* | 196r, 198v, 222r, 232v, 233r, 260r, 260v | Unione perfetta |
| Fil 2,8 | *Christus factus est pro nobis obediens* | 14r | Pivot cristologico (I.6) |
| Gal 2,20 | *Vivo autem, iam non ego, vivit vero in me Christus* | 173v | Trasformazione |
| 1 Tm 1,17 | *Soli Deo sit honor et gloria* (Regi autem saeculorum…) | 253r, 263r | Sigillo conclusivo |
| 2 Ts 3,5 | *Dominus autem dirigat corda* | 255v, 256r | Anti-quietista; discernimento |

### 2. Liturgia

| Citazione | Fonte | Carte | Contesto |
|---|---|---|---|
| *Pater noster, qui es in caelis* | Liturgia Romana | 21r | Orazione d'unione, stato infuso |
| *Te Deum* (*Dignare Domine / Pleni sunt caeli / Te Deum laudamus*) | *Te Deum* | 100r, 100v, 113v, 114r, 216r, 252v | Protezione dottrinale / lode |

### 3. Patristica e scolastica

| Citazione / Opera | Autore | Carte | Nota |
|---|---|---|---|
| *Amor meus crucifissus est, et ego cum illo* | S. Ignazio d'Antiochia, *Ad Romanos* 7 (MG 5-694) | 219v (III.24) | Trasformazione mistica |
| *De Civitate Dei* | S. Agostino | 248v | Riferimento dottrinale |
| *Summa contra Gentiles* III.38 | S. Tommaso d'Aquino | 133r, 160v | Riferimento scolastico |
| *Secretum meum mihi* (ricezione) | Tradizione esegetica (Gregorio, Bernardo) | — | Uso patristico-medievale |

### 4. Mistica (post-tridentina, carmelitana, italiana)

| Autore | Carte | Riferimento | Nota |
|---|---|---|---|
| Teresa d'Ávila | 16v | *Castillo interior* | Modello rovesciato nel *Castello* («serafica madre Teresa», c. 16v) |
| Giovanni della Croce | 91r | *Subida* / *Noche* | Schema purgativo, sospensione potenze |
| Miguel de Molinos | 19r, 63r | *Guía espiritual* | Contro-modello implicito («molinia»), rischio |
| Maria Maddalena de' Pazzi | 16v, 31v | *Revelazioni* | Metafora della calamita |
| Geltrude di Helfta | 16v | *Legatus divinae pietatis* | Genealogia mistica |
| Chiara da Montefalco | 16v | *Vita et revelationes* | Esempio di mistica del cuore |
| Caterina da Siena | 16v | *Dialogo* | Modello di autorità femminile |

### 5. Agiografia

| Santa | Carte | Opera / Fonte base | Funzione |
|---|---|---|---|
| Santa Maria Maddalena | 2r | Tradizione esegetica / agiografica | Esempio di conversione (I.1) |
| Santa Rosalia | 2r | Vita secentesca siciliana | Modello ascetico locale (I.1) |
| Santa Geltrude (di Helfta) | 16v | Vitae | Genealogia mistica |
| Santa Chiara da Montefalco | 16v | Vitae | Mistica del cuore |
| Santa Caterina da Siena | 16v | *Legenda Major* (Raymondo da Capua) | Legittimazione dottrinale |
