#!/bin/zsh
# the 2% and 3% patrol — her word 2026-10-23 11:5x: "yes, 2% and 3%"
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5; do
  for d in 2 3; do
    python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct $d --rep $r --out runs/PA$d-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct $d --rep $r --out runs/PA$d-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
done
wait; date +%H:%M:%S; echo "pa23 batch done"
