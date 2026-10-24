#!/bin/zsh
B=(--rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
for r in 1 2 3 4 5; do
  python3 game.py --n 2 $B --seed-price 1.475 --seed-rounds 10 --rep $r --out runs/PM-HF-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 2 $B --seed-price 2.50 --seed-rounds 10 --rep $r --out runs/PM-HH-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 3 $B --rep $r --out runs/PM-N3-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 5 $B --rep $r --out runs/PM-N5-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 2 --mu 0.1 $B --rep $r --out runs/PM-MU1-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 2 --mu 0.5 $B --rep $r --out runs/PM-MU5-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 2 --mu 1.0 $B --rep $r --out runs/PM-MU10-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py --n 2 $B --models anthropic/claude-haiku-5.5,deepseek/deepseek-v4.1-flash --provider Together --rep $r --out runs/PM-MX-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M
