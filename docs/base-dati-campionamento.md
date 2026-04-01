# 📚 **Base dati per il campionamento**

## **Intertestualità sotto sorveglianza: un modello TEI+IA per *Il Castello dell’anima* di suor Teresa di San Geronimo**

***

## 📝 **Introduzione**

Questo documento descrive la struttura del *dataset di campionamento* utilizzato per l’edizione digitale e l’analisi computazionale del ***Castello dell’anima*** di suor Teresa di San Geronimo.

Il dataset è progettato per essere:

*   **chiaro** → organizzato e consultabile
*   **riusabile** → pronto per analisi, encoding e IA
*   **trasparente** → motivazioni esplicite per ciascuna scelta
*   **interoperabile** → integrabile con il file TEI P5 e la pipeline IA

Il progetto combina:

*   **codifica TEI P5**
*   **analisi retorico‑dottrinale delle glosse**
*   **intertestualità strutturale**
*   **generazione controllata di varianti IA** (–CIT, +CIT’, +GLOSSA\_IA)

Il campionamento copre i capitoli più rilevanti dei tre libri dell’opera:  
segmenti ad alta sensibilità dottrinale, zone con densa intertestualità, e passaggi caratterizzati da glosse autoriali e dispositivi prudenziali.

Il documento contiene inoltre:

*   un’**authority list** delle citazioni bibliche, liturgiche, patristiche, mistiche
*   una **matrice di 30 glosse tipizzate** (funzione → rischio → valore)
*   una **sintesi dell’intertestualità strutturale** dell’opera

***

## 📁 **Dataset – Castello dell’anima (TEI+IA)**

*Documentazione del campione, authority list e glosse tipizzate.*

Le citazioni e i riferimenti al testo derivano da:  
***Il Castello dell’anima* di suor Teresa di San Geronimo. Edizione critica. Palermo: Centro Studi, 2024.**

Il dataset include:

*   ✅ capitoli selezionati dei tre libri
*   ✅ criteri filologici e dottrinali della selezione
*   ✅ authority list delle citazioni
*   ✅ glosse tipizzate con funzione/rischio
*   ✅ quadro dell’intertestualità strutturale

***

## 🔗 **Interoperabilità**

Il dataset è progettato per interagire con:

1.  **File TEI** – `Castello dell’anima – base.xml`
2.  **Pipeline IA controllata** – varianti ±CIT, +GLOSSA\_IA
3.  **Guida TEI-driven** del progetto

***

## 🎯 **Scopo del documento**

1.  Definire il dataset di campionamento per l’analisi TEI+IA.
2.  Motivare la selezione dei capitoli in base a:
    *   sensibilità dottrinale
    *   densità intertestuale
    *   presenza di glosse/dispositivi prudenziali
    *   utilità per esperimenti computazionali
3.  Fornire una **authority list** unificata.
4.  Fornire una **matrice di 30 glosse**.
5.  Documentare i principi di **intertestualità sorvegliata** utili per l’encoding TEI.

***

## 🔄 **Versioning**

| Versione | Data           | Autore            |
| -------- | -------------- | ----------------- |
| v0.0     | 2026-03-09     | Luciano Longo     |
| v1.1     | 2026-03-25     | Luciano Longo     |
| **v1.2** | **2026-04-01** | **Luciano Longo** |

***

## 💻 **Uso del documento**

Il documento, collocato in `docs/`, serve a:

*   accompagnare il file TEI
*   supportare la generazione di varianti IA
*   guidare query e pattern TEI
*   consentire la replicazione degli esperimenti

***

## 🗂️ **Struttura del dataset**

1.  Dataset → capitoli selezionati e motivazioni
2.  Razionale metodologico della selezione
3.  Authority list delle citazioni
4.  Citazioni classificate per funzione/rischio
5.  Glosse tipizzate (30 esempi)
6.  Intertestualità strutturale
7.  Allegati e riferimenti critici

***

# 1️⃣ **Dataset: Capitoli selezionati**

Criteri:

*   sensibilità dottrinale
*   densità intertestuale
*   presenza di glosse
*   utilità per esperimenti TEI+IA (–CIT, +CIT’, +GLOSSA\_IA)

***

## 📘 LIBRO I — *Anime principianti*

**Funzione:** pedagogia + ethos

| Capitolo | Titolo                                                                  | Motivo della selezione                                 |
| -------- | ----------------------------------------------------------------------- | ------------------------------------------------------ |
| I.1–2    | *Si tratta della miseria humana / Come il mondo è una continua guerra…* | Costruzione dell’ethos; nessuna citazione → **+CIT**   |
| I.5      | *Virtù dell’humiltà*                                                    | Citazione salmica → segmento **legittimante**          |
| I.6      | *Virtù dell’obbedienza*                                                 | Citazione cristologica → perfetto per **–CIT / +CIT’** |

***

## 📗 LIBRO II — *Anime proficienti*

**Funzione:** discernimento + rischio dottrinale

| Capitolo   | Titolo                                                    | Motivo                                      |
| ---------- | --------------------------------------------------------- | ------------------------------------------- |
| II.1–2     | *Dispositione dell’anima*                                 | Baseline dottrinale                         |
| II.8 (a–d) | *Oratione d’unione*                                       | Nodo critico → **+GLOSSA\_IA**              |
| II.9a–b    | *Travagli delle anime*                                    | Casistica mistica → spostamenti citazionali |
| II.10b     | *Segni per conoscere se la gratia è di Dio o del Demonio* | Segmento ad alta sensibilità                |

***

## 📕 LIBRO III — *Anime perfette*

**Funzione:** mistica alta + glosse difensive

| Capitolo | Titolo                                              | Motivo                                          |
| -------- | --------------------------------------------------- | ----------------------------------------------- |
| III.8    | *Cella secreta / matrimonio spirituale*             | Ricchissimo di glosse e citazioni stabilizzanti |
| III.9a–b | *Passaggio alla cella di Dio / Stato di solitudine* | Confronto presenza/assenza glosse               |
| III.12   | *Stato d'otio*                                      | Nessuna glossa → **+GLOSSA\_IA**                |
| III.14   | *Santa ignoranza*                                   | Elevato rischio teologico                       |
| III.24   | *Non si medita la passione…*                        | Citazione semiliturgica pericolosa              |
| III.34   | *Trasformatione totale*                             | Culmine teologico                               |
| III.40   | *Ultima cella dell’anima*                           | Fine del ciclo ascensionale                     |

***

# 2️⃣ **Razionale della selezione**

### Criteri principali

1.  **Sensibilità dottrinale**
2.  **Densità intertestuale**
3.  **Comparabilità strutturale** tra i libri

### Note per libro

*   **Libro I** → costruzione ethos; capitoli privi di citazioni per test di aggiunta.
*   **Libro II** → zone di discernimento e rischio moliniano.
*   **Libro III** → mistica alta, glosse difensive sistematiche.

***

# 3️⃣ **Citazioni utili alla base dati**

Elenco completo già normalizzato per riferimenti biblici/liturgici.

(Non lo ripeto qui integralmente, in README basta una sintesi; la versione lunga rimane nella cartella *docs/*.)

***

# 4️⃣ **Classificazione funzionale delle citazioni**

*   **Legittimazione dottrinale**
*   **Ancoraggio cristologico**
*   **Marcatori di sofferenza / notte mistica**
*   **Citazioni sponsali**
*   **Sigilli dottrinali (rifinitura)**
*   **Sapienziali / metafisiche**
*   **Patristiche e mistiche**

***

# 5️⃣ **Glosse tipizzate (30 esempi)**

Ogni glossa è classificata per:

*   **funzione retorico‑dottrinale (TEI)**
*   **rischio ermeneutico disinnescato**
*   **valore per la pipeline IA**

Categorie principali:

*   Attenuatio
*   Correctio
*   Declaratio
*   Explicatio
*   Esperienziali
*   Analogia/metafora
*   Potenze/volontà
*   Guida spirituale
*   Sicurezza mistica
*   Trasformazione

***

# 6️⃣ **Intertestualità strutturale**

Sintesi delle principali reti intertestuali:

*   rapporto con Teresa d’Ávila → rovesciamento del modello del castello
*   tradizione giovannea → notte mistica, sospensione potenze
*   metafore mistiche femminili → calamita, attrazione
*   consonanze con Molinos → intertestualità liminare
*   genealogie agiografiche → autorità femminile legittimante
*   intertestualità culturale → *amor con amor si paga*
*   intertesto esperienziale → “non parlo senza l’esperienza”

***

# 📎 **Appendice — Authority File**

Include:

1.  **Biblia – Vulgata / Nova Vulgata**
2.  **Liturgia Romana / Te Deum**
3.  **Patristica (Ignazio, tradizione esegetica)**
4.  **Mistica post-tridentina (Carmelo, Pazzi, Helfta)**
5.  **Agiografia femminile (Caterina, Rosalia, Chiara, Geltrude)**

(Le tabelle complete sono riportate in versione estesa nel file principale del dataset.)
