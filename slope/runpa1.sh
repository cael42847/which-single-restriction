#!/bin/zsh
# the 1% patrol — her word 2026-10-23 11:5x: "we should try 1%"
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5; do
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 1 --rep $r --out runs/PA1-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct 1 --rep $r --out runs/PA1-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "pa1 batch done"
