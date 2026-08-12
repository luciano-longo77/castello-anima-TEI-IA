#!/usr/bin/env python3
"""
Estrattore degli interventi editoriali sul teiText del *Castello dell'anima*.

Distingue due PIANI e li rendiconta separatamente:

  - NORMALIZZAZIONE (piano diplomatico-editoriale): le scelte in <choice>
      orig/reg (regolarizzazione grafica), sic/corr (correzione), abbr/expan (scioglimento).
      Attribuzione: reg/expan = globale (editorialDecl, nessun @resp per-istanza);
                    corr = per-istanza (@resp + @cert).

  - GENETICO (lavoro dell'autrice/materialita sul foglio): add, del, subst, retrace,
      restore, gap, supplied, metamark. Qui contano @hand, @place, @type, @rend, @cert.

Per ogni intervento riporta la carta (<pb n>), il <seg> contenitore e lo stato di
attribuzione, cosi da poter controllare a colpo d'occhio la coerenza dei criteri.

Uso:
    python3 estrattore_interventi.py [teiText.xml] [--csv interventi.csv]

Senza --csv stampa solo i prospetti riassuntivi; con --csv scrive anche il dettaglio
per-istanza (una riga per intervento).
"""
import sys, csv
from collections import Counter, defaultdict
from lxml import etree

T = "{http://www.tei-c.org/ns/1.0}"
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
def ln(e): return e.tag.split("}")[-1] if isinstance(e.tag, str) else "?"

PATH = "tei/text/castello-anima-teiText.xml"
CSV = None
args = sys.argv[1:]
if "--csv" in args:
    i = args.index("--csv"); CSV = args[i+1]; del args[i:i+2]
if args: PATH = args[0]

doc = etree.parse(PATH); R = doc.getroot()

# --- contesto: per ogni elemento, carta corrente (ultimo pb in ordine di documento) e seg contenitore ---
folio_of = {}
cur = "?"
for e in R.iter():
    if ln(e) == "pb":
        cur = e.get("n") or "?"
    folio_of[e] = cur

def enclosing_seg(e):
    p = e.getparent()
    while p is not None:
        if ln(p) == "seg" and p.get(XMLID):
            return p.get(XMLID)
        p = p.getparent()
    return "-"

# ============ PIANO 1 · NORMALIZZAZIONE (choice) ============
NORM_PAIRS = [("orig","reg","regolarizzazione grafica"),
              ("sic","corr","correzione di errore materiale"),
              ("abbr","expan","scioglimento di abbreviazione")]
norm_rows = []   # (piano, coppia, folio, seg, orig_txt, edito_txt, resp, cert)
norm_stats = defaultdict(lambda: {"n":0,"resp":0,"cert":0})
for ch in R.iter(T+"choice"):
    for a, b, desc in NORM_PAIRS:
        ea = ch.find(T+a); eb = ch.find(T+b)
        if ea is not None and eb is not None:
            st = norm_stats[b]; st["n"] += 1
            if eb.get("resp"): st["resp"] += 1
            if eb.get("cert"): st["cert"] += 1
            norm_rows.append(("NORM", f"{a}/{b}", folio_of.get(ch,"?"), enclosing_seg(ch),
                              (ea.text or "").strip(), (eb.text or "").strip(),
                              eb.get("resp") or "", eb.get("cert") or ""))

# ============ PIANO 2 · GENETICO ============
GEN_TAGS = ["add","del","subst","retrace","restore","gap","supplied","metamark"]
gen_rows = []
gen_stats = defaultdict(Counter)
for tag in GEN_TAGS:
    for e in R.iter(T+tag):
        typ = e.get("type") or ""; place = e.get("place") or ""; rend = e.get("rend") or ""
        hand = e.get("hand") or ""; cert = e.get("cert") or ""; reason = e.get("reason") or ""
        gen_stats[tag]["n"] += 1
        if hand: gen_stats[tag]["hand"] += 1
        if cert: gen_stats[tag]["cert"] += 1
        gen_rows.append(("GEN", tag, folio_of.get(e,"?"), enclosing_seg(e),
                         typ, place or rend or reason, hand, cert,
                         (e.text or "").strip()[:40]))

# ============ PROSPETTI ============
print("="*72)
print("PIANO 1 · NORMALIZZAZIONE (choice)  —  attribuzione: reg/expan globale, corr per-istanza")
print("="*72)
print(f"{'coppia':14}{'n':>5}{'@resp':>8}{'@cert':>8}   nota")
NOTE = {"reg":"attribuzione globale (editorialDecl): @resp atteso 0",
        "corr":"per-istanza: @resp e @cert attesi = n",
        "expan":"attribuzione globale; @cert solo dove pertinente"}
for a,b,desc in NORM_PAIRS:
    s = norm_stats[b]
    print(f"{a+'/'+b:14}{s['n']:>5}{s['resp']:>8}{s['cert']:>8}   {NOTE.get(b,'')}")

print()
print("="*72)
print("PIANO 2 · GENETICO (lavoro sul foglio)")
print("="*72)
print(f"{'elemento':10}{'n':>5}{'@hand':>8}{'@cert':>8}")
for tag in GEN_TAGS:
    s = gen_stats[tag]
    if s["n"]:
        print(f"{tag:10}{s['n']:>5}{s['hand']:>8}{s['cert']:>8}")

# dettaglio valori dei tipi genetici
print("\n--- dettaglio valori (piano genetico) ---")
def vals(tag, attr):
    c = Counter()
    for e in R.iter(T+tag):
        v = e.get(attr)
        if v:
            for t in v.split(): c[t]+=1
    return dict(c)
for tag,attr in [("del","type"),("del","rend"),("del","place"),("add","type"),
                 ("add","place"),("gap","reason"),("gap","unit"),
                 ("supplied","reason"),("supplied","unit"),("retrace","hand"),("retrace","cert")]:
    d = vals(tag,attr)
    if d: print(f"  {tag}/@{attr}: {d}")

# ============ CONTROLLI DI COERENZA ============
print("\n" + "="*72)
print("CONTROLLI DI COERENZA")
print("="*72)
issues = []
# reg/expan non devono portare @resp (attribuzione globale)
if norm_stats["reg"]["resp"]: issues.append(f"{norm_stats['reg']['resp']} reg con @resp (atteso 0: attribuzione globale)")
if norm_stats["expan"]["resp"]: issues.append(f"{norm_stats['expan']['resp']} expan con @resp (atteso 0: attribuzione globale)")
# corr deve essere pienamente attribuito
if norm_stats["corr"]["resp"] != norm_stats["corr"]["n"]: issues.append("corr non tutte con @resp")
if norm_stats["corr"]["cert"] != norm_stats["corr"]["n"]: issues.append("corr non tutte con @cert")
# supplied: congettura -> @resp e @cert obbligatori (regola guida 2.2.4)
for e in R.iter(T+"supplied"):
    if not e.get("resp") or not e.get("cert"):
        issues.append(f"supplied senza @resp/@cert a c.{folio_of.get(e,'?')} (seg {enclosing_seg(e)})")
# subst = add + del
for s in R.iter(T+"subst"):
    if not s.findall(T+"add") or not s.findall(T+"del"):
        issues.append(f"subst malformato a c.{folio_of.get(s,'?')}")
if issues:
    print(f"  {len(issues)} rilievi:")
    for x in issues[:40]: print("   -", x)
else:
    print("  Nessun rilievo: i due piani sono coerenti con la policy dichiarata.")

# ============ CSV opzionale ============
if CSV:
    with open(CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["piano","elemento/coppia","carta","seg","tipo/orig","place|rend|reason|edito","hand","cert","testo"])
        for r in norm_rows:
            w.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], ""])
        for r in gen_rows:
            w.writerow([r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8]])
    print(f"\nCSV dettaglio per-istanza scritto in: {CSV} "
          f"({len(norm_rows)+len(gen_rows)} righe)")
