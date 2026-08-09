#!/usr/bin/env python3
"""
Guardia di co-occorrenza @ana (E3) - invarianti sulle combinazioni di assi nel testo.

Per ogni <seg> con @ana verifica:
  1. esattamente 1 token #impact-*
  2. esattamente 1 token #operation-*
  3. esattamente 1 fase base (#phase-introduction | #phase-mediana | #phase-conclusive)
  4. #phase-critical, se presente, deve co-occorrere con una fase base

Fallisce (exit 1) elencando i segmenti che violano le invarianti.
Uso:  python3 cooccurrence_guard.py [TEXT_XML]
"""
import sys
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
BASE_PHASE = {"phase-introduction", "phase-mediana", "phase-conclusive"}
TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"

doc = etree.parse(TEXT)
errors = []
n = 0
for seg in doc.iterfind(".//t:seg", NS):
    ana = seg.get("ana")
    if not ana:
        continue
    n += 1
    sid = seg.get(XMLID) or f"(riga {seg.sourceline})"
    toks = [x[1:] for x in ana.split() if x.startswith("#")]
    n_imp = sum(1 for x in toks if x.startswith("impact-"))
    n_op = sum(1 for x in toks if x.startswith("operation-"))
    n_bp = sum(1 for x in toks if x in BASE_PHASE)
    if n_imp != 1:
        errors.append(f"{sid}: {n_imp} token #impact-* (atteso 1)")
    if n_op != 1:
        errors.append(f"{sid}: {n_op} token #operation-* (atteso 1)")
    if n_bp != 1:
        errors.append(f"{sid}: {n_bp} fasi base (atteso 1)")
    if "phase-critical" in toks and n_bp < 1:
        errors.append(f"{sid}: #phase-critical senza una fase base")

if errors:
    print(f"::error::Guardia co-occorrenza: {len(errors)} violazioni su {n} seg.")
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print(f"Guardia co-occorrenza superata: {n} seg, tutte le invarianti rispettate "
      "(1 impact, 1 operation, 1 fase base; phase-critical sempre con base).")
