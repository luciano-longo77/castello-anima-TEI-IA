# Protocollo operativo: applicazione dell'indice d'impatto
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

*Guida operativa del modello TEI+IA del* Castello dell'anima*.*
> Vocabolario: `tassonomia-gh.xml`, asse `impact`.
> Definizione e formula: `indice-impatto.md`.

## Indice

- [Il modello mentale: due metà separate](#il-modello-mentale-due-metà-separate)
- [Passo 0 — Perimetro](#passo-0--perimetro-a-che-cosa-si-applica)
- [Passo 1 — N (necessità interpretativa)](#passo-1--assegnare-n-necessità-interpretativa--giudizio)
- [Passo 2 — A (riduzione dell'ambiguità)](#passo-2--assegnare-a-riduzione-dellambiguità--giudizio)
- [Passo 3 — F (funzione prudenziale)](#passo-3--leggere-f-funzione-prudenziale--lettura-non-stima)
- [Passo 4 — cert](#passo-4--registrare-cert-certezza-dellannotatore)
- [Passo 5 — Calcolo](#passo-5--calcolo--meccanico)
- [Passo 6 — Discretizzazione](#passo-6--discretizzazione--meccanico)
- [Passo 7 — Codifica](#passo-7--codifica--la-doppia-registrazione)
- [Passo 8 — Validazione](#passo-8--validazione--meccanico-checklist)
- [Esempio svolto — c. 159r](#esempio-svolto-per-intero--c-159r)
- [Parametri fissati e residui](#parametri-fissati-e-residui)

## Il modello mentale: due metà separate

L'intera procedura si regge su una distinzione. La prima metà è **giudizio filologico**:
assegni N e A, e leggi F. La seconda metà è **meccanica**: il calcolo, la discretizzazione, la
codifica e la validazione non richiedono alcun giudizio e sono affidati a uno script
(`impact_index.py`). Il confine tra le due metà è ciò che rende l'indice riproducibile: se un
numero che dovrebbe uscire dalla formula viene immesso manualmente, il confine è violato — è
esattamente l'errore che affliggeva la versione precedente (137 valori su 182 non tornavano).

> **Regola d'oro.** Tu scegli le **bande** di N e A e leggi F; lo script converte le bande nei
> valori-ancora, calcola I, assegna la classe, scrive la codifica e la valida. **I non si
> digita: lo calcola lo script.**

## Passo 0 - Perimetro: a che cosa si applica

L'indice si applica **solo** a un'unità già codificata come dispositivo di mediazione, una
glossa (`<note type="glossa">`), una citazione (`<cit>`), un segmento prudenziale (`<seg>`),
un'autocorrezione, dotata del suo `@xml:id`. Non si applica al testo nudo. Se l'occorrenza
non è ancora segmentata come funzionale, l'indice non entra: **prima si codifica, poi si
valuta.**

Quando in un segmento coesistono più connettivi, **F** si legge dal marcatore che realizza la
**funzione prudenziale del segmento**, non da un connettivo di servizio (per es. il *cioè* che
chiarisce «sposalitio» accanto all'*intendo dunque dire* che ridefinisce la proposizione). Il
segmento, del resto, racchiude l'**asserzione esposta insieme al presidio** che la regola.

## Passo 1 - Assegnare N (necessità interpretativa): GIUDIZIO

**N** misura quanto il passo sia dottrinalmente esposto e quanto lo sia *prima* dell'intervento. Il criterio è
controfattuale e interno al *Castello*: «se togliessi questo presidio, il nodo scivolerebbe
verso il panteismo o il quietismo?». Più la risposta è sì, più **N** è alta. 

**Modulatori** (spingono la scelta verso la banda superiore): lessico a rischio (unione, fusione,
*otium*, annichilazione, trasformazione), metafore forti, alta densità glossematica locale,
collocazione nei nodi più esposti del Libro III.

**Rubrica N** — scegli la banda; il **valore-ancora** è assegnato automaticamente (fasce
semiaperte: nessuna sovrapposizione ai bordi):

| Banda | Criterio di banda | Valore-ancora | Riscontro nel *Castello* |
|-------|:-----------------:|:-------------:|--------------------------|
| Critica | N ≥ 0.85 | **0.90** | La rimozione esporrebbe a eresia esplicita (panteismo/quietismo). Es. «divenuta un altro Dio» senza glossa; «sicurtà totale». |
| Alta | 0.65 ≤ N < 0.85 | **0.75** | Passo teologicamente sensibile: la glossa è strutturalmente utile, ma il nodo non collassa in eresia esplicita. |
| Media | 0.45 ≤ N < 0.65 | **0.55** | Chiarificazione utile, esposizione moderata; l'assenza non produrrebbe deriva dottrinale. |
| Bassa | N < 0.45 | **0.30** | Funzione marginale, ornamentale o descrittiva. |

## Passo 2 - Assegnare A (riduzione dell'ambiguità): GIUDIZIO

**A** misura quanto l'intervento restringe le letture possibili: quanto dell'ambiguità di partenza
viene chiusa grazie all'occorrenza. **A** è un **input** dell'indice; il suo effetto sulla tenuta
del discorso è poi messo alla prova, a valle, dal **test controfattuale (ΔI)**, che è cosa
distinta dal valore di **A**.

**Modulatori**: presenza di lessico polisemico ad alto rischio nel passo, grado di esplicitezza
della formula nel delimitare, cooccorrenza con citazioni stabilizzanti che rinforzano la
chiusura.

**Rubrica A** — scegli la banda; il **valore-ancora** è assegnato automaticamente (fasce
semiaperte):

| Banda | Criterio di banda | Valore-ancora | Riscontro nel *Castello* |
|-------|:-----------------:|:-------------:|--------------------------|
| Alta | A ≥ 0.80 | **0.85** | Chiude quasi del tutto l'ambiguità e delimita con precisione. Es. «per quanto sta da parte di Dio» (c. 173v); «non dico del mondo… intendo dunque dire… i gusti di spirito» (c. 159r). |
| Media | 0.55 ≤ A < 0.80 | **0.675** | Restringe il campo ma lascia un margine di lettura. |
| Bassa | A < 0.55 | **0.40** | Tocca l'ambiguità solo marginalmente. |

## Passo 3 - Leggere *F* (funzione prudenziale): LETTURA, non stima

**F** non si stima: si **legge** dalla forma del marcatore, e si classifica in tre gradi. È il parametro meno inferenziale **quasi oggettivo** ed è per questo
che nel modello pesa di più. Non promuovere **F** perché l'occorrenza *sembra importante*: quello
è compito di **N**, non di **F**. Sul piano della **tassonomia**, la classe formale coincide con il **rango
dell'asse `operation`**: 
- *delimitazione* → **1**;
- *attenuatio*/*precisatio*/*riequilibrio* → **2**;
- *declaratio* → **3**.

In caso di **dubbio**: resta al grado inferiore, e sale solo se la forma del marcatore lo
giustifica davvero. **F** risponde alla domanda «che *forma* ha il gesto?», mai «quanto conta?».

**Rubrica F:**

| F | Classe formale | Come riconoscerla — marcatori tipo |
|:-:|----------------|------------------------------------|
| 1 | Connettivo circoscrittivo | Circoscrive una singola parola o sintagma: *cioè*, *ossia*, *o vero*. |
| 2 | Ridefinizione proposizionale | Ridisegna una proposizione esposta: *s'intende* / *non s'intende* / *m'esplico*; attenuatio e precisatio su una proposizione. |
| 3 | Dichiarazione performativa | Presa di posizione dottrinale in prima persona: *io mi dichiaro*, *mi dichiaro*; declaratio. |

## Passo 4 - Registrare *cert* (certezza dell'annotatore)

- **`high`** se marcatore inequivoco e passo chiaro;
- **`medium`** se l'attribuzione richiede inferenza;
- **`low`** se resta un dubbio reale.

**Non incide sul calcolo di I**: documenta l'affidabilità del giudizio.

## Passo 5 - Calcolo *meccanico*

Si normalizza **F** (`Fnorm = F/3`, cioè 1 → 0.333, 2 → 0.667, 3 → 1.0) e si applica la formula.
Lo fa lo script; **tu non digiti I**.

```
I = (4·Fnorm + 2·N + 1·A) / 7          wF = 4/7   wN = 2/7   wA = 1/7
```

## Passo 6 - Discretizzazione *meccanico*

Si confronta **I** con le **soglie fisse** e si ottiene la classe:

| Banda | Soglia |
|-------|--------|
| `impact-low` | I < 0.50 |
| `impact-medium` | 0.50 ≤ I < 0.66 |
| `impact-high` | 0.66 ≤ I < 0.82 |
| `impact-critical` | I ≥ 0.82 |

## Passo 7 - Codifica: la doppia registrazione

Il risultato si scrive in **due posti**, nello stesso file del testo: sul segmento la sola
categoria in `@ana`; in `<standOff>` il fascio computabile come **feature structure** collegata
via `@corresp`. La banda scelta è registrata come `<symbol>` in `N_band`/`A_band`; il
valore-ancora nei rispettivi `<numeric>`. La formula è dichiarata **una sola volta**
nell'`editorialDecl`, non ripetuta a ogni occorrenza.

```xml
<!-- nel testo: la sola categoria  -->
<seg xml:id="seg-c8-desiderio"
     ana="#rischio-precisatio #operation-precisatio #risk-quietismo #exposition-critical
          #phase-mediana #phase-critical #mystic_state-quiete
          #relation-mistica-passiva-quiete #impact-high"
     hand="#ink_1" cert="medium"> (...) incomincia l'anima a perdire qualunque desiderio, e non dico
     del mondo (...) intendo dunque dire che non desidera più gusti di spirito (...)</seg>

<!-- in standoff (stesso documento): il fascio computabile -->
<standOff type="impact-index">
  <fs xml:id="idx-seg-c8-desiderio" corresp="#seg-c8-desiderio" cert="medium">
    <f name="N_band"><symbol value="critica"/></f>
    <f name="A_band"><symbol value="alta"/></f>
    <f name="N"><numeric value="0.90"/></f>
    <f name="A"><numeric value="0.85"/></f>
    <f name="F"><numeric value="2"/></f>
    <f name="Fnorm"><numeric value="0.667"/></f>
    <f name="I"><numeric value="0.760"/></f>
  </fs>
</standOff>
```

## Passo 8 - Validazione *meccaniac* (checklist)

- [ ] il segmento ha `@xml:id`;
- [ ] `@ana` contiene la classe `#impact-X` più func (rischio) / operation / risk / exposition;
- [ ] esiste l'`<fs>` in `<standOff>` con `@corresp` che punta al segmento;
- [ ] la `<fs>` dichiara `N_band` e `A_band` (le bande scelte) come `<symbol>`;
- [ ] **N ∈ {0.90, 0.75, 0.55, 0.30}** e **A ∈ {0.85, 0.675, 0.40}** (valori-ancora); **F ∈ {1, 2, 3}**;
- [ ] I ricalcolato = formula (tolleranza 0) — controllo aritmetico via script;
- [ ] la classe `#impact-X` coincide con la banda in cui cade I;
- [ ] ogni puntatore (`#impact-X` → tassonomia; `#ink_1` → header) risolve: 0 dangling cross-file;
- [ ] il file valida contro `tei_all` (RelaxNG).

## Esempio *c. 159r*

**Occorrenza:** la *precisatio* di c. 159r con cui l'autrice restringe la formula «perdire
qualunque desiderio»: *e non dico del mondo (...) intendo dunque dire che non desidera più gusti di
spirito come prima* (`seg-c8-desiderio` nel teiText).

| Passo | Esito e perché |
|-------|----------------|
| N (giudizio) | banda **Critica → 0.90**: «perdere qualunque desiderio», non delimitato, è leggibile come annichilazione della volontà (quietismo). |
| A (giudizio) | banda **Alta → 0.85**: la *precisatio* restringe il campo ai «gusti di spirito», escludendo l'annullamento totale del volere. |
| F (lettura) | **2** — ridefinizione proposizionale (*precisatio* su una proposizione), non un semplice «cioè» né una «declaratio». |
| cert | **medium**. |
| Calcolo (script) | Fnorm = 2/3 = 0.667; I = (4·0.667 + 2·0.90 + 1·0.85) / 7 = **0.760**. |
| Classe (script) | **impact-high** (0.66 ≤ I < 0.82). |
| Codifica | `<seg>` con `@ana="… #impact-high"` + `<fs>` in standoff (vedi Passo 7). |

## Parametri fissati e residui

**Decisioni chiuse (invariate):**

- **Valori-ancora:** N — Critica 0.90 · Alta 0.75 · Media 0.55 · Bassa 0.30; A — Alta 0.85 ·
  Media 0.675 · Bassa 0.40. L'annotatore sceglie la banda; il valore è determinato.
- **Soglie delle 4 classi:** low I < 0.50 · medium 0.50 ≤ I < 0.66 · high 0.66 ≤ I < 0.82 ·
  critical I ≥ 0.82; tagliate sulla distribuzione reale del campione (29 glosse).
- **Normalizzazione di F:** Fnorm = F/3 (1 → 0.333, 2 → 0.667, 3 → 1.0).
- **Derivazione di F:** rango dell'asse `operation` (delimitazione → 1;
  attenuatio/precisatio/riequilibrio → 2; declaratio → 3).

**Nota sulle scale.** Le rubriche di **N** e **A** sono *scale di input* per il giudizio
dell'annotatore; le quattro bande `impact-*` sono la *scala di output* calcolata su **I**. Hanno
soglie vicine ma distinte e non vanno confuse.
