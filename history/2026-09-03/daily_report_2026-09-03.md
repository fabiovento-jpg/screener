# Growth & Momentum Screener

- software_version: 3.9.0
- market_session_date: 2026-09-03
- generated_at: 2026-09-03T23:46:43+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 717.67 | 711.03 | 0.933 | +/-0.50% | 657.13 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26584.05 | 25989.50 | 2.288 | +/-0.50% | 24378.83 | true | sopra il buffer superiore |

## Scanner

- universe_count: 539
- analyzed_count: 72
- passed_count: 1
- excluded_count: 538

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 1
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 10

Dati insufficienti:
- 10 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 1 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| NESR | National Energy Services Reunited Corp | 34.50 | 59.15 | 4.53 | 0.49 | 7.07 | true | NORMAL | 59.07 | 173.86 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## TIPOLOGIA DEL SETUP ED ESEGUIBILITA'

La tipologia teorica dice cosa il motore stava costruendo. Non dice che il titolo sia pronto: quello lo dice l'eseguibilita'.

| Ticker | Tipologia teorica | Trade plan | Eseguibilita' | Readiness | Motivo |
|---|---|---|---|---|---|
| NESR | NOT_APPLICABLE | NOT_APPLICABLE | NOT_APPLICABLE | nessuna | TOO_FAR_FROM_ACTIONABLE_PIVOT |

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

### NESR
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

Storico insufficiente: 10
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 98 | 200 | 1776346200 | 1788442200 |
| BSP | 46 | 200 | 1782912600 | 1788442200 |
| FRVO | 79 | 200 | 1778679000 | 1788442200 |
| HONA | 57 | 200 | 1781530200 | 1788442200 |
| INIO | 64 | 200 | 1780579800 | 1788442200 |
| IOND | 28 | 200 | 1785245400 | 1788442200 |
| LFTO | 64 | 200 | 1780579800 | 1788442200 |
| MWH | 142 | 200 | 1770820200 | 1788442200 |
| QNT | 64 | 200 | 1780579800 | 1788442200 |
| SPCX | 58 | 200 | 1781271000 | 1788442200 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


## FRESCHEZZA DELLA SEDUTA

- stato: **FRESH**
- seduta attesa: 2026-09-03
- benchmark autorevole: QQQ (ultima barra 2026-09-03)
  - IXIC: 2026-09-03
  - QQQ: 2026-09-03
- ritardo: 0 giorni di calendario
- ultima barra daily di QQQ = 2026-09-03, coincidente con la seduta attesa

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
- biotech_pre_revenue: 22
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 539
- esclusioni strutturali 47
- sopravvissuti 492
- identita' verificata: si
- funnel completo: 539 = 47 + 420 + 10 + 61 + 1 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## SEC / DILUTION - DIAGNOSTICA SHADOW

Il percorso legacy di enforcement e' invariato durante il freeze. Le classificazioni seguenti migliorano la spiegazione ma non modificano selezione, audit o operativita'.

### NESR

Filing:
- nessun prospetto di offerta nella finestra

Shelf:
- capacita' potenziale di emissione (S-3ASR del 2026-05-26)
- nessuna emissione provata dalla shelf da sola

Shares XBRL:
- stato dato shadow: FRESH
- fact legacy: 2026-06-30 (65 giorni), entro la freschezza
- fact shadow selezionato: 2026-06-30
- confronto 6M: 0.0641%
- motivo: confronto 2025-12-31 -> 2026-06-30: intervallo 181 giorni
- fatti rifiutati:
  - 2025-12-31 val=100787173.0 form=10-K eta=246 motivi=STALE_BEYOND_FRESHNESS_LIMIT

Disposizione:
- evidenza filing: POTENTIAL_EQUITY_CAPACITY
- qualita' dato shares: FRESH
- diluizione confermata: no
- capacita' potenziale: si
- BLOCKED_FAIL_CLOSED
- esito operativo invariato: local_status NOT_VERIFIABLE, blocks_final_setup True
- differenze legacy/shadow: LEGACY_AND_SHADOW_AGREE


## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| MU | 70.00 | fallisce il gate rsi14 | rsi14 | 0.85 | 53.49 | 7.27 | 30.98 |
| IBKR | 59.00 | fallisce il gate rsi14 | rsi14 | 1.23 | 50.84 | 4.74 | 6.24 |
| NVDA | 50.00 | fallisce il gate distance_resistance_hard | distance_resistance_hard | 1.06 | 59.21 | 4.21 | 0.88 |

## Funnel

- **idonei totali: 1** = shortlist 1 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 539
- esclusioni strutturali: -47 → 492
- esclusioni fondamentali: -420 → 72 allo stadio tecnico
- esclusioni tecniche: -71
- **shortlist: 1** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 280, eps_growth 67, operating_margin 39, price_above_sma50 39, eps_next_year 34.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 280 |
| eps_growth | 67 |
| operating_margin | 39 |
| price_above_sma50 | 39 |
| eps_next_year | 34 |
| altri gate | 69 |
| **esclusi da un gate** | **528** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 10
- errori runtime            : 0
- promossi                  : 1

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 47 |
| FUNDAMENTAL_EXCLUSION | 420 |
| DATA_INSUFFICIENT | 10 |
| TECHNICAL_EXCLUSION | 61 |
| PROMOTED | 1 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **539** |
| universo iniziale | 539 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### NESR
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: POTENTIAL_DILUTION
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2025-12-31 -> 2026-06-30 · intervallo 181 g (target 180, scarto 1) · corrente vecchia di 65 g · variazione +0.064% · confidence HIGH
- buyback: **PASS** — nessun riacquisto riportato
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — shelf registration presente: capacita' potenziale di emissione, nessuna emissione dimostrata
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 538 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-03T23:30:05+02:00 -> 2026-09-03T23:46:43+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-03T23:30:26+02:00 (finviz_mcp_status: NOT_CONFIGURED)
