#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia regole-fissate - invarianti stratigrafiche e strutturali del teiText del
*Castello dell'anima* (audit 2026-08). Opera sul modulo (xi:include NON risolto:
vede solo i <seg> di contenuto, non gli esempi del teiHeader).

Verifica:
  R1  <retrace> = ritracciatura, strato bruno T0->T1: hand="#ink_1" (mai #ink_3-dark);
      e mai annidato dentro <add> (il testo aggiunto non e' una ritracciatura).
  R2  xml:id dei <seg>: seg-cNpP-label | seg-pro-pP-label | seg-tit-*.
  R3  @ana interpretativo solo sul <seg> (in standOff sul <span>): mai su cit/rs/term/quote.
  R5  sobrieta: #phase-critical mai su #impact-low, e solo con operazione-guardia
      (precisatio/attenuatio/riequilibrio/declaratio) o rischio caldo
      (quietismo/panteismo/impeccabilita/dottrinale).

(R4 <supplied> con @resp/@cert e' gia' imposta da interventi_guard.py;
 la co-occorrenza di base @ana da cooccurrence_guard.py.)

Fallisce (exit 1) elencando le violazioni.
Uso:  python3 regole_fissate_guard.py [TEXT_XML]
"""
import sys, re
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"
def T(t): return "{%s}%s" % (TEI, t)
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"

R = etree.parse(TEXT).getroot()
errors = []

SEG_ID = re.compile(r"^seg-(c\d+p\d+[a-z]?|pro-p\d+|tit)-")
ANA_VIETATO = {T("cit"), T("rs"), T("term"), T("quote")}
GUARD_OPS = {"#operation-precisatio", "#operation-attenuatio", "#operation-riequilibrio", "#operation-declaratio"}
CALDI = {"#risk-quietismo", "#risk-panteismo", "#risk-impeccabilita", "#risk-dottrinale"}

# R1 - retrace: strato bruno #ink_1, mai annidato in <add>
for rr in R.iter(T("retrace")):
    if rr.get("hand") != "#ink_1":
        errors.append("R1 <retrace> hand=%s (atteso #ink_1): la ritracciatura e' T0->T1 bruno, non T3 scuro" % rr.get("hand"))
    par = rr.getparent()
    if par is not None and par.tag == T("add"):
        errors.append("R1 <retrace> annidato in <add>: il testo aggiunto non e' ritracciato (rimuovere il retrace spurio)")

# R2 - naming xml:id dei seg
for s in R.iter(T("seg")):
    sid = s.get(XMLID)
    if sid and not SEG_ID.match(sid):
        errors.append("R2 seg xml:id fuori convenzione (seg-cNpP-label / seg-pro-pP-* / seg-tit-*): %s" % sid)

# R3 - @ana interpretativo solo sul seg (span in standOff), mai su cit/rs/term/quote
for el in R.iter():
    if el.get("ana") and el.tag in ANA_VIETATO:
        errors.append("R3 @ana su <%s>: l'annotazione interpretativa va nell'@ana del <seg>" % el.tag.split("}")[-1])

# R5 - sobrieta del phase-critical
for s in R.iter(T("seg")):
    toks = set((s.get("ana") or "").split())
    if "#phase-critical" in toks:
        sid = s.get(XMLID)
        if "#impact-low" in toks:
            errors.append("R5 #phase-critical su #impact-low: %s" % sid)
        if not (toks & GUARD_OPS or toks & CALDI):
            errors.append("R5 #phase-critical senza recinzione (ne operazione-guardia ne rischio caldo): %s" % sid)

if errors:
    print("::error::Guardia regole-fissate: %d violazioni." % len(errors))
    for e in errors:
        print("  -", e)
    sys.exit(1)
print("Guardia regole-fissate superata (R1 retrace, R2 naming, R3 @ana-seg, R5 sobrieta).")
