#!/usr/bin/env python3
"""Test del validatore sulle fixture in tests/fixtures/.

    python3 tests/run_tests.py

Le fixture non sono dati di mercato: sono due run costruiti a mano, uno
conforme e uno che contiene i difetti osservati nel run 2026-08-05, per
verificare che il validatore li distingua.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "tools" / "validate_run.py"

EXIT_VALID, EXIT_INVALID, EXIT_NOT_AUDITABLE = 0, 1, 2


def run(fixture):
    proc = subprocess.run(
        [sys.executable, str(VALIDATOR), str(ROOT / "tests" / "fixtures" / fixture)],
        capture_output=True, text=True,
    )
    return proc.returncode, proc.stdout


CASES = [
    # (fixture, exit code atteso, frammenti attesi nell'output)
    ("run_conforme", EXIT_VALID, [
        "RUN VALID",
        "Divergenze dichiarato/ricalcolato: nessuna.",
        # soglie tutte dichiarate dal motore: il validatore non deduce nulla
        "DATA QUALITY SCORE: 97/100",
    ]),
    ("run_con_bug", EXIT_INVALID, [
        "RUN INVALID",
        # la catena SMA rotta viene ricalcolata gate per gate
        "price_above_sma50        dichiarato=PASS       ricalcolato=FAIL",
        "sma50_above_sma150       dichiarato=PASS       ricalcolato=FAIL",
        "sma150_above_sma200      dichiarato=PASS       ricalcolato=FAIL",
        "trend_structural_pass    dichiarato=PASS       ricalcolato=FAIL",
        # fail-open su valore nullo e su soglia violata
        "revenue_growth           dichiarato=PASS       ricalcolato=UNVERIFIED",
        "eps_growth               dichiarato=PASS       ricalcolato=FAIL",
        # rollup di record e promozione indebita
        "BUG      dichiarato=PASS atteso=FAIL",
        "PROMOSSI CON GATE NON-PASS: BUG",
        # il dato c'e' tutto: la qualita' resta alta mentre il run e' invalido
        "DATA QUALITY SCORE: 98/100",
    ]),
]


def main():
    failures = 0
    for fixture, expected_code, fragments in CASES:
        code, out = run(fixture)
        if code != expected_code:
            print(f"FAIL {fixture}: exit {code}, atteso {expected_code}")
            failures += 1
        for fragment in fragments:
            if fragment not in out:
                print(f"FAIL {fixture}: manca dall'output {fragment!r}")
                failures += 1
        if code == expected_code and all(f in out for f in fragments):
            print(f"ok   {fixture} (exit {code})")

    # Il run reale pubblicato non deve mai risultare valido per sbaglio:
    # oggi e' INVALID, e in ogni caso non e' completamente auditabile.
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(ROOT / "latest")],
                          capture_output=True, text=True)
    if proc.returncode not in (EXIT_INVALID, EXIT_NOT_AUDITABLE):
        print(f"FAIL latest/: exit {proc.returncode}, atteso INVALID o NON AUDITABILE")
        failures += 1
    else:
        print(f"ok   latest/ (exit {proc.returncode})")

    print("\n" + ("TUTTI I TEST OK" if not failures else f"{failures} TEST FALLITI"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
