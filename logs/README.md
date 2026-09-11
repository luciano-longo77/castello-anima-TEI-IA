# `logs/` — registro delle run della pipeline IA
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

## **Registro delle run della pipeline IA**
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

## Le misure del pilota (file derivati)
Oltre a `runs.tsv`, la cartella raccoglie le **misure** calcolate sui loci del **pilota**
(l'elenco dei loci è in [`../tools/pilot-loci.tsv`](../tools/pilot-loci.tsv), con la nota di metodo in
[`../tools/pilot-loci.md`](../tools/pilot-loci.md)). Ogni riga è chiavata per `locus_id`; le misure di
giudizio sono validate dall'editore (`rater=#editor`) e coerenti tra i file.

| file | cosa misura | schema (colonne) |
| :--- | :--- | :--- |
| [`delta-I.tsv`](delta-I.tsv) | **indice d'impatto** controfattuale: I del costituito (`lem`) e del controfattuale (`rdg`), con ΔI | `locus_id · operation · esito · N_lem · A_lem · F_lem · I_lem · N_rdg · A_rdg · F_rdg · I_rdg · dI · rater · note` |
| [`D1-D3.tsv`](D1-D3.tsv) | misure interpretative **D1** (chiarezza argomentativa) e **D3** (stabilità dottrinale), costituito → controfattuale | `locus_id · operation · esito · D1_lem · D1_rdg · dD1 · D3_lem · D3_rdg · dD3 · rater · note` |
| [`D2-pilot.tsv`](D2-pilot.tsv) | **coesione strutturale** (D2): effetto della rimozione del `<seg>` sulle catene semantiche — misura **deterministica** (nessun giudizio), **rigenerabile** | `locus_id · operation · chains_touched · chains_broken · chains_shortened · degree · neighbors_isolated · delta_connectivity` |
| [`T10-aggregato.tsv`](T10-aggregato.tsv) | **join** finale per locus: ΔI · D2 (broken/shortened/conn) · ΔD1 · ΔD3 — fonte unica per grafici e §4 | `locus_id · operation · esito · I_lem · I_rdg · dI · D2_broken · D2_shortened · D2_conn · dD1 · dD3` |
| [`checklist-filologica.tsv`](checklist-filologica.tsv) | **controllo filologico 4-assi** per variante (A1 stile · A2 dottrina · A3 antianacronismo · A4 integrità TEI) → esito: esplicita il vaglio editoriale del §3.4.2 (valori `OK` / `n/a` / `FALLITA`) | `locus_id · operation · A1_stile · A2_dottrina · A3_antianacronismo · A4_integrita_tei · esito · note` |

**Convenzioni.** Gli ancoraggi del modello: N {critica .90 / alta .75 / media .55 / bassa .30}; A {alta .85 / media .675 / bassa .40};
F {delimitazione 1 / attenuatio·precisatio·riequilibrio 2 / declaratio 3}; D1 {alta .90 / media .65 / bassa .40 / nulla .15}; D3 {alta .90 / media .65 / bassa .40 / critica .15};
`I = (4·F/3 + 2·N + A)/7`. Le celle **vuote** indicano misure **n/a** (esito `respinta` o `non-eseguibile`: nessun controfattuale valido da misurare).

**Rigenerare D2** (deterministico, dal teiText + elenco loci del pilota):

```bash
python3 tools/delta_cohesion.py tei/text/castello-anima-teiText.xml --pilot tools/pilot-loci.tsv --tsv > logs/D2-pilot.tsv
```
