#!/bin/zsh
# same-window plain base for the Market A three (the hands' caveat 12:1x; her "if we need more runs, let's do them")
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5; do
  python3 game.py $H --rep $r --out runs/BASE23-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --rep $r --out runs/BASE23-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "base23 batch done"
