 // ==================== XML DATA ====================
        const xmlString = `<?xml version="1.0" encoding="UTF-8"?>
<?xml-model href="schema/tassonomia.rng"
            type="application/xml"
            schematypens="http://relaxng.org/ns/structure/1.0"?>
<?xml-model href="schema/tassonomia.sch"
            type="application/xml"
            schematypens="http://purl.oclc.org/dsdl/schematron"?>

<TEI xmlns="http://www.tei-c.org/ns/1.0" xml:id="castello-anima-tassonomia" xml:lang="it">

    <teiHeader>
        <fileDesc>
            <titleStmt>
                <title> Tassonomia prudenziale per la progettazione di un modello TEI IA per lo
                    studio dell'intertestualità sotto sorveglianza del "Castello dell’anima" di suor
                    Teresa di San Geronimo </title>
                <respStmt>
                    <resp>Progettazione del modello tassonomico (taxonomy.xml)</resp>
                    <name xml:id="p-longo">Luciano Longo</name>
                </respStmt>
            </titleStmt>

            <publicationStmt>
                <publisher>Progetto TEI + IA controllata</publisher>
                <date when="2026-03-30">30 marzo 2026</date>
                <availability>
                    <licence target="https://creativecommons.org/licenses/by/4.0/"> CC‑BY 4.0 – Open
                        Access </licence>
                </availability>
            </publicationStmt>

            <sourceDesc>
                <bibl type="ms"> Palermo, BCP, ms. 2 Qq E 29 (sec. XVII ex.) - "Castello dell’anima"
                    di suor Teresa di San Geronimo (Anna La Longa) </bibl>
            </sourceDesc>
        </fileDesc>

        <encodingDesc>
            <classDecl>

                <!-- 1. Tassonomia delle FUNZIONI RETORICHE -->
                <taxonomy xml:id="func">

                    <category xml:id="legittimazione">
                        <desc> Procedure retoriche che consolidano l’ortodossia del discorso mistico
                            mediante appoggi biblici, liturgici e tradizionali (anche aurorali),
                            usati per evitare sospetti di quietismo e per ancorare temi rischiosi
                            all’autorità della Chiesa, dei santi. </desc>

                        <category xml:id="legittimazione-biblica">
                            <desc>Citazioni e parafrasi scritturali, spesso in latino, impiegate per
                                rendere accettabili concetti come "quiete", "infusione" e "unione",
                                mostrando conformità alla dottrina e inserendo l’esperienza mistica
                                in una cornice canonica.</desc>
                        </category>

                        <category xml:id="legittimazione-liturgica">
                            <desc>Ricorso a formule, stilemi e registri liturgici come garanzia
                                devozionale e dottrinale, utile a circoscrivere affermazioni
                                speculative e a integrare il trattato nella tradizione della
                                preghiera ecclesiale.</desc>
                        </category>

                        <category xml:id="legittimazione-tradizione">
                            <desc>Appello a maestri della mistica (Teresa d’Avila, Giovanni della
                                Croce, Maria Maddalena de’ Pazzi) come legittimazione autorevole,
                                creando continuità con la genealogia carmelitana e rafforzando la
                                credibilità di un’autrice priva di formazione scolastica.</desc>
                        </category>
                    </category>

                    <category xml:id="pedagogia">
                        <desc>Strategie formative rivolte ad anime "incipienti", "proficienti" e
                            "perfette", basate su distinzioni operative, esemplificazioni concrete e
                            introduzione graduale ai concetti mistici, al fine di guidare il lettore
                            nel discernimento e prevenire errori dottrinali.</desc>

                        <category xml:id="pedagogia-introduzione">
                            <desc>Sezioni introduttive e inquadramenti che predispongono il lettore
                                all’orazione mentale e alla costruzione del “castello”, facendo leva
                                sull’obbedienza e sulla dichiarata umiltà dell’autrice.</desc>
                        </category>

                        <category xml:id="pedagogia-discernimento">
                            <desc>Distinzioni tra (1) "meditazione", (2) "contemplazione acquisita",
                                (3) "contemplazione infusa", (4) "quiete" e (5) "sospensione delle
                                potenze", con cui l’autrice chiarisce la progressione mistica e
                                aiuta il lettore-ascoltatore a riconoscere illusioni o inganni
                                spirituali.</desc>
                        </category>

                        <category xml:id="pedagogia-esemplificazione">
                            <desc>Uso di immagini quotidiane (acqua, mare, torrente, giardino,
                                specchio) e comparazioni che rendono intelligibili realtà
                                sovrasensibili, traducendo la teologia mistica in scenari
                                comprensibili anche a un pubblico poco istruito.</desc>
                        </category>
                    </category>

                    <category xml:id="rischio">
                        <desc>Insieme di strategie volte a prevenire o correggere letture
                            potenzialmente eterodosse, specialmente nei punti critici (ex: Libro
                            III), dove emergono concetti come "impeccabilità", "fusione con Dio",
                            "notte oscura" e perdita apparente del "libero arbitrio".</desc>

                        <category xml:id="rischio-attenuatio">
                            <desc>Glosse esplicative aggiunte per smorzare formulazioni rischiose,
                                spesso tramite “cioè”, “intendo dire”, “mi dichiaro”, con cui
                                l’autrice riduce ambiguità dottrinali.</desc>
                        </category>

                        <category xml:id="rischio-precisatio">
                            <desc>Limitazioni semantiche che delimitano concetti radicali (come
                                “divenir un altro Dio”, “sicurtà totale”), precisando che il libero
                                arbitrio non viene mai abolito e che l’azione resta sempre
                                divina.</desc>
                        </category>

                        <category xml:id="rischio-declaratio">
                            <desc>Dichiarazioni esplicite di adesione alla Chiesa e di rifiuto della
                                “molinia” (Molinos), formulate per disinnescare ogni sospetto di
                                quietismo e per riconfigurare enunciati pericolosi in senso
                                ortodosso.</desc>
                        </category>
                    </category>

                    <category xml:id="ethos">
                        <desc>Costruzione dell’immagine autoriale come donna ignorante, obbediente e
                            priva di lettere, che scrive per comando del confessore; strategia di
                            protezione che al contempo rivendica l’esperienza diretta come fonte
                            primaria di sapere mistico.</desc>

                        <category xml:id="ethos-umilta">
                            <desc>Professioni di "indegnità" e “ignoranza” per minimizzazione la
                                propria autorità, l'autrice usa queste formule per giustificare la
                                scrittura teologica da parte di una donna.</desc>
                        </category>

                        <category xml:id="ethos-esperienza">
                            <desc>Rivendicazione dell’esperienza (“non parlo senza l’esperienza”)
                                come fondamento epistemico che legittima il discorso spirituale in
                                mancanza di titoli di studio o di formazione teologica.</desc>
                        </category>

                        <category xml:id="ethos-obbedienza">
                            <desc>Insistenza sull’obbedienza al confessore (a scopo difensiovo),
                                vista come condizione necessaria per scrivere e come garanzia di
                                umiltà, prudenza e sottomissione dottrinale.</desc>
                        </category>
                    </category>

                </taxonomy>

                <!-- 2. Tassonomia dell’IMPATTO ESPLICATIVO -->
                <taxonomy xml:id="impact">
                    <category xml:id="impact-high">
                        <desc>Passaggi che chiariscono concetti dottrinali centrali (contemplazione
                            infusa, unione, quiete, notte dei sensi); decisivi per la comprensione
                            dell’opera e frequente oggetto di glosse prudenziali.</desc>
                    </category>
                    <category xml:id="impact-medium">
                        <desc>Elementi che rafforzano e integrano i concetti principali mediante
                            esempi, distinzioni e spiegazioni accessorie, senza modificarne
                            l’assetto teologico.</desc>
                    </category>
                    <category xml:id="impact-low">
                        <desc>Parti ornamentali o reiterative utili all’enfasi ma non decisive per
                            l’argomentazione teologica.</desc>
                    </category>
                    <category xml:id="impact-critical">
                        <desc>Nodi ad altissimo rischio interpretativo, come la trasformazione,
                            l’apparente "impeccabilità", la "sicurtà divina", la "sospensione delle
                            potenze" e la relazione fra volontà umana e azione divina.</desc>
                    </category>
                    <category xml:id="impact-supportive">
                        <desc>Supporti locali come glosse chiarificatrici, definizioni
                            terminologiche e citazioni brevi, che rendono intelligibili punti
                            complessi.</desc>
                    </category>
                    <category xml:id="impact-redundant">
                        <desc>Riprese iterative e amplificazioni che appesantiscono il discorso ma
                            ne confermano il significato senza aggiungere nuovi contenuti.</desc>
                    </category>
                    <category xml:id="impact-local">
                        <desc>Unità con effetto interpretativo limitato al paragrafo, impiegate per
                            chiarire concetti o casi specifici.</desc>
                    </category>
                    <category xml:id="impact-global">
                        <desc>Passaggi che influenzano l’interpretazione dell’intero capitolo o
                            libro, come introduzioni, transizioni e sommari interni.</desc>
                    </category>
                    <category xml:id="impact-structural">
                        <desc>Elementi portanti della struttura del trattato: passaggi di stato
                            dell’anima, principi organizzativi dei tre libri, gerarchie concettuali
                            delle virtù e delle potenze.</desc>
                    </category>
                </taxonomy>

                <!-- 3. Tassonomia del RISCHIO DOTTRINALE -->
                <taxonomy xml:id="risk">
                    <category xml:id="risk-dottrinale">
                        <desc>Rischio generale di equivocità su dottrine come "grazia", "libertà",
                            "unione" e "contemplazione", soprattutto nei punti dove la lingua
                            dell’autrice risulta ambigua o metaforicamente esasperata.</desc>
                    </category>
                    <category xml:id="risk-quietismo">
                        <desc>Possibile lettura quietista dei concetti di “quiete”, “otio”, “non
                            operare”, “abbandono totale”; rischio amplificato dal contesto storico e
                            dalle accuse processuali.</desc>
                    </category>
                    <category xml:id="risk-panteismo">
                        <desc>Rischio di interpretazione panteistica nelle espressioni sulla
                            “trasformatione” e sul “divenir un altro Dio”; necessità di glosse per
                            riaffermare la distinzione ontologica creatura/Creatore.</desc>
                    </category>
                    <category xml:id="risk-impeccabilita">
                        <desc>Ambiguità relative alla “sicurtà” mistica e alla percezione
                            dell’impossibilità di peccare nello stato di unione (impeccabilità);
                            richiede continui interventi mitiganti.</desc>
                    </category>
                    <category xml:id="risk-ambiguita">
                        <desc>Punti in cui la formulazione è oscura, metaforica o oscillante,
                            generando difficoltà interpretative non collocabili in categorie
                            specifiche.</desc>
                    </category>
                </taxonomy>

                <!-- 4. Tassonomia degli STATI MISTICI -->
                <taxonomy xml:id="mystic_state">
                    <category xml:id="mystic_state-unione">
                        <desc>Stato mistico di massimo avvicinamento a Dio, descritto con lessico
                            alto e analogie complesse; luogo delle maggiori ambiguità
                            teologiche.</desc>
                    </category>
                    <category xml:id="mystic_state-quiete">
                        <desc>Stato di sospensione delle potenze, spesso minacciato da
                            interpretazioni quietistiche; descritto come pace interiore infusa da
                            Dio.</desc>
                    </category>
                    <category xml:id="mystic_state-otium">
                        <desc>Ozio delle potenze inteso non come inerzia quietista, ma come
                            sospensione operata da Dio affinché l’anima riceva passivamente la
                            contemplazione infusa.</desc>
                    </category>
                    <category xml:id="mystic_state-sicurta">
                        <desc>Percezione di sicurezza spirituale (sicurtà) data da Dio nell’unione;
                            concetto altamente ambiguo e frequentemente oggetto di glosse
                            correttivo-esplicative.</desc>
                    </category>
                    <category xml:id="mystic_state-trasformazione">
                        <desc>Processo di assimilazione dell’anima a Dio, distinto dalla fusione
                            ontologica; caratterizzato da un linguaggio audace che richiede
                            precisazioni prudenziali.</desc>
                    </category>
                </taxonomy>

                <!-- 5. Tassonomia delle OPERAZIONI PRUDENZIALI -->
                <taxonomy xml:id="operation">
                    <category xml:id="operation-delimitazione">
                        <desc>Operazioni che circoscrivono semanticamente concetti rischiosi,
                            evitando letture estreme e gui­dando l’interpretazione entro limiti
                            ortodossi.</desc>
                    </category>
                    <category xml:id="operation-attenuatio">
                        <desc>Interventi che smorzano formulazioni troppo ardite mediante
                            spiegazioni aggiunte, spesso negli spazi marginali del
                            manoscritto.</desc>
                    </category>
                    <category xml:id="operation-precisatio">
                        <desc>Chiarimenti puntuali volti a definire meglio concetti ambigui, tipici
                            della riflessione autografa posteriore alla stesura iniziale.</desc>
                    </category>
                    <category xml:id="operation-declaratio">
                        <desc>Dichiarazioni dirette di ortodossia, con cui l’autrice esplicita la
                            propria adesione alla dottrina per evitare interpretazioni
                            sospette.</desc>
                    </category>
                    <category xml:id="operation-riequilibrio">
                        <desc>Interventi equilibranti che compensano un’affermazione rischiosa con
                            una precisazione ortodossa prima o dopo l’enunciato mistico.</desc>
                    </category>
                </taxonomy>

                <!-- 6. Tassonomia del LIVELLO DI ESPOSIZIONE -->
                <taxonomy xml:id="exposition">
                    <category xml:id="exposition-low">
                        <desc>Esposizione prudente di temi dottrinali, con ricorso limitato a
                            tecnicismi e metafore.</desc>
                    </category>
                    <category xml:id="exposition-medium">
                        <desc>Esposizione moderata di contenuti mistici, con appoggi occasionali a
                            citazioni e spiegazioni aggiuntive.</desc>
                    </category>
                    <category xml:id="exposition-high">
                        <desc>Esposizione intensa di dottrine mistiche complesse che richiedono
                            glosse, precisazioni e cautele retoriche.</desc>
                    </category>
                    <category xml:id="exposition-critical">
                        <desc>Livello massimo di esposizione dottrinale, tipico delle sezioni sul
                            matrimonio spirituale, la trasformazione e l’unione; punti fortemente a
                            rischio di censura.</desc>
                    </category>
                </taxonomy>

                <!-- 7. Tassonomia della FASE DISCORSIVA -->
                <taxonomy xml:id="phase">
                    <category xml:id="phase-introduction">
                        <desc>Segmenti introduttivi che stabiliscono tono, pubblico e obbedienza
                            iniziale, preparando la progressione mistica.</desc>
                    </category>
                    <category xml:id="phase-mediana">
                        <desc>Sezioni centrali in cui si analizzano stati intermedi del cammino
                            contemplativo, con esempi ed esperienze.</desc>
                    </category>
                    <category xml:id="phase-critical">
                        <desc>Passaggi dove emergono concetti teologicamente delicati, bisognosi di
                            glosse e interventi prudenziali.</desc>
                    </category>
                    <category xml:id="phase-conclusive">
                        <desc>Chiusure che ricapitolano i contenuti, riordinano la materia e
                            predispongono alla transizione verso stati più elevati.</desc>
                    </category>
                </taxonomy>

                <!-- 8. Tassonomia delle RELAZIONI -->
                <taxonomy xml:id="relation">
                    <category xml:id="relation-mistica-infusa-purificazione">
                        <desc>Relazione concettuale che descrive il passaggio dalle prove purgative
                            alla contemplazione infusa.</desc>
                    </category>
                    <category xml:id="relation-mistica-attiva-meditazione">
                        <desc>Relazione progressiva dalla meditazione attiva alla maturazione
                            spirituale che prepara alla contemplazione.</desc>
                    </category>
                    <category xml:id="relation-mistica-passiva-quiete">
                        <desc>Relazione tra contemplazione passiva e quiete, descritta come
                            sospensione delle potenze per opera di Dio.</desc>
                    </category>
                    <category xml:id="relation-mistica-unione-sposalitio">
                        <desc>Sequenza che conduce dall’unione allo sposalizio spirituale e alla
                            trasformazione, secondo i modelli mistici tradizionali.</desc>
                    </category>
                    <category xml:id="relation-causa-effetto">
                        <desc>Relazioni logiche che collegano prove, tribolazioni e grazie ai loro
                            esiti spirituali.</desc>
                    </category>
                    <category xml:id="relation-premessa-conseguenza">
                        <desc>Strutture deduttive che sorreggono spiegazioni teologiche, tipiche
                            della trattatistica mistica.</desc>
                    </category>
                    <category xml:id="relation-analogia">
                        <desc>Relazioni analogiche basate su comperazioni naturali o quotidiane per
                            spiegare realtà mistiche.</desc>
                    </category>
                    <category xml:id="relation-contrasto">
                        <desc>Opposizioni concettuali (buio/luce, guerra/pace) usate per chiarire
                            stati dell’anima e passaggi mistici.</desc>
                    </category>
                    <category xml:id="relation-intertesto-biblico">
                        <desc>Richiami espliciti o impliciti alla Scrittura che sostengono la
                            dottrina mistica.</desc>
                    </category>
                    <category xml:id="relation-intertesto-liturgico">
                        <desc>Riferimenti a testi, formule o registri liturgici che rinforzano il
                            tono devoto e la legittimità dell’opera.</desc>
                    </category>
                    <category xml:id="relation-intertesto-teresiano">
                        <desc>Risonanze e riprese del linguaggio e dei temi di Teresa d’Avila e
                            delle tradizioni carmelitane.</desc>
                    </category>
                    <category xml:id="relation-intertesto-molinista">
                        <desc>Affinità o divergenze rispetto al linguaggio della Guida di Molinos,
                            spesso tematizzate per prendere le distanze dal quietismo.</desc>
                    </category>
                </taxonomy>

            </classDecl>
        </encodingDesc>
    </teiHeader>

    <text>
        <body>
            <p>Il presente schema definisce le classi di metadati utilizzate per l'addestramento e
                la supervisione di modelli di IA applicati alla codifica TEI. Ogni categoria
                identifica un nodo concettuale specifico relativo agli stati mistici, ai rischi
                dottrinali e alle operazioni di riequilibrio testuale rilevate nel manoscritto di
                suor Teresa di San Geronimo.</p>
            <p>Il file esemplificativo è in taxonomy/esempi</p>
        </body>
    </text>

</TEI>
`;

        // ==================== DOCUMENTATION CONTENT ====================
        const documentationHTML = `
        <div class="fade-in" style="max-width: 800px; margin: 0 auto;">
            <h1 style="font-family: var(--font-serif); font-size: 1.8rem; color: var(--bg-sidebar); margin-bottom: 0.5rem;">Documentazione Tassonomia Prudenziale</h1>
            <p style="font-family: var(--font-serif); font-style: italic; color: var(--text-muted); margin-bottom: 2rem;">Modello TEI + IA per lo studio dell'intertestualità del <em>Castello dell'anima</em></p>
            
            <div style="background: var(--bg-paper); padding: 1.5rem; border-radius: 6px; border-left: 3px solid var(--accent-gold); margin-bottom: 2rem;">
                <h2 style="font-family: var(--font-serif); font-size: 1.1rem; color: var(--bg-sidebar); margin-bottom: 0.75rem;">Informazioni sul Progetto</h2>
                <table style="width: 100%; font-size: 0.85rem; line-height: 1.6;">
                    <tr><td style="padding: 0.3rem 0; color: var(--text-muted);">Autore:</td><td><strong>Luciano Longo</strong></td></tr>
                    <tr><td style="padding: 0.3rem 0; color: var(--text-muted);">Data V-0.1:</td><td>30 marzo 2026</td></tr>
                    <tr><td style="padding: 0.3rem 0; color: var(--text-muted);">Data V-1:</td><td>19 aprile 2026</td></tr>
                    <tr><td style="padding: 0.3rem 0; color: var(--text-muted);">Licenza:</td><td>
                        Creative Commons Attribution 4.0 International (CC BY 4.0) – Open Access
                        </td></tr>
                    <tr><td style="padding: 0.3rem 0; color: var(--text-muted);">Fonte:</td><td>Palermo, BCP, ms. 2 Qq E 29 (sec. XVII ex.)</td></tr>
                </table>
            </div>

            <h2 style="font-family: var(--font-serif); font-size: 1.3rem; color: var(--bg-sidebar); margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid var(--accent-gold);">Struttura della Tassonomia</h2>
            
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 1rem; margin-bottom: 2rem;">
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">1. Funzioni Retoriche</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Legittimazione, pedagogia, rischio, ethos</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">2. Impatto Prudenziale</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Valutazione dell'impatto dottrinale</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">3. Rischi Dottrinali</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Quietismo, panteismo, impeccabilità</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">4. Stati Mistici</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Unione, quiete, otium, sicurtà</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">5. Operazioni Prudenziali</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Delimitazione, attenuatio, precisatio</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">6. Livello Esposizione</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Bassa, media, alta, critica</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">7. Fase Discorsiva</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Iniziale, mediana, critica, conclusiva</p>
                </div>
                <div style="background: #fff; padding: 1rem; border-radius: 5px; border: 1px solid var(--border-color); box-shadow: var(--shadow-sm);">
                    <h3 style="font-family: var(--font-serif); font-size: 0.95rem; color: var(--accent-blue); margin-bottom: 0.5rem;">8. Relazioni</h3>
                    <p style="font-size: 0.8rem; color: var(--text-muted); line-height: 1.5;">Mistiche, argomentative, intertestuali</p>
                </div>
            </div>

            <h2 style="font-family: var(--font-serif); font-size: 1.3rem; color: var(--bg-sidebar); margin: 2rem 0 1rem; padding-bottom: 0.5rem; border-bottom: 2px solid var(--accent-gold);">Note Metodologiche</h2>
            <div style="font-family: var(--font-serif); font-size: 0.9rem; line-height: 1.7; color: var(--text-main); text-align: justify;">
                <p style="margin-bottom: 1rem;">Questa tassonomia è stata progettata come dispositivo interpretativo prudenziale
                a partire dal <em>Castello dell’anima</em> di Teresa di San Geronimo (sec. XVII),
                con l’obiettivo di rendere esplicite e formalmente controllabili le categorie
                ermeneutiche che intervengono nell’annotazione di un testo caratterizzato da
                elevata densità teologica e da potenziali ambiguità dottrinali.
                </p>

                <p style="margin-bottom: 1rem;">
                Il modello TEI adottato consente di articolare l’annotazione secondo più dimensioni
                tassonomiche distinte (funzioni interpretative, rischio dottrinale, operazioni
                prudenziali, impatto interpretativo), rendendo verificabili le strategie discorsive
                attraverso cui l’autrice costruisce e governa il proprio posizionamento entro i
                confini dell’ortodossia cattolica del XVII secolo.
                </p>

                <p style="margin-bottom: 1rem;">
                Per la descrizione dettagliata del modello, delle scelte di progettazione e dei
                meccanismi di governo formale, si rimanda alla documentazione metodologica allegata
                al repository, che costituisce il riferimento normativo per l’implementazione
                della tassonomia.
                </p>

                <p style="margin-bottom: 1rem;">
                La documentazione metodologica allegata al repository fornisce una descrizione
                analitica della tassonomia interpretativa, precisandone lo statuto epistemologico,
                l’architettura multi‑asse e i criteri di definizione delle categorie. In particolare,
                essa esplicita il razionale delle singole tassonomie (funzioni interpretative,
                rischio dottrinale, operazioni prudenziali, impatto interpretativo, stati mistici,
                relazioni e fasi discorsive), chiarendo in che modo ciascun asse contribuisca a
                modellare e governare l’atto ermeneutico.
                </p>
                <p style="margin-bottom: 1rem;">La stessa documentazione illustra inoltre le scelte di implementazione in ambiente
                TEI, la collocazione della tassonomia nel <code>teiHeader</code> come oggetto autonomo,
                nonché i meccanismi di governo formale basati su ODD, Relax NG e Schematron, che
                vincolano strutturalmente e semanticamente l’uso delle categorie. Tali materiali
                costituiscono pertanto il riferimento normativo e interpretativo per
                l’implementazione della tassonomia e per il suo impiego controllato nell’annotazione
                del testo.
                </p>
                <p style="margin-bottom: 1rem;">
                La descrizione completa della tassonomia interpretativa e dei suoi principi
                di governo è disponibile nel documento metodologico allegato al repository
                (<em>paper-tassonomia.md</em>), che costituisce il riferimento normativo e
                interpretativo per il modello qui rappresentato (vedi anche
                <a href="rel-html/documento_metodologico.pdf">Documentazione metodologica completa</a>)
                </p>

            </div>
        </div>`;

        // ==================== STATE ====================
        let parsedData = [];
        let currentTaxonomyId = null;
        let searchMode = false;
        let searchMatches = [];

        // ==================== DOM ELEMENTS ====================
        const taxonListEl = document.getElementById('taxon-list');
        const treeRootEl = document.getElementById('tree-root');
        const detailsContentEl = document.getElementById('details-content');
        const searchInput = document.getElementById('search-input');
        const resetSearchBtn = document.getElementById('reset-search');
        const searchInfoEl = document.getElementById('search-info');
        const searchCountEl = document.getElementById('search-count');

        // XML Modal elements
        const xmlModal = document.getElementById('xml-modal');
        const xmlContent = document.getElementById('xml-content');
        const closeXmlModalBtn = document.getElementById('close-xml-modal');
        const btnDownloadXml = document.getElementById('btn-download-xml');
        const btnExternalXml = document.getElementById('btn-external-xml');
        const btnCopyXml = document.getElementById('btn-copy-xml');
        const xmlStats = document.getElementById('xml-stats');

        // Documentation Modal elements
        const docModal = document.getElementById('doc-modal');
        const docContent = document.getElementById('doc-content');
        const closeDocModalBtn = document.getElementById('close-doc-modal');
        const btnDownloadDoc = document.getElementById('btn-download-doc');

        // Toast
        const toast = document.getElementById('toast');
        const toastMessage = document.getElementById('toast-message');

        // Names mapping for UI
        const friendlyNames = {
            'func': '1. Funzioni retoriche',
            'impact': '2. Impatto prudenziale',
            'risk': '3. Rischio dottrinale',
            'mystic_state': '4. Stati mistici',
            'operation': '5. Operazioni prudenziali',
            'exposition': '6. Livello di esposizione',
            'phase': '7. Fase discorsiva',
            'relation': '8. Relazioni Intertestuali',
        };

        // ==================== PARSER ====================
        function parseXML(xmlStr) {
            const parser = new DOMParser();
            const xmlDoc = parser.parseFromString(xmlStr, "text/xml");
            const taxonomies = xmlDoc.querySelectorAll("taxonomy");
            const result = [];

            taxonomies.forEach(tax => {
                const id = tax.getAttribute("xml:id");
                const categories = [];

                const cats = Array.from(tax.children).filter(n => n.nodeName === "category");

                cats.forEach(cat => {
                    const catId = cat.getAttribute("xml:id");
                    const descNode = cat.querySelector("desc");
                    const descText = descNode ? descNode.textContent.trim() : "Nessuna descrizione disponibile.";

                    const getSubCats = (parent) => {
                        const subs = [];
                        const subNodes = Array.from(parent.children).filter(n => n.nodeName === "category");
                        subNodes.forEach(sub => {
                            const subId = sub.getAttribute("xml:id");
                            const subDescNode = sub.querySelector("desc");
                            const subDesc = subDescNode ? subDescNode.textContent.trim() : "";
                            subs.push({
                                id: subId,
                                desc: subDesc,
                                children: getSubCats(sub),
                                parent: parent.getAttribute("xml:id")
                            });
                        });
                        return subs;
                    };

                    categories.push({
                        id: catId,
                        desc: descText,
                        children: getSubCats(cat),
                        parent: id
                    });
                });

                result.push({
                    id: id,
                    name: friendlyNames[id] || id.toUpperCase(),
                    categories: categories
                });
            });
            return result;
        }

        // ==================== XML SYNTAX HIGHLIGHTER ====================
        function highlightXML(xml) {
            let escaped = xml
                .replace(/&/g, '&amp;')
                .replace(/</g, '&lt;')
                .replace(/>/g, '&gt;');

            escaped = escaped.replace(/(&lt;!--[\s\S]*?--&gt;)/g, '<span class="xml-comment">$1</span>');
            escaped = escaped.replace(/(&lt;\?xml[\s\S]*?\?&gt;)/g, '<span class="xml-declaration">$1</span>');
            escaped = escaped.replace(/(&lt;\?[\s\S]*?\?&gt;)/g, '<span class="xml-declaration">$1</span>');

            escaped = escaped.replace(/(&lt;\/?)([\w:-]+)((?:\s+[\w:-]+(?:\s*=\s*(?:"[^"]*"|'[^']*'))?)*)\s*(\/?&gt;)/g,
                function (match, open, tag, attrs, close) {
                    const highlightedAttrs = attrs.replace(
                        /([\w:-]+)(\s*=\s*)("[^"]*"|'[^']*')/g,
                        '<span class="xml-attr">$1</span>$2<span class="xml-attr-value">$3</span>'
                    );
                    return `<span class="xml-tag">${open}${tag}</span>${highlightedAttrs}<span class="xml-tag-close">${close}</span>`;
                });

            const lines = escaped.split('\n');
            return lines.map(line => `<div class="xml-line">${line || '&nbsp;'}</div>`).join('');
        }

        // ==================== RENDERERS ====================
        function init() {
            parsedData = parseXML(xmlString);
            renderSidebar();

            if (parsedData.length > 0) {
                loadTaxonomy(parsedData[0].id);
            }
        }

        function renderSidebar() {
            taxonListEl.innerHTML = '';
            parsedData.forEach(tax => {
                const li = document.createElement('li');
                li.className = 'taxon-item';
                li.dataset.id = tax.id;

                const countNodes = (cats) => {
                    let count = cats.length;
                    cats.forEach(c => {
                        if (c.children) count += countNodes(c.children);
                    });
                    return count;
                };

                const totalNodes = countNodes(tax.categories);

                li.innerHTML = `
                <span>${tax.name}</span>
                <span class="taxon-count">${totalNodes}</span>
            `;
                li.onclick = () => {
                    resetSearch();
                    loadTaxonomy(tax.id);
                };
                taxonListEl.appendChild(li);
            });
        }

        function loadTaxonomy(id) {
            currentTaxonomyId = id;
            searchMode = false;
            searchInfoEl.classList.remove('active');

            document.querySelectorAll('.taxon-item').forEach(el => {
                if (el.dataset.id === id) el.classList.add('active');
                else el.classList.remove('active');
            });

            const taxData = parsedData.find(t => t.id === id);
            if (!taxData) return;

            treeRootEl.innerHTML = '';
            const rootContainer = document.createElement('div');
            rootContainer.className = 'tree-container fade-in';

            const title = document.createElement('h2');
            title.className = 'tree-header';
            title.innerHTML = `${taxData.name} <span>${taxData.categories.length} categorie</span>`;
            rootContainer.appendChild(title);

            taxData.categories.forEach(cat => {
                rootContainer.appendChild(createTreeNode(cat, true));
            });

            treeRootEl.appendChild(rootContainer);
            detailsContentEl.innerHTML = createPlaceholderHTML('Seleziona un nodo per i dettagli.');
        }

        function createTreeNode(nodeData, isRoot = false, isSearchResult = false) {
            const hasChildren = nodeData.children && nodeData.children.length > 0;

            const nodeEl = document.createElement('div');
            nodeEl.className = `tree-node ${isRoot ? 'root' : ''}`;
            nodeEl.dataset.nodeId = nodeData.id;

            const contentEl = document.createElement('div');
            contentEl.className = 'node-content';
            if (isSearchResult) contentEl.classList.add('search-match');

            const toggleBtn = document.createElement('div');
            toggleBtn.className = `toggle-btn ${hasChildren ? '' : 'hidden'}`;
            toggleBtn.innerHTML = '▶';
            contentEl.appendChild(toggleBtn);

            const labelEl = document.createElement('div');
            labelEl.className = 'node-label';
            labelEl.textContent = formatLabel(nodeData.id);
            contentEl.appendChild(labelEl);

            const idEl = document.createElement('span');
            idEl.className = 'node-id';
            idEl.textContent = nodeData.id;
            contentEl.appendChild(idEl);

            nodeEl.appendChild(contentEl);

            if (hasChildren) {
                const childrenContainer = document.createElement('div');
                childrenContainer.className = 'children-container';

                nodeData.children.forEach(child => {
                    childrenContainer.appendChild(createTreeNode(child, false, isSearchResult));
                });

                nodeEl.appendChild(childrenContainer);

                contentEl.onclick = (e) => {
                    e.stopPropagation();
                    const isOpen = childrenContainer.classList.contains('open');
                    if (isOpen) {
                        childrenContainer.classList.remove('open');
                        toggleBtn.classList.remove('rotated');
                    } else {
                        childrenContainer.classList.add('open');
                        toggleBtn.classList.add('rotated');
                    }
                    showDetails(nodeData);
                };
            } else {
                contentEl.onclick = (e) => {
                    e.stopPropagation();
                    showDetails(nodeData);
                };
            }

            return nodeEl;
        }

        function formatLabel(id) {
            return id.replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase());
        }

        function showDetails(data) {
            document.querySelectorAll('.node-content').forEach(el => el.classList.remove('selected'));

            detailsContentEl.innerHTML = `
            <div class="details-header fade-in">
                <div class="details-title">${formatLabel(data.id)}</div>
                <div class="details-id">ID: ${data.id}</div>
            </div>
            <div class="details-body fade-in">
                <div class="details-section">
                    <div class="details-section-title">Definizione</div>
                    <div class="details-desc">${data.desc}</div>
                </div>
                ${data.children && data.children.length > 0 ? `
                <div class="details-section">
                    <div class="details-section-title">Sotto-categorie (${data.children.length})</div>
                    <ul class="subcategories-list">
                        ${data.children.map(c => `<li>${formatLabel(c.id)}</li>`).join('')}
                    </ul>
                </div>
                ` : ''}
                <div class="details-section">
                    <div class="details-section-title">Tassonomia</div>
                    <div class="details-desc" style="font-family: var(--font-mono); font-size: 0.8rem;">
                        ${data.parent || 'root'}
                    </div>
                </div>
            </div>
        `;
        }

        function createPlaceholderHTML(text) {
            return `
            <div class="placeholder-panel fade-in">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5">
                    <circle cx="12" cy="12" r="10"/>
                    <path d="M12 16v-4M12 8h.01"/>
                </svg>
                <p>${text}</p>
            </div>
        `;
        }

        // ==================== SEARCH ====================
        function performSearch(term) {
            term = term.toLowerCase().trim();

            if (!term) {
                resetSearch();
                return;
            }

            searchMode = true;
            searchMatches = [];

            parsedData.forEach(tax => {
                const findMatches = (nodes, taxonomyId) => {
                    nodes.forEach(node => {
                        const idMatch = node.id.toLowerCase().includes(term);
                        const descMatch = node.desc.toLowerCase().includes(term);
                        const labelMatch = formatLabel(node.id).toLowerCase().includes(term);

                        if (idMatch || descMatch || labelMatch) {
                            searchMatches.push({
                                ...node,
                                taxonomy: taxonomyId,
                                taxonomyName: friendlyNames[taxonomyId] || taxonomyId
                            });
                        }

                        if (node.children && node.children.length > 0) {
                            findMatches(node.children, taxonomyId);
                        }
                    });
                };
                findMatches(tax.categories, tax.id);
            });

            searchCountEl.textContent = searchMatches.length;
            searchInfoEl.classList.add('active');

            treeRootEl.innerHTML = '';
            const rootContainer = document.createElement('div');
            rootContainer.className = 'tree-container fade-in';

            const title = document.createElement('h2');
            title.className = 'tree-header';
            title.innerHTML = `Risultati ricerca <span>"${term}"</span>`;
            rootContainer.appendChild(title);

            if (searchMatches.length === 0) {
                const noResults = document.createElement('div');
                noResults.style.cssText = 'text-align: center; padding: 3rem; color: var(--text-muted); font-family: var(--font-serif); font-style: italic;';
                noResults.textContent = 'Nessun risultato trovato.';
                rootContainer.appendChild(noResults);
            } else {
                const grouped = {};
                searchMatches.forEach(match => {
                    if (!grouped[match.taxonomy]) {
                        grouped[match.taxonomy] = [];
                    }
                    grouped[match.taxonomy].push(match);
                });

                Object.keys(grouped).forEach(taxId => {
                    const taxGroup = document.createElement('div');
                    taxGroup.style.marginBottom = '1.5rem';

                    const groupTitle = document.createElement('h3');
                    groupTitle.style.cssText = 'font-family: var(--font-serif); font-size: 1rem; color: var(--accent-blue); margin-bottom: 0.75rem; padding-bottom: 0.4rem; border-bottom: 1px solid var(--border-color);';
                    groupTitle.textContent = friendlyNames[taxId] || taxId;
                    taxGroup.appendChild(groupTitle);

                    grouped[taxId].forEach(match => {
                        taxGroup.appendChild(createTreeNode(match, true, true));
                    });

                    rootContainer.appendChild(taxGroup);
                });
            }

            treeRootEl.appendChild(rootContainer);
            detailsContentEl.innerHTML = createPlaceholderHTML('Seleziona un risultato per i dettagli.');
        }

        function resetSearch() {
            searchInput.value = '';
            searchMode = false;
            searchInfoEl.classList.remove('active');
            if (currentTaxonomyId) {
                loadTaxonomy(currentTaxonomyId);
            }
        }

        // ==================== MODAL FUNCTIONS ====================
        function openXmlModal() {
            const highlighted = highlightXML(xmlString);
            xmlContent.innerHTML = highlighted;

            const lineCount = xmlString.split('\n').length;
            const sizeKB = (new Blob([xmlString]).size / 1024).toFixed(2);
            xmlStats.textContent = `${lineCount} linee • ${sizeKB} KB`;

            const blob = new Blob([xmlString], { type: 'application/xml' });
            const blobUrl = URL.createObjectURL(blob);
            btnDownloadXml.href = blobUrl;
            btnExternalXml.href = blobUrl;

            xmlModal.classList.add('active');
        }

        function closeXmlModal() {
            xmlModal.classList.remove('active');
        }

        function openDocModal() {
            docContent.innerHTML = documentationHTML;
            docModal.classList.add('active');
        }

        function closeDocModal() {
            docModal.classList.remove('active');
        }

        function copyXmlToClipboard() {
            navigator.clipboard.writeText(xmlString).then(() => {
                showToast('XML copiato negli appunti!');
            }).catch(() => {
                showToast('Errore nella copia');
            });
        }

        function showToast(message) {
            toastMessage.textContent = message;
            toast.classList.add('show');
            setTimeout(() => {
                toast.classList.remove('show');
            }, 3000);
        }

        // ==================== EVENT LISTENERS ====================
        let searchTimeout;
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            searchTimeout = setTimeout(() => {
                performSearch(e.target.value);
            }, 300);
        });

        resetSearchBtn.addEventListener('click', () => {
            resetSearch();
            searchInput.focus();
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape') {
                if (searchInput.value && !xmlModal.classList.contains('active') && !docModal.classList.contains('active')) {
                    resetSearch();
                    searchInput.blur();
                } else if (xmlModal.classList.contains('active')) {
                    closeXmlModal();
                } else if (docModal.classList.contains('active')) {
                    closeDocModal();
                }
            }
        });

        // XML Modal events
        document.getElementById('open-xml-viewer').addEventListener('click', (e) => {
            e.preventDefault();
            openXmlModal();
        });

        closeXmlModalBtn.addEventListener('click', closeXmlModal);

        xmlModal.addEventListener('click', (e) => {
            if (e.target === xmlModal) {
                closeXmlModal();
            }
        });

        btnCopyXml.addEventListener('click', copyXmlToClipboard);

        // Documentation Modal events
        document.getElementById('open-doc-viewer').addEventListener('click', (e) => {
            e.preventDefault();
            openDocModal();
        });

        closeDocModalBtn.addEventListener('click', closeDocModal);

        docModal.addEventListener('click', (e) => {
            if (e.target === docModal) {
                closeDocModal();
            }
        });

        // ==================== START ====================
        init();