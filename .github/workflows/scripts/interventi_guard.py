#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia interventi-editoriali - impone la coerenza degli interventi editoriali MARCATI
sul teiText del *Castello dell'anima* (modello interpretativo: normalizzazione grafica
silenziosa e dichiarata; apparato sostanziale solo in app/rdg).

Verifiche ATTIVE nel modello interpretativo:
  - ogni `supplied` con `@resp` E `@cert` (integrazione congetturale/su guasto);
  - ogni `subst` ben formato (almeno un `add` e un `del`).

Controlli LEGACY (rete di sicurezza; vacui finche' non esistono `<choice>`, che il modello
interpretativo non usa - la normalizzazione grafica non e' marcata nel testo di lettura):
  - `reg`/`expan` SENZA `@resp` (attribuzione globale in editorialDecl);
  - `corr` pienamente attribuito (`@resp` + `@cert` su ognuna).

Uso:  python3 interventi_guard.py [TEXT_XML]
"""
import sys
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"; XML = "http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s" % (TEI, t)
def Q(a): return "{%s}%s" % (XML, a)
def ln(e): return e.tag.split("}")[-1] if isinstance(e.tag, str) else "?"

TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"
R = etree.parse(TEXT).getroot()

# carta corrente e seg contenitore, per localizzare i rilievi
folio_of = {}; cur = "?"
for e in R.iter():
    if ln(e) == "pb": cur = e.get("n") or "?"
    folio_of[e] = cur
def seg_of(e):
    p = e.getparent()
    while p is not None:
        if ln(p) == "seg" and p.get(Q("id")): return p.get(Q("id"))
        p = p.getparent()
    return "-"

# conteggi normalizzazione (solo il figlio 'edito' di ogni choice)
stats = {b: {"n": 0, "resp": 0, "cert": 0} for b in ("reg", "corr", "expan")}
for ch in R.iter(T("choice")):
    for a, b in (("orig", "reg"), ("sic", "corr"), ("abbr", "expan")):
        ea = ch.find(T(a)); eb = ch.find(T(b))
        if ea is not None and eb is not None:
            st = stats[b]; st["n"] += 1
            if eb.get("resp"): st["resp"] += 1
            if eb.get("cert"): st["cert"] += 1

errors = []
# 1) attribuzione globale: reg/expan non devono portare @resp per-istanza
if stats["reg"]["resp"]:
    errors.append("%d `reg` con @resp (atteso 0: attribuzione globale in editorialDecl)" % stats["reg"]["resp"])
if stats["expan"]["resp"]:
    errors.append("%d `expan` con @resp (atteso 0: attribuzione globale in editorialDecl)" % stats["expan"]["resp"])
# 2) corr pienamente attribuito
if stats["corr"]["resp"] != stats["corr"]["n"]:
    errors.append("`corr`: %d/%d con @resp (attese tutte)" % (stats["corr"]["resp"], stats["corr"]["n"]))
if stats["corr"]["cert"] != stats["corr"]["n"]:
    errors.append("`corr`: %d/%d con @cert (attese tutte)" % (stats["corr"]["cert"], stats["corr"]["n"]))
# 3) supplied: @resp + @cert obbligatori (congettura)
for e in R.iter(T("supplied")):
    if not e.get("resp") or not e.get("cert"):
        errors.append("`supplied` senza @resp/@cert a c.%s (seg %s)" % (folio_of.get(e, "?"), seg_of(e)))
# 4) subst = add + del
for s in R.iter(T("subst")):
    if not s.findall(T("add")) or not s.findall(T("del")):
        errors.append("`subst` malformato a c.%s (manca add o del)" % folio_of.get(s, "?"))

if errors:
    print("::error::Guardia interventi editoriali: %d violazioni." % len(errors))
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print("Guardia interventi editoriali superata: reg/expan ad attribuzione globale, "
      "corr pienamente attribuito, %d supplied con @resp+@cert, subst ben formati."
      % sum(1 for _ in R.iter(T("supplied"))))
