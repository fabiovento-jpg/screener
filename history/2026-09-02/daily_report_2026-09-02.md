# Growth & Momentum Screener

- software_version: 3.8.1
- market_session_date: 2026-09-02
- generated_at: 2026-09-02T23:42:12+02:00
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
| QQQ | 709.24 | 710.89 | -0.232 | +/-0.50% | 656.59 | true | dentro il buffer (zona neutrale) |
| Nasdaq Composite (IXIC) | 26217.82 | 25967.35 | 0.965 | +/-0.50% | 24360.42 | true | sopra il buffer superiore |

## Scanner

- universe_count: 541
- analyzed_count: 46
- passed_count: 0
- excluded_count: 541

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 0
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori runtime TradingView: 0
- storico insufficiente (dato mancante, non errore): 11

Dati insufficienti:
- 11 titoli con meno di 200 barre giornaliere
- esclusi prima della valutazione dei gate tecnici
- nessun errore runtime TradingView
- missing_data_count: 0 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

**NESSUN SETUP VALIDO OGGI**

- 0 setup promossi

## QUALITA' E SUFFICIENZA DEI DATI

Storico insufficiente: 11
Errori runtime TradingView: 0

Titoli esclusi perche' privi di storico sufficiente, non per un guasto del provider: la serie e' arrivata regolarmente ed e' piu' corta del minimo richiesto.

| Ticker | Barre disponibili | Richieste | Prima data | Ultima data |
|---|---|---|---|---|
| ARXS | 97 | 200 | 1776346200 | 1788355800 |
| BSP | 45 | 200 | 1782912600 | 1788355800 |
| FRVO | 78 | 200 | 1778679000 | 1788355800 |
| HONA | 56 | 200 | 1781530200 | 1788355800 |
| INIO | 63 | 200 | 1780579800 | 1788355800 |
| IOND | 27 | 200 | 1785245400 | 1788355800 |
| LFTO | 63 | 200 | 1780579800 | 1788355800 |
| MFP | 47 | 200 | 1782739800 | 1788355800 |
| MWH | 141 | 200 | 1770820200 | 1788355800 |
| QNT | 63 | 200 | 1780579800 | 1788355800 |
| SPCX | 57 | 200 | 1781271000 | 1788355800 |

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
- adr: 25
- biotech_pre_revenue: 21
- price_min: conteggio non osservabile, applicato dal provider
- market_cap_min: conteggio non osservabile, applicato dal provider
- avg_volume_min: conteggio non osservabile, applicato dal provider

Mega-cap:
- nessun tetto di capitalizzazione e' configurato: un titolo non viene mai escluso per dimensione.

Riconciliazione:
- universo iniziale 541
- esclusioni strutturali 46
- sopravvissuti 495
- identita' verificata: si
- funnel completo: 541 = 46 + 449 + 11 + 35 + 0 + 0

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
| NVDA | 72.00 | fallisce il gate distance_resistance_hard | distance_resistance_hard | 1.24 | 56.67 | 5.88 | 2.70 |

## Funnel

- **idonei totali: 0** = shortlist 0 + fuori dal cap 0
- near misses (non idonei): 1

- universo iniziale: 541
- esclusioni strutturali: -46 → 495
- esclusioni fondamentali: -449 → 46 allo stadio tecnico
- esclusioni tecniche: -46
- **shortlist: 0** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 296, eps_growth 109, adr 25, operating_margin 23, biotech_pre_revenue 21.
Dettaglio completo in `funnel_latest.json`.

## RICONCILIAZIONE DEL FUNNEL

| Causa primaria di esclusione | Ticker |
|---|---|
| revenue_growth | 296 |
| eps_growth | 109 |
| adr | 25 |
| operating_margin | 23 |
| biotech_pre_revenue | 21 |
| altri gate | 56 |
| **esclusi da un gate** | **530** |

Voci disgiunte dalle precedenti, che completano l'universo:

- dati insufficienti        : 11
- errori runtime            : 0
- promossi                  : 0

| Esito terminale | Ticker |
|---|---|
| STRUCTURAL_EXCLUSION | 46 |
| FUNDAMENTAL_EXCLUSION | 449 |
| DATA_INSUFFICIENT | 11 |
| TECHNICAL_EXCLUSION | 35 |
| PROMOTED | 0 |
| RUNTIME_ERROR | 0 |
| **totale riconciliato** | **541** |
| universo iniziale | 541 |

Asserzione: `universe_initial = structural_exclusions + fundamental_exclusions + data_insufficient + technical_exclusions + promoted + runtime_errors`

Esito: **verificata**. Ogni ticker compare in un solo bucket terminale e la somma coincide con l'universo iniziale.


## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

Nessun candidato quantitativo in questo run: nessuna verifica diluizione da riportare.
Storico proprietario `shares_outstanding.jsonl`: 540 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

Nessun errore registrato.

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-09-02T23:30:32+02:00 -> 2026-09-02T23:42:12+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-09-02T23:30:53+02:00 (finviz_mcp_status: NOT_CONFIGURED)
