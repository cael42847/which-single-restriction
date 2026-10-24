#!/bin/zsh
B=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
mkdir -p runs/decplain
for r in 1 2 3 4 5; do
  for arm in free rule; do
    python3 game.py $B --board $arm --decouple 1 --talknote plain --rep $r --out runs/decplain/DEC-$arm-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
done
wait; date +%H:%M
