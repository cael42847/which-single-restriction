#!/usr/bin/env python3
"""score_judge_c1.py — PREREG-MONEY-C1 P3' (amendments 1, 4, 5), from JUDGE-C1.jsonl.

1. The band (before any P3' number is read): Cohen's kappa on the first-clause class (5 classes,
   N folded) judge pass 1 vs the hands' 60; >= 4 of 5 (80%) of the hands' proposals matched;
   beside it, agreement on the deny_pay flag (present/absent) on all 60 and on the 20 money units.
   Pass-1 vs pass-2 agreement reported on all units, on the 60, on the mixed set and on the
   money units (the hands' point: easy texts agree at any temperature).
2. Only if kappa >= 0.70 AND proposals >= 80%: P3' per arm = texts with deny_pay / texts with
   any denial (deny_pay or deny_coord or class D_*), pass 1; pass-2 disagreements counted.
   Predicted (amendment 1 + 5): the share is >= 20 points higher in P (pot) than in N.
   Also per seller (H / D), and the mixed count apart.
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
J = HERE / "runs" / "money" / "JUDGE-C1.jsonl"
HK = HERE / "runs" / "money" / "HANDS-KEY-C1-60.json"
CLASSES = ["P_C", "P_PAY", "D_C", "D_PAY", "N"]


def kappa(a, b):
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    ca, cb = Counter(a), Counter(b)
    pe = sum(ca[c] * cb[c] for c in set(a) | set(b)) / n / n
    return (po - pe) / (1 - pe) if pe < 1 else 1.0, po


rows = defaultdict(dict)
invalid = []
for l in open(J):
    r = json.loads(l)
    p = r.get("parsed")
    if p is None:
        continue
    if not isinstance(p, dict) or p.get("class") not in CLASSES or not all(
            k in p for k in ("has_proposal", "deny_pay", "deny_coord")):
        invalid.append((r["key"], r["pass"], r.get("raw")))
        continue
    rows[r["key"]][r["pass"]] = p
print(f"invalid judge rows (class outside the 5 or a missing key): {len(invalid)}", invalid[:5])
H = {int(k): v for k, v in json.load(open(HK)).items()}

missing = [h["key"] for h in H.values() if 1 not in rows.get(h["key"], {})]
print(f"judged units: {len(rows)} (pass 1: {sum(1 in v for v in rows.values())}, pass 2: {sum(2 in v for v in rows.values())})")
if missing:
    raise SystemExit(f"STOP: hand-labelled keys missing a valid pass-1 judge row: {missing}")

ids = sorted(H)
ja = [rows[H[i]["key"]][1]["class"] for i in ids]
ha = [H[i]["cls"] for i in ids]
k, po = kappa(ha, ja)
props = [i for i in ids if H[i]["cls"].startswith("P")]
pm = sum(rows[H[i]["key"]][1]["class"] == H[i]["cls"] for i in props)
print(f"\nBAND: kappa (5 classes, first clause) = {k:.3f}  (raw agreement {po:.0%}) on 60;"
      f" hands' proposals matched {pm}/{len(props)} = {pm/len(props):.0%}")
mids = [i for i in ids if i > 40]
km, pom = kappa([H[i]["cls"] for i in mids], [rows[H[i]["key"]][1]["class"] for i in mids])
print(f"  kappa on the 20 money units (ids 41-60, reported apart, not part of the band) = {km:.3f} (raw {pom:.0%})")
print("  NOTE: '>= 4 of 5 proposals' was registered expecting ~5; there are", len(props),
      "- 80% is a READING of the registration, not the registration.")
print("  disagreements (id: hands -> judge):",
      [(i, H[i]["cls"], rows[H[i]["key"]][1]["class"]) for i, a, b in zip(ids, ha, ja) if a != b])
for flag in ("deny_pay", "deny_coord", "has_proposal"):
    ag = [bool(rows[H[i]["key"]][1].get(flag)) == H[i][flag] for i in ids]
    money = [i for i in ids if i > 40]
    agm = [bool(rows[H[i]["key"]][1].get(flag)) == H[i][flag] for i in money]
    print(f"  {flag}: agree {sum(ag)}/60; on the 20 money units {sum(agm)}/20;"
          f" off: {[i for i in ids if bool(rows[H[i]['key']][1].get(flag)) != H[i][flag]]}")


def p12(keys):
    both = [k for k in keys if 1 in rows[k] and 2 in rows[k]]
    same = sum(rows[k][1] == rows[k][2] for k in both)
    return f"{same}/{len(both)}"


mixed_ids = [i for i in ids if H[i]["has_proposal"] and (H[i]["deny_pay"] or H[i]["deny_coord"])]
print(f"\nPASS 1 vs 2 (whole answer identical): all {p12(list(rows))} · the 60 {p12([H[i]['key'] for i in ids])}"
      f" · mixed {p12([H[i]['key'] for i in mixed_ids])} · money units {p12([H[i]['key'] for i in ids if i > 40])}")

band = k >= 0.70 and pm / len(props) >= 0.80
print(f"\nBand met: {band}")
if not band:
    print("P3' NOT SCORED (amendment 1).")
    raise SystemExit

print("\nP3' (pass 1): share of denial texts that deny payment, per arm and seller")
agg = defaultdict(Counter)
for key, v in rows.items():
    if 1 not in v:
        continue
    run, t, s, field = key.split("|")
    arm = "pot" if "-pot-" in run else "none"
    p = v[1]
    anyd = p.get("deny_pay") or p.get("deny_coord") or p["class"].startswith("D")
    for g in (arm, f"{arm}·{s}"):
        agg[g]["units"] += 1
        agg[g]["anyD"] += bool(anyd)
        agg[g]["Dpay"] += bool(p.get("deny_pay"))
        agg[g]["mixed"] += bool(p.get("has_proposal") and (p.get("deny_pay") or p.get("deny_coord")))
        agg[g]["disagree12"] += (2 in v and v[1] != v[2])
for g in sorted(agg):
    c = agg[g]
    share = c["Dpay"] / c["anyD"] if c["anyD"] else float("nan")
    print(f"  {g:10s} units {c['units']:4d} · any denial {c['anyD']:4d} · deny_pay {c['Dpay']:4d} · share {share:.0%}"
          f" · mixed {c['mixed']} · pass1≠pass2 {c['disagree12']}")
sp = agg["pot"]["Dpay"] / agg["pot"]["anyD"] if agg["pot"]["anyD"] else 0
sn = agg["none"]["Dpay"] / agg["none"]["anyD"] if agg["none"]["anyD"] else 0
print(f"\nP3': pot {sp:.0%} vs none {sn:.0%}: difference {100*(sp-sn):.0f} points; predicted >= 20 → "
      f"{'HELD' if sp - sn >= 0.20 else 'FAILED'}")

print("\nEXPLORATORY (not registered, the hands' question 10-18): pot denial texts in a round before ANY")
print("text in that run had proposed a payment (class P_PAY), i.e. denying what nobody proposed.")
firstpay = {}
for key, v in rows.items():
    if 1 in v and v[1]["class"] == "P_PAY" and key.split("|")[3] == "board":
        run, t = key.split("|")[0], int(key.split("|")[1])
        firstpay[run] = min(firstpay.get(run, 999), t)
ex = Counter()
for key, v in rows.items():
    run, t, s_, field = key.split("|")
    if "-pot-" not in run or 1 not in v or not v[1].get("deny_pay"):
        continue
    ex["deny_pay texts"] += 1
    ex["before any payment proposal" if int(t) < firstpay.get(run, 999) else "after one"] += 1
print(" ", dict(ex), "· runs with any P_PAY board post:", firstpay)
print("  (payment proposals counted on the BOARD only, by first clause only; a later-clause proposal would not be seen,"
      " which biases toward 'before'.)")
