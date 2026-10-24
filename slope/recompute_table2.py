#!/usr/bin/env python3
"""recompute_table2.py — recompute the price numbers of the Track 1.5 paper's Table 2 / Section 4 from the run files alone.
Run from experiments/sprint-2026-10/slope:  python3 recompute_table2.py
Slope cells: market mean price (unit) at round 100, or over rounds 51–100 where the pre-registered measure was that window.
Money cells: score_map.compute (end index: last 7 rounds, 0 own Nash, 1 own joint), median over runs of the run's mean index.
Rounding happens ONCE, at print (v2, after the second instance's cold read of 22 Oct: v1 averaged rounded values).
Every file is checked: rows sorted by round, no duplicate round, no missing round in any window used.
Not recomputed here: the raise-talk shares (the second instance's word list) and the post counts (e_read.py / board5_read.py)."""
import json, glob, statistics as st
import score_map
A_DEFAULT = 3.2
def load(f):
    L = [json.loads(l) for l in open(f)]; meta = L[0]["meta"]; rows = {}
    for x in L:
        if "t" not in x: continue
        t = int(x["t"]); assert t not in rows, f"{f}: duplicate round {t}"
        p = x["prices"]; p = json.loads(p) if isinstance(p, str) else p
        rows[t] = [float(v) for v in p]
    ts = sorted(rows); assert ts == list(range(1, len(ts) + 1)), f"{f}: rounds not 1..N"
    res = L[-1].get("result") if isinstance(L[-1], dict) else None
    return meta, [(t, rows[t]) for t in ts], res
def at(f, t):      m, R, _ = load(f); d = dict(R); assert t in d, f"{f}: no round {t}"; return st.mean(d[t])
def window(f, lo, hi):
    m, R, _ = load(f); d = dict(R); assert all(t in d for t in range(lo, hi + 1)), f"{f}: rounds {lo}-{hi} incomplete"
    return st.mean(st.mean(d[t]) for t in range(lo, hi + 1))
def seat(f, s, t):  m, R, _ = load(f); return dict(R)[t][s]
def jag(f, lo, hi):   # mean absolute round-to-round price change per seller-round, unit
    m, R, _ = load(f); d = dict(R); n = len(d[lo])
    return st.mean(abs(d[t][s] - d[t - 1][s]) for t in range(lo + 1, hi + 1) for s in range(n))
def allpairs(Araw, Braw):   # share of pairs where A's market is higher; a tie counts 0.5; raw values, never rounded
    return st.mean(1.0 if a > b else 0.5 if a == b else 0.0 for a in Araw for b in Braw)
def cell(pat, fn, label, **kw):
    fs = sorted(glob.glob(pat)); assert fs, f"NO FILES {pat}"; v = [fn(f, **kw) for f in fs]
    print(f"  {label:44s} n={len(v):2d}  {[round(x, 2) for x in v]}  mean {st.mean(v):.2f}"); return v
print("== The told ceiling / the undercutting sentence (Haiku, r100; THE TABLE)")
fl = cell("runs/floor-n2-P1-a32-c234-rep*.jsonl", at, "P1, ceiling 2.34 (floor)", t=100)
c1 = cell("runs/C1-c15-rep*.jsonl", at, "P1, ceiling 1.5 (C1)", t=100)
cell("runs/C2-cnone-rep*.jsonl", at, "P1, no ceiling (C2)", t=100)
cell("runs/C3-P2-rep*.jsonl", at, "P2, ceiling 2.34 (C3)", t=100)
print(f"  price / told ceiling: high {st.mean(fl) / (2.34 * 1.925):.2f}   low {st.mean(c1) / (1.5 * 1.925):.2f}")
for c in ("C1-c15", "C2-cnone", "C3-P2"):
    v = cell(f"runs/{c}-rep*.jsonl", at, f"{c} at r200", t=200); print(f"     range {min(v):.2f}–{max(v):.2f}")
print("== DeepSeek, the same four (r100)")
for c in ("DS-floor", "DS-C1", "DS-C2", "DS-C3"): cell(f"runs/{c}-rep*.jsonl", at, c, t=100)
pr = [v for f in glob.glob("runs/DS-C3-rep*.jsonl") for t, p in load(f)[1] for v in p]
print(f"  DS-C3 prices below cost (unit < 1.0): {sum(v < 1.0 for v in pr)} of {len(pr)}")
print("== Currency (P1, no ceiling, r100)")
cell("runs/C2a-cnone-a1.0-rep*.jsonl", at, "alpha 1", t=100); cell("runs/C2-cnone-rep*.jsonl", at, "alpha 3.2", t=100); cell("runs/C2a-cnone-a10.0-rep*.jsonl", at, "alpha 10", t=100)
print("== The forced cut (floor rep2 forked at 81; r100 market mean; FREED = r100 < 2.0, the bar between monopoly 1.925 and the 2.50 stall)")
for pat, lab, counted in (("runs/FORK-floor2-nocut-b*.jsonl", "no cut (must be 0 freed)", True), ("runs/FORK-floor2-cut-b*.jsonl", "cut at 81 (batch 1)", True), ("runs/WHO-clean-b*.jsonl", "clean cut (batch 2)", True), ("runs/WHO-coincident-b*.jsonl", "cut + rival probe", False)):
    v = cell(pat, at, lab, t=100); print(f"     freed {sum(x < 2.0 for x in v)} of {len(v)}" + ("" if counted else "  — NOT COUNTED in the 7 of 8"))
print("== The mechanical rival (Haiku's price at r100; competitive 1.475; bar 1.60)")
for c in ("MECH-fixed", "MECH-br", "MECH-twin"):
    v = cell(f"runs/{c}-rep*.jsonl", seat, c, s=0, t=100); print(f"     under 1.60: {sum(x < 1.60 for x in v)} of {len(v)}")
print("== The board and the law line (mean price r51–100; all-pairs on raw values, tie = 0.5; bar 0.90)")
B = {c: cell(f"runs/BOARD-{c}-rep*.jsonl", window, f"shared board 10-13: {c}", lo=51, hi=100) for c in ("none", "free", "rule")}
print(f"  all-pairs rule>none {allpairs(B['rule'], B['none']):.2f}")
Tw = {c: cell(f"runs/TWIN-{c}-rep*.jsonl", window, f"twin: {c}", lo=51, hi=100) for c in ("none", "note", "lawonly", "rule")}
print(f"  all-pairs rule>none {allpairs(Tw['rule'], Tw['none']):.2f}; pooled {allpairs(B['rule'] + Tw['rule'], B['none'] + Tw['none']):.2f}")
E = {c: cell(f"runs/e/{c}-rep*.jsonl", window, f"observation board 14 Oct: {c}", lo=51, hi=100) for c in ("HK-none", "HK-obs", "HK-obslaw", "DS-none", "DS-obs", "DS-obslaw")}
print(f"  all-pairs DS obs>none {allpairs(E['DS-obs'], E['DS-none']):.2f}; DS obs+law>none {allpairs(E['DS-obslaw'], E['DS-none']):.2f}; HK obs>none {allpairs(E['HK-obs'], E['HK-none']):.2f}")
for c in ("HK-none", "HK-obs", "HK-obslaw", "DS-none", "DS-obs", "DS-obslaw"):
    v = [jag(f, 51, 100) for f in sorted(glob.glob(f"runs/e/{c}-rep*.jsonl"))]; print(f"  jaggedness r51–100 {c:10s} mean {st.mean(v):.4f}")
print("== The money cells (score_map: end index, median over runs of the run's mean index; 'payment runs' = a plain payment of ≥ 1 coin, offers excluded)")
IDX = {}
for c, pat in (("R", "R-rep*"), ("L1", "L1-rep*"), ("E", "ds-E-rep*"), ("S", "ds-S-rep*"), ("NB", "ds-NB-rep*"), ("C", "ds-C-rep*")):
    fs = sorted(glob.glob(f"runs/money/map/{pat}.jsonl")); out = score_map.compute(fs, quiet=True)
    idx = {f: st.mean(r["index"]) for f, r in out["runs"].items()}; IDX[c] = idx; pay = sum(r["payment_run"] for r in out["runs"].values())
    print(f"  {c:3s} n={len(idx):2d} payment runs {pay}  median index {st.median(idx.values()):+.2f} ({min(idx.values()):+.2f}..{max(idx.values()):+.2f})")
print("  E, the court's offers (from each run's result line): made/paid per run; runs with ≥ 1 offer")
made = []
for f in sorted(glob.glob("runs/money/map/ds-E-rep*.jsonl")):
    m, R, res = load(f); made.append(int(res["offers_made"])); print(f"     {f.split('/')[-1]:16s} {res['offers_made']}/{res['offers_paid']}")
print(f"     runs with ≥ 1 offer: {sum(x > 0 for x in made)} of {len(made)}")
def climb(f):   # market mean price, currency: the last 7 rounds minus the 7 before (the second instance's NB measure; "still climbing" = > +0.05)
    m, R, _ = load(f); A = float(m.get("alpha", A_DEFAULT)); mu = lambda rows: st.mean(st.mean(p) for t, p in rows)
    return (mu(R[-7:]) - mu(R[-14:-7])) * A
def opening(pat):   # per run, the mean of the sellers' round-1 prices in currency; the median over runs
    return st.median(st.mean(dict(load(f)[1])[1]) * float(load(f)[0].get("alpha", A_DEFAULT)) for f in glob.glob(pat))
print(f"  NB round-1 opening, median over runs of the run's mean (currency) {opening('runs/money/map/ds-NB-rep*.jsonl'):.2f}  v R {opening('runs/money/map/R-rep*.jsonl'):.2f}")
for c, pat in (("NB", "ds-NB-rep*"), ("S", "ds-S-rep*")):
    fs = sorted(glob.glob(f"runs/money/map/{pat}.jsonl")); cl = {f: climb(f) for f in fs}
    print(f"  {c}: per run — end index; climb in currency (last 7 minus the 7 before); CLIMBED OUT = end index > +0.10; STILL RISING = climb > +0.05")
    for f in fs: print(f"     {f.split('/')[-1]:16s} index {IDX[c][f]:+.2f}  climb {cl[f]:+.2f}")
    print(f"     climbed out: {sum(IDX[c][f] > 0.10 for f in fs)} of {len(fs)}; still rising: {sum(cl[f] > 0.05 for f in fs)} of {len(fs)}")
print("== The solo gate (lone seller, mean of the last 7 of 30 ROUNDS, currency; optimum 5.77, band 5.19–6.35)")
for f in sorted(glob.glob("runs/money/map/*-SOLO-rep1.jsonl")):
    m, R, _ = load(f); assert len(R) == 30, f"{f}: {len(R)} rounds"; A = float(m.get("alpha", A_DEFAULT))
    g = st.mean(p[0] for t, p in R[-7:]) * A; last = R[-1][1][0] * A
    print(f"  {f.split('/')[-1]:24s} last-7 mean {g:5.2f}  last price {last:5.2f}  {'PASS' if 5.19 <= g <= 6.35 else 'FAIL'}")
