#!/bin/zsh
# the four established cells to n=20 — her yes 2026-10-23 14:0x (symmetry: all four or none)
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 11 12 13 14 15 16 17 18 19 20; do
  python3 game.py $H --seed-price 1.475 --seed-rounds 5 --rep $r --out runs/SA-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 20 --rep $r --out runs/PA20-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "estab20 batch done"
