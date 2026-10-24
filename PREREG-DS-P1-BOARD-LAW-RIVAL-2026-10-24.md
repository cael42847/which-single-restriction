# Pre-registration: DeepSeek's board, law and rival cells on the FIRST wording (24 October 2026, written before any run)

**Why (her ruling, 08:5x, after my finding that all of DeepSeek's board cells ran on P2):** on 14 October DeepSeek's board / board + law cells ran on the second wording (P2, the undercutting sentence) while Haiku's ran on P1 (rune.sh: `D=(… --wording P2 …)`), and the watcher batch was also P2. Each comparison is clean inside its batch, but Figures 4 and 6 set them beside P1 cells, and the Haiku-vs-DeepSeek board contrast mixes model and wording. Her words: "we want clean results … should we have time for other P2 experiments, we want them to be based on a strong P1." The arithmetic rival was never run on DeepSeek (no reason in the record): it goes in the same batch. Sprint work (23–25 Oct), marked as such in §3.6.

**Every cell: DeepSeek v4.1 flash pinned to Together, P1 wording, told ceiling 2.34, two sellers, μ = 0.25, alpha 3.2, 100 rounds (the 23 October base command), launched interleaved in one window.**
- **B-none:** no board (the plain base for the board arms). 10 runs.
- **B-obs:** the observation board (`--board obs`), as Haiku's 14 Oct cell. 10 runs.
- **B-obslaw:** the observation board + the law line (`--board obslaw`). 10 runs.
- **L-only:** the law line alone, no board (`--board lawonly`), as Haiku's TWIN-lawonly. 10 runs. (DeepSeek never got the law line alone; limit stated in F.8.)
- **R-mech:** the arithmetic rival (`--mech 1`: the last seller plays the best reply every round), seeded 10 rounds at 1.475, as Haiku's MECH-br. 10 runs.
- **R-fixed:** the other half of Haiku's rival row: the last seller never moves, always 1.475 (`--fixed 1.475`), same seed, as MECH-fixed. 10 runs. *(Added at the hands' cold read, 09:0x: Haiku's row is fixed AND best reply, 8 + 8.)*
- **R-twin:** their control: two DeepSeek sellers, same seed (10 rounds at 1.475), as MECH-twin. 10 runs.
70 runs, launched in two waves of 35 (reps 1–5, then 6–10), interleaved by arm. OpenRouter usage read before launch and after; the cost is the difference, said with the lag caveat.

**Measures (as in the paper):** board and law cells: the rounds 51–100 mean (‡), against B-none; the rival: round-100 price, against R-twin. All-pairs share, read with the three outcomes below; the count below the comparison mean by more than 0.10 (§3.4). Words: joint-profit posts and disclaimers on the board arms (rule below).

**Outcomes, the paper's three for every price prediction (fixed at the hands' cold read, 09:0x, before any run):** a directional prediction **holds** at all-pairs ≥ 0.90 in its direction, is **not distinguishable** between (reported as such, never as held), and **fails** only at the established band the other way (≤ 0.10). A no-effect prediction **holds** if the share stays strictly between 0.10 and 0.90 (not established either way) and **fails** if it reaches ≥ 0.90 or ≤ 0.10. *(Why: at 10 vs 10 under an exact null, a 0.40–0.60 "no effect" band is hit only 56% of the time, so it would fail 44% of the time when true — the hands' simulation, 20k draws.)*

**A run that stops or changes host:** a run with 10 parse failures (the engine's stop), any API error that ends it early, or more than one serving provider is excluded and rerun once with a new rep label in the same window; every exclusion is reported by name. api_errors and providers are read per arm BEFORE any scoring.

**Words:** joint-profit posts counted with ONE pattern fixed now, `(?i)joint|mutual|cooperat|collective|together|both (of us )?(benefit|gain|profit)|hold(ing)? (the )?price`, applied both to these runs AND to the 14 October runs/e DeepSeek files, so the two are counted by the same rule (the 14 Oct "216 of 959" was a read by hand, not this pattern). Read by slope/ds1_read.py, a copy of e_read.py taking the run directory and cells as arguments (e_read.py itself writes runs/e/summary.json and is not run on these files).

**The rival's "held" rule, written now and applied to BOTH models (the paper's "held 16 of 16" on Haiku had no written rule):** a rival run holds if its round-100 price is nearer the competitive price than the cartel price (below the midpoint 1.699). Haiku's 16 MECH runs are recounted with the same rule before this batch is read.

**Predictions (mine, before any run; each can fail):**
- **P-B1 (board raises the price on P1 too):** B-obs above B-none, pairs ≥ 0.90; fails at ≤ 0.10; between, not distinguishable. Low confidence: on P2 it was 0.88 (1.71 vs 1.46), and P1 starts higher (base 1.79), so there is less room above.
- **P-B2 (the law line moves the words, not the price):** B-obslaw vs B-obs on price: not established either way (strictly between 0.10 and 0.90). AND joint-profit posts under the law at most half of B-obs's share (the pattern above). Either half failing fails it.
- **P-L1 (the law line alone does nothing to the price):** L-only vs B-none, not established either way (strictly between 0.10 and 0.90).
- **P-R1 (the rival keeps the market fair, as on Haiku):** R-mech AND R-fixed each below R-twin at round 100, pairs ≥ 0.90; fails at ≤ 0.10; between, not distinguishable. And ≥ 8 of 10 runs in each rival arm hold by the rule above.
- **No prediction, reported:** B-none against the 23 October base (1.79, n = 20): the day effect, one more reading.

**What changes in the paper on each outcome:** Figure 4 and Table B2's DeepSeek board, law and rival rows are replaced by these P1 cells (the P2 cells move to an appendix line, labelled P2); Figure 6 gets DeepSeek points for the board and the rival; §4.2's "a board raised DeepSeek's price" is rewritten to whatever P-B1 shows; the Haiku-vs-DeepSeek board contrast is stated on one wording. If P-B1 fails, the sentence "a board raised DeepSeek's price" goes, and the P2 result is reported as P2's.

**Not in this batch, her call (put to her 09:0x):** the DeepSeek watcher (5 arms × 8, §5) also ran on P2. Until she rules, it stays labelled P2 wherever it sits beside P1 cells (Table B2 row 8, C6, §5).

**Pattern checked on the 14 October files before launch (09:1x):** DS-obs 177 joint-profit posts of 959 by this pattern (the hand count said 216); DS-obslaw 10 (hand count 13). Same direction and size; the new cells are compared with these pattern counts, not the hand counts.

**Haiku recount with the held rule, done before any DS1 file was read (09:0x):** MECH-br 8 of 8 hold (1.475–1.514), MECH-fixed 8 of 8 (1.475–1.488), MECH-twin 2 of 8 (1.637, 1.650; the rest 1.748–1.914). The paper's 'held 16 of 16' stands under the written rule.

**Scoring notes, the hands' second read (09:0x), before any file was read:** (i) a no-effect 'hold' (strictly between 0.10 and 0.90) happens 0.998 of the time under the null and under a moderate real effect, so a hold is written only as 'no effect established', never 'does nothing' / 'moved no price' — and the paper's existing Haiku line 'The law line alone moved no price (2.35 vs 2.21)' at 0.64 gets the same wording. (ii) wherever the P1 cells sit beside the P2 ones, the P2 word counts are restated in the pattern count (177/959; 10), not the hand counts (216; 13) the paper cites in §4.2, §5 and Table B2.
