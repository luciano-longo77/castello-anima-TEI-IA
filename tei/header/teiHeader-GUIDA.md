# Guida alla navigazione del *teiHeader*
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

## Indice
- [1. Cos'è questo file](#1-cosè-questo-file)
- [2. Struttura generale del teiHeader](#2-struttura-generale-del-teiheader)
- [3. Mappa rapida della navigazione](#3-mappa-rapida-della-navigazione)
- [4. Il sistema tassonomico (classDecl)](#4-il-sistema-tassonomico-classdecl)
- [5. Mani e testimoni](#5-mani-e-testimoni)
- [6. Responsabilità e agenti](#6-responsabilità-e-agenti)
- [7. Protocollo IA e audit-trail (xenoData)](#7-protocollo-ia-e-audit-trail-xenodata)
- [8. Il diario editoriale (revisionDesc)](#8-il-diario-editoriale-revisiondesc)
- [9. Come cercare velocemente](#9-come-cercare-velocemente)
- [10. Riferimenti utili](#10-riferimenti-utili)
- [11. Contatti](#11-contatti)

---

## 1. Cos'è questo file

`castello-anima-teiHeader.xml` è il **modello di descrizione** dell'edizione: contiene tutti i **metadati** — bibliografici, codicologici, tassonomici, di protocollo IA e di tracciabilità — ma **non** il testo del manoscritto, che sta nel file separato `../text/castello-anima-teiText.xml` e richiama l'header via `xi:include`. Questa separazione tiene distinti il **testo-oggetto** (là) e il **modello che lo descrive** (qui).

Per capire *dov'è* e *com'è codificato* un passo, si usa la guida del testo ([`../text/teiText-GUIDA.md`](../text/teiText-GUIDA.md)); per capire *cosa significa* un `@ana`, una mano, un testimone o un agente responsabile, si usa **questa** guida. Il riferimento tecnico completo dell'header è [`teiHeader-README.md`](teiHeader-README.md).

## 2. Struttura generale del teiHeader

```
<teiHeader>
 ├── <fileDesc>                     ← identità bibliografica dell'edizione
 │     ├── <titleStmt>               ← titolo, autrice, editor, responsabilità
 │     ├── <editionStmt> · <publicationStmt>  ← edizione, editore, licenza (CC BY 4.0)
 │     ├── <notesStmt xml:id="notes-for-castello-anima">
 │     └── <sourceDesc>              ← <listWit> (testimoni Tb0…Tc), descrizione del ms
 ├── <encodingDesc>                 ← come è codificata l'edizione
 │     ├── <projectDesc> · <refsDecl> · <samplingDecl> · <editorialDecl> · <tagsDecl>
 │     ├── <variantEncoding> ×2      ← modello dell'apparato (inline + esterno)
 │     ├── <listPrefixDef>           ← prefissi (es. seg-, idx-)
 │     ├── <classDecl>               ← ★ le 12 tassonomie (categorie di @ana + processo)
 │     └── <schemaRef type="schematron">
 ├── <profileDesc>                  ← contesto interpretativo
 │     ├── <langUsage> · <textClass>
 │     └── <particDesc>              ← <listPerson> / <listOrg>: agenti e riferimenti
 ├── <xenoData> ×2                  ← ★ protocollo IA (JSON) + puntatore METS
 └── <revisionDesc>                 ← ★ 95 <change>: il diario editoriale datato
```

I tre nodi contrassegnati con ★ — `classDecl`, `xenoData`, `revisionDesc` — sono quelli che il `teiText` richiama continuamente: le categorie di `@ana`, il protocollo di simulazione IA e la cronologia delle fasi/operazioni.

## 3. Mappa rapida della navigazione

### 🔹 Per capire cosa significa una categoria `@ana`
Vai nel `classDecl` ([§4](#4-il-sistema-tassonomico-classdecl)): cerca la `<category xml:id="…">` con quell'id e leggine il `<catDesc>`. Es. `#operation-attenuatio`, `#risk-quietismo`, `#impact-high`. La sintesi discorsiva delle categorie è anche in [`../../docs/data-dictionary.md`](../../docs/data-dictionary.md).

### 🔹 Per sapere qual è una mano
Nel `sourceDesc` → `physDesc/handDesc` cerca la `<handNote xml:id="ink_…">` ([§5](#5-mani-e-testimoni)). Es. `#ink_1` (autografa, inchiostro bruno), `#ink_3-dark` (aggiunta tardiva), `#ink_4-external` (mano esterna).

### 🔹 Per sapere cos'è un testimone
Nel `sourceDesc` → `<listWit>` cerca la `<witness xml:id="txt-…">` ([§5](#5-mani-e-testimoni)). Es. `#txt-b0` (testo base Tb0), `#txt-c` (edizione critica Tc, cioè il `lem` dell'apparato).

### 🔹 Per sapere chi è un agente responsabile (`@resp` / `@who`)
Nel `particDesc` cerca la `<person xml:id="…">` o la `<org xml:id="…">` ([§6](#6-responsabilità-e-agenti)). Es. `#editor`, `#s-teresa`, `#esterno`, `#AI_controllata`, `#QA`.

### 🔹 Per capire il protocollo IA e la sua tracciabilità
Vai nel primo `<xenoData>` (blocco JSON, [§7](#7-protocollo-ia-e-audit-trail-xenodata)): modello, operazioni (−CIT / +TEXTsub / +CIT), parametri, e i `required_fields` dell'`audit_trail` — le stesse 9 colonne di [`../../logs/runs.tsv`](../../logs/runs.tsv).

### 🔹 Per ricostruire la storia del lavoro
Vai nel `revisionDesc` ([§8](#8-il-diario-editoriale-revisiondesc)): ogni `<change when="…" who="#…" ana="#fase-…|#workflow-…">` è un passo datato, attribuito e classificato.

### 🔹 Per le bande dell'indice d'impatto
I vocabolari `impact-band-N` e `impact-band-A` sono nel `classDecl`, ma **non** si applicano via `@ana`: alimentano i `symbol` delle `fs` nello `standOff impact-index` del `teiText`. Formula e soglie stanno in [`../../docs/indice-impatto.md`](../../docs/indice-impatto.md).

## 4. Il sistema tassonomico (classDecl)

Il `classDecl` contiene **12 tassonomie (8+2+2)** per un totale di **106 categorie** = **60 interpretative** (le stesse di [`../taxonomy/tassonomia-gh.xml`](../taxonomy/tassonomia-gh.xml)) + **46 editoriali** (`fase` + `workflow`, riservate al `revisionDesc`).

```
INTERPRETATIVE (via @ana)        AUSILIARIE (nei symbol delle fs)   DI PROCESSO (solo revisionDesc)
├── func (4 rami · 16 categorie) ├── impact-band-N (4)              ├── fase (42)
├── operation (5)                └── impact-band-A (3)              └── workflow (4)
├── risk (5)
├── exposition (4)
├── phase (4)
├── mystic_state (5)
├── relation (10)
└── impact (4)
```

- **8 assi interpretativi** applicati al testo via `@ana` sui `<seg>`, nell'ordine canonico **func · operation · risk · exposition · phase · mystic_state · relation · impact** (`relation` è ripetibile; `#phase-critical` è un **modificatore**, non un asse).
- **2 vocabolari-banda ausiliari** (`impact-band-N`, `impact-band-A`): non vanno su `@ana`, servono alle `<fs>` dell'indice d'impatto.
- **2 tassonomie di processo** (`fase` 42, `workflow` 4): **non** vanno su `@ana` del testo, ma sull'`@ana` dei `<change>` del `revisionDesc` ([§8](#8-il-diario-editoriale-revisiondesc)).

> **Nota sugli `xml:id`.** Ogni categoria ha `xml:id` e `catDesc` non vuoto; l'`xml:id` porta il prefisso della tassonomia radice — **eccetto l'asse `func`**, esente per consentire ai suoi quattro rami di primo livello (`legittimazione`, `pedagogia`, `rischio`, `ethos`) di non portare il prefisso `func-`.

## 5. Mani e testimoni

**Mani** (`handDesc/handNote`) — la stratigrafia materiale del manoscritto:

| id | supporto | fase | descrizione |
|---|---|---|---|
| `#ink_1` | inchiostro bruno | T0/T1 | mano **principale autografa** di Teresa; grafia di base |
| `#ink_2` | inchiostro bruno | T1, T2 | seconda fase autografa: glosse e interventi marginali |
| `#ink_3-dark` | inchiostro scuro | T3 | intervento autografo **tardivo** (margini, righe bianche) |
| `#ink_4-external` | inchiostro | T4 | **mano esterna** non identificata; note marginali/foglietti (Libro III) |
| `#pencil_1` | matita | Tm | strato autografo a matita: correzioni e brevi annotazioni |

**Testimoni** (`listWit/witness`) — gli strati redazionali che l'apparato mette a confronto:

| id | sigla | cos'è |
|---|---|---|
| `#txt-b0` | Tb0 | testo base |
| `#txt-b1` | Tb1 | interventi immediati |
| `#txt-1` | T1 | riscrittura sul testo base |
| `#txt-2` | T2 | interventi correttivi-glossativi |
| `#txt-3` | T3 | interventi correttivi-glossativi successivi (medium diverso) |
| `#txt-m` | Tm | interventi autografi a matita |
| `#txt-4` | T4 | interventi glossativi esterni |
| `#txt-c` | Tc | **edizione critica** — il `<lem>` dell'apparato, l'*ultima volontà* |

Non tutte le mani e tutti i testimoni compaiono nel campione codificato: il modello dichiara la stratigrafia **completa** del manoscritto, mentre il `teiText` usa (via `@hand` / `@wit`) il sottoinsieme effettivamente attestato nei loci trattati (tipicamente `#ink_1`, `#ink_3-dark`, `#ink_4-external`; `#txt-b0`, `#txt-c`).

## 6. Responsabilità e agenti

Nel `particDesc` sono dichiarati gli agenti (bersaglio di `@resp` nel testo/apparato e di `@who` nel `revisionDesc`) e i riferimenti storici e dottrinali.

**Agenti operativi** — chi *fa* qualcosa nell'edizione:

| id | tipo | ruolo |
|---|---|---|
| `#editor` | person | Luciano Longo, responsabile dell'edizione critica |
| `#QA` | person | Quality Assurance: controllo strutturale e tassonomico TEI |
| `#s-teresa` | person | l'autrice autografa (interventi d'autrice) |
| `#esterno` | person | mano esterna non identificata (note marginali, Libro III) |
| `#AI_controllata` | org | pipeline IA controllata: generazione eventi controfattuali sotto vincolo |

**Riferimenti** — chi/che cosa il testo *evoca*: `#Anna-La-Longa` (identità civile dell'autrice), `#dio` (referente divino), `#p-avila`, `#p-john`, `#p-molinos`, `#CelestinoSanNicolo` (guide dottrinali/spirituali), e le istituzioni `#Carmelo`, `#Inquisizione`, `#BCP` (Biblioteca Comunale di Palermo, luogo di conservazione).

## 7. Protocollo IA e audit-trail (xenoData)

Il primo `<xenoData>` è un blocco **JSON** che formalizza il protocollo di simulazione:

- **model** — `primary: Claude Opus 4.8`, `fallback: Gemini` (coerente con [`../../AI-USE.md`](../../AI-USE.md)), con i vincoli di stile secentesco e integrità TEI;
- **operations** — `−CIT` (rimozione), `+TEXTsub` (recupero cancellature), `+CIT` (integrazione citazione, `max_words: 35`, l'unica **generativa**);
- **parameters** — `temperature 0.2`, `top_p 0.95`;
- **audit_trail.required_fields** — `locus_id · operation · seed · model · prompt_hash · output_hash · reviewer · esito · notes`: **le stesse 9 colonne, nello stesso ordine**, di [`../../logs/runs.tsv`](../../logs/runs.tsv);
- **governance** — `expert-in-the-loop`.

Il secondo `<xenoData type="mets">` contiene il puntatore METS (`mets.xml`). Il razionale completo del protocollo è in [`../../docs/protocollo-IA-codifica.md`](../../docs/protocollo-IA-codifica.md); sul `seed` **nominale** in `+CIT` (il motore non espone un `seed`, la riproducibilità poggia su modello+versione, prompt e `output_hash`) vedi lì e in [`../../logs/README.md`](../../logs/README.md).

## 8. Il diario editoriale (revisionDesc)

Il `revisionDesc` raccoglie **95 `<change>`** datati e attribuiti. Ogni voce ha:

- `@when` — la data;
- `@who` — l'agente (`#editor`, `#QA`, `#AI_controllata`);
- `@ana` — la classificazione, presa **esclusivamente** dalle tassonomie di processo del `classDecl`: **`#fase-…`** (42 fasi di lavoro, es. `#fase-annotazione-campione`, `#fase-quality-assurance`) oppure **`#workflow-…`** (le 4 operazioni: `#workflow-rimozione`, `#workflow-recupero-cancellature`, `#workflow-aggiunta`, `#workflow-validazione`).

È qui — e solo qui — che vivono `fase` e `workflow`: sul `<seg>` del testo non compaiono mai. Le operazioni controfattuali `#workflow-*` tracciate qui trovano riscontro nell'apparato esterno ([`../../variants/README.md`](../../variants/README.md)) e nei log ([`../../logs/runs.tsv`](../../logs/runs.tsv)).

## 9. Come cercare velocemente

| Cerchi… | Come |
|---|---|
| il significato di una categoria `@ana` | `xml:id="…"` nel `classDecl` → leggi il `<catDesc>` |
| una mano | `<handNote xml:id="ink_…">` in `handDesc` |
| un testimone / la sigla di uno strato | `<witness xml:id="txt-…">` in `<listWit>` |
| chi è un `@resp` / `@who` | `<person>` / `<org>` con quell'`xml:id` nel `particDesc` |
| le operazioni IA e i loro codici | primo `<xenoData>` (JSON) → `operations` |
| i campi di tracciabilità di una run | `<xenoData>` → `audit_trail.required_fields` |
| quando e da chi è stato fatto un passo | `<change>` nel `revisionDesc` (`@when` · `@who` · `@ana`) |
| dov'è e com'è codificato un passo | → nel `teiText` ([`../text/teiText-GUIDA.md`](../text/teiText-GUIDA.md)) |

## 10. Riferimenti utili

- Riferimento tecnico del file: [`teiHeader-README.md`](teiHeader-README.md)
- Guida al testo (dove sono i passi): [`../text/teiText-GUIDA.md`](../text/teiText-GUIDA.md)
- Tassonomia interpretativa (fonte delle 60 categorie): [`../taxonomy/tassonomia-gh.xml`](../taxonomy/tassonomia-gh.xml)
- Dizionario delle categorie: [`../../docs/data-dictionary.md`](../../docs/data-dictionary.md)
- Protocollo della codifica AI-assisted: [`../../docs/protocollo-IA-codifica.md`](../../docs/protocollo-IA-codifica.md)
- Indice d'impatto (formula e bande): [`../../docs/indice-impatto.md`](../../docs/indice-impatto.md)
- Log delle run e apparato esterno: [`../../logs/README.md`](../../logs/README.md) · [`../../variants/README.md`](../../variants/README.md)

## 11. Contatti

**Luciano Longo** — <luciano.longo@dedalus.com> · [ORCID](https://orcid.org/0009-0005-7557-7546) · [GitHub](https://github.com/luciano-longo77)
