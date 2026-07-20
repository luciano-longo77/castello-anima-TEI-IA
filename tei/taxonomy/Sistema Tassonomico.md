# Sistema Tassonomico del modello TEI interpretativo

**Castello dell'anima – Teresa di San Geronimo**

Questo documento descrive in modo **formale, normativo e vincolante** il sistema di tassonomie adottato per l'annotazione semantica del manoscritto autografo *Castello dell'anima* (Palermo, BCP, ms. 2 Qq E 29).

Il modello è progettato per rappresentare in modo **computabile**, **interrogabile** e **filologicamente auditabile** la dinamica prudenziale, retorica e dottrinale della scrittura mistica tardo‑seicentesca sottoposta a sorveglianza inquisitoriale.

Il sistema tassonomico qui descritto costituisce il **core semantico** dell'edizione digitale e governa l'uso dell'attributo `@ana` nel corpus TEI.

## Indice

1. [Principi generali del modello](#1-principi-generali-del-modello)
   - 1.1 [Stack di Validazione (componenti del pacchetto)](#11-stack-di-validazione-componenti-del-pacchetto)
2. [Assi interpretativi del sistema](#2-assi-interpretativi-del-sistema)
   - 2.1 [Asse fenomenologico](#21-asse-fenomenologico)
   - 2.2 [Asse prudenziale](#22-asse-prudenziale)
   - 2.3 [Asse strutturale ed esplicativo](#23-asse-strutturale-ed-esplicativo)
3. [Tassonomie operative (core)](#3-tassonomie-operative-core)
4. [Uso dell'attributo `@ana`](#4-uso-dellattributo-ana)
5. [Indice composito N–A–F](#5-indice-composito-naf)
6. [Querying (XPath/XQuery – esempi)](#6-querying-xpathxquery--esempi)
7. [Validazione e setup ambientale](#7-validazione-e-setup-ambientale)
   - 7.1 [Configurazione oXygen XML Editor](#71-configurazione-oxygen-xml-editor)
   - 7.2 [Vincoli Schematron e ODD](#72-vincoli-schematron-e-odd)
8. [Come citare questo lavoro](#8-come-citare-questo-lavoro)
9. [Contribuzione e workflow](#9-contribuzione-e-workflow)
10. [Statuto del documento](#10-statuto-del-documento)

***

## 1. Principi generali del modello

Il sistema tassonomico si fonda sui seguenti principi strutturali:

*   Ogni valore dell'attributo `@ana` fa riferimento in modo **esplicito e univoco** a una categoria dichiarata in una tassonomia all'interno di `classDecl`.
*   Ogni tassonomia definisce **un asse interpretativo distinto**, non riducibile agli altri.
*   Le tassonomie sono **ortogonali ma non indipendenti**: la loro combinazione è regolata da vincoli interpretativi espliciti.
*   Non è ammessa l'introduzione di valori annotativi che non siano dichiarati nelle tassonomie.

Il modello non è ontologico in senso rigido, ma costituisce una **ontologia interpretativa leggera**, progettata per garantire:

*   interrogabilità computazionale (XPath, XQuery);
*   trasparenza metodologica;
*   auditabilità filologica e riproducibilità dell'annotazione.

### 1.1 Stack di Validazione (componenti del pacchetto)

L'integrità del sistema è garantita da una catena di validazione a tre livelli inclusa nella repository:

1.  **Sorgente (ODD):** definizione astratta e documentazione tecnica in `taxonomy.odd`.
2.  **Struttura (Relax NG):** validazione grammaticale e controllo di integrità strutturale tramite `schema/taxonomy-rng.rng`.
3.  **Logica (Schematron):** vincoli semantici avanzati e coerenza dei prefissi/relazioni tramite `schema/taxonomy-sch.sch`.

***

## 2. Assi interpretativi del sistema

Il modello si articola in **tre assi interpretativi principali**, ciascuno dei quali corrisponde a un diverso livello di descrizione del testo.

### 2.1 Asse fenomenologico

Descrive **ciò di cui il testo parla** e il modo in cui il contenuto mistico e dottrinale viene articolato nel discorso.

Tassonomie coinvolte:

*   `func` — funzioni retoriche e discorsive;
*   `mystic_state` — stati mistici e fenomenologici;
*   `relation` — relazioni concettuali e intertestuali.

### 2.2 Asse prudenziale

Descrive **come il testo gestisce il rischio dottrinale** in un contesto storico‑inquisitoriale.

Tassonomie coinvolte:

*   `risk` — condizioni storiche e teologiche di esposizione;
*   `operation` — operazioni discorsive concrete (attenuatio, precisatio, declaratio, riequilibrio);
*   `exposition` — livello di esposizione dottrinale.

**Vincolo interpretativo fondamentale**
Le categorie `func` relative alla gestione del rischio presuppongono sempre una categoria di `operation` corrispondente:

*   `func` risponde a: *perché il testo interviene*;
*   `operation` risponde a: *come il testo interviene*.

> **Nota:** questo vincolo è al momento solo prosa normativa; non esiste un `constraintSpec` Schematron che lo verifichi automaticamente.
Va rispettato in fase di annotazione editoriale.

### 2.3 Asse strutturale ed esplicativo

Descrive **dove** un segmento agisce nel discorso e **con quale forza interpretativa**.

Tassonomie coinvolte:

*   `impact` — impatto interpretativo;
*   `phase` — fase discorsiva.

***

## 3. Tassonomie operative (core)

```xml
<classDecl>
  <taxonomy xml:id="func"/>
  <taxonomy xml:id="relation"/>
  <taxonomy xml:id="impact"/>
  <taxonomy xml:id="risk"/>
  <taxonomy xml:id="mystic_state"/>
  <taxonomy xml:id="operation"/>
  <taxonomy xml:id="exposition"/>
  <taxonomy xml:id="phase"/>
</classDecl>
```

**Elenco completo dei valori ammessi**
L'elenco delle `<category>` per ciascuna tassonomia è definito nel file **`./tassonomia-gh.xml`**, che costituisce la **fonte normativa primaria** dei valori annotativi.

***

## 4. Uso dell'attributo `@ana`

In TEI P5 l'attributo `@ana` ha tipo **pointer** e **deve contenere URI o fragment identifier** che puntano alle categorie tassonomiche (es. riferimenti interni `#xml-id`).

L'attributo `@ana` può contenere **valori multipli**, separati da spazi, ciascuno riferito a una categoria distinta.

### Esempio (forma TEI‑compliant)

```xml
<seg ana="#pedagogia #relation-mistica-attiva-meditazione #risk-dottrinale #operation-delimitazione #impact-high #phase-mediana">
```

> **Nota sui prefissi:** `func` è l'unico asse esente dal vincolo di prefisso (§7.2) — le sue categorie di primo livello (`legittimazione`, `pedagogia`, `rischio`, `ethos`) non portano il prefisso `func-`. Tutte le altre tassonomie richiedono che l'`xml:id` inizi col prefisso della tassonomia radice (es. `risk-dottrinale`, non `dottrinale` né `risk-risk-dottrinale`).

***

## 5. Indice composito N–A–F

L'indice **N–A–F** è un indicatore interpretativo composito utilizzato in fase analitica:

*   **N** = Necessità interpretativa
*   **A** = Ambiguità semantica
*   **F** = Funzione prudenziale

L'indice non costituisce una tassonomia, ma un **valore derivato** calcolato a partire da `risk`, `impact` e dalla densità delle `operation`.

***

## 6. Querying (XPath/XQuery – esempi)

> **Nota:** le query presuppongono che il namespace TEI (`xmlns:tei="http://www.tei-c.org/ns/1.0"`) sia correttamente dichiarato nel processore XPath/XQuery e che `@ana` contenga **pointer** (`#xml-id`).

Segmenti ad alto rischio con operazione attenuativa:

```xpath
//tei:seg[matches(@ana, '\#risk-dottrinale') and matches(@ana, '\#operation-attenuatio')]
```

***

## 7. Validazione e setup ambientale

### 7.1 Configurazione oXygen XML Editor

Per attivare la validazione automatica (strutturale e logica) durante l'editing, il file `tassonomia-gh.xml` deve puntare agli schemi locali inclusi nel pacchetto:

```xml
<?xml-model href="schema/taxonomy-rng.rng"
            type="application/xml"
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="schema/taxonomy-sch.sch"
            type="application/xml"
            schematypens="http://purl.oclc.org/dsdl/schematron"?>
```

### 7.2 Vincoli Schematron e ODD

Il sistema impone controlli rigorosi per prevenire derive ermeneutiche:

*   **Coerenza dei riferimenti:** `@ana` deve puntare a categorie esistenti (`#xml-id`) definite in `tassonomia-gh.xml`.
*   **Prefissi:** per tutte le tassonomie, le categorie con trattino rispettano il prefisso della tassonomia radice a cui appartengono (verificato contro l'antenato `taxonomy` più vicino, non contro il padre immediato — questo permette a nodi‑contenitore come `risk-dottrinale` di avere figli come `risk-quietismo` senza doppia prefissazione); l'asse `func` è **esente** per consentire la convergenza di sotto‑assi funzionali (`#rischio-*`, `#ethos-*`, `#pedagogia-*`).
*   **Presenza e non vacuità di `catDesc`:** ogni categoria deve dichiarare una `catDesc` non vuota.
*   **Unicità degli `xml:id`:** verificata anche via Schematron come rete di sicurezza aggiuntiva, poiché la ridefinizione locale dell'attributo `xml:id` su `taxonomy`/`category` può non preservare il vincolo nativo `data type="ID"` nella compilazione RelaxNG.
*   **Integrità strutturale:** lo schema Relax NG garantisce la correttezza grammaticale e l'obbligatorietà dei componenti.

***

## 8. Come citare questo lavoro

Se utilizzi questo sistema tassonomico o i file di validazione nella tua ricerca, cita come segue:

**Citazione bibliografica**

> Luciano Longo, *Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima di Teresa di San Geronimo*, 2026, Repository GitHub: (https://github.com/luciano-longo77/castello-anima-TEI-IA).

**Formato BibTeX**

```bibtex
@software{longo_tassonomia_2026,
  author       = {Longo, Luciano},
  title        = {Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/USERNAME/NOME-REPO}}
}
```

***

## 9. Contribuzione e workflow

Ogni modifica al sistema tassonomico deve avvenire tramite **Pull Request** e includere:

1.  Aggiornamento di `tassonomia-gh.xml`.
2.  Rigenerazione dello schema `.rng` (ed eventualmente dello `.sch`) a partire dal file `taxonomy.odd`.
3.  Aggiornamento del presente README per riflettere i nuovi assi o categorie — inclusi eventuali aggiornamenti alla mappatura a tre assi interpretativi (§2) se una nuova tassonomia viene introdotta.

***

## 10. Statuto del documento

Questo README ha **statuto normativo**. Ogni divergenza tra questo documento e i file XML della repository costituisce **errore del modello**.

***
**Licenza:** Tutti i contenuti del repository sono rilasciati sotto licenza **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
Vedi il file **SPDX-License-Identifier: CC-BY-4.0** per i dettagli completi.
