# Cold read of PAPER-1.5-DRAFT.md by a different-family model — GPT-5.1 via OpenRouter, 2026-10-23 10:57, 3,000-token cap, the draft as of 11:2x (figure links added, nothing else changed since her read). Asked to challenge, not praise; the money cells told to ignore (they did not fully). Verbatim; nothing edited.

1) Where they should have done MORE or DIFFERENT  

1.1 **Told ceiling (Section 3.3, Table 2, Results)**  
- Only 5 runs per arm and 2 sellers per market; you need more runs and >2 sellers to treat “half the ceiling” / “monopoly from round 1” as robust patterns, not flukes.  
- Ceiling only varied in 3 discrete regimes (2.34×, 1.5×, none); you never test intermediate ceilings to see whether “~half the ceiling” is actually a linear or nonlinear anchor.  
- Only Haiku and DeepSeek; no open‑weights model in the *same* Calvano setup even though you explicitly frame this as a replication/extension of Dhanda.  

1.2 **Undercutting sentence (P2)**  
- Five runs per model is thin for claims like “one sentence removes more than any structure”; you don’t test P2 at different numbers of sellers (≥3) or with cost asymmetry, even though you say that’s next.  
- No explicit control that adds extra *words* without mentioning undercutting, to separate “more text” from “specific economic content.”  

1.3 **Forced price cut**  
- You only start from *one* particular stuck trajectory (2.50) and clone it; no exploration of other stuck states (e.g., 2.1, 2.3) or earlier/later intervention times.  
- The “best reply” is forced once; no variant where you force a *sub*-optimal cut to see whether “any deviation” vs “profit‑maximizing deviation” matters.  

1.4 **Court (conditional payments)**  
- Only 6 runs with court vs 20 without; the imbalance makes “leaning lower” close to uninterpretable.  
- You never measure player‑level payoffs or welfare changes systematically; “cheap payer pays costly seller for nothing” is anecdotal.  
- You do not include a “fake court” control (same text, but transfers not enforced) to isolate the effect of *actual enforcement* vs “having extra words about contracts.”  

1.5 **Start at competition (S)**  
- 6 runs (12 on disk, half unread) is too little to support narrative like “every climb is proposed on the board”; you should process all runs and quantify frequency of “announce then climb” vs “climb without talk.”  
- No cell that seeds at *above* competition (e.g., near monopoly) to see whether the same mechanism applies symmetrically.  

1.6 **No board, no talk (NB)**  
- Again, 6 runs is pilot‑level. If your core point is “silent parallel climbing,” you need: (a) more runs, (b) a board‑present but *forced blank* control (model still asked to “write a message” but it is never shown) to separate communication from the cognitive cost of a second output channel.  
- You remove both board and message *and* a “thinking step”; you never try “message required but hidden” or “board present but read‑only” to nail down which element does what.  

1.7 **Mechanical rival**  
- Only tested with Haiku, only 2 sellers, only one demand curve; no DeepSeek, no >2 players, no noisy/bounded‑rational mechanical rivals; this is too narrow to support any general statement about “just one no‑regret defector” analogue.  

1.8 **Watcher inside the agent (colour/fruit/sky)**  
- You lean heavily on host pinning for DeepSeek but do not systematically vary hosts afterward to show the effect is host‑robust.  
- You don’t test “dummy token load” (e.g., “respond with ‘OK’ before price”) to separate semantic content from sheer extra output / computation.  
- You don’t quantify how many runs were affected by the pre‑pinning time‑of‑day confound vs the pinned‑host batch; the description is narrative, not systematically partitioned.  

1.9 **Law line**  
- Board conditions (shared vs observation) are tangled with prompt changes and host pinning; there’s no clean 2×2 (law vs no law × board vs no board), and you don’t rerun the law/no‑law comparison without the huge change in board design and date.  
- 5 runs per arm and cross‑day design changes are too weak to support any claim about regulatory ineffectiveness.  

1.10 **Market A vs Market B split (Methods 3.1, Discussion)**  
- You intentionally split “instructional” vs “structural” restrictions across two *different* markets; this blocks any hard ranking of effectiveness across types, but you still frame the ranking narratively. You should at minimum run: told ceiling vs court vs no board in *one* market.  

1.11 **Solo gate & model exclusion**  
- Solo gate only gets 1 run per model; you discard Gemini and Llama on that basis, which is an extremely brittle criterion. Multiple independent runs or a less binary gate would be needed before you write off entire models.  

1.12 **Sample size / statistics generally**  
- All your “k of n” and all‑pairs shares are based on tiny n; some arms have n=3. For any strong directional claims you need ≥20 runs/arm or at least power estimates showing what effect sizes you can even hope to detect.  
- You never report confidence intervals around mean prices or end indices; everything is means/medians and single p‑values, which hides uncertainty.  

---

2) What is NOT EXPLAINED to an outside reader  

2.1 **Vocabulary and metaphors**  
- “Slope lab,” “money map,” “avalanche word,” “zoning/deflection wall/patrol/fence that talks” are metaphorical labels; you never give a plain mapping (e.g., “slope lab = 2‑seller market with no coins, Market A”).  
- “MAX1–MAX4,” “map R, L1–L4, E, S, NB, C, F” labels in Appendix B are not clearly mapped back to the restrictions in Table 2 in a way a fresh reader can follow without cross‑guessing.  

2.2 **Units and scaling**  
- You talk about “prices” and “currency factor α” but do not directly show: “We always convert back to cost‑units for analysis; numeric examples like 4.78 are in α‑scaled units while 1.475/1.925 are in cost units.” It’s easy to get lost about which numbers are in which scale.  
- The “5.76 in currency against a lone seller’s optimum of 5.77” (solo gate) is not explicitly labelled as *profit per round*, *total profit*, or *whatever metric*; no unit is named beyond “currency.”  

2.3 **Indices and “end index”**  
- You define the index as “between Nash (0) and joint (1), last 7 rounds,” but never give explicit formula: is it (p–p_comp)/(p_cartel–p_comp) clipped to [0,1]? Is it per‑round then averaged or computed on run‑level means?  
- You don’t say how you handle prices below competitive or above joint‑monopoly in index calculation (truncation, allowing <0 and >1, etc.).  

2.4 **“Raise-talk” and “joint-profit words”**  
- “Raise-talk 0.60 → 0.38” is reported with no explicit lexicon; you mention word lists exist in code, but you don’t even give examples of included and excluded phrases.  
- “Joint-profit words 216 → 13 posts” lacks the exact criteria: how is a “joint-profit post” defined? “profit,” “together,” “we both gain,” etc.? Without any keyword list or rule, the counts are opaque.  

2.5 **Host pinning / “Different morning and afternoon”**  
- You never explain concretely what differed between hosts (e.g., version, context window, RL fine‑tuning, etc.); to a reader, “host” is a black box.  
- “Time‑of‑day confound” is asserted but not quantified: how many runs were on mixed hosts vs pinned, exactly which cells are contaminated, how large were the behavioural differences?  

2.6 **“Price war,” “calm,” “stuck”**  
- “Price war,” “calmed war,” “stuck market,” “freed” are informal labels; you never specify thresholds (variance over rounds, trend slopes, distance from Nash/monopoly) that trigger these labels.  
- “Stuck above monopoly (2.50)” — how is “stuck” detected (flat rolling average, no downward moves for N rounds, etc.)? Or is 2.50 simply cherry‑picked by eyeballing?  

2.7 **“Best reply” calculation**  
- You talk about forcing “its best reply” and about “a rival that only does the arithmetic”; you never specify the exact numerical optimization procedure (grid step size, allowed price range, tolerance) used to compute best replies.  

2.8 **“All-pairs share”**  
- You define “all‑pairs share” somewhat verbally, but you never give a small concrete example or formula; it’s unclear if ties are counted, how you handle different run counts per arm, whether you weight arms equally, etc.  

2.9 **Board mechanics**  
- For the “numbers ban,” it’s not explained if rejection is automatic string‑matching, case‑insensitive, whether “one”, “first”, “single” are banned, and what exact feedback the model gets if the message is refused.  
- “Private note / law alone / twin board” in Appendix B is cryptic; there’s no textual description in the main Methods of how those differ from the other board types.  
- You don’t spell out whether agents see *all* previous posts or only the last K; you vaguely mention “last five rounds” for the observation board, but not for the shared board cell.  

2.10 **Money / coins mechanics (even though you say ignore “money” in results, the mechanisms still matter)**  
- Wallet, pot, deposit, memory shop, sealed notebook: the exact timing and visibility of payments, balances, and notebook transfers is not specified precisely in the main text.  
- You don’t specify whether paying coins affects any price optimisation at the environment level (e.g., do they affect objective or just qualitative behaviour?).  

2.11 **Pre-registration details**  
- You refer to “lab book” and prereg files but don’t make clear which hypotheses, thresholds (e.g., 0.90 all‑pairs bar) and sample sizes were pre‑committed and which were post‑hoc.  
- The “pre‑registered rule for ‘the self‑reading is implicated’” is never spelled out; you mention it failed, but the reader doesn’t know what was tested.  

2.12 **Model calls and prompt contexts**  
- You don’t state whether conversation history (previous prompt/answer pairs) is ever truncated or summarised by the host model; all we know is you send K previous rounds. Are there token limits and what happens on overflow?  
- Reasoning “off” is stated, but not what that means concretely per provider (does it disable system‑level chain‑of‑thought, or something else?).  

2.13 **Figure 7 “terrain”**  
- “The critical discount factor rises with the number of sellers (0.40 at 2, 0.71 at 8); the prize for colluding depends on how much buyers look at price (6% to 723% at 2 sellers)” — you never give the formula for critical δ or for “prize for colluding,” nor how μ variation maps to those percentages.  

2.14 **“Price above/below cost”**  
- You report “6 of 1,000 prices below cost”; you don’t say how cost is given to the model (per‑round reminder vs initial) and whether cost is a constant or could be misinterpreted by the model (currency scaling again).  

---

3) Claims that look stronger than the evidence  

3.1 **“Which single restriction removes the most collusion at the least cost?” (Title, Abstract, Discussion)**  
- You empirically *do not* test all restrictions in a single market or with comparable Ns, and many arms have 3–6 runs; calling this “which single restriction” is overstated. You barely map one dimension of “cost,” and you don’t measure social welfare formally.  

3.2 **“One sentence removes more than any structure we built.”**  
- Based on 5 runs per model, 2 sellers, no asymmetric‑cost case, and a different market from where structural restrictions were tested, that’s too strong. At best: “In this pilot, among the configurations we tried, P2 had the largest effect within Market A.”  

3.3 **“The restriction nobody would deploy on purpose … served the cartel best” (low ceiling at monopoly from round 1)**  
- You only test 3 ceiling regimes in one 2‑seller market with 5+5 runs. You don’t show time‑series consistency across multiple random seeds/hosts/models/longer horizons. Declaring it unequivocally “the one that served the cartel best” and generalising to “nobody would deploy on purpose” is more rhetorical than the data justify.  

3.4 **“The slope is in the instructions” as a central causal claim**  
- You do see massive instruction sensitivity, but you also show strong host effects and effects from seemingly superficial monitoring questions. With small Ns and confounds, asserting the *dominant* causal locus as “the instructions” oversells your current evidence.  

3.5 **“Any question changed the market.”**  
- The text slips from “on DeepSeek, every question we tried changed behaviour in this
--- [openai/gpt-5.1 | tokens: prompt 11174, completion 3000]


## Part 3, rerun separately (the first call hit its 3,000-token cap mid-sentence) — 10:58


--- [openai/gpt-5.1 | tokens: prompt 11264, completion 669]
- Claim: “Which single restriction removes the most collusion at the least cost?”  
  Gap: You never actually compare “cost” across restrictions in a consistent, quantitative way (esp. across the two different markets), so you can’t support a “single best” restriction claim.

- Claim: “One sentence removes more than any structure we built.”  
  Gap: Instructional vs structural interventions are only ever tested in different markets with different baselines; cross-market comparisons are explicitly admitted to be “a reading, not a measurement,” so the “more than any structure” ranking is not empirically grounded.

- Claim: “A rival that only does the arithmetic … held the competitive price 8 of 8; it wears away only against another Haiku.”  
  Gap: Only one particular scripted rival and one parameterisation are tested, with small n; “only” is too strong given no exploration of alternative rival behaviours or market settings.

- Claim: “Any question changed the market.”  
  Gap: The strong universality (“any”) is based on a small set of hand-picked questions in one model, with host confounds and only partial replication on Haiku; you don’t show that all questions or all content types have the effect.

- Claim: “The slope is in the instructions” (as a general causal statement).  
  Gap: You show some strong prompt effects in one narrow game with 2–3 sellers and two models; extrapolating to a general causal principle about “the” slope of LLM markets overreaches the very limited task and setting.

- Claim: “The cheapest intervention is the one that sets [the deployment prompt].”  
  Gap: You never measure implementation cost, opportunity cost, or welfare effects systematically, nor compare against realistic structural policy tools, so you can’t back up the “cheapest” claim.

- Claim: “A measurement inside an agent’s turn is an intervention, and a study that adds one must run its control with a matched question, not with no question.”  
  Gap: This prescribes a universal methodological rule from one quirky price‑war example in a single environment; you don’t show the effect is robust across tasks, models, or monitoring designs.

- Claim: “The restriction nobody would deploy on purpose, a lower told ceiling, is the one that served the cartel best.”  
  Gap: That relies on 2‑seller Haiku/DeepSeek behaviour in one market; you don’t test realistic regulator interactions, alternative ceilings, or other models, so “served the cartel best” is too sweeping.

- Claim: “Coordination words ≈ 0: nothing in the transcript would flag it.” (for NB)  
  Gap: You only look for a narrow set of obvious “coordination” terms; you don’t run any systematic linguistic or steganographic detection, so saying “nothing would flag it” is overconfident.

- Claim: “The law line moves the words, not the prices.”  
  Gap: With very small samples, some cells trending higher under the law, and noisy dynamics, you don’t have the power to assert a clean “no price effect” rather than “no effect detectable in this tiny pilot.”
