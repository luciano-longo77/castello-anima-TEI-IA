#!/usr/bin/env python3
"""Genera il SKOS del gemello (17 stati-mistici) + l'allineamento con castello-anima-vocab.
Deterministico: legge i catDesc reali dal TEI-Header del gemello. Dipendenza: lxml (+ rdflib per validare)."""
from lxml import etree
import re, io

TWIN_HDR = "Micro-commits/MC-1/data/TEI-Header.xml"
BASE_ED  = "https://w3id.org/castello-edizione-vocab/"
BASE_AN  = "https://w3id.org/castello-anima-vocab/"
ns = {'t':'http://www.tei-c.org/ns/1.0'}; X='{http://www.w3.org/XML/1998/namespace}id'

def states():
    r = etree.parse(TWIN_HDR).getroot()
    out = []
    for tax in r.findall('.//t:taxonomy', ns):
        if tax.get(X) and 'stati' in tax.get(X):
            for c in tax.findall('.//t:category', ns):
                cd = c.find('t:catDesc', ns)
                d = re.sub(r'\s+',' ', ''.join(cd.itertext()).strip()) if cd is not None else ''
                out.append((c.get(X), d))
    return out

def esc(s): return s.replace('\\','\\\\').replace('"','\\"')
def label(cid): return cid.replace('-', ' ')

# --- 1) castello-edizione-vocab.ttl -------------------------------------
st = states()
L = []
L.append("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .")
L.append("@prefix dct:  <http://purl.org/dc/terms/> .")
L.append("@prefix ed:   <%s> ." % BASE_ED)
L.append("")
L.append("<%s> a skos:ConceptScheme ;" % (BASE_ED))
L.append('    dct:title "Castello dell\'anima — vocabolario dell\'edizione (stati mistici)"@it ;')
L.append('    dct:description "SKOS dei 17 stati-mistici del repo castello-dell-anima-edizione (MC-1); gemello di castello-anima-vocab."@it .')
L.append("")
for cid, d in st:
    L.append("ed:%s a skos:Concept ;" % cid)
    L.append("    skos:topConceptOf <%s> ;" % BASE_ED)
    L.append("    skos:inScheme <%s> ;" % BASE_ED)
    L.append('    skos:notation "%s" ;' % cid)
    L.append('    skos:prefLabel "%s"@it ;' % esc(label(cid)))
    if d:
        L.append('    skos:definition "%s"@it .' % esc(d))
    else:
        L[-1] = L[-1].rstrip(' ;') + ' .'
    L.append("")
io.open('/tmp/li2/fix/castello-edizione-vocab.ttl','w',encoding='utf-8').write('\n'.join(L))

# --- 2) alignments-castello-anima-edizione.ttl --------------------------
CLOSE = [("mystic_state-quiete","quiete"),("mystic_state-otium","otio"),
         ("mystic_state-unione","unione"),("mystic_state-illuminazione","contemplazione-infusa")]
NARROW= [("mystic_state-purificazione","purga"),("mystic_state-purificazione","notte")]
RELATED=[("relation-mistica-unione-sposalitio","matrimonio-spirituale"),
         ("relation-mistica-unione-sposalitio","trasformazione"),
         ("relation-mistica-infusa-purificazione","contemplazione-infusa"),
         ("relation-mistica-passiva-quiete","quiete")]
twin_ids = {c for c,_ in st}
for _,t in CLOSE+NARROW+RELATED:
    assert t in twin_ids, "target gemello inesistente: "+t
A = []
A.append("@prefix skos: <http://www.w3.org/2004/02/skos/core#> .")
A.append("@prefix an: <%s> ." % BASE_AN)
A.append("@prefix ed: <%s> ." % BASE_ED)
A.append("")
A.append("# Allineamento castello-anima-vocab  <->  castello-edizione-vocab (Fase 2 SKOS)")
def block(pairs, pred):
    for s,t in pairs:
        A.append("an:%s skos:%s ed:%s ." % (s, pred, t))
A.append("# closeMatch"); block(CLOSE,"closeMatch")
A.append("# narrowMatch (il concetto 'anima' e' piu' ampio del corrispettivo 'edizione')"); block(NARROW,"narrowMatch")
A.append("# relatedMatch (relazione 'anima' <-> concetto 'edizione')"); block(RELATED,"relatedMatch")
A.append("")
io.open('/tmp/li2/fix/alignments-castello-anima-edizione.ttl','w',encoding='utf-8').write('\n'.join(A))
print("scritti: castello-edizione-vocab.ttl (%d concetti) + alignments (%d match)" % (len(st), len(CLOSE)+len(NARROW)+len(RELATED)))
