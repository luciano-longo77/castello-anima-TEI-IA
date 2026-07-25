<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt2">
    <title>ISO Schematron rules</title>
    <!-- This file generated 2026-07-18-->
    <ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
    <pattern id="schematron-constraint-category-catdesc-present-1">
        <rule context="tei:category">
            <assert test="tei:catDesc" role="error">Errore filologico: ogni &lt;category&gt; deve contenere un elemento &lt;catDesc&gt; per l'autodocumentazione semantica.</assert>
        </rule>
    </pattern>
    <pattern id="schematron-constraint-category-catdesc-not-empty-2">
        <rule context="tei:category">
            <assert test="normalize-space(string(tei:catDesc)) != ''" role="error">Assegnazione semantica fallita: il contenuto di &lt;catDesc&gt; non può essere vuoto.</assert>
        </rule>
    </pattern>
    <pattern id="schematron-constraint-category-prefix-consistency-3">
        <rule context="tei:category">
            <let name="taxID" value="string(ancestor::tei:taxonomy[1]/@xml:id)"/>
            <assert role="error"
                test="$taxID = 'func' or starts-with(@xml:id, concat($taxID, '-'))"> Errore di coerenza del dato: l'attributo @xml:id della &lt;category&gt; (<value-of select="@xml:id"/>) deve iniziare con il prefisso della tassonomia radice (<value-of select="$taxID"/>-), fatto salvo l'asse esente 'func'.</assert>
        </rule>
    </pattern>
    <pattern id="schematron-constraint-taxonomy-category-xmlid-unique-4">
        <rule context="tei:category | tei:taxonomy">
            <assert role="error" test="count(//*[@xml:id = current()/@xml:id]) = 1"> Errore di unicità: l'attributo @xml:id ('<value-of select="@xml:id"/>') di &lt;<name/>&gt; non è univoco nel documento; è usato da almeno un altro elemento.</assert>
        </rule>
    </pattern>
</schema>
