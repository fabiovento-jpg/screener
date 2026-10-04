#!/usr/bin/env python3
"""Ledger FORWARD_ONLY di MOMENTUM_12_1_LIQUID500_V1: append-only e verificabile.

Il ledger registra esclusivamente trade del campione FORWARD_OOS. Nessun trade
storico puo' entrarci: il guard rifiuta qualunque riga con
`signal_date < FORWARD_START_DATE`, e il rifiuto non ha deroghe.

L'immutabilita' non e' una promessa ma una catena: ogni riga porta `row_hash`,
calcolato sul proprio contenuto piu' il `row_hash` della riga precedente. Una
modifica retroattiva a una riga qualsiasi rompe la catena di tutte le righe
successive, e `--verify` la rileva.

Uso:
    python3 tools/forward_ledger.py --verify
    python3 tools/forward_ledger.py --append trade.json
    python3 tools/forward_ledger.py --append-many trades.json
    python3 tools/forward_ledger.py --summary

Exit code: 0 ok, 1 catena rotta o append rifiutato, 64 errore d'uso.
"""

import argparse
import csv
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STRATEGY = "MOMENTUM_12_1_LIQUID500_V1"
FREEZE = ROOT / "forward" / STRATEGY / "freeze.json"
LEDGER = ROOT / "forward" / STRATEGY / "ledger_FORWARD_ONLY.csv"

# L'ordine e' parte del contratto: `row_hash` si calcola su questi campi in
# questa sequenza, quindi riordinarli invaliderebbe ogni riga gia' scritta.
FIELDS = [
    "signal_date", "ticker", "security_id", "PRET", "ADV20",
    "entry_date", "entry_price", "planned_exit_date", "exit_date", "exit_price",
    "return", "spy_matched_return", "liquid500_ew_matched_return",
    "strategy_version", "sample", "prev_hash", "row_hash",
]
HASHED = [f for f in FIELDS if f not in ("row_hash",)]

GENESIS = "0" * 64
EXIT_OK, EXIT_REFUSED, EXIT_USAGE = 0, 1, 64


def freeze():
    with open(FREEZE, encoding="utf-8") as handle:
        return json.load(handle)


def row_hash(row):
    payload = "|".join(f"{k}={row.get(k, '')}" for k in HASHED)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def read_rows():
    if not LEDGER.exists():
        return []
    with open(LEDGER, newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def verify(rows):
    """Ritorna la lista dei problemi trovati nella catena."""
    problems, previous = [], GENESIS
    for index, row in enumerate(rows, start=1):
        if row.get("prev_hash") != previous:
            problems.append(
                f"riga {index} ({row.get('ticker')} {row.get('signal_date')}): "
                f"prev_hash {row.get('prev_hash')!r}, atteso {previous!r}")
        expected = row_hash(row)
        if row.get("row_hash") != expected:
            problems.append(
                f"riga {index} ({row.get('ticker')} {row.get('signal_date')}): "
                f"row_hash non corrisponde al contenuto — riga alterata dopo la scrittura")
        previous = row.get("row_hash") or ""
    return problems


def refusals(trade, cfg):
    """Motivi per cui un trade non puo' entrare nel ledger."""
    out = []
    missing = [f for f in FIELDS if f not in ("prev_hash", "row_hash", "sample",
                                              "strategy_version")
               and f not in trade]
    if missing:
        out.append("campi mancanti: " + ", ".join(missing))

    signal_date = str(trade.get("signal_date", ""))
    start = cfg["forward_start_date"]
    if not signal_date:
        out.append("signal_date assente")
    elif signal_date < start:
        out.append(f"signal_date {signal_date} precede FORWARD_START_DATE {start}: "
                   "nessun trade pre-forward puo' entrare nel ledger")

    version = trade.get("strategy_version", STRATEGY)
    if version != STRATEGY:
        out.append(f"strategy_version {version!r}, atteso {STRATEGY!r}")
    return out


def append(trades, cfg):
    rows = read_rows()
    problems = verify(rows)
    if problems:
        print("APPEND RIFIUTATO — la catena del ledger e' gia' rotta:")
        for problem in problems:
            print(f"  - {problem}")
        return EXIT_REFUSED

    accepted = []
    previous = rows[-1]["row_hash"] if rows else GENESIS
    for trade in trades:
        reasons = refusals(trade, cfg)
        if reasons:
            print(f"APPEND RIFIUTATO — {trade.get('ticker', '?')} "
                  f"{trade.get('signal_date', '?')}:")
            for reason in reasons:
                print(f"  - {reason}")
            return EXIT_REFUSED
        row = {field: "" for field in FIELDS}
        row.update({k: v for k, v in trade.items() if k in FIELDS})
        row["strategy_version"] = STRATEGY
        row["sample"] = cfg["forward_sample"]
        row["prev_hash"] = previous
        row["row_hash"] = row_hash(row)
        previous = row["row_hash"]
        accepted.append(row)

    exists = LEDGER.exists()
    with open(LEDGER, "a", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS)
        if not exists:
            writer.writeheader()
        for row in accepted:
            writer.writerow(row)

    for row in accepted:
        print(f"registrato  {row['signal_date']}  {row['ticker']:8} "
              f"PRET={row['PRET']}  entry={row['entry_date']}  "
              f"row_hash={row['row_hash'][:12]}")
    print(f"\n{len(accepted)} righe aggiunte. Totale ledger: {len(rows) + len(accepted)}.")
    return EXIT_OK


def summary(rows, cfg):
    closed = [r for r in rows if r.get("exit_date")]
    cohorts = sorted({r["signal_date"] for r in rows})
    closed_cohorts = sorted({r["signal_date"] for r in rows
                             if r["signal_date"] not in
                             {x["signal_date"] for x in rows if not x.get("exit_date")}})
    print(f"strategia:      {STRATEGY}")
    print(f"stato:          {cfg['research_status']} — {cfg['capital_authorization']},"
          f" {cfg['order_policy']}")
    print(f"campione:       {cfg['forward_sample']} da {cfg['forward_start_date']}")
    print(f"righe:          {len(rows)} ({len(closed)} chiuse)")
    print(f"coorti:         {len(cohorts)} aperte, {len(closed_cohorts)} complete")
    gate = cfg["promotion_gate"]
    print(f"gate promozione: minimo {gate['min_complete_monthly_cohorts']} coorti complete"
          f" (preferenza {gate['strongly_preferred_cohorts']})")
    if len(closed_cohorts) < gate["min_complete_monthly_cohorts"]:
        mancanti = gate["min_complete_monthly_cohorts"] - len(closed_cohorts)
        print(f"\nNESSUNA VALUTAZIONE DI PROMOZIONE: mancano {mancanti} coorti complete.")
        print("Le metriche forward non vanno lette come evidenza prima della soglia.")
    return EXIT_OK


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--verify", action="store_true")
    group.add_argument("--append", type=Path, metavar="TRADE_JSON")
    group.add_argument("--append-many", type=Path, metavar="TRADES_JSON")
    group.add_argument("--summary", action="store_true")
    args = parser.parse_args()

    cfg = freeze()
    rows = read_rows()

    if args.verify:
        problems = verify(rows)
        if problems:
            print(f"CATENA ROTTA — {len(problems)} problemi:")
            for problem in problems:
                print(f"  - {problem}")
            return EXIT_REFUSED
        print(f"catena integra: {len(rows)} righe, nessuna alterazione rilevata")
        return EXIT_OK

    if args.summary:
        return summary(rows, cfg)

    path = args.append or args.append_many
    with open(path, encoding="utf-8") as handle:
        payload = json.load(handle)
    trades = payload if isinstance(payload, list) else [payload]
    if args.append and len(trades) != 1:
        print("[errore] --append accetta un solo trade; usa --append-many")
        return EXIT_USAGE
    return append(trades, cfg)


if __name__ == "__main__":
    sys.exit(main())
