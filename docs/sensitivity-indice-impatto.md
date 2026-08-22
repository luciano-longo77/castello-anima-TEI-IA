# Analisi di sensibilità dell'indice d'impatto
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*
[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA) [![Vocabolario SKOS](https://img.shields.io/badge/SKOS-vocabolario%20online-1b7f5c)](https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/site/)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

**Script:** [`tools/sensitivity.py`](../tools/sensitivity.py) · **Dato:** `tei/text/castello-anima-teiText.xml` (944 `<seg>` = 944 `<fs>`). Solo lettura, riproducibile.

## A cosa serve

L'indice `I = (4·Fnorm + 2·N + A) / 7` e la sua classificazione in bande (`#impact-low/medium/high/critical`) poggiano su parametri **scelti a tavolino**: i pesi AHP `F:N:A = 4:2:1`, i valori-ancora (N 0.90/0.75/0.55/0.30 · A 0.85/0.675/0.40) e le soglie (0.50 / 0.66 / 0.82). La domanda legittima di un revisore è: *le conclusioni interpretative dipendono da queste scelte, o sono robuste?* Questa analisi lo misura: perturba ogni gruppo di parametri e conta quanti dei 944 seg **cambiano banda** rispetto al baseline.

## Metodo

Per ogni scenario lo script ricalcola `I` da `N_band`, `A_band`, `F` (le bande scelte dall'annotatore, non il decimale memorizzato), riassegna la classe e confronta col baseline. Tre famiglie di perturbazioni:
- **pesi** F:N:A alternativi (3:2:1, 5:2:1, 4:3:1, 4:1:1, 4:2:2, 1:1:1, 3:2:2);
- **ancore** N e A con shift globale ±0.05 e ±0.10;
- **soglie** di classe con shift globale ±0.02 e ±0.03.

## Risultati

Baseline: **720 low · 93 medium · 115 high · 16 critical**.

| perturbazione | seg che cambiano banda |
|---|---|
| pesi 3:2:1 / 3:2:2 | 0 (0.0%) |
| pesi 4:3:1 | 1 (0.1%) |
| pesi 4:2:2 | 6 (0.6%) |
| pesi 5:2:1 | 8 (0.8%) |
| pesi 1:1:1 (equipeso) | 9 (1.0%) |
| pesi 4:1:1 | 10 (1.1%) |
| ancore ±0.05 | 1–8 (≤0.8%) |
| soglie ±0.02 | 1–8 (≤0.8%) |
| **ancore ±0.10** (perturbazione grande) | 105 (11.1%) |
| **soglie −0.03** (perturbazione grande) | 82 (8.7%) |

**Massimo su tutti gli scenari: 11.1%.**

### Seg «di frontiera»
Solo **9 seg** hanno `I` entro 0.02 da una soglia — sono gli unici realmente esposti a un cambio: `I=0.501` (×2), `I=0.505` (×6) al confine **low↔medium**, e `I=0.652` (×1) al confine **medium↔high**. Tutti in Libro III; tutti al confine tra fasce **basse** (narrativo ↔ guardia lieve). Elenco completo nell'output dello script.

### Movimento delle bande alte (high/critical) per scenario
Le guardie forti restano ferme **in 13 scenari su 15**. Le toccano solo le due perturbazioni *estreme*:

| scenario | seg che cambiano banda | di cui high/critical | transizione |
|---|---|---|---|
| **pesi 1:1:1** (equipeso) | 9 | **3** | `critical → high` |
| **ancore −0.10** | 105 | **97** | `high → medium` |
| *(gli altri 13 scenari)* | 0–105 | **0** | — |

In **nessuno** scenario un seg `high`/`critical` scende a `low`: le uniche transizioni possibili sono `critical→high` e `high→medium` (attenuazione di **una sola banda**).

## Lettura

1. **Robustezza alta.** Sotto perturbazioni *ragionevoli* (qualunque schema di pesi sensato; ancore ±0.05; soglie ±0.02) **≤1.1% dei seg cambia banda**. Le tarature non sono arbitrarie nei loro effetti: l'ordinamento è stabile.
2. **Le guardie forti reggono, e non si spengono mai.** Nessun seg `high` o `critical` è **di frontiera** (nessuno entro 0.02 da una soglia), e sotto ogni perturbazione *ragionevole* (qualsiasi schema di pesi tranne l'equipeso totale; ancore ±0.05; soglie ±0.02) **nessuna guardia forte cambia banda**. Solo due perturbazioni *estreme* le toccano: l'equipeso `1:1:1`, che azzera il primato di `F` (**3 `critical` → `high`**, i seg `F=3 declaratio`), e il collasso di **tutte** le ancore di −0.10 (**97 `high` → `medium`**). Ma in nessuno scenario — nemmeno estremo — un seg `high`/`critical` scende a `low`: la sorveglianza dove conta, sotto un rimodellamento sostanziale, **si attenua al massimo di una banda, non si spegne**.
3. **La (lieve) sensibilità è al confine low↔medium.** Gli unici spostamenti *di frontiera* riguardano seg *narrativi/di guardia lieve* attorno a `I≈0.50` — la distinzione meno consequente del modello.
4. **Perturbazioni grandi = grandi.** Uno shift di ±0.10 su *tutte* le ancore (10 punti) o −0.03 su *tutte* le soglie è un cambio di modello sostanziale; che perfino così solo ~1 seg su 9 cambi banda — e che le guardie forti al più scendano di una banda, mai a `low` — conferma la tenuta.

**Conclusione:** l'indice d'impatto è **parametricamente robusto**; le conclusioni interpretative non dipendono dalla taratura *fine*. Le guardie forti (`high`/`critical`) sono **invariate sotto ogni perturbazione ragionevole** e **non collassano mai a `low`**: solo un rimodellamento *estremo* (equipeso totale, oppure ancore −0.10) le attenua di una banda. I 9 seg di frontiera sono i soli candidati a una verifica umana mirata.

## Riproduzione

```
python3 tools/sensitivity.py tei/text/castello-anima-teiText.xml
```
