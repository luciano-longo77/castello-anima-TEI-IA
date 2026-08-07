# Sistema Tassonomico
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

## Abstract
Questo documento descrive in modo **formale** il sistema di tassonomie adottato per l'annotazione semantica del manoscritto autografo *Castello dell'anima* (Palermo, BCP, ms. 2 Qq E 29, sec. XVII ex.). Il modello è progettato per rappresentare in modo **computabile**, **interrogabile** e **filologicamente auditabile** la dinamica prudenziale, retorica e dottrinale della scrittura mistica tardomoderna. Il sistema tassonomico qui descritto costituisce il **core semantico** dell'edizione digitale e governa l'uso dell'attributo `@ana` nel corpus TEI.

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
5. [Indice composito di impatto (N–A–F)](#5-indice-composito-di-impatto-naf)
- 5.1 [Formula (AHP)](#51-formula-ahp)
- 5.2 [Discretizzazione (soglie calibrate)](#52-discretizzazione-soglie-calibrate)
- 5.3 [Registrazione TEI](#53-registrazione-tei)
- 5.4 [Robustezza](#54-robustezza)
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
`tei/taxonomy/schema/taxonomy-sch.sch` (generato da ODD, queryBinding="xslt").

**Flusso di generazione**:
`taxonomy-odd.odd` → Roma (oXygen) → `taxonomy-rng.rng` + `taxonomy-sch.sch`.

## 2. Assi interpretativi del sistema
Il modello si articola in **tre assi interpretativi principali**, ciascuno dei quali corrisponde a un diverso livello di descrizione del testo.

### 2.1 Asse fenomenologico
Descrive **ciò di cui il testo parla** e il modo in cui il contenuto mistico e dottrinale viene articolato nel discorso. Tassonomie coinvolte:

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

*   `impact` — impatto interpretativo, **esito della discretizzazione dell'indice composito N–A–F (§5)**, non giudizio diretto;
*   `phase` — fase discorsiva.

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
L'elenco delle `<category>` per ciascuna tassonomia è definito nel file
**`./tassonomia-gh.xml`**, che costituisce la **fonte normativa primaria** dei valori annotativi.

## 4. Uso dell'attributo `@ana`
In TEI P5 l'attributo `@ana` ha tipo **pointer** e **deve contenere URI o fragment identifier** che puntano alle categorie tassonomiche (es. riferimenti interni `#xml-id`).
L'attributo `@ana` può contenere **valori multipli**, separati da spazi bianchi (whitespace), ciascuno riferito a una categoria distinta.

### Esempio (forma TEI‑compliant)
```xml
<seg
ana="#pedagogia
#relation-mistica-attiva-meditazione
#risk-dottrinale
#operation-delimitazione
#impact-high #phase-mediana">
Testo annotato del manoscritto...
</seg>
```

### 4.1 Regole sui prefissi
**Regola generale**: per tutte le tassonomie, le categorie che portano il trattino (`-`) devono iniziare con il prefisso della tassonomia radice a cui appartengono.

**Esempio**:
- Tassonomia `risk`
→ categorie come `risk-dottrinale`, `risk-quietismo`, `risk-panteismo`, `risk-impeccabilita`, `risk-ambiguita` (prefisso `risk-` obbligatorio)
- Tassonomia `operation`
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
```xml
<seg
ana="#phase-critical
#phase-mediana
#exposition-critical
#risk-quietismo">
Testo con problematiche teologiche in sezione centrale...
</seg>
```

**Esempio scorretto** (manca fase posizionale):
```xml
<seg
ana="#phase-critical
#exposition-critical
#risk-quietismo">

<!-- Errore: manca fase posizionale (introduction/mediana/conclusive) -->
</seg>
```

**Implementazione**: il vincolo è **gestito in fase editoriale** (prosa normativa).
Un futuro constraint Schematron può essere aggiunto per enforcing automatico (vedi §8.3).

## 5. Indice composito di impatto (N–A–F)
L'indice di impatto è un valore **derivato** (non una tassonomia) che quantifica
la forza regolativa di ogni occorrenza annotata. Combina tre parametri:

- **N** = necessità interpretativa (esposizione dottrinale del passo *prima*
  dell'intervento), continuo 0–1;
- **A** = riduzione dell'ambiguità (quanto l'intervento restringe le letture),
  continuo 0–1;
- **F** = funzione prudenziale, espressa come **classe formale del marcatore** su
  scala ordinale {1, 2, 3}, **derivata dal rango dell'asse `operation`**:
  - `operation-delimitazione` → F = 1 (il «cioè»: circoscrive una parola);
  - `operation-attenuatio` / `operation-precisatio` / `operation-riequilibrio`
    → F = 2 (il «ciò s'intende»: ridefinisce una proposizione);
  - `operation-declaratio` → F = 3 (il «io mi dichiaro»: dichiarazione performativa).

### 5.1 Formula (AHP)
Pesi da confronti a coppie (Analytic Hierarchy Process) in rapporto F : N : A = 4 : 2 : 1:

    I = (4·F_norm + 2·N + 1·A) / 7,   con F_norm = F/3

(w_F = 4/7, w_N = 2/7, w_A = 1/7).

> **Nota sull'etichetta.** La sigla storica «N–A–F» elenca i parametri, non la
> loro gerarchia. Nel modello AHP **F è il peso dominante** (4/7), seguito da N
> (2/7) e A (1/7): l'ordine di importanza è dunque F → N → A.

### 5.2 Discretizzazione (soglie calibrate)
Il valore I è ricondotto alle 4 categorie dell'asse `impact`. Le soglie **non sono
fissate a priori**: sono **calibrate sul campione** e verificate contro la
distribuzione reale dei valori di I (le 29 glosse). Il taglio superiore isola le
occorrenze a massima forza regolativa; i tagli intermedi cadono in corrispondenza
degli addensamenti della distribuzione. Una volta calibrate, restano **invarianti
su tutto il corpus**:

- `impact-low`:      I < 0.50
- `impact-medium`:   0.50 ≤ I < 0.66
- `impact-high`:     0.66 ≤ I < 0.82
- `impact-critical`: I ≥ 0.82

Nel campione la banda `impact-critical` viene a **coincidere** con le *declaratio*
(F = 3), i sigilli performativi di ortodossia. Si tratta di un **esito riscontrato**,
non di una definizione: la banda è determinata dalla soglia (I ≥ 0.82), non dalla
categoria di `operation`. La coincidenza è coerente con il `catDesc` di
`impact-critical`.

### 5.3 Registrazione TEI
La classe discreta è dichiarata in `@ana` sul segmento (una delle 4 categorie
`impact`); il calcolo (N, A, F, I) è registrato come **feature structure** `<fs>`
in `<standOff type="impact-index">`, collegata al segmento via `@corresp`. La
formula è dichiarata **una sola volta** nell'`editorialDecl`, non ripetuta.

### 5.4 Robustezza
Ricalcolo con pesi alternativi (analisi di sensibilità) e prova inter-annotatore
(*encoding challenge*): le divergenze di classificazione e di pesi vengono pubblicate.

## 6. Vincoli semantici cross-assiali
Alcuni vincoli collegano categorie provenienti da assi diversi. Di seguito sono elencati i vincoli **cross-assiali** principali.

### 6.1 Corrispondenza `rischio-*` ↔ `operation-*`
**Regola semantica fondamentale**:
Ogni categoria della tassonomia `func` che appartenga al ramo `rischio` (cioè `rischio-attenuatio`, `rischio-precisatio`, `rischio-declaratio`) presuppone logicamente una categoria corrispondente dalla tassonomia `operation`.

| Categoria `func`     | Categoria `operation` |
|----------------------|-----------------------|
| `rischio-attenuatio` | `operation-attenuatio`|
| `rischio-precisatio` | `operation-precisatio`|
| `rischio-declaratio` | `operation-declaratio`|

**Significato**:
- `rischio-attenuatio` descrive la **strategia autoriale** di mitigazione di un enunciato rischioso (perché l'autrice interviene)
- `operation-attenuatio` descrive il **meccanismo discorsivo concreto** (glossa, precisazione, parentetica) tramite cui la mitigazione avviene (come il testo interviene)

**Regola di applicazione**:
Un segmento che riceve `#rischio-attenuatio` deve ricevere anche `#operation-attenuatio`. Analogamente per `precisatio` e `declaratio`.

**Esempio corretto**:
```xml
<seg
ana="#rischio-attenuatio
#operation-attenuatio
#risk-dottrinale
#legittimazione">
Glosse esplicative che smorzano formulazioni rischiose...
</seg>
```

**Esempio scorretto** (manca operazione corrispondente):
```xml
<seg ana="#rischio-attenuatio
#legittimazione">
<!-- Errore: manca #operation-attenuatio -->
</seg>
```

**Implementazione**:
il vincolo è **formalmente dichiarato ma non ancora codificato in Schematron** (vedi §8.3).
È gestito mediante **linee guide editoriali** e **revisione manuale** in fase di annotazione.

**Status**: Un futuro aggiornamento a `taxonomy-sch.sch` dovrà includere una regola Schematron che enforci questa corrispondenza automaticamente.

## 7. Querying (XPath/XQuery – esempi)
>**Nota:** le query presuppongono che il namespace TEI (`xmlns:tei="http://www.tei-c.org/ns/1.0"`) sia correttamente dichiarato nel processore XPath/XQuery e che `@ana` contenga **pointer** (fragment identifier con `#`).

### Segmenti ad alto rischio con operazione attenuativa
```xpath
//tei:seg[matches(@ana, '#risk-dottrinale') and matches(@ana, '#operation-attenuatio')]
```

### Segmenti marcati come critical in fase mediana
```xpath
//tei:seg[matches(@ana, '#phase-critical') and matches(@ana, '#phase-mediana')]
```

### Segmenti che ricevono strategia di rischio (per validazione)
```xpath
//tei:seg[matches(@ana, '#rischio-')]
```

### Tutti i segmenti che violano il vincolo `rischio-*` ↔ `operation-*` (per validazione manuale)
```xpath
//tei:seg[matches(@ana, '#rischio-attenuatio') and not(matches(@ana, '#operation-attenuatio'))]
```

## 8. Validazione e setup ambientale
### 8.1 Configurazione oXygen XML Editor
Per attivare la validazione automatica (strutturale e logica) durante l'editing del corpus TEI, il file corpus deve referenziare gli schemi locali inclusi nel pacchetto:
```xml
<?xml-model
href="../../tei/taxonomy/schema/taxonomy-rng.rng" type="application/xml"
schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="../../tei/taxonomy/schema/taxonomy-sch.sch" type="application/xml"
schematypens="http://purl.oclc.org/dsdl/schematron"?>
```
(Regolare il percorso relativo `href` in base alla posizione del corpus rispetto al directory `tei/taxonomy/schema/`.)

### 8.2 Vincoli Schematron (automatici)
Il sistema impone controlli rigorosi via Schematron (definiti in `taxonomy-sch.sch`):

*   **`category-catdesc-present`**: Ogni `<category>` deve contenere un `<catDesc>`.
*   **`category-catdesc-not-empty`**: Il contenuto di ogni `<catDesc>` non può essere vuoto (solo spazi bianchi).
*   **`category-prefix-consistency`**: Per tutte le tassonomie tranne `func`, le categorie con trattino rispettano il prefisso della tassonomia radice (es. `risk-*`, `operation-*`, `exposition-*`, etc.).
*   **`taxonomy-category-xmlid-unique`**: Unicità globale di `@xml:id` su tutti gli elementi `<taxonomy>` e `<category>` (rete di sicurezza per bug RNG).

### 8.3 Vincoli editoriali (prosa normativa)
I seguenti vincoli sono **gestiti manualmente in fase di annotazione** e **non ancora enforced da Schematron**:

**Coerenza `@ana` → categorie**: `@ana` deve puntare a categorie effettivamente definite in `tassonomia-gh.xml` (verificabile via XPath, ma non enforced da schema RNG/Schematron).

**Corrispondenza `rischio-*` ↔ `operation-*`** (vedi §6.1): quando un segmento riceve `#rischio-attenuatio` (o `precisatio`, `declaratio`), deve ricevere la corrispondente `#operation-attenuatio` (o `precisatio`, `declaratio`).

**Compatibilità `phase-critical`** (vedi §4.2):
`#phase-critical` deve comparire insieme a una fase posizionale (`#phase-introduction`, `#phase-mediana`, o `#phase-conclusive`).

**Registrazione dell'indice `impact-index`** (vedi §5.3): ogni segmento con una categoria `impact-*` deve avere una `<fs>` corrispondente in `<standOff type="impact-index">` (collegata via `@corresp`), e la classe formale F ivi registrata deve essere congruente con la categoria `operation-*` dichiarata in `@ana` (delimitazione → F=1; attenuatio/precisatio/riequilibrio → F=2; declaratio → F=3).

**Prossimi passi**: questi vincoli vanno convertiti in regole Schematron e inclusi in `taxonomy-sch.sch` per automazione completa della validazione. Sono candidati per una futura versione dell'ODD.

## 9. Come citare questo lavoro
Se utilizzi questo sistema tassonomico o i file di validazione nella tua ricerca, cita come segue:

**Citazione bibliografica**
> Luciano Longo, *Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima di Teresa di San Geronimo* (versione 2026), Repository GitHub: https://github.com/luciano-longo77/castello-anima-TEI-IA

**Formato BibTeX**
```bibtex
@software{longo_tassonomia_2026,
  author       = {Longo, Luciano},
  title        = {Sistema Tassonomico del modello TEI interpretativo per il Castello dell'anima},
  year         = {2026},
  publisher    = {GitHub},
  howpublished = {\url{https://github.com/luciano-longo77/castello-anima-TEI-IA}},
  note         = {TEI + IA controllata}
}
```

## 10. Contribuzione e workflow
Ogni modifica al sistema tassonomico deve avvenire tramite **Pull Request** e includere:

1. **Aggiornamento di `tei/taxonomy/tassonomia-gh.xml`**: aggiunta/modifica di categorie o descrizioni.
2. **Rigenerazione dello schema** (se necessario): usare Roma (oXygen) per generare `taxonomy-rng.rng` e `taxonomy-sch.sch` a partire da `tei/taxonomy/schema/taxonomy-odd.odd`. Includere entrambi i file generati nella PR.
3. **Aggiornamento del presente documento (`Sistema Tassonomico.md`)** per riflettere i nuovi assi, categorie, o vincoli, inclusi eventuali aggiornamenti alla mappatura a tre assi interpretativi (§2) se una nuova tassonomia viene introdotta.

## 11. Statuto del documento
Questo documento descrive il sistema tassonomico a **scopo di orientamento**. La **fonte normativa vincolante** resta *tassonomia-gh.xml (dati) e taxonomy-odd.odd (definizione formale)*; in caso di divergenza tra questo documento e i file XML della repository, prevalgono questi ultimi.

**Versione corrente**: 2026-08-07.

**Changelog essenziale**
- *2026-08-07* — §5 riscritto sul modello AHP (indice AURORA): formula `I = (4·F_norm + 2·N + 1·A)/7` (pesi F:N:A = 4:2:1), **F** derivato dal rango dell'asse `operation` (non più continuo), soglie a quattro bande calibrate sul campione; §2.3 allineato (`impact` come esito del calcolo); §8.3 esteso con il vincolo di registrazione `impact-index`. **Schema invariato** (nessun asse nuovo: F è derivato, non reificato). Allineamento con XML e schema riverificato.
- *2026-07-29* — versione precedente (indice N–A–F con pesi ad hoc `I = 0.40·N + 0.35·A + 0.25·F`, F continuo, soglie 0.4/0.7).

**Licenza:**
Tutti i contenuti del repository sono rilasciati sotto licenza
**Creative Commons Attribution 4.0 International (CC BY 4.0)**.
Vedi il file **SPDX-License-Identifier: CC-BY-4.0** per i dettagli completi.
