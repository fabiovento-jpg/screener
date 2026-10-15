# FORWARD SHADOW PROTOCOL — MOMENTUM_12_1_LIQUID500_V1

**Stato operativo di ricerca: `CANDIDATE_SHADOW`**

```
NOT VALIDATED FOR CAPITAL
NO AUTOMATIC ORDER
```

Questo documento e' **congelato**. Nessuna sua parte va modificata durante il
forward test. Una modifica a questo file durante il periodo invalida il campione
forward: e' esattamente la condizione che il criterio di promozione esclude.

---

## 1. Classificazione

| Campo | Valore |
|---|---|
| Strategia | `MOMENTUM_12_1_LIQUID500_V1` |
| Classificazione storica | **`FAILED`** secondo il gate congelato originale |
| Stato operativo di ricerca | **`CANDIDATE_SHADOW`** |
| Autorizzazione capitale | **nessuna** |
| Ordini automatici | **nessuno** |

La classificazione storica `FAILED` **resta invariata**. `CANDIDATE_SHADOW` non
la sostituisce e non la attenua: e' uno stato di osservazione prospettica
parallelo. La strategia **non e'** `VALIDATED_SHADOW`.

`HIGH52_GH` resta `VALIDATED_SHADOW`, separata e non modificata. Nessuna
variante `HIGH52` viene riaperta.

---

## 2. Parametri congelati

Nessuno di questi valori puo' cambiare durante il forward test.

| Parametro | Valore congelato |
|---|---|
| Universo | TOP500 per ADV20, **point-in-time** |
| Formation | 252 sedute |
| Skip | 21 sedute |
| Selezione | top quintile (Q5) del ranking PRET |
| Ingresso | **open della seduta successiva** al signal date |
| Holding | 126 sedute |
| Stop loss | **nessuno** |
| Filtro di regime | **nessuno** |
| Filtro SMA | **nessuno** |
| Altri parametri | **nessuno** |

Nessun altro backtest, nessuna variante, nessun tuning.

---

## 3. Perche' il forward test

Il development 2023-2025 e' forte. I valori che seguono sono **registrati come
forniti** e non sono stati ricalcolati in questo repository, che non contiene il
motore di backtest ne' i dati delle coorti:

| Metrica development | Valore |
|---|---|
| Anni positivi | 3 su 3 |
| Avg trade | +15,19% |
| Profit factor | 3,09 |
| Excess vs SPY | +5,44% |
| Excess vs Liquid500 EW | +7,09% |
| Portfolio CAGR | 25,67% (SPY 21,26%) |
| Robustezza | tiene senza i best 2 e senza il top 1% |
| MaxDD development | **-29,94%** |

Contro, e sono le ragioni per cui serve conferma prospettica:

- l'ipotesi e' **derivata post-hoc** dal 2023-2025;
- OOS 2022: **solo 2 coorti**;
- OOS 2026: **solo 4 coorti chiuse**;
- OOS combinato, excess vs SPY: **-0,68%**.

Un development forte su un'ipotesi formulata dopo aver visto quel development
non e' evidenza. Il forward test e' l'unico campione non contaminato.

---

## 4. Forward freeze

| Campo | Valore |
|---|---|
| `FORWARD_START_DATE` | **2026-10-05** (lunedi') |
| Attivazione | 2026-10-04 (domenica) |
| Campione | `FORWARD_OOS` |

`FORWARD_START_DATE` e' la prima seduta USA successiva all'attivazione. **Non e'
retroattiva.**

Regole del campione, senza eccezioni:

1. ogni ranking e ogni segnale con `signal_date >= 2026-10-05` appartiene a
   `FORWARD_OOS`;
2. nessun dato, ranking o trade precedente al 2026-10-05 puo' entrare nel
   campione forward, **in nessuna circostanza e per nessun motivo**;
3. il campione forward non si riapre e non si ricostruisce a posteriori.

### Primo segnale atteso

| Evento | Data |
|---|---|
| Primo `signal_date` forward | 2026-10-30 (ultima seduta di ottobre 2026) |
| Primo `entry_date` | 2026-11-02 open |
| Primo `planned_exit_date` | 126a seduta dall'ingresso |

### Da confermare prima del primo segnale

Il giorno del ranking mensile **non e'** fra i parametri che mi sono stati
elencati. Questo documento assume la **ultima seduta di calendario del mese**
come `signal_date`, con ingresso all'open successivo, perche' e' la convenzione
compatibile con coorti mensili e holding di 126 sedute.

**Se il development usava un giorno diverso, va corretto prima del 2026-10-30.**
Dopo quella data una correzione e' una modifica di parametro durante il forward
test, e azzera il campione.

---

## 5. Criterio di promozione

**Congelato ora, prima di qualunque risultato forward.** Queste soglie non
vanno cambiate in futuro in base ai risultati osservati.

Una promozione futura richiede **tutte** queste condizioni insieme:

| # | Condizione |
|---|---|
| 1 | almeno **12 coorti mensili complete** |
| 2 | avg return forward > 0 |
| 3 | profit factor forward > 1 |
| 4 | excess return forward vs SPY > 0 |
| 5 | excess return forward vs Liquid500 EW > 0 |
| 6 | portfolio return forward > SPY |
| 7 | nessuna modifica ai parametri durante il periodo |
| 8 | nessuna esclusione manuale dei trade |

**Preferenza forte: 24 coorti complete.**

Dodici coorti sono il minimo, non l'obiettivo. Una promozione a 12 coorti con
margini sottili resta debole; a 24 coorti lo stesso risultato significa molto
piu'.

Le condizioni 7 e 8 sono condizioni sul **processo**, non sui rendimenti: se
cadono, le altre sei non contano. Un parametro ritoccato a metà periodo o un
trade escluso a mano rendono il campione inutilizzabile, qualunque sia il
risultato.

---

## 6. Drawdown

Il limite arbitrario **SPY -10 punti non viene piu' usato** per modificare la
strategia. Non e' un criterio: era una soglia inventata.

Durante il forward test il drawdown viene **soltanto misurato**, mai usato per
intervenire:

- forward MaxDD della strategia
- SPY MaxDD
- Liquid500 EW MaxDD
- volatilita'
- Sharpe (descrittivo)

La valutazione del rischio avviene **dopo** una conferma reale dell'edge. Non si
modifica la strategia durante il forward test per reagire a un drawdown: un
drawdown dentro il campione e' un dato del campione, non un guasto da riparare.

---

## 7. Ledger

| Campo | Valore |
|---|---|
| Nome | `FORWARD_ONLY` |
| File | `forward/MOMENTUM_12_1_LIQUID500_V1/ledger_FORWARD_ONLY.csv` |
| Append | esclusivamente via `tools/forward_ledger.py` |

Colonne registrate per ogni trade:

```
signal_date  ticker  security_id  PRET  ADV20
entry_date  entry_price  planned_exit_date  exit_date  exit_price
return  spy_matched_return  liquid500_ew_matched_return
strategy_version  sample  prev_hash  row_hash
```

Il ledger e' **append-only e immutabile**. L'immutabilita' non e' una promessa:
ogni riga porta `row_hash`, calcolato sul proprio contenuto piu' il `row_hash`
della riga precedente. Una modifica retroattiva a una riga qualsiasi rompe la
catena di tutte le righe successive, e `tools/forward_ledger.py --verify` la
rileva.

Il guard rifiuta, senza possibilita' di deroga:

- qualunque riga con `signal_date < 2026-10-05`;
- qualunque riga con `strategy_version` diverso da `MOMENTUM_12_1_LIQUID500_V1`;
- qualunque append su un ledger la cui catena di hash e' gia' rotta.

---

## 8. Cosa questo protocollo non autorizza

- nessun ordine, automatico o suggerito;
- nessun consiglio di acquisto;
- nessuna allocazione di capitale;
- nessuna promozione di stato prima delle 12 coorti complete e delle altre
  sette condizioni;
- nessuna modifica dei parametri, delle soglie di promozione o di questo
  documento durante il forward test.
