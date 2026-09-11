# Guida introduttiva — il progetto in una pagina
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

> **Cos'è questo file.** Una **panoramica narrativa** del progetto: il filo del discorso — dal
> testo al modello, dalla pipeline alle misure — per chi arriva nuovo o legge il paper. **Non è
> normativo**: non definisce regole, formule o valori. Per *dove trovare* le cose usa la mappa dei
> file in [`README.md`](README.md); per il *dettaglio autoritativo* segui i rimandi qui sotto, che
> puntano sempre al documento-fonte. In caso di divergenza, **valgono i documenti-autorità**, non
> questa pagina.

---

## 1. In una pagina

L'edizione digitale del *Castello dell'anima* è **TEI-driven** e **AI-assisted**. Il testo di
lettura è una trascrizione interpretativa a **normalizzazione grafica silenziosa**, con apparato
**solo sostanziale** e annotazione interpretativa multilivello. Su questa base, una **pipeline IA
controllata** (l'IA *propone*, l'editore *decide*) mette alla prova il testo con esperimenti
**controfattuali** misurabili. Due principi tengono insieme tutto: **ogni intervento è
tracciabile** e **il testo di lettura non viene mai toccato** dagli esperimenti.

## 2. Il modello (come è annotato il testo)

Il testo è segmentato in unità di senso (`<seg>`), ciascuna caratterizzata su **otto assi
interpretativi** in `@ana` (funzione, operazione retorica, rischio dottrinale, esposizione, fase,
stato mistico, relazione intertestuale, impatto). A ogni segmento è associato un **indice
d'impatto** — una misura numerica della sua forza regolativa, a bande — e l'annotazione vive in
**quattro strati `<standOff>`** (indice d'impatto, figure retoriche, aree semantiche, catene
tematiche). Le citazioni latine sono marcate come `<cit>` e censite a parte.

- il *cosa significa* di ogni asse e categoria → [`data-dictionary.md`](data-dictionary.md) *(derivato dalla tassonomia)*
- il *come si codifica* (segmentazione, `@ana`, apparato, standOff) → [`teiText-guida-codifica.md`](teiText-guida-codifica.md) *(autorità del modello)*
- il *come si calcola* l'indice d'impatto (formula, bande, ancore) → [`indice-impatto.md`](indice-impatto.md) → [`Protocollo-indice-impatto.md`](Protocollo-indice-impatto.md)
- il *cosa si normalizza in silenzio e cosa resta* → [`criteri-trascrizione.md`](criteri-trascrizione.md)
- le *citazioni* e le loro carte → [`anagrafe-citazioni.md`](anagrafe-citazioni.md)

## 3. La pipeline controfattuale (come lavora l'IA)

Per misurare quanto un elemento *regge* il testo, la pipeline ne genera una **variante
controfattuale** e ne osserva l'effetto. Le operazioni consolidate sono tre:

- **−CIT** — toglie una citazione/glossa di legittimazione (sottrattiva);
- **+TEXTsub** — recupero di cancellatura, in due sottotipi (*ripristino-cassatura* e *rimozione-aggiunta*) (sottrattiva);
- **+CIT** — esplicita una citazione **allusa e attestata** (additiva: l'**unica** operazione generativa).

Ogni variante è **validata dall'editore** e registrata in un **apparato standoff esterno**,
ancorato al `<seg>` ma tenuto **fuori dal testo di lettura**. Le sottrattive sono deterministiche;
il +CIT è generativo, con una tracciabilità dichiarata onestamente (compreso il trattamento del
`seed`) — regole e prompt nel runbook.

- il *runbook* completo dell'IA (ruolo, prompt, verifica, determinismo) → [`protocollo-IA-codifica.md`](protocollo-IA-codifica.md)
- l'*apparato esterno* delle varianti (come è codificato) → [`../variants/README.md`](../variants/README.md)
- il *campione* e i criteri di selezione dei loci → [`base-dati_campionamento.md`](base-dati_campionamento.md)

## 4. Le misure (cosa si ottiene)

Ogni esperimento produce misure per locus: la variazione dell'indice d'impatto (**ΔI**), la
**chiarezza** e la **stabilità dottrinale** (D1, D3, rubriche editoriali), la **coesione**
strutturale (D2, deterministica e rigenerabile), il loro **join** finale (T10) e un **controllo
filologico a 4 assi** (check-list) con il relativo esito. Tutte le misure sono chiavate per locus e
coerenti tra loro.

- registro delle run, schema delle misure e comandi → [`../logs/README.md`](../logs/README.md)
- rubriche di giudizio D1/D3 → [`rubriche-D1-D3.md`](rubriche-D1-D3.md)
- ogni intervento editoriale marcato (rendiconto) → [`interventi-editoriali.md`](interventi-editoriali.md) *(derivato)*

## 5. Perché funziona

L'IA non interpreta al posto del filologo: **misura e mette alla prova** il testo entro un
perimetro definito dal TEI e sotto vaglio editoriale. Il risultato è un **laboratorio filologico
digitale** — *tracciabile* (ogni run ha impronta e verdetto), *riproducibile* (le operazioni
sottrattive e la coesione sono deterministiche; il +CIT è certificato dall'impronta del suo output)
e *falsificabile* (chiunque può rieseguire e verificare). La verifica autoritativa resta la **CI**
(RelaxNG, Schematron, otto guardie, NFC) e l'apparato esterno tiene il testo di lettura **fuori dal
raggio** dell'esperimento.

---

*Documento di orientamento, versionato col repository. Per la navigazione file-per-file →
[`README.md`](README.md); per le regole e i valori → i documenti-autorità linkati sopra.*
