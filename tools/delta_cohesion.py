#!/usr/bin/env python3
"""delta_cohesion.py — misura strutturale della coesione (D2) del «Castello dell'anima».

Dato un <seg>, misura quanto la rete di catene semantiche (standOff `semantic-chains`)
si degrada rimuovendolo: è la componente **deterministica** della prova sperimentale
(nessun LLM, nessun giudizio — pura topologia sul grafo già esistente).

Modello del grafo:
  - ogni <linkGrp>/<link @target="#a #b …"> è una CATENA (tema/stato/metafora/allegoria);
  - i <seg> elencati nel @target sono i suoi MEMBRI;
  - due seg sono ADIACENTI se condividono almeno una catena (co-membership).

Micro-scelta dichiarata (nodo T4):
  - catena «SPEZZATA»  = rimuovendo il seg scende **sotto 2 membri** (un <link> con <2 target
    non è più una relazione: il capo si perde);
  - catena «ACCORCIATA» = resta **>=2 membri** ma perde questo seg.

Metriche restituite per seg:
  - chains_touched   : catene di cui il seg è membro
  - chains_broken    : catene che scendono sotto 2 membri (spezzate)
  - chains_shortened : catene che restano >=2 ma perdono il seg
  - members_lost     : somma dei legami-membro persi (= chains_touched)
  - degree           : n. di seg DISTINTI co-incatenati (vicini nel grafo)
  - neighbors_isolated : vicini che, tolto il seg, perdono OGNI catena in comune con esso
  - delta_connectivity : archi di co-membership rimossi dal grafo togliendo il seg

Uso:
  python3 tools/delta_cohesion.py tei/text/castello-anima-teiText.xml SEGID [SEGID ...]
  python3 tools/delta_cohesion.py tei/text/castello-anima-teiText.xml --detail SEGID
Solo lettura; non modifica il file. Dipendenza: solo stdlib.
"""
import sys, re
from collections import defaultdict

def load_chains(path):
    """Ritorna lista di catene: (type, subtype, [segid,...])."""
    t = open(path, encoding="utf-8").read()
    m = re.search(r'<standOff type="semantic-chains">(.*?)</standOff>', t, re.S)
    if not m:
        return []
    body = m.group(1)
    chains = []
    for lg in re.finditer(r'<linkGrp\b[^>]*?type="([^"]*)"[^>]*?subtype="([^"]*)"[^>]*?>(.*?)</linkGrp>', body, re.S):
        typ, sub, inner = lg.group(1), lg.group(2), lg.group(3)
        for lk in re.finditer(r'<link\b[^>]*target="([^"]*)"', inner):
            members = [x.lstrip('#') for x in lk.group(1).split() if x.strip().startswith('#')]
            chains.append((typ, sub, members))
    return chains

def analyze(chains, seg):
    touched = [c for c in chains if seg in c[2]]
    broken = [c for c in touched if len([m for m in c[2] if m != seg]) < 2]
    shortened = [c for c in touched if len([m for m in c[2] if m != seg]) >= 2]
    # grafo di co-membership
    neighbors = defaultdict(int)   # vicino -> n. catene condivise col seg
    for c in touched:
        for m in c[2]:
            if m != seg:
                neighbors[m] += 1
    degree = len(neighbors)
    delta_connectivity = sum(neighbors.values())  # archi (seg--vicino) pesati per catene condivise
    # vicini che perdono OGNI legame col seg = tutti (per definizione, rimosso il seg);
    # ma "isolati" nel senso forte: vicini la cui UNICA catena era una che si spezza
    isolated = 0
    for nb, shared in neighbors.items():
        # catene condivise col seg che si spezzano vs che sopravvivono accorciate
        surviving = sum(1 for c in shortened if nb in c[2])
        if surviving == 0:
            isolated += 1
    return {
        "seg": seg,
        "chains_touched": len(touched),
        "chains_broken": len(broken),
        "chains_shortened": len(shortened),
        "members_lost": len(touched),
        "degree": degree,
        "neighbors_isolated": isolated,
        "delta_connectivity": delta_connectivity,
        "_touched": touched, "_broken": broken,
    }

def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    path = argv[1]
    detail = "--detail" in argv
    segs = [a for a in argv[2:] if not a.startswith("--")]
    chains = load_chains(path)
    if not chains:
        print("Nessuna catena trovata nello standOff semantic-chains."); return 1
    print("# grafo catene: %d catene, %d seg distinti coinvolti" %
          (len(chains), len({m for _,_,ms in chains for m in ms})))
    hdr = ("seg", "touch", "broken", "short", "degree", "isol", "Δconn")
    print("%-34s %5s %6s %5s %6s %5s %6s" % hdr)
    print("-" * 70)
    for seg in segs:
        r = analyze(chains, seg)
        print("%-34s %5d %6d %5d %6d %5d %6d" % (
            r["seg"], r["chains_touched"], r["chains_broken"], r["chains_shortened"],
            r["degree"], r["neighbors_isolated"], r["delta_connectivity"]))
        if detail:
            for typ, sub, ms in r["_touched"]:
                mark = "SPEZZA" if r["_broken"] and (typ, sub, ms) in r["_broken"] else "accorcia"
                print("      [%-8s] %-28s (%d→%d membri)" % (mark, sub, len(ms), len(ms)-1))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
