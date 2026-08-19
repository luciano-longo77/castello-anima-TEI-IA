#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera docs/interventi-editoriali.md da tei/text/castello-anima-teiText.xml.

Rendiconta gli interventi editoriali MARCATI: l'apparato sostanziale/genetico
(add, del, subst dentro app/rdg), le ritracciature (retrace) e le integrazioni
editoriali (gap, unclear, supplied, metamark). Nel modello interpretativo la
normalizzazione grafica e' SILENZIOSA e dichiarata una volta per tutte
(docs/criteri-trascrizione.md + editorialDecl): nel testo di lettura non
compaiono elementi diplomatici (choice: orig/reg, sic/corr, abbr/expan). Un
controllo segnala eventuali choice residui (attesi 0).

Emette prospetti, l'esito dei controlli di coerenza e un'appendice per-istanza
(una riga per intervento, con carta e seg) navigabile su GitHub.

Uso: python3 tools/estrattore_interventi.py [teiText.xml] [output.md]
Richiede lxml. Output deterministico (nessun timestamp): i diff sono puliti."""

import sys
from collections import Counter, defaultdict
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"; XML = "http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s" % (TEI, t)
def Q(a): return "{%s}%s" % (XML, a)
def ln(e): return e.tag.split("}")[-1] if isinstance(e.tag, str) else "?"

SRC = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"
OUT = sys.argv[2] if len(sys.argv) > 2 else "docs/interventi-editoriali.md"

PREAMBLE = (
"# Interventi editoriali: rendiconto verificabile\n"
"## Intertestualità sotto sorveglianza\n"
"### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*\n"
"[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) "
"[![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)]"
"(https://github.com/luciano-longo77/castello-anima-TEI-IA)\n\n"
"**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  \n"
"**Editor**: Luciano Longo  \n"
"**Licenza**: CC BY 4.0\n\n---\n\n"
"**Fonte**\n"
"*Generato da `tei/text/castello-anima-teiText.xml`. Fotografa ogni intervento editoriale "
"**marcato**: l'apparato sostanziale/genetico (`add`/`del`/`subst`, dentro `app`/`rdg`), le "
"ritracciature (`retrace`) e le integrazioni editoriali (`gap`/`unclear`/`supplied`). La "
"**normalizzazione grafica** è silenziosa e dichiarata una volta per tutte "
"(`docs/criteri-trascrizione.md` + `editorialDecl`): nel testo di lettura non compaiono "
"elementi diplomatici (`choice`). L'attribuzione delle integrazioni è per-istanza "
"(`supplied`: `@resp` + `@cert`).*\n\n---")

doc = etree.parse(SRC); R = doc.getroot()

# contesto: carta corrente e seg contenitore per ogni elemento
folio_of = {}; cur = "?"
for e in R.iter():
    if ln(e) == "pb": cur = e.get("n") or "?"
    folio_of[e] = cur
def enclosing_seg(e):
    p = e.getparent()
    while p is not None:
        if ln(p) == "seg" and p.get(Q("id")): return p.get(Q("id"))
        p = p.getparent()
    return "-"

# ---- APPARATO GENETICO / SOSTANZIALE + INTEGRAZIONI ----
GEN_TAGS = ["add", "del", "subst", "retrace", "restore", "gap", "unclear", "supplied", "metamark"]
gen_rows = []; gen_stats = defaultdict(Counter)
for tag in GEN_TAGS:
    for e in R.iter(T(tag)):
        hand = e.get("hand") or ""; cert = e.get("cert") or ""
        info = e.get("type") or e.get("place") or e.get("rend") or e.get("reason") or ""
        gen_stats[tag]["n"] += 1
        if hand: gen_stats[tag]["hand"] += 1
        if cert: gen_stats[tag]["cert"] += 1
        gen_rows.append((tag, folio_of.get(e, "?"), enclosing_seg(e), info, hand, cert,
                         (e.text or "").strip()[:40]))

def vals(tag, attr):
    c = Counter()
    for e in R.iter(T(tag)):
        v = e.get(attr)
        if v:
            for t in v.split(): c[t] += 1
    return c

# ---- CONTROLLI DI COERENZA ----
issues = []
nchoice = sum(1 for _ in R.iter(T("choice")))
if nchoice:
    issues.append("%d `choice` presenti (attese 0 nel modello interpretativo: "
                  "la normalizzazione grafica e' silenziosa e dichiarata)" % nchoice)
for e in R.iter(T("supplied")):
    if not e.get("resp") or not e.get("cert"):
        issues.append("`supplied` senza `@resp`/`@cert` a c.%s (seg %s)" %
                      (folio_of.get(e, "?"), enclosing_seg(e)))
for s in R.iter(T("subst")):
    if not s.findall(T("add")) or not s.findall(T("del")):
        issues.append("`subst` malformato a c.%s (manca add o del)" % folio_of.get(s, "?"))

# ============ EMISSIONE MARKDOWN ============
o = [PREAMBLE, ""]

o.append("## 1. Apparato genetico e integrazioni\n")
o.append("| elemento | n | con `@hand` | con `@cert` |")
o.append("|---|---:|---:|---:|")
for tag in GEN_TAGS:
    s = gen_stats[tag]
    if s["n"]:
        o.append("| `%s` | %d | %d | %d |" % (tag, s["n"], s["hand"], s["cert"]))
o.append("")
o.append("### 1.1 Dettaglio dei valori\n")
o.append("| attributo | valori (conteggio) |")
o.append("|---|---|")
for tag, attr in [("del", "type"), ("del", "rend"), ("del", "place"), ("add", "type"),
                  ("add", "place"), ("gap", "reason"), ("gap", "unit"),
                  ("supplied", "reason"), ("retrace", "hand"), ("retrace", "cert")]:
    c = vals(tag, attr)
    if c:
        cell = " · ".join("`%s` (%d)" % (k, c[k]) for k in sorted(c))
        o.append("| `%s/@%s` | %s |" % (tag, attr, cell))
o.append("")

o.append("## 2. Controlli di coerenza\n")
if issues:
    o.append("**Rilievi: %d.**\n" % len(issues))
    for x in issues:
        o.append("- %s" % x)
else:
    o.append("**Nessun rilievo.** Coerente con la policy dichiarata: nessun `choice` "
             "(normalizzazione silenziosa), ogni `supplied` con `@resp`+`@cert`, "
             "ogni `subst` = `add`+`del`.")
o.append("")

o.append("## 3. Appendice · dettaglio per-istanza\n")
o.append("*Una riga per intervento, in ordine di documento; `carta` = ultimo `pb` precedente, "
         "`seg` = segmento contenitore. Ordine deterministico: i diff mostrano esattamente cosa cambia.*\n")
o.append("| # | elemento | carta | seg | tipo/valore | mano | cert | testo |")
o.append("|---:|---|---|---|---|---|---|---|")
i = 0
for r in gen_rows:  # (tag, folio, seg, info, hand, cert, text)
    i += 1
    o.append("| %d | `%s` | %s | %s | %s | %s | %s | %s |" %
             (i, r[0], r[1], r[2], r[3], r[4], r[5], r[6].replace("|", "\\|")))
o.append("")

open(OUT, "w", encoding="utf-8").write("\n".join(o))
print("Scritto %s (%d interventi genetici/integrazioni; %d rilievi)" %
      (OUT, len(gen_rows), len(issues)))
