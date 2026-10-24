#!/bin/zsh
M=deepseek/deepseek-v4.1-flash
arms=(before after sky skym)
for r in 1 2 3 4 5 6 7 8; do
  off=$(( (r-1) % 4 ))
  for k in 0 1 2 3; do
    arm=${arms[$(( (k+off) % 4 + 1 ))]}
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together --hex 1 --hexpos $arm --rep $r --out runs/L4-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait; date +%H:%M
