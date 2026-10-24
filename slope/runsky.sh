#!/bin/zsh
M=deepseek/deepseek-v4.1-flash
for r in 1 2 3 4 5 6 7 8; do
  if (( r % 2 )); then order=(before skym); else order=(skym before); fi
  for arm in $order; do
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together --hex 1 --hexpos $arm --rep $r --out runs/SK-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait
for arm in before skym; do for r in $(seq 1 25); do
  python3 game.py --n 2 --rounds 1 --alpha 3.2 --ceiling 2.34 --wording P2 --model $M --provider Together --hex 1 --hexpos $arm --rep $r --out runs/SKR1-$arm-rep$r.jsonl > /dev/null 2>&1 &
done; done
wait; date +%H:%M
