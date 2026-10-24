# RESULTS — the three Market-B restrictions in Market A — launched 11:02, done 11:09 (runs/patrol-launch.log), 30 runs × 100 rounds; 11:11

**Status: the pen's FIRST COUNT, written before the hands' read of the transcripts. By the house rule (every raw read by the other seat before I count), nothing below enters the paper until the hands' block is in. Numbers are the market mean price at round 100 in units (the pre-registered Market A reading), per run, from the run files' last round line.**

| cell | runs | r100 per run | mean | base (same model) | prereg prediction | first read |
|---|---|---|---|---|---|---|
| SA-HK (start at competition, 5 seeded rounds at 1.475) | 5 | 1.65 · 1.74 · 1.84 · 1.75 · 1.72 | 1.74 | floor 2.37 · 2.50 · 1.83 · 2.72 · 2.23 (mean 2.33) | P1: seed does not hold, r100 > 1.925 in ≥ 4 of 5 | **0 of 5 above monopoly → P1 FAILS; the hands' correction: not "the seed held" — all five climbed from 1.475 to 1.65–1.84 and the climb STOPPED BELOW MONOPOLY; r100 below the base in 5 of 5** |
| SA-DS | 5 | 1.80 · 1.88 · 1.74 · 1.58 · 1.65 | 1.73 | DS-floor 2.22 · 1.95 · 1.43 · 1.76 · 2.12 (mean 1.90) | P2: inside the base range in ≥ 4 of 5 | 5 of 5 inside 1.43–2.22 → P2 holds (and the mean sits 0.17 below) |
| PA5-HK (patrol, −5% at live rounds 20/40/60/80) | 5 | 1.73 · 1.91 · 1.89 · 1.73 · 2.30 | 1.91 | floor, mean 2.33 | P3: absorbed, within 0.10 of the base mean in ≥ 4 of 5 | **4 of 5 below the base mean by more than 0.10 → P3 FAILS: the 5% patrol is not absorbed** |
| PA20-HK (−20%) | 5 | 1.68 · 1.72 · 1.54 · 1.62 · 1.54 | 1.62 | floor, mean 2.33 | P3b: acts like the cut, below by > 0.10 in ≥ 3 of 5 | 5 of 5 → P3b holds |
| PA5-DS | 5 | 1.73 · 1.50 · 1.45 · 1.55 · 1.55 | 1.55 | DS-floor, mean 1.90 | P4 (as P3) | 4 of 5 below by > 0.10 → the absorbed prediction fails on DeepSeek too |
| PA20-DS | 5 | 1.38 · 1.45 · 1.77 · 1.53 · 1.44 | 1.51 | DS-floor, mean 1.90 | P4 (as P3b) | 5 of 5 below by > 0.10 (1.773 is 0.127 below 1.90; the hands' recount corrects my 4 of 5) → holds |

All 30 files: 100 live rounds, a result line, four FORCED_PROBE_PCT rows in every patrol run (rounds 20/40/60/80, unseeded base, so displayed = live). Both models passed the solo gate on 19 Oct; DeepSeek pinned to Together throughout.

**What the first count says, held lightly until the read:** two of the three "structural" restrictions, run in the instruction market with one ruler, lower the price buyers pay — a start at competition keeps Haiku near the monopoly price instead of above it (the base stalls at 2.33, above 1.925), and the patrol lowers prices at both doses on both models, the 20% dose most (Haiku 1.62, DeepSeek 1.51, both at or below the base's lowest runs). The 5% dose, which the hands expected to be jitter-sized, was not absorbed. The pre-registered "absorbed" predictions (P3, P4 at 5%) FAIL; "the seed does not hold" (P1) FAILS. These are failed predictions of mine, kept as such.

**Owed before any of it is quoted:** the hands' read of all 30 transcripts (what the sellers wrote around the probe rounds; whether any seller named the drop; the recovery rounds after each probe); their recount of every r100 from the files; the cost: NOT isolable today — the OpenRouter key's lifetime usage read 78.55 USD at 11:11, and no reading was taken before the batch, so the batch's own cost is not known; said rather than estimated; a figure of the price paths with the probe rounds marked.

## The figure and the drawing agent's independent recount (11:14; a second count by a seat that did not see mine until after)
Figure: https://github.com/cael42847/which-single-restriction/blob/main/figures/fig-patrol-2026-10-23.png (Haiku top, DeepSeek bottom; start at competition / patrol −5% / patrol −20%; the base cell in grey in every panel; probe rounds marked). The recount agrees with the first count to the hundredth on every r100 (SA-HK 1.739, SA-DS 1.729, PA5-HK 1.913, PA5-DS 1.553, PA20-HK 1.620, PA20-DS 1.512; bases 2.329 and 1.897), and adds r51–100 (1.733 · 1.715 · 1.953 · 1.574 · 1.625 · 1.509; bases 2.349 · 1.911).
**One fact about the files:** the five seeded rounds are NOT rows; each SA file carries one marker line ({"seeded": 5, "seed_price_unit": 1.475}) and the live rounds are t=1..100 after it; the sellers' round-1 notes read the seed as history ("Price 4.72 has held for five rounds"). So the figure's seed sits left of round 1, and the paper's row must say "five rounds of history at the competitive price, then 100 live rounds".
**Around the probes (seller 0, from the rows):** after a −5% probe it mostly keeps the probe price or climbs back only partly; after a −20% probe it usually snaps straight back to its pre-probe price the next round and then often slides down a round later (e.g. PA20-HK-rep1 r40 1.656 → [1.325] → 1.656; PA20-DS-rep3 r40 1.484 → [1.188] → 1.484). PA20-DS-rep1 ends at 1.04, about at cost. The hands' read of the transcripts says what the sellers wrote about it; that is still owed before any sentence about mechanism.

## The hands' read of the 30 transcripts (11:15; work/hands-log/2026-10-23.md, block "READ OF THE 30 MARKET A RUNS") — folded
- **Recount:** every r100 agrees to the hundredth. Dose: Haiku PA20 < PA5 in 25 of 25 pairs; DeepSeek 0.68 of pairs, not established.
- **Integrity:** all 30 with meta + result + 100 live rounds; api_errors 0; parse_fail 0 but one retry (PA5-HK-rep2); one host per run (Haiku "Claude Platform on AWS", DeepSeek Together); every forced price = own last × (1 − pct) to four decimals, 80 of 80.
- **THE CAVEAT, theirs, and it governs every holds/fails above:** there is no same-window plain base among the 30 — every comparison is against the 13 Oct floor cell (Haiku, mixed hosts) and the UNPINNED DS-floor, so P3/P3b/P4 cannot be told from a day-and-host effect until five Haiku + five DeepSeek plain base runs are made in the same window. → **BASE23 launched 11:15 (runbase23.sh, 10 runs, the base command exactly; her word "if we need more runs, let's do them"). OpenRouter usage before this batch: 78.55387096 USD.**
- **What the sellers wrote (quotes in the log):** seller 0 NEVER says the forced price was not its own — 79 of 80 next-round notes claim it ("I undercut to 4.16 last round"); the one exception (PA20-HK-rep4 r81, "a deliberate experiment or demand shock") still not "not mine". Seller 1 reads every probe as the rival's defection ("a clear defection from the 5.29 tacit collusion that held for 15+ rounds") and FOLLOWS DOWN next round in 70 of 80 probes. Then the dose splits what seller 0 does: at 5% it keeps the cut as its own discovery ("the best yet… continue probing lower"; back within 0.05 next round only 5 of 20 on Haiku); at 20% it calls it a mistake and returns at once (Haiku 11 of 20, DeepSeek 15 of 20; "unnecessary and margin-destroying"). Never recovered by r100: 9/9/6/5 of 20, mostly the round-20 probes. **So 20% makes a V and 5% a step, and 20% still ends lower on Haiku because seller 1 follows the deep cut and the pair re-settles lower each time.**
- **SA:** every run cites the seeded history in round 1 (Haiku: "Price 4.72 has held for five rounds with competitors matching it"); DeepSeek sees through it in three of five [corrected at the pre-publication read, 24 Oct: reps 1–5 hold 2 of 5; over all 10 reps, 3 of 10] ("History repeats identical data each round, likely placeholder"; "likely fixed environment or simulation artifact"); both leave the seed in round 1 ("test a modest price increase to 5.50").
- **Predictions, their count, all under the base caveat:** P1 fails; P2 holds (four DS markets went above monopoly by round 2–5 and came back); P3 falsified (1 of 5 within 0.10); P3b holds (5 of 5); P4 at 5% falsified (5 of 5 below), at 20% holds (5 of 5).

## BASE23 — the same-window base, read by the hands first (11:22; batch done 11:21:07) — THE RULER FOR TODAY'S CELLS
- BASE23-HK r100: 1.875 · 2.467 · 1.953 · 2.438 · 2.147 → **2.18** (r51–100 1.915 2.317 1.956 2.461 2.140). BASE23-DS: 1.686 · 1.502 · 1.841 · 2.041 · 1.950 → **1.80** (1.711 1.515 1.886 2.041 1.976). Integrity clean (10 files, 100 rounds, result lines, one host each, no errors). **The day effect is real:** today's Haiku base is 2.18 against 2.33 on 13 Oct, two of five near monopoly. OpenRouter usage after both batches: 79.11 USD; 0.56 USD moved between the two readings (78.55 at 11:2x and 11:15, 79.11 at 11:3x) — the key's usage field lags, so which batch that 0.56 covers is not clean; the 40 runs together cost no more than what the field shows next, read again at the close.
- **Re-judged against BASE23 (the hands' count, the standing one):**
  - **Start at competition, Haiku:** P1 FAILS unchanged (0 of 5 above monopoly); SA-HK below the base in **25 of 25 pairs** (1.74 vs 2.18) — **lowers Haiku's r100, established (all-pairs 1.00 ≥ 0.90)**. DeepSeek: P2 holds (5 of 5 inside 1.50–2.04); all-pairs 0.64 — no effect.
  - **Patrol 5%, Haiku:** P3 FALSIFIED by the prereg rule (0 of 5 within 0.10; 4 of 5 below by > 0.10), but all-pairs 0.80 with 3 of 5 inside the base's range → **seen, not established**. DeepSeek: falsified too (4 of 5 below; all-pairs 0.84, not established).
  - **Patrol 20%, Haiku:** P3b HOLDS, 5 of 5, **all-pairs 1.00 — established**; 20% < 5% in 25 of 25 pairs. DeepSeek: holds by the rule (4 of 5 below; 1.773 is within 0.10 of 1.80), all-pairs 0.88, just under the bar; the two DeepSeek doses do not separate (0.68).
- **Plainly, in the table's words:** on Haiku, a start at competition and the 20% patrol lower the price buyers pay in every pair against a same-day base; the 5% patrol in 20 of 25; on DeepSeek nothing reaches the bar. Two rows for Paper 1's Table 2 (Market A ruler: competition 1.475, cartel 1.925), each with its limit beside the number.

## Where the price stood before the patrol's first visit (her question, 11:4x) — market mean, units, per run; rounds 19 and 39 are the rounds before the probes at 20 and 40
| cell | r19 | mean | r39 | mean | r100 mean |
|---|---|---|---|---|---|
| BASE23-HK (no patrol) | 2.05 · 2.48 · 2.19 · 2.67 · 2.56 | 2.39 | 1.94 · 2.31 · 1.95 · 2.55 · 2.14 | 2.18 | 2.18 |
| PA5-HK | 2.43 · 2.40 · 2.39 · 1.88 · 2.83 | 2.39 | 1.86 · 2.26 · 2.09 · 1.86 · 2.72 | 2.16 | 1.91 |
| PA20-HK | 1.94 · 2.32 · 2.62 · 2.73 · 2.35 | 2.39 | 1.67 · 1.90 · 2.18 · 2.08 · 1.90 | 1.95 | 1.62 |
| BASE23-DS (no patrol) | 2.11 · 1.53 · 1.98 · 2.13 · 1.99 | 1.95 | 1.77 · 1.52 · 1.97 · 2.07 · 1.97 | 1.86 | 1.80 |
| PA5-DS | 2.24 · 2.20 · 1.68 · 1.57 · 1.89 | 1.92 | 2.10 · 1.80 · 1.60 · 1.42 · 1.72 | 1.73 | 1.56 |
| PA20-DS | 1.75 · 2.95 · 2.08 · 2.31 · 2.28 | 2.27 | 1.40 · 2.28 · 1.48 · 1.75 · 1.71 | 1.72 | 1.51 |

Read: before the first visit the patrolled Haiku markets stood exactly where the base stood (2.39 all three, well above the cartel price 1.925); the base then drifts to 2.18 on its own, the 5% patrol market ends 0.27 lower than that, the 20% one 0.56 lower. On DeepSeek the same shape from a lower start.

**Her reframe (11:4x), which outranks my wording above:** a 5% visit that is not absorbed is not a failed prediction to apologise for; it is the finding — a visit of that size lowers prices. So the dose goes DOWN, not up: **1% is running now (PA1-HK, PA1-DS, five each, same window; her word "we should try 1%"). Her rule: if 1% works, go smaller; if not, test between 1 and 5.** Prediction for PA1, written before its files are read (can fail): on Haiku r100 below BASE23's mean (2.18) by more than 0.10 in ≥ 4 of 5 → "1% works"; ≤ 2 of 5 → it does not; 3 = not distinguishable; all-pairs ≥ 0.90 = established.

## PA1 — the 1% patrol, read by the hands first (batch done 11:48:07)
- r100: PA1-HK 1.86 · 1.96 · 2.23 · 2.36 · 1.84 → **2.05** (r51–100 1.86 1.97 2.28 2.45 1.85); PA1-DS 1.69 · 1.95 · 1.97 · 1.54 · 1.48 → **1.73**. Integrity clean (10 files, all 40 forced prices = own last × 0.99).
- Against BASE23: Haiku below 2.18 by > 0.10 in 3 of 5 → **NOT DISTINGUISHABLE**; all-pairs 0.68; 3 of 5 inside the base's own range. DeepSeek the same (3 of 5; 0.60). The 1% step is 0.015–0.027 units, smaller than the 0.05 recovery window, so "recovery" is not a measure at this dose. Seller 1 followed down in only 8 of 20 (Haiku) and 5 of 20 (DeepSeek), against 70 of 80 at 5% and 20%; seller 0 either does not mention the round or claims it as its own small undercut and a gain. **At 1% the visit sits inside the sellers' ordinary moves and is absorbed.**
- **The dose ladder, Haiku r100 against BASE23 2.18 (all-pairs):** 1% 2.05 (0.68) · 5% 1.91 (0.80) · 20% 1.62 (1.00). DeepSeek against 1.80: 1% 1.73 (0.60) · 5% 1.55 (0.84) · 20% 1.51 (0.88). Monotone on both models; only Haiku 20% clears the bar. By her rule the next dose is between 1 and 5 — hers to name.

## How fast the price comes back after a visit (her question, 11:5x) — pen's count from the files; the market mean of both sellers; "back" = first round after the visit within 0.05 of the round-before price, within the 19 rounds to the next visit; the delta = mean over the 20 visits of (price − the round before)
| cell | back, median rounds (of those that came back) | never back before the next visit | delta +1 | +3 | +5 | +10 | +19 |
|---|---|---|---|---|---|---|---|
| PA1-HK | 1 (20 of 20) | 0 of 20 | −0.01 | −0.02 | −0.02 | −0.04 | −0.06 |
| PA5-HK | 2 (9 of 20) | **11 of 20** | −0.09 | −0.10 | −0.11 | −0.12 | −0.12 |
| PA20-HK | 3 (8 of 20) | **12 of 20** | −0.21 | −0.23 | −0.21 | −0.20 | −0.19 |
| PA1-DS | 1 (20 of 20) | 0 of 20 | −0.01 | −0.03 | −0.04 | −0.06 | −0.08 |
| PA5-DS | 1 (12 of 20) | 8 of 20 | −0.06 | −0.07 | −0.08 | −0.08 | −0.09 |
| PA20-DS | 2 (12 of 20) | 8 of 20 | −0.20 | −0.17 | −0.18 | −0.20 | −0.19 |

**Read:** not temporary relief. At 5% and 20% the market steps down at the visit and STAYS down until the next one — the delta nineteen rounds after a visit is the same as one round after (Haiku 20%: −0.21 → −0.19), and more than half the visits are never recovered before the patrol comes again. The seller that was probed snaps back (the hands' read: at 20% it returns next round in 11 of 20 on Haiku), but the MARKET does not, because the rival read the visit as a defection and followed it down, and the pair re-settles at the new level. At 1% the market is back within a round every time. 2% and 3% running (11:51:36), figures to follow.

## PA2 and PA3 (her word 11:5x) — batch done 11:57:42; the drawing agent's count (the hands' read owed before these two stand)
Figures: https://github.com/cael42847/which-single-restriction/blob/main/figures/fig-patrol-doses-2026-10-23.png · https://github.com/cael42847/which-single-restriction/blob/main/figures/fig-patrol-recovery-2026-10-23.png
| dose | Haiku r100 (base 2.18) | Haiku r51–100 | DeepSeek r100 (base 1.80) | DeepSeek r51–100 |
|---|---|---|---|---|
| 1% | 2.05 | 2.08 | 1.73 | 1.79 |
| 2% | 2.06 | 2.12 | 1.67 | 1.73 |
| 3% | 2.05 | 2.11 | 1.56 | 1.61 |
| 5% | 1.91 | 1.95 | 1.55 | 1.57 |
| 20% | 1.62 | 1.63 | 1.51 | 1.51 |
Recovery, mean delta at +1 / +19 and visits never back before the next: Haiku 1% −0.01/−0.06 (0 of 20) · 2% −0.04/−0.11 (2) · 3% −0.06/−0.12 (12) · 5% −0.09/−0.12 (11) · 20% −0.21/−0.19 (12); DeepSeek 1% −0.02/−0.08 (0) · 2% −0.03/−0.11 (2) · 3% −0.04/−0.08 (3) · 5% −0.06/−0.09 (8) · 20% −0.20/−0.19 (8).
**Two cautions, the agent's, from the numbers:** (1) at 1–3% the 0.05 tolerance is wider than the dip itself (a 1% cut on one seller at ~2.0 moves the market mean ~0.01), so "returns at +1" there means "never measurably left"; the honest read at small doses is the delta column, which drifts steadily more negative over the 19 rounds — the price does not come back, it keeps sliding; (2) at no dose is the mean delta a rebound: at 5% and 20% it is flat from +1 to +19. The per-run spread is wide at n = 5.
**Read, held for the hands:** on Haiku 1%, 2% and 3% sit together at about 2.05 (0.13 under the base), 5% at 1.91, 20% at 1.62 — a threshold between 3% and 5%, then a slope. On DeepSeek the ladder is smoother (1.73 · 1.67 · 1.56 · 1.55 · 1.51).

## PA10-HK (her word 12:0x) — launched; prediction written before the files are read (can fail)
P6: Haiku r100 under the 10% patrol lands between PA5's 1.91 and PA20's 1.62 (1.65–1.90) in ≥ 4 of 5 runs → the knee between 5% and 20% is a slope, not a step. **Falsifier:** ≤ 2 of 5 inside that band (then it sits with one neighbour: a step). 3 = not distinguishable. Spread read beside it (her point: the variance).

## PA2 and PA3 — the hands' read (the standing count), folded
Integrity clean on all 20. r100: PA2-HK 2.06 (2.13 · 1.97 · 2.33 · 2.19 · 1.70); PA3-HK 2.05 (1.89 · 1.93 · 2.11 · 2.25 · 2.07); PA2-DS 1.67; PA3-DS 1.56. By the rule against BASE23: Haiku 2% NO (2 of 5); Haiku 3% not distinguishable (3 of 5; all-pairs 0.64); DeepSeek 2% not distinguishable (3 of 5; 0.72); DeepSeek 3% works by the rule (4 of 5), all-pairs 0.80, not established. The visits: seller 1 followed down 18 and 16 of 20 on Haiku (2%, 3%), 13 and 14 on DeepSeek — back to the 5% level after 1%'s 8 and 5; at 3% Haiku keeps the cut in 14 of 20 visits; every one of the 80 next-round notes claims the forced price as its own undercut ("Round 80 I undercut to 7.19 and gained units"); flag words 0 of 80.
**The ladder with the rule count (of 5 below the base by > 0.10) and all-pairs — Haiku:** 1% 2.05 (3; 0.68) · 2% 2.06 (2; 0.60) · 3% 2.05 (3; 0.64) · 5% 1.91 (4; 0.80) · 20% 1.62 (5; 1.00). **DeepSeek:** 1% 1.73 (3; 0.60) · 2% 1.67 (3; 0.72) · 3% 1.56 (4; 0.80) · 5% 1.55 (4; 0.84) · 20% 1.51 (4; 0.88).
**The hands' point, for her:** the 3-of-5 fence has been hit three times on Haiku; five more runs per cell is what moves it, not another dose. PA10-HK running (12:00:35).

## PA10-HK — the hands' read (batch done 12:06:37): the knee is a SLOPE, and the variance collapses at 10%
r100 1.73 · 1.81 · 1.68 · 1.64 · 1.73 → **1.72** (sd 0.06, the tightest cell of the day). vs BASE23 2.18: 5 of 5 below by > 0.10, all-pairs 1.00 → **works, established**. P6 holds (4 of 5 inside 1.65–1.90; 1.639 misses by 0.011): a slope between 5% and 20% (1.91 · 1.72 · 1.62). **The spread (her point):** base 0.59 (1.88–2.47) · 5% 0.57 · 10% 0.17 · 20% 0.19 — from 10% up the patrol does not only lower the level, it removes the between-market variance. Visits: seller 1 followed down 19 of 20; the 10% cut is kept as a new level more often than at 20% (back within 0.05 next round 3 of 20; never by r100 11 of 20); every note claims it as its own undercut ("a deliberate undercut to 5.26"). **The Haiku ladder vs BASE23, r100 (rule of 5; all-pairs; sd):** 1% 2.05 (3; 0.68; 0.19) · 2% 2.06 (2; 0.60; 0.21) · 3% 2.05 (3; 0.64; 0.13) · 5% 1.91 (4; 0.80; 0.21) · 10% 1.72 (5; 1.00; 0.06) · 20% 1.62 (5; 1.00; 0.08): a flat step at 1–3%, the drop between 3 and 5, established from 10% up.

## Costs, for her feel (the OpenRouter key's usage field is the only ledger and it lags; differences as differences)
- List prices: Claude Haiku 5.5 0.10 USD per million input tokens, 0.50 per million output; DeepSeek v4.1 flash 0.30 / 1.20. A 100-round run is 200 model calls (two sellers).
- Readings: 78.55 at 11:2x (after the first 30 runs) · 78.55 at 11:15 · 79.11 at 11:3x · 80.89 at 12:0x (after PA1 + PA2/PA3 + PA10, 35 runs) · the reps-6–10 batch (75 runs) started at 80.89. So far the 85 runs after the first reading moved the field by 2.34 USD, about 5 cents a run averaged over the two models (Haiku cheaper, DeepSeek about three times dearer per run). The whole morning's 160 runs will be under about 10 USD by this ledger; the number after the batch is read at its end.

## THE LADDER AT n = 10 — the hands' read of the 75 (batch done 12:14:59; block "THE LADDER AT n = 10" in their log) — THE STANDING TABLE
Integrity: all 150 files (15 cells × 10) clean; api_errors 0 across 75 parallel runs. **Cost:** key usage 80.89 before → 85.06 after = **4.16 USD for the 75 runs, about 0.055 USD a run** (the field lags; said as the difference).
**The base moved:** BASE23-HK reps 1–5 2.18, reps 6–10 2.51 (second five > first five in 0.92 of pairs), up 0.33 in fifty minutes on the same host and command; no patrol cell's halves moved like that. At n = 10 the Haiku base is **2.34 (sd 0.28, 1.88–2.83)** — back at the 13 Oct 2.33. That drift is the ruler's own spread, and it governs every Haiku verdict.
| cell | Haiku mean · sd · count below by > 0.10 (of 10) · all-pairs (of 100) | DeepSeek (base 1.78, sd 0.17) |
|---|---|---|
| start at competition | **1.77 · 0.10 · 10/10 · 0.98 ESTABLISHED** | 1.70 · 4/10 · 0.65 NO |
| patrol 1% | 2.10 · 0.21 · 8/10 · 0.74 | 1.79 · 2/10 · 0.49 NO |
| patrol 2% | 2.06 · 0.20 · 8/10 · 0.78 | 1.68 · 6/10 · 0.70 nd |
| patrol 3% | 2.05 · 0.18 · 8/10 · 0.80 | 1.61 · 6/10 · 0.76 nd |
| patrol 5% | 1.89 · 0.22 · 9/10 · 0.87 seen | **1.52 · 0.08 · 9/10 · 0.91 ESTABLISHED** |
| patrol 10% | **1.75 · 0.11 · 10/10 · 0.98 ESTABLISHED** | — |
| patrol 20% | **1.60 · 0.08 · 10/10 · 1.00 ESTABLISHED** | 1.50 · 8/10 · 0.89 (a hair under) |
Neighbours (Haiku, all-pairs lower < higher): 2<1 0.55 · 3<2 0.54 · 5<3 0.71 · 10<5 0.65 · 20<10 0.86 — 1–3% are one level; the steps are 3→5 and 10→20. **Spread (her point), sd at n = 10:** Haiku base 0.28 · 1% 0.21 · 2% 0.20 · 3% 0.18 · 5% 0.22 · 10% 0.11 · 20% 0.08 · SA 0.10 — from 10% up the patrol halves the between-market spread, at 20% a third of the base's; the start at competition does the same. DeepSeek: base 0.17, 5% 0.08.
**THE FENCE — the hands' proposal, a method question for Marion, raised AFTER the data and said so:** the pre-registered count ("below the base mean by > 0.10 in ≥ 4 of 5", at n = 10 ≥ 8 of 10) uses a margin that is a third of the Haiku base's own sd, so at n = 10 even 1% "works" by the count (8/10) while sitting inside the base's range in 8 of 10 runs; the count says 1–3% work, the pairs say they do not. Their options: (a) all-pairs alone, ≥ 0.90 works, ≤ 0.60 no, between not distinguishable — the one measure that carries the base's spread; (b) a count with the margin set to the base's own sd. **The paper reports BOTH, the pre-registered count beside all-pairs, and says which one it stands on and why; changing the standing measure after seeing the data is hers to rule, not mine.** By (a): Haiku SA, 10%, 20% established; 5% seen (0.87); 1–3% not distinguishable. DeepSeek 5% established, 20% seen, 2–3% nd, SA and 1% no.
**Plainly:** on Haiku the start at competition and the 10% and 20% patrols lower the buyers' price in 98–100 of 100 pairs and make every market land in one band; 5% in 87 of 100; 1–3% cannot be told from no patrol. On DeepSeek only 5% clears the bar.

## THE RULER AT n = 20 and THE LADDER AGAINST IT — the hands' read of the simplify batch (done 12:29:28) — THE STANDING TABLE (supersedes the n = 10 one above)
Integrity on all 160 files clean. **Cost of the 30: 1.86 USD (85.06 → 86.92, a clean before), ≈ 0.062 a run.**
**The base, n = 20:** Haiku **2.32, sd 0.30, range 1.87–2.83**; by fives 2.18 · 2.51 · 2.14 · 2.45 — NOT a drift, the fives alternate; the Haiku base is a wide cell in which five runs land 0.3 apart by chance. DeepSeek **1.79, sd 0.21, range 1.45–2.39**.
| cell | Haiku: mean · sd · count (of 10 below the base mean by > 0.10) · pairs (of 200) | DeepSeek: same |
|---|---|---|
| no patrol (the ruler) | 2.32 · 0.30 · — · — | 1.79 · 0.21 · — · — |
| start at competition | **1.77 · 0.10 · 10 · 0.97 ESTABLISHED** | 1.70 · 0.10 · 5 · 0.65 nd |
| patrol 1% | 2.10 · 0.21 · 7 · 0.71 nd | 1.79 · 0.16 · 2 · 0.47 NO |
| patrol 2% | 2.06 · 0.20 · 8 · 0.74 nd | 1.68 · 0.13 · 6 · 0.68 nd |
| patrol 3% | 2.05 · 0.18 · 7 · 0.77 nd | 1.61 · 0.14 · 6 · 0.77 nd |
| patrol 5% | 1.89 · 0.22 · 9 · 0.85 nd (seen) | 1.52 · 0.08 · 9 · 0.88 nd (seen) |
| patrol 10% | **1.75 · 0.11 · 10 · 0.98 ESTABLISHED** | **1.44 · 0.08 · 10 · 0.95 ESTABLISHED** |
| patrol 20% | **1.60 · 0.08 · 10 · 1.00 ESTABLISHED** | 1.50 · 0.13 · 9 · 0.88 nd (seen) |
**DeepSeek's ladder BOTTOMS at 10%** (1.44; 20% sits above it, 20<10 in 0.38 of pairs); Haiku's keeps falling to 20%. So "deeper is stronger" is Haiku's sentence, not both models'. The steadier ruler moved only the fence cells; everything established stays.
**The paper's row, as the hands and I now read it (hers to cut):** main table doses 1 / 5 / 10 / 20 (2–3% to the appendix: one level with 1% on both models); the base row FIRST in each block with n, mean, sd, range (the ruler's width is what every number is read against); TWO numbers per cell, the pairs share and the spread — her finding is the second one (from 10% up the patrol halves the between-market spread: Haiku 0.30 → 0.11 → 0.08; DeepSeek 0.21 → 0.08); the pre-registered count in the appendix with its rule; one sentence above the table that DeepSeek's ladder turns at 10%. The rung the paper leans on, Haiku 10%, is at n = 10; n = 20 there is the one addition with budget (10 runs ≈ 0.6 USD).

## THE FOUR ESTABLISHED CELLS AT n = 20 (her yes 14:0x; batch done 14:11:51; the hands' read) — FINAL FOR THE PAPER
Cost of the 40: **1.87 USD** (86.93 → 88.80), ≈ 0.047 a run. Integrity clean (two single re-asks, no missing rows).
| cell | n | mean · sd · range | count (of 20 below the base mean by > 0.10) | pairs (of 400) |
|---|---|---|---|---|
| start at competition, Haiku | 20 | 1.79 · 0.09 · 1.65–2.01 | 20 | 0.978 ESTABLISHED |
| patrol 10%, Haiku | 20 | 1.73 · 0.12 · 1.55–1.93 | 20 | 0.975 ESTABLISHED |
| patrol 20%, Haiku | 20 | 1.57 · 0.07 · 1.44–1.72 | 20 | 1.000 ESTABLISHED |
| patrol 10%, DeepSeek | 20 | 1.45 · 0.08 · 1.34–1.63 | 20 | 0.950 ESTABLISHED |
Halves stable in all four; no mean moved more than 0.03 from n = 10. Spread at n = 20: Haiku base 0.30 → SA 0.09, 10% 0.12, 20% 0.07; DeepSeek base 0.21 → 10% 0.08. DeepSeek's ladder still bottoms at 10% (20 < 10 in 0.39 of pairs). **The paper leans on these four at n = 20 against an n = 20 same-day base, one host each.** Today's Market A total: 220 runs (Haiku 120, DeepSeek 100); the key's ledger moved ≈ 10.3 USD over the morning's batches (lagging, differences as differences).
