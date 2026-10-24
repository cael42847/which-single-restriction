#!/bin/zsh
B=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --seed-price 1.475 --seed-rounds 10)
for r in 1 2 3 4 5 6 7 8; do
  python3 game.py $B --hold 1 --rep $r --out runs/HOLD-hold-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $B --rep $r --out runs/HOLD-free-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M
