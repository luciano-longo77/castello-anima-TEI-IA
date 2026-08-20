#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera il vocabolario SKOS (Turtle) del *Castello dell'anima* da tassonomia-gh.xml.

SINGLE SOURCE OF TRUTH = tei/taxonomy/tassonomia-gh.xml. Questo .ttl e' un ARTEFATTO
GENERATO: non va editato a mano (come taxonomy-rng.rng / taxonomy-sch.sch). Un
ConceptScheme per asse (10); ogni <category> -> skos:Concept. La skos:notation e' il
token ESATTO com'e' nel dato: '#<id>' per gli assi di @ana (func compreso, senza prefisso),
il valore nudo ('critica'/'alta'/'media'/'bassa') per le bande impact-band-N/A che nel
teiText compaiono come <symbol value="..."/> nelle <fs>. Solo lxml (nessuna dipendenza).

Uso: python3 gen_skos.py tassonomia-gh.xml <base-URI> [alignments.tsv] > vocab.ttl"""
import sys, re
from lxml import etree

TEI="http://www.tei-c.org/ns/1.0"; XML="http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s"%(TEI,t)
def Q(a): return "{%s}%s"%(XML,a)

SRC  = sys.argv[1] if len(sys.argv)>1 else "tei/taxonomy/tassonomia-gh.xml"
BASE = sys.argv[2] if len(sys.argv)>2 else "https://w3id.org/castello-anima-vocab/"
ALIGN= sys.argv[3] if len(sys.argv)>3 else None
if not BASE.endswith("/"): BASE+="/"

def esc(s):
    s=re.sub(r"\s+"," ",(s or "").strip())
    return s.replace("\\","\\\\").replace('"','\\"')
def human(cid):  # prefLabel: id "umanizzato"
    return cid.replace("-"," ").replace("_"," ")
def notation(axis_id, cid):
    # bande: token = valore del <symbol> (senza '#'), cioe' l'id meno il prefisso dell'asse
    if axis_id.startswith("impact-band-"):
        return cid[len(axis_id)+1:] if cid.startswith(axis_id+"-") else cid
    # tutti gli altri assi (func compreso): token @ana = '#'+id
    return "#"+cid

# allineamenti esterni opzionali (TSV: id <TAB> closeMatch|exactMatch <TAB> URI)
align={}
if ALIGN:
    try:
        for ln in open(ALIGN,encoding="utf-8"):
            ln=ln.rstrip("\n")
            if not ln or ln.lstrip().startswith("#"): continue
            p=ln.split("\t")
            if len(p)>=3 and p[1] in ("closeMatch","exactMatch"):
                align.setdefault(p[0],[]).append((p[1],p[2]))
    except FileNotFoundError: pass

doc=etree.parse(SRC); R=doc.getroot()
out=[]
out.append("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .")
out.append("@prefix dct:  <http://purl.org/dc/terms/> .")
out.append("@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .")
out.append("@prefix :     <%s> ."%BASE)
out.append("")
out.append("# Vocabolario SKOS del Castello dell'anima — GENERATO da tassonomia-gh.xml (non editare a mano).")
out.append("")

nsch=ncon=0
for tax in R.iter(T("taxonomy")):
    ax=tax.get(Q("id"))
    if not ax: continue
    nsch+=1
    out.append("<%s%s> a skos:ConceptScheme ;"%(BASE,ax))
    out.append('    dct:title "Asse %s"@it .'%ax)
    out.append("")
    for c in tax.iter(T("category")):
        cid=c.get(Q("id"))
        if not cid: continue
        ncon+=1
        par=c.getparent()
        pid=par.get(Q("id")) if par.tag==T("category") else None
        desc=esc(c.findtext(T("catDesc")))
        lines=["<%s%s> a skos:Concept ;"%(BASE,cid)]
        lines.append("    skos:inScheme <%s%s> ;"%(BASE,ax))
        if pid: lines.append("    skos:broader <%s%s> ;"%(BASE,pid))
        else:   lines.append("    skos:topConceptOf <%s%s> ;"%(BASE,ax))
        lines.append('    skos:notation "%s" ;'%esc(notation(ax,cid)))
        lines.append('    skos:prefLabel "%s"@it ;'%esc(human(cid)))
        for kind,uri in align.get(cid,[]):
            lines.append("    skos:%s <%s> ;"%(kind,uri))
        lines.append('    skos:definition "%s"@it .'%desc)
        out.append("\n".join(lines)); out.append("")

sys.stderr.write("SKOS: %d ConceptScheme, %d Concept\n"%(nsch,ncon))
sys.stdout.write("\n".join(out)+"\n")
