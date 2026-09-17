# Screener — output quantitativi Nasdaq Scanner (release 4.0.0)

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
| Tecnica Classic (OHLCV, medie, RSI, ATR, volumi) | TradingView, via il server MCP `tradingview` sul CDP locale |
| Expansion: OHLCV daily, calendario, corporate actions | Alpaca Market Data (SIP, `adjustment=raw`) |
| Expansion: membership e capitalizzazione osservate dopo la chiusura | Finviz (query dedicata, senza filtri prezzo/volume) |
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

## Release 4.0.0: profili separati

Dalla release 4.0.0 ogni run pubblica due profili con contabilità distinta:

- **Classic** (versione 3.9.0, invariata): i file `scanner_v3_*`, `eligible_*`,
  `funnel_*`, `excluded_*`, `review_queue_*`, `run_metadata_*` mantengono
  schema e semantica precedenti.
- **EXPANSION_SHADOW_V1** (versione 0.1.0): profilo daily long in *shadow*,
  selezione autonoma sull'universo Nasdaq **prima** dei gate Classic.
  Livelli etichettati `SHADOW_DAILY_OHLC` con `execution_verified=false`:
  sono piani condizionali modellati su barre giornaliere, non ingressi
  verificati, non istruzioni d'ordine e non modificano i totali Classic.

File aggiuntivi in `latest/` (e copie datate in `history/<seduta>/`):

| file | contenuto |
|---|---|
| `release_manifest_latest.json` | `release_version`, `run_id`, `market_session_date`, `engine_git_sha` (commit del motore, **non** del publisher), stato del run, profili (versione, mode, attivazione, `cohort_id`, `protocol_hash`, `adapter_hash`) e `artifacts` con percorso e SHA-256 di ogni file del run; non contiene il proprio hash |
| `expansion_latest.json` | segnali Expansion con valori dei gate, riferimenti alle barre, trigger, stop, tetto dell'open T+1, quantità virtuale, motivo di ammissione/non ammissione; `plans_for_next_session`; `evaluations` (un record per membro) |
| `expansion_funnel_latest.json` | riconciliazione dell'universo: `terminal_outcomes` (un esito per membro, somma = `members_unique`), non valutabili, `gate_failures_non_exclusive` (non sommabili) |
| `expansion_shadow_latest.json` | conto virtuale 10.000 USD: piani pending, posizioni aperte, trade chiusi con R netto/costi/ambiguità, equity, curva R, contatore dei 30 trade, checkpoint e kill |
| `publication_status_latest.json` | ultimo tentativo di pubblicazione (`last_attempt.status` = `PUBLISHED_IN_THIS_COMMIT` o `FAILED`) e ultima pubblicazione riuscita |

Stati Expansion (`status`): `SIGNALS`, `NO_SIGNALS`, `NOT_ACTIVATED`,
`WAITING_FIRST_PROSPECTIVE_SESSION`, `DATA_UNAVAILABLE`, `INGEST_REJECTED`,
`ADAPTER_MISMATCH`, `EXPANSION_OUTPUT_UNAVAILABLE`, `PAUSED_*`, `KILLED_*`,
`SETTLING_*`, `INCONCLUSIVE_*`, `PILOT_PASSED_NO_LIVE_AUTHORIZATION`.
Uno stato bloccato non equivale a zero segnali. Una posizione aperta, un
segnale scaduto o un dato mancante non sono trade a 0R.

Se `publication_status_latest.json` riporta `FAILED`, i file `latest/`
appartengono a `last_successful_publication`, non al tentativo fallito.
Lo storico non viene riscritto: un secondo run della stessa seduta pubblica
copie con suffisso `__<run_id>`.

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
