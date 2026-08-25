# w3id — URI permanenti per il vocabolario SKOS

Il vocabolario usa la base URI **`https://w3id.org/castello-anima-vocab/`**. w3id.org fornisce un redirect permanente indipendente dall'host reale (GitHub Pages, Zenodo, un dominio proprio…): gli URI dei concetti restano stabili anche se cambia dove il `.ttl` è pubblicato.

## Stato: attivo

Il setup è **completo** — la PR [`perma-id/w3id.org` #6580](https://github.com/perma-id/w3id.org/pull/6580) è stata **mergiata**: gli URI `https://w3id.org/castello-anima-vocab/…` sono **dereferenziabili**.

1. **`.ttl` pubblicato** su GitHub Pages (deploy da `main`):
   `https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/castello-anima-vocab.ttl`.
2. **Redirect w3id attivo**: la cartella `castello-anima-vocab/`, con il suo `.htaccess`, è nel repo `perma-id/w3id.org`; `https://w3id.org/castello-anima-vocab/…` reindirizza all'host Pages.

## Content negotiation (`303 See Other`)

Il redirect è **`303 See Other`** — lo standard per il Linked Data, che distingue il *concetto* dal *documento* che lo descrive (non è più un `302` generico). Le regole dell'`.htaccess`:

- richiesta **RDF/Turtle** (`Accept: text/turtle`, `application/rdf+xml`, `application/x-turtle`) → il `.ttl` completo;
- **un singolo concetto** (`…/<id>`) → la sua scheda nel viewer (`vocab/site/?c=<id>`);
- la **base** del vocabolario → l'indice del viewer (`vocab/site/`).

Il `.ttl` è generato con la base `w3id` già all'interno: gli URI erano dereferenziabili appena passata la PR, **senza rigenerare**.

## Vocabolario gemello

Lo stesso schema vale per l'edizione gemella: base `https://w3id.org/castello-edizione-vocab/` (17 stati mistici), con `.htaccess` speculare in `perma-id/w3id.org` (anch'esso `303`) verso `castello-dell-anima-edizione`. I due vocabolari sono allineati via `skos:*Match` in [`../vocab/alignments-castello-anima-edizione.ttl`](../vocab/alignments-castello-anima-edizione.ttl).
