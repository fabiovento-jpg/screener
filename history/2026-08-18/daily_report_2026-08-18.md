# Growth & Momentum Screener

- software_version: 3.8.1
- market_session_date: 2026-08-18
- generated_at: 2026-08-18T23:42:09+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: QUANTITATIVE_CANDIDATES_PRESENT

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 717.51 | 712.98 | 0.635 | +/-0.50% | 651.51 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26289.70 | 25914.50 | 1.448 | +/-0.50% | 24204.65 | true | sopra il buffer superiore |

## Scanner

- universe_count: 547
- analyzed_count: 44
- passed_count: 1
- excluded_count: 546

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 1
- promossi con campi ancora irrisolti dopo enrichment: 1 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori tecnici TradingView: 12
- di cui storico insufficiente: 12
- missing_data_count: 1 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

Un quantitative candidate NON e' un setup finale. Richiede verifica qualitativa SEC/Investor Relations prima di qualsiasi decisione operativa.

| Ticker | Nome | price_tv | RSI14 | ATR% | RVOL20 | dist.res.% | structural | earnings_state | rev Q/Q % | EPS Q/Q % |
|---|---|---|---|---|---|---|---|---|---|---|
| KNSA | Kiniksa Pharmaceuticals International Plc | 79.49 | 66.40 | 3.80 | 0.54 | 4.34 | true | NORMAL | 55.36 | 33.30 |

Per ogni titolo: manual_review_required=true, final_setup_ready=false, verifiche aperte: sec_dilution, investor_relations_results, guidance, real_catalyst, pattern_quality.

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| STLD | 70.00 | fallisce il gate rsi14 | rsi14 | 0.88 | 46.84 | 8.38 | 15.58 |
| STX | 70.00 | fallisce il gate rsi14 | rsi14 | 0.84 | 53.07 | 12.62 | 26.70 |
| ASML | 55.00 | fallisce il gate rsi14 | rsi14 | 0.96 | 53.91 | 3.68 | 10.93 |

## Funnel

- **idonei totali: 1** = shortlist 1 + fuori dal cap 0
- near misses (non idonei): 3

- universo iniziale: 547
- esclusioni strutturali: -47 → 500
- esclusioni fondamentali: -456 → 44 allo stadio tecnico
- esclusioni tecniche: -43
- **shortlist: 1** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 300, eps_growth 108, adr 25, operating_margin 25, biotech_pre_revenue 22.
Dettaglio completo in `funnel_latest.json`.

## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

### KNSA
- stato locale: **NOT_VERIFIABLE** — verifica locale SEC/diluizione incompleta: 3 controlli sono stati completati, ma restano 3 subcheck materiali da verificare esternamente.
- confidenza misura: NOT_VERIFIABLE
- azioni in circolazione: **NOT_VERIFIABLE**
  - motivo: storico proprietario: intervallo fra le osservazioni 8 gg, scarto 172 oltre la tolleranza 45
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

- [tradingview] ARXS: storico insufficiente (86 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (195 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (34 barre, ne servono 200)
- [tradingview] FRVO: storico insufficiente (67 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (44 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (45 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (52 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (52 barre, ne servono 200)
- [tradingview] MWH: storico insufficiente (130 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (52 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (126 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (46 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-18T23:30:33+02:00 -> 2026-08-18T23:42:09+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-18T23:30:53+02:00 (finviz_mcp_status: NOT_CONFIGURED)
