# `pilot-loci.tsv` — loci del pilota della pipeline IA controllata (Fase 2)

Documentazione di corredo del file dati [`pilot-loci.tsv`](pilot-loci.tsv), tenuto come **TSV puro**
(sola intestazione + righe, 3 colonne `locus_id · operation · note`) perché resti renderizzabile e
ricercabile su GitHub. Qui la metodologia di selezione, che nel TSV non trova posto.

## Criterio di selezione
Alta esposizione dottrinale **+** centralità nel grafo delle catene semantiche **+** *presidio reale*
coerente con l'operazione (l'operazione dev'essere effettivamente eseguibile su quel locus):

| operazione | presidio richiesto nel `<seg>` |
| :--- | :--- |
| **-CIT** | un `<cit>` di legittimazione da rimuovere |
| **+TEXTsub** | recupero di uno strato genetico autoriale assente dal testo costituito, in **due forme**: **(a)** ripristino di una *cassatura d'autrice* (`<del>` leggibile); **(b)** rimozione di un'*aggiunta a margine/interlinea* (recupero dello stato pre-aggiunta) |
| **+CIT** | un'allusione a una fonte **già documentata** in `docs/anagrafe-citazioni.md` e **usata altrove** nel testo, ma **non esplicitata** a questo nodo |

## Nota su +TEXTsub (loci iniziali scartati)
I 4 loci +TEXTsub inizialmente ipotizzati (`c16p37`, `c5p38`, `c7p24` e la sola *cassatura* di `c6p4`)
sono stati **scartati**: contengono cancellature illeggibili (`<gap>`) o frammenti di poche lettere, senza
lezione sostanziale da ripristinare. La ricognizione dell'intero testo (103 `<del>` leggibili, 72 di 1-2
caratteri) conferma che l'autografo **non attesta auto-censura di passaggi**: le forme +TEXTsub praticabili
sono la (a) su una vera sostituzione di parola e la (b) sulle guardie prudenziali a margine. Censimento
completo delle aggiunte in [`../variants/backlog-textsub-additions.md`](../variants/backlog-textsub-additions.md).

## Nota su +CIT (cluster «un altro Dio»)
Il +CIT opera sul **cluster di deificazione** «l'anima divenuta un altro Dio (per participatione/gratia)».
La fonte è **Gal 2,20** (anagrafe #22), che l'autrice **cita esplicitamente all'àncora `c7p7`**
(*«Nico ego sed non ego, nimis vero in me Christus»*) — e proprio lì il nodo è `#impact-low`
(`#legittimazione-biblica`). Gli **stessi** enunciati di deificazione **senza** la citazione sono invece
`#impact-high/medium #risk-panteismo`. Il +CIT integra quella citazione (forma **1a**, come attestata a
`c7p7`) ai nodi paralleli non citati, per misurare se la legittimazione scritturale **abbassa il rischio
dottrinale**. `c7p7` resta il **controllo** (versione già citata, invariata).

## Composizione del pilota (10 loci)
| operazione | n | loci |
| :--- | :-- | :--- |
| **-CIT** | 2 | `c8p9-luce-tenebre`, `c40p7-declaratio-dossologia` |
| **+TEXTsub** | 4 | `c6p5-obedienza-penitenza` (a); `c6p4-fomite-peccato`, `c21p10-quattro-passioni`, `c24p16-glossa-humanita` (b) |
| **+CIT** | 4 | `c8p24-divenuta-altrodio` (B); `c5p16`, `c7p4`, `c7p10` (C) |

## Riproduzione della misura strutturale (D2)
```
python3 tools/delta_cohesion.py tei/text/castello-anima-teiText.xml --pilot tools/pilot-loci.tsv --tsv > logs/D2-pilot.tsv
```
