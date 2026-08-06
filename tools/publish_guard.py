#!/usr/bin/env python3
"""Cancello di pubblicazione: `latest/` si aggiorna solo se il run e' certificato.

Un run che non supera la validazione puo' restare in locale per debug, ma non
deve diventare la fonte del report del mattino. Questo strumento decide, e in
opzione esegue la pubblicazione.

    scanner -> publish_guard.py -> consentito? -> aggiorna latest/
                                -> bloccato?   -> latest/ resta com'e'

Blocca per default se:

  - il verdetto non e' RUN VALID (quindi anche RUN NON AUDITABILE);
  - il validatore ha dovuto dedurre una o piu' soglie;
  - un titolo promosso ha `audit_status` diverso da PASS, dichiarato o
    ricalcolato.

Uso:
    python3 tools/publish_guard.py <run_dir>
    python3 tools/publish_guard.py <run_dir> --publish-to latest/
    python3 tools/publish_guard.py <run_dir> --json

Deroghe, entrambe da usare consapevolmente e sempre riportate nell'output:
    --allow-not-auditable   accetta RUN NON AUDITABILE (strumentazione parziale)
    --allow-deduced         accetta soglie non dichiarate dal motore

Exit code: 0 pubblicazione consentita, 1 bloccata, 64 errore d'uso.
"""

import argparse
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import validate_run as V  # noqa: E402

EXIT_ALLOW, EXIT_BLOCK, EXIT_USAGE = 0, 1, 64


def assess(run_dir, allow_not_auditable=False, allow_deduced=False):
    """Valuta un run e restituisce (decisione, motivi, risultato validazione)."""
    meta_path = next(iter(sorted(run_dir.glob("run_metadata_*.json"))), None)
    excl_path = next(iter(sorted(run_dir.glob("excluded_*.json"))), None)
    pass_path = next(iter(sorted(run_dir.glob("scanner_v3_*.json"))), None)
    if not (meta_path and excl_path and pass_path):
        raise FileNotFoundError(
            f"{run_dir}: attesi run_metadata_*, excluded_* e scanner_v3_*.json")

    meta = V.load(meta_path)
    thresholds, provenance = V.resolve_thresholds(meta)
    rep = V.Report()
    error_tickers = {e.get("ticker") for e in meta.get("errors", []) if e.get("ticker")}
    promoted = V.load(pass_path).get("titoli", [])
    excluded = V.load(excl_path).get("titoli", [])
    for record in promoted:
        V.validate_record(rep, record, thresholds, True, error_tickers)
    for record in excluded:
        V.validate_record(rep, record, thresholds, False, error_tickers)
    result, _ = V.build_result(run_dir, meta, promoted, excluded, rep, provenance)

    blockers = []
    verdict = result["verdict"]
    if verdict == "RUN INVALID":
        counts = result["divergence_counts"]
        blockers.append(
            "verdetto RUN INVALID: {} divergenze (fail-open {}, esclusioni "
            "ingiustificate {}, etichettatura {})".format(
                len(result["divergences"]), counts["fail_open"],
                counts["false_exclusion"], counts["labeling"]))
    elif verdict == "RUN NON AUDITABILE":
        detail = "verdetto RUN NON AUDITABILE: {} gate non ricalcolabili".format(
            len(result["not_auditable_gates"]))
        if allow_not_auditable:
            result.setdefault("waivers", []).append(detail)
        else:
            blockers.append(detail)

    if result["deduced_thresholds"]:
        detail = "soglie non dichiarate dal motore: " + ", ".join(result["deduced_thresholds"])
        if allow_deduced:
            result.setdefault("waivers", []).append(detail)
        else:
            blockers.append(detail)

    if result["promoted_with_non_pass_gate"]:
        blockers.append("promossi con gate ricalcolato non-PASS: "
                        + ", ".join(result["promoted_with_non_pass_gate"]))
    if result["promoted_with_declared_audit_status_not_pass"]:
        blockers.append("promossi con audit_status dichiarato non-PASS: " + ", ".join(
            f"{e['ticker']} ({e['audit_status']})"
            for e in result["promoted_with_declared_audit_status_not_pass"]))

    return (not blockers), blockers, result


def publish(run_dir, target):
    """Copia i JSON e i CSV del run in `target`, rinominandoli in *_latest.*."""
    target.mkdir(parents=True, exist_ok=True)
    published = []
    for path in sorted(run_dir.iterdir()):
        if path.suffix not in (".json", ".csv"):
            continue
        stem = path.stem
        # scanner_v3_2026-08-05 -> scanner_v3_latest
        prefix = stem.rsplit("_", 1)[0] if "_" in stem else stem
        destination = target / f"{prefix}_latest{path.suffix}"
        shutil.copy2(path, destination)
        published.append(destination.name)
    return published


def main(argv=None):
    parser = argparse.ArgumentParser(add_help=True, description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("run_dir", type=Path)
    parser.add_argument("--publish-to", type=Path, default=None,
                        help="directory da aggiornare se la pubblicazione e' consentita")
    parser.add_argument("--allow-not-auditable", action="store_true")
    parser.add_argument("--allow-deduced", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        allowed, blockers, result = assess(
            args.run_dir, args.allow_not_auditable, args.allow_deduced)
    except FileNotFoundError as exc:
        print(f"[errore] {exc}")
        return EXIT_USAGE

    published = []
    if allowed and args.publish_to is not None:
        published = publish(args.run_dir, args.publish_to)

    quality = result["data_quality"]["run_score"]
    if args.json:
        print(json.dumps({
            "run": str(args.run_dir),
            "decision": "ALLOW" if allowed else "BLOCK",
            "verdict": result["verdict"],
            "data_quality_score": quality,
            "blockers": blockers,
            "waivers": result.get("waivers", []),
            "published": published,
        }, indent=2, ensure_ascii=False))
    else:
        print(f"run:      {args.run_dir}")
        print(f"verdetto: {result['verdict']}   qualita': {quality}/100")
        for waiver in result.get("waivers", []):
            print(f"  deroga accettata: {waiver}")
        if allowed:
            print("\nPUBBLICAZIONE CONSENTITA")
            if published:
                print("  aggiornati: " + ", ".join(published))
            elif args.publish_to is not None:
                print("  nessun file da pubblicare")
        else:
            print(f"\nPUBBLICAZIONE BLOCCATA — {len(blockers)} motivi")
            for blocker in blockers:
                print(f"  - {blocker}")
            print("\n`latest/` resta invariato. Il run puo' essere conservato per debug.")

    return EXIT_ALLOW if allowed else EXIT_BLOCK


if __name__ == "__main__":
    sys.exit(main())
