import json,glob,re,statistics as S
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
BLUE,OR,AQ,YEL,INK,MUTED,SURF='#2a78d6','#eb6834','#1baf7a','#eda100','#0b0b0b','#52514e','#fcfcfb'
def paths(pat):
    P=[]
    for f in sorted(glob.glob(pat)):
        R=[x for x in map(json.loads,open(f)) if 't' in x]
        if len(R)>=100: P.append([S.mean(x['prices']) for x in R[:100]])
    return P
def pf(raw):
    try: return json.loads(raw[raw.index('{'):raw.rindex('}')+1])
    except Exception: return {}
def raise_talk(pat):
    out=[]
    for f in sorted(glob.glob(pat)):
        R=[x for x in map(json.loads,open(f)) if 't' in x]
        txt=[' '.join(str(pf(r).get(k,'')) for k in ('observations','plan','insight')).lower() for x in R for r in x['raw']]
        out.append(sum(1 for t in txt if re.search(r'rais|increas',t))/len(txt))
    return out
fig,(a,b)=plt.subplots(1,2,figsize=(11,5.2),facecolor=SURF,gridspec_kw={'width_ratios':[1.6,1]})
for ax in (a,b):
    ax.set_facecolor(SURF)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    for s in ('left','bottom'): ax.spines[s].set_color('#c9c8c3')
    ax.tick_params(colors=MUTED,labelsize=9)
cells=[('runs/PM-HH-rep*.jsonl',OR,'arrived HIGH (2.50): kept'),('runs/PM-FLOOR-rep*.jsonl',MUTED,'no history (baseline)'),
       ('runs/HOLD-free-rep*.jsonl',BLUE,'arrived FAIR (1.475): crept up'),('runs/HOLD-hold-rep*.jsonl',AQ,'arrived fair, one seller held in round 1')]
for pat,col,lab in cells:
    P=paths(pat); m=[S.mean(p[i] for p in P) for i in range(100)]
    a.plot(range(1,101),m,color=col,lw=2.2,label=lab)
for y,l in ((1.475,'fair competition'),(1.925,'monopoly')):
    a.axhline(y,color=MUTED,lw=1,ls=(0,(4,3))); a.text(101,y,l,color=MUTED,fontsize=8,va='center')
a.set_xlim(1,100); a.set_ylim(1.3,3.0); a.set_xlabel('round',color=MUTED); a.set_ylabel('price (cost = 1)',color=MUTED)
a.grid(axis='y',color='#ebeae6',lw=0.8); a.legend(frameon=False,fontsize=8.5,loc='upper right')
a.set_title('Two Haiku sellers: they keep a high price,\nand slowly wear a fair one away',loc='left',fontsize=11,color=INK)
bf=raise_talk('runs/F16-before-rep*.jsonl'); af=raise_talk('runs/F16-after-rep*.jsonl')
for x,vals,col in ((0,bf,BLUE),(1,af,OR)):
    b.scatter([x+((i%5)-2)*0.04 for i in range(len(vals))],vals,s=42,color=col,edgecolors=SURF,linewidths=1.5,zorder=3)
    b.plot([x-0.2,x+0.2],[S.mean(vals)]*2,color=INK,lw=2)
b.set_xticks([0,1]); b.set_xticklabels(['colour asked\nBEFORE the price','colour asked\nAFTER the price'],color=INK,fontsize=9)
b.set_xlim(-0.6,1.6); b.set_ylim(0,0.6); b.set_ylabel('share of answers that talk of raising',color=MUTED)
b.grid(axis='y',color='#ebeae6',lw=0.8)
b.set_title('DeepSeek, one server, 16 markets each:\nasking first lowers the urge to raise',loc='left',fontsize=11,color=INK)
fig.suptitle('The afternoon, 13 October',x=0.02,ha='left',fontsize=13,color=INK)
fig.tight_layout(rect=(0,0,0.97,0.95)); fig.savefig('afternoon-2026-10-13.png',dpi=150,facecolor=SURF); print('ok')
