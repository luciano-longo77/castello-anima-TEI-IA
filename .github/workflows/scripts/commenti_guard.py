#!/usr/bin/env python3
"""
Guardia commenti-seg - impone procedura e grammatica dei commenti <!-- ... --> sopra i <seg>.

Per ogni <seg> con @ana verifica che lo preceda un commento nel formato canonico:

  <CODICE> <ETICHETTA>. <descrizione>. N=<banda>/<ancora>[(...)]; A=<banda>/<ancora>[(...)];
  F=<n> <operazione> -> I=<X.XXX> <classe>. [Genetico: ... | Norm: ...]

Controlla: presenza del commento; clausola N/A/F->I ben formata; bande valide e ancore
col decimale giusto (mai 'None'); F coerente con l'operazione; commento-I == fs-I e classe
== banda di I; keyword d'apparato ammesse (solo 'Genetico:' e 'Norm:'); codice iniziale presente.

Uso:  python3 commenti_guard.py [TEXT_XML]
"""
import sys, re
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
T = "{http://www.tei-c.org/ns/1.0}"
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"

NA = {"critica": 0.90, "alta": 0.75, "media": 0.55, "bassa": 0.30}
AA = {"alta": 0.85, "media": 0.675, "bassa": 0.40}
OPF = {"delimitazione": 1, "attenuatio": 2, "precisatio": 2, "riequilibrio": 2, "declaratio": 3}
def cls(I): return "low" if I < 0.50 else "medium" if I < 0.66 else "high" if I < 0.82 else "critical"
FORBIDDEN = ["Norm sost.:", "Graph.:", "Graf.:"]  # keyword d'apparato fuori standard

# clausola numerica canonica (i motivi tra parentesi sono facoltativi)
CLAUSE = re.compile(
    r"N=(?P<nb>critica|alta|media|bassa)/(?P<na>None|\d\.\d+)\s*(?:\([^)]*\))?\s*;\s*"
    r"A=(?P<ab>alta|media|bassa)/(?P<aa>None|\d\.\d+)\s*(?:\([^)]*\))?\s*;\s*"
    r"F=(?P<f>\d)\s+(?P<op>delimitazione|attenuatio|precisatio|riequilibrio|declaratio)"
    r"\s*(?:\([^)]*\))?\s*->\s*"
    r"I=(?P<I>\d\.\d+)\s+(?P<cl>low|medium|high|critical)")

# indice I dalle fs (per il confronto commento-I == fs-I)
doc = etree.parse(TEXT); R = doc.getroot()
fsI = {}
for f in R.iter(T + "fs"):
    sid = (f.get("corresp") or "").lstrip("#")
    for ff in f.findall(T + "f"):
        if ff.get("name") == "I":
            fsI[sid] = float(ff.find(T + "numeric").get("value"))

src = open(TEXT, encoding="utf-8").read()
# Per ogni <seg> associa il commento che lo precede (l'ultimo <!-- --> prima del tag,
# senza altri <seg> in mezzo): robusto anche quando fra commento e seg c'e' <argument>/<head>.
seg_matches = list(re.finditer(r'<seg\s+xml:id="([^"]+)"', src))
pairs, prev_end = [], 0
for m in seg_matches:
    window = src[prev_end:m.start()]
    coms = re.findall(r'<!--((?:(?!-->).)*?)-->', window, re.S)
    if coms:
        pairs.append((coms[-1], m.group(1)))
    prev_end = m.end()
commented = {sid for _, sid in pairs}

errors, warns = [], []
seg_ids = [s.get(XMLID) for s in R.iter(T + "seg") if s.get(XMLID) and s.get("ana")]

# 1) ogni seg (con @ana) ha un commento davanti
for sid in seg_ids:
    if sid not in commented:
        errors.append("%s: manca il commento sopra il <seg>" % sid)

for raw, sid in pairs:
    c = " ".join(raw.split())
    where = sid
    # 2) codice iniziale
    if not re.match(r"^[A-Z]+\d+[a-z]?\b", c):
        warns.append("%s: manca il CODICE iniziale (es. S1/C1)" % where)
    # 3) clausola numerica
    m = CLAUSE.search(c)
    if not m:
        errors.append("%s: clausola N/A/F->I assente o malformata" % where)
        continue
    nb, na, ab, aa = m["nb"], m["na"], m["ab"], m["aa"]
    Fv, op, I, cl = int(m["f"]), m["op"], float(m["I"]), m["cl"]
    # 4) ancore col decimale giusto (mai None)
    if na == "None" or abs(float(na) - NA[nb]) > 1e-9:
        errors.append("%s: ancora N errata (N=%s/%s, atteso %s)" % (where, nb, na, NA[nb]))
    if aa == "None" or abs(float(aa) - AA[ab]) > 1e-9:
        errors.append("%s: ancora A errata (A=%s/%s, atteso %s)" % (where, ab, aa, AA[ab]))
    # 5) F coerente con operazione
    if OPF[op] != Fv:
        errors.append("%s: F=%d incoerente con '%s' (atteso %d)" % (where, Fv, op, OPF[op]))
    # 6) classe == banda di I
    if cl != cls(I):
        errors.append("%s: classe '%s' != banda di I=%.3f (%s)" % (where, cl, I, cls(I)))
    # 7) commento-I == fs-I
    if sid in fsI and abs(I - fsI[sid]) > 0.0005:
        errors.append("%s: commento-I=%.3f != fs-I=%.3f" % (where, I, fsI[sid]))
    # 8) keyword d'apparato ammesse
    for kw in FORBIDDEN:
        if kw in raw:
            errors.append("%s: keyword d'apparato fuori standard '%s' (usare 'Norm:')" % (where, kw))

if warns:
    print("Avvisi (non bloccanti):")
    for w in warns[:50]:
        print("  -", w)
if errors:
    print("::error::Guardia commenti: %d violazioni." % len(errors))
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print("Guardia commenti superata: %d commenti conformi (clausola N/A/F->I, ancore, "
      "commento-I == fs-I, keyword ammesse)." % len(pairs))
