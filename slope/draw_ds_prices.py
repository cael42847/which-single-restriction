import json,glob,statistics as S
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
BLUE,OR,AQ,YEL,VIO,INK,MUTED,SURF='#2a78d6','#eb6834','#1baf7a','#eda100','#4a3aa7','#0b0b0b','#52514e','#fcfcfb'
def runs(pat):
    out=[]
    for f in sorted(glob.glob(pat)):
        R=[x for x in map(json.loads,open(f)) if 't' in x]
        if len(R)>=100: out.append(R[:100])
    return out
fig,(a,b)=plt.subplots(1,2,figsize=(11,5.2),facecolor=SURF,gridspec_kw={'width_ratios':[1.5,1]})
for ax in (a,b):
    ax.set_facecolor(SURF)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    for s in ('left','bottom'): ax.spines[s].set_color('#c9c8c3')
    ax.tick_params(colors=MUTED,labelsize=9); ax.grid(axis='y',color='#ebeae6',lw=0.8)
# left: one market each, price paths of both sellers (same window, same server)
for R,col,lab in ((runs('runs/A5-noask-rep*.jsonl')[2],OR,'no question'),(runs('runs/A5-before-rep*.jsonl')[2],BLUE,'colour asked before the price')):
    for i in range(2):
        a.plot(range(1,101),[x['prices'][i] for x in R],color=col,lw=1.6 if i==0 else 1.0,alpha=1 if i==0 else 0.6,label=lab if i==0 else None)
for y,l in ((1.475,'fair competition'),(1.925,'monopoly'),(1.0,'cost')):
    a.axhline(y,color=MUTED,lw=1,ls=(0,(4,3))); a.text(101,y,l,color=MUTED,fontsize=8,va='center')
a.set_xlim(1,100); a.set_ylim(0.9,3.2); a.set_xlabel('round',color=MUTED); a.set_ylabel('price (cost = 1)',color=MUTED)
a.legend(frameon=False,fontsize=9,loc='upper right')
a.set_title('One market each, two DeepSeek sellers (thick and thin):\nthe war without a question, the calm with one',loc='left',fontsize=11,color=INK)
# right: where the price settles, per question (mean over rounds 51-100, one dot per market)
arms=[('no\nquestion','runs/A5-noask-rep*.jsonl',OR),('fruit','runs/A5-fruit-rep*.jsonl',YEL),('sky','runs/A5-sky-rep*.jsonl',AQ),
      ('colour\nafter','runs/A5-after-rep*.jsonl',VIO),('colour\nbefore','runs/A5-before-rep*.jsonl',BLUE)]
for k,(lab,pat,col) in enumerate(arms):
    v=[S.mean(S.mean(x['prices']) for x in R[50:]) for R in runs(pat)]
    b.scatter([k+((i%4)-1.5)*0.07 for i in range(len(v))],v,s=40,color=col,edgecolors=SURF,linewidths=1.5,zorder=3)
    b.plot([k-0.25,k+0.25],[S.mean(v)]*2,color=INK,lw=2)
for y,l in ((1.475,'fair'),(1.925,'monopoly')):
    b.axhline(y,color=MUTED,lw=1,ls=(0,(4,3))); b.text(4.45,y,l,color=MUTED,fontsize=8,va='center')
b.set_xticks(range(5)); b.set_xticklabels([x[0] for x in arms],fontsize=9,color=INK); b.set_xlim(-0.5,4.9); b.set_ylim(1.2,2.0)
b.set_ylabel('average price, rounds 51–100',color=MUTED)
b.set_title('Where the price settles\n(8 markets per question, same server, same hour)',loc='left',fontsize=11,color=INK)
fig.suptitle('DeepSeek: asking a question calms the price war, and the price goes up',x=0.02,ha='left',fontsize=13,color=INK)
fig.tight_layout(rect=(0,0,0.97,0.94)); fig.savefig('deepseek-prices-2026-10-13.png',dpi=150,facecolor=SURF); print('ok')
