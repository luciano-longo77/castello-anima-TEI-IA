# Guida ragionata alla codifica del `<text>`
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

## Premessa

Questo documento espone **il set di tag adottato per la codifica del testo** del *Castello dell'anima* e lo **argomenta**: per ciascun fenomeno spiega *quale* elemento si usa, *con quali attributi e valori*. È dunque, insieme, la parte metodologica sulla marcatura e il **contratto di codifica** per `castello-anima-teiText.xml`.

Tre principi lo governano:

1. **Ancoraggio.** Ogni puntatore (`#id`) usato in `castello-anima-teiHeader.xml` (mani, testimoni, entità, tassonomia `workflow`) o in `tassonomia-gh.xml` (categorie `@ana`). 
2. **Trasparenza filologica.** Ogni scelta editoriale è marcata e attribuita.
3. **Verificabilità.** Elementi, attributi e annidamenti qui descritti sono verificati contro le specifiche **TEI P5** (`tei_all`): un esemplare che li esercita tutti supera il controllo strutturale con **0 errori**. La validazione RelaxNG completa (ordine, occorrenze, Schematron) si fa in oXygen.

> La forma canonica *machine-actionable* di questi vincoli è l'**ODD**; questo documento ne è il contenuto pronto (schema + manuale generabili in un secondo momento). Le liste di valori vincolati sono in [Appendice](#appendice--liste-di-valori-i-puntatori).

---

# Parte 1 · Il set di tag, ragionato

La marcatura è stratificata in cinque livelli, dal più esterno (la struttura del libro) al più interno (l'interpretazione e la misura d'impatto). Ogni livello risponde a una domanda diversa e usa gli elementi che *quella* domanda richiede.

## 1. La struttura del testo

Il testo è un autografo unico, articolato in **Libri** e **capitoli**: una gerarchia continua. Per questo la struttura si rende con `<div>` annidati (`@type` = `book` › `chapter`) e **non** con `<milestone>`, che segnerebbe confini senza contenere il testo. Le rubriche dei capitoli sono `<head>`; l'eventuale cappello che precede un capitolo è `<argument>` (elemento di struttura dedicato, non una `<note>`).

```xml
<div type="chapter" n="1" xml:id="III-cap1">
  <head>Capitolo Primo</head>
  <p n="1"> … </p>
</div>
```

Il paragrafo è `<p>` (con `@n` come integrazione editoriale). La **materialità** entra con `<pb n="158r"/>` — la foliazione *reale* del manoscritto e con `<lb break="no"/>`, riservato ai **soli** a-capo rilevanti (parola spezzata), non a ogni riga. Il materiale non-testuale di pagina (segnature, richiami, numeri di carta) è `<fw>`, tenuto distinto dal testo d'autore.

L'unità portante dell'annotazione è **`<seg>`**, non `<ab>` né `<p>`: è l'unica che porta `@ana` (l'interpretazione) a granularità sub-paragrafo ed è governata dal `classDecl`. Ogni `seg` del corpo ha un `@xml:id` nel formato `seg-c<cap>p<par>-<label>` (es. `seg-c1p8-desiderio`), che diventa l'ancora per l'apparato e per l'indice d'impatto.

```xml
<seg xml:id="seg-c1p8-desiderio" ana="#operation-precisatio #risk-quietismo #impact-high" hand="#ink_1">
  incomincia l'anima a perdire qualunque desiderio
</seg>
```

Dove serve un ancoraggio *senza* spezzare il flusso (per lo stand-off), si usa `<anchor xml:id="…"/>`.

## 2. Il livello diplomatico

Principio: **ogni volta che l'editore regolarizza, scioglie o corregge**, il testo conserva *entrambe* le forme dentro `<choice>` — grafia originale ↔ regolarizzata (`orig`/`reg`), abbreviazione ↔ scioglimento (`abbr`/`expan`), errore materiale ↔ correzione (`sic`/`corr`). La correzione porta sempre `@resp="#editor"` e `@cert`.

```xml
<choice><sic>perdire</sic><corr resp="#editor" cert="low">perdere</corr></choice>
```

La **lettura incerta** è `<unclear reason="…" cert="…">`, la **perdita materiale** è `<gap reason="…" unit="…"/>`, l'**integrazione congetturale** è `<supplied reason="hole" resp="#editor" cert="medium">` — dove `@reason` registra la causa materiale (es. il buco della carta) e `@cert` il grado della congettura. Il **latino citazionale** non si marca come lingua straniera ma come citazione: `<cit>`/`<quote xml:lang="la">` (vedi §6); `<foreign xml:lang="la">` resta disponibile per spezzoni in lingua *non* citazionali (nel corpus attuale: nessuno).

## 3. La genetica sulla carta

Qui si registra il *lavoro dell'autrice sul foglio*. L'aggiunta è `<add>` (con `@place` topografico e `@type` = natura dell'atto), la cassatura è `<del>` (con `@rend` = *come* è cassata). Quando cassatura e aggiunta sono **un solo atto sostitutivo** (es. la correzione di una lettera, *e→i*) si usa `<subst>` che le racchiude, non `del`+`add` sciolti — e lo schema (Schematron) esige che `subst` contenga almeno un `add` e un `del`.

```xml
<subst hand="#ink_1">
  <del place="inline" type="correction">e</del>
  <add place="inline" type="substitution">i</add>
</subst>
```

Il **ripasso** del tratto (non una variante di lezione, ma un rinforzo) è `<retrace>`; il ripristino d'autore è `<restore>`; il segno di richiamo o spostamento — che *non è testo* — è `<metamark>`.

Due assi vanno tenuti **distinti** e **non confusi**:
- **`@hand` = la mano fisica** (`#ink_1`, `#ink_2`, `#ink_3-dark`, `#pencil_1`, `#ink_4-external`): *chi/con che strumento* scrive;
- **`@wit` = la fase genetica** (i testimoni-strato del `listWit`): *in quale stadio* di elaborazione.

Lo stesso inchiostro può comparire in più fasi; la stessa fase può usare più mani. `retrace` porta `@hand`, non `@wit`.

## 4. L'apparato genetico (parallel-segmentation)

L'edizione è un **autografo stratificato**: non ci sono testimoni indipendenti da collazionare, ma *fasi* di riscrittura sullo stesso foglio. Il metodo TEI adatto è la **segmentazione parallela**: ogni luogo di variazione è un `<app>` che contiene la lezione a testo (`<lem>`) e le fasi (`<rdg>`).

Scelta ecdotica di fondo: **`lem` = ultima volontà autoriale**, cioè l'edizione critica (`@wit="#txt-c"`). Le fasi anteriori vanno in `rdg`, ordinate con `@varSeq`. La **mano esterna** (`#txt-4`) non fissa mai il testo: **mai a `lem`**, solo a `rdg`.

```xml
<app>
  <lem wit="#txt-c">silentio</lem>
  <rdg wit="#txt-b0" varSeq="1"><del place="inline" hand="#ink_1">sonno</del></rdg>
  <rdg wit="#txt-b1" varSeq="2"><add place="above" hand="#ink_1">silentio</add></rdg>
</app>
```

`lem` e `rdg` possono essere **vuoti**: una lezione presente in una fase ma assente nel testo critico (o viceversa) si rende con l'elemento vuoto, non omettendolo.

Gli **eventi IA controfattuali** (il protocollo −CIT / +TEXTsub / +CIT) sono anch'essi `rdg`, mai `lem`: l'IA non fissa mai il testo. Portano `@type="ai-counterfactual"`, `@resp="#AI_controllata"` e un `@ana` alla tassonomia `workflow` dell'header; il loro scarto d'impatto (ΔI) si misura sulle dimensioni D1 chiarezza · D2 coesione · D3 stabilità dottrinale.

```xml
<rdg type="ai-counterfactual" resp="#AI_controllata" ana="#workflow-rimozione" cert="medium">sonno</rdg>
```

## 5. L'interpretazione e l'indice d'impatto

L'annotazione interpretativa si àncora al testo tramite **`@ana` sul `seg`**, con puntatori alle categorie del `classDecl` (le 8 tassonomie): `@ana`, non un `@type` libero, perché deve restare *governata* dal vocabolario normativo. Regola: un valore per asse (eccetto `#phase-critical`, trasversale); nel dubbio si sale alla categoria superiore (*astensione semantica*).

Le **figure retoriche** si annotano in **stand-off** con `<span>`/`<spanGrp>`: il tratto di testo che realizza la figura si àncora per riferimento e si classifica con `@ana` su un vocabolario retorico locale (`#fig-metafora`, `#fig-similitudine`…), tenuto nel file del testo come `interpGrp`. Così l'annotazione retorica non spezza il flusso testuale e resta governata da un vocabolario, senza gravare sulla tassonomia normativa. Le relazioni esplicite fra loci (rischio↔operazione, intertesto) sono `<link>`/`<linkGrp>`; il referente generico è `<rs>`; il termine tecnico-mistico è `<term>`; la glossa autoriale è resa da `<add>` con una `<note type="glossa">` vuota (vedi §3). 
La glossa autoriale si codifica come **aggiunta materiale `<add>`** — con la collocazione grafica in `@place` (margin, interlinear…) e la mano in `@hand` — collocata **dentro il `<seg>`** che glossa e chiusa da una **`<note type="glossa">` vuota**, il cui `@ana` ne dichiara la funzione prudenziale (asse `operation`). Il contenimento nel segmento sostituisce il puntatore; `@corresp` resta riservato al solo legame `<fs>`-indice → `seg`.

L'**indice d'impatto** tiene distinta la *categoria discreta* dal *calcolo*. La categoria (`#impact-*`) sta in `@ana` sul `seg`; il fascio numerico sta in un `<fs>` (feature structure) in uno strato `<standOff type="impact-index">`, fratello di `<text>` nello stesso documento, collegato via `@corresp`. Si usa `fs`, **non `<val>`** (non ammesso in `seg`). La formula AHP — `I = (4·Fnorm + 2·N + 1·A)/7` con `F` dal rango dell'asse `operation` — è dichiarata **una volta** in `editorialDecl`; il valore `I` è prodotto dallo script, mai digitato a mano.

```xml
<standOff type="impact-index">
  <fs xml:id="idx-seg-c1p8-desiderio" corresp="#seg-c1p8-desiderio" cert="medium">
    <f name="N_band"><symbol value="critica"/></f>
    <f name="A_band"><symbol value="alta"/></f>
    <f name="N"><numeric value="0.90"/></f>
    <f name="A"><numeric value="0.85"/></f>
    <f name="F"><numeric value="2"/></f>
    <f name="Fnorm"><numeric value="0.667"/></f>
    <f name="I"><numeric value="0.760"/></f>
  </fs>
</standOff>
```

## 6. Citazioni ed entità

La citazione è `<cit>` che racchiude `<quote>` (con `@xml:lang`) e la fonte `<bibl>` — non un `<ref>` penzolante — ed è collocata **dentro il `<seg>`** che la contiene: la sua funzione intertestuale è dichiarata nell'`@ana` del `seg` (`#relation-intertesto-*`, ed eventualmente `#legittimazione-*`), non su `cit`; l'indice d'impatto resta sul `seg`. I rinvii interni sono `<ref>`/`<ptr>` con `@target` a `xml:id` esistenti. Le entità nominate (`<rs>`, `<orgName>`…) portano `@ref` alle entità dell'header; le date sono `<date>` normalizzate.

---

# Parte 2 · Vincoli su elementi e attributi

## 2.1 Vocabolari chiusi (dichiarati `editorialDecl`)

Questi attributi ammettono **solo** i valori elencati.

| Attributo | Valori |
|---|---|
| `div/@type` | `book` · `preface` · `chapter` |
| `add/@type` | `correction` · `substitution` · `integration` · `punctuation` |
| `del/@type` | `correction` · `deletion` · `substitution` · `integration` · `punctuation` |
| `add/@place`, `del/@place` | **canonici TEI:** `above` · `below` · `inline` · `margin` — **estensioni progetto:** `interlinear` · `interlinear-above` · `supralinear` · `margin-left` · `margin-right` |
| `del/@rend` | `strikethrough` · `erased` · `overwritten` · `expunged` · `crossed` |
| `gap/@reason`, `unclear/@reason` | `illegible` · `damage` · `ink-fade` · `abrasion` · `binding` · `hole` · `stain` · `trimmed` |
| `gap/@unit`, `supplied/@unit` | `char` · `chars` · `word` · `words` · `line` · `lines` |
| `supplied/@reason` | `hole` *(cause materiali, come `gap/@reason`)* |
| `app/@type` | `substitution` · `addition` · `deletion` · `transposition` · `variant` |
| `rdg/@type` | `authorial` · `external` · `ai-counterfactual` |
| `rdg/@cause` | `correction` · `clarification` · `orthodoxy` · `attenuation` · `precision` · `amplification` |
| `note/@type` | `editorial` · `doctrinal` · `contextual` · `glossa` · `critical` · `linguistic` |
| `hi/@rend` | `italic` · `underline` · `superscript` · `larger` · `spaced` · `rubric` |
| `fw/@type` | `header` · `footer` · `pageNum` · `sig` · `catch` |
| `@cert` (globale) | `low` · `medium` · `high` |

## 2.2 Regole trasversali

1. **0 dangling** — ogni `#id` (`@ana`/`@hand`/`@wit`/`@ref`/`@resp`/`@target`/`@corresp`) risolve a un `xml:id` reale (verifica cross-file in CI).
2. **Un valore per asse** in `@ana`, eccetto `#phase-critical` (che si affianca a una fase posizionale).
3. **Astensione semantica** — nel dubbio, categoria immediatamente superiore.
4. **Niente normalizzazione tacita** → sempre `choice`. **Niente lezioni inventate** → `unclear`/`gap`/`supplied` + `@cert`/`@resp`. **Attribuzione a due livelli**: le regolarizzazioni meccaniche (`orig`/`reg`, `abbr`/`expan`) sono attribuite **globalmente** all'editore nell'`editorialDecl` (nessun `@resp` per-istanza; `@cert` solo dove pertinente); gli interventi sostanziali o congetturali (`sic`/`corr`, `supplied`) sono attribuiti e certificati **per-istanza** (`@resp` + `@cert`, con `supplied` di default `cert="medium"`).
5. **`lem` = ultima volontà** (`#txt-c`); fasi ordinate con `@varSeq`; **`#txt-4` mai a `lem`**; eventi IA solo in `rdg` con `@resp="#AI_controllata"`.
6. **`@hand` (mano fisica) ≠ `@wit` (fase genetica).** `@type` su `add`/`del` (atto materiale) ≠ `@type` su `app` (variazione d'apparato).
7. **`I` mai a mano** — categoria in `@ana`, numeri in `<fs>` dallo script.

## 2.3 Inventario degli elementi

Il testo usa questi elementi (che il `tagsDecl` dell'header dichiara), raggruppati per funzione:

- **Struttura:** `div` `head` `argument` `titlePage` `titlePart` `p` `pb` `lb` `fw` `seg` `anchor`
- **Diplomatica:** `choice` `orig` `reg` `abbr` `expan` `sic` `corr` `unclear` `gap` `supplied` `foreign`
- **Genetica:** `add` `del` `subst` `restore` `retrace` `metamark`
- **Apparato:** `app` `lem` `rdg`
- **Interpretazione / stand-off:** `seg` `span` `spanGrp` `interp` `interpGrp` `link` `linkGrp` `rs` `hi` `term` `note` `soCalled`
- **Indice d'impatto:** `standOff` `fs` `f` `numeric` `symbol`
- **Citazioni ed entità:** `cit` `quote` `bibl` `ref` `ptr` `persName` `placeName` `orgName` `date`

---

# Appendice · Liste di valori (i puntatori)

Valori **chiusi**, letti dai file costruiti. Usare solo questi.

### A1 · `@hand` — le 5 mani
| Valore | Mano | medium |
|---|---|---|
| `#ink_1` | autografa, stesura base + correzioni/integrazioni inline | brown-ink |
| `#ink_2` | autografa, 2ª fase | brown-ink |
| `#ink_3-dark` | autografa, ritocchi (`retrace`) e glosse tardive | dark-ink |
| `#pencil_1` | autografa, correzioni/meditazioni a matita | pencil |
| `#ink_4-external` | mano **esterna** (mai a `lem`) | ink |

### A2 · `@wit` — gli 8 testimoni/fasi (ordine per `@varSeq`)
`#txt-b0` (1) · `#txt-b1` (2) · `#txt-1` (3) · `#txt-2` (4) · `#txt-3` (5) · `#txt-m` (6) · `#txt-4` (esterno) · `#txt-c` (edizione critica → solo a `lem`)

### A3 · `@ref` / `@resp` — le 17 entità
Persone `#Anna-La-Longa` `#s-teresa` `#dio` `#esterno` `#p-avila` `#p-john` `#p-molinos` `#CelestinoSanNicolo` `#editor` `#QA` · Luoghi `#Palermo` `#Caltanissetta` `#Sicilia` · Org `#AI_controllata` `#BCP` `#Carmelo` `#Inquisizione`

### A4 · `@ana` — le 8 tassonomie interpretative (un valore per asse)
| Asse | Valori |
|---|---|
| **func** *(senza prefisso)* | `#legittimazione(-biblica/-liturgica/-tradizione)` · `#pedagogia(-introduzione/-discernimento/-esemplificazione)` · `#rischio(-attenuatio/-precisatio/-declaratio)` · `#ethos(-umilta/-esperienza/-obbedienza)` |
| **impact** | `#impact-low/-medium/-high/-critical` |
| **risk** | `#risk-dottrinale/-quietismo/-panteismo/-impeccabilita/-ambiguita` |
| **mystic_state** | `#mystic_state-purificazione/-illuminazione/-quiete/-otium/-unione` |
| **operation** | `#operation-delimitazione/-attenuatio/-precisatio/-declaratio/-riequilibrio` |
| **exposition** | `#exposition-low/-medium/-high/-critical` |
| **phase** | `#phase-introduction/-mediana/-conclusive/-critical` |
| **relation** | `#relation-mistica`(+4) · `#relation-intertesto(-biblico/-liturgico/-teresiano/-molinista)` |

### A5 · `#fig-*` — figure retoriche (`interpGrp` in un `<standOff type="rhetorical-figures">`)
`#fig-metafora` `#fig-similitudine` `#fig-allegoria` `#fig-antitesi` `#fig-preterizione` `#fig-professio-fidei` *(dichiarate nell'`interpGrp`; estendibile alla bisogna)*

### A6 · `#area-*` — aree semantiche concettuali (`interpGrp type="area-concettuale"` in un `<standOff type="semantic-focus">`)

Vocabolario locale che proietta il testo su dieci **aree concettuali** ricorrenti; ogni tratto rilevante è ancorato con `<span>` e classificato via `@ana`. Non grava sulla tassonomia normativa.

`#area-obedientia` (obbedienza) · `#area-humilitas` (umiltà) · `#area-sapientia` (sapienza divina) · `#area-orthodoxia` (ortodossia) · `#area-purificatio` (purificazione) · `#area-ascensio` (ascesa) · `#area-pax` (pace/quiete) · `#area-otium` (otium) · `#area-unio` (unione/sposalizio) · `#area-desiderium` (desiderio)

### A7 · `#workflow-*` — operazioni IA controfattuali (tassonomia `workflow` dell'header)
`#workflow-rimozione` (−CIT) · `#workflow-recupero-cancellature` (+TEXTsub) · `#workflow-aggiunta` (+CIT) · `#workflow-validazione` — dimensioni ΔI: **D1** chiarezza · **D2** coesione · **D3** stabilità dottrinale.

---

## Conformità

Il set di tag qui descritto è verificato contro le specifiche **TEI P5** (`tei_all`): 0 errori al controllo strutturale (esistenza elementi, attributi ammessi, modelli di contenuto). Restano da eseguire in oXygen la validazione **RelaxNG** completa e i vincoli **Schematron** (0-dangling cross-file, `subst` = `add`+`del`, `lem`=`#txt-c`, IA solo `rdg`), che la forma **ODD** del progetto renderà automatici.
