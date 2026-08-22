# Documentazione del progetto — guida di navigazione
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0

---

## Cos'è questa cartella

`docs/` raccoglie la **documentazione metodologica ed editoriale** dell'edizione: i criteri di trascrizione, il modello dell'indice d'impatto, il protocollo della codifica assistita da AI, il dizionario delle categorie, l'anagrafe delle citazioni, la base-dati del campione e i rendiconti verificabili. Il **testo** e la sua annotazione stanno in [`../tei/text/`](../tei/text/); i **metadati** (mani, testimoni, tassonomia, criteri) nel [`teiHeader`](../tei/header/); gli **schemi e le guardie** in [`../schema/`](../schema/) e [`../.github/workflows/`](../.github/workflows/).

Il modello è **interpretativo**: normalizzazione grafica **silenziosa e dichiarata**, apparato **solo sostanziale** (`app`/`lem`/`rdg`), **zero `choice`**; naming dei segmenti `seg-b<L>-cNpP-label`. Coerenza garantita in CI da **8 guardie** + RelaxNG + Schematron. L'annotazione interpretativa vive in quattro strati `<standOff>` — indice d'impatto, figure retoriche, aree semantiche e **catene semantiche** (`<link>`/`<linkGrp>`): le catene coprono **tutti e tre i libri** (199 `<linkGrp>`: Libro I 40, Libro II 46, Libro III 113).

---

## 1. Navigazione per obiettivo

| Se vuoi… | Vai a |
|---|---|
| capire **come si trascrive** (cosa si normalizza in silenzio, cosa resta) | [`criteri-trascrizione.md`](criteri-trascrizione.md) |
| capire **come si codifica** il `<text>` (segmentazione, `@ana`, apparato, standOff) | [`teiText-guida-codifica.md`](teiText-guida-codifica.md) |
| capire **cosa significa** una categoria `@ana` (gli 8 assi e i loro `xml:id`) | [`data-dictionary.md`](data-dictionary.md) *(derivato)* |
| capire **come si calcola** l'indice d'impatto (formula, bande, ancore) | [`indice-impatto.md`](indice-impatto.md) → [`Protocollo-indice-impatto.md`](Protocollo-indice-impatto.md) |
| sapere **come lavora l'AI** nella codifica (ruolo, guardie, verifica umana) | [`protocollo-IA-codifica.md`](protocollo-IA-codifica.md) |
| vedere **quali citazioni** ci sono e in quali carte | [`anagrafe-citazioni.md`](anagrafe-citazioni.md) |
| capire **cos'è il campione** e come è stato selezionato | [`base-dati_campionamento.md`](base-dati_campionamento.md) |
| vedere **ogni intervento editoriale marcato** (apparato, integrazioni) | [`interventi-editoriali.md`](interventi-editoriali.md) *(derivato)* |

---

## 2. Tutti i file, in breve

| File | Cosa contiene | Origine |
|---|---|---|
| [`criteri-trascrizione.md`](criteri-trascrizione.md) | Criteri di trascrizione e **normalizzazione grafica silenziosa**; cosa si normalizza e cosa (patina linguistica) si conserva. | a mano |
| [`teiText-guida-codifica.md`](teiText-guida-codifica.md) | Guida ragionata alla codifica del `<text>`: `seg`, `@ana` a 8 assi, apparato sostanziale, indice, standOff. | a mano |
| [`indice-impatto.md`](indice-impatto.md) | Il modello `impact-index`: formula AHP `I=(4·Fnorm+2·N+A)/7`, bande, pipeline `seg → fs`. | a mano |
| [`Protocollo-indice-impatto.md`](Protocollo-indice-impatto.md) | Protocollo operativo: come si applicano ancore, bande e formula caso per caso. | a mano |
| [`protocollo-IA-codifica.md`](protocollo-IA-codifica.md) | Runbook della codifica **assistita da AI** (IT/EN): ruolo dell'AI, 8 guardie, verifica umana finale. | a mano |
| [`data-dictionary.md`](data-dictionary.md) | Dizionario degli **8 assi** e delle categorie della tassonomia, con gli `xml:id` usati in `@ana`. | **derivato** da `tassonomia-gh.xml` |
| [`anagrafe-citazioni.md`](anagrafe-citazioni.md) | Anagrafe delle **citazioni latine** (`cit`/`quote`/`bibl`) con carte e fonti. | a mano |
| [`base-dati_campionamento.md`](base-dati_campionamento.md) | **Base-dati del campione ragionato**: loci, capitoli, criteri di selezione, matrice d'impatto. | a mano |
| [`interventi-editoriali.md`](interventi-editoriali.md) | Rendiconto verificabile di **ogni intervento marcato**: apparato `add`/`del`/`subst`, `retrace`, integrazioni. | **derivato** da `castello-anima-teiText.xml` |

---

## 3. Documenti derivati — non modificare a mano

Due file di questa cartella sono **rigenerati da script**: le modifiche manuali verrebbero sovrascritte. Vanno aggiornati **solo** rigenerandoli dalla fonte (la CI lo fa in automatico ai push pertinenti).

| File derivato | Fonte | Rigenerazione |
|---|---|---|
| [`data-dictionary.md`](data-dictionary.md) | [`../tei/taxonomy/tassonomia-gh.xml`](../tei/taxonomy/) | `python3 tools/gen_data_dictionary.py` — workflow [`gen-data-dictionary.yml`](../.github/workflows/gen-data-dictionary.yml) |
| [`interventi-editoriali.md`](interventi-editoriali.md) | [`../tei/text/castello-anima-teiText.xml`](../tei/text/) | `python3 tools/estrattore_interventi.py` — workflow [`gen-interventi-editoriali.yml`](../.github/workflows/gen-interventi-editoriali.yml) |

---

## 4. Correlati — fuori da `docs/`

- **Testo e navigazione**: [`../tei/text/teiText-GUIDA.md`](../tei/text/teiText-GUIDA.md) (navigazione del file) · [`../tei/text/teiText-README.md`](../tei/text/teiText-README.md) (riferimento tecnico).
- **Metadati**: [`../tei/header/teiHeader-GUIDA.md`](../tei/header/teiHeader-GUIDA.md) · [`../tei/header/teiHeader-README.md`](../tei/header/teiHeader-README.md).
- **Tassonomia**: [`../tei/taxonomy/`](../tei/taxonomy/) (fonte normativa degli 8 assi).
- **Schemi e validazione**: [`../schema/`](../schema/) (RelaxNG + Schematron) · [`../.github/workflows/README.md`](../.github/workflows/README.md) (CI e 8 guardie).
- **Strumenti**: [`../tools/README.md`](../tools/README.md) (assistente `@ana`, calcolatore e visualizzatore dell'indice).
- **Panoramica del progetto**: [`../README.md`](../README.md).

---

## 5. Percorsi tipici

**«Voglio annotare un nuovo passo»** → [`criteri-trascrizione.md`](criteri-trascrizione.md) (come renderlo) → [`teiText-guida-codifica.md`](teiText-guida-codifica.md) (come codificarlo) → [`data-dictionary.md`](data-dictionary.md) (quali categorie `@ana`) → [`indice-impatto.md`](indice-impatto.md) (come pesarlo).

**«Voglio capire un `@ana` che leggo nel testo»** → [`data-dictionary.md`](data-dictionary.md) (significato degli assi) → [`Protocollo-indice-impatto.md`](Protocollo-indice-impatto.md) (perché quella banda).

**«Voglio verificare cosa ha toccato l'editore»** → [`interventi-editoriali.md`](interventi-editoriali.md) (rendiconto marcato) → [`criteri-trascrizione.md`](criteri-trascrizione.md) (cosa invece è normalizzato in silenzio).

---

## 6. Contatti

**Luciano Longo** — <luciano.longo@dedalus.com> · [ORCID](https://orcid.org/0009-0005-7557-7546) · [GitHub](https://github.com/luciano-longo77)
