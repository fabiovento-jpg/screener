# Growth & Momentum Screener

- software_version: 3.4.0
- market_session_date: 2026-08-07
- generated_at: 2026-08-07T23:38:43+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: NO_VALID_SETUP

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 723.03 | 714.57 | 1.184 | +/-0.50% | 647.85 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26690.60 | 25941.68 | 2.887 | +/-0.50% | 24090.44 | true | sopra il buffer superiore |

## Scanner

- universe_count: 547
- analyzed_count: 37
- passed_count: 0
- excluded_count: 547
- missing_data_count: 0

## Quantitative candidates

**NESSUN SETUP QUANTITATIVO**

- 0 setup promossi

## Errori

- [tradingview] ARXS: storico insufficiente (79 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (188 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (27 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (37 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (38 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (45 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (39 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-07T23:30:10+02:00 -> 2026-08-07T23:38:43+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-07T23:30:31+02:00 (finviz_mcp_status: NOT_CONFIGURED)
