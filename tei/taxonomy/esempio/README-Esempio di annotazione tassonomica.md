# Esempio di annotazione tassonomica

## Cos'è questo file

`taxonomy-text-model.xml` mostra, su un brano reale del *Castello dell'anima* (apertura del Libro III), come si applica in pratica il sistema tassonomico dell'edizione. Non è un file di lavoro dell'edizione vera e propria — serve solo a documentare l'uso corretto dell'attributo `@ana`.

## Come leggerlo

Ogni `<seg>` o `<cit>` porta un attributo `@ana` con una lista di riferimenti separati da spazio, ciascuno preceduto da `#`. Ogni riferimento punta a una categoria dichiarata in [`tassonomia-gh.xml`](../tassonomia-gh.xml) — non sono etichette libere, ma id realmente definiti lì.

Esempio:
```xml
<p n="1">
<seg xml:id="III-pref-p1-004"
  ana="#rischio-declaratio
        #operation-declaratio
          #risk-dottrinale
            #exposition-medium
              #phase-introduction
                #phase-critical">
                  Anche padre mi protesto, che se dirò qualche cosa che contradichi la santa fede, non sarà
                  per mia malitia, ma per ignoranza, e cossì quanto dirò non intendo contradire quel che dice
                  la nostra santa Chiesa Catolica Romana, confessandomi sua figlia, e seguace, tutto che indegna.
</seg>
```

Un segmento porta sempre più riferimenti insieme, uno per ciascun asse interpretativo pertinente 
(funzione retorica, impatto interpretativo, rischio dottrinale, stato mistico, operazione prudenziale, livello di esposizione, fase discorsiva) non un solo tag generico.

## Validazione

Ogni riferimento `@ana` in questo file è verificato automaticamente a ogni modifica: il workflow di CI 
(`.github/workflows/main.yml`) controlla che ciascun token corrisponda a un `xml:id` realmente dichiarato in `tassonomia-gh.xml`. Se un file esempio contiene una categoria inventata, il workflow fallisce e lo segnala.

## A cosa serve

Prima di annotare il testo reale dell'edizione, usa questo file come riferimento per il formato corretto — struttura dell'attributo `@ana`, sintassi dei puntatori (`#xml-id`), combinazione di più assi sullo stesso segmento.
