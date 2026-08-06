# Schema 4.0 — strumentazione dei gate

Principio: **lo scanner non chiede fiducia**. Ogni record deve contenere tutti i
numeri necessari perche' chiunque — l'autore, un LLM, un altro programma —
ricalcoli ogni gate senza leggere il codice sorgente e senza rieseguire la
scansione. Un gate pubblicato come solo `pass`/`fail` non e' un dato: e'
un'affermazione.

Vale per i titoli promossi (`scanner_v3_*.json`) e per quelli esclusi
(`excluded_*.json`), senza distinzione.

## 1. Quattro stati, non due

Ogni gate ha uno di quattro stati:

| Stato | Significato | Promuove |
|---|---|---|
| `PASS` | valori presenti, condizione soddisfatta | si' |
| `FAIL` | valori presenti, condizione non soddisfatta | no |
| `UNVERIFIED` | un valore necessario e' `null` o assente alla fonte | no |
| `ERROR` | il gate non e' stato valutato per un errore di pipeline | no |

`UNVERIFIED` ed `ERROR` non sono un pass: sono l'assenza di un verdetto. La
distinzione fra i due conta perche' hanno cause diverse — il primo e' un buco
del provider, il secondo un guasto del run (e va anche in `run_metadata.errors`).

Nel record gli stati si esprimono con tre liste; tutto cio' che non compare in
nessuna delle tre e' `PASS`:

```json
"failed_gates": ["price_above_sma50"],
"unverified_gates": ["operating_margin"],
"error_gates": []
```

## 2. `audit_status` di record

Ogni record espone un `audit_status` che riassume i suoi gate con la precedenza
`ERROR > FAIL > UNVERIFIED > PASS`:

```json
"ticker": "AAON",
"audit_status": "FAIL"
```

`audit_status = "PASS"` significa che **ogni** gate e' `PASS`. Un titolo con
anche un solo gate `UNVERIFIED` non e' `PASS`: e' `UNVERIFIED`. Questo elimina
il caso ambiguo per cui oggi un dato mancante finisce per assomigliare a una
promozione.

`audit_status` resta distinto da `final_setup_ready`, che il README impone a
`false` finche' non c'e' revisione qualitativa. `audit_status = PASS` dice solo
che i gate quantitativi sono stati superati e sono ricalcolabili.

## 3. Valuta tutto, escludi subito

Lo short-circuit non va rimosso: va separato in due decisioni distinte che oggi
coincidono.

- **Esclusione**: immediata al primo `FAIL`. Il titolo e' fuori, non cambia.
- **Valutazione**: prosegue su tutti i gate rimanenti, e ne pubblica i valori.

```
gate1 FAIL -> segna FAIL, il titolo e' escluso
           -> continua: gate2, gate3, gate4, ... fino alla fine
```

Nel run 2026-08-05 AAON e' escluso dal solo `earnings_window` allo stadio
fondamentale e non arriva mai a quello tecnico: le sue SMA non esistono
nell'output. Non e' un caso isolato — 472 record su 551 non hanno alcun valore
tecnico, 79 non hanno alcun valore fondamentale.

### Il costo non e' uniforme

Misurato sui `retrieved_at` del run 2026-08-05:

| Stadio | Costo osservato | Estensione a 551 titoli |
|---|---|---|
| Fondamentale (Finviz) | un solo fetch bulk, timestamp identico per 472 record | gratis, gia' copre l'universo |
| Tecnico (TradingView) | 395 s per 33 titoli = **12,3 s/titolo** | **~113 minuti** |

Quindi:

- per i gate fondamentali e d'universo la valutazione completa e' **a costo
  zero**: i dati sono gia' stati scaricati per tutti, vanno solo valutati e
  pubblicati. Qui non c'e' motivo di fermarsi al primo `FAIL`.
- per i gate tecnici il vincolo e' la latenza per titolo, non il calcolo. Le
  strade sono tre: accettare un run da ~2 ore; parallelizzare le richieste
  (12,3 s/titolo e' tempo d'attesa, non di CPU: con 8 richieste in parallelo si
  torna sotto i 15 minuti); oppure restare selettivi.

### Se si resta selettivi

L'unica forma accettabile e' dichiararlo. I gate non calcolati vanno pubblicati
con valori `null`, stato `UNVERIFIED` e motivo esplicito:

```json
"unverified_gates": ["price_above_sma50", "rsi14"],
"missing_details": {
  "sma50": {"reason": "stage_not_executed", "source": "TradingView MCP"}
}
```

Mai per omissione. Un campo assente e un campo dichiarato mancante non sono la
stessa cosa: il secondo e' un dato, il primo e' un silenzio.

## 4. Valori richiesti, gate per gate

Tutti in `values`, con `null` quando il dato non c'e'.

| Gate | Valori |
|---|---|
| `price_min` | `price` |
| `market_cap_min` | `market_cap` |
| `avg_volume_min` | `avg_volume_20d` |
| `price_above_sma50` | `price`, `sma50` |
| `sma50_above_sma150` | `sma50`, `sma150` |
| `sma150_above_sma200` | `sma150`, `sma200` |
| `ema21_above_ema50` | `ema21`, `ema50` |
| `rsi14` | `rsi14` |
| `atr_pct` | `atr_pct` |
| `rvol20` | `rvol20` |
| `performance_21d` | `performance_21d_pct` |
| `no_extended_move_10d` | `move_10d_pct` |
| `within_25pct_52w_high` | `distance_52w_high_pct` |
| `distance_resistance` | `distance_resistance_pct` |
| `revenue_growth` | `revenue_growth_yoy` |
| `eps_growth` | `eps_growth_yoy` |
| `eps_next_year` | `eps_next_year` |
| `operating_margin` | `operating_margin` |
| `adr` | `is_adr` |
| `biotech_pre_revenue` | `industry`, `revenue_ttm` |
| `earnings_window` | `days_to_earnings` |

Esempio completo:

```json
{
  "ticker": "AAON",
  "audit_status": "FAIL",
  "failed_gates": ["earnings_window"],
  "unverified_gates": [],
  "error_gates": [],
  "values": {
    "price": 93.15,
    "market_cap": 7600000000,
    "avg_volume_20d": 1250000,

    "ema21": 95.30,
    "ema50": 98.70,
    "sma50": 106.40,
    "sma150": 109.80,
    "sma200": 119.30,
    "trend_structural_pass": false,

    "rsi14": 61.3,
    "atr_pct": 4.8,
    "rvol20": 1.41,
    "performance_21d_pct": 12.4,
    "move_10d_pct": 9.1,
    "distance_52w_high_pct": 6.2,
    "distance_resistance_pct": 11.7,

    "revenue_growth_yoy": 54.3,
    "eps_growth_yoy": 36.2,
    "eps_next_year": 41.7,
    "operating_margin": 10.4,

    "is_adr": false,
    "industry": "Building Products",
    "revenue_ttm": 1250000000,
    "days_to_earnings": 3
  }
}
```

### `trend_structural_pass`

E' esattamente `price > sma50 && sma50 > sma150 && sma150 > sma200`. Non
include `ema21/ema50`: le EMA sono un gate separato e restano fuori dal flag
strutturale. Se uno qualsiasi dei quattro valori e' `null`, il flag e' `false` e
i gate corrispondenti vanno in `unverified_gates` o `error_gates`.

## 5. Soglie dichiarate, non dedotte

`run_metadata.thresholds` deve contenere ogni soglia usata, in forma piatta e
con la semantica del confronto esplicita. Oggi mancano quelle dei gate
fondamentali, il massimo di distanza dai massimi e la regola della finestra
earnings: il validatore le deduce dalla separazione osservata nei dati e lo
dichiara nel report, ma e' un'inferenza sul comportamento, non un contratto.

```json
"thresholds": {
  "price_min": 15.0,
  "market_cap_min": 2000000000,
  "avg_volume_min": 750000,

  "rsi_min": 55.0,
  "rsi_max": 72.0,
  "atr_pct_min": 3.0,
  "rvol20_min": 1.2,
  "performance_21d_min": 0.0,
  "performance_21d_max": 30.0,
  "move_10d_max": 30.0,

  "within_52w_high_max_pct": 25.0,
  "distance_resistance_min": 8.0,

  "revenue_growth_min": 20.0,
  "eps_growth_min": 30.0,
  "eps_growth_alt_min": 20.0,
  "eps_growth_alt_revenue_min": 40.0,
  "eps_next_year_min": 15.0,
  "eps_next_year_comparison": "strict",
  "operating_margin_min": 8.0,

  "trend_structure": "price > sma50 > sma150 > sma200",
  "ema_structure": "ema21 > ema50",
  "earnings_blackout_days": 7,
  "earnings_window_rule": "no_earnings_within_blackout",
  "pead_window_min": 1,
  "pead_window_max": 15
}
```

`eps_growth` ammette un ramo alternativo: passa con
`eps_growth_yoy >= eps_growth_min`, oppure con `eps_growth_yoy >=
eps_growth_alt_min` accompagnato da `revenue_growth_yoy >=
eps_growth_alt_revenue_min`. Il fatturato viene consultato solo se il ramo
principale non basta, cosi' un titolo con EPS sopra la soglia piena non diventa
`UNVERIFIED` perche' manca il fatturato. Se invece serve il ramo alternativo e
il fatturato e' `null`, il gate e' `UNVERIFIED`: e' il caso di IDYA, USAR e
AMLX, che oggi passano.

Il validatore accetta anche la forma a intervallo attuale (`"rsi": [55, 72]`) e
la normalizza, ma la forma piatta e' quella canonica: `rsi_min` e `rsi_max` non
richiedono di sapere quale elemento della lista sia il minimo.

## 6. Dati mancanti

`missing_fields` elenca **ogni** campo `null` presente in `values`, e
`run_metadata.missing_data_count` li conta. Un campo `null` implica che il gate
che lo usa sia in `unverified_gates` o `error_gates`: mai `PASS`.

`missing_details` dichiara per ciascuno il motivo e la fonte interrogata. I
motivi ammessi determinano lo stato del gate e la penalita' di qualita':

| `reason` | Stato del gate | Penalita' |
|---|---|---|
| `source_no_data` | `UNVERIFIED` | -3 |
| `stage_not_executed` | `UNVERIFIED` | -3 |
| `pipeline_error` | `ERROR` | -10 |

```json
"missing_details": {
  "operating_margin": {"reason": "source_no_data", "source": "finvizfinance"},
  "sma200": {"reason": "pipeline_error", "source": "TradingView MCP"}
}
```

## 7. `data_quality_score`

Un numero per record, da 0 a 100, con il minimo a 0:

```
100 - 3 per ogni campo atteso non utilizzabile
    - 10 se la causa e' un guasto di pipeline
```

Il conteggio parte dai **campi attesi** dal registro dei gate, non da quelli
presenti nel record. E' la differenza che rende la metrica utile: contando solo
i `null` presenti, il run 2026-08-05 prenderebbe 99/100, perche' i campi che
mancano non sono `null` — sono assenti. Cosi' misurata, la metrica premierebbe
l'omissione. Un campo assente vale quindi `not_exported`, -3 come un `null`.

Con questa definizione il run 2026-08-05 vale **39/100**, minimo 0, tutti i 551
record sotto 100.

`data_quality_score` misura la **disponibilita' del dato, non la correttezza del
gate**. Sono indipendenti, e vanno letti insieme: nella fixture `run_con_bug` un
titolo promosso a torto con la catena SMA rotta ha `data_quality_score` 100 —
tutti i valori ci sono, sono i gate a mentire. Un run puo' essere `RUN INVALID`
con qualita' 100, o `RUN VALID` con qualita' 60.

Il punteggio di run e' la media dei punteggi di record. Il validatore lo
ricalcola e segnala i record il cui punteggio dichiarato non corrisponde.

## 8. Pubblicazione condizionata

`latest/` si aggiorna solo dopo un verdetto positivo. `tools/publish_guard.py`
blocca su verdetto diverso da `RUN VALID`, soglie dedotte, o titoli promossi con
`audit_status` diverso da `PASS`; in quel caso non scrive nulla nella
destinazione. Le due deroghe (`--allow-not-auditable`, `--allow-deduced`) sono
esplicite e restano stampate nell'output del run.

## 9. Verifica

```
python3 tools/validate_run.py latest/          # leggibile
python3 tools/validate_run.py latest/ --json   # per consumo automatico
python3 tests/run_tests.py                     # test del validatore
```

Il validatore ricalcola ogni gate dai valori pubblicati e lo confronta con lo
stato dichiarato. Verdetto:

| Verdetto | Exit | Significato |
|---|---|---|
| `RUN VALID` | 0 | ogni gate ricalcolabile e coerente col dichiarato |
| `RUN INVALID` | 1 | almeno un gate dichiarato diverge dal ricalcolo |
| `RUN NON AUDITABILE` | 2 | strumentazione incompleta: gate non ricalcolabili |

Le divergenze sono raggruppate per gravita':

- **fail-open** — dichiarato `PASS` dove il ricalcolo nega il pass. E' il caso
  pericoloso: un titolo puo' essere promosso senza titolo per esserlo.
- **esclusioni ingiustificate** — il motore esclude un titolo che il ricalcolo
  promuove.
- **etichettatura** — entrambi non-`PASS` ma con etichette diverse (tipicamente
  `FAIL` dichiarato dove il dato manca e lo stato corretto sarebbe `UNVERIFIED`
  o `ERROR`). L'esito operativo e' giusto, lo stato dichiarato no.

Tutte e tre rendono il run `INVALID`: un gate che diverge dal ricalcolo e' un
gate di cui non ci si puo' fidare, indipendentemente dalla direzione.
