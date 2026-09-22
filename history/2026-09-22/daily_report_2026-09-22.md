# Daily scanner — release 4.0.0

- run_id: `20260922T213002Z` · market_session_date: 2026-09-22 · generato: 2026-09-22T23:50:13+02:00
- engine_git_sha: `e1821abf25675c474f156b37078880ebddc5c972` · run_status: **COMPLETE**
- Classic 3.9.0 (riferimento, sezione seguente invariata) · Expansion 0.1.0 (SIGNALS) · intraday: SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA

---
# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-22
- generated_at: 2026-09-22T23:48:41+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 747.46 | 710.98 | 5.130 | +/-0.50% | 663.82 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 27244.27 | 26115.81 | 4.321 | +/-0.50% | 24590.69 | true | sopra il buffer superiore |

## Scanner

- universe_count: 532
- analyzed_count: 75
- passed_count: 3
- excluded_count: 528

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
| STX | Seagate Technology Holdings Plc | 919.84 | 59.66 | 5.91 | 1.43 | 10.24 | true | NORMAL | 48.49 | 149.17 |
| MRVL | Marvell Technology Inc | 262.36 | 63.95 | 5.52 | 0.90 | 14.35 | true | NORMAL | 36.55 | 49.42 |
| SNDK | Sandisk Corp | 1887.04 | 64.69 | 6.25 | 1.18 | 20.87 | true | NORMAL | 371.59 | 28016.32 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| STX | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| MRVL | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| SNDK | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |

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

Una sola seduta non conferma ne' smentisce alcuna ipotesi sull'ancoraggio dello stop: queste righe servono ad accumulare osservazioni.


## QUALITA' E SUFFICIENZA DEI DATI

Storico insufficiente: 13
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 110 | 200 | 1776346200 | 1790083800 |
| BSP | 58 | 200 | 1782912600 | 1790083800 |
| FRVO | 91 | 200 | 1778679000 | 1790083800 |
| HONA | 69 | 200 | 1781530200 | 1790083800 |
| INIO | 76 | 200 | 1780579800 | 1790083800 |
| IOND | 40 | 200 | 1785245400 | 1790083800 |
| LFTO | 76 | 200 | 1780579800 | 1790083800 |
| MFP | 60 | 200 | 1782739800 | 1790083800 |
| MWH | 154 | 200 | 1770820200 | 1790083800 |
| QNT | 76 | 200 | 1780579800 | 1790083800 |
| SHAZ | 150 | 200 | 1771425000 | 1790083800 |
| SPCX | 70 | 200 | 1781271000 | 1790083800 |
| XE | 103 | 200 | 1777296600 | 1790083800 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-22
- benchmark autorevole: QQQ (ultima barra 2026-09-22)
  - IXIC: 2026-09-22
  - QQQ: 2026-09-22
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-22, coincidente con la seduta attesa

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
- biotech_pre_revenue: 20
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 532
- esclusioni strutturali 45
- sopravvissuti 487
- identita' verificata: si
- funnel completo: 532 = 45 + 412 + 13 + 58 + 3 + 1 + 0

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
- fact legacy: 2026-07-31 (53 giorni), entro la freschezza
- fact shadow selezionato: 2026-07-31
- confronto 6M: 3.9305%
- motivo: confronto 2026-01-27 -> 2026-07-31: intervallo 185 giorni
- fatti rifiutati:
  - 2026-01-27 val=218073067.0 form=10-Q eta=238 motivi=STALE_BEYOND_FRESHNESS_LIMIT

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
- fact legacy: 2026-08-21 (32 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-21
- confronto 6M: 0.2974%
- motivo: confronto 2026-03-04 -> 2026-08-21: intervallo 170 giorni
- fatti rifiutati:
  - 2026-03-04 val=874300000.0 form=10-K eta=202 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: AMBIGUOUS_REQUIRES_REVIEW
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- BLOCKED_AMBIGUOUS_CLASSIFICATION
- esito operativo invariato: local_status FAIL, blocks_final_setup True
- differenze legacy/shadow: LEGACY_FORM_ONLY_CLASSIFICATION

### SNDK

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-08-07 (46 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-07
- confronto 6M: -0.7781%
- motivo: confronto 2026-01-23 -> 2026-08-07: intervallo 196 giorni
- fatti rifiutati:
  - 2026-01-23 val=147567249.0 form=10-Q eta=242 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE


## Idonei fuori dalla shortlist

Hanno superato **tutti** i gate quantitativi ma restano fuori dai primi 3 per score. **Non sono near miss.**

| Ticker | Score | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|
| MU | 65.00 | 1.15 | 66.06 | 13.38 | 9.36 |

- MU: piano **NOT_APPLICABLE**; stato **NOT_APPLICABLE**. TOO_FAR_FROM_ACTIONABLE_PIVOT: 14.49% dal pivot, oltre 5.0%. Nessun livello prodotto; TRADE_PLAN_NOT_VALID; MISSING_LEVELS:entry_trigger,entry_ideal,entry_max,stop_trigger; PATTERN_QUALITY_FAIL; FINAL_SETUP_NOT_READY

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| LSCC | 80.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 1.64 | 56.41 | 4.11 | 26.50 |
| TER | 70.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 0.89 | 58.79 | 6.11 | 22.38 |
| NESR | 55.00 | fallisce il gate rsi14 | rsi14 | 1.15 | 51.15 | 0.18 | 11.63 |

## Funnel

- **idonei totali: 4** = shortlist 3 + fuori dal cap 1
- near misses (non idonei): 3

- universo iniziale: 532
- esclusioni strutturali: -45 → 487
- esclusioni fondamentali: -412 → 75 allo stadio tecnico
- esclusioni tecniche: -71
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 275, eps_growth 69, operating_margin 37, eps_next_year 31, adr 25.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 275 |
| eps_growth | 69 |
| operating_margin | 37 |
| eps_next_year | 31 |
| adr | 25 |
| altri gate | 78 |
| **esclusi da un gate** | **515** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 13
- errori runtime            : 0
- promossi                  : 3
- idonei fuori cap          : 1

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 45 |
| FUNDAMENTAL_EXCLUSION | 412 |
| DATA_INSUFFICIENT | 13 |
| TECHNICAL_EXCLUSION | 58 |
| PROMOTED | 3 |
| ELIGIBLE_NOT_SHORTLISTED | 1 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **532** |
| universo iniziale | 532 |

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
  - misura: 2026-01-27 -> 2026-07-31 · intervallo 185 g (target 180, scarto 5) · corrente vecchia di 53 g · variazione +3.931% · confidence HIGH
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
  - misura: 2026-03-04 -> 2026-08-21 · intervallo 170 g (target 180, scarto 10) · corrente vecchia di 32 g · variazione +0.297% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 400.000.000 USD (al 2026-08-01)
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: sotto-controlli falliti: recent_equity_offering_check. Esito negativo accertato localmente

### SNDK
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: BUYBACK
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-23 -> 2026-08-07 · intervallo 196 g (target 180, scarto 16) · corrente vecchia di 46 g · variazione -0.778% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 4.524.000.000 USD (al 2026-07-03)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 531 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-22T23:30:10+02:00 -> 2026-09-22T23:48:41+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-22T23:30:36+02:00 (finviz_mcp_status: NOT_CONFIGURED)

---

## Expansion shadow — EXPANSION_SHADOW_V1 0.1.0

- mode: **SHADOW_DAILY_OHLC**, execution_verified=**false** (piani condizionali su barre daily, non ingressi verificati dal vivo, non istruzioni d'ordine Fineco)
- stato profilo: **SIGNALS**
- ledger: PROSPECTIVE · cohort_id: `EXPANSION_SHADOW_V1-PROSPECTIVE-2026-09-17-802a3409-ea1129c5`
- protocol_hash: `802a3409633f2bac82559314fedf8ead775c41178508d6e7bbb207d63571f6c2` · adapter_hash: `ea1129c5d705604a0fe4d696b900ed0b77bdc5e06bebdf490ba44834c4da332b`
- universo: NASDAQ_COMMON_PRE_CLASSIC (prima dei gate Classic; non deriva da scanner_v3, eligible o review_queue)
- Contabilita' separata dal Classic: non modifica technical_ready_total, actionable_total ne' final_setup_ready.

### Funnel Expansion

- righe sorgente: 808 · membri unici: 808 · position_updates: 0
- riconciliato: True (somma esiti terminali 808)
- non valutabili: 2 (0.0025; soglia pausa 0.05)

| esito terminale | n |
|---|---:|
| NOT_EVALUABLE_DATA_UNAVAILABLE | 2 |
| OUT_OF_PERIMETER_INSTRUMENT_TYPE | 46 |
| SIGNAL_ADMITTED | 1 |
| SIGNAL_EXCLUDED_PORTFOLIO_CAP | 4 |
| SIGNAL_GATES_FAILED | 477 |
| SIGNAL_PLAN_REJECTED_SIZE_ZERO | 1 |
| STRUCTURAL_FILTER_FAILED | 277 |

Fallimenti per gate (non esclusivi, non sommabili): PRICE=74, CAP=0, LIQUIDITY=209, RETURN=692, RANGE=638, VOLUME=654, CLOSE_LOCATION=560, GREEN_BODY=430

### Piani condizionali per la prossima seduta (2026-09-23)

PIANI CONDIZIONALI SHADOW_DAILY_OHLC — validi solo nella seduta indicata; fill modellato max(open, trigger)×1,001; target = 2R dal fill (nessun TP1/TP2, nessun Entry Ideal).

| # | ticker | trigger | stop | tetto open T+1 | qty virtuale | rischio USD peggior fill | RVOL20 | TR/A14 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | VKTX | 41.80 | 36.19 | 43.20 | 3 | 21.16 | 19.21 | 7.79 |

Il tetto e' un vincolo dell'OPEN del modello daily (open sopra il tetto o <= stop: piano annullato), non un Entry Max per ordini intraday.

Segnali non ammessi: SGRY (PORTFOLIO_CAP), TNGX (PORTFOLIO_CAP), RMBS (PORTFOLIO_CAP), DNLI (PORTFOLIO_CAP), VICR (SIZE_ZERO)

### Contabilita' shadow e contatore

- stato ledger: **OBSERVING** · max drawdown R: 1.23 (kill a 6.0R)
- trade entrati: 2/30 · chiusi: 0 · aperti: 2 · piani pending: 1
- date d'ingresso distinte: 1/10 · sedute valide: 4/90
- somma R netta: 0 · media R: n/d · PF_R: n/d (NO_OUTCOMES) · win rate: n/d
- equity R (EOD, marks inclusi): -0.822 · P&L realizzato USD: 0 · equity virtuale USD: 9984.90
- trade ambigui (barra daily): 0
- attivazione: 2026-09-17T10:55:59.605535+00:00 · prima T0 ammessa: 2026-09-17
- Nessuna conclusione economica prima di 30 trade chiusi; posizioni aperte e segnali scaduti non sono 0R.

  - aperta TEM: ingresso 2026-09-18 a 81.58, stop 72.18, target 100.38, qty 2, mark 77.19, sedute 3
  - aperta ILMN: ingresso 2026-09-18 a 249.38, stop 232.05, target 284.03, qty 1, mark 247.46, sedute 3
  - evento EXPIRED WBD: TRIGGER_NOT_TOUCHED

---

## Stato intraday (monitor separato, ciclo 15 minuti)

- stato: **SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA** — FUORI_SESSIONE · esito: CANDIDATI_OSSERVATI · lista vuota: False
- ultimo tentativo: 2026-09-22T21:00:04.354Z · ultimo ciclo riuscito: 2026-09-22T20:30:04.757Z · candidati: {'classic_idonei': ['MRVL', 'MU', 'SNDK'], 'esplorativi': ['ABSI', 'ABUS', 'ADPT', 'AUGO', 'BAND', 'BHF', 'BLLN', 'BWIN', 'BZ', 'CALM', 'CBRL', 'CDNA', 'CHKP', 'CLPT', 'CTKB', 'DXCM', 'EYE', 'FIVN', 'GCT', 'GLXY', 'GRAL', 'GRML', 'HALO', 'HCSG', 'IBRX', 'IMVT', 'INOD', 'KLIC', 'KLRA', 'KOD', 'MATW', 'MAZE', 'MLTX', 'MMED', 'MOMO', 'MPWR', 'NAMS', 'NCI', 'NEOG', 'NICE', 'NVAX', 'OKTA', 'OMER', 'PONY', 'PSKY', 'PTON', 'PYPL', 'RARE', 'RMBS', 'RYAAY', 'SAIL', 'SBET', 'SDGR', 'SGRY', 'SHOP', 'SNEX', 'SOFI', 'SRAD', 'SRRK', 'TTAN', 'VICR', 'VKTX', 'VOR', 'WBD', 'XENE', 'XMTR'], 'expansion': ['ILMN', 'TEM', 'WBD']} · ritardo max rilevazione s: None
- ultima seduta: 2026-09-22 · cicli completati: 29 · ultimo ciclo: 2026-09-22T20:30:04.757Z
- feed: ALPACA_SIP_1Min_RITARDATO_15_MIN · alert operativo: BLOCCATO: FEED_SIP_RITARDATO_15_MINUTI, VERIFICA_TEMPESTIVA_DEL_TRIGGER_NON_DISPONIBILE, PIANO_SHADOW_DAILY_OHLC_NON_OPERATIVO, CANALE_DI_NOTIFICA_AUTORIZZATO_NON_CONFIGURATO
- ritardo effettivo dei dati s (min/max): 1804/1804 · durata ultimo ciclo s: 35.3 · richieste: 14 (+5 sottoprocesso), HTTP 429: 0
- setup qualificati nell'ultimo ciclo: discovery 0/66, expansion 0/1 · canale Telegram: ATTIVO · esiti avvisi: {}
- verifica tempestiva del trigger: NON_DISPONIBILE: nessuno stream consolidato autorizzato (DDE Fineco solo per id confermati e presidiato; IEX = una sede)
- scoperta esplorativa: ATTIVA
- stato esportato il: 2026-09-22T21:00:04.505Z
- Gli esiti intraday sono separati e non modificano fill, stop o campione del daily.

### Scoperta: riepilogo della seduta (definitivo)

- candidati unici: **71** (ricorrenze ciclo×ticker 375, non sono titoli distinti) · setup qualificati unici: **0**
- candidati per ciclo: 15:30=0, 15:45=0, 16:00=2, 16:15=2, 16:30=3, 16:45=3, 17:00=7, 17:15=6, 17:30=7, 17:45=7, 18:00=7, 18:15=7, 18:30=8, 18:45=8, 19:00=9, 19:15=11, 19:30=11, 19:45=11, 20:00=11, 20:15=12, 20:30=12, 20:45=15, 21:00=16, 21:15=16, 21:30=24, 21:45=24, 22:00=26, 22:15=44, 22:30=66
- ultimo motivo osservato per ticker: SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=48, SETUP_ASSENTE/STOP_TOO_WIDE=9, SETUP_ASSENTE/NOT_NEAR_EMA21=6, NON_VALUTABILE_INTEGRITA_DATI/TOO_FAR_FROM_ACTIONABLE_PIVOT=5, NON_VALUTABILE_INTEGRITA_DATI/NOT_NEAR_EMA21=1, SETUP_ASSENTE/PATTERN_QUALITY=1, SETUP_ASSENTE/RESISTANCE_TOO_CLOSE=1
- setup qualificati nella seduta (conservati anche se l'ultimo ciclo non li qualifica): nessuno
- esclusioni tecniche attendibili (dati omogenei, percorso discovery 1.1.0): SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=48, SETUP_ASSENTE/STOP_TOO_WIDE=9, SETUP_ASSENTE/NOT_NEAR_EMA21=6, SETUP_ASSENTE/PATTERN_QUALITY=1, SETUP_ASSENTE/RESISTANCE_TOO_CLOSE=1
- non valutabili per integrita' dei dati (verdetto del motore conservato, avvisi impediti): GRML (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), IMCC (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), NCI (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), SNEX (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), VOR (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), WBD (SETUP_ASSENTE/NOT_NEAR_EMA21, 1 eventi) · osservati non omogenei in almeno un ciclo: GRML (27 cicli, 2 eventi), IMCC (1 cicli, 1 eventi), NCI (4 cicli, 2 eventi), SNEX (2 cicli, 2 eventi), VOR (5 cicli, 1 eventi), WBD (14 cicli, 1 eventi)
- ultimo ciclo: idonei Classic 3, piani Expansion 1, posizioni 2, barre nuove 7448, eventi nuovi 0
- dettaglio: `stato_30m\riepilogo_seduta_2026-09-22.json` (locale, non pubblicato)

