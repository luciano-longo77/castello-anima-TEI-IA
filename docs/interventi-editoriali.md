# Interventi editoriali: rendiconto verificabile
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

**Fonte**
*Generato da `tei/text/castello-anima-teiText.xml`. Fotografa ogni intervento editoriale distinguendo il piano della **normalizzazione** (scelte in `choice`) da quello **genetico** (lavoro dell'autrice sul foglio). L'attribuzione è a due livelli: `reg`/`expan` globale (`editorialDecl`), `corr`/`supplied` per-istanza (`@resp` + `@cert`).*

---

## 1. Piano della normalizzazione (`choice`)
| coppia | n | con `@resp` | con `@cert` | attribuzione attesa |
|---|---:|---:|---:|---|
| `orig/reg` | 130 | 0 | 0 | globale (`editorialDecl`): `@resp` = 0 |
| `sic/corr` | 20 | 20 | 20 | per-istanza: `@resp` e `@cert` = n |
| `abbr/expan` | 16 | 0 | 5 | globale; `@cert` solo dove pertinente |


## 2. Piano genetico (lavoro sul foglio)

| elemento | n | con `@hand` | con `@cert` |
|---|---:|---:|---:|
| `add` | 28 | 28 | 6 |
| `del` | 55 | 55 | 0 |
| `subst` | 15 | 0 | 0 |
| `retrace` | 24 | 24 | 24 |
| `gap` | 20 | 0 | 0 |
| `supplied` | 21 | 0 | 21 |

### 2.1 Dettaglio dei valori

| attributo | valori (conteggio) |
|---|---|
| `del/@type` | `correction` (20) · `deletion` (35) |
| `del/@rend` | `strikethrough` (35) |
| `del/@place` | `inline` (47) |
| `add/@type` | `substitution` (18) |
| `add/@place` | `inline` (11) · `margin` (1) · `margin-left` (2) · `margin-right` (1) · `supralinear` (5) |
| `gap/@reason` | `hole` (8) · `illegible` (12) |
| `gap/@unit` | `char` (15) · `chars` (2) · `word` (3) |
| `supplied/@reason` | `hole` (21) |
| `retrace/@hand` | `#ink_3-dark` (24) |
| `retrace/@cert` | `low` (1) · `medium` (23) |

## 3. Controlli di coerenza

**Nessun rilievo.** I due piani sono coerenti con la policy dichiarata: `reg`/`expan` senza `@resp` (attribuzione globale), `corr` pienamente attribuito, ogni `supplied` con `@resp`+`@cert`, ogni `subst` = `add`+`del`.

## 4. Appendice · dettaglio per-istanza

*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, `seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*

| # | piano | elemento | carta | seg | tipo/valore | mano | cert | testo |
|---:|---|---|---|---|---|---|---|---|
| 1 | norm | `abbr/expan` | 158r | - | I.M.I. → Iesus Maria Ioseph | | high | |
| 2 | norm | `sic/corr` | 158r | seg-158r-obedienza | sapere → sapete | | high | |
| 3 | norm | `sic/corr` | 158r | seg-158r-autodemotio | l'opera nostra → l'opere nostre | | high | |
| 4 | norm | `sic/corr` | 158r | seg-158r-invocatio | domandano → domandavo | | medium | |
| 5 | norm | `orig/reg` | 158r | seg-158r-invocatio | à → a | |  | |
| 6 | norm | `sic/corr` | 158r | seg-158r-invocatio | noi → voi | | medium | |
| 7 | norm | `sic/corr` | 158r | seg-158r-invocatio | nostro → vostro | | medium | |
| 8 | norm | `orig/reg` | 158r | seg-158r-invocatio | agiuuto → agiuto | |  | |
| 9 | norm | `orig/reg` | 158r | seg-158r-invocatio | à → a | |  | |
| 10 | norm | `orig/reg` | 158r | seg-158r-incapacitas | poiche → poiché | |  | |
| 11 | norm | `sic/corr` | 158r | seg-158r-incapacitas | trattano → trattavo | | high | |
| 12 | norm | `sic/corr` | 158r | seg-158r-declaratio | contra di chi → contradichi | | medium | |
| … | … | … | … | … | … | … | … | *(troncato: nel file completo 329 righe)* |
