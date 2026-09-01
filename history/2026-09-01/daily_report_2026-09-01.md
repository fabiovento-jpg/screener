# Growth & Momentum Screener

- software_version: 3.8.1
- market_session_date: 2026-09-01
- generated_at: 2026-09-01T23:40:05+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: NO_VALID_SETUP

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **NEUTRAL**
- market_regime_allows_new_entries: false
- **REGIME NEUTRAL: nessuna nuova promozione consentita.**

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 707.64 | 710.98 | -0.470 | +/-0.50% | 656.08 | true | dentro il buffer (zona neutrale) |
| Nasdaq Composite (IXIC) | 26099.76 | 25954.74 | 0.559 | +/-0.50% | 24343.68 | true | sopra il buffer superiore |

## Scanner

- universe_count: 534
- analyzed_count: 42
- passed_count: 0
- excluded_count: 534

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 0
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 10

Dati insufficienti:
- 10 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 0 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

**NESSUN SETUP VALIDO OGGI**

- 0 setup promossi

## QUALITA' E SUFFICIENZA DEI DATI

Storico insufficiente: 10
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 96 | 200 | 1776346200 | 1788269400 |
| BSP | 44 | 200 | 1782912600 | 1788269400 |
| FRVO | 77 | 200 | 1778679000 | 1788269400 |
| HONA | 55 | 200 | 1781530200 | 1788269400 |
| INIO | 62 | 200 | 1780579800 | 1788269400 |
| IOND | 26 | 200 | 1785245400 | 1788269400 |
| LFTO | 62 | 200 | 1780579800 | 1788269400 |
| MWH | 140 | 200 | 1770820200 | 1788269400 |
| QNT | 62 | 200 | 1780579800 | 1788269400 |
| SPCX | 56 | 200 | 1781271000 | 1788269400 |

Dettaglio completo per titolo, con gli indicatori non calcolabili e quelli non tentati, in `run_metadata`.


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
- biotech_pre_revenue: 20
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 534
- esclusioni strutturali 44
- sopravvissuti 490
- identita' verificata: si
- funnel completo: 534 = 44 + 448 + 10 + 32 + 0 + 0

Divergenze di configurazione rilevate:
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (price_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (market_cap_min): valore ripetuto in prosa e coincidente con la costante
- [DUPLICATE_CONFIG_VALUE] prompts\scanner_v3_daily.md (avg_volume_min): valore ripetuto in prosa e coincidente con la costante

Nota: nessun tetto di capitalizzazione configurato: le mega-cap non vengono escluse per dimensione
Nota: ETF, ETN e fondi chiusi sono esclusi alla fonte da 'Stocks only (ex-Funds)'; per gli altri strumenti la tipologia non e' dichiarata dal provider


## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| NVDA | 52.00 | fallisce il gate rsi14 | rsi14 | 0.86 | 51.87 | 5.23 | 5.99 |

## Funnel

- **idonei totali: 0** = shortlist 0 + fuori dal cap 0
- near misses (non idonei): 1

- universo iniziale: 534
- esclusioni strutturali: -44 → 490
- esclusioni fondamentali: -448 → 42 allo stadio tecnico
- esclusioni tecniche: -42
- **shortlist: 0** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 296, eps_growth 107, operating_margin 25, adr 24, price_above_sma50 21.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 296 |
| eps_growth | 107 |
| operating_margin | 25 |
| adr | 24 |
| price_above_sma50 | 21 |
| altri gate | 51 |
| **esclusi da un gate** | **524** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 10
- errori runtime            : 0
- promossi                  : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 44 |
| FUNDAMENTAL_EXCLUSION | 448 |
| DATA_INSUFFICIENT | 10 |
| TECHNICAL_EXCLUSION | 32 |
| PROMOTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **534** |
| universo iniziale | 534 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

Nessun candidato quantitativo in questo run: nessuna verifica diluizione da riportare.
Storico proprietario `shares_outstanding.jsonl`: 533 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-01T23:30:05+02:00 -> 2026-09-01T23:40:05+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-01T23:30:26+02:00 (finviz_mcp_status: NOT_CONFIGURED)
