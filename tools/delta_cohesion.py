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
  python3 tools/delta_cohesion.py TEIXML SEGID [SEGID ...]        # tabella leggibile
  python3 tools/delta_cohesion.py TEIXML --detail SEGID           # + dettaglio catene
  python3 tools/delta_cohesion.py TEIXML --pilot FILE.tsv         # loci letti da file
  python3 tools/delta_cohesion.py TEIXML --pilot FILE.tsv --tsv   # uscita TSV (artefatto)

--pilot FILE.tsv : file TSV con colonna 1 = locus_id, colonna 2 (opzionale) = operazione;
                   righe vuote e righe che iniziano con '#' sono ignorate; una riga di
                   intestazione 'locus_id...' è saltata automaticamente.
--tsv            : stampa una riga d'intestazione + una riga TSV per locus (rigenerabile,
                   da redirigere in logs/D2-pilot.tsv).

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

def load_pilot(path):
    """Legge un TSV di loci: ritorna lista di (locus_id, operation)."""
    out = []
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        cols = line.split("\t")
        cid = cols[0].strip()
        if not cid or cid.lower() == "locus_id":   # salta intestazione
            continue
        op = cols[1].strip() if len(cols) > 1 else "-"
        out.append((cid, op))
    return out

def analyze(chains, seg):
    touched = [c for c in chains if seg in c[2]]
    broken = [c for c in touched if len([m for m in c[2] if m != seg]) < 2]
    shortened = [c for c in touched if len([m for m in c[2] if m != seg]) >= 2]
    neighbors = defaultdict(int)
    for c in touched:
        for m in c[2]:
            if m != seg:
                neighbors[m] += 1
    degree = len(neighbors)
    delta_connectivity = sum(neighbors.values())
    isolated = 0
    for nb in neighbors:
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

TSV_COLS = ["locus_id", "operation", "chains_touched", "chains_broken",
            "chains_shortened", "degree", "neighbors_isolated", "delta_connectivity"]

def main(argv):
    if len(argv) < 3:
        print(__doc__); return 2
    path = argv[1]
    detail = "--detail" in argv
    tsv = "--tsv" in argv
    # loci: da --pilot FILE oppure posizionali
    loci = []  # (id, op)
    if "--pilot" in argv:
        i = argv.index("--pilot")
        if i + 1 >= len(argv):
            print("errore: --pilot richiede un file", file=sys.stderr); return 2
        loci = load_pilot(argv[i + 1])
    pos = [a for a in argv[2:] if not a.startswith("--")]
    # gli id posizionali (escluso l'argomento di --pilot) si aggiungono con op '-'
    if "--pilot" in argv:
        pos = [a for a in pos if a != argv[argv.index("--pilot") + 1]]
    loci += [(a, "-") for a in pos]
    if not loci:
        print("errore: nessun locus (usa SEGID posizionali o --pilot FILE)", file=sys.stderr); return 2

    chains = load_chains(path)
    if not chains:
        print("Nessuna catena trovata nello standOff semantic-chains.", file=sys.stderr); return 1

    if tsv:
        print("\t".join(TSV_COLS))
        for cid, op in loci:
            r = analyze(chains, cid)
            print("\t".join(str(x) for x in [cid, op, r["chains_touched"], r["chains_broken"],
                  r["chains_shortened"], r["degree"], r["neighbors_isolated"], r["delta_connectivity"]]))
        return 0

    # modalità leggibile
    print("# grafo catene: %d catene, %d seg distinti coinvolti" %
          (len(chains), len({m for _, _, ms in chains for m in ms})))
    print("%-34s %-10s %5s %6s %5s %6s %5s %6s" %
          ("seg", "operation", "touch", "broken", "short", "degree", "isol", "Δconn"))
    print("-" * 84)
    for cid, op in loci:
        r = analyze(chains, cid)
        print("%-34s %-10s %5d %6d %5d %6d %5d %6d" % (
            cid, op, r["chains_touched"], r["chains_broken"], r["chains_shortened"],
            r["degree"], r["neighbors_isolated"], r["delta_connectivity"]))
        if detail:
            for typ, sub, ms in r["_touched"]:
                mark = "SPEZZA" if (typ, sub, ms) in r["_broken"] else "accorcia"
                print("      [%-8s] %-28s (%d→%d membri)" % (mark, sub, len(ms), len(ms) - 1))
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
