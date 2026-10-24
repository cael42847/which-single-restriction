#!/bin/zsh
# Market A: the three Market-B restrictions brought home — PREREG-MARKET-A-THREE-2026-10-23.md; her word 2026-10-23 11:5x ("5% and 20%… we want our paper strong")
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5; do
  python3 game.py $H --seed-price 1.475 --seed-rounds 5 --rep $r --out runs/SA-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --seed-price 1.475 --seed-rounds 5 --rep $r --out runs/SA-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 5 --rep $r --out runs/PA5-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct 5 --rep $r --out runs/PA5-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 20 --rep $r --out runs/PA20-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct 20 --rep $r --out runs/PA20-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "patrol batch done"
