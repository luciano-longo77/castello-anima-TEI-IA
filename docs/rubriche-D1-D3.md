# Rubriche D1 (chiarezza) e D3 (stabilità dottrinale)
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

## A cosa servono

Le varianti controfattuali della Fase 2 (`variants/castello-anima-variants.xml`) si misurano su
**tre dimensioni**: **D2** *coesione* (strutturale, deterministica — già in `logs/D2-pilot.tsv`), **D1**
*chiarezza argomentativa* e **D3** *stabilità dottrinale percepita*. D1 e D3 sono **interpretative**:
richiedono un giudizio. Perché quel giudizio sia **verificabile e riproducibile** — non un'impressione —
serve una **rubrica ancorata**, esattamente come le ancore N/A dell'indice d'impatto.

Ogni rubrica si applica a **entrambe** le letture del locus: il `<lem>` (**testo costituito**) e il
`<rdg>` (**controfattuale**). Il risultato d'interesse è il **Δ** = punteggio(rdg) − punteggio(lem):
*di quanto* la perturbazione sposta chiarezza e stabilità.

## Procedura (expert-in-the-loop)

L'**IA propone** un punteggio con una **motivazione** di una riga; l'**editore assegna** il punteggio
definitivo (è l'autorità sul giudizio interpretativo, come sul re-banding di ΔI). Se il punteggio
dell'editore diverge da quello proposto, si registrano **entrambi** (colonna `note`): la divergenza è un
dato, non un errore. Nessun punteggio è "automatico".

## D1 — Chiarezza argomentativa

*Quanto l'argomento del passo è esplicito, coeso e comprensibile in sé* (indipendentemente dalla sua
ortodossia). Scala a quattro bande ancorate:

| banda | valore | ancora |
| :--- | :--: | :--- |
| **alta** | 0.90 | argomento pienamente esplicito e autosufficiente; nessuna ambiguità, nessun implicito da ricostruire |
| **media** | 0.65 | comprensibile, ma con un passaggio implicito o un riferimento da inferire |
| **bassa** | 0.40 | ellittico od oscuro; richiede ricostruzione; ambiguità sostanziale sul senso |
| **nulla** | 0.15 | incomprensibile, tautologico o **vuoto** (es. un `<seg>` svuotato dalla rimozione di una glossa che ne era l'intero contenuto) |

## D3 — Stabilità dottrinale percepita

*Quanto la lettura suona ortodossa e "sorvegliata"* — cioè l'**assenza di rischio dottrinale percepito**,
data la presenza o meno di guardie, precisazioni e legittimazioni. Scala a quattro bande ancorate:

| banda | valore | ancora |
| :--- | :--: | :--- |
| **alta** | 0.90 | pienamente ortodosso; guardie/legittimazioni presenti ed esplicite; nessun rischio percepito |
| **media** | 0.65 | affermazione potenzialmente rischiosa ma **temperata** (precisazione, attenuazione o contesto che la contiene) |
| **bassa** | 0.40 | affermazione rischiosa **esposta**, con guardia debole o soltanto implicita |
| **critica** | 0.15 | lettura che suona **eterodossa e non sorvegliata**: panteismo, impeccabilità o quietismo enunciati senza alcun freno |

> **D3 ≠ indice d'impatto.** L'`#impact-*` (e la sua N) qualifica il **segmento nel testo costituito**;
> D3 qualifica la **singola lettura** (lem *oppure* rdg). Una perturbazione può lasciare invariato l'impatto
> del segmento e però far crollare la stabilità della *lettura* controfattuale: è proprio ciò che D3 cattura.

## Come si legge il Δ (ipotesi per operazione)

Il segno atteso del Δ orienta la lettura (e un Δ di segno opposto è un risultato notevole, da discutere):

| operazione | effetto atteso | ΔD3 | ΔD1 |
| :--- | :--- | :--: | :--: |
| **-CIT** | toglie una legittimazione | **< 0** (meno stabile) | ≈ 0 / lieve + |
| **+TEXTsub** (b, rimozione guardia) | toglie una precisazione prudenziale | **≪ 0** (crollo) | ≈ 0 |
| **+TEXTsub** (a, ripristino cassatura) | reintroduce la lezione anteriore | dipende dal caso | dipende |
| **+CIT** | **aggiunge** una legittimazione scritturale | **> 0** (più stabile) | ≈ 0 / lieve + |

Il caso **+CIT** è l'unico *additivo*: ci si attende che alzi D3 (è la dimostrazione «cita → abbassa il
rischio», con l'àncora `c7p7` come controllo già citato e a basso rischio).

## Registrazione (`logs/D1-D3.tsv`)

Una riga per variante, schema:

| campo | significato |
| :--- | :--- |
| `locus_id` · `operation` | il locus e l'operazione |
| `D1_lem` · `D1_rdg` · `dD1` | chiarezza del costituito, del controfattuale, e la differenza |
| `D3_lem` · `D3_rdg` · `dD3` | stabilità del costituito, del controfattuale, e la differenza |
| `rater` | chi assegna il punteggio definitivo (`#editor`) |
| `note` | motivazione; ed eventuale punteggio IA proposto se diverge |

Insieme a **ΔI** (indice) e **Δcoesione** (D2), le quattro misure confluiscono nella tabella aggregata
del §3.4 (T10).
