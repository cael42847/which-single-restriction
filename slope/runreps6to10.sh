#!/bin/zsh
# five more runs per cell (reps 6–10) — her word 2026-10-23 12:1x: "so we should do 5 more runs"; the 3-of-5 fence (the hands)
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 6 7 8 9 10; do
  python3 game.py $H --rep $r --out runs/BASE23-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --rep $r --out runs/BASE23-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --seed-price 1.475 --seed-rounds 5 --rep $r --out runs/SA-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --seed-price 1.475 --seed-rounds 5 --rep $r --out runs/SA-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  for d in 1 2 3 5 20; do
    python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct $d --rep $r --out runs/PA$d-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
    python3 game.py $D --probe-rounds 20,40,60,80 --probe-pct $d --rep $r --out runs/PA$d-DS-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
  python3 game.py $H --probe-rounds 20,40,60,80 --probe-pct 10 --rep $r --out runs/PA10-HK-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "reps 6-10 batch done"
