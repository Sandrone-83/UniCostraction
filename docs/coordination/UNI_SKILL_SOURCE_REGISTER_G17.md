# UniCostraction — Registro fonti della Skill Library G17

Questo registro elenca fonti primarie o documentazione ufficiale utilizzabili per
progettare skill originali per AuraTrix/AulaFIX. Non è una copia delle fonti, non
è una certificazione di conformità professionale e non sostituisce la verifica
della versione vigente al momento dell'uso.

## Regola di utilizzo

Ogni skill deve separare:

1. procedura originale di UniCostraction;
2. riferimento esterno e versione/URL;
3. stato di licenza e diritti di redistribuzione;
4. controlli che richiedono un professionista abilitato o una pubblica amministrazione;
5. output prodotto dall'assistente e materiale che può essere solo una bozza.

Non sono ammessi copia-incolla di manuali, norme, standard, template proprietari,
capitolati, formulari o codice non compatibile con la licenza del repository.

## Registro

| ID | Area | Fonte ufficiale | Utilizzo ammesso nella skill | Diritti / stato |
|---|---|---|---|---|
| SRC-BSI-IFC | BIM/openBIM | https://technical.buildingsmart.org/standards/ifc/ | Terminologia, versioning IFC, schema di verifica e scambio | Standard pubblicato con licenza indicata da buildingSMART; citare e verificare la versione. Non incorporare il testo ISO. |
| SRC-BSI-SERVER | BIM/openBIM | https://standards.buildingsmart.org/ | IFC, IDS, BCF, MVD e servizi ufficiali da usare come riferimenti operativi | Riferimento ufficiale; diritti specifici per ciascun artefatto da verificare prima di redistribuire file o estratti. |
| SRC-BSI-VALIDATION | BIM/QA | https://technical.buildingsmart.org/standards/ifc/ | Progettare gate di validazione IFC e controlli di interoperabilità | Il servizio e la documentazione sono fonte esterna; la skill descrive il processo senza replicare il servizio. |
| SRC-BLENDER-MANUAL | 3D/render | https://docs.blender.org/ | Modellazione, scene, rendering, gestione asset e troubleshooting | Documentazione ufficiale; non copiare capitoli. Scrivere procedure originali e collegare la versione usata. |
| SRC-BLENDER-API | 3D/automation | https://docs.blender.org/api/main/index.html | Automazione Python, accesso a dati, operatori, bmesh, mathutils e controlli di riproducibilità | API/documentazione di terzi; gli script UniCostraction devono avere licenza esplicita e test locali. |
| SRC-AUTODESK-DOTNET | CAD/AutoCAD | https://help.autodesk.com/cloudhelp/2025/ENU/OARX-DevGuide-Managed/files/GUID-4E1AAFA9-740E-4097-800C-CAED09CDFF12.htm | Automazione controllata di disegni, database CAD, comandi e plugin .NET | Documentazione proprietaria di riferimento; non redistribuire manuali o SDK. Richiedere installazione/licenza Autodesk per esecuzione reale. |
| SRC-FREECAD | CAD/BIM | https://github.com/FreeCAD/FreeCAD | Modellazione parametrica, API e workflow riproducibili in ambiente open source | Il repository dichiara LGPL-2.1; verificare la licenza dei singoli componenti e degli asset. |
| SRC-IFCOS | BIM/IFC | https://github.com/IfcOpenShell/IfcOpenShell | Parsing, authoring, geometry, IDS/BCF, query e automazione IFC | Repository con componenti LGPL/GPL; ogni integrazione deve conservare gli avvisi di licenza e non confondere supporto software con conformità del modello. |
| SRC-IFCOS-DOCS | BIM/automation | https://docs.ifcopenshell.org/ | API Python, validazione e casi d'uso per modelli IFC | Documentazione di riferimento; codice nuovo originale, testato e con licenza del progetto UniCostraction. |
| SRC-BONSAI | BIM/Blender | https://extensions.blender.org/add-ons/bonsai/ | Workflow IFC nativo in Blender, classificazione, proprietà e documenti | Add-on di terzi; verificare licenze/versione prima di distribuire. |
| SRC-FFMPEG | video/media | https://ffmpeg.org/documentation.html | Transcoding, probe, mux/demux, filtri, controllo codec e QA media | FFmpeg ha condizioni di licenza dipendenti dalla build/configurazione; consultare LICENSE/legal prima di redistribuire. |
| SRC-KDENLIVE | video/media | https://docs.kdenlive.org/en/ | Montaggio, asset management, timeline, audio, titoli, export e troubleshooting | Manuale ufficiale del progetto; procedure originali, nessuna copia massiva. |
| SRC-NORMATTIVA-380 | urbanistica/edilizia | https://www.normattiva.it/atto/caricaDettaglioAtto?atto.articolo.numero=0&atto.codiceRedazionale=001G0429 | Mappa di titoli abilitativi, procedimenti edilizi, vigilanza e normativa tecnica | Fonte legislativa ufficiale; testo soggetto a vigenza e aggiornamenti. La skill non dà pareri legali e deve indicare data di verifica. |
| SRC-ANAC-DLGS36 | appalti/PA | https://www.anticorruzione.it/-/faq.codice.contratti-d.lgs.36.2023%3B | Orientamento procedurale su codice contratti, PCP e quesiti applicativi | FAQ/atti ufficiali da verificare per aggiornamento; non trasformare l'esempio in consulenza o garanzia di aggiudicazione. |
| SRC-MIT-BIM | BIM/appalti | https://www.mit.gov.it/node/21814 | Gestione informativa digitale e applicazione BIM nel ciclo dei contratti pubblici | Linee guida e atti ufficiali; verificare data, allegati e regime transitorio. |
| SRC-ADE-CATASTO | catasto | https://assistenzaipocat.agenziaentrate.gov.it/ | Pregeo, Docfa, consultazione e flussi catastali da trasformare in checklist | Servizi ufficiali; l'adempimento è riservato ai soggetti e alle modalità previste, con verifica dell'ufficio competente. |
| SRC-ADE-PREGEO | catasto | https://swdownload1.agenziaentrate.gov.it/pub/pregeo/guidapregeo10_01032011.pdf | Struttura concettuale e controlli di qualità per aggiornamento cartografico | Guida ufficiale storica: verificare versione e attualità prima di usarla come riferimento operativo. |
| SRC-ADE-DOCFA | catasto | https://agenziaentrate.gov.it/portale/web/guest/schede/fabbricatiterreni/aggiornamento-catasto-fabbricati-docfa/docfa-versioni-precedenti/software-docfa-4003 | Riconoscimento del workflow Docfa e dei requisiti software | Versione storica: non presentarla come requisito corrente senza controllo live. |
| SRC-EU-EPBD | energia/edifici | https://eur-lex.europa.eu/eli/dir/2024/1275/oj/ita | Concetti e obblighi europei su prestazione energetica degli edifici | Fonte UE da leggere nella versione vigente e nel recepimento nazionale; non sostituisce il diritto italiano applicabile. |

## Fonti G18 da verificare nella revisione delle skill

| ID | Area | Fonte ufficiale | Utilizzo ammesso nella skill | Diritti / stato |
|---|---|---|---|---|
| SRC-JRC-EUROCODES | strutture/metodi | https://eurocodes.jrc.ec.europa.eu/en-eurocodes | Mappa delle famiglie Eurocodici, ambiti di applicazione, NDP e differenza fra guida e testo normativo | JRC è fonte istituzionale; gli Eurocodici restano standard CEN con diritti propri. Non copiare il testo. |
| SRC-ILO-CONSTRUCTION-SAFETY | sicurezza internazionale | https://www.ilo.org/resource/other/safety-and-health-construction-revised-edition | Contesto comparativo per sistemi di gestione OSH e prevenzione dei rischi di cantiere | Codice ILO da citare e usare secondo i termini della pubblicazione; non sostituisce D.Lgs. 81/2008 o norme locali. |
| SRC-UNEP-BUILDINGS-GSR | ambiente/clima | https://wedocs.unep.org/entities/publication/dd0a1d99-dba3-46da-93ab-ef2a26fc3c14 | Dati e indicatori globali su edifici, materiali, energia, resilienza e decarbonizzazione | Pubblicazione istituzionale con licenza indicata nella scheda; verificare eccezioni e usare dati con anno/edizione. |
| SRC-JRC-EUROCODES-FAQ | strutture/licensing | https://eurocodes.jrc.ec.europa.eu/faq | Esplicitare nella skill che JRC non redistribuisce gli standard e che l'accesso al testo dipende dagli enti CEN/NSB | Riferimento di licensing; non è autorizzazione alla copia o alla redistribuzione. |

## Stati di provenienza

- `reference_only`: la skill può collegare la fonte, ma nessun testo esterno è
  stato importato nel corpus.
- `license_review`: la fonte o l'artefatto richiede verifica puntuale prima di
  essere copiato o redistribuito.
- `source_backed_procedure`: la procedura UniCostraction è originale e la fonte
  primaria è identificata, ma l'output deve ancora essere verificato sul caso reale.
- `professional_review_required`: l'esecuzione o la firma richiede tecnico,
  legale, impresa, RUP, ufficio pubblico o altro soggetto competente.

## Nota anti-errore

Un URL ufficiale dimostra l'identità del riferimento, non la completezza del
corpus né la correttezza automatica della skill. Norme, prezzi, software, versioni
e procedure amministrative cambiano: la libreria deve registrare la data di
verifica e degradare a `needs_review` quando non può confermare l'attualità.
