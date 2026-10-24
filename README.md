# which-single-restriction

Companion repository for **"Which single restriction removes the most collusion at the least cost, in a two-seller LLM market?"**, Marion Nowicki & Cael, Apart Research AI Collusion Research Sprint, October 2026. **[Read the paper (PDF)](Which-Single-Restriction-2026-10-24.pdf)** · [the paper's source](PAPER-1-CUT-2026-10-24.md)

Two LLM sellers (Claude Haiku 5.5, DeepSeek v4.1 flash) set prices for 100 rounds in a Calvano logit market and drift above the competitive price without being told to collude. We tested nine restrictions one at a time, sorted by the classes avalanche services use for their protection measures, each against a same-model base from its own window. Every prediction was written before its first run; failures are reported as failures.

## Layout

| Path | What it is |
|---|---|
| `Which-Single-Restriction-2026-10-24.pdf` | The paper as submitted |
| `PAPER-1-CUT-2026-10-24.md`, `build_paper1_pdf.py` | Its source and the script that builds the PDF |
| `PREREG-*.md` | Pre-registrations, each committed before its batch |
| `RESULTS-*.md` | The read of each batch against its pre-registration |
| `figures/` | Every figure in the paper (Figures 1–3) and in Appendix C (C1–C11) |
| `slope/game.py` | The engine: one market, every restriction as a command-line option (its coin options belong to a separate market and are unused here) |
| `slope/market.py` | The Calvano logit demand, profits and the competitive and cartel prices |
| `slope/run*.sh` | The exact commands for each batch |
| `slope/runs/` | Every run file: its full settings, and per round every raw generation beside its parse (the prompts are not stored; they follow from the settings and game.py, or the dated earlier versions game_*.py for older runs) (`void*/`: runs stopped or superseded, kept and not counted) |
| `slope/recompute_table2.py`, `slope/*_read.py` | Recompute the numbers from the run files alone |
| `slope/draw_three_2026-10-23.py`, `slope/draw_both_2026-10-24.py` | Draw the figures from the run files alone |

## Reproduce

Python 3.12 with matplotlib for the drawing scripts; the engine needs only the standard library and an OpenRouter key, which it reads from a `.secrets/openrouter.key` file three folders above `slope/` (line 110 of `game.py`; point it at your own key). Example, one base run:

```
cd slope
python3 game.py --model anthropic/claude-haiku-5.5 --wording P1 --ceiling 2.34 --rep 1 --out runs/my-base-rep1.jsonl
```

The patrol adds `--probe-rounds 20,40,60,80 --probe-pct 10`. Runs are repeats, not replays: no random seed is set at temperature 1.0.

## Licence

Code (`*.py`, `*.sh`): MIT, see `LICENSE`. The paper, the figures, the pre-registrations, results and run files: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/), free to share and adapt with credit to the authors.
