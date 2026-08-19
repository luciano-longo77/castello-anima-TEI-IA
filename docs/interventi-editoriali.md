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
| `orig/reg` | 0 | 0 | 0 | globale (`editorialDecl`): `@resp` = 0 |
| `sic/corr` | 0 | 0 | 0 | per-istanza: `@resp` e `@cert` = n |
| `abbr/expan` | 0 | 0 | 0 | globale; `@cert` solo dove pertinente |

## 2. Piano genetico (lavoro sul foglio)

| elemento | n | con `@hand` | con `@cert` |
|---|---:|---:|---:|
| `add` | 69 | 69 | 7 |
| `del` | 96 | 96 | 0 |
| `subst` | 16 | 0 | 0 |
| `retrace` | 51 | 51 | 33 |
| `gap` | 65 | 0 | 0 |
| `supplied` | 150 | 0 | 150 |

### 2.1 Dettaglio dei valori

| attributo | valori (conteggio) |
|---|---|
| `del/@type` | `correction` (20) · `deletion` (62) |
| `del/@rend` | `strikethrough` (76) |
| `del/@place` | `inline` (74) |
| `add/@type` | `addition` (8) · `substitution` (18) |
| `add/@place` | `bottom` (1) · `infralinear` (2) · `inline` (16) · `margin` (3) · `margin-bottom` (1) · `margin-left` (9) · `margin-right` (9) · `supralinear` (20) |
| `gap/@reason` | `cancelled` (1) · `hole` (24) · `illegible` (40) |
| `gap/@unit` | `char` (59) · `chars` (2) · `word` (4) |
| `supplied/@reason` | `hole` (145) · `omitted` (2) · `stain` (3) |
| `retrace/@hand` | `#ink_1` (51) |
| `retrace/@cert` | `medium` (33) |

## 3. Controlli di coerenza

**Nessun rilievo.** I due piani sono coerenti con la policy dichiarata: `reg`/`expan` senza `@resp` (attribuzione globale), `corr` pienamente attribuito, ogni `supplied` con `@resp`+`@cert`, ogni `subst` = `add`+`del`.

## 4. Appendice · dettaglio per-istanza

*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, `seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*

| # | piano | elemento | carta | seg | tipo/valore | mano | cert | testo |
|---:|---|---|---|---|---|---|---|---|
| 1 | gen | `add` | 1r | seg-b1-c1p1-miseria-creato | substitution | #ink_1 |  | quante |
| 2 | gen | `add` | 9r | seg-b1-c4p47-san-paolo-vocatione | addition | #ink_1 |  | Domine, quid vis me facere? |
| 3 | gen | `add` | 11v | seg-b1-c5p23-conformita-volere | addition | #ink_1 |  | da esser |
| 4 | gen | `add` | 12v | seg-b1-c5p37-humilta-demonio | addition | #ink_1 |  | certa |
| 5 | gen | `add` | 12v | seg-b1-c5p38-humilta-vera-quiete | addition | #ink_1 |  | è vera |
| 6 | gen | `add` | 13v | seg-b1-c5p59-schiava-esempio | addition | #ink_1 |  | sono |
| 7 | gen | `add` | 14r | seg-b1-c6p5-obedienza-penitenza | addition | #ink_1 |  | obedienza |
| 8 | gen | `add` | 21v | seg-b1-c11p28-amor-proprio-cella | addition | #ink_1 |  | più piccole |
| 9 | gen | `add` | 23r | seg-b1-c11p58-carita-cura | addition | #ink_1 |  |  |
| 10 | gen | `add` | 158r | seg-b3-pro-p1-incapacitas | substitution | #ink_1 |  | i |
| 11 | gen | `add` | 158v | seg-b3-c1p4-pace2 | substitution | #ink_1 |  | e |
| 12 | gen | `add` | 158v | seg-b3-c1p7-viaggio | substitution | #ink_1 |  | e |
| 13 | gen | `add` | 159v | seg-b3-c2p1-obbedienza-incipit | substitution | #ink_1 |  | a |
| 14 | gen | `add` | 159v | seg-b3-c2p3-comparatione-teresa | supralinear | #ink_3-dark | medium | adacquar |
| 15 | gen | `add` | 160v | seg-b3-c2p10-linguaggio-oscuro | substitution | #ink_1 |  | i |
| 16 | gen | `add` | 161v | seg-b3-c2p16-silentio-non-parla | substitution | #ink_1 |  | i |
| 17 | gen | `add` | 161v | seg-b3-c2p19-demonio-escluso | substitution | #ink_1 |  | i |
| 18 | gen | `add` | 162r | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 19 | gen | `add` | 162v | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 20 | gen | `add` | 162v | seg-b3-c3p1-esortazione | substitution | #ink_1 |  | o |
| 21 | gen | `add` | 162v | seg-b3-c3p3-raccoglimento | supralinear | #ink_1 |  |  |
| 22 | gen | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | a |
| 23 | gen | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | i |
| 24 | gen | `add` | 164v | seg-b3-c3p14-mirabilia | margin-left | #ink_3-dark | medium | dico ciò non perché non s'ha detto la |
| 25 | gen | `add` | 165r | seg-b3-c4p5-precisatio-sospensione | substitution | #ink_1 |  | i |
| 26 | gen | `add` | 167r | seg-b3-c5p7-amore-prossimo | substitution | #ink_1 |  | e |
| 27 | gen | `add` | 167r | seg-b3-c5p8-non-desiderar-croce | supralinear | #ink_1 |  | ar |
| 28 | gen | `add` | 167r | seg-b3-c5p9-non-desiderar-morte | margin-left | #ink_1 | medium | Ciò s'intende per non |
| 29 | gen | `add` | 167r | seg-b3-c5p10-palla-cera | inline | #ink_3-dark | medium | Ciò non s'intende a cose di male, ma che |
| 30 | gen | `add` | 168r | seg-b3-c6p2-trasformazione-fomite | margin-right | #ink_3-dark |  | More alli mali habiti dell' |
| 31 | gen | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-right | #ink_3-dark |  | ciò perché l' |
| 32 | gen | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-bottom | #ink_3-dark |  | in questi tempi viene tanto supeditato d |
| 33 | gen | `add` | 169r | seg-b3-c6p8-innocenza-guardia | margin-right | #ink_3-dark |  | però sappiasi che siemo in via, tememo,  |
| 34 | gen | `add` | 169r | seg-b3-c6p8-innocenza-guardia | supralinear | #ink_1 |  | mo |
| 35 | gen | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | quasi |
| 36 | gen | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | pe |
| 37 | gen | `add` | 171r | seg-b3-c6p22-fiamma-estasi | supralinear | #ink_1 |  | alle volte |
| 38 | gen | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | margin-left | #ink_1 |  | questo s'intende per qua |
| 39 | gen | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | supralinear | #ink_1 |  | n |
| 40 | gen | `add` | 174r | seg-b3-c7p12-dichiarazione-ortodossia-consomato | margin-right | #ink_3-dark |  | quasi |
| 41 | gen | `add` | 174v | seg-b3-c7p17-glossa-fortezza-timore | margin-left | #ink_1 |  | cioè per la |
| 42 | gen | `add` | 174v | seg-b3-c7p17-glossa-desiderio-temporaneo | margin-left | #ink_1 |  | cioè per qualche tempo dura il |
| 43 | gen | `add` | 176r | seg-b3-c8p4-riequilibrio-vita | margin | #ink_3-dark | medium | sì bene lo |
| 44 | gen | `add` | 176v | seg-b3-c8p10-quattroparti | substitution | #ink_1 |  | i |
| 45 | gen | `add` | 178r | seg-b3-c8p22-replica-hore | supralinear | #ink_1 |  | cioè |
| 46 | gen | `add` | 179r | seg-b3-c8p27-continua-oratione | margin-right | #ink_3-dark | medium | sì bene i sensi non donano in desordene, |
| 47 | gen | `add` | 182v | seg-b3-c10p6-precisazione-volonta | margin | #ink_3-dark |  | cioè non ha sensi, e passioni tanto vive |
| 48 | gen | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | e |
| 49 | gen | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | o |
| 50 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | solo |
| 51 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | ancora |
| 52 | gen | `add` | 197v | seg-b3-c16p6-carne-con-carne | margin-right | #ink_1 |  | E viene l'anima a non credere più quanto |
| 53 | gen | `add` | 200v | seg-b3-c16p25-allegoria-re | supralinear | #ink_3-dark |  | stanza |
| 54 | gen | `add` | 210r | seg-b3-c19p24-rimando-metatestuale | margin-left | #ink_1 |  | Doppo d'haver fornito questo capitolo, e |
| 55 | gen | `add` | 219v | seg-b3-c24p6-prudenza-penitenza | supralinear | #ink_1 |  | giorni |
| 56 | gen | `add` | 221r | seg-b3-c24p16-glossa-humanita | margin-right | #ink_3-dark |  | cioè non che la |
| 57 | gen | `add` | 247r | seg-b3-c34p6-mutatione-oscuro | supralinear | #ink_1 |  | habituale |
| 58 | gen | `add` | 247r | seg-b3-c34p7-effetti-taciuti | supralinear | #ink_1 |  | la gratia di |
| 59 | gen | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | supralinear | #ink_1 |  | queste |
| 60 | gen | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | margin-right | #ink_3-dark | medium | ; e questo del palar tanto mi pareva pes |
| 61 | gen | `add` | 258v | seg-b3-c38p19-dichiaro-permettendo | bottom | #ink_1 |  | Qui mi dichiaro che |
| 62 | gen | `add` | 259r | - | inline | #ink_3-dark |  | per quanto può stare in via |
| 63 | gen | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | inline | #ink_3-dark |  | cioè fuor della sua capacetà, ma |
| 64 | gen | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | infralinear | #ink_1 |  | di essa |
| 65 | gen | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | inline | #ink_3-dark |  | cioè questa libertà perduta non intento  |
| 66 | gen | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | infralinear | #ink_1 |  | o altre cose simili |
| 67 | gen | `add` | 261v | seg-b3-c39p16-declaratio-antipanteismo | inline | #ink_3-dark |  | Io mi dichiaro che in tutte queste sorti |
| 68 | gen | `add` | 262r | seg-b3-c39p21-corredenzione | inline | #ink_3-dark |  | Ciò s'intende unir li soi meriti con que |
| 69 | gen | `add` | 262v | seg-b3-c40p3-sonno-corpo | margin-right | #ink_1 |  | S'intende però che il spirituali |
| 70 | gen | `del` | 1r | seg-b1-c1p1-miseria-creato | correction | #ink_1 |  | queste |
| 71 | gen | `del` | 3v | seg-b1-c2p14-claustrati-secolari | strikethrough | #ink_1 |  |  |
| 72 | gen | `del` | 6r | seg-b1-c4p4-adoperarsi-notte | strikethrough | #ink_1 |  |  |
| 73 | gen | `del` | 10v | seg-b1-c5p11-fondamento-castello | strikethrough | #ink_1 |  |  |
| 74 | gen | `del` | 11r | seg-b1-c5p16-non-dar-parere | strikethrough | #ink_1 |  |  |
| 75 | gen | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 76 | gen | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 77 | gen | `del` | 12r | seg-b1-c5p33-finta-humilta | strikethrough | #ink_1 |  |  |
| 78 | gen | `del` | 12v | seg-b1-c5p36-falsita-mondo | strikethrough | #ink_1 |  | Divini |
| 79 | gen | `del` | 12v | seg-b1-c5p38-humilta-vera-quiete | strikethrough | #ink_1 |  |  |
| 80 | gen | `del` | 12v | seg-b1-c5p41-rimedi-padre | strikethrough | #ink_1 |  |  |
| 81 | gen | `del` | 13v | seg-b1-c5p61-comperatione-fine | strikethrough | #ink_1 |  | s |
| 82 | gen | `del` | 14r | seg-b1-c6p4-desiderio-sudita | strikethrough | #ink_1 |  |  |
| 83 | gen | `del` | 14r | seg-b1-c6p5-obedienza-penitenza | strikethrough | #ink_1 |  | penitenza |
| 84 | gen | `del` | 14v | seg-b1-c6p11-vera-obedienza | strikethrough | #ink_1 |  | d'animo |
| 85 | gen | `del` | 158r | seg-b3-pro-p1-invocatio | correction | #ink_1 |  | to |
| 86 | gen | `del` | 158r | seg-b3-pro-p1-incapacitas | correction | #ink_1 |  | e |
| 87 | gen | `del` | 158v | seg-b3-c1p4-pace2 | correction | #ink_1 |  | a |
| 88 | gen | `del` | 158v | seg-b3-c1p7-viaggio | correction | #ink_1 |  | è |
| 89 | gen | `del` | 159r | seg-b3-c1p10-unione-velata | correction | #ink_1 |  | sc |
| 90 | gen | `del` | 159v | seg-b3-c2p1-obbedienza-incipit | correction | #ink_1 |  | e |
| 91 | gen | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  | o |
| 92 | gen | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  |  |
| 93 | gen | `del` | 160r | seg-b3-c2p4-giardino-quiete | deletion | #ink_1 |  | o |
| 94 | gen | `del` | 160r | seg-b3-c2p6-differenza-raccoglimento | deletion | #ink_1 |  |  |
| 95 | gen | `del` | 160v | seg-b3-c2p10-linguaggio-oscuro | correction | #ink_1 |  | e |
| 96 | gen | `del` | 161r | seg-b3-c2p13-castellano-secreto | deletion | #ink_1 |  |  |
| 97 | gen | `del` | 161r | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  |  |
| 98 | gen | `del` | 161v | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  | diff |
| 99 | gen | `del` | 161v | seg-b3-c2p16-silentio-non-parla | correction | #ink_1 |  | e |
| 100 | gen | `del` | 161v | seg-b3-c2p19-demonio-escluso | correction | #ink_1 |  | e |
| 101 | gen | `del` | 162r | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 102 | gen | `del` | 162v | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 103 | gen | `del` | 162v | seg-b3-c3p1-esortazione | correction | #ink_1 |  | a |
| 104 | gen | `del` | 162v | seg-b3-c3p2-definizione-oblio | deletion | #ink_1 |  | , |
| 105 | gen | `del` | 162v | seg-b3-c3p3-raccoglimento | deletion | #ink_1 |  | sonno |
| 106 | gen | `del` | 163r | seg-b3-c3p4-opera-divina | deletion | #ink_1 |  | di |
| 107 | gen | `del` | 163r | seg-b3-c3p5-propriastima | deletion | #ink_1 |  | s. |
| 108 | gen | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 109 | gen | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 110 | gen | `del` | 163v | seg-b3-c3p7-statuette | deletion | #ink_1 |  | di silen |
| 111 | gen | `del` | 164r | seg-b3-c3p12-linguaggio | deletion | #ink_1 |  |  |
| 112 | gen | `del` | 165r | seg-b3-c4p3-ineffabilita-labirinto | deletion | #ink_1 |  | pa |
| 113 | gen | `del` | 165r | seg-b3-c4p5-precisatio-sospensione | correction | #ink_1 |  | e |
| 114 | gen | `del` | 167r | seg-b3-c5p7-amore-prossimo | correction | #ink_1 |  | a |
| 115 | gen | `del` | 167v | seg-b3-c5p12-affetti-persi | deletion | #ink_1 |  | che |
| 116 | gen | `del` | 167v | seg-b3-c5p16-tocchi-sostanza | deletion | #ink_1 |  | vecchi |
| 117 | gen | `del` | 168r | seg-b3-c6p4-fomite-peccato | deletion | #ink_1 |  |  |
| 118 | gen | `del` | 169r | seg-b3-c6p8-innocenza-guardia | deletion | #ink_1 |  | npe |
| 119 | gen | `del` | 169r | seg-b3-c6p8b-mondo-beati | deletion | #ink_1 |  |  |
| 120 | gen | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 121 | gen | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 122 | gen | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | dire |
| 123 | gen | `del` | 170v | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  |  |
| 124 | gen | `del` | 170v | seg-b3-c6p21-braggia-similitudine | deletion | #ink_1 |  |  |
| 125 | gen | `del` | 171v | seg-b3-c6p26-esposti-guardia | deletion | #ink_1 |  |  |
| 126 | gen | `del` | 172v | seg-b3-c6p33-puo-cadere-guardia | deletion | #ink_1 |  |  |
| 127 | gen | `del` | 173v | seg-b3-c7p9-precisazione-operare-participatione | deletion | #ink_1 |  | ed |
| 128 | gen | `del` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | deletion | #ink_1 |  |  |
| 129 | gen | `del` | 174v | seg-b3-c7p21-similitudine-cera-sole | deletion | #ink_1 |  | per |
| 130 | gen | `del` | 175r | seg-b3-c7p22-fiamma-fuoco | deletion | #ink_1 |  | ap |
| 131 | gen | `del` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | deletion | #ink_1 |  | pop |
| 132 | gen | `del` | 175v | - | deletion | #ink_1 |  | se |
| 133 | gen | `del` | 176v | seg-b3-c8p8-distrattioni | deletion | #ink_1 |  | co |
| 134 | gen | `del` | 176v | seg-b3-c8p10-quattroparti | correction | #ink_1 |  | e |
| 135 | gen | `del` | 177v | seg-b3-c8p18-bocca-sostanza | deletion | #ink_1 |  | d |
| 136 | gen | `del` | 177v | seg-b3-c8p19-contatto-gloria | deletion | #ink_1 |  | intende |
| 137 | gen | `del` | 178r | seg-b3-c8p21-esorto-hore | deletion | #ink_1 |  | t |
| 138 | gen | `del` | 178r | seg-b3-c8p21-sicurta-cadute | deletion | #ink_1 |  | , |
| 139 | gen | `del` | 179r | seg-b3-c8p25-estremi-sole | deletion | #ink_1 |  |  |
| 140 | gen | `del` | 179r | seg-b3-c8p25-propria-stima | deletion | #ink_1 |  | che |
| 141 | gen | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 142 | gen | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 143 | gen | `del` | 183r | seg-b3-c10p8-riequilibrio-fatica | deletion | #ink_1 |  |  |
| 144 | gen | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | a |
| 145 | gen | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | e |
| 146 | gen | `del` | 193r | seg-b3-c12p3-ricevere-consenso | deletion | #ink_1 |  | con |
| 147 | gen | `del` | 193r | seg-b3-c12p4-addormentarsi-amato | deletion | #ink_1 |  |  |
| 148 | gen | `del` | 193v | seg-b3-c12p5-atti-continui | deletion | #ink_1 |  | per |
| 149 | gen | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | f |
| 150 | gen | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | sopr. |
| 151 | gen | `del` | 195v | seg-b3-c14p5-sapienza-agonia | deletion | #ink_1 |  | s'an |
| 152 | gen | `del` | 195v | seg-b3-c14p6-ombra-certezza | deletion | #ink_1 |  |  |
| 153 | gen | `del` | 201r | seg-b3-c16p28-niente-trasformatione | deletion | #ink_1 |  |  |
| 154 | gen | `del` | 202r | seg-b3-c16p37-certezza-niente | deletion | #ink_1 |  |  |
| 155 | gen | `del` | 207v | seg-b3-c19p4-definizione-amicitia | deletion | #ink_1 |  | super |
| 156 | gen | `del` | 208v | seg-b3-c19p11-riepilogo-gradi | deletion | #ink_1 |  | super |
| 157 | gen | `del` | 221r | seg-b3-c24p16-glossa-humanita | deletion | #ink_3-dark |  | G |
| 158 | gen | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | di Dio |
| 159 | gen | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | detta |
| 160 | gen | `del` | 248v | seg-b3-c34p17-olimpo-altezza | deletion | #ink_1 |  | t |
| 161 | gen | `del` | 257v | seg-b3-c38p9-brama-padre-preghiera | deletion | #ink_1 |  |  |
| 162 | gen | `del` | 258r | seg-b3-c38p13-persecutione-terzapersona | deletion | #ink_1 |  | tanti |
| 163 | gen | `del` | 258v | seg-b3-c38p18-fede-oscurata | deletion | #ink_1 |  |  |
| 164 | gen | `del` | 258v | seg-b3-c38p19-perdita-fede | deletion | #ink_1 |  |  |
| 165 | gen | `del` | 262r | - | deletion | #ink_1 |  | trigesimo |
| 166 | gen | `subst` | 1r | seg-b1-c1p1-miseria-creato |  |  |  |  |
| 167 | gen | `subst` | 14r | seg-b1-c6p5-obedienza-penitenza |  |  |  |  |
| 168 | gen | `subst` | 159v | seg-b3-c2p1-obbedienza-incipit |  |  |  |  |
| 169 | gen | `subst` | 160v | seg-b3-c2p10-linguaggio-oscuro |  |  |  |  |
| 170 | gen | `subst` | 161v | seg-b3-c2p16-silentio-non-parla |  |  |  |  |
| 171 | gen | `subst` | 161v | seg-b3-c2p19-demonio-escluso |  |  |  |  |
| 172 | gen | `subst` | 162r | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 173 | gen | `subst` | 162v | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 174 | gen | `subst` | 162v | seg-b3-c3p1-esortazione |  |  |  |  |
| 175 | gen | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 176 | gen | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 177 | gen | `subst` | 165r | seg-b3-c4p5-precisatio-sospensione |  |  |  |  |
| 178 | gen | `subst` | 167r | seg-b3-c5p7-amore-prossimo |  |  |  |  |
| 179 | gen | `subst` | 176v | seg-b3-c8p10-quattroparti |  |  |  |  |
| 180 | gen | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 181 | gen | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 182 | gen | `retrace` | 159v | seg-b3-c2p2-fondo-anima |  | #ink_1 | medium | tem |
| 183 | gen | `retrace` | 160v | seg-b3-c2p10-linguaggio-oscuro |  | #ink_1 | medium | è |
| 184 | gen | `retrace` | 163r | seg-b3-c3p4-fondoraccolto |  | #ink_1 | medium | tom |
| 185 | gen | `retrace` | 163r | seg-b3-c3p5-chiarezza |  | #ink_1 | medium | te |
| 186 | gen | `retrace` | 163v | seg-b3-c3p7-declaratio-verita |  | #ink_1 | medium | u |
| 187 | gen | `retrace` | 164r | seg-b3-c3p9-fortezza |  | #ink_1 | medium | e |
| 188 | gen | `retrace` | 164r | seg-b3-c3p11-comunicazione |  | #ink_1 | medium | r |
| 189 | gen | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | m |
| 190 | gen | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | n |
| 191 | gen | `retrace` | 164v | seg-b3-c3p14-mirabilia |  | #ink_1 | medium | mino |
| 192 | gen | `retrace` | 164v | seg-b3-c4p2-attuale-habituale |  | #ink_1 | medium | l |
| 193 | gen | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | c |
| 194 | gen | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | n |
| 195 | gen | `retrace` | 165r | seg-b3-c4p7-nuova-caccia-vecchia |  | #ink_1 | medium | s |
| 196 | gen | `retrace` | 166v | seg-b3-c5p6-cessano-zeli |  | #ink_1 | medium | z |
| 197 | gen | `retrace` | 167v | seg-b3-c5p12-affetti-persi |  | #ink_1 | medium | a |
| 198 | gen | `retrace` | 169r | seg-b3-c6p8-innocenza-guardia |  | #ink_1 |  | b |
| 199 | gen | `retrace` | 170v | seg-b3-c6p17-fede-prattica-guardia |  | #ink_1 |  | l |
| 200 | gen | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | n |
| 201 | gen | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | t |
| 202 | gen | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | p |
| 203 | gen | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | g |
| 204 | gen | `retrace` | 170v | seg-b3-c6p22-fiamma-estasi |  | #ink_1 |  | m |
| 205 | gen | `retrace` | 172v | seg-b3-c6p33-puo-cadere-guardia |  | #ink_1 |  | in |
| 206 | gen | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 207 | gen | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 208 | gen | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | c |
| 209 | gen | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | m |
| 210 | gen | `retrace` | 176r | seg-b3-c8p3-morte-vitanuova |  | #ink_1 | medium | m |
| 211 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | r |
| 212 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | m |
| 213 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | t |
| 214 | gen | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | n |
| 215 | gen | `retrace` | 176r | seg-b3-c8p6-sensi-sposalitio |  | #ink_1 | medium | nn |
| 216 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | c |
| 217 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 218 | gen | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 219 | gen | `retrace` | 177r | seg-b3-c8p15-lambino |  | #ink_1 | medium | lambino |
| 220 | gen | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | tinuo |
| 221 | gen | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | co |
| 222 | gen | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | ricittavolo |
| 223 | gen | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | co |
| 224 | gen | `retrace` | 178r | seg-b3-c8p21-esorto-hore |  | #ink_1 | medium | scu |
| 225 | gen | `retrace` | 197v | seg-b3-c16p6-carne-con-carne |  | #ink_1 |  | c |
| 226 | gen | `retrace` | 198v | seg-b3-c16p15-molte-strade |  | #ink_1 |  | r |
| 227 | gen | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | m |
| 228 | gen | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | t |
| 229 | gen | `retrace` | 200v | seg-b3-c16p26-festa-sensi |  | #ink_1 |  | e |
| 230 | gen | `retrace` | 202r | seg-b3-c16p37-certezza-niente |  | #ink_1 |  | e |
| 231 | gen | `retrace` | 219v | seg-b3-c24p2-timore-naturale |  | #ink_1 |  | d |
| 232 | gen | `retrace` | 220v | seg-b3-c24p13-fiducia-abbandono |  | #ink_1 |  | men |
| 233 | gen | `gap` | 3v | seg-b1-c2p14-claustrati-secolari | cancelled |  |  |  |
| 234 | gen | `gap` | 6r | seg-b1-c4p4-adoperarsi-notte | illegible |  |  |  |
| 235 | gen | `gap` | 10v | seg-b1-c5p11-fondamento-castello | illegible |  |  |  |
| 236 | gen | `gap` | 11r | seg-b1-c5p16-non-dar-parere | illegible |  |  |  |
| 237 | gen | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 238 | gen | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 239 | gen | `gap` | 12r | seg-b1-c5p33-finta-humilta | illegible |  |  |  |
| 240 | gen | `gap` | 12v | seg-b1-c5p38-humilta-vera-quiete | illegible |  |  |  |
| 241 | gen | `gap` | 12v | seg-b1-c5p41-rimedi-padre | illegible |  |  |  |
| 242 | gen | `gap` | 13v | seg-b1-c5p61-comperatione-fine | illegible |  |  |  |
| 243 | gen | `gap` | 14r | seg-b1-c6p4-desiderio-sudita | illegible |  |  |  |
| 244 | gen | `gap` | 23r | seg-b1-c11p58-carita-cura | hole |  |  |  |
| 245 | gen | `gap` | 159r | seg-b3-c1p10-unione-velata | illegible |  |  |  |
| 246 | gen | `gap` | 159r | - | hole |  |  |  |
| 247 | gen | `gap` | 159v | seg-b3-c2p3-comparatione-teresa | illegible |  |  |  |
| 248 | gen | `gap` | 160r | seg-b3-c2p6-differenza-raccoglimento | illegible |  |  |  |
| 249 | gen | `gap` | 161r | seg-b3-c2p13-castellano-secreto | illegible |  |  |  |
| 250 | gen | `gap` | 161r | seg-b3-c2p15-comunicazione-diretta | illegible |  |  |  |
| 251 | gen | `gap` | 162v | seg-b3-c3p1-santamadre | hole |  |  |  |
| 252 | gen | `gap` | 163r | seg-b3-c3p5-propriastima | hole |  |  |  |
| 253 | gen | `gap` | 163v | seg-b3-c3p7-statuette | hole |  |  |  |
| 254 | gen | `gap` | 163v | seg-b3-c3p7-magnificar | hole |  |  |  |
| 255 | gen | `gap` | 164r | seg-b3-c3p12-linguaggio | illegible |  |  |  |
| 256 | gen | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 257 | gen | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 258 | gen | `gap` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  |  |  |
| 259 | gen | `gap` | 168r | seg-b3-c6p3-morire-spogliarsi | illegible |  |  |  |
| 260 | gen | `gap` | 168r | seg-b3-c6p4-fomite-peccato | hole |  |  |  |
| 261 | gen | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 262 | gen | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 263 | gen | `gap` | 169r | seg-b3-c6p8b-mondo-beati | illegible |  |  |  |
| 264 | gen | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 265 | gen | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 266 | gen | `gap` | 170r | seg-b3-c6p15-adamo-guardia | hole |  |  |  |
| 267 | gen | `gap` | 170r | seg-b3-c6p15-adamo-guardia | illegible |  |  |  |
| 268 | gen | `gap` | 170v | seg-b3-c6p17-fede-prattica-guardia | illegible |  |  |  |
| 269 | gen | `gap` | 170v | seg-b3-c6p21-braggia-similitudine | illegible |  |  |  |
| 270 | gen | `gap` | 171v | seg-b3-c6p26-esposti-guardia | illegible |  |  |  |
| 271 | gen | `gap` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  |  |  |
| 272 | gen | `gap` | 178r | seg-b3-c8p21-esorto-hore | illegible |  |  |  |
| 273 | gen | `gap` | 179r | seg-b3-c8p25-estremi-sole | illegible |  |  |  |
| 274 | gen | `gap` | 179r | seg-b3-c8p25-propria-stima | illegible |  |  |  |
| 275 | gen | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 276 | gen | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 277 | gen | `gap` | 183r | seg-b3-c10p8-riequilibrio-fatica | illegible |  |  |  |
| 278 | gen | `gap` | 193r | seg-b3-c12p4-addormentarsi-amato | illegible |  |  |  |
| 279 | gen | `gap` | 195v | seg-b3-c14p6-ombra-certezza | illegible |  |  |  |
| 280 | gen | `gap` | 198v | seg-b3-c16p13-esperienza-propria | hole |  |  |  |
| 281 | gen | `gap` | 201r | seg-b3-c16p28-niente-trasformatione | illegible |  |  |  |
| 282 | gen | `gap` | 202r | seg-b3-c16p37-certezza-niente | illegible |  |  |  |
| 283 | gen | `gap` | 202v | seg-b3-c16p39-capi-eresia | illegible |  |  |  |
| 284 | gen | `gap` | 221r | seg-b3-c24p16-glossa-humanita | hole |  |  |  |
| 285 | gen | `gap` | 246v | seg-b3-c34p3-identita-distinte | hole |  |  |  |
| 286 | gen | `gap` | 248v | seg-b3-c34p17-olimpo-altezza | illegible |  |  |  |
| 287 | gen | `gap` | 257v | seg-b3-c38p9-brama-padre-preghiera | illegible |  |  |  |
| 288 | gen | `gap` | 258v | seg-b3-c38p18-fede-oscurata | illegible |  |  |  |
| 289 | gen | `gap` | 261r | seg-b3-c39p16-annichilazione-insensibile | hole |  |  |  |
| 290 | gen | `gap` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  |  |  |
| 291 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 292 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 293 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 294 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 295 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 296 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 297 | gen | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 298 | gen | `supplied` | 3r | seg-b1-c2p6-nemico-demonio | hole |  | high | r |
| 299 | gen | `supplied` | 3r | seg-b1-c2p7-tre-nemici | hole |  | high | n |
| 300 | gen | `supplied` | 3v | seg-b1-c2p8-citta-assediata | hole |  | high | ste |
| 301 | gen | `supplied` | 6v | seg-b1-c4p15-notte-necessaria | hole |  | high | ra |
| 302 | gen | `supplied` | 7v | seg-b1-c4p26-prima-purga-dura | hole |  | high | p |
| 303 | gen | `supplied` | 8r | seg-b1-c4p32-merito-bandiera | hole |  | high | p |
| 304 | gen | `supplied` | 9r | seg-b1-c4p47-san-paolo-vocatione | hole |  | high | co |
| 305 | gen | `supplied` | 9v | seg-b1-c4p55-temer-occasione | hole |  | high | ch |
| 306 | gen | `supplied` | 10r | seg-b1-c5p1-metafora-fondamento | hole |  | high | lo |
| 307 | gen | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | u |
| 308 | gen | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | m |
| 309 | gen | `supplied` | 10v | seg-b1-c5p3-cristo-peccatori | hole |  | medium | i |
| 310 | gen | `supplied` | 10v | seg-b1-c5p11-fondamento-castello | hole |  | high | nto |
| 311 | gen | `supplied` | 10v | seg-b1-c5p13-esterno-interno | hole |  | high | qu |
| 312 | gen | `supplied` | 11r | seg-b1-c5p19-mortificar-passioni | hole |  | high | re |
| 313 | gen | `supplied` | 11r | seg-b1-c5p20-anime-principianti | hole |  | high | o f |
| 314 | gen | `supplied` | 11v | seg-b1-c5p26-rammarico-quiete | hole |  | high | l |
| 315 | gen | `supplied` | 11v | seg-b1-c5p28-distacco-spirito | hole |  | high | i |
| 316 | gen | `supplied` | 12r | seg-b1-c5p28-distacco-spirito | omitted |  | high | ma |
| 317 | gen | `supplied` | 12r | seg-b1-c5p33-finta-humilta | hole |  | high | bil |
| 318 | gen | `supplied` | 12v | seg-b1-c5p41-rimedi-padre | hole |  | high | op |
| 319 | gen | `supplied` | 13r | seg-b1-c5p49-humilta-contrario | hole |  | high | m |
| 320 | gen | `supplied` | 13r | seg-b1-c5p51-voltare-mondo | hole |  | high | a |
| 321 | gen | `supplied` | 13v | seg-b1-c5p51-voltare-mondo | hole |  | high | à l' |
| 322 | gen | `supplied` | 14r | seg-b1-c6p5-obedienza-penitenza | hole |  | high | l |
| 323 | gen | `supplied` | 14r | seg-b1-c6p8-vite-santi | hole |  | high | d |
| 324 | gen | `supplied` | 14v | seg-b1-c6p16-approfittate-intelletto | hole |  | high | i |
| 325 | gen | `supplied` | 15r | seg-b1-c6p18-conclusione | omitted |  | high | t |
| 326 | gen | `supplied` | 20r | seg-b1-c11p3-fatiche-niente | hole |  | high | qui |
| 327 | gen | `supplied` | 20v | seg-b1-c11p13-mondo-schernisce | hole |  | high | lto |
| 328 | gen | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | m |
| 329 | gen | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | l |
| 330 | gen | `supplied` | 21r | seg-b1-c11p23-ripugnanza-merito | hole |  | high | li d |
| 331 | gen | `supplied` | 21v | seg-b1-c11p23-ripugnanza-merito | hole |  | high | l |
| 332 | gen | `supplied` | 21v | seg-b1-c11p30-obedienza-toglie | hole |  | high | gli |
| 333 | gen | `supplied` | 22r | seg-b1-c11p42-frutti-fanciulli | hole |  | high | al |
| 334 | gen | `supplied` | 22v | seg-b1-c11p50-contadino-diligente | hole |  | high | r |
| 335 | gen | `supplied` | 23r | seg-b1-c11p56-principianti-forze | hole |  | high | co |
| 336 | gen | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | medium | l |
| 337 | gen | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | high | tra |
| 338 | gen | `supplied` | 23v | seg-b1-c11p64-cieca-obedienza | hole |  | high | e |
| 339 | gen | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | p |
| 340 | gen | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | i e |
| 341 | gen | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | a co |
| 342 | gen | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | d h |
| 343 | gen | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | e |
| 344 | gen | `supplied` | 159r | - | hole |  | medium | e |
| 345 | gen | `supplied` | 160r | seg-b3-c2p5-sposo-quiete | hole |  | medium | e |
| 346 | gen | `supplied` | 160v | seg-b3-c2p12-castello-fondo | hole |  | medium | u |
| 347 | gen | `supplied` | 161r | seg-b3-c2p13-castellano-secreto | hole |  | medium | e |
| 348 | gen | `supplied` | 161v | seg-b3-c2p18-pace-continua | hole |  | medium | io |
| 349 | gen | `supplied` | 162r | seg-b3-c2p20-autonomia-direttore | hole |  | medium | a |
| 350 | gen | `supplied` | 162v | seg-b3-c3p1-santamadre | hole |  | medium | i |
| 351 | gen | `supplied` | 163r | seg-b3-c3p5-propriastima | hole |  | medium | nt |
| 352 | gen | `supplied` | 163v | seg-b3-c3p7-statuette | hole |  | medium | a |
| 353 | gen | `supplied` | 163v | seg-b3-c3p7-magnificar | hole |  | medium | i |
| 354 | gen | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | modo |
| 355 | gen | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | arse |
| 356 | gen | `supplied` | 165r | seg-b3-c4p8-conclusio | hole |  | medium | à |
| 357 | gen | `supplied` | 166v | seg-b3-c5p6-non-capace-pena | hole |  | medium | e |
| 358 | gen | `supplied` | 167r | seg-b3-c5p7-amore-prossimo | hole |  | medium | i |
| 359 | gen | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | e |
| 360 | gen | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | o |
| 361 | gen | `supplied` | 169r | seg-b3-c6p8-innocenza-guardia | hole |  | high | e |
| 362 | gen | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | a |
| 363 | gen | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | n |
| 364 | gen | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | à |
| 365 | gen | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | a |
| 366 | gen | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | stain |  | medium | n |
| 367 | gen | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | hole |  | medium | ano |
| 368 | gen | `supplied` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | hole |  | medium | s |
| 369 | gen | `supplied` | 174v | seg-b3-c7p17-glossa-fortezza-timore | hole |  | low | deve temere |
| 370 | gen | `supplied` | 175v | seg-b3-c8p2-roma | hole |  | medium | v |
| 371 | gen | `supplied` | 177r | seg-b3-c8p15-lambino | hole |  | medium | a |
| 372 | gen | `supplied` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  | medium | a |
| 373 | gen | `supplied` | 179r | seg-b3-c8p27-continua-oratione | hole |  | medium | oratione |
| 374 | gen | `supplied` | 197r | seg-b3-c16p3-distinzione-unione | hole |  | medium | c |
| 375 | gen | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | ret |
| 376 | gen | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | n |
| 377 | gen | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | a |
| 378 | gen | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | P |
| 379 | gen | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | e |
| 380 | gen | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | Anch |
| 381 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ra |
| 382 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | e |
| 383 | gen | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ass |
| 384 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | g |
| 385 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | c |
| 386 | gen | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | re |
| 387 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | sa |
| 388 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | rl |
| 389 | gen | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | iù |
| 390 | gen | `supplied` | 209v | seg-b3-c19p22-partecipazione-corpo | hole |  | medium | me |
| 391 | gen | `supplied` | 219r | - | hole |  | medium | enta |
| 392 | gen | `supplied` | 220v | seg-b3-c24p10-distinzione-interni | hole |  | medium | cu |
| 393 | gen | `supplied` | 220v | seg-b3-c24p12-abbandono-padre | hole |  | medium | n |
| 394 | gen | `supplied` | 220v | seg-b3-c24p14-critica-padri | hole |  | medium | c |
| 395 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | esse |
| 396 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | nza |
| 397 | gen | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | star |
| 398 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | medium | o pare |
| 399 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | e |
| 400 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 401 | gen | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 402 | gen | `supplied` | 242r | seg-b3-c32p2-incognito-ineffabile | hole |  | high | a |
| 403 | gen | `supplied` | 242v | seg-b3-c32p2-incognito-ineffabile | hole |  | high | v |
| 404 | gen | `supplied` | 242v | seg-b3-c32p3-trasformazione-crocifisso | hole |  | high | l |
| 405 | gen | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | in |
| 406 | gen | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | è |
| 407 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | croci |
| 408 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | sì co |
| 409 | gen | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | li |
| 410 | gen | `supplied` | 246v | seg-b3-c34p3-identita-distinte | hole |  | high | ù |
| 411 | gen | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | ivon |
| 412 | gen | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | no |
| 413 | gen | `supplied` | 248r | seg-b3-c34p13-tentatione-agostino | hole |  | high | i |
| 414 | gen | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | hole |  | high | ne |
| 415 | gen | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | stain |  | medium | e |
| 416 | gen | `supplied` | 256v | seg-b3-c38p4-aridita-continua | hole |  | high | vo |
| 417 | gen | `supplied` | 257r | seg-b3-c38p8-discernimento-brama | hole |  | high | ti |
| 418 | gen | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | i |
| 419 | gen | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | dre |
| 420 | gen | `supplied` | 257v | seg-b3-c38p11-benevolenza-honore | hole |  | high | he |
| 421 | gen | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | ar |
| 422 | gen | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | re |
| 423 | gen | `supplied` | 259r | seg-b3-c39p4-deificatione-imagine | hole |  | high | ic |
| 424 | gen | `supplied` | 259v | seg-b3-c39p5-precisazione-matrimonio | hole |  | medium | perita |
| 425 | gen | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | tro si |
| 426 | gen | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | dal |
| 427 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | stain |  | medium | re |
| 428 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d |
| 429 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d in |
| 430 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d a |
| 431 | gen | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | in |
| 432 | gen | `supplied` | 261r | seg-b3-c39p13-silentio-annientamento | hole |  | high | nel |
| 433 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | rtù |
| 434 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | st' |
| 435 | gen | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | é |
| 436 | gen | `supplied` | 262r | seg-b3-c39p20-salamandra | hole |  | medium | tan |
| 437 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | p |
| 438 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ti |
| 439 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | pro |
| 440 | gen | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ità |
| 441 | gen | `supplied` | 262v | seg-b3-c40p2-cella-intima | hole |  | medium | t |
| 442 | gen | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ugiato |
| 443 | gen | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ett |
| 444 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 445 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | s |
| 446 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 447 | gen | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | ho |
