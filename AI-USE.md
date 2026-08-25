# Uso dell'IA · Use of AI

*Lingua · Language: [Italiano](#italiano) · [English](#english)*

---

<a id="italiano"></a>
## 🇮🇹 Italiano

### Scopo di questo documento
Nell'ottica della **trasparenza** e dell'integrità della ricerca, questo documento dichiara in modo chiaro se e come strumenti di **Intelligenza Artificiale (IA)** sono stati impiegati nella realizzazione di questo repository. La responsabilità scientifica e autoriale dei contenuti resta interamente **umana**.

### Strumenti impiegati
Non tutti gli strumenti elencati sono usati in ogni fase; la sezione **«Ambiti d'uso»** specifica l'impiego effettivo.

- **Claude / Claude Code (Anthropic)** — assistente conversazionale e di programmazione.
- **Google Gemini** e **Gemini Notebook** — assistente conversazionale e analisi/sintesi di documenti.
- **Elicit** (elicit.com) — assistente di ricerca per il reperimento e la sintesi della letteratura scientifica.
- **Litmaps** (litmaps.com) — mappatura e visualizzazione delle reti di citazioni della letteratura scientifica.

### Ambiti d'uso
L'IA è stata usata come **strumento di supporto** per:
- **Codifica TEI** — compiti tecnici e ripetitivi (controlli di validità XML/TEI, coerenza della marcatura, bozze di script di verifica) e **test di protocolli di trascrizione automatizzata**;
- **Esperimenti controfattuali controllati** (Fase 2) — generazione di *varianti sperimentali* di singoli luoghi (rimozione di una citazione `-CIT`, ripristino di una cassatura d'autrice `+TEXTsub`, integrazione di una citazione richiamata `+CIT`) al **solo scopo di misurarne l'effetto** su chiarezza, coesione e stabilità dottrinale. Ogni variante è **validata dall'editore** (l'IA *propone, non decide*; nessuna fonte inventata — la citazione deve esistere nell'anagrafe), è **tracciata** (seed, hash, esito in `logs/runs.tsv`) e **non entra mai nel testo costituito**: resta in un apparato standoff *esterno* (`variants/`), separato dall'edizione. Metodo in [`docs/protocollo-IA-codifica.md`](docs/protocollo-IA-codifica.md);
- **Ricognizione bibliografica** — reperimento, mappatura e sintesi preliminare della letteratura (Elicit, Litmaps), sempre con **verifica diretta** di ogni fonte e citazione da parte dell'autore.

### Supervisione umana e responsabilità
- Ogni output dell'IA è stato **riletto, verificato e validato** dall'autore.
- Le **decisioni scientifiche** — interpretazione, metodo, costituzione del testo, scelte ecdotiche e filologiche — sono **dell'autore**; l'IA non le determina.
- L'autore è l'**unico responsabile** dei contenuti pubblicati e ne mantiene la piena paternità intellettuale.

### Ciò che l'IA *non* fa
- Non stabilisce il testo critico né le lezioni, e non sostituisce il giudizio filologico.
- Non genera né "inventa" fonti, riferimenti bibliografici o dati: ogni citazione è verificata dall'autore.
- Non figura come autore o co-autore dei contributi scientifici né come *contributor* del codice.

### Dati e riservatezza
- I materiali testuali elaborati sono **di pubblico dominio o di proprietà dell'autore**, e il loro uso non viola diritti di terzi.
- I dati condivisi con gli strumenti di IA sono le **trascrizioni** dei testi.
- Le **immagini** dei testimoni sono state condivise **unicamente per testare il protocollo di trascrizione automatizzata** e **non sono conservate** da alcuno degli strumenti di IA impiegati.
- Non sono stati immessi dati personali o riservati oltre a quanto strettamente necessario e lecito.

### Tracciabilità e riproducibilità
- Il contributo dell'IA è **assistivo e supervisionato**: è dichiarato in questo documento ed è ricostruibile dalla **cronologia dei commit** del repository, di cui l'autore è l'unico autore.
- L'autore **conserva tutti i *prompt*** e i flussi di *prompt-engineering* impiegati, organizzati come ***skill* riutilizzabili** degli strumenti di IA e sottoposti a **revisione mensile**.
- Per la **codifica TEI assistita da AI**, il metodo operativo — ruolo dell'AI, prompt, cardinalità, guardie e verifica — è fissato nel [**protocollo operativo per la codifica assistita da AI**](docs/protocollo-IA-codifica.md), versionato col repository e verificabile in CI: attua in modo concreto i principi di trasparenza e sorveglianza umana dichiarati qui.

### Allineamento ai principi di *Trustworthy AI*
Questo uso è coerente con le *Ethics Guidelines for Trustworthy AI* (High-Level Expert Group on AI, Commissione Europea, 2019), in particolare **trasparenza**, **azione e sorveglianza umana** e **responsabilità (*accountability*)**.

---

<a id="english"></a>
## 🇬🇧 English

### Purpose of this document
In the spirit of **transparency** and research integrity, this document clearly states whether and how **Artificial Intelligence (AI)** tools were used in producing this repository. Scholarly and authorial responsibility for the content remains entirely **human**.

### Tools used
Not all listed tools are used at every stage; the **"Scope of use"** section specifies actual use.

- **Claude / Claude Code (Anthropic)** — conversational and coding assistant.
- **Google Gemini** and **Gemini Notebook** — conversational assistant and document analysis/synthesis.
- **Elicit** (elicit.com) — research assistant for finding and summarising scholarly literature.
- **Litmaps** (litmaps.com) — mapping and visualisation of scholarly citation networks.

### Scope of use
AI was used as a **supporting tool** for:
- **TEI encoding** — technical and repetitive tasks (XML/TEI validity checks, markup consistency, drafts of verification scripts) and **testing of automated transcription protocols**;
- **Controlled counterfactual experiments** (Phase 2) — generation of *experimental variants* of individual loci (citation removal `-CIT`, authorial-deletion recovery `+TEXTsub`, integration of an alluded citation `+CIT`) **solely to measure their effect** on clarity, cohesion and doctrinal stability. Every variant is **editor-validated** (the AI *proposes, does not decide*; no invented sources — the citation must exist in the authority list), **traced** (seed, hash, outcome in `logs/runs.tsv`) and **never enters the constituted text**: it stays in an *external* standoff apparatus (`variants/`), separate from the edition. Method in [`docs/protocollo-IA-codifica.md`](docs/protocollo-IA-codifica.md);
- **Bibliographic reconnaissance** — finding, mapping and preliminary summarising of the literature (Elicit, Litmaps), always with the author's **direct verification** of every source and citation.

### Human oversight and responsibility
- Every AI output was **reviewed, checked and validated** by the author.
- **Scholarly decisions** — interpretation, method, constitution of the text, ecdotic and philological choices — are **the author's**; they are not determined by AI.
- The author is **solely responsible** for the published content and retains full intellectual authorship.

### What AI does *not* do
- It does not establish the critical text or its readings, and does not replace philological judgement.
- It does not generate or "invent" sources, bibliographic references or data: every citation is verified by the author.
- It is not listed as an author or co-author of scholarly work, nor as a code *contributor*.

### Data and confidentiality
- The textual materials processed are **in the public domain or the author's property**, and their use does not infringe third-party rights.
- The data shared with the AI tools are the **transcriptions** of the texts.
- **Images** of the witnesses were shared **solely to test the automated transcription protocol** and are **not retained** by any of the AI tools used.
- No personal or confidential data were entered beyond what is strictly necessary and lawful.

### Traceability and reproducibility
- The AI contribution is **assistive and supervised**: it is disclosed in this document and reconstructable from the repository's **commit history**, of which the author is the sole author.
- The author **keeps all *prompts*** and the *prompt-engineering* workflows used, organised as **reusable *skills*** for the AI tools and subject to **monthly review**.
- For **AI-assisted TEI encoding**, the operational method — the AI's role, prompts, cardinalities, guards and verification — is fixed in the [**AI-assisted encoding protocol**](docs/protocollo-IA-codifica.md), versioned with the repository and CI-verifiable: it concretely implements the transparency and human-oversight principles declared here.

### Alignment with *Trustworthy AI* principles
This use is consistent with the *Ethics Guidelines for Trustworthy AI* (High-Level Expert Group on AI, European Commission, 2019), in particular **transparency**, **human agency and oversight**, and **accountability**.

---

### Riferimenti · References
- European Commission — High-Level Expert Group on AI, *Ethics Guidelines for Trustworthy AI*, 2019.
- European Commission — ERA Forum, *Living Guidelines on the Responsible Use of Generative AI in Research*, marzo · March 2024.
- ALLEA, *The European Code of Conduct for Research Integrity* (ed. rivista · revised ed.).

---

*Ultimo aggiornamento · Last updated: 11 · 08 · 2026 — Luciano Longo*
