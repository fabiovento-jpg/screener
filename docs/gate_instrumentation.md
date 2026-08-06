# Schema 3.1 — strumentazione dei gate

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

## 3. Nessuno short-circuit

Nel run 2026-08-05 AAON e' escluso dal solo `earnings_window` allo stadio
fondamentale, e non arriva mai allo stadio tecnico: le sue SMA non esistono
nell'output. Non e' un caso isolato — 472 record su 551 non hanno alcun valore
tecnico, 79 non hanno alcun valore fondamentale.

L'export completo richiede quindi che **tutti i gate siano valutati per tutti i
titoli dell'universo**, anche dopo il primo fallimento. Se calcolare un blocco
per l'intero universo e' troppo costoso, l'alternativa accettabile e' marcare i
gate non calcolati come `UNVERIFIED` con i rispettivi valori a `null` —
esplicitamente, mai per omissione.

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

`run_metadata.thresholds` deve contenere ogni soglia usata, con la semantica del
confronto esplicita. Oggi mancano quelle dei gate fondamentali, il massimo di
distanza dai massimi e la regola della finestra earnings; il validatore le
deduce dalla separazione osservata nei dati, che e' un ripiego fragile:

```json
"revenue_growth_min": 20.0,
"eps_growth_min": 30.0,
"eps_next_year_min": 15.0,
"eps_next_year_comparison": "strict",
"operating_margin_min": 8.0,
"within_52w_high_max_pct": 25.0,
"trend_structure": "price > sma50 > sma150 > sma200",
"ema_structure": "ema21 > ema50",
"earnings_window_rule": "no_earnings_within_blackout"
```

## 6. Dati mancanti

`missing_fields` elenca **ogni** campo `null` presente in `values`, e
`run_metadata.missing_data_count` li conta. Un campo `null` implica che il gate
che lo usa sia in `unverified_gates` o `error_gates`: mai `PASS`.

## 7. Verifica

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
