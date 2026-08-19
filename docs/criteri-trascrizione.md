# Criteri di trascrizione e normalizzazione

*Edizione digitale del **Castello dell'anima** di Teresa di San Geronimo (Anna La Longa),
ms. Palermo, Biblioteca Comunale, 2 Qq E 29.*

Questo documento fissa **una volta per tutte** le procedure di normalizzazione applicate al testo.
È la fonte di autorità della politica editoriale: nell'encoding TEI il testo è dato **già
nella forma interpretativa costituita**, senza marcare inline i singoli passaggi
diplomatica → interpretativa. Le procedure qui dichiarate valgono per l'intero corpus e sono
richiamate nel `teiHeader` (`encodingDesc/editorialDecl`).

> **Modello editoriale.** Trascrizione **interpretativa moderatamente interventista** (non
> diplomatica conservativa): si ammoderna e regolarizza grafia e interpunzione per la
> leggibilità, conservando i tratti linguistici significativi. Nell'encoding **non compaiono
> elementi diplomatici** (`orig`/`reg`, `sic`/`corr`, `abbr`/`expan`, correzioni grafiche
> `subst`/`del`/`add` d'ambito grafico): l'unico apparato marcato è quello **sostanziale**
> (`app`/`lem`/`rdg`, varianti d'autrice nei punti teologicamente sensibili). Le integrazioni
> editoriali restano segnalate (`supplied`/`gap`).

---

## 1. Normalizzazioni grafiche **silenziose**
Applicate senza segnalazione inline (responsabilità dell'editore, `#editor`, dichiarata qui).

### 1.1 Segni diacritici
Adeguati all'uso moderno:

| Forma del testimone | Forma normalizzata |
|---|---|
| `buon'animo` | `buon animo` |
| `ed'` + vocale | `ed` + vocale |
| `poiche` / `poi che` (causale) | `poiché` |
| `perche` / `per che` | `perché` |

### 1.2 Alternanze regolarizzate

| Testimone | → |
|---|---|
| `à` / `hà` / `a` (prep.) | `a` |
| `ò` / `hò` / `o` (cong. disgiuntiva) | `o` |
| `hò` / `ho` / `ò` (verbo) | `ho` / `[h]o` |
| `quì` / `qui` | `qui` |
| `ne` / `né` | `né` |
| `se` / `sè` | `sé` |
| `si` / `sì` | `sì` |
| `perche` / `perché` | `perché` |

### 1.3 Unione e separazione delle parole
Conformate all'uso odierno: `per che > perché`; `inalto > in alto`; `egli > e gli`;
`nelei > né lei`; `nonsapeva > non sapeva`; `inquestitempi > in questi tempi`; ecc.

### 1.4 Maiuscole / minuscole
Normalizzate all'uso moderno: `Io > io`; `Padre / padre` (riferito alla guida spirituale)
`> padre`; `Statua / statua > statua`; `Divina / divina > divina`; ecc.

### 1.5 Punteggiatura
Ritoccata dove obsoleta o dove la piena intelligibilità del testo risulti compromessa. In
particolare i **due punti** del testimone (valore di pausa media) sono resi, secondo il
contesto, con punto e virgola o punto fermo.

### 1.6 Abbreviazioni
Sciolte **senza indicazione**: `d.a > detta`; `total.te > totalmente`; `final.te > finalmente`;
`dunq. > dunque`; `V.R. > Vostra Reverenza`.

---

## 2. Elementi **segnalati** (restano nell'encoding)

### 2.1 Integrazioni editoriali — `[ ]`
Le parentesi quadre segnalano sia le **integrazioni congetturali** sia quelle su **guasto
meccanico** (buco). Nell'encoding TEI:
- integrazione → `<supplied reason="hole|conjecture" resp="#editor" cert="…">…</supplied>`;
- lettere illeggibili entro il guasto (i `…` della Nota) → `<gap reason="illegible" unit="char" quantity="…"/>`.

### 2.2 Apparato sostanziale — solo `<app>`
I **ripensamenti della scrivente** e le varianti d'autrice teologicamente rilevanti sono
resi con l'apparato in segmentazione parallela `app`/`lem`/`rdg` (il `lem` è l'ultima volontà).
Le cassature all'interno delle lezioni si trascrivono, nell'apparato, entro parentesi
uncinate `< >`. **Nessun altro elemento diplomatico** è marcato inline nel testo di lettura.

### 2.3 Convenzioni di supporto
- `/` (nel testo-fonte) = fine di ogni carta → in TEI `<pb n="…"/>`.
- Numero di carta tra parentesi tonde `( )` → in TEI l'attributo `@n` su `<pb>`.
- Note filologico-linguistiche e note di commento **unificate**.

---

## 3. Responsabilità e attribuzione
Le normalizzazioni grafiche e gli scioglimenti di abbreviazione (§1) sono responsabilità
dell'editore (`#editor`) e sono dichiarati **qui una volta per tutte**: non si ripete
`@resp` sui singoli luoghi. Restano attribuiti e certificati per-istanza (`@resp` + `@cert`)
i soli interventi **sostanziali o congetturali**: le integrazioni (`supplied`, di norma
`cert="medium"` salvo diversa valutazione) e le varianti dell'apparato (`app`/`rdg`).

*Fonte: Nota al testo, §2 «Criteri di trascrizione».*
