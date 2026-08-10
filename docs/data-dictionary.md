# Assi e categorie della tassonomia: dizionario dei dati
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)
**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

**Fonte**
*Generato da `tei/taxonomy/tassonomia-gh.xml`. Mappa ogni asse ai suoi `xml:id` e alla forma con cui compaiono in `@ana` nel testo.*
**Convenzione `@ana`:** token separati da spazio, con `#`. L'asse **`func`** compare **senza** prefisso d'asse (es. `#legittimazione-tradizione`); **tutti gli altri assi** col prefisso `#{asse}-…` (es. `#impact-low`, `#mystic_state-unione`).

---

## `func` — Funzioni retoriche

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `legittimazione` | `#legittimazione` | Procedure retoriche che consolidano l’ortodossia del discorso mistico mediante appoggi biblici, l… |
| `legittimazione-biblica` | `#legittimazione-biblica` | Citazioni e parafrasi scritturali, spesso in latino, impiegate per rendere accettabili concetti c… |
| `legittimazione-liturgica` | `#legittimazione-liturgica` | Ricorso a formule, stilemi e registri liturgici come garanzia devozionale e dottrinale, utile a c… |
| `legittimazione-tradizione` | `#legittimazione-tradizione` | Appello a maestri della mistica esplicitamente richiamati in prima persona dall’autrice ("la mia … |
| `pedagogia` | `#pedagogia` | Strategie formative rivolte ad anime "incipienti", "proficienti" e "perfette", basate su distinzi… |
| `pedagogia-introduzione` | `#pedagogia-introduzione` | Sezioni introduttive e inquadramenti che predispongono il lettore all’orazione mentale e alla cos… |
| `pedagogia-discernimento` | `#pedagogia-discernimento` | Distinzioni tra (1) "meditazione", (2) "contemplazione acquisita", (3) "contemplazione infusa", (… |
| `pedagogia-esemplificazione` | `#pedagogia-esemplificazione` | Uso di immagini quotidiane (acqua, mare, torrente, giardino, specchio) e comparazioni che rendono… |
| `rischio` | `#rischio` | Insieme di strategie volte a prevenire o correggere letture potenzialmente eterodosse, specialmen… |
| `rischio-attenuatio` | `#rischio-attenuatio` | Glosse esplicative aggiunte per smorzare formulazioni rischiose, spesso tramite “cioè”, “intendo … |
| `rischio-precisatio` | `#rischio-precisatio` | Limitazioni semantiche che delimitano concetti radicali (come “divenir un altro Dio”, “sicurtà to… |
| `rischio-declaratio` | `#rischio-declaratio` | Dichiarazioni esplicite di adesione alla Chiesa e di rifiuto della “molinia” (Molinos), formulate… |
| `ethos` | `#ethos` | Costruzione dell’immagine autoriale come donna ignorante, obbediente e priva di lettere, che scri… |
| `ethos-umilta` | `#ethos-umilta` | Professioni di "indegnità" e "ignoranza" per minimizzare la propria autorità; l’autrice usa quest… |
| `ethos-esperienza` | `#ethos-esperienza` | Rivendicazione dell’esperienza (“non parlo senza l’esperienza”) come fondamento epistemico che le… |
| `ethos-obbedienza` | `#ethos-obbedienza` | Insistenza sull’obbedienza al confessore (a scopo difensivo), vista come condizione necessaria pe… |

## `impact` — Indice d'impatto (classe discreta)

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `impact-high` | `#impact-high` | Fascia alta dell'indice (0.66 ≤ I < 0.82): forte forza regolativa del marcatore. Passaggi che rid… |
| `impact-medium` | `#impact-medium` | Fascia intermedia dell'indice (0.50 ≤ I < 0.66): forza regolativa moderata. Marcatori che rafforz… |
| `impact-low` | `#impact-low` | Fascia inferiore dell'indice (I < 0.50): minima forza regolativa del marcatore. Parti ornamentali… |
| `impact-critical` | `#impact-critical` | Fascia superiore dell'indice (I ≥ 0.82): massima forza regolativa del marcatore. Nel campione coi… |

## `risk` — Rischio dottrinale

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `risk-dottrinale` | `#risk-dottrinale` | Rischio generale di equivocità su dottrine come "grazia", "libertà", "unione" e "contemplazione",… |
| `risk-quietismo` | `#risk-quietismo` | Possibile lettura quietista dei concetti di “quiete”, “otio”, “non operare”, “abbandono totale”; … |
| `risk-panteismo` | `#risk-panteismo` | Rischio di interpretazione panteistica nelle espressioni sulla “trasformatione” e sul “divenir un… |
| `risk-impeccabilita` | `#risk-impeccabilita` | Ambiguità relative alla “sicurtà” mistica e alla percezione dell’impossibilità di peccare nello s… |
| `risk-ambiguita` | `#risk-ambiguita` | Punti in cui la formulazione è oscura, metaforica o oscillante, generando difficoltà interpretati… |

## `mystic_state` — Stati mistici

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `mystic_state-purificazione` | `#mystic_state-purificazione` | Fase purgativa del cammino mistico: prove, tribolazioni, sofferenze che preparano l’anima alla co… |
| `mystic_state-illuminazione` | `#mystic_state-illuminazione` | Fase illuminativa: elevazione, dolcezza, chiarezza contemplativa che precede l’unione piena. |
| `mystic_state-quiete` | `#mystic_state-quiete` | Stato di sospensione delle potenze, spesso minacciato da interpretazioni quietistiche; descritto … |
| `mystic_state-otium` | `#mystic_state-otium` | Ozio delle potenze inteso non come inerzia quietista, ma come sospensione operata da Dio affinché… |
| `mystic_state-unione` | `#mystic_state-unione` | Stato mistico di massimo avvicinamento a Dio, descritto con lessico alto e analogie complesse; lu… |

## `operation` — Operazioni prudenziali

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `operation-delimitazione` | `#operation-delimitazione` | Operazioni che circoscrivono semanticamente concetti rischiosi, evitando letture estreme e guidan… |
| `operation-attenuatio` | `#operation-attenuatio` | Interventi che smorzano formulazioni troppo ardite mediante spiegazioni aggiunte, spesso negli sp… |
| `operation-precisatio` | `#operation-precisatio` | Chiarimenti puntuali volti a definire meglio concetti ambigui, tipici della riflessione autografa… |
| `operation-declaratio` | `#operation-declaratio` | Dichiarazioni dirette di ortodossia, con cui l’autrice esplicita la propria adesione alla dottrin… |
| `operation-riequilibrio` | `#operation-riequilibrio` | Interventi equilibranti che compensano un’affermazione rischiosa con una precisazione ortodossa p… |

## `exposition` — Livello d'esposizione

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `exposition-low` | `#exposition-low` | Esposizione prudente di temi dottrinali, con ricorso limitato a tecnicismi e metafore. |
| `exposition-medium` | `#exposition-medium` | Esposizione moderata di contenuti mistici, con appoggi occasionali a citazioni e spiegazioni aggi… |
| `exposition-high` | `#exposition-high` | Esposizione intensa di dottrine mistiche complesse che richiedono glosse, precisazioni e cautele … |
| `exposition-critical` | `#exposition-critical` | Livello massimo di esposizione dottrinale, tipico delle sezioni sul matrimonio spirituale, la tra… |

## `phase` — Fase discorsiva

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `phase-introduction` | `#phase-introduction` | Segmenti introduttivi che stabiliscono tono, pubblico e obbedienza iniziale, preparando la progre… |
| `phase-mediana` | `#phase-mediana` | Sezioni centrali in cui si analizzano stati intermedi del cammino contemplativo, con esempi ed es… |
| `phase-conclusive` | `#phase-conclusive` | Chiusure che ricapitolano i contenuti, riordinano la materia e predispongono alla transizione ver… |
| `phase-critical` | `#phase-critical` | Marcatore trasversale, non posizionale: segnala che il segmento è teologicamente delicato indipen… |

## `relation` — Relazioni intertestuali

| `xml:id` | in `@ana` | Descrizione |
|---|---|---|
| `relation-mistica` | `#relation-mistica` | Relazioni che descrivono la progressione fenomenologica tra stati mistici lungo il cammino contem… |
| `relation-mistica-infusa-purificazione` | `#relation-mistica-infusa-purificazione` | Relazione concettuale che descrive il passaggio dalle prove purgative alla contemplazione infusa. |
| `relation-mistica-attiva-meditazione` | `#relation-mistica-attiva-meditazione` | Relazione progressiva dalla meditazione attiva alla maturazione spirituale che prepara alla conte… |
| `relation-mistica-passiva-quiete` | `#relation-mistica-passiva-quiete` | Relazione tra contemplazione passiva e quiete, descritta come sospensione delle potenze per opera… |
| `relation-mistica-unione-sposalitio` | `#relation-mistica-unione-sposalitio` | Sequenza che conduce dall’unione allo sposalizio spirituale e alla trasformazione, secondo i mode… |
| `relation-intertesto` | `#relation-intertesto` | Relazioni con fonti esterne al testo, di diversa natura e provenienza. |
| `relation-intertesto-biblico` | `#relation-intertesto-biblico` | Richiami espliciti o impliciti alla Scrittura che sostengono la dottrina mistica. |
| `relation-intertesto-liturgico` | `#relation-intertesto-liturgico` | Riferimenti a testi, formule o registri liturgici che rinforzano il tono devoto e la legittimità … |
| `relation-intertesto-teresiano` | `#relation-intertesto-teresiano` | Risonanze e riprese del linguaggio e dei temi di Teresa d’Avila e delle tradizioni carmelitane. |
| `relation-intertesto-molinista` | `#relation-intertesto-molinista` | Affinità o divergenze rispetto al linguaggio della Guida di Molinos, spesso tematizzate per prend… |
