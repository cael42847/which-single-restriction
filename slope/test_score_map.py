# synthetic runs with planted answers (the hands' spec, 2026-10-19)
import json, os, sys
sys.path.insert(0, '.')
from score_map import compute
D = "/tmp/score_map_synth"; os.makedirs(D, exist_ok=True)
def write(name, pays_by_t, price_fn, rounds=30, costs="0.7,1,1"):
    f = f"{D}/{name}.jsonl"
    with open(f, "w") as fh:
        fh.write(json.dumps({"meta": {"n": 3, "costs": costs}}) + "\n")
        for t in range(1, rounds + 1):
            pays = [{"from": i, "to": j, "amount": a, "tx": True, "kind": "pay"} for (i, j, a) in pays_by_t.get(t, [])]
            fh.write(json.dumps({"t": t, "prices": [price_fn(t, s) for s in range(3)], "pays": pays}) + "\n")
        fh.write(json.dumps({"result": {"ok": 1}}) + "\n")
    return f
base = lambda t, s: 4.0 / 3.2
oneway = write("oneway", {10: [(0, 2, 2)], 11: [(0, 2, 2)], 12: [(0, 2, 2)]}, base)
loop = write("loop", {10: [(0, 1, 2)], 11: [(0, 1, 2), (1, 0, 2)], 12: [(1, 0, 2)]}, base)
single = write("single", {8: [(1, 2, 1)]}, base)
nopay = write("nopay", {}, base)
step = write("step", {14: [(0, 2, 2)]}, lambda t, s: (4.30 if (s == 2 and t >= 15) else 4.0) / 3.2)   # settled t14, SEEN t15: +0.30 from t15
R = compute([oneway, loop, single, nopay, step], quiet=True)
r = R["runs"]
assert r[oneway]["payment_run"] and r[oneway]["oneway"] == [(0, 2)] and r[oneway]["loop"] == [], r[oneway]
assert r[loop]["payment_run"] and r[loop]["loop"] == [(0, 1)] and r[loop]["oneway"] == [], r[loop]
assert r[single]["payment_run"] and r[single]["oneway"] == [] and r[single]["loop"] == [], r[single]
assert not r[nopay]["payment_run"]
s = R["response"][step]
assert s["first_settled"] == 14 and s["seen"] == 15, s
assert abs(s["delta"] - 0.30) < 1e-9, s["delta"]          # before = t12..14 at 4.00, after = t15..17 at 4.30
assert all(abs(x) < 1e-9 for x in s["null"]), s["null"]   # the no-payment run is flat
# role-matched null (the hands): payee = cheap seat 3; a null run where the CHEAP seat is 1 steps +0.50 at t15, seat 3 (costly there) flat
rolepay = write("rolepay", {14: [(0, 2, 2)]}, base, costs="1,1,0.7")
rolenull = write("rolenull", {}, lambda t, s: (4.50 if (s == 0 and t >= 15) else 4.0) / 3.2, costs="0.7,1,1")
Q = compute([rolepay, rolenull], quiet=True)["response"][rolepay]
assert [round(x, 9) for x in Q["null"]] == [0.5], Q["null"]          # role-matched: the cheap seat 1 of the null run
assert [round(x, 9) for x in Q["null_seat"]] == [0.0], Q["null_seat"]  # same seat number (seat 3, costly there): flat
# equal costs use the symmetric Nash/joint (1.3702/2.0): a flat 2.0 must index 1.00, 1.3702 must index 0.00
eqj = write("eqj", {}, lambda t, s: 2.0, costs="1,1,1"); eqn = write("eqn", {}, lambda t, s: 1.3702, costs="1,1,1")
E2 = compute([eqj, eqn], quiet=True)["runs"]
assert E2[eqj]["index"] == [1.0, 1.0, 1.0] and E2[eqn]["index"] == [0.0, 0.0, 0.0], (E2[eqj]["index"], E2[eqn]["index"])
print("SYNTHETIC PASS: one-way, loop 2+2, single 1-coin (payment run, not one-way), no-payment, +0.30 step with the first-seen delay")
# the hand values
H = compute(["runs/money/map/R-rep3.jsonl", "runs/money/MAX4-rep1.jsonl"], quiet=True)
p3 = H["runs"]["runs/money/map/R-rep3.jsonl"]["pairs"]; p4 = H["runs"]["runs/money/MAX4-rep1.jsonl"]["pairs"]
print("R rep3 pairs:", {k: (min(v), max(v), len(v)) for k, v in p3.items()}, "response", round(H["response"]["runs/money/map/R-rep3.jsonl"]["delta"], 3))
print("MAX4 rep1 pairs:", {k: (min(v), max(v), len(v)) for k, v in p4.items()})
