### 📝 Change Log: Progetto "Castello dell'anima"
## [2026-04-18] – Tassonomia interpretativa prudenziale

# Consolidamento Infrastrutturale e Validazione v2.0

#### **v0.1 – Definizione Metodologica**
- **Added:** Definizione del framework teorico per l'analisi del testo di Teresa di San Geronimo (mistica sotto sorveglianza).
- **Documentation:** Identificazione dei tre assi portanti iniziali:
    - `func` (Funzioni retoriche e intenzionalità).
    - `risk` (Punti critici dottrinali soggetti a censura).
    - `impact` (Intensità dell’effetto interpretativo).
- **Notes:** Obiettivo di trasformare l'analisi filologica in un modello computabile.

#### **v0.2 – Infrastruttura TEI P5**
- **Added:** Creazione del file `tassonomia.xml` seguendo lo standard TEI (Text Encoding Initiative).
- **Changed:** Implementazione dell'uso sistematico dell'attributo `@ana` per la marcatura semantica.
- **Fixed:** Passaggio da una logica a stringhe semplici a un sistema di **Pointer/URI** (es. `#ethos-obbedienza`) per garantire la compatibilità con i processori XSLT e la validità XML.

#### **v1.0 – Catena di Validazione (ODD & Schemi)**
- **Added:** Creazione del file **ODD** (`tassonomia.odd`) come "Single Source of Truth" del progetto.
- **Changed:** Derivazione automatica degli schemi tecnici:
    - `tassonomia.rng` (Relax NG) per il controllo strutturale.
    - `tassonomia.sch` (Schematron) per il controllo semantico vincolante.
- **Fixed:** Implementazione della regola dei prefissi: ogni ID di categoria deve iniziare con l'ID della tassonomia padre (es. `impact-high`, `risk-quietismo`).

#### **v1.2 – Normalizzazione "International Tech"**
- **Changed:** Uniformazione della nomenclatura degli assi verso l'inglese accademico per garantire interoperabilità internazionale.
- **Updated:** Revisione completa degli assi `exposition` (low/medium/high/critical) e `phase` (introduction/development/conclusion).
- **Legal:** Inserimento della licenza **CC-BY 4.0** per la distribuzione Open Access del modello.
- **Documentation:** Redazione finale del file `Sistema Tassonomico.md` (o `Documento Metodologico.md`).

#### **v1.3 – Automazione e Visualizzazione**
- **Added:** Workflow **GitHub Actions** (`validate-taxonomy.yaml`) per la validazione automatica (CI/CD) a ogni push.
- **UX:** Sviluppo di `tassonomia.html`, dashboard interattiva per l'esplorazione visuale delle 42 categorie tassonomiche.
- **Application:** Creazione di `taxonomy-text-model.xml` come test-case per la validazione incrociata (Coerenza 100%).

#### **v2.0 – Consolidamento e Release Finale**
- **Fixed:** Risoluzione di tutte le incongruenze tra definizioni in `classDecl` e applicazioni nel testo.
- **Notes:** Il sistema è dichiarato **"Production Ready"** e stabile scientificamente. 
- **Verdetto:** Rigore scientifico e robustezza tecnica validati con successo.

---

### **Riepilogo Componenti Finali**
1. **Core:** `tassonomia.xml` (base dati semantica normalizzata).
2. **Validazione:** `tassonomia.odd`, `tassonomia.rng`, `tassonomia.sch`.
3. **Governance:** `Documento Metodologico.md`, `validate-taxonomy.yaml`.
4. **UX:** `tassonomia.html` (Interfaccia di consultazione).
5. **Applicazione:** `taxonomy-text-model.xml`.