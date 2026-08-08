# Indice d'impatto (`impact-index`)

Documentazione operativa dell'indice d'impatto del modello TEI+IA del *Castello dell'anima*.
Riferimento nel saggio: §3.1.3. Vocabolario: `tassonomia-gh.xml`, asse `impact`.

## Cos'è

Metrica composita che misura la **forza regolativa** di una glossa, citazione o segmento
prudenziale nel punto esatto in cui compare. Opera **a valle** dell'interpretazione
filologica, su unità già codificate: non giudica l'ortodossia dell'intervento, ne
quantifica l'incidenza sulla tenuta del discorso. Pesi e soglie sono **fissi e invariati**
su tutto il corpus, così ogni occorrenza è comparabile con ogni altra, anche fra testimoni
diversi (un `impact-high` nel *Castello* e in un altro codice designano la stessa intensità).

## I tre parametri (scala 0–1)

| Sigla | Parametro | Definizione operativa |
|-------|-----------|-----------------------|
| **N** | necessità interpretativa | quanto il passo era dottrinalmente esposto *prima* dell'intervento; stima controfattuale interna al *Castello*, senza termini di confronto esterni |
| **A** | riduzione dell'ambiguità | quanto l'occorrenza restringe le letture possibili dei termini ad alta densità mistica (unione, fusione, *otium*, annichilazione, trasformazione) |
| **F** | funzione prudenziale | rango ordinale dell'operazione del marcatore (vedi sotto) — non stimato |

## F — rango ordinale dell'asse `operation`

F è il **rango dell'operazione** dichiarata in `@ana`, normalizzato `Fnorm = F/3`.

| Grado | Operazioni (`operation`) | Correlato fenomenologico (Casapullo) |
|:-----:|--------------------------|--------------------------------------|
| 1 | `delimitazione` | *cioè* — delimita una parola |
| 2 | `attenuatio`, `precisatio`, `riequilibrio` | *s'intende / non s'intende* — ridisegna una proposizione |
| 3 | `declaratio` | *io mi dichiaro* — dichiarazione performativa |

I gradi sono **classi funzionali**, non un elenco chiuso di formule: un marcatore non
canonico si assegna al grado la cui operazione condivide. La scala è robusta perché colloca
nello stesso grado le operazioni più difficili da distinguere (attenuatio ↔ precisatio).

Serialità decrescente dei marcatori nell'edizione — **cioè 289 · s'intende/non s'intende
128 · mi dichiaro 3** (fonte: `3_edizione.pdf`; criterio: stringa esatta, apostrofo curvo,
occorrenze ricongiunte a cavallo di riga; forma affermativa «ciò s'intende» = 0).

## Formula (pesi AHP)

```
I = (4·Fnorm + 2·N + 1·A) / 7          Fnorm = F / 3
wF = 4/7    wN = 2/7    wA = 1/7        (F : N : A = 4 : 2 : 1)
```

Pesi derivati per confronto a coppie (Analytic Hierarchy Process), **internamente
consistenti**: F:A = 4 coincide con (F:N) × (N:A) = 2 × 2 → *consistency ratio* = 0.
F è dominante perché è il segnale meno inferenziale (N è condizione ma non atto; A è in
parte già catturato dalla scelta del marcatore).

## Bande (asse `impact`)

Soglie fisse, tagliate sulla distribuzione del campione e invariate sul corpus:

| Banda | Soglia |
|-------|--------|
| `impact-low` | I < 0.50 |
| `impact-medium` | 0.50 ≤ I < 0.66 |
| `impact-high` | 0.66 ≤ I < 0.82 |
| `impact-critical` | I ≥ 0.82 |

## Codifica TEI

Doppia registrazione: la **categoria discreta** in `@ana` sul `<seg>`; il **calcolo** in un
`<fs>` dentro `<standOff type="impact-index">`, fratello di `<text>`, collegato via
`@corresp`. La formula è dichiarata **una sola volta** in `editorialDecl`; il valore `I` è
prodotto dallo script, mai digitato a mano. Si usa `<fs>`, non `<val>`.

```xml
<!-- nel testo: la sola categoria discreta -->
<seg xml:id="seg-159r-desiderio"
     ana="#rischio-precisatio #operation-precisatio #risk-quietismo #exposition-critical #impact-high"
     hand="#ink_1">incomincia l'anima a perdire qualunque desiderio…</seg>

<!-- in standoff, stesso documento del testo: il fascio computabile -->
<standOff type="impact-index">
  <fs xml:id="idx-159r-desiderio" corresp="#seg-159r-desiderio" cert="medium">
    <f name="N"><numeric value="0.92"/></f>
    <f name="A"><numeric value="0.82"/></f>
    <f name="F"><numeric value="2"/></f>
    <f name="Fnorm"><numeric value="0.667"/></f>
    <f name="I"><numeric value="0.761"/></f>
  </fs>
</standOff>
```

Esempio: N = 0.92, A = 0.82, F = 2 (operation `precisatio` → grado 2) → **I = 0.761 →
`impact-high`**.

## Uso controfattuale

Negli scenari del protocollo — `#workflow-rimozione` (−CIT), `#workflow-recupero-cancellature`
(+TEXTsub), `#workflow-aggiunta` (+CIT) — lo scarto **ΔI** (indice prima/dopo la
perturbazione) misura quanto il nodo dipende dal presidio, lungo tre dimensioni:
**D1** chiarezza · **D2** coesione · **D3** stabilità dottrinale percepita.

## Robustezza

- ricalcolo con **pesi alternativi** → quota di segmenti che cambiano banda pubblicata come misura di sensibilità;
- **prova inter-annotatore** (codificatori TEI esterni ripetono in autonomia i confronti a coppie, divergenze documentate);
- **pipeline deterministica** (versione del modello e parametri fissati e rilasciati) → indice indipendente dall'annotatore e dal modello.
