# `logs/` — registro delle run della pipeline IA

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
| `esito` | `approvata` · `respinta` · `da-rivedere` |
| `notes` | note filologiche/di validazione |

## Determinismo e replicabilità
Generazione a `temperature 0.2`, `top_p 0.95`. Fissando `seed` + `prompt_hash`, la run è
**riproducibile** e verificabile da terzi; `output_hash` certifica quale testo è stato
effettivamente validato ed eventualmente codificato come `<rdg type="workflow-*">` nell'apparato
standoff **esterno** [`../variants/castello-anima-variants.xml`](../variants/castello-anima-variants.xml)
(ancorato per `@loc` al `<seg>`), senza toccare il teiText di produzione.
