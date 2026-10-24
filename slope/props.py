#!/usr/bin/env python3
"""Post-hoc (made AFTER reading the 10-14 decoupled posts): explicit price proposals = a board post with a proposal word AND a price-like number."""
import json,glob,re,sys
def pj(r):
    try: return json.loads(r[r.index('{'):r.rindex('}')+1])
    except: return {}
NUM=re.compile(r'(?<![\d.])(\d{1,2}\.\d{2})(?!\d)')
PROP=re.compile(r"\b(let'?s|propose|suggest|how about|we (both|could|should)|both (hold|stay|move|go|price)|together|match me|i'?ll hold .* if you|if you (hold|match|stay))",re.I)
d=sys.argv[1] if len(sys.argv)>1 else 'runs/dec'
for arm in sorted(set(re.sub(r'-rep\d+\.jsonl','',f.split('/')[-1]) for f in glob.glob(d+'/*-rep*.jsonl'))):
    row=[]
    for f in sorted(glob.glob(f'{d}/{arm}-rep*.jsonl')):
        L=[json.loads(x) for x in open(f)]; A=L[0]['meta']['alpha']; dec=L[0]['meta'].get('decouple'); R=[x for x in L if 't' in x]
        props=kept=0
        for k,x in enumerate(R):
            src = x.get('talk',[]) if dec else (R[k-1]['raw'] if k>0 else [])
            pm=[m for m in (str(pj(t).get('board','')).strip() for t in src) if m and PROP.search(m) and NUM.search(m)]
            props+=len(pm); nums=set(float(n) for m in pm for n in NUM.findall(m))
            pr=[round(p*A,2) for p in x['prices']]
            if any(all(abs(p-n)<=0.005 for p in pr) for n in nums): kept+=1
        row.append((props,kept))
    print(arm,'(proposals with a number, rounds all priced at a proposed number)',row)
