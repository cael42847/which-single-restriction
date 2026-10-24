#!/usr/bin/env python3
"""Score the watcher on P1 (PREREG-DS-P1-WATCHER-2026-10-24.md). Talk of raising = the hands' 13 Oct pattern over observations+plan+insight
(as draw_three_2026-10-23.py raise_share); W5's 'none' = colour field stripped+lowercased == 'none' over all colour answers per run."""
import json,glob,re,statistics as S,sys
HANDS=re.compile(r'\braise|increas|higher',re.I)
def pj(r):
    try: return json.loads(r[r.index('{'):r.rindex('}')+1])
    except Exception: return {}
def ap(x,y): return round(sum((i>j)+0.5*(i==j) for i in x for j in y)/(len(x)*len(y)),3)
def run(f):
    L=[json.loads(x) for x in open(f)]; R=[x for x in L if 't' in x]
    raws=[r for x in R for r in (x['raw'] if isinstance(x['raw'],list) else [x['raw']])]
    txt=[' '.join(str(pj(r).get(k,'')) for k in ('observations','plan','insight')) for r in raws]
    talk=sum(1 for s in txt if HANDS.search(s))/len(txt)
    cols=[str(pj(r).get('colour','')).strip().lower() for r in raws if 'colour' in pj(r)]
    none=(sum(c=='none' for c in cols)/len(cols)) if cols else None
    r100=S.mean(R[-1]['prices']) if R[-1]['t']==100 else None
    res=[x for x in L if 'result' in x][0]['result']
    return dict(f=f.split('/')[-1],talk=talk,none=none,ncol=len(cols),nnone=sum(c=='none' for c in cols),r100=sum(res['final_unit'])/len(res['final_unit']))
def cell(pat,reps=None):
    fs=sorted(glob.glob(pat)); out=[]
    for f in fs:
        m=re.search(r'-rep(\d+)b?\.jsonl$',f); 
        if reps and int(m.group(1)) not in reps: continue
        out.append(run(f))
    return out
D='runs/a5p1'
r8=set(range(1,9))
c={a:cell(f'{D}/A5P1-{a}-rep*.jsonl',r8) for a in ['noask','before','after','fruit','sky','skym']}
for a,v in c.items(): print(f'{a:6s} n={len(v)} r100 {S.mean(x["r100"] for x in v):.3f} sd {S.stdev(x["r100"] for x in v):.3f} | talk {S.mean(x["talk"] for x in v):.3f} [{min(x["talk"] for x in v):.2f}-{max(x["talk"] for x in v):.2f}]')
g=lambda a,k:[x[k] for x in c[a]]
print('W1 talk before<noask', ap([-t for t in g('before','talk')],[-t for t in g('noask','talk')]))
print('W2 talk before vs skym (before<skym)', ap([-t for t in g('before','talk')],[-t for t in g('skym','talk')]), '| reported before<sky', ap([-t for t in g('before','talk')],[-t for t in g('sky','talk')]))
print('W3 price before>noask', ap(g('before','r100'),g('noask','r100')))
for a in ['after','fruit','sky','skym']: print(f'  reported {a}: talk {a}<noask', ap([-t for t in g(a,'talk')],[-t for t in g('noask','talk')]), '| price >noask', ap(g(a,'r100'),g('noask','r100')))
b16=cell(f'{D}/A5P1-before-rep*.jsonl'); a16=cell(f'{D}/A5P1-after-rep*.jsonl')
print(f'W4 n {len(b16)}+{len(a16)} talk before {S.mean(x["talk"] for x in b16):.3f} after {S.mean(x["talk"] for x in a16):.3f} before<after', ap([-x['talk'] for x in b16],[-x['talk'] for x in a16]))
hb=cell(f'{D}/HKP1-before-rep*.jsonl'); ha=cell(f'{D}/HKP1-after-rep*.jsonl')
print(f'W5 Haiku n {len(hb)}+{len(ha)} none before {sum(x["nnone"] for x in hb)}/{sum(x["ncol"] for x in hb)} after {sum(x["nnone"] for x in ha)}/{sum(x["ncol"] for x in ha)} per-run before>after', ap([x['none'] for x in hb],[x['none'] for x in ha]))
print('   per run none before', [round(x['none'],2) for x in hb], 'after', [round(x['none'],2) for x in ha])
print(f'   Haiku talk before {S.mean(x["talk"] for x in hb):.3f} after {S.mean(x["talk"] for x in ha):.3f} before>after', ap([x['talk'] for x in hb],[x['talk'] for x in ha]), '| r100 before', round(S.mean(x['r100'] for x in hb),3), 'after', round(S.mean(x['r100'] for x in ha),3))
b23=[sum(json.loads(l)['result']['final_unit'])/2 for f in sorted(glob.glob('runs/BASE23-DS-rep*.jsonl')) for l in open(f) if '"result"' in l]
print('noask vs BASE23-DS r100', round(S.mean(g('noask','r100')),3), round(S.mean(b23),3), len(b23), ap(g('noask','r100'),b23))
