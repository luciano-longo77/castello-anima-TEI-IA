# `variants/` — varianti controfattuali della pipeline IA

Questa cartella raccoglie le **varianti controfattuali** generate dalla pipeline IA
controllata (Fase 2) e **validate dall'editore**. Sono tenute in un **file separato** —
non nel testo di lettura — per non mescolare l'apparato **genetico d'autrice** con lo
strato **sperimentale IA**.

## Cosa contiene
- [`castello-anima-variants.xml`](castello-anima-variants.xml) — apparato **standoff esterno**
  (un `<TEI>` autonomo con `<listApp type="counterfactual-ai">`): raccoglie tutte le
  varianti, ciascuna ancorata per `@loc` al `<seg>` del testo. Il teiText di produzione
  resta **intatto** (link unidirezionale: dall'apparato al testo, mai il contrario).
- questo `README.md`.

Per ogni **locus × operazione** una variante generata sotto controllo:

| operazione | codice | tipo | cosa fa |
| :--- | :--- | :--- | :--- |
| rimozione citazione | **−CIT** | sottrattiva | toglie la citazione/`<cit>` di legittimazione dal segmento |
| recupero cancellatura | **+TEXTsub** | sottrattiva | ripristina una lezione cassata d'autrice (dal `<rdg wit="#txt-b0">`) |
| integrazione citazione | **+CIT** | additiva | restituisce una citazione *richiamata ma non esplicitata* (max 35 parole) |

## Governance (expert-in-the-loop)
Nessuna variante è validata senza il **vaglio dell'editore** (protocollo
`docs/protocollo-IA-codifica.md`: l'IA *propone, non decide*; `@cert`/`@resp`; niente
lezioni inventate). Le operazioni **sottrattive** (−CIT, +TEXTsub) sono deterministiche per
costruzione (rimozione/ripristino di una porzione già presente nella tradizione); l'operazione
**additiva** (+CIT) è generativa e va prodotta a parametri fissati (`temperature 0.2`,
`top_p 0.95`, **seed registrato**). La distinzione è formalizzata nel protocollo.

## Tracciabilità
Ogni variante approvata è:
1. codificata in `castello-anima-variants.xml` come **`<app loc="…seg…" type="workflow-*">`**
   (`workflow-rimozione` / `workflow-recupero-cancellature` / `workflow-aggiunta`), con
   `<lem wit="#txt-c">` (lezione costituita) e `<rdg resp="#AI_controllata" cert="…">` (il
   controfattuale). L'operazione sta su **`@type`** (token), non su `@ana`: la tassonomia
   `workflow` risiede nel `teiHeader` — riservata al `revisionDesc` — e la guardia **E2**
   risolve gli `@ana` del testo solo contro `tassonomia-gh.xml`; tenere le varianti in un file
   esterno lascia inoltre il teiText fuori dal loro raggio, senza rischi per le guardie;
2. accompagnata da **una riga** in [`../logs/runs.tsv`](../logs/runs.tsv) (schema in
   `teiHeader` → `xenoData/audit_trail`): `locus_id · operation · seed · prompt_hash ·
   output_hash · reviewer · esito · notes`.

Così la variante non è un file scollegato: **entra nella tradizione critica** del testo come
apparato (un `<rdg>` in `<app>`, come una variante d'autore), ma **standoff** — ancorata al
`<seg>` per `@loc` — ed è **rigenerabile** dal seed.
