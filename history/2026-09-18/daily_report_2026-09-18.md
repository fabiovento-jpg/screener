# Daily scanner — release 4.0.0

- run_id: `20260918T213001Z` · market_session_date: 2026-09-18 · generato: 2026-09-18T23:47:51+02:00
- engine_git_sha: `e1821abf25675c474f156b37078880ebddc5c972` · run_status: **COMPLETE**
- Classic 3.9.0 (riferimento, sezione seguente invariata) · Expansion 0.1.0 (SIGNALS) · intraday: SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA

---
# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-18
- generated_at: 2026-09-18T23:46:42+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 721.45 | 709.95 | 1.620 | +/-0.50% | 662.60 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26522.56 | 26071.57 | 1.730 | +/-0.50% | 24553.20 | true | sopra il buffer superiore |

## Scanner

- universe_count: 522
- analyzed_count: 71
- passed_count: 3
- excluded_count: 519

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 3
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 11

Dati insufficienti:
- 11 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 3 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| SNDK | Sandisk Corp | 1791.82 | 61.43 | 6.51 | 1.69 | 31.04 | true | NORMAL | 371.59 | 28016.32 |
| MU | Micron Technology Inc | 1015.80 | 58.28 | 4.85 | 1.47 | 23.55 | true | NORMAL | 345.72 | 1372.09 |
| AMD | Advanced Micro Devices Inc | 559.82 | 65.35 | 4.29 | 1.74 | 4.45 | true | NORMAL | 50.11 | 158.80 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| SNDK | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| MU | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| AMD | BREAKOUT | INVALID | NOT_EXECUTABLE | nessuna | STOP_TOO_WIDE |

Conteggi diagnostici, disgiunti dalle metriche preesistenti:

- strutture teoriche breakout : 1
- strutture teoriche pullback : 0
- trade plan validi           : 0
- trade plan invalidi         : 1
- BREAKOUT_READY validi       : 0
- PULLBACK_READY validi       : 0
- executable                  : 0
- not executable              : 1

Nessun BREAKOUT_READY valido.
Nessun PULLBACK_READY valido.
AMD presenta una struttura teorica di breakout, ma il trade plan e' INVALID e lo stato operativo e' NOT_EXECUTABLE. Motivo: STOP_TOO_WIDE.


## DIAGNOSTICA STOP - SOLO OSSERVAZIONE

Questi dati sono diagnostici e non modificano stop, selezione o operativita'.

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

### AMD
- ancora utilizzata: STRUCTURAL_SUPPORT / RECENT_SWING_LOW
- eta ancora: 4 barre
- structural support: 480,3300
- contraction low: 424,0316 (AVAILABLE_DIAGNOSTIC_CALCULATION)
- finestra della base: 57 barre
- stop trigger: 474,3290
- distanza dal close: 15,271% / 3,562 ATR
- distanza dall'entry (entry_ideal): 19,212% / 4,699 ATR
- structural support vs contraction low: 56,2984 (13,277%, 2,345 ATR)
- osservazione: ANCHOR_INSIDE_BASE
- esito piano invariato: INVALID - STOP_TOO_WIDE

Una sola seduta non conferma ne' smentisce alcuna ipotesi sull'ancoraggio dello stop: queste righe servono ad accumulare osservazioni.


## QUALITA' E SUFFICIENZA DEI DATI

Storico insufficiente: 11
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 108 | 200 | 1776346200 | 1789738200 |
| BSP | 56 | 200 | 1782912600 | 1789738200 |
| FRVO | 89 | 200 | 1778679000 | 1789738200 |
| HONA | 67 | 200 | 1781530200 | 1789738200 |
| INIO | 74 | 200 | 1780579800 | 1789738200 |
| LFTO | 74 | 200 | 1780579800 | 1789738200 |
| MWH | 152 | 200 | 1770820200 | 1789738200 |
| QNT | 74 | 200 | 1780579800 | 1789738200 |
| SHAZ | 148 | 200 | 1771425000 | 1789738200 |
| SPCX | 68 | 200 | 1781271000 | 1789738200 |
| XE | 101 | 200 | 1777296600 | 1789738200 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-18
- benchmark autorevole: QQQ (ultima barra 2026-09-18)
  - IXIC: 2026-09-18
  - QQQ: 2026-09-18
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-18, coincidente con la seduta attesa

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
- biotech_pre_revenue: 19
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 522
- esclusioni strutturali 44
- sopravvissuti 478
- identita' verificata: si
- funnel completo: 522 = 44 + 407 + 11 + 57 + 3 + 0 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## SEC / DILUTION - DIAGNOSTICA SHADOW

Il percorso legacy di enforcement e' invariato durante il freeze. Le classificazioni seguenti migliorano la spiegazione ma non modificano selezione, audit o operativita'.

### SNDK

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-08-07 (42 giorni), entro la freschezza
- fact shadow selezionato: 2026-08-07
- confronto 6M: -0.7781%
- motivo: confronto 2026-01-23 -> 2026-08-07: intervallo 196 giorni
- fatti rifiutati:
  - 2026-01-23 val=147567249.0 form=10-Q eta=238 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE

### MU

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-06-17 (93 giorni), entro la freschezza
- fact shadow selezionato: 2026-06-17
- confronto 6M: 0.3451%
- motivo: confronto 2025-12-10 -> 2026-06-17: intervallo 189 giorni
- fatti rifiutati:
  - 2025-12-10 val=1125509261.0 form=10-Q eta=282 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE

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
- fact legacy: 2026-07-29 (51 giorni), entro la freschezza
- fact shadow selezionato: 2026-07-29
- confronto 6M: 0.1266%
- motivo: confronto 2026-01-30 -> 2026-07-29: intervallo 180 giorni
- fatti rifiutati:
  - 2026-01-30 val=1630410843.0 form=10-K eta=231 motivi=STALE_BEYOND_FRESHNESS_LIMIT

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
| MRVL | 60.00 | fallisce il gate within_25pct_52w_high | within_25pct_52w_high | 1.04 | 58.03 | 2.94 | 22.82 |

## Funnel

- **idonei totali: 3** = shortlist 3 + fuori dal cap 0
- near misses (non idonei): 1

- universo iniziale: 522
- esclusioni strutturali: -44 → 478
- esclusioni fondamentali: -407 → 71 allo stadio tecnico
- esclusioni tecniche: -68
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 273, eps_growth 66, price_above_sma50 37, operating_margin 36, eps_next_year 31.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 273 |
| eps_growth | 66 |
| price_above_sma50 | 37 |
| operating_margin | 36 |
| eps_next_year | 31 |
| altri gate | 65 |
| **esclusi da un gate** | **508** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 11
- errori runtime            : 0
- promossi                  : 3
- idonei fuori cap          : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 44 |
| FUNDAMENTAL_EXCLUSION | 407 |
| DATA_INSUFFICIENT | 11 |
| TECHNICAL_EXCLUSION | 57 |
| PROMOTED | 3 |
| ELIGIBLE_NOT_SHORTLISTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **522** |
| universo iniziale | 522 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + eligible_not_shortlisted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### SNDK
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: BUYBACK
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-23 -> 2026-08-07 · intervallo 196 g (target 180, scarto 16) · corrente vecchia di 42 g · variazione -0.778% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 4.524.000.000 USD (al 2026-07-03)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### MU
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: NORMAL_SBC
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2025-12-10 -> 2026-06-17 · intervallo 189 g (target 180, scarto 9) · corrente vecchia di 93 g · variazione +0.345% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 650.000.000 USD (al 2026-05-28)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### AMD
- stato locale: **FAIL** — verifica locale diluizione fallita. Controllo responsabile: equity offering.
- classificazione: POTENTIAL_DILUTION
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2026-01-30 -> 2026-07-29 · intervallo 180 g (target 180, scarto 0) · corrente vecchia di 51 g · variazione +0.127% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 221.000.000 USD (al 2026-06-27)
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — shelf registration presente: capacita' potenziale di emissione, nessuna emissione dimostrata
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: sotto-controlli falliti: recent_equity_offering_check. Esito negativo accertato localmente

Storico proprietario `shares_outstanding.jsonl`: 521 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-18T23:30:08+02:00 -> 2026-09-18T23:46:42+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-18T23:30:30+02:00 (finviz_mcp_status: NOT_CONFIGURED)

---

## Expansion shadow — EXPANSION_SHADOW_V1 0.1.0

- mode: **SHADOW_DAILY_OHLC**, execution_verified=**false** (piani condizionali su barre daily, non ingressi verificati dal vivo, non istruzioni d'ordine Fineco)
- stato profilo: **SIGNALS**
- ledger: PROSPECTIVE · cohort_id: `EXPANSION_SHADOW_V1-PROSPECTIVE-2026-09-17-802a3409-ea1129c5`
- protocol_hash: `802a3409633f2bac82559314fedf8ead775c41178508d6e7bbb207d63571f6c2` · adapter_hash: `ea1129c5d705604a0fe4d696b900ed0b77bdc5e06bebdf490ba44834c4da332b`
- universo: NASDAQ_COMMON_PRE_CLASSIC (prima dei gate Classic; non deriva da scanner_v3, eligible o review_queue)
- Contabilita' separata dal Classic: non modifica technical_ready_total, actionable_total ne' final_setup_ready.

### Funnel Expansion

- righe sorgente: 805 · membri unici: 805 · position_updates: 0
- riconciliato: True (somma esiti terminali 805)
- non valutabili: 2 (0.0025; soglia pausa 0.05)

| esito terminale | n |
|---|---:|
| NOT_EVALUABLE_DATA_UNAVAILABLE | 2 |
| OUT_OF_PERIMETER_INSTRUMENT_TYPE | 45 |
| SIGNAL_ADMITTED | 1 |
| SIGNAL_EXCLUDED_PORTFOLIO_CAP | 2 |
| SIGNAL_GATES_FAILED | 447 |
| SIGNAL_PLAN_REJECTED_SIZE_ZERO | 4 |
| STRUCTURAL_FILTER_FAILED | 304 |

Fallimenti per gate (non esclusivi, non sommabili): PRICE=77, CAP=0, LIQUIDITY=232, RETURN=708, RANGE=706, VOLUME=165, CLOSE_LOCATION=551, GREEN_BODY=457

### Piani condizionali per la prossima seduta (2026-09-21)

PIANI CONDIZIONALI SHADOW_DAILY_OHLC — validi solo nella seduta indicata; fill modellato max(open, trigger)×1,001; target = 2R dal fill (nessun TP1/TP2, nessun Entry Ideal).

| # | ticker | trigger | stop | tetto open T+1 | qty virtuale | rischio USD peggior fill | RVOL20 | TR/A14 |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 1 | MSTR | 154.47 | 135.28 | 159.26 | 1 | 24.14 | 1.99 | 2.43 |

Il tetto e' un vincolo dell'OPEN del modello daily (open sopra il tetto o <= stop: piano annullato), non un Entry Max per ordini intraday.

Segnali non ammessi: HOOD (PORTFOLIO_CAP), RIOT (PORTFOLIO_CAP), AMAT (SIZE_ZERO), COIN (SIZE_ZERO), SNDK (SIZE_ZERO), STX (SIZE_ZERO)

### Contabilita' shadow e contatore

- stato ledger: **OBSERVING** · max drawdown R: 1.20 (kill a 6.0R)
- trade entrati: 2/30 · chiusi: 0 · aperti: 2 · piani pending: 1
- date d'ingresso distinte: 1/10 · sedute valide: 2/90
- somma R netta: 0 · media R: n/d · PF_R: n/d (NO_OUTCOMES) · win rate: n/d
- equity R (EOD, marks inclusi): -1.205 · P&L realizzato USD: 0 · equity virtuale USD: 9978.37
- trade ambigui (barra daily): 0
- attivazione: 2026-09-17T10:55:59.605535+00:00 · prima T0 ammessa: 2026-09-17
- Nessuna conclusione economica prima di 30 trade chiusi; posizioni aperte e segnali scaduti non sono 0R.

  - aperta TEM: ingresso 2026-09-18 a 81.58, stop 72.18, target 100.38, qty 2, mark 77.84, sedute 1
  - aperta ILMN: ingresso 2026-09-18 a 249.38, stop 232.05, target 284.03, qty 1, mark 239.62, sedute 1
  - evento EXPIRED TSEM: OPEN_ABOVE_CEILING

---

## Stato intraday (monitor separato, ciclo 15 minuti)

- stato: **SEDUTA_CONCLUSA_OSSERVAZIONE_DIFFERITA** — FUORI_SESSIONE · esito: CANDIDATI_OSSERVATI · lista vuota: False
- ultimo tentativo: 2026-09-18T21:00:03.065Z · ultimo ciclo riuscito: 2026-09-18T20:30:03.567Z · candidati: {'classic_idonei': ['AMD'], 'esplorativi': ['ABNB', 'ABSI', 'ACGL', 'ACHV', 'ACRS', 'ADEA', 'ADI', 'ADMA', 'ADTN', 'AEIS', 'AHCO', 'ALKT', 'ALMU', 'ALOY', 'ALVO', 'AMAT', 'AMGN', 'AMRX', 'AOSL', 'ARXS', 'ASST', 'ASTH', 'ATRO', 'AVBP', 'AVGO', 'AVO', 'AVT', 'AXTI', 'BGC', 'BHF', 'BIAF', 'BKR', 'BLMN', 'BNC', 'BPOP', 'BRUN', 'BSY', 'BTDR', 'BTSG', 'BUSE', 'CAR', 'CBC', 'CBRS', 'CDNS', 'CFFN', 'CHEF', 'CLBK', 'COIN', 'COLL', 'COO', 'COST', 'CRBP', 'CRDO', 'CRVS', 'CRWV', 'CTKB', 'CWST', 'DFDV', 'DRS', 'DXCM', 'EBC', 'ELMT', 'EMBC', 'ETOR', 'EWBC', 'EXPO', 'EYE', 'FDMT', 'FER', 'FIBK', 'FIGR', 'FNKO', 'FORM', 'FRNM', 'FRVO', 'FULT', 'FWDI', 'FWONK', 'FWRG', 'GCMG', 'GEMI', 'GFS', 'GOOG', 'GOOGL', 'GPRE', 'GRAL', 'GRPN', 'GSIT', 'GTX', 'HALO', 'HLIT', 'HOOD', 'HOPE', 'HQY', 'HTFL', 'HUT', 'HWC', 'IART', 'IBRX', 'IDXX', 'IMNM', 'INIO', 'INTC', 'INVA', 'IRON', 'ISRG', 'KLAC', 'LAUR', 'LIN', 'LITE', 'LIVN', 'LRCX', 'LSCC', 'LTRX', 'MAMA', 'MANH', 'MAR', 'MARA', 'MATW', 'MIDD', 'MKSI', 'MKTX', 'MMYT', 'MPWR', 'MSTR', 'MTSI', 'NAMS', 'NCI', 'NDAQ', 'NEO', 'NEOG', 'NMRK', 'NTAP', 'NTRA', 'NTRS', 'NTSK', 'NVAX', 'NVMI', 'NWBI', 'OCTV', 'OLED', 'OMDA', 'ON', 'OSW', 'OZK', 'PCT', 'PDFS', 'PFG', 'PGNY', 'PLAY', 'POOL', 'POWI', 'PTC', 'PTRN', 'PUBM', 'PURR', 'PWP', 'RARE', 'REG', 'RELY', 'RILY', 'RMBS', 'RUM', 'SBET', 'SBLK', 'SEIC', 'SENS', 'SFD', 'SFNC', 'SGML', 'SHEN', 'SHOO', 'SITM', 'SLDB', 'SLM', 'SMMT', 'SMPL', 'SMTC', 'SNEX', 'SNPS', 'STLN', 'STTK', 'SWBI', 'TEAM', 'TFSL', 'TGTX', 'TH', 'TJGC', 'TMUS', 'TRMB', 'TRMD', 'TROW', 'TSEM', 'TWST', 'TXN', 'TXRH', 'TYRA', 'UBSI', 'UPB', 'UPST', 'VCTR', 'VIAV', 'VICR', 'VISN', 'VITL', 'VNDA', 'VRDN', 'VRSN', 'VSAT', 'WB', 'WDC', 'WMG', 'WMT', 'WSBC', 'WWD', 'XERS', 'XHLD', 'XMTR', 'XNCR', 'XRAY'], 'expansion': ['ILMN', 'TEM', 'TSEM']} · ritardo max rilevazione s: None
- ultima seduta: 2026-09-18 · cicli completati: 29 · ultimo ciclo: 2026-09-18T20:30:03.567Z
- feed: ALPACA_SIP_1Min_RITARDATO_15_MIN · alert operativo: BLOCCATO: FEED_SIP_RITARDATO_15_MINUTI, VERIFICA_TEMPESTIVA_DEL_TRIGGER_NON_DISPONIBILE, PIANO_SHADOW_DAILY_OHLC_NON_OPERATIVO, CANALE_DI_NOTIFICA_AUTORIZZATO_NON_CONFIGURATO
- ritardo effettivo dei dati s (min/max): 1803/1803 · durata ultimo ciclo s: 61.0 · richieste: 20 (+10 sottoprocesso), HTTP 429: 0
- setup qualificati nell'ultimo ciclo: discovery 0/220, expansion 2/3 · canale Telegram: ATTIVO · esiti avvisi: {'DUPLICATO_SOPPRESSO': 2}
- verifica tempestiva del trigger: NON_DISPONIBILE: nessuno stream consolidato autorizzato (DDE Fineco solo per id confermati e presidiato; IEX = una sede)
- scoperta esplorativa: ATTIVA
- stato esportato il: 2026-09-18T21:00:03.107Z
- Gli esiti intraday sono separati e non modificano fill, stop o campione del daily.

### Scoperta: riepilogo della seduta (definitivo)

- candidati unici: **225** (ricorrenze ciclo×ticker 495, non sono titoli distinti) · setup qualificati unici: **0**
- candidati per ciclo: 15:30=0, 15:45=0, 16:00=1, 16:15=3, 16:30=2, 16:45=2, 17:00=3, 17:15=5, 17:30=5, 17:45=5, 18:00=5, 18:15=5, 18:30=5, 18:45=7, 19:00=9, 19:15=10, 19:30=12, 19:45=13, 20:00=14, 20:15=15, 20:30=14, 20:45=15, 21:00=15, 21:15=16, 21:30=18, 21:45=21, 22:00=23, 22:15=32, 22:30=220
- ultimo motivo osservato per ticker: SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=178, NON_VALUTABILE_INTEGRITA_DATI/TOO_FAR_FROM_ACTIONABLE_PIVOT=21, SETUP_ASSENTE/STOP_TOO_WIDE=10, SETUP_ASSENTE/NOT_NEAR_EMA21=5, SETUP_ASSENTE/PATTERN_QUALITY=4, DATI_MANCANTI/DATA_INSUFFICIENT_HISTORY=3, NON_VALUTABILE_INTEGRITA_DATI/STOP_TOO_WIDE=2, NON_VALUTABILE_INTEGRITA_DATI/DATA_INSUFFICIENT_HISTORY=1, SETUP_ASSENTE/RESISTANCE_TOO_CLOSE=1
- setup qualificati nella seduta (conservati anche se l'ultimo ciclo non li qualifica): nessuno
- esclusioni tecniche attendibili (dati omogenei, percorso discovery 1.1.0): SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT=178, SETUP_ASSENTE/STOP_TOO_WIDE=10, SETUP_ASSENTE/NOT_NEAR_EMA21=5, SETUP_ASSENTE/PATTERN_QUALITY=4, SETUP_ASSENTE/RESISTANCE_TOO_CLOSE=1
- non valutabili per integrita' dei dati (verdetto del motore conservato, avvisi impediti): ALOY (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), ASST (SETUP_ASSENTE/STOP_TOO_WIDE, 3 eventi), ATRO (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), BIAF (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), BNC (SETUP_ASSENTE/STOP_TOO_WIDE, 1 eventi), BRUN (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), CLBK (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), DFDV (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), FRNM (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), FWDI (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 3 eventi), IMCC (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), KLAC (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), MEDS (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), MIDD (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), NCI (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), OCTV (DATI_MANCANTI/DATA_INSUFFICIENT_HISTORY, 1 eventi), SBET (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), SENS (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), SHOE (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), SNEX (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), STLN (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), TJGC (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 2 eventi), VISN (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi), XHLD (SETUP_ASSENTE/TOO_FAR_FROM_ACTIONABLE_PIVOT, 1 eventi) · osservati non omogenei in almeno un ciclo: ALOY (1 cicli, 1 eventi), ASST (11 cicli, 3 eventi), ATRO (1 cicli, 1 eventi), BIAF (16 cicli, 2 eventi), BNC (26 cicli, 1 eventi), BRUN (1 cicli, 2 eventi), CLBK (1 cicli, 2 eventi), DFDV (22 cicli, 2 eventi), FRNM (2 cicli, 1 eventi), FWDI (15 cicli, 3 eventi), IMCC (18 cicli, 1 eventi), KLAC (1 cicli, 1 eventi), MEDS (1 cicli, 1 eventi), MIDD (1 cicli, 2 eventi), NCI (24 cicli, 2 eventi), OCTV (3 cicli, 1 eventi), SBET (1 cicli, 1 eventi), SENS (1 cicli, 1 eventi), SHOE (4 cicli, 1 eventi), SNEX (1 cicli, 2 eventi), STLN (1 cicli, 1 eventi), TJGC (13 cicli, 2 eventi), VISN (1 cicli, 1 eventi), XHLD (2 cicli, 1 eventi)
- ultimo ciclo: idonei Classic 1, piani Expansion 3, posizioni 0, barre nuove 62762, eventi nuovi 0
- dettaglio: `stato_30m\riepilogo_seduta_2026-09-18.json` (locale, non pubblicato)

