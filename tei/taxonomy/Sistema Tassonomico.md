# Sistema Tassonomico del modello TEI interpretativo
**Castello dell'anima – Teresa di San Geronimo**

---
Questo documento descrive in modo **formale, normativo e vincolante** il sistema di tassonomie adottato per l'annotazione semantica del manoscritto autografo *Castello dell'anima* (Palermo, BCP, ms. 2 Qq E 29, sec. XVII ex.). Il modello è progettato per rappresentare in modo **computabile**, **interrogabile** e **filologicamente auditabile** la dinamica prudenziale, retorica e dottrinale della scrittura mistica tardomoderna.Il sistema tassonomico qui descritto costituisce il **core semantico** dell'edizione digitale e governa l'uso dell'attributo `@ana` nel corpus TEI.
---
## Indice
1. [Principi generali del modello] (#1-principi-generali-del-modello)   
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

## 1. Principi generali del modello
Il sistema tassonomico si fonda sui seguenti principi strutturali: 
* Ogni valore dell'attributo `@ana` fa riferimento in modo **esplicito e univoco** a una categoria dichiarata in una tassonomia all'interno di `classDecl`.
* Ogni tassonomia definisce **un asse interpretativo distinto**, non riducibile agli altri.
* Le tassonomie sono **ortogonali ma non indipendenti**: la loro combinazione è regolata da vincoli interpretativi espliciti, alcuni **enforced da Schematron** (automatico) e altri **gestiti in fase editoriale** (manuale).

Non è ammessa l'introduzione di valori annotativi che non siano dichiarati nelle tassonomie. Il modello non è ontologico in senso rigido, ma costituisce una **ontologia interpretativa leggera**, progettata per garantire: 
* interrogabilità computazionale (XPath, XQuery);
* trasparenza metodologica;
* auditabilità filologica e riproducibilità dell'annotazione.

### 1.1 Stack di Validazione (componenti del pacchetto)
L'integrità del sistema è garantita da una catena di validazione a tre livelli inclusa nella repository:
1.  **Sorgente (ODD):** definizione astratta e documentazione tecnica in 
`tei/taxonomy/schema/taxonomy-odd.odd`.
2.  **Struttura (Relax NG):** validazione grammaticale e controllo di integrità strutturale tramite 
`tei/taxonomy/schema/taxonomy-rng.rng` (generato da ODD).
3.  **Logica (Schematron):** vincoli semantici avanzati e coerenza dei prefissi/relazioni tramite 
`tei/taxonomy/schema/taxonomy-sch.sch` (generato da ODD, queryBinding=\"xslt2\").

**Flusso di generazione**: 
`taxonomy.odd` → Roma (oXygen) → `taxonomy-rng.rng` + `taxonomy-sch.sch`.

## 2. Assi interpretativi del sistema

Il modello si articola in **tre assi interpretativi principali**, ciascuno dei quali corrisponde a un diverso livello di descrizione del testo.

### 2.1 Asse fenomenologico
Descrive **ciò di cui il testo parla** e il modo in cui il contenuto mistico e dottrinale viene articolato nel discorso.Tassonomie coinvolte:
* `func` — funzioni retoriche e discorsive;
* `mystic_state` — stati mistici e fenomenologici;
* `relation` — relazioni concettuali e intertestuali.

### 2.2 Asse prudenziale
Descrive **come il testo gestisce il rischio dottrinale** in un contesto storico‑inquisitoriale.
Tassonomie coinvolte:
*   `risk` — condizioni storiche e teologiche di esposizione;
*   `operation` — operazioni discorsive concrete (delimitazione, attenuatio, precisatio, declaratio, riequilibrio);
*   `exposition` — livello di esposizione dottrinale.

### 2.3 Asse strutturale ed esplicativo

Descrive **dove** un segmento agisce nel discorso e **con quale forza interpretativa**. Tassonomie coinvolte:
*   `impact` — impatto interpretativo;
*   `phase` — fase discorsiva.## 3. Tassonomie operative (core)
```xml<classDecl>  <taxonomy xml:id=\"func\"/>
<taxonomy xml:id=\"relation\"/>
<taxonomy xml:id=\"impact\"/>
<taxonomy xml:id=\"risk\"/>
<taxonomy xml:id=\"mystic_state\"/>
<taxonomy xml:id=\"operation\"/>
<taxonomy xml:id=\"exposition\"/>
<taxonomy xml:id=\"phase\"/></classDecl>
```

**Elenco completo dei valori ammessi**
L'elenco delle `<category>` per ciascuna tassonomia è definito nel file 
**`./tassonomia-gh.xml`**, che costituisce la **fonte normativa primaria** dei valori annotativi.

## 4. Uso dell'attributo `@ana`
In TEI P5 l'attributo `@ana` ha tipo **pointer** e **deve contenere URI o fragment identifier** che puntano alle categorie tassonomiche (es. riferimenti interni `#xml-id`).
L'attributo `@ana` può contenere **valori multipli**, separati da spazi bianchi (whitespace), ciascuno riferito a una categoria distinta.

### Esempio (forma TEI‑compliant)
```xml<seg ana=\"#pedagogia
#relation-mistica-attiva-meditazione
#risk-dottrinale
#operation-delimitazione
#impact-high #phase-mediana\">    
Testo annotato del manoscritto...</seg>
```

### 4.1 Regole sui prefissi
**Regola generale**: per tutte le tassonomie, le categorie che portano il trattino (`-`) devono iniziare con il prefisso della tassonomia radice a cui appartengono.

**Esempio**:
- Tassonomia `risk` 
→ categorie come `risk-dottrinale`, `risk-quietismo`, `risk-panteismo`, `risk-impeccabilita`, `risk-ambiguita` (prefisso `risk-` obbligatorio)- Tassonomia `operation` 
→ categorie come `operation-delimitazione`, `operation-attenuatio`, `operation-precisatio`, `operation-declaratio`, `operation-riequilibrio` (prefisso `operation-` obbligatorio)

- Tassonomia `exposition` 
→ categorie come `exposition-low`, `exposition-medium`, `exposition-high`, `exposition-critical` (prefisso `exposition-` obbligatorio)

**Eccezione**: l'asse `func` è **esente dal vincolo di prefisso tassonomia**. 
Le sue categorie di primo livello non portano il prefisso `func-`:
- ✅ `legittimazione`, `pedagogia`, `rischio`, `ethos` (NO prefisso `func-`).

Le loro sottocategorie seguono la gerarchia naturale e il prefisso della categoria madre:
- ✅ `legittimazione-biblica`, `legittimazione-liturgica`, `legittimazione-tradizione`
- ✅ `pedagogia-introduzione`, `pedagogia-discernimento`, `pedagogia-esemplificazione`
- ✅ `rischio-attenuatio`, `rischio-precisatio`, `rischio-declaratio`
- ✅ `ethos-umilta`, `ethos-esperienza`, `ethos-obbedienza`

**Implementazione**: 
il vincolo è **enforced dal file `taxonomy-sch.sch`** mediante la regola Schematron `category-prefix-consistency`.

### 4.2 Marcatori trasversali: `phase-critical`
La categoria `phase-critical` della tassonomia `phase` è un **marcatore trasversale**, non posizionale.

**Significato**: segnala che il segmento è **teologicamente delicato** indipendentemente da dove si colloca nella sequenza discorsiva (introduzione, sezione mediana, o conclusione).
**Regola di applicazione**: quando un passaggio riceve `#phase-critical`, deve ricevere **contemporaneamente** uno e uno solo tra:
- `#phase-introduction` (se il passaggio critico si trova nella fase introduttiva)
- `#phase-mediana` (se il passaggio critico si trova in sezione centrale)
- `#phase-conclusive` (se il passaggio critico si trova in conclusione)

**Esempio corretto**:

```
xml
<seg ana=\"#phase-critical #phase-mediana #exposition-critical #risk-quietismo\">
Testo con problematiche teologiche in sezione centrale...</seg>
```

**Esempio scorretto** (manca fase posizionale):
```xml
<seg ana=\"#phase-critical #exposition-critical #risk-quietismo\">    
<!-- Errore: manca fase posizionale (introduction/mediana/conclusive) -->
</seg>
```

**Implementazione**: il vincolo è **gestito in fase editoriale** (prosa normativa). 
Un futuro constraint Schematron può essere aggiunto per enforcing automatico (vedi §8.3).

## 5. Indice composito N–A–F
L'indice **N–A–F** è un indicatore interpretativo composito utilizzato in fase analitica per quantificare l'impatto semantico di una occorrenza annotata.*   
**N** = Necessità interpretativa*   
**A** = Ambiguità semantica*   
**F** = Funzione prudenzialeL'indice non costituisce una tassonomia, ma un **valore derivato** calcolato a partire dai tre assi.

### 5.1 Formula di calcolo
La formula N–A–F è calcolata come segue:

**N (Necessità interpretativa)**: 
funzione della densità di `#risk-*` presenti nel `@ana`.- Se `@ana` contiene 1+ categoria da `risk`: N = 1- Altrimenti: N = 0

**A (Ambiguità semantica)**: 
funzione della specifica categoria di rischio dottrinale.- `risk-ambiguita` → A = 1.0- `risk-dottrinale`, `risk-quietismo`, `risk-panteismo`, `risk-impeccabilita` → A = 0.7- Altrimenti: A = 0

**F (Funzione prudenziale)**: 
funzione della densità di `#operation-*` presenti nel `@ana`.
- Se `@ana` contiene 1+ categoria da `operation`: F = 1
- Altrimenti: F = 0

**Valore composito N–A–F**:
```
NAF_score = (N × 0.3) + (A × 0.4) + (F × 0.3)
```

**Mapping a categorie `#impact-*`**:
- N–A–F ≥ 0.7 → `#impact-critical` o `#impact-high`
- 0.4 ≤ N–A–F < 0.7 → `#impact-medium`
-  N–A–F < 0.4 → `#impact-low`
**Nota**: il calcolo è **indicativo e non vincolante** in fase di annotazione manuale. 
L'annotatore assegna `#impact-*` secondo il proprio giudizio interpretativo; il valore N–A–F servirà come **controllo di coerenza** in fase di revisione e validazione corpus.

## 6. Vincoli semantici cross-assiali
Alcuni vincoli collegano categorie provenienti da assi diversi. Di seguito sono elencati i vincoli **cross-assiali** principali.

### 6.1 Corrispondenza `rischio-*` ↔ `operation-*`
**Regola semantica fondamentale**: 
Ogni categoria della tassonomia `func` che appartenga al ramo `rischio` (cioè `rischio-attenuatio`, `rischio-precisatio`, `rischio-declaratio`) presuppone logicamente una categoria corrispondente dalla tassonomia `operation`.

| Categoria `func`     | Categoria `operation` corrispondente |
|----------------------|--------------------------------------|
| `rischio-attenuatio` | `operation-attenuatio`               |
| `rischio-precisatio` | `operation-precisatio`               |
| `rischio-declaratio` | `operation-declaratio`               |

**Significato**:
- `rischio-attenuatio` descrive la **strategia autoriale** di mitigazione di un enunciato rischioso (perché l'autrice interviene)
- `operation-attenuatio` descrive il **meccanismo discorsivo concreto** (glossa, precisazione, parentetica) tramite cui la mitigazione avviene (come il testo interviene)

**Regola di applicazione**: 
Un segmento che riceve `#rischio-attenuatio` deve ricevere anche `#operation-attenuatio`. Analogamente per `precisatio` e `declaratio`.

**Esempio corretto**:
```
xml<seg ana=\"#rischio-attenuatio #operation-attenuatio #risk-dottrinale #legittimazione\">    
Glosse esplicative che smorzano formulazioni rischiose...</seg>
```

**Esempio scorretto** (manca operazione corrispondente):
```
xml<seg ana=\"#rischio-attenuatio #legittimazione\">
<!-- Errore: manca #operation-attenuatio -->
</seg>
```
**Implementazione**: 
il vincolo è **formalmente dichiarato ma non ancora codificato in Schematron** (vedi §8.3). 
È gestito mediante **linee guide editoriali** e **revisione manuale** in fase di annotazione.

**Status**: Un futuro aggiornamento a `taxonomy-sch.sch` dovrà includere una regola Schematron che enforci questa corrispondenza automaticamente.

## 7. Querying (XPath/XQuery – esempi)

>**Nota:** le query presuppongono che il namespace TEI (`xmlns:tei=\"http://www.tei-c.org/ns/1.0\"`) sia correttamente dichiarato nel processore XPath/XQuery e che `@ana` contenga **pointer** (fragment identifier con `#`).

### Segmenti ad alto rischio con operazione attenuativa

```
xpath//tei:seg[matches(@ana, '#risk-dottrinale') and matches(@ana, '#operation-attenuatio')]
```

### Segmenti marcati come critical in fase mediana

```
xpath//tei:seg[matches(@ana, '#phase-critical') and matches(@ana, '#phase-mediana')]
```

### Segmenti che ricevono estrategia di rischio (per validazione)
```
xpath//tei:seg[matches(@ana, '#rischio-')]
```

### Tutti i segmenti che violano il vincolo `rischio-
*` ↔ `operation-*` (per validazione manuale)
```
xpath//tei:seg[matches(@ana, '#rischio-attenuatio') and not(matches(@ana, '#operation-attenuatio'))]
```

## 8. Validazione e setup ambientale
### 8.1 Configurazione oXygen XML Editor
Per attivare la validazione automatica (strutturale e logica) durante l'editing del corpus TEI, il file corpus deve referenziare gli schemi locali inclusi nel pacchetto:

```xml
<?xml-model href=\"../../tei/taxonomy/schema/taxonomy-rng.rng\" type=\"application/xml\"            
schematypens=\"http://relaxng.org/ns/structure/1.0\"?><?xml-model href=\"../../tei/taxonomy/schema/taxonomy-sch.sch\" type=\"application/xml\"            
schematypens=\"http://purl.oclc.org/dsdl/schematron\"?>
```
(Regolare il percorso relativo `href` in base alla posizione del corpus rispetto al directory `tei/taxonomy/schema/`.)

### 8.2 Vincoli Schematron (automatici)
Il sistema impone controlli rigorosi via Schematron (definiti in `taxonomy-sch.sch`):
*   **`category-catdesc-present`**: Ogni `<category>` deve contenere un `<catDesc>`.
*   **`category-catdesc-not-empty`**: Il contenuto di ogni `<catDesc>` non può essere vuoto (biancheria-only).
*   **`category-prefix-consistency`**: Per tutte le tassonomie tranne `func`, le categorie con trattino rispettano il prefisso della tassonomia radice (es. `risk-*`, `operation-*`, `exposition-*`, etc.).*
*   **`taxonomy-category-xmlid-unique`**: Unicità globale di `@xml:id` su tutti gli elementi `<taxonomy>` e `<category>` (rete di sicurezza per bug RNG).

### 8.3 Vincoli editoriali (prosa normativa)
I seguenti vincoli sono **gestiti manualmente in fase di annotazione** e **non yet enforced da Schematron**:*   

**Coerenza `@ana` → categorie**: `@ana` deve puntare a categorie effettivamente definite in `tassonomia-gh.xml` (verificabile via XPath, ma non enforced da schema RNG/Schematron).*   

**Corrispondenza `rischio-*` ↔ `operation-*`** (vedi §6.1): quando un segmento riceve `#rischio-attenuatio` (o `precisatio`, `declaratio`), deve ricevere la correspondente `#operation-attenuatio` (o `precisatio`, `declaratio`).*  
 
 **Compatibilità `phase-critical`** (vedi §4.2): 
 `#phase-critical` deve comparire insieme a una fase posizionale (`#phase-introduction`, `#phase-mediana`, o `#phase-conclusive`).

**Prossimi passi**: questi tre vincoli vanno convertiti in regole Schematron e inclusi in `taxonomy-sch.sch` per automazione completa della validazione. Sono candidati per una future versione dell'ODD.

## 9. Come citare questo lavoro
Se utilizzi questo sistema tassonomico o i file di validazione nella tua ricerca, cita come segue:

**Citazione bibliografica**
> Luciano Longo, *Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima di Teresa di San Geronimo* (versione 2026), Repository GitHub: https://github.com/luciano-longo77/castello-anima-TEI-IA

**Formato BibTeX**
```bibtex@software
{longo_tassonomia_2026,  
author       = {Longo, Luciano},
title        = {Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima},  
year         = {2026},
publisher    = {GitHub},  
howpublished = {\\url{https://github.com/luciano-longo77/castello-anima-TEI-IA}},  
note         = {TEI + IA controllata}}
```


## 10. Contribuzione e workflow
Ogni modifica al sistema tassonomico deve avvenire tramite 

**Pull Request** e includere: **Aggiornamento di `tei/taxonomy/tassonomia-gh.xml`**: aggiunta/modifica di categorie o descrizioni.

**Rigenerazione dello schema** (se necessario): usare Roma (oXygen) per generare `taxonomy-rng.rng` e `taxonomy-sch.sch` a partire da `tei/taxonomy/schema/taxonomy-odd.odd`. Includere entrambi i file generati nella PR.  

**Aggiornamento del presente documento (`Sistema Tassonomico.md`)** per riflettere i nuovi assi, categorie, o vincoli, inclusi eventuali aggiornamenti alla mappatura a tre assi interpretativi (§2) se una nuova tassonomia viene introdotta.

## 11. Statuto del documento
Questo documento ha **statuto normativo**. Ogni divergenza tra questo documento e i file XML della repository (`tassonomia-gh.xml`, `taxonomy-odd.odd`, `taxonomy-rng.rng`, `taxonomy-sch.sch`) costituisce **errore del modello** e deve essere risolto prioritariamente.

**Versione corrente**: 2026-07-26 (allineamento 100% con XML e schema).

**Licenza:**
Tutti i contenuti del repository sono rilasciati sotto licenza
**Creative Commons Attribution 4.0 International (CC BY 4.0)**.
Vedi il file **SPDX-License-Identifier: CC-BY-4.0** per i dettagli completi.
