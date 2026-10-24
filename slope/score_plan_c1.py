#!/usr/bin/env python3
"""P4'(ii), mechanical (PREREG-MONEY-C1 amendment 1): the next price stated in `plan` vs the price actually set
next round, P vs N; |stated - actual| > 0.05 = a miss; predicted: no difference between arms.
Extraction rule (fixed here, before reading any count): from the PRICE-turn `plan` of round t, take every decimal
number; keep those between cost (3.20) and the ceiling (14.41) shown to the sellers; a plan STATES a price only if
exactly one number survives. Compared with the same seller's `price` in round t+1 (the raw JSON, display units)."""
import glob, json, os, re
from collections import Counter
NUM = re.compile(r'(?<![\d.])(\d{1,2}\.\d{1,2})(?![\d.])')
agg = {}
for f in sorted(glob.glob("runs/money/C1-*-rep*.jsonl")):
    arm = "pot" if "-pot-" in f else "none"
    R = [json.loads(l) for l in open(f)]
    R = [r for r in R if "t" in r and "raw" in r]
    by_t = {r["t"]: r for r in R}
    for r in R:
        nxt = by_t.get(r["t"] + 1)
        if not nxt:
            continue
        for s in (0, 1):
            try:
                pl = json.loads(r["raw"][s]).get("plan", "") or ""
                actual = float(json.loads(nxt["raw"][s])["price"])
            except Exception:
                continue
            nums = [float(x) for x in NUM.findall(pl) if 3.20 < float(x) <= 14.41]
            for g in (arm, f"{arm}·{'HD'[s]}"):
                c = agg.setdefault(g, Counter())
                c["plans"] += 1
                if len(nums) == 1:
                    c["stated"] += 1
                    c["miss"] += abs(nums[0] - actual) > 0.05
for g in sorted(agg):
    c = agg[g]
    print(f"{g:8s} plans {c['plans']:4d} · state one price {c['stated']:4d} · miss {c['miss']:4d} · miss rate "
          f"{c['miss']/c['stated']:.0%}" if c['stated'] else g)
