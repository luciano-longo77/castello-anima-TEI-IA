# w3id — URI permanenti per il vocabolario SKOS

Il vocabolario usa la base URI **`https://w3id.org/castello-anima-vocab/`**. w3id.org fornisce un redirect permanente indipendente dall'host reale (GitHub Pages, Zenodo, un dominio proprio…): gli URI dei concetti restano stabili anche se cambia dove il `.ttl` è pubblicato.

## Passi

1. **Pubblica il `.ttl`** (host immediato): abilita **GitHub Pages** (Settings → Pages → deploy da `main`). Il file sarà a
   `https://luciano-longo77.github.io/castello-anima-TEI-IA/vocab/castello-anima-vocab.ttl`.
2. **PR a w3id** (persistenza): fork di [`perma-id/w3id.org`](https://github.com/perma-id/w3id.org), aggiungi la cartella `castello-anima-vocab/` con il file `.htaccess` (contenuto in `htaccess.txt` di questo pacchetto), apri una PR. Approvata la PR, `https://w3id.org/castello-anima-vocab/…` reindirizza all'host Pages.

## Nota tecnica

Il redirect iniziale è `302`. Per Linked Data canonico si può passare a **`303 See Other`** (distingue il *concetto* dal *documento* che lo descrive). Il `.ttl` è già generato con la base `w3id` all'interno: gli URI diventano dereferenziabili appena la PR passa, **senza rigenerare**.
