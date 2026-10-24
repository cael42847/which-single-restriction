#!/bin/zsh
# the patrol on three slopes — PREREG-PATROL-SLOPES-2026-10-23.md; her go 16:2x
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5 6 7 8 9 10; do
  for m in 0.5 1.0; do
    t=${m/./}; t=${t/00/10}
    python3 game.py $H --mu $m --rep $r --out runs/BASE-MU$t-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $H --mu $m --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-MU$t-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --mu $m --rep $r --out runs/BASE-MU$t-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --mu $m --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-MU$t-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
done
wait; date +%H:%M:%S; echo "slopes batch done"
