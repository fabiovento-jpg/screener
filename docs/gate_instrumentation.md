# Strumentazione dei gate — schema richiesto

Questo documento definisce cosa il motore dello Scanner 3.0 deve scrivere nei
JSON di output perche' ogni gate sia **verificabile a posteriori**, senza
accesso al codice e senza rieseguire la scansione.

Regola generale: **nessun gate puo' essere pubblicato come solo `pass`/`fail`.
Ogni gate deve pubblicare gli operandi numerici che lo determinano**, sia per i
titoli promossi (`scanner_v3_*.json`) sia per quelli esclusi (`excluded_*.json`).

## 1. Blocco struttura di trend

La regola e' una catena unica:

```
price > SMA50 > SMA150 > SMA200
```

Nell'output attuale la catena e' spezzata in tre gate distinti
(`price_above_sma50`, `sma50_above_sma150`, `sma150_above_sma200`) piu' un
quarto gate indipendente (`ema21_above_ema50`). La scomposizione va bene, ma
deve essere accompagnata dai valori e dal risultato aggregato.

Ogni record — promosso o escluso — deve contenere in `values`:

```json
"price": 93.15,
"sma50": 106.40,
"sma150": 109.80,
"sma200": 119.30,
"ema21": 95.02,
"ema50": 101.77,
"trend_structural_pass": false
```

Vincoli che il validatore verifica:

- `trend_structural_pass` e' esattamente
  `price > sma50 && sma50 > sma150 && sma150 > sma200`. Non include `ema21/ema50`:
  le EMA sono un gate separato e vanno lasciate fuori dal flag strutturale.
- `trend_structural_pass = true` e' incompatibile con la presenza di
  `price_above_sma50`, `sma50_above_sma150` o `sma150_above_sma200` in
  `failed_gates`.
- se uno qualsiasi fra `price`, `sma50`, `sma150`, `sma200` e' `null`,
  `trend_structural_pass` deve essere `false` e i gate corrispondenti devono
  comparire in `failed_gates` (regola fail-closed del README).

## 2. Stesso trattamento per tutti gli altri gate

Ogni gate deve pubblicare i propri operandi nel record, anche quando il titolo
e' gia' stato escluso da un gate precedente. Un'esclusione anticipata non
giustifica l'assenza dei valori: senza di essi il gate non e' auditabile.

| Gate | Valori richiesti in `values` |
|---|---|
| `price_above_sma50`, `sma50_above_sma150`, `sma150_above_sma200` | `price`, `sma50`, `sma150`, `sma200` |
| `ema21_above_ema50` | `ema21`, `ema50` |
| `rsi14` | `rsi14` |
| `atr_pct` | `atr14`, `atr_pct` |
| `rvol20` | `rvol20` |
| `performance_21d` | `performance_21d_pct` |
| `within_25pct_52w_high` | `week52_high`, `distance_52w_high_pct` |
| `distance_resistance` | `resistance`, `distance_resistance_pct` |
| `no_extended_move_10d` | `move_10d_pct` |
| `revenue_growth` | `revenue_growth_yoy` |
| `eps_growth` | `eps_growth_yoy` |
| `eps_next_year` | `eps_next_year` |
| `operating_margin` | `operating_margin` |
| `earnings_window` | `next_earnings_date`, `days_to_earnings` |
| `adr`, `biotech_pre_revenue` | `industry`, piu' il campo che ha attivato il filtro |

## 3. Soglie: vanno dichiarate tutte

`run_metadata.thresholds` oggi non dichiara le soglie dei gate fondamentali ne'
la definizione della catena SMA/EMA. Dedurle dai dati e' possibile ma fragile.
Vanno aggiunte, con la semantica del confronto esplicita (`>=` o `>`):

```json
"revenue_growth_min": 20.0,
"eps_growth_min": 30.0,
"eps_next_year_min": 15.0,
"eps_next_year_comparison": "strict",
"operating_margin_min": 8.0,
"trend_structure": "price > sma50 > sma150 > sma200",
"ema_structure": "ema21 > ema50",
"within_52w_high_max_pct": 25.0
```

## 4. Dati mancanti

`missing_fields` deve elencare **ogni** campo `null` presente in `values`, e
`run_metadata.missing_data_count` deve contarli. Un campo assente o `null`
implica che il gate che lo usa compaia in `failed_gates`: mai il contrario.

## 5. Verifica

```
python3 tools/validate_run.py latest/
```

Il validatore ricalcola l'esito di ogni gate dai valori pubblicati, lo confronta
con `failed_gates`, segnala i fail-open su dato mancante ed elenca i gate che
restano non auditabili perche' i valori non sono stati scritti. Exit code 1 in
presenza di incoerenze.
