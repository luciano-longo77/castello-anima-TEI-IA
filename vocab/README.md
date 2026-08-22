# `vocab/` — vocabolario SKOS del *Castello dell'anima*
# Intertestualità sotto sorveglianza
## *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA) [![Vocabolario SKOS](https://img.shields.io/badge/SKOS-vocabolario%20online-1b7f5c)](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

Vocabolario controllato **SKOS** degli assi interpretativi dell'edizione, a supporto degli argomenti **FAIR** (interoperabile, riusabile, interrogabile via SPARQL). Non aggiunge contenuto interpretativo: dà alle categorie di `@ana` una forma standard, dereferenziabile.

> 🔗 **Esplora il vocabolario online** — navigabile, con ricerca e URI dereferenziabili (ci clicchi e si apre):
> **<https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/>**
> Una pagina per concetto, es. [`…/vocab/site/?c=rischio-precisatio`](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/?c=rischio-precisatio). Il Turtle grezzo (per le macchine): [`castello-anima-vocab.ttl`](castello-anima-vocab.ttl).

## Allineamento col vocabolario gemello

Gli stati mistici sono allineati in SKOS al repo gemello **[`castello-dell-anima-edizione`](https://github.com/luciano-longo77/castello-dell-anima-edizione)** (17 stati-mistici, base `https://w3id.org/castello-edizione-vocab/`). Il ponte è in **[`alignments-castello-anima-edizione.ttl`](alignments-castello-anima-edizione.ttl)**: 4 `skos:closeMatch` (quiete, otium, unione, illuminazione↔contemplazione-infusa), 2 `skos:narrowMatch` (purificazione ⊃ purga, notte), 4 `skos:relatedMatch` (le relazioni mistiche). Rigenerabile con [`../tools/gen_edizione_skos.py`](../tools/gen_edizione_skos.py).

## Patto fondamentale: **genera, non editare**

La **fonte normativa è il TEI** — `../tei/taxonomy/tassonomia-gh.xml`. Il file `castello-anima-vocab.ttl` è un **artefatto generato**, esattamente come `taxonomy-rng.rng` e `taxonomy-sch.sch`. **Non va editato a mano.** Per aggiornarlo:

```bash
python3 ../tools/gen_skos.py ../tei/taxonomy/tassonomia-gh.xml https://w3id.org/castello-anima-vocab/ alignments.tsv > castello-anima-vocab.ttl
```

La CI (`Vocab SKOS`) impone due invarianti a ogni push: **(1) sync** — il `.ttl` committato deve essere byte-identico alla rigenerazione dalla tassonomia; **(2) round-trip** — ogni token `@ana` e ogni banda del teiText deve avere un `skos:Concept` con quella `notation`.

## Modello

- **Un `skos:ConceptScheme` per asse** (10: gli 8 assi di `@ana` + le 2 bande di servizio `impact-band-N/A`).
- `category` → `skos:Concept`; annidamento → `skos:broader`; radice d'asse → `skos:topConceptOf`; `skos:inScheme` sempre.
- `skos:notation` = **token esatto come nel dato**: `#<id>` per gli assi di `@ana` (`func` compreso, senza prefisso d'asse), valore nudo (`critica`/`alta`/`media`/`bassa`) per le bande, che nel teiText compaiono come `<symbol value="…"/>` nelle `<fs>`.
- `skos:prefLabel@it` (id umanizzato) · `skos:definition@it` (dal `catDesc`).
- **Copertura**: 60 concetti (8/10 assi «pieni»). `#fig-*` (figure retoriche) e `#area-*` (aree semantiche) sono **esclusi**: dichiarati *inline* nel teiText, non in tassonomia — rinviati a consolidamento futuro.

## URI e persistenza

Base URI: `https://w3id.org/castello-anima-vocab/` (ogni concetto = base + `xml:id`). Persistenza via **w3id.org** (vedi `../w3id/`) con **GitHub Pages** come host del file. Gli URI «si accendono» quando la PR a w3id passa, senza rigenerare (la base è già nel `.ttl`).

## Allineamenti esterni (opzionali)

`alignments.tsv` (TSV a 3 colonne: `xml:id  closeMatch|exactMatch  URI`) è **vuoto di default**, con esempi Wikidata commentati. Aggiungendo righe, gli `skos:closeMatch`/`exactMatch` entrano alla prossima rigenerazione. È **scelta editoriale per-concetto**, non automatica.

## File

| File | Cosa |
|---|---|
| `castello-anima-vocab.ttl` | il vocabolario (GENERATO — non editare) |
| `site/index.html` | sito navigabile: una pagina per concetto (`?c=<id>`), legge il `.ttl` live |
| `alignments.tsv` | allineamenti esterni opzionali (fonte per la rigenerazione) |
| `../tools/gen_skos.py` | il generatore (solo `lxml`) |
| `../tools/4-vocabolario-skos.html` | viewer offline (dati incorporati, apribile da disco) |
| `../.github/workflows/scripts/skos_guard.py` | guardia round-trip (solo `lxml`) |
| `../.github/workflows/vocab-skos.yml` | CI: sync + round-trip |
