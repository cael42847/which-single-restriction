#!/bin/zsh
# the instruction cells against today's base — her yes 2026-10-23 22:3x ("we do it all now"); PREREG-SAMEDAY-INSTRUCTIONS-2026-10-23.md
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for wave in "1 2 3 4 5 6 7 8 9 10" "11 12 13 14 15 16 17 18 19 20"; do
  for r in ${=wave}; do
    python3 game.py $H --wording P2 --rep $r --out runs/SD-P2-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $H --ceiling none --rep $r --out runs/SD-NC-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --wording P2 --rep $r --out runs/SD-P2-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --ceiling none --rep $r --out runs/SD-NC-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
  wait; date +%H:%M:%S; echo "wave done"
done
echo "sameday batch done"
