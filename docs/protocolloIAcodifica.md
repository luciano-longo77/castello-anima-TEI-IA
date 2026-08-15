# Protocollo operativo per la codifica assistita da AI — *Castello dell'anima*
## AI-assisted encoding runbook · *Il Castello dell'anima* (TEI-IA)

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![CC BY 4.0](https://img.shields.io/badge/licenza-CC%20BY%204.0-7b2d3b)](https://creativecommons.org/licenses/by/4.0/)

**Autrice / Author of the work**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703) · **Editor**: Luciano Longo

> **Cos'è / What this is.** Non è un riassunto del modello di codifica (quello è in [`teiText-guida-codifica.md`](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/docs/teiText-guida-codifica.md) e nella tassonomia, ed è l'unica autorità). È il **manuale operativo** per *pilotare un'AI*: i presupposti d'ingresso, le **stringhe di prompt** da incollare, gli **output attesi** e i **comandi di verifica reali**. · *Not a summary of the encoding model (that lives in `teiText-guida-codifica.md` and the taxonomy — the sole authority). It is the **runbook** to *drive an AI*: input preconditions, copy-paste **prompt strings**, expected **outputs**, and the **real verification commands**.*

---

## 0. Presupposti d'ingresso · Input preconditions

**Prima di dare qualunque compito all'AI, la sessione deve avere allegati** (l'AI non usa id/regole assenti da questi file) · **Before any task, the session must have attached** (the AI uses no id/rule absent from these files):

| # | Allegato · Attachment | Ruolo · Role |
|--:|---|---|
| 1 | **questo file** `protocollo-IA-codifica.md` | il come · the *how* |
| 2 | `docs/teiText-guida-codifica.md` | **il modello** (autorità) · the **model** (authority) |
| 3 | `tei/taxonomy/tassonomia-gh.xml` | categorie ammesse per `@ana` · allowed `@ana` categories |
| 4 | `tei/header/castello-anima-teiHeader.xml` | mani `#ink_1`/`#ink_3-dark`, testimoni `#txt-c`/`#txt-b0`/`#txt-b1`, resp. `#editor`/`#s-teresa` · hands, witnesses, resp. |
| 5 | `docs/anagrafe-citazioni.md` | citazioni note + carte · known citations + folios |
| 6 | il capitolo/modulo su cui si lavora · the chapter/module in hand | `tei/text/…` |

**Ambiente di verifica** (locale come in CI) · **Verification environment** (local, as in CI): `python3` + `lxml`, `xmllint` (`libxml2-utils`), `jing`; le 7 guardie in `.github/workflows/scripts/`, `schema/tei_all.rng`, `schema/impactindex.sch`. **Per la riproducibilità, fissa e registra le versioni** (nel change log o in un file di ambiente): TEI P5 (release del `tei_all.rng` vendorizzato), `python`, `lxml`, `libxml2`/`xmllint`, `jing`; e — quando si usa l'AI — **modello e versione**. · *For reproducibility, **pin and record the versions** (in the change log or an environment file): TEI P5 (the vendored `tei_all.rng` release), `python`, `lxml`, `libxml2`/`xmllint`, `jing`; and — when the AI is used — **model and version**.*

**Stato di lavoro** · **Working state**: si opera **su un ramo, mai su `main`**; **un capitolo/segmento per volta**; nulla si consegna se non passa §3. · *work on a branch, never `main`; one chapter/segment at a time; nothing ships unless it passes §3.*

---

# 🇮🇹 Runbook (Italiano)

## 1. Confini (non negoziabili)
1. **Proponi, non decidere.** Ogni intervento è una proposta; valida l'editore umano.
2. **Non inventare lezioni.** Illeggibile → `<unclear>`/`<gap>`; congettura → `<supplied resp="#editor" cert="…">`. Se non sai, **chiedi**.
3. **Solo id dichiarati.** `@ana`/`@hand`/`@wit`/`@resp` puntano a id realmente presenti negli allegati §0. Un valore non dichiarato **non esiste**: segnalalo.
4. **Mai normalizzazioni tacite.** Documento (`orig`/`sic`/`abbr`/`del`) ≠ interpretazione (`reg`/`corr`/`expan`/`supplied`).
5. **Tutto verificabile.** Non proporre nulla che non superi la catena §3.

## 2. Ciclo operativo
Per **ogni** blocco: **① incolla il PROMPT → ② l'AI produce l'OUTPUT → ③ esegui la VERIFICA (§3) → ④ l'AI emette la dichiarazione di trasparenza (§4) → ⑤ l'editore valida → blocco successivo.**
**Ri-validazione obbligatoria a blocchi**: dopo ogni capitolo (o ~10 `<seg>`) ri-esegui l'intera catena §3 e rileggi §1. Un blocco che non passa **non** si consegna.
**Politica di fallimento**: dopo un errore segnalato dalla catena §3, l'AI può proporre **solo** una **correzione localizzata all'errore**; ogni modifica ulteriore è una **nuova proposta** con nuova validazione. Il limite di **2 iterazioni** vale per **lo stesso errore sullo stesso blocco**; un errore nuovo riavvia il conteggio solo previa registrazione del nuovo diff. Se al terzo tentativo lo stesso errore persiste, si ferma e passa la mano all'editore (non "aggiustare" allargando il diff).
**Clausola comune a tutti i task** (formato operativo di «se non sai, chiedi» dei §1): se manca un allegato, un id, una regola o un'evidenza sufficiente — token `@ana` sconosciuto, fonte non in anagrafe, testo illeggibile, due segmentazioni ugualmente plausibili, input incompleto — **non completare il task**: restituisci soltanto `BLOCCATO: <motivo> — serve <file/regola/decisione>` (nel linguaggio del prompt, per uniformità dei log).

### Task A — Segmentare un capitolo
**PROMPT** (sostituisci `{N}`):
```
Segmenta il capitolo {N} del Libro III in <seg>, seguendo teiText-guida-codifica.md.
- gerarchia: div[@type="chapter" n="{N}"] > (head, argument?) > p[@n] > seg
- un <seg> = un'unità di senso annotabile; rispetta i confini di paragrafo del testo
- xml:id di ogni seg = seg-c{N}p{P}-{label}  (label: parola-chiave italiana minuscola)
- materialità dov'è: <pb n="…r/v"/>, <fw>, <lb break="no"/> solo su parola spezzata
- NON assegnare @ana in questo task
- se il capitolo è lungo, procedi per BLOCCHI di paragrafi dichiarando dove ti fermi;
  non troncare mai un elemento XML aperto (meglio meno paragrafi, ma completi)
Output: solo il frammento XML del capitolo, poi fermati.
```
**VERIFICA**: `xmllint --noout` (buona formazione) + `regole_fissate_guard.py` (naming `seg-cNpP-label`).

### Task B — Assegnare `@ana` a un `<seg>`
**PROMPT**:
```
Assegna @ana a questo <seg> secondo gli 8 assi di teiText-guida-codifica.md e della tassonomia.
- ordine canonico: func · operation · risk · exposition · phase(+phase-critical) · mystic_state · relation(0+) · impact
- cardinalità (phase-critical è un MODIFICATORE della fase, non un 9° asse):
    func=1..n · operation=1 · risk=1 · exposition=1 · phase-base=1 · phase-critical=0..1 · mystic_state=0..1 · relation=0..n · impact=1
    (func può portare più funzioni retoriche insieme; mystic_state è opzionale su segmenti di sola cornice)
- tutti i token sono #id presi dalla tassonomia allegata
- SOBRIETÀ: rischio caldo (quietismo/panteismo/impeccabilita/dottrinale) e #phase-critical
  SOLO dove il testo recinta localmente (glossa, «non…ma», «però», operazione-guardia F≥2).
  Altrimenti: #risk-ambiguita + #operation-delimitazione, niente #phase-critical.
- #phase-critical mai su #impact-low.
Output: il solo attributo ana="…" + 1 riga di motivazione per asso non ovvio.
```
**VERIFICA**: `e2_guard.py` (token→tassonomia) + `cooccurrence_guard.py` (cardinalità di tutti gli assi: impact/operation/risk/exposition=1, func≥1, mystic_state≤1, 1 fase base, phase-critical≤1) + `regole_fissate_guard.py` (sobrietà).

### Task C — Apparato genetico
**PROMPT**:
```
Codifica il lavoro d'autrice su questo passo (vedi teiText-guida-codifica.md):
- correzione: <subst><del>…</del><add>…</add></subst> con @hand/@place
- ritracciatura del tratto bruno T0→T1: <retrace hand="#ink_1">…</retrace>  (mai #ink_3-dark, mai dentro <add>)
- aggiunta prudenziale scura tardiva T3: <add hand="#ink_3-dark">…</add>
- variante di fase: <app><lem wit="#txt-c">…</lem><rdg wit="#txt-b0" varSeq="n">…</rdg></app>
Non promuovere una rdg a lem senza istruzione dell'editore.
Output: il frammento XML dell'apparato, poi fermati.
```
**VERIFICA**: `interventi_guard.py` (`subst`=add+del; `supplied` con `@resp`+`@cert`) + `regole_fissate_guard.py` (retrace).

### Task D — Bande d'impatto
**PROMPT**:
```
Per questo <seg> il compito EDITORIALE è scegliere SOLO le bande e l'operazione:
- N_band ∈ {critica,alta,media,bassa}; A_band ∈ {alta,media,bassa}; operazione = rango F
- NON scegliere né arrotondare I a intuito: N, A e I vanno ricavati applicando le ancore
  fisse e la formula normativa di teiText-guida-codifica.md / impactindex.sch (o generati
  dallo script), con l'arrotondamento definito lì; tu porti solo bande+operazione
- costruisci la <fs corresp="#{segid}" xml:id="idx-{segid}"> con N_band,A_band,N,A,F,I
- la classe #impact-* nell'@ana del seg deve corrispondere alla banda di I
Output: la <fs> + il commento-seg canonico N=…/…; A=…/…; F=… op -> I=… classe.
```
**VERIFICA**: Schematron `impactindex.sch` (ancore + formula + classe↔I) + `commenti_guard.py` (commento-I == fs-I).

### Task E — Citazione
**PROMPT**:
```
Marca la citazione latina dentro il suo <seg> (vedi anagrafe-citazioni.md):
- <cit><quote xml:lang="la">…</quote><bibl>…</bibl></cit>
- NIENTE @ana/@type su <cit>: la funzione sta nell'@ana del seg (#relation-intertesto-*)
- l'indice d'impatto resta sul seg (nessuna <fs> verso la cit)
- se la fonte non è nell'anagrafe, segnalalo: non inventare il riferimento.
Output: il frammento XML + la riga da aggiungere all'anagrafe (rif. + carte).
```
**VERIFICA**: `citazioni_guard.py` + `cit_glossa_guard.py`.

---

# 🇬🇧 Runbook (English)

## 1. Boundaries (non-negotiable)
1. **Propose, don't decide.** Every intervention is a proposal; the human editor validates.
2. **Never invent readings.** Illegible → `<unclear>`/`<gap>`; conjecture → `<supplied resp="#editor" cert="…">`. If unsure, **ask**.
3. **Declared ids only.** `@ana`/`@hand`/`@wit`/`@resp` point to ids actually present in the §0 attachments. An undeclared value **does not exist**: flag it.
4. **No silent normalisation.** Document (`orig`/`sic`/`abbr`/`del`) ≠ interpretation (`reg`/`corr`/`expan`/`supplied`).
5. **Everything verifiable.** Propose nothing that fails the §3 chain.

## 2. Operating loop
For **every** block: **① paste the PROMPT → ② the AI yields the OUTPUT → ③ run the VERIFICATION (§3) → ④ the AI emits the transparency statement (§4) → ⑤ the editor validates → next block.**
**Mandatory block re-validation**: after each chapter (or ~10 `<seg>`) re-run the whole §3 chain and re-read §1. A block that does not pass is **not** shipped.
**Failure policy**: after an error flagged by the §3 chain, the AI may propose **only** a **fix localised to that error**; any further change is a **new proposal** with fresh validation. The **2-iteration** limit applies to **the same error on the same block**; a new error restarts the count only after the new diff is recorded. If the same error persists on the third try, stop and hand over to the editor (do not "fix" by widening the diff).
**Clause common to all tasks** (the operational form of §1's "if unsure, ask"): if an attachment, id, rule or sufficient evidence is missing — unknown `@ana` token, source not in the anagrafe, illegible text, two equally plausible segmentations, incomplete input — **do not complete the task**: return only `BLOCKED: <reason> — needs <file/rule/decision>` (in the prompt's language, for log uniformity).

### Task A — Segment a chapter
**PROMPT** (replace `{N}`):
```
Segment chapter {N} of Book III into <seg>, following teiText-guida-codifica.md.
- hierarchy: div[@type="chapter" n="{N}"] > (head, argument?) > p[@n] > seg
- one <seg> = one annotatable sense-unit; respect the text's paragraph boundaries
- each seg xml:id = seg-c{N}p{P}-{label}  (label: lowercase Italian keyword)
- materiality where it is: <pb n="…r/v"/>, <fw>, <lb break="no"/> only on a split word
- do NOT assign @ana in this task
- if the chapter is long, proceed in paragraph BLOCKS stating where you stop;
  never truncate an open XML element (fewer paragraphs, but complete)
Output: the chapter's XML fragment only, then stop.
```
**VERIFY**: `xmllint --noout` (well-formedness) + `regole_fissate_guard.py` (naming).

### Task B — Assign `@ana` to a `<seg>`
**PROMPT**:
```
Assign @ana to this <seg> per the 8 axes of teiText-guida-codifica.md and the taxonomy.
- canonical order: func · operation · risk · exposition · phase(+phase-critical) · mystic_state · relation(0+) · impact
- cardinality (phase-critical is a MODIFIER of the phase, not a 9th axis):
    func=1..n · operation=1 · risk=1 · exposition=1 · phase-base=1 · phase-critical=0..1 · mystic_state=0..1 · relation=0..n · impact=1
    (func may carry several rhetorical functions at once; mystic_state is optional on pure-framing segments)
- every token is a #id taken from the attached taxonomy
- RESTRAINT: hot risk (quietismo/panteismo/impeccabilita/dottrinale) and #phase-critical
  ONLY where the text locally fences (gloss, "not…but", "however", guard-operation F≥2).
  Otherwise: #risk-ambiguita + #operation-delimitazione, no #phase-critical.
- #phase-critical never on #impact-low.
Output: the ana="…" attribute only + 1 line of rationale per non-obvious axis.
```
**VERIFY**: `e2_guard.py` + `cooccurrence_guard.py` (all-axis cardinality: impact/operation/risk/exposition=1, func≥1, mystic_state≤1, 1 base phase, phase-critical≤1) + `regole_fissate_guard.py` (restraint).

### Task C — Genetic apparatus
**PROMPT**:
```
Encode the authorial work on this passage (see teiText-guida-codifica.md):
- correction: <subst><del>…</del><add>…</add></subst> with @hand/@place
- brown re-inking T0→T1: <retrace hand="#ink_1">…</retrace>  (never #ink_3-dark, never inside <add>)
- late cautionary dark addition T3: <add hand="#ink_3-dark">…</add>
- phase variant: <app><lem wit="#txt-c">…</lem><rdg wit="#txt-b0" varSeq="n">…</rdg></app>
Do not promote a rdg to lem without the editor's instruction.
Output: the apparatus XML fragment, then stop.
```
**VERIFY**: `interventi_guard.py` + `regole_fissate_guard.py` (retrace).

### Task D — Impact bands
**PROMPT**:
```
For this <seg> the EDITORIAL task is to choose ONLY the bands and the operation:
- N_band ∈ {critica,alta,media,bassa}; A_band ∈ {alta,media,bassa}; operation = F rank
- do NOT pick or round I by intuition: N, A and I follow from applying the fixed anchors
  and the normative formula of teiText-guida-codifica.md / impactindex.sch (or are
  script-generated), with the rounding defined there; you supply only bands+operation
- build <fs corresp="#{segid}" xml:id="idx-{segid}"> with N_band,A_band,N,A,F,I
- the seg's #impact-* class must match the band of I
Output: the <fs> + the canonical seg-comment N=…/…; A=…/…; F=… op -> I=… class.
```
**VERIFY**: Schematron `impactindex.sch` + `commenti_guard.py`.

### Task E — Citation
**PROMPT**:
```
Mark the Latin citation inside its <seg> (see anagrafe-citazioni.md):
- <cit><quote xml:lang="la">…</quote><bibl>…</bibl></cit>
- NO @ana/@type on <cit>: the function lives in the seg's @ana (#relation-intertesto-*)
- the impact index stays on the seg (no <fs> pointing to the cit)
- if the source is not in the anagrafe, flag it: do not invent the reference.
Output: the XML fragment + the row to add to the anagrafe (ref + folios).
```
**VERIFY**: `citazioni_guard.py` + `cit_glossa_guard.py`.

---

# 🔧 Strumenti condivisi · Shared tooling

## 3. Catena di verifica (identica alla CI) · Verification chain (identical to CI)
Dal root del repository. Ogni comando che fallisce è un blocco da correggere prima di consegnare. · *From the repo root. Any failing command is a block to fix before shipping.*

```bash
TEXT=tei/text/castello-anima-teiText.xml
TAX=tei/taxonomy/tassonomia-gh.xml
RNG=schema/tei_all.rng
SCH=schema/impactindex.sch

# 1. NFC (normalizzazione Unicode)
python3 - "$TEXT" <<'PY'
import sys, unicodedata
s=open(sys.argv[1],encoding="utf-8").read()
sys.exit(0 if s==unicodedata.normalize("NFC",s) else "NON-NFC")
PY

# 2. Buona formazione + risoluzione XInclude, poi documento risolto
xmllint --noout --xinclude "$TEXT"
xmllint --nofixup-base-uris --xinclude "$TEXT" > resolved.xml

# 3. RelaxNG (TEI All vendorizzato) sul documento risolto
jing "$RNG" resolved.xml

# 4. Le sette guardie (sul modulo, xi:include NON risolto)
python3 .github/workflows/scripts/e2_guard.py            "$TEXT" "$TAX"
python3 .github/workflows/scripts/cooccurrence_guard.py  "$TEXT" "$TAX"   # $TAX esplicito = stessa tassonomia di e2
python3 .github/workflows/scripts/cit_glossa_guard.py    "$TEXT"
python3 .github/workflows/scripts/citazioni_guard.py     "$TEXT"
python3 .github/workflows/scripts/commenti_guard.py      "$TEXT"
python3 .github/workflows/scripts/interventi_guard.py    "$TEXT"
python3 .github/workflows/scripts/regole_fissate_guard.py "$TEXT"

# 5. Schematron indice d'impatto — impactindex.sch del repo: queryBinding="xslt" (XSLT 1.0),
#    regole INTRA-MODULO (fs + seg sono nel testo), quindi gira su $TEXT NON risolto. Verificato: OK.
python3 - "$TEXT" "$SCH" <<'PY'
import sys
from lxml import etree, isoschematron
doc = etree.parse(sys.argv[1])
sch = isoschematron.Schematron(etree.parse(sys.argv[2]), store_report=True)
if not sch.validate(doc):
    ns={"svrl":"http://purl.oclc.org/dsdl/svrl"}
    for f in sch.validation_report.xpath("//svrl:failed-assert", namespaces=ns):
        print(" -", f.get("location","?"), (f.findtext("svrl:text", namespaces=ns) or "").strip())
    sys.exit(1)
print("Schematron OK")
PY
```
> **Nota (contesto d'esecuzione).** Lo step 5 esegue lo `impactindex.sch` **del repo** (intra-modulo, `xslt`): correttamente su `$TEXT`. È **cosa diversa** dallo schema di riferimento dell'**Appendice A** (superset `xslt2`): la sua sola regola *referenziale* `ana-e2` richiederebbe `resolved.xml`, ma quella referenzialità in CI la garantisce già `e2_guard.py` (step 4). Nessuna contraddizione tra i due. · *Step 5 runs the **repo's** `impactindex.sch` (intra-module, `xslt`) correctly on `$TEXT`. That is **distinct** from the Appendix A reference schema (`xslt2` superset), whose only *referential* rule `ana-e2` would need `resolved.xml` — but that integrity is already ensured in CI by `e2_guard.py` (step 4). No contradiction between the two.*

## 4. Output di trasparenza · Transparency outputs
**(a) Per ogni intervento** l'AI emette una riga tracciabile · **for each intervention** the AI emits a traceable line:
```
[regola: R2 naming | fonte: interpretativa | @resp=#editor | @cert=medium] seg-c3p4-abbandono: label da «abbandono» (§ operation-delimitazione)
```
**(b) A fine sessione** una voce per il `<revisionDesc>` · **at session end** a `<revisionDesc>` entry:
```xml
<change when="AAAA-MM-GG" who="#editor">Sintesi degli interventi proposti dall'AI e validati (capitoli/segmenti toccati, tipo di intervento). Nessuna modifica silenziosa.</change>
```
`@when` è la data della **validazione editoriale**, non della generazione AI; se una revisione copre più giornate, registra eventi `<change>` distinti. · *`@when` is the **editorial-validation** date, not the AI-generation date; if a review spans several days, record separate `<change>` events.*

Questo protocollo attua la dichiarazione d'uso dell'IA del repository — [**AI-USE.md**](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/AI-USE.md): là il *cosa si dichiara*, qui il *come si esegue* in modo verificabile. · *This runbook implements the repository's AI-use disclosure — [**AI-USE.md**](https://github.com/luciano-longo77/castello-anima-TEI-IA/blob/main/AI-USE.md): there the what, here the verifiable how.*

---

# 📎 Appendice A — Invarianti auto-verificabili (XPath/Schematron)
## Appendix A — Self-verifiable invariants (XPath/Schematron)

> Le **stesse invarianti** della catena §3, come **specifica leggibile** in Schematron, perché l'AI ne faccia un **controllo preliminare dichiarativo** prima di ogni output. **Tre livelli distinti, non confondibili**: (1) l'auto-verifica dell'AI è un *pre-check logico*, **non** è prova di validazione; (2) l'**unico controllo autoritativo** è la pipeline §3 (le 7 guardie Python + lo Schematron `impactindex.sch` del repo); (3) il **giudizio editoriale** umano resta sovrano. Ogni `@test` falso è un errore da correggere prima di proporre. **Autorità vs. specifica**: le **sette guardie Python + lo Schematron `impactindex.sch` del repo** sono l'**implementazione autoritativa** della catena §3 (l'asse è ricavato *semanticamente* dalla tassonomia); questa Appendice ne è una **specifica leggibile**, in cui alcuni assi sono formalizzati **per prefisso** (`starts-with`) — una formalizzazione orientativa che può non coincidere token-per-token con il controllo semantico Python. In caso di divergenza, **vince l'implementazione autoritativa (Python/impactindex.sch)**. · *The same invariants as the §3 chain, as a **readable specification** in Schematron, for the AI to run as a **declarative pre-check** before every output. **Three distinct, non-interchangeable levels**: (1) the AI's self-check is a *logical pre-check*, **not** evidence of validation; (2) the **sole authoritative** check is the §3 pipeline (the 7 Python guards + the repo's `impactindex.sch`); (3) human **editorial judgement** remains sovereign. Any false `@test` is an error to fix before proposing. **Authority vs. specification**: the **seven Python guards + the repo's `impactindex.sch`** are the **authoritative implementation** of the §3 chain (the axis is derived *semantically* from the taxonomy); this appendix is a **readable specification** in which some axes are formalised **by prefix** (`starts-with`) — an indicative formalisation that may not match the Python semantic check token-for-token. On divergence, **the authoritative implementation (Python/impactindex.sch) wins**.*
>
> ⚙️ **Processore.** Questo schema è `queryBinding="xslt2"` (usa `tokenize`/`matches`/`every`/`abs`): richiede uno Schematron **XSLT2/3** (es. SchXslt+Saxon). **Verificato: `lxml.isoschematron` lo RIFIUTA** («does not work with schemas using the "xslt2" query language»), quindi **non** è questo il motore della CI. La CI esegue le guardie Python + `impactindex.sch` del repo (che è `queryBinding="xslt"`, XSLT 1.0, e gira su `lxml`). L'Appendice A è dunque **riferimento/spec**, non un secondo motore di pipeline. · *⚙️ **Processor.** This schema is `queryBinding="xslt2"` (uses `tokenize`/`matches`/`every`/`abs`): it needs an **XSLT2/3** Schematron (e.g. SchXslt+Saxon). **Verified: `lxml.isoschematron` REJECTS it**, so it is **not** the CI engine. CI runs the Python guards + the repo's `impactindex.sch` (`queryBinding="xslt"`, XSLT 1.0, runs on `lxml`). Appendix A is therefore **reference/spec**, not a second pipeline engine.*

```xml
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
  <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>

  <!-- ATTENZIONE: questo Schematron NON copre il 100% delle regole. La grammatica dei
       commenti-seg resta a commenti_guard.py (regex, non esprimibile in XPath). Superare
       lo Schematron NON sostituisce la catena §3: gli script Python vanno comunque eseguiti. -->

  <!-- @ana: sintassi + integrità referenziale (e2_guard) -->
  <!-- CONTESTO: la referenzialità (asserzione 3) va valutata su resolved.xml
       (l'XInclude risolto): le <category> stanno nel teiHeader incluso e devono essere in-tree.
       Sul modulo NON risolto le <category> mancano e la verifica autoritativa e' e2_guard.py,
       che unisce tassonomia-gh.xml come file separato. Le altre asserzioni sono intra-modulo. -->
  <sch:pattern id="ana-e2">
    <sch:rule context="tei:*[@ana]">
      <sch:assert test="not(contains(@ana,';')) and not(matches(@ana,'(^|\s)[A-Za-z_]+:[^#/\s]'))"
        >E2: @ana in pseudo-sintassi. Usare '#id' separati da spazio.</sch:assert>
      <sch:assert test="every $t in tokenize(normalize-space(@ana),' ') satisfies starts-with($t,'#')"
        >E2: ogni token di @ana deve iniziare con '#'.</sch:assert>
      <sch:assert test="every $t in tokenize(normalize-space(@ana),' ') satisfies
        (//tei:category[@xml:id=substring($t,2)] or //*[@xml:id=substring($t,2)])"
        >E2: token @ana non dichiarato (né category in tassonomia né xml:id locale).</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- co-occorrenza / cardinalita' degli assi sul seg.
       Cardinalita' CONFERMATE sul corpus (203 seg) e imposte anche da cooccurrence_guard.py
       (che ricava l'asse dalla tassonomia, controllo semantico non per-prefisso):
         impact/operation/risk/exposition = 1 ; func >= 1 (piu' funzioni possibili) ;
         mystic_state = 0..1 (opzionale) ; 1 fase base ; phase-critical = 0..1 con base ; relation = 0..n.
       Divisione dei compiti: cooccurrence_guard.py verifica la CARDINALITA' e l'assegnazione
       dell'asse (ed e' fail-closed: segnala token senza '#' o non classificati); e2_guard.py e'
       AUTORITATIVO sulla forma '#id' e sulla referenzialita' del token. Validazione congiunta.
       NB i prefissi reali: l'asse func NON ha prefisso #func- (e' #legittimazione-*/#pedagogia-*/
       #rischio-*/#ethos-*); mystic_state e' con underscore (#mystic_state-*). -->
  <sch:pattern id="ana-cooccurrence">
    <sch:rule context="tei:seg[@ana]">
      <sch:let name="t" value="tokenize(normalize-space(@ana),' ')"/>
      <sch:assert test="count($t[. = ('#phase-introduction','#phase-mediana','#phase-conclusive')])=1"
        >Attesa esattamente 1 fase base.</sch:assert>
      <sch:assert test="count($t[.='#phase-critical']) &lt;= 1">#phase-critical al massimo una volta.</sch:assert>
      <sch:assert test="not($t = '#phase-critical') or
        $t[. = ('#phase-introduction','#phase-mediana','#phase-conclusive')]"
        >#phase-critical senza una fase base.</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#impact-')])=1">Atteso esattamente 1 #impact-*.</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#operation-')])=1">Atteso esattamente 1 #operation-*.</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#risk-')])=1">Atteso esattamente 1 #risk-*.</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#exposition-')])=1">Atteso esattamente 1 #exposition-*.</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#mystic_state-')]) &lt;= 1">mystic_state al massimo 1 (0..1).</sch:assert>
      <sch:assert test="count($t[starts-with(.,'#legittimazione') or starts-with(.,'#pedagogia')
        or starts-with(.,'#rischio') or starts-with(.,'#ethos')]) &gt;= 1"
        >Atteso almeno 1 valore dell'asse func (legittimazione/pedagogia/rischio/ethos).</sch:assert>
      <!-- eccedenza ammessa solo dell'asse relation (#relation-*, 0..n). Regola sui <seg>:
           gli id locali fig-*/area- ammessi da ana-e2 compaiono sugli <span> in standOff, non qui. -->
      <sch:assert test="every $r in $t[not(starts-with(.,'#impact-') or starts-with(.,'#operation-')
        or starts-with(.,'#risk-') or starts-with(.,'#exposition-') or starts-with(.,'#mystic_state-')
        or starts-with(.,'#phase-') or starts-with(.,'#legittimazione') or starts-with(.,'#pedagogia')
        or starts-with(.,'#rischio') or starts-with(.,'#ethos'))] satisfies starts-with($r,'#relation-')"
        >Token @ana fuori dagli assi dichiarati (func, operation, risk, exposition, phase, mystic_state, relation, impact) o dal modificatore phase-critical.</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- regole fissate: retrace, naming, @ana-seg, sobrietà (regole_fissate_guard) -->
  <sch:pattern id="regole-fissate">
    <sch:rule context="tei:retrace">
      <sch:assert test="@hand='#ink_1'">R1: retrace è la ritracciatura bruna T0→T1: hand = #ink_1 (mai #ink_3-dark).</sch:assert>
      <sch:assert test="not(parent::tei:add)">R1: retrace mai dentro add.</sch:assert>
    </sch:rule>
    <sch:rule context="tei:seg[@xml:id]">
      <sch:assert test="matches(@xml:id,'^seg-(c\d+p\d+[a-z]?|pro-p\d+|tit)-')"
        >R2: xml:id del seg fuori convenzione (seg-cNpP-label | seg-pro-pP-* | seg-tit-*).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:cit[@ana] | tei:rs[@ana] | tei:term[@ana] | tei:quote[@ana]">
      <sch:assert test="false()">R3: @ana solo sul seg (mai su cit/rs/term/quote).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:seg[tokenize(normalize-space(@ana),' ') = '#phase-critical']">
      <!-- confronto per TOKEN, non contains(): niente falsi positivi da sottostringhe -->
      <sch:let name="a" value="tokenize(normalize-space(@ana),' ')"/>
      <sch:assert test="not($a = '#impact-low')">R5: #phase-critical mai su #impact-low.</sch:assert>
      <sch:assert test="$a = ('#operation-precisatio','#operation-attenuatio','#operation-riequilibrio','#operation-declaratio',
        '#risk-quietismo','#risk-panteismo','#risk-impeccabilita','#risk-dottrinale')"
        >R5: #phase-critical senza recinzione (né operazione-guardia né rischio caldo).</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- interventi editoriali: normalizzazione + genetico (interventi_guard) -->
  <sch:pattern id="interventi">
    <sch:rule context="tei:choice/tei:reg | tei:choice/tei:expan">
      <sch:assert test="not(@resp)">reg/expan: nessun @resp per-istanza (attribuzione globale in editorialDecl).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:choice/tei:corr">
      <sch:assert test="@resp and @cert">corr: @resp + @cert obbligatori.</sch:assert>
    </sch:rule>
    <sch:rule context="tei:supplied">
      <sch:assert test="@resp and @cert">supplied: @resp + @cert obbligatori (congettura editoriale).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:subst">
      <sch:assert test="tei:add and tei:del">subst malformato: servono almeno un add e un del.</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- citazioni e glosse (citazioni_guard + cit_glossa_guard) -->
  <sch:pattern id="citazioni-glosse">
    <sch:rule context="tei:quote">
      <sch:assert test="parent::tei:cit">Ogni quote dentro un cit (nessuna citazione orfana).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:cit">
      <sch:assert test="ancestor::tei:seg/@xml:id">cit dentro un seg con @xml:id.</sch:assert>
      <sch:assert test="tei:quote[@xml:lang][normalize-space()]">cit: una quote con @xml:lang e testo.</sch:assert>
      <sch:assert test="tei:bibl[normalize-space()]">cit: una bibl (fonte) non vuota.</sch:assert>
      <sch:assert test="not(@ana) and not(@type)">cit: niente @ana/@type (la funzione sta sul seg).</sch:assert>
      <sch:assert test="ancestor::tei:seg[tokenize(normalize-space(@ana),' ')[starts-with(.,'#relation-intertesto')]]"
        >Il seg della cit deve avere #relation-intertesto-* in @ana.</sch:assert>
    </sch:rule>
    <sch:rule context="tei:note[@type='glossa']">
      <sch:assert test="not(node())">note type='glossa' deve essere vuota.</sch:assert>
      <sch:assert test="parent::tei:add">note type='glossa' figlia di add.</sch:assert>
      <sch:assert test="not(tokenize(normalize-space(@ana),' ')[starts-with(.,'#impact-')])">note type='glossa' senza #impact-* (l'indice è del seg).</sch:assert>
    </sch:rule>
    <sch:rule context="tei:fs[@corresp]">
      <sch:let name="tgt" value="substring-after(@corresp,'#')"/>
      <sch:assert test="not(//*[@xml:id=$tgt][self::tei:cit or self::tei:note])"
        >Nessuna fs verso cit/note: l'indice d'impatto sta solo sul seg.</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- C0 in pattern proprio: una fs con banda DEVE avere @corresp. Separato dal pattern
       impact-index perche' in Schematron un nodo e' processato da una sola <rule> per <pattern>. -->
  <sch:pattern id="impact-ancoraggio">
    <sch:rule context="tei:fs[tei:f[@name='N_band'] or tei:f[@name='A_band']]">
      <sch:assert test="@corresp">C0: fs d'impatto senza @corresp (nessun ancoraggio al &lt;seg&gt;).</sch:assert>
    </sch:rule>
  </sch:pattern>
  <!-- indice d'impatto: correlazione fs<->seg, bande, ancore, formula, classe (impactindex.sch) -->
  <sch:pattern id="impact-index">
    <sch:rule context="tei:fs[tei:f[@name='N_band'] and tei:f[@name='A_band']]">
      <sch:let name="sid" value="substring-after(@corresp,'#')"/>
      <sch:let name="seg" value="//tei:seg[@xml:id=$sid]"/>
      <!-- correlazione fs<->seg (restrizione di progetto): @corresp singolo, campi completi, target seg con @ana, naming idx- -->
      <sch:assert test="matches(@corresp,'^#[A-Za-z_][A-Za-z0-9_.-]*$')"
        >Indice: @corresp non è un singolo riferimento nella forma #xml:id.</sch:assert>
      <sch:assert test="tei:f[@name='N_band'] and tei:f[@name='A_band'] and tei:f[@name='N']
        and tei:f[@name='A'] and tei:f[@name='F'] and tei:f[@name='I']"
        >Indice: fs incompleta (servono N_band, A_band, N, A, F, I).</sch:assert>
      <sch:assert test="count($seg)=1">Indice: @corresp non punta a un unico &lt;seg&gt; esistente.</sch:assert>
      <sch:assert test="$seg/@ana">Indice: il &lt;seg&gt; puntato dalla fs non ha @ana.</sch:assert>
      <sch:assert test="@xml:id = concat('idx-',$sid)">Indice: xml:id della fs ≠ 'idx-' + xml:id del seg.</sch:assert>
      <sch:let name="ana" value="tokenize(normalize-space(string($seg/@ana)),' ')"/>
      <sch:let name="N"  value="number(tei:f[@name='N']/tei:numeric/@value)"/>
      <sch:let name="A"  value="number(tei:f[@name='A']/tei:numeric/@value)"/>
      <sch:let name="F"  value="number(tei:f[@name='F']/tei:numeric/@value)"/>
      <sch:let name="I"  value="number(tei:f[@name='I']/tei:numeric/@value)"/>
      <sch:let name="nb" value="tei:f[@name='N_band']/tei:symbol/@value"/>
      <sch:let name="ab" value="tei:f[@name='A_band']/tei:symbol/@value"/>
      <sch:let name="Icalc" value="(4*($F div 3) + 2*$N + $A) div 7"/>
      <sch:assert test="($nb='critica' and $N=0.90) or ($nb='alta' and $N=0.75)
        or ($nb='media' and $N=0.55) or ($nb='bassa' and $N=0.30)"
        >Indice: N non è l'ancora della banda (critica 0.90 · alta 0.75 · media 0.55 · bassa 0.30).</sch:assert>
      <sch:assert test="($ab='alta' and $A=0.85) or ($ab='media' and $A=0.675) or ($ab='bassa' and $A=0.40)"
        >Indice: A non è l'ancora della banda (alta 0.85 · media 0.675 · bassa 0.40).</sch:assert>
      <!-- I e' serializzato a 3 decimali (verificato 203/203 fs). Il confronto e' per TOLLERANZA
           sul valore numerico completo: la modalita' di arrotondamento (half-up/half-even/tronc.)
           e' ininfluente ai fini della validazione, perche' l'errore max di arrotondamento a 3
           decimali (<= 0.0005) rientra nella tolleranza 0.001. -->
      <sch:assert test="abs($I - $Icalc) &lt; 0.001">Indice: I ≠ formula (4·Fnorm + 2·N + A) div 7.</sch:assert>
      <sch:assert test="($I &lt; 0.50 and $ana='#impact-low')
        or ($I &gt;= 0.50 and $I &lt; 0.66 and $ana='#impact-medium')
        or ($I &gt;= 0.66 and $I &lt; 0.82 and $ana='#impact-high')
        or ($I &gt;= 0.82 and $ana='#impact-critical')"
        >Indice: la classe #impact-* del seg è incoerente con I (soglie 0.50 / 0.66 / 0.82).</sch:assert>
    </sch:rule>
    <!-- completezza inversa: ogni <seg> annotato ha ESATTAMENTE una fs gemella (1:1, verificato) -->
    <sch:rule context="tei:seg[@ana]">
      <sch:let name="sid" value="string(@xml:id)"/>
      <sch:assert test="count(//tei:fs[@corresp = concat('#',$sid)]) = 1"
        >Indice: il &lt;seg&gt; annotato non ha esattamente una &lt;fs&gt; gemella (corresp='#'+xml:id).</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
```

**Copertura e contesto d'esecuzione.** Questa Appendice è un **ausilio di auto-correzione**, non un sostituto della catena §3: superarla **non** basta, gli script Python vanno comunque eseguiti. **Non c'è invariante dichiarata qui che la CI non applichi**: la completezza `fs↔seg` (1:1) e la completezza dei campi della `fs` sono ora nel `impactindex.sch` del repo (pattern `indice-completezza`, verificato: passa 203/203 e intercetta le `fs` incomplete); il mapping `F↔operazione` è in `commenti_guard.py` (tabella `OPF`). Nota: nell'Appendice `@corresp` usa `matches()` (XSLT2); nel `impactindex.sch` del repo (XSLT1, senza regex) l'equivalente è `starts-with('#')` + assenza di spazi + `sid` non vuoto/non-`#` + target esistente. Il `impactindex.sch` del repo è stato irrobustito e ri-testato con `lxml`: `current()` sostituito da variabile `$sid`, confronto delle classi d'impatto **token-safe** (`concat(' ',…,' ')`), e regola **C0** (una `fs` con banda senza `@corresp` viene intercettata). In particolare (a) la regola `ana-e2` va valutata su **`resolved.xml`** (dove le `<category>` del teiHeader sono in-tree); sul modulo la referenzialità la garantisce `e2_guard.py`; (b) la grammatica dei **commenti-seg** non è esprimibile in XPath e resta a `commenti_guard.py`; (c) `ana-e2` ammette **di proposito** anche `xml:id` locali oltre alle `<category>` (i vocabolari standOff `fig-*`/`area-*` puntati dagli `@ana` degli `<span>`): non è un falso positivo ma una scelta di modello. **Gerarchia di autorità fs↔commento**: l'`I` della `<fs>` è **normativo**, il commento-seg ne è la **rappresentazione leggibile** e deve coincidere; in caso di divergenza fallisce la validazione e **non** si "aggiusta" il commento senza prima verificare la `<fs>` (`commenti_guard.py` ricava l'`I` dal documento e lo confronta, non tratta i due come dati indipendenti). · *This appendix is a **self-correction aid**, not a replacement for the §3 chain: passing it is **not** enough — the Python scripts must still run. In particular (a) the `ana-e2` rule must be evaluated on **`resolved.xml`** (where the teiHeader `<category>` set is in-tree); on the bare module referential integrity is guaranteed by `e2_guard.py`; (b) the **seg-comment** grammar is not XPath-expressible and stays with `commenti_guard.py`; (c) `ana-e2` **intentionally** also admits local `xml:id`s beyond `<category>` (the standOff `fig-*`/`area-*` vocabularies pointed to by `<span>` `@ana`s): this is a model choice, not a false positive.*

**Regola non esprimibile in XPath (commenti_guard).** Ogni `<seg>` con `@ana` deve essere **preceduto** da un commento `<!-- … -->` con la clausola `N=<banda>/<ancora>; A=<banda>/<ancora>; F=<n> <operazione> -> I=<X.XXX> <classe>`; ancore↔bande, `F`↔operazione, classe↔soglia di `I`, e l'`I` del commento = l'`I` della `<fs>` gemella. **Convenzione numerica di `I`**: serializzato a **3 decimali** (verificato: 203/203 fs); il confronto è fra valori numerici entro tolleranza (0.001 nello Schematron, 0.0005 nel raffronto commento↔fs), sicché la **modalità di arrotondamento** (half-up/half-even/troncamento) è **ininfluente** ai fini della validazione. · *Not XPath-expressible (comment guard): every `<seg>` with `@ana` must be **preceded** by a `<!-- … -->` comment with the clause `N=<band>/<anchor>; A=<band>/<anchor>; F=<n> <operation> -> I=<X.XXX> <class>`; anchors↔bands, `F`↔operation, class↔`I` threshold, and the comment's `I` = the twin `<fs>`'s `I`. **`I` numeric convention**: serialized to **3 decimals** (verified: 203/203 fs); comparison is numeric within tolerance (0.001 in Schematron, 0.0005 for comment↔fs).*

---

*Questo protocollo è documentazione di metodo, versionata col repository; ne costituisce il **riferimento operativo** per la **trasparenza e la riproducibilità** dell'uso dell'AI nell'edizione (la garanzia piena richiede anche il versionamento dell'ambiente — §0 — e le fixture negative). · This protocol is method documentation, versioned with the repository; it is the **operational reference** for the **transparency and reproducibility** of AI use in the edition (full guarantee also requires environment pinning — §0 — and negative fixtures).*
