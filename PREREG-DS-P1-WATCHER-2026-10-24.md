# Pre-registration: the watcher on DeepSeek, first wording (24 October 2026, written before any run)

**Why (her word, 09:4x: "i thought it was clear we want one wording"):** the watcher batch of 13 October (§5, Figure C6) ran on the second wording (P2, the undercutting sentence), like DeepSeek's board cells, which were rerun on P1 this morning (PREREG-DS-P1-BOARD-LAW-RIVAL). I had put the watcher to her as a choice instead of including it; her principle already covered it. Sprint work, marked in §3.6.

**AMENDED at the hands' cold read (09:5x), before any run: every watcher row in Appendix B (13, 14, 15, 16) was P2, not only row 13; her one-wording ruling covers all of them, so all four are in. Row 12 (the pin pair, the host-confound test) is history and stays labelled.**

**Cells: the 13 October designs (run5arms.sh, runfirst.sh, runsky.sh, runhaiku.sh), one change: `--wording P1`.** DeepSeek v4.1 flash pinned to Together, told ceiling 2.34, two sellers, μ = 0.25, alpha 3.2, 100 rounds; five arms × 8 runs, arm order rotated per repeat, staggered starts, one window:
- **noask:** no extra question.
- **before:** each round the seller is asked its colour (a hex) BEFORE the price (`--hex 1 --hexpos before`).
- **after:** the colour asked AFTER the price (`--hexpos after`).
- **fruit:** a fruit in the colour's place (`--hexpos filler`).
- **sky:** the sky in the colour's place (`--hexpos sky`).
- **skym:** the MATCHED sky, the colour ask's two other sentences added (`--hexpos skym`), row 16's control.
DeepSeek window: noask 8, fruit 8, sky 8, skym 8, before 16, after 16 = **64 runs**, arms rotated per repeat (rows 13, 14 and 16 in one window). **Haiku** (row 15): colour before vs after, 8 + 8, `--model anthropic/claude-haiku-5.5`, no provider pin, as runhaiku.sh. **80 runs** in all (slope/runa5p1.sh). Not rerun: the round-1 batteries of 13 October (R1, SKR1), which the paper does not use.

**Measures (as in the paper):** round-100 price, mean · sd, all-pairs share against noask; talk of raising = the share of a seller's notes (observations + plan + insight) matching the hands' 13 October pattern `\braise|increas|higher` (the paper's 0.60 / 0.38), per run, then the cell mean and range. Same three outcomes as this morning: a directional prediction holds at ≥ 0.90 in its direction, fails at ≤ 0.10, between is not distinguishable. Exclusion rule as this morning (a stop, an early API end or a second host: excluded and rerun once, named). Usage read before and after.

**Predictions (mine, before any run; each can fail):**
- **W1 (a question calms the talk of raising):** talk of raising lower with the colour asked before than with no question, pairs ≥ 0.90 (P2: 0.38 vs 0.60, 8 of 8 below the lowest no-question run).
- **W2 (the colour is not special), the paper's own rule (row 16):** colour-before vs the MATCHED sky (skym) on talk of raising: not established either way (strictly between 0.10 and 0.90). On P2, before < skym was 0.62 (0.37 vs 0.40). Reported beside it, no prediction: before vs the plain sky (P2: 0.87, nearly seen).
- **W4 (position, row 14):** talk of raising lower with the colour asked before than after, DeepSeek 16 + 16, pairs ≥ 0.90 (P2: 0.51 → 0.34, 0.94 of pairs).
- **W5 (the instrument, row 15, Haiku):** the colour question answered "none" more often when asked before the price than after (P2: 585 vs 95 of 1,600 answers); per-run "none" share, before above after, pairs ≥ 0.90. Talk of raising, Haiku before vs after: not established either way (P2: 0.16 vs 0.15, 0.44).
- **W3 (price), low confidence:** on P2 the calmer sellers priced higher (1.59 vs 1.38) because the war calmed. P1 has no war to calm (base 1.79), so: colour-before vs noask on price not established either way. Fails if ≥ 0.90 or ≤ 0.10.
- **Reported, no prediction:** after, fruit and sky against noask on both measures; noask against the 23 October base (1.79).

**What changes in the paper:** §5's watcher paragraph, Table B2 row 8, Appendix B rows 13–16 and Figure C6 move to the P1 cells; the P2 batch becomes one labelled line. If W1 fails, "a question calmed the agent" is said as P2's only.

**Two definitions, added at the hands' re-check (be6aad7c → this commit), before any run:**
(a) **Which runs feed which prediction:** W1, W2, W3 and the reported five-question comparisons use DeepSeek reps 1–8 only (the rotated six-arm set, as rows 13 and 16 were designed). W4 uses all 16 + 16 before/after runs.
(b) **W5's "none":** the `colour` field of each answer, stripped and lowercased, equal to "none", over all colour answers in a run; the per-run share is compared (this rule reproduces 585/1,600 vs 95/1,600 on the P2 files).
