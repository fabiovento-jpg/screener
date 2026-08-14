# Growth & Momentum Screener

- software_version: 3.8.0
- market_session_date: 2026-08-14
- generated_at: 2026-08-14T23:40:39+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 731.07 | 712.95 | 2.542 | +/-0.50% | 650.62 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26729.15 | 25906.62 | 3.175 | +/-0.50% | 24178.91 | true | sopra il buffer superiore |

## Scanner

- universe_count: 552
- analyzed_count: 44
- passed_count: 3
- excluded_count: 549

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 3
- promossi con campi ancora irrisolti dopo enrichment: 3 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori tecnici TradingView: 12
- di cui storico insufficiente: 12
- missing_data_count: 3 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| TSEM | Tower Semiconductor Ltd | 265.48 | 57.72 | 8.69 | 0.54 | 20.51 | true | PEAD_WINDOW | 23.66 | 93.04 |
| ASML | ASML Holding NV | 1844.08 | 59.48 | 3.96 | 0.56 | 8.45 | true | NORMAL | 24.38 | 31.87 |
| KNSA | Kiniksa Pharmaceuticals International Plc | 76.75 | 62.19 | 4.20 | 0.57 | 8.07 | true | NORMAL | 55.36 | 33.30 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| AVGO | 80.00 | fallisce il gate rsi14 | rsi14 | 1.65 | 46.50 | 4.95 | 25.96 |
| STLD | 60.00 | fallisce il gate rsi14 | rsi14 | 0.78 | 52.51 | 8.85 | 12.89 |
| STX | 54.00 | fallisce il gate performance_21d | performance_21d | 0.93 | 62.01 | 30.58 | 17.62 |

## Funnel

- **idonei totali: 3** = shortlist 3 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 552
- esclusioni strutturali: -46 → 506
- esclusioni fondamentali: -462 → 44 allo stadio tecnico
- esclusioni tecniche: -41
- **shortlist: 3** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 305, eps_growth 106, operating_margin 27, adr 25, eps_next_year 22.
Dettaglio completo in `funnel_latest.json`.

## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### TSEM
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2024-12-31 -> 2025-12-31 · intervallo 365 g (target 180, scarto 185) · corrente vecchia di 226 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 226 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — nessun riacquisto riportato
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### ASML
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - misura: 2024-12-31 -> 2025-12-31 · intervallo 365 g (target 180, scarto 185) · corrente vecchia di 226 g · confidence NOT_VERIFIABLE
  - motivo: osservazione corrente vecchia di 226 giorni (limite 150): non abbastanza attuale per un confronto a 6 mesi
- buyback: **PASS** — riacquisti rilevati per 5.950.000.000 EUR (al 2025-12-31)
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

### KNSA
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - motivo: storico proprietario: intervallo fra le osservazioni 4 gg, scarto 176 oltre la tolleranza 45
- buyback: **PASS** — nessun riacquisto riportato
- equity offering: **PASS** — nessun prospetto di offerta prezzata negli ultimi ~6 mesi
- shelf: **PASS** — nessuna shelf registration negli ultimi ~6 mesi
- ATM: **NOT_VERIFIABLE** — un programma ATM si desume solo dal testo dei prospetti: non determinabile da dati strutturati XBRL
- convertibili/warrant: **NOT_VERIFIABLE** — tag XBRL su convertibili e warrant assenti per la maggior parte degli emittenti: non determinabile in modo oggettivo
- verifica esterna richiesta: **true** · externally_verified: false · external_status: n/d · fonti: SEC EDGAR, Investor Relations
- motivo conclusivo: non verificabili localmente: shares_change_check, atm_check, convertibles_warrants_check. Richiede revisione esterna (SEC EDGAR + Investor Relations): NON e' una bocciatura

Storico proprietario `shares_outstanding.jsonl`: 551 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (84 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (193 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (32 barre, ne servono 200)
- [tradingview] EA: storico insufficiente (96 barre, ne servono 200)
- [tradingview] FRVO: storico insufficiente (65 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (42 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (43 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (50 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (50 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (50 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (124 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (44 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-14T23:30:05+02:00 -> 2026-08-14T23:40:39+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-14T23:30:26+02:00 (finviz_mcp_status: NOT_CONFIGURED)
