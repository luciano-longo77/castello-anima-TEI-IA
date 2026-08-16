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
| `orig/reg` | 167 | 0 | 0 | globale (`editorialDecl`): `@resp` = 0 |
| `sic/corr` | 20 | 20 | 20 | per-istanza: `@resp` e `@cert` = n |
| `abbr/expan` | 16 | 0 | 5 | globale; `@cert` solo dove pertinente |

## 2. Piano genetico (lavoro sul foglio)

| elemento | n | con `@hand` | con `@cert` |
|---|---:|---:|---:|
| `add` | 91 | 91 | 7 |
| `del` | 139 | 139 | 1 |
| `subst` | 25 | 0 | 0 |
| `retrace` | 52 | 52 | 34 |
| `gap` | 54 | 0 | 0 |
| `supplied` | 104 | 0 | 104 |

### 2.1 Dettaglio dei valori

| attributo | valori (conteggio) |
|---|---|
| `del/@type` | `correction` (20) · `deletion` (119) |
| `del/@rend` | `strikethrough` (119) |
| `del/@place` | `inline` (131) |
| `add/@type` | `substitution` (21) |
| `add/@place` | `bottom` (1) · `infralinear` (2) · `inline` (26) · `margin` (2) · `margin-bottom` (1) · `margin-left` (8) · `margin-right` (9) · `supralinear` (34) |
| `gap/@reason` | `hole` (23) · `illegible` (31) |
| `gap/@unit` | `char` (49) · `chars` (2) · `word` (3) |
| `supplied/@reason` | `hole` (101) · `stain` (3) |
| `retrace/@hand` | `#ink_1` (52) |
| `retrace/@cert` | `medium` (34) |

## 3. Controlli di coerenza

**Nessun rilievo.** I due piani sono coerenti con la policy dichiarata: `reg`/`expan` senza `@resp` (attribuzione globale), `corr` pienamente attribuito, ogni `supplied` con `@resp`+`@cert`, ogni `subst` = `add`+`del`.

## 4. Appendice · dettaglio per-istanza

*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, `seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*

| # | piano | elemento | carta | seg | tipo/valore | mano | cert | testo |
|---:|---|---|---|---|---|---|---|---|
| 1 | norm | `abbr/expan` | 158r | - | I.M.I. → Iesus Maria Ioseph | | high | |
| 2 | norm | `sic/corr` | 158r | seg-b3-pro-p1-obedienza | sapere → sapete | | high | |
| 3 | norm | `sic/corr` | 158r | seg-b3-pro-p1-autodemotio | l'opera nostra → l'opere nostre | | high | |
| 4 | norm | `sic/corr` | 158r | seg-b3-pro-p1-invocatio | domandano → domandavo | | medium | |
| 5 | norm | `orig/reg` | 158r | seg-b3-pro-p1-invocatio | à → a | |  | |
| 6 | norm | `sic/corr` | 158r | seg-b3-pro-p1-invocatio | noi → voi | | medium | |
| 7 | norm | `sic/corr` | 158r | seg-b3-pro-p1-invocatio | nostro → vostro | | medium | |
| 8 | norm | `orig/reg` | 158r | seg-b3-pro-p1-invocatio | agiuuto → agiuto | |  | |
| 9 | norm | `orig/reg` | 158r | seg-b3-pro-p1-invocatio | à → a | |  | |
| 10 | norm | `orig/reg` | 158r | seg-b3-pro-p1-incapacitas | poiche → poiché | |  | |
| 11 | norm | `sic/corr` | 158r | seg-b3-pro-p1-incapacitas | trattano → trattavo | | high | |
| 12 | norm | `sic/corr` | 158r | seg-b3-pro-p2-declaratio | contra di chi → contradichi | | medium | |
| 13 | norm | `orig/reg` | 158r | seg-b3-c1p1-croce | altri tanto → altritanto | |  | |
| 14 | norm | `orig/reg` | 158r | seg-b3-c1p1-pace | à → a | |  | |
| 15 | norm | `sic/corr` | 158v | seg-b3-c1p1-scala | ad → al | | high | |
| 16 | norm | `abbr/expan` | 158v | seg-b3-c1p2-notte | dunq → dunque | |  | |
| 17 | norm | `orig/reg` | 158v | seg-b3-c1p2-notte | ed'unirsi → ed unirsi | |  | |
| 18 | norm | `sic/corr` | 158v | - | suo → secondo | | medium | |
| 19 | norm | `orig/reg` | 158v | seg-b3-c1p3-purga | ne → né | |  | |
| 20 | norm | `orig/reg` | 158v | seg-b3-c1p4-pace2 | de' i → dei | |  | |
| 21 | norm | `sic/corr` | 158v | seg-b3-c1p4-pace2 | la → le | | high | |
| 22 | norm | `orig/reg` | 158v | seg-b3-c1p4-arca | ed'altri → ed altri | |  | |
| 23 | norm | `orig/reg` | 158v | seg-b3-c1p4-astinuata | e → e' | |  | |
| 24 | norm | `orig/reg` | 158v | seg-b3-c1p5-intro | ad'intendire → ad intendire | |  | |
| 25 | norm | `orig/reg` | 158v | seg-b3-c1p6-statua | Cossi → Cossì | |  | |
| 26 | norm | `orig/reg` | 158v | seg-b3-c1p6-statua | à → a | |  | |
| 27 | norm | `orig/reg` | 158v | seg-b3-c1p6-statua | ed' esposta → ed esposta | |  | |
| 28 | norm | `orig/reg` | 158v | seg-b3-c1p7-attesa | ne → né | |  | |
| 29 | norm | `orig/reg` | 158v | seg-b3-c1p7-attesa | ne → né | |  | |
| 30 | norm | `orig/reg` | 158v | seg-b3-c1p7-viaggio | quì → qui | |  | |
| 31 | norm | `orig/reg` | 158v | seg-b3-c1p7-viaggio | à → a | |  | |
| 32 | norm | `orig/reg` | 158v | seg-b3-c1p7-viaggio | à → a | |  | |
| 33 | norm | `orig/reg` | 159r | seg-b3-c1p7-reposa | ne'i → nei | |  | |
| 34 | norm | `orig/reg` | 159r | seg-b3-c1p7-reposa | ò → o | |  | |
| 35 | norm | `orig/reg` | 159r | seg-b3-c1p7-reposa | per che → perché | |  | |
| 36 | norm | `orig/reg` | 159r | seg-b3-c1p8-desiderio | à → a | |  | |
| 37 | norm | `abbr/expan` | 159r | seg-b3-c1p8-desiderio | qualunq → qualunque | |  | |
| 38 | norm | `orig/reg` | 159r | seg-b3-c1p8-desiderio | à → a | |  | |
| 39 | norm | `orig/reg` | 159r | seg-b3-c1p8-desiderio | ne meno → né meno | |  | |
| 40 | norm | `abbr/expan` | 159r | seg-b3-c1p8-desiderio | dunq → dunque | |  | |
| 41 | norm | `abbr/expan` | 159r | seg-b3-c1p8-concopiscibile | qualunq → qualunque | |  | |
| 42 | norm | `orig/reg` | 159r | seg-b3-c1p9-precis2 | poiche → poiché | |  | |
| 43 | norm | `orig/reg` | 159r | seg-b3-c1p9-precis2 | hò → ho | |  | |
| 44 | norm | `orig/reg` | 159r | seg-b3-c1p10-unione-velata | scuopri → scuoprì | |  | |
| 45 | norm | `orig/reg` | 159r | seg-b3-c1p11-nuovavita | à → a | |  | |
| 46 | norm | `orig/reg` | 159r | seg-b3-c1p11-quiete | poiche → poiché | |  | |
| 47 | norm | `abbr/expan` | 159r | seg-b3-c1p11-quiete | qualunq → qualunque | |  | |
| 48 | norm | `orig/reg` | 161r | seg-b3-c2p13-castellano-secreto | e → è | |  | |
| 49 | norm | `orig/reg` | 161v | seg-b3-c2p15-comunicazione-diretta | e → è | |  | |
| 50 | norm | `orig/reg` | 161v | seg-b3-c2p15-comunicazione-diretta | E → È | |  | |
| 51 | norm | `orig/reg` | 162r | - | sù → su | |  | |
| 52 | norm | `orig/reg` | 162r | - | ò → o | |  | |
| 53 | norm | `orig/reg` | 162r | seg-b3-c3p1-donnecciola | poiche → poiché | |  | |
| 54 | norm | `abbr/expan` | 162r | seg-b3-c3p1-miracolo | dun → dunque | |  | |
| 55 | norm | `abbr/expan` | 162r | seg-b3-c3p1-miracolo | V.R. → Vostra Reverenza | | high | |
| 56 | norm | `sic/corr` | 162r | seg-b3-c3p1-miracolo | miracoloso → miracolo | | medium | |
| 57 | norm | `orig/reg` | 162r | seg-b3-c3p1-ripugnanza | raggione → ragione | |  | |
| 58 | norm | `orig/reg` | 162r | seg-b3-c3p1-ripugnanza | poiche → poiché | |  | |
| 59 | norm | `orig/reg` | 162r | seg-b3-c3p1-ripugnanza | ne → né | |  | |
| 60 | norm | `sic/corr` | 162r | seg-b3-c3p1-ripugnanza | trattare → trattarne | | medium | |
| 61 | norm | `orig/reg` | 162v | seg-b3-c3p1-esortazione | difficoltosa → difficoltosa | |  | |
| 62 | norm | `orig/reg` | 162v | seg-b3-c3p1-esortazione | dobij → dobii | |  | |
| 63 | norm | `orig/reg` | 162v | seg-b3-c3p1-esortazione | poiche → poiché | |  | |
| 64 | norm | `sic/corr` | 162v | seg-b3-c3p1-esortazione | che → chi | | medium | |
| 65 | norm | `orig/reg` | 162v | seg-b3-c3p1-santamadre | o → obedienza | |  | |
| 66 | norm | `orig/reg` | 162v | seg-b3-c3p1-santamadre | perche → perché | |  | |
| 67 | norm | `sic/corr` | 162v | seg-b3-c3p2-definizione-oblio | detto stato → dello stato | | medium | |
| 68 | norm | `orig/reg` | 162v | seg-b3-c3p2-definizione-oblio | ò → o | |  | |
| 69 | norm | `orig/reg` | 162v | seg-b3-c3p2-definizione-oblio | adormentarsi → adormentarsi | |  | |
| 70 | norm | `abbr/expan` | 162v | seg-b3-c3p3-differenza-sonno | dunq → dunque | |  | |
| 71 | norm | `orig/reg` | 162v | seg-b3-c3p3-differenza-sonno | poiche → poiché | |  | |
| 72 | norm | `orig/reg` | 162v | seg-b3-c3p3-internarsi | poiche → poiché | |  | |
| 73 | norm | `orig/reg` | 163r | seg-b3-c3p3-interpell | poiche → poiché | |  | |
| 74 | norm | `orig/reg` | 163r | seg-b3-c3p3-interpell | ò → o | |  | |
| 75 | norm | `orig/reg` | 163r | seg-b3-c3p3-interpell | poiche → poiché | |  | |
| 76 | norm | `abbr/expan` | 163r | seg-b3-c3p4-fondoraccolto | qualunq → qualunque | |  | |
| 77 | norm | `orig/reg` | 163r | seg-b3-c3p4-fondoraccolto | o → o | |  | |
| 78 | norm | `orig/reg` | 163r | seg-b3-c3p4-abbraccio | e → è | |  | |
| 79 | norm | `orig/reg` | 163r | seg-b3-c3p5-similitudine-sole | poiche → poiché | |  | |
| 80 | norm | `sic/corr` | 163r | seg-b3-c3p5-sole-verita | possa → porta | | medium | |
| 81 | norm | `orig/reg` | 163r | seg-b3-c3p5-propriastima | poiche → poiché | |  | |
| 82 | norm | `abbr/expan` | 163r | seg-b3-c3p6-tenebre | V.R. → Vostra Reverenza | | high | |
| 83 | norm | `sic/corr` | 163r | seg-b3-c3p6-luce-soprannaturale | questà → quella | | medium | |
| 84 | norm | `orig/reg` | 163v | seg-b3-c3p7-declaratio-verita | poiche → poiché | |  | |
| 85 | norm | `orig/reg` | 164r | seg-b3-c3p9-fortezza | e → è | |  | |
| 86 | norm | `sic/corr` | 164r | seg-b3-c3p9-certezza | poi → più | | medium | |
| 87 | norm | `orig/reg` | 164r | seg-b3-c3p9-desiderio | desiderii → desiderii | |  | |
| 88 | norm | `orig/reg` | 164r | seg-b3-c3p9-desiderio | poiche → poiché | |  | |
| 89 | norm | `sic/corr` | 164r | seg-b3-c3p9-desiderio | possedendo → possedendolo | | medium | |
| 90 | norm | `orig/reg` | 164r | seg-b3-c3p9-desiderio | perche → perché | |  | |
| 91 | norm | `orig/reg` | 164r | seg-b3-c3p9-desiderio | posesso → posesso | |  | |
| 92 | norm | `orig/reg` | 164r | seg-b3-c3p12-linguaggio | ne → né | |  | |
| 93 | norm | `sic/corr` | 164r | seg-b3-c3p12-oscurita | questa → creda | | medium | |
| 94 | norm | `abbr/expan` | 164r | seg-b3-c3p12-oscurita | V.R. → Vostra Reverenza | | high | |
| 95 | norm | `orig/reg` | 164r | seg-b3-c3p12-oscurita | poiche → poiché | |  | |
| 96 | norm | `orig/reg` | 164v | seg-b3-c3p14-cisterna | à → a | |  | |
| 97 | norm | `orig/reg` | 164v | seg-b3-c3p14-mirabilia | Ò → O | |  | |
| 98 | norm | `orig/reg` | 164v | seg-b3-c3p14-mirabilia | perche → perché | |  | |
| 99 | norm | `orig/reg` | 164v | seg-b3-c3p14-mirabilia | perche → perché | |  | |
| 100 | norm | `orig/reg` | 168r | seg-b3-c5p17-conclusio | ha → a | |  | |
| 101 | norm | `orig/reg` | 168r | seg-b3-c6p1-matrimonio-intro | hà → a | |  | |
| 102 | norm | `orig/reg` | 171r | seg-b3-c6p23-immobilita-sensibili | ne hà → né a | |  | |
| 103 | norm | `orig/reg` | 173r | seg-b3-c7p1-esordio-inadeguatezza | hò → ho | |  | |
| 104 | norm | `orig/reg` | 173v | seg-b3-c7p5-ineffabilita-preterizione | poiche → poiché | |  | |
| 105 | norm | `orig/reg` | 173v | seg-b3-c7p7-sicurta-sposo | poiche → poiché | |  | |
| 106 | norm | `orig/reg` | 173v | seg-b3-c7p7-sicurta-sposo | hò → ho | |  | |
| 107 | norm | `orig/reg` | 173v | seg-b3-c7p9-precisazione-operare-participatione | hò → ho | |  | |
| 108 | norm | `orig/reg` | 174r | seg-b3-c7p12-dichiarazione-ortodossia-consomato | hò → ho | |  | |
| 109 | norm | `orig/reg` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | hò → ho | |  | |
| 110 | norm | `orig/reg` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | hò → ho | |  | |
| 111 | norm | `orig/reg` | 175v | seg-b3-c8p1-secretum | Perciò → perciò | |  | |
| 112 | norm | `orig/reg` | 175v | seg-b3-c8p1-secretum | ne → né | |  | |
| 113 | norm | `abbr/expan` | 175v | seg-b3-c8p1-secretum | Dunq → Dunque | |  | |
| 114 | norm | `sic/corr` | 175v | seg-b3-c8p2-roma | E → È | | medium | |
| 115 | norm | `orig/reg` | 175v | seg-b3-c8p2-roma | ne → né | |  | |
| 116 | norm | `orig/reg` | 175v | seg-b3-c8p2-roma | poiche → poiché | |  | |
| 117 | norm | `orig/reg` | 175v | seg-b3-c8p2-roma | ne → né | |  | |
| 118 | norm | `orig/reg` | 175v | seg-b3-c8p3-cella-ineffabile | ne → né | |  | |
| 119 | norm | `orig/reg` | 175v | seg-b3-c8p3-cella-ineffabile | ne → né | |  | |
| 120 | norm | `orig/reg` | 175v | seg-b3-c8p3-cella-ineffabile | poiche → poiché | |  | |
| 121 | norm | `orig/reg` | 175v | seg-b3-c8p3-cella-ineffabile | ne → né | |  | |
| 122 | norm | `orig/reg` | 175v | seg-b3-c8p3-cella-ineffabile | poiche → poiché | |  | |
| 123 | norm | `orig/reg` | 176r | seg-b3-c8p4-fuoco | perché → perché | |  | |
| 124 | norm | `orig/reg` | 176r | seg-b3-c8p4-fuoco | poiche → poiché | |  | |
| 125 | norm | `orig/reg` | 176r | seg-b3-c8p4-riequilibrio-vita | Perciò → Perciò | |  | |
| 126 | norm | `orig/reg` | 176r | seg-b3-c8p5-programma | poiche → poiché | |  | |
| 127 | norm | `orig/reg` | 176r | seg-b3-c8p5-programma | poiche → poiché | |  | |
| 128 | norm | `orig/reg` | 176r | seg-b3-c8p6-sensi-sposalitio | poiche → poiché | |  | |
| 129 | norm | `orig/reg` | 176r | seg-b3-c8p6-sensi-sposalitio | o → o | |  | |
| 130 | norm | `orig/reg` | 176r | seg-b3-c8p6-sensi-sposalitio | poiche → poiché | |  | |
| 131 | norm | `abbr/expan` | 176r | seg-b3-c8p6-musica | V.G. → Vostra Grazia | | high | |
| 132 | norm | `orig/reg` | 176v | seg-b3-c8p8-distrattioni | Ne → Né | |  | |
| 133 | norm | `orig/reg` | 176v | seg-b3-c8p9-passioni | benché → benché | |  | |
| 134 | norm | `abbr/expan` | 176v | seg-b3-c8p10-quattroparti | dunq → dunque | |  | |
| 135 | norm | `orig/reg` | 177r | seg-b3-c8p11-divisione-inferiore | o → o | |  | |
| 136 | norm | `orig/reg` | 177r | seg-b3-c8p11-divisione-inferiore | perché → perché | |  | |
| 137 | norm | `orig/reg` | 177r | seg-b3-c8p12-spirito-fondo | o → o | |  | |
| 138 | norm | `orig/reg` | 177r | seg-b3-c8p12-divisione-strana | poiche → poiché | |  | |
| 139 | norm | `orig/reg` | 177r | seg-b3-c8p12-divisione-strana | perché → perché | |  | |
| 140 | norm | `orig/reg` | 177r | seg-b3-c8p12-divisione-strana | distinguere → distinguere | |  | |
| 141 | norm | `orig/reg` | 177r | seg-b3-c8p13-pura-sostanza | perché → perché | |  | |
| 142 | norm | `orig/reg` | 177r | seg-b3-c8p13-pura-sostanza | perché → perché | |  | |
| 143 | norm | `orig/reg` | 177v | seg-b3-c8p16-comunicazione | poiche → poiché | |  | |
| 144 | norm | `orig/reg` | 177v | seg-b3-c8p17-non-sospensione | poiche → poiché | |  | |
| 145 | norm | `orig/reg` | 177v | seg-b3-c8p18-bocca-sostanza | perciò → perciò | |  | |
| 146 | norm | `orig/reg` | 178r | seg-b3-c8p21-possesso-inseparabile | poiche → poiché | |  | |
| 147 | norm | `orig/reg` | 178r | seg-b3-c8p21-possesso-inseparabile | ne → né | |  | |
| 148 | norm | `orig/reg` | 178r | seg-b3-c8p21-guardia-temere | ne → né | |  | |
| 149 | norm | `orig/reg` | 178r | seg-b3-c8p21-esorto-hore | ne → né | |  | |
| 150 | norm | `orig/reg` | 178r | seg-b3-c8p21-esorto-hore | poiche → poiché | |  | |
| 151 | norm | `orig/reg` | 178r | seg-b3-c8p21-esorto-hore | e → è | |  | |
| 152 | norm | `orig/reg` | 178r | seg-b3-c8p21-esorto-hore | e → è | |  | |
| 153 | norm | `orig/reg` | 178r | seg-b3-c8p22-replica-hore | ne → né | |  | |
| 154 | norm | `orig/reg` | 178r | seg-b3-c8p22-replica-hore | rindimento → rindimento | |  | |
| 155 | norm | `orig/reg` | 178v | seg-b3-c8p22-totalmente-passiva | poiche → poiché | |  | |
| 156 | norm | `orig/reg` | 178v | seg-b3-c8p22-opera-quiete | perché → perché | |  | |
| 157 | norm | `orig/reg` | 178v | seg-b3-c8p22-opera-quiete | poiche → poiché | |  | |
| 158 | norm | `orig/reg` | 178v | seg-b3-c8p23-mortificatione | perciò → perciò | |  | |
| 159 | norm | `abbr/expan` | 178v | seg-b3-c8p23-mortificatione | dunq → dunque | |  | |
| 160 | norm | `orig/reg` | 178v | seg-b3-c8p24-felice-notte | Poiche → Poiché | |  | |
| 161 | norm | `orig/reg` | 179r | seg-b3-c8p25-estremi-sole | e → è | |  | |
| 162 | norm | `orig/reg` | 179r | seg-b3-c8p25-estremi-sole | e → è | |  | |
| 163 | norm | `orig/reg` | 179r | seg-b3-c8p25-propria-stima | poiche → poiché | |  | |
| 164 | norm | `orig/reg` | 179r | seg-b3-c8p26-padrone-assoluto | ne → né | |  | |
| 165 | norm | `orig/reg` | 179r | seg-b3-c8p26-padrone-assoluto | ne → né | |  | |
| 166 | norm | `orig/reg` | 179r | seg-b3-c8p26-padrone-assoluto | ne → né | |  | |
| 167 | norm | `orig/reg` | 179r | seg-b3-c8p26-padrone-assoluto | ne → né | |  | |
| 168 | norm | `orig/reg` | 179r | seg-b3-c8p26-padrone-assoluto | ne → né | |  | |
| 169 | norm | `orig/reg` | 179r | seg-b3-c8p27-continua-oratione | ne → né | |  | |
| 170 | norm | `orig/reg` | 179r | seg-b3-c8p27-sostanziale-unione | ne → né | |  | |
| 171 | norm | `orig/reg` | 179r | seg-b3-c8p28-mare-simile | ne → né | |  | |
| 172 | norm | `orig/reg` | 179v | seg-b3-c8p29-tesoro | ne → né | |  | |
| 173 | norm | `orig/reg` | 179v | seg-b3-c8p29-tesoro |  → scarsizza | |  | |
| 174 | norm | `orig/reg` | 179v | seg-b3-c8p29-tesoro | ne → né | |  | |
| 175 | norm | `orig/reg` | 183r | seg-b3-c10p8-riequilibrio-fatica | e → è | |  | |
| 176 | norm | `orig/reg` | 195r | seg-b3-c14p2-ignoranza-nascosta | à → a | |  | |
| 177 | norm | `orig/reg` | 195r | seg-b3-c14p2-ignoranza-nascosta | per che → perché | |  | |
| 178 | norm | `orig/reg` | 197v | seg-b3-c16p5-contatto-abbraccio | e → è | |  | |
| 179 | norm | `orig/reg` | 197v | seg-b3-c16p5-contatto-abbraccio | e → è | |  | |
| 180 | norm | `orig/reg` | 199r | seg-b3-c16p17-segno-aridita | e → è | |  | |
| 181 | norm | `orig/reg` | 199r | seg-b3-c16p18-non-perdita-tempo | e → è | |  | |
| 182 | norm | `orig/reg` | 199v | seg-b3-c16p21-mutazione-desiderio | E → È | |  | |
| 183 | norm | `orig/reg` | 201r | seg-b3-c16p28-niente-trasformatione | E → È | |  | |
| 184 | norm | `orig/reg` | 202r | seg-b3-c16p34-desideri-nuovi | e → è | |  | |
| 185 | norm | `orig/reg` | 202r | seg-b3-c16p34-desideri-nuovi | pero → però | |  | |
| 186 | norm | `orig/reg` | 207r | seg-b3-c19p3-precisazione-gratia | e → è | |  | |
| 187 | norm | `orig/reg` | 207v | seg-b3-c19p5-definizione-supernaturale | perche → perché | |  | |
| 188 | norm | `orig/reg` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | E → È | |  | |
| 189 | norm | `orig/reg` | 208v | seg-b3-c19p11-riepilogo-gradi | e → è | |  | |
| 190 | norm | `orig/reg` | 246v | seg-b3-c34p4-corpo-spirituale | e → è | |  | |
| 191 | norm | `orig/reg` | 247r | seg-b3-c34p4-distinzione-eucaristia | E → È | |  | |
| 192 | norm | `orig/reg` | 247r | seg-b3-c34p5-trionfante-resurrezione | e → è | |  | |
| 193 | norm | `orig/reg` | 247r | seg-b3-c34p6-mutatione-oscuro | e → è | |  | |
| 194 | norm | `orig/reg` | 247v | seg-b3-c34p8-timore-filiale | E → È | |  | |
| 195 | norm | `orig/reg` | 247v | seg-b3-c34p10-indifferenza-desideri | e → è | |  | |
| 196 | norm | `orig/reg` | 248r | seg-b3-c34p13-nota-autobiografica | è → e | |  | |
| 197 | norm | `orig/reg` | 256r | seg-b3-c38p2-nuova-crocifissione | e → è | |  | |
| 198 | norm | `orig/reg` | 256v | seg-b3-c38p4-aridita-continua | e → è | |  | |
| 199 | norm | `orig/reg` | 256v | seg-b3-c38p5-oratione-arida | e → è | |  | |
| 200 | norm | `orig/reg` | 258v | seg-b3-c38p18-fede-oscurata | e → è | |  | |
| 201 | norm | `orig/reg` | 262v | seg-b3-c40p4-dardo-amore | e → è | |  | |
| 202 | norm | `orig/reg` | 262v | seg-b3-c40p4-dardo-amore | e → è | |  | |
| 203 | norm | `orig/reg` | 263r | seg-b3-c40p7-declaratio-dossologia | e → è | |  | |
| 204 | gen | `add` | 158r | seg-b3-pro-p1-incapacitas | substitution | #ink_1 |  | i |
| 205 | gen | `add` | 158v | seg-b3-c1p4-pace2 | substitution | #ink_1 |  | e |
| 206 | gen | `add` | 158v | seg-b3-c1p7-viaggio | substitution | #ink_1 |  | e |
| 207 | gen | `add` | 159v | seg-b3-c2p1-obbedienza-incipit | substitution | #ink_1 |  | a |
| 208 | gen | `add` | 159v | seg-b3-c2p3-comparatione-teresa | supralinear | #ink_3-dark | medium | adacquar |
| 209 | gen | `add` | 160v | seg-b3-c2p10-linguaggio-oscuro | substitution | #ink_1 |  | i |
| 210 | gen | `add` | 161v | seg-b3-c2p16-silentio-non-parla | substitution | #ink_1 |  | i |
| 211 | gen | `add` | 161v | seg-b3-c2p19-demonio-escluso | substitution | #ink_1 |  | i |
| 212 | gen | `add` | 161v | seg-b3-c2p19-demonio-escluso | substitution | #ink_1 |  | g |
| 213 | gen | `add` | 162r | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 214 | gen | `add` | 162v | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 215 | gen | `add` | 162v | seg-b3-c3p1-esortazione | substitution | #ink_1 |  | o |
| 216 | gen | `add` | 162v | seg-b3-c3p3-raccoglimento | supralinear | #ink_1 |  |  |
| 217 | gen | `add` | 163r | seg-b3-c3p5-sole-verita | supralinear | #ink_1 |  | va |
| 218 | gen | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | a |
| 219 | gen | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | i |
| 220 | gen | `add` | 164v | seg-b3-c3p14-cisterna | substitution | #ink_1 |  | i |
| 221 | gen | `add` | 164v | seg-b3-c3p14-mirabilia | margin-left | #ink_3-dark | medium | dico ciò non |
| 222 | gen | `add` | 165r | seg-b3-c4p5-precisatio-sospensione | substitution | #ink_1 |  | i |
| 223 | gen | `add` | 166v | seg-b3-c5p4-distinzione-matrimonio | substitution | #ink_1 |  | i |
| 224 | gen | `add` | 167r | seg-b3-c5p7-amore-prossimo | substitution | #ink_1 |  | e |
| 225 | gen | `add` | 167r | seg-b3-c5p8-non-desiderar-croce | supralinear | #ink_1 |  | ar |
| 226 | gen | `add` | 167r | seg-b3-c5p9-non-desiderar-morte | margin-left | #ink_1 | medium | Ciò s'intende per non |
| 227 | gen | `add` | 167r | seg-b3-c5p10-palla-cera | inline | #ink_3-dark | medium | Ciò non s'intende a cose di male, ma che |
| 228 | gen | `add` | 168r | seg-b3-c6p2-trasformazione-fomite | margin-right | #ink_3-dark |  | More alli mali habiti dell' |
| 229 | gen | `add` | 168r | seg-b3-c6p3-morire-spogliarsi | supralinear | #ink_1 |  | con |
| 230 | gen | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-right | #ink_3-dark |  | ciò perché l' |
| 231 | gen | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-bottom | #ink_3-dark |  | in questi tempi viene tanto supeditato d |
| 232 | gen | `add` | 169r | seg-b3-c6p8-innocenza-guardia | margin-right | #ink_3-dark |  | però sappiasi che siemo in via, tememo,  |
| 233 | gen | `add` | 169r | seg-b3-c6p8-innocenza-guardia | supralinear | #ink_1 |  | mo |
| 234 | gen | `add` | 169r | seg-b3-c6p9-discernimento-guardia | supralinear | #ink_1 |  | le |
| 235 | gen | `add` | 169r | seg-b3-c6p10-impassibilita-guardia | supralinear | #ink_1 |  | dine |
| 236 | gen | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | quasi |
| 237 | gen | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | pe |
| 238 | gen | `add` | 170v | seg-b3-c6p18-dilatazione-sostanza | supralinear | #ink_1 |  | ché |
| 239 | gen | `add` | 171r | seg-b3-c6p22-fiamma-estasi | supralinear | #ink_1 |  | alle volte |
| 240 | gen | `add` | 173r | - | supralinear | #ink_1 |  | fa |
| 241 | gen | `add` | 173r | seg-b3-c7p2-chiamata-talamo | inline | #ink_1 |  | ì |
| 242 | gen | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | margin-left | #ink_1 |  | questo s'intende per qua |
| 243 | gen | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | supralinear | #ink_1 |  | n |
| 244 | gen | `add` | 174r | seg-b3-c7p12-dichiarazione-ortodossia-consomato | margin-right | #ink_3-dark |  | quasi |
| 245 | gen | `add` | 174v | seg-b3-c7p17-glossa-fortezza-timore | margin-left | #ink_1 |  | cioè per la |
| 246 | gen | `add` | 174v | seg-b3-c7p17-glossa-desiderio-temporaneo | margin-left | #ink_1 |  | cioè per qualche tempo dura il |
| 247 | gen | `add` | 176r | seg-b3-c8p4-riequilibrio-vita | margin | #ink_3-dark | medium | sì bene lo |
| 248 | gen | `add` | 176v | seg-b3-c8p10-quattroparti | substitution | #ink_1 |  | i |
| 249 | gen | `add` | 178r | seg-b3-c8p22-replica-hore | supralinear | #ink_1 |  | cioè |
| 250 | gen | `add` | 179r | seg-b3-c8p27-continua-oratione | margin-right | #ink_3-dark | medium | sì bene i sensi non donano in desordene, |
| 251 | gen | `add` | 182r | seg-b3-c10p1-apertura-esortativa | supralinear | #ink_1 |  | a |
| 252 | gen | `add` | 182r | seg-b3-c10p2-descrizione-soggillo | inline | #ink_1 |  | o |
| 253 | gen | `add` | 182r | seg-b3-c10p3-discernimento-modalita | inline | #ink_1 |  | o |
| 254 | gen | `add` | 182r | seg-b3-c10p4-attenuazione-impeccabilita | inline | #ink_1 |  | o |
| 255 | gen | `add` | 182v | seg-b3-c10p6-precisazione-volonta | margin | #ink_3-dark |  | cioè non ha sensi, e passioni tanto vive |
| 256 | gen | `add` | 183r | seg-b3-c10p8-riequilibrio-fatica | supralinear | #ink_3-dark |  | le |
| 257 | gen | `add` | 183r | seg-b3-c10p10-paradosso-tutto-niente | inline | #ink_1 |  | e |
| 258 | gen | `add` | 183v | seg-b3-c10p12-preterizione-annichilazione | inline | #ink_1 |  | i |
| 259 | gen | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | e |
| 260 | gen | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | o |
| 261 | gen | `add` | 195v | seg-b3-c14p9-unione-durata | substitution | #ink_1 |  | s |
| 262 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | solo |
| 263 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | ancora |
| 264 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | margin-right | #ink_1 |  | E viene l'anima a non credere più quanto |
| 265 | gen | `add` | 200v | seg-b3-c16p25-allegoria-re | supralinear | #ink_3-dark |  | stanza |
| 266 | gen | `add` | 209r | seg-b3-c19p12-definizione-quiete | supralinear | #ink_1 |  | sua |
| 267 | gen | `add` | 209r | seg-b3-c19p14-definizione-amore-potenze | inline | #ink_3-dark |  | n |
| 268 | gen | `add` | 209v | seg-b3-c19p19-definizione-matrimonio | supralinear | #ink_1 |  | fa |
| 269 | gen | `add` | 210r | seg-b3-c19p24-rimando-metatestuale | margin-left | #ink_1 |  | Doppo d'haver fornito questo capitolo, e |
| 270 | gen | `add` | 219v | seg-b3-c24p6-prudenza-penitenza | supralinear | #ink_1 |  | giorni |
| 271 | gen | `add` | 220r | seg-b3-c24p7-imitazione-bestemmie | supralinear | #ink_1 |  | no |
| 272 | gen | `add` | 220v | seg-b3-c24p13-fiducia-abbandono | supralinear | #ink_1 |  | i |
| 273 | gen | `add` | 221r | seg-b3-c24p16-glossa-humanita | margin-right | #ink_3-dark |  | cioè non che la |
| 274 | gen | `add` | 242v | seg-b3-c32p5-notte-luce | supralinear | #ink_1 |  | so |
| 275 | gen | `add` | 247r | seg-b3-c34p6-mutatione-oscuro | supralinear | #ink_1 |  | habituale |
| 276 | gen | `add` | 247r | seg-b3-c34p7-effetti-taciuti | supralinear | #ink_1 |  | la gratia di |
| 277 | gen | `add` | 247v | seg-b3-c34p11-riequilibrio-patire | supralinear | #ink_1 |  | a |
| 278 | gen | `add` | 248v | seg-b3-c34p17-humilta-precipitare | supralinear | #ink_1 |  | e |
| 279 | gen | `add` | 256v | seg-b3-c38p5-oratione-arida | supralinear | #ink_1 |  | mio |
| 280 | gen | `add` | 257v | seg-b3-c38p9-brama-padre-preghiera | supralinear | #ink_1 |  | in |
| 281 | gen | `add` | 257v | seg-b3-c38p11-benevolenza-honore | supralinear | #ink_1 |  | r |
| 282 | gen | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | supralinear | #ink_1 |  | queste |
| 283 | gen | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | margin-right | #ink_3-dark | medium | ; e questo del palar tanto mi pareva pes |
| 284 | gen | `add` | 258v | seg-b3-c38p18-fede-oscurata | supralinear | #ink_1 |  | no |
| 285 | gen | `add` | 258v | seg-b3-c38p19-dichiaro-permettendo | bottom | #ink_1 |  | Qui mi dichiaro che |
| 286 | gen | `add` | 259r | - | inline | #ink_3-dark |  | per quanto può stare in via |
| 287 | gen | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | inline | #ink_3-dark |  | cioè fuor della sua capacetà, ma |
| 288 | gen | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | infralinear | #ink_1 |  | di essa |
| 289 | gen | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | inline | #ink_3-dark |  | cioè questa libertà perduta non intento  |
| 290 | gen | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | infralinear | #ink_1 |  | o altre cose simili |
| 291 | gen | `add` | 260v | seg-b3-c39p12b-annichilazione | supralinear | #ink_1 |  | e a |
| 292 | gen | `add` | 261v | seg-b3-c39p16-declaratio-antipanteismo | inline | #ink_3-dark |  | Io mi dichiaro che in tutte queste sorti |
| 293 | gen | `add` | 262r | seg-b3-c39p21-corredenzione | inline | #ink_3-dark |  | Ciò s'intende unir li soi martiri con qu |
| 294 | gen | `add` | 262v | seg-b3-c40p3-sonno-corpo | margin-right | #ink_1 |  | S'intende però che il spirituali |
| 295 | gen | `del` | 158r | seg-b3-pro-p1-invocatio | correction | #ink_1 |  | to |
| 296 | gen | `del` | 158r | seg-b3-pro-p1-incapacitas | correction | #ink_1 |  | e |
| 297 | gen | `del` | 158v | seg-b3-c1p4-pace2 | correction | #ink_1 |  | a |
| 298 | gen | `del` | 158v | seg-b3-c1p7-viaggio | correction | #ink_1 |  | è |
| 299 | gen | `del` | 159r | seg-b3-c1p10-unione-velata | correction | #ink_1 |  | sc |
| 300 | gen | `del` | 159v | seg-b3-c2p1-obbedienza-incipit | correction | #ink_1 |  | e |
| 301 | gen | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  | o |
| 302 | gen | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  |  |
| 303 | gen | `del` | 160r | seg-b3-c2p4-giardino-quiete | deletion | #ink_1 |  | o |
| 304 | gen | `del` | 160r | seg-b3-c2p6-differenza-raccoglimento | deletion | #ink_1 |  |  |
| 305 | gen | `del` | 160v | seg-b3-c2p10-linguaggio-oscuro | correction | #ink_1 |  | e |
| 306 | gen | `del` | 160v | seg-b3-c2p10-linguaggio-oscuro | deletion | #ink_1 |  | d. |
| 307 | gen | `del` | 161r | seg-b3-c2p13-castellano-secreto | deletion | #ink_1 |  |  |
| 308 | gen | `del` | 161r | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  |  |
| 309 | gen | `del` | 161v | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  | diff |
| 310 | gen | `del` | 161v | seg-b3-c2p16-silentio-non-parla | correction | #ink_1 |  | e |
| 311 | gen | `del` | 161v | seg-b3-c2p19-demonio-escluso | correction | #ink_1 |  | e |
| 312 | gen | `del` | 161v | seg-b3-c2p19-demonio-escluso | deletion | #ink_1 |  | c |
| 313 | gen | `del` | 162r | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 314 | gen | `del` | 162v | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 315 | gen | `del` | 162v | seg-b3-c3p1-esortazione | correction | #ink_1 |  | a |
| 316 | gen | `del` | 162v | seg-b3-c3p1-santamadre | deletion | #ink_1 |  |  |
| 317 | gen | `del` | 162v | seg-b3-c3p2-definizione-oblio | deletion | #ink_1 |  | , |
| 318 | gen | `del` | 162v | seg-b3-c3p3-raccoglimento | deletion | #ink_1 |  | sonno |
| 319 | gen | `del` | 163r | seg-b3-c3p4-opera-divina | deletion | #ink_1 |  | di |
| 320 | gen | `del` | 163r | seg-b3-c3p5-propriastima | deletion | #ink_1 |  | s. |
| 321 | gen | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 322 | gen | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 323 | gen | `del` | 163v | seg-b3-c3p7-statuette | deletion | #ink_1 |  | di silen |
| 324 | gen | `del` | 164r | seg-b3-c3p12-linguaggio | deletion | #ink_1 |  |  |
| 325 | gen | `del` | 164v | seg-b3-c3p14-cisterna | correction | #ink_1 |  | e |
| 326 | gen | `del` | 165r | seg-b3-c4p3-ineffabilita-labirinto | deletion | #ink_1 |  | pa |
| 327 | gen | `del` | 165r | seg-b3-c4p5-precisatio-sospensione | correction | #ink_1 |  | e |
| 328 | gen | `del` | 166v | seg-b3-c5p4-distinzione-matrimonio | deletion | #ink_1 |  | a |
| 329 | gen | `del` | 167r | seg-b3-c5p7-amore-prossimo | correction | #ink_1 |  | a |
| 330 | gen | `del` | 167r | seg-b3-c5p9-non-desiderar-morte | deletion | #ink_1 |  | , |
| 331 | gen | `del` | 167v | seg-b3-c5p12-affetti-persi | deletion | #ink_1 |  | che |
| 332 | gen | `del` | 167v | seg-b3-c5p16-tocchi-sostanza | deletion | #ink_1 |  | vecchi |
| 333 | gen | `del` | 168r | seg-b3-c6p4-fomite-peccato | deletion | #ink_1 |  |  |
| 334 | gen | `del` | 169r | seg-b3-c6p8-innocenza-guardia | deletion | #ink_1 |  | npe |
| 335 | gen | `del` | 169r | seg-b3-c6p8b-mondo-beati | deletion | #ink_1 |  |  |
| 336 | gen | `del` | 169r | seg-b3-c6p8b-mondo-beati | deletion | #ink_1 |  | d |
| 337 | gen | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 338 | gen | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 339 | gen | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | dire |
| 340 | gen | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | r |
| 341 | gen | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | e |
| 342 | gen | `del` | 169v | seg-b3-c6p12-castello-anima | deletion | #ink_1 |  | ed |
| 343 | gen | `del` | 169v | seg-b3-c6p12-castello-anima | deletion | #ink_1 |  | centro |
| 344 | gen | `del` | 170r | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  | tutt |
| 345 | gen | `del` | 170r | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  | dis |
| 346 | gen | `del` | 170v | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  |  |
| 347 | gen | `del` | 170v | seg-b3-c6p20-consumazione-dolce | deletion | #ink_1 |  | co |
| 348 | gen | `del` | 170v | seg-b3-c6p21-braggia-similitudine | deletion | #ink_1 |  |  |
| 349 | gen | `del` | 171v | seg-b3-c6p26-esposti-guardia | deletion | #ink_1 |  |  |
| 350 | gen | `del` | 172v | seg-b3-c6p32-monte-similitudine | deletion | #ink_1 |  | congio |
| 351 | gen | `del` | 172v | seg-b3-c6p33-puo-cadere-guardia | deletion | #ink_1 |  | Dio |
| 352 | gen | `del` | 172v | seg-b3-c6p33-puo-cadere-guardia | deletion | #ink_1 |  |  |
| 353 | gen | `del` | 173r | seg-b3-c7p2-chiamata-talamo | deletion | #ink_1 |  | e |
| 354 | gen | `del` | 173v | seg-b3-c7p9-precisazione-operare-participatione | deletion | #ink_1 |  | ed |
| 355 | gen | `del` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | deletion | #ink_1 |  |  |
| 356 | gen | `del` | 174v | seg-b3-c7p21-similitudine-cera-sole | deletion | #ink_1 |  | per |
| 357 | gen | `del` | 175r | seg-b3-c7p22-fiamma-fuoco | deletion | #ink_1 |  | ap |
| 358 | gen | `del` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | deletion | #ink_1 |  | pop |
| 359 | gen | `del` | 175v | - | deletion | #ink_1 |  | se |
| 360 | gen | `del` | 176v | seg-b3-c8p8-distrattioni | deletion | #ink_1 |  | co |
| 361 | gen | `del` | 176v | seg-b3-c8p10-quattroparti | correction | #ink_1 |  | e |
| 362 | gen | `del` | 177v | seg-b3-c8p18-bocca-sostanza | deletion | #ink_1 |  | d |
| 363 | gen | `del` | 177v | seg-b3-c8p19-contatto-gloria | deletion | #ink_1 |  | intende |
| 364 | gen | `del` | 178r | seg-b3-c8p21-esorto-hore | deletion | #ink_1 |  | t |
| 365 | gen | `del` | 178r | seg-b3-c8p21-sicurta-cadute | deletion | #ink_1 |  | , |
| 366 | gen | `del` | 179r | seg-b3-c8p25-estremi-sole | deletion | #ink_1 |  |  |
| 367 | gen | `del` | 179r | seg-b3-c8p25-propria-stima | deletion | #ink_1 |  | che |
| 368 | gen | `del` | 182r | seg-b3-c10p1-apertura-esortativa | deletion | #ink_1 |  | , |
| 369 | gen | `del` | 182r | seg-b3-c10p2-descrizione-soggillo | deletion | #ink_1 |  | e |
| 370 | gen | `del` | 182r | seg-b3-c10p3-discernimento-modalita | deletion | #ink_1 |  | e |
| 371 | gen | `del` | 182r | seg-b3-c10p4-attenuazione-impeccabilita | deletion | #ink_1 |  | e |
| 372 | gen | `del` | 182v | seg-b3-c10p6-precisazione-volonta | deletion | #ink_1 |  | nella |
| 373 | gen | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 374 | gen | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 375 | gen | `del` | 183r | seg-b3-c10p8-riequilibrio-fatica | deletion | #ink_1 |  |  |
| 376 | gen | `del` | 183r | seg-b3-c10p10-paradosso-tutto-niente | deletion | #ink_1 |  | a |
| 377 | gen | `del` | 183v | seg-b3-c10p12-preterizione-annichilazione | deletion | #ink_1 |  | e |
| 378 | gen | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | a |
| 379 | gen | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | e |
| 380 | gen | `del` | 193r | seg-b3-c12p3-ricevere-consenso | deletion | #ink_1 |  | con |
| 381 | gen | `del` | 193r | seg-b3-c12p4-addormentarsi-amato | deletion | #ink_1 |  |  |
| 382 | gen | `del` | 193v | seg-b3-c12p5-atti-continui | deletion | #ink_1 |  | per |
| 383 | gen | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | f |
| 384 | gen | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | sopr. |
| 385 | gen | `del` | 195r | seg-b3-c14p1-ombra-chiarezza | deletion | #ink_1 |  | , |
| 386 | gen | `del` | 195v | seg-b3-c14p5-sapienza-agonia | deletion | #ink_1 |  | s'an |
| 387 | gen | `del` | 195v | seg-b3-c14p6-ombra-certezza | deletion | #ink_1 |  |  |
| 388 | gen | `del` | 195v | seg-b3-c14p9-unione-durata | deletion | #ink_1 |  | c |
| 389 | gen | `del` | 198v | seg-b3-c16p15-molte-strade | deletion | #ink_1 |  | sa |
| 390 | gen | `del` | 198v | seg-b3-c16p15-molte-strade | deletion | #ink_1 |  | à |
| 391 | gen | `del` | 198v | seg-b3-c16p16-liberta-passione | deletion | #ink_1 |  | t |
| 392 | gen | `del` | 199v | seg-b3-c16p21-mutazione-desiderio | deletion | #ink_1 |  | non |
| 393 | gen | `del` | 200v | seg-b3-c16p25-allegoria-re | deletion | #ink_1 | low | p |
| 394 | gen | `del` | 200v | seg-b3-c16p27-cortina-attributi | deletion | #ink_1 |  | un |
| 395 | gen | `del` | 201r | seg-b3-c16p27-cortina-attributi | deletion | #ink_1 |  | una |
| 396 | gen | `del` | 201r | seg-b3-c16p28-niente-trasformatione | deletion | #ink_1 |  |  |
| 397 | gen | `del` | 201v | seg-b3-c16p34-desideri-nuovi | deletion | #ink_1 |  | e |
| 398 | gen | `del` | 202r | seg-b3-c16p37-certezza-niente | deletion | #ink_1 |  |  |
| 399 | gen | `del` | 202v | seg-b3-c16p39-capi-eresia | deletion | #ink_1 |  | s'accol |
| 400 | gen | `del` | 207r | seg-b3-c19p3-precisazione-gratia | deletion | #ink_1 |  | al |
| 401 | gen | `del` | 207v | seg-b3-c19p4-definizione-amicitia | deletion | #ink_1 |  | super |
| 402 | gen | `del` | 207v | seg-b3-c19p5-definizione-supernaturale | deletion | #ink_1 |  | non |
| 403 | gen | `del` | 207v | seg-b3-c19p5-definizione-supernaturale | deletion | #ink_1 |  | che |
| 404 | gen | `del` | 208v | seg-b3-c19p10-critica-mondanita | deletion | #ink_1 |  | , |
| 405 | gen | `del` | 208v | seg-b3-c19p11-riepilogo-gradi | deletion | #ink_1 |  | super |
| 406 | gen | `del` | 208v | seg-b3-c19p12-definizione-quiete | deletion | #ink_1 |  | no |
| 407 | gen | `del` | 208v | seg-b3-c19p12-definizione-quiete | deletion | #ink_1 |  | che |
| 408 | gen | `del` | 209v | seg-b3-c19p21-definizione-corpo-cristo | deletion | #ink_1 |  | o |
| 409 | gen | `del` | 209v | seg-b3-c19p22-partecipazione-corpo | deletion | #ink_1 |  | , |
| 410 | gen | `del` | 220v | seg-b3-c24p12-abbandono-padre | deletion | #ink_1 |  | intorela |
| 411 | gen | `del` | 220v | seg-b3-c24p13-fiducia-abbandono | deletion | #ink_1 |  | or |
| 412 | gen | `del` | 220v | seg-b3-c24p13-fiducia-abbandono | deletion | #ink_1 |  | , |
| 413 | gen | `del` | 221r | seg-b3-c24p16-imitazione-passione | deletion | #ink_1 |  | d |
| 414 | gen | `del` | 221r | seg-b3-c24p16-glossa-humanita | deletion | #ink_3-dark |  | G |
| 415 | gen | `del` | 242v | seg-b3-c32p4-unione-vera-croce | deletion | #ink_1 |  | che |
| 416 | gen | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | di Dio |
| 417 | gen | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | detta |
| 418 | gen | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | s |
| 419 | gen | `del` | 246v | seg-b3-c34p2-principii-lode | deletion | #ink_1 |  | far |
| 420 | gen | `del` | 246v | seg-b3-c34p4-corpo-spirituale | deletion | #ink_1 |  | r |
| 421 | gen | `del` | 247r | seg-b3-c34p7-effetti-taciuti | deletion | #ink_1 |  | sccano |
| 422 | gen | `del` | 247r | seg-b3-c34p7-effetti-taciuti | deletion | #ink_1 |  | , |
| 423 | gen | `del` | 248v | seg-b3-c34p17-olimpo-altezza | deletion | #ink_1 |  | t |
| 424 | gen | `del` | 257v | seg-b3-c38p9-brama-padre-preghiera | deletion | #ink_1 |  |  |
| 425 | gen | `del` | 258r | seg-b3-c38p13-persecutione-terzapersona | deletion | #ink_1 |  | tanti |
| 426 | gen | `del` | 258r | seg-b3-c38p17-miracolo-supernaturale | deletion | #ink_1 |  | che |
| 427 | gen | `del` | 258v | seg-b3-c38p18-fede-oscurata | deletion | #ink_1 |  |  |
| 428 | gen | `del` | 258v | seg-b3-c38p19-perdita-fede | deletion | #ink_1 |  |  |
| 429 | gen | `del` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | deletion | #ink_1 |  | in |
| 430 | gen | `del` | 260r | seg-b3-c39p12-cupio-dissolvi | deletion | #ink_1 |  | D |
| 431 | gen | `del` | 261v | seg-b3-c39p19-ricchezza-virtu | deletion | #ink_1 |  | per |
| 432 | gen | `del` | 262r | seg-b3-c39p20-salamandra | deletion | #ink_1 |  | Dio |
| 433 | gen | `del` | 262r | - | deletion | #ink_1 |  | trigesimo |
| 434 | gen | `subst` | 159v | seg-b3-c2p1-obbedienza-incipit |  |  |  |  |
| 435 | gen | `subst` | 160v | seg-b3-c2p10-linguaggio-oscuro |  |  |  |  |
| 436 | gen | `subst` | 161v | seg-b3-c2p16-silentio-non-parla |  |  |  |  |
| 437 | gen | `subst` | 161v | seg-b3-c2p19-demonio-escluso |  |  |  |  |
| 438 | gen | `subst` | 161v | seg-b3-c2p19-demonio-escluso |  |  |  |  |
| 439 | gen | `subst` | 162r | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 440 | gen | `subst` | 162v | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 441 | gen | `subst` | 162v | seg-b3-c3p1-esortazione |  |  |  |  |
| 442 | gen | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 443 | gen | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 444 | gen | `subst` | 164v | seg-b3-c3p14-cisterna |  |  |  |  |
| 445 | gen | `subst` | 165r | seg-b3-c4p5-precisatio-sospensione |  |  |  |  |
| 446 | gen | `subst` | 166v | seg-b3-c5p4-distinzione-matrimonio |  |  |  |  |
| 447 | gen | `subst` | 167r | seg-b3-c5p7-amore-prossimo |  |  |  |  |
| 448 | gen | `subst` | 173r | seg-b3-c7p2-chiamata-talamo |  |  |  |  |
| 449 | gen | `subst` | 176v | seg-b3-c8p10-quattroparti |  |  |  |  |
| 450 | gen | `subst` | 182r | seg-b3-c10p2-descrizione-soggillo |  |  |  |  |
| 451 | gen | `subst` | 182r | seg-b3-c10p3-discernimento-modalita |  |  |  |  |
| 452 | gen | `subst` | 182r | seg-b3-c10p4-attenuazione-impeccabilita |  |  |  |  |
| 453 | gen | `subst` | 183r | seg-b3-c10p10-paradosso-tutto-niente |  |  |  |  |
| 454 | gen | `subst` | 183v | seg-b3-c10p12-preterizione-annichilazione |  |  |  |  |
| 455 | gen | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 456 | gen | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 457 | gen | `subst` | 195v | seg-b3-c14p9-unione-durata |  |  |  |  |
| 458 | gen | `subst` | 220v | seg-b3-c24p13-fiducia-abbandono |  |  |  |  |
| 459 | gen | `retrace` | 159v | seg-b3-c2p2-fondo-anima |  | #ink_1 | medium | tem |
| 460 | gen | `retrace` | 160v | seg-b3-c2p10-linguaggio-oscuro |  | #ink_1 | medium | è |
| 461 | gen | `retrace` | 163r | seg-b3-c3p4-fondoraccolto |  | #ink_1 | medium | tom |
| 462 | gen | `retrace` | 163r | seg-b3-c3p5-chiarezza |  | #ink_1 | medium | te |
| 463 | gen | `retrace` | 163v | seg-b3-c3p7-declaratio-verita |  | #ink_1 | medium | u |
| 464 | gen | `retrace` | 164r | seg-b3-c3p9-fortezza |  | #ink_1 | medium | e |
| 465 | gen | `retrace` | 164r | seg-b3-c3p11-comunicazione |  | #ink_1 | medium | r |
| 466 | gen | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | m |
| 467 | gen | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | n |
| 468 | gen | `retrace` | 164v | seg-b3-c3p14-mirabilia |  | #ink_1 | medium | mino |
| 469 | gen | `retrace` | 164v | seg-b3-c4p2-attuale-habituale |  | #ink_1 | medium | l |
| 470 | gen | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | c |
| 471 | gen | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | n |
| 472 | gen | `retrace` | 165r | seg-b3-c4p7-nuova-caccia-vecchia |  | #ink_1 | medium | s |
| 473 | gen | `retrace` | 166v | seg-b3-c5p6-cessano-zeli |  | #ink_1 | medium | z |
| 474 | gen | `retrace` | 167v | seg-b3-c5p12-affetti-persi |  | #ink_1 | medium | a |
| 475 | gen | `retrace` | 169r | seg-b3-c6p8-innocenza-guardia |  | #ink_1 |  | b |
| 476 | gen | `retrace` | 170v | seg-b3-c6p17-fede-prattica-guardia |  | #ink_1 |  | l |
| 477 | gen | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | n |
| 478 | gen | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | t |
| 479 | gen | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | p |
| 480 | gen | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | g |
| 481 | gen | `retrace` | 170v | seg-b3-c6p22-fiamma-estasi |  | #ink_1 |  | m |
| 482 | gen | `retrace` | 172v | seg-b3-c6p33-puo-cadere-guardia |  | #ink_1 |  | in |
| 483 | gen | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 484 | gen | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 485 | gen | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | c |
| 486 | gen | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | m |
| 487 | gen | `retrace` | 176r | seg-b3-c8p3-morte-vitanuova |  | #ink_1 | medium | m |
| 488 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | r |
| 489 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | m |
| 490 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | t |
| 491 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | n |
| 492 | gen | `retrace` | 176r | seg-b3-c8p6-sensi-sposalitio |  | #ink_1 | medium | nn |
| 493 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | c |
| 494 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 495 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 496 | gen | `retrace` | 177r | seg-b3-c8p15-lambino |  | #ink_1 | medium | lambino |
| 497 | gen | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | tinuo |
| 498 | gen | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | co |
| 499 | gen | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | ricittavolo |
| 500 | gen | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | co |
| 501 | gen | `retrace` | 178r | seg-b3-c8p21-esorto-hore |  | #ink_1 | medium | scu |
| 502 | gen | `retrace` | 179v | seg-b3-c8p29-tesoro |  | #ink_1 | medium | scarsizza |
| 503 | gen | `retrace` | 197v | seg-b3-c16p6-carne-con-carne |  | #ink_1 |  | c |
| 504 | gen | `retrace` | 198v | seg-b3-c16p15-molte-strade |  | #ink_1 |  | r |
| 505 | gen | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | m |
| 506 | gen | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | t |
| 507 | gen | `retrace` | 200v | seg-b3-c16p26-festa-sensi |  | #ink_1 |  | e |
| 508 | gen | `retrace` | 202r | seg-b3-c16p37-certezza-niente |  | #ink_1 |  | e |
| 509 | gen | `retrace` | 219v | seg-b3-c24p2-timore-naturale |  | #ink_1 |  | d |
| 510 | gen | `retrace` | 220v | seg-b3-c24p13-fiducia-abbandono |  | #ink_1 |  | men |
| 511 | gen | `gap` | 159r | seg-b3-c1p10-unione-velata | illegible |  |  |  |
| 512 | gen | `gap` | 159r | - | hole |  |  |  |
| 513 | gen | `gap` | 159v | seg-b3-c2p3-comparatione-teresa | illegible |  |  |  |
| 514 | gen | `gap` | 160r | seg-b3-c2p6-differenza-raccoglimento | illegible |  |  |  |
| 515 | gen | `gap` | 161r | seg-b3-c2p13-castellano-secreto | illegible |  |  |  |
| 516 | gen | `gap` | 161r | seg-b3-c2p15-comunicazione-diretta | illegible |  |  |  |
| 517 | gen | `gap` | 162v | seg-b3-c3p1-santamadre | illegible |  |  |  |
| 518 | gen | `gap` | 162v | seg-b3-c3p1-santamadre | hole |  |  |  |
| 519 | gen | `gap` | 163r | seg-b3-c3p5-propriastima | hole |  |  |  |
| 520 | gen | `gap` | 163v | seg-b3-c3p7-statuette | hole |  |  |  |
| 521 | gen | `gap` | 163v | seg-b3-c3p7-magnificar | hole |  |  |  |
| 522 | gen | `gap` | 164r | seg-b3-c3p12-linguaggio | illegible |  |  |  |
| 523 | gen | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 524 | gen | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 525 | gen | `gap` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  |  |  |
| 526 | gen | `gap` | 168r | seg-b3-c6p3-morire-spogliarsi | illegible |  |  |  |
| 527 | gen | `gap` | 168r | seg-b3-c6p4-fomite-peccato | hole |  |  |  |
| 528 | gen | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 529 | gen | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 530 | gen | `gap` | 169r | seg-b3-c6p8b-mondo-beati | illegible |  |  |  |
| 531 | gen | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 532 | gen | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 533 | gen | `gap` | 170r | seg-b3-c6p15-adamo-guardia | hole |  |  |  |
| 534 | gen | `gap` | 170r | seg-b3-c6p15-adamo-guardia | illegible |  |  |  |
| 535 | gen | `gap` | 170v | seg-b3-c6p17-fede-prattica-guardia | illegible |  |  |  |
| 536 | gen | `gap` | 170v | seg-b3-c6p21-braggia-similitudine | illegible |  |  |  |
| 537 | gen | `gap` | 171v | seg-b3-c6p26-esposti-guardia | illegible |  |  |  |
| 538 | gen | `gap` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  |  |  |
| 539 | gen | `gap` | 178r | seg-b3-c8p21-esorto-hore | illegible |  |  |  |
| 540 | gen | `gap` | 179r | seg-b3-c8p25-estremi-sole | illegible |  |  |  |
| 541 | gen | `gap` | 179r | seg-b3-c8p25-propria-stima | illegible |  |  |  |
| 542 | gen | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 543 | gen | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 544 | gen | `gap` | 183r | seg-b3-c10p8-riequilibrio-fatica | illegible |  |  |  |
| 545 | gen | `gap` | 193r | seg-b3-c12p4-addormentarsi-amato | illegible |  |  |  |
| 546 | gen | `gap` | 195v | seg-b3-c14p6-ombra-certezza | illegible |  |  |  |
| 547 | gen | `gap` | 198v | seg-b3-c16p13-esperienza-propria | hole |  |  |  |
| 548 | gen | `gap` | 201r | seg-b3-c16p28-niente-trasformatione | illegible |  |  |  |
| 549 | gen | `gap` | 202r | seg-b3-c16p37-certezza-niente | illegible |  |  |  |
| 550 | gen | `gap` | 202v | seg-b3-c16p39-capi-eresia | illegible |  |  |  |
| 551 | gen | `gap` | 221r | seg-b3-c24p16-glossa-humanita | hole |  |  |  |
| 552 | gen | `gap` | 246v | seg-b3-c34p3-identita-distinte | hole |  |  |  |
| 553 | gen | `gap` | 248v | seg-b3-c34p17-olimpo-altezza | illegible |  |  |  |
| 554 | gen | `gap` | 257v | seg-b3-c38p9-brama-padre-preghiera | illegible |  |  |  |
| 555 | gen | `gap` | 258v | seg-b3-c38p18-fede-oscurata | illegible |  |  |  |
| 556 | gen | `gap` | 261r | seg-b3-c39p16-annichilazione-insensibile | hole |  |  |  |
| 557 | gen | `gap` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  |  |  |
| 558 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 559 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 560 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 561 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 562 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 563 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 564 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 565 | gen | `supplied` | 159r | - | hole |  | medium | e |
| 566 | gen | `supplied` | 160r | seg-b3-c2p5-sposo-quiete | hole |  | medium | e |
| 567 | gen | `supplied` | 160v | seg-b3-c2p12-castello-fondo | hole |  | medium | u |
| 568 | gen | `supplied` | 161r | seg-b3-c2p13-castellano-secreto | hole |  | medium | e |
| 569 | gen | `supplied` | 161v | seg-b3-c2p18-pace-continua | hole |  | medium | io |
| 570 | gen | `supplied` | 162r | seg-b3-c2p20-autonomia-direttore | hole |  | medium | a |
| 571 | gen | `supplied` | 162v | seg-b3-c3p1-santamadre | hole |  | medium | i |
| 572 | gen | `supplied` | 163r | seg-b3-c3p5-propriastima | hole |  | medium | nt |
| 573 | gen | `supplied` | 163v | seg-b3-c3p7-statuette | hole |  | medium | a |
| 574 | gen | `supplied` | 163v | seg-b3-c3p7-magnificar | hole |  | medium | i |
| 575 | gen | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | modo |
| 576 | gen | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | arse |
| 577 | gen | `supplied` | 165r | seg-b3-c4p8-conclusio | hole |  | medium | à |
| 578 | gen | `supplied` | 166v | seg-b3-c5p6-non-capace-pena | hole |  | medium | e |
| 579 | gen | `supplied` | 167r | seg-b3-c5p7-amore-prossimo | hole |  | medium | i |
| 580 | gen | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | e |
| 581 | gen | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | o |
| 582 | gen | `supplied` | 169r | seg-b3-c6p8-innocenza-guardia | hole |  | high | e |
| 583 | gen | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | a |
| 584 | gen | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | n |
| 585 | gen | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | à |
| 586 | gen | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | a |
| 587 | gen | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | stain |  | medium | n |
| 588 | gen | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | hole |  | medium | ano |
| 589 | gen | `supplied` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | hole |  | medium | s |
| 590 | gen | `supplied` | 174v | seg-b3-c7p17-glossa-fortezza-timore | hole |  | low | deve temere |
| 591 | gen | `supplied` | 175v | seg-b3-c8p2-roma | hole |  | medium | v |
| 592 | gen | `supplied` | 177r | seg-b3-c8p15-lambino | hole |  | medium | a |
| 593 | gen | `supplied` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  | medium | a |
| 594 | gen | `supplied` | 179r | seg-b3-c8p27-continua-oratione | hole |  | medium | oratione |
| 595 | gen | `supplied` | 197r | seg-b3-c16p3-distinzione-unione | hole |  | medium | c |
| 596 | gen | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | ret |
| 597 | gen | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | n |
| 598 | gen | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | a |
| 599 | gen | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | P |
| 600 | gen | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | e |
| 601 | gen | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | Anch |
| 602 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ra |
| 603 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | e |
| 604 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ass |
| 605 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | g |
| 606 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | c |
| 607 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | re |
| 608 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | sa |
| 609 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | rl |
| 610 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | iù |
| 611 | gen | `supplied` | 209v | seg-b3-c19p22-partecipazione-corpo | hole |  | medium | me |
| 612 | gen | `supplied` | 219r | - | hole |  | medium | enta |
| 613 | gen | `supplied` | 220v | seg-b3-c24p10-distinzione-interni | hole |  | medium | cu |
| 614 | gen | `supplied` | 220v | seg-b3-c24p12-abbandono-padre | hole |  | medium | n |
| 615 | gen | `supplied` | 220v | seg-b3-c24p14-critica-padri | hole |  | medium | c |
| 616 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | esse |
| 617 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | nza |
| 618 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | star |
| 619 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | medium | o pare |
| 620 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | e |
| 621 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 622 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 623 | gen | `supplied` | 242r | seg-b3-c32p2-incognito-ineffabile | hole |  | high | a |
| 624 | gen | `supplied` | 242v | seg-b3-c32p2-incognito-ineffabile | hole |  | high | v |
| 625 | gen | `supplied` | 242v | seg-b3-c32p3-trasformazione-crocifisso | hole |  | high | l |
| 626 | gen | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | in |
| 627 | gen | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | è |
| 628 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | croci |
| 629 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | sì co |
| 630 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | li |
| 631 | gen | `supplied` | 246v | seg-b3-c34p3-identita-distinte | hole |  | high | ù |
| 632 | gen | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | ivon |
| 633 | gen | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | no |
| 634 | gen | `supplied` | 248r | seg-b3-c34p13-tentatione-agostino | hole |  | high | i |
| 635 | gen | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | hole |  | high | ne |
| 636 | gen | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | stain |  | medium | e |
| 637 | gen | `supplied` | 256v | seg-b3-c38p4-aridita-continua | hole |  | high | vo |
| 638 | gen | `supplied` | 257r | seg-b3-c38p8-discernimento-brama | hole |  | high | ti |
| 639 | gen | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | i |
| 640 | gen | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | dre |
| 641 | gen | `supplied` | 257v | seg-b3-c38p11-benevolenza-honore | hole |  | high | he |
| 642 | gen | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | ar |
| 643 | gen | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | re |
| 644 | gen | `supplied` | 259r | seg-b3-c39p4-deificatione-imagine | hole |  | high | ic |
| 645 | gen | `supplied` | 259v | seg-b3-c39p5-precisazione-matrimonio | hole |  | medium | perita |
| 646 | gen | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | tro si |
| 647 | gen | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | dal |
| 648 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | stain |  | medium | re |
| 649 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d |
| 650 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d in |
| 651 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d a |
| 652 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | in |
| 653 | gen | `supplied` | 261r | seg-b3-c39p13-silentio-annientamento | hole |  | high | nel |
| 654 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | rtù |
| 655 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | st' |
| 656 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | é |
| 657 | gen | `supplied` | 262r | seg-b3-c39p20-salamandra | hole |  | medium | tan |
| 658 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | p |
| 659 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ti |
| 660 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | pro |
| 661 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ità |
| 662 | gen | `supplied` | 262v | seg-b3-c40p2-cella-intima | hole |  | medium | t |
| 663 | gen | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ugiato |
| 664 | gen | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ett |
| 665 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 666 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | s |
| 667 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 668 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | ho |
