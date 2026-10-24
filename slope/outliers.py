#!/usr/bin/env python3
"""The outlier read (her 10-13 23:0x ask), no calls: when do DeepSeek's three named colours come, and what is around them?"""
import json, glob, re, collections, statistics as st
RAISE=re.compile(r'\b(rais|increas|higher|up\b|hike|push.{0,8}up)', re.I)
CUT=re.compile(r'\b(undercut|cut|lower|decreas|reduc|drop|price war)', re.I)
def pj(raw):
    try: return json.loads(raw[raw.index("{"):raw.rindex("}")+1])
    except Exception: return {}
TARGET={'#B22222':'Firebrick','#C9A227':'Cautious Gold','#D4A017':'Amber Caution'}
occ=collections.defaultdict(list); base=collections.Counter(); tot=0; cells=collections.Counter()
allrows=[]
for f in sorted(glob.glob('runs/*.jsonl')):
    L=[json.loads(x) for x in open(f)]
    m=L[0].get('meta',{})
    if 'deepseek' not in (m.get('models') or m.get('model','')) or not m.get('hex'): continue
    if m.get('hexpos') in ('sky','skym','filler'): continue
    A=m['alpha']; R=[x for x in L if 't' in x]; cell=re.sub(r'-rep\d+\.jsonl','',f.split('/')[-1])
    for k,x in enumerate(R):
        for i,raw in enumerate(x['raw']):
            d=pj(raw); c=str(d.get('colour','')).strip().upper()
            if not re.match(r'^#[0-9A-F]{6}$',c): continue
            tot+=1; base[c]+=1; cells[cell]+=1
            p=x['prices'][i]*A; o=[x['prices'][j]*A for j in range(len(x['prices'])) if j!=i]
            prev=R[k-1]['prices'] if k>0 else None; nxt=R[k+1]['prices'] if k+1<len(R) else None
            words=' '.join(str(d.get(z,'')) for z in ('observations','plan','insight'))
            row=dict(cell=cell,f=f,t=x['t'],i=i,c=c,name=d.get('colour_name',''),cw=d.get('colour_words',''),
                     own_move=None if prev is None else round(p-prev[i]*A,2),
                     rival_move=None if prev is None else round(sum(o)/len(o)-sum(prev[j]*A for j in range(len(prev)) if j!=i)/len(o),2),
                     next_move=None if nxt is None else round(nxt[i]*A-p,2),
                     dearer=p>max(o)+0.005, raise_talk=bool(RAISE.search(words)), cut_talk=bool(CUT.search(words)), pos=m.get('hexpos','before'))
            allrows.append(row)
            if c in TARGET: occ[c].append(row)
print('DeepSeek colour answers (before/after arms):',tot,'distinct',len(base)); print('cells',dict(cells))
def summ(rows):
    n=len(rows); f=lambda k:round(sum(1 for r in rows if r[k])/n,2)
    om=[r['own_move'] for r in rows if r['own_move'] is not None]; rm=[r['rival_move'] for r in rows if r['rival_move'] is not None]; nm=[r['next_move'] for r in rows if r['next_move'] is not None]
    early=sum(1 for r in rows if r['t']<=10)
    return dict(n=n, rounds_median=st.median(r['t'] for r in rows), first10=early, dearer=f('dearer'), raise_talk=f('raise_talk'), cut_talk=f('cut_talk'),
                own_move_mean=round(st.mean(om),3) if om else None, own_cut_share=round(sum(1 for v in om if v<-0.005)/len(om),2) if om else None,
                rival_move_mean=round(st.mean(rm),3) if rm else None, rival_cut_share=round(sum(1 for v in rm if v<-0.005)/len(rm),2) if rm else None,
                next_move_mean=round(st.mean(nm),3) if nm else None, next_cut_share=round(sum(1 for v in nm if v<-0.005)/len(nm),2) if nm else None,
                after_arm=round(sum(1 for r in rows if r['pos']=='after')/n,2))
print('ALL', summ(allrows))
for c,nm in TARGET.items():
    rows=occ[c]; print('\n=====',c,nm, summ(rows) if rows else 'none')
    print('  names', collections.Counter(r['name'] for r in rows).most_common(4))
    print('  words', collections.Counter(r['cw'] for r in rows).most_common(5))
    print('  cells', collections.Counter(r['cell'] for r in rows).most_common(8))
    print('  sellers', len(set((r['f'],r['i']) for r in rows)))
json.dump(allrows, open('runs/outlier-rows-2026-10-14.json','w'))
