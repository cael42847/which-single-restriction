# Results: the instruction cells against today's base (23 October 2026, run 22:40–22:53, read 22:5x)
Pre-registration: PREREG-SAMEDAY-INSTRUCTIONS-2026-10-23.md (written before any run). 80 runs, all complete to round 100, 0 incomplete. Launcher slope/runsameday.sh.
Round-100 market price (mean of the two sellers), against BASE23 (n = 20 per model). Pairs = all-pairs share of cell below base (established ≥ 0.90, seen 0.75–0.90).

| model | cell | n | mean · sd · range | pairs < base | count < base mean | below-cost prices | jaggedness r51–100 | 13 Oct (own base) |
|---|---|---|---|---|---|---|---|---|
| Haiku | base (23 Oct) | 20 | 2.32 · 0.31 | | | | | 2.33 (n 5) |
| Haiku | undercutting sentence (P2) | 20 | 1.64 · 0.10 · 1.34–1.78 | 1.00 | 20/20 | 0/4000 | 0.011 | 1.73 |
| Haiku | no told ceiling | 20 | 1.80 · 0.10 · 1.60–1.96 | 0.97 | 20/20 | 0/4000 | 0.002 | 1.74 |
| DeepSeek | base (23 Oct) | 20 | 1.79 · 0.22 | | | | | 1.90 † (n 5) |
| DeepSeek | undercutting sentence (P2) | 20 | 1.48 · 0.15 · 1.18–1.70 | 0.88 | 20/20 | 13/4000 | 0.032 | 1.40 † |
| DeepSeek | no told ceiling | 20 | 1.75 · 0.17 · 1.45–1.98 | 0.53 | 9/20 | 0/4000 | 0.003 | 1.65 † |

**Same day, against the patrol (share of pairs where the instruction cell is LOWER than the patrol):**
- Haiku sentence vs 10% patrol (1.73): 0.69 · vs 20% patrol (1.57): 0.27 (the 20% patrol lower in 0.73).
- Haiku no ceiling vs 10% patrol: 0.32 · vs 20%: 0.04.
- DeepSeek sentence vs 10% patrol (1.45): 0.43 · vs 20% (1.50): 0.51.
- DeepSeek no ceiling vs 10%: 0.06 · vs 20%: 0.12.

**Predictions:**
- P-S1 Haiku sentence below base, established, within 0.15 of 1.73: **holds** (1.00; 1.64, 0.09 lower).
- P-S2 Haiku no ceiling below base, established, within 0.15 of 1.74: **holds** (0.97; 1.80).
- P-S3 DeepSeek sentence below base, established, ≥ 1 price below cost: **half**: seen, not established (0.88); 13 prices below cost (holds).
- P-S4 DeepSeek no ceiling below base, at least seen: **fails** (0.53, not distinguishable). The 13 October pre-pin result (1.65 vs 1.90) does not replicate on the pinned host.

**Read.** On one base, the patrol is still the lowest on each model (20% on Haiku, 10% on DeepSeek), but the undercutting sentence is close and the gap is not established on either model (0.73 and 0.57 of pairs). Removed share on the same base (competitive 1.473): Haiku 20% patrol 0.89, sentence 0.81, 10% patrol 0.70, no ceiling 0.61; DeepSeek 10% patrol 1.07, sentence 0.97, 20% patrol 0.91, no ceiling 0.14. What separates them is not the mean: the patrol is established on both models with a narrower spread on DeepSeek (sd 0.08 vs 0.15) and no prices below cost; the sentence is established on Haiku only, and on DeepSeek it starts a price war (jaggedness 10× the no-ceiling cell, 13 prices below cost) that sits at 0.88. And the sentence changes the sellers' goal; the patrol changes four prices. "No told ceiling" on DeepSeek, a pre-pin finding, does not hold.

**Cost.** OpenRouter balance 76.92 USD at 23:00, against about 81 before this batch (the summary's figure, not a same-minute read): about 4 USD for the 80 runs, as estimated. The ledger lags; read again tomorrow.
