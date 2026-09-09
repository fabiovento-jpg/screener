# Screener — output quantitativi Nasdaq Scanner 3.0

Repository degli **output quantitativi** dello Scanner Nasdaq 3.0.
Contiene esclusivamente dati generati automaticamente: nessun codice, nessuna
configurazione, nessuna credenziale.

## Nessuna raccomandazione finanziaria

I file contengono misurazioni, gate quantitativi e piani tecnici con ingresso,
stop e target, quando disponibili. Lo stato del piano e i motivi di blocco
restano espliciti: un titolo idoneo o fuori cap non e automaticamente operativo.
La revisione qualitativa resta separata.

## Fonti

| Dominio | Fonte |
|---|---|
| Tecnica (OHLCV, medie, RSI, ATR, volumi) | TradingView, via il server MCP `tradingview` sul CDP locale |
| Screening universo e fondamentali | Finviz, tramite il pacchetto Python `finvizfinance` |

Il campo `sources` di ogni record dichiara il provider e l'orario di
acquisizione dei due gruppi di dati.

## Struttura

```
latest/     ultimo run valido
history/    un cartella per giorno, YYYY-MM-DD
```

Replay e verifiche offline restano locali in `reports/` e non vengono pubblicati.

`latest/` viene aggiornato **solo** quando un run si conclude completo e supera
tutte le validazioni. Se una scansione fallisce, l'ultimo output valido resta
intatto. In `history/` sono conservati gli ultimi 30 giorni.

Ogni file:

- `scanner_v3_*` — shortlist editoriale dei titoli idonei
- `eligible_*` — tutti gli idonei, inclusi quelli fuori cap, con piano completo, stato e motivi di esclusione dall’operativita
- `funnel_*` — riconciliazione dell’universo, con idonei fuori shortlist separati
- `excluded_*` — titoli esclusi, con i gate falliti e i valori che li hanno causati
- `run_metadata_*` — metadati del run: regime di mercato, conteggi, soglie applicate, errori, `report_status`
- `daily_report.md` / `daily_report_*` — report giornaliero autoesplicativo in markdown
- `review_queue_*` — coda di revisione: titoli **vicini** ai filtri ma esclusi.
  Non è una watchlist e non contiene candidati: `quantitative_near_misses` hanno
  fallito un gate tecnico, `prefilter_watch` non hanno mai visto i gate tecnici
  (`technical_gates_evaluated: false`)

## Date e orari

I JSON riportano `generated_at` e, nei metadati, `run_started_at`,
`run_completed_at` e `market_session_date` (la seduta USA a cui i dati si
riferiscono, non necessariamente il giorno di esecuzione). Gli orari di
esecuzione sono in fuso Europe/Rome; la sessione di mercato è in date di
calendario US.

## Dati mancanti

Un valore non disponibile è `null`, mai stimato, e compare in `missing_fields`
con motivo e fonte interrogata in `missing_details`. Un gate non verificabile
non promuove il titolo.

## `final_setup_ready` è sempre `false`

Superare i gate quantitativi non produce un setup operativo. Ogni record
riporta:

```json
"quantitative_pass": true,
"manual_review_required": true,
"final_setup_ready": false,
"unverified_final_checks": ["pattern", "shares_change_6m_pct", "sec_dilution_check", "verified_catalyst", "qualitative_review"]
```

`hard_filter_pass` e `quantitative_pass` indicano **esclusivamente** il
superamento dei gate quantitativi verificabili in locale. I controlli elencati
in `unverified_final_checks` non sono concludibili da questo motore e
richiedono verifica su SEC, Investor Relations e fonti pubbliche.
`final_setup_ready` resta `false` finché quella revisione qualitativa non è
completata, e non viene mai impostato automaticamente.
