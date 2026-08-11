# Growth & Momentum Screener

- software_version: 3.5.0
- market_session_date: 2026-08-11
- generated_at: 2026-08-11T23:39:18+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 718.45 | 713.88 | 0.641 | +/-0.50% | 648.96 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26445.44 | 25924.90 | 2.008 | +/-0.50% | 24127.23 | true | sopra il buffer superiore |

## Scanner

- universe_count: 548
- analyzed_count: 40
- passed_count: 3
- excluded_count: 543
- missing_data_count: 3

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | Broadcom Inc | 416.08 | 58.33 | 3.87 | 0.69 | 18.97 | true | NORMAL | 47.87 | 85.59 |
| STLD | Steel Dynamics Inc | 263.69 | 60.85 | 3.26 | 0.78 | 9.50 | true | NORMAL | 33.44 | 84.19 |
| ASML | ASML Holding NV | 1799.38 | 56.36 | 4.41 | 0.77 | 11.15 | true | NORMAL | 24.38 | 31.87 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Idonei fuori dalla shortlist

Hanno superato **tutti** i gate quantitativi ma restano fuori dai primi 3 per score. **Non sono near miss.**

| Ticker | Score | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|
| INCY | 45.00 | 0.55 | 56.32 | 5.99 | 9.52 |
| KNSA | 21.00 | 0.49 | 65.56 | 27.67 | 6.61 |

## Near misses

Nessun near miss: nessun titolo non idoneo e' a un solo gate dall'idoneita'.

## Funnel

- **idonei totali: 5** = shortlist 3 + fuori dal cap 2
- near misses (non idonei): 0

- universo iniziale: 548
- esclusioni strutturali: -46 → 502
- esclusioni fondamentali: -462 → 40 allo stadio tecnico
- esclusioni tecniche: -35
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 304, eps_growth 106, operating_margin 29, adr 24, biotech_pre_revenue 22.
Dettaglio completo in `funnel_latest.json`.

## Diluizione

- stato: **NOT_VERIFIABLE** — il controllo non e' eseguibile con le fonti collegate, quindi non ha esito positivo.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: richiede verifica esterna su SEC EDGAR, Investor Relations
- motivo: variazione azioni a 6 mesi non disponibile: FinViz espone solo valori puntuali (Outstanding/Float) e lo storico proprietario e' in accumulo dal 2026-08-11. Nessuna fonte esterna collegata.
- fonti verificate: FinViz screener (Outstanding, Float: valori puntuali); storico proprietario shares_outstanding.jsonl (richiede 180 giorni)
- storico proprietario: 547 righe scritte in questo run (uso come gate: False, servono 180 giorni)

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (81 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (190 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (29 barre, ne servono 200)
- [tradingview] EA: storico insufficiente (96 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (39 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (40 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (47 barre, ne servono 200)
- [tradingview] IOND: storico insufficiente (11 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (41 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-11T23:30:04+02:00 -> 2026-08-11T23:39:18+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-11T23:30:24+02:00 (finviz_mcp_status: NOT_CONFIGURED)
