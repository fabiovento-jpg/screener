# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-09
- generated_at: 2026-09-09T23:47:13+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 716.31 | 711.17 | 0.723 | +/-0.50% | 658.90 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26253.33 | 26043.61 | 0.805 | +/-0.50% | 24436.22 | true | sopra il buffer superiore |

## Scanner

- universe_count: 533
- analyzed_count: 74
- passed_count: 2
- excluded_count: 531

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
| MU | Micron Technology Inc | 1027.77 | 60.61 | 5.23 | 0.86 | 22.11 | true | NORMAL | 345.72 | 1372.09 |
| SMTC | Semtech Corp | 163.94 | 65.54 | 6.68 | 1.03 | 8.18 | true | PEAD_WINDOW | 32.72 | 608.78 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| MU | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |
| SMTC | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |

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

### SMTC
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
| ARXS | 101 | 200 | 1776346200 | 1788960600 |
| BSP | 49 | 200 | 1782912600 | 1788960600 |
| FRVO | 82 | 200 | 1778679000 | 1788960600 |
| HONA | 60 | 200 | 1781530200 | 1788960600 |
| INIO | 67 | 200 | 1780579800 | 1788960600 |
| IOND | 31 | 200 | 1785245400 | 1788960600 |
| LFTO | 67 | 200 | 1780579800 | 1788960600 |
| MWH | 145 | 200 | 1770820200 | 1788960600 |
| QNT | 67 | 200 | 1780579800 | 1788960600 |
| SHAZ | 141 | 200 | 1771425000 | 1788960600 |
| SPCX | 61 | 200 | 1781271000 | 1788960600 |
| XE | 94 | 200 | 1777296600 | 1788960600 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-09
- benchmark autorevole: QQQ (ultima barra 2026-09-09)
  - IXIC: 2026-09-09
  - QQQ: 2026-09-09
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-09, coincidente con la seduta attesa

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
- adr: 27
- biotech_pre_revenue: 20
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 533
- esclusioni strutturali 47
- sopravvissuti 486
- identita' verificata: si
- funnel completo: 533 = 47 + 412 + 12 + 60 + 2 + 0 + 0

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
- fact legacy: 2026-06-17 (84 giorni), entro la freschezza
- fact shadow selezionato: 2026-06-17
- confronto 6M: 0.3451%
- motivo: confronto 2025-12-10 -> 2026-06-17: intervallo 189 giorni
- fatti rifiutati:
  - 2025-12-10 val=1125509261.0 form=10-Q eta=273 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE

### SMTC

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- nessuna shelf nella finestra

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-05-22 (110 giorni), entro la freschezza
- fact shadow selezionato: 2026-05-22
- confronto 6M: 0.6604%
- motivo: confronto 2025-11-21 -> 2026-05-22: intervallo 182 giorni
- fatti rifiutati:
  - 2025-11-21 val=92540057.0 form=10-Q eta=292 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: NO_DILUTION_SIGNAL_FOUND
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: no
- NO_BLOCKING_SIGNAL_FOUND_DIAGNOSTIC_ONLY
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE


## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| AMD | 82.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 1.23 | 60.43 | 10.98 | 12.21 |
| MRVL | 70.00 | fallisce il gate within_25pct_52w_high | within_25pct_52w_high | 0.82 | 55.54 | 12.68 | 40.37 |
| STX | 70.00 | fallisce il gate rsi14 | rsi14 | 0.92 | 54.53 | 10.60 | 29.24 |

## Funnel

- **idonei totali: 2** = shortlist 2 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 533
- esclusioni strutturali: -47 → 486
- esclusioni fondamentali: -412 → 74 allo stadio tecnico
- esclusioni tecniche: -72
- **shortlist: 2** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 273, eps_growth 67, operating_margin 40, price_above_sma50 37, eps_next_year 32.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 273 |
| eps_growth | 67 |
| operating_margin | 40 |
| price_above_sma50 | 37 |
| eps_next_year | 32 |
| altri gate | 70 |
| **esclusi da un gate** | **519** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 12
- errori runtime            : 0
- promossi                  : 2
- idonei fuori cap          : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 47 |
| FUNDAMENTAL_EXCLUSION | 412 |
| DATA_INSUFFICIENT | 12 |
| TECHNICAL_EXCLUSION | 60 |
| PROMOTED | 2 |
| ELIGIBLE_NOT_SHORTLISTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **533** |
| universo iniziale | 533 |

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
  - misura: 2025-12-10 -> 2026-06-17 · intervallo 189 g (target 180, scarto 9) · corrente vecchia di 84 g · variazione +0.345% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 650.000.000 USD (al 2026-05-28)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### SMTC
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: NORMAL_SBC
- confidenza misura: LOWER
- azioni in circolazione: **PASS**
  - misura: 2025-11-21 -> 2026-05-22 · intervallo 182 g (target 180, scarto 2) · corrente vecchia di 110 g · variazione +0.660% · confidence LOWER
- buyback: **PASS** — nessun riacquisto rilevato nel periodo
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 532 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-09T23:30:06+02:00 -> 2026-09-09T23:47:13+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-09T23:30:25+02:00 (finviz_mcp_status: NOT_CONFIGURED)
