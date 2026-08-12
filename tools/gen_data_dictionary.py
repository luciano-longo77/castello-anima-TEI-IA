#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera docs/data-dictionary.md da tei/taxonomy/tassonomia-gh.xml (assi @ana + bande N/A/F).
Uso: python3 tools/gen_data_dictionary.py [tassonomia.xml] [output.md]
Richiede lxml."""
PREAMBLE = "# Assi e categorie della tassonomia: dizionario dei dati\n## Intertestualità sotto sorveglianza\n### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*\n[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)\n\n**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  \n**Editor**: Luciano Longo  \n**Licenza**: CC BY 4.0\n\n---\n\n**Fonte**\n*Generato da `tei/taxonomy/tassonomia-gh.xml`. Mappa ogni asse ai suoi `xml:id` e alla forma con cui compaiono in `@ana` nel testo.*\n**Convenzione `@ana`:** token separati da spazio, con `#`. L'asse **`func`** compare **senza** prefisso d'asse (es. `#legittimazione-tradizione`); **tutti gli altri assi** col prefisso `#{asse}-…` (es. `#impact-low`, `#mystic_state-unione`).\n\n---"
BANDS = "## Bande di calcolo dell'indice: `N_band` / `A_band` / `F`\n\n*Le bande **non** compaiono in `@ana`: sono i valori `<symbol>`/`<numeric>` dei campi della feature structure `<fs>` nello `standOff type=\"impact-index\"`. L'annotatore sceglie la **banda**; il decimale è l'**ancora fissa** con cui lo script calcola l'indice. Formula: **`I = (4·Fnorm + 2·N + A) / 7`** (pesi AHP F:N:A = 4:2:1); la classe `#impact-*` in `@ana` coincide con la banda di `I`.*\n\n### `N` — necessità interpretativa (quattro bande)\n\n| `N_band` (`<symbol>`) | ancora `N` | intervallo | Descrizione |\n|---|---|---|---|\n| `critica` | 0.90 | N ≥ 0.85 | La rimozione del presidio esporrebbe il passo a eresia esplicita (panteismo o quietismo). |\n| `alta` | 0.75 | 0.65 ≤ N < 0.85 | Passo teologicamente sensibile: la glossa è strutturalmente utile, ma il nodo non collassa in eresia esplicita. |\n| `media` | 0.55 | 0.45 ≤ N < 0.65 | Chiarificazione utile, esposizione moderata; l'assenza non produrrebbe deriva dottrinale. |\n| `bassa` | 0.30 | N < 0.45 | Funzione marginale, ornamentale o descrittiva. |\n\n### `A` — riduzione dell'ambiguità (tre bande)\n\n| `A_band` (`<symbol>`) | ancora `A` | intervallo | Descrizione |\n|---|---|---|---|\n| `alta` | 0.85 | A ≥ 0.80 | Chiude quasi del tutto l'ambiguità e delimita con precisione. |\n| `media` | 0.675 | 0.55 ≤ A < 0.80 | Restringe il campo ma lascia un margine di lettura. |\n| `bassa` | 0.40 | A < 0.55 | Tocca l'ambiguità solo marginalmente. |\n\n### `F` — rango dell'operazione prudenziale (dall'asse `operation`)\n\n| operazione | `F` | `Fnorm` = F/3 | classi d'impatto raggiungibili |\n|---|---|---|---|\n| `delimitazione` | 1 | 0.333 | low / medium |\n| `attenuatio` · `precisatio` · `riequilibrio` | 2 | 0.667 | medium / high |\n| `declaratio` | 3 | 1.0 | high / critical |\n\n*Soglie di classe: `impact-low` I<0.50 · `impact-medium` 0.50≤I<0.66 · `impact-high` 0.66≤I<0.82 · `impact-critical` I≥0.82.*"

import sys
from lxml import etree
TEI="http://www.tei-c.org/ns/1.0"; XML="http://www.w3.org/XML/1998/namespace"
def T(t): return "{%s}%s"%(TEI,t)
def Q(a): return "{%s}%s"%(XML,a)

TAX = sys.argv[1] if len(sys.argv)>1 else "tei/taxonomy/tassonomia-gh.xml"
OUT = sys.argv[2] if len(sys.argv)>2 else "docs/data-dictionary.md"

# Assi @ana da documentare (ordine di sezione) e loro titoli.
AXES = ["func","impact","risk","mystic_state","operation","exposition","phase","relation"]
TITLES = {
  "func":         "`func`- Funzioni retoriche",
  "impact":       "`impact`- Indice d'impatto (classe discreta)",
  "risk":         "`risk`- Rischio dottrinale",
  "mystic_state": "`mystic_state` - Stati mistici",
  "operation":    "`operation` - Operazioni prudenziali",
  "exposition":   "`exposition` - Livello d'esposizione",
  "phase":        "`phase` - Fase discorsiva",
  "relation":     "`relation` - Relazioni intertestuali",
}

def trunc(d): return d if len(d)<=97 else d[:97]+"…"
def desc(c):
    cd=c.find(T("catDesc"))
    return " ".join("".join(cd.itertext()).split()) if cd is not None else ""

R=etree.parse(TAX).getroot()
def rows_for(axis):
    for tax in R.iter(T("taxonomy")):
        if tax.get(Q("id"))==axis:
            out=[]
            for c in tax.iter(T("category")):
                cid=c.get(Q("id"))
                if cid: out.append("| `%s` | `#%s` | %s |"%(cid,cid,trunc(desc(c))))
            return out
    return []

sections=[]
for ax in AXES:
    hdr="## %s\n\n| `xml:id` | in `@ana` | Descrizione |\n|---|---|---|\n"%TITLES[ax]
    sections.append(hdr+"\n".join(rows_for(ax)))
    if ax=="impact":
        sections.append(BANDS)   # sezione bande N/A/F subito dopo impact

out = PREAMBLE + "\n\n" + "\n\n".join(sections) + "\n"
open(OUT,"w",encoding="utf-8").write(out)
print("Scritto %s (%d assi + bande)"%(OUT, len(AXES)))
