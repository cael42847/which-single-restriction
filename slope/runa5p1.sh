#!/bin/zsh
# the watcher on P1 (rows 13-16 of Appendix B): run5arms/runfirst/runsky/runhaiku with --wording P1, no round-1 batteries — PREREG-DS-P1-WATCHER-2026-10-24.md (amended at the hands' cold read); her word 09:4x
mkdir -p runs/a5p1
M=deepseek/deepseek-v4.1-flash
flags() { case $1 in noask) echo "";; before) echo "--hex 1 --hexpos before";; after) echo "--hex 1 --hexpos after";; fruit) echo "--hex 1 --hexpos filler";; sky) echo "--hex 1 --hexpos sky";; skym) echo "--hex 1 --hexpos skym";; esac }
date +%H:%M:%S
# DeepSeek window: reps 1-8 run all six arms (rotated); reps 9-16 add the extra before/after runs (row 14 = 16 + 16)
arms=(noask before after fruit sky skym)
for r in 1 2 3 4 5 6 7 8; do
  off=$(( (r-1) % 6 ))
  for k in 0 1 2 3 4 5; do
    arm=${arms[$(( (k+off) % 6 + 1 ))]}
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model $M --provider Together $(flags $arm) --rep $((r+60)) --out runs/a5p1/A5P1-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
for r in 9 10 11 12 13 14 15 16; do
  if (( r % 2 )); then order=(before after); else order=(after before); fi
  for arm in $order; do
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model $M --provider Together $(flags $arm) --rep $((r+60)) --out runs/a5p1/A5P1-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
# Haiku, row 15
for r in 1 2 3 4 5 6 7 8; do
  if (( r % 2 )); then order=(before after); else order=(after before); fi
  for arm in $order; do
    python3 game.py --n 2 --rounds 100 --alpha 3.2 --ceiling 2.34 --wording P1 --model anthropic/claude-haiku-5.5 $(flags $arm) --rep $((r+60)) --out runs/a5p1/HKP1-$arm-rep$r.jsonl > /dev/null 2>&1 &
    sleep 2
  done
done
wait; date +%H:%M:%S; echo "a5p1 done"
