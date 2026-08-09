# tools/
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0  
Strumenti a riga di comando per l'edizione TEI+IA del *Castello dell'anima*.

## `impact_index.py`

Calcolo deterministico e audit dell'**indice d'impatto** (`I = (4·F/3 + 2·N + A)/7`, pesi AHP 4:2:1).
Applica il modello **a bande‑ancora**: N ∈ {0.90, 0.75, 0.55, 0.30}, A ∈ {0.85, 0.675, 0.40};
F = rango dell'asse `operation` (delimitazione=1; attenuatio/precisatio/riequilibrio=2; declaratio=3).
Definizione e protocollo: `docs/indice-impatto.md`, `docs/Protocollo-indice-impatto.md`.

Richiede `python3` e `lxml` (`pip install lxml`).

### Modalità

- **audit** (default) — legge le `<fs>` già presenti, ri‑mappa N/A alle bande, ricalcola I con le
  ancore e lo confronta con l'`#impact-*` dichiarato in `@ana`; valida i puntatori
  (`@corresp`/`@target` → `xml:id` esistenti; ogni `<seg>` con `#impact-*` ha la sua `<fs>`).
- **authoring** (`--bands`) — da una tabella `id;banda_N;banda_A` stampa I, banda e valori calcolati.

### Uso

```bash
# audit dell'intero teiText
python3 tools/impact_index.py tei/text/castello-anima-teiText.xml

# audit + validazione schema (RelaxNG TEI All + Schematron dell'indice)
python3 tools/impact_index.py tei/text/castello-anima-teiText.xml \
        --rng schema/tei_all.rng --sch schema/impactindex.sch

# authoring da bande decise dall'annotatore
python3 tools/impact_index.py tei/text/castello-anima-teiText.xml --bands bande.csv
```

```csv
# bande.csv — id;banda_N;banda_A
seg-c8-desiderio;critica;alta
```

## Nota

La **scrittura** delle `<fs>` (con `N_band`/`A_band`) è affidata all'annotatore visuale
`annotatoreindice.html` («I mai a mano»); `impact_index.py` serve a **verificare** e a calcolare.
La guardia equivalente in CI è lo Schematron `schema/impactindex.sch` (workflow *Validate Text*).
