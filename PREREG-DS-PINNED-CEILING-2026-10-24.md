# Pre-registration: DeepSeek's lower told ceiling, pinned (24 October 2026, written before any run)

**Why (her word 14:1x (before 14:17, the first commit of this file), "go"):** the only DeepSeek cell still pre-pin in Paper 1 is the 1.5 × told ceiling (13 October, n = 5, 1.73 against a pre-pin base of 1.90). One pinned batch with a same-window base removes the † concept from the paper's body. Sprint work, marked in Appendix B.

**Cells (same window, interleaved):** DeepSeek v4.1 flash pinned to Together, P1 wording, two sellers, μ = 0.25, alpha 3.2, 100 rounds.
- **DSB24 (base):** told ceiling 2.34 × cartel (the base command, as BASE23-DS). 10 runs.
- **DSC15 (lower ceiling):** told ceiling 1.5 × cartel (`--ceiling 1.5`, as DS-C1). 10 runs.
20 runs, slope/runceil24.sh. Usage read before and after.

**Measures:** round-100 price (the mean of the two sellers' prices in round 100, as the pre-pin 1.73 vs 1.90 was), mean · sd · range; all-pairs share against DSB24; outcomes as this morning: a directional prediction holds at ≥ 0.90, fails at ≤ 0.10, between is not distinguishable. Exclusion rule as this morning (a stop, an early API end or a second host: excluded and rerun once, named); the per-call providers and api_errors are read on every file before scoring, as this morning.

**Predictions (mine, before any run):**
- **C1 (the lower ceiling lowers the price):** DSC15 below DSB24, pairs ≥ 0.90. Low-to-moderate confidence: before the pin 1.73 vs 1.90 at n = 5; on Haiku 1.97 vs 2.33.
- **C2 (it lands near the cartel price), amended at the hands' cold read before any run:** comparative — DSC15's mean is closer to the cartel price 1.925 than DSB24's is. Reported beside it, with no prediction: each arm's distance from 1.925, so a reader sees whether a band would separate them. (The first wording, "within 0.15 of 1.925 or below it", was passed by the base arm too, so it tested nothing.)
- **Reported, no prediction:** DSB24 against the 23 October base (1.79, n = 20).

**What changes in the paper:** Table B2 / Figure 2's DeepSeek row 1 (1.5 ×) moves to the pinned cells; every † leaves the body (Methods keeps one sentence: every DeepSeek run was pinned to one host); the 13 October pre-pin cells stay as history rows in Appendix B.
