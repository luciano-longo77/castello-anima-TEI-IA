#!/usr/bin/env python3
"""
Guardia cit/glossa - invarianti dei nuovi tag intertestuali e glossematici.

Impone la convenzione decisa per il Castello dell'anima:
  A) <cit> e' sempre DENTRO un <seg>, contiene un <quote> (e di norma un <bibl>);
     non porta indice d'impatto (nessuna <fs> lo riferisce): l'indice resta sul <seg>.
  B) <note type="glossa"> e' VUOTA, figlia di <add>, e il suo @ana e' ristretto
     all'asse operation (+ eventuale func); non contiene mai #impact-* (l'impatto
     e' del segmento, non della glossa).
  C) Nessuna <fs>/@corresp punta a un <cit> o a una <note> (indice solo su <seg>).

Fallisce (exit 1) elencando le violazioni.
Uso:  python3 cit_glossa_guard.py [TEXT_XML]
"""
import sys
from lxml import etree

NS = {"t": "http://www.tei-c.org/ns/1.0"}
T = "{http://www.tei-c.org/ns/1.0}"
XMLID = "{http://www.w3.org/XML/1998/namespace}id"
TEXT = sys.argv[1] if len(sys.argv) > 1 else "tei/text/castello-anima-teiText.xml"

FUNC = {
    "legittimazione", "legittimazione-biblica", "legittimazione-liturgica", "legittimazione-tradizione",
    "pedagogia", "pedagogia-introduzione", "pedagogia-discernimento", "pedagogia-esemplificazione",
    "rischio", "rischio-attenuatio", "rischio-precisatio", "rischio-declaratio",
    "ethos", "ethos-umilta", "ethos-esperienza", "ethos-obbedienza",
}
def ln(e): return etree.QName(e).localname if isinstance(e.tag, str) else None
def ancestor_localnames(e):
    out = []
    p = e.getparent()
    while p is not None:
        n = ln(p)
        if n: out.append(n)
        p = p.getparent()
    return out

doc = etree.parse(TEXT)
R = doc.getroot()
errors, warns = [], []
n_cit = n_note = 0

# A) cit
for cit in R.iter(T + "cit"):
    n_cit += 1
    where = "riga %s" % cit.sourceline
    if "seg" not in ancestor_localnames(cit):
        errors.append("<cit> fuori da <seg> (%s)" % where)
    if cit.find(T + "quote") is None:
        errors.append("<cit> senza <quote> (%s)" % where)
    if cit.find(T + "bibl") is None:
        warns.append("<cit> senza <bibl> (fonte non dichiarata) (%s)" % where)

# B) note type=glossa
for note in R.iter(T + "note"):
    if note.get("type") != "glossa":
        continue
    n_note += 1
    where = "riga %s" % note.sourceline
    # vuota: niente testo significativo, niente figli
    if (note.text and note.text.strip()) or len(note) > 0:
        errors.append("<note type='glossa'> non vuota (%s)" % where)
    if ln(note.getparent()) != "add":
        errors.append("<note type='glossa'> non figlia di <add> (%s)" % where)
    toks = [t.lstrip("#") for t in (note.get("ana") or "").split()]
    if not toks:
        errors.append("<note type='glossa'> senza @ana (%s)" % where)
    for t in toks:
        ok = t.startswith("operation-") or t in FUNC
        if not ok:
            errors.append("<note type='glossa'>/@ana '%s' fuori da operation(+func) (%s)" % (t, where))
        if t.startswith("impact-"):
            errors.append("<note type='glossa'> porta #impact-* (l'indice e' del seg) (%s)" % where)

# C) nessuna fs verso cit/note
id2el = {e.get(XMLID): e for e in R.iter() if e.get(XMLID)}
for fs in R.iter(T + "fs"):
    tgt = (fs.get("corresp") or "").lstrip("#")
    el = id2el.get(tgt)
    if el is not None and ln(el) in ("cit", "note"):
        errors.append("<fs corresp=#%s> punta a <%s> (indice solo su <seg>)" % (tgt, ln(el)))

if warns:
    print("Avvisi (non bloccanti):")
    for w in warns[:50]:
        print("  -", w)
if errors:
    print("::error::Guardia cit/glossa: %d violazioni." % len(errors))
    for e in errors[:100]:
        print("  -", e)
    sys.exit(1)
print("Guardia cit/glossa superata: %d <cit> (dentro <seg>, con <quote>), "
      "%d <note type='glossa'> (vuote, in <add>, @ana=operation/func, senza impact); "
      "nessuna <fs> verso cit/note." % (n_cit, n_note))
