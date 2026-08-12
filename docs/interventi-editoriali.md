# Interventi editoriali: rendiconto verificabile
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

**Fonte**
*Generato da `tei/text/castello-anima-teiText.xml`. Fotografa ogni intervento editoriale distinguendo il piano della **normalizzazione** (scelte in `choice`) da quello **genetico** (lavoro dell'autrice sul foglio). L'attribuzione è a due livelli: `reg`/`expan` globale (`editorialDecl`), `corr`/`supplied` per-istanza (`@resp` + `@cert`).*

---

## 1. Piano della normalizzazione (`choice`)

| coppia | n | con `@resp` | con `@cert` | attribuzione attesa |
|---|---:|---:|---:|---|
| `orig/reg` | 130 | 0 | 0 | globale (`editorialDecl`): `@resp` = 0 |
| `sic/corr` | 20 | 20 | 20 | per-istanza: `@resp` e `@cert` = n |
| `abbr/expan` | 16 | 0 | 5 | globale; `@cert` solo dove pertinente |

## 2. Piano genetico (lavoro sul foglio)

| elemento | n | con `@hand` | con `@cert` |
|---|---:|---:|---:|
| `add` | 28 | 28 | 6 |
| `del` | 55 | 55 | 0 |
| `subst` | 15 | 0 | 0 |
| `retrace` | 24 | 24 | 24 |
| `gap` | 20 | 0 | 0 |
| `supplied` | 21 | 0 | 21 |

### 2.1 Dettaglio dei valori

| attributo | valori (conteggio) |
|---|---|
| `del/@type` | `correction` (20) · `deletion` (35) |
| `del/@rend` | `strikethrough` (35) |
| `del/@place` | `inline` (47) |
| `add/@type` | `substitution` (18) |
| `add/@place` | `inline` (11) · `margin` (1) · `margin-left` (2) · `margin-right` (1) · `supralinear` (5) |
| `gap/@reason` | `hole` (8) · `illegible` (12) |
| `gap/@unit` | `char` (15) · `chars` (2) · `word` (3) |
| `supplied/@reason` | `hole` (21) |
| `retrace/@hand` | `#ink_3-dark` (24) |
| `retrace/@cert` | `low` (1) · `medium` (23) |

## 3. Controlli di coerenza

**Nessun rilievo.** I due piani sono coerenti con la policy dichiarata: `reg`/`expan` senza `@resp` (attribuzione globale), `corr` pienamente attribuito, ogni `supplied` con `@resp`+`@cert`, ogni `subst` = `add`+`del`.

## 4. Appendice · dettaglio per-istanza

*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, `seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*

| # | piano | elemento | carta | seg | tipo/valore | mano | cert | testo |
|---:|---|---|---|---|---|---|---|---|
| 1 | norm | `abbr/expan` | 158r | - | I.M.I. → Iesus Maria Ioseph | | high | |
| 2 | norm | `sic/corr` | 158r | seg-158r-obedienza | sapere → sapete | | high | |
| 3 | norm | `sic/corr` | 158r | seg-158r-autodemotio | l'opera nostra → l'opere nostre | | high | |
| 4 | norm | `sic/corr` | 158r | seg-158r-invocatio | domandano → domandavo | | medium | |
| 5 | norm | `orig/reg` | 158r | seg-158r-invocatio | à → a | |  | |
| 6 | norm | `sic/corr` | 158r | seg-158r-invocatio | noi → voi | | medium | |
| 7 | norm | `sic/corr` | 158r | seg-158r-invocatio | nostro → vostro | | medium | |
| 8 | norm | `orig/reg` | 158r | seg-158r-invocatio | agiuuto → agiuto | |  | |
| 9 | norm | `orig/reg` | 158r | seg-158r-invocatio | à → a | |  | |
| 10 | norm | `orig/reg` | 158r | seg-158r-incapacitas | poiche → poiché | |  | |
| 11 | norm | `sic/corr` | 158r | seg-158r-incapacitas | trattano → trattavo | | high | |
| 12 | norm | `sic/corr` | 158r | seg-158r-declaratio | contra di chi → contradichi | | medium | |
| 13 | norm | `orig/reg` | 158r | seg-c1-croce | altri tanto → altritanto | |  | |
| 14 | norm | `orig/reg` | 158r | seg-c1-pace | à → a | |  | |
| 15 | norm | `sic/corr` | 158v | seg-c1-scala | ad → al | | high | |
| 16 | norm | `abbr/expan` | 158v | seg-c2-notte | dunq → dunque | |  | |
| 17 | norm | `orig/reg` | 158v | seg-c2-notte | ed'unirsi → ed unirsi | |  | |
| 18 | norm | `sic/corr` | 158v | - | suo → secondo | | medium | |
| 19 | norm | `orig/reg` | 158v | seg-c3-purga | ne → né | |  | |
| 20 | norm | `orig/reg` | 158v | seg-c4-pace2 | de' i → dei | |  | |
| 21 | norm | `sic/corr` | 158v | seg-c4-pace2 | la → le | | high | |
| 22 | norm | `orig/reg` | 158v | seg-c4-arca | ed'altri → ed altri | |  | |
| 23 | norm | `orig/reg` | 158v | seg-c4-astinuata | e → e' | |  | |
| 24 | norm | `orig/reg` | 158v | seg-c5-intro | ad'intendire → ad intendire | |  | |
| 25 | norm | `orig/reg` | 158v | seg-c6-statua | Cossi → Cossì | |  | |
| 26 | norm | `orig/reg` | 158v | seg-c6-statua | à → a | |  | |
| 27 | norm | `orig/reg` | 158v | seg-c6-statua | ed' esposta → ed esposta | |  | |
| 28 | norm | `orig/reg` | 158v | seg-c7-attesa | ne → né | |  | |
| 29 | norm | `orig/reg` | 158v | seg-c7-attesa | ne → né | |  | |
| 30 | norm | `orig/reg` | 158v | seg-c7-viaggio | quì → qui | |  | |
| 31 | norm | `orig/reg` | 158v | seg-c7-viaggio | à → a | |  | |
| 32 | norm | `orig/reg` | 158v | seg-c7-viaggio | à → a | |  | |
| 33 | norm | `orig/reg` | 159r | seg-c7-reposa | ne'i → nei | |  | |
| 34 | norm | `orig/reg` | 159r | seg-c7-reposa | ò → o | |  | |
| 35 | norm | `orig/reg` | 159r | seg-c7-reposa | per che → perché | |  | |
| 36 | norm | `orig/reg` | 159r | seg-c8-desiderio | à → a | |  | |
| 37 | norm | `abbr/expan` | 159r | seg-c8-desiderio | qualunq → qualunque | |  | |
| 38 | norm | `orig/reg` | 159r | seg-c8-desiderio | à → a | |  | |
| 39 | norm | `orig/reg` | 159r | seg-c8-desiderio | ne meno → né meno | |  | |
| 40 | norm | `abbr/expan` | 159r | seg-c8-desiderio | dunq → dunque | |  | |
| 41 | norm | `abbr/expan` | 159r | seg-c8-concopiscibile | qualunq → qualunque | |  | |
| 42 | norm | `orig/reg` | 159r | seg-c9-precis2 | poiche → poiché | |  | |
| 43 | norm | `orig/reg` | 159r | seg-c9-precis2 | hò → ho | |  | |
| 44 | norm | `orig/reg` | 159r | seg-c10-unione-velata | scuopri → scuoprì | |  | |
| 45 | norm | `orig/reg` | 159r | seg-c11-nuovavita | à → a | |  | |
| 46 | norm | `orig/reg` | 159r | seg-c11-quiete | poiche → poiché | |  | |
| 47 | norm | `abbr/expan` | 159r | seg-c11-quiete | qualunq → qualunque | |  | |
| 48 | norm | `orig/reg` | 161r | seg-c2p13-castellano-secreto | e → è | |  | |
| 49 | norm | `orig/reg` | 161v | seg-c2p15-comunicazione-diretta | e → è | |  | |
| 50 | norm | `orig/reg` | 161v | seg-c2p15-comunicazione-diretta | E → È | |  | |
| 51 | norm | `orig/reg` | 162r | - | sù → su | |  | |
| 52 | norm | `orig/reg` | 162r | - | ò → o | |  | |
| 53 | norm | `orig/reg` | 162r | seg-c3p1-donnecciola | poiche → poiché | |  | |
| 54 | norm | `abbr/expan` | 162r | seg-c3p1-miracolo | dun → dunque | |  | |
| 55 | norm | `abbr/expan` | 162r | seg-c3p1-miracolo | V.R. → Vostra Reverenza | | high | |
| 56 | norm | `sic/corr` | 162r | seg-c3p1-miracolo | miracoloso → miracolo | | medium | |
| 57 | norm | `orig/reg` | 162r | seg-c3p1-ripugnanza | raggione → ragione | |  | |
| 58 | norm | `orig/reg` | 162r | seg-c3p1-ripugnanza | poiche → poiché | |  | |
| 59 | norm | `orig/reg` | 162r | seg-c3p1-ripugnanza | ne → né | |  | |
| 60 | norm | `sic/corr` | 162r | seg-c3p1-ripugnanza | trattare → trattarne | | medium | |
| 61 | norm | `orig/reg` | 162v | seg-c3p1-esortazione | difficoltosa → difficoltosa | |  | |
| 62 | norm | `orig/reg` | 162v | seg-c3p1-esortazione | dobij → dobii | |  | |
| 63 | norm | `orig/reg` | 162v | seg-c3p1-esortazione | poiche → poiché | |  | |
| 64 | norm | `sic/corr` | 162v | seg-c3p1-esortazione | che → chi | | medium | |
| 65 | norm | `orig/reg` | 162v | seg-c3p1-santamadre | o → obedienza | |  | |
| 66 | norm | `orig/reg` | 162v | seg-c3p1-santamadre | perche → perché | |  | |
| 67 | norm | `sic/corr` | 162v | seg-c3p2-definizione-oblio | detto stato → dello stato | | medium | |
| 68 | norm | `orig/reg` | 162v | seg-c3p2-definizione-oblio | ò → o | |  | |
| 69 | norm | `orig/reg` | 162v | seg-c3p2-definizione-oblio | adormentarsi → adormentarsi | |  | |
| 70 | norm | `abbr/expan` | 162v | seg-c3p3-differenza-sonno | dunq → dunque | |  | |
| 71 | norm | `orig/reg` | 162v | seg-c3p3-differenza-sonno | poiche → poiché | |  | |
| 72 | norm | `orig/reg` | 162v | seg-c3p3-internarsi | poiche → poiché | |  | |
| 73 | norm | `orig/reg` | 163r | seg-c3p3-interpell | poiche → poiché | |  | |
| 74 | norm | `orig/reg` | 163r | seg-c3p3-interpell | ò → o | |  | |
| 75 | norm | `orig/reg` | 163r | seg-c3p3-interpell | poiche → poiché | |  | |
| 76 | norm | `abbr/expan` | 163r | seg-c3p4-fondoraccolto | qualunq → qualunque | |  | |
| 77 | norm | `orig/reg` | 163r | seg-c3p4-fondoraccolto | o → o | |  | |
| 78 | norm | `orig/reg` | 163r | seg-c3p4-abbraccio | e → è | |  | |
| 79 | norm | `orig/reg` | 163r | seg-c3p5-similitudine-sole | poiche → poiché | |  | |
| 80 | norm | `sic/corr` | 163r | seg-c3p5-sole-verita | possa → porta | | medium | |
| 81 | norm | `orig/reg` | 163r | seg-c3p5-propriastima | poiche → poiché | |  | |
| 82 | norm | `abbr/expan` | 163r | seg-c3p6-tenebre | V.R. → Vostra Reverenza | | high | |
| 83 | norm | `sic/corr` | 163r | seg-c3p6-luce-soprannaturale | questà → quella | | medium | |
| 84 | norm | `orig/reg` | 163v | seg-c3p7-declaratio-verita | poiche → poiché | |  | |
| 85 | norm | `orig/reg` | 164r | seg-c3p9-fortezza | e → è | |  | |
| 86 | norm | `sic/corr` | 164r | seg-c3p9-certezza | poi → più | | medium | |
| 87 | norm | `orig/reg` | 164r | seg-c3p9-desiderio | desiderii → desiderii | |  | |
| 88 | norm | `orig/reg` | 164r | seg-c3p9-desiderio | poiche → poiché | |  | |
| 89 | norm | `sic/corr` | 164r | seg-c3p9-desiderio | possedendo → possedendolo | | medium | |
| 90 | norm | `orig/reg` | 164r | seg-c3p9-desiderio | perche → perché | |  | |
| 91 | norm | `orig/reg` | 164r | seg-c3p9-desiderio | posesso → posesso | |  | |
| 92 | norm | `orig/reg` | 164r | seg-c3p12-linguaggio | ne → né | |  | |
| 93 | norm | `sic/corr` | 164r | seg-c3p12-oscurita | questa → creda | | medium | |
| 94 | norm | `abbr/expan` | 164r | seg-c3p12-oscurita | V.R. → Vostra Reverenza | | high | |
| 95 | norm | `orig/reg` | 164r | seg-c3p12-oscurita | poiche → poiché | |  | |
| 96 | norm | `orig/reg` | 164v | seg-c3p14-cisterna | à → a | |  | |
| 97 | norm | `orig/reg` | 164v | seg-c3p14-mirabilia | Ò → O | |  | |
| 98 | norm | `orig/reg` | 164v | seg-c3p14-mirabilia | perche → perché | |  | |
| 99 | norm | `orig/reg` | 164v | seg-c3p14-mirabilia | perche → perché | |  | |
| 100 | norm | `orig/reg` | 168r | seg-c5p17-conclusio | ha → a | |  | |
| 101 | norm | `orig/reg` | 175v | seg-c8-s2-secretum | Perciò → perciò | |  | |
| 102 | norm | `orig/reg` | 175v | seg-c8-s2-secretum | ne → né | |  | |
| 103 | norm | `abbr/expan` | 175v | seg-c8-s2-secretum | Dunq → Dunque | |  | |
| 104 | norm | `sic/corr` | 175v | seg-c8-s3-roma | E → È | | medium | |
| 105 | norm | `orig/reg` | 175v | seg-c8-s3-roma | ne → né | |  | |
| 106 | norm | `orig/reg` | 175v | seg-c8-s3-roma | poiche → poiché | |  | |
| 107 | norm | `orig/reg` | 175v | seg-c8-s3-roma | ne → né | |  | |
| 108 | norm | `orig/reg` | 175v | seg-c8-s4-cella-ineffabile | ne → né | |  | |
| 109 | norm | `orig/reg` | 175v | seg-c8-s4-cella-ineffabile | ne → né | |  | |
| 110 | norm | `orig/reg` | 175v | seg-c8-s4-cella-ineffabile | poiche → poiché | |  | |
| 111 | norm | `orig/reg` | 175v | seg-c8-s4-cella-ineffabile | ne → né | |  | |
| 112 | norm | `orig/reg` | 175v | seg-c8-s4-cella-ineffabile | poiche → poiché | |  | |
| 113 | norm | `orig/reg` | 176r | seg-c8-s6-fuoco | perché → perché | |  | |
| 114 | norm | `orig/reg` | 176r | seg-c8-s6-fuoco | poiche → poiché | |  | |
| 115 | norm | `orig/reg` | 176r | seg-c8-s7-riequilibrio-vita | Perciò → Perciò | |  | |
| 116 | norm | `orig/reg` | 176r | seg-c8-s8-programma | poiche → poiché | |  | |
| 117 | norm | `orig/reg` | 176r | seg-c8-s8-programma | poiche → poiché | |  | |
| 118 | norm | `orig/reg` | 176r | seg-c8-s9-sensi-sposalitio | poiche → poiché | |  | |
| 119 | norm | `orig/reg` | 176r | seg-c8-s9-sensi-sposalitio | o → o | |  | |
| 120 | norm | `orig/reg` | 176r | seg-c8-s9-sensi-sposalitio | poiche → poiché | |  | |
| 121 | norm | `abbr/expan` | 176r | seg-c8-s10-musica | V.G. → Vostra Grazia | | high | |
| 122 | norm | `orig/reg` | 176v | seg-c8-s12-distrattioni | Ne → Né | |  | |
| 123 | norm | `orig/reg` | 176v | seg-c8-s13-passioni | benché → benché | |  | |
| 124 | norm | `abbr/expan` | 176v | seg-c8-s14-quattroparti | dunq → dunque | |  | |
| 125 | norm | `orig/reg` | 177r | seg-c8-s15b-divisione-inferiore | o → o | |  | |
| 126 | norm | `orig/reg` | 177r | seg-c8-s15b-divisione-inferiore | perché → perché | |  | |
| 127 | norm | `orig/reg` | 177r | seg-c8-s16-spirito-fondo | o → o | |  | |
| 128 | norm | `orig/reg` | 177r | seg-c8-s17-divisione-strana | poiche → poiché | |  | |
| 129 | norm | `orig/reg` | 177r | seg-c8-s17-divisione-strana | perché → perché | |  | |
| 130 | norm | `orig/reg` | 177r | seg-c8-s17-divisione-strana | distinguere → distinguere | |  | |
| 131 | norm | `orig/reg` | 177r | seg-c8-s18-pura-sostanza | perché → perché | |  | |
| 132 | norm | `orig/reg` | 177r | seg-c8-s18-pura-sostanza | perché → perché | |  | |
| 133 | norm | `orig/reg` | 177v | seg-c8-s21-comunicazione | poiche → poiché | |  | |
| 134 | norm | `orig/reg` | 177v | seg-c8-s22-non-sospensione | poiche → poiché | |  | |
| 135 | norm | `orig/reg` | 177v | seg-c8-s24-bocca-sostanza | perciò → perciò | |  | |
| 136 | norm | `orig/reg` | 178r | seg-c8-s28-possesso-inseparabile | poiche → poiché | |  | |
| 137 | norm | `orig/reg` | 178r | seg-c8-s28-possesso-inseparabile | ne → né | |  | |
| 138 | norm | `orig/reg` | 178r | seg-c8-s29-guardia-temere | ne → né | |  | |
| 139 | norm | `orig/reg` | 178r | seg-c8-s30-esorto-hore | ne → né | |  | |
| 140 | norm | `orig/reg` | 178r | seg-c8-s30-esorto-hore | poiche → poiché | |  | |
| 141 | norm | `orig/reg` | 178r | seg-c8-s30-esorto-hore | e → è | |  | |
| 142 | norm | `orig/reg` | 178r | seg-c8-s30-esorto-hore | e → è | |  | |
| 143 | norm | `orig/reg` | 178r | seg-c8-s32-replica-hore | ne → né | |  | |
| 144 | norm | `orig/reg` | 178r | seg-c8-s32-replica-hore | rindimento → rindimento | |  | |
| 145 | norm | `orig/reg` | 178v | seg-c8-s33-totalmente-passiva | poiche → poiché | |  | |
| 146 | norm | `orig/reg` | 178v | seg-c8-s34-opera-quiete | perché → perché | |  | |
| 147 | norm | `orig/reg` | 178v | seg-c8-s34-opera-quiete | poiche → poiché | |  | |
| 148 | norm | `orig/reg` | 178v | seg-c8-s35-mortificatione | perciò → perciò | |  | |
| 149 | norm | `abbr/expan` | 178v | seg-c8-s35-mortificatione | dunq → dunque | |  | |
| 150 | norm | `orig/reg` | 178v | seg-c8-s37-felice-notte | Poiche → Poiché | |  | |
| 151 | norm | `orig/reg` | 179r | seg-c8-s38-estremi-sole | e → è | |  | |
| 152 | norm | `orig/reg` | 179r | seg-c8-s38-estremi-sole | e → è | |  | |
| 153 | norm | `orig/reg` | 179r | seg-c8-s39-propria-stima | poiche → poiché | |  | |
| 154 | norm | `orig/reg` | 179r | seg-c8-s40-padrone-assoluto | ne → né | |  | |
| 155 | norm | `orig/reg` | 179r | seg-c8-s40-padrone-assoluto | ne → né | |  | |
| 156 | norm | `orig/reg` | 179r | seg-c8-s40-padrone-assoluto | ne → né | |  | |
| 157 | norm | `orig/reg` | 179r | seg-c8-s40-padrone-assoluto | ne → né | |  | |
| 158 | norm | `orig/reg` | 179r | seg-c8-s40-padrone-assoluto | ne → né | |  | |
| 159 | norm | `orig/reg` | 179r | seg-c8-s41-continua-oratione | ne → né | |  | |
| 160 | norm | `orig/reg` | 179r | seg-c8-s42-sostanziale-unione | ne → né | |  | |
| 161 | norm | `orig/reg` | 179r | seg-c8-s43-mare-simile | ne → né | |  | |
| 162 | norm | `orig/reg` | 179v | seg-c8-s45-tesoro | ne → né | |  | |
| 163 | norm | `orig/reg` | 179v | seg-c8-s45-tesoro |  → scarsizza | |  | |
| 164 | norm | `orig/reg` | 179v | seg-c8-s45-tesoro | ne → né | |  | |
| 165 | norm | `orig/reg` | 195r | seg-c14p2-ignoranza-nascosta | à → a | |  | |
| 166 | norm | `orig/reg` | 195r | seg-c14p2-ignoranza-nascosta | per che → perché | |  | |
| 167 | gen | `add` | 158r | seg-158r-incapacitas | substitution | #ink_1 |  | i |
| 168 | gen | `add` | 158v | seg-c4-pace2 | substitution | #ink_1 |  | e |
| 169 | gen | `add` | 158v | seg-c7-viaggio | substitution | #ink_1 |  | e |
| 170 | gen | `add` | 159v | seg-c2p1-obbedienza-incipit | substitution | #ink_1 |  | a |
| 171 | gen | `add` | 159v | seg-c2p3-comparatione-teresa | supralinear | #ink_3-dark | medium | adacquar |
| 172 | gen | `add` | 160v | seg-c2p10-linguaggio-oscuro | substitution | #ink_1 |  | i |
| 173 | gen | `add` | 161v | seg-c2p16-silentio-non-parla | substitution | #ink_1 |  | i |
| 174 | gen | `add` | 161v | seg-c2p19-demonio-escluso | substitution | #ink_1 |  | i |
| 175 | gen | `add` | 162r | seg-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 176 | gen | `add` | 162v | seg-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 177 | gen | `add` | 162v | seg-c3p1-esortazione | substitution | #ink_1 |  | o |
| 178 | gen | `add` | 162v | seg-c3p3-raccoglimento | supralinear | #ink_1 |  |  |
| 179 | gen | `add` | 163r | seg-c3p5-sole-verita | supralinear | #ink_1 |  | va |
| 180 | gen | `add` | 163v | seg-c3p7-declaratio-verita | substitution | #ink_1 |  | a |
| 181 | gen | `add` | 163v | seg-c3p7-declaratio-verita | substitution | #ink_1 |  | i |
| 182 | gen | `add` | 164v | seg-c3p14-cisterna | substitution | #ink_1 |  | i |
| 183 | gen | `add` | 164v | seg-c3p14-mirabilia | margin-left | #ink_3-dark | medium | dico ciò non |
| 184 | gen | `add` | 165r | seg-c4p5-precisatio-sospensione | substitution | #ink_1 |  | i |
| 185 | gen | `add` | 167r | seg-c5p7-amore-prossimo | substitution | #ink_1 |  | e |
| 186 | gen | `add` | 167r | seg-c5p8-non-desiderar-croce | supralinear | #ink_1 |  | ar |
| 187 | gen | `add` | 167r | seg-c5p9-non-desiderar-morte | margin-left | #ink_1 | medium | Ciò s'intende per non |
| 188 | gen | `add` | 167r | seg-c5p10-palla-cera | inline | #ink_3-dark | medium | Ciò non s'intende a cose di male, ma che |
| 189 | gen | `add` | 176r | seg-c8-s7-riequilibrio-vita | margin | #ink_3-dark | medium | sì bene lo |
| 190 | gen | `add` | 176v | seg-c8-s14-quattroparti | substitution | #ink_1 |  | i |
| 191 | gen | `add` | 178r | seg-c8-s32-replica-hore | supralinear | #ink_1 |  | cioè |
| 192 | gen | `add` | 179r | seg-c8-s41-continua-oratione | margin-right | #ink_3-dark | medium | sì bene i sensi non donano in desordene, |
| 193 | gen | `add` | 193r | seg-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | e |
| 194 | gen | `add` | 193r | seg-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | o |
| 195 | gen | `del` | 158r | seg-158r-invocatio | correction | #ink_1 |  | to |
| 196 | gen | `del` | 158r | seg-158r-incapacitas | correction | #ink_1 |  | e |
| 197 | gen | `del` | 158v | seg-c4-pace2 | correction | #ink_1 |  | a |
| 198 | gen | `del` | 158v | seg-c7-viaggio | correction | #ink_1 |  | è |
| 199 | gen | `del` | 159r | seg-c10-unione-velata | correction | #ink_1 |  | sc |
| 200 | gen | `del` | 159v | seg-c2p1-obbedienza-incipit | correction | #ink_1 |  | e |
| 201 | gen | `del` | 159v | seg-c2p3-comparatione-teresa | deletion | #ink_1 |  | o |
| 202 | gen | `del` | 159v | seg-c2p3-comparatione-teresa | deletion | #ink_1 |  |  |
| 203 | gen | `del` | 160r | seg-c2p4-giardino-quiete | deletion | #ink_1 |  | o |
| 204 | gen | `del` | 160r | seg-c2p6-differenza-raccoglimento | deletion | #ink_1 |  |  |
| 205 | gen | `del` | 160v | seg-c2p10-linguaggio-oscuro | correction | #ink_1 |  | e |
| 206 | gen | `del` | 160v | seg-c2p10-linguaggio-oscuro | deletion | #ink_1 |  | d. |
| 207 | gen | `del` | 161r | seg-c2p13-castellano-secreto | deletion | #ink_1 |  |  |
| 208 | gen | `del` | 161r | seg-c2p15-comunicazione-diretta | deletion | #ink_1 |  |  |
| 209 | gen | `del` | 161v | seg-c2p15-comunicazione-diretta | deletion | #ink_1 |  | diff |
| 210 | gen | `del` | 161v | seg-c2p16-silentio-non-parla | correction | #ink_1 |  | e |
| 211 | gen | `del` | 161v | seg-c2p19-demonio-escluso | correction | #ink_1 |  | e |
| 212 | gen | `del` | 162r | seg-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 213 | gen | `del` | 162v | seg-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 214 | gen | `del` | 162v | seg-c3p1-esortazione | correction | #ink_1 |  | a |
| 215 | gen | `del` | 162v | seg-c3p1-santamadre | deletion | #ink_1 |  |  |
| 216 | gen | `del` | 162v | seg-c3p2-definizione-oblio | deletion | #ink_1 |  | , |
| 217 | gen | `del` | 162v | seg-c3p3-raccoglimento | deletion | #ink_1 |  | sonno |
| 218 | gen | `del` | 163r | seg-c3p4-opera-divina | deletion | #ink_1 |  | di |
| 219 | gen | `del` | 163r | seg-c3p5-propriastima | deletion | #ink_1 |  | s. |
| 220 | gen | `del` | 163v | seg-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 221 | gen | `del` | 163v | seg-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 222 | gen | `del` | 163v | seg-c3p7-statuette | deletion | #ink_1 |  | di silen |
| 223 | gen | `del` | 164r | seg-c3p12-linguaggio | deletion | #ink_1 |  |  |
| 224 | gen | `del` | 164v | seg-c3p14-cisterna | correction | #ink_1 |  | e |
| 225 | gen | `del` | 165r | seg-c4p3-ineffabilita-labirinto | deletion | #ink_1 |  | pa |
| 226 | gen | `del` | 165r | seg-c4p5-precisatio-sospensione | correction | #ink_1 |  | e |
| 227 | gen | `del` | 167r | seg-c5p7-amore-prossimo | correction | #ink_1 |  | a |
| 228 | gen | `del` | 167r | seg-c5p9-non-desiderar-morte | deletion | #ink_1 |  | , |
| 229 | gen | `del` | 167v | seg-c5p12-affetti-persi | deletion | #ink_1 |  | che |
| 230 | gen | `del` | 167v | seg-c5p16-tocchi-sostanza | deletion | #ink_1 |  | vecchi |
| 231 | gen | `del` | 175v | - | deletion | #ink_1 |  | se |
| 232 | gen | `del` | 176v | seg-c8-s12-distrattioni | deletion | #ink_1 |  | co |
| 233 | gen | `del` | 176v | seg-c8-s14-quattroparti | correction | #ink_1 |  | e |
| 234 | gen | `del` | 177v | seg-c8-s24-bocca-sostanza | deletion | #ink_1 |  | d |
| 235 | gen | `del` | 177v | seg-c8-s25-contatto-gloria | deletion | #ink_1 |  | intende |
| 236 | gen | `del` | 178r | seg-c8-s30-esorto-hore | deletion | #ink_1 |  | t |
| 237 | gen | `del` | 178r | seg-c8-s31-sicurta-cadute | deletion | #ink_1 |  | , |
| 238 | gen | `del` | 179r | seg-c8-s38-estremi-sole | deletion | #ink_1 |  |  |
| 239 | gen | `del` | 179r | seg-c8-s39-propria-stima | deletion | #ink_1 |  | che |
| 240 | gen | `del` | 193r | seg-c12p2-atteggiare-acquisita | correction | #ink_1 |  | a |
| 241 | gen | `del` | 193r | seg-c12p2-atteggiare-acquisita | correction | #ink_1 |  | e |
| 242 | gen | `del` | 193r | seg-c12p3-ricevere-consenso | deletion | #ink_1 |  | con |
| 243 | gen | `del` | 193r | seg-c12p4-addormentarsi-amato | deletion | #ink_1 |  |  |
| 244 | gen | `del` | 193v | seg-c12p5-atti-continui | deletion | #ink_1 |  | per |
| 245 | gen | `del` | 193v | seg-c12p7-otio-possesso | deletion | #ink_1 |  | f |
| 246 | gen | `del` | 193v | seg-c12p7-otio-possesso | deletion | #ink_1 |  | sopr. |
| 247 | gen | `del` | 195r | seg-c14p1-ombra-chiarezza | deletion | #ink_1 |  | , |
| 248 | gen | `del` | 195v | seg-c14p5-sapienza-agonia | deletion | #ink_1 |  | s'an |
| 249 | gen | `del` | 195v | seg-c14p6-ombra-certezza | deletion | #ink_1 |  |  |
| 250 | gen | `subst` | 159v | seg-c2p1-obbedienza-incipit |  |  |  |  |
| 251 | gen | `subst` | 160v | seg-c2p10-linguaggio-oscuro |  |  |  |  |
| 252 | gen | `subst` | 161v | seg-c2p16-silentio-non-parla |  |  |  |  |
| 253 | gen | `subst` | 161v | seg-c2p19-demonio-escluso |  |  |  |  |
| 254 | gen | `subst` | 162r | seg-c3p1-ripugnanza |  |  |  |  |
| 255 | gen | `subst` | 162v | seg-c3p1-ripugnanza |  |  |  |  |
| 256 | gen | `subst` | 162v | seg-c3p1-esortazione |  |  |  |  |
| 257 | gen | `subst` | 163v | seg-c3p7-declaratio-verita |  |  |  |  |
| 258 | gen | `subst` | 163v | seg-c3p7-declaratio-verita |  |  |  |  |
| 259 | gen | `subst` | 164v | seg-c3p14-cisterna |  |  |  |  |
| 260 | gen | `subst` | 165r | seg-c4p5-precisatio-sospensione |  |  |  |  |
| 261 | gen | `subst` | 167r | seg-c5p7-amore-prossimo |  |  |  |  |
| 262 | gen | `subst` | 176v | seg-c8-s14-quattroparti |  |  |  |  |
| 263 | gen | `subst` | 193r | seg-c12p2-atteggiare-acquisita |  |  |  |  |
| 264 | gen | `subst` | 193r | seg-c12p2-atteggiare-acquisita |  |  |  |  |
| 265 | gen | `retrace` | 159v | seg-c2p2-fondo-anima |  | #ink_3-dark | medium | col tem |
| 266 | gen | `retrace` | 160v | seg-c2p10-linguaggio-oscuro |  | #ink_3-dark | medium | è |
| 267 | gen | `retrace` | 161v | seg-c2p19-demonio-escluso |  | #ink_3-dark | medium | fingere |
| 268 | gen | `retrace` | 163r | seg-c3p4-fondoraccolto |  | #ink_3-dark | medium | tom |
| 269 | gen | `retrace` | 163r | seg-c3p5-chiarezza |  | #ink_3-dark | medium | te |
| 270 | gen | `retrace` | 163v | seg-c3p7-declaratio-verita |  | #ink_3-dark | medium | conchi |
| 271 | gen | `retrace` | 164r | seg-c3p9-fortezza |  | #ink_3-dark | medium | e |
| 272 | gen | `retrace` | 164r | seg-c3p11-comunicazione |  | #ink_3-dark | medium | r |
| 273 | gen | `retrace` | 164v | seg-c3p13-santotio |  | #ink_3-dark | medium | m |
| 274 | gen | `retrace` | 164v | seg-c3p13-santotio |  | #ink_3-dark | medium | n |
| 275 | gen | `retrace` | 164v | seg-c3p14-mirabilia |  | #ink_3-dark | medium | ter |
| 276 | gen | `retrace` | 164v | seg-c4p2-attuale-habituale |  | #ink_3-dark | medium | attoale |
| 277 | gen | `retrace` | 165r | seg-c4p3-ineffabilita-labirinto |  | #ink_3-dark | medium | licenza |
| 278 | gen | `retrace` | 165r | seg-c4p7-nuova-caccia-vecchia |  | #ink_3-dark | medium | tesoro |
| 279 | gen | `retrace` | 166v | seg-c5p4-distinzione-matrimonio |  | #ink_3-dark | low | tutti |
| 280 | gen | `retrace` | 166v | seg-c5p6-cessano-zeli |  | #ink_3-dark | medium | zeli |
| 281 | gen | `retrace` | 167v | seg-c5p12-affetti-persi |  | #ink_3-dark | medium | affetti |
| 282 | gen | `retrace` | 176r | seg-c8-s5-morte-vitanuova |  | #ink_3-dark | medium | m |
| 283 | gen | `retrace` | 177r | seg-c8-s20-lambino |  | #ink_3-dark | medium | lambino |
| 284 | gen | `retrace` | 177v | seg-c8-s25-contatto-gloria |  | #ink_3-dark | medium | con |
| 285 | gen | `retrace` | 177v | seg-c8-s25-contatto-gloria |  | #ink_3-dark | medium | co |
| 286 | gen | `retrace` | 177v | seg-c8-s26-cella-chiarezza |  | #ink_3-dark | medium | ricittavolo |
| 287 | gen | `retrace` | 178r | seg-c8-s30-esorto-hore |  | #ink_3-dark | medium | tras |
| 288 | gen | `retrace` | 179v | seg-c8-s45-tesoro |  | #ink_3-dark | medium | scarsizza |
| 289 | gen | `gap` | 159r | seg-c10-unione-velata | illegible |  |  |  |
| 290 | gen | `gap` | 159r | - | hole |  |  |  |
| 291 | gen | `gap` | 159v | seg-c2p3-comparatione-teresa | illegible |  |  |  |
| 292 | gen | `gap` | 160r | seg-c2p6-differenza-raccoglimento | illegible |  |  |  |
| 293 | gen | `gap` | 161r | seg-c2p13-castellano-secreto | illegible |  |  |  |
| 294 | gen | `gap` | 161r | seg-c2p15-comunicazione-diretta | illegible |  |  |  |
| 295 | gen | `gap` | 162v | seg-c3p1-santamadre | illegible |  |  |  |
| 296 | gen | `gap` | 162v | seg-c3p1-santamadre | hole |  |  |  |
| 297 | gen | `gap` | 163r | seg-c3p5-propriastima | hole |  |  |  |
| 298 | gen | `gap` | 163v | seg-c3p7-statuette | hole |  |  |  |
| 299 | gen | `gap` | 163v | seg-c3p7-magnificar | hole |  |  |  |
| 300 | gen | `gap` | 164r | seg-c3p12-linguaggio | illegible |  |  |  |
| 301 | gen | `gap` | 164v | seg-c3p14-mirabilia | hole |  |  |  |
| 302 | gen | `gap` | 164v | seg-c3p14-mirabilia | hole |  |  |  |
| 303 | gen | `gap` | 167r | seg-c5p9-non-desiderar-morte | hole |  |  |  |
| 304 | gen | `gap` | 178r | seg-c8-s30-esorto-hore | illegible |  |  |  |
| 305 | gen | `gap` | 179r | seg-c8-s38-estremi-sole | illegible |  |  |  |
| 306 | gen | `gap` | 179r | seg-c8-s39-propria-stima | illegible |  |  |  |
| 307 | gen | `gap` | 193r | seg-c12p4-addormentarsi-amato | illegible |  |  |  |
| 308 | gen | `gap` | 195v | seg-c14p6-ombra-certezza | illegible |  |  |  |
| 309 | gen | `supplied` | 159r | - | hole |  | medium | e |
| 310 | gen | `supplied` | 160r | seg-c2p5-sposo-quiete | hole |  | medium | e |
| 311 | gen | `supplied` | 160v | seg-c2p12-castello-fondo | hole |  | medium | u |
| 312 | gen | `supplied` | 161r | seg-c2p13-castellano-secreto | hole |  | medium | e |
| 313 | gen | `supplied` | 161v | seg-c2p18-pace-continua | hole |  | medium | io |
| 314 | gen | `supplied` | 162r | seg-c2p20-autonomia-direttore | hole |  | medium | a |
| 315 | gen | `supplied` | 162v | seg-c3p1-santamadre | hole |  | medium | i |
| 316 | gen | `supplied` | 163r | seg-c3p5-propriastima | hole |  | medium | nt |
| 317 | gen | `supplied` | 163v | seg-c3p7-statuette | hole |  | medium | a |
| 318 | gen | `supplied` | 163v | seg-c3p7-magnificar | hole |  | medium | i |
| 319 | gen | `supplied` | 164v | seg-c3p14-mirabilia | hole |  | medium | modo |
| 320 | gen | `supplied` | 164v | seg-c3p14-mirabilia | hole |  | medium | arse |
| 321 | gen | `supplied` | 165r | seg-c4p8-conclusio | hole |  | medium | a |
| 322 | gen | `supplied` | 166v | seg-c5p6-non-capace-pena | hole |  | medium | e |
| 323 | gen | `supplied` | 167r | seg-c5p7-amore-prossimo | hole |  | medium | i |
| 324 | gen | `supplied` | 167r | seg-c5p9-non-desiderar-morte | hole |  | medium | e |
| 325 | gen | `supplied` | 167r | seg-c5p9-non-desiderar-morte | hole |  | medium | o |
| 326 | gen | `supplied` | 175v | seg-c8-s3-roma | hole |  | medium | v |
| 327 | gen | `supplied` | 177r | seg-c8-s20-lambino | hole |  | medium | a |
| 328 | gen | `supplied` | 177v | seg-c8-s24-bocca-sostanza | hole |  | medium | a |
| 329 | gen | `supplied` | 179r | seg-c8-s41-continua-oratione | hole |  | medium | oratione |
