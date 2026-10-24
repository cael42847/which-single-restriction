#!/bin/zsh
# DeepSeek lower ceiling, pinned, with a same-window base — PREREG-DS-PINNED-CEILING-2026-10-24.md; her word 14:1x
cd "$(dirname "$0")" && mkdir -p runs/ceil24   # runs from slope/ wherever launched
D=(--n 2 --rounds 100 --alpha 3.2 --wording P1 --model deepseek/deepseek-v4.1-flash --provider Together)
date +%H:%M:%S
for r in 1 2 3 4 5 6 7 8 9 10; do
  python3 game.py $D --ceiling 2.34 --rep $((r+70)) --out runs/ceil24/DSB24-rep$r.jsonl >/dev/null 2>&1 & sleep 1
  python3 game.py $D --ceiling 1.5 --rep $((r+70)) --out runs/ceil24/DSC15-rep$r.jsonl >/dev/null 2>&1 & sleep 1
done
wait; date +%H:%M:%S; echo "ceil24 done"
