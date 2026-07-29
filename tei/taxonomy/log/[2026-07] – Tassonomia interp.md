### 📝 Change Log: Progetto "Castello dell'anima"

## [2026-07-01] – Allineamento licenza

### Changed
- Corretta la licenza dichiarata nel `teiHeader` da CC BY-NC 4.0 a CC BY 4.0, per coerenza con `tassonomia-gh.xml`, l'ODD e il file `LICENSE` del repository.

### Notes
- Allineamento, non modifica: `tassonomia-gh.xml` dichiarava già CC BY 4.0; era il `teiHeader` a essere disallineato.

---

## [2026-07-10] – Unificazione langUsage

### Changed
- Unificati in un solo elemento `langUsage` i due blocchi precedentemente separati nel `teiHeader`.

### Notes
- Intervento sul `teiHeader`; nessuna modifica a `tassonomia-gh.xml`.

---

## [2026-07-18] – Conversione elemento abstract

### Changed
- Convertito in `encodingDesc` l'elemento `<ab xml:base="abstract">` in `<p xml:base="abstract">`, a parità di contenuto, per rimuovere un'incertezza di validità sulla posizione dell'elemento.

### Notes
- Intervento sul `teiHeader`; nessuna modifica a `tassonomia-gh.xml`.

---

## [2026-07-29] – Verifica di coerenza completa

### Documentation
- Verificata sistematicamente la coerenza tra `tassonomia-gh.xml` e `teiHeader`: le 8 tassonomie interpretative risultano identiche, sia negli `xml:id` sia nel testo delle `catDesc` (unica differenza rilevata: convenzione tipografica dell'apostrofo, curvo in `tassonomia-gh.xml` vs dritto nel `teiHeader` — nessuna divergenza di contenuto).
- Verificata la licenza: CC BY 4.0 in entrambi i file, stesso URL target.
- Verificato il funzionamento reale delle 4 regole Schematron (`category-catdesc-present`, `category-catdesc-not-empty`, `category-prefix-consistency`, `taxonomy-category-xmlid-unique`) tramite esecuzione diretta, non per lettura.

### Fixed
- Corretti 6 riferimenti `@ana` a categorie inesistenti nel file `tei/taxonomy/esempio/taxonomy-text-model.xml` (`relation-premessa-conseguenza`, `impact-supportive` ×2, `relation-analogia`, `relation-causa-effetto`, `relation-contrasto`), rimossi senza sostituzione.
- Corretto `queryBinding="xslt2"` → `queryBinding="xslt"` in `taxonomy-sch.sch`, per compatibilità con il motore di validazione `lxml` usato in CI.

### Added
- Attivato workflow di validazione automatica (`.github/workflows/main.yml`): verifica ben-formazione, RelaxNG, Schematron, presenza delle 8 tassonomie core, e ora anche la validità referenziale di `@ana` in tutti i file dentro `tei/taxonomy/esempio/`.

### Notes
- Stato attuale: `tassonomia-gh.xml` verificato coerente su tutti i punti controllati; CI attiva e funzionante (run #6, esito Success).
