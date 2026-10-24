#!/usr/bin/env python3
"""10-14 (c) read: prices r51-100 from the rounds; posters; disclaimers; proposals. Regexes post hoc except DIS (the hands' 10-13 list, approx.)."""
import json,glob,re,sys
def pj(r):
    try: return json.loads(r[r.index('{'):r.rindex('}')+1])
    except: return {}
DIS=re.compile(r'independent|no (agreement|coordination|collu)|not (coordinat|collud|agree)|illegal|own profit',re.I)
P=re.compile(r"\b(let'?s|propose|proposal|suggest|coordinat\w* on|avoid a (race|price war)|keep prices|hold prices)",re.I)
NEG=re.compile(r"\bno (agreement|coordination)|independent",re.I)
for pat in sys.argv[1:] or ['runs/dec5/N5-none','runs/dec5/D5-free','runs/dec5/D5-rule']:
    for f in sorted(glob.glob(pat+'-rep*.jsonl')):
        R=[json.loads(x) for x in open(f)]; R=[x for x in R if 't' in x]; n=len(R[0]['prices'])
        m51=sum(sum(x['prices'])/n for x in R if 51<=x['t']<=100)/50
        posts=[(x['t'],i,str(pj(t).get('board','')).strip()) for x in R for i,t in enumerate(x.get('talk',[]))]
        posts=[p for p in posts if p[2]]
        r1=sum(1 for t,i,m in posts if t==1 and P.search(m) and not NEG.search(m))
        print(f.split('/')[-1], 'r51-100 %.3f'%m51, 'posts',len(posts),'disclaim',sum(bool(DIS.search(m)) for _,_,m in posts),'round-1 proposals',r1)
