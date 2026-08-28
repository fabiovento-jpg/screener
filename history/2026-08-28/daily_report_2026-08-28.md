# Growth & Momentum Screener

- software_version: 3.8.1
- market_session_date: 2026-08-28
- generated_at: 2026-08-28T23:40:27+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 716.43 | 712.06 | 0.613 | +/-0.50% | 655.17 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26402.41 | 25959.02 | 1.708 | +/-0.50% | 24315.70 | true | sopra il buffer superiore |

## Scanner

- universe_count: 542
- analyzed_count: 43
- passed_count: 1
- excluded_count: 541

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 1
- promossi con campi ancora irrisolti dopo enrichment: 1 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori tecnici TradingView: 10
- di cui storico insufficiente: 10
- missing_data_count: 1 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| IBKR | Interactive Brokers Group Inc | 95.84 | 57.33 | 3.28 | 0.50 | 3.04 | true | NORMAL | 21.38 | 36.62 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| NVDA | 72.00 | fallisce il gate rsi14 | rsi14 | 1.55 | 52.34 | 11.54 | 5.94 |
| HALO | 26.00 | fallisce il gate atr_pct | atr_pct | 0.71 | 67.29 | 26.47 | 4.09 |

## Funnel

- **idonei totali: 1** = shortlist 1 + fuori dal cap 0
- near misses (non idonei): 2

- universo iniziale: 542
- esclusioni strutturali: -45 → 497
- esclusioni fondamentali: -454 → 43 allo stadio tecnico
- esclusioni tecniche: -42
- **shortlist: 1** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 298, eps_growth 108, operating_margin 26, adr 25, eps_next_year 21.
Dettaglio completo in `funnel_latest.json`.

## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### IBKR
- stato locale: **FAIL** — verifica locale diluizione fallita. Controllo responsabile: equity offering.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2010-11-08 -> 2011-05-06 · intervallo 179 g (target 180, scarto 1) · corrente vecchia di 5593 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 5593 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — nessun riacquisto rilevato nel periodo
- equity offering: **FAIL** — prospetto 424B5 depositato negli ultimi ~6 mesi
- shelf: **PASS** — shelf registration presente: capacita' potenziale di emissione, nessuna emissione dimostrata
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: sotto-controlli falliti: recent_equity_offering_check. Esito negativo accertato localmente

Storico proprietario `shares_outstanding.jsonl`: 541 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (94 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (42 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (53 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (60 barre, ne servono 200)
- [tradingview] IOND: storico insufficiente (24 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (60 barre, ne servono 200)
- [tradingview] MFP: storico insufficiente (44 barre, ne servono 200)
- [tradingview] MWH: storico insufficiente (138 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (60 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (54 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-28T23:30:06+02:00 -> 2026-08-28T23:40:27+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-28T23:30:27+02:00 (finviz_mcp_status: NOT_CONFIGURED)
