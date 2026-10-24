#!/bin/zsh
B=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --seed-price 1.475 --seed-rounds 10)
for r in 1 2 3 4 5 6 7 8; do
  python3 game.py $B --fixed 1.475 --rep $r --out runs/MECH-fixed-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $B --mech 1 --rep $r --out runs/MECH-br-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $B --rep $((r+30)) --out runs/MECH-twin-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M
