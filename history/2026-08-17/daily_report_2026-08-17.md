# Growth & Momentum Screener

- software_version: 3.8.0
- market_session_date: 2026-08-17
- generated_at: 2026-08-17T23:41:10+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 729.87 | 712.74 | 2.404 | +/-0.50% | 651.10 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26644.90 | 25902.90 | 2.865 | +/-0.50% | 24193.00 | true | sopra il buffer superiore |

## Scanner

- universe_count: 548
- analyzed_count: 45
- passed_count: 3
- excluded_count: 542

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 3
- promossi con campi ancora irrisolti dopo enrichment: 3 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori tecnici TradingView: 13
- di cui storico insufficiente: 13
- missing_data_count: 3 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| ASML | ASML Holding NV | 1883.12 | 62.34 | 3.80 | 0.81 | 6.20 | true | NORMAL | 24.38 | 31.87 |
| INCY | Incyte Corp | 123.50 | 60.41 | 3.04 | 1.11 | 7.37 | true | NORMAL | 37.72 | 38.02 |
| TSEM | Tower Semiconductor Ltd | 263.73 | 57.10 | 8.52 | 0.60 | 21.31 | true | PEAD_WINDOW | 23.66 | 93.04 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Idonei fuori dalla shortlist

Hanno superato **tutti** i gate quantitativi ma restano fuori dai primi 3 per score. **Non sono near miss.**

| Ticker | Score | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|
| STX | 44.00 | 0.78 | 63.65 | 26.30 | 15.10 |
| IBKR | 42.00 | 0.96 | 58.15 | 4.20 | 3.72 |
| KNSA | 26.00 | 0.47 | 65.95 | 23.82 | 4.75 |

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| AVGO | 70.00 | fallisce il gate rsi14 | rsi14 | 1.10 | 46.26 | 5.83 | 26.14 |
| LRCX | 60.00 | fallisce il gate ema21_above_ema50 | ema21_above_ema50 | 0.80 | 57.75 | 9.75 | 27.53 |
| STLD | 55.00 | fallisce il gate rsi14 | rsi14 | 0.66 | 54.60 | 9.62 | 11.85 |

## Funnel

- **idonei totali: 6** = shortlist 3 + fuori dal cap 3
- near misses (non idonei): 3

- universo iniziale: 548
- esclusioni strutturali: -46 → 502
- esclusioni fondamentali: -457 → 45 allo stadio tecnico
- esclusioni tecniche: -39
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 302, eps_growth 107, adr 25, operating_margin 25, biotech_pre_revenue 21.
Dettaglio completo in `funnel_latest.json`.

## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### ASML
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2024-12-31 -> 2025-12-31 · intervallo 365 g (target 180, scarto 185) · corrente vecchia di 229 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 229 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — riacquisti rilevati per 5.950.000.000 EUR (al 2025-12-31)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### INCY
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - motivo: storico proprietario: intervallo fra le osservazioni 7 gg, scarto 173 oltre la tolleranza 45
- buyback: **PASS** — nessun riacquisto rilevato nel periodo
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### TSEM
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2024-12-31 -> 2025-12-31 · intervallo 365 g (target 180, scarto 185) · corrente vecchia di 229 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 229 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — nessun riacquisto riportato
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 546 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (85 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (194 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (33 barre, ne servono 200)
- [tradingview] FRVO: storico insufficiente (66 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (43 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (44 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (51 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (51 barre, ne servono 200)
- [tradingview] MFP: storico insufficiente (33 barre, ne servono 200)
- [tradingview] MWH: storico insufficiente (129 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (51 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (125 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (45 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-17T23:30:10+02:00 -> 2026-08-17T23:41:10+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-17T23:30:30+02:00 (finviz_mcp_status: NOT_CONFIGURED)
