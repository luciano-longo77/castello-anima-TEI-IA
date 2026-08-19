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
| `add` | 69 | 69 | 7 |
| `del` | 96 | 96 | 0 |
| `subst` | 16 | 0 | 0 |
| `retrace` | 51 | 51 | 33 |
| `gap` | 65 | 0 | 0 |
| `unclear` | 6 | 0 | 0 |
| `supplied` | 150 | 0 | 150 |

### 1.1 Dettaglio dei valori

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
| 10 | `add` | 158r | seg-b3-pro-p1-incapacitas | substitution | #ink_1 |  | i |
| 11 | `add` | 158v | seg-b3-c1p4-pace2 | substitution | #ink_1 |  | e |
| 12 | `add` | 158v | seg-b3-c1p7-viaggio | substitution | #ink_1 |  | e |
| 13 | `add` | 159v | seg-b3-c2p1-obbedienza-incipit | substitution | #ink_1 |  | a |
| 14 | `add` | 159v | seg-b3-c2p3-comparatione-teresa | supralinear | #ink_3-dark | medium | adacquar |
| 15 | `add` | 160v | seg-b3-c2p10-linguaggio-oscuro | substitution | #ink_1 |  | i |
| 16 | `add` | 161v | seg-b3-c2p16-silentio-non-parla | substitution | #ink_1 |  | i |
| 17 | `add` | 161v | seg-b3-c2p19-demonio-escluso | substitution | #ink_1 |  | i |
| 18 | `add` | 162r | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 19 | `add` | 162v | seg-b3-c3p1-ripugnanza | substitution | #ink_1 |  | i |
| 20 | `add` | 162v | seg-b3-c3p1-esortazione | substitution | #ink_1 |  | o |
| 21 | `add` | 162v | seg-b3-c3p3-raccoglimento | supralinear | #ink_1 |  |  |
| 22 | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | a |
| 23 | `add` | 163v | seg-b3-c3p7-declaratio-verita | substitution | #ink_1 |  | i |
| 24 | `add` | 164v | seg-b3-c3p14-mirabilia | margin-left | #ink_3-dark | medium | dico ciò non perché non s'ha detto la |
| 25 | `add` | 165r | seg-b3-c4p5-precisatio-sospensione | substitution | #ink_1 |  | i |
| 26 | `add` | 167r | seg-b3-c5p7-amore-prossimo | substitution | #ink_1 |  | e |
| 27 | `add` | 167r | seg-b3-c5p8-non-desiderar-croce | supralinear | #ink_1 |  | ar |
| 28 | `add` | 167r | seg-b3-c5p9-non-desiderar-morte | margin-left | #ink_1 | medium | Ciò s'intende per non |
| 29 | `add` | 167r | seg-b3-c5p10-palla-cera | inline | #ink_3-dark | medium | Ciò non s'intende a cose di male, ma che |
| 30 | `add` | 168r | seg-b3-c6p2-trasformazione-fomite | margin-right | #ink_3-dark |  | More alli mali habiti dell' |
| 31 | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-right | #ink_3-dark |  | ciò perché l' |
| 32 | `add` | 168r | seg-b3-c6p4-fomite-peccato | margin-bottom | #ink_3-dark |  | in questi tempi viene tanto supeditato d |
| 33 | `add` | 169r | seg-b3-c6p8-innocenza-guardia | margin-right | #ink_3-dark |  | però sappiasi che siemo in via, tememo,  |
| 34 | `add` | 169r | seg-b3-c6p8-innocenza-guardia | supralinear | #ink_1 |  | mo |
| 35 | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | quasi |
| 36 | `add` | 170r | seg-b3-c6p15-adamo-guardia | margin-left | #ink_3-dark |  | pe |
| 37 | `add` | 171r | seg-b3-c6p22-fiamma-estasi | supralinear | #ink_1 |  | alle volte |
| 38 | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | margin-left | #ink_1 |  | questo s'intende per qua |
| 39 | `add` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | supralinear | #ink_1 |  | n |
| 40 | `add` | 174r | seg-b3-c7p12-dichiarazione-ortodossia-consomato | margin-right | #ink_3-dark |  | quasi |
| 41 | `add` | 174v | seg-b3-c7p17-glossa-fortezza-timore | margin-left | #ink_1 |  | cioè per la |
| 42 | `add` | 174v | seg-b3-c7p17-glossa-desiderio-temporaneo | margin-left | #ink_1 |  | cioè per qualche tempo dura il |
| 43 | `add` | 176r | seg-b3-c8p4-riequilibrio-vita | margin | #ink_3-dark | medium | sì bene lo |
| 44 | `add` | 176v | seg-b3-c8p10-quattroparti | substitution | #ink_1 |  | i |
| 45 | `add` | 178r | seg-b3-c8p22-replica-hore | supralinear | #ink_1 |  | cioè |
| 46 | `add` | 179r | seg-b3-c8p27-continua-oratione | margin-right | #ink_3-dark | medium | sì bene i sensi non donano in desordene, |
| 47 | `add` | 182v | seg-b3-c10p6-precisazione-volonta | margin | #ink_3-dark |  | cioè non ha sensi, e passioni tanto vive |
| 48 | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | e |
| 49 | `add` | 193r | seg-b3-c12p2-atteggiare-acquisita | substitution | #ink_1 |  | o |
| 50 | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | solo |
| 51 | `add` | 197v | seg-b3-c16p6-carne-con-carne | supralinear | #ink_3-dark |  | ancora |
| 52 | `add` | 197v | seg-b3-c16p6-carne-con-carne | margin-right | #ink_1 |  | E viene l'anima a non credere più quanto |
| 53 | `add` | 200v | seg-b3-c16p25-allegoria-re | supralinear | #ink_3-dark |  | stanza |
| 54 | `add` | 210r | seg-b3-c19p24-rimando-metatestuale | margin-left | #ink_1 |  | Doppo d'haver fornito questo capitolo, e |
| 55 | `add` | 219v | seg-b3-c24p6-prudenza-penitenza | supralinear | #ink_1 |  | giorni |
| 56 | `add` | 221r | seg-b3-c24p16-glossa-humanita | margin-right | #ink_3-dark |  | cioè non che la |
| 57 | `add` | 247r | seg-b3-c34p6-mutatione-oscuro | supralinear | #ink_1 |  | habituale |
| 58 | `add` | 247r | seg-b3-c34p7-effetti-taciuti | supralinear | #ink_1 |  | la gratia di |
| 59 | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | supralinear | #ink_1 |  | queste |
| 60 | `add` | 258r | seg-b3-c38p13-persecutione-terzapersona | margin-right | #ink_3-dark | medium | ; e questo del palar tanto mi pareva pes |
| 61 | `add` | 258v | seg-b3-c38p19-dichiaro-permettendo | bottom | #ink_1 |  | Qui mi dichiaro che |
| 62 | `add` | 259r | - | inline | #ink_3-dark |  | per quanto può stare in via |
| 63 | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | inline | #ink_3-dark |  | cioè fuor della sua capacetà, ma |
| 64 | `add` | 259v | seg-b3-c39p5-precisazione-matrimonio | infralinear | #ink_1 |  | di essa |
| 65 | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | inline | #ink_3-dark |  | cioè questa libertà perduta non intento  |
| 66 | `add` | 259v | seg-b3-c39p6-precisazione-liberoarbitrio | infralinear | #ink_1 |  | o altre cose simili |
| 67 | `add` | 261v | seg-b3-c39p16-declaratio-antipanteismo | inline | #ink_3-dark |  | Io mi dichiaro che in tutte queste sorti |
| 68 | `add` | 262r | seg-b3-c39p21-corredenzione | inline | #ink_3-dark |  | Ciò s'intende unir li soi meriti con que |
| 69 | `add` | 262v | seg-b3-c40p3-sonno-corpo | margin-right | #ink_1 |  | S'intende però che il spirituali |
| 70 | `del` | 1r | seg-b1-c1p1-miseria-creato | correction | #ink_1 |  | queste |
| 71 | `del` | 3v | seg-b1-c2p14-claustrati-secolari | strikethrough | #ink_1 |  |  |
| 72 | `del` | 6r | seg-b1-c4p4-adoperarsi-notte | strikethrough | #ink_1 |  |  |
| 73 | `del` | 10v | seg-b1-c5p11-fondamento-castello | strikethrough | #ink_1 |  |  |
| 74 | `del` | 11r | seg-b1-c5p16-non-dar-parere | strikethrough | #ink_1 |  |  |
| 75 | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 76 | `del` | 12r | seg-b1-c5p31-parola-ingioriosa | strikethrough | #ink_1 |  |  |
| 77 | `del` | 12r | seg-b1-c5p33-finta-humilta | strikethrough | #ink_1 |  |  |
| 78 | `del` | 12v | seg-b1-c5p36-falsita-mondo | strikethrough | #ink_1 |  | Divini |
| 79 | `del` | 12v | seg-b1-c5p38-humilta-vera-quiete | strikethrough | #ink_1 |  |  |
| 80 | `del` | 12v | seg-b1-c5p41-rimedi-padre | strikethrough | #ink_1 |  |  |
| 81 | `del` | 13v | seg-b1-c5p61-comperatione-fine | strikethrough | #ink_1 |  | s |
| 82 | `del` | 14r | seg-b1-c6p4-desiderio-sudita | strikethrough | #ink_1 |  |  |
| 83 | `del` | 14r | seg-b1-c6p5-obedienza-penitenza | strikethrough | #ink_1 |  | penitenza |
| 84 | `del` | 14v | seg-b1-c6p11-vera-obedienza | strikethrough | #ink_1 |  | d'animo |
| 85 | `del` | 158r | seg-b3-pro-p1-invocatio | correction | #ink_1 |  | to |
| 86 | `del` | 158r | seg-b3-pro-p1-incapacitas | correction | #ink_1 |  | e |
| 87 | `del` | 158v | seg-b3-c1p4-pace2 | correction | #ink_1 |  | a |
| 88 | `del` | 158v | seg-b3-c1p7-viaggio | correction | #ink_1 |  | è |
| 89 | `del` | 159r | seg-b3-c1p10-unione-velata | correction | #ink_1 |  | sc |
| 90 | `del` | 159v | seg-b3-c2p1-obbedienza-incipit | correction | #ink_1 |  | e |
| 91 | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  | o |
| 92 | `del` | 159v | seg-b3-c2p3-comparatione-teresa | deletion | #ink_1 |  |  |
| 93 | `del` | 160r | seg-b3-c2p4-giardino-quiete | deletion | #ink_1 |  | o |
| 94 | `del` | 160r | seg-b3-c2p6-differenza-raccoglimento | deletion | #ink_1 |  |  |
| 95 | `del` | 160v | seg-b3-c2p10-linguaggio-oscuro | correction | #ink_1 |  | e |
| 96 | `del` | 161r | seg-b3-c2p13-castellano-secreto | deletion | #ink_1 |  |  |
| 97 | `del` | 161r | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  |  |
| 98 | `del` | 161v | seg-b3-c2p15-comunicazione-diretta | deletion | #ink_1 |  | diff |
| 99 | `del` | 161v | seg-b3-c2p16-silentio-non-parla | correction | #ink_1 |  | e |
| 100 | `del` | 161v | seg-b3-c2p19-demonio-escluso | correction | #ink_1 |  | e |
| 101 | `del` | 162r | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 102 | `del` | 162v | seg-b3-c3p1-ripugnanza | correction | #ink_1 |  | e |
| 103 | `del` | 162v | seg-b3-c3p1-esortazione | correction | #ink_1 |  | a |
| 104 | `del` | 162v | seg-b3-c3p2-definizione-oblio | deletion | #ink_1 |  | , |
| 105 | `del` | 162v | seg-b3-c3p3-raccoglimento | deletion | #ink_1 |  | sonno |
| 106 | `del` | 163r | seg-b3-c3p4-opera-divina | deletion | #ink_1 |  | di |
| 107 | `del` | 163r | seg-b3-c3p5-propriastima | deletion | #ink_1 |  | s. |
| 108 | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 109 | `del` | 163v | seg-b3-c3p7-declaratio-verita | correction | #ink_1 |  | e |
| 110 | `del` | 163v | seg-b3-c3p7-statuette | deletion | #ink_1 |  | di silen |
| 111 | `del` | 164r | seg-b3-c3p12-linguaggio | deletion | #ink_1 |  |  |
| 112 | `del` | 165r | seg-b3-c4p3-ineffabilita-labirinto | deletion | #ink_1 |  | pa |
| 113 | `del` | 165r | seg-b3-c4p5-precisatio-sospensione | correction | #ink_1 |  | e |
| 114 | `del` | 167r | seg-b3-c5p7-amore-prossimo | correction | #ink_1 |  | a |
| 115 | `del` | 167v | seg-b3-c5p12-affetti-persi | deletion | #ink_1 |  | che |
| 116 | `del` | 167v | seg-b3-c5p16-tocchi-sostanza | deletion | #ink_1 |  | vecchi |
| 117 | `del` | 168r | seg-b3-c6p4-fomite-peccato | deletion | #ink_1 |  |  |
| 118 | `del` | 169r | seg-b3-c6p8-innocenza-guardia | deletion | #ink_1 |  | npe |
| 119 | `del` | 169r | seg-b3-c6p8b-mondo-beati | deletion | #ink_1 |  |  |
| 120 | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 121 | `del` | 169r | seg-b3-c6p9-discernimento-guardia | deletion | #ink_1 |  |  |
| 122 | `del` | 169r | seg-b3-c6p10-impassibilita-guardia | deletion | #ink_1 |  | dire |
| 123 | `del` | 170v | seg-b3-c6p17-fede-prattica-guardia | deletion | #ink_1 |  |  |
| 124 | `del` | 170v | seg-b3-c6p21-braggia-similitudine | deletion | #ink_1 |  |  |
| 125 | `del` | 171v | seg-b3-c6p26-esposti-guardia | deletion | #ink_1 |  |  |
| 126 | `del` | 172v | seg-b3-c6p33-puo-cadere-guardia | deletion | #ink_1 |  |  |
| 127 | `del` | 173v | seg-b3-c7p9-precisazione-operare-participatione | deletion | #ink_1 |  | ed |
| 128 | `del` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | deletion | #ink_1 |  |  |
| 129 | `del` | 174v | seg-b3-c7p21-similitudine-cera-sole | deletion | #ink_1 |  | per |
| 130 | `del` | 175r | seg-b3-c7p22-fiamma-fuoco | deletion | #ink_1 |  | ap |
| 131 | `del` | 175r | seg-b3-c7p24-conclusione-precisazione-nature | deletion | #ink_1 |  | pop |
| 132 | `del` | 175v | - | deletion | #ink_1 |  | se |
| 133 | `del` | 176v | seg-b3-c8p8-distrattioni | deletion | #ink_1 |  | co |
| 134 | `del` | 176v | seg-b3-c8p10-quattroparti | correction | #ink_1 |  | e |
| 135 | `del` | 177v | seg-b3-c8p18-bocca-sostanza | deletion | #ink_1 |  | d |
| 136 | `del` | 177v | seg-b3-c8p19-contatto-gloria | deletion | #ink_1 |  | intende |
| 137 | `del` | 178r | seg-b3-c8p21-esorto-hore | deletion | #ink_1 |  | t |
| 138 | `del` | 178r | seg-b3-c8p21-sicurta-cadute | deletion | #ink_1 |  | , |
| 139 | `del` | 179r | seg-b3-c8p25-estremi-sole | deletion | #ink_1 |  |  |
| 140 | `del` | 179r | seg-b3-c8p25-propria-stima | deletion | #ink_1 |  | che |
| 141 | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 142 | `del` | 182v | seg-b3-c10p7-precisazione-perseveranza | deletion | #ink_1 |  |  |
| 143 | `del` | 183r | seg-b3-c10p8-riequilibrio-fatica | deletion | #ink_1 |  |  |
| 144 | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | a |
| 145 | `del` | 193r | seg-b3-c12p2-atteggiare-acquisita | correction | #ink_1 |  | e |
| 146 | `del` | 193r | seg-b3-c12p3-ricevere-consenso | deletion | #ink_1 |  | con |
| 147 | `del` | 193r | seg-b3-c12p4-addormentarsi-amato | deletion | #ink_1 |  |  |
| 148 | `del` | 193v | seg-b3-c12p5-atti-continui | deletion | #ink_1 |  | per |
| 149 | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | f |
| 150 | `del` | 193v | seg-b3-c12p7-otio-possesso | deletion | #ink_1 |  | sopr. |
| 151 | `del` | 195v | seg-b3-c14p5-sapienza-agonia | deletion | #ink_1 |  | s'an |
| 152 | `del` | 195v | seg-b3-c14p6-ombra-certezza | deletion | #ink_1 |  |  |
| 153 | `del` | 201r | seg-b3-c16p28-niente-trasformatione | deletion | #ink_1 |  |  |
| 154 | `del` | 202r | seg-b3-c16p37-certezza-niente | deletion | #ink_1 |  |  |
| 155 | `del` | 207v | seg-b3-c19p4-definizione-amicitia | deletion | #ink_1 |  | super |
| 156 | `del` | 208v | seg-b3-c19p11-riepilogo-gradi | deletion | #ink_1 |  | super |
| 157 | `del` | 221r | seg-b3-c24p16-glossa-humanita | deletion | #ink_3-dark |  | G |
| 158 | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | di Dio |
| 159 | `del` | 246r | seg-b3-c34p1-distinzione-crocifisso | deletion | #ink_1 |  | detta |
| 160 | `del` | 248v | seg-b3-c34p17-olimpo-altezza | deletion | #ink_1 |  | t |
| 161 | `del` | 257v | seg-b3-c38p9-brama-padre-preghiera | deletion | #ink_1 |  |  |
| 162 | `del` | 258r | seg-b3-c38p13-persecutione-terzapersona | deletion | #ink_1 |  | tanti |
| 163 | `del` | 258v | seg-b3-c38p18-fede-oscurata | deletion | #ink_1 |  |  |
| 164 | `del` | 258v | seg-b3-c38p19-perdita-fede | deletion | #ink_1 |  |  |
| 165 | `del` | 262r | - | deletion | #ink_1 |  | trigesimo |
| 166 | `subst` | 1r | seg-b1-c1p1-miseria-creato |  |  |  |  |
| 167 | `subst` | 14r | seg-b1-c6p5-obedienza-penitenza |  |  |  |  |
| 168 | `subst` | 159v | seg-b3-c2p1-obbedienza-incipit |  |  |  |  |
| 169 | `subst` | 160v | seg-b3-c2p10-linguaggio-oscuro |  |  |  |  |
| 170 | `subst` | 161v | seg-b3-c2p16-silentio-non-parla |  |  |  |  |
| 171 | `subst` | 161v | seg-b3-c2p19-demonio-escluso |  |  |  |  |
| 172 | `subst` | 162r | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 173 | `subst` | 162v | seg-b3-c3p1-ripugnanza |  |  |  |  |
| 174 | `subst` | 162v | seg-b3-c3p1-esortazione |  |  |  |  |
| 175 | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 176 | `subst` | 163v | seg-b3-c3p7-declaratio-verita |  |  |  |  |
| 177 | `subst` | 165r | seg-b3-c4p5-precisatio-sospensione |  |  |  |  |
| 178 | `subst` | 167r | seg-b3-c5p7-amore-prossimo |  |  |  |  |
| 179 | `subst` | 176v | seg-b3-c8p10-quattroparti |  |  |  |  |
| 180 | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 181 | `subst` | 193r | seg-b3-c12p2-atteggiare-acquisita |  |  |  |  |
| 182 | `retrace` | 159v | seg-b3-c2p2-fondo-anima |  | #ink_1 | medium | tem |
| 183 | `retrace` | 160v | seg-b3-c2p10-linguaggio-oscuro |  | #ink_1 | medium | è |
| 184 | `retrace` | 163r | seg-b3-c3p4-fondoraccolto |  | #ink_1 | medium | tom |
| 185 | `retrace` | 163r | seg-b3-c3p5-chiarezza |  | #ink_1 | medium | te |
| 186 | `retrace` | 163v | seg-b3-c3p7-declaratio-verita |  | #ink_1 | medium | u |
| 187 | `retrace` | 164r | seg-b3-c3p9-fortezza |  | #ink_1 | medium | e |
| 188 | `retrace` | 164r | seg-b3-c3p11-comunicazione |  | #ink_1 | medium | r |
| 189 | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | m |
| 190 | `retrace` | 164v | seg-b3-c3p13-santotio |  | #ink_1 | medium | n |
| 191 | `retrace` | 164v | seg-b3-c3p14-mirabilia |  | #ink_1 | medium | mino |
| 192 | `retrace` | 164v | seg-b3-c4p2-attuale-habituale |  | #ink_1 | medium | l |
| 193 | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | c |
| 194 | `retrace` | 165r | seg-b3-c4p3-ineffabilita-labirinto |  | #ink_1 | medium | n |
| 195 | `retrace` | 165r | seg-b3-c4p7-nuova-caccia-vecchia |  | #ink_1 | medium | s |
| 196 | `retrace` | 166v | seg-b3-c5p6-cessano-zeli |  | #ink_1 | medium | z |
| 197 | `retrace` | 167v | seg-b3-c5p12-affetti-persi |  | #ink_1 | medium | a |
| 198 | `retrace` | 169r | seg-b3-c6p8-innocenza-guardia |  | #ink_1 |  | b |
| 199 | `retrace` | 170v | seg-b3-c6p17-fede-prattica-guardia |  | #ink_1 |  | l |
| 200 | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | n |
| 201 | `retrace` | 170v | seg-b3-c6p20-consumazione-dolce |  | #ink_1 |  | t |
| 202 | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | p |
| 203 | `retrace` | 170v | seg-b3-c6p21-braggia-similitudine |  | #ink_1 |  | g |
| 204 | `retrace` | 170v | seg-b3-c6p22-fiamma-estasi |  | #ink_1 |  | m |
| 205 | `retrace` | 172v | seg-b3-c6p33-puo-cadere-guardia |  | #ink_1 |  | in |
| 206 | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 207 | `retrace` | 174r | seg-b3-c7p15-similitudine-omicida |  | #ink_1 |  | n |
| 208 | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | c |
| 209 | `retrace` | 175v | seg-b3-c8p1-secretum |  | #ink_1 | medium | m |
| 210 | `retrace` | 176r | seg-b3-c8p3-morte-vitanuova |  | #ink_1 | medium | m |
| 211 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | r |
| 212 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | m |
| 213 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | t |
| 214 | `retrace` | 176r | seg-b3-c8p4-riequilibrio-vita |  | #ink_1 | medium | n |
| 215 | `retrace` | 176r | seg-b3-c8p6-sensi-sposalitio |  | #ink_1 | medium | nn |
| 216 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | c |
| 217 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 218 | `retrace` | 176v | seg-b3-c8p7-navicella |  | #ink_1 | medium | n |
| 219 | `retrace` | 177r | seg-b3-c8p15-lambino |  | #ink_1 | medium | lambino |
| 220 | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | tinuo |
| 221 | `retrace` | 177v | seg-b3-c8p19-contatto-gloria |  | #ink_1 | medium | co |
| 222 | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | ricittavolo |
| 223 | `retrace` | 177v | seg-b3-c8p20-cella-chiarezza |  | #ink_1 | medium | co |
| 224 | `retrace` | 178r | seg-b3-c8p21-esorto-hore |  | #ink_1 | medium | scu |
| 225 | `retrace` | 197v | seg-b3-c16p6-carne-con-carne |  | #ink_1 |  | c |
| 226 | `retrace` | 198v | seg-b3-c16p15-molte-strade |  | #ink_1 |  | r |
| 227 | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | m |
| 228 | `retrace` | 199v | seg-b3-c16p21-mutazione-desiderio |  | #ink_1 |  | t |
| 229 | `retrace` | 200v | seg-b3-c16p26-festa-sensi |  | #ink_1 |  | e |
| 230 | `retrace` | 202r | seg-b3-c16p37-certezza-niente |  | #ink_1 |  | e |
| 231 | `retrace` | 219v | seg-b3-c24p2-timore-naturale |  | #ink_1 |  | d |
| 232 | `retrace` | 220v | seg-b3-c24p13-fiducia-abbandono |  | #ink_1 |  | men |
| 233 | `gap` | 3v | seg-b1-c2p14-claustrati-secolari | cancelled |  |  |  |
| 234 | `gap` | 6r | seg-b1-c4p4-adoperarsi-notte | illegible |  |  |  |
| 235 | `gap` | 10v | seg-b1-c5p11-fondamento-castello | illegible |  |  |  |
| 236 | `gap` | 11r | seg-b1-c5p16-non-dar-parere | illegible |  |  |  |
| 237 | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 238 | `gap` | 12r | seg-b1-c5p31-parola-ingioriosa | illegible |  |  |  |
| 239 | `gap` | 12r | seg-b1-c5p33-finta-humilta | illegible |  |  |  |
| 240 | `gap` | 12v | seg-b1-c5p38-humilta-vera-quiete | illegible |  |  |  |
| 241 | `gap` | 12v | seg-b1-c5p41-rimedi-padre | illegible |  |  |  |
| 242 | `gap` | 13v | seg-b1-c5p61-comperatione-fine | illegible |  |  |  |
| 243 | `gap` | 14r | seg-b1-c6p4-desiderio-sudita | illegible |  |  |  |
| 244 | `gap` | 23r | seg-b1-c11p58-carita-cura | hole |  |  |  |
| 245 | `gap` | 159r | seg-b3-c1p10-unione-velata | illegible |  |  |  |
| 246 | `gap` | 159r | - | hole |  |  |  |
| 247 | `gap` | 159v | seg-b3-c2p3-comparatione-teresa | illegible |  |  |  |
| 248 | `gap` | 160r | seg-b3-c2p6-differenza-raccoglimento | illegible |  |  |  |
| 249 | `gap` | 161r | seg-b3-c2p13-castellano-secreto | illegible |  |  |  |
| 250 | `gap` | 161r | seg-b3-c2p15-comunicazione-diretta | illegible |  |  |  |
| 251 | `gap` | 162v | seg-b3-c3p1-santamadre | hole |  |  |  |
| 252 | `gap` | 163r | seg-b3-c3p5-propriastima | hole |  |  |  |
| 253 | `gap` | 163v | seg-b3-c3p7-statuette | hole |  |  |  |
| 254 | `gap` | 163v | seg-b3-c3p7-magnificar | hole |  |  |  |
| 255 | `gap` | 164r | seg-b3-c3p12-linguaggio | illegible |  |  |  |
| 256 | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 257 | `gap` | 164v | seg-b3-c3p14-mirabilia | hole |  |  |  |
| 258 | `gap` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  |  |  |
| 259 | `gap` | 168r | seg-b3-c6p3-morire-spogliarsi | illegible |  |  |  |
| 260 | `gap` | 168r | seg-b3-c6p4-fomite-peccato | hole |  |  |  |
| 261 | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 262 | `gap` | 169r | seg-b3-c6p8-innocenza-guardia | illegible |  |  |  |
| 263 | `gap` | 169r | seg-b3-c6p8b-mondo-beati | illegible |  |  |  |
| 264 | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 265 | `gap` | 169r | seg-b3-c6p9-discernimento-guardia | illegible |  |  |  |
| 266 | `gap` | 170r | seg-b3-c6p15-adamo-guardia | hole |  |  |  |
| 267 | `gap` | 170r | seg-b3-c6p15-adamo-guardia | illegible |  |  |  |
| 268 | `gap` | 170v | seg-b3-c6p17-fede-prattica-guardia | illegible |  |  |  |
| 269 | `gap` | 170v | seg-b3-c6p21-braggia-similitudine | illegible |  |  |  |
| 270 | `gap` | 171v | seg-b3-c6p26-esposti-guardia | illegible |  |  |  |
| 271 | `gap` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  |  |  |
| 272 | `gap` | 178r | seg-b3-c8p21-esorto-hore | illegible |  |  |  |
| 273 | `gap` | 179r | seg-b3-c8p25-estremi-sole | illegible |  |  |  |
| 274 | `gap` | 179r | seg-b3-c8p25-propria-stima | illegible |  |  |  |
| 275 | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 276 | `gap` | 182v | seg-b3-c10p7-precisazione-perseveranza | illegible |  |  |  |
| 277 | `gap` | 183r | seg-b3-c10p8-riequilibrio-fatica | illegible |  |  |  |
| 278 | `gap` | 193r | seg-b3-c12p4-addormentarsi-amato | illegible |  |  |  |
| 279 | `gap` | 195v | seg-b3-c14p6-ombra-certezza | illegible |  |  |  |
| 280 | `gap` | 198v | seg-b3-c16p13-esperienza-propria | hole |  |  |  |
| 281 | `gap` | 201r | seg-b3-c16p28-niente-trasformatione | illegible |  |  |  |
| 282 | `gap` | 202r | seg-b3-c16p37-certezza-niente | illegible |  |  |  |
| 283 | `gap` | 202v | seg-b3-c16p39-capi-eresia | illegible |  |  |  |
| 284 | `gap` | 221r | seg-b3-c24p16-glossa-humanita | hole |  |  |  |
| 285 | `gap` | 246v | seg-b3-c34p3-identita-distinte | hole |  |  |  |
| 286 | `gap` | 248v | seg-b3-c34p17-olimpo-altezza | illegible |  |  |  |
| 287 | `gap` | 257v | seg-b3-c38p9-brama-padre-preghiera | illegible |  |  |  |
| 288 | `gap` | 258v | seg-b3-c38p18-fede-oscurata | illegible |  |  |  |
| 289 | `gap` | 261r | seg-b3-c39p16-annichilazione-insensibile | hole |  |  |  |
| 290 | `gap` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  |  |  |
| 291 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 292 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 293 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 294 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 295 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 296 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 297 | `gap` | 262v | seg-b3-c40p3-sonno-corpo | hole |  |  |  |
| 298 | `unclear` | 168r | seg-b3-c6p4-fomite-peccato | illegible |  |  | st |
| 299 | `unclear` | 172v | seg-b3-c6p33-puo-cadere-guardia | illegible |  |  | ch |
| 300 | `unclear` | 174r | seg-b3-c7p14-precisazione-impossibilita-peccato | illegible |  |  | P |
| 301 | `unclear` | 174v | seg-b3-c7p17-glossa-fortezza-timore | illegible |  |  | lacciuto |
| 302 | `unclear` | 219r | - | stain |  |  | emita |
| 303 | `unclear` | 258v | seg-b3-c38p19-perdita-fede | stain |  |  | no |
| 304 | `supplied` | 3r | seg-b1-c2p6-nemico-demonio | hole |  | high | r |
| 305 | `supplied` | 3r | seg-b1-c2p7-tre-nemici | hole |  | high | n |
| 306 | `supplied` | 3v | seg-b1-c2p8-citta-assediata | hole |  | high | ste |
| 307 | `supplied` | 6v | seg-b1-c4p15-notte-necessaria | hole |  | high | ra |
| 308 | `supplied` | 7v | seg-b1-c4p26-prima-purga-dura | hole |  | high | p |
| 309 | `supplied` | 8r | seg-b1-c4p32-merito-bandiera | hole |  | high | p |
| 310 | `supplied` | 9r | seg-b1-c4p47-san-paolo-vocatione | hole |  | high | co |
| 311 | `supplied` | 9v | seg-b1-c4p55-temer-occasione | hole |  | high | ch |
| 312 | `supplied` | 10r | seg-b1-c5p1-metafora-fondamento | hole |  | high | lo |
| 313 | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | u |
| 314 | `supplied` | 10r | seg-b1-c5p3-cristo-peccatori | hole |  | high | m |
| 315 | `supplied` | 10v | seg-b1-c5p3-cristo-peccatori | hole |  | medium | i |
| 316 | `supplied` | 10v | seg-b1-c5p11-fondamento-castello | hole |  | high | nto |
| 317 | `supplied` | 10v | seg-b1-c5p13-esterno-interno | hole |  | high | qu |
| 318 | `supplied` | 11r | seg-b1-c5p19-mortificar-passioni | hole |  | high | re |
| 319 | `supplied` | 11r | seg-b1-c5p20-anime-principianti | hole |  | high | o f |
| 320 | `supplied` | 11v | seg-b1-c5p26-rammarico-quiete | hole |  | high | l |
| 321 | `supplied` | 11v | seg-b1-c5p28-distacco-spirito | hole |  | high | i |
| 322 | `supplied` | 12r | seg-b1-c5p28-distacco-spirito | omitted |  | high | ma |
| 323 | `supplied` | 12r | seg-b1-c5p33-finta-humilta | hole |  | high | bil |
| 324 | `supplied` | 12v | seg-b1-c5p41-rimedi-padre | hole |  | high | op |
| 325 | `supplied` | 13r | seg-b1-c5p49-humilta-contrario | hole |  | high | m |
| 326 | `supplied` | 13r | seg-b1-c5p51-voltare-mondo | hole |  | high | a |
| 327 | `supplied` | 13v | seg-b1-c5p51-voltare-mondo | hole |  | high | à l' |
| 328 | `supplied` | 14r | seg-b1-c6p5-obedienza-penitenza | hole |  | high | l |
| 329 | `supplied` | 14r | seg-b1-c6p8-vite-santi | hole |  | high | d |
| 330 | `supplied` | 14v | seg-b1-c6p16-approfittate-intelletto | hole |  | high | i |
| 331 | `supplied` | 15r | seg-b1-c6p18-conclusione | omitted |  | high | t |
| 332 | `supplied` | 20r | seg-b1-c11p3-fatiche-niente | hole |  | high | qui |
| 333 | `supplied` | 20v | seg-b1-c11p13-mondo-schernisce | hole |  | high | lto |
| 334 | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | m |
| 335 | `supplied` | 20v | seg-b1-c11p15-parole-aspre | hole |  | high | l |
| 336 | `supplied` | 21r | seg-b1-c11p23-ripugnanza-merito | hole |  | high | li d |
| 337 | `supplied` | 21v | seg-b1-c11p23-ripugnanza-merito | hole |  | high | l |
| 338 | `supplied` | 21v | seg-b1-c11p30-obedienza-toglie | hole |  | high | gli |
| 339 | `supplied` | 22r | seg-b1-c11p42-frutti-fanciulli | hole |  | high | al |
| 340 | `supplied` | 22v | seg-b1-c11p50-contadino-diligente | hole |  | high | r |
| 341 | `supplied` | 23r | seg-b1-c11p56-principianti-forze | hole |  | high | co |
| 342 | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | medium | l |
| 343 | `supplied` | 23r | seg-b1-c11p58-carita-cura | hole |  | high | tra |
| 344 | `supplied` | 23v | seg-b1-c11p64-cieca-obedienza | hole |  | high | e |
| 345 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | p |
| 346 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | i e |
| 347 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | a co |
| 348 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | d h |
| 349 | `supplied` | 23v | seg-b1-c11p66-fidare-al-padre | hole |  | high | e |
| 350 | `supplied` | 159r | - | hole |  | medium | e |
| 351 | `supplied` | 160r | seg-b3-c2p5-sposo-quiete | hole |  | medium | e |
| 352 | `supplied` | 160v | seg-b3-c2p12-castello-fondo | hole |  | medium | u |
| 353 | `supplied` | 161r | seg-b3-c2p13-castellano-secreto | hole |  | medium | e |
| 354 | `supplied` | 161v | seg-b3-c2p18-pace-continua | hole |  | medium | io |
| 355 | `supplied` | 162r | seg-b3-c2p20-autonomia-direttore | hole |  | medium | a |
| 356 | `supplied` | 162v | seg-b3-c3p1-santamadre | hole |  | medium | i |
| 357 | `supplied` | 163r | seg-b3-c3p5-propriastima | hole |  | medium | nt |
| 358 | `supplied` | 163v | seg-b3-c3p7-statuette | hole |  | medium | a |
| 359 | `supplied` | 163v | seg-b3-c3p7-magnificar | hole |  | medium | i |
| 360 | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | modo |
| 361 | `supplied` | 164v | seg-b3-c3p14-mirabilia | hole |  | medium | arse |
| 362 | `supplied` | 165r | seg-b3-c4p8-conclusio | hole |  | medium | à |
| 363 | `supplied` | 166v | seg-b3-c5p6-non-capace-pena | hole |  | medium | e |
| 364 | `supplied` | 167r | seg-b3-c5p7-amore-prossimo | hole |  | medium | i |
| 365 | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | e |
| 366 | `supplied` | 167r | seg-b3-c5p9-non-desiderar-morte | hole |  | medium | o |
| 367 | `supplied` | 169r | seg-b3-c6p8-innocenza-guardia | hole |  | high | e |
| 368 | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | a |
| 369 | `supplied` | 169r | seg-b3-c6p10-impassibilita-guardia | hole |  | high | n |
| 370 | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | à |
| 371 | `supplied` | 170r | seg-b3-c6p15-adamo-guardia | hole |  | high | a |
| 372 | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | stain |  | medium | n |
| 373 | `supplied` | 170v | seg-b3-c6p19-amor-sensibile-antitesi | hole |  | medium | ano |
| 374 | `supplied` | 173v | seg-b3-c7p7-glossa-impeccabilita-consenso | hole |  | medium | s |
| 375 | `supplied` | 174v | seg-b3-c7p17-glossa-fortezza-timore | hole |  | low | deve temere |
| 376 | `supplied` | 175v | seg-b3-c8p2-roma | hole |  | medium | v |
| 377 | `supplied` | 177r | seg-b3-c8p15-lambino | hole |  | medium | a |
| 378 | `supplied` | 177v | seg-b3-c8p18-bocca-sostanza | hole |  | medium | a |
| 379 | `supplied` | 179r | seg-b3-c8p27-continua-oratione | hole |  | medium | oratione |
| 380 | `supplied` | 197r | seg-b3-c16p3-distinzione-unione | hole |  | medium | c |
| 381 | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | ret |
| 382 | `supplied` | 200r | seg-b3-c16p25-allegoria-re | hole |  | medium | n |
| 383 | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | a |
| 384 | `supplied` | 201r | seg-b3-c16p31-impossibile-cadere | hole |  | medium | P |
| 385 | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | e |
| 386 | `supplied` | 207r | seg-b3-c19p3-precisazione-gratia | hole |  | medium | Anch |
| 387 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ra |
| 388 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | e |
| 389 | `supplied` | 207v | seg-b3-c19p6-definizione-volonta | hole |  | medium | ass |
| 390 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | g |
| 391 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | c |
| 392 | `supplied` | 208r | seg-b3-c19p8-precisazione-contemplatione-infusa | hole |  | medium | re |
| 393 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | sa |
| 394 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | rl |
| 395 | `supplied` | 209r | seg-b3-c19p16-precisazione-sposalitio-sostanza | hole |  | medium | iù |
| 396 | `supplied` | 209v | seg-b3-c19p22-partecipazione-corpo | hole |  | medium | me |
| 397 | `supplied` | 219r | - | hole |  | medium | enta |
| 398 | `supplied` | 220v | seg-b3-c24p10-distinzione-interni | hole |  | medium | cu |
| 399 | `supplied` | 220v | seg-b3-c24p12-abbandono-padre | hole |  | medium | n |
| 400 | `supplied` | 220v | seg-b3-c24p14-critica-padri | hole |  | medium | c |
| 401 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | esse |
| 402 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | nza |
| 403 | `supplied` | 221r | seg-b3-c24p16-glossa-humanita | hole |  | medium | star |
| 404 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | medium | o pare |
| 405 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | e |
| 406 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 407 | `supplied` | 242r | seg-b3-c32p2-incomincio | hole |  | high | r |
| 408 | `supplied` | 242r | seg-b3-c32p2-incognito-ineffabile | hole |  | high | a |
| 409 | `supplied` | 242v | seg-b3-c32p2-incognito-ineffabile | hole |  | high | v |
| 410 | `supplied` | 242v | seg-b3-c32p3-trasformazione-crocifisso | hole |  | high | l |
| 411 | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | in |
| 412 | `supplied` | 242v | seg-b3-c32p5-notte-luce | hole |  | high | è |
| 413 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | croci |
| 414 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | sì co |
| 415 | `supplied` | 246r | seg-b3-c34p1-distinzione-crocifisso | hole |  | high | li |
| 416 | `supplied` | 246v | seg-b3-c34p3-identita-distinte | hole |  | high | ù |
| 417 | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | ivon |
| 418 | `supplied` | 247r | seg-b3-c34p7-effetti-taciuti | hole |  | high | no |
| 419 | `supplied` | 248r | seg-b3-c34p13-tentatione-agostino | hole |  | high | i |
| 420 | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | hole |  | high | ne |
| 421 | `supplied` | 248v | seg-b3-c34p18-silentio-comparazione | stain |  | medium | e |
| 422 | `supplied` | 256v | seg-b3-c38p4-aridita-continua | hole |  | high | vo |
| 423 | `supplied` | 257r | seg-b3-c38p8-discernimento-brama | hole |  | high | ti |
| 424 | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | i |
| 425 | `supplied` | 257v | seg-b3-c38p10-tantalo | hole |  | high | dre |
| 426 | `supplied` | 257v | seg-b3-c38p11-benevolenza-honore | hole |  | high | he |
| 427 | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | ar |
| 428 | `supplied` | 257v | seg-b3-c38p13-persecutione-terzapersona | hole |  | high | re |
| 429 | `supplied` | 259r | seg-b3-c39p4-deificatione-imagine | hole |  | high | ic |
| 430 | `supplied` | 259v | seg-b3-c39p5-precisazione-matrimonio | hole |  | medium | perita |
| 431 | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | tro si |
| 432 | `supplied` | 260r | seg-b3-c39p12b-veemenza | hole |  | medium | dal |
| 433 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | stain |  | medium | re |
| 434 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d |
| 435 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d in |
| 436 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | d a |
| 437 | `supplied` | 260v | seg-b3-c39p13-silentio-annientamento | hole |  | high | in |
| 438 | `supplied` | 261r | seg-b3-c39p13-silentio-annientamento | hole |  | high | nel |
| 439 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | rtù |
| 440 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | st' |
| 441 | `supplied` | 261v | seg-b3-c39p19-ricchezza-virtu | hole |  | high | é |
| 442 | `supplied` | 262r | seg-b3-c39p20-salamandra | hole |  | medium | tan |
| 443 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | p |
| 444 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ti |
| 445 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | pro |
| 446 | `supplied` | 262r | seg-b3-c40p2-cella-intima | hole |  | medium | ità |
| 447 | `supplied` | 262v | seg-b3-c40p2-cella-intima | hole |  | medium | t |
| 448 | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ugiato |
| 449 | `supplied` | 262v | seg-b3-c40p3-sonno-corpo | hole |  | medium | ett |
| 450 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 451 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | s |
| 452 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | a |
| 453 | `supplied` | 262v | seg-b3-c40p5-morte-apparente | hole |  | medium | ho |
