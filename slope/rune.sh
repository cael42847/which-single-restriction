#!/bin/zsh
mkdir -p runs/e
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model deepseek/deepseek-v4.1-flash --provider Together)
for r in 1 2 3 4 5; do
  for arm in none obs obslaw; do
    python3 game.py $H --board $arm --rep $r --out runs/e/HK-$arm-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --board $arm --rep $r --out runs/e/DS-$arm-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
done
wait; date +%H:%M
