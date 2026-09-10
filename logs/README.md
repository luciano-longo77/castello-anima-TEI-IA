# `logs/` — registro delle run della pipeline IA
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0
---

Registro **verificabile** di ogni run della pipeline controfattuale (Fase 2): **una riga
per run** in [`runs.tsv`](runs.tsv). È ciò che trasforma un'affermazione («l'ambiguità
cresce del 20%») in un **artefatto rigenerabile** («ecco la run, con questo seed»).

## Schema della riga (TSV)
Campi obbligatori — coincidono con `teiHeader` → `xenoData` → `audit_trail/required_fields`:

| campo | significato |
| :--- | :--- |
| `locus_id` | `xml:id` del `<seg>` perturbato |
| `operation` | `-CIT` · `+TEXTsub` · `+CIT` |
| `seed` | seed deterministico della generazione |
| `prompt_hash` | hash del prompt usato |
| `output_hash` | hash dell'output generato |
| `reviewer` | chi ha validato (editore) |
| `esito` | `approvata` · `respinta` · `da-rivedere` · `non-eseguibile` |
| `notes` | note filologiche/di validazione |

## Determinismo e replicabilità
Generazione a `temperature 0.2`, `top_p 0.95`. Fissando `seed` + `prompt_hash`, la run è
**riproducibile** e verificabile da terzi; `output_hash` certifica quale testo è stato
effettivamente validato ed eventualmente codificato come `<rdg type="workflow-*">` nell'apparato
standoff **esterno** [`../variants/castello-anima-variants.xml`](../variants/castello-anima-variants.xml)
(ancorato per `@loc` al `<seg>`), senza toccare il teiText di produzione.
