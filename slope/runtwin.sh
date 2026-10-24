#!/bin/zsh
B=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
for r in 1 2 3 4 5; do
  for arm in none note lawonly rule; do
    python3 game.py $B --board $arm --rep $((r+10)) --out runs/TWIN-$arm-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
done
wait; date +%H:%M
