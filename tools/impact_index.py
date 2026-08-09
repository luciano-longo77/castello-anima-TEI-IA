#!/usr/bin/env python3
"""
Indice d'impatto TEI+IA — calcolo deterministico e audit su documento intero.
Progetto: castello-anima-TEI-IA.

USO
  python3 impact_index.py TEIFILE [--bands bands.csv] [--rng schema.rng] [--sch rules.sch]

MODALITA'
  audit   (default): legge le <fs> gia' presenti nel file, RI-mappa i decimali
          di N e A alle bande della griglia, RICALCOLA I con i valori-ancora,
          e confronta la banda risultante con l'impact-* dichiarato in @ana.
          Serve a verificare se il metodo a bande riproduce le classi del file.
  authoring (--bands): usa una tabella  id;banda_N;banda_A  fornita dall'umano
          e genera I + banda + blocco <fs> da zero.

VALIDAZIONE (sempre)
  - F derivabile da @ana #operation-*
  - ogni <fs>@corresp punta a un <seg> esistente
  - ogni <seg> con #impact-* ha una <fs> che lo referenzia
  - ogni @target / @corresp / <link>@target risolve a un xml:id esistente
  - coerenza banda dichiarata vs ricalcolata
  - opz.: RelaxNG (--rng) e Schematron (--sch) via lxml
"""
import sys, csv, argparse
from lxml import etree

# ---------- GRIGLIA (dichiarata una volta) ----------
F_BY_OPERATION = {"delimitazione": 1, "attenuatio": 2, "precisatio": 2,
                  "riequilibrio": 2, "declaratio": 3}
N_ANCHOR = {"critica": 0.90, "alta": 0.75, "media": 0.55, "bassa": 0.30}
A_ANCHOR = {"alta": 0.85, "media": 0.675, "bassa": 0.40}
WF, WN, WA = 4, 2, 1; WSUM = WF + WN + WA

def n_band_of(x):   # decimale -> banda N
    return "critica" if x >= 0.85 else "alta" if x >= 0.65 else "media" if x >= 0.45 else "bassa"
def a_band_of(x):   # decimale -> banda A
    return "alta" if x >= 0.80 else "media" if x >= 0.55 else "bassa"
def impact_band(I):
    return "impact-low" if I < 0.50 else "impact-medium" if I < 0.66 else "impact-high" if I < 0.82 else "impact-critical"

def compute(F, n_band, a_band):
    Fnorm = F/3; N = N_ANCHOR[n_band]; A = A_ANCHOR[a_band]
    I = (WF*Fnorm + WN*N + WA*A)/WSUM
    return dict(F=F, Fnorm=round(Fnorm,3), N=N, A=A, I=round(I,3), impact=impact_band(I))

# ---------- parsing tollerante ai namespace ----------
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
def ln(el): return etree.QName(el).localname
def local_iter(root, name): return (e for e in root.iter() if isinstance(e.tag,str) and ln(e)==name)

def ana_tokens(el):
    return [t.lstrip("#") for t in (el.get("ana") or "").split()]
def operation_of(el):
    for t in ana_tokens(el):
        if t.startswith("operation-"): return t[len("operation-"):]
    return None
def impact_of(el):
    for t in ana_tokens(el):
        if t.startswith("impact-"): return t
    return None

def load(path):
    return etree.parse(path, etree.XMLParser(recover=True, remove_blank_text=False))

def collect(tree):
    root = tree.getroot()
    segs, fss, ids = {}, {}, set()
    for e in root.iter():
        if not isinstance(e.tag, str): continue
        i = e.get(XMLID)
        if i: ids.add(i)
    for s in local_iter(root, "seg"):
        i = s.get(XMLID)
        if i: segs[i] = dict(id=i, operation=operation_of(s), impact=impact_of(s))
    for fs in local_iter(root, "fs"):
        vals = {}
        for f in local_iter(fs, "f"):
            nm = f.get("name")
            num = next(local_iter(f, "numeric"), None)
            if nm and num is not None:
                try: vals[nm] = float(num.get("value"))
                except (TypeError, ValueError): pass
        fss[fs.get(XMLID)] = dict(id=fs.get(XMLID), corresp=(fs.get("corresp") or "").lstrip("#"), vals=vals)
    return root, segs, fss, ids

# ---------- validazione puntatori ----------
def check_pointers(root, segs, fss, ids):
    prob = []
    for fid, fs in fss.items():
        if fs["corresp"] and fs["corresp"] not in ids:
            prob.append(f"<fs {fid}> @corresp -> #{fs['corresp']} INESISTENTE")
    fs_targets = {fs["corresp"] for fs in fss.values() if fs["corresp"]}
    for sid, s in segs.items():
        if s["impact"] and sid not in fs_targets:
            prob.append(f"<seg {sid}> ha {s['impact']} ma nessuna <fs> lo referenzia via @corresp")
    for e in root.iter():
        if not isinstance(e.tag, str): continue
        for attr in ("target", "corresp"):
            v = e.get(attr)
            if not v: continue
            for ref in v.split():
                r = ref.lstrip("#")
                if ref.startswith("#") and r not in ids:
                    prob.append(f"<{ln(e)}> @{attr} -> {ref} INESISTENTE")
    return prob

def run_schema(tree, rng, sch):
    out = []
    if rng:
        try:
            rl = etree.RelaxNG(etree.parse(rng))
            out.append(("RelaxNG", rl.validate(tree), rl.error_log))
        except Exception as ex: out.append(("RelaxNG", None, str(ex)))
    if sch:
        try:
            from lxml.isoschematron import Schematron
            sc = Schematron(etree.parse(sch), error_finder=Schematron.ASSERTS_AND_REPORTS)
            out.append(("Schematron", sc.validate(tree), sc.error_log))
        except Exception as ex: out.append(("Schematron", None, str(ex)))
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("teifile")
    ap.add_argument("--bands"); ap.add_argument("--rng"); ap.add_argument("--sch")
    a = ap.parse_args()
    tree = load(a.teifile); root, segs, fss, ids = collect(tree)
    print(f"# File: {a.teifile}")
    print(f"# segmenti: {len(segs)} | feature-structure <fs>: {len(fss)} | xml:id totali: {len(ids)}\n")

    bands = {}
    if a.bands:
        with open(a.bands) as fh:
            for row in csv.reader(fh, delimiter=";"):
                if len(row) >= 3 and not row[0].startswith("#"):
                    bands[row[0].strip()] = (row[1].strip().lower(), row[2].strip().lower())

    print(f"{'segmento':28s} {'op':13s} {'F':>1} {'Nb':7s} {'Ab':6s} {'I':>6} {'calcolato':15s} {'dichiarato':15s} esito")
    print("-"*110)
    mism = 0
    for sid, s in sorted(segs.items()):
        op = s["operation"]; F = F_BY_OPERATION.get(op)
        if F is None:
            print(f"{sid:28s} {str(op):13s}  ?  ----  ----   ----   (F non derivabile)"); continue
        if a.bands:
            if sid not in bands: continue
            nb, ab = bands[sid]
        else:
            fs = next((f for f in fss.values() if f["corresp"] == sid), None)
            if not fs or "N" not in fs["vals"] or "A" not in fs["vals"]:
                print(f"{sid:28s} {op:13s} {F} (nessuna <fs> N/A: salto)"); continue
            nb, ab = n_band_of(fs["vals"]["N"]), a_band_of(fs["vals"]["A"])
        r = compute(F, nb, ab)
        decl = s["impact"] or "(assente)"
        ok = (decl == r["impact"])
        if not ok: mism += 1
        print(f"{sid:28s} {op:13s} {F} {nb:7s} {ab:6s} {r['I']:6.3f} {r['impact']:15s} {decl:15s} {'OK' if ok else 'DIVERGE'}")

    print("\n## Validazione puntatori")
    prob = check_pointers(root, segs, fss, ids)
    print("  nessun problema" if not prob else "\n".join("  - "+p for p in prob))
    print(f"\n## Coerenza bande: {len(segs)-mism} OK, {mism} divergenti (classe ai bordi -> il decimale contava)")

    for name, res, log in run_schema(tree, a.rng, a.sch):
        print(f"\n## {name}: {'VALIDO' if res else 'NON valido' if res is not None else 'errore'}")
        if not res and log: print("   " + str(log)[:500])

if __name__ == "__main__":
    main()
