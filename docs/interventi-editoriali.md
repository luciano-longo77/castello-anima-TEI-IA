# Interventi editoriali: rendiconto verificabile
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

**Fonte**
*Generato da `tei/text/castello-anima-teiText.xml`. Fotografa ogni intervento editoriale **marcato**: l'apparato sostanziale/genetico (`add`/`del`/`subst`, dentro `app`/`rdg`), le ritracciature (`retrace`) e le integrazioni editoriali (`gap`/`unclear`/`supplied`). La **normalizzazione grafica** è silenziosa e dichiarata una volta per tutte (`docs/criteri-trascrizione.md` + `editorialDecl`): nel testo di lettura non compaiono elementi diplomatici (`choice`). L'attribuzione delle integrazioni è per-istanza (`supplied`: `@resp` + `@cert`).*

---

## 1. Apparato genetico e integrazioni

| elemento | n | con `@hand` | con `@cert` |
|---|---:|---:|---:|
| `add` | 71 | 71 | 7 |
| `del` | 96 | 96 | 0 |
| `subst` | 16 | 0 | 0 |
| `retrace` | 51 | 51 | 33 |
| `gap` | 67 | 0 | 0 |
| `unclear` | 6 | 0 | 0 |
| `supplied` | 200 | 0 | 200 |

### 1.1 Dettaglio dei valori

| attributo | valori (conteggio) |
|---|---|
| `del/@type` | `correction` (20) · `deletion` (62) |
| `del/@rend` | `strikethrough` (76) |
| `del/@place` | `inline` (74) |
| `add/@type` | `addition` (8) · `substitution` (18) |
| `add/@place` | `bottom` (1) · `infralinear` (2) · `inline` (16) · `margin` (4) · `margin-bottom` (1) · `margin-left` (9) · `margin-right` (9) · `supralinear` (21) |
| `gap/@reason` | `cancelled` (1) · `hole` (24) · `illegible` (42) |
| `gap/@unit` | `char` (59) · `chars` (2) · `word` (6) |
| `supplied/@reason` | `damage` (13) · `editorial` (5) · `heading-omitted` (1) · `hole` (161) · `illegible` (3) · `omitted` (7) · `stain` (10) |
| `retrace/@hand` | `#ink_1` (51) |
| `retrace/@cert` | `medium` (33) |

## 2. Controlli di coerenza

**Nessun rilievo.** Coerente con la policy dichiarata: nessun `choice` (normalizzazione silenziosa), ogni `supplied` con `@resp`+`@cert`, ogni `subst` = `add`+`del`.

## 3. Appendice · dettaglio per-istanza

*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, `seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*

| # | elemento | carta | seg | tipo/valore | mano | cert | testo |
|---:|---|---|---|---|---|---|---|
| 1 | `add` | 1r | seg-b1-c1p1-miseria-creato | substitution | #ink_1 |  | quante |
| 2 | `add` | 9r | seg-b1-c4p47-san-paolo-vocatione | addition | #ink_1 |  | Domine, quid vis me facere? |
| 3 | `add` | 11v | seg-b1-c5p23-conformita-volere | addition | #ink_1 |  | da esser |
| 4 | `add` | 12v | seg-b1-c5p37-humilta-demonio | addition | #ink_1 |  | certa |
| 5 | `add` | 12v | seg-b1-c5p38-humilta-vera-quiete | addition | #ink_1 |  | è vera |
| 6 | `add` | 13v | seg-b1-c5p59-schiava-esempio | addition | #ink_1 |  | sono |
| 7 | `add` | 14r | seg-b1-c6p5-obedienza-penitenza | addition | #ink_1 |  | obedienza |
| 8 | `add` | 21v | seg-b1-c11p28-amor-proprio-cella | addition | #ink_1 |  | più piccole |
| 9 | `add` | 23r | seg-b1-c11p58-carita-cura | addition | #ink_1 |  |  |
| 10 | `add` | 85v | seg-b2-c7p33-certezza-salvatione | supralinear | #ink_1 |  | intervallo di |
| 11 | `add` | 146r | seg-b2-c21p10-quattro-passioni | margin | #ink_4-external |  | Mi dichiarò però che resta nell'anima pa |
| 12 | `add` | 158r | seg-b3-pro-p1-incapacitas | substitution | #ink_1 |  | i |
| 13 | `add` | 158v | seg-b3-c1p4-pace2 | substitution | #ink_1 |  | e |
| 14 | `add` | 158v | seg-b3-c1p7-viaggio | substitution | #ink_1 |  | e |
| 15 | `add` | 159v | seg-b3-c2p1-obbedienza-incipit | substitution | #ink_1 |  | a |
| 16 | `add` | 159v | seg-b3-c2p3-comparatione-teresa | supralinear | #ink_3-dark | medium | adacquar |
| 17 | `add` | 160v | seg-b3-c2p10-linguaggio-oscuro | substitution | #ink_1 |  | i |
| 18 | `add` | 161v | seg-b3-c2p16-silentio-non-parla | substitution | #ink_1 |  | i |
| 19 | `add` | 161v | seg-b3-c2p19-demonio-escluso | substitution | #ink_1 |  | i |
| 20 | `add` | 162r | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 21 | `add` | 162v | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 22 | `add` | 162v | seg-b3-c3p1-esortazione | substitution | #ink_1 |  | o |
| 23 | `add` | 162v | seg-b3-c3p3-raccoglimento | supralinear | #ink_1 |  |  |
| 24 | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | a |
| 25 | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | i |
| 26 | `add` | 164v | seg-b3-c3p14-mirabilia | margin-left | #ink_3-dark | medium | dico ciò non perché non s'ha detto la |
| 27 | `add` | 165r | seg-b3-c4p5-precisatio-sospensione | substitution | #ink_1 |  | i |
| 28 | `add` | 167r | seg-b3-c5p7-amore-prossimo | substitution | #ink_1 |  | e |
| 29 | `add` | 167r | seg-b3-c5p8-non-desiderar-croce | supralinear | #ink_1 |  | ar |
| 30 | `add` | 167r | seg-b3-c5p9-non-desiderar-morte | margin-left | #ink_1 | medium | Ciò s'intende per non |
| 31 | `add` | 167r | seg-b3-c5p10-palla-cera | inline | #ink_3-dark | medium | Ciò non s'intende a cose di male, ma che |
| 32 | `add` | 168r | seg-b3-c6p2-trasformazione-fomite | margin-right | #ink_3-dark |  | More alli mali habiti dell' |
| 33 | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-right | #ink_3-dark |  | ciò perché l' |
| 34 | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-bottom | #ink_3-dark |  | in questi tempi viene tanto supeditato d |
| 35 | `add` | 169r | seg-b3-c6p8-innocenza-guardia | margin-right | #ink_3-dark |  | però sappiasi che siemo in via, tememo,  |
| 36 | `add` | 169r | seg-b3-c6p8-innocenza-guardia | supralinear | #ink_1 |  | mo |
| 37 | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | quasi |
| 38 | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | pe |
| 39 | `add` | 171r | seg-b3-c6p22-fiamma-estasi | supralinear | #ink_1 |  | alle volte |
| 40 | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | margin-left | #ink_1 |  | questo s'intende per qua |
| 41 | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | supralinear | #ink_1 |  | n |
| 42 | `add` | 174r | seg-b3-c7p12-dichiarazione-ortodossia-consomato | margin-right | #ink_3-dark |  | quasi |
| 43 | `add` | 174v | seg-b3-c7p17-glossa-fortezza-timore | margin-left | #ink_1 |  | cioè per la |
| 44 | `add` | 174v | seg-b3-c7p17-glossa-desiderio-temporaneo | margin-left | #ink_1 |  | cioè per qualche tempo dura il |
| 45 | `add` | 176r | seg-b3-c8p4-riequilibrio-vita | margin | #ink_3-dark | medium | sì bene lo |
| 46 | `add` | 176v | seg-b3-c8p10-quattroparti | substitution | #ink_1 |  | i |
| 47 | `add` | 178r | seg-b3-c8p22-replica-hore | supralinear | #ink_1 |  | cioè |
| 48 | `add` | 179r | seg-b3-c8p27-continua-oratione | margin-right | #ink_3-dark | medium | sì bene i sensi non donano in desordene, |
| 49 | `add` | 182v | seg-b3-c10p6-precisazione-volonta | margin | #ink_3-dark |  | cioè non ha sensi, e passioni tanto vive |
| 50 | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | e |
| 51 | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | o |
| 52 | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | solo |
| 53 | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | ancora |
| 54 | `add` | 197v | seg-b3-c16p6-carne-con-carne | margin-right | #ink_1 |  | E viene l'anima a non credere più quanto |
| 55 | `add` | 200v | seg-b3-c16p25-allegoria-re | supralinear | #ink_3-dark |  | stanza |
| 56 | `add` | 210r | seg-b3-c19p24-rimando-metatestuale | margin-left | #ink_1 |  | Doppo d'haver fornito questo capitolo, e |
| 57 | `add` | 219v | seg-b3-c24p6-prudenza-penitenza | supralinear | #ink_1 |  | giorni |
| 58 | `add` | 221r | seg-b3-c24p16-glossa-humanita | margin-right | #ink_3-dark |  | cioè non che la |
| 59 | `add` | 247r | seg-b3-c34p6-mutatione-oscuro | supralinear | #ink_1 |  | habituale |
| 60 | `add` | 247r | seg-b3-c34p7-effetti-taciuti | supralinear | #ink_1 |  | la gratia di |
| 61 | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | supralinear | #ink_1 |  | queste |
| 62 | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | margin-right | #ink_3-dark | medium | ; e questo del palar tanto mi pareva pes |
| 63 | `add` | 258v | seg-b3-c38p19-dichiaro-permettendo | bottom | #ink_1 |  | Qui mi dichiaro che |
| 64 | `add` | 259r | - | inline | #ink_3-dark |  | per quanto può stare in via |
| 65 | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | inline | #ink_3-dark |  | cioè fuor della sua capacetà, ma |
| 66 | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | infralinear | #ink_1 |  | di essa |
| 67 | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | inline | #ink_3-dark |  | cioè questa libertà perduta non intento  |
| 68 | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | infralinear | #ink_1 |  | o altre cose simili |
| 69 | `add` | 261v | seg-b3-c39p16-declaratio-antipanteismo | inline | #ink_3-dark |  | Io mi dichiaro che in tutte queste sorti |
| 70 | `add` | 262r | seg-b3-c39p21-corredenzione | inline | #ink_3-dark |  | Ciò s'intende unir li soi meriti con que |
| 71 | `add` | 262v | seg-b3-c40p3-sonno-corpo | margin-right | #ink_1 |  | S'intende però che il spirituali |
| 72 | `del` | 1r | seg-b1-c1p1-miseria-creato | correction | #ink_1 |  | queste |
| 73 | `del` | 3v | seg-b1-c2p14-claustrati-secolari | strikethrough | #ink_1 |  |  |
| 74 | `del` | 6r | seg-b1-c4p4-adoperarsi-notte | strikethrough | #ink_1 |  |  |
| 75 | `del` | 10v | seg-b1-c5p11-fondamento-castello | strikethrough | #ink_1 |  |  |
| 76 | `del` | 11r | seg-b1-c5p16-non-dar-parere | strikethrough | #ink_1 |  |  |
| 77 | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 78 | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 79 | `del` | 12r | seg-b1-c5p33-finta-humilta | strikethrough | #ink_1 |  |  |
| 80 | `del` | 12v | seg-b1-c5p36-falsita-mondo | strikethrough | #ink_1 |  | Divini |
| 81 | `del` | 12v | seg-b1-c5p38-humilta-vera-quiete | strikethrough | #ink_1 |  |  |
| 82 | `del` | 12v | seg-b1-c5p41-rimedi-padre | strikethrough | #ink_1 |  |  |
| 83 | `del` | 13v | seg-b1-c5p61-comperatione-fine | strikethrough | #ink_1 |  | s |
| 84 | `del` | 14r | seg-b1-c6p4-desiderio-sudita | strikethrough | #ink_1 |  |  |
| 85 | `del` | 14r | seg-b1-c6p5-obedienza-penitenza | strikethrough | #ink_1 |  | penitenza |
| 86 | `del` | 14v | seg-b1-c6p11-vera-obedienza | strikethrough | #ink_1 |  | d'animo |
| 87 | `del` | 158r | seg-b3-pro-p1-invocatio | correction | #ink_1 |  | to |
| 88 | `del` | 158r | seg-b3-pro-p1-incapacitas | correction | #ink_1 |  | e |
| 89 | `del` | 158v | seg-b3-c1p4-pace2 | correction | #ink_1 |  | a |
| 90 | `del` | 158v | seg-b3-c1p7-viaggio | correction | #ink_1 |  | è |
| 91 | `del` | 159r | seg-b3-c1p10-unione-velata | correction | #ink_1 |  | sc |
| 92 | `del` | 159v | seg-b3-c2p1-obbedienza-incipit | correction | #ink_1 |  | e |
| 93 | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  | o |
| 94 | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  |  |
| 95 | `del` | 160r | seg-b3-c2p4-giardino-quiete | deletion | #ink_1 |  | o |
| 96 | `del` | 160r | seg-b3-c2p6-differenza-raccoglimento | deletion | #ink_1 |  |  |
| 97 | `del` | 160v | seg-b3-c2p10-linguaggio-oscuro | correction | #ink_1 |  | e |
| 98 | `del` | 161r | seg-b3-c2p13-castellano-secreto | deletion | #ink_1 |  |  |
| 99 | `del` | 161r | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  |  |
| 100 | `del` | 161v | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  | diff |
| 101 | `del` | 161v | seg-b3-c2p16-silentio-non-parla | correction | #ink_1 |  | e |
| 102 | `del` | 161v | seg-b3-c2p19-demonio-escluso | correction | #ink_1 |  | e |
| 103 | `del` | 162r | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 104 | `del` | 162v | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 105 | `del` | 162v | seg-b3-c3p1-esortazione | correction | #ink_1 |  | a |
| 106 | `del` | 162v | seg-b3-c3p2-definizione-oblio | deletion | #ink_1 |  | , |
| 107 | `del` | 162v | seg-b3-c3p3-raccoglimento | deletion | #ink_1 |  | sonno |
| 108 | `del` | 163r | seg-b3-c3p4-opera-divina | deletion | #ink_1 |  | di |
| 109 | `del` | 163r | seg-b3-c3p5-propriastima | deletion | #ink_1 |  | s. |
| 110 | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 111 | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 112 | `del` | 163v | seg-b3-c3p7-statuette | deletion | #ink_1 |  | di silen |
| 113 | `del` | 164r | seg-b3-c3p12-linguaggio | deletion | #ink_1 |  |  |
| 114 | `del` | 165r | seg-b3-c4p3-ineffabilita-labirinto | deletion | #ink_1 |  | pa |
| 115 | `del` | 165r | seg-b3-c4p5-precisatio-sospensione | correction | #ink_1 |  | e |
| 116 | `del` | 167r | seg-b3-c5p7-amore-prossimo | correction | #ink_1 |  | a |
| 117 | `del` | 167v | seg-b3-c5p12-affetti-persi | deletion | #ink_1 |  | che |
| 118 | `del` | 167v | seg-b3-c5p16-tocchi-sostanza | deletion | #ink_1 |  | vecchi |
| 119 | `del` | 168r | seg-b3-c6p4-fomite-peccato | deletion | #ink_1 |  |  |
| 120 | `del` | 169r | seg-b3-c6p8-innocenza-guardia | deletion | #ink_1 |  | npe |
| 121 | `del` | 169r | seg-b3-c6p8b-mondo-beati | deletion | #ink_1 |  |  |
| 122 | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 123 | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 124 | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | dire |
| 125 | `del` | 170v | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  |  |
| 126 | `del` | 170v | seg-b3-c6p21-braggia-similitudine | deletion | #ink_1 |  |  |
| 127 | `del` | 171v | seg-b3-c6p26-esposti-guardia | deletion | #ink_1 |  |  |
| 128 | `del` | 172v | seg-b3-c6p33-puo-cadere-guardia | deletion | #ink_1 |  |  |
| 129 | `del` | 173v | seg-b3-c7p9-precisazione-operare-participatione | deletion | #ink_1 |  | ed |
| 130 | `del` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | deletion | #ink_1 |  |  |
| 131 | `del` | 174v | seg-b3-c7p21-similitudine-cera-sole | deletion | #ink_1 |  | per |
| 132 | `del` | 175r | seg-b3-c7p22-fiamma-fuoco | deletion | #ink_1 |  | ap |
| 133 | `del` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | deletion | #ink_1 |  | pop |
| 134 | `del` | 175v | - | deletion | #ink_1 |  | se |
| 135 | `del` | 176v | seg-b3-c8p8-distrattioni | deletion | #ink_1 |  | co |
| 136 | `del` | 176v | seg-b3-c8p10-quattroparti | correction | #ink_1 |  | e |
| 137 | `del` | 177v | seg-b3-c8p18-bocca-sostanza | deletion | #ink_1 |  | d |
| 138 | `del` | 177v | seg-b3-c8p19-contatto-gloria | deletion | #ink_1 |  | intende |
| 139 | `del` | 178r | seg-b3-c8p21-esorto-hore | deletion | #ink_1 |  | t |
| 140 | `del` | 178r | seg-b3-c8p21-sicurta-cadute | deletion | #ink_1 |  | , |
| 141 | `del` | 179r | seg-b3-c8p25-estremi-sole | deletion | #ink_1 |  |  |
| 142 | `del` | 179r | seg-b3-c8p25-propria-stima | deletion | #ink_1 |  | che |
| 143 | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 144 | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 145 | `del` | 183r | seg-b3-c10p8-riequilibrio-fatica | deletion | #ink_1 |  |  |
| 146 | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | a |
| 147 | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | e |
| 148 | `del` | 193r | seg-b3-c12p3-ricevere-consenso | deletion | #ink_1 |  | con |
| 149 | `del` | 193r | seg-b3-c12p4-addormentarsi-amato | deletion | #ink_1 |  |  |
| 150 | `del` | 193v | seg-b3-c12p5-atti-continui | deletion | #ink_1 |  | per |
| 151 | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | f |
| 152 | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | sopr. |
| 153 | `del` | 195v | seg-b3-c14p5-sapienza-agonia | deletion | #ink_1 |  | s'an |
| 154 | `del` | 195v | seg-b3-c14p6-ombra-certezza | deletion | #ink_1 |  |  |
| 155 | `del` | 201r | seg-b3-c16p28-niente-trasformatione | deletion | #ink_1 |  |  |
| 156 | `del` | 202r | seg-b3-c16p37-certezza-niente | deletion | #ink_1 |  |  |
| 157 | `del` | 207v | seg-b3-c19p4-definizione-amicitia | deletion | #ink_1 |  | super |
| 158 | `del` | 208v | seg-b3-c19p11-riepilogo-gradi | deletion | #ink_1 |  | super |
| 159 | `del` | 221r | seg-b3-c24p16-glossa-humanita | deletion | #ink_3-dark |  | G |
| 160 | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | di Dio |
| 161 | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | detta |
| 162 | `del` | 248v | seg-b3-c34p17-olimpo-altezza | deletion | #ink_1 |  | t |
| 163 | `del` | 257v | seg-b3-c38p9-brama-padre-preghiera | deletion | #ink_1 |  |  |
| 164 | `del` | 258r | seg-b3-c38p13-persecutione-terzapersona | deletion | #ink_1 |  | tanti |
| 165 | `del` | 258v | seg-b3-c38p18-fede-oscurata | deletion | #ink_1 |  |  |
| 166 | `del` | 258v | seg-b3-c38p19-perdita-fede | deletion | #ink_1 |  |  |
| 167 | `del` | 262r | - | deletion | #ink_1 |  | trigesimo |
| 168 | `subst` | 1r | seg-b1-c1p1-miseria-creato |  |  |  |  |
| 169 | `subst` | 14r | seg-b1-c6p5-obedienza-penitenza |  |  |  |  |
| 170 | `subst` | 159v | seg-b3-c2p1-obbedienza-incipit |  |  |  |  |
| 171 | `subst` | 160v | seg-b3-c2p10-linguaggio-oscuro |  |  |  |  |
| 172 | `subst` | 161v | seg-b3-c2p16-silentio-non-parla |  |  |  |  |
| 173 | `subst` | 161v | seg-b3-c2p19-demonio-escluso |  |  |  |  |
| 174 | `subst` | 162r | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 175 | `subst` | 162v | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 176 | `subst` | 162v | seg-b3-c3p1-esortazione |  |  |  |  |
| 177 | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 178 | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 179 | `subst` | 165r | seg-b3-c4p5-precisatio-sospensione |  |  |  |  |
| 180 | `subst` | 167r | seg-b3-c5p7-amore-prossimo |  |  |  |  |
| 181 | `subst` | 176v | seg-b3-c8p10-quattroparti |  |  |  |  |
| 182 | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 183 | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 184 | `retrace` | 159v | seg-b3-c2p2-fondo-anima |  | #ink_1 | medium | tem |
| 185 | `retrace` | 160v | seg-b3-c2p10-linguaggio-oscuro |  | #ink_1 | medium | è |
| 186 | `retrace` | 163r | seg-b3-c3p4-fondoraccolto |  | #ink_1 | medium | tom |
| 187 | `retrace` | 163r | seg-b3-c3p5-chiarezza |  | #ink_1 | medium | te |
| 188 | `retrace` | 163v | seg-b3-c3p7-declaratio-verita |  | #ink_1 | medium | u |
| 189 | `retrace` | 164r | seg-b3-c3p9-fortezza |  | #ink_1 | medium | e |
| 190 | `retrace` | 164r | seg-b3-c3p11-comunicazione |  | #ink_1 | medium | r |
| 191 | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | m |
| 192 | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | n |
| 193 | `retrace` | 164v | seg-b3-c3p14-mirabilia |  | #ink_1 | medium | mino |
| 194 | `retrace` | 164v | seg-b3-c4p2-attuale-habituale |  | #ink_1 | medium | l |
| 195 | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | c |
| 196 | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | n |
| 197 | `retrace` | 165r | seg-b3-c4p7-nuova-caccia-vecchia |  | #ink_1 | medium | s |
| 198 | `retrace` | 166v | seg-b3-c5p6-cessano-zeli |  | #ink_1 | medium | z |
| 199 | `retrace` | 167v | seg-b3-c5p12-affetti-persi |  | #ink_1 | medium | a |
| 200 | `retrace` | 169r | seg-b3-c6p8-innocenza-guardia |  | #ink_1 |  | b |
| 201 | `retrace` | 170v | seg-b3-c6p17-fede-prattica-guardia |  | #ink_1 |  | l |
| 202 | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | n |
| 203 | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | t |
| 204 | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | p |
| 205 | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | g |
| 206 | `retrace` | 170v | seg-b3-c6p22-fiamma-estasi |  | #ink_1 |  | m |
| 207 | `retrace` | 172v | seg-b3-c6p33-puo-cadere-guardia |  | #ink_1 |  | in |
| 208 | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 209 | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 210 | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | c |
| 211 | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | m |
| 212 | `retrace` | 176r | seg-b3-c8p3-morte-vitanuova |  | #ink_1 | medium | m |
| 213 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | r |
| 214 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | m |
| 215 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | t |
| 216 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | n |
| 217 | `retrace` | 176r | seg-b3-c8p6-sensi-sposalitio |  | #ink_1 | medium | nn |
| 218 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | c |
| 219 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 220 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 221 | `retrace` | 177r | seg-b3-c8p15-lambino |  | #ink_1 | medium | lambino |
| 222 | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | tinuo |
| 223 | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | co |
| 224 | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | ricittavolo |
| 225 | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | co |
| 226 | `retrace` | 178r | seg-b3-c8p21-esorto-hore |  | #ink_1 | medium | scu |
| 227 | `retrace` | 197v | seg-b3-c16p6-carne-con-carne |  | #ink_1 |  | c |
| 228 | `retrace` | 198v | seg-b3-c16p15-molte-strade |  | #ink_1 |  | r |
| 229 | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | m |
| 230 | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | t |
| 231 | `retrace` | 200v | seg-b3-c16p26-festa-sensi |  | #ink_1 |  | e |
| 232 | `retrace` | 202r | seg-b3-c16p37-certezza-niente |  | #ink_1 |  | e |
| 233 | `retrace` | 219v | seg-b3-c24p2-timore-naturale |  | #ink_1 |  | d |
| 234 | `retrace` | 220v | seg-b3-c24p13-fiducia-abbandono |  | #ink_1 |  | men |
| 235 | `gap` | 3v | seg-b1-c2p14-claustrati-secolari | cancelled |  |  |  |
| 236 | `gap` | 6r | seg-b1-c4p4-adoperarsi-notte | illegible |  |  |  |
| 237 | `gap` | 10v | seg-b1-c5p11-fondamento-castello | illegible |  |  |  |
| 238 | `gap` | 11r | seg-b1-c5p16-non-dar-parere | illegible |  |  |  |
| 239 | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 240 | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 241 | `gap` | 12r | seg-b1-c5p33-finta-humilta | illegible |  |  |  |
| 242 | `gap` | 12v | seg-b1-c5p38-humilta-vera-quiete | illegible |  |  |  |
| 243 | `gap` | 12v | seg-b1-c5p41-rimedi-padre | illegible |  |  |  |
| 244 | `gap` | 13v | seg-b1-c5p61-comperatione-fine | illegible |  |  |  |
| 245 | `gap` | 14r | seg-b1-c6p4-desiderio-sudita | illegible |  |  |  |
| 246 | `gap` | 23r | seg-b1-c11p58-carita-cura | hole |  |  |  |
| 247 | `gap` | 145v | seg-b2-c21p9-resta-il-male | illegible |  |  |  |
| 248 | `gap` | 152v | seg-b2-c21p36-protesta | illegible |  |  |  |
| 249 | `gap` | 159r | seg-b3-c1p10-unione-velata | illegible |  |  |  |
| 250 | `gap` | 159r | - | hole |  |  |  |
| 251 | `gap` | 159v | seg-b3-c2p3-comparatione-teresa | illegible |  |  |  |
| 252 | `gap` | 160r | seg-b3-c2p6-differenza-raccoglimento | illegible |  |  |  |
| 253 | `gap` | 161r | seg-b3-c2p13-castellano-secreto | illegible |  |  |  |
| 254 | `gap` | 161r | seg-b3-c2p15-comunicazione-diretta | illegible |  |  |  |
| 255 | `gap` | 162v | seg-b3-c3p1-santamadre | hole |  |  |  |
| 256 | `gap` | 163r | seg-b3-c3p5-propriastima | hole |  |  |  |
| 257 | `gap` | 163v | seg-b3-c3p7-statuette | hole |  |  |  |
| 258 | `gap` | 163v | seg-b3-c3p7-magnificar | hole |  |  |  |
| 259 | `gap` | 164r | seg-b3-c3p12-linguaggio | illegible |  |  |  |
| 260 | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 261 | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 262 | `gap` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  |  |  |
| 263 | `gap` | 168r | seg-b3-c6p3-morire-spogliarsi | illegible |  |  |  |
| 264 | `gap` | 168r | seg-b3-c6p4-fomite-peccato | hole |  |  |  |
| 265 | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 266 | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 267 | `gap` | 169r | seg-b3-c6p8b-mondo-beati | illegible |  |  |  |
| 268 | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 269 | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 270 | `gap` | 170r | seg-b3-c6p15-adamo-guardia | hole |  |  |  |
| 271 | `gap` | 170r | seg-b3-c6p15-adamo-guardia | illegible |  |  |  |
| 272 | `gap` | 170v | seg-b3-c6p17-fede-prattica-guardia | illegible |  |  |  |
| 273 | `gap` | 170v | seg-b3-c6p21-braggia-similitudine | illegible |  |  |  |
| 274 | `gap` | 171v | seg-b3-c6p26-esposti-guardia | illegible |  |  |  |
| 275 | `gap` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  |  |  |
| 276 | `gap` | 178r | seg-b3-c8p21-esorto-hore | illegible |  |  |  |
| 277 | `gap` | 179r | seg-b3-c8p25-estremi-sole | illegible |  |  |  |
| 278 | `gap` | 179r | seg-b3-c8p25-propria-stima | illegible |  |  |  |
| 279 | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 280 | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 281 | `gap` | 183r | seg-b3-c10p8-riequilibrio-fatica | illegible |  |  |  |
| 282 | `gap` | 193r | seg-b3-c12p4-addormentarsi-amato | illegible |  |  |  |
| 283 | `gap` | 195v | seg-b3-c14p6-ombra-certezza | illegible |  |  |  |
| 284 | `gap` | 198v | seg-b3-c16p13-esperienza-propria | hole |  |  |  |
| 285 | `gap` | 201r | seg-b3-c16p28-niente-trasformatione | illegible |  |  |  |
| 286 | `gap` | 202r | seg-b3-c16p37-certezza-niente | illegible |  |  |  |
| 287 | `gap` | 202v | seg-b3-c16p39-capi-eresia | illegible |  |  |  |
| 288 | `gap` | 221r | seg-b3-c24p16-glossa-humanita | hole |  |  |  |
| 289 | `gap` | 246v | seg-b3-c34p3-identita-distinte | hole |  |  |  |
| 290 | `gap` | 248v | seg-b3-c34p17-olimpo-altezza | illegible |  |  |  |
| 291 | `gap` | 257v | seg-b3-c38p9-brama-padre-preghiera | illegible |  |  |  |
| 292 | `gap` | 258v | seg-b3-c38p18-fede-oscurata | illegible |  |  |  |
| 293 | `gap` | 261r | seg-b3-c39p16-annichilazione-insensibile | hole |  |  |  |
| 294 | `gap` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  |  |  |
| 295 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 296 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 297 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 298 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 299 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 300 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 301 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 302 | `unclear` | 168r | seg-b3-c6p4-fomite-peccato | illegible |  |  | st |
| 303 | `unclear` | 172v | seg-b3-c6p33-puo-cadere-guardia | illegible |  |  | ch |
| 304 | `unclear` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | illegible |  |  | P |
| 305 | `unclear` | 174v | seg-b3-c7p17-glossa-fortezza-timore | illegible |  |  | lacciuto |
| 306 | `unclear` | 219r | - | stain |  |  | emita |
| 307 | `unclear` | 258v | seg-b3-c38p19-perdita-fede | stain |  |  | no |
| 308 | `supplied` | 3r | seg-b1-c2p6-nemico-demonio | hole |  | high | r |
| 309 | `supplied` | 3r | seg-b1-c2p7-tre-nemici | hole |  | high | n |
| 310 | `supplied` | 3v | seg-b1-c2p8-citta-assediata | hole |  | high | ste |
| 311 | `supplied` | 6v | seg-b1-c4p15-notte-necessaria | hole |  | high | ra |
| 312 | `supplied` | 7v | seg-b1-c4p26-prima-purga-dura | hole |  | high | p |
| 313 | `supplied` | 8r | seg-b1-c4p32-merito-bandiera | hole |  | high | p |
| 314 | `supplied` | 9r | seg-b1-c4p47-san-paolo-vocatione | hole |  | high | co |
| 315 | `supplied` | 9v | seg-b1-c4p55-temer-occasione | hole |  | high | ch |
| 316 | `supplied` | 10r | seg-b1-c5p1-metafora-fondamento | hole |  | high | lo |
| 317 | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | u |
| 318 | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | m |
| 319 | `supplied` | 10v | seg-b1-c5p3-cristo-peccatori | hole |  | medium | i |
| 320 | `supplied` | 10v | seg-b1-c5p11-fondamento-castello | hole |  | high | nto |
| 321 | `supplied` | 10v | seg-b1-c5p13-esterno-interno | hole |  | high | qu |
| 322 | `supplied` | 11r | seg-b1-c5p19-mortificar-passioni | hole |  | high | re |
| 323 | `supplied` | 11r | seg-b1-c5p20-anime-principianti | hole |  | high | o f |
| 324 | `supplied` | 11v | seg-b1-c5p26-rammarico-quiete | hole |  | high | l |
| 325 | `supplied` | 11v | seg-b1-c5p28-distacco-spirito | hole |  | high | i |
| 326 | `supplied` | 12r | seg-b1-c5p28-distacco-spirito | omitted |  | high | ma |
| 327 | `supplied` | 12r | seg-b1-c5p33-finta-humilta | hole |  | high | bil |
| 328 | `supplied` | 12v | seg-b1-c5p41-rimedi-padre | hole |  | high | op |
| 329 | `supplied` | 13r | seg-b1-c5p49-humilta-contrario | hole |  | high | m |
| 330 | `supplied` | 13r | seg-b1-c5p51-voltare-mondo | hole |  | high | a |
| 331 | `supplied` | 13v | seg-b1-c5p51-voltare-mondo | hole |  | high | à l' |
| 332 | `supplied` | 14r | seg-b1-c6p5-obedienza-penitenza | hole |  | high | l |
| 333 | `supplied` | 14r | seg-b1-c6p8-vite-santi | hole |  | high | d |
| 334 | `supplied` | 14v | seg-b1-c6p16-approfittate-intelletto | hole |  | high | i |
| 335 | `supplied` | 15r | seg-b1-c6p18-conclusione | omitted |  | high | t |
| 336 | `supplied` | 20r | seg-b1-c11p3-fatiche-niente | hole |  | high | qui |
| 337 | `supplied` | 20v | seg-b1-c11p13-mondo-schernisce | hole |  | high | lto |
| 338 | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | m |
| 339 | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | l |
| 340 | `supplied` | 21r | seg-b1-c11p23-ripugnanza-merito | hole |  | high | li d |
| 341 | `supplied` | 21v | seg-b1-c11p23-ripugnanza-merito | hole |  | high | l |
| 342 | `supplied` | 21v | seg-b1-c11p30-obedienza-toglie | hole |  | high | gli |
| 343 | `supplied` | 22r | seg-b1-c11p42-frutti-fanciulli | hole |  | high | al |
| 344 | `supplied` | 22v | seg-b1-c11p50-contadino-diligente | hole |  | high | r |
| 345 | `supplied` | 23r | seg-b1-c11p56-principianti-forze | hole |  | high | co |
| 346 | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | medium | l |
| 347 | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | high | tra |
| 348 | `supplied` | 23v | seg-b1-c11p64-cieca-obedienza | hole |  | high | e |
| 349 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | p |
| 350 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | i e |
| 351 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | a co |
| 352 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | d h |
| 353 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | e |
| 354 | `supplied` | 66v | seg-b2-c2p9-secretum | stain |  | medium | i |
| 355 | `supplied` | 70v | seg-b2-c3p8-proibir-lettura | omitted |  | medium | darà questo |
| 356 | `supplied` | 71v | seg-b2-c3p15-non-humore | omitted |  | high | ta |
| 357 | `supplied` | 73v | seg-b2-c4p8-enumerazione-sensi | stain |  | medium | ro |
| 358 | `supplied` | 75r | seg-b2-c5p4-liberta-quiete | omitted |  | medium | a |
| 359 | `supplied` | 75r | seg-b2-c5p4-liberta-quiete | omitted |  | medium | n |
| 360 | `supplied` | 75r | seg-b2-c5p5-timor-di-dio | omitted |  | medium | s |
| 361 | `supplied` | 75v | seg-b2-c5p8-dispositione-sponsale | stain |  | medium | qua |
| 362 | `supplied` | 80v | seg-b2-c7p1-raccoglimento-quiete | editorial |  | medium | isc |
| 363 | `supplied` | 81v | seg-b2-c7p4-sameritana | stain |  | medium | ia |
| 364 | `supplied` | 82r | seg-b2-c7p10-sensi-non-persi | stain |  | medium | ora |
| 365 | `supplied` | 82v | seg-b2-c7p10-volonta-fragilta | editorial |  | medium | con |
| 366 | `supplied` | 83r | seg-b2-c7p17-volonta-opera | editorial |  | medium | a |
| 367 | `supplied` | 84r | seg-b2-c7p21-terza-sospensione | editorial |  | medium | o |
| 368 | `supplied` | 86r | seg-b2-c7p35-effetti-falsi | editorial |  | medium | a |
| 369 | `supplied` | 88r | seg-b2-c8p3-abbandono-corpo | stain |  | high | e |
| 370 | `supplied` | 92r | seg-b2-c8p13-unione-attuale | stain |  | high | ua |
| 371 | `supplied` | 94v | seg-b2-c8p17-uscita-effetti | hole |  | high | to |
| 372 | `supplied` | 104v | seg-b2-c9p8-gelosia | illegible |  | medium | 'a |
| 373 | `supplied` | 104v | seg-b2-c9p8-gelosia | illegible |  | medium | io |
| 374 | `supplied` | 104v | seg-b2-c9p8-gelosia | illegible |  | medium | ge |
| 375 | `supplied` | 108r | seg-b2-c9p32-chiusa-bassello | damage |  | high | co |
| 376 | `supplied` | 108r | seg-b2-c9p32-chiusa-bassello | damage |  | high | utt |
| 377 | `supplied` | 108v | seg-b2-c10p4-horto-aura | damage |  | medium | i |
| 378 | `supplied` | 138r | - | heading-omitted |  | high | Capitolo vigesimo |
| 379 | `supplied` | 138r | seg-b2-c20p3-artefice-fuoco | damage |  | medium | e |
| 380 | `supplied` | 138r | seg-b2-c20p4-attonita-assorbita | damage |  | medium | sì |
| 381 | `supplied` | 138v | seg-b2-c20p8-alligirimenti | damage |  | medium | nd |
| 382 | `supplied` | 139r | seg-b2-c20p12-principi-sollievi | damage |  | medium | orti |
| 383 | `supplied` | 139v | seg-b2-c20p18-scoltore-statua | damage |  | medium | bel |
| 384 | `supplied` | 140r | seg-b2-c20p24-abbandono-unione | damage |  | medium | poi |
| 385 | `supplied` | 141v | seg-b2-c20p39-olio-balsami | damage |  | medium | d |
| 386 | `supplied` | 142r | seg-b2-c20p42-disciplina | damage |  | medium | ua |
| 387 | `supplied` | 143r | seg-b2-c21p1-artefice-fuoco | hole |  | medium | r |
| 388 | `supplied` | 144r | seg-b2-c21p6-tre-notti | hole |  | medium | c |
| 389 | `supplied` | 145r | seg-b2-c21p6-tre-notti | hole |  | medium | rt |
| 390 | `supplied` | 145v | seg-b2-c21p8-purga-passioni | damage |  | medium | delli sensi |
| 391 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | hole |  | medium | tre |
| 392 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | damage |  | low | supeditate |
| 393 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | hole |  | medium | d |
| 394 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | hole |  | medium | per |
| 395 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | hole |  | medium | art |
| 396 | `supplied` | 145v | seg-b2-c21p9-resta-il-male | hole |  | medium | l |
| 397 | `supplied` | 146r | seg-b2-c21p11-iam-hiems | hole |  | medium | er |
| 398 | `supplied` | 147r | seg-b2-c21p14-statua-legno | hole |  | medium | r |
| 399 | `supplied` | 147v | seg-b2-c21p16-purga-lunga | hole |  | medium | D |
| 400 | `supplied` | 149r | seg-b2-c21p21-torniamo-patire | hole |  | medium | in |
| 401 | `supplied` | 149v | seg-b2-c21p23-tentazioni-scrupoli | hole |  | medium | ca |
| 402 | `supplied` | 151v | seg-b2-c21p31-contadino-prencipe | hole |  | medium | sa |
| 403 | `supplied` | 152r | seg-b2-c21p33-abbandono-naturale | hole |  | medium | l |
| 404 | `supplied` | 159r | - | hole |  | medium | e |
| 405 | `supplied` | 160r | seg-b3-c2p5-sposo-quiete | hole |  | medium | e |
| 406 | `supplied` | 160v | seg-b3-c2p12-castello-fondo | hole |  | medium | u |
| 407 | `supplied` | 161r | seg-b3-c2p13-castellano-secreto | hole |  | medium | e |
| 408 | `supplied` | 161v | seg-b3-c2p18-pace-continua | hole |  | medium | io |
| 409 | `supplied` | 162r | seg-b3-c2p20-autonomia-direttore | hole |  | medium | a |
| 410 | `supplied` | 162v | seg-b3-c3p1-santamadre | hole |  | medium | i |
| 411 | `supplied` | 163r | seg-b3-c3p5-propriastima | hole |  | medium | nt |
| 412 | `supplied` | 163v | seg-b3-c3p7-statuette | hole |  | medium | a |
| 413 | `supplied` | 163v | seg-b3-c3p7-magnificar | hole |  | medium | i |
| 414 | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | modo |
| 415 | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | arse |
| 416 | `supplied` | 165r | seg-b3-c4p8-conclusio | hole |  | medium | à |
| 417 | `supplied` | 166v | seg-b3-c5p6-non-capace-pena | hole |  | medium | e |
| 418 | `supplied` | 167r | seg-b3-c5p7-amore-prossimo | hole |  | medium | i |
| 419 | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | e |
| 420 | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | o |
| 421 | `supplied` | 169r | seg-b3-c6p8-innocenza-guardia | hole |  | high | e |
| 422 | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | a |
| 423 | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | n |
| 424 | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | à |
| 425 | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | a |
| 426 | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | stain |  | medium | n |
| 427 | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | hole |  | medium | ano |
| 428 | `supplied` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | hole |  | medium | s |
| 429 | `supplied` | 174v | seg-b3-c7p17-glossa-fortezza-timore | hole |  | low | deve temere |
| 430 | `supplied` | 175v | seg-b3-c8p2-roma | hole |  | medium | v |
| 431 | `supplied` | 177r | seg-b3-c8p15-lambino | hole |  | medium | a |
| 432 | `supplied` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  | medium | a |
| 433 | `supplied` | 179r | seg-b3-c8p27-continua-oratione | hole |  | medium | oratione |
| 434 | `supplied` | 197r | seg-b3-c16p3-distinzione-unione | hole |  | medium | c |
| 435 | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | ret |
| 436 | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | n |
| 437 | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | a |
| 438 | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | P |
| 439 | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | e |
| 440 | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | Anch |
| 441 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ra |
| 442 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | e |
| 443 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ass |
| 444 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | g |
| 445 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | c |
| 446 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | re |
| 447 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | sa |
| 448 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | rl |
| 449 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | iù |
| 450 | `supplied` | 209v | seg-b3-c19p22-partecipazione-corpo | hole |  | medium | me |
| 451 | `supplied` | 219r | - | hole |  | medium | enta |
| 452 | `supplied` | 220v | seg-b3-c24p10-distinzione-interni | hole |  | medium | cu |
| 453 | `supplied` | 220v | seg-b3-c24p12-abbandono-padre | hole |  | medium | n |
| 454 | `supplied` | 220v | seg-b3-c24p14-critica-padri | hole |  | medium | c |
| 455 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | esse |
| 456 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | nza |
| 457 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | star |
| 458 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | medium | o pare |
| 459 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | e |
| 460 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 461 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 462 | `supplied` | 242r | seg-b3-c32p2-incognito-ineffabile | hole |  | high | a |
| 463 | `supplied` | 242v | seg-b3-c32p2-incognito-ineffabile | hole |  | high | v |
| 464 | `supplied` | 242v | seg-b3-c32p3-trasformazione-crocifisso | hole |  | high | l |
| 465 | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | in |
| 466 | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | è |
| 467 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | croci |
| 468 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | sì co |
| 469 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | li |
| 470 | `supplied` | 246v | seg-b3-c34p3-identita-distinte | hole |  | high | ù |
| 471 | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | ivon |
| 472 | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | no |
| 473 | `supplied` | 248r | seg-b3-c34p13-tentatione-agostino | hole |  | high | i |
| 474 | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | hole |  | high | ne |
| 475 | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | stain |  | medium | e |
| 476 | `supplied` | 256v | seg-b3-c38p4-aridita-continua | hole |  | high | vo |
| 477 | `supplied` | 257r | seg-b3-c38p8-discernimento-brama | hole |  | high | ti |
| 478 | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | i |
| 479 | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | dre |
| 480 | `supplied` | 257v | seg-b3-c38p11-benevolenza-honore | hole |  | high | he |
| 481 | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | ar |
| 482 | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | re |
| 483 | `supplied` | 259r | seg-b3-c39p4-deificatione-imagine | hole |  | high | ic |
| 484 | `supplied` | 259v | seg-b3-c39p5-precisazione-matrimonio | hole |  | medium | perita |
| 485 | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | tro si |
| 486 | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | dal |
| 487 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | stain |  | medium | re |
| 488 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d |
| 489 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d in |
| 490 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d a |
| 491 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | in |
| 492 | `supplied` | 261r | seg-b3-c39p13-silentio-annientamento | hole |  | high | nel |
| 493 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | rtù |
| 494 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | st' |
| 495 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | é |
| 496 | `supplied` | 262r | seg-b3-c39p20-salamandra | hole |  | medium | tan |
| 497 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | p |
| 498 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ti |
| 499 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | pro |
| 500 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ità |
| 501 | `supplied` | 262v | seg-b3-c40p2-cella-intima | hole |  | medium | t |
| 502 | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ugiato |
| 503 | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ett |
| 504 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 505 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | s |
| 506 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 507 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | ho |
