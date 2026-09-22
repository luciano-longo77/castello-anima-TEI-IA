#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia cross-file dell'apparato esterno (variants ↔ teiText ↔ runs.tsv).

L'apparato `variants/castello-anima-variants.xml` e' uno standoff: aggancia i controfattuali
IA al testo per @loc, un <TEI> autonomo (nessun xi:include). E' formalmente valido per RelaxNG
anche se @loc punta a un <seg> INESISTENTE, o se un log non ha la sua variante: lo schema TEI
generale non puo' garantire l'aggancio semantico. Questa guardia lo verifica.

CONTROLLI
  1. ogni <app>@loc risolve a ESATTAMENTE un <seg> del teiText (@loc e' l'xml:id NUDO, senza '#');
  2. ogni riga di logs/runs.tsv (locus_id, operation) ha una <app> corrispondente in variants,
     e viceversa ogni <app> ha la sua riga di run;
  3. l'operazione del log combacia con il @type dell'<app> (workflow-* ↔ -CIT/+TEXTsub/+CIT);
  4. l'esito (approvata/respinta/non-eseguibile) e' coerente fra runs.tsv e la <note type="run">
     dell'<app>;
  5. lem/@wit, rdg/@resp e i @ref bibliografici interni ('#…') risolvono contro il teiHeader
     dell'edizione (richiamato via xi:include dal teiText).

Fallisce (exit 1) elencando ogni disallineamento.

Uso:
  python3 variants_crossref_guard.py [VARIANTS] [TEXT] [RUNS]
default:
  VARIANTS = variants/castello-anima-variants.xml
  TEXT     = tei/text/castello-anima-teiText.xml   (xi:include risolto per gli id del teiHeader)
  RUNS     = logs/runs.tsv
"""
import sys, csv, re
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"
def T(t): return "{%s}%s" % (TEI, t)
XMLID = "{http://www.w3.org/XML/1998/namespace}id"

VARIANTS = sys.argv[1] if len(sys.argv) > 1 else "variants/castello-anima-variants.xml"
TEXT     = sys.argv[2] if len(sys.argv) > 2 else "tei/text/castello-anima-teiText.xml"
RUNS     = sys.argv[3] if len(sys.argv) > 3 else "logs/runs.tsv"

# mappa workflow (apparato) ↔ codice operazione (log)
WF2OP = {
    "workflow-rimozione":            "-CIT",
    "workflow-recupero-cancellature":"+TEXTsub",
    "workflow-aggiunta":             "+CIT",
}

def localname(t): return t.split("}", 1)[1] if "}" in t else t

try:
    var = etree.parse(VARIANTS)
    txt = etree.parse(TEXT); txt.xinclude()          # risolve il teiHeader → id di mani/testimoni/agenti
except Exception as e:
    print(f"::error::Parsing/XInclude fallito: {e}")
    sys.exit(1)

# universi di riferimento nel teiText (+ header incluso)
seg_ids  = [s.get(XMLID) for s in txt.iter(T("seg")) if s.get(XMLID)]
seg_set  = set(seg_ids)
all_ids  = {e.get(XMLID) for e in txt.iter() if isinstance(e.tag, str) and e.get(XMLID)}

# righe di run
try:
    runs = list(csv.DictReader(open(RUNS, encoding="utf-8"), delimiter="\t"))
except Exception as e:
    print(f"::error::Lettura {RUNS} fallita: {e}")
    sys.exit(1)

errors = []
apps = list(var.iter(T("app")))

# (1) @loc → esattamente un <seg>
app_by_key = {}          # (locus, op) -> app  (per i controlli 2-4)
for a in apps:
    loc = a.get("loc")
    typ = a.get("type")
    if not loc:
        errors.append(f"<app> senza @loc (type={typ})"); continue
    n = seg_ids.count(loc)
    if n == 0:
        errors.append(f"<app @loc='{loc}'> non corrisponde ad alcun <seg> del teiText")
    elif n > 1:
        errors.append(f"<app @loc='{loc}'> corrisponde a {n} <seg> (deve essere unico)")
    op = WF2OP.get(typ)
    if op is None:
        errors.append(f"<app @loc='{loc}'> ha @type='{typ}' fuori dal vocabolario workflow-*")
    else:
        app_by_key[(loc, op)] = a
    # (5) lem/@wit, rdg/@resp, @ref interni risolvono
    for lem in a.iter(T("lem")):
        for w in (lem.get("wit") or "").split():
            if w.startswith("#") and w[1:] not in all_ids:
                errors.append(f"<app @loc='{loc}'> lem/@wit -> {w} INESISTENTE")
    for rdg in a.iter(T("rdg")):
        for r in (rdg.get("resp") or "").split():
            if r.startswith("#") and r[1:] not in all_ids:
                errors.append(f"<app @loc='{loc}'> rdg/@resp -> {r} INESISTENTE")
    for el in a.iter():
        for ref in (el.get("ref") or "").split():
            if ref.startswith("#") and ref[1:] not in all_ids:
                errors.append(f"<app @loc='{loc}'> <{localname(el.tag)}>@ref -> {ref} INESISTENTE")

# esito dichiarato nella <note type="run"> di ciascuna app
def app_esito(a):
    for n in a.iter(T("note")):
        if n.get("type") == "run":
            m = re.search(r"esito=([^\s·]+)", "".join(n.itertext()))
            if m: return m.group(1)
    return None

runs_keys = {(r["locus_id"], r["operation"]) for r in runs}
app_keys  = set(app_by_key.keys())

# (2) copertura biunivoca runs ↔ app
for k in runs_keys - app_keys:
    errors.append(f"runs.tsv {k} non ha una <app> corrispondente in variants")
for k in app_keys - runs_keys:
    errors.append(f"<app> {k} non ha una riga in runs.tsv")

# (4) esito coerente runs.tsv ↔ note della app
runs_by_key = {(r["locus_id"], r["operation"]): r for r in runs}
for k in app_keys & runs_keys:
    e_run = runs_by_key[k]["esito"]
    e_app = app_esito(app_by_key[k])
    if e_app is not None and e_app != e_run:
        errors.append(f"{k}: esito runs.tsv='{e_run}' ≠ note app='{e_app}'")

if errors:
    print(f"::error::Guardia cross-file variants: {len(errors)} disallineamenti.")
    for e in errors[:100]:
        print(f"  - {e}")
    if len(errors) > 100:
        print(f"  ... e altri {len(errors) - 100}.")
    sys.exit(1)

print(f"Guardia cross-file variants superata: {len(apps)} <app> agganciate correttamente "
      f"(@loc unici sul teiText, {len(runs)} run in runs.tsv, operazioni/esiti/testimoni/agenti coerenti).")
