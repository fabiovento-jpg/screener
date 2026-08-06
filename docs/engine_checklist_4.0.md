# Migrazione del motore allo schema 4.0 — checklist

Quattro interventi, in ordine di priorita'. Ognuno ha un criterio di
accettazione verificabile con gli strumenti in `tools/`: non serve rileggere il
codice del motore per sapere se e' stato fatto.

Stato di partenza, run 2026-08-05: `RUN INVALID`, qualita' 39/100, 7 soglie
dedotte, 45 divergenze fail-open.

---

## Priorita' 1 — chiudere il fail-open

Ogni gate esce sempre con uno stato fra `PASS`, `FAIL`, `UNVERIFIED`, `ERROR`.
La regola non ammette eccezioni:

```
UNVERIFIED o ERROR non possono mai contribuire a hard_filter_pass = true
```

Oggi non e' cosi': 45 gate dichiarati `PASS` non superano il ricalcolo, di cui
42 perche' un valore mancante non ha fatto fallire il gate. Il caso piu' netto e'
`eps_growth`, che con `revenue_growth_yoy` a `null` non viene valutato affatto:
IDYA passa con EPS -35,99, USAR con -1,55, AMLX con 10,88, contro una soglia di
30. Nessuno dei tre supera nemmeno il ramo alternativo (EPS >= 20 con fatturato
>= 40): il fatturato e' `null`, quindi il ramo non e' valutabile e il gate deve
essere `UNVERIFIED`.

**Criterio di accettazione**

```
python3 tools/validate_run.py <run>   ->  0 divergenze fail-open
```

## Priorita' 2 — pubblicare le soglie

`run_metadata.thresholds` deve contenere ogni regola effettivamente applicata,
in forma piatta. Sette soglie oggi mancano e il validatore le deduce:
`revenue_growth_min`, `eps_growth_min`, `eps_growth_alt_min`,
`eps_growth_alt_revenue_min`, `eps_next_year_min`, `operating_margin_min`,
`within_52w_high_max_pct`.

Le due del ramo alternativo di `eps_growth` meritano una nota: sono coerenti con
il run 2026-08-05, ma **non sono falsificabili su quei dati**. Nessun titolo ha
EPS fra 20 e 30 con fatturato sopra 40, quindi il ramo alternativo non decide
nulla e la sua presenza nel motore non e' osservabile dall'esterno. E' esattamente
il tipo di regola che deve essere dichiarata, perche' non c'e' modo di dedurla.

L'elenco completo e' in `docs/gate_instrumentation.md`, sezione 5. Il validatore
accetta anche la forma a intervallo attuale (`"rsi": [55, 72]`) e la normalizza.

**Criterio di accettazione**

```
python3 tools/validate_run.py <run>   ->  nessuna riga "SOGLIE NON DICHIARATE"
```

## Priorita' 3 — esportare tutti gli operandi gia' calcolati

Per ogni titolo che raggiunge lo stadio tecnico, `values` deve contenere:

```
price  ema21  ema50  sma50  sma150  sma200
rsi14  atr14  atr_pct  rvol20  performance_21d_pct
week52_high  distance_52w_high_pct  resistance  distance_resistance_pct
```

piu' `trend_structural_pass`. Nessuno di questi richiede calcolo aggiuntivo:
sono gia' tutti in memoria quando i gate vengono valutati, e per i 7 titoli con
storico insufficiente il motore li elenca gia' per nome in `missing_fields`.

Per i titoli fermati prima dello stadio tecnico valgono le stesse chiavi, con
valori `null` e motivo dichiarato:

```json
"unverified_gates": ["price_above_sma50", "sma50_above_sma150", "rsi14"],
"missing_details": {
  "sma50": {"reason": "stage_not_executed", "source": "TradingView MCP"}
}
```

**Criterio di accettazione**

```
python3 tools/validate_run.py <run>   ->  nessun gate in "GATE NON AUDITABILI"
                                          data_quality_score coerente col dichiarato
```

## Priorita' 4 — audit prima della pubblicazione

`latest/` si aggiorna solo dopo un verdetto positivo:

```
scanner -> tools/publish_guard.py -> consentito -> aggiorna latest/
                                  -> bloccato   -> latest/ resta invariato
```

Il guard blocca su: verdetto diverso da `RUN VALID` (quindi anche
`RUN NON AUDITABILE`), soglie dedotte, promossi con `audit_status` diverso da
`PASS` — sia dichiarato sia ricalcolato.

```
python3 tools/publish_guard.py <run_dir> --publish-to latest/
```

Exit 0 pubblicazione consentita, 1 bloccata. Un run bloccato non scrive nulla
nella destinazione: resta disponibile in `history/` o in locale per il debug, ma
non diventa la fonte del report del mattino.

Due deroghe esistono, entrambe esplicite e riportate nell'output del guard:
`--allow-not-auditable` per accettare un run parzialmente auditabile,
`--allow-deduced` per accettare soglie non dichiarate. Sono pensate per la fase
di transizione: ogni deroga usata resta stampata nel log del run, cosi' la
scelta e' tracciata invece che silenziosa.

---

## Ordine consigliato

Priorita' 1 e 2 sono indipendenti e insieme portano il run da `RUN INVALID` a
`RUN NON AUDITABILE` — un miglioramento reale: il motore smette di affermare
cose false, e ammette cio' che non sa. La 3 porta a `RUN VALID`. La 4 rende la
proprieta' permanente invece che verificata a mano una volta.
