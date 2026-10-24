#!/bin/zsh
for r in 1 2 3 4 5 6 7 8; do
  if (( r % 2 )); then order=(before after); else order=(after before); fi
  for arm in $order; do
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P2 --model anthropic/claude-haiku-5.5 --hex 1 --hexpos $arm --rep $r --out runs/HK-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait; date +%H:%M
