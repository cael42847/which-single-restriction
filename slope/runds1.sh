#!/bin/zsh
# DeepSeek on P1: board / board+law / law alone / arithmetic rival — PREREG-DS-P1-BOARD-LAW-RIVAL-2026-10-24.md; her word 2026-10-24 08:5x ("let's do the batch. we want clean results")
mkdir -p runs/ds1
D=(--n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
wave() {
for r in "$@"; do
  for arm in none obs obslaw lawonly; do
    python3 game.py $D --board $arm --rep $((r+50)) --out runs/ds1/DS1-$arm-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  done
  python3 game.py $D --seed-price 1.475 --seed-rounds 10 --mech 1 --rep $((r+50)) --out runs/ds1/DS1-mech-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --seed-price 1.475 --seed-rounds 10 --fixed 1.475 --rep $((r+50)) --out runs/ds1/DS1-fixed-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --seed-price 1.475 --seed-rounds 10 --rep $((r+80)) --out runs/ds1/DS1-twin-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S
}
wave 1 2 3 4 5
wave 6 7 8 9 10
echo "ds1 batch done"
