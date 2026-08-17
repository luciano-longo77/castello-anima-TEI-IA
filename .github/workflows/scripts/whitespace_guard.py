#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia anti-corruzione da riformattazione ("whitespace-in-parola").

Un editor XML con auto-indent (oXygen, VS Code "Format Document", ecc.) puo'
iniettare spazi/newline DENTRO i contenitori inline a piu' figli usati a livello
di lettera - <subst> (del/add) e <choice> (orig/reg, sic/corr, abbr/expan) -
spezzando la parola nel testo di lettura. Esempi reali osservati:
    'divenne'  -> 'd e i venne'      (D<subst><del>e</del><add>i</add></subst>venne)
    'queste'/'quante' saldati -> 'queste quante'
    'Ditemi'   -> 'Ditem e i'
Questi contenitori sono SEMPRE tight (le lezioni si toccano, nessuno spazio):
in codifica corretta il .text del contenitore e il .tail di ogni figlio sono vuoti.

Il guaio: RelaxNG, Schematron e il controllo NFC NON intercettano questa
corruzione - il file resta valido ma il testo e' rotto. Questa guardia la
riconosce alla radice.

REGOLA
  Dentro <subst> e <choice> non e' ammesso alcun nodo di testo di soli spazi,
  ne' alcun newline: il .text del contenitore e il .tail di ciascun figlio
  devono essere vuoti (None o "").

Fallisce (exit 1) elencando le violazioni con il <seg> contenitore.
Uso:  python3 whitespace_guard.py [FILE.xml ...]
      (default: tei/text/castello-anima-teiText.xml)
"""
import sys
from lxml import etree

TEI = "http://www.tei-c.org/ns/1.0"
def T(t): return "{%s}%s" % (TEI, t)
XMLID = "{http://www.w3.org/XML/1998/namespace}id"

# contenitori inline a piu' figli, sempre "tight" a livello di parola
TIGHT = {T("subst"), T("choice")}

def seg_of(el):
    p = el
    while p is not None:
        if p.tag == T("seg") and p.get(XMLID):
            return p.get(XMLID)
        p = p.getparent()
    return "(fuori-seg)"

def has_ws(s):
    """True se il nodo di testo s e' whitespace spurio (soli spazi o con newline)."""
    if not s:
        return False
    if s.strip() == "":      # soli spazi / newline / tab
        return True
    if "\n" in s:            # newline dentro contenuto tight (indentazione iniettata)
        return True
    return False

def intra_word(el):
    """True se il contenitore e' saldato a una parola (carattere-lettera prima o dopo).
    Solo in questo caso il whitespace interno spezza davvero una parola: un <choice>
    abbr/expan isolato in un <fw> (acrostico I.M.I.) NON e' intra-parola e va esente."""
    # carattere immediatamente precedente
    prev = el.getprevious()
    before = (prev.tail if prev is not None else el.getparent().text) or ""
    after = el.tail or ""
    left = before[-1:] if before else ""
    right = after[:1] if after else ""
    return left.isalpha() or right.isalpha()

def main(files):
    errors = []
    for path in files:
        try:
            root = etree.parse(path).getroot()
        except Exception as e:
            errors.append("%s: errore di parsing: %s" % (path, e))
            continue
        for el in root.iter():
            if el.tag not in TIGHT:
                continue
            # solo se il contenitore e' saldato a una parola: e' li' che il
            # whitespace interno spezza il testo di lettura (esenta acrostici/
            # alternative isolate come <fw><choice><abbr/><expan/></choice></fw>)
            if not intra_word(el):
                continue
            name = el.tag.split("}")[-1]
            sid = seg_of(el)
            if has_ws(el.text):
                errors.append("%s: <%s> in %s ha whitespace nel .text (parola spezzata da riformattazione)"
                              % (path, name, sid))
            for ch in el:
                if has_ws(ch.tail):
                    errors.append("%s: <%s> in %s: whitespace fra i figli dopo <%s> (parola spezzata)"
                                  % (path, name, sid, ch.tag.split("}")[-1]))
    if errors:
        print("::error::Guardia anti-corruzione whitespace: %d violazioni." % len(errors))
        for e in errors[:200]:
            print("  -", e)
        if len(errors) > 200:
            print("  ... (%d ulteriori)" % (len(errors) - 200))
        return 1
    print("Guardia anti-corruzione whitespace superata (nessun whitespace dentro <subst>/<choice>).")
    return 0

if __name__ == "__main__":
    files = sys.argv[1:] or ["tei/text/castello-anima-teiText.xml"]
    sys.exit(main(files))
