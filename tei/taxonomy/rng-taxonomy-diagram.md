# Diagramma concettuale del governo tassonomico (TEI / RNG)

Il diagramma seguente rappresenta in forma schematica la struttura di governo
della tassonomia interpretativa in ambiente TEI.  
La visualizzazione ha **funzione esplicativa** e non sostituisce lo schema formale
di validazione (Relax NG e Schematron).

```mermaid
flowchart TD
    TEI --> teiHeader
    teiHeader --> encodingDesc
    encodingDesc --> classDecl
    classDecl --> taxonomy

    taxonomy --> category
    category --> desc

    category -.->|xml:id stabile| ana["@ana nei testi"]

    note right of taxonomy
      Tassonomie distinte
      (func, risk, impact,
       mystic_state, operation,
       exposition, phase, relation)
    end

    note right of desc
      <desc> obbligatorio
      (vincolo Schematron)
    end