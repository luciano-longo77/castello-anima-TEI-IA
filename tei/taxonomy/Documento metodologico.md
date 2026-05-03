<!--
Documento metodologico.

Questo paper descrive la tassonomia interpretativa prudenziale
implementata in `tassonomia.xml` e governata tramite schema TEI,
Rel​ax NG e Schematron.

Il documento non introduce categorie nuove né propone estensioni
del modello: costituisce la descrizione formale e critica
della tassonomia così come implementata nel repository.
-->

# Una tassonomia interpretativa prudenziale per l’annotazione TEI  
## Statuto, architettura e governo di un modello ermeneutico

## Abstract

Il contributo presenta una **tassonomia interpretativa prudenziale** progettata a partire dal *Castello dell’anima* di Teresa di San Geronimo (secolo XVII), come modello per la formalizzazione e il governo dell’annotazione interpretativa in ambiente TEI. La tassonomia è concepita come un **oggetto ermeneutico autonomo**, formalizzato nel `teiHeader` e governato mediante vincoli strutturali (Relax NG) e semantici (Schematron). L’obiettivo non è classificare contenuti tematici, ma rendere **esplicite, verificabili e controllabili** le categorie interpretative che presiedono all’annotazione di testi ad alta densità ermeneutica. Il modello si fonda su un’architettura multi‑asse, distingue nettamente la definizione delle categorie dal loro uso nel testo e costituisce un’infrastruttura metodologica verificabile e riproducibile.

---

## 1. Oggetto e statuto della tassonomia interpretativa

La tassonomia qui presentata non è una ontologia tematica del contenuto testuale, né un apparato descrittivo del lessico o dei concetti dottrinali. Essa nasce come **dispositivo di governo dell’interpretazione**, progettato per rendere esplicite le categorie attraverso cui un testo viene letto, segmentato e annotato.

Nel contesto del *Castello dell’anima*, l’annotazione comporta necessariamente l’attivazione di categorie interpretative non neutre: funzioni retoriche, strategie prudenziali, livelli di rischio dottrinale, gradi di esposizione concettuale. La tassonomia assume come principio di base che tali categorie **non possano rimanere implicite**, né essere affidate a etichette estemporanee o a note discorsive non formalizzate.

Per questo motivo la tassonomia è modellizzata come **oggetto TEI autonomo**, collocato nel `teiHeader` e separato dal corpo del testo. Essa non descrive il testo, ma **dichiara le condizioni interpretative del suo trattamento**. Il suo statuto è quindi metatestuale ed ermeneutico: la tassonomia non è un supporto dell’edizione, ma una infrastruttura concettuale che precede e governa l’annotazione.

---

## 2. Architettura della tassonomia interpretativa prudenziale

### 2.1 Razionale della struttura multi‑asse

L’interpretazione di un testo mistico non è riducibile a una singola dimensione semantica. Una stessa unità testuale può, simultaneamente, svolgere una funzione retorica, attivare un rischio dottrinale, richiedere un’operazione prudenziale e avere un impatto interpretativo differente sul contesto immediato e sull’opera nel suo complesso.

Per rispondere a questa complessità, la tassonomia adotta una **architettura multi‑asse**, articolata in tassonomie distinte, ciascuna dedicata a una specifica dimensione dell’atto interpretativo. Questa separazione impedisce la sovrapposizione di categorie eterogenee e garantisce la leggibilità e l’interrogabilità del modello.

### 2.2 Le tassonomie core

Il modello definisce otto tassonomie principali, ciascuna formalizzata come elemento `<taxonomy>` dotato di identificatore stabile:

- **Funzioni interpretative (`func`)**  
  Modella il ruolo discorsivo e retorico dei segmenti testuali (legittimazione, ethos, pedagogia).  
  Non descrive contenuti, ma funzioni svolte nel discorso.

- **Rischio dottrinale (`risk`)**  
  Esplicita i punti di possibile ambiguità o criticità interpretativa (quietismo, ambiguità, lettura impropria).  
  Svolge una funzione eminentemente prudenziale.

- **Impatto interpretativo (`impact`)**  
  Indica il peso interpretativo di un segmento sul contesto esegetico, distinguendo nodi portanti da passaggi di supporto.

- **Stati mistici (`mystic_state`)**  
  Modella gli stati dell’esperienza mistica non come temi, ma come categorie operative dell’interpretazione.

- **Operazioni prudenziali (`operation`)**  
  Rende esplicite le strategie testuali di controllo e mitigazione del rischio (`attenuatio`, `delimitatio`, `precisatio`).

- **Livello di esposizione (`exposition`)**  
  Descrive il grado di esplicitazione concettuale, indipendentemente dal contenuto teologico.

- **Fase discorsiva (`phase`)**  
  Colloca i segmenti all’interno della progressione argomentativa dell’opera.

- **Relazioni (`relation`)**  
  Formalizza legami intertestuali, analogici e argomentativi.

### 2.3 Categorie e descrizioni

Ogni categoria è identificata da un `xml:id` stabile ed è obbligatoriamente accompagnata da un elemento `<desc>`. La descrizione non ha valore meramente documentativo, ma costituisce il **luogo in cui l’interpretazione viene resa esplicita**. Una categoria priva di descrizione è considerata metodologicamente invalida. Questa scelta trasforma la tassonomia in uno spazio di responsabilità ermeneutica, impedendo l’uso di etichette prive di fondamento interpretativo dichiarato.

---

## 3. Implementazione TEI e governo formale

### 3.1 Collocazione nel `teiHeader`

La tassonomia è implementata nel `teiHeader`, all’interno di `<encodingDesc>/<classDecl>`. Questa collocazione sancisce la sua funzione di **metamodello interpretativo**, distinto dal testo e dichiarato prima di ogni annotazione.

Il file `tassonomia.xml` è concepito come documento TEI completo e autosufficiente, dotato di statuto scientifico autonomo.

### 3.2 Vincoli strutturali e semantici

Il governo della tassonomia è garantito da due livelli di validazione:

- **Relax NG**, che definisce la struttura ammessa e l’obbligatorietà degli elementi;
- **Schematron**, che impone regole semantiche, tra cui l’obbligo di descrizioni non vuote e la coerenza degli identificatori rispetto alla tassonomia di appartenenza.

Questi vincoli trasformano la tassonomia in un oggetto formalmente sorvegliato e sottratto a modifiche arbitrarie.

### 3.3 Separazione tra definizione e uso

Un principio centrale del modello è la separazione rigorosa tra definizione delle categorie interpretative e loro uso nel testo. I file testuali non sono validati contro lo schema della tassonomia, ma utilizzano le categorie esclusivamente tramite riferimenti `@ana`. Questa separazione evita la confusione tra fenomeno testuale e apparato interpretativo e garantisce la stabilità ontologica delle categorie.

---

## 4. Uso controllato della tassonomia

L’uso della tassonomia avviene attraverso l’attributo `@ana`, inteso come riferimento a categorie già dichiarate e governate. Ogni unità testuale può attivare simultaneamente più categorie appartenenti a tassonomie diverse, riflettendo la natura multidimensionale dell’interpretazione.

L’annotazione non mira a classificare il testo, ma a **rendere visibile la stratificazione ermeneutica** che presiede alla sua lettura. In questo senso, la tassonomia non riduce la complessità interpretativa, ma la esplicita e la rende governabile.

---

## Conclusione

La tassonomia interpretativa prudenziale qui presentata propone un modello alternativo all’annotazione tematica tradizionale. Formalizzando l’interpretazione come livello ontologico separato e governato, il modello consente di affrontare testi ad alta densità ermeneutica senza rinunciare al controllo metodologico.

La TEI è utilizzata non solo come linguaggio di rappresentazione del testo, ma come **strumento di governo dell’atto interpretativo**. In questo senso, la tassonomia non è un complemento dell’edizione, ma una sua condizione epistemica dichiarata.