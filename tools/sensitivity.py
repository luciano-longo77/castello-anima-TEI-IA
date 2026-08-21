#!/usr/bin/env python3
"""Analisi di sensibilità dell'indice d'impatto del «Castello dell'anima».

Verifica quanto le BANDE (#impact-low/medium/high/critical) resistono a perturbazioni
dei parametri scelti a tavolino: pesi AHP (F:N:A), valori-ancora (N/A), soglie di classe.
Legge le <fs> dello standOff impact-index dal teiText, ricalcola I sotto ogni scenario
dalle bande N_band/A_band/F (le scelte dell'annotatore), riassegna la classe e conta
quanti seg cambiano banda rispetto al baseline. Individua inoltre i seg "di frontiera"
(I entro un margine da una soglia), i più esposti a un cambio.

Uso:  python3 tools/sensitivity.py [tei/text/castello-anima-teiText.xml]
Solo lettura; non modifica il file. Dipendenza: lxml.
"""
import sys
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"
def T(t): return "{%s}%s" % (TEI, t)

# ---- modello baseline ---------------------------------------------------
N_ANCHOR = {"critica": 0.90, "alta": 0.75, "media": 0.55, "bassa": 0.30}
A_ANCHOR = {"alta": 0.85, "media": 0.675, "bassa": 0.40}
WEIGHTS  = (4.0, 2.0, 1.0)                 # F : N : A
THRESH   = (0.50, 0.66, 0.82)             # low<0.50<=medium<0.66<=high<0.82<=critical
BANDS    = ("low", "medium", "high", "critical")

def impact(F, nb, ab, w=WEIGHTS, na=N_ANCHOR, aa=A_ANCHOR):
    wf, wn, wa = w
    Fnorm = F / 3.0
    return (wf * Fnorm + wn * na[nb] + wa * aa[ab]) / (wf + wn + wa)

def band(I, th=THRESH):
    t0, t1, t2 = th
    return "low" if I < t0 else "medium" if I < t1 else "high" if I < t2 else "critical"

# ---- lettura fs ---------------------------------------------------------
def load(path):
    r = etree.parse(path).getroot()
    segs = []
    for fs in r.findall(".//" + T("standOff") + "[@type='impact-index']//" + T("fs")):
        d = {}
        for f in fs.findall(T("f")):
            sym = f.find(T("symbol")); num = f.find(T("numeric"))
            d[f.get("name")] = sym.get("value") if sym is not None else (num.get("value") if num is not None else None)
        segs.append({"id": (fs.get("corresp") or "").lstrip("#"),
                     "F": int(float(d["F"])), "nb": d["N_band"], "ab": d["A_band"]})
    return segs

# ---- scenari di perturbazione ------------------------------------------
def scenarios():
    sc = []
    # pesi alternativi (baseline 4:2:1)
    for w in [(3,2,1),(5,2,1),(4,3,1),(4,1,1),(4,2,2),(1,1,1),(3,2,2)]:
        sc.append(("pesi F:N:A = %d:%d:%d" % w, dict(w=tuple(map(float, w)))))
    # ancore: shift globale +/- delta
    for d in (0.05, -0.05, 0.10, -0.10):
        na = {k: max(0.0, min(1.0, v + d)) for k, v in N_ANCHOR.items()}
        aa = {k: max(0.0, min(1.0, v + d)) for k, v in A_ANCHOR.items()}
        sc.append(("ancore N,A shift %+0.2f" % d, dict(na=na, aa=aa)))
    # soglie: shift globale +/- delta
    for d in (0.02, -0.02, 0.03, -0.03):
        th = tuple(round(t + d, 3) for t in THRESH)
        sc.append(("soglie shift %+0.2f" % d, dict(th=th)))
    return sc

def run(path):
    segs = load(path)
    n = len(segs)
    base = [band(impact(s["F"], s["nb"], s["ab"])) for s in segs]
    from collections import Counter
    print("=== SENSIBILITA' INDICE D'IMPATTO ===")
    print("file: %s | seg: %d" % (path, n))
    print("baseline bande:", dict(Counter(base)))
    print()
    print("%-28s %8s  %s" % ("scenario", "cambi", "% seg"))
    print("-" * 55)
    worst = 0
    for name, kw in scenarios():
        w  = kw.get("w",  WEIGHTS)
        na = kw.get("na", N_ANCHOR)
        aa = kw.get("aa", A_ANCHOR)
        th = kw.get("th", THRESH)
        changed = 0
        for s, b0 in zip(segs, base):
            b1 = band(impact(s["F"], s["nb"], s["ab"], w=w, na=na, aa=aa), th=th)
            if b1 != b0:
                changed += 1
        worst = max(worst, changed)
        print("%-28s %8d  %5.1f%%" % (name, changed, 100.0 * changed / n))
    print("-" * 55)
    print("cambio massimo su tutti gli scenari: %d/%d (%.1f%%)" % (worst, n, 100.0 * worst / n))
    print()
    # frontiera: distanza dalla soglia piu' vicina (baseline)
    edges = THRESH
    frontier = []
    for s in segs:
        I = impact(s["F"], s["nb"], s["ab"])
        dmin = min(abs(I - e) for e in edges)
        frontier.append((dmin, s["id"], I, band(I)))
    frontier.sort()
    near = [f for f in frontier if f[0] <= 0.02]
    print("seg 'di frontiera' (|I - soglia| <= 0.02): %d" % len(near))
    for dmin, sid, I, b in near[:20]:
        print("   d=%.3f  I=%.3f  %-8s  %s" % (dmin, I, b, sid))

if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml")
