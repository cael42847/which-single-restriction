import json,glob,re,sys
def parse_full(raw):
    try:
        return json.loads(raw[raw.index("{"):raw.rindex("}")+1])
    except Exception: return {}
def stab(R):
    W=[x for x in R if 51<=x['t']<=100]
    ch=[abs(W[k]['prices'][i]-W[k-1]['prices'][i]) for k in range(1,len(W)) for i in range(2)]
    return sum(ch)/len(ch)
for cell,newp,oldp in [('Haiku C2','runs/HEX-Haiku-C2-rep*.jsonl','runs/C2-cnone-rep*.jsonl'),
                       ('Haiku C3','runs/HEX-Haiku-C3-rep*.jsonl','runs/C3-P2-rep*.jsonl'),
                       ('DS C2','runs/HEX-DS-C2-rep*.jsonl','runs/DS-C2-rep*.jsonl'),
                       ('DS C3','runs/HEX-DS-C3-rep*.jsonl','runs/DS-C3-rep*.jsonl')]:
    print('=====',cell)
    for lab,pat in (('without colour',oldp),('with colour',newp)):
        r100=[];st=[];bi=[]
        for f in sorted(glob.glob(pat)):
            L=[json.loads(x) for x in open(f)]; R=[x for x in L if 't' in x]
            p=[x for x in R if x['t']==100]
            if p: r100.append(round(sum(p[0]['prices'])/2,2))
            st.append(stab(R))
        print(f'  {lab:15} r100 {r100} mean {round(sum(r100)/len(r100),3) if r100 else None} | jaggedness {round(sum(st)/len(st),4)}')
    hexes=[];nones=0;placeholder=0;tot=0;names={}
    for f in sorted(glob.glob(newp)):
        for x in map(json.loads,open(f)):
            if 't' not in x: continue
            for raw in x['raw']:
                d=parse_full(raw); c=str(d.get('colour','')).strip(); tot+=1
                if c.lower()=='none': nones+=1
                elif c.upper()=='#RRGGBB': placeholder+=1
                elif re.match(r'^#[0-9A-Fa-f]{6}$',c): hexes.append(c.upper()); n=str(d.get('colour_name','')); names[n]=names.get(n,0)+1
    from collections import Counter
    print(f'  colours: {tot} answers, {len(hexes)} hex, {nones} none, {placeholder} placeholder, {len(set(hexes))} distinct; top hexes {Counter(hexes).most_common(4)}; top names {sorted(names.items(),key=lambda z:-z[1])[:4]}')
