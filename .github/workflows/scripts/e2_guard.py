#!/usr/bin/env python3
"""
Guardia E2 - integrità referenziale di @ana nel testo.

Verifica che OGNI token di @ana nel file di testo TEI risolva a:
  - un xml:id di <category> dichiarato nella tassonomia (tassonomia-gh.xml), oppure
  - un xml:id di vocabolario locale dichiarato nel testo (es. <interp>/<interpGrp>
    negli strati <standOff>), oppure
  - un qualunque xml:id presente nel documento del testo.

Fallisce (exit 1) se trova token @ana non dichiarati, oppure @ana in pseudo-sintassi
(con ';' o 'asse:valore') invece di puntatori '#id' separati da spazio.

Uso:
  python3 e2_guard.py [TEXT_XML] [TAXONOMY_XML]
default:
  TEXT_XML     = tei/text/castello-anima-teiText.xml
  TAXONOMY_XML = tei/taxonomy/tassonomia-gh.xml
"""
import sys, re
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
XMLID = "{http://www.w3.org/XML/1998/namespace}id"

TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"
TAX  = sys.argv[2] if len(sys.argv) > 2 else "tei/taxonomy/tassonomia-gh.xml"

def ids_of(doc, xpath):
    return {e.get(XMLID) for e in doc.iterfind(xpath, NS) if e.get(XMLID)}

try:
    text = etree.parse(TEXT)
    tax  = etree.parse(TAX)
except Exception as e:
    print(f"::error::Parsing fallito: {e}")
    sys.exit(1)

tax_ids   = ids_of(tax, ".//t:category")
local_ids = {e.get(XMLID) for e in text.iter() if e.get(XMLID)}
declared  = tax_ids | local_ids

errors = []
bad_syntax = []
n_tokens = 0

for el in text.iter():
    a = el.get("ana")
    if not a:
        continue
    # pseudo-sintassi non ammessa
    if ";" in a or re.search(r"(^|\s)[A-Za-z_]+:[^#/\s]", a):
        bad_syntax.append((el.sourceline, a[:80]))
        continue
    for tok in a.split():
        n_tokens += 1
        if not tok.startswith("#"):
            errors.append((el.sourceline, tok, "token senza '#' (non e' un puntatore)"))
            continue
        tid = tok[1:]
        if tid not in declared:
            errors.append((el.sourceline, tok, "non dichiarato in tassonomia ne' localmente"))

if bad_syntax:
    print("::error::@ana in pseudo-sintassi (usare '#id' separati da spazio):")
    for line, val in bad_syntax[:50]:
        print(f"  - riga {line}: {val}")

if errors:
    print(f"::error::Guardia E2: {len(errors)} token @ana non risolti (su {n_tokens} controllati).")
    for line, tok, why in errors[:100]:
        print(f"  - riga {line}: {tok} -> {why}")

if bad_syntax or errors:
    sys.exit(1)

print(f"Guardia E2 superata: {n_tokens} token @ana, tutti risolti "
      f"({len(tax_ids)} categorie in tassonomia + {len(local_ids)} id locali).")
