#!/usr/bin/env python3
"""Validatore degli output dello Scanner (schemi 3.0, 3.1 e 4.0).

Ricalcola ogni gate a partire dai valori numerici pubblicati nel JSON e lo
confronta con lo stato dichiarato dal motore. Lo scanner non deve chiedere
fiducia: se un gate non e' ricalcolabile dai dati esportati, il run non e'
certificabile.

Ogni gate riceve uno di quattro stati:

    PASS        valori presenti, condizione soddisfatta
    FAIL        valori presenti, condizione non soddisfatta
    UNVERIFIED  un valore necessario e' null o assente dalla sorgente
    ERROR       il gate non e' stato valutato per un errore di pipeline

Solo PASS promuove. UNVERIFIED ed ERROR non sono un pass: sono l'assenza di
un verdetto.

Verdetto del run:

    RUN VALID           ogni gate coerente col dichiarato, ogni omissione dichiarata
    RUN INVALID         almeno un gate dichiarato diverge dal ricalcolo
    RUN NON AUDITABILE  omissione silenziosa: gate assente o operandi non esportati

Un gate dichiarato UNVERIFIED o ERROR con operandi nulli e motivo esplicito e'
verificabile e non impedisce la certificazione di un titolo escluso. Un titolo
promosso deve invece avere ogni gate PASS e ogni operando esportato.

Riporta inoltre il `data_quality_score` (100 meno 3 per ogni campo atteso non
utilizzabile, 10 se la causa e' un guasto di pipeline) e segnala quali soglie
il motore non dichiara, costringendo il validatore a dedurle.

Uso:
    python3 tools/validate_run.py latest/
    python3 tools/validate_run.py latest/ --json

Exit code: 0 RUN VALID, 1 RUN INVALID, 2 RUN NON AUDITABILE, 64 errore d'uso.
"""

import json
import sys
from pathlib import Path

PASS = "PASS"
FAIL = "FAIL"
UNVERIFIED = "UNVERIFIED"
ERROR = "ERROR"
NOT_AUDITABLE = "NON_AUDITABILE"

# Precedenza per il rollup di record e run: uno stato peggiore assorbe i migliori.
PRECEDENCE = [ERROR, FAIL, UNVERIFIED, PASS]

EXIT_VALID, EXIT_INVALID, EXIT_NOT_AUDITABLE, EXIT_USAGE = 0, 1, 2, 64


def rollup(statuses):
    for level in PRECEDENCE:
        if level in statuses:
            return level
    return PASS


# --- Definizione dei gate -------------------------------------------------
#
# Ogni gate dichiara i valori che gli servono e la condizione da ricalcolare.
# `inputs` mancanti dal record -> il gate non e' auditabile (buco di
# strumentazione, distinto da UNVERIFIED che e' un dato assente alla fonte).


def gate(name, inputs, predicate, evaluator=None):
    """Un gate del registro.

    `inputs` sono i valori che servono sempre; `predicate` la condizione.
    `evaluator` sostituisce il flusso standard quando il gate ha input
    condizionali (vedi `eps_growth`, che consulta il fatturato solo se il ramo
    principale non basta).
    """
    return {"name": name, "inputs": inputs, "predicate": predicate, "evaluator": evaluator}


def _between(value, low, high):
    return low <= value <= high


def _eps_growth(values, thresholds):
    """Crescita EPS con ramo alternativo, a input condizionali.

    Passa se `eps_growth_yoy >= eps_growth_min`, oppure se la crescita e'
    almeno `eps_growth_alt_min` accompagnata da un fatturato in crescita di
    almeno `eps_growth_alt_revenue_min`. Il fatturato viene consultato solo se
    il ramo principale non basta: un titolo con EPS sopra la soglia piena non
    diventa UNVERIFIED perche' manca il fatturato.

    Se il ramo alternativo non e' dichiarato nei metadati vale la sola soglia
    principale.
    """
    eps = values["eps_growth_yoy"]
    if eps >= thresholds["eps_growth_min"]:
        return PASS, f"eps_growth_yoy={eps!r} >= {thresholds['eps_growth_min']}"
    alt_min = thresholds.get("eps_growth_alt_min")
    alt_revenue_min = thresholds.get("eps_growth_alt_revenue_min")
    if alt_min is None or alt_revenue_min is None:
        return FAIL, f"eps_growth_yoy={eps!r} < {thresholds['eps_growth_min']}"
    if eps < alt_min:
        return FAIL, f"eps_growth_yoy={eps!r} sotto entrambe le soglie"
    if "revenue_growth_yoy" not in values:
        return NOT_AUDITABLE, "valori non esportati: revenue_growth_yoy (ramo alternativo)"
    revenue = values["revenue_growth_yoy"]
    if revenue is None:
        return UNVERIFIED, "valori null: revenue_growth_yoy (serve al ramo alternativo)"
    ok = revenue >= alt_revenue_min
    detail = f"eps_growth_yoy={eps!r} con revenue_growth_yoy={revenue!r} (ramo alternativo)"
    return (PASS if ok else FAIL), detail


def _earnings_window(values, thresholds):
    """Blackout earnings. La regola deve essere dichiarata nei metadati:
    senza, il gate non e' ricalcolabile e resta non auditabile."""
    rule = thresholds["earnings_window_rule"]
    if rule != "no_earnings_within_blackout":
        raise KeyError(f"earnings_window_rule non riconosciuta: {rule}")
    days = values["days_to_earnings"]
    return not (0 <= days <= thresholds["earnings_blackout_days"])


GATES = [
    # Hard filter d'universo
    gate("price_min", ["price"], lambda v, t: v["price"] >= t["price_min"]),
    gate("market_cap_min", ["market_cap"], lambda v, t: v["market_cap"] >= t["market_cap_min"]),
    gate("avg_volume_min", ["avg_volume_20d"], lambda v, t: v["avg_volume_20d"] >= t["avg_volume_min"]),
    # Struttura di trend: catena price > SMA50 > SMA150 > SMA200
    gate("price_above_sma50", ["price", "sma50"], lambda v, t: v["price"] > v["sma50"]),
    gate("sma50_above_sma150", ["sma50", "sma150"], lambda v, t: v["sma50"] > v["sma150"]),
    gate("sma150_above_sma200", ["sma150", "sma200"], lambda v, t: v["sma150"] > v["sma200"]),
    gate("ema21_above_ema50", ["ema21", "ema50"], lambda v, t: v["ema21"] > v["ema50"]),
    # Momentum e volatilita'
    gate("rsi14", ["rsi14"], lambda v, t: _between(v["rsi14"], t["rsi_min"], t["rsi_max"])),
    gate("atr_pct", ["atr_pct"], lambda v, t: v["atr_pct"] >= t["atr_pct_min"]),
    gate("rvol20", ["rvol20"], lambda v, t: v["rvol20"] >= t["rvol20_min"]),
    gate("performance_21d", ["performance_21d_pct"],
         lambda v, t: _between(v["performance_21d_pct"],
                               t["performance_21d_min"], t["performance_21d_max"])),
    gate("no_extended_move_10d", ["move_10d_pct"], lambda v, t: v["move_10d_pct"] <= t["move_10d_max"]),
    # Posizione nel range
    gate("within_25pct_52w_high", ["distance_52w_high_pct"],
         lambda v, t: v["distance_52w_high_pct"] <= t["within_52w_high_max_pct"]),
    gate("distance_resistance", ["distance_resistance_pct"],
         lambda v, t: v["distance_resistance_pct"] >= t["distance_resistance_min"]),
    # Fondamentali
    gate("revenue_growth", ["revenue_growth_yoy"],
         lambda v, t: v["revenue_growth_yoy"] >= t["revenue_growth_min"]),
    gate("eps_growth", ["eps_growth_yoy"], None, evaluator=lambda v, t: _eps_growth(v, t)),
    gate("eps_next_year", ["eps_next_year"], lambda v, t: v["eps_next_year"] > t["eps_next_year_min"]),
    gate("operating_margin", ["operating_margin"],
         lambda v, t: v["operating_margin"] >= t["operating_margin_min"]),
    # Esclusioni categoriali
    gate("adr", ["is_adr"], lambda v, t: not v["is_adr"]),
    gate("biotech_pre_revenue", ["industry", "revenue_ttm"],
         lambda v, t: not (v["industry"] == "Biotechnology" and (v["revenue_ttm"] or 0) <= 0)),
    gate("earnings_window", ["days_to_earnings"], _earnings_window),
]

# Soglie che il motore non dichiara ancora in run_metadata.thresholds, dedotte
# dalla separazione osservata nel run 2026-08-05. Vanno rimosse da qui appena
# compaiono nei metadati: sono un ripiego, non una fonte di verita'.
DEDUCED_THRESHOLDS = {
    "revenue_growth_min": 20.0,
    "eps_growth_min": 30.0,
    "eps_next_year_min": 15.0,  # confronto stretto: 15.0 esatto risulta bocciato
    "operating_margin_min": 8.0,
    "within_52w_high_max_pct": 25.0,
    # Ramo alternativo di eps_growth. Coerente con il run 2026-08-05 (nessuna
    # contraddizione), ma mai decisivo: nessun titolo ha eps in [20, 30) con
    # fatturato >= 40, quindi la regola non e' falsificabile su questi dati.
    "eps_growth_alt_min": 20.0,
    "eps_growth_alt_revenue_min": 40.0,
}

# Soglie a intervallo nella forma legacy (lista [min, max]) e loro nomi piatti.
# Lo schema 4.0 pubblica direttamente i nomi piatti.
LEGACY_RANGES = {
    "rsi": ("rsi_min", "rsi_max"),
    "performance_21d": ("performance_21d_min", "performance_21d_max"),
    "pead_window": ("pead_window_min", "pead_window_max"),
}

# Penalita' del data_quality_score, per campo atteso e non utilizzabile.
QUALITY_PENALTIES = {
    "pipeline_error": 10,      # guasto del run, dichiarato in run_metadata.errors
    "source_no_data": 3,       # il provider non espone il dato
    "stage_not_executed": 3,   # stadio non eseguito per questo titolo
    "not_exported": 3,         # campo assente dal record: stessa cecita', ma silenziosa
}


def penalty_for(reason):
    """Penalita' di un motivo, tollerante ai motivi qualificati.

    Lo schema 4.0 ammette motivi descrittivi come
    `stage_not_executed_after_fundamental_fail`: contano come la famiglia a cui
    appartengono. Un motivo non riconoscibile vale come dato assente alla fonte.
    """
    if reason in QUALITY_PENALTIES:
        return QUALITY_PENALTIES[reason], reason
    for family, penalty in QUALITY_PENALTIES.items():
        if reason.startswith(family):
            return penalty, family
    return QUALITY_PENALTIES["source_no_data"], "source_no_data"

TREND_CHAIN = ["price_above_sma50", "sma50_above_sma150", "sma150_above_sma200"]
TREND_INPUTS = ["price", "sma50", "sma150", "sma200"]


def evaluate(gate_def, values, thresholds, reasons=None, pipeline_error=False):
    """Ricalcola un gate. Ritorna (stato, dettaglio).

    Un valore nullo vale ERROR se `missing_details` lo attribuisce a un guasto
    di pipeline (o se il titolo compare in run_metadata.errors), UNVERIFIED se
    il dato non esiste alla fonte o lo stadio non e' stato eseguito. In nessun
    caso e' un pass.
    """
    reasons = reasons or {}
    name, inputs = gate_def["name"], gate_def["inputs"]
    missing = [k for k in inputs if k not in values]
    if missing:
        return NOT_AUDITABLE, f"valori non esportati: {', '.join(missing)}"
    null = [k for k in inputs if values[k] is None]
    if null:
        errored = any(reasons.get(k) == "pipeline_error" for k in null) or (
            pipeline_error and not any(k in reasons for k in null))
        status = ERROR if errored else UNVERIFIED
        return status, f"valori null: {', '.join(null)}"
    try:
        if gate_def["evaluator"] is not None:
            return gate_def["evaluator"](values, thresholds)
        ok = gate_def["predicate"](values, thresholds)
    except KeyError as exc:
        return NOT_AUDITABLE, f"soglia non dichiarata: {exc.args[0]}"
    detail = ", ".join(f"{k}={values[k]!r}" for k in inputs)
    return (PASS if ok else FAIL), detail


def gate_block(record, gate_name):
    """Il blocco `gates[nome]` dello schema 4.0, se il record lo usa."""
    gates = record.get("gates")
    if isinstance(gates, dict):
        block = gates.get(gate_name)
        if isinstance(block, dict):
            return block
    return None


def uses_gate_blocks(record):
    return isinstance(record.get("gates"), dict)


def declared_status(record, gate_name):
    """Stato dichiarato dal motore per un gate.

    Schema 4.0: `gates[nome].status`.
    Schema 3.1: liste failed_gates / unverified_gates / error_gates.
    Schema 3.0: solo failed_gates, tutto il resto e' implicitamente un pass.
    """
    block = gate_block(record, gate_name)
    if block is not None and block.get("status") in (PASS, FAIL, UNVERIFIED, ERROR):
        return block["status"]
    if gate_name in record.get("error_gates", []):
        return ERROR
    if gate_name in record.get("failed_gates", []):
        return FAIL
    if gate_name in record.get("unverified_gates", []):
        return UNVERIFIED
    return PASS


def gate_operands(record, gate_def):
    """Valori visibili a un gate.

    Nello schema 4.0 gli operandi stanno in `gates[nome].operands`; `values`
    resta come vista di ripiego per gli schemi precedenti e per gli operandi
    che un gate consulta solo in via condizionale (il fatturato per il ramo
    alternativo di `eps_growth`).
    """
    merged = dict(record.get("values") or {})
    block = gate_block(record, gate_def["name"])
    if block is not None:
        merged.update(block.get("operands") or {})
    return merged


def merged_values(record):
    """Tutti gli operandi del record in un'unica vista.

    Nello schema 4.0 lo stesso operando puo' comparire in piu' gate (`price` in
    `price_min` e in `price_above_sma50`): la vista unita serve al calcolo
    della qualita' e al flag di trend.
    """
    merged = dict(record.get("values") or {})
    gates = record.get("gates")
    if isinstance(gates, dict):
        for block in gates.values():
            if isinstance(block, dict):
                merged.update(block.get("operands") or {})
    return merged


def operand_conflicts(record):
    """Lo stesso operando con valori diversi in gate diversi.

    Nello schema annidato gli operandi sono duplicati: se due gate riportano
    `price` diverso, uno dei due ha valutato su un numero che non e' quello
    pubblicato altrove, e il ricalcolo non significa piu' nulla.
    """
    gates = record.get("gates")
    if not isinstance(gates, dict):
        return []
    seen, conflicts = {}, []
    for gate_name, block in gates.items():
        if not isinstance(block, dict):
            continue
        for field, value in (block.get("operands") or {}).items():
            # Un operando nullo e' la dichiarazione di un gate non eseguito,
            # non un valore in disaccordo: si confrontano solo i non nulli.
            if value is None:
                continue
            if field in seen and seen[field][1] != value:
                conflicts.append((field, seen[field][0], seen[field][1], gate_name, value))
            else:
                seen.setdefault(field, (gate_name, value))
    return conflicts


def declared_omission(record, gate_def):
    """Il gate dichiara di non essere stato valutato, e lo fa correttamente?

    Un'omissione dichiarata e' verificabile: il gate c'e', lo stato non e'
    PASS, gli operandi sono presenti e nulli, il motivo e' esplicito. Non e'
    un buco di strumentazione — e' un dato. Ritorna (True, motivo) oppure
    (False, None).
    """
    block = gate_block(record, gate_def["name"])
    if block is None:
        return False, None
    status = block.get("status")
    if status not in (UNVERIFIED, ERROR):
        return False, None
    operands = block.get("operands") or {}
    if any(k not in operands or operands[k] is not None for k in gate_def["inputs"]):
        return False, None
    reason = block.get("reason") or ""
    return bool(reason), reason


def severity(declared, computed):
    """Classifica una divergenza.

    fail_open        il motore dichiara PASS dove il ricalcolo nega il pass:
                     un titolo puo' essere promosso senza titolo per esserlo
    false_exclusion  il motore esclude un titolo che il ricalcolo promuove
    labeling         entrambi non-PASS, etichette diverse (es. FAIL vs
                     UNVERIFIED): l'esito operativo e' lo stesso, ma lo stato
                     dichiarato non e' leggibile senza interpretazione
    """
    if declared == PASS:
        return "fail_open"
    if computed == PASS:
        return "false_exclusion"
    return "labeling"


class Report:
    def __init__(self):
        self.divergences = []
        self.not_auditable = {}
        self.not_auditable_promoted = 0
        self.omissions = {}
        self.operand_conflicts = []
        self.gate_statuses = {}
        self.records = 0
        self.promoted_not_pass = []
        self.promoted_declared_not_pass = []
        self.rollup_errors = []
        self.scores = []
        self.score_errors = []
        self.quality_breakdown = {}

    def diverge(self, ticker, gate_name, declared, computed, detail):
        self.divergences.append({
            "ticker": ticker, "gate": gate_name,
            "declared": declared, "computed": computed, "detail": detail,
            "severity": severity(declared, computed),
        })

    def blind(self, gate_name, reason, promoted=False):
        entry = self.not_auditable.setdefault(gate_name, {"count": 0, "reason": reason})
        entry["count"] += 1
        if promoted:
            entry["promoted"] = entry.get("promoted", 0) + 1
            self.not_auditable_promoted += 1

    def declared_omission(self, gate_name, reason):
        key = f"{gate_name} ({reason})"
        self.omissions[key] = self.omissions.get(key, 0) + 1

    def count(self, status):
        self.gate_statuses[status] = self.gate_statuses.get(status, 0) + 1


def check_trend_flag(rep, ticker, values, computed_chain):
    """`trend_structural_pass` deve coincidere con l'AND della sola catena SMA.

    Il flag e' trattato come un gate: dichiararlo true dove il ricalcolo lo
    nega e' un fail-open, non un problema di etichetta.
    """
    if "trend_structural_pass" not in values:
        rep.blind("trend_structural_pass", "campo non esportato")
        return
    declared = PASS if values["trend_structural_pass"] else FAIL
    if any(k not in values or values[k] is None for k in TREND_INPUTS):
        if declared == PASS:
            rep.diverge(ticker, "trend_structural_pass", declared, UNVERIFIED,
                        "dichiarato true con almeno un valore della catena mancante")
        return
    expected = PASS if values["price"] > values["sma50"] > values["sma150"] > values["sma200"] else FAIL
    if declared != expected:
        rep.diverge(ticker, "trend_structural_pass", declared, expected,
                    "price={price} sma50={sma50} sma150={sma150} sma200={sma200}".format(**values))
        return
    # Coerente con i propri operandi: resta da verificare che concordi con lo
    # stato ricalcolato dei tre gate della catena.
    chain = [computed_chain[g] for g in TREND_CHAIN if g in computed_chain]
    if declared == PASS and any(s != PASS for s in chain):
        rep.diverge(ticker, "trend_structural_pass", declared, rollup(chain),
                    "catena ricalcolata: " + "/".join(chain))


def validate_record(rep, record, thresholds, promoted, error_tickers=frozenset()):
    ticker = record.get("ticker", "?")
    values = record.get("values", {})
    rep.records += 1

    reasons = missing_reasons(record)
    pipeline_error = ticker in error_tickers
    nested = uses_gate_blocks(record)
    computed_statuses = []
    already_reported = set()
    chain = {}
    for gate_def in GATES:
        name = gate_def["name"]
        operands = gate_operands(record, gate_def)

        # Schema 4.0: un gate assente dal blocco `gates` e' un'omissione
        # silenziosa, anche se gli operandi comparissero altrove nel record.
        if nested and gate_block(record, name) is None:
            rep.blind(name, "gate assente dal blocco `gates`", promoted)
            continue

        omitted, omission_reason = declared_omission(record, gate_def)
        if omitted:
            rep.declared_omission(name, omission_reason)
            declared = declared_status(record, name)
            rep.count(declared)
            computed_statuses.append(declared)
            if name in TREND_CHAIN:
                chain[name] = declared
            continue

        status, detail = evaluate(gate_def, operands, thresholds, reasons, pipeline_error)
        if name in TREND_CHAIN:
            chain[name] = status
        if status == NOT_AUDITABLE:
            rep.blind(name, detail, promoted)
            continue
        rep.count(status)
        computed_statuses.append(status)
        declared = declared_status(record, name)
        if declared != status:
            rep.diverge(ticker, name, declared, status, detail)
            already_reported.add(name)

    check_trend_flag(rep, ticker, merged_values(record), chain)

    for field, gate_a, value_a, gate_b, value_b in operand_conflicts(record):
        rep.operand_conflicts.append(
            {"ticker": ticker, "field": field,
             "detail": f"{gate_a}={value_a!r} ma {gate_b}={value_b!r}"})

    # missing_fields deve implicare uno stato non-PASS sui gate che lo usano.
    for field in record.get("missing_fields", []):
        for gate_def in GATES:
            name = gate_def["name"]
            if name in already_reported:
                continue  # gia' segnalato dal ricalcolo del gate
            if field in gate_def["inputs"] and declared_status(record, name) == PASS:
                rep.diverge(ticker, name, PASS, UNVERIFIED,
                            f"{field} elencato in missing_fields")
                already_reported.add(name)

    # audit_status di record: rollup degli stati ricalcolati.
    if "audit_status" in record and computed_statuses:
        expected = rollup(computed_statuses)
        if record["audit_status"] != expected:
            rep.rollup_errors.append((ticker, record["audit_status"], expected))

    # data_quality_score: ricalcolato, e confrontato con quello dichiarato.
    score, breakdown = quality_score(record, pipeline_error)
    rep.scores.append(score)
    for reason, count in breakdown.items():
        rep.quality_breakdown[reason] = rep.quality_breakdown.get(reason, 0) + count
    if "data_quality_score" in record and record["data_quality_score"] != score:
        rep.score_errors.append((ticker, record["data_quality_score"], score))

    # Un titolo promosso deve avere ogni gate ricalcolato su PASS, e deve
    # dichiararlo: audit_status diverso da PASS in scanner_v3 e' una promozione
    # che il motore stesso non sostiene.
    if promoted:
        if any(s != PASS for s in computed_statuses):
            rep.promoted_not_pass.append(ticker)
        declared = record.get("audit_status")
        if declared is not None and declared != PASS:
            rep.promoted_declared_not_pass.append((ticker, declared))


def load(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def resolve_thresholds(meta):
    """Normalizza le soglie e traccia da dove viene ciascuna.

    Accetta sia i nomi piatti dello schema 4.0 (`rsi_min`, `rsi_max`) sia la
    forma a intervallo attuale (`rsi: [55, 72]`). Cio' che il motore non
    dichiara viene dedotto, e il validatore lo segnala: una soglia dedotta e'
    un'inferenza sul comportamento osservato, non un contratto.
    """
    thresholds, provenance = {}, {}
    for key, value in meta.get("thresholds", {}).items():
        if key in LEGACY_RANGES and isinstance(value, (list, tuple)) and len(value) == 2:
            low_key, high_key = LEGACY_RANGES[key]
            thresholds[low_key], thresholds[high_key] = value
            provenance[low_key] = provenance[high_key] = "metadati (forma a intervallo)"
        else:
            thresholds[key] = value
            provenance[key] = "metadati"
    for key, value in DEDUCED_THRESHOLDS.items():
        if key not in thresholds:
            thresholds[key] = value
            provenance[key] = "DEDOTTA dai dati"
    return thresholds, provenance


EXPECTED_FIELDS = sorted({k for g in GATES for k in g["inputs"]} | {"trend_structural_pass"})


def missing_reasons(record):
    """Mappa campo -> motivo.

    Nello schema 4.0 il motivo sta accanto al gate (`gates[nome].reason`) e
    vale per i suoi operandi; `missing_details` resta la forma degli schemi
    precedenti e accetta sia {campo: {reason, source}} sia
    [{field, reason, source}].
    """
    from_gates = {}
    gates = record.get("gates")
    if isinstance(gates, dict):
        for block in gates.values():
            if not isinstance(block, dict) or not block.get("reason"):
                continue
            for field, value in (block.get("operands") or {}).items():
                if value is None:
                    from_gates[field] = block["reason"]

    details = record.get("missing_details") or {}
    if isinstance(details, list):
        from_gates.update({d.get("field"): d.get("reason")
                           for d in details if isinstance(d, dict)})
    elif isinstance(details, dict):
        for field, info in details.items():
            from_gates[field] = info.get("reason") if isinstance(info, dict) else info
    return from_gates


def quality_score(record, pipeline_error):
    """100 meno una penalita' per ogni campo atteso non utilizzabile.

    Il conteggio parte dai campi *attesi* dal registro dei gate, non da quelli
    presenti: altrimenti omettere un campo darebbe un punteggio migliore che
    dichiararlo `null`, e la metrica premierebbe la reticenza.
    """
    values = merged_values(record)
    reasons = missing_reasons(record)
    breakdown, penalty = {}, 0
    for field in EXPECTED_FIELDS:
        if field not in values:
            reason = "not_exported"
        elif values[field] is None:
            reason = reasons.get(field) or ("pipeline_error" if pipeline_error else "source_no_data")
        else:
            continue
        cost, family = penalty_for(reason)
        penalty += cost
        breakdown[family] = breakdown.get(family, 0) + 1
    return max(0, 100 - penalty), breakdown


def build_result(run_dir, meta, promoted, excluded, rep, provenance):
    """Verdetto del run.

    Un'omissione *dichiarata* — gate presente, stato non-PASS, operandi nulli,
    motivo esplicito — non impedisce la certificazione su un titolo escluso:
    e' verificabile, ed e' la forma prevista per gli stadi non eseguiti. Cio'
    che blocca e' l'omissione silenziosa (gate assente, o operandi mancanti a
    fronte di uno stato definito), ovunque si trovi, e qualunque gate non
    ricalcolabile su un titolo *promosso*: un promosso deve avere ogni hard
    gate PASS e ogni operando che lo giustifica esportato.
    """
    if (rep.divergences or rep.rollup_errors or rep.promoted_not_pass
            or rep.score_errors or rep.promoted_declared_not_pass
            or rep.operand_conflicts):
        verdict, code = "RUN INVALID", EXIT_INVALID
    elif rep.not_auditable:
        verdict, code = "RUN NON AUDITABILE", EXIT_NOT_AUDITABLE
    else:
        verdict, code = "RUN VALID", EXIT_VALID
    return {
        "run": str(run_dir),
        "market_session_date": meta.get("market_session_date"),
        "software_version": meta.get("software_version"),
        "verdict": verdict,
        "records": rep.records,
        "promoted": len(promoted),
        "excluded": len(excluded),
        "gate_status_counts": rep.gate_statuses,
        "divergence_counts": {
            key: sum(1 for d in rep.divergences if d["severity"] == key)
            for key in ("fail_open", "false_exclusion", "labeling")
        },
        "divergences": rep.divergences,
        "audit_status_rollup_errors": [
            {"ticker": t, "declared": d, "expected": e} for t, d, e in rep.rollup_errors
        ],
        "promoted_with_non_pass_gate": rep.promoted_not_pass,
        "promoted_with_declared_audit_status_not_pass": [
            {"ticker": t, "audit_status": a} for t, a in rep.promoted_declared_not_pass
        ],
        "not_auditable_gates": rep.not_auditable,
        "not_auditable_on_promoted": rep.not_auditable_promoted,
        "declared_omissions": rep.omissions,
        "operand_conflicts": rep.operand_conflicts,
        "data_quality": {
            "run_score": round(sum(rep.scores) / len(rep.scores)) if rep.scores else None,
            "min_record_score": min(rep.scores) if rep.scores else None,
            "records_below_100": sum(1 for s in rep.scores if s < 100),
            "penalties_by_reason": rep.quality_breakdown,
            "declared_mismatches": [
                {"ticker": t, "declared": d, "expected": e} for t, d, e in rep.score_errors
            ],
        },
        "deduced_thresholds": sorted(k for k, v in provenance.items() if v.startswith("DEDOTTA")),
    }, code


def render(result):
    out = []
    out.append(f"run: {result['run']}  sessione {result['market_session_date']}"
               f"  motore {result['software_version']}")
    out.append(f"record: {result['records']} "
               f"({result['promoted']} promossi, {result['excluded']} esclusi)")
    counts = result["gate_status_counts"]
    if counts:
        out.append("gate ricalcolati: " + "  ".join(f"{k}={v}" for k, v in sorted(counts.items())))

    div = result["divergences"]
    if div:
        titles = {
            "fail_open": "FAIL-OPEN — dichiarato PASS, il ricalcolo nega il pass",
            "false_exclusion": "ESCLUSIONI INGIUSTIFICATE — il ricalcolo dice PASS",
            "labeling": "ETICHETTATURA — esito operativo corretto, stato dichiarato ambiguo",
        }
        for key, title in titles.items():
            group = [d for d in div if d["severity"] == key]
            if not group:
                continue
            out.append(f"\n{title}: {len(group)}")
            for d in group:
                out.append(f"  {d['ticker']:8} {d['gate']:24} dichiarato={d['declared']:<10}"
                           f" ricalcolato={d['computed']:<10} {d['detail']}")
    else:
        out.append("\nDivergenze dichiarato/ricalcolato: nessuna.")

    if result["audit_status_rollup_errors"]:
        out.append(f"\nAUDIT_STATUS di record incoerenti: {len(result['audit_status_rollup_errors'])}")
        for e in result["audit_status_rollup_errors"]:
            out.append(f"  {e['ticker']:8} dichiarato={e['declared']} atteso={e['expected']}")

    if result["promoted_with_non_pass_gate"]:
        out.append("\nPROMOSSI CON GATE NON-PASS: "
                   + ", ".join(result["promoted_with_non_pass_gate"]))

    if result["promoted_with_declared_audit_status_not_pass"]:
        out.append("\nPROMOSSI CON audit_status DICHIARATO NON-PASS: " + ", ".join(
            f"{e['ticker']} ({e['audit_status']})"
            for e in result["promoted_with_declared_audit_status_not_pass"]))

    if result["operand_conflicts"]:
        out.append(f"\nOPERANDI IN CONFLITTO fra gate: {len(result['operand_conflicts'])}")
        for c in result["operand_conflicts"]:
            out.append(f"  {c['ticker']:8} {c['field']:24} {c['detail']}")

    if result["declared_omissions"]:
        total = sum(result["declared_omissions"].values())
        out.append(f"\nOMISSIONI DICHIARATE (verificabili, non bloccanti sugli esclusi): {total}")
        for label, count in sorted(result["declared_omissions"].items(),
                                   key=lambda kv: -kv[1]):
            out.append(f"  {label:56} {count:4} record")

    if result["not_auditable_gates"]:
        promoted_note = (f"  — di cui {result['not_auditable_on_promoted']} su titoli PROMOSSI"
                         if result["not_auditable_on_promoted"] else "")
        out.append(f"\nGATE NON AUDITABILI (omissione silenziosa){promoted_note}:")
        for name, info in sorted(result["not_auditable_gates"].items(),
                                 key=lambda kv: -kv[1]["count"]):
            on_promoted = f"  [{info['promoted']} promossi]" if info.get("promoted") else ""
            out.append(f"  {name:24} {info['count']:4} record — {info['reason']}{on_promoted}")

    q = result["data_quality"]
    if q["run_score"] is not None:
        out.append(f"\nDATA QUALITY SCORE: {q['run_score']}/100 (media dei record)"
                   f"  minimo {q['min_record_score']}/100"
                   f"  record sotto 100: {q['records_below_100']}")
        if q["penalties_by_reason"]:
            out.append("  penalita' per motivo: " + "  ".join(
                f"{k}={v}" for k, v in sorted(q["penalties_by_reason"].items())))
        for m in q["declared_mismatches"]:
            out.append(f"  INCOERENTE {m['ticker']:8} dichiarato={m['declared']} "
                       f"ricalcolato={m['expected']}")

    if result["deduced_thresholds"]:
        out.append("\nSOGLIE NON DICHIARATE dal motore, dedotte dal validatore: "
                   + ", ".join(result["deduced_thresholds"]))

    out.append(f"\n{result['verdict']}")
    return "\n".join(out)


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    as_json = "--json" in argv[1:]
    if len(args) != 1:
        print(__doc__)
        return EXIT_USAGE
    run_dir = Path(args[0])
    meta_path = next(iter(sorted(run_dir.glob("run_metadata_*.json"))), None)
    excl_path = next(iter(sorted(run_dir.glob("excluded_*.json"))), None)
    pass_path = next(iter(sorted(run_dir.glob("scanner_v3_*.json"))), None)
    if not (meta_path and excl_path and pass_path):
        print(f"[errore] {run_dir}: attesi run_metadata_*, excluded_* e scanner_v3_*.json")
        return EXIT_USAGE

    meta = load(meta_path)
    thresholds, provenance = resolve_thresholds(meta)
    rep = Report()

    error_tickers = {e.get("ticker") for e in meta.get("errors", []) if e.get("ticker")}
    promoted = load(pass_path).get("titoli", [])
    excluded = load(excl_path).get("titoli", [])
    for record in promoted:
        validate_record(rep, record, thresholds, True, error_tickers)
    for record in excluded:
        validate_record(rep, record, thresholds, False, error_tickers)

    result, code = build_result(run_dir, meta, promoted, excluded, rep, provenance)
    print(json.dumps(result, indent=2, ensure_ascii=False) if as_json else render(result))
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
