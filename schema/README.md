# `/schema` — schemi di validazione del testo

Questa cartella contiene gli schemi con cui si valida il **testo** dell'edizione
(`tei/text/castello-anima-teiText.xml` + `tei/header/castello-anima-teiHeader.xml`).

| file | tipo | ruolo |
| :--- | :--- | :--- |
| **`tei_all.rng`** | RelaxNG (TEI P5 «TEI All», versione vendorizzata) | validazione **strutturale**: esistenza elementi, attributi ammessi, modelli di contenuto. Versione fissata per una validazione riproducibile. |
| **`impactindex.sch`** | Schematron | vincoli dell'**indice d'impatto** sulle `<fs>`: vocabolario delle bande, ancore N/A esatte, formula `I=(4·Fnorm+2·N+A)/7` (tolleranza 0.001), classe `#impact-*` ↔ soglia di `I`. |

Il `teiHeader` dichiara questi schemi via `<?xml-model?>` (→ `tei_all.rng` locale) e
`<schemaRef type="schematron" url="../../schema/impactindex.sch"/>`.

## Dove trovare ODD, RNG e Schematron

- **Testo (questa cartella).** RNG = `tei_all.rng`; Schematron = `impactindex.sch`.
  Ai due schemi si aggiungono, in CI, **8 guardie Python** (`.github/workflows/scripts/`)
  che coprono i vincoli non esprimibili in RNG (co-occorrenza `@ana`, grammatica dei
  commenti-`seg`, citazioni, interventi editoriali, regole fissate, whitespace anti-corruzione).
  L'**ODD del modello** del testo è previsto (backlog): il suo contenuto — tagset,
  attributi, annidamenti, liste di valori — è già documentato in forma pronta in
  [`docs/teiText-guida-codifica.md`](../docs/teiText-guida-codifica.md).

- **Tassonomia (cartella separata).** Ha un **ODD reale** e la sua catena di validazione:
  [`tei/taxonomy/schema/taxonomy-odd.odd`](../tei/taxonomy/schema/taxonomy-odd.odd) →
  [`taxonomy-rng.rng`](../tei/taxonomy/schema/taxonomy-rng.rng) +
  [`taxonomy-sch.sch`](../tei/taxonomy/schema/taxonomy-sch.sch),
  descritti in [`tei/taxonomy/schema/README-schema.md`](../tei/taxonomy/schema/README-schema.md).

## Come li usa la CI

- **`Validate Text`** (`.github/workflows/validate-text.yml`): NFC → XInclude →
  `jing schema/tei_all.rng` sul documento risolto → 8 guardie → `impactindex.sch`.
- **`Validate Taxonomy`** (`.github/workflows/main.yml`): valida
  `tei/taxonomy/tassonomia-gh.xml` contro `taxonomy-rng.rng` + `taxonomy-sch.sch`.

## Riproducibilità

`tei_all.rng` è **vendorizzato** (release TEI P5 fissata) per evitare che aggiornamenti
upstream cambino l'esito della validazione. Per la piena riproducibilità, registra le
versioni di TEI P5, `jing`, `python`/`lxml`, `libxml2`/`xmllint` (vedi
[`docs/protocollo-IA-codifica.md`](../docs/protocollo-IA-codifica.md)).
