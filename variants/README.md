# `variants/` - varianti della pipeline IA
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

**Introduzione.** La cartella `variants/` ospita lo **strato sperimentale** dell'edizione: le *varianti controfattuali* con cui il progetto mette alla prova la **necessità strutturale** dei dispositivi retorico-dottrinali dell'autrice — citazioni di legittimazione, glosse attenuative, cancellature e guardie tardive. Nella logica del modello TEI-driven e AI-assisted, il testo costituito nel `teiText` risponde alla domanda «*che cosa* dice il testo e *come* è codificato»; le varianti rispondono alla domanda complementare «*che cosa accade se* quel dispositivo viene rimosso o alterato?». Sono il prodotto di **operazioni controfattuali sotto controllo editoriale** — in gran parte **deterministiche** (rimozione di una citazione, ripristino di una cancellatura d'autrice: si opera su testo *già presente* nella tradizione), con la sola **+CIT** realmente **generativa** (esplicitazione di una citazione allusa e attestata) — **proposte** dalla pipeline IA e **validate dall'editore**. Vivono in un file autonomo per non contaminare l'apparato **genetico d'autrice** con lo strato **sperimentale**.

**Legame con il repository e col progetto.** Le varianti non sono un esercizio isolato: acquistano senso solo in rapporto al testo che perturbano e alle misure che ne discendono. Il loro punto d'aggancio è il [`teiText`](../tei/text/castello-anima-teiText.xml) — ciascun controfattuale rinvia, per `@loc`, a un preciso `<seg>` del testo costituito, e lo fa in una sola direzione, dall'apparato al testo e mai viceversa, perché il testo di lettura non deve mai risentire dell'esperimento. È questo ancoraggio a rendere ogni variante *verificabile*: non un'affermazione generica sull'autrice, ma un intervento su un luogo identificabile. Dal luogo così isolato discendono le misure: togliere o alterare un dispositivo produce uno scarto quantificabile — d'impatto (ΔI), di coesione (D2), di chiarezza (D1), di stabilità dottrinale (D3) — che il progetto raccoglie in [`../logs/`](../logs/) e, per la parte deterministica, sa rigenerare con gli script di [`../tools/`](../tools/). Le regole che tengono onesto l'intero processo — che cosa l'IA può proporre e che cosa no, come si registra ogni run — sono fissate nel [protocollo](../docs/protocollo-IA-codifica.md); i risultati, infine, costituiscono la base empirica del **paper**. `variants/` e [`../logs/`](../logs/) sono così le due metà di uno stesso dittico — qui il *materiale* dell'esperimento, lì la sua *misura* — separate nei file ma inseparabili nel metodo.

## Cosa contiene
- [`castello-anima-variants.xml`](castello-anima-variants.xml) — apparato **standoff esterno**
  (un `<TEI>` autonomo con `<listApp type="counterfactual-ai">`): raccoglie tutte le
  varianti, ciascuna ancorata per `@loc` al `<seg>` del testo. Il teiText di produzione
  resta **intatto** (link unidirezionale: dall'apparato al testo, mai il contrario).
- [`backlog-textsub-additions.md`](backlog-textsub-additions.md) — **censimento** delle aggiunte marginali/interlineari (guardie T3) candidate a un +TEXTsub del sottotipo *rimozione-aggiunta*; backlog di estensione post-paper.
- questo `README.md`.

Per ogni **locus × operazione** una variante generata sotto controllo:

| operazione | codice | tipo | cosa fa |
| :--- | :--- | :--- | :--- |
| rimozione citazione | **-CIT** | sottrattiva | toglie la citazione/`<cit>` di legittimazione dal segmento |
| recupero cancellatura | **+TEXTsub** | sottrattiva | riporta il testo allo stato **pre-revisione**, in due sottotipi: **`ripristino-cassatura`** (recupera una lezione cassata d'autrice, dal `<rdg wit="#txt-b0">`) e **`rimozione-aggiunta`** (toglie una glossa/guardia **aggiunta** a margine o interlinea — strato tardivo T3 `#ink_3-dark` d'autrice o mano esterna `#ink_4-external`), per misurare da cosa la guardia proteggeva |
| integrazione citazione | **+CIT** | additiva | restituisce una citazione *richiamata ma non esplicitata* (max 35 parole) |

## Governance (expert-in-the-loop)
Nessuna variante è validata senza il **vaglio dell'editore** (protocollo
`docs/protocollo-IA-codifica.md`: l'IA *propone, non decide*; `@cert`/`@resp`; niente
lezioni inventate). Le operazioni **sottrattive** (-CIT, +TEXTsub) sono deterministiche per
costruzione (rimozione/ripristino di una porzione già presente nella tradizione); l'operazione
**additiva** (+CIT) è generativa: il motore adottato **non espone un parametro `seed`**, quindi il
`seed` registrato è **nominale** e la riproducibilità poggia su **modello+versione, prompt e
`output_hash`** (generazione a `temperature 0.2`, `top_p 0.95`). La distinzione è formalizzata nel protocollo.

## Tracciabilità
Ogni variante approvata è:
1. codificata in `castello-anima-variants.xml` come **`<app loc="seg-…" type="workflow-*">`**
   (`workflow-rimozione` / `workflow-recupero-cancellature` / `workflow-aggiunta`), con
   `@loc` *location-referenced* (l'`xml:id` del `<seg>` **nudo, senza `#`**: non è un puntatore),
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
`<seg>` per `@loc` — ed è **rigenerabile** dal seed (per le sottrattive) o **certificata** dall'`output_hash` (per il +CIT generativo, che non ha un seed effettivo).
