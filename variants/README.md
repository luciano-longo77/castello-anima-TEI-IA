# `variants/` — varianti controfattuali della pipeline IA

Questa cartella raccoglie le **varianti controfattuali** generate dalla pipeline IA
controllata (Fase 2) e **validate dall'editore** prima di entrare nel testo.

## Cosa contiene
Per ogni **locus × operazione** una variante generata sotto controllo:

| operazione | codice | cosa fa |
| :--- | :--- | :--- |
| rimozione citazione | **−CIT** | toglie la citazione/`<cit>` di legittimazione dal segmento |
| recupero cancellatura | **+TEXTsub** | ripristina una lezione cassata d'autrice (dal `<rdg wit="#txt-b0">`) |
| integrazione citazione | **+CIT** | restituisce una citazione *richiamata ma non esplicitata* (max 35 parole) |

## Governance (expert-in-the-loop)
Nessuna variante entra nel testo senza il **vaglio dell'editore** (protocollo
`docs/protocollo-IA-codifica.md`: l'IA *propone, non decide*; `@cert`/`@resp`; niente
lezioni inventate). Generazione deterministica: `temperature 0.2`, `top_p 0.95`, **seed registrato**.

## Tracciabilità
Ogni variante approvata è:
1. codificata nel teiText come **`<rdg ana="#workflow-*">`** nell'apparato del locus
   (`#workflow-rimozione` / `#workflow-recupero-cancellature` / `#workflow-aggiunta`);
2. accompagnata da **una riga** in [`../logs/runs.tsv`](../logs/runs.tsv) (schema in
   `teiHeader` → `xenoData/audit_trail`): `locus_id · operation · seed · prompt_hash ·
   output_hash · reviewer · esito · notes`.

Così la variante non è un file esterno scollegato: **entra nella tradizione critica** del
testo (un `<rdg>` in `<app>`, come una variante d'autore) ed è **rigenerabile** dal seed.
