# Indice d'impatto (`impact-index`)

## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

Documentazione dell'**indice d'impatto** del modello TEI+IA del *Castello dell'anima*.
Vocabolario: `tassonomia-gh.xml`, asse `impact`. Procedura di assegnazione passo per passo:
`Protocollo-indice-impatto.md`.

---

## Indice

- [Cos'è](#cosè)
- [Posizione nella pipeline](#posizione-nella-pipeline)
- [I tre parametri](#i-tre-parametri-scala-01)
- [F - rango ordinale dell'asse `operation`](#f--rango-ordinale-dellasse-operation)
- [N e A - bande e valori-ancora](#n-e-a--bande-e-valori-ancora)
- [Formula (pesi AHP)](#formula-pesi-ahp)
- [Bande (asse `impact`)](#bande-asse-impact)
- [Comportamento dell'indice](#comportamento-dellindice)
- [Codifica TEI](#codifica-tei)
- [Automazione - `impact_index.py`](#automazione--impact_indexpy)
- [Pipeline e workflow controfattuale](#pipeline-e-workflow-controfattuale)
- [Robustezza e riproducibilità](#robustezza-e-riproducibilità)

---

## Cos'è

Metrica composita che misura la **forza regolativa** di una glossa, citazione o segmento
prudenziale nel punto esatto in cui compare. Opera **a valle** dell'interpretazione
filologica, su unità già codificate: non giudica l'ortodossia dell'intervento, ne
quantifica l'incidenza sulla tenuta del discorso. Pesi e soglie sono **fissi e invariati**
su tutto il corpus, così ogni occorrenza è comparabile con ogni altra.

L'indice è, insieme, un **valore statico**, quanto un nodo pesa nella sua posizione, e la
base di una **misura dinamica**: sotto perturbazione controllata (§ *Pipeline e workflow*),
la sua oscillazione **ΔI** dice quanto il discorso dipende da quel nodo. Il primo valore descrive,
il secondo prova.

## Posizione nella pipeline

L'indice non è un modulo isolato: è il terzo anello di una catena che va dal dato materiale alla misura sperimentale.

```
trascrizione diplomatica
        ↓
annotazione TEI interpretativa      ← <seg> + tassonomia @ana (func, operation, risk,
        ↓                             exposition, phase, mystic_state, relation) + @hand/@place
INDICE D'IMPATTO  ← (questo documento)   a valle, su unità già codificate
        ↓
validazione a 3 livelli             ← RelaxNG · Schematron · sperimentale (TEI+IA)
        ↓
IA controllata (expert-in-the-loop) ← eventi controfattuali, mai retroattivi sul testo
        ↓
misura ΔI su D1/D2/D3
```

La direzione è  **(1)** filologo → **(2)** codifica TEI → **(3)** intervento computazionale.
L'attribuzione di senso resta in ogni fase prerogativa del filologo; l'indice ne è un
derivato formale, non un giudizio autonomo.

## I tre parametri (scala 0–1)

| Sigla | Parametro | Definizione operativa |
|-------|-----------|-----------------------|
| **N** | necessità interpretativa | quanto il passo era dottrinalmente esposto *prima* dell'intervento; stima controfattuale interna al *Castello*, senza termini di confronto esterni |
| **A** | riduzione dell'ambiguità | quanto l'occorrenza restringe le letture possibili dei termini ad alta densità mistica (unione, fusione, *otium*, annichilazione, trasformazione) |
| **F** | funzione prudenziale | rango ordinale dell'operazione del marcatore (vedi sotto) — non stimato |

N e A sono le due sole **decisioni interpretative**; F si legge dalla codifica. La procedura
d'assegnazione — rubriche, criteri, esempi ancorati — è nel `Protocollo-indice-impatto.md`.

## F - rango ordinale dell'asse `operation`

F è il **rango dell'operazione** dichiarata in `@ana`, normalizzato `Fnorm = F/3`.

| Grado | Operazioni (`operation`) | Correlato fenomenologico (Casapullo) |
|:-----:|--------------------------|--------------------------------------|
| 1 | `delimitazione` | *cioè* — delimita una parola |
| 2 | `attenuatio`, `precisatio`, `riequilibrio` | *s'intende / non s'intende* — ridisegna una proposizione |
| 3 | `declaratio` | *io mi dichiaro* — dichiarazione performativa |

I gradi sono **classi funzionali**, non un elenco chiuso di formule: un marcatore non
canonico si assegna al grado la cui **operazione** condivide. La scala è robusta perché colloca
nello stesso grado le operazioni più difficili da distinguere (attenuatio ↔ precisatio).
Serialità decrescente dei marcatori nell'edizione — **cioè 289 · s'intende/non s'intende
128 · mi dichiaro 3** .

## N e A - bande e valori-ancora

Poiché la formula richiede un **numero** ma il giudizio filologico è affidabile solo a
livello di **banda**, N e A si assegnano scegliendo una banda; il valore è poi determinato da
un **valore-ancora fisso** per banda. L'annotatore sceglie la banda, non il decimale.

| Parametro | Critica | Alta | Media | Bassa |
|-----------|:-------:|:----:|:-----:|:-----:|
| **N** | 0.90 | 0.75 | 0.55 | 0.30 |
| **A** | — | 0.85 | 0.675 | 0.40 |

Le soglie di banda e i criteri d'attribuzione (con esempi ancorati) sono nel **Protocollo**.
Effetto: l'indice diventa **interamente ordinale**, tre giudizi di banda (F si legge, N e A
si scelgono) e ogni cifra è determinata. Due annotatori che concordano sulle bande ottengono
lo stesso identico **I**: l'accordo inter-annotatore si misura sulla banda, non su un decimale non
ispezionabile.

## Formula (pesi AHP)

```
I = (4·Fnorm + 2·N + 1·A) / 7          Fnorm = F / 3
wF = 4/7    wN = 2/7    wA = 1/7        (F : N : A = 4 : 2 : 1)
```

Pesi derivati per confronto a coppie (Analytic Hierarchy Process): F:N = 2, N:A = 2,
F:A = 4. **Internamente consistenti** perché F:A = 4 coincide con (F:N) × (N:A) = 2 × 2 →
*consistency ratio* = 0; verificabile a mano. F è dominante perché è il segnale meno
inferenziale (N è condizione ma non atto; A è in parte già catturato dalla scelta del
marcatore).

> **Nota di replica.** Nella formula si inserisce **sempre `Fnorm`, mai F grezzo**: un F non
> normalizzato (1–3 anziché 0,333–1) porterebbe I fuori scala senza segnalare l'errore.

## Bande (asse `impact`)

Soglie fisse, tagliate sulla distribuzione reale del campione (29 glosse) e invariate sul
corpus:

| Banda | Soglia |
|-------|--------|
| `impact-low` | I < 0.50 |
| `impact-medium` | 0.50 ≤ I < 0.66 |
| `impact-high` | 0.66 ≤ I < 0.82 |
| `impact-critical` | I ≥ 0.82 |

## Comportamento dell'indice

Con i valori-ancora, il grado di F **determina una finestra di due classi**; dentro la
finestra sono N e A a scegliere la classe. È una proprietà della formula, verificabile
calcolando l'indice ai due estremi delle ancore per ciascun grado:

| F (operazione) | I minimo → massimo | Classi raggiungibili |
|:--------------:|:------------------:|----------------------|
| 1 (`delimitazione`) | 0.333 → 0,569 | `low` / `medium` |
| 2 (`attenuatio`/`precisatio`/`riequilibrio`) | 0.524 → 0,760 | `medium` / `high` |
| 3 (`declaratio`) | 0.714 → 0.950 | `high` / `critical` |

Due letture: (1) **F fissa la finestra** — giustificazione del peso dominante 4/7: una
`delimitazione` non raggiunge mai `high`, una `declaratio` non scende mai sotto `high`. (2)
**dentro la finestra decidono N e A** — nel grado 2, per esempio, sono i due parametri stimati
a separare `medium` da `high`: la prova che non sono decorativi, ma risolvono la classe dove F
lascia margine. Il confronto banda↔decimale su un campione già codificato si ottiene con
`impact_index.py` in modalità audit (§ *Automazione*).

## Codifica TEI

Doppia registrazione: la **categoria discreta** in `@ana` sul `<seg>`; il **calcolo** in un
`<fs>` dentro `<standOff type="impact-index">`, fratello di `<text>`, collegato via
`@corresp`. La formula è dichiarata **una sola volta** in `editorialDecl`; il valore `I` è
prodotto dal calcolo, mai immesso dall'annotatore. Si usa `<fs>`, non `<val>`.

```xml
<!-- nel testo: la sola categoria discreta -->
<seg xml:id="seg-c8-desiderio"
     ana="#rischio-precisatio #operation-precisatio #risk-quietismo #exposition-critical
          #phase-mediana #phase-critical #mystic_state-quiete
          #relation-mistica-passiva-quiete #impact-high"
     hand="#ink_1" cert="medium"> (...) incomincia l'anima a perdire qualunque desiderio (...)</seg>

<!-- in standoff, stesso documento del testo: il fascio computabile -->
<standOff type="impact-index">
  <fs xml:id="idx-seg-c8-desiderio" corresp="#seg-c8-desiderio" cert="medium">
    <f name="N_band"><symbol value="critica"/></f>   <!-- banda scelta dall'annotatore -->
    <f name="A_band"><symbol value="alta"/></f>      <!-- banda scelta dall'annotatore -->
    <f name="N"><numeric value="0.90"/></f>          <!-- banda Critica → ancora 0,90 -->
    <f name="A"><numeric value="0.85"/></f>          <!-- banda Alta    → ancora 0,85 -->
    <f name="F"><numeric value="2"/></f>             <!-- operation precisatio → grado 2 -->
    <f name="Fnorm"><numeric value="0.667"/></f>
    <f name="I"><numeric value="0.760"/></f>
  </fs>
</standOff>
```

**Esempio.** N: banda Critica → 0,90 · A: banda Alta → 0,85 · F: `precisatio` → grado 2 →
**I = (4·0,667 + 2·0,90 + 0,85) / 7 = 0,760 → `impact-high`**.

## Automazione — `impact_index.py`

Il calcolo è affidato a uno **script deterministico** (Python, `lxml`), fedele al principio:
I non si digita, si calcola. Confine netto fra ciò che resta umano e ciò che è meccanico.

**Input umano — due sole etichette per segmento:** la banda di N e la banda di A.

**Il resto è automatico:** lettura di F dall'asse `operation`, `Fnorm = F/3`, conversione
delle bande nei valori-ancora, calcolo di I, assegnazione della banda `impact-*`, checklist di
validazione. (La *scrittura* della `<fs>` nel documento è affidata agli strumenti visuali —
Calcolatore e Annotatore in `tools/` —; lo script calcola, verifica e rende auditabile.)

Due modalità:

- **authoring** — da una tabella `id;banda_N;banda_A` calcola I e la banda per molti segmenti
  (la scrittura della `<fs>` è affidata agli strumenti visuali);
- **audit** — legge le `<fs>` già presenti, ri-mappa i loro valori alle bande, ricalcola con
  le ancore e confronta con l'`impact-*` dichiarato; risolve i puntatori
  (`@corresp`/`@target`/`<link>` → `xml:id` esistenti); esegue RelaxNG e Schematron opzionali.

```bash
# audit dell'intero teiText + validazione TEI
python3 impact_index.py tei/text/castello-anima-teiText.xml \
        --rng <schema-relaxng> --sch <regole-schematron>

# authoring da bande decise dall'annotatore
python3 impact_index.py tei/text/castello-anima-teiText.xml --bands bande.csv
```

```csv
# bande.csv  —  id;banda_N;banda_A
seg-c8-desiderio;critica;alta
seg-c2-purificazione;critica;alta
```

Due annotatori con le stesse due bande ottengono **output identico**: la riproducibilità è
garantita per costruzione. Collocazione nel repo: `tools/`, accanto ai dati che valida.

## Pipeline e workflow controfattuale

L'indice statico è la premessa di una **prova sperimentale**. La pipeline IA non tocca il
testo stabilito: genera **eventi controfattuali** su unità già codificate e ne misura
l'effetto, in un regime **expert-in-the-loop**.

### I tre scenari

Ogni perturbazione è una lettura alternativa `<rdg>`, marcata con un token di workflow e
registrata nel `<revisionDesc>`:

| Token workflow | Sigla | Operazione |
|----------------|:-----:|------------|
| `#workflow-rimozione` | **−CIT** | rimozione di una glossa o citazione dal testo |
| `#workflow-recupero-cancellature` | **+TEXTsub** | recupero di una cancellatura autoriale, quando il manoscritto lo consente |
| `#workflow-aggiunta` | **+CIT** | integrazione *in extenso* di una citazione solo richiamata |
| `#workflow-validazione` | — | verifica della tenuta dei criteri annotativi sotto perturbazione |

Gli eventi controfattuali convalidati sono archiviati in uno **strato subordinato** dello
`standOff` come *eventi simulati*, **senza alcuna retroazione** sul testo stabilito: la
perturbazione entra solo come termine di confronto ermeneutico a valle.

### La misura: ΔI

Per ogni scenario si ricalcola l'indice sul nodo perturbato e se ne prende lo scarto:

```
ΔI = I(dopo perturbazione) − I(prima)
```

ΔI è un **sensore di instabilità**: se il valore statico dice *quanto un nodo pesa*, la sua
oscillazione dice *quanto il discorso dipende da esso*. È qui — e non nel valore statico di A
— che il test controfattuale interviene: A è un *input* dell'indice, mentre ciò che la
perturbazione verifica è ΔI. La variazione si proietta su tre dimensioni osservabili:

- **D1 — chiarezza argomentativa** (riduzione delle ambiguità nei nodi sensibili);
- **D2 — coesione locale** (continuità tematica e referenziale col contesto);
- **D3 — stabilità dottrinale percepita** (persistenza/oscillazione della cornice teologica).

Un ΔI ampio a fronte di una `−CIT` segnala un nodo che *dipende* dal proprio presidio; un ΔI
trascurabile, un presidio ridondante. Così la logica seriale della prudenza dottrinale passa
da postulato a evidenza verificabile.

### Governance dell'IA

L'IA agisce come **perturbatore probabilistico controllato**, mai come interprete:

- modello, parametri (**temperatura, top-p, seed**), prompt e audit-trail sono fissati e
  registrati nel blocco `xenoData` del teiHeader;
- ogni output è sottoposto a controllo **expert-in-the-loop**: l'IA propone la perturbazione,
  il filologo ne stabilisce l'accettabilità dottrinale, teologica e stilistica;
- l'**indice d'impatto è calcolato dalla formula AHP su N/A/F ed è quindi indipendente dal
  modello IA**: l'IA interviene solo nella generazione degli scenari, non nel calcolo di I.

## Robustezza e riproducibilità

- **Sensibilità ai pesi** — ricalcolo con ponderazioni alternative; la quota di segmenti che
  cambiano banda è pubblicata come misura di sensibilità.
- **Prova inter-annotatore** — codificatori TEI esterni annotano lo stesso campione e ripetono
  in autonomia i confronti a coppie; l'accordo si misura sulla **banda** (non sul decimale) e
  le divergenze sono documentate.
- **Determinismo** — versione del modello e parametri fissati; `I` prodotto dallo script; la
  griglia (formula, ancore, soglie) dichiarata una sola volta e invariata sul corpus.
- **FAIR** — testo, tassonomia, schemi e strumenti versionati in repository pubblico; ogni
  passaggio, dalla trascrizione alla misura, tracciabile e replicabile.
