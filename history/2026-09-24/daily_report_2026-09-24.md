# Daily scanner — release 4.0.0

- run_id: `20260924T213001Z` · market_session_date: 2026-09-24 · generato: 2026-09-24T23:47:51+02:00
- engine_git_sha: `e1821abf25675c474f156b37078880ebddc5c972` · run_status: **COMPLETE**
- Classic 3.9.0 (riferimento, sezione seguente invariata) · Expansion 0.1.0 (SIGNALS) · intraday: ATTIVO_OSSERVAZIONE_DIFFERITA

---
# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-24
- generated_at: 2026-09-24T23:46:41+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 741.10 | 711.88 | 4.104 | +/-0.50% | 664.99 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26939.36 | 26145.79 | 3.035 | +/-0.50% | 24624.66 | true | sopra il buffer superiore |

## Scanner

- universe_count: 521
- analyzed_count: 72
- passed_count: 2
- excluded_count: 519

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 2
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 12

Dati insufficienti:
- 12 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 2 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| STX | Seagate Technology Holdings Plc | 905.92 | 57.23 | 5.70 | 0.80 | 11.93 | true | NORMAL | 48.49 | 149.17 |
| MRVL | Marvell Technology Inc | 258.95 | 62.00 | 5.32 | 0.62 | 15.85 | true | NORMAL | 36.55 | 49.42 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| STX | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| MRVL | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |

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

### STX
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

### MRVL
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

Storico insufficiente: 12
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 112 | 200 | 1776346200 | 1790256600 |
| BSP | 60 | 200 | 1782912600 | 1790256600 |
| FRVO | 93 | 200 | 1778679000 | 1790256600 |
| HONA | 71 | 200 | 1781530200 | 1790256600 |
| INIO | 78 | 200 | 1780579800 | 1790256600 |
| IOND | 42 | 200 | 1785245400 | 1790256600 |
| LFTO | 78 | 200 | 1780579800 | 1790256600 |
| MWH | 156 | 200 | 1770820200 | 1790256600 |
| QNT | 78 | 200 | 1780579800 | 1790256600 |
| SHAZ | 152 | 200 | 1771425000 | 1790256600 |
| SPCX | 72 | 200 | 1781271000 | 1790256600 |
| XE | 105 | 200 | 1777296600 | 1790256600 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-24
- benchmark autorevole: QQQ (ultima barra 2026-09-24)
  - IXIC: 2026-09-24
  - QQQ: 2026-09-24
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-24, coincidente con la seduta attesa

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
- adr: 24
- biotech_pre_revenue: 18
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 521
- esclusioni strutturali 42
- sopravvissuti 479
- identita' verificata: si
- funnel completo: 521 = 42 + 407 + 12 + 58 + 2 + 0 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## SEC / DILUTION - DIAGNOSTICA SHADOW

Il percorso legacy di enforcement e' invariato durante il freeze. Le classificazioni seguenti migliorano la spiegazione ma non modificano selezione, audit o operativita'.

### STX

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-07-31 (55 giorni), entro la freschezza
- fact shadow selezionato: 2026-07-31
- confronto 6M: 3.9305%
- motivo: confronto 2026-01-27 -> 2026-07-31: intervallo 185 giorni
- fatti rifiutati:
  - 2026-01-27 val=218073067.0 form=10-Q eta=240 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE

### MRVL

Filing:
- 424B5 del 2026-04-06 (accession 0001193125-26-142958)
  - security: non disponibile
  - tipo security: UNKNOWN
  - transazione: UNKNOWN
  - classificazione diagnostica: AMBIGUOUS_REQUIRES_REVIEW (confidenza LOW)
  - questione aperta: nessun testo del prospetto disponibile: security description, natura primary/resale e numero di azioni non sono determinabili dai soli metadati
  - questione aperta: il form da solo non stabilisce il tipo di security

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-08-21 (34 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-21
- confronto 6M: 0.2974%
- motivo: confronto 2026-03-04 -> 2026-08-21: intervallo 170 giorni
- fatti rifiutati:
  - 2026-03-04 val=874300000.0 form=10-K eta=204 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: AMBIGUOUS_REQUIRES_REVIEW
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- BLOCKED_AMBIGUOUS_CLASSIFICATION
- esito operativo invariato: local_status FAIL, blocks_final_setup True
- differenze legacy/shadow: LEGACY_FORM_ONLY_CLASSIFICATION


## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| LSCC | 60.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 0.63 | 55.92 | 5.27 | 26.82 |
| SNDK | 60.00 | fallisce il gate within_25pct_52w_high | within_25pct_52w_high | 0.76 | 56.19 | 18.43 | 30.06 |
| ALAB | 54.00 | fallisce il gate within_25pct_52w_high | within_25pct_52w_high | 0.86 | 63.61 | 27.55 | 38.55 |

## Funnel

- **idonei totali: 2** = shortlist 2 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 521
- esclusioni strutturali: -42 → 479
- esclusioni fondamentali: -407 → 72 allo stadio tecnico
- esclusioni tecniche: -70
- **shortlist: 2** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 271, eps_growth 67, operating_margin 39, eps_next_year 29, price_above_sma50 27.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 271 |
| eps_growth | 67 |
| operating_margin | 39 |
| eps_next_year | 29 |
| price_above_sma50 | 27 |
| altri gate | 74 |
| **esclusi da un gate** | **507** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 12
- errori runtime            : 0
- promossi                  : 2
- idonei fuori cap          : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 42 |
| FUNDAMENTAL_EXCLUSION | 407 |
| DATA_INSUFFICIENT | 12 |
| TECHNICAL_EXCLUSION | 58 |
| PROMOTED | 2 |
| ELIGIBLE_NOT_SHORTLISTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **521** |
| universo iniziale | 521 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + eligible_not_shortlisted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### STX
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: POTENTIAL_DILUTION
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-27 -> 2026-07-31 · intervallo 185 g (target 180, scarto 5) · corrente vecchia di 55 g · variazione +3.931% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 176.000.000 USD (al 2026-07-03)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### MRVL
- stato locale: **FAIL** — verifica locale diluizione fallita. Controllo responsabile: equity offering.
- classificazione: POTENTIAL_DILUTION
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-03-04 -> 2026-08-21 · intervallo 170 g (target 180, scarto 10) · corrente vecchia di 34 g · variazione +0.297% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 400.000.000 USD (al 2026-08-01)
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: sotto-controlli falliti: recent_equity_offering_check. Esito negativo accertato localmente

Storico proprietario `shares_outstanding.jsonl`: 520 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-24T23:30:12+02:00 -> 2026-09-24T23:46:41+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-24T23:30:34+02:00 (finviz_mcp_status: NOT_CONFIGURED)

---

## Expansion shadow — EXPANSION_SHADOW_V1 0.1.0

- mode: **SHADOW_DAILY_OHLC**, execution_verified=**false** (piani condizionali su barre daily, non ingressi verificati dal vivo, non istruzioni d'ordine Fineco)
- stato profilo: **SIGNALS**
- ledger: PROSPECTIVE · cohort_id: `EXPANSION_SHADOW_V1-PROSPECTIVE-2026-09-17-802a3409-ea1129c5`
- protocol_hash: `802a3409633f2bac82559314fedf8ead775c41178508d6e7bbb207d63571f6c2` · adapter_hash: `ea1129c5d705604a0fe4d696b900ed0b77bdc5e06bebdf490ba44834c4da332b`
- universo: NASDAQ_COMMON_PRE_CLASSIC (prima dei gate Classic; non deriva da scanner_v3, eligible o review_queue)
- Contabilita' separata dal Classic: non modifica technical_ready_total, actionable_total ne' final_setup_ready.

### Funnel Expansion

- righe sorgente: 797 · membri unici: 797 · position_updates: 0
- riconciliato: True (somma esiti terminali 797)
- non valutabili: 1 (0.0013; soglia pausa 0.05)

| esito terminale | n |
|---|---:|
| NOT_EVALUABLE_DATA_UNAVAILABLE | 1 |
| OUT_OF_PERIMETER_INSTRUMENT_TYPE | 44 |
| SIGNAL_ADMITTED | 3 |
| SIGNAL_EXCLUDED_PORTFOLIO_CAP | 4 |
| SIGNAL_GATES_FAILED | 466 |
| SIGNAL_PLAN_REJECTED_SIZE_ZERO | 1 |
| SIGNAL_PLAN_REJECTED_STOP_TOO_WIDE | 1 |
| STRUCTURAL_FILTER_FAILED | 277 |

Fallimenti per gate (non esclusivi, non sommabili): PRICE=77, CAP=0, LIQUIDITY=208, RETURN=716, RANGE=683, VOLUME=671, CLOSE_LOCATION=507, GREEN_BODY=348

### Piani condizionali per la prossima seduta (2026-09-25)

PIANI CONDIZIONALI SHADOW_DAILY_OHLC — validi solo nella seduta indicata; fill modellato max(open, trigger)×1,001; target = 2R dal fill (nessun TP1/TP2, nessun Entry Ideal).

| # | ticker | trigger | stop | tetto open T+1 | qty virtuale | rischio USD peggior fill | RVOL20 | TR/A14 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | CDNA | 63.19 | 54.31 | 65.41 | 2 | 22.34 | 2.15 | 4.22 |
| 2 | VCYT | 49.06 | 43.30 | 50.49 | 3 | 21.74 | 2.06 | 2.58 |
| 3 | RVMD | 201.62 | 189.16 | 204.74 | 1 | 15.78 | 1.96 | 1.68 |

Il tetto e' un vincolo dell'OPEN del modello daily (open sopra il tetto o <= stop: piano annullato), non un Entry Max per ordini intraday.

Segnali non ammessi: ICLR (PORTFOLIO_CAP), ADPT (PORTFOLIO_CAP), TEM (PORTFOLIO_CAP), TXG (PORTFOLIO_CAP), GRAL (STOP_TOO_WIDE), TWST (SIZE_ZERO)

### Contabilita' shadow e contatore

- stato ledger: **OBSERVING** · max drawdown R: 1.23 (kill a 6.0R)
- trade entrati: 3/30 · chiusi: 3 · aperti: 0 · piani pending: 3
- date d'ingresso distinte: 2/10 · sedute valide: 6/90
- somma R netta: 0.086 · media R: 0.029 · PF_R: 1.07 (FINITE) · win rate: 0.33
- equity R (EOD, marks inclusi): 0.086 · P&L realizzato USD: 1.85 · equity virtuale USD: 10001.85
- trade ambigui (barra daily): 0
- attivazione: 2026-09-17T10:55:59.605535+00:00 · prima T0 ammessa: 2026-09-17
- Nessuna conclusione economica prima di 30 trade chiusi; posizioni aperte e segnali scaduti non sono 0R.

  - chiusa TEM: 2026-09-18→2026-09-24 TIME_EXIT, net_R -0.045, PnL USD -0.84
  - chiusa ILMN: 2026-09-18→2026-09-24 TIME_EXIT, net_R 1.284, PnL USD 22.25
  - chiusa VKTX: 2026-09-23→2026-09-24 GAP_STOP, net_R -1.154, PnL USD -19.56

---

## Stato intraday (monitor separato, ciclo 15 minuti)

- stato: **ATTIVO_OSSERVAZIONE_DIFFERITA** — APERTA · esito: CANDIDATI_OSSERVATI · lista vuota: False
- ultimo tentativo: 2026-09-24T14:15:04.490Z · ultimo ciclo riuscito: 2026-09-24T14:15:04.490Z · candidati: {'classic_idonei': ['MRVL', 'SNDK', 'STX'], 'esplorativi': [], 'expansion': ['ILMN', 'TEM', 'VKTX']} · ritardo max rilevazione s: None
- ultima seduta: 2026-09-24 · cicli completati: 4 · ultimo ciclo: 2026-09-24T14:15:04.490Z
- feed: ALPACA_SIP_1Min_RITARDATO_15_MIN · alert operativo: BLOCCATO: FEED_SIP_RITARDATO_15_MINUTI, VERIFICA_TEMPESTIVA_DEL_TRIGGER_NON_DISPONIBILE, PIANO_SHADOW_DAILY_OHLC_NON_OPERATIVO, CANALE_DI_NOTIFICA_AUTORIZZATO_NON_CONFIGURATO
- ritardo effettivo dei dati s (min/max): 904/904 · durata ultimo ciclo s: 15.3 · richieste: 12 (+0 sottoprocesso), HTTP 429: 0
- setup qualificati nell'ultimo ciclo: discovery 0/0, expansion 0/0 · canale Telegram: ATTIVO · esiti avvisi: {}
- verifica tempestiva del trigger: NON_DISPONIBILE: nessuno stream consolidato autorizzato (DDE Fineco solo per id confermati e presidiato; IEX = una sede)
- scoperta esplorativa: ATTIVA
- stato esportato il: 2026-09-24T14:15:19.387Z
- Gli esiti intraday sono separati e non modificano fill, stop o campione del daily.

### Scoperta: riepilogo della seduta (provvisorio)

- candidati unici: **0** (ricorrenze ciclo×ticker 0, non sono titoli distinti) · setup qualificati unici: **0**
- candidati per ciclo: 15:30=0, 15:45=0, 16:00=0, 16:15=0
- ultimo motivo osservato per ticker: nessuno
- setup qualificati nella seduta (conservati anche se l'ultimo ciclo non li qualifica): nessuno
- esclusioni tecniche attendibili (dati omogenei, percorso discovery 1.1.0): nessuna
- non valutabili per integrita' dei dati (verdetto del motore conservato, avvisi impediti): nessuno
- ultimo ciclo: idonei Classic 3, piani Expansion 0, posizioni 3, barre nuove 90, eventi nuovi 0
- dettaglio: `stato_30m\riepilogo_seduta_2026-09-24.json` (locale, non pubblicato)

