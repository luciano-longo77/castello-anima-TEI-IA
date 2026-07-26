# Castello dell'anima — Edizione Digitale TEI + IA (teiHeader)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Versione**: working draft — 25 luglio 2026  
**Licenza**: CC BY 4.0

---

## 1. Cos'è, e cosa non è, questo modello

Questo `teiHeader` non è un contenitore di metadati descrittivi nel senso tradizionale. È l'infrastruttura di governo di un'edizione che tratta l'annotazione interpretativa come **dato di prima classe**, non come commento a margine del testo — e che rende esplicito, tracciabile e verificabile l'apporto di un protocollo IA-assistito all'interno del processo editoriale, invece di trattarlo come un dettaglio tecnico invisibile.

Tre scelte architetturali distinguono questo modello da un `teiHeader` descrittivo standard:

- **Separazione categoriale tra interpretazione e processo.** Il `classDecl` non contiene un'unica tassonomia indifferenziata, ma due famiglie concettualmente distinte: otto assi interpretativi che governano la lettura del testo (§3), e due assi di provenienza editoriale (`fase`, `workflow`) che documentano *come* l'edizione è stata prodotta, incluso l'apporto dell'IA. Le due famiglie non si mescolano mai nei riferimenti `@ana` — è una scelta deliberata, verificata Schematron alla mano, non solo dichiarata in prosa.
- **Auditabilità del protocollo IA a doppio livello.** La stessa logica operativa — tre procedure controfattuali, verifica *expert-in-the-loop*, misurazione su dimensioni esplicite — è espressa sia in prosa filologica (`projectDesc`) sia in specifica machine-readable (`xenoData`). Chi consulta il file può verificare che le due descrizioni coincidano, non deve fidarsi di una dichiarazione unica non controllabile.
- **Il rischio dottrinale come categoria di analisi, non di giudizio.** La tassonomia `risk` non etichetta il testo come "sospetto"; modella le condizioni storiche di esposizione a cui la scrivente doveva rispondere, distinte dalle strategie retoriche con cui vi rispondeva (`func`, `operation`). È una distinzione metodologica, non solo terminologica: separa il fenomeno storico dall'azione autoriale su di esso.

---

## 2. Il protocollo TEI + IA

Il cuore metodologicamente più originale del progetto è il trattamento del protocollo IA come **oggetto filologico verificabile**, non come funzionalità accessoria.

### 2.1 Le tre procedure controfattuali

| Codice | Procedura | Funzione critica |
|---|---|---|
| `-CIT` | Rimozione del dispositivo testuale (glossa/citazione) | Osservare l'effetto della sua assenza |
| `+TEXTsub` | Recupero di una cancellatura autoriale | Rendere visibile un livello genetico non altrimenti accessibile |
| `+CIT` | Integrazione per esteso di una citazione richiamata ma non riportata | Esplicitare un rimando lasciato implicito dall'autrice |

Ogni evento generato è sottoposto a **verifica expert-in-the-loop** — non è mai incorporato nel testo stabilito, ma archiviato come lettura alternativa (`<app>/<lem>/<rdg>`) e misurato su tre dimensioni dichiarate esplicitamente: chiarezza argomentativa, coesione locale, stabilità dottrinale percepita (D1–D3).

### 2.2 Perché due livelli di descrizione

Il protocollo è documentato sia in `projectDesc` (prosa filologica, motivazione metodologica) sia in `xenoData` (specifica JSON: modello IA, vincoli linguistici, parametri di generazione, campi obbligatori dell'audit trail). Questo non è ridondanza: è la condizione perché un revisore esterno possa verificare che la descrizione discorsiva del metodo e il suo comportamento macchina-leggibile **coincidano**, invece di dover fidarsi dell'una o dell'altra.

### 2.3 Cosa il protocollo esplicitamente non fa

Nessun evento controfattuale modifica il testo base. Nessuna operazione IA interviene senza revisione umana dichiarata. I vincoli linguistici (`historical_style`, `forbidden: modernisms/anachronisms/semantic elaborations`) sono dichiarati come parametri verificabili, non come intenzioni generiche.

---

## 3. Il sistema tassonomico

Otto assi interpretativi, organizzati in tre livelli complementari (dichiarati esplicitamente in `projectDesc`):

- **Fenomenologico** — cosa il testo tematizza: `func` (funzioni retoriche), `mystic_state` (stati mistici), `relation` (relazioni intertestuali e fenomenologiche)
- **Prudenziale** — come il testo gestisce il rischio: `risk` (condizioni di esposizione dottrinale), `operation` (strategie discorsive di mitigazione), `exposition` (grado di esplicitazione)
- **Strutturale** — dove e con quale peso: `impact` (rilevanza interpretativa), `phase` (posizione nella progressione discorsiva)

A questi si affiancano due tassonomie di processo, **non interpretative**: `fase` (42 categorie, fasi di lavoro editoriale) e `workflow` (4 categorie, esclusivamente gli scenari controfattuali IA). La distinzione non è cosmetica: nessuna categoria di `workflow` descrive un'attività editoriale generica, e nessuna categoria di `fase` descrive un evento controfattuale — la separazione è stata verificata categoria per categoria, non solo dichiarata.

Ogni categoria richiede una `catDesc` non vuota e un `xml:id` che rispetta il prefisso della tassonomia radice: vincoli imposti non editorialmente ma meccanicamente, tramite Schematron.

---

## 4. Validazione

Il modello è verificato, non solo dichiarato conforme:

- **Struttura**: RelaxNG (via ODD di progetto)
- **Coerenza semantica**: 4 regole ISO Schematron — presenza e non-vacuità di `catDesc`, coerenza del prefisso `xml:id` rispetto alla tassonomia radice (verificata contro l'antenato, non il padre immediato — permette a nodi-contenitore come `risk-dottrinale` di avere figli con lo stesso prefisso), unicità globale degli `xml:id`
- **Puntatori interni**: ogni `@ana`, `@ref`, `@who`, `@corresp` nel documento risolve a un `xml:id` realmente dichiarato — nessun riferimento orfano

Questi tre livelli sono verificabili indipendentemente da chiunque riesegua la validazione sul file, non solo dichiarati in questo README.

---

## 5. Apparato storico-critico

Descrizione codicologica completa (mani, inchiostri, strati genetici Tb0–T3), ricostruzione biografica e processuale dell'autrice ancorata a identificatori esterni verificabili (VIAF, Wikidata, GeoNames), e un apparato di note critiche articolato su sei assi (materiale, prudenziale, linguistico, teologico, di trasmissione, stilistico) — non manualistico, con argomentazione filologica propria in ciascuna nota.

---

## 6. Limiti dichiarati

Non tutto nel modello è già chiuso, e va detto:

- Il vincolo interpretativo secondo cui le categorie `func` di gestione del rischio presuppongono sempre un'operazione `operation` corrispondente è normativo solo in prosa (`projectDesc` §3) — non esiste ancora una regola Schematron che lo verifichi meccanicamente.
- Il collegamento fra testo e immagini del manoscritto è oggi limitato a `@facs` su `<pb>` — non è previsto un vero apparato di facsimile digitale (`<facsimile>`/`<surface>`/IIIF), scelta consapevole ma che limita la fruizione rispetto a edizioni digitali costruite attorno alla sincronizzazione immagine-testo.
- Non è presente un identificatore persistente (DOI/ARK) per la citazione stabile dell'edizione, né una dichiarazione di finanziamento (`fundingStmt`).

---

## 7. Come citare

Longo, Luciano (2026). *Castello dell'anima — teiHeader dell'edizione digitale TEI + IA*. Working draft, 25 luglio 2026. Licenza CC BY 4.0.

---

## 8. Contatti

**Editor**: Luciano Longo  
Email: luciano.longo@dedalus.com  
ORCID: https://orcid.org/0009-0005-7557-7546
