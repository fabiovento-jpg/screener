# Daily scanner — release 4.0.0

- run_id: `20260921T213001Z` · market_session_date: 2026-09-21 · generato: 2026-09-21T23:49:07+02:00
- engine_git_sha: `e1821abf25675c474f156b37078880ebddc5c972` · run_status: **COMPLETE**
- Classic 3.9.0 (riferimento, sezione seguente invariata) · Expansion 0.1.0 (SIGNALS) · intraday: SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA

---
# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-21
- generated_at: 2026-09-21T23:47:54+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 741.47 | 710.27 | 4.393 | +/-0.50% | 663.20 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 27122.08 | 26088.38 | 3.962 | +/-0.50% | 24571.74 | true | sopra il buffer superiore |

## Scanner

- universe_count: 528
- analyzed_count: 74
- passed_count: 3
- excluded_count: 525

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 3
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 13

Dati insufficienti:
- 13 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 3 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| MU | Micron Technology Inc | 1043.96 | 61.24 | 4.71 | 1.10 | 20.22 | true | NORMAL | 345.72 | 1372.09 |
| SNDK | Sandisk Corp | 1766.64 | 59.77 | 6.52 | 0.96 | 32.91 | true | NORMAL | 371.59 | 28016.32 |
| MRVL | Marvell Technology Inc | 257.38 | 62.42 | 5.70 | 0.96 | 16.56 | true | NORMAL | 36.55 | 49.42 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| MU | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| SNDK | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
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

### MU
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

### SNDK
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

Storico insufficiente: 13
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 109 | 200 | 1776346200 | 1789997400 |
| BSP | 57 | 200 | 1782912600 | 1789997400 |
| FRVO | 90 | 200 | 1778679000 | 1789997400 |
| HONA | 68 | 200 | 1781530200 | 1789997400 |
| INIO | 75 | 200 | 1780579800 | 1789997400 |
| IOND | 39 | 200 | 1785245400 | 1789997400 |
| LFTO | 75 | 200 | 1780579800 | 1789997400 |
| MFP | 59 | 200 | 1782739800 | 1789997400 |
| MWH | 153 | 200 | 1770820200 | 1789997400 |
| QNT | 75 | 200 | 1780579800 | 1789997400 |
| SHAZ | 149 | 200 | 1771425000 | 1789997400 |
| SPCX | 69 | 200 | 1781271000 | 1789997400 |
| XE | 102 | 200 | 1777296600 | 1789997400 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-21
- benchmark autorevole: QQQ (ultima barra 2026-09-21)
  - IXIC: 2026-09-21
  - QQQ: 2026-09-21
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-21, coincidente con la seduta attesa

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
- adr: 26
- biotech_pre_revenue: 19
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 528
- esclusioni strutturali 45
- sopravvissuti 483
- identita' verificata: si
- funnel completo: 528 = 45 + 409 + 13 + 58 + 3 + 0 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## SEC / DILUTION - DIAGNOSTICA SHADOW

Il percorso legacy di enforcement e' invariato durante il freeze. Le classificazioni seguenti migliorano la spiegazione ma non modificano selezione, audit o operativita'.

### MU

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-06-17 (96 giorni), entro la freschezza
- fact shadow selezionato: 2026-06-17
- confronto 6M: 0.3451%
- motivo: confronto 2025-12-10 -> 2026-06-17: intervallo 189 giorni
- fatti rifiutati:
  - 2025-12-10 val=1125509261.0 form=10-Q eta=285 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE

### SNDK

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-08-07 (45 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-07
- confronto 6M: -0.7781%
- motivo: confronto 2026-01-23 -> 2026-08-07: intervallo 196 giorni
- fatti rifiutati:
  - 2026-01-23 val=147567249.0 form=10-Q eta=241 motivi=STALE_BEYOND_FRESHNESS_LIMIT

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
- fact legacy: 2026-08-21 (31 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-21
- confronto 6M: 0.2974%
- motivo: confronto 2026-03-04 -> 2026-08-21: intervallo 170 giorni
- fatti rifiutati:
  - 2026-03-04 val=874300000.0 form=10-K eta=201 motivi=STALE_BEYOND_FRESHNESS_LIMIT

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
| STX | 60.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 1.16 | 55.04 | 3.19 | 26.63 |
| SMTC | 48.00 | fallisce il gate performance_21d | performance_21d | 1.23 | 62.57 | 42.03 | 4.56 |
| IBKR | 42.00 | fallisce il gate rsi14 | rsi14 | 0.86 | 54.08 | 3.74 | 5.94 |

## Funnel

- **idonei totali: 3** = shortlist 3 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 528
- esclusioni strutturali: -45 → 483
- esclusioni fondamentali: -409 → 74 allo stadio tecnico
- esclusioni tecniche: -71
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 273, eps_growth 68, operating_margin 37, eps_next_year 31, price_above_sma50 30.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 273 |
| eps_growth | 68 |
| operating_margin | 37 |
| eps_next_year | 31 |
| price_above_sma50 | 30 |
| altri gate | 73 |
| **esclusi da un gate** | **512** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 13
- errori runtime            : 0
- promossi                  : 3
- idonei fuori cap          : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 45 |
| FUNDAMENTAL_EXCLUSION | 409 |
| DATA_INSUFFICIENT | 13 |
| TECHNICAL_EXCLUSION | 58 |
| PROMOTED | 3 |
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

### MU
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: NORMAL_SBC
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2025-12-10 -> 2026-06-17 · intervallo 189 g (target 180, scarto 9) · corrente vecchia di 96 g · variazione +0.345% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 650.000.000 USD (al 2026-05-28)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### SNDK
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: BUYBACK
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-23 -> 2026-08-07 · intervallo 196 g (target 180, scarto 16) · corrente vecchia di 45 g · variazione -0.778% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 4.524.000.000 USD (al 2026-07-03)
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
  - misura: 2026-03-04 -> 2026-08-21 · intervallo 170 g (target 180, scarto 10) · corrente vecchia di 31 g · variazione +0.297% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 400.000.000 USD (al 2026-08-01)
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
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

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-21T23:30:10+02:00 -> 2026-09-21T23:47:54+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-21T23:30:34+02:00 (finviz_mcp_status: NOT_CONFIGURED)

---

## Expansion shadow — EXPANSION_SHADOW_V1 0.1.0

- mode: **SHADOW_DAILY_OHLC**, execution_verified=**false** (piani condizionali su barre daily, non ingressi verificati dal vivo, non istruzioni d'ordine Fineco)
- stato profilo: **SIGNALS**
- ledger: PROSPECTIVE · cohort_id: `EXPANSION_SHADOW_V1-PROSPECTIVE-2026-09-17-802a3409-ea1129c5`
- protocol_hash: `802a3409633f2bac82559314fedf8ead775c41178508d6e7bbb207d63571f6c2` · adapter_hash: `ea1129c5d705604a0fe4d696b900ed0b77bdc5e06bebdf490ba44834c4da332b`
- universo: NASDAQ_COMMON_PRE_CLASSIC (prima dei gate Classic; non deriva da scanner_v3, eligible o review_queue)
- Contabilita' separata dal Classic: non modifica technical_ready_total, actionable_total ne' final_setup_ready.

### Funnel Expansion

- righe sorgente: 806 · membri unici: 806 · position_updates: 0
- riconciliato: True (somma esiti terminali 806)
- non valutabili: 2 (0.0025; soglia pausa 0.05)

| esito terminale | n |
|---|---:|
| NOT_EVALUABLE_DATA_UNAVAILABLE | 2 |
| OUT_OF_PERIMETER_INSTRUMENT_TYPE | 46 |
| SIGNAL_ADMITTED | 1 |
| SIGNAL_EXCLUDED_PORTFOLIO_CAP | 7 |
| SIGNAL_GATES_FAILED | 467 |
| SIGNAL_PLAN_REJECTED_SIZE_ZERO | 3 |
| SIGNAL_PLAN_REJECTED_STOP_TOO_WIDE | 1 |
| STRUCTURAL_FILTER_FAILED | 279 |

Fallimenti per gate (non esclusivi, non sommabili): PRICE=74, CAP=0, LIQUIDITY=210, RETURN=672, RANGE=695, VOLUME=686, CLOSE_LOCATION=536, GREEN_BODY=396

### Piani condizionali per la prossima seduta (2026-09-22)

PIANI CONDIZIONALI SHADOW_DAILY_OHLC — validi solo nella seduta indicata; fill modellato max(open, trigger)×1,001; target = 2R dal fill (nessun TP1/TP2, nessun Entry Ideal).

| # | ticker | trigger | stop | tetto open T+1 | qty virtuale | rischio USD peggior fill | RVOL20 | TR/A14 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | WBD | 30.94 | 29.62 | 31.27 | 14 | 23.52 | 12.51 | 9.54 |

Il tetto e' un vincolo dell'OPEN del modello daily (open sopra il tetto o <= stop: piano annullato), non un Entry Max per ordini intraday.

Segnali non ammessi: SHOP (PORTFOLIO_CAP), FIVN (PORTFOLIO_CAP), FSLY (PORTFOLIO_CAP), INOD (PORTFOLIO_CAP), RMBS (PORTFOLIO_CAP), LUNR (PORTFOLIO_CAP), AKAM (PORTFOLIO_CAP), ALAB (SIZE_ZERO), AMD (SIZE_ZERO), GRAL (STOP_TOO_WIDE), META (SIZE_ZERO)

### Contabilita' shadow e contatore

- stato ledger: **OBSERVING** · max drawdown R: 1.23 (kill a 6.0R)
- trade entrati: 2/30 · chiusi: 0 · aperti: 2 · piani pending: 1
- date d'ingresso distinte: 1/10 · sedute valide: 3/90
- somma R netta: 0 · media R: n/d · PF_R: n/d (NO_OUTCOMES) · win rate: n/d
- equity R (EOD, marks inclusi): -1.231 · P&L realizzato USD: 0 · equity virtuale USD: 9977.95
- trade ambigui (barra daily): 0
- attivazione: 2026-09-17T10:55:59.605535+00:00 · prima T0 ammessa: 2026-09-17
- Nessuna conclusione economica prima di 30 trade chiusi; posizioni aperte e segnali scaduti non sono 0R.

  - aperta TEM: ingresso 2026-09-18 a 81.58, stop 72.18, target 100.38, qty 2, mark 78.03, sedute 2
  - aperta ILMN: ingresso 2026-09-18 a 249.38, stop 232.05, target 284.03, qty 1, mark 238.82, sedute 2
  - evento EXPIRED MSTR: OPEN_ABOVE_CEILING

---

## Stato intraday (monitor separato, ciclo 15 minuti)

- stato: **SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA** — FUORI_SESSIONE · esito: CANDIDATI_OSSERVATI · lista vuota: False
- ultimo tentativo: 2026-09-21T21:00:04.258Z · ultimo ciclo riuscito: 2026-09-21T20:30:05.154Z · candidati: {'classic_idonei': ['AMD', 'MU', 'SNDK'], 'esplorativi': ['AEP', 'ALHC', 'ALKS', 'ALMU', 'AMD', 'AMRX', 'ARM', 'ASST', 'AUR', 'AVBP', 'BNC', 'COGT', 'COIN', 'CRDO', 'CRML', 'DFDV', 'DNLI', 'FSLY', 'FWDI', 'GEMI', 'GRAL', 'GRML', 'GRPN', 'HELP', 'INTC', 'LBTYA', 'LBTYK', 'META', 'MSTR', 'NAMS', 'NEOG', 'NICE', 'NNE', 'NUAI', 'SDGR', 'SFD', 'SHEN', 'SHOP', 'SRRK', 'TTAN', 'VEEE', 'VITL', 'VKTX', 'VNET', 'VOR', 'VRSN', 'WBD'], 'expansion': ['ILMN', 'MSTR', 'TEM']} · ritardo max rilevazione s: None
- ultima seduta: 2026-09-21 · cicli completati: 29 · ultimo ciclo: 2026-09-21T20:30:05.154Z
- feed: ALPACA_SIP_1Min_RITARDATO_15_MIN · alert operativo: BLOCCATO: FEED_SIP_RITARDATO_15_MINUTI, VERIFICA_TEMPESTIVA_DEL_TRIGGER_NON_DISPONIBILE, PIANO_SHADOW_DAILY_OHLC_NON_OPERATIVO, CANALE_DI_NOTIFICA_AUTORIZZATO_NON_CONFIGURATO
- ritardo effettivo dei dati s (min/max): 1805/1805 · durata ultimo ciclo s: 34.1 · richieste: 14 (+4 sottoprocesso), HTTP 429: 0
- setup qualificati nell'ultimo ciclo: discovery 0/47, expansion 0/1 · canale Telegram: ATTIVO · esiti avvisi: {}
- verifica tempestiva del trigger: NON_DISPONIBILE: nessuno stream consolidato autorizzato (DDE Fineco solo per id confermati e presidiato; IEX = una sede)
- scoperta esplorativa: ATTIVA
- stato esportato il: 2026-09-21T21:00:04.309Z
- Gli esiti intraday sono separati e non modificano fill, stop o campione del daily.

### Scoperta: riepilogo della seduta (definitivo)

- candidati unici: **49** (ricorrenze ciclo×ticker 352, non sono titoli distinti) · setup qualificati unici: **0**
- candidati per ciclo: 15:30=0, 15:45=0, 16:00=3, 16:15=4, 16:31=5, 16:45=6, 17:00=7, 17:15=7, 17:30=8, 17:45=8, 18:00=8, 18:15=9, 18:30=9, 18:45=10, 19:00=11, 19:15=12, 19:30=12, 19:45=12, 20:00=14, 20:15=14, 20:30=13, 20:45=15, 21:00=15, 21:15=16, 21:30=16, 21:45=18, 22:00=20, 22:15=33, 22:30=47
- ultimo motivo osservato per ticker: SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=29, SETUP_ASSENTE/STOP_TOO_WIDE=6, NON_VALUTABILE_INTEGRITA_DATI/TOO_FAR_FROM_ACTIONABLE_PIVOT=6, NON_VALUTABILE_INTEGRITA_DATI/NOT_NEAR_EMA21=3, SETUP_ASSENTE/NO_PREVIOUS_BREAKOUT=2, SETUP_ASSENTE/NOT_NEAR_EMA21=1, NON_VALUTABILE_INTEGRITA_DATI/RESISTANCE_TOO_CLOSE=1, NON_VALUTABILE_INTEGRITA_DATI/STOP_TOO_WIDE=1
- setup qualificati nella seduta (conservati anche se l'ultimo ciclo non li qualifica): nessuno
- esclusioni tecniche attendibili (dati omogenei, percorso discovery 1.1.0): SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=29, SETUP_ASSENTE/STOP_TOO_WIDE=6, SETUP_ASSENTE/NO_PREVIOUS_BREAKOUT=2, SETUP_ASSENTE/NOT_NEAR_EMA21=1
- non valutabili per integrita' dei dati (verdetto del motore conservato, avvisi impediti): ADAM (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), ASST (SETUP_ASSENTE/NOT_NEAR_EMA21, 3 eventi), BNC (SETUP_ASSENTE/NOT_NEAR_EMA21, 1 eventi), DFDV (SETUP_ASSENTE/STOP_TOO_WIDE, 1 eventi), FWDI (SETUP_ASSENTE/NOT_NEAR_EMA21, 3 eventi), GRML (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), HELP (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), NUAI (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), VEEE (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), VOR (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), WBD (SETUP_ASSENTE/RESISTANCE_TOO_CLOSE, 1 eventi) · osservati non omogenei in almeno un ciclo: ADAM (11 cicli, 1 eventi), ASST (3 cicli, 3 eventi), BNC (18 cicli, 1 eventi), DFDV (23 cicli, 1 eventi), FWDI (7 cicli, 3 eventi), GRML (27 cicli, 2 eventi), HELP (1 cicli, 1 eventi), NUAI (25 cicli, 1 eventi), VEEE (27 cicli, 1 eventi), VOR (2 cicli, 1 eventi), WBD (26 cicli, 1 eventi)
- ultimo ciclo: idonei Classic 3, piani Expansion 1, posizioni 2, barre nuove 5470, eventi nuovi 0
- dettaglio: `stato_30m\riepilogo_seduta_2026-09-21.json` (locale, non pubblicato)

