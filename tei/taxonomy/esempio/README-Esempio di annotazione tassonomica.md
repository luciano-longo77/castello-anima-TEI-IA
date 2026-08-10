# Esempio di annotazione tassonomica
## Intertestualità sotto sorveglianza
### *Modello TEI-driven e AI-assisted per l'analisi di citazioni, glosse e rimandi nel Castello dell'anima*

[![TEI P5](https://img.shields.io/badge/TEI-P5-334155)](https://tei-c.org/) [![Castello dell'anima](https://img.shields.io/badge/Castello%20dell%27anima-7b2d3b)](https://github.com/luciano-longo77/castello-anima-TEI-IA)

**Autrice**: Teresa di San Geronimo (Anna La Longa, 1670–post 1703)  
**Editor**: Luciano Longo  
**Licenza**: CC BY 4.0  

## Cos'è questo file

`taxonomy-text-model.xml` mostra, su un brano reale del *Castello dell'anima* (apertura del Libro III, c. 158r), come si applica in pratica il sistema tassonomico dell'edizione. Non è un file di lavoro dell'edizione vera e propria, serve solo a documentare l'uso corretto dell'attributo `@ana`.

## Come leggerlo

Ogni `<seg>` porta un attributo `@ana` con una lista di riferimenti separati da spazio, ciascuno preceduto da `#`. Ogni riferimento punta a una categoria dichiarata in [`tassonomia-gh.xml`](../tassonomia-gh.xml) — non sono etichette libere, ma id realmente definiti lì.

Esempio (dal file, il segmento `seg-158r-declaratio`):
```xml
<seg xml:id="seg-158r-declaratio" type="indicatio" subtype="dichiarazione-ortodossia"
     hand="#ink_1" cert="high"
     ana="#rischio-declaratio #operation-declaratio #risk-dottrinale
          #exposition-high #phase-introduction #mystic_state-quiete #impact-critical">
  Anche padre mi protesto, che se dirò qualche cosa che contradichi la santa fede
</seg>
```

Un segmento porta sempre più riferimenti insieme, uno per ciascun asse interpretativo pertinente — funzione retorica (`func`, qui `rischio-declaratio`), operazione prudenziale (`operation`), rischio dottrinale (`risk`), livello di esposizione (`exposition`), fase discorsiva (`phase`), stato mistico (`mystic_state`), impatto interpretativo (`impact`) — non un solo tag generico.

**Nota sull'asse `impact`.** La classe `#impact-*` non è una scelta libera dell'annotatore: è l'**esito della discretizzazione dell'indice composito N–A–F** (vedi [`Sistema Tassonomico.md`](../Sistema%20Tassonomico.md) §5). Il *calcolo* corrispondente — bande, valori‑ancora, N/A/F/I — non vive in `@ana`, ma in una feature structure `<fs>` dentro `<standOff type="impact-index">` nel `teiText` completo. Questo esempio illustra il **solo livello `@ana`** e perciò non include lo `standOff`.

## Validazione

Ogni riferimento `@ana` in questo file è verificato automaticamente a ogni modifica: il workflow di CI *Validate Taxonomy* (`.github/workflows/main.yml`) controlla che ciascun token corrisponda a un `xml:id` realmente dichiarato in `tassonomia-gh.xml`. Se un file esempio contiene una categoria inventata, il workflow fallisce e lo segnala.

## A cosa serve

Prima di annotare il testo reale dell'edizione, usa questo file come riferimento per il formato corretto — struttura dell'attributo `@ana`, sintassi dei puntatori (`#xml-id`), combinazione di più assi sullo stesso segmento.
