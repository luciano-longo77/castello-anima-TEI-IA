# Sistema Tassonomico del modello TEI interpretativo

**Castello dell'anima – Teresa di San Geronimo**

Questo documento descrive in modo **formale, normativo e vincolante** il sistema di tassonomie adottato per l'annotazione semantica del manoscritto autografo *Castello dell'anima* (Palermo, BCP, ms. 2 Qq E 29, sec. XVII ex.).

Il modello è progettato per rappresentare in modo **computabile**, **interrogabile** e **filologicamente auditabile** la dinamica prudenziale, retorica e dottrinale della scrittura mistica tardomoderna.

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
   - 4.1 [Regole sui prefissi](#41-regole-sui-prefissi)
   - 4.2 [Marcatori trasversali: `phase-critical`](#42-marcatori-trasversali-phase-critical)
5. [Indice composito N–A–F](#5-indice-composito-naf)
   - 5.1 [Formula di calcolo](#51-formula-di-calcolo)
6. [Vincoli semantici cross-assiali](#6-vincoli-semantici-cross-assiali)
   - 6.1 [Corrispondenza `rischio-*` ↔ `operation-*`](#61-corrispondenza-rischio--operation)
7. [Querying (XPath/XQuery – esempi)](#7-queryingxpathxquery--esempi)
8. [Validazione e setup ambientale](#8-validazione-e-setup-ambientale)
   - 8.1 [Configurazione oXygen XML Editor](#81-configurazione-oxygen-xml-editor)
   - 8.2 [Vincoli Schematron (automatici)](#82-vincoli-schematron-automatici)
   - 8.3 [Vincoli editoriali (prosa normativa)](#83-vincoli-editoriali-prosa-normativa)
9. [Come citare questo lavoro](#9-come-citare-questo-lavoro)
10. [Contribuzione e workflow](#10-contribuzione-e-workflow)
11. [Statuto del documento](#11-statuto-del-documento)

***

## 1. Principi generali del modello

Il sistema tassonomico si fonda sui seguenti principi strutturali:

*   Ogni valore dell'attributo `@ana` fa riferimento in modo **esplicito e univoco** a una categoria dichiarata in una tassonomia all'interno di `classDecl`.
*   Ogni tassonomia definisce **un asse interpretativo distinto**, non riducibile agli altri.
*   Le tassonomie sono **ortogonali ma non indipendenti**: la loro combinazione è regolata da vincoli interpretativi espliciti, alcuni **enforced da Schematron** (automatico) e altri **gestiti in fase editoriale** (manuale).
*   Non è ammessa l'introduzione di valori annotativi che non siano dichiarati nelle tassonomie.

Il modello non è ontologico in senso rigido, ma costituisce una **ontologia interpretativa leggera**, progettata per garantire:

*   interrogabilità computazionale (XPath, XQuery);
*   trasparenza metodologica;
*   auditabilità filologica e riproducibilità dell'annotazione.

### 1.1 Stack di Validazione (componenti del pacchetto)

L'integrità del sistema è garantita da una catena di validazione a tre livelli inclusa nella repository:

1.  **Sorgente (ODD):** definizione astratta e documentazione tecnica in `tei/taxonomy/schema/taxonomy-odd.odd`.
2.  **Struttura (Relax NG):** validazione grammaticale e controllo di integrità strutturale tramite `tei/taxonomy/schema/taxonomy-rng.rng` (generato da ODD).
3.  **Logica (Schematron):** vincoli semantici avanzati e coerenza dei prefissi/relazioni tramite `tei/taxonomy/schema/taxonomy-sch.sch` (generato da ODD, queryBinding="xslt2").

**Flusso di generazione**: `taxonomy.odd` → Roma (oXygen) → `taxonomy-rng.rng` + `taxonomy-sch.sch`.

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
*   `operation` — operazioni discorsive concrete (delimitazione, attenuatio, precisatio, declaratio, riequilibrio);
*   `exposition` — livello di esposizione dottrinale.

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
