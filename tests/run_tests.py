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
GUARD = ROOT / "tools" / "publish_guard.py"

EXIT_VALID, EXIT_INVALID, EXIT_NOT_AUDITABLE = 0, 1, 2


def run(fixture, script=None, extra=()):
    proc = subprocess.run(
        [sys.executable, str(script or VALIDATOR),
         str(ROOT / "tests" / "fixtures" / fixture), *extra],
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


# Il cancello di pubblicazione: (fixture, exit atteso, frammenti, opzioni)
GUARD_CASES = [
    ("run_conforme", 0, ["PUBBLICAZIONE CONSENTITA"], ()),
    ("run_con_bug", 1, ["PUBBLICAZIONE BLOCCATA",
                        "promossi con gate ricalcolato non-PASS: BUG",
                        "`latest/` resta invariato"], ()),
    # una deroga si applica solo al motivo che copre, non agli altri
    ("run_con_bug", 1, ["PUBBLICAZIONE BLOCCATA"], ("--allow-not-auditable", "--allow-deduced")),
]


def check_guard_blocks_publication():
    """Un run bloccato non deve scrivere nulla nella directory di destinazione."""
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "latest"
        code, _ = run("run_con_bug", GUARD, ("--publish-to", str(target)))
        if code != 1:
            return f"guard --publish-to su run invalido: exit {code}, atteso 1"
        if target.exists() and any(target.iterdir()):
            return "guard --publish-to ha scritto file per un run bloccato"
    with tempfile.TemporaryDirectory() as tmp:
        target = Path(tmp) / "latest"
        code, _ = run("run_conforme", GUARD, ("--publish-to", str(target)))
        if code != 0:
            return f"guard --publish-to su run valido: exit {code}, atteso 0"
        names = sorted(p.name for p in target.iterdir()) if target.exists() else []
        expected = ["excluded_latest.json", "run_metadata_latest.json",
                    "scanner_v3_latest.json"]
        if names != expected:
            return f"guard ha pubblicato {names}, atteso {expected}"
    return None


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

    for fixture, expected_code, fragments, extra in GUARD_CASES:
        code, out = run(fixture, GUARD, extra)
        label = f"guard {fixture}" + (f" {' '.join(extra)}" if extra else "")
        ok = code == expected_code and all(f in out for f in fragments)
        if code != expected_code:
            print(f"FAIL {label}: exit {code}, atteso {expected_code}")
            failures += 1
        for fragment in fragments:
            if fragment not in out:
                print(f"FAIL {label}: manca dall'output {fragment!r}")
                failures += 1
        if ok:
            print(f"ok   {label} (exit {code})")

    problem = check_guard_blocks_publication()
    if problem:
        print(f"FAIL {problem}")
        failures += 1
    else:
        print("ok   guard scrive solo quando la pubblicazione e' consentita")

    # Il run reale pubblicato non deve mai risultare valido per sbaglio:
    # oggi e' INVALID, e in ogni caso non e' completamente auditabile.
    proc = subprocess.run([sys.executable, str(VALIDATOR), str(ROOT / "latest")],
                          capture_output=True, text=True)
    if proc.returncode not in (EXIT_INVALID, EXIT_NOT_AUDITABLE):
        print(f"FAIL latest/: exit {proc.returncode}, atteso INVALID o NON AUDITABILE")
        failures += 1
    else:
        print(f"ok   latest/ (exit {proc.returncode})")

    proc = subprocess.run([sys.executable, str(GUARD), str(ROOT / "latest")],
                          capture_output=True, text=True)
    if proc.returncode != 1:
        print(f"FAIL guard latest/: exit {proc.returncode}, atteso 1 (bloccato)")
        failures += 1
    else:
        print("ok   guard latest/ (bloccato)")

    print("\n" + ("TUTTI I TEST OK" if not failures else f"{failures} TEST FALLITI"))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
