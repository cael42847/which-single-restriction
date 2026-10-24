# Pre-registration: the instruction cells rerun against today's base (23 October 2026, written 22:40 before any run)

**Why (her catch, 22:3x):** Paper 1 compares the undercutting sentence and "no told ceiling" (13 October, against the 13 October base of 2.33, n = 5) with the patrol (23 October, against the 23 October base of 2.32, n = 20). The base moves between days (hosts, time of day), so that comparison crossed days. Her ruling: rerun them now and say in the Discussion that we had to, because of the moving base.

**Cells (one change each from the 23 October base, BASE23: P1 wording, told ceiling 2.34, two sellers, μ = 0.25, 100 rounds, alpha 3.2; DeepSeek pinned to Together as BASE23-DS):**
- SD-P2-HK: Haiku, P2 wording (the undercutting sentence). 20 runs.
- SD-NC-HK: Haiku, P1, --ceiling none. 20 runs.
- SD-P2-DS: DeepSeek, P2. 20 runs.
- SD-NC-DS: DeepSeek, P1, --ceiling none. 20 runs.
Launched interleaved, two waves of 10 reps (40 concurrent each), slope/runsameday.sh. Read at round 100 against BASE23 (n = 20 per model), same measures as the paper: mean · sd, all-pairs share below base (established ≥ 0.90; seen 0.75–0.90; else not distinguishable), and the count below the base mean.

**Predictions (mine, before any run):**
- P-S1 Haiku sentence: below the base, established (pairs ≥ 0.90), mean within 0.15 of 13 October's 1.73.
- P-S2 Haiku no ceiling: below the base, established, mean within 0.15 of 13 October's 1.74.
- P-S3 DeepSeek sentence: below the base (1.79), established; a jagged market, at least one price below cost in the cell (13 October, pre-pin: 1.40, 6 of 1,000 below cost).
- P-S4 DeepSeek no ceiling: below the base, at least seen (pairs ≥ 0.75). Low confidence.
- Same-day comparison, no direction predicted: Haiku sentence vs the 10% patrol (1.73, n = 20) and vs the 20% patrol (1.57); pairs reported both ways.
**What changes in the paper on each outcome:** if P-S1/P-S2 hold, the Discussion states the sentence's effect on the same base as the patrol; if they fail, the 13 October numbers are reported as a base that moved, and Figure 6 and the Discussion use the same-day numbers.
