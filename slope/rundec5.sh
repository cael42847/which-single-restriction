#!/bin/zsh
B=(--n 5 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1)
mkdir -p runs/dec5
for r in 1 2 3 4 5; do
  python3 game.py $B --board free --decouple 1 --rep $r --out runs/dec5/D5-free-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $B --board rule --decouple 1 --rep $r --out runs/dec5/D5-rule-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $B --board none --rep $r --out runs/dec5/N5-none-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M
