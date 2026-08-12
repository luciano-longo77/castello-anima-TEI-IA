# CI del *Castello dell'anima* — workflow e guardie

Questa cartella contiene l'**integrazione continua** dell'edizione: a ogni `push`/`pull_request`
GitHub Actions verifica che testo, tassonomia e header restino **ben formati, validi e coerenti**.
La validazione è **a più livelli**: prima la buona formazione e lo schema (RelaxNG), poi le regole
semantiche (Schematron), infine le **guardie** Python che impongono le invarianti del modello.

[![Validate Text](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/validate-text.yml/badge.svg?branch=main)](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/validate-text.yml)
[![Validate Taxonomy](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/main.yml)
[![Genera data-dictionary](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/gen-data-dictionary.yml/badge.svg?branch=main)](https://github.com/luciano-longo77/castello-anima-TEI-IA/actions/workflows/gen-data-dictionary.yml)

## I tre workflow

| File | Nome | Quando parte | Che cosa garantisce |
|---|---|---|---|
| `validate-text.yml` | **Validate Text** | modifiche a `tei/text/**`, `tei/taxonomy/`, `tei/header/`, `schema/`, `.github/workflows/**` | il teiText è valido e coerente su tutti i piani |
| `main.yml` | **Validate Taxonomy** | modifiche a `tei/taxonomy/**`, `tei/header/**` | la tassonomia è valida e la sua copia nell'header non diverge |
| `gen-data-dictionary.yml` | **Genera data-dictionary** | modifiche a `tei/taxonomy/tassonomia-gh.xml`, al generatore o al workflow; oppure a mano | rigenera e ricommitta `docs/data-dictionary.md` dalla tassonomia |

Tutti e tre accettano l'avvio manuale dalla scheda **Actions** (`workflow_dispatch`).

### `validate-text.yml` — Validate Text
Sul file `tei/text/castello-anima-teiText.xml`, in sequenza:
1. **NFC** — tutti i file XML in forma Unicode NFC.
2. **Ben formato + XInclude** (`xmllint --xinclude`) e composizione del documento risolto.
3. **RelaxNG** (`jing schema/tei_all.rng`) sul documento risolto.
4. **Guardia E2** — ogni token `@ana` risolve a una categoria della tassonomia o a un id locale.
5. **Guardia co-occorrenza** — 1 `#impact-*`, 1 `#operation-*`, 1 fase base per `seg`; `#phase-critical` con base.
6. **Guardia cit/glossa** — `cit` dentro `seg` con `quote`; `note type="glossa"` vuota in `add` (asse operation); nessuna `fs` verso cit/note.
7. **Guardia commenti** — grammatica dei commenti `<!-- … -->` sui `seg` (clausola N/A/F→I, ancore col decimale, `commento-I == fs-I`, keyword ammesse).
8. **Schematron** (`schema/impactindex.sch`) — R1 vocabolario bande, R2 ancore + formula, R3 classe ↔ I.

### `main.yml` — Validate Taxonomy
Due job:
- **validate** — su `tei/taxonomy/tassonomia-gh.xml`: ben formato, **RelaxNG** (`tei/taxonomy/schema/taxonomy-rng.rng`), **Schematron** (`taxonomy-sch.sch`), presenza delle **8 tassonomie core**, `@ana` referenziale negli esempi (`tei/taxonomy/esempio/*.xml`), validazione strutturale degli esempi contro `tei_all.rng` e guardia di co-occorrenza sugli esempi.
- **e1-guard** — **guardia E1**: le 8 tassonomie interpretative copiate nel `classDecl` dell'header sono **identiche** alla fonte `tassonomia-gh.xml` (categorie e `catDesc`). Impedisce che header e fonte divergano.

### `gen-data-dictionary.yml` — Genera data-dictionary
Esegue `tools/gen_data_dictionary.py` e, se `docs/data-dictionary.md` è cambiato, lo **committa da solo** (con `git pull --rebase` prima del push per evitare collisioni). Richiede *Read and write permissions* per le Actions.

## Le guardie (`scripts/`)

Script Python indipendenti, richiamati dai workflow ma eseguibili anche **in locale** (`python3 scripts/<guardia>.py <file>`), utili prima di committare.

| Script | Verifica |
|---|---|
| `e2_guard.py` | integrità referenziale di `@ana` (ogni token → id reale in tassonomia o nel documento) |
| `cooccurrence_guard.py` | invarianti di co-occorrenza degli assi (1 impact / 1 operation / 1 fase base; `phase-critical` con base) |
| `cit_glossa_guard.py` | modello intertestuale: `cit` nel `seg` con `quote`; `note glossa` vuota in `add` con `@ana` operation; indice solo sul `seg` |
| `commenti_guard.py` | grammatica dei commenti dei `seg` (clausola N/A/F→I, ancore col decimale, `commento-I == fs-I`, keyword `Genetico:`/`Norm:`) |

## Dove stanno gli schemi

- **Testo:** `schema/tei_all.rng` (RelaxNG TEI All, vendorizzato) · `schema/impactindex.sch` (Schematron dell'indice).
- **Tassonomia:** `tei/taxonomy/schema/taxonomy-rng.rng` · `tei/taxonomy/schema/taxonomy-sch.sch`.

## Eseguire la CI in locale (prima di committare)

```bash
pip install lxml            # le guardie usano lxml
sudo apt-get install -y libxml2-utils jing   # xmllint + jing (per RelaxNG)

# Validate Text (in sequenza)
python3 - <<'PY'
import unicodedata; s=open("tei/text/castello-anima-teiText.xml",encoding="utf-8").read()
assert s==unicodedata.normalize("NFC",s), "NON NFC"
PY
xmllint --noout --xinclude tei/text/castello-anima-teiText.xml
xmllint --nofixup-base-uris --xinclude tei/text/castello-anima-teiText.xml > resolved.xml
jing schema/tei_all.rng resolved.xml
python3 .github/workflows/scripts/e2_guard.py         tei/text/castello-anima-teiText.xml tei/taxonomy/tassonomia-gh.xml
python3 .github/workflows/scripts/cooccurrence_guard.py tei/text/castello-anima-teiText.xml
python3 .github/workflows/scripts/cit_glossa_guard.py   tei/text/castello-anima-teiText.xml
python3 .github/workflows/scripts/commenti_guard.py     tei/text/castello-anima-teiText.xml
```

## Regola pratica: dove va cosa

- **Le guardie (`.py`)** stanno **qui**, in `.github/workflows/scripts/`. La documentazione di metodo
  (grammatiche, protocolli) sta in `docs/` o nella *skill*, **non** qui.
- Aggiungere una guardia = committare lo script in `scripts/` **e** aggiungere lo step nel workflow
  che la richiama (altrimenti non gira).
