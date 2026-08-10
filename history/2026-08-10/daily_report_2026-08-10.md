# Growth & Momentum Screener

- software_version: 3.4.0
- market_session_date: 2026-08-10
- generated_at: 2026-08-10T23:39:38+02:00
- market_closed_confirmed: true
- market_session_forced: false
- report_status: NO_VALID_SETUP

## Market regime

Regola implementata (nessuna interpretazione, 3 stati, versione 2.1-3state-buffer-qqq-structure): buffer di +/-0.50% attorno alla SMA50. BULL solo se: QQQ close > QQQ SMA50*(1+buffer), QQQ SMA50 > QQQ SMA200, e Nasdaq close > Nasdaq SMA50*(1+buffer). BEAR se almeno una tra: QQQ close < QQQ SMA50*(1-buffer), Nasdaq close < Nasdaq SMA50*(1-buffer), QQQ SMA50 <= QQQ SMA200. NEUTRAL in tutti gli altri casi. Il rapporto SMA50/SMA200 del Nasdaq e' pubblicato come diagnostica e NON entra nella regola. Se una componente non e' calcolabile il regime e' null e il run e' incompleto.

- Regime: **BULL**
- market_regime_allows_new_entries: true

| Componente | Close | SMA50 | dist. da SMA50 % | buffer | SMA200 | SMA50>SMA200 | esito componente |
|---|---|---|---|---|---|---|---|
| QQQ | 720.87 | 714.27 | 0.924 | +/-0.50% | 648.40 | true | sopra il buffer superiore |
| Nasdaq Composite (IXIC) | 26605.35 | 25935.44 | 2.583 | +/-0.50% | 24108.70 | true | sopra il buffer superiore |

## Scanner

- universe_count: 546
- analyzed_count: 39
- passed_count: 0
- excluded_count: 546
- missing_data_count: 0

## Quantitative candidates

**NESSUN SETUP QUANTITATIVO**

- 0 setup promossi

## Errori

- [tradingview] ARXS: storico insufficiente (80 barre, ne servono 200)
- [tradingview] BLLN: storico insufficiente (189 barre, ne servono 200)
- [tradingview] BSP: storico insufficiente (28 barre, ne servono 200)
- [tradingview] HAPN: storico insufficiente (38 barre, ne servono 200)
- [tradingview] HONA: storico insufficiente (39 barre, ne servono 200)
- [tradingview] INIO: storico insufficiente (46 barre, ne servono 200)
- [tradingview] IOND: storico insufficiente (10 barre, ne servono 200)
- [tradingview] SPCX: storico insufficiente (40 barre, ne servono 200)

## Sources

- TradingView MCP: ok - dati tecnici raccolti durante il run (2026-08-10T23:30:36+02:00 -> 2026-08-10T23:39:38+02:00)
- Finviz (finvizfinance): OK - universo e fondamentali recuperati alle 2026-08-10T23:30:56+02:00 (finviz_mcp_status: NOT_CONFIGURED)
