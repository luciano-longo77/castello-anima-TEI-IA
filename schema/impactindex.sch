<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt">
  <sch:ns prefix="tei" uri="http://www.tei-c.org/ns/1.0"/>
  <sch:pattern id="indice-impatto">
    <sch:rule context="tei:fs[tei:f[@name='N_band'] and tei:f[@name='A_band']]">
      <sch:let name="nb" value="tei:f[@name='N_band']/tei:symbol/@value"/>
      <sch:let name="ab" value="tei:f[@name='A_band']/tei:symbol/@value"/>
      <sch:let name="N"  value="number(tei:f[@name='N']/tei:numeric/@value)"/>
      <sch:let name="A"  value="number(tei:f[@name='A']/tei:numeric/@value)"/>
      <sch:let name="F"  value="number(tei:f[@name='F']/tei:numeric/@value)"/>
      <sch:let name="I"  value="number(tei:f[@name='I']/tei:numeric/@value)"/>
      <sch:let name="Icalc" value="(4 * ($F div 3) + 2*$N + $A) div 7"/>
      <sch:let name="ana" value="string(//tei:seg[@xml:id = substring-after(current()/@corresp,'#')]/@ana)"/>

      <!-- R1 — vocabolario delle bande -->
      <sch:assert test="$nb='critica' or $nb='alta' or $nb='media' or $nb='bassa'"
        >R1: banda N "<sch:value-of select="$nb"/>" fuori vocabolario.</sch:assert>
      <sch:assert test="$ab='alta' or $ab='media' or $ab='bassa'"
        >R1: banda A "<sch:value-of select="$ab"/>" fuori vocabolario.</sch:assert>

      <!-- R2 — i numerici coincidono con i valori-ancora e I con la formula -->
      <sch:assert test="($nb='critica' and $N=0.90) or ($nb='alta' and $N=0.75) or ($nb='media' and $N=0.55) or ($nb='bassa' and $N=0.30)"
        >R2: N=<sch:value-of select="$N"/> non è l'ancora della banda <sch:value-of select="$nb"/>.</sch:assert>
      <sch:assert test="($ab='alta' and $A=0.85) or ($ab='media' and $A=0.675) or ($ab='bassa' and $A=0.40)"
        >R2: A=<sch:value-of select="$A"/> non è l'ancora della banda <sch:value-of select="$ab"/>.</sch:assert>
      <sch:assert test="($I - $Icalc &lt; 0.001) and ($I - $Icalc &gt; -0.001)"
        >R2: I=<sch:value-of select="$I"/> ≠ formula (<sch:value-of select="round($Icalc*1000) div 1000"/>).</sch:assert>

      <!-- R3 — la classe #impact-* sul <seg> coincide con la banda di I -->
      <sch:assert test="($I &lt; 0.50 and contains($ana,'#impact-low')) or ($I &gt;= 0.50 and $I &lt; 0.66 and contains($ana,'#impact-medium')) or ($I &gt;= 0.66 and $I &lt; 0.82 and contains($ana,'#impact-high')) or ($I &gt;= 0.82 and contains($ana,'#impact-critical'))"
        >R3: #impact-* del segmento incoerente con I=<sch:value-of select="$I"/>.</sch:assert>
    </sch:rule>
  </sch:pattern>
</sch:schema>
