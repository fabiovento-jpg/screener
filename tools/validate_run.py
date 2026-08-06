#!/usr/bin/env python3
"""Validatore degli output dello Scanner 3.0.

Ricalcola l'esito di ogni gate a partire dai valori numerici scritti nel JSON
e lo confronta con la lista `failed_gates`. Serve a rispondere a una domanda
sola: i gate dichiarati sono coerenti con i numeri pubblicati?

Un gate e' auditabile solo se il record contiene i valori che lo determinano.
I gate non auditabili vengono contati a parte: non sono un "pass", sono un
buco di strumentazione.

Uso:
    python3 tools/validate_run.py latest/
    python3 tools/validate_run.py history/2026-08-05/

Exit code 0 se non ci sono incoerenze, 1 altrimenti.
"""

import json
import sys
from pathlib import Path

# Soglie non dichiarate in run_metadata.thresholds, dedotte dalla separazione
# osservata nei dati (valore, confronto stretto). Vanno sostituite dai valori
# reali appena il motore le pubblica nei metadati.
# eps_next_year usa il confronto stretto: nel run 2026-08-05 un valore esatto
# di 15.0 risulta fallito, quindi la soglia e' "> 15" e non ">= 15".
FUNDAMENTAL_THRESHOLDS = {
    "revenue_growth": ("revenue_growth_yoy", 20.0, False),
    "eps_growth": ("eps_growth_yoy", 30.0, False),
    "eps_next_year": ("eps_next_year", 15.0, True),
    "operating_margin": ("operating_margin", 8.0, False),
}

# Gate della struttura di trend: catena price > SMA50 > SMA150 > SMA200.
TREND_CHAIN = [
    ("price_above_sma50", "price", "sma50"),
    ("sma50_above_sma150", "sma50", "sma150"),
    ("sma150_above_sma200", "sma150", "sma200"),
    ("ema21_above_ema50", "ema21", "ema50"),
]


class Report:
    def __init__(self):
        self.mismatches = []
        self.fail_open = []
        self.unauditable = {}
        self.audited = 0

    def mismatch(self, ticker, gate, detail):
        self.mismatches.append((ticker, gate, detail))

    def opened(self, ticker, gate, detail):
        self.fail_open.append((ticker, gate, detail))

    def blind(self, gate):
        self.unauditable[gate] = self.unauditable.get(gate, 0) + 1


def check_threshold(rep, ticker, failed, values, gate, key, minimum, maximum=None, strict=False):
    """Verifica un gate a soglia. `key` assente -> gate non auditabile."""
    if key not in values:
        rep.blind(gate)
        return
    value = values[key]
    flagged = gate in failed
    if value is None:
        # Dato non disponibile: il gate non e' verificabile e non deve promuovere.
        if not flagged:
            rep.opened(ticker, gate, f"{key}=null ma il gate non e' in failed_gates")
        return
    if maximum is None:
        ok = value > minimum if strict else value >= minimum
    else:
        ok = minimum <= value <= maximum
    if ok and flagged:
        rep.mismatch(ticker, gate, f"{key}={value!r} rispetta la soglia ma il gate risulta fallito")
    elif not ok and not flagged:
        rep.mismatch(ticker, gate, f"{key}={value!r} viola la soglia ma il gate non risulta fallito")


def check_pair(rep, ticker, failed, values, gate, upper, lower):
    """Verifica un gate di confronto fra due serie (es. price > sma50)."""
    if upper not in values or lower not in values:
        rep.blind(gate)
        return
    a, b = values[upper], values[lower]
    flagged = gate in failed
    if a is None or b is None:
        if not flagged:
            rep.opened(ticker, gate, f"{upper}={a!r} {lower}={b!r} ma il gate non e' in failed_gates")
        return
    ok = a > b
    if ok and flagged:
        rep.mismatch(ticker, gate, f"{upper}={a} > {lower}={b} ma il gate risulta fallito")
    elif not ok and not flagged:
        rep.mismatch(ticker, gate, f"{upper}={a} <= {lower}={b} ma il gate non risulta fallito")


def check_trend_flag(rep, ticker, values, failed):
    """`trend_structural_pass` deve coincidere con l'AND della catena."""
    if "trend_structural_pass" not in values:
        rep.blind("trend_structural_pass")
        return
    declared = values["trend_structural_pass"]
    needed = ["price", "sma50", "sma150", "sma200"]
    if any(values.get(k) is None for k in needed) or not all(k in values for k in needed):
        if declared:
            rep.opened(ticker, "trend_structural_pass",
                       "dichiarato true con almeno un valore della catena mancante")
        return
    computed = (values["price"] > values["sma50"] > values["sma150"] > values["sma200"])
    if declared != computed:
        rep.mismatch(
            ticker, "trend_structural_pass",
            "dichiarato {} ma price={} sma50={} sma150={} sma200={} danno {}".format(
                declared, values["price"], values["sma50"], values["sma150"],
                values["sma200"], computed),
        )
    chain_failed = {g for g, _, _ in TREND_CHAIN[:3]} & set(failed)
    if declared and chain_failed:
        rep.mismatch(ticker, "trend_structural_pass",
                     f"dichiarato true ma failed_gates contiene {sorted(chain_failed)}")


def validate_record(rep, record, thresholds):
    ticker = record.get("ticker", "?")
    values = record.get("values", {})
    failed = set(record.get("failed_gates", []))
    rep.audited += 1

    for gate, upper, lower in TREND_CHAIN:
        check_pair(rep, ticker, failed, values, gate, upper, lower)
    check_trend_flag(rep, ticker, values, failed)

    rsi_min, rsi_max = thresholds["rsi"]
    perf_min, perf_max = thresholds["performance_21d"]
    check_threshold(rep, ticker, failed, values, "rsi14", "rsi14", rsi_min, rsi_max)
    check_threshold(rep, ticker, failed, values, "atr_pct", "atr_pct", thresholds["atr_pct_min"])
    check_threshold(rep, ticker, failed, values, "rvol20", "rvol20", thresholds["rvol20_min"])
    check_threshold(rep, ticker, failed, values, "performance_21d", "performance_21d_pct",
                    perf_min, perf_max)
    check_threshold(rep, ticker, failed, values, "distance_resistance", "distance_resistance_pct",
                    thresholds["distance_resistance_min"])
    if "distance_52w_high_pct" in values:
        check_threshold(rep, ticker, failed, values, "within_25pct_52w_high",
                        "distance_52w_high_pct", float("-inf"), 25.0)
    else:
        rep.blind("within_25pct_52w_high")

    for gate, (key, minimum, strict) in FUNDAMENTAL_THRESHOLDS.items():
        check_threshold(rep, ticker, failed, values, gate, key, minimum, strict=strict)

    # Un campo dichiarato mancante non puo' lasciare passare il gate corrispondente.
    for field in record.get("missing_fields", []):
        for gate, (key, _, _strict) in FUNDAMENTAL_THRESHOLDS.items():
            if field == key and gate not in failed:
                rep.opened(ticker, gate, f"{key} in missing_fields ma il gate non e' in failed_gates")
        for gate, upper, lower in TREND_CHAIN:
            if field in (upper, lower) and gate not in failed:
                rep.opened(ticker, gate, f"{field} in missing_fields ma il gate non e' in failed_gates")


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    run_dir = Path(argv[1])
    meta_path = next((p for p in run_dir.glob("run_metadata_*.json")), None)
    excl_path = next((p for p in run_dir.glob("excluded_*.json")), None)
    pass_path = next((p for p in run_dir.glob("scanner_v3_*.json")), None)
    if not (meta_path and excl_path and pass_path):
        print(f"[errore] {run_dir}: attesi run_metadata_*, excluded_* e scanner_v3_*.json")
        return 2

    meta = load(meta_path)
    thresholds = meta["thresholds"]
    rep = Report()

    promoted = load(pass_path).get("titoli", [])
    excluded = load(excl_path).get("titoli", [])
    for record in promoted + excluded:
        validate_record(rep, record, thresholds)

    print(f"run: {run_dir}  sessione {meta.get('market_session_date')}")
    print(f"record esaminati: {rep.audited} ({len(promoted)} promossi, {len(excluded)} esclusi)")

    if rep.mismatches:
        print(f"\nINCOERENZE gate/valori: {len(rep.mismatches)}")
        for ticker, gate, detail in rep.mismatches:
            print(f"  {ticker:8} {gate:24} {detail}")
    else:
        print("\nIncoerenze gate/valori: nessuna fra i gate auditabili.")

    if rep.fail_open:
        print(f"\nFAIL-OPEN su dato mancante: {len(rep.fail_open)}")
        for ticker, gate, detail in rep.fail_open:
            print(f"  {ticker:8} {gate:24} {detail}")
    else:
        print("Fail-open su dato mancante: nessuno.")

    if rep.unauditable:
        print("\nGATE NON AUDITABILI (valori non pubblicati nel JSON):")
        for gate, count in sorted(rep.unauditable.items(), key=lambda kv: -kv[1]):
            print(f"  {gate:24} {count} record senza i valori necessari")

    return 1 if (rep.mismatches or rep.fail_open) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
