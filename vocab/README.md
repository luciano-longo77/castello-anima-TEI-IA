# `vocab/` — vocabolario SKOS del *Castello dell'anima*

Vocabolario controllato **SKOS** degli assi interpretativi dell'edizione, a supporto degli argomenti **FAIR** (interoperabile, riusabile, interrogabile via SPARQL). Non aggiunge contenuto interpretativo: dà alle categorie di `@ana` una forma standard, dereferenziabile.

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
| `alignments.tsv` | allineamenti esterni opzionali (fonte per la rigenerazione) |
| `../tools/gen_skos.py` | il generatore (solo `lxml`) |
| `../.github/workflows/scripts/skos_guard.py` | guardia round-trip (solo `lxml`) |
| `../.github/workflows/vocab-skos.yml` | CI: sync + round-trip |
