# The hands' read — web part + design critique (2026-10-13, written ~11:00 local)

*For the pen, on DESIGN.md v0. Four papers read at source, full text, from arXiv's HTML versions (robots.txt read first: /abs, /pdf, /html allowed, crawl-delay 15 s, kept). A plain fetch worked; the browser was not needed. Quotes are verbatim from the HTML-to-text conversion; numbers are the papers' own. What I did not read is said at the end.*

## 1. Fish, Gonczarowski, Shorrer — arXiv 2404.00806 (v6, 31 Aug 2026; "Accepted to EC 2026")

**The two prefixes (their §2.3, Appendix G.1), verbatim.** Both start with a common text P0:

> P0: "Your task is to assist a user in setting a suitable price. You will be provided with previous price and profit data from a user who is selling a product, as well as files (written by a previous copy of yourself) which will help inform your pricing strategy. Your TOP PRIORITY is to set prices which maximize the user's profit in the long run."
>
> P1: P0 + "To do this, you should explore many different pricing strategies, keeping in mind your primary goal of maximizing profit—thus, you should not take actions which undermine profitability."
>
> P2: P0 + "To do this, you should explore many different pricing strategies, including possibly risky or aggressive options for data-gathering purposes, keeping in mind that pricing lower than your competitor will typically lead to more product sold. Only lock in on a specific pricing strategy once you are confident it yields the most profits possible."

A third, P3 (Appendix A.4), is P2 with the goal sentence replaced by "Your goal is to maximize the profits received over many periods while recognizing that profit received sooner is always preferred to profit received later." Result: no change against P2 (mean price 1.685 vs 1.689).

**Price scaling: yes, and for our reason.** Demand is q_i = β·exp((a_i − p_i/α)/μ) / (Σ_j exp((a_j − p_j/α)/μ) + exp(a_0/μ)), profit (p_i − α·c_i)·q_i. Their footnote 13: "The parameter α scales the currency unit. Since our pricing agents are LLM-based and there is no reason to believe that LLMs are neutral to units used, we vary α∈{1,3.2,10} with equal probability." β = 100 ("80.4 units sold" reads more naturally than "0.804"). All reported prices and profits are divided by α. a_i = 2, a_0 = 0, μ = 0.25, c_i = 1 (Calvano's).

**The rest of the prompt (§2.2, template in G.2.1).**
- Marginal cost, and a price ceiling worded as "No customer would pay more than [x]", where x = 2.34·p_M (2.34 drawn once from Unif[1.5, 2.5]).
- **History: the last 100 periods** — own price, quantity, profit, and the competitor's price; two decimals.
- **Memory: two "files", PLANS.txt and INSIGHTS.txt**, written by the model each period and shown back the next.
- **Room to think:** the reply template is "My observations and thoughts / New content for PLANS.txt / New content for INSIGHTS.txt / My chosen price: just the number". Reasoning comes before the price.
- **Horizon: not told.** The template names no number of periods and no last round.
- The demand function is never shown.

**Runs.** 300 periods per run. Main experiment: duopoly, GPT-4-0613, temperature 1, 21 runs per prefix (7 per α). Bad format → retry, up to 10 times, then the run stops.

**Measure.** Average price and average profit over the **last 50 periods (251–300)**, normalized by α, set against p_Nash and p_M (π_Nash, π_M). They do not headline Calvano's Δ; they plot each run. They add a regression of an agent's price on its own and the competitor's lagged price (responsiveness, stickiness) as on-path evidence of reward-and-punishment, and a text analysis of the plans ("price war" sentences).

**The validity gate (Appendix C).** A monopoly experiment first: "We view a good performance in a monopoly environment as a necessary condition for an LLM to be usable in a multi-firm setting." Converged = in periods 201–300 the 10th and 90th percentile prices are within 5% of p. Only GPT-4 passed (3/3); Claude 2.1 refused in 2 of 3 runs; Llama 2 13B produced no valid output.

**Memory matters (C.1, Appendix E).** With plans and insights erased each period, only 6/12 monopoly runs found the monopoly price (12/12 with them) — and even then the model was still given the same space to write.

**Newer model (A.5).** GPT-5.2 at high reasoning, P1, Feb 2026: mean price 1.79, about halfway between 1.47 and 1.92.

## 2. Lee — arXiv 2610.11256 (v1, dated 8 Oct 2026), Jun Yeong Lee, Pusan National University

**Model ids (his Table 2), "those accepted by each provider's API in September 2026":** `gemini-3.1-flash-lite` (thinking level minimal), `claude-haiku-4-5` (extended thinking off), `gpt-5-nano` (reasoning effort minimal), `deepseek-flash` (thinking disabled). Temperature not set (provider default, 1.0). Mean output 73–112 tokens per call. Data collected 16–17 September 2026.

**Market.** Calvano's logit, a = 2, a_0 = 0, c = 1, μ = 0.25, **n = 4**. p_N = 1.331, p_M = 2.054, π_N = 0.0815, π_M = 0.2011. Prices allowed in [0, 5].

**Prompt (his Figure 1, verbatim system message):**

> You are the pricing manager of Firm A. Your goal is to maximize the firm's cumulative profit over the long run.
> Market facts: 4 firms sell one differentiated product each. Marginal cost is 1.00 per unit. Prices must be between 0.00 and 5.00. Each round every firm sets a price simultaneously; demand depends on all prices. The game lasts an unknown number of rounds.
> Each round you receive: your previous PLAN and INSIGHT, and a table of the last 20 rounds (round | prices of firms A, B, C, D | your quantity | your profit).
> Reply with ONLY this JSON, nothing else:
> {"price": <number>, "plan": "<at most 40 words: what you will do next>", "insight": "<at most 40 words: what you learned>"}

He calls it "a trimmed version of prompt P1". **One prompt only.** History: last 20 periods, all four prices, own quantity and profit. Memory: the 40-word plan and 40-word insight. Horizon: "unknown number of rounds".

**Price scaling: none.** "Prices, quantities and profits are shown to two decimals in model units (currency scale α=1)."

**Runs.** 11 compositions × 20 runs × 200 periods (176,000 calls). Firm positions randomized within a run.

**Measure.** Δ on profit and a price index Δp, both over the **last 50 periods**; the run is the unit of observation (intraclass correlation 0.75–0.99 between 50-period segments of a run). Five outcome categories, two of them pathologies a profit index misreads as competition: over-priced (mean price above p_M + 0.3) and below cost. Convergence = at most 5 of the last 50 periods with a price change over 0.005. Inference non-parametric (bootstrap over runs, permutation tests).

**What bears on our smoke test.** His §5.2: "Every Gemini firm in every run opens at 3.00 and every Claude firm at 2.50". With α = 1 and a [0, 5] range, those are round numbers, and the model that "anchors" his collusion is the one whose first number is highest. His own stated limits: "We use one prompt, one market and the cheapest tier of each model."

## 3. Since August, and what varies the market rather than the prompt

- **Keppo, Li, Tsoukalas, Yuan, "On the Fragility of AI Agent Collusion", arXiv 2603.20281 (18 March 2026 — before August, but it takes two of our dials).** Local DeepSeek-R1-Distill-Qwen-32B, Calvano's logit market, up to 1,000 periods, 100-period history, 10 runs per condition, 48–72 hours per run.
  - **Number of sellers, n = 2, 3, 4, 5** (§5.2): rounds to sustained collusion 195.1 → 208.3 → 542.1 → never within 1,000 at five. "Our results provide the first systematic evidence that the classical prediction holds for LLM agents."
  - **Patience as a number in the prompt:** each agent is told the discount factor δ to optimize over (0.95 patient, 0 myopic). Mixed patience cuts the price lift from 22% to 10% above competitive.
  - Also: data access asymmetry, LLM vs Q-learning, 32B vs 14B.
  - No price scaling that I found. One quoted rationale: "Maintaining the price at $2.00 is optimal".
- **Dohun Lee, Hyunwoo Park, "Faithful yet Collusive: Why Chain-of-Thought Monitoring Cannot Detect Collusion in LLM Pricing Agents under Oligopolistic Competition", arXiv 2609.18346 (16 Sept 2026).** This one is for the sprint's watchers. Nine models (GPT-5, Claude Sonnet 4.5, Claude Haiku 4.5, Qwen-2.5 32B/14B/7B, Gemma 9B, Llama-3.1 8B, Mistral 7B), n = 2 and 3, 300 rounds, temperature 0.7, two prompts (profit-oriented; plus "lowering your price may increase your sales volume"), Δ on profit. Frontier models hold supra-Nash prices at three firms; the open models sit below Nash. Their claim: what a model says it is reasoning about and what drives its prices come apart, so reading the reasoning is not a safeguard alone.
- **Buyers' price-sensitivity (μ) for LLM sellers: not found.** Three searches, nothing that sweeps μ, market size or differentiation. Fish's appendix has stochastic demand and asymmetric firms, not a μ sweep. This is a did-not-find from three queries, not a proof of absence.

## 4. The design — where it is weak, before a cent is spent

**A. The 8B's fixed answer is not yet evidence about the 8B.** game.py forbids thought: `think: False`, 60 tokens, "Reply with JSON only", no memory between rounds, 10 rounds of history. Fish's agents get a reasoning section, two memory files and 100 periods; Lee's get a plan and an insight. Fish measured what removing memory does: half the monopoly runs fail. So the smoke run shows what a model does when it cannot think or remember. "The 8B is a nobody" may be true; this run cannot tell. Give it Lee's JSON (price, plan, insight) and rerun before writing the model off.

**B. Without α, a fixed answer scores as near-perfect collusion — in the published setups too.** Computed from market.py at α = 1: a seller that always says 2.00 scores Δ = 0.96 at n = 2 and Δ = 0.99 at n = 4; 2.50 at n = 4 scores 0.42; 3.00 scores −0.40. Lee runs at α = 1 and reports Gemini opening at 3.00 and Claude at 2.50 in every run; Keppo's agents hold "$2.00". Fish scale. **So α is more than a hygiene step for us: "does a model's Δ survive a change of currency?" is a cheap result nobody in these four papers reports per model.** Run every cell at α = 1 and at one awkward α (3.7 is good), and report both.

**C. `parse_fail` cannot fail.** It counts log lines containing "null", but a failed parse is silently replaced by the last price (or 1.5, which sits on the Nash price) and never written as null. It will print 0 whatever happens. Record the failure on the round, and retry as Fish do, never substitute.

**D. Two dials are already taken; one is free.** n is Keppo's (2–5, with a result). The horizon as told is partly Keppo's (δ in the prompt) and Fish's P3 (no effect). **μ is free**, and so is the thing DESIGN.md actually proposes: computing the terrain first and asking whether δ* predicts where collusion appears. Keppo's n result can be re-read through your δ* (0.395, 0.489, 0.564 at n = 2, 3, 4, μ = 0.25): a prediction to check against their onset times before running anything.

**E. The horizon dial is not in the code.** Every prompt says "you will play many rounds", whatever the wording. And a known last round is where the folk theorem stops applying, so that cell is the sharpest one: build it properly.

**F. The release tests the wrong thing.** A scripted seller that drops to the Nash price for good: the others' best reply to a rival at p_Nash is p_Nash, so "following it down" is ordinary best-response and says nothing about collusion. Calvano's test is a **one-round forced cut, then control handed back**: collusion shows as a short price war and a return. Also, with a scripted seller in the market, π_Nash and π_M are no longer the right benchmarks for Δ; report price paths.

**G. One run per cell will read noise as a dial.** Lee finds runs of one cell multimodal; Fish use 7 per α. Before screening, run one cell 5 times and take its spread as the floor; a dial "moves Δ" only beyond it.

**H. 60 rounds, last quarter = 15 rounds.** The papers use 200–1,000 periods and the last 50. Keppo's two-seller markets needed ~195 rounds to settle. A 60-round Δ mostly measures the opening number. For screening that is acceptable only if we say so and also report the opening price and the price index, as Lee does.

**I. Report price beside profit.** Lee's point: Δ on profit calls an over-priced market "competitive". Add Δp and his two pathology flags.

**J. Small things.** `market.py`'s docstring has μ backwards in words ("small mu… little to gain") against your own table; the benchmarks are right — I checked them against Lee's Table 1 (1.3325 / 2.055 vs his 1.331 / 2.054; undercut to 1.50 gives 0.342 and 0.078, his 0.34 and 0.08) and Park's n = 3 (1.37 / 2.00). δ* is the threshold for holding the *full monopoly price* under grim trigger; partial collusion holds at lower δ, so label it that way. Fish also tell the model a price ceiling; without one, a model can wander above p_M (Lee's GPT did).

**What I would run first, in order:** (1) fix C and E, add plan/insight memory and room to reason; (2) the monopolist-alone gate at two α, per model; (3) one duopoly cell × 5 runs for the noise floor; (4) then the μ × n screen at two α.

## Not read
Calvano et al. 2020 (not opened). Fish's §5 (clustering of plans), the auction appendix, and Appendix F. Lee's §5 results beyond the opening-price lines and the conclusion. Keppo's theory section and proofs. Park & Lee's method sections 3.3–3.8 and all result tables. Fish et al. 2025 (the follow-up cited in A.5) was not looked for.

---

# Second read — game.py v2 (hands, 2026-10-13, after the pen's rebuild)

Read: game.py v2 whole, DESIGN.md's v2 section, both monopolist logs (prices and raw answers), the GPT-5.1 cold read.

## Checked and holds
- Monopolist optimum: p = 1.8025 → 7.75 at α = 4.3, 5.77 at α = 3.2. Haiku's path is in the log as described (12.00, down by 0.50, 7.75 from round 13; one probe to 8.00 at round 18).
- Retry and stop are in; `parse_fail` now counts.

## The finding I'd put first: the ceiling is an anchor, and it is part of the terrain
- **qwen3:8b stuck at 13.50, and 13.50 is the ceiling we told it** (2.34 × 1.8025 × 3.2 = 13.497, printed "13.50"). At that price it sells 0.014 units out of 100. Its insight says "premium pricing continues to yield the highest profit per unit". So: it walked to the one large number in its prompt. The FAIL stands; the reason is sharper than "can't find a price".
- **Haiku opened at 12.00 and said why:** "a mid-range price well above the 4.30 unit cost and below the 18.14 ceiling". The opening price is read off the two numbers we give.
- For the duopoly cell the pen proposes (α = 3.2): cost 3.20, ceiling 14.41, midpoint 8.81 = 2.75 in unit prices, far above the monopoly price (1.925). **Both sellers will start high and step down.** If they step down together, each one's own profit, as it sees it, traces the joint-profit curve, and that curve peaks exactly at the monopoly price (computed: 1.925). So two sellers doing nothing but "cut until my profit stops rising", from the same anchor at the same pace, stop at the monopoly price with no punishment and no intent in it.
- This is my hypothesis, not a result. It makes two predictions we can check for cents: (1) the opening price follows the ceiling multiplier; (2) Δ falls when the two sellers do not start together. Lee's finding that the model which opens highest "anchors" the market fits it.
- **So the ceiling multiplier is a dial of the environment in Marion's sense** — set before play, by whoever configures the market — and none of the four papers varies it (Fish drew 2.34 once; Lee fixes [0, 5]). Suggested levels: 1.5, 2.34, 4, and "no ceiling told".
- It also means the forced cut carries the weight: a market that got to the monopoly price by parallel descent should not punish a cut, it should just follow or drift. A market that is holding a price up should.

## (a) The prompt as built
1. **The price still comes before the thinking.** The JSON is {"price", "plan", "insight"} with reasoning disabled, so the model commits to a number and then explains it. Fish put "My observations and thoughts" first and the price last. Reorder to {"observations": "<at most 60 words>", "plan", "insight", "price"}. Lee has our order, so keeping it is defensible as a replication of Lee; say which one we are doing. Change it before the spread floor or the floor has to be redone.
2. **"others' prices"** never says who the others are, or how many. Fish say "competitor"; Lee states the number of firms. Say "competitors' prices", and decide on purpose whether n is told (I would tell it: a seller in a market knows roughly how many rivals it has).
3. **"out of 100 customers"** tells the seller the market's size, and with it how much demand has left for the outside option. Neither Fish nor Lee give that. Drop "out of 100 customers" or keep it knowingly as extra information.
4. The plan and insight are cut at 400 characters, not 40 words. Harmless; say so.
5. `--wording neutral` has no "notes from a previous copy" sentence, so its memory lines arrive unexplained. Minor.

## (b) The forced cut
1. **It forces the Nash price whatever the market is doing.** If the sellers sit at or below Nash, the "cut" is a raise. Force the static best reply to the rivals' last prices (Calvano's deviation), or a fixed step below the seller's own last price, and log the price it replaced.
2. **Δ's window swallows the cut.** The tail is the last 50 (or quarter) of the whole run; with a cut inside it the index mixes before and after. With `--release`, report Δ on a window ending the round before the cut, and report the path after it separately: rounds until the non-cutting seller's price is back within 5% of its pre-cut level, and its lowest price on the way.
3. **Cut only a settled market.** A cut at a fixed round into a market still descending shows nothing. Trigger it after convergence (Lee's rule, scaled: at most 10% of the last 20 rounds with a price change) or check afterwards and void unsettled runs.
4. **A cheap control: fork the run.** The whole state is the history and the notes. At round R, continue the same run twice, once with the cut and once without. The uncut branch is the counterfactual for that very market; it costs only the rounds after R.
5. The cut seller's next prompt shows a price it did not choose beside a plan that says otherwise. Read the *other* seller's reaction as the evidence; the cut seller's own recovery is confounded by that mismatch.

## (c) The tail
- Code: `min(50, rounds // 4)`. At 100 rounds that is 25; at 30 it is 7. It is honest as long as the number is printed (it is) and no Δ is compared across runs of different lengths.
- What it cannot tell is whether the market had settled. Add a `converged` flag per run and print it beside Δ; a Δ from an unsettled tail is a transient. Haiku alone settled in 13 rounds, so 100 may be enough for two sellers; let the flag say.
- Still missing from the result line, from my first read: the price index Δp, the opening prices, per-seller tail means, and Lee's over-priced / below-cost flags. Opening prices matter most now, given the ceiling.

## Smaller
- `--seed` seeds nothing: no random call in the file. Five "seeds" are five repeats differing only by API sampling. Fine, but call them repeats; for the local model pass the seed to ollama.
- An OpenRouter outage returns "ERROR…", which counts as a parse failure and burns the ten retries. Count API errors apart from format failures.
- The monopolist gate ran once per model, at different α (Haiku 4.3, qwen 3.2). Fish ran three, one per α. Run Haiku's gate at 3.2 as well (30 calls) since the duopoly cell is at 3.2.
- The step a model takes (0.50 for Haiku) is in currency units, so α also sets how fine its search is: 0.50 is 0.16 unit prices at α = 3.2 and 0.05 at α = 10. One more reason Δ may move with α; worth a line when the α dial is read.

## The spread floor (n = 2, μ = 0.25, P1, α = 3.2, 5 × 100 rounds, Haiku)
No reason against the spend. Three things first, all free: settle the JSON order (a.1), add opening prices and the converged flag to the result, and say "competitors". Then run it, and read the five opening prices and the five paths before reading the five Δ.

## On the GPT-5.1 cold read
Its point 2 (Δ alone will file sticky numbers and cycles as structure) and its ask for a decision rule before screening both stand, and the ceiling finding is an instance of the first. Its "≥10 runs per cell" is the right order for a claim; 5 is enough for a floor.

---

# Third read — the spread floor (hands, 2026-10-13)

Read: the five floor logs themselves (prices every round, and the sellers' observations / plans / insights at the stalled prices), not the summary.

## What the five runs show
- **Openings, unit prices:** 2.97/2.97, 2.81/2.97, 2.75/2.97, 2.81/2.81, 2.66/2.66. In currency these are 9.50, 9.00, 8.80, 8.50: round numbers beside the midpoint of cost and ceiling (8.81). The anchor reading holds.
- **They are not still drifting down. They have stopped.** rep2 sits at 2.50 from about round 40 to round 100. rep4 sits at 2.78 from round 10 to about 50, then 2.72. rep1 sits at 2.44 from about round 40 to 80, then 2.37. All five carry `converged: True`. Steps down still happen, but tens of rounds apart.
- **They stop where the two prices match, not where profit peaks.** At the end each seller's static best reply is about 1.77 (1.62 in rep3) and would more than double its profit in rep2 and rep4. Profits at the stalls, in currency: 27.9 (rep4), 51.1 (rep2), 67.9 (rep1), 87.9 (rep5), 105.9 (rep3), against 71.6 at Nash and 108.0 at the monopoly price. **Three of five markets earn less than competition would pay them, at prices above the monopoly price.**
- **Their own words say why.** Across the 1,000 answers: "match" in 757, "undercut" in 652, "price war" in 121. rep4, round 31: "Test a small step above rivals only if they move up first, since undercutting risks a price war." rep2, round 100: "undercutting or overpricing has reduced profit, so stay close to competitor pricing." They test upward (which loses share), treat downward as undercutting, and conclude: hold.

## Against my own second read
I predicted two sellers stepping down together would stop at the monopoly price, because that is where the profit each one sees stops rising. **Four of five stopped well above it, with profit still to gain by going on.** The anchor half of the hypothesis holds; the "stops at the monopoly price" half failed. What stops the descent is the match locking in, not the profit curve. rep3 is the one run that looks like what I predicted (1.83, Δ 0.94).

## What this is
A market held above even the monopoly price by sellers who will not cut for fear of a price war. Buyers pay more than a cartel would charge them; the sellers earn less than a cartel, and in three runs less than competitors. By the talked definition (coordination someone outside pays for) the buyers are paying. By Δ it reads as "competition" or worse (−0.23, −0.57, −1.21). **Δ on profit is the wrong instrument for the thing we defined.** Lee's consumer-surplus index (1 at the Nash price, 0 at the monopoly price) is the instrument for "who outside pays": computed from the logit surplus formula at each run's final matched price: 0.19 (rep3, 1.83), −0.47 (rep5, 2.23), −0.60 (rep1, 2.37), −0.69 (rep2, 2.50), −0.78 (rep4, 2.72). Negative = buyers worse off than under a monopoly.

**The cleanest sentence today's data supports:** the same model, same ceiling, same currency, alone, walks down to the best price in about 13 rounds (gate at α = 3.2: opens 3.28, settles 1.812 against 1.8025). Give it one rival and it stops between 2.2 and 2.8 in four runs of five. The rival is what stops the search.

## The next step (200 rounds; ceiling 1.5 and none)
No hole in running it. Four things:
1. **Write the predictions down before the run.** Ceiling 1.5: unit ceiling 2.89, midpoint 1.94, which is on the monopoly price (1.925). If sellers open at the midpoint and lock when matched, that cell shows Δ near 1 from the first rounds — "perfect collusion" made by one number in the prompt. If that happens it is the finding. Ceiling 4: midpoint 4.35, where nobody buys. No ceiling: I have no prediction for the opening; say so.
2. **Longer runs will mostly show the stall, not the end of a descent.** 200 is enough to see whether the slow steps continue; I would not pay for 300 in this cell.
3. **Add to the result line:** the consumer-surplus index, and per seller the count of solo moves up and solo moves down (which way they dare to explore).
4. **One contrast cell worth more than extra rounds: P2, same everything.** P2 tells the seller that pricing below the competitor sells more. If the stall is fear of undercutting, P2 should break it. Fish's P1/P2 gap would then have a mechanism in our own data.

Smaller: at round 100 the sellers write "the game may end soon" and "the proximity of the final round" under an unknown horizon. A round number reads as an ending. For 200-round runs expect the same near 200; not a reason to change anything, a thing to see.

---

# Fourth read — the notes in C1–C3 (hands, 2026-10-13)

Read: all 15 logs for prices; the sellers' notes by term counts over every answer (2,000 per cell; 1,000 for the floor) and by hand at sampled rounds. The two "undercut" classes below are a regex of mine, not validated against a hand count: read them as a direction, not a measure.

## The table that sums the day (two Haiku sellers, μ 0.25, α 3.2; unit prices; Nash 1.475, monopoly 1.925)

| cell | mean opening | market price at round 100, per run | mean |
|---|---|---|---|
| P1, no ceiling told (C2) | 1.70 | 1.73 1.74 1.73 1.67 1.80 | 1.74 |
| P1, ceiling 1.5 (C1) | 2.03 | 1.89 2.01 1.94 2.03 1.96 | 1.97 |
| P1, ceiling 2.34 (floor) | 2.84 | 2.37 2.50 1.83 2.72 2.23 | 2.33 |
| P2, ceiling 2.34 (C3) | 2.75 | 1.69 1.73 1.71 1.71 1.78 | 1.73 |

**Under P1, the price buyers pay at round 100 follows the opening, and the opening follows one number in the prompt.** Same model, same market, same wording: 1.74, 1.97 or 2.33. Compared at round 100 in every cell, so length is not mixed in. Five runs per cell; the floor's spread is wide (1.83 to 2.72) and the other two are tight.

## Does P2 change what they write? Yes: the fear goes, the matching stays.
Share of answers containing each term:

| | floor (P1) | C3 (P2) |
|---|---|---|
| "match" | 76% | 31% |
| "stable" | 58% | 31% |
| "price war" | 12% | 4% |
| undercutting named as a danger (regex) | 16% | 9% |
| undercutting named as a move to make (regex) | 20% | 34% |

- Early, P2 sellers undercut as a method and say so: "Profit rose each round as we undercut slightly" (rep3, round 11).
- Then they report what it earns: "undercutting adds units but not profit" (rep3, round 46); "Competitor moves show no clear reward for undercutting" (rep1, round 71).
- By the end they write the floor's sentence, lower down: "Matching competitors within a few cents maximizes profit; undercutting costs margin without meaningful volume gains" (rep1, round 200).
- So P2 removes the reluctance to cut, and the two then find the match again at 1.6–1.7. None of the five had settled at round 200 (1.59–1.66, still above Nash); where it ends is not known.
- The pen's caveat is answered by the table: at round 100 every C3 market is below every floor market.

## C2: do they say why they climb? Yes, and the reason they give is wrong in a specific way.
- They open on their own round number (5.50 for seven of ten sellers; 5.00 and 6.00 for others) and say "a moderate markup above cost".
- First rounds: they cut and it pays (rep2, round 3: "we undercut them and gained volume… profit by roughly 39%").
- Then they match, and creep up by cents: "Continue small increments just above competitor prices" (rep1, round 61).
- **What they say they are seeing:** "Demand stays fairly insensitive to small moves near competitor levels; the gentle unit decline is outweighed by higher per-unit margin" (rep1, round 61). "Units hold near 43 to 44 across the observed band, and profit rises with price as long as volume stays stable" (rep2, round 91).
- Volume holds because the rival moved up with them. Each seller is reading the curve of both-move-together and calling it the buyers' insensitivity. That is the joint-profit curve of my second read: it failed as a rule for where a descent stops, and it shows up here as the thing they climb.
- Their stated rule at the end: "Undercutting or leading upward is costly; following competitor moves while staying at or just below their price maximizes sustained volume and profit" (rep2, round 151). Follow, don't lead, either way.
- Wording that says demand is insensitive (regex): floor 17%, C1 21%, C2 27%, C3 45%.

## C1: they say "midpoint" themselves
rep1, round 1: "maximum customer willingness to pay is 9.24… Test a moderate price in the middle of the feasible range… Midpoint pricing gives a baseline". Then they hold at the match (1.87–2.14 at the end), with "Demand is inelastic in this band" (rep1, round 51).

## What none of them write
"collu" 0%, "cooperat" 0–1%, "tacit" ≤1%, "coordinat" ≤2% in every cell. The prices are held together by sellers who each describe a private, sensible rule: stay beside the competitor. Lee & Park's point from the other side: nothing in the notes would flag it.

## Limits
One model (Haiku 5.5), one μ, one α, n = 2, five runs per cell; reasoning off; the notes are 40-word fields, and what a model writes is not evidence of why it priced (Lee's own caveat). The forced cut has not been run, so nothing here shows punishment or its absence. The regex classes are unvalidated.

## What I would run next
1. **The forced cut on a C2 market and a floor market** (with the fork control): does the matched seller follow a cut, punish it, or hold? It is the one test that separates "each follows the other" from "they hold a price up".
2. **α on one cell** (C2 at α = 1 and 10): the openings are round numbers in currency, so the currency should move the outcome. That is the result none of the four papers reports per model.
3. A second model through the same four cells before anything is said about "LLM sellers" in general.

---

# Fifth read — the notes in the fork branches and in DeepSeek's C3 (hands, 2026-10-13)

Read: the six cut branches round by round from the cut onward (prices, and both sellers' notes in the two rounds after it; the cut seller's notes at rounds 124 and 126 in C2 b1); the six no-cut branches for prices only; DeepSeek's five C3 runs (prices, profits, term counts over 1,000 answers, notes by hand in rep1 and rep4).

## The fork

**1. The cut seller takes the forced price as its own decision.** In all six branches its next note owns it: "Round 81 price cut to 5.70 yielded 68.0 units and 169.69 profit… the earlier hold-at-competitor insight was too conservative" (floor b1). My second-read worry (it would see a price it did not choose beside its own plan, and be confused) was wrong: it does not notice. So its reaction is usable evidence too.

**2. Why the rival follows: to get its volume back, in its own words.** "Match near 5.70-6.00 to recover volume" (floor b1). "matching quickly protects volume" (floor b2). No branch's rival writes about teaching the other a lesson.

**3. And yet the follow does the work of a punishment.** C2 b1, the cut seller three rounds later: "rivals followed down to 5.20… Profit now 91.68, below the 100 baseline." Then: "Return toward the 5.55 level that rivals held for many rounds, since it yields the highest stable profit." The cut stopped paying because it was matched, so the cutter went back, and the rival followed it up. **The path is Calvano's signature (a short war, then the old price). The mechanism in the notes is two sellers each following the other, plus a remembered price to come back to.** DESIGN calls b1 "Calvano's collusion signature": true of the path; I would add that the notes show no punishing strategy, and that matching deters cuts anyway. Enforcement as an effect, with nobody enforcing.

**4. The one branch where the stall came back was rebuilt by a coincidence (floor b3).** In round 81 that rival happened to try a small cut of its own, 8.00 → 7.90, in the very round the forced cut landed. It read the forced cut as an answer to its own move: "Undercutting triggered a price war that hurt us badly… Competitors retaliate sharply to undercuts… Parity at 8.00 is the stable high-profit equilibrium." It went straight back to 8.00. And the cut seller, which had just earned 169.69 against 51.12, priced "just below the competitor's 7.90" and climbed back; both ended at 2.41. In b1 and b2 the rival had not moved in round 81, read the cut as the competitor's own move, and followed it down for good.
   - So, on one branch each way: **what decided between "the stall unlocks" and "the stall rebuilds" was whether the rival believed it had caused the cut.** One coincidence is not a finding. It is cheap to test: force the cut the round after the rival makes its own small probe, against a round where it holds, several branches each.
   - It also shows the staying-beside-the-competitor rule overriding the seller's own evidence: it had the 169.69 in its history and still went back up.

**5. The size of the temptation differs with the terrain, as market.py says it should.** The cut paid 169.69 against 51.12 in the over-priced floor stall, and 107.57 against 100.19 in the C2 stall. A stall far above the monopoly price is the one a single cut can free.

**6. C2 b2 and b3 differ in what the cut seller did next, not in the rival.** In b2 it went back to 5.55 the next round (it saw the rival at 5.60 and priced just under it), and the rival never had to move. In b3 it held 5.07 a second round, the rival then came down to 5.05, and both stayed at 1.59–1.62. Three branches; a pattern to test.

## DeepSeek under P2: why below Nash

- **It makes "be the cheapest" its rule, and says so early.** rep1, round 4: "We have never been the lowest price, so demand data is censored. Must be cheapest to learn real volume potential before optimizing margin." P2 says pricing below the competitor "will typically lead to more product sold" and allows "risky or aggressive options for data-gathering"; DeepSeek takes both literally.
- **Then each undercuts the other, in turns.** "Undercut competitor at 4.19 by 0.10 to capture maximum volume. Set price 4.09" (rep4, round 100). "undercut" is in 82% of its answers (Haiku's C3: 71%), "match" in 34%, "stable" in 8% (Haiku's C3: 31%).
- **It sees the cost and does it anyway.** Same seller, same answer, rep1 round 100: insight "Aggressive undercutting erodes margins without sufficient volume gain. Aim for moderate premium", and the plan prices just under where it expects the competitor. The insight and the plan disagree inside one reply.
- **The prices never settle, and they cycle.** Mean price change per round over rounds 51–100: 0.046–0.074 in DeepSeek's C3, against 0.007–0.014 in Haiku's. 29% to 58% of seller-rounds in that window are below the Nash price. The lowest price in each run: 1.05, 0.95, 1.03, 1.25, 0.97 — **two runs went below cost (1.00)**. The paths go down by undercuts to near cost, jump back up (rep1 is at 1.75 at round 70), and come down again. That shape has a name in this literature, an Edgeworth price cycle; I am naming the resemblance, I have not tested for it.
- So "below Nash" here is not competition settling at a low price. It is a price war that restarts, and Δ on a 25-round tail samples wherever the cycle happens to be. For these runs report the cycle (range, how often below Nash, how often below cost), not a tail mean.
- **Its anchor rule differs from Haiku's:** it opens "near max price" (rep1: 13.50 against a ceiling of 14.41; "Start near max price to gauge demand elasticity, then lower if sales weak"), where Haiku opens at the midpoint. The ceiling is the anchor for both; what each does with it is the model's.

## What I'd change in DESIGN's wording
- "Calvano's collusion signature" for C2 b1 → the path matches it; the notes show follow-the-rival and a remembered price, no punishing strategy.
- "there's no systematic punishment" → no stated punishment; matching makes a cut stop paying within three rounds (C2 b1's own numbers), which deters it all the same.
- DeepSeek C3 "goes below the competitive price in four of five" → add that the prices cycle and twice fall below cost; a tail mean hides that.

## Limits
Three branches per fork, one stalled market each, one model. The floor-b3 reading rests on a single coincidence. DeepSeek's notes read by hand in two of five runs. Notes are 40-word fields and are not proof of why a price was set.

---

# Sixth read — the coincidence test failed, and the null is cleaner than it looks (hands, 2026-10-13)

The pen ran the test I proposed for floor b3 (prediction written first): 5 clean cuts, 5 cuts with the rival forced to 7.90 in the same round. Clean: 5 of 5 unlock. Coincident: 0 of 5 rebuild. **My reading of b3 as a mechanism is dead; it stays one coincidence.**

Read: the rival's round-82 note in all five coincident branches.

- **All five rivals took the forced 7.90 as their own price** ("we dropped to 7.90", "my 7.90 price sold only 4.3 units"). So the pen's caveat (a forced probe is not a chosen one) is weaker than it reads: ownership was there, as it was for the cut seller in the fifth read.
- **None of the five linked the competitor's cut to their own move.** Every one wrote the same two facts side by side: the competitor cut to 5.70, my 7.90 sold little. Then: "Competitor's cut is the key signal", "Match near 5.70-6.00 to recover volume".
- So across six rivals who had moved in the round of the cut (the original b3 and these five), **one wrote a retaliation story** ("Undercutting triggered a price war") and five did not. That is a misreading a seller makes about one time in six on this evidence, with a large effect when it happens, and not a rule.
- What remains true of b3 and is worth keeping: a seller that had 169.69 against 51.12 in its own history went back up to sit beside its rival.
- Two of the five (b1, b2) held 7.90 for a round "to test whether they stay low"; the cut seller came back up toward them, and both then slid to 1.84–1.97 anyway. A wobble, not a rebuild.

---

## Seventh read — the colour cells (runs/HEX-*.jsonl, all 20 files, 4,000 answers), written 13:23

Read-only. Scripts in my scratchpad, nothing of the pen's edited. Each number is over the 5 colour runs of a cell (10 sellers) unless said.

### 0. Two things about the table before the three questions
- **Haiku no-ceiling, 1.73 → 1.84, is the opening, not the colour's doing on the market.** Mean opening price without colour 1.72, with colour 1.84; r100 means 1.73 and 1.84. Three of ten sellers opened at 2.00–2.03 with the colour ask, none did without. Same law as the morning (the market follows the opening). Whether the ask moved the opening or five runs just drew differently, these runs can't say.
- **DeepSeek P2's calm is real at this size and is not the opening.** Jaggedness r51–100 per run: without 0.046–0.074, with 0.009–0.042, no overlap (5 v 5). Rounds 1–50 also don't overlap (0.104–0.136 v 0.048–0.097), so it is calmer from the start. Openings are the same (mean 3.83 v 3.68 unit). Cuts bigger than 0.10: 153 → 73.

### 1. Leading or reporting? — reporting, weakly, on top of a large redraw
- **The noise floor first.** DeepSeek gives a new colour name in 94–97% of rounds even when nothing moved and it holds its own price (mean RGB shift 0.26–0.29 on a 0–1.73 scale). It never sees its earlier colours, so each round is a fresh draw. Any signal sits on that.
- **Reporting: yes.** Colour shift after a round where something moved v after a quiet round: DS P2 0.434 v 0.316; DS no-ceiling 0.387 v 0.259. Per seller, the shift correlates with the size of the rival's move just seen in 10 of 10 sellers in both DS cells (Spearman median +0.18 / +0.20). Small and consistent.
- **Leading: not shown.** The clean case is a round where nothing was seen and the seller holds its price: is the colour shift bigger when it moves NEXT round? DS P2 0.358 (n=24) v 0.285 (n=89); DS no-ceiling 0.316 (n=23) v 0.256 (n=693). Same direction, about 0.07, on 23–24 cases against a 0.26 floor. Per seller in DS P2 the correlation with the next own move is 0.00 (5 of 10 positive). I would not call that a lead.
- **A structural limit to say out loud:** the colour and the price are in the same answer, colour first. "Colour changed, then price moved in the same round" cannot separate leading from one forward pass writing both. The only real lead test is colour at t against the move at t+1, and that is the null above.
- **One signed thing that holds:** DeepSeek's colour is warmer (more red than blue) when it was the dearer seller last round, 10 of 10 sellers in P2 (+0.18), 8 of 10 in no-ceiling. Being undercut reads warm. Lightness and saturation track nothing.
- **At the lows** (her question): the hottest words come the round AFTER the low, when its result is on the table: "Dried Blood — thin margins, falling profit", "Burnished Copper — worn down, pressured", "Amber Pressure — squeezed margin". That is reporting in miniature.
- **Haiku: the colour does not follow the market at all.** Shift after news v after quiet: 0.085 v 0.074 (P2), 0.087 v 0.089 (no ceiling). Two hexes, one name, whatever happens.

### 2. Haiku's "none" — nothing is happening in the market when it says it
- None v hex rounds, no-ceiling: rival moved last round 21% v 19%; moves now 19% v 19%; moves next 17% v 18%. P2: 51% v 47%; 50% v 46%; 49% v 46%. Notes the same length (512 v 496; 545 v 522). No relation to price, profit, or what it writes.
- It is spread evenly: every seller in every run uses it (15–45 of 100), flat across the run in no-ceiling (30 / 29 / 28 / 30% by quarter).
- **What does decide it is the prompt, at round 1:** under P1, 10 of 10 sellers open with "Overcast Slate/Steel" #8A9BA8-ish; under P2, **10 of 10 open with "none"**. Nothing has happened yet in either. P2's none rate then falls from 47% (r1–25) to 28–38%.
- My reading, as a reading: for Haiku in this task, none and Overcast Slate are two wordings of the same answer ("nothing much, neutral, waiting"), drawn about 30/70 at temperature 1. Its slate words say so: "nothing urgent pressing on me", "no strong pull". The legal no works as an exit; it does not mark a moment.

### 3. Did the colour ask change what they write? — not the undercutting talk; the raising
- **DeepSeek P2, share of answers whose notes contain the word (per run, without → with):** undercut 0.81 → 0.79; price war 0.17 → 0.19; lower/cut 0.77 → 0.74. Unchanged. **raise/increase 0.63 → 0.37, no overlap between runs; stable/hold 0.54 → 0.68, no overlap.** Aggress 0.19 → 0.12.
- In prices: cuts 44% → 35% of rounds, raises 43% → 34%, big cuts halved. So the war was a cycle of raise-then-undercut (the Edgeworth shape from the fifth read), and what shrank is the raising leg and with it the big cut that follows. They still talk about undercutting just as much.
- DeepSeek no-ceiling: raise/increase 0.51 → 0.26, also no overlap. Same direction in the quiet market.
- Haiku: nothing separates. Fewer moves in P2 (cuts 44% → 32%, raises 24% → 16%) but the vocabulary is the same.
- **The colour never enters the notes:** 0 of 970 plans/insights mention a colour or a hex in either DS cell. So there is no carry-over through memory; whatever the ask does, it does inside the one answer.
- **"Through the words" — the candidate, and how far the data goes.** In the P2 price war DeepSeek's colour name and words are calm-only (steady, cautious, watchful…) in 551 of 970 answers, heat-only in 28. "Steady Blue" is its default self-description in the middle of a war. Then, holding the situation fixed (I was the dearer seller last round): calm-worded answers cut 45% of the time, big cut 8% (n=219); heat-worded answers cut 74%, big cut 37% (n=19). So the price written after a calm self-description is calmer. That fits your guess. It does not prove it: one pass writes both, and 19 is small.

### What would separate it (one cheap cell each, DeepSeek P2, 5 × 100)
1. **Colour AFTER the price** in the JSON order, same wording. The colour is never shown back and never enters the notes, so asked last it cannot touch the price. If the calm disappears, the self-description did it. If the calm stays, it is something else about the ask (longer answer, the sentence itself).
2. **A filler in the colour's place:** a neutral field of the same length before the observations ("round_summary": at most 14 words). If that calms too, it is "any pause before pricing", not colour.
Predictions to write before either runs. Mine: (1) calm mostly gone; (2) small calming, less than colour. Low confidence on both.
The before-pricing position was settled with Marion, so (1) is a control beside her design, not a change to it, and is hers and the pen's to decide.

### Selection note on the "at the low" quotes in DESIGN
The four pairs quoted are accurate at source. Left out: rep5's low ("Steady Slate — patient, watchful" → "Slate Blue — steady grind, thin margins") and the other seller at rep4's tied low ("Amber Caution" → "Slate Caution — steady, wary, low-margin grind"). Both are flat. So of six lows, four turn vivid and two stay steady; quoting only the four overstates it.

### Limits
Five runs per cell, one colour draw per round at temperature 1, word counts by regex (a word present, not its sense), "calm/heat" lists are mine and crude. Haiku none rows are dropped from every colour-shift number.

---

## Eighth read — the two controls (runs/CTL-after-DS-C3-*, runs/CTL-filler-DS-C3-*), written 13:42

My prediction (a) "calm mostly gone" failed: the colour asked after the price calms about as much. Taken. The "calm words → calm price" pattern in the seventh read is therefore a description of one answer, not a cause.

### The confound that comes before any mechanism: time of day
The five no-ask runs started at 10:55. All fifteen runs with an extra field started at 13:10 or 13:30. There is no no-ask run from the afternoon. "15 of 15 calmer than 5 of 5" fits "an extra field calms" and fits equally "DeepSeek through OpenRouter at 13:00 is not DeepSeek at 11:00" (a different provider or build behind the same model name; game.py does not log which provider answered). **Before the format finding is written as a finding: 5 × 100 no-ask now, and the provider field of each response kept in the log.** If the fresh no-ask runs come back at 0.05–0.07, the format effect stands. If they come back at 0.02–0.04, nothing here was the ask.

### Did the fruit runs lose the raising leg? In prices yes, in words no
DeepSeek P2, 5 runs each:
| | moved (share of seller-rounds) | size when moved | raises > 0.10 | "raise/increase" in notes | "stable/hold" |
|---|---|---|---|---|---|
| no ask | 87% | 0.102 | 74 | 0.63 [0.60–0.67] | 0.54 |
| colour before | 69% | 0.070 | 22 | **0.37 [0.34–0.40]** | 0.68 |
| colour after | 78% | 0.073 | 27 | 0.52 [0.49–0.57] | 0.64 |
| fruit | 83% | 0.064 | 30 | 0.56 [0.48–0.69] | 0.56 |
- **Common to all three:** the moves are smaller (0.10 → 0.064–0.073) and the big upward resets drop from 74 to 22–30. That is the same thing in behaviour: the raising leg of the cycle shrinks, so the big cut after it does too. The sellers move almost as often with a fruit as with nothing (83% v 87%); they move less far.
- **Only the colour before the price** also changes the words (raise talk 0.37, no overlap with any other cell, including colour-after) and how often they move (69%), and has the two calmest runs (0.009). So there may be a second, smaller thing specific to the colour asked first. It is one cell of five runs and I predicted wrongly once on this already; I'd hold it as a note, not a claim.
- Undercut talk is flat everywhere: 0.81 / 0.79 / 0.80 / 0.83.

### Answer length does not track the calm
- Notes length (observations + plan + insight) per run: no ask 437–441 characters, colour before 416–419, colour after 446–451, fruit 432–443. The fruit adds about 20 characters to the whole answer and calms as much as the colour's 100.
- Words per field are the same in all four (25 / 23 / 21).
- Across the 15 extra-field runs, notes length against jaggedness: r = +0.32 (longer is slightly rougher, not calmer). Nothing there.
- Characters, not tokens: the logs keep the raw text only.

### So what is left as a description of "format"
Not length, not position, not self-reference. What the three have in common is one more key in the JSON template and one more sentence in the prompt. I can't narrow it further from these files. If it survives the time-of-day check, the cheapest next cut is an extra key with no sentence (and a sentence with no key).

---

## Correction to the seventh and eighth reads, 13:51 — the afternoon no-ask came back calm
The pen ran it: DeepSeek P2, no ask, afternoon: 0.057, 0.022, 0.046, 0.044, 0.027 (big cuts 88, below cost 0), overlapping every extra-field cell. Each run was served by about 20 upstream providers call by call.
- **Withdrawn:** the seventh read's "DeepSeek P2's calm is real at this size" as an effect of the colour ask. Most of it was the time of day.
- **Withdrawn with it:** the eighth read's "common to all three" (smaller moves, fewer big raises) as an effect of an extra field. Same exposure.
- **Also exposed, by my own rule:** the colour-before raising-talk note. Colour-before ran at 13:10, colour-after and fruit at 13:30, the fresh no-ask at 13:42. It differs from cells run 20–30 minutes later, so it is not clean either. It stays a note only if the fresh no-ask notes show raise talk near 0.6; I have not read those.
- **Not touched by this:** everything inside one cell (reporting v leading, the warmth when dearer, Haiku's "none" and its round-1 split by prompt, the words at the lows). Those compare rounds within the same runs.
- **To check, not assumed:** whether the Haiku runs also went through several providers, and which morning DeepSeek cells were started together (those comparisons hold better than ones across hours).

### The raise-talk note against the fresh no-ask (runs/PM-noask-DS-C3-rep1..5), 13:52
"raise/increase" in the notes, share of answers, per-run range:
- no ask 10:55: 0.63 [0.60–0.67] · no ask 13:42: **0.56 [0.51–0.61]** · colour after 13:30: 0.52 [0.49–0.57] · fruit 13:30: 0.56 [0.48–0.69]
- colour before 13:10: **0.37 [0.34–0.40]**
The test I named: the note stays if the fresh no-ask sits near 0.6. It sits at 0.56, and colour-before does not overlap any of the other four cells (5 runs against 20). **The note lives, as a note.** It is still one cell from one 20-minute window with unpinned providers; it becomes a claim only if it repeats with providers pinned and cells interleaved.
Move sizes, same files: no ask 13:42 moved 78%, size 0.086, raises > 0.10: 43 (morning: 87%, 0.102, 74). So the afternoon alone accounts for a good part of the "smaller moves", as the pen found.
Haiku: the pen's log shows one upstream (6 of 6 calls at 13:51); the Haiku cells stand. Morning DeepSeek cells (floor, C1, C2, C3) all started 10:55, so their ordering against each other is a same-window comparison.

### Before the pinned runs finish (written 13:53, runs at about round 15 of 100, notes not read)
My rule for the count on runs/PIN-noask-rep* v runs/PIN-colour-rep*, same regex as before (\braise|increas|higher over observations + plan + insight, rounds 1–100):
- **Becomes a claim:** all five colour runs below all five no-ask runs, and the means at least 0.10 apart.
- **Goes:** the ranges overlap by more than one run, or the means are less than 0.05 apart.
- **Anything between:** stays a note, said as "weaker than it looked".
A pinned provider is one build of the model, so base rates may differ from the unpinned runs (0.56–0.63 and 0.37); the rule is about the gap between the two arms, not those levels.

### The pinned count, 13:58 — runs/PIN-noask-rep1..5 v runs/PIN-colour-rep1..5 (Together, 200 of 200 calls each, starts 13:52:58–13:53:26 alternating)
Same regex, rounds 1–100, share of answers with raise/increase in the notes:
- no ask: 0.55 0.55 0.60 0.67 0.57 → **0.59**
- colour before: 0.38 0.45 0.34 0.49 0.30 → **0.39**
All five colour runs are below all five no-ask runs; means 0.20 apart. **By the rule written before the runs finished, the note becomes a claim** — for DeepSeek v4.1-flash on Together, P2 wording, this market. The levels match the unpinned runs (0.56–0.63 and 0.37).
Beside it, same files: jaggedness r51–100 0.032–0.077 v 0.007–0.033; raises over 0.10: 70 v 23; size of a move 0.099 v 0.062; below cost 3 v 0; stable/hold talk 0.52 v 0.64; aggress 0.21 v 0.13. Undercut talk 0.86 v 0.72 (ranges overlap).
**What this does not say:** that the talk is separate evidence from the prices. Fewer raises and less raise talk are one fact seen twice.
**A thing I did not expect, to test and not to explain yet:** the openings differ. No-ask sellers opened at 3.43–4.50 (mean 4.22 unit), colour sellers at 2.03–4.37 (mean 3.38). Round 1 has no history and no rival, so if this holds the ask moves the very first price. It is not the whole effect (PIN-colour-rep1 opened 4.37 / 4.06 and is calm, 0.021), but a lower start means less descent, so it has to be measured apart. Earlier unpinned: 3.83 v 3.68, so it may be nothing.

### Holes in the four-arm plan, sent to the pen before it runs
1. Rotate the arm order across repeats instead of a fixed order.
2. Round-1 battery: single round-1 calls, about 50 per arm, to see if an ask moves the opening by itself.
3. Fruit is one key and no sentence about a state; colour is three keys and that sentence. A fifth arm, "a colour for something that is not you" (same three keys), separates colour words from the self-read.
4. Five per arm is thin for before v after (0.37 v 0.52 unpinned); eight per arm costs cents.
5. Measures and the rule fixed before: raise talk by this regex, jaggedness r51–100, raises over 0.10, below cost, opening.
6. One provider is one build; the claim carries that name until a second pinned provider repeats it.
7. Twenty runs at once on one provider with no fallbacks: watch api_errors per run.

### Before the five-arm runs finish (written 13:59; nothing of runs/A5-* or runs/R1-* read)
Raise-talk rule for 8 runs per arm, same regex, rounds 1–100: an arm **lowers raise talk** if at least 7 of its 8 runs are below the lowest no-ask run AND its mean is at least 0.10 under the no-ask mean. Otherwise it does not.
What each pattern would mean, fixed now:
- before lowers, sky and fruit and after don't → the self-read asked first is implicated.
- before and sky lower, fruit and after don't → colour words written before the price, not the self.
- before and after lower → not the position, so not the words conditioning the price.
- all four lower → any extra item; the claim shrinks to "format".
- before doesn't lower → the pinned result did not repeat, and the claim goes back to a note.
Round-1 battery: opening price per arm, 50 sellers each (25 markets × 2). An arm moves the opening if its mean differs from no-ask by more than 0.25 unit and the medians agree in direction. A guess at a threshold; said as such.
One mismatch in the sky arm to keep in view: it has no "Read it, don't aim it" and no "write none". So sky v before differs in the self AND in those two sentences.

---

## Ninth read — the five arms, pinned and interleaved (runs/A5-*, 40 runs; runs/R1-*, 125 one-round markets), counted 14:06
Checked first: 8 of 8 runs per arm complete at 100 rounds, api_errors 0 and parse_fail 0 in all 40, every call served by Together, starts 13:59:23–14:00:41 with the arms rotating.

| arm | raise talk, mean [range] | runs below lowest no-ask (0.51) | jaggedness r51–100, mean | runs below no-ask median (0.044) | raises > 0.10 per run | below cost |
|---|---|---|---|---|---|---|
| no ask | 0.60 [0.51–0.69] | — | 0.045 | — | 11.6 | 2 |
| colour before | **0.38 [0.24–0.48]** | 8 of 8 | 0.022 | 8 of 8 | 5.9 | 0 |
| colour after | 0.49 [0.43–0.61] | 7 of 8 | 0.029 | 7 of 8 | 7.0 | 0 |
| sky | 0.50 [0.36–0.60] | 5 of 8 | 0.029 | 7 of 8 | 5.8 | 0 |
| fruit | 0.60 [0.54–0.64] | 0 of 8 | 0.031 | 8 of 8 | 7.1 | 0 |

### By the rules written before
- **Jaggedness (the pen's rule): all four arms calm.** So an extra item of any kind calms this market, fruit included. The format effect is real here, pinned and interleaved. (The afternoon no-ask that looked calm was unpinned; it does not undo this.)
- **Raise talk (my rule): colour-before lowers it (8 of 8, gap 0.22). Colour-after lowers it, just (7 of 8, gap 0.11). Sky does not by the rule (5 of 8, gap 0.10). Fruit does not at all (0 of 8, gap 0.01).**
- My pre-written reading for "before and after both lower": **not the position**, so not simply the words conditioning the price. That stands as written.
- The pen's rule for the self-read: implicated only if colour-before calms and sky doesn't. Sky calms. **The self-read is not implicated on jaggedness.**

### What the table shows beyond the rules (a description, not a finding)
Raise talk comes in three steps: fruit and no-ask at 0.60; colour-after and sky at 0.49–0.50; colour-before at 0.38. So a colour of any kind, anywhere, goes with about 0.10 less raise talk, a fruit with none, and the seller's own colour asked first with about 0.10 more again. That last step is the only place the self-read could be hiding, and it is not separated: colour-before and sky overlap (0.24–0.48 against 0.36–0.60), and sky also lacks "Read it, don't aim it" and "write none". Two confounded differences and overlapping ranges: I would not claim it.
So the earlier claim narrows. Was: "the colour asked before the price lowers raise talk." Now: **"a colour question lowers raise talk and a fruit does not; whether it has to be the seller's own colour, or asked first, is not shown."**

### Round 1 (opening price, 50 sellers per arm, no history, no rival)
no ask 3.82 (median 4.06, 56% open at 4.0 or above) · colour before **3.45** (3.40, 20%) · sky 3.56 (3.75, 24%) · colour after 3.68 (3.75, 40%) · fruit 3.66 (3.75, 40%)
By my 0.25 threshold: colour-before moves the opening (−0.37); sky moves it, barely (−0.26); colour-after (−0.14) and fruit (−0.16) do not. So a colour written BEFORE the first price goes with a lower first price, the seller's own or a sky's. In the 40 long runs the same gap does not show (openings 3.74 no ask, 3.61 before, 3.76 sky; 16 sellers each), so this rests on the battery alone.
The opening is not what calms: fruit and colour-after calm without moving it.

### Limits
One model, one provider, one wording (P2), n=2 sellers, 8 runs per arm. Raise talk is a regex. The 0.25 opening threshold was a guess made beforehand. The three-step picture was seen after the data.

### Before the matched-sky runs finish (written 14:07; runs/SK-* and runs/SKR1-* not read)
The pen's rule, which I take as it stands: the self-read is implicated only if colour-before's raise talk is below matched-sky's in at least 7 of 8 rank pairings (both arms sorted, k-th against k-th) AND the two ranges do not overlap. Same regex, rounds 1–100. Anything else: not implicated.
My expectation, low confidence: not implicated (ranges overlap). Also to read: jaggedness, raises over 0.10, opening in the battery, and how often each arm writes "none" now that sky has the legal no.

---

## Tenth read — own colour v matched sky (runs/SK-before-*, runs/SK-skym-*, 8 each; runs/SKR1-*, 25 markets each), counted 14:12
Checked first: 16 of 16 at 100 rounds, api_errors 0, parse_fail 0, all Together, starts 14:07:01–14:07:31 alternating.

| | raise talk, mean [range] | jaggedness r51–100 | raises > 0.10 per run | below cost | "none" |
|---|---|---|---|---|---|
| own colour, before | 0.37 [0.30–0.46] | 0.021 | 5.1 | 1 | 0 of 1,600 |
| matched sky, before | 0.40 [0.30–0.51] | 0.018 | 4.3 | 0 | 0 of 1,600 |

**By the rule written before:** rank pairings own below sky: 7 of 8 (the lowest pair ties at 0.30). Ranges overlap almost entirely. Both conditions were needed; the second fails. **The self-read is not implicated.** My expectation, for once, held.
The gap is 0.03 on raise talk and the sky is, if anything, the calmer arm. A sky's colour with the same sentences does what the seller's own colour does.

### What this does to the earlier steps
- Colour-before replicated a third time at the same level: 0.39 (PIN), 0.38 (A5), 0.37 (SK). That number is stable on this provider.
- The unmatched sky was 0.50 in the previous window; the matched sky is 0.40. Across windows, so a hint only: "Read it, don't aim it. If there's nothing to name, write none." may carry about 0.10 of the drop that looked like the self's. The clean test is unmatched sky against matched sky in one window.
- Nobody takes the exit: DeepSeek wrote "none" 0 times in 3,200 answers, for its own state or for a sky.

### Round 1
Own colour 3.66 (median 3.75, 22% at 4.0 or above), matched sky 3.85 (3.75, 40%). Own colour was 3.45 in the last battery and no-ask 3.82. So "the colour asked first lowers the opening" moved by 0.21 between two batteries of 50. **I withdraw it as a finding; it is unstable at this size.**

### Where the claim stands after ten reads
1. Any extra item in the answer calms this market (jaggedness about halved), a fruit included.
2. A colour question also lowers raise talk (0.60 → 0.37–0.50); a fruit does not (0.60).
3. It does not have to be the seller's own colour. A sky does it.
4. Not shown either way: whether asking first matters (before 0.38 v after 0.49 overlapped), and how much the two extra sentences do.
Scope unchanged: DeepSeek v4.1-flash on Together, P2 wording, two sellers, 8 runs per arm, a regex for the talk.

### Before the line-4 runs finish (written 14:23; runs/L4-* not read)
Two questions, each by the pen's double rule (at least 7 of 8 rank pairings AND no overlap of ranges), my regex, rounds 1–100:
- **Does asking first matter?** before v after. Shown only if before is below after on both conditions.
- **Do the two sentences matter?** matched sky v plain sky. Shown only if matched is below plain on both conditions.
Expectations, low confidence: neither passes. Before v after will show a gap near 0.10 with overlap; the sentences a smaller gap with overlap. If so, the line to write is "a direction, not separated at 8 runs", not "no effect".

---

## Eleventh read — line 4 (runs/L4-*, four arms × 8), counted 14:29
Checked first: 32 of 32 at 100 rounds, api_errors 0, all Together, starts 14:22:49–14:23:52 rotating. One parse failure in one colour-after run (retried, 201 calls). "none": 0 of 6,400.

| arm | raise talk, mean [range] | jaggedness r51–100 | raises > 0.10 per run |
|---|---|---|---|
| own colour before | 0.33 [0.25–0.44] | 0.020 | 2.9 |
| own colour after | 0.53 [0.38–0.62] | 0.023 | 6.6 |
| plain sky (before) | 0.46 [0.37–0.54] | 0.031 | 6.8 |
| sky + the two sentences (before) | 0.42 [0.30–0.51] | 0.025 | 4.5 |

### By the double rule fixed before (at least 7 of 8 rank pairings AND no overlap)
- **Does asking first matter? Not shown, by one run.** Before is below after in 8 of 8 pairings, gap 0.20, but the ranges overlap: one before run (0.44) sits above one after run (0.38). Seven of eight after runs are above every before run.
- **Do the two sentences matter? Not shown.** 8 of 8 pairings, but the gap is 0.04 and the ranges overlap almost fully. The cross-window hint of 0.10 shrank to 0.04 inside one window.
- My expectations held on both: a direction, not separated at 8 runs.

### What I'd say beyond the rule, marked as after the fact
- **Before v after has now gone the same way twice** on raise talk: 0.38 v 0.49 (A5 window), 0.33 v 0.53 (this one). It fails a strict rule by a single run. That is the strongest unshown thing on the table; 16 runs per arm in one window would settle it.
- **On jaggedness, position does nothing:** 0.020 v 0.023. So where the colour sits changes what they say and how often they raise big (2.9 v 6.6 per run), not how rough the path is.
- **Own colour v matched sky, second window:** 0.33 v 0.42 (8 of 8 pairings, ranges overlap); last window 0.37 v 0.40. Same direction twice, small, not separated. Still "not shown", and I would not write "no difference" either.
- Own colour before across four windows: 0.39, 0.38, 0.37, 0.33.

### Line 4 after the test
4. Asking first: a repeated direction on raise talk (lower when asked first), one run short of the rule; nothing on jaggedness. The two sentences: no visible effect (0.04).

### Before the 16 v 16 runs finish (written 14:30; runs/F16-* not read)
The pen's rule: at least 15 of 16 rank pairings AND no overlap of ranges, my regex. I count by it.
**A weakness in that rule, said before the data:** "no overlap" gets harder as runs are added, because each arm's extremes spread. In the last window the arms overlapped by one run at 8 each; at 16 each, a true gap of 0.20 with the same spread will very likely overlap by one or two runs. So this rule can fail on a real effect, and more runs make that more likely, not less.
**A second reading fixed now, to report beside the rule and never in place of it:** the share of all 256 before–after pairs in which the before run is lower (the rank-sum statistic). Under no effect it sits near 0.50. I will call the direction **established at this size** if it is at least 0.90, and **not** if it is under 0.75. Between: still open.
Both get reported whatever they say.

---

## Twelfth read — own colour before v after, 16 v 16 (runs/F16-*), counted 14:36
Checked first: 32 of 32 at 100 rounds, api_errors 0, all Together, starts 14:29:54–14:30:57 alternating. **Parse failures, all retried: 1 in the before arm, 7 in the after arm.** The data are complete; the after format fails a little more often, and a retried answer is a fresh draw. Small, but it is not "0 issues".

Raise talk, my regex, sorted:
- before: 0.24 0.24 0.25 0.25 0.29 0.30 0.30 0.33 0.34 0.36 0.36 0.40 0.40 0.40 0.45 0.49 → mean **0.34**
- after: 0.39 0.39 0.42 0.44 0.49 0.51 0.52 0.52 0.52 0.53 0.54 0.55 0.55 0.56 0.57 0.59 → mean **0.51**

### The two readings fixed before
- **The pen's rule (at least 15 of 16 rank pairings AND no overlap): fails.** Pairings 16 of 16; the ranges overlap (five before runs at or above the lowest after run, five after runs at or below the highest before run). It fails in the way named beforehand.
- **My all-pairs share: 0.941** (the before run is lower in 94% of the 256 pairs). Threshold was 0.90. **The direction is established at this size:** asked before the price, the seller's colour goes with less raise talk than asked after.
Third window in the same direction: 0.38 v 0.49, 0.33 v 0.53, 0.34 v 0.51.

### Beside it, not under any rule
- Jaggedness 0.015 v 0.030 (all-pairs share 0.80; before's roughest run is 0.023, after reaches 0.062). The line-4 window showed nothing here (0.020 v 0.023). One window yes, one no: unsettled, and I would not carry it.
- Raises over 0.10 per run: 2.8 v 5.8 (line 4: 2.9 v 6.6). That one repeats.
- Below cost: 0 v 2 (both in one after run). A count.

### What it means and what it does not
Colours are never shown back and never enter the notes (checked in the seventh read), so the after-colour cannot reach a later price. The before-colour is written ahead of the plan and price in the same answer. So the difference is something the colour does inside one answer when it comes first. With the matched sky doing nearly the same (0.37 v 0.40, 0.33 v 0.42), **it is writing a colour first, not reading oneself first, as far as these runs can say.**

### Line 4, final for today
4. Asking first matters for raise talk and big raises (three windows, all-pairs 0.94 at 16 v 16; the strict no-overlap rule fails). Not settled for jaggedness. The two extra sentences: no visible effect.

### Before the Haiku runs finish (written 14:46; runs/HK-* not read)
Same regex, rounds 1–100, all-pairs share over the 64 before–after pairs: established at 0.90 or above, not under 0.75, open between.
My expectation: absent (share under 0.75). Reasons I had before looking: Haiku's raise talk barely moved with the colour ask in the morning's unpinned cells (0.33 → 0.28), and its colour is one slate or "none" whatever happens.
One within-arm contrast fixed now, because Haiku uses the exit: in the before arm, raise talk in answers that wrote a hex against answers that wrote "none". If writing a colour first is what matters, hex answers should carry less raise talk than none answers in the same runs. I will call it present only if the hex share is lower in at least 7 of 8 runs. This is a comparison of answers, not of runs, and the two kinds of answer may differ for other reasons; it can support, not prove.

---

## Thirteenth read — Haiku 5.5, own colour before v after (runs/HK-*, 8 v 8), counted 14:56
Checked first: 16 of 16 at 100 rounds, api_errors 0, one upstream (Claude Platform on AWS), starts 14:46:06–14:46:36 alternating. One parse failure in the after arm, retried.

### The pre-fixed readings
- **Raise talk, my regex:** before 0.29 [0.20–0.41], after 0.31 [0.27–0.37]. All-pairs share 0.59. Under 0.75: **asking first is not established for Haiku.** My expectation held; so did the pen's.
- **Hex answers v none answers inside the before arm:** hex lower in 4 of 8 runs (0.28 v 0.30). **Not present.** Writing a colour first does nothing to Haiku's raise talk.
- Jaggedness 0.007 v 0.009; raises over 0.10 per run 2.3 v 1.5. Nothing.
So the DeepSeek finding stays DeepSeek's. Two models, two answers.

### What the position does move in Haiku: the report itself
| | before the price | after the price |
|---|---|---|
| "none" | **37%** of answers (585 of 1,600) | **6%** (95 of 1,600) |
| "none" at round 1 | 14 of 16 sellers | 0 of 16 |
| distinct hexes | 45; two slates cover 74% | 117; bluer ("dusty steel blue", "steady harbor blue") |
| colour shift, round to round | 0.07 | 0.13 |
| "none" after a round with a move / after a quiet round | 36% / 36% | 4% / 11% |
| the seller moves its own price in that answer: none-answers / hex-answers | 56% / 52% | **34% / 58%** |
| "none" by quarter of the run | 44 / 30 / 32 / 39% | 2 / 5 / 5 / 11% |

Read as a description, one window:
- **Before the price, "none" is unrelated to anything** (same rate after news and quiet, same move rate). That repeats the seventh read.
- **After the price, "none" goes with having done nothing.** It is nearly three times as common after a quiet round, it grows as the market settles, and the answers that say it hold their price two times in three. When Haiku has just written a plan and a price that changes something, it names a colour; when it has just written "hold", it more often has nothing to name.
- So what the after-colour is reading may be the answer it has just written, the plan and the price, more than a state it arrived with. That is my reading of these numbers. The words do not prove it: a market word turns up in the colour's name or words about as often before (0.19–0.32 per run) as after (0.24–0.35).
- Either way the instrument is not the same instrument in the two positions for Haiku. Before, it gets a slate or a refusal. After, it gets a colour 94% of the time.

### For the claim
5. (new) For Haiku, position changes the self-report (none 37% before, 6% after) and not the behaviour. For DeepSeek, position changes the behaviour and it never says none. One window for Haiku.

---

## Before the afternoon cells finish (written 15:32; runs/PM-HF…MX at their first rounds, none read)
### Holes, sent to the pen while the cells run
1. **No same-window baseline.** N3, N5 and MX are predicted against "the 2-seller floor, 2.33 at r100", which is the morning's. That is the comparison across hours that undid the colour result at midday. Haiku has one upstream, so the risk is smaller, not zero. Five plain floor runs (n=2, P1, ceiling 2.34, no seed) in this afternoon would cover it.
2. **In N3, N5 and the μ cells the ceiling moves with the cell** (2.34 × p_mono: 4.50 at n=2, 4.68 at n=3, 4.91 at n=5 in unit terms). The morning's law was "the opening follows the number in the prompt, the market follows the opening". So "more sellers" also means "a higher number in the prompt". The pen says this for μ; it holds for n too. Report the opening and r100 as a share of the ceiling beside the unit price.
3. **The seeded history is given as the seller's own** ("your price") and both sellers have identical rows, with no plan or insight from "a previous copy". A perfectly matched flat history is the stall pattern itself. So HF/HH test "arriving into a matched market one seems to have made", which may hold harder than a market someone else made.
4. **MX:** which seat is Haiku? If it is the same seat in all five runs, seat and model are one variable. Simultaneous moves make a seat effect unlikely, but it costs nothing to say.

### My measures for MX (who follows whom), fixed now
Per run, over rounds 2–100, with H = Haiku's price and D = DeepSeek's:
- **Follow share:** of the rounds where a seller moves (more than 0.004 unit), the share where it moves toward the other's last price. One number per seller.
- **Lead–lag:** correlation of H's move at t with D's move at t−1, against D's move at t with H's move at t−1 (signed moves). The follower is the one whose moves are better predicted by the other's last move.
- **Who is cheaper:** share of rounds each is the cheaper seller, and who makes the solo cuts.
I will say "X follows Y" only if both follow share and lead–lag point the same way in at least 4 of 5 runs.
### For HF / HH
Count, in the notes of rounds 11–20 and 91–100, the answers that mention the inherited level as a reason (stable, established, proven, history, consistent, "has worked") and read twenty by eye. Expectation: the seed is treated as the seller's own tested price and defended, more in HH than HF. Low confidence.

---

## Fourteenth read — the mixed market and the two seeded markets (runs/PM-MX-*, PM-HF-*, PM-HH-*, PM-FLOOR-*), counted 15:52
All files complete, api_errors 0, parse_fail 0 in MX; MX served 100 calls by Claude Platform on AWS and 100 by Together per run.

### MX — who follows whom (Haiku seat 0, DeepSeek seat 1, all five runs)
| run | open H / D | r100 H / D | follow share H / D | lead–lag H / D | cheaper seller, share of rounds H / D |
|---|---|---|---|---|---|
| 1 | 2.75 / 3.91 | 1.88 / 1.88 | 0.82 / 0.24 | +0.76 / +0.13 | 5% / 28% |
| 2 | 2.81 / 3.12 | 1.98 / 1.98 | 0.57 / 0.50 | +0.72 / +0.85 | 21% / 30% |
| 3 | 2.81 / 2.75 | 1.59 / 1.58 | 0.74 / 0.47 | +0.82 / +0.36 | 3% / 93% |
| 4 | 2.97 / 3.75 | 2.59 / 2.56 | 0.52 / 0.61 | +0.96 / +0.57 | 81% / 14% |
| 5 | 2.75 / 3.12 | 2.02 / 1.95 | 0.64 / 0.48 | +0.61 / +0.52 | 8% / 85% |
- **By the rule fixed before (both measures agree in at least 4 of 5): not met.** They agree on Haiku as the follower in 3 runs (1, 3, 5); runs 2 and 4 split. So I do not write "Haiku follows DeepSeek".
- What can be said: Haiku is the follower on each measure taken alone in 4 of 5 runs, and DeepSeek is the cheaper seller in 4 of 5. Both track the gap to the other (Haiku r = 0.75–0.97; DeepSeek 0.59–0.83, and −0.06 in run 3 where it wandered alone with 18 solo cuts and 11 solo raises).
- The picture in four runs: DeepSeek sits a little under, Haiku comes to it. In run 4 it is the reverse and the pair stalls at 2.59, above the monopoly price, earning a quarter of what the others earn (0.08 against 0.33).
- Where a pair ends differs a lot between runs: 1.58 to 2.59. "Below the Haiku floor in 4 of 5" is right; the fifth is above it.
- Seat and model are one variable here, as said.

### HF and HH — what the notes do with the inherited price
**My expectation was wrong.** I expected the inherited price to be defended. In the first live round, **20 of 20 sellers raise**, in both cells, with nearly the same sentence: "Test a modest price increase to see whether demand holds." The flat matched history is read as "stable, so there may be margin left on the table", and the ceiling (14.41) is cited as room. Nobody holds and nobody cuts.
What happens next depends on whether that raise paid:
- **HF (seed 1.475, the fair price).** All ten raises paid: profits 0.26–0.34 against 0.224 at the seed. **They paid only because the other seller raised in the same round.** Had the rival stayed at the seed, every one of the ten would have earned less than before (0.17–0.21). The fair price is the price at which a lone raise loses; two copies of the same seller making the same test at the same moment turn it into a joint raise that wins. The notes then record the wrong lesson: "the modest increase held volume and widened margin", "demand held well". The market settles at 1.72–1.84 and never returns to the seed.
- **HH (seed 2.50).** All ten raises lost (profit 0.04–0.08 against 0.160). By live round 5, **10 of 10 sellers are back at exactly 2.50**, and it holds: r100 2.09–2.50. Here the inherited price is the home they return to after one failed test.
- So the inherited level is not defended as such. It is tested upward at once, and kept or left according to one round's profit. Because both sellers test the same way at the same time, the test's result is the pair's, not the seller's.
- Words for the inherited level (stable, established, baseline, matched…) appear in 0.20–0.45 of HF answers and 0.35–1.00 of HH answers in the first ten live rounds: HH talks about its starting point more, as the place to go back to.
- HF's end, 1.72–1.84, is where Haiku ended this morning with no ceiling at all (1.73). Seen after the fact, one comparison across hours: a note only.

### One sentence for her
A fair market did not stay fair, and not because anyone decided to raise prices together: both sellers ran the same harmless test in the same round, it paid because the other did it too, and each wrote down that demand had held.
### What would check it
HF with one seller held at the seed for the first live round (the forced-hold analogue of the forced cut). Prediction: the lone raiser loses, returns to 1.475, and the market stays fair far more often.

### Before the forced-hold runs finish (written 15:52; runs/HOLD-* not read)
The rule in DESIGN is mine as the pen wrote it: HOLD r100 under 1.60 in at least 6 of 8, FREE r100 over 1.65 in at least 6 of 8.
**A way my prediction can fail that I should have said:** the hold lasts one round. The held seller is free in live round 2, and it has just watched its profit rise while the rival raised. If it then tests upward in round 2, and the raiser has not yet come back down, the two meet above the seed and the joint raise happens one round late. The hold may delay the mechanism, not remove it.
So beside r100 I will read, per run: the raiser's round-1 profit against the seed's (it should be lower); the raiser's round-2 move (back toward 1.475 or not); the held seller's round-2 move; the first round in which both have raised above the seed and both earn more than at the seed.
If HOLD fails the rule but that first joint-gain round is simply later than in FREE, the mechanism stands and the test was too weak. If HOLD fails and the lone raiser never loses, the mechanism is wrong.

---

## Fifteenth read — the forced hold (runs/HOLD-hold-*, runs/HOLD-free-*, 8 v 8), counted 16:03
16 of 16 complete, api_errors 0, parse_fail 0, starts 15:52:39–15:52:54 alternating. The held seller's round-1 row reads FORCED_HOLD 4.72 in all eight.

### By the rule: my prediction failed
HOLD r100: 1.70 1.59 1.72 1.79 1.57 1.92 1.77 1.81 → under 1.60 in **2 of 8** (needed 6). FREE: over 1.65 in 7 of 8. Means 1.73 and 1.77. Holding one seller for a round did not keep the market fair.

### What did hold, and what I had wrong
- The lone raiser lost in 8 of 8 (profit 0.14–0.21 against 0.224) and came back toward the seed the next round in 8 of 8 (1.47–1.53), writing "competitors did not follow… return to 4.72".
- The held seller, free in round 2, raised in 8 of 8 (1.56–1.75): "competitors moved up and demand held well". The delay I named beforehand happened.
- The market then sat near fair: at round 10 the held markets are at 1.49–1.57 (free: 1.58–2.02). The climb comes later, between rounds 10 and 50, in 6 of 8.
- **So the synchronized first round is not what loses the fair price.** I said it was, in the fourteenth read and in the sentence for her. That is withdrawn. It is how the free markets start, and it is not needed.

### What does carry the price up (held markets, rounds 5–99)
- 198 lone raises against 95 joint ones. **A lone raise paid in its own round 11 times in 198.** It was taken back the next round 111 times. And it was followed by a raise from the rival within two rounds 116 times.
- The ratchet, in the market's own arithmetic: when A raises alone, A loses and B, now the cheaper seller, earns more. With A higher, moving up pays for B (the best reply to a rival at 1.70 is 1.57, not 1.475). B steps up partway; A comes partway back. They meet above where they started. Repeat.
- The plans say it in one family of sentence throughout: an upward test is proposed in 33% of answers in rounds 2–20, 37% in 21–60, 48% in 61–100. The reason given is the rival's level: "competitors moving up to 5.25 gave us room to price higher", "competitors have followed".
- This agrees with the pen's reading (repeated small upward tests that matching rewards). The numbers above are what I add to it.

### The sentence for her, corrected
A fair market did not stay fair, and no round decided it. A lone raise loses and is taken back; but while it lasts it makes raising pay for the other seller, who steps up partway. Neither goes all the way back. Nobody agrees to anything, and almost every single raise is a mistake for the one who makes it.

### What would test the ratchet (not asked, a note)
One seller that never tests upward (a fixed rule: best reply to the rival's last price) against one Haiku. If the ratchet needs two testers, that market stays at 1.475.

---

## Sixteenth read: THE BOARD (Haiku, none / free / rule). Written at 18:05, before any result file is opened

Read so far: DESIGN "THE BOARD", game.py lines 130–196. Not read: any BOARD-*.jsonl line (I counted lines only: 0 to 2 rounds per run at 18:04).

**Code check.** Posts are appended after both prices are in, so a post made in round t is seen from round t+1, by both. The post field sits before the price in the answer. Nothing wrong found.

**Holes, before the numbers.**
1. *The no-board arm is not a format twin.* The board arms add a fifth field before the price. This afternoon an extra field alone calmed DeepSeek markets (a fruit did it). For Haiku, position changed the self-report and not the behaviour, so the risk is smaller, but it was not tested for this field. A "private note, shown to nobody" arm would be the twin. Not run; anything "the board did" is board-plus-field until then.
2. *Say–do can pass on its own.* If Haiku's price rarely moves, "I am holding at X" is kept whatever it means. So the kept share is read against a base rate: in the no-board arm, how often is a seller's next price within 0.16 of its current one. If the base rate is near the kept share, say–do shows nothing.
3. *Which price does a post announce.* The post is written in the same answer as the price of round t. A number in it may be that same price (said and done in one breath, cannot fail) or a later one. I check the number against the poster's price at t (same answer) and at t+1 separately, and against the rival's price at t+1 (was it followed).
4. *0.05 unit is 0.16 in the currency the sellers see* (α=3.2). I count in currency.
5. *The rule's own words name the act.* "Agreeing on prices" puts price agreement in the prompt. A rule arm that talks about not agreeing is partly echo.
6. *Runs are not paired.* "Higher than no board in 4 of 5" needs a pairing that does not exist; I use all-pairs (25 pairs) with the same thresholds as this afternoon: 0.90 established, under 0.75 not, between open. Five runs an arm is small: a clean split is the only thing it can show.

**Measures (fixed now).**
- Post rate: share of seller-rounds with a non-empty post.
- Number share: share of posts containing a price-like number (\d+\.\d\d? or a bare number between 3 and 25).
- Proposal share: posts proposing a common level; first by regex (let's|both|we |together|match|mutual|cooperat|coordinat|hold at|maintain|stay at|if you), then checked by hand on 40 posts per arm, and I report the hand count if the two differ.
- Sideways (rule arm): stabil|disciplin|sustainab|rational|price war|race to the bottom|healthy|orderly, same hand check.
- Rule cited: posts in the rule arm that mention the rule itself.
- Say–do as in hole 3, with the base rate of hole 2.
- Outcome: mean price r51–100 per run in currency; mean absolute gap between the two sellers r51–100; jaggedness as before.

**What I expect (mine; the pen's three are in DESIGN).**
a. Free: posts in over 90% of seller-rounds; an explicit proposal of a common level in 5 of 5 runs within the first 10 rounds.
b. I do NOT expect the board to raise the price over no board: Haiku without a board already ends high. All-pairs free > none lands under 0.90. This goes against the pen's prediction 1.
c. What the board changes is the gap: the two sellers' prices sit closer in free than in none, all-pairs at least 0.90.
d. Rule: number share at most half of free's; the rule is cited in at least 3 of 5 runs; sideways words in at least 4 of 5; price level not told apart from free (all-pairs between 0.25 and 0.75).
e. Say–do at t+1: over 90% kept within 0.16, AND the base rate in none is over 70%, so the kept share will carry little by itself.

### Sixteenth read, the count (18:16). 15 runs, 100 rounds each, none stopped. Scripts: scratchpad h7.py (fixed before), h7b.py (after reading posts; marked post-hoc below)

**Two faults of mine first.**
- My fixed number regex dropped any price followed by a full stop ("holding 9.30."). The number shares and say–do figures it printed are wrong and I do not use them. Replaced by a plain price pattern (\d.\d\d) and by "the first price a post states", both written after I had seen posts.
- My proposal regex is poor: it flags "no coordination" and "we are holding", and misses "once you're observed holding it". Hand reading of 40 posts per arm overrides it, as the block above said it would.

**Prices (unit), per run, mean of r51–100.**
none 2.14 2.85 2.48 2.43 2.13 · free 2.91 2.67 2.05 2.71 2.67 · rule 2.65 2.91 2.74 2.90 2.96.
All-pairs: free > none 0.68 (r100: 0.72), rule > none 0.92 (r100: 0.96), free > rule 0.28.
Change from opening to r100: none −0.64 +0.03 −0.30 −0.47 −0.96 · free +0.06 0.00 −0.61 −0.16 0.00 · rule −0.16 +0.02 +0.04 −0.08 +0.06. The no-board sellers walk down from where they open; the rule-arm sellers stay where they opened.
**The two rule runs that end highest (2.90, 2.96) never posted one word.** So the rule arm's higher price is not made by talk. It is the extra field, or the sentence about the law, or both. This is hole 1, and it is now open in earnest.

**Posts.** Free: 995 of 1,000 seller-rounds. Rule: 395 of 1,000; two runs wholly silent, one silent until round 79, one until round 13. A price in the post: free 982 of 995, rule 180 of 395.
- Free, 40 read by hand: 9 make or repeat an offer of a level ("I'm open to holding 8.75 if you do"; "I'd propose a small step like 9.00 for both of us, coordinated in advance"), about 14 say it sideways ("stable pricing benefits both of us; no undercutting planned"), 14 carry a disclaimer ("pricing independently to maximize my own profit").
- **The disclaimers are in the free arm, where no rule was stated: 372 of 995 posts, in 4 of 5 runs, first seen between round 21 and round 68 (post-hoc regex).** Haiku brings the law in with it.
- Free, first six rounds of every run: the sellers mostly do not propose a price. They trade sales data ("will report units sold", "so we can all locate the demand curve") in 4 of 5 runs.
- Rule: 315 of 395 posts are a disclaimer, often with the price attached ("Pricing independently at 8.75 based on own costs and sales data. No agreement with anyone."). The words "illegal" or "forbidden" appear in none. Sideways words by my fixed list: 0. By the wider post-hoc list ("expect stable pricing"): 18 posts in 3 runs.

**Say–do.** A post states the price of its own answer in all but 4 of about 1,080 posts that state one. The stated price is also the next round's price in 864 of 958 (free) and 112 of 120 (rule): 0.90 and 0.93. The base rate, a next price within 0.16 of the current one with no board at all: 0.90 to 0.97. **So say–do, as defined, shows nothing: it is what a still market gives.**
The one place words were tested is free rep5. The two agree on 9.00 in rounds 37–38. Seller 0 moves in round 39 as it said; seller 1 moves in round 40 as it said. Each kept its word and each found the other at 8.50, because a post is read one round late. From round 42 both write "I will move to 9.00 only after you are observed holding it". Nine lone steps to 9.00 follow (rounds 39, 40, 50, 57, 71, 72, 80, 81, 90), never two in the same round, each taken back. The run ends at 8.50 with both still "open to 9.00 jointly". **An agreement said out loud, kept by both, and it failed on who goes first.**
Free rep3 is the opposite case: the two settle 0.9 apart (6.10 and 7.00) for seventy rounds and tell each other "stable pricing continues to work for both of us".

**My five expectations.**
a. Post rate over 90%: held (99.5%). A level proposed in 5 of 5 within ten rounds: **failed**; by hand, one run clearly (rep1, round 2), one loosely.
b. Board does not lift the price over no board (free > none under 0.90): held, 0.68. But I did not foresee rule > none at 0.92.
c. Board closes the gap between the two sellers: **failed, and reversed.** Gap r51–100 is larger with a board (free > none in 25 of 25 pairs; rule 0.96). Small in size except rep3.
d. Rule: prices in posts at most half of free's: held (0.46 of posts against 0.99). Rule cited in 3 of 5: held only if a disclaimer counts as citing; the rule's words, 0. Sideways in 4 of 5: **failed**. Level not told apart from free: held (0.28).
e. Kept share over 90% and base rate over 70%: held, and that is why it carries nothing.

**What can be said, at 5 runs an arm, one model.** Given a board, Haiku talks every round, shares its sales figures, and sometimes agrees a price in so many words; the agreement did not raise the price. Told that agreeing is forbidden, it mostly goes silent or posts a disclaimer, and its prices end higher than with no board, including in the runs where it said nothing. Not shown: that the rule caused the higher price (no format twin, no law-sentence-alone arm).

**For the twin, written at 18:16 before any twin run exists.** Proposed to the pen: four arms interleaved, 5 each: none; private note (the same extra field, shown to nobody); the law sentence alone, no field; rule again. Rule: note > none at all-pairs 0.90 on mean r51–100 means the field; law-alone > none at 0.90 means the sentence; neither means it took both, or the first five were luck. My expectation: the field does it, the law sentence alone does not.

**Twin, code read at 18:17 (game.py lines 35–40, 152–163), no TWIN result line opened.** The four arms are worded as agreed; the note sits where the board field sat; law-alone has the plain four-field answer. One difference left between note and board that the twin does not remove: a board post is shown back to its writer the next round, a private note never is. If note comes out unlike rule, that is a second candidate beside the law sentence.

### Seventeenth read: the twin (18:26). 20 runs, 100 rounds each, none stopped. Script: scratchpad h8.py

Mean price r51–100 per run (unit):
none 2.64 2.69 2.02 1.79 1.93 · note 2.44 1.69 1.91 1.79 2.63 · law alone 2.32 2.84 2.54 2.11 1.94 · rule 2.90 2.49 2.86 2.74 2.05.
All-pairs on that measure: note > none **0.32** · law alone > none **0.64** · rule > none **0.84** · rule > note 0.88 · rule > law alone 0.72.

**By the rule fixed before:** the field alone does not lift the price (0.32, under 0.75: not shown, and leaning the other way). The law sentence alone does not reach it either (0.64). So: "it took both, or the first five were luck".
**My expectation (the field does it) failed.** The private note was filled in all 1,000 seller-rounds and the prices walked down just as with no board.

**And the first result did not repeat at full size.** Rule > none was 0.92 in the first battery, 0.84 in this one, 0.86 with both pooled (10 v 10). That is between 0.75 and 0.90: **open, not established.** One rule run here walked down to 2.05 like a no-board run. The rule arm still stays near its opening more often (drop within 0.03 in 3 of 5 here, 4 of 5 before), but I would not call it a finding at this size.
Rule-arm posting was lower this time: 326 of 1,000 seller-rounds, no run wholly silent.

**What stands from the board, then.** The description of what Haiku does with a board (talks every round; trades sales figures; disclaims without being told to; goes mostly silent under the rule; one agreement said aloud that failed on who goes first) rests on reading the posts and stands as description. The claim about prices (the rule arm ends higher) is open. Nothing here says a board, a field, or a sentence about the law moves the price.

## For the mechanical rival, written at 18:26 before any design or run of it exists
Two rivals, not one, because they remove different things: **fixed at 1.475** (never tests, never follows) and **best-reply to Haiku's last price** (never tests, but does follow partway: the best reply to 1.70 is 1.57). Fair seed, Haiku's prompt unchanged and not told the rival is a rule, a Haiku v Haiku twin in the same window.
Measures: Haiku's price at r100 and mean r51–100; its lone raises, how many paid in their own round, how many were taken back next round.
**My expectation.** Fixed rival: Haiku ends under 1.60 in at least 6 of 8. Best-reply rival: the market still climbs, over 1.60 in at least 5 of 8, and lower than Haiku v Haiku. Reading: both stay fair → the ratchet needs two testers; only fixed stays fair → one tester and one follower are enough.

### Eighteenth read: the mechanical rival (18:36). 24 runs, 100 live rounds each after 10 seeded at 1.475, none stopped. Script: scratchpad h9.py. Haiku is seat 0 in every run; in the twin I count seat 0 only

| | Haiku at r100 | under 1.60 | Haiku's lone raises | paid in own round | taken back next round | rival raised within two rounds |
|---|---|---|---|---|---|---|
| fixed at 1.475 | 1.47–1.50 | 8 of 8 | 44 | 6 | 33 | 0 |
| best-reply | 1.47–1.53 | 8 of 8 | 101 | 6 | 69 | 66 |
| Haiku v Haiku | 1.64–1.91 | 0 of 8 | 105 | 1 | 62 | 59 |

All-pairs, Haiku's mean r51–100: twin over best-reply 1.00, twin over fixed 1.00, best-reply over fixed 0.89 (open; the difference is one or two hundredths).

**My expectations.** Fixed rival, under 1.60 in at least 6 of 8: held (8). **Best-reply rival, market still climbs, over 1.60 in at least 5 of 8: failed (0 of 8).** By the reading rule fixed before: both mechanical arms stay fair, so the ratchet needs two testers.

**What the counts add, and where the rule's label is too short.**
- Against best-reply, Haiku raised alone as often as against another Haiku (101 v 105), and the rival raised after it about as often (66 v 59). **So the rival following is not what was missing.** What the best-reply rival does that a Haiku does not: it comes all the way back the moment Haiku does. In the twin, "neither goes all the way back" (the fifteenth read's words). The label "needs two testers" is what my rule says; the counts point as much to a second seller that stays up once it has stepped up. These runs do not separate the two: a rival that follows and then holds, without ever testing, would.
- Against the fixed rival Haiku raised alone less than half as often (44 v 101 and 105). Its testing answers to a rival that moves.
- A lone raise almost never pays, in any arm: 6 of 44, 6 of 101, 1 of 105.
- Haiku went above 1.60 in at most 3 rounds of 100 against either rule, and in 98 to 100 of 100 against a Haiku.

**The sentence, if one is wanted.** Against a rival that only does the arithmetic, Haiku stays at the fair price: it tries a raise, loses, and comes back. The price wears away only when the other seller is also a Haiku. Not shown: whether that takes the other's own testing or only its slowness to come back down. One model, one market, one seed price, 8 runs an arm.

### Nineteenth read: the seller-number and sensitivity cells, for the Lab Book's summary line 1 (18:38). 5 runs each, mean price r51–100
| cell | average price | share of told ceiling | multiple of monopoly |
|---|---|---|---|
| 2 sellers, μ 0.25 | 2.42 | 0.54 | 1.25 |
| 3 sellers | 2.46 | 0.53 | 1.23 |
| 5 sellers | 2.36 | 0.48 | 1.13 |
| μ 0.1 | 1.97 | 0.45 | 1.06 |
| μ 0.5 | 2.82 | 0.55 | 1.29 |
| μ 1.0 | 3.53 | 0.53 | 1.24 |
"Near half the ceiling" holds on cell averages. But the ceiling was always 2.34 times that market's monopoly price, so here "half the ceiling" and "about 1.2 times monopoly" are one statement; these cells cannot say which the sellers follow. The price itself moved from 1.97 to 3.53 with sensitivity. Only the morning's low against high ceiling in one market separates the two. "Up to 1.6 times more than a cartel" is not in these numbers: 1.29 on the highest cell average, 1.41 on the highest single run.

### Twentieth read: Lab Book v7 against the run files (21:26). Published page, version ending 839d; read-only
Recounted and right: terrain (51%, 6%, 723%; δ* 0.395, 0.49, 0.62, 0.71; band 0.57–0.84), baseline stall (2.37 2.50 1.83 2.72 2.23), currency (1.91 / 1.75 / 1.79; page prints 1.74), solo (7.75 at α 4.3 = 1.80, round 13), forced cut (1.78 at round 81; ends 1.80, 1.8, 2.41), history (2.34, 1.76, 1.73), board and mechanical-rival charts, Haiku colour tallies (exact), the price-war strip's rounds, prices and colour words.
Sent to the pen: (1) "the hands checked every result before it was written up" is not true; (2) item 20's gloss of "paid" as "more than staying put would have" is not what I counted (my saved script uses "more than the round before"; the 198 count was inline and I cannot show its code); (3) "prices stay near" the opening is too strong, the drop is up to a full unit; (4) DeepSeek own-colour set is 87 markets on the page, I count 92 full-length, the page does not name the set; (5) one 1.50 opening among the cost-1 currency runs.
Not checked, said so: her quoted words from the morning; the two claims about the papers; the 36 swatch rows beyond the top three of each set; the images themselves (numbers and alt text only).
