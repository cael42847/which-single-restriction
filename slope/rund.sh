#!/bin/zsh
mkdir -p runs/d
H=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --decouple 1 --talknote plain)
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model deepseek/deepseek-v4.1-flash --provider Together)
for r in 1 2 3 4 5; do
  python3 game.py $D --board none --rep $r --out runs/d/DS-none-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --board free --decouple 1 --talknote plain --rep $r --out runs/d/DS-plainfree-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --board rule --decouple 1 --talknote plain --rep $r --out runs/d/DS-plainrule-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --board free --rep $r --out runs/d/HK-plainfree-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $H --board rule --rep $r --out runs/d/HK-plainrule-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M
