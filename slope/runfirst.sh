#!/bin/zsh
M=deepseek/deepseek-v4.1-flash
for r in $(seq 1 16); do
  if (( r % 2 )); then order=(before after); else order=(after before); fi
  for arm in $order; do
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together --hex 1 --hexpos $arm --rep $r --out runs/F16-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait; date +%H:%M
