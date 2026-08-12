#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia citazioni - impone la grammatica di encoding delle citazioni nel teiText
del *Castello dell'anima* e intercetta le citazioni non marcate.

Per ogni citazione latina il modello prevede: dentro il <seg> che la contiene,
un <cit> con <quote xml:lang="…"> (il testo citato) e <bibl> (la fonte); la
funzione intertestuale sta nell'@ana del SEG (#relation-intertesto-*), non su
<cit>; l'indice d'impatto resta sul seg (nessuna <fs> verso la cit).

Verifica:
  A. nessuna <quote> "orfana": ogni <quote> sta dentro una <cit>  (→ citazioni presenti e marcate);
  B. ogni <cit>:
     1. è dentro un <seg> con @xml:id;
     2. ha una <quote> con @xml:lang e testo non vuoto;
     3. ha una <bibl> non vuota (la fonte);
     4. NON porta @ana né @type (la funzione va sul seg);
     5. il <seg> contenitore ha @ana con un token #relation-intertesto-*;
  C. nessuna <fs> dello standOff impact-index punta a una <cit> (indice solo sul seg).

Uso:  python3 citazioni_guard.py [TEXT_XML]
"""
import sys
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"; XML = "http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s" % (TEI, t)
def Q(a): return "{%s}%s" % (XML, a)
def ln(e): return e.tag.split("}")[-1] if isinstance(e.tag, str) else "?"
def txt(e): return "".join(e.itertext()).strip() if e is not None else ""

TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"
R = etree.parse(TEXT).getroot()

def enclosing_seg(e):
    p = e.getparent()
    while p is not None:
        if ln(p) == "seg": return p
        p = p.getparent()
    return None

errors = []

# --- A. nessuna <quote> fuori da <cit> (citazione non marcata) ---
for q in R.iter(T("quote")):
    p = q.getparent()
    if p is None or ln(p) != "cit":
        seg = enclosing_seg(q)
        where = (seg.get(Q("id")) if seg is not None else "?") if seg is not None else "?"
        errors.append("<quote> fuori da <cit> (citazione non marcata) in seg %s: %r"
                      % (where, txt(q)[:40]))

# --- B. grammatica di ogni <cit> ---
cit_ids = set()
for c in R.iter(T("cit")):
    seg = enclosing_seg(c)
    where = (seg.get(Q("id")) if seg is not None else None) or "?"
    cid = c.get(Q("id"))
    if cid: cit_ids.add(cid)
    # 1. dentro un seg con xml:id
    if seg is None or not seg.get(Q("id")):
        errors.append("cit non dentro un <seg> con @xml:id (presso %s)" % where)
    # 2. quote con xml:lang e testo
    q = c.find(T("quote"))
    if q is None:
        errors.append("%s: <cit> senza <quote>" % where)
    else:
        if not q.get(Q("lang")):
            errors.append("%s: <quote> senza @xml:lang" % where)
        if not txt(q):
            errors.append("%s: <quote> vuota" % where)
    # 3. bibl non vuota
    b = c.find(T("bibl"))
    if b is None or not txt(b):
        errors.append("%s: <cit> senza <bibl> (fonte) o bibl vuota" % where)
    # 4. niente @ana / @type su cit
    if c.get("ana"):
        errors.append("%s: <cit> con @ana (la funzione va sull'@ana del seg)" % where)
    if c.get("type"):
        errors.append("%s: <cit> con @type (non ammesso: nessun @type su cit)" % where)
    # 5. il seg contenitore dichiara la funzione intertestuale
    if seg is not None:
        ana = seg.get("ana") or ""
        if not any(tok.startswith("#relation-intertesto") for tok in ana.split()):
            errors.append("%s: il <seg> della cit non ha #relation-intertesto-* in @ana" % where)

# --- C. nessuna fs verso una cit (indice solo sul seg) ---
for f in R.iter(T("fs")):
    corr = (f.get("corresp") or "").lstrip("#")
    if corr in cit_ids:
        errors.append("fs %s punta a una <cit> (l'indice d'impatto va sul <seg>)" % (f.get(Q("id")) or corr))

ncit = sum(1 for _ in R.iter(T("cit")))
if errors:
    print("::error::Guardia citazioni: %d violazioni." % len(errors))
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print("Guardia citazioni superata: %d <cit> conformi (quote@xml:lang + bibl dentro <seg>, "
      "niente @ana/@type su cit, seg con #relation-intertesto, nessuna quote orfana)." % ncit)
