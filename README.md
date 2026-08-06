# Screener — output quantitativi Nasdaq Scanner 3.0

Repository degli **output quantitativi** dello Scanner Nasdaq 3.0.
Contiene i dati generati automaticamente e gli strumenti per verificarli:
nessun codice del motore di scansione, nessuna configurazione, nessuna
credenziale.

## Nessuna raccomandazione finanziaria

Questo repository **non contiene raccomandazioni di investimento**. Non ci sono
buy zone, target, stop, rating o punteggi. I file riportano misurazioni e
l'esito booleano di filtri quantitativi definiti dall'utente. Ogni decisione
operativa è successiva ed esterna a questi dati.

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
docs/       schema di strumentazione dei gate e audit dei run
tools/      validatore degli output
tests/      fixture e test del validatore
```

`latest/` viene aggiornato **solo** quando un run si conclude completo e supera
tutte le validazioni. Se una scansione fallisce, l'ultimo output valido resta
intatto. In `history/` sono conservati gli ultimi 30 giorni.

Ogni file:

- `scanner_v3_*` — titoli che superano tutti i gate quantitativi
- `excluded_*` — titoli esclusi, con i gate falliti e i valori che li hanno causati
- `run_metadata_*` — metadati del run: regime di mercato, conteggi, soglie applicate, errori

## Verifica dei gate

Lo scanner non chiede fiducia: ogni record deve pubblicare i valori numerici che
determinano ogni gate, per i titoli promossi come per quelli esclusi, cosi' che
chiunque possa ricalcolarli senza leggere il codice sorgente. Lo schema richiesto
e' in [`docs/gate_instrumentation.md`](docs/gate_instrumentation.md).

Ogni gate ha quattro stati possibili — `PASS`, `FAIL`, `UNVERIFIED`, `ERROR` — e
solo `PASS` promuove. Il campo `audit_status` di ogni record ne e' il riassunto,
con precedenza `ERROR > FAIL > UNVERIFIED > PASS`; `data_quality_score` misura
invece quanto dato era disponibile (100 meno 3 per ogni campo atteso non
utilizzabile, 10 se la causa e' un guasto di pipeline). I due numeri sono
indipendenti: un run puo' essere invalido con qualita' 100, o valido con
qualita' 60.

```
python3 tools/validate_run.py latest/          # leggibile
python3 tools/validate_run.py latest/ --json   # per consumo automatico
python3 tests/run_tests.py                     # test del validatore
```

Il validatore ricalcola ogni gate dai valori pubblicati e lo confronta con lo
stato dichiarato: `RUN VALID` (exit 0), `RUN INVALID` (exit 1, almeno un gate
diverge), `RUN NON AUDITABILE` (exit 2, valori non esportati). Segnala inoltre
quali soglie il motore non dichiara, costringendolo a dedurle. L'esito sul run
2026-08-05 e' in [`docs/audit_2026-08-05.md`](docs/audit_2026-08-05.md): oggi
**RUN INVALID**, qualita' 39/100.

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
