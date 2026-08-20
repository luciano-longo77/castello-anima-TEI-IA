#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Guardia round-trip SKOS <-> teiText (solo lxml).

Verifica che OGNI token @ana dei <seg> e OGNI banda <symbol value> delle <fs> del teiText
abbia un skos:Concept con quella skos:notation nel vocabolario generato. Le bande sono
verificate PER-SCHEME (value 'media' esiste sia in impact-band-N sia in impact-band-A):
il <symbol> in <f name="N_band"> deve risolvere nello scheme impact-band-N, ecc.
I token #fig-* / #area-* (sugli <span>, dichiarati inline, non in tassonomia) sono ESCLUSI.

Uso: python3 skos_guard.py tei/text/castello-anima-teiText.xml vocab/castello-anima-vocab.ttl"""
import sys, re
from lxml import etree
TEI="http://www.tei-c.org/ns/1.0"; XML="http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s"%(TEI,t)

TEXT = sys.argv[1] if len(sys.argv)>1 else "tei/text/castello-anima-teiText.xml"
TTL  = sys.argv[2] if len(sys.argv)>2 else "vocab/castello-anima-vocab.ttl"

# --- parse .ttl (Turtle) a mano: blocchi di Concept -> (scheme, notation) ---
ttl=open(TTL,encoding="utf-8").read()
ana_notn=set()                 # notation degli assi @ana (i "#...")
band_notn={}                   # scheme -> set(value) per le bande
blocks=re.split(r"\n(?=<)", ttl)
for b in blocks:
    if "a skos:Concept" not in b: continue
    msch=re.search(r"skos:inScheme\s+<[^>]*/([^>/]+)>", b)
    mnot=re.search(r'skos:notation\s+"((?:[^"\\]|\\.)*)"', b)
    if not (msch and mnot): continue
    sch=msch.group(1); nt=mnot.group(1).replace('\\"','"')
    if sch.startswith("impact-band-"): band_notn.setdefault(sch,set()).add(nt)
    else: ana_notn.add(nt)

doc=etree.parse(TEXT); R=doc.getroot()
def in_header(e):
    p=e.getparent()
    while p is not None:
        if p.tag==T("teiHeader"): return True
        p=p.getparent()
    return False

err=[]
# 1) token @ana sui <seg> (esclusi #fig-*/#area-* e placeholder #impact*)
for s in R.iter(T("seg")):
    if in_header(s): continue
    for tok in (s.get("ana") or "").split():
        if tok.startswith("#fig-") or tok.startswith("#area-") or tok=="#impact*": continue
        if tok not in ana_notn:
            err.append("@ana '%s' senza skos:Concept (notation) — seg %s"%(tok, s.get("{%s}id"%XML)))
# 2) bande <symbol> nelle <fs> (per-scheme via @name della <f>)
BAND_SCHEME={"N_band":"impact-band-N","A_band":"impact-band-A"}
for fs in R.iter(T("fs")):
    for f in fs.findall(T("f")):
        sch=BAND_SCHEME.get(f.get("name"))
        if not sch: continue
        sym=f.find(T("symbol"))
        if sym is None: continue
        v=sym.get("value")
        if v not in band_notn.get(sch,set()):
            err.append("banda <symbol value='%s'> (%s) senza skos:Concept nello scheme %s — fs %s"%(v,f.get("name"),sch,fs.get("{%s}id"%XML)))

na=len(ana_notn); nb=sum(len(v) for v in band_notn.values())
if err:
    print("::error::Round-trip SKOS fallito: %d violazioni"%len(err))
    for e in err[:40]: print("  -",e)
    sys.exit(1)
print("Round-trip SKOS superato: tutti gli @ana e le bande del teiText risolvono al vocabolario (%d notation @ana + %d bande, %d scheme)."%(na,nb,len(band_notn)+1 if band_notn else 0))
