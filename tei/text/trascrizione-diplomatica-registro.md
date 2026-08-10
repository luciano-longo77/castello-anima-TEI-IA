# Trascrizione diplomatica - procedure e registro degli interventi
## Dal livello diplomatico al livello interpretativo
### Intertestualità sotto sorveglianza
#### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)
**Editor**: Luciano Longo
**Licenza**: CC BY 4.0

*Documento operativo: descrive **dove** si interviene sul testo e **come** si rende
l'intervento in TEI, e fornisce una **tabella-registro** da compilare per annotare ogni
passaggio dalla trascrizione diplomatica all'edizione interpretativa.*

---

## 1. Principio

La **trascrizione diplomatica** conserva il testimone così com'è: grafie d'autore,
abbreviazioni, cancellature, aggiunte, incertezze di lettura, materialità della pagina.
Non corregge e non normalizza in modo silenzioso: **ogni scelta editoriale è marcata e
attribuita** (`@resp`), così che la lezione originale resti sempre recuperabile.

Il passaggio al **livello interpretativo** non cancella il diplomatico: lo **stratifica**.
La forma d'autore e la forma regolarizzata convivono in `<choice>`; l'interpretazione
(funzione retorica, rischio, impatto…) si aggiunge sopra, tramite `@ana` sul `<seg>` e gli
strati `<standOff>`.

---

## 2. Dove si interviene e come

Ogni fenomeno del testimone ha **una** soluzione TEI canonica nel progetto. La lezione
diplomatica non si perde mai: sta in `orig` / `sic` / `abbr` / `del`, la forma editoriale in
`reg` / `corr` / `expan` / `add`.

| Fenomeno sul testimone | Soluzione TEI | Attributi chiave | Esempio (dal *Castello*) |
|---|---|---|---|
| Grafia d'autore da regolarizzare | `choice` › `orig` / `reg` | — | à → a |
| Errore evidente da correggere | `choice` › `sic` / `corr` | — | sapere → sapete |
| Abbreviazione / sigla da sciogliere | `choice` › `abbr` / `expan` | — | I.M.I. → Iesus Maria Ioseph |
| Cancellatura autoriale | `del` | `@rend @hand @resp @type` | del *to* (rend=strikethrough) |
| Aggiunta autoriale | `add` | `@place @hand @resp @type` | add *i* (place=inline) |
| Sostituzione (cancella + aggiunge) | `subst` › `del` + `add` | `@hand` | *to* → *i* entro subst |
| Variante fra fasi redazionali | `app` › `lem` / `rdg` | `@wit @varSeq` | lem *secondo* / rdg *to secondo* |
| Lettura incerta | `unclear` | `@reason @cert` | unclear reason=ink-fade |
| Perdita materiale (lacuna) | `gap` | `@reason @unit @quantity` | gap reason=damage unit=word |
| Integrazione congetturale dell'editore | `supplied` | `@reason @resp` | supplied resp=#editor |
| Latino entro il volgare | `foreign` | `@xml:lang="la"` | foreign *Consummatum est* |
| Enfasi grafica (non semantica) | `hi` | `@rend` | hi rend=rubric |
| Materiale di cornice (segnatura, richiamo, n. carta) | `fw` | `@type` | fw type=catch |
| Cambio di carta / foliazione | `pb` | `@n` | pb n=158r |
| A-capo di parola spezzata (solo questo) | `lb` | `@break="no"` | lb break=no |

> **Non si tocca** con marcatura editoriale: punteggiatura e maiuscole possono essere
> regolarizzate **solo** dentro `reg`/`corr` (mai in silenzio); gli a-capo ordinari **non**
> si segnano con `<lb/>` (riservato alle sole parole spezzate).

### Vocabolari chiusi (promemoria)

- `del/@rend`: `strikethrough · erased · overwritten · expunged · crossed`
- `del/@type`, `add/@type`: `correction · substitution · addition · deletion · clarification`
- `gap/@reason`, `unclear/@reason`: `illegible · damage · ink-fade · abrasion · binding · hole · stain · trimmed`
- `gap/@unit`: `char · chars · word · words · line · lines`
- `app/@type`: `substitution · addition · deletion · transposition · variant`
- `rdg/@type`: `authorial · external · ai-counterfactual`
- `@cert` (globale): `low · medium · high`

---

## 3. Convenzioni trasversali

- **`@hand`** = mano fisica che scrive (`#ink_1` autografa base, `#ink_2`, `#ink_3-dark`,
  `#pencil_1`, `#ink_4-external`).
- **`@resp`** = responsabilità della scelta: `#s-teresa` (interventi autoriali sul testimone),
  `#editor` (interventi dell'editore: `supplied`, `reg`, `corr`).
- **`@wit` / `@varSeq`**: nell'apparato, `lem` = ultima volontà autoriale (`#txt-c`, edizione
  critica); le fasi anteriori vanno in `rdg` ordinate con `@varSeq`. La **mano esterna**
  (`#txt-4`) e gli eventi IA (`@resp="#AI_controllata"`) **mai a `lem`**, solo a `rdg`.
- **`@cert`**: si dichiara ogni volta che la lettura o l'integrazione non è sicura.

---

## 4. Registro degli interventi

Compilare **una riga per intervento**. La colonna *Diplomatica → Esito* tiene sempre visibile
il prima/dopo; *Elemento TEI* rende esplicito il tipo di operazione.

| # | Luogo (c./§) | Fenomeno | Diplomatica → Esito | Elemento TEI | `@resp` · `@cert` | Note (attributi, mano) |
|---|---|---|---|---|---|---|
| 1 | 158r | grafia | à → a | choice › orig/reg | #editor | regolarizzazione accento |
| 2 | 158r | errore | sapere → sapete | choice › sic/corr | #editor · high | lapsus d'autore |
| 3 | 158r | sigla | I.M.I. → Iesus Maria Ioseph | choice › abbr/expan | #editor · high | invocazione iniziale |
| 4 | — | sostituzione | to → i | subst › del+add | #s-teresa · high | rend=strikethrough; place=inline; hand #ink_1 |
| 5 | — | variante di fase | to secondo → secondo | app › lem/rdg | #s-teresa | lem @wit=#txt-c; rdg @wit=#txt-b0; @varSeq; hand #ink_1 |
| 6 |  |  |  |  |  |  |
| 7 |  |  |  |  |  |  |
| 8 |  |  |  |  |  |  |


### Dal diplomatico all'interpretativo

Quando il segmento è stabile a livello diplomatico, si aggiunge lo **strato interpretativo**:
`@ana` sul `<seg>` (funzione, rischio, operazione, esposizione, fase, stato mistico, impatto)
e, dove serve, gli strati `<standOff>` (indice d'impatto, figure retoriche, aree semantiche,
catene). L'indice d'impatto **non si digita**: la `<fs>` registra le bande, lo script calcola `I`.

---

**Verifica**: buona formazione, RelaxNG (TEI All), guardie di CI (NFC, `@ana` referenziale,
co-occorrenza, `impactindex.sch`).
