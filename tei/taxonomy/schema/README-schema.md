# Schema — file di validazione della tassonomia

Questa cartella contiene i file che governano la validazione formale del sistema tassonomico. Non contengono la tassonomia stessa (quella è in [`tassonomia-gh.xml`](../tassonomia-gh.xml)) — definiscono le regole a cui `tassonomia-gh.xml` deve conformarsi.

## I tre file

| File | Ruolo | Origine |
|---|---|---|
| `taxonomy.odd` | **Fonte normativa** — definizione astratta del modello, in linguaggio ODD (TEI) | Scritto a mano |
| `taxonomy-rng.rng` | Schema RelaxNG — validazione strutturale | **Generato automaticamente** da `taxonomy.odd` |
| `taxonomy-sch.sch` | Regole Schematron — validazione semantica (4 regole: presenza `catDesc`, non-vacuità, coerenza prefisso, unicità `xml:id`) | **Generato automaticamente** da `taxonomy.odd` |

## ⚠️ Non modificare `.rng` e `.sch` a mano

Sono file generati. Qualsiasi modifica diretta viene persa al prossimo giro di rigenerazione. Per cambiare una regola di validazione, modifica **sempre** `taxonomy.odd`, poi rigenera.

## Come rigenerare

Con Roma (integrato in oXygen XML Editor):
taxonomy.odd → Roma → taxonomy-rng.rng + taxonomy-sch.sch

Dopo la rigenerazione, entrambi i file vanno committati insieme alla modifica dell'ODD che li ha prodotti.

## Validazione automatica

Ogni push che tocca `tei/taxonomy/**` attiva il workflow [`main.yml`](../../../.github/workflows/main.yml), che valida `tassonomia-gh.xml` contro questi due schemi (più un controllo sui file in `esempio/`). Se `taxonomy-rng.rng` o `taxonomy-sch.sch` non sono presenti o non aggiornati, la CI fallisce.

## Documentazione completa

Per la descrizione delle 8 tassonomie, delle regole Schematron nel dettaglio e dei vincoli editoriali non ancora automatizzati, vedi [`Sistema Tassonomico.md`](../Sistema%20Tassonomico.md).
