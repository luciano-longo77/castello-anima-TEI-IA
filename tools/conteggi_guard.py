#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guardia dei conteggi - i numeri canonici del corpus, verificati in macchina.

La documentazione e il paper affermano in prosa una serie di numeri-chiave
(«944 <seg>», «944 <fs>», «37 <cit>», «199 <linkGrp>: Libro I 40, II 46, III 113»,
«409 figure retoriche», «1011 fuochi semantici»). Sono affermazioni VERE oggi, ma
scritte a mano: nulla impedisce che una modifica al corpus le faccia divergere
SENZA far fallire la pipeline (ne' RelaxNG ne' Schematron contano gli elementi).
E' la stessa classe di refuso - un numero in prosa che non torna piu' - gia'
intercettata a mano durante l'audit.

Questa guardia rende quei numeri MACCHINA-VERIFICABILI: ricava i conteggi dal
teiText (teiHeader incluso via xi:include) e li confronta con le costanti canoniche
dichiarate qui sotto. Se il corpus cambia, la guardia diventa ROSSA e obbliga a un
aggiornamento CONSAPEVOLE della costante *e* della prosa (docs + paper) - non a una
divergenza silenziosa.

NB - conteggio, non semantica: l'aggancio referenziale degli @ana, dei puntatori e
dell'apparato e' gia' coperto dalle altre guardie (E2, puntatori, cross-file). Qui
si contano soltanto gli elementi, con il minor numero di assunzioni possibile.

NB - e' un VERIFICATORE STANDALONE (vive in tools/, come impact_index.py e
sensitivity.py), da lanciare a mano o in un check di release. NON e' una «nona
guardia» di validate-text.yml. Se un giorno lo si vuole in CI, va aggiunto come
STEP di un workflow gia' esistente (categoria a se', come NFC / RelaxNG /
Schematron) - MAI come nuovo workflow o nuova guardia, per non intaccare il
conteggio «8 guardie / 6 workflow» dichiarato in docs e paper.

Fallisce (exit 1) elencando ogni numero divergente (atteso vs osservato).

Uso:
  python3 tools/conteggi_guard.py [TEXT_XML]
default:
  TEXT_XML = tei/text/castello-anima-teiText.xml
"""
import sys, re
from collections import Counter
from lxml import etree

XMLID = "{http://www.w3.org/XML/1998/namespace}id"

# ---------- conteggi canonici (fonte di verita' dei numeri in prosa) ----------
# Aggiornare QUI e nella prosa (docs + paper) solo a fronte di un cambiamento
# VOLUTO del corpus. La guardia esiste per impedire che divergano di nascosto.
EXPECTED = {
    "seg":                944,   # segmenti con xml:id
    "fs":                 944,   # feature-structure dell'indice d'impatto (1:1 con seg)
    "cit":                 37,   # citazioni (32 latine + 5 volgari)
    "linkGrp":            199,   # catene semantiche (totale)
    "span_rhetorical":    409,   # figure retoriche (standOff rhetorical-figures)
    "span_semantic":     1011,   # fuochi semantici (standOff semantic-focus)
}
# catene per libro (Libro I / II / III), desunte dal prefisso seg-b<L> dei membri
EXPECTED_CHAINS_BY_BOOK = {"1": 40, "2": 46, "3": 113}


def ln(el):
    return etree.QName(el).localname


def count_spans_in_standoff(root, standoff_type):
    n = 0
    for so in root.iter():
        if isinstance(so.tag, str) and ln(so) == "standOff" and so.get("type") == standoff_type:
            n += sum(1 for e in so.iter() if isinstance(e.tag, str) and ln(e) == "span")
    return n


def main(argv):
    path = argv[1] if len(argv) > 1 else "tei/text/castello-anima-teiText.xml"
    try:
        tree = etree.parse(path)
        tree.xinclude()                      # rende visibile l'header, come fa la CI
    except Exception as e:
        print(f"::error::Parsing/XInclude fallito: {e}")
        return 1
    root = tree.getroot()

    # ---- conteggi osservati ----
    observed = {
        "seg":             sum(1 for e in root.iter()
                               if isinstance(e.tag, str) and ln(e) == "seg" and e.get(XMLID)),
        "fs":              sum(1 for e in root.iter()
                               if isinstance(e.tag, str) and ln(e) == "fs"),
        "cit":             sum(1 for e in root.iter()
                               if isinstance(e.tag, str) and ln(e) == "cit"),
        "linkGrp":         sum(1 for e in root.iter()
                               if isinstance(e.tag, str) and ln(e) == "linkGrp"),
        "span_rhetorical": count_spans_in_standoff(root, "rhetorical-figures"),
        "span_semantic":   count_spans_in_standoff(root, "semantic-focus"),
    }

    # catene per libro (dal prefisso dei membri dei <link>)
    chains_by_book = Counter()
    for lg in root.iter():
        if not (isinstance(lg.tag, str) and ln(lg) == "linkGrp"):
            continue
        books = set()
        for lk in lg.iter():
            if isinstance(lk.tag, str) and ln(lk) == "link":
                for tok in (lk.get("target") or "").split():
                    m = re.match(r"#?seg-b(\d)", tok)
                    if m:
                        books.add(m.group(1))
        if len(books) == 1:
            chains_by_book[next(iter(books))] += 1
        elif books:
            chains_by_book["misto:" + "".join(sorted(books))] += 1
        else:
            chains_by_book["?"] += 1

    errors = []
    for k, exp in EXPECTED.items():
        obs = observed[k]
        if obs != exp:
            errors.append(f"{k}: atteso {exp}, osservato {obs}")

    # 1:1 seg <-> fs (invariante forte del modello)
    if observed["seg"] != observed["fs"]:
        errors.append(f"seg/fs: la corrispondenza 1:1 e' rotta ({observed['seg']} seg vs {observed['fs']} fs)")

    for book, exp in EXPECTED_CHAINS_BY_BOOK.items():
        obs = chains_by_book.get(book, 0)
        if obs != exp:
            errors.append(f"catene Libro {book}: atteso {exp}, osservato {obs}")
    extra_books = {b: n for b, n in chains_by_book.items()
                   if b not in EXPECTED_CHAINS_BY_BOOK}
    if extra_books:
        errors.append(f"catene con libro imprevisto/misto: {dict(extra_books)}")
    somma = sum(EXPECTED_CHAINS_BY_BOOK.values())
    if somma != EXPECTED["linkGrp"]:
        errors.append(f"incoerenza interna delle costanti: somma per libro {somma} != linkGrp {EXPECTED['linkGrp']}")

    if errors:
        print(f"::error::Guardia conteggi: {len(errors)} numero/i canonico/i divergente/i "
              f"(prosa docs+paper da riallineare o modifica non voluta del corpus).")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Guardia conteggi superata: %d seg = %d fs (1:1), %d cit, %d linkGrp "
          "(Libro I %d · II %d · III %d), %d figure retoriche, %d fuochi semantici — "
          "tutti i numeri canonici combaciano con docs e paper." % (
              observed["seg"], observed["fs"], observed["cit"], observed["linkGrp"],
              chains_by_book.get("1", 0), chains_by_book.get("2", 0), chains_by_book.get("3", 0),
              observed["span_rhetorical"], observed["span_semantic"]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
