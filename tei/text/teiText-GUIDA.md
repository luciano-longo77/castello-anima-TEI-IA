# Guida alla navigazione del *teiText*
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

## Indice
- [1. Cos'è questo file](#1-cosè-questo-file)
- [2. Struttura generale del teiText](#2-struttura-generale-del-teitext)
- [3. Mappa rapida della navigazione](#3-mappa-rapida-della-navigazione)
- [4. Come è fatto un segmento](#4-come-è-fatto-un-segmento)
- [5. Come cercare velocemente](#5-come-cercare-velocemente)
- [6. Esempio di percorso tipico](#6-esempio-di-percorso-tipico)
- [7. Riferimenti utili](#7-riferimenti-utili)
- [8. Contatti](#8-contatti)

---

## 1. Cos'è questo file

`castello-anima-teiText.xml` contiene il **testo del manoscritto** e i suoi quattro strati di annotazione. I **metadati** (mani, testimoni, tassonomia, criteri editoriali) non sono qui: stanno nel `teiHeader`, richiamato via `xi:include`. Per capire *cosa significa* un `@ana`, una mano o un testimone, si va nell'header (vedi [`../header/teiHeader-GUIDA.md`](../header/teiHeader-GUIDA.md)). Per capire *dov'è* e *com'è codificato* un passo, si usa questa guida.

Il testo è dato nella forma **interpretativa** costituita, a normalizzazione grafica **silenziosa e dichiarata** ([`../../docs/criteri-trascrizione.md`](../../docs/criteri-trascrizione.md)); l'unico apparato inline è quello **sostanziale** (`app`/`lem`/`rdg`). Riferimento tecnico completo del file: [`teiText-README.md`](teiText-README.md).

## 2. Struttura generale del teiText

```
<TEI>
 ├── <teiHeader> (via xi:include → ../header/…)
 └── <text><body>
       ├── <div type="book" n="1">          ← Libro I (proemio + I.1, I.2, I.4, I.5, I.6, I.11)
       │     └── <div type="chapter">        ← I-cap1 … → <p> → <seg xml:id="seg-b1-cNpP-label" ana="…">
       ├── <div type="book" n="2">          ← Libro II (segnaposto, da codificare)
       └── <div type="book" n="3">          ← Libro III (proemio + 19 capitoli)
             └── <div type="chapter" n="1">  ← III-cap1 → <p> → <seg xml:id="seg-b3-cNpP-label" ana="…">
 └── <standOff type="impact-index">        ← una <fs> per <seg>
 └── <standOff type="rhetorical-figures">  ← figure retoriche (<span>)
 └── <standOff type="semantic-focus">      ← aree tematiche (<span>)
 └── <standOff type="semantic-chains">     ← catene e relazioni (<link>)
```

Sono codificati il **Libro I** (proemio + I.1, I.2, I.4, I.5, I.6, I.11) e il **Libro III** (proemio + 19 capitoli); il **Libro II** è presente come `div` segnaposto (da codificare).

## 3. Mappa rapida della navigazione

### 🔹 Per trovare un capitolo
Cerca `xml:id="I-capN"` / `xml:id="III-capN"` (es. `I-cap2`, `III-cap8`) oppure `type="chapter" n="N"` dentro il `div` del libro.

### 🔹 Per leggere l'apparato sostanziale
- Variante **sostanziale** d'autrice (aggiunte/cassature/sostituzioni): `<app><lem wit="#txt-c">…</lem><rdg wit="#txt-b0" varSeq="1"><subst><del>…</del><add>…</add></subst></rdg></app>` — `lem` è l'**ultima volontà**; `<subst>`/`<del>`/`<add>` con `@hand`/`@place` stanno **dentro il `<rdg>`**. *(Le correzioni puramente grafiche non si marcano: normalizzazione silenziosa.)*
- Ritracciatura del tratto bruno T0→T1: `<retrace hand="#ink_1">`.
- Aggiunta prudenziale tardiva (inchiostro scuro T3): `<add hand="#ink_3-dark">`.
- Lacuna materiale / restituzione: `<gap reason="hole"/>` o `<supplied reason="hole" resp="#editor" cert="…">` (le parentesi quadre `[ ]`).

### 🔹 Per passare da un `<seg>` al suo indice d'impatto
Il `<seg xml:id="seg-b3-c8p2-roma">` è collegato alla `<fs xml:id="idx-seg-b3-c8p2-roma" corresp="#seg-b3-c8p2-roma">` nello `standOff type="impact-index"`: stesso identificatore, prefisso `idx-`.

### 🔹 Per vedere le figure retoriche o l'area di un segmento
Negli standOff `rhetorical-figures` e `semantic-focus` cerca lo `<span from="#seg-…">`.

### 🔹 Per trovare una citazione
Le citazioni sono `<cit><quote xml:lang="la">…</quote><bibl>…</bibl></cit>` dentro il `<seg>`. L'elenco completo con le carte è in [`../../docs/anagrafe-citazioni.md`](../../docs/anagrafe-citazioni.md).

## 4. Come è fatto un segmento

```xml
<seg xml:id="seg-b3-c1p8-desiderio"
     ana="#rischio-precisatio #operation-precisatio #risk-quietismo #exposition-critical
          #phase-mediana #phase-critical #mystic_state-quiete
          #relation-mistica-passiva-quiete #impact-high" hand="#ink_1">
  incomincia l'anima a perdire qualunque desiderio…
</seg>
```
*(esempio reale, `@ana` completo: gli 8 assi nell'ordine canonico func · operation · risk · exposition · phase · mystic_state · relation · impact, più il modificatore `#phase-critical` e `#relation-*`.)*
- `@xml:id` = ancora per apparato, indice d'impatto, standOff (formato `seg-b<L>-cNpP-label`, `b<L>` = numero del libro).
- `@ana` = l'interpretazione **a 8 assi** (`#phase-critical` è un modificatore, non un asse; `relation` è ripetibile). Le categorie vengono dal `classDecl`.
- `@hand` = la mano fisica.

Il calcolo dell'impatto **non** sta nel `seg` (che porta solo la classe `#impact-*`), ma nella `fs` gemella dello standOff.

## 5. Come cercare velocemente

| Cerchi… | Come |
|---|---|
| un capitolo | `xml:id="I-capN"` / `xml:id="III-capN"` |
| un segmento e il suo senso | `xml:id="seg-b<L>-cNpP-…"` → leggi il suo `@ana` |
| il calcolo d'impatto di un seg | `corresp="#seg-b<L>-cNpP-…"` nello `standOff impact-index` |
| le varianti sostanziali d'autrice | `<app>` (con `<subst>`/`<del>`/`<add>` dentro `<rdg>`) |
| le ritracciature | `<retrace>` (sempre `hand="#ink_1"`) |
| le restituzioni editoriali | `<supplied>` |
| una citazione | `<cit>` / `<bibl>` |
| cosa significa una categoria `@ana` | → nel `teiHeader` (`classDecl`) |

## 6. Esempio di percorso tipico

**«Voglio capire come è annotato il "perdere il desiderio" in III.1»**
1. Vai a `xml:id="III-cap1"`.
2. Cerca il `<seg>` col testo → `seg-b3-c1p8-desiderio`.
3. Leggi il suo `@ana` (funzione, rischio, operazione, fase, stato, impatto).
4. Per il calcolo dell'impatto, cerca `idx-seg-b3-c1p8-desiderio` nello `standOff impact-index`.
5. Per il senso delle categorie, apri il `teiHeader` (`classDecl`) o [`docs/data-dictionary.md`](../../docs/data-dictionary.md).

## 7. Riferimenti utili

- Riferimento tecnico del file: [`teiText-README.md`](teiText-README.md)
- Metodologia di codifica: [`docs/teiText-guida-codifica.md`](../../docs/teiText-guida-codifica.md)
- Criteri di trascrizione e normalizzazione: [`docs/criteri-trascrizione.md`](../../docs/criteri-trascrizione.md)
- Indice d'impatto: [`docs/indice-impatto.md`](../../docs/indice-impatto.md)
- Anagrafe delle citazioni: [`docs/anagrafe-citazioni.md`](../../docs/anagrafe-citazioni.md)
- Interventi editoriali (rendiconto): [`docs/interventi-editoriali.md`](../../docs/interventi-editoriali.md)
- Metadati e categorie: [`../header/teiHeader-GUIDA.md`](../header/teiHeader-GUIDA.md)

## 8. Contatti

**Luciano Longo** — <luciano.longo@dedalus.com> · [ORCID](https://orcid.org/0009-0005-7557-7546) · [GitHub](https://github.com/luciano-longo77)
