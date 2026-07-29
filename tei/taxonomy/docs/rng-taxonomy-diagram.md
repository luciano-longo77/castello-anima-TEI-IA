# Diagramma concettuale del governo tassonomico (TEI / RNG)

Il diagramma seguente rappresenta in forma schematica la struttura di governo
della tassonomia interpretativa in ambiente TEI.  
La visualizzazione ha **funzione esplicativa** e non sostituisce lo schema formale
di validazione (Relax NG e Schematron).

```
graph TD
    TEI --> teiHeader
    teiHeader --> encodingDesc
    encodingDesc --> classDecl
    classDecl --> taxonomy

    taxonomy --> category
    category --> descNode["catDesc"]

    category -.-> anaNode

    subgraph NoteTaxonomy
        taxList["func, risk, impact, mystic_state, operation, exposition, phase, relation"]
    end
    taxonomy --- NoteTaxonomy

    subgraph NoteCategory
        catConstraint["vincolo Schematron (context: category)"]
    end
    category --- NoteCategory
```
