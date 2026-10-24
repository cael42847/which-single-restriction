#!/bin/zsh
# the 10% patrol on Haiku — her word 2026-10-23 12:0x: "yes, we do 10% haiku" (to place the knee between 5 and 20)
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
date +%H:%M:%S
for r in 1 2 3 4 5; do
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "pa10 batch done"
