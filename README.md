# Intertestualità sotto sorveglianza
## *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

Questo repository documenta un progetto che integra **TEI interpretativo** e **Intelligenza Artificiale (IA) controllata** *expert-in-the-loop*, per lo studio delle funzioni intertestuali nel *Castello dell'anima* (1692–1693) di **suor Teresa di San Geronimo**. La ricerca si concentra sul modo in cui citazioni, glosse autoriali e rimandi mistici contribuiscono alla costruzione di *chiarezza*, *coesione* e *stabilità dottrinale* all'interno di un testo caratterizzato da **forte vigilanza teologica**.

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

- **(O3)** Strutturare un **campione di 14 loci (16 capitoli)** selezionati per sensibilità dottrinale, densità intertestuale e presenza di fenomeni di revisione.

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
- gestione di varianti e fenomeni grafici con `add`, `del`, `subst`, `app`.

Organizzata in tre sottocartelle:

- **`/tei/header`** — il `teiHeader` completo dell'edizione (`castello-anima-teiHeader.xml`) e la relativa documentazione (README, guida di navigazione). ➡️
  [Leggi il README del teiHeader](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/header/teiHeader-README.md)
- **`/tei/taxonomy`** — il sistema tassonomico interpretativo del progetto: la tassonomia normativa (`tassonomia-gh.xml`), i tre documenti di schema dedicati alla tassonomia (ODD, RelaxNG, Schematron), esempi di annotazione, log di lavorazione. ➡️
 [Leggi il README del sistema tassonomico](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/taxonomy/Sistema%20Tassonomico.md)
- **`/tei/text`** — il testo del manoscritto codificato in TEI.➡️
  [Leggi la Guida ragionata alla codifica del text](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/teiText-guida-codifica.md)

### `/schema`

Schema di validazione generale del progetto: l'ODD del modello, il **`tei_all.rng` vendorizzato** (TEI All, versione fissata per una validazione riproducibile) e lo **Schematron dell'indice d'impatto** (`impactindex.sch`), a copertura dell'intero modello — non solo della tassonomia.

### `/docs`

Raccoglie tutta la documentazione del progetto. Ogni README o documento prodotto per le singole sezioni (header, tassonomia, schema) confluisce anche qui, come punto di accesso unico alla documentazione completa.

### `/tools`

Strumenti d'ausilio all'annotazione (non validati dalla CI): l'**Assistente @ana**, il **Calcolatore** e il **Visualizzatore** dell'indice d'impatto (pagine HTML autonome, apribili nel browser) e `impact_index.py` (audit/authoring da riga di comando). 
➡️ [Leggi il README di `tools/`](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tools/README.md).

### `/.github/workflows`

Due workflow di validazione automatica (CI), attivi a ogni push/PR:

- **Validate Taxonomy** — buona formazione, RelaxNG + Schematron della tassonomia, e guardia **E1** (le 8 tassonomie interpretative in `tassonomia-gh.xml` coincidono con la copia nella testata).
- **Validate Text** — buona formazione, risoluzione `xi:include`, RelaxNG (TEI All, versione fissata), guardia **NFC**, guardia **E2** (ogni token `@ana` risolve a una categoria dichiarata), guardia di **co-occorrenza** e **Schematron dell'indice d'impatto** (`impactindex.sch`).
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

Valore composito discretizzato in quattro classi (`impact-low`, `impact-medium`, `impact-high`, `impact-critical`), calcolato secondo la formula del progetto AURORA `I = (4·F_norm + 2·N + 1·A) / 7`, con pesi AHP in rapporto F : N : A = 4 : 2 : 1, assegnato a citazioni e glosse in base a:

- **N** — necessità interpretativa (esposizione dottrinale del passo prima dell'intervento);
- **A** — riduzione dell'ambiguità (quanto l'intervento restringe le letture possibili);
- **F** — funzione prudenziale come classe formale del marcatore (ordinale 1/2/3, derivata dall'asse `operation`), normalizzata come `F_norm = F/3`.

Le soglie delle quattro classi sono calibrate sulla distribuzione reale del campione. 
N e A si assegnano per **bande** (l'annotatore sceglie la banda, non il decimale), ciascuna con un **valore‑ancora fisso**; la doppia registrazione porta la classe `#impact-*` in `@ana` e il calcolo in una `<fs>` dentro `<standOff type="impact-index">`. ➡️
 [Leggi il README dell'Indice d'impatto (impact-index)](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/indice-impatto.md)

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

Il dataset include un **campione di 14 loci (16 capitoli)** distribuiti nei tre Libri dell'opera.  
I segmenti selezionati presentano:

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
Filologia digitale e Digital Humanities  
Contatti: <luciano.longo@dedalus.com> / <https://orcid.org/0009-0005-7557-7546> / <https://github.com/luciano-longo77>
