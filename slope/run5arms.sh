#!/bin/zsh
# five arms x 8, order rotated per repeat, staggered starts; then the round-1 battery
M=deepseek/deepseek-v4.1-flash
arms=(noask before after fruit sky)
flags() { case $1 in noask) echo "";; before) echo "--hex 1 --hexpos before";; after) echo "--hex 1 --hexpos after";; fruit) echo "--hex 1 --hexpos filler";; sky) echo "--hex 1 --hexpos sky";; esac }
for r in 1 2 3 4 5 6 7 8; do
  off=$(( (r-1) % 5 ))
  for k in 0 1 2 3 4; do
    arm=${arms[$(( (k+off) % 5 + 1 ))]}
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together $(flags $arm) --rep $r --out runs/A5-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait
for arm in $arms; do for r in $(seq 1 25); do
  python3 game.py --n 2 --rounds 1 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together $(flags $arm) --rep $r --out runs/R1-$arm-rep$r.jsonl > /dev/null 2>&1 &
done; done
wait
date +%H:%M
