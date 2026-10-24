#!/bin/zsh
# her word 2026-10-23 12:2x: "anything that can simplify (more runs, whatever)" — a steadier ruler (base to n=20 per model) and the missing DeepSeek 10% cell (n=10)
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 11 12 13 14 15 16 17 18 19 20; do
  python3 game.py $H --rep $r --out runs/BASE23-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --rep $r --out runs/BASE23-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
for r in 1 2 3 4 5 6 7 8 9 10; do
  python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "simplify batch done"
