# Growth & Momentum Screener

- software_version: 3.7.1
- market_session_date: 2026-08-13
- generated_at: 2026-08-13T23:40:23+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 732.07 | 713.21 | 2.644 | +/-0.50% | 650.11 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26803.01 | 25909.11 | 3.450 | +/-0.50% | 24163.45 | true | sopra il buffer superiore |

## Scanner

- universe_count: 548
- analyzed_count: 42
- passed_count: 3
- excluded_count: 542
- missing_data_count: 3

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| STX | Seagate Technology Holdings Plc | 921.37 | 57.65 | 8.09 | 0.81 | 24.27 | true | NORMAL | 48.49 | 149.17 |
| AVGO | Broadcom Inc | 417.82 | 59.05 | 3.75 | 0.72 | 18.47 | true | NORMAL | 47.87 | 85.59 |
| ASML | ASML Holding NV | 1847.90 | 59.89 | 4.12 | 0.72 | 8.23 | true | NORMAL | 24.38 | 31.87 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Idonei fuori dalla shortlist

Hanno superato **tutti** i gate quantitativi ma restano fuori dai primi 3 per score. **Non sono near miss.**

| Ticker | Score | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|
| STLD | 45.00 | 0.51 | 57.40 | 10.60 | 10.83 |
| INCY | 35.00 | 0.43 | 55.11 | 4.72 | 10.02 |
| KNSA | 31.00 | 0.63 | 65.15 | 26.16 | 6.57 |

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| TSEM | 50.00 | fallisce il gate rsi14 | rsi14 | 0.65 | 54.44 | 0.78 | 26.48 |

## Funnel

- **idonei totali: 6** = shortlist 3 + fuori dal cap 3
- near misses (non idonei): 1

- universo iniziale: 548
- esclusioni strutturali: -44 → 504
- esclusioni fondamentali: -462 → 42 allo stadio tecnico
- esclusioni tecniche: -36
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 303, eps_growth 108, operating_margin 26, adr 24, biotech_pre_revenue 20.
Dettaglio completo in `funnel_latest.json`.

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
  - misura: 2026-01-27 -> 2026-07-31 · intervallo 185 g (target 180, scarto 5) · corrente vecchia di 13 g · variazione +3.931% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 176.000.000 USD (al 2026-07-03)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### AVGO
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 4 controlli sono stati completati, ma restano 2 subcheck materiali da verificare esternamente.
- classificazione: NORMAL_SBC
- confidenza misura: HIGH
- azioni in circolazione: **PASS**
  - misura: 2025-11-28 -> 2026-05-29 · intervallo 182 g (target 180, scarto 2) · corrente vecchia di 76 g · variazione +0.344% · confidence HIGH
- buyback: **PASS** — riacquisti rilevati per 8.450.000.000 USD (al 2026-05-03)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### ASML
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2024-12-31 -> 2025-12-31 · intervallo 365 g (target 180, scarto 185) · corrente vecchia di 225 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 225 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — riacquisti rilevati per 5.950.000.000 EUR (al 2025-12-31)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 547 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (83 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (192 barre, ne servono 200)
- [tradingview] EA: storico insufficiente (96 barre, ne servono 200)
- [tradingview] EQPT: storico insufficiente (139 barre, ne servono 200)
- [tradingview] FRVO: storico insufficiente (64 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (41 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (42 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (49 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (49 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (49 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (123 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (43 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-13T23:30:04+02:00 -> 2026-08-13T23:40:23+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-13T23:30:23+02:00 (finviz_mcp_status: NOT_CONFIGURED)
