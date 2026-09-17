# Daily scanner — release 4.0.0

- run_id: `20260917T220619Z` · market_session_date: 2026-09-17 · generato: 2026-09-18T00:08:06+02:00
- engine_git_sha: `afbdfefe903d1b3c5c2db931f1783907821a9420` · run_status: **COMPLETE**
- Classic 3.9.0 (riferimento, sezione seguente invariata) · Expansion 0.1.0 (SIGNALS) · intraday: SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA

---
# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-17
- generated_at: 2026-09-17T23:47:28+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 716.92 | 709.99 | 0.976 | +/-0.50% | 662.08 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26418.29 | 26065.26 | 1.354 | +/-0.50% | 24536.97 | true | sopra il buffer superiore |

## Scanner

- universe_count: 528
- analyzed_count: 73
- passed_count: 1
- excluded_count: 527

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 1
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 13

Dati insufficienti:
- 13 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 1 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| AMD | Advanced Micro Devices Inc | 545.09 | 62.78 | 4.48 | 1.60 | 7.27 | true | NORMAL | 50.11 | 158.80 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| AMD | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |

Conteggi diagnostici, disgiunti dalle metriche preesistenti:

- strutture teoriche breakout : 0
- strutture teoriche pullback : 0
- trade plan validi           : 0
- trade plan invalidi         : 0
- BREAKOUT_READY validi       : 0
- PULLBACK_READY validi       : 0
- executable                  : 0
- not executable              : 0

Nessun BREAKOUT_READY valido.
Nessun PULLBACK_READY valido.


## DIAGNOSTICA STOP - SOLO OSSERVAZIONE

Questi dati sono diagnostici e non modificano stop, selezione o operativita'.

### AMD
- ancora utilizzata: NOT_AVAILABLE / n/d
- eta ancora: n/d
- structural support: n/d
- contraction low: n/d (NOT_APPLICABLE)
- finestra della base: n/d
- stop trigger: n/d
- distanza dal close: n/d% / n/d ATR
- distanza dall'entry (n/d): n/d% / n/d ATR
- structural support vs contraction low: n/d (n/d%, n/d ATR)
- osservazione: ANCHOR_NOT_COMPARABLE
- esito piano invariato: NOT_APPLICABLE - TOO_FAR_FROM_ACTIONABLE_PIVOT

Una sola seduta non conferma ne' smentisce alcuna ipotesi sull'ancoraggio dello stop: queste righe servono ad accumulare osservazioni.


## QUALITA' E SUFFICIENZA DEI DATI

Storico insufficiente: 13
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 107 | 200 | 1776346200 | 1789651800 |
| BSP | 55 | 200 | 1782912600 | 1789651800 |
| FRVO | 88 | 200 | 1778679000 | 1789651800 |
| HONA | 66 | 200 | 1781530200 | 1789651800 |
| INIO | 73 | 200 | 1780579800 | 1789651800 |
| IOND | 37 | 200 | 1785245400 | 1789651800 |
| LFTO | 73 | 200 | 1780579800 | 1789651800 |
| MFP | 57 | 200 | 1782739800 | 1789651800 |
| MWH | 151 | 200 | 1770820200 | 1789651800 |
| QNT | 73 | 200 | 1780579800 | 1789651800 |
| SHAZ | 147 | 200 | 1771425000 | 1789651800 |
| SPCX | 67 | 200 | 1781271000 | 1789651800 |
| XE | 100 | 200 | 1777296600 | 1789651800 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-17
- benchmark autorevole: QQQ (ultima barra 2026-09-17)
  - IXIC: 2026-09-17
  - QQQ: 2026-09-17
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-17, coincidente con la seduta attesa

Il controllo non tocca gate, soglie, score, regime o promozione: decide soltanto se il run vale come osservazione.


## DEFINIZIONE DELL'UNIVERSO

Provider:
- Finviz (Finviz via finvizfinance screener views)
- exchange: NASDAQ
- filtri applicati dal provider: Average Volume, Exchange, Industry, Market Cap., Price

Soglie:
- prezzo minimo: 15.0
- market cap minimo: 2000000000
- market cap massimo: NON CONFIGURATO
- volume medio minimo: 750000

Issuer e strumenti:
- ADR: esclusi
- FPI: temporaneamente non supportati, esclusi dopo i gate sui soli idonei
- biotech pre-revenue: esclusi
- common stock only: non verificabile
- ETF e fondi: esclusi alla fonte
- warrant e unit: non verificabile
- nota: il provider non espone un campo security_type: l'universo non puo' essere dichiarato common-stock-only

Applicazione:
- filtri provider: exchange, price_min, market_cap_min, avg_volume_min, instrument_scope
- filtri locali: etf_etn_cef, spac_shell, adr, warrant_preferred, biotech_pre_revenue, foreign_private_issuer

Esclusioni osservabili:
- adr: 25
- biotech_pre_revenue: 21
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 528
- esclusioni strutturali 46
- sopravvissuti 482
- identita' verificata: si
- funnel completo: 528 = 46 + 409 + 13 + 59 + 1 + 0 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## SEC / DILUTION - DIAGNOSTICA SHADOW

Il percorso legacy di enforcement e' invariato durante il freeze. Le classificazioni seguenti migliorano la spiegazione ma non modificano selezione, audit o operativita'.

### AMD

Filing:
- 424B5 del 2026-08-14 (accession 0001193125-26-352628)
  - security: non disponibile
  - tipo security: UNKNOWN
  - transazione: UNKNOWN
  - classificazione diagnostica: AMBIGUOUS_REQUIRES_REVIEW (confidenza LOW)
  - questione aperta: nessun testo del prospetto disponibile: security description, natura primary/resale e numero di azioni non sono determinabili dai soli metadati
  - questione aperta: il form da solo non stabilisce il tipo di security
- 424B5 del 2026-08-13 (accession 0001193125-26-348029)
  - security: non disponibile
  - tipo security: UNKNOWN
  - transazione: UNKNOWN
  - classificazione diagnostica: AMBIGUOUS_REQUIRES_REVIEW (confidenza LOW)
  - questione aperta: nessun testo del prospetto disponibile: security description, natura primary/resale e numero di azioni non sono determinabili dai soli metadati
  - questione aperta: il form da solo non stabilisce il tipo di security

Shelf:
- capacita' potenziale di emissione (S-3ASR del 2026-08-13)
- nessuna emissione provata dalla shelf da sola

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-07-29 (50 giorni), entro la freschezza
- fact shadow selezionato: 2026-07-29
- confronto 6M: 0.1266%
- motivo: confronto 2026-01-30 -> 2026-07-29: intervallo 180 giorni
- fatti rifiutati:
  - 2026-01-30 val=1630410843.0 form=10-K eta=230 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: AMBIGUOUS_REQUIRES_REVIEW
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: si
- BLOCKED_AMBIGUOUS_CLASSIFICATION
- esito operativo invariato: local_status FAIL, blocks_final_setup True
- differenze legacy/shadow: LEGACY_FORM_ONLY_CLASSIFICATION


## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| MRVL | 70.00 | fallisce il gate within_25pct_52w_high | within_25pct_52w_high | 0.88 | 56.78 | 11.46 | 24.61 |
| MU | 60.00 | fallisce il gate rsi14 | rsi14 | 0.89 | 53.81 | 3.91 | 28.39 |
| INCY | 42.00 | fallisce il gate atr_pct | atr_pct | 1.13 | 57.66 | 3.36 | 3.90 |

## Funnel

- **idonei totali: 1** = shortlist 1 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 528
- esclusioni strutturali: -46 → 482
- esclusioni fondamentali: -409 → 73 allo stadio tecnico
- esclusioni tecniche: -72
- **shortlist: 1** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 274, eps_growth 67, price_above_sma50 41, operating_margin 36, eps_next_year 32.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 274 |
| eps_growth | 67 |
| price_above_sma50 | 41 |
| operating_margin | 36 |
| eps_next_year | 32 |
| altri gate | 64 |
| **esclusi da un gate** | **514** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 13
- errori runtime            : 0
- promossi                  : 1
- idonei fuori cap          : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 46 |
| FUNDAMENTAL_EXCLUSION | 409 |
| DATA_INSUFFICIENT | 13 |
| TECHNICAL_EXCLUSION | 59 |
| PROMOTED | 1 |
| ELIGIBLE_NOT_SHORTLISTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **528** |
| universo iniziale | 528 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + eligible_not_shortlisted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### AMD
- stato locale: **FAIL** — verifica locale diluizione fallita. Controllo responsabile: equity offering.
- classificazione: POTENTIAL_DILUTION
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-30 -> 2026-07-29 · intervallo 180 g (target 180, scarto 0) · corrente vecchia di 50 g · variazione +0.127% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 221.000.000 USD (al 2026-06-27)
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — shelf registration presente: capacita' potenziale di emissione, nessuna emissione dimostrata
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: sotto-controlli falliti: recent_equity_offering_check. Esito negativo accertato localmente

Storico proprietario `shares_outstanding.jsonl`: 527 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-17T23:30:09+02:00 -> 2026-09-17T23:47:28+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-17T23:30:36+02:00 (finviz_mcp_status: NOT_CONFIGURED)

---

## Expansion shadow — EXPANSION_SHADOW_V1 0.1.0

- mode: **SHADOW_DAILY_OHLC**, execution_verified=**false** (piani condizionali su barre daily, non ingressi verificati dal vivo, non istruzioni d'ordine Fineco)
- stato profilo: **SIGNALS**
- ledger: PROSPECTIVE · cohort_id: `EXPANSION_SHADOW_V1-PROSPECTIVE-2026-09-17-802a3409-ea1129c5`
- protocol_hash: `802a3409633f2bac82559314fedf8ead775c41178508d6e7bbb207d63571f6c2` · adapter_hash: `ea1129c5d705604a0fe4d696b900ed0b77bdc5e06bebdf490ba44834c4da332b`
- universo: NASDAQ_COMMON_PRE_CLASSIC (prima dei gate Classic; non deriva da scanner_v3, eligible o review_queue)
- Contabilita' separata dal Classic: non modifica technical_ready_total, actionable_total ne' final_setup_ready.

### Funnel Expansion

- righe sorgente: 807 · membri unici: 807 · position_updates: 0
- riconciliato: True (somma esiti terminali 807)
- non valutabili: 2 (0.0025; soglia pausa 0.05)

| esito terminale | n |
|---|---:|
| NOT_EVALUABLE_DATA_UNAVAILABLE | 2 |
| OUT_OF_PERIMETER_INSTRUMENT_TYPE | 44 |
| SIGNAL_ADMITTED | 3 |
| SIGNAL_EXCLUDED_PORTFOLIO_CAP | 2 |
| SIGNAL_GATES_FAILED | 450 |
| SIGNAL_PLAN_REJECTED_SIZE_ZERO | 1 |
| SIGNAL_PLAN_REJECTED_STOP_TOO_WIDE | 1 |
| STRUCTURAL_FILTER_FAILED | 304 |

Fallimenti per gate (non esclusivi, non sommabili): PRICE=74, CAP=0, LIQUIDITY=236, RETURN=657, RANGE=674, VOLUME=651, CLOSE_LOCATION=634, GREEN_BODY=494

### Piani condizionali per la prossima seduta (2026-09-18)

PIANI CONDIZIONALI SHADOW_DAILY_OHLC — validi solo nella seduta indicata; fill modellato max(open, trigger)×1,001; target = 2R dal fill (nessun TP1/TP2, nessun Entry Ideal).

| # | ticker | trigger | stop | tetto open T+1 | qty virtuale | rischio USD peggior fill | RVOL20 | TR/A14 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | TEM | 81.50 | 72.18 | 83.83 | 2 | 23.46 | 2.01 | 2.62 |
| 2 | TSEM | 221.86 | 210.93 | 224.59 | 1 | 13.88 | 1.86 | 1.77 |
| 3 | ILMN | 247.23 | 232.05 | 251.02 | 1 | 19.22 | 1.79 | 1.90 |

Il tetto e' un vincolo dell'OPEN del modello daily (open sopra il tetto o <= stop: piano annullato), non un Entry Max per ordini intraday.

Segnali non ammessi: SMCI (PORTFOLIO_CAP), APLD (PORTFOLIO_CAP), NTRA (SIZE_ZERO), SDGR (STOP_TOO_WIDE)

### Contabilita' shadow e contatore

- stato ledger: **OBSERVING** · max drawdown R: 0.00 (kill a 6.0R)
- trade entrati: 0/30 · chiusi: 0 · aperti: 0 · piani pending: 3
- date d'ingresso distinte: 0/10 · sedute valide: 1/90
- somma R netta: 0 · media R: n/d · PF_R: n/d (NO_OUTCOMES) · win rate: n/d
- equity R (EOD, marks inclusi): 0.000 · P&L realizzato USD: 0 · equity virtuale USD: 10000.00
- trade ambigui (barra daily): 0
- attivazione: 2026-09-17T10:55:59.605535+00:00 · prima T0 ammessa: 2026-09-17
- Nessuna conclusione economica prima di 30 trade chiusi; posizioni aperte e segnali scaduti non sono 0R.


---

## Stato intraday (monitor separato, ciclo 15 minuti)

- stato: **SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA** — FUORI_SESSIONE · esito: CANDIDATI_OSSERVATI · lista vuota: False
- ultimo tentativo: 2026-09-17T21:00:03.350Z · ultimo ciclo riuscito: 2026-09-17T20:30:03.628Z · candidati: {'classic_idonei': [], 'esplorativi': ['ABEO', 'ABSI', 'ACRS', 'AEMD', 'AGNC', 'ALHC', 'ALVO', 'ARQT', 'ASST', 'ATRC', 'BIAF', 'CAI', 'CBC', 'COCO', 'CROX', 'CRSP', 'CTKB', 'DAIC', 'DFDV', 'DRVN', 'EBAY', 'ELMT', 'ELVN', 'FANG', 'FRNM', 'FTRE', 'GENB', 'GFS', 'GRAL', 'HBAN', 'HELP', 'HNRG', 'HONA', 'IBRX', 'ILMN', 'IMMR', 'INIO', 'JBHT', 'LTRX', 'MATW', 'MBLY', 'MGNI', 'NAMS', 'NAVI', 'NEOG', 'NVAX', 'OCTV', 'ON', 'OPCH', 'PGEN', 'PHVS', 'PUBM', 'PURR', 'PWP', 'RARE', 'RUM', 'SDGR', 'SNDX', 'STLN', 'TEM', 'TH', 'TWST', 'VERA', 'VICR', 'VITL', 'ZYME'], 'expansion': []} · ritardo max rilevazione s: None
- ultima seduta: 2026-09-17 · cicli completati: 29 · ultimo ciclo: 2026-09-17T20:30:03.628Z
- feed: ALPACA_SIP_1Min_RITARDATO_15_MIN · alert operativo: BLOCCATO: FEED_SIP_RITARDATO_15_MINUTI, VERIFICA_TEMPESTIVA_DEL_TRIGGER_NON_DISPONIBILE, PIANO_SHADOW_DAILY_OHLC_NON_OPERATIVO, CANALE_DI_NOTIFICA_AUTORIZZATO_NON_CONFIGURATO
- ritardo effettivo dei dati s (min/max): 1803/1803 · durata ultimo ciclo s: 33.1 · richieste: 14 (+5 sottoprocesso), HTTP 429: 0
- setup qualificati nell'ultimo ciclo: discovery 0/0, expansion 0/0 · canale Telegram: NON_CONFIGURATO · esiti avvisi: {}
- verifica tempestiva del trigger: NON_DISPONIBILE: nessuno stream consolidato autorizzato (DDE Fineco solo per id confermati e presidiato; IEX = una sede)
- scoperta esplorativa: ATTIVA
- stato esportato il: 2026-09-17T21:13:57.517Z
- Gli esiti intraday sono separati e non modificano fill, stop o campione del daily.

### Scoperta: riepilogo della seduta (definitivo)

- candidati unici: **69** (ricorrenze ciclo×ticker 303, non sono titoli distinti) · setup qualificati unici: **0**
- candidati per ciclo: 15:30=0, 15:45=0, 16:00=2, 16:15=3, 16:30=2, 16:45=3, 17:00=5, 17:15=5, 17:30=5, 17:45=6, 18:00=6, 18:15=7, 18:30=8, 18:45=7, 19:00=7, 19:15=6, 19:30=6, 19:45=8, 20:00=8, 20:15=8, 20:30=9, 20:45=8, 21:00=8, 21:15=13, 21:30=15, 21:45=17, 22:00=23, 22:15=42, 22:30=66
- ultimo motivo osservato per ticker: DATI_MANCANTI/VERIFICA_ESPLORATIVA=66, SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=2, SETUP_ASSENTE/STOP_TOO_WIDE=1
- setup qualificati nella seduta (conservati anche se l'ultimo ciclo non li qualifica): nessuno
- esclusioni tecniche attendibili (dati omogenei, percorso discovery 1.1.0): DATI_MANCANTI/VERIFICA_ESPLORATIVA=66, SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=2, SETUP_ASSENTE/STOP_TOO_WIDE=1
- non valutabili per integrita' dei dati (verdetto del motore conservato, avvisi impediti): nessuno · osservati non omogenei in almeno un ciclo: AEMD (6 cicli, 4 eventi), BIAF (6 cicli, 2 eventi), DAIC (4 cicli, 1 eventi) · integrita' non accertata nell'ultimo stato: 69 ticker
- ultimo ciclo: idonei Classic 0, piani Expansion 0, posizioni 0, barre nuove 8441, eventi nuovi 0
- dettaglio: `stato_30m\riepilogo_seduta_2026-09-17.json` (locale, non pubblicato)

