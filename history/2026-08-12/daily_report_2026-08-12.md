# Growth & Momentum Screener

- software_version: 3.7.0
- market_session_date: 2026-08-12
- generated_at: 2026-08-12T23:39:25+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 723.70 | 713.49 | 1.430 | +/-0.50% | 649.53 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26588.48 | 25914.93 | 2.599 | +/-0.50% | 24145.46 | true | sopra il buffer superiore |

## Scanner

- universe_count: 548
- analyzed_count: 39
- passed_count: 3
- excluded_count: 543
- missing_data_count: 3

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| AVGO | Broadcom Inc | 416.05 | 58.31 | 3.80 | 0.86 | 18.98 | true | NORMAL | 47.87 | 85.59 |
| ASML | ASML Holding NV | 1810.07 | 57.15 | 4.26 | 0.74 | 10.49 | true | NORMAL | 24.38 | 31.87 |
| INCY | Incyte Corp | 120.77 | 55.68 | 3.20 | 0.54 | 9.80 | true | PEAD_WINDOW | 37.72 | 38.02 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Idonei fuori dalla shortlist

Hanno superato **tutti** i gate quantitativi ma restano fuori dai primi 3 per score. **Non sono near miss.**

| Ticker | Score | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|
| STLD | 45.00 | 0.59 | 60.30 | 12.78 | 9.71 |
| KNSA | 41.00 | 0.81 | 66.02 | 26.09 | 6.13 |

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| TSEM | 60.00 | fallisce il gate no_extended_move_10d | no_extended_move_10d | 0.95 | 56.84 | 1.89 | 22.91 |
| AEIS | 50.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 0.47 | 57.14 | 10.52 | 15.55 |
| MPWR | 50.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 0.68 | 55.17 | 3.53 | 20.29 |

## Funnel

- **idonei totali: 5** = shortlist 3 + fuori dal cap 2
- near misses (non idonei): 3

- universo iniziale: 548
- esclusioni strutturali: -47 → 501
- esclusioni fondamentali: -462 → 39 allo stadio tecnico
- esclusioni tecniche: -34
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 303, eps_growth 106, operating_margin 27, adr 25, biotech_pre_revenue 22.
Dettaglio completo in `funnel_latest.json`.

## Diluizione

- stato locale: **NOT_VERIFIABLE** — non eseguibile con le sole fonti collegate, quindi senza esito positivo.
- **NOT_VERIFIABLE non equivale a bocciatura**: richiede revisione esterna. L'esito negativo accertato sarebbe FAIL.
- external_verification_required: True · externally_verified: False · external_status: None
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

- [tradingview] ARXS: storico insufficiente (82 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (191 barre, ne servono 200)
- [tradingview] EA: storico insufficiente (96 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (40 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (41 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (48 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (48 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (122 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (42 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-12T23:30:10+02:00 -> 2026-08-12T23:39:25+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-12T23:30:30+02:00 (finviz_mcp_status: NOT_CONFIGURED)
