import json, glob
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
def paths(pattern):
    out=[]
    for f in sorted(glob.glob(pattern)):
        R=[json.loads(x) for x in open(f)]; R=[x for x in R if 't' in x and x['t']<=100]
        out.append([sum(x['prices'])/len(x['prices']) for x in R])
    return out
cells=[("The ceiling told is high (2.34× monopoly)", "runs/floor-n2-P1-a32-c234-rep*.jsonl","runs/DS-floor-rep*.jsonl"),
       ("The ceiling told is low (1.5× monopoly)","runs/C1-c15-rep*.jsonl","runs/DS-C1-rep*.jsonl"),
       ("No ceiling told","runs/C2-cnone-rep*.jsonl","runs/DS-C2-rep*.jsonl"),
       ("High ceiling + one sentence: \"pricing lower than\nyour competitor will typically sell more\"","runs/C3-P2-rep*.jsonl","runs/DS-C3-rep*.jsonl")]
BLUE,OR,INK,MUTED,SURF='#2a78d6','#eb6834','#0b0b0b','#52514e','#fcfcfb'
fig,axs=plt.subplots(2,2,figsize=(12,8.5),sharey=True,facecolor=SURF)
for ax,(title,h,d) in zip(axs.flat,cells):
    ax.set_facecolor(SURF)
    for pat,col,name in ((h,BLUE,'Claude Haiku 5.5'),(d,OR,'DeepSeek v4.1 flash')):
        P=paths(pat)
        for p in P: ax.plot(range(1,len(p)+1),p,color=col,alpha=0.18,lw=1)
        L=min(len(p) for p in P); m=[sum(p[i] for p in P)/len(P) for i in range(L)]
        ax.plot(range(1,L+1),m,color=col,lw=2.2,label=name+' (mean of 5)')
    for y,lab in ((1.475,'fair competition'),(1.925,'monopoly')):
        ax.axhline(y,color=MUTED,lw=1,ls=(0,(4,3)))
        ax.text(101,y,lab,color=MUTED,fontsize=9,va='center')
    ax.set_title(title,fontsize=11,color=INK,loc='left')
    ax.set_xlim(1,100); ax.set_ylim(0.9,4.6)
    for s in ('top','right'): ax.spines[s].set_visible(False)
    for s in ('left','bottom'): ax.spines[s].set_color('#c9c8c3')
    ax.tick_params(colors=MUTED,labelsize=9); ax.grid(axis='y',color='#ebeae6',lw=0.8)
axs[1,0].set_xlabel('round',color=MUTED); axs[1,1].set_xlabel('round',color=MUTED)
axs[0,0].set_ylabel('price (cost = 1)',color=MUTED); axs[1,0].set_ylabel('price (cost = 1)',color=MUTED)
axs[0,0].legend(frameon=False,fontsize=9,loc='upper right')
fig.suptitle('Two AI sellers, one product, nobody watching: where the price goes',x=0.02,ha='left',fontsize=14,color=INK)
fig.text(0.02,0.935,'Each panel is one environment, set before anyone plays. Thin lines: five separate markets. Same currency (cost = 1) everywhere.',fontsize=10,color=MUTED)
fig.tight_layout(rect=(0,0,0.96,0.93))
fig.savefig('slope-four-markets-2026-10-13.png',dpi=150,facecolor=SURF)
print('ok')
