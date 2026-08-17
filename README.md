# Edizione Critica Digitale *Il Castello dell'anima* (Libro III)
## Introduzione

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) ![DSE](https://img.shields.io/badge/DSE-Digital_Scholarly_Editing-8B0000) ![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-7b2d3b)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0 

## Indice

- [Obiettivo principale](#obiettivo-principale)
- [Fase 1: Edizione critica del III libro](#fase-1-edizione-critica-del-iii-libro)
  - [Introduzione al progetto](#introduzione-al-progetto)
    - [Contesto storico e teologico](#contesto-storico-e-teologico)
    - [Struttura del trattato](#struttura-del-trattato)
  - [Edizione digitale del III libro](#edizione-digitale-del-iii-libro)
    - [Trascrizione e digitalizzazione](#trascrizione-e-digitalizzazione)
    - [Elementi TEI utilizzati nella trascrizione](#elementi-tei-utilizzati-nella-trascrizione)
    - [Criteri editoriali](#criteri-editoriali)
    - [Apparato critico](#apparato-critico)
    - [Strutturazione del testo](#strutturazione-del-testo)
    - [Note filologiche](#note-filologiche)
  - [Analisi delle correzioni e aggiunte](#analisi-delle-correzioni-e-aggiunte)
  - [Pubblicazione open access](#pubblicazione-open-access)
- [Workflow TEI](#workflow-tei)
- [Conclusione](#conclusione)
- [Struttura del repository](#struttura-del-repository)

## Obiettivo principale

Realizzare un’**edizione critica digitale** del **III libro** del *Castello dell’anima* di suor Teresa di San Geronimo, con particolare attenzione alla dimensione genetica, alle dinamiche correttive e alle modalità di autocontrollo dottrinale presenti nell’autografo.

L’edizione si fonda sull’assunto metodologico che il manoscritto autografo *Palermo, Biblioteca Comunale, ms. 2 Qq E 29*  costituisca l’**unica tradizione diretta dell’opera**. Tutti i fenomeni grafici, materiali e linguistici sono pertanto trattati come potenzialmente rilevanti sul piano filologico, storico e interpretativo.

## Fase 1: Edizione critica del III libro
## Introduzione al progetto
### Contesto storico e teologico

Il Castello dell’anima articola il percorso di perfezione spirituale secondo tre stadi progressivi:

- anime incipienti
- anime proficienti
- anime perfette

**Suor Teresa di San Geronimo** (Anna La Longa, 1670–post 1703), terziaria carmelitana palermitana, sviluppa la propria riflessione mistica in un contesto caratterizzato da forte sorveglianza dottrinale. A partire dalla fine del Seicento, temi quali l’**unione mistica**, la **quiete** e l’**otium delle potenze** erano considerati suscettibili di equivoci teologici e frequentemente associati al sospetto di quietismo.

Nel **III libro**, tali tensioni emergono con particolare evidenza attraverso:

- un incremento delle aggiunte marginali e interlineari;
- riscritture e precisazioni dottrinali;
- dichiarazioni esplicite di adesione all’ortodossia cattolica.

### Struttura del trattato

Il **III libro** è dedicato allo stadio delle **anime perfette** e rappresenta la sezione più densa dal punto di vista dottrinale e genetico. Per questo motivo è assunto come focus dell’edizione critica, con attenzione specifica alla stratificazione scrittoria e ai processi di revisione autoriale.

## Edizione digitale del III libro
### Trascrizione e digitalizzazione

Il lavoro editoriale si articola in due passaggi principali:

1. **Trascrizione diplomatico-conservativa a due livelli** del manoscritto autografo. Il *livello documentario* conserva integralmente la patina linguistica del testo (oscillazioni diacritiche, grafiche e sintattiche, considerate parte costitutiva del dato autografo); accanto ad esso, un *livello editoriale* — regolarizzazione grafica, scioglimento delle abbreviazioni, correzione degli errori materiali — è codificato **in parallelo** tramite `<choice>` (`<orig>`/`<reg>`, `<abbr>`/`<expan>`, `<sic>`/`<corr>`), reversibile e attribuito (`@resp`/`@cert`), **senza mai sostituire** la lezione documentaria. Le due lezioni coesistono sullo stesso piano: la scelta del livello è demandata alla lettura o all'elaborazione a valle.

2. **Codifica in XML‑TEI** (P5), finalizzata alla strutturazione, interrogabilità e versionabilità del testo, senza sovrapporre al testo base livelli interpretativi o normalizzanti.

### Elementi TEI utilizzati nella trascrizione

La codifica si articola in **tre layer** — filologico‑grafico, mistico‑dottrinale, intertestuale — che poggiano su una **trascrizione a due livelli** (diplomatico ⇄ interpretativo) resa con `<choice>`:

 ```xml
<!-- Layer filologico-grafico: trascrizione a due livelli -->

<choice>
<orig>à</orig>
<reg>a</reg>
</choice>  --> grafia originale ⇄ regolarizzata

<choice>
<abbr>dunq</abbr>
<expan>dunque</expan>
</choice>  --> abbreviazione ⇄ scioglimento

<choice>
<sic>ad</sic>
<corr>al</corr>
</choice>   --> lezione erronea ⇄ correzione editoriale

<add>        aggiunte marginali o interlineari
<del>        cancellazioni
<subst>      sostituzione (del + add come evento unico)
<retrace>    rivergatura a inchiostro (ripasso di una lezione già presente; testo invariato, ≠ add/subst)
<unclear>    grafia indecifrabile
<gap>        lacune o abrasioni
<supplied>   integrazioni su guasto meccanico

<!-- Layer mistico-dottrinale: lessico agganciato al vocabolario degli stati -->
stato mistico
<term ref="#unione">unione</term>                    

<!-- Layer intertestuale: rimandi e citazioni -->
rimando a fonte
<ref target="#avila-castello">castello dell'anima</ref>   

citazione con fonte
<cit>
<quote xml:lang="la">…</quote>
<bibl/>
</cit>   
                
```

La trascrizione a **due livelli**, in cui la *lezione diplomatica* e la sua *regolarizzazione* coesistono via `<choice>`, non va confusa con un'eventuale trascrizione ampiamente regolarizzata a soli fini di leggibilità o di elaborazione computazionale: quest'ultima sarebbe un livello *derivato* e non fa parte del testo dell'edizione.

### Criteri editoriali
L’edizione adotta un approccio diplomatico‑conservativo, che:

* preserva integralmente la patina linguistica dell’autografo;
* conserva oscillazioni grafiche, diacritiche e morfosintattiche;
* non opera alcuna normalizzazione linguistica o ortografica;
* scioglie le abbreviazioni materiali esclusivamente per garantire la leggibilità del testo.

Le irregolarità linguistiche (italiano regionale siciliano, sintassi semicolta, interferenze latine) sono assunte come dati storici e sociolinguistici dell’autografo e non vengono corrette o interpretate nel testo base.

#### Mani scriventi
Le mani scriventi sono descritte mediante un apparato dedicato:

```xml
<handDesc>
  <handNote xml:id="ink_1">...</handNote>
  <handNote xml:id="ink_2">...</handNote>
  <handNote xml:id="ink_3-dark">...</handNote>
  <handNote xml:id="pencil_1">...</handNote>
  <handNote xml:id="ink_4-external">...</handNote>
</handDesc>
```

Le mani descritte sono **cinque**: quattro autografe di Teresa 
-`ink_1` e `ink_2` (inchiostro bruno),
- `ink_3-dark` (inchiostro scuro),
- `pencil_1` (matita)
- più la mano esterna `ink_4-external`.

#### Apparato critico

```xml
<app>
  <lem wit="#txt-c">lezione critica costituita</lem>
  <rdg wit="#txt-b0"><subst><del hand="#ink_1" resp="#s-teresa">prima lezione</del><add hand="#ink_1" resp="#s-teresa">lezione corretta</add></subst></rdg>
  <!-- correzione immediata "currente calamo": una sola <rdg> con <subst>, senza @varSeq;
       @varSeq si aggiunge solo quando concorrono più letture di campagne distinte -->

</app>

<listWit>
  <witness xml:id="txt-b0">Testo base</witness>
  <witness xml:id="txt-b1">Interventi immediati</witness>
  <witness xml:id="txt-1">Riscrittura su testo base</witness>
  <witness xml:id="txt-2">Interventi correttivi‑glossativi</witness>
  <witness xml:id="txt-3">Interventi correttivi successivi</witness>
  <witness xml:id="txt-4">Interventi glossativi esterni</witness>
  <witness xml:id="txt-c" resp="#editor">Testo critico costituito (lemma)</witness>
</listWit>
```

Le `witness` dichiarate sono **sette**: i sei livelli genetici (Tb0, Tb1, T1–T4) più il livello costituito **Tc** (`txt-c`, `@resp="#editor"`), che `<lem wit="#txt-c">` richiama come lezione dell'edizione.

### Strutturazione del testo

```xml
<div type="book" n="3">
  <div type="chapter" n="1">
    <head>Capitolo primo</head>

    <argument>
        <p>Si tratta della dispositione che lascia
            nell'anima la <term ref="#notte">notte dello spirito</term>.
        </p>
    </argument>

    <p n="3" xml:id="III-cap1-p3">Quando più un'anima è ragionata di
      <term><choice><orig>Croce</orig><reg resp="#editor">croce</reg></choice></term>,
      e <term>travagli</term>
        <choice>
          <orig>altri tanto</orig>
          <reg resp="#editor">altritanto</reg>
        </choice>
        è più sicuro lo stato suo (...)</p>
  </div>
</div>
```

L'unità testuale di riferimento è il paragrafo **`<p n="…">`**, mentre il lessico mistico è isolato da **`<term ref="…">`**. La numerazione dei paragrafi è **continua d'autrice** lungo tutto il micro-commit (proemio §§ 1–2, cap. I §§ 3–12, …): il primo paragrafo del cap. I è perciò `n="3"`, non `n="1"`.

### Note filologiche
L’edizione include:

* note filologiche ed esplicative:
  
  ```xml
  <note type="material">...</note>
  <note type="source">...</note>
  ```
* identificazione delle mani scriventi (@hand);
* analisi delle strategie di mitigazione dottrinale.
  
## Analisi delle correzioni e aggiunte
Le modifiche testuali sono classificate come:

* varianti sostitutive;
* aggiunte marginali o interlineari;
* cancellazioni;
* rivergature a inchiostro (`<retrace>`): ripasso di una lezione già presente (testo invariato), distinto dalle aggiunte e dalle sostituzioni.

La posizione materiale delle modifiche è indicata tramite attributi di localizzazione e correlata alla foliazione originale.

## Pubblicazione open access
L’edizione è pubblicata in open access nei seguenti formati:

* XML/TEI (dati primari)
* HTML (interfaccia di consultazione)


## Workflow TEI
1. Ricognizione materiale del manoscritto (`<msDesc>`)
2. Trascrizione diplomatico‑conservativa
3. Definizione delle mani (`<handDesc>`)
4. Strutturazione del testo (`<div>`, `<p>`) e trascrizione a due livelli (`<choice>`)
5. Codifica delle varianti d'autrice in apparato (`<app>`, `<lem>`, `<rdg>` con `<subst>`) e delle rivergature a inchiostro (`<retrace>`)
6. Segnaletica materiale: foliazione e cambi-riga (`<pb>`, `<lb>`, `<fw>`) — senza `@facs` (immagini non autorizzate)
7. Revisione filologica e validazione XML
8. Pubblicazione e documentazione metodologica

## Conclusione
L’edizione critica digitale del III del *Castello dell’anima* mira a restituire il testo come processo stratificato, influenzato dal contesto storico‑dottrinale e dalle pratiche di autocontrollo. La separazione tra edizione critica e sperimentazione computazionale consente di coniugare rigore filologico e innovazione metodologica senza compromettere lo statuto del testo.

## Struttura del repository

Il repository è organizzato su due piani: i **modelli TEI generici** dell'edizione (`tei-model/`) e i **micro-commit** che rilasciano il testo capitolo per capitolo (`Micro-commits/`, MC-1…MC-8). La validazione automatica del modello leggero è in `.github/workflows/`. L'annotazione multiassiale sperimentale (indice d'impatto, `seg`/`@ana`, standOff) e l'elaborazione computazionale/IA non fanno parte di questa edizione.

**Gerarchia di autorità.** La fonte autorevole dell'edizione è il **TEI conforme allo schema ODD** (`data/*.xml` validati); lo schema (`.odd` → `.rng`) è normativo, la documentazione lo *descrive*, e i viewer HTML in `output/`/`tool/` sono **artefatti derivati**, non rappresentazioni normative del testo.

```text
.
├── README.md                     # Questo documento: edizione critica + guida al repository
├── .github/workflows/            # CI di validazione del modello leggero
│   ├── validate.yml              #   NFC → XInclude → jing → guardia puntatori
│   ├── guardia_nfc.py
│   ├── guardia_puntatori.py
│   └── README.md
├── tei-model/                    # Modelli TEI generici dell'edizione (3 layer, 2 livelli)
│   ├── README.md                 #   modello a 3 layer + diagramma d'insieme
│   ├── header/                   #   teiHeader-model.xml + README + diagramma + output/
│   └── text/                     #   text-model.xml + README + diagramma + output/
└── Micro-commits/                # I micro-commit dell'edizione (MC-1…MC-8)
    ├── README.md                 #   piano editoriale e roadmap
    └── MC-1/                     #   Commit 1 — Libro III, capp. I–V
        ├── README.md             #     introduzione sintetica e cartulazione del MC
        ├── data/                 #     TEI-Header.xml, castello-anima-text.xml, ODD/RNG
        ├── docs/                 #     Introduzione, Struttura-cartulazione, Header-README
        ├── output/               #     prototipi di visualizzazione (viewer, cartulazione)
        └── tool/                 #     viewer-stati-mistici.html (ricerca degli stati mistici)
```

## Licenza
Creative Commons Attribution 4.0 International (**CC BY 4.0**).  

---

## 👤 Curatore
**Luciano Longo**   
- Contatti: <luciano.longo@dedalus.com> 
- ORCID: <https://orcid.org/0009-0005-7557-7546> 
- GitHub: <https://github.com/luciano-longo77>
- Website: <https://luciano-longo77.github.io>
