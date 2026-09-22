#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
link_check.py — verifica di raggiungibilità degli URI ESTERNI (warning-only).

Il modello è FAIR: identificatori persistenti (w3id.org, VIAF, GeoNames, arXiv,
DHQ, creativecommons, loc.gov, wikidata…) puntano fuori dal repo. Nulla, oggi,
segnala se uno di quegli URI diventa irraggiungibile o cambia redirect. Questa
utility li raccoglie dai file dell'edizione e ne controlla lo stato HTTP.

NON BLOCCANTE per scelta: è diagnostica di manutenzione, non un cancello di
validità. Esce SEMPRE con codice 0 (anche con URI rotti); segnala i problemi
come warning. Un errore di rete o un timeout NON è un difetto dell'edizione:
gli identificatori restano corretti anche se un server è momentaneamente giù.
Per questo NON è un workflow di validazione (non intacca il conteggio «6 workflow»):
va eseguita a mano o, se si vuole, come job periodico *separato* e warning-only.

Rispetta le variabili d'ambiente di proxy (HTTPS_PROXY/HTTP_PROXY) tramite urllib.

Uso:
  python3 tools/link_check.py            # controlla e stampa un rapporto
  python3 tools/link_check.py --list     # solo elenco degli URI trovati (nessuna rete)
  python3 tools/link_check.py --timeout 15 [FILE ...]

Default dei file: teiText, teiHeader, vocabolario TTL, e tutti i .md di docs/ e la radice.
"""
import sys, re, glob, os
from urllib import request, error

DEFAULT_FILES = [
    "tei/text/castello-anima-teiText.xml",
    "tei/header/castello-anima-teiHeader.xml",
    "vocab/castello-anima-vocab.ttl",
]

URI_RE = re.compile(r'https?://[^\s"\'<>)\]}]+')
# code-fence / markdown badge noise da ripulire in coda all'URI
TRAILING = ".,;:)]}>\"'"


def collect_files(args):
    files = [a for a in args if not a.startswith("-")]
    if files:
        return files
    files = list(DEFAULT_FILES)
    files += sorted(glob.glob("docs/*.md"))
    files += sorted(glob.glob("*.md"))
    return [f for f in files if os.path.isfile(f)]


def extract_uris(files):
    """Ritorna dict uri -> set(file) in cui compare."""
    found = {}
    for path in files:
        try:
            s = open(path, encoding="utf-8").read()
        except OSError as e:
            print(f"  (salto {path}: {e})")
            continue
        for raw in URI_RE.findall(s):
            uri = raw.rstrip(TRAILING)
            found.setdefault(uri, set()).add(path)
    return found


def check(uri, timeout):
    """Ritorna (ok, dettaglio). ok=True se stato < 400. Prova HEAD, poi GET."""
    headers = {"User-Agent": "castello-anima-link-check/1.0"}
    for method in ("HEAD", "GET"):
        try:
            req = request.Request(uri, method=method, headers=headers)
            with request.urlopen(req, timeout=timeout) as resp:
                code = resp.getcode()
                final = resp.geturl()
                redir = "" if final.rstrip("/") == uri.rstrip("/") else f" -> {final}"
                return (code < 400, f"{code}{redir}")
        except error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400, 501):
                continue  # alcuni server rifiutano HEAD: riprova con GET
            return (e.code < 400, f"HTTP {e.code}")
        except error.URLError as e:
            return (False, f"URLError: {e.reason}")
        except Exception as e:  # timeout, TLS, ecc.
            return (False, f"{type(e).__name__}: {e}")
    return (False, "irraggiungibile")


def main(argv):
    args = argv[1:]
    list_only = "--list" in args
    timeout = 10
    if "--timeout" in args:
        i = args.index("--timeout")
        try:
            timeout = int(args[i + 1])
            args = args[:i] + args[i + 2:]
        except (IndexError, ValueError):
            print("errore: --timeout richiede un intero", file=sys.stderr); return 0

    files = collect_files([a for a in args if a != "--list"])
    uris = extract_uris(files)
    print(f"# link_check — {len(uris)} URI esterni distinti in {len(files)} file\n")

    if list_only:
        for uri in sorted(uris):
            print(f"  {uri}    ({len(uris[uri])} file)")
        print(f"\n# --list: nessuna richiesta di rete effettuata.")
        return 0

    ok = broken = 0
    problems = []
    for uri in sorted(uris):
        good, detail = check(uri, timeout)
        if good:
            ok += 1
            # segnala comunque i redirect (drift silenzioso dell'URI persistente)
            if "->" in detail:
                print(f"  ~ {detail:28s} {uri}")
        else:
            broken += 1
            problems.append((uri, detail, sorted(uris[uri])))

    print(f"\n## Rapporto: {ok} raggiungibili, {broken} da verificare (totale {len(uris)})")
    for uri, detail, where in problems:
        print(f"::warning::LINK da verificare [{detail}] {uri}")
        print(f"    in: {', '.join(where)}")
    if broken:
        print(f"\n(non bloccante: {broken} URI da controllare a mano — l'esito resta 0)")
    else:
        print("\nTutti gli URI esterni rispondono.")
    return 0  # SEMPRE 0: warning-only


if __name__ == "__main__":
    sys.exit(main(sys.argv))
