# teiText
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

## Indice
- [1. Definizione e perimetro del file](#1-definizione-e-perimetro-del-file)
- [2. Architettura del testo](#2-architettura-del-testo)
- [3. I piani della codifica](#3-i-piani-della-codifica)
- [4. I quattro strati standOff](#4-i-quattro-strati-standoff)
- [5. Convenzioni degli `xml:id`](#5-convenzioni-degli-xmlid)
- [6. Validazione e qualità del dato](#6-validazione-e-qualità-del-dato)
- [7. Citazione](#7-citazione)
- [8. Contatti](#8-contatti)

---

## 1. Definizione e perimetro del file

`castello-anima-teiText.xml` è il **testo del manoscritto** codificato in TEI P5: il corpo dell'opera (`<text>`) e i quattro strati di annotazione `<standOff>` fratelli di `<text>`. Il file **non** contiene i metadati: il `teiHeader` è tenuto separato in `../header/castello-anima-teiHeader.xml` e richiamato via **`xi:include`**. I due file sono un'unica edizione e vanno tenuti accoppiati.

Il testo codificato è un **campione ragionato** su due Libri:
- **Libro III** (anime perfette): **19 capitoli** — III.1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 14, 16, 19, 24, 32, 34, 38, 39, 40 — più il proemio;
- **Libro I** (anime principianti): **proemio** più i capitoli **I.1, I.2, I.4, I.5, I.6, I.11**.

Il solo **Libro II** compare come `div` segnaposto (campione pianificato — II.1, II.2, II.8, II.9, II.10 — non ancora trascritto). Il criterio di selezione è dichiarato nel `<samplingDecl>` dell'header e documentato in [`docs/base-dati_campionamento.md`](../../docs/base-dati_campionamento.md).

## 2. Architettura del testo

- **Gerarchia**: `<div type="book">` › `<div type="chapter">`; le rubriche sono `<head>`, il cappello di capitolo è `<argument>` (solo a livello di libro).
- **Unità di annotazione**: **`<seg>`** (sub-paragrafo) — l'unica che porta l'`@ana` interpretativo. Il paragrafo è `<p n="…">`.
- **Materialità**: `<pb n="158r"/>` (foliazione reale), `<fw>` (segnature/richiami), `<lb break="no"/>` (solo parola spezzata).
- **Cifre del campione**: **697** `<seg>` · **599** `<p>` · **143** `<pb>` · **1406** `<term>` · **1313** `<rs>` · **27** `<cit>`/`<bibl>`.

## 3. I piani della codifica

Il testo è dato nella forma **interpretativa** costituita, a **normalizzazione grafica silenziosa e dichiarata** (cfr. [`docs/criteri-trascrizione.md`](../../docs/criteri-trascrizione.md) e l'`editorialDecl` dell'header, dalla *Nota al testo, §2*). Nel testo di lettura **non** compaiono elementi diplomatici inline: l'unico apparato marcato è quello **sostanziale**.

| piano | elementi | note |
|---|---|---|
| **Normalizzazione grafica** | *(nessun elemento inline)* | applicata **silenziosamente** e dichiarata una volta per tutte; nel testo di lettura non compaiono `choice`/`orig`/`reg`, `sic`/`corr`, `abbr`/`expan` (**0 `choice`**) |
| **Apparato sostanziale** | `<app>`/`<lem>`/`<rdg>` | **148 `app`**; `lem` = ultima volontà (`@wit="#txt-c"`), `rdg` = stato genetico (`@wit="#txt-b0"`). Le varianti d'autrice — aggiunte, cassature, sostituzioni — vivono **solo dentro l'apparato**: 96 `del` · 69 `add` · 16 `subst`, tutti entro `app`/`rdg` |
| **Ritracciature** | `<retrace>` | **51 `retrace` tutti `#ink_1`** (ritracciatura bruna T0→T1); lo strato scuro tardivo prudenziale è `<add hand="#ink_3-dark">` (T3) |
| **Integrazioni editoriali** | `<gap>` `<unclear>` `<supplied>` | 65 `gap` · 6 `unclear` · **150 `supplied`** (`@reason="hole"`, `@resp="#editor"`, `@cert`) — le parentesi quadre `[ ]` della Nota al testo |
| **Interpretativo** | `@ana` sul `<seg>` (8 assi) | governato dal `classDecl`; **1 valore per asse**, con eccezioni: `func` 1..n · `mystic_state` 0..1 · `relation` 0..n; `#phase-critical` è un modificatore della fase, non un asse. Cardinalità imposte da `cooccurrence_guard.py` |
| **Intertesto** | `<cit>`/`<quote xml:lang="la">`/`<bibl>` | **27** citazioni latine, registrate anche in [`docs/anagrafe-citazioni.md`](../../docs/anagrafe-citazioni.md) |

## 4. I quattro strati standOff

Fratelli di `<text>`, ancorati al testo per `@corresp`/`@from`/`@target`:

1. **`impact-index`** — una `<fs>` per `<seg>` (**697**) con i 7 campi dell'indice d'impatto (N_band, A_band, N, A, F, Fnorm, I).
2. **`rhetorical-figures`** — `<span>` che classificano le figure (`#fig-metafora`, `#fig-similitudine`…) su un `interpGrp` locale.
3. **`semantic-focus`** — un'area (`#area-*`) per ogni `<seg>` (**697**).
4. **`semantic-chains`** — `<link>`/`<linkGrp>` per le catene tematiche e le relazioni (rischio↔operazione, intertesto).

Gli `interpGrp` dei vocabolari `fig-*`/`area-*` sono dichiarati **una volta** nel file del testo.

## 5. Convenzioni degli `xml:id`

- **Libro / capitolo**: `Libro-I` · `I-cap1`, `I-cap2`, … ; `Libro-III` · `III-cap1`, `III-cap2`, …
- **Segmento**: **`seg-b<L>-cNpP-label`** (`b<L>` = numero del libro, es. `b1`, `b3`; es. `seg-b1-c2p6-nemico-demonio`, `seg-b3-c8p2-roma`); proemio `seg-b<L>-pro-pP-label`; titolo `seg-b<L>-tit-…`.
- **Feature structure d'impatto**: `idx-<segid>` (es. `idx-seg-b3-c8p2-roma`).
- **Vocabolari standOff**: `fig-*`, `area-*`.

Le convenzioni sono **imposte in CI** dalla guardia `regole_fissate_guard.py`.

## 6. Validazione e qualità del dato

Il file è **NFC**, ben formato, e valido contro:
- **RelaxNG** `../../schema/tei_all.rng` (TEI All vendorizzato) sul documento risolto (`xi:include`);
- **Schematron** `../../schema/impactindex.sch` (indice d'impatto);
- le **8 guardie** Python in `../../.github/workflows/scripts/` (E2 `@ana`→tassonomia, co-occorrenza, cit/glossa, citazioni, commenti, interventi, regole-fissate, whitespace-anticorruzione).

La CI (`Validate Text`) esegue tutta la catena a ogni push/PR. La **metodologia di codifica** è in [`docs/teiText-guida-codifica.md`](../../docs/teiText-guida-codifica.md); la **navigazione** del file in [`teiText-GUIDA.md`](teiText-GUIDA.md).

## 7. Citazione

Vedi `CITATION.cff` nella radice del repository.

## 8. Contatti

**Luciano Longo** — <luciano.longo@dedalus.com> · [ORCID](https://orcid.org/0009-0005-7557-7546) · [GitHub](https://github.com/luciano-longo77)
