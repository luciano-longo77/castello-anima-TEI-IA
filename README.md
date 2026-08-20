# Intertestualità sotto sorveglianza
## *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA) [![Vocabolario SKOS](https://img.shields.io/badge/SKOS-vocabolario%20online-1b7f5c)](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

Questo repository documenta un progetto che integra **TEI interpretativo** e **Intelligenza Artificiale (IA) controllata** *expert-in-the-loop*, per lo studio delle funzioni intertestuali nel *Castello dell'anima* (1692–1693) di **suor Teresa di San Geronimo**. La ricerca si concentra sul modo in cui citazioni, glosse autoriali e rimandi mistici contribuiscono alla costruzione di *chiarezza*, *coesione* e *stabilità dottrinale* all'interno di un testo caratterizzato da **forte vigilanza teologica**.

> 🔗 **Vocabolario SKOS navigabile online** — gli otto assi interpretativi sono pubblicati come **vocabolario controllato SKOS**, con URI dereferenziabili (ci clicchi e si apre): **[esplora il vocabolario](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/)**.

---

## Indice

- [Intertestualità sotto sorveglianza](#intertestualità-sotto-sorveglianza)
  * [Obiettivi](#obiettivi)
  * [Struttura del repository](#struttura-del-repository)
  * [Modello TEI](#modello-tei)
  * [Pipeline AI](#pipeline-ai)
  * [Il campione](#il-campione)
  * [Stato dell'arte e ragioni del modello](#stato-dellarte-e-ragioni-del-modello)
  * [Contributo del progetto](#contributo-del-progetto)
  * [Licenza](#licenza)
  * [Autore](#-autore)

---

## Obiettivi (O)

- **(O1)** Rappresentare in TEI citazioni bibliche, liturgiche, mistiche e proverbiali come **oggetti analitici** dotati di fonte, funzione retorica e impatto esplicativo.

- **(O2)** Modellare **glosse autoriali** (attenuatio, precisatio, declaratio) come dispositivi di chiarificazione e delimitazione dottrinale.

- **(O3)** Strutturare un **campione di 29 loci (36 capitoli)** selezionati per sensibilità dottrinale, densità intertestuale e presenza di fenomeni di revisione.

- **(O4)** Implementare una **pipeline AI controllata** che consente:

  * **rimozione** di un dispositivo testuale dal testo **(`-CIT`)**,
  * **recupero** nel testo di una cancellatura autoriale **(`+TEXTsub`)**,
  * **integrazione** per esteso di una citazione richiamata ma non riportata **(`+CIT`)**,

con successiva **valutazione degli effetti** su chiarezza argomentativa, coesione locale e stabilità dottrinale percepita.

---

## Struttura del repository

### `/tei`

Modellazione secondo TEI P5 con:

- struttura gerarchica in `div` per Libri e capitoli;
- citazioni annotate con `cit/quote/ref/bibl`;
- segmentazione retorica con `seg`;
- funzioni, rischio, operazioni prudenziali, stati mistici, esposizione, fase discorsiva e relazioni tramite l'attributo `@ana`, con puntatori alle categorie dichiarate in `classDecl`;
- gestione delle varianti sostanziali d'autrice con `app`/`lem`/`rdg` (che contengono `add`/`del`/`subst`); la normalizzazione grafica è silenziosa e dichiarata (`docs/criteri-trascrizione.md`).

Organizzata in tre sottocartelle:

- **`/tei/header`** — il `teiHeader` completo dell'edizione (`castello-anima-teiHeader.xml`) e la relativa documentazione (README, guida di navigazione). ➡️
  [Leggi il README del teiHeader](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/header/teiHeader-README.md)
- **`/tei/taxonomy`** — il sistema tassonomico interpretativo del progetto: la tassonomia normativa (`tassonomia-gh.xml`), i tre documenti di schema dedicati alla tassonomia (ODD, RelaxNG, Schematron), esempi di annotazione, log di lavorazione. ➡️
 [Leggi il README del sistema tassonomico](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/taxonomy/Sistema%20Tassonomico.md)
- **`/tei/text`** — il testo del manoscritto codificato in TEI.➡️
  [Leggi la Guida ragionata alla codifica del text](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/teiText-guida-codifica.md)

### `/schema`

Schema di validazione generale del progetto: l'ODD del modello, il **`tei_all.rng` vendorizzato** (TEI All, versione fissata per una validazione riproducibile) e lo **Schematron dell'indice d'impatto** (`impactindex.sch`), a copertura dell'intero modello — non solo della tassonomia.

### `/vocab`

Il **vocabolario SKOS** degli assi interpretativi, **generato** da `tassonomia-gh.xml` (fonte normativa: non si edita a mano): **10 `skos:ConceptScheme` / 60 `skos:Concept`** con URI dereferenziabili (`https://w3id.org/castello-anima-vocab/…`). Contiene il Turtle (`castello-anima-vocab.ttl`), un **sito navigabile** (`vocab/site/`) e gli allineamenti esterni opzionali (`alignments.tsv`). La guardia CI **Vocab SKOS** garantisce la coerenza col teiText (sync + round-trip).
➡️ **[Esplora il vocabolario online](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/)** · [Leggi il README di `vocab/`](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/vocab/README.md)

### `/docs`

Raccoglie tutta la documentazione del progetto. Ogni README o documento prodotto per le singole sezioni (header, tassonomia, schema) confluisce anche qui, come punto di accesso unico alla documentazione completa.

### `/tools`

Strumenti d'ausilio all'annotazione: l'**Assistente @ana**, il **Calcolatore** e il **Visualizzatore** dell'indice d'impatto, e il **Visualizzatore del vocabolario SKOS** (pagine HTML autonome, apribili nel browser) e `impact_index.py` (audit/authoring da riga di comando) — aiuti alla codifica, **non** parte della validazione automatica. Qui stanno anche i **generatori** invocati dai workflow `gen-*` della CI: `gen_data_dictionary.py` (rigenera `docs/data-dictionary.md` dalla tassonomia), `estrattore_interventi.py` (rigenera `docs/interventi-editoriali.md` dal teiText) e `gen_skos.py` (rigenera il vocabolario SKOS dalla tassonomia).
➡️ [Leggi il README di `tools/`](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tools/README.md).

### `/.github/workflows`

Cinque workflow di GitHub Actions, attivi a ogni push/PR (e avviabili a mano):

- **Validate Text** — sul teiText: buona formazione, risoluzione `xi:include`, RelaxNG (TEI All, versione fissata), guardia **NFC**, guardia **E2** (ogni token `@ana` risolve a una categoria dichiarata), **co-occorrenza** degli assi, **cit/glossa**, **citazioni**, **commenti**, **interventi editoriali**, **regole-fissate** (retrace/naming/`@ana`-su-seg/sobrietà), **whitespace** (anti-corruzione: whitespace intra-parola in `subst`/`choice`) e **Schematron dell'indice d'impatto** (`impactindex.sch`).
- **Validate Taxonomy** — sulla tassonomia: buona formazione, RelaxNG + Schematron dedicati, validazione degli esempi, e guardia **E1** (le tassonomie interpretative in `tassonomia-gh.xml` coincidono con la copia nel `classDecl` della testata).
- **Vocab SKOS** — sul vocabolario: rigenera il `.ttl` dalla tassonomia e verifica **sync** (il file committato è byte-identico alla rigenerazione) e **round-trip** (ogni token `@ana` e ogni banda del teiText risolve a un `skos:Concept`).
- **Genera data-dictionary** — esegue `tools/gen_data_dictionary.py` e ricommitta `docs/data-dictionary.md` se cambiato.
- **Genera interventi-editoriali** — esegue `tools/estrattore_interventi.py` e ricommitta `docs/interventi-editoriali.md` se cambiato.

➡️ [Leggi il README della CI](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/.github/workflows/README.md)

---

## Modello TEI

### Citazioni

Rappresentate come entità autonome con:

- testo citato,
- origine canonica o mistica,
- riferimento normalizzato,
- funzione retorica (legittimazione, pedagogia, gestione del rischio, ethos).

### Glosse

Annotate come glosse esplicative, attenuative o dichiarative, collocate nei punti a maggiore esposizione dottrinale del testo.

### Segmenti retorici

Porzioni di testo rilevanti, classificate tramite `@ana` secondo la funzione che svolgono nel discorso.

### Indice di impatto

Valore composito discretizzato in quattro classi (`impact-low`, `impact-medium`, `impact-high`, `impact-critical`), calcolato secondo la formula 
**`I = (4·Fnorm + 2·N + 1·A) / 7`**, con pesi derivanti da un confronto a coppie secondo il principio dell'**Analytic Hierarchy Process** (AHP).
Il confronto restituisce il rapporto **F : N : A = 4 : 2 : 1**, assegnato a citazioni e glosse in base a:

- **N** — necessità interpretativa (esposizione dottrinale del passo prima dell'intervento);
- **A** — riduzione dell'ambiguità (quanto l'intervento restringe le letture possibili);
- **F** — funzione prudenziale come classe formale del marcatore (ordinale 1/2/3, derivata dall'asse `operation`), normalizzata come `Fnorm = F/3`.

Le soglie delle quattro classi sono calibrate sulla distribuzione reale del campione. 
N e A si assegnano per **bande** (l'annotatore sceglie la banda, non il decimale), ciascuna con un **valore‑ancora fisso**; la doppia registrazione porta la classe `#impact-*` in `@ana` e il calcolo in una `<fs>` dentro `<standOff type="impact-index">`. ➡️
 [Leggi il README dell'Indice d'impatto (impact-index)](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/indice-impatto.md)

> Fonte: **T. L. Saaty**, *The Analytic Hierarchy Process: Planning, Priority Setting, Resource Allocation*, New York, McGraw-Hill, 1980
---

## Pipeline AI

La pipeline opera su eventi controfattuali generati sotto controllo, secondo tre procedure:

- **`-CIT`**: rimozione di un dispositivo testuale (glossa o citazione) per valutare l'effetto della sua assenza;
- **`+TEXTsub`**: recupero nel testo di parole o passaggi che l'autrice stessa aveva cancellato, quando il manoscritto ne permette il recupero;
- **`+CIT`**: integrazione per esteso di una citazione che l'autrice richiama senza riportarne le parole.

Ogni evento è sottoposto a:

1. generazione controllata, con seed deterministico per garantire replicabilità,
2. verifica esperta (*expert-in-the-loop*),
3. rianalisi TEI con misurazione dell'impatto su chiarezza argomentativa, coesione locale e stabilità dottrinale percepita.

---

## Il campione

Il dataset è un **campione ragionato**: non trascrive l'intera opera, ma i capitoli a maggiore rilevanza dottrinale, intertestuale e genetica. Secondo il piano di campionamento (vedi *Base dati per il campionamento*), il campione consta di **29 loci di selezione, corrispondenti a 36 capitoli**, distribuiti nei tre Libri.

I capitoli sono selezionati perché presentano:

- nodi dottrinali sensibili (contemplazione, unione, sicurezza spirituale, discernimento),
- elevata densità di citazioni o rimandi,
- glosse autoriali impiegate per chiarificazione o attenuazione,
- estensione comparabile e equilibrio fra fenomeni retorici.

Questo campione costituisce la base per l'annotazione TEI e per la sperimentazione AI.

➡️ [Leggi la **Base dati per il campionamento**](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/base-dati_campionamento.md) 

---

## Stato dell'arte e ragioni del modello

Dalle linee di ricerca degli studi attuali emerge che:

- **(1)** la scrittura mistica femminile post tridentina è caratterizzata da forte pressione normativa e sorveglianza dottrinale;
- **(2)** citazioni e glosse formano **una infrastruttura di controllo** che stabilizza il discorso nei punti ad alta esposizione;
- **(3)** mancano strumenti replicabili per misurare il ruolo dell'intertestualità in contesti analoghi;

Su questa base

- il progetto propone un *modello computazionale TEI+IA* che tende a colmare questo vuoto metodologico.

---

## Contributo del progetto

Il modello permette di:

- **(1)** analizzare in modo sistematico il rapporto fra citazione, glossa e costruzione del discorso mistico;
- **(2)** rendere osservabili e misurabili fenomeni normalmente affidati alla sola interpretazione qualitativa;
- **(3)** verificare l'effetto delle varianti tramite scenari controfattuali controllati;
- **(4)** fornire un protocollo replicabile per lo studio di testi mistici post tridentini e materiali prodotti in contesti di sorveglianza dottrinale.

---

## Licenza

Creative Commons Attribution 4.0 International (**CC BY 4.0**).  
Vedi il file `LICENCE.md` per i dettagli completi.

---

## 👤 Autore
**Luciano Longo**   
- Contatti: <luciano.longo@dedalus.com> 
- ORCID: <https://orcid.org/0009-0005-7557-7546> 
- GitHub: <https://github.com/luciano-longo77>
- Website: <https://luciano-longo77.github.io>
