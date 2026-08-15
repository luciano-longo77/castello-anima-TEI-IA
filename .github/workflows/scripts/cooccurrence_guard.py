#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia di co-occorrenza @ana (E3) - cardinalita' degli assi interpretativi sul <seg>.

Controllo SEMANTICO (per categoria della tassonomia, non per prefisso): ogni token @ana
e' ricondotto al suo asse leggendo tassonomia-gh.xml (taxonomy xml:id="func"|"risk"|...).

Per ogni <seg> con @ana verifica le cardinalita' del modello (confermate sul corpus):
  impact        == 1
  operation     == 1
  risk          == 1
  exposition    == 1
  func          >= 1     (un passo puo' svolgere piu' funzioni retoriche: decisione editoriale)
  mystic_state  <= 1     (opzionale su segmenti di sola cornice/etica: decisione editoriale)
  fase base     == 1     (#phase-introduction | #phase-mediana | #phase-conclusive)
  phase-critical<= 1     e solo insieme a una fase base (modificatore, non asse)
  relation       0..n    (nessun vincolo di conteggio)

Fail-closed: segnala anche i token @ana privi di '#' e quelli non classificati in alcun
asse della tassonomia (cosi' la guardia e' sicura anche eseguita da sola). e2_guard.py resta
il controllo AUTORITATIVO della forma '#id' e della referenzialita' del token; qui il focus
e' la CARDINALITA' e l'assegnazione dell'asse.

Uso:  python3 cooccurrence_guard.py [TEXT_XML] [TAXONOMY_XML]
default: tei/text/castello-anima-teiText.xml  tei/taxonomy/tassonomia-gh.xml
"""
import sys
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
T = "{http://www.tei-c.org/ns/1.0}"
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
BASE_PHASE = {"phase-introduction", "phase-mediana", "phase-conclusive"}

TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"
TAX  = sys.argv[2] if len(sys.argv) > 2 else "tei/taxonomy/tassonomia-gh.xml"

# categoria -> asse (dalla tassonomia). Solo gli assi interpretativi dell'@ana del seg.
INTERP_AXES = {"func", "operation", "risk", "exposition", "phase", "mystic_state", "relation", "impact"}
try:
    tax_doc = etree.parse(TAX)
    doc = etree.parse(TEXT)
except (OSError, etree.XMLSyntaxError) as exc:
    print(f"::error::Input non leggibile: {exc}")
    sys.exit(2)

cat2axis = {}
for tx in tax_doc.iter(T + "taxonomy"):
    ax = tx.get(XMLID)
    if ax not in INTERP_AXES:
        continue
    for c in tx.iter(T + "category"):
        if c.get(XMLID):
            cat2axis[c.get(XMLID)] = ax
errors = []
n = 0
for seg in doc.iterfind(".//t:seg", NS):
    ana = seg.get("ana")
    if not ana:
        continue
    n += 1
    sid = seg.get(XMLID) or f"(riga {seg.sourceline})"
    per = {ax: 0 for ax in INTERP_AXES}
    n_base = n_crit = 0
    for raw in ana.split():
        if not raw.startswith("#"):
            errors.append(f"{sid}: token @ana privo del prefisso '#': {raw!r}")
            continue
        tid = raw[1:]
        # token speciali dell'asse phase: conteggiati a parte come fase-base vs modificatore,
        # non come valore-asse generico. (phase-critical E' comunque una categoria dell'asse
        # phase in tassonomia; lo trattiamo esplicitamente per chiarezza e per restare robusti
        # a una futura ristrutturazione della tassonomia.)
        if tid in BASE_PHASE:
            n_base += 1
            continue
        if tid == "phase-critical":
            n_crit += 1
            continue
        ax = cat2axis.get(tid)
        if ax is None:
            errors.append(f"{sid}: token #{tid} non classificato in alcun asse della tassonomia")
            continue
        per[ax] += 1

    # cardinalita' a valore fisso
    for ax in ("impact", "operation", "risk", "exposition"):
        if per[ax] != 1:
            errors.append(f"{sid}: {per[ax]} token dell'asse {ax} (atteso 1)")
    # func: almeno 1
    if per["func"] < 1:
        errors.append(f"{sid}: 0 token dell'asse func (atteso >= 1)")
    # mystic_state: al piu' 1
    if per["mystic_state"] > 1:
        errors.append(f"{sid}: {per['mystic_state']} token mystic_state (atteso <= 1)")
    # fase base: esattamente 1
    if n_base != 1:
        errors.append(f"{sid}: {n_base} fasi base (atteso 1)")
    # phase-critical: al piu' 1 e con una fase base
    if n_crit > 1:
        errors.append(f"{sid}: {n_crit} #phase-critical (atteso <= 1)")
    if n_crit and n_base < 1:
        errors.append(f"{sid}: #phase-critical senza una fase base")

if errors:
    print(f"::error::Guardia co-occorrenza: {len(errors)} violazioni su {n} seg.")
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print(f"Guardia co-occorrenza superata: {n} seg, cardinalita' rispettate "
      "(impact/operation/risk/exposition=1, func>=1, mystic_state<=1, 1 fase base, "
      "phase-critical<=1 con base; relation 0..n).")
