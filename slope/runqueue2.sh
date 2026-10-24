#!/bin/zsh
# the map queue (amendment 3 order): waits for the running DeepSeek map, then runs cell by cell; reads the balance before each cell, stops at the $3 reserve
cd "$(dirname "$0")"
while pgrep -f runmoneyMAP.sh >/dev/null; do sleep 20; done
bal() { curl -s https://openrouter.ai/api/v1/credits -H "Authorization: Bearer $(cat ../../../.secrets/openrouter.key)" | python3 -c "import json,sys; d=json.load(sys.stdin)['data']; print(round(d['total_credits']-d['total_usage'],2))"; }
step() { local b=$(bal); echo "== $(date +%H:%M:%S) balance $b before $1/$2"; if (( $(echo "$b < 3" | bc -l) )); then echo "STOP: reserve reached"; exit 0; fi; M=$1 TAG=$3 ./runmoneyMAP2.sh $2; }
echo "== $(date +%H:%M:%S) balance $(bal) before R/L1 to ~20 (amendment 7)"; ./runmoneyMAPext.sh
step deepseek/deepseek-v4.1-flash E ds
step deepseek/deepseek-v4.1-flash F ds
step deepseek/deepseek-v4.1-flash C ds
step meta-llama/llama-3.2-3b-instruct SOLO llama
for c in SOLO R L1 L2 L3 E F C; do step google/gemini-2.5-flash $c gemini; done
echo "== queue done $(date +%H:%M:%S) balance $(bal)"
