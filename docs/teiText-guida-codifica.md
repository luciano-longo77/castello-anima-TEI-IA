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

Il testo è dato nella forma **interpretativa** costituita: trascrizione moderatamente interventista, con **normalizzazione grafica silenziosa e dichiarata** (cfr. [`criteri-trascrizione.md`](criteri-trascrizione.md), dalla *Nota al testo, §2*, e l'`editorialDecl` dell'header). L'unico apparato marcato inline è quello **sostanziale** (`app`/`lem`/`rdg`); le integrazioni editoriali restano segnalate (`supplied`/`gap`).

Tre principi lo governano:

1. **Ancoraggio.** Ogni puntatore (`#id`) usato — in `castello-anima-teiHeader.xml` (mani, testimoni, entità, tassonomia `workflow`) o in `tassonomia-gh.xml` (categorie `@ana`) — risolve a un `xml:id` reale.
2. **Trasparenza filologica a due livelli.** La **normalizzazione grafica** è dichiarata *una volta per tutte* e applicata silenziosamente (nessun `@resp` per-istanza); gli interventi **sostanziali** (varianti d'apparato) e **congetturali** (integrazioni `supplied`) sono marcati, attribuiti e certificati **per-istanza**.
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

L'unità portante dell'annotazione è **`<seg>`**, non `<ab>` né `<p>`: è l'unica che porta `@ana` (l'interpretazione) a granularità sub-paragrafo ed è governata dal `classDecl`. Ogni `seg` del corpo ha un `@xml:id` nel formato `seg-b<libro>-c<cap>p<par>-<label>` (`b<libro>` = numero del libro, es. `b1`, `b3`; es. `seg-b1-c2p6-nemico-demonio`, `seg-b3-c1p8-desiderio`), che diventa l'ancora per l'apparato e per l'indice d'impatto.

```xml
<seg xml:id="seg-b3-c1p8-desiderio" ana="#operation-precisatio #risk-quietismo #impact-high" hand="#ink_1">
  incomincia l'anima a perdire qualunque desiderio
</seg>
```

Dove serve un ancoraggio *senza* spezzare il flusso (per lo stand-off), si usa `<anchor xml:id="…"/>`.

## 2. Trascrizione interpretativa e integrazioni

Il testo è dato **già nella forma interpretativa costituita**. La normalizzazione grafica — grafia e diacritici, interpunzione, scioglimento delle abbreviazioni, divisione delle parole, maiuscole/minuscole, refusi di copia — è applicata **silenziosamente** e dichiarata una volta per tutte in [`criteri-trascrizione.md`](criteri-trascrizione.md) e nell'`editorialDecl`. Nel testo di lettura **non** compaiono elementi diplomatici inline: nessun `<choice>`, né le sue coppie `orig`/`reg`, `sic`/`corr`, `abbr`/`expan`. La forma a testo è già quella regolarizzata.

Restano marcate le sole **integrazioni e incertezze materiali**: la **lettura incerta** è `<unclear reason="…" cert="…">`, la **perdita materiale** è `<gap reason="…" unit="…"/>`, l'**integrazione congetturale o su guasto** è `<supplied reason="hole" resp="#editor" cert="medium">` — dove `@reason` registra la causa materiale (es. il buco della carta) e `@cert` il grado della congettura. Corrispondono alle parentesi quadre `[ ]` della Nota al testo.

```xml
que<supplied reason="hole" resp="#editor" cert="high">ste</supplied>
```

Il **latino citazionale** non si marca come lingua straniera ma come citazione: `<cit>`/`<quote xml:lang="la">` (vedi §6); `<foreign xml:lang="la">` resta disponibile per spezzoni in lingua *non* citazionali (nel corpus attuale: nessuno).

## 3. La genetica d'autrice (nell'apparato)

Il *lavoro dell'autrice sul foglio* — le varianti **sostanziali**: ripensamenti, aggiunte, cassature, sostituzioni teologicamente o filologicamente rilevanti — si registra **dentro l'apparato** (`app`/`rdg`, §4), non inline nel testo di lettura. Gli elementi `<add>` (aggiunta, con `@place` topografico e `@type` = natura dell'atto), `<del>` (cassatura, con `@rend` = *come* è cassata) e `<subst>` (quando cassatura e aggiunta sono **un solo atto sostitutivo**; lo Schematron esige che `subst` contenga almeno un `add` e un `del`) compaiono quindi **entro i `<rdg>`**.

```xml
<rdg wit="#txt-b0" varSeq="1">
  <subst hand="#ink_1"><del rend="strikethrough">sonno</del><add place="above">silentio</add></subst>
</rdg>
```

Le correzioni puramente **grafiche** — lettera-su-lettera, refusi di copia, regolarizzazioni — rientrano nella **normalizzazione silenziosa** (§2) e **non si marcano**. Restano invece inline, perché non sono varianti di lezione:
- il **ripasso** del tratto (rinforzo, non variante) è `<retrace>` — porta `@hand`, ed è lo strumento dello strato prudenziale tardivo a inchiostro scuro (`#ink_3-dark`, T3);
- il ripristino d'autore è `<restore>`; il segno di richiamo o spostamento — che *non è testo* — è `<metamark>`.

Due assi vanno tenuti **distinti** e **non confusi**:
- **`@hand` = la mano fisica** (`#ink_1`, `#ink_2`, `#ink_3-dark`, `#pencil_1`, `#ink_4-external`): *chi/con che strumento* scrive;
- **`@wit` = la fase genetica** (i testimoni-strato del `listWit`): *in quale stadio* di elaborazione.

Lo stesso inchiostro può comparire in più fasi; la stessa fase può usare più mani. `retrace` porta `@hand`, non `@wit`.

## 4. L'apparato sostanziale (parallel-segmentation)

L'edizione è un **autografo stratificato**: non ci sono testimoni indipendenti da collazionare, ma *fasi* di riscrittura sullo stesso foglio. Il metodo TEI adatto è la **segmentazione parallela**: ogni luogo di variazione **sostanziale** è un `<app>` che contiene la lezione a testo (`<lem>`) e le fasi (`<rdg>`). È l'**unico** apparato marcato inline: le regolarizzazioni grafiche non vi entrano (sono silenziose, §2).

Scelta ecdotica di fondo: **`lem` = ultima volontà autoriale**, cioè l'edizione critica (`@wit="#txt-c"`). Le fasi anteriori vanno in `rdg`, ordinate con `@varSeq`. La **mano esterna** (`#txt-4`) non fissa mai il testo: **mai a `lem`**, solo a `rdg`.

```xml
<app>
  <lem wit="#txt-c">silentio</lem>
  <rdg wit="#txt-b0" varSeq="1"><del place="inline" hand="#ink_1">sonno</del></rdg>
  <rdg wit="#txt-b1" varSeq="2"><add place="above" hand="#ink_1">silentio</add></rdg>
</app>
```

`lem` e `rdg` possono essere **vuoti**: una lezione presente in una fase ma assente nel testo critico (o viceversa) si rende con l'elemento vuoto, non omettendolo.

Gli **eventi IA controfattuali** (il protocollo -CIT / +TEXTsub / +CIT) sono anch'essi `rdg`, mai `lem`: l'IA non fissa mai il testo. **Non entrano nel teiText**: per non mescolare l'apparato genetico d'autrice con lo strato sperimentale, sono registrati nell'apparato standoff **esterno** [`../variants/castello-anima-variants.xml`](../variants/castello-anima-variants.xml), come `<app loc="seg-…">` (ancoraggio *location-referenced*, `xml:id` nudo del `<seg>`) con `<lem wit="#txt-c">` e un `<rdg resp="#AI_controllata">`. L'operazione sta su **`@type`** (`workflow-rimozione` / `workflow-recupero-cancellature` / `workflow-aggiunta`), **non** su `@ana`: la tassonomia `workflow` è nell'header (riservata al `revisionDesc`) e la guardia **E2** risolve gli `@ana` del testo solo contro `tassonomia-gh.xml`. Il loro scarto d'impatto (ΔI) si misura sulle dimensioni D1 chiarezza · D2 coesione · D3 stabilità dottrinale.

```xml
<!-- in variants/castello-anima-variants.xml, NON nel teiText -->
<app loc="seg-b2-c8p9-luce-tenebre" type="workflow-rimozione">
  <lem wit="#txt-c">…lezione costituita con la citazione…</lem>
  <rdg resp="#AI_controllata" cert="high"/>
</app>
```

## 5. L'interpretazione e l'indice d'impatto

L'annotazione interpretativa si àncora al testo tramite **`@ana` sul `seg`**, con puntatori alle categorie del `classDecl` (le 8 tassonomie): `@ana`, non un `@type` libero, perché deve restare *governata* dal vocabolario normativo. Regola: un valore per asse (eccetto `#phase-critical`, trasversale); nel dubbio si sale alla categoria superiore (*astensione semantica*).

Le **figure retoriche** si annotano in **stand-off** con `<span>`/`<spanGrp>`: il tratto di testo che realizza la figura si àncora per riferimento e si classifica con `@ana` su un vocabolario retorico locale (`#fig-metafora`, `#fig-similitudine`…), tenuto nel file del testo come `interpGrp`. Così l'annotazione retorica non spezza il flusso testuale e resta governata da un vocabolario, senza gravare sulla tassonomia normativa. Le relazioni esplicite fra loci (rischio↔operazione, intertesto) sono `<link>`/`<linkGrp>`; il referente generico è `<rs>`; il termine tecnico-mistico è `<term>`; la glossa autoriale è resa da `<add>` con una `<note type="glossa">` vuota (vedi sotto).

La glossa autoriale si codifica come **aggiunta materiale `<add>`** — con la collocazione grafica in `@place` (margin, interlinear…) e la mano in `@hand` — collocata **dentro il `<seg>`** che glossa e chiusa da una **`<note type="glossa">` vuota**, il cui `@ana` ne dichiara la funzione prudenziale (asse `operation`). Il contenimento nel segmento sostituisce il puntatore; `@corresp` resta riservato al solo legame `<fs>`-indice → `seg`.

L'**indice d'impatto** tiene distinta la *categoria discreta* dal *calcolo*. La categoria (`#impact-*`) sta in `@ana` sul `seg`; il fascio numerico sta in un `<fs>` (feature structure) in uno strato `<standOff type="impact-index">`, fratello di `<text>` nello stesso documento, collegato via `@corresp`. Si usa `fs`, **non `<val>`** (non ammesso in `seg`). La formula AHP — `I = (4·Fnorm + 2·N + 1·A)/7` con `F` dal rango dell'asse `operation` — è dichiarata **una volta** in `editorialDecl`; il valore `I` è prodotto dallo script, mai digitato a mano.

```xml
<standOff type="impact-index">
  <fs xml:id="idx-seg-b3-c1p8-desiderio" corresp="#seg-b3-c1p8-desiderio" cert="medium">
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

Le **catene semantiche** raccolgono in **stand-off** i legami tematici e relazionali fra `<seg>`: nello `<standOff type="semantic-chains">` ogni `<linkGrp type="…" subtype="…">` contiene un `<link target="#seg-… #seg-…">` che unisce i segmenti che condividono un tema, una metafora o una relazione (rischio↔operazione, intertesto). A differenza dell'indice d'impatto (una `<fs>` per seg) e del focus (una o più aree per seg), le catene sono **facoltative** e collegano *insiemi* di segmenti. Coprono **tutti e tre i libri**: 199 `<linkGrp>` in totale (Libro I 40, Libro II 46, Libro III 113).

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
| `rdg/@type` | `authorial` · `external` *(le varianti IA controfattuali stanno nell'apparato esterno: `app/@type=workflow-*` + `rdg/@resp=#AI_controllata`, cfr. §4)* |
| `rdg/@cause` | `correction` · `clarification` · `orthodoxy` · `attenuation` · `precision` · `amplification` |
| `note/@type` | `editorial` · `doctrinal` · `contextual` · `glossa` · `critical` · `linguistic` |
| `hi/@rend` | `italic` · `underline` · `superscript` · `larger` · `spaced` · `rubric` |
| `fw/@type` | `header` · `footer` · `pageNum` · `sig` · `catch` |
| `@cert` (globale) | `low` · `medium` · `high` |

> Gli elementi `add`/`del`/`subst` compaiono **solo dentro `app`/`rdg`** (§3–4). Gli elementi diplomatici di normalizzazione (`choice`, `orig`/`reg`, `sic`/`corr`, `abbr`/`expan`) **non sono usati** nel modello interpretativo: la normalizzazione è silenziosa e dichiarata (§2).

## 2.2 Regole trasversali

1. **0 dangling** — ogni `#id` (`@ana`/`@hand`/`@wit`/`@ref`/`@resp`/`@target`/`@corresp`) risolve a un `xml:id` reale (verifica cross-file in CI).
2. **Un valore per asse** in `@ana`, eccetto `#phase-critical` (che si affianca a una fase posizionale).
3. **Astensione semantica** — nel dubbio, categoria immediatamente superiore.
4. **Normalizzazione grafica silenziosa** → dichiarata una volta per tutte ([`criteri-trascrizione.md`](criteri-trascrizione.md) + `editorialDecl`), **nessun `choice`** inline. **Niente lezioni inventate** → `unclear`/`gap`/`supplied` + `@cert`/`@resp`. **Attribuzione**: la normalizzazione grafica è attribuita **globalmente** all'editore (nessun `@resp` per-istanza); restano attribuiti e certificati **per-istanza** i soli interventi **sostanziali** (varianti d'apparato `app`/`rdg`) e **congetturali** (`supplied`, di default `cert="medium"`).
5. **`lem` = ultima volontà** (`#txt-c`); fasi ordinate con `@varSeq`; **`#txt-4` mai a `lem`**; eventi IA solo in `rdg` con `@resp="#AI_controllata"`.
6. **`@hand` (mano fisica) ≠ `@wit` (fase genetica).** `@type` su `add`/`del` (atto materiale) ≠ `@type` su `app` (variazione d'apparato).
7. **`I` mai a mano** — categoria in `@ana`, numeri in `<fs>` dallo script.

## 2.3 Inventario degli elementi

Il testo usa questi elementi (che il `tagsDecl` dell'header dichiara), raggruppati per funzione:

- **Struttura:** `div` `head` `argument` `titlePage` `titlePart` `p` `pb` `lb` `fw` `seg` `anchor`
- **Integrazioni / incertezze:** `unclear` `gap` `supplied` `foreign`
- **Genetica (dentro l'apparato):** `add` `del` `subst` `restore` `retrace` `metamark`
- **Apparato sostanziale:** `app` `lem` `rdg`
- **Interpretazione / stand-off:** `seg` `span` `spanGrp` `interp` `interpGrp` `link` `linkGrp` `rs` `hi` `term` `note` `soCalled`
- **Indice d'impatto:** `standOff` `fs` `f` `numeric` `symbol`
- **Citazioni ed entità:** `cit` `quote` `bibl` `ref` `ptr` `persName` `placeName` `orgName` `date`

> Non compaiono nel testo di lettura, coerentemente col modello interpretativo: `choice` `orig` `reg` `abbr` `expan` `sic` `corr`.

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

Vocabolario locale che proietta il testo su **31 aree concettuali** (dichiarate nell'`interpGrp type="area-concettuale"`); ogni tratto rilevante è ancorato con `<span>` e classificato via `@ana`. Non grava sulla tassonomia normativa.

`#area-obedientia` (obbedienza) · `#area-humilitas` (umiltà) · `#area-sapientia` (sapienza divina) · `#area-orthodoxia` (ortodossia) · `#area-purificatio` (purificazione) · `#area-ascensio` (ascesa) · `#area-pax` (pace/quiete) · `#area-otium` (otium) · `#area-unio` (unione/sposalizio) · `#area-desiderium` (desiderio) · `#area-innocentia` (innocenza, stato adamico) · `#area-passio` (passione/croce) · `#area-abnegatio` (distacco e abnegazione) · `#area-amor-proprius` (amor proprio) · `#area-conversio` (conversione dell'io) · `#area-directio-spiritualis` (direzione spirituale) · `#area-gratia` (grazia) · `#area-imitatio-Christi` (imitazione di Cristo) · `#area-intellectus` (intelletto) · `#area-militia-spiritualis` (militia spiritualis) · `#area-miseria-mundi` (miseria del mondo) · `#area-mortificatio` (mortificazione) · `#area-mundus` (mondo) · `#area-nox-sensuum` (notte dei sensi esterni) · `#area-oratio` (oratione) · `#area-sponsa-Christi` (anima sposa di Cristo) · `#area-superbia` (superbia) · `#area-tentatio` (tentazione) · `#area-veritas` (verità che libera) · `#area-vita-religiosa` (vita religiosa) · `#area-voluntas` (volontà)

### A7 · `#workflow-*` — operazioni IA controfattuali (tassonomia `workflow` dell'header)
`#workflow-rimozione` (-CIT) · `#workflow-recupero-cancellature` (+TEXTsub) · `#workflow-aggiunta` (+CIT) · `#workflow-validazione` — dimensioni ΔI: **D1** chiarezza · **D2** coesione · **D3** stabilità dottrinale.

---

## Conformità

Il set di tag qui descritto è verificato contro le specifiche **TEI P5** (`tei_all`): 0 errori al controllo strutturale (esistenza elementi, attributi ammessi, modelli di contenuto). Restano da eseguire in oXygen la validazione **RelaxNG** completa e i vincoli **Schematron** (0-dangling cross-file, `subst` = `add`+`del`, `lem`=`#txt-c`, IA solo `rdg`), che la forma **ODD** del progetto renderà automatici.
