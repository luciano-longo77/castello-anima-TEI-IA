# Intertestualità sotto sorveglianza
### Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel *Castello dell'anima*

Questo repository documenta un progetto che integra **TEI interpretativo** e **Intelligenza Artificiale controllata** per lo studio delle funzioni intertestuali nel *Castello dell'anima* (1692–1693) di suor Teresa di San Geronimo. La ricerca si concentra sul modo in cui citazioni, glosse autoriali e rimandi mistici contribuiscono alla costruzione di chiarezza, coesione e stabilità dottrinale all'interno di un testo caratterizzato da forte vigilanza teologica.

---

## Indice

- [Intertestualità sotto sorveglianza](#intertestualità-sotto-sorveglianza)
  * [Obiettivi](#-obiettivi)
  * [Struttura del repository](#-struttura-del-repository)
  * [Modello TEI](#-modello-tei)
  * [Pipeline AI](#-pipeline-ai)
  * [Il campione](#-il-campione)
  * [Stato dell'arte e ragioni del modello](#-stato-dellarte-e-ragioni-del-modello)
  * [Contributo del progetto](#-contributo-del-progetto)
  * [Licenza](#-licenza)
  * [Autore](#-autore)

---

## Obiettivi

- Rappresentare in TEI citazioni bibliche, liturgiche, mistiche e proverbiali come **oggetti analitici** dotati di fonte, funzione retorica e impatto esplicativo.

- Modellare **glosse autoriali** (attenuatio, precisatio, declaratio) come dispositivi di chiarificazione e delimitazione dottrinale.

- Strutturare un **campione di 14 capitoli** selezionati per sensibilità dottrinale, densità intertestuale e presenza di fenomeni di revisione.

- Implementare una **pipeline AI controllata** che consente:

  * rimozione di un dispositivo testuale dal testo (`-CIT`),
  * recupero nel testo di una cancellatura autoriale (`+TEXTsub`),
  * integrazione per esteso di una citazione richiamata ma non riportata (`+CIT`),

con successiva valutazione degli effetti su chiarezza argomentativa, coesione locale e stabilità dottrinale percepita.

---

##  Struttura del repository

### `/tei`

Modellazione secondo TEI P5 con:

- struttura gerarchica in `div` per Libri e capitoli;
- citazioni annotate con `cit/quote/ref/bibl`;
- segmentazione retorica con `seg`;
- funzioni, rischio, operazioni prudenziali, stati mistici, esposizione, fase discorsiva e relazioni tramite l'attributo `@ana`, con puntatori alle categorie dichiarate in `classDecl`;
- gestione di varianti e fenomeni grafici con `add`, `del`, `subst`, `app`.

Organizzata in tre sottocartelle:

- **`/tei/header`** — il `teiHeader` completo dell'edizione (`castello-anima-teiHeader.xml`) e la relativa documentazione (README, guida di navigazione). ➡️ [Leggi il README del teiHeader](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/header/teiHeader-README.md)
- **`/tei/taxonomy`** — il sistema tassonomico interpretativo del progetto: la tassonomia normativa (`tassonomia-gh.xml`), i tre documenti di schema dedicati alla tassonomia (ODD, RelaxNG, Schematron), esempi di annotazione, log di lavorazione.,
 [Leggi il README del sistema tassonomico](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/tei/taxonomy/Sistema%20Tassonomico.md)
- **`/tei/text`** — il testo del manoscritto codificato in TEI.

### `/schema`

Schema di validazione generale del progetto (ODD, RelaxNG, Schematron), a copertura dell'intero modello — non solo della tassonomia.

### `/docs`

Raccoglie tutta la documentazione del progetto. Ogni README o documento prodotto per le singole sezioni (header, tassonomia, schema) confluisce anche qui, come punto di accesso unico alla documentazione completa.

### `/.github/workflows`

Il workflow di validazione automatica (CI/CD) che verifica la tassonomia a ogni modifica.

---

## 🧩 Modello TEI

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

Valore composito (alto, medio, basso), calcolato secondo la formula `I = 0.40*N + 0.35*A + 0.25*F`, assegnato a citazioni e glosse in base a:

- necessità interpretativa (N),
- capacità di ridurre ambiguità (A),
- funzione prudenziale (F) nel chiarire o delimitare concetti teologici complessi.

---

## 🤖 Pipeline AI

La pipeline opera su eventi controfattuali generati sotto controllo, secondo tre procedure:

- **`-CIT`**: rimozione di un dispositivo testuale (glossa o citazione) per valutare l'effetto della sua assenza;
- **`+TEXTsub`**: recupero nel testo di parole o passaggi che l'autrice stessa aveva cancellato, quando il manoscritto ne permette il recupero;
- **`+CIT`**: integrazione per esteso di una citazione che l'autrice richiama senza riportarne le parole.

Ogni evento è sottoposto a:

1. generazione controllata, con seed deterministico per garantire replicabilità,
2. verifica esperta (*expert-in-the-loop*),
3. rianalisi TEI con misurazione dell'impatto su chiarezza argomentativa, coesione locale e stabilità dottrinale percepita.

---

## 🔬 Il campione

Il dataset include **14 capitoli** distribuiti nei tre Libri dell'opera.  
I segmenti selezionati presentano:

- nodi dottrinali sensibili (contemplazione, unione, sicurezza spirituale, discernimento),
- elevata densità di citazioni o rimandi,
- glosse autoriali impiegate per chiarificazione o attenuazione,
- estensione comparabile e equilibrio fra fenomeni retorici.

Questo campione costituisce la base per l'annotazione TEI e per la sperimentazione AI.

---

## 📌 Stato dell'arte e ragioni del modello

Dalle linee di ricerca degli studi attuali emerge che:

- la scrittura mistica femminile post tridentina è caratterizzata da forte pressione normativa e sorveglianza dottrinale;
- citazioni e glosse formano **una infrastruttura di controllo** che stabilizza il discorso nei punti ad alta esposizione;
- mancano strumenti replicabili per misurare il ruolo dell'intertestualità in contesti analoghi;

Su questa base

- 📡 il progetto propone un modello computazionale TEI+IA che colma questo vuoto metodologico.

---

## 🌐 Contributo del progetto

Il modello permette di:

- analizzare in modo sistematico il rapporto fra citazione, glossa e costruzione del discorso mistico;
- rendere osservabili e misurabili fenomeni normalmente affidati alla sola interpretazione qualitativa;
- verificare l'effetto delle varianti tramite scenari controfattuali controllati;
- fornire un protocollo replicabile per lo studio di testi mistici post tridentini e materiali prodotti in contesti di sorveglianza dottrinale.

---

## 📄 Licenza

Creative Commons Attribution 4.0 International (**CC BY 4.0**).  
Vedi il file `SPDX-License-Identifier: CC-BY-4.0` per i dettagli completi.

---

## 👤 Autore

**Luciano Longo**  
Filologia digitale e Digital Humanities  
Contatti: <luciano.longo@dedalus.com> / <https://orcid.org/0009-0005-7557-7546> / <https://github.com/luciano-longo77>
