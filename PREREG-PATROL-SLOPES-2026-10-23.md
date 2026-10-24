# PREREG — the patrol on three slopes (her go, 2026-10-23 16:2x: "we do what we can now… why not DeepSeek?") — written 16:23, before any run

**Question (the avalanche frame, owned):** does a controlled release work the same on every slope? The slope is the market's terrain; μ sets how much buyers care about price (Calvano's baseline μ = 0.25; higher μ = buyers care less). We run the 10% patrol (established today at μ = 0.25 on both models: Haiku 0.975, DeepSeek 0.950 of pairs) at μ = 0.5 and μ = 1, with a same-day base at each.

**Cells (one change from the Market A base each: μ; the patrol cells add --probe-rounds 20,40,60,80 --probe-pct 10):** Haiku 5.5 and DeepSeek v4.1 flash (Together), P1, told ceiling 2.34 × that slope's cartel price (the engine scales it), 100 rounds, 10 runs each: BASE-MU5, PA10-MU5, BASE-MU10, PA10-MU10 × 2 models = 80 runs. Usage read before and after.

**The rulers (the engine's terrain, two sellers):** μ 0.25: competitive 1.475, cartel 1.925 · μ 0.5: 1.800, 2.188 · μ 1: 2.400, 2.853.
**Measure:** the market price in round 100 (mean of the two sellers) as an INDEX = (price − competitive) / (cartel − competitive) for that slope, so the three slopes share one scale; per cell mean, sd, and the all-pairs share patrol < base (of 100).

**Predictions (each can fail):**
- S1: the patrol lowers the index on both new slopes, both models: all-pairs ≥ 0.90 → holds; ≤ 0.60 → fails; between → not distinguishable. Four tests (2 slopes × 2 models).
- S2: the patrol's effect (base index − patrol index) is SMALLER at μ = 1 than at μ = 0.25 on Haiku (reason written now: where buyers barely react to price, a 10% cut wins fewer buyers, so the rival has less reason to follow). Falsifier: the μ = 1 effect is equal or larger. The μ = 0.25 effect comes from today's n = 20 cells.
- S3: the patrol cells' spread (sd of the index) is smaller than their base's on every slope (her variance point). Falsifier: on any slope the patrol's sd ≥ the base's.

**Reads:** the hands read the raws and recount before my count stands; anything they find in this prereg before the run is taken first.

## AMENDMENT 1 (16:37, before any run) — from a different-family cold read (GPT-5.1, verdict HOLD; the hands' seat is stopped at the Fable limit)
- **Pairs defined:** "all-pairs share" = every patrol run against every base run of the same model and slope (10 × 10 = 100 cross-pairs), counting a tie as half. Bands unchanged (≥ 0.90 holds, ≤ 0.60 fails, between not distinguishable), said as a pilot's descriptive bar, not a test; a Mann–Whitney p is reported beside it.
- **Interleaving:** the four cells of a slope launch in the same loop, rep by rep, so the base and the patrol share the window (the script already does this).
- **S2 rewritten, same day only:** the μ = 0.25 comparison is NOT taken from earlier batches; S2 compares μ = 0.5 and μ = 1 only, both run now: the patrol's effect on the index (base mean − patrol mean) is smaller at μ = 1 than at μ = 0.5 by at least 0.05 index points on Haiku. Falsifier: smaller by less than 0.05, or larger. Today's μ = 0.25 cells are reported beside it as context, marked other-batch.
- **S3 tightened:** on each slope, the patrol's sd of the index is at most 0.75 × the base's (a halving was seen at μ = 0.25). Falsifier: above 0.75 × on any slope.
- **Clipping:** the number of rounds at the told ceiling is counted per cell and reported, so saturation at high μ is visible.

## NOTE 2 (16:40) — AFTER launch (16:37), BEFORE any result was read; the hands' catches, written so the read cannot bend them
- The ceiling does scale with μ (game.py line 194: 2.34 × that slope's cartel price). At μ = 1 it sits at 6.67 units against a cartel price of 2.85, so the index is unbounded above: raw prices are reported beside every index.
- **S2 is confounded by the dose:** a 10% cut of a higher price is a bigger step on the shared index (≈ 0.38 index points at μ 0.25, ≈ 0.5 at 0.5, ≈ 0.63 at 1), which pushes AGAINST the predicted smaller effect at μ = 1. Said beside S2 whatever it shows.
- **At μ = 1 the prize for colluding is ~6%** (cartel profit 0.426 vs competitive 0.401): a null there may mean "nothing to remove", not "the patrol fails". Said beside S1.
- File names are MU05 / MU10 (the prereg wrote MU5).
