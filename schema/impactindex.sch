<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt">
  <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
  <!-- C0 in pattern PROPRIO: in Schematron un nodo e' processato da una sola <rule> per <pattern>;
       tenendo C0 (contesto "ha banda") separato da C1-C4 (contesto "ha @corresp") si evita che,
       su una fs normale che matcha entrambi, le C1-C4 vengano saltate. -->
  <sch:pattern id="indice-ancoraggio">
    <!-- C0: una fs con banda d'impatto (N_band/A_band) DEVE avere @corresp -->
    <sch:rule context="tei:fs[tei:f[@name='N_band'] or tei:f[@name='A_band']]">
      <sch:assert test="@corresp">C0: fs d'impatto senza @corresp (nessun ancoraggio al &lt;seg&gt;).</sch:assert>
    </sch:rule>
  </sch:pattern>
  <sch:pattern id="indice-completezza">
    <!-- ogni fs d'impatto: @corresp singolo #xml:id, i 6 campi, naming idx-, target seg con @ana -->
    <sch:rule context="tei:fs[@corresp]">
      <sch:let name="sid" value="substring-after(@corresp,'#')"/>
      <sch:assert test="starts-with(@corresp,'#') and not(contains(normalize-space(@corresp),' '))
        and string-length($sid) &gt; 0 and not(starts-with($sid,'#'))"
        >C1: @corresp deve essere un singolo riferimento nella forma #xml:id.</sch:assert>
      <sch:assert test="tei:f[@name='N_band'] and tei:f[@name='A_band'] and tei:f[@name='N']
        and tei:f[@name='A'] and tei:f[@name='F'] and tei:f[@name='Fnorm'] and tei:f[@name='I']"
        >C2: fs d'impatto incompleta (servono N_band, A_band, N, A, F, Fnorm, I).</sch:assert>
      <sch:assert test="@xml:id = concat('idx-',$sid)"
        >C3: xml:id della fs diverso da 'idx-' + xml:id del seg.</sch:assert>
      <sch:assert test="count(//tei:seg[@xml:id=$sid])=1 and //tei:seg[@xml:id=$sid]/@ana"
        >C4: @corresp non punta a un unico &lt;seg&gt; con @ana.</sch:assert>
    </sch:rule>
    <!-- completezza inversa: ogni <seg> annotato ha ESATTAMENTE una fs gemella -->
    <sch:rule context="tei:seg[@ana]">
      <sch:let name="sid" value="string(@xml:id)"/>
      <sch:assert test="count(//tei:fs[@corresp=concat('#',$sid)])=1"
        >C5: il &lt;seg&gt; annotato non ha esattamente una &lt;fs&gt; gemella (corresp='#'+xml:id).</sch:assert>
    </sch:rule>
  </sch:pattern>

  <!-- ============================================================================
       Indice d'impatto: vocabolario bande (R1), ancore + formula (R2), classe<->I (R3).
       ============================================================================ -->
  <sch:pattern id="indice-impatto">
    <sch:rule context="tei:fs[tei:f[@name='N_band'] and tei:f[@name='A_band']]">
      <sch:let name="nb" value="tei:f[@name='N_band']/tei:symbol/@value"/>
      <sch:let name="ab" value="tei:f[@name='A_band']/tei:symbol/@value"/>
      <sch:let name="N"  value="number(tei:f[@name='N']/tei:numeric/@value)"/>
      <sch:let name="A"  value="number(tei:f[@name='A']/tei:numeric/@value)"/>
      <sch:let name="F"  value="number(tei:f[@name='F']/tei:numeric/@value)"/>
      <sch:let name="I"  value="number(tei:f[@name='I']/tei:numeric/@value)"/>
      <sch:let name="Icalc" value="(4 * ($F div 3) + 2*$N + $A) div 7"/>
      <sch:let name="sid" value="substring-after(@corresp,'#')"/>
      <sch:let name="ana" value="string(//tei:seg[@xml:id=$sid]/@ana)"/>
      <sch:let name="anaP" value="concat(' ', normalize-space($ana), ' ')"/>

      <!-- R1 - vocabolario delle bande -->
      <sch:assert test="$nb='critica' or $nb='alta' or $nb='media' or $nb='bassa'"
        >R1: banda N "<sch:value-of select="$nb"/>" fuori vocabolario.</sch:assert>
      <sch:assert test="$ab='alta' or $ab='media' or $ab='bassa'"
        >R1: banda A "<sch:value-of select="$ab"/>" fuori vocabolario.</sch:assert>

      <!-- R2 - i numerici coincidono con i valori-ancora e I con la formula -->
      <sch:assert test="($nb='critica' and $N=0.90) or ($nb='alta' and $N=0.75) or ($nb='media' and $N=0.55) or ($nb='bassa' and $N=0.30)"
        >R2: N=<sch:value-of select="$N"/> non è l'ancora della banda <sch:value-of select="$nb"/>.</sch:assert>
      <sch:assert test="($ab='alta' and $A=0.85) or ($ab='media' and $A=0.675) or ($ab='bassa' and $A=0.40)"
        >R2: A=<sch:value-of select="$A"/> non è l'ancora della banda <sch:value-of select="$ab"/>.</sch:assert>
      <sch:assert test="($I - $Icalc &lt; 0.001) and ($I - $Icalc &gt; -0.001)"
        >R2: I=<sch:value-of select="$I"/> ≠ formula (<sch:value-of select="round($Icalc*1000) div 1000"/>).</sch:assert>

      <!-- R3 - la classe #impact-* sul <seg> coincide con la banda di I.
           Confronto TOKEN-SAFE in XPath 1.0 (spazi-delimitatori, var anaP), non substring. -->
      <sch:assert test="($I &lt; 0.50 and contains($anaP,' #impact-low ')) or ($I &gt;= 0.50 and $I &lt; 0.66 and contains($anaP,' #impact-medium ')) or ($I &gt;= 0.66 and $I &lt; 0.82 and contains($anaP,' #impact-high ')) or ($I &gt;= 0.82 and contains($anaP,' #impact-critical '))"
        >R3: #impact-* del segmento incoerente con I=<sch:value-of select="$I"/>.</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
