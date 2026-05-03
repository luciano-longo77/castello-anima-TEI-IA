<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron">
    
    
    <!--  SCHEMATRON PER IL VOCABOLARIO TASSONOMICO TEI
     Castello dell’anima – sistema prudenziale -->
    
    <pattern id="taxonomy-rules">
        
        
        <!-- Regole per TUTTE le category -->
        
        
        <rule context="*[local-name() = 'category']">
            
            <!-- Ogni category deve avere un desc -->
            <assert test="*[local-name() = 'desc']">
                Ogni &lt;category&gt; deve contenere un elemento &lt;desc&gt;.
            </assert>
            
            <!-- Il desc non deve essere vuoto -->
            <assert test="normalize-space(*[local-name() = 'desc']) != ''">
                Il contenuto di &lt;desc&gt; non può essere vuoto.
            </assert>
            
        </rule>
        
        
        <!-- Regola di prefisso: SOLO per taxonomy ≠ func    -->
        
        <rule context="
            *[local-name() = 'category']
            [not(ancestor::*[local-name() = 'taxonomy'][@xml:id='func'])]">
            
            <let name="taxID"
                value="ancestor::*[local-name() = 'taxonomy'][1]/@xml:id"/>
            <assert test="
                not(contains(@xml:id, '-'))
                or
                starts-with(@xml:id, concat($taxID, '-'))
                ">
                L’attributo @xml:id della &lt;category&gt; deve iniziare con
                il prefisso della tassonomia padre (&lt;value-of select="$taxID"/&gt;-).
            </assert>
            
        </rule>
        
        
        <!-- NOTA  taxonomy xml:id='func' è ESENTE dalla regola perché ammette sotto‑assi funzionali interni: rischio-*, ethos-*, pedagogia-*-->
        
    </pattern>
    
</schema>
