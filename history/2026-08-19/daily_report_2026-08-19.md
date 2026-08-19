# Growth & Momentum Screener

- software_version: 3.8.1
- market_session_date: 2026-08-19
- generated_at: 2026-08-19T23:40:19+02:00
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
| QQQ | 716.08 | 712.98 | 0.434 | +/-0.50% | 651.96 | true | dentro il buffer (zona neutrale) |
| Nasdaq Composite (IXIC) | 26331.08 | 25922.53 | 1.576 | +/-0.50% | 24218.40 | true | sopra il buffer superiore |

## Scanner

- universe_count: 550
- analyzed_count: 44
- passed_count: 0
- excluded_count: 550

Diagnostica del run. Sono conteggi **informativi**, non stadi del funnel: i ticker con errore tecnico sono gia' compresi in `excluded_count` e nelle esclusioni tecniche, quindi non vanno sommati a nulla.
- promossi con campi mancanti alla fonte: 0
- promossi con campi ancora irrisolti dopo enrichment: 0 (enrichment tentato e non riuscito; `pattern` e `previous_revenue_growth_yoy` non rientrano: sono assenti per progetto)
- errori tecnici TradingView: 13
- di cui storico insufficiente: 13
- missing_data_count: 0 (campo legacy: promossi con campi mancanti alla fonte)

## Quantitative candidates

**NESSUN SETUP VALIDO OGGI**

- 0 setup promossi

## Near misses

Titoli **NON idonei**: falliscono esattamente un gate. Massimo 3, ordinati per score decrescente.

| Ticker | Score | Motivo | Responsabile | RVOL | RSI | perf21% | dist.res.% |
|---|---|---|---|---|---|---|---|
| INCY | 52.00 | fallisce il gate atr_pct | atr_pct | 0.86 | 67.84 | 9.44 | 3.21 |

## Funnel

- **idonei totali: 0** = shortlist 0 + fuori dal cap 0
- near misses (non idonei): 1

- universo iniziale: 550
- esclusioni strutturali: -46 → 504
- esclusioni fondamentali: -460 → 44 allo stadio tecnico
- esclusioni tecniche: -44
- **shortlist: 0** (cap 3)

Gate piu' selettivi (causa primaria): revenue_growth 303, eps_growth 109, operating_margin 26, adr 24, biotech_pre_revenue 22.
Dettaglio completo in `funnel_latest.json`.

## SEC / Diluizione

Esito della pipeline SEC/XBRL locale, **per candidato**: ogni controllo e' riportato con il proprio stato e la propria motivazione, senza sintesi discrezionali.

- **NOT_VERIFIABLE non equivale a bocciatura**: significa che quel controllo non e' concludibile sui dati strutturati e richiede la verifica esterna. L'esito negativo accertato sarebbe FAIL.
- **non blocca la shortlist quantitativa** (stadio preliminare locale)
- **blocca il setup finale**: finche' `externally_verified` e' false, `final_setup_ready` resta false.

Nessun candidato quantitativo in questo run: nessuna verifica diluizione da riportare.
Storico proprietario `shares_outstanding.jsonl`: 549 righe scritte in questo run. E' una fonte di riserva per la sola variazione azioni (uso come gate: False); i controlli qui sopra vengono da SEC/XBRL.

## Livelli di validazione

1. **shortlist quantitativa** — questo motore: tutti i gate locali superati. NON e' un setup operativo.
2. **candidato verificato esternamente** — dopo SEC EDGAR e Investor Relations. Fuori dalla portata di questo motore.
3. **setup finale valido** — solo dopo il livello 2. `final_setup_ready` non e' mai `true` qui.

## Errori

- [tradingview] ARXS: storico insufficiente (87 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (196 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (35 barre, ne servono 200)
- [tradingview] FRVO: storico insufficiente (68 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (45 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (46 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (53 barre, ne servono 200)
- [tradingview] LFTO: storico insufficiente (53 barre, ne servono 200)
- [tradingview] MFP: storico insufficiente (35 barre, ne servono 200)
- [tradingview] MWH: storico insufficiente (131 barre, ne servono 200)
- [tradingview] QNT: storico insufficiente (53 barre, ne servono 200)
- [tradingview] SHAZ: storico insufficiente (127 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (47 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-19T23:30:11+02:00 -> 2026-08-19T23:40:19+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-19T23:30:31+02:00 (finviz_mcp_status: NOT_CONFIGURED)
