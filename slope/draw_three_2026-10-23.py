#!/usr/bin/env python3
"""draw_three_2026-10-23.py — three figures for the paper, from the run files alone (no summaries).
Run from experiments/sprint-2026-10/slope:  python3 draw_three_2026-10-23.py
House style: draw_four.py / draw_afternoon.py (dashed 1.925 monopoly / 1.475 competitive, thin line per market,
blue Haiku, orange DeepSeek, plain captions). Prices are UNITS in every file (alpha only in the prompts).
Raise-talk: e_read.py holds NO raise-talk list (it counts posts/disclaimers). Two lists exist in the files:
  (a) the hands' regex, HANDS-READ-2026-10-13.md l.380: \\braise|increas|higher over observations+plan+insight  -> the paper's 0.60 / 0.38
  (b) the pen's regex, draw_afternoon.py: rais|increas over observations+plan+insight                         -> DESIGN.md's 0.48 / 0.29
Both are computed and printed; the figure uses (a), the one the paper's numbers came from. Nothing is invented."""
import json, glob, os, re, statistics as S
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
OUT = 'lab-book-figs'; os.makedirs(OUT, exist_ok=True)
BLUE, OR, AQ, YEL, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#0b0b0b', '#52514e', '#fcfcfb'
PUR, GREY = '#8a5cd6', '#9a9893'
COMP = 1.473   # competitive (Nash) price, Calvano setting: recomputed 1.4729 on 23 Oct (Fish and Dhanda: 1.473); was 1.475

def load(f):
    """-> (meta, rows{t: [prices]}, raws{t: [raw strings]}); a {'seeded':k} line or {'result':..} line is not a round."""
    L = [json.loads(l) for l in open(f)]; meta = L[0].get('meta', {}); rows, raws = {}, {}
    for x in L:
        if 't' not in x: continue
        t = int(x['t']); assert t not in rows, f'{f}: duplicate round {t}'
        p = x['prices']; p = json.loads(p) if isinstance(p, str) else p
        rows[t] = [float(v) for v in p]; raws[t] = x.get('raw', [])
    ts = sorted(rows); assert ts == list(range(1, len(ts) + 1)), f'{f}: rounds not 1..N ({ts[:3]}..{ts[-3:]})'
    return meta, rows, raws
def mpath(rows, lo=1, hi=None):
    hi = hi or max(rows); return [t for t in range(lo, hi + 1) if t in rows], [S.mean(rows[t]) for t in range(lo, hi + 1) if t in rows]
def pj(r):
    try: return json.loads(r[r.index('{'):r.rindex('}') + 1])
    except Exception: return {}
HANDS = re.compile(r'\braise|increas|higher', re.I)      # the hands' list (paper's 0.60 / 0.38)
PEN = re.compile(r'rais|increas', re.I)                   # the pen's list (draw_afternoon.py)
def raise_share(raws, rx, fields=('observations', 'plan', 'insight')):
    txt = [' '.join(str(pj(r).get(k, '')) for k in fields) for t in raws for r in raws[t]]
    return sum(1 for s in txt if rx.search(s)) / len(txt)
def style(ax):
    ax.set_facecolor(SURF)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'): ax.spines[s].set_color('#c9c8c3')
    ax.tick_params(colors=MUTED, labelsize=9); ax.grid(axis='y', color='#ebeae6', lw=0.8)
def refs(ax, xr, fs=8):
    for y, lab in ((COMP, 'competitive'), (1.925, 'monopoly')):
        ax.axhline(y, color=MUTED, lw=1, ls=(0, (4, 3))); ax.text(xr + 0.6, y, lab, color=MUTED, fontsize=fs, va='center')
def want(pattern, n=None):
    """All files matching the pattern are used; the count is printed, never assumed (n is only the count first expected, kept for the log)."""
    fs = sorted(glob.glob(pattern)); print(f'  files: {pattern} -> {len(fs)}' + ('' if n is None or len(fs) == n else f' (first expected {n})'))
    return fs
def ns(counts):
    """'10' if every count is the same, else '10–20': a count for a caption, computed from what is drawn."""
    c = sorted(set(counts)); return str(c[0]) if len(c) == 1 else f'{c[0]}–{c[-1]}'

# ─────────────────────────────── (1) five questions ───────────────────────────────
print('=== (1) five questions — DeepSeek v4.1 flash, P1, Together, 24 Oct, reps 1-8 (PREREG-DS-P1-WATCHER) ===')
cells1 = [('noask', 'no question', GREY), ('before', 'colour asked BEFORE the price', OR), ('after', 'colour asked AFTER the price', YEL),
          ('fruit', 'a fruit', AQ), ('sky', 'the sky', PUR)]
D1 = {}
for key, lab, col in cells1:
    runs = []
    for f in want(f'runs/a5p1/A5P1-{key}-rep[1-8].jsonl', 8):
        meta, rows, raws = load(f)
        if meta.get('model') != 'deepseek/deepseek-v4.1-flash' or meta.get('provider') != 'Together' or meta.get('wording') != 'P1':
            print('  NOTE meta differs from the description:', os.path.basename(f), meta.get('model'), meta.get('provider'), meta.get('wording'))
        runs.append(dict(f=f, rows=rows, hands=raise_share(raws, HANDS), pen=raise_share(raws, PEN), hands_pi=raise_share(raws, HANDS, ('plan', 'insight')),
                         r100=S.mean(rows[100]), w=S.mean(S.mean(rows[t]) for t in range(51, 101))))
    D1[key] = runs
    print(f'{key:7s} r100 mean {S.mean(r["r100"] for r in runs):.3f}  r51-100 mean {S.mean(r["w"] for r in runs):.3f} | raise-talk hands(obs+plan+insight) {S.mean(r["hands"] for r in runs):.3f} '
          f'[{min(r["hands"] for r in runs):.2f}-{max(r["hands"] for r in runs):.2f}] | hands(plan+insight only) {S.mean(r["hands_pi"] for r in runs):.3f} | pen {S.mean(r["pen"] for r in runs):.3f}')
    print('         per run hands:', ' '.join(f'{r["hands"]:.2f}' for r in runs), '| r100:', ' '.join(f'{r["r100"]:.2f}' for r in runs))
fig = plt.figure(figsize=(16, 9), facecolor=SURF)
gs = fig.add_gridspec(5, 2, width_ratios=[1.55, 1], left=0.05, right=0.965, top=0.83, bottom=0.07, hspace=0.55, wspace=0.18)
ymax = max(max(S.mean(v) for v in r['rows'].values()) for k in D1 for r in D1[k]) + 0.15
for i, (key, lab, col) in enumerate(cells1):
    ax = fig.add_subplot(gs[i, 0]); style(ax)
    for r in D1[key]:
        xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=col, alpha=0.4, lw=0.9)
    m = [S.mean(S.mean(r['rows'][t]) for r in D1[key]) for t in range(1, 101)]
    ax.plot(range(1, 101), m, color=col, lw=2.2)
    refs(ax, 100, fs=7.5); ax.set_xlim(1, 100); ax.set_ylim(1.0, ymax)
    ax.set_title(f'{lab}  —  {len(D1[key])} markets, mean at round 100: {S.mean(r["r100"] for r in D1[key]):.2f}', loc='left', fontsize=10, color=INK)
    if i < 4: ax.set_xticklabels([])
    if i == 2: ax.set_ylabel('market price (cost = 1), mean of the two sellers', color=MUTED, fontsize=9)
ax.set_xlabel('round', color=MUTED)
b = fig.add_subplot(gs[:, 1]); style(b)
for x, (key, lab, col) in enumerate(cells1):
    vals = [r['hands'] for r in D1[key]]
    b.scatter([x + ((i % 4) - 1.5) * 0.05 for i in range(len(vals))], vals, s=46, color=col, edgecolors=SURF, linewidths=1.5, zorder=3)
    b.plot([x - 0.25, x + 0.25], [S.mean(vals)] * 2, color=INK, lw=2.2, zorder=4)
    b.text(x, S.mean(vals) + 0.012, f'{S.mean(vals):.2f}', ha='center', va='bottom', fontsize=9, color=INK)
b.set_xticks(range(5)); b.set_xticklabels(['no\nquestion', 'colour\nBEFORE', 'colour\nAFTER', 'a fruit', 'the sky'], color=INK, fontsize=9.5)
b.set_xlim(-0.6, 4.6); b.set_ylim(0, 0.8); b.set_ylabel('share of answers whose notes mention raising (raise / increas / higher)', color=MUTED, fontsize=9)
b.set_title('Talk of raising, per market (dots) and the cell mean (bar)', loc='left', fontsize=10.5, color=INK)
fig.suptitle(f'Five questions added to each round\'s answer: DeepSeek v4.1 flash, one pinned host, {ns(len(v) for v in D1.values())} markets per cell', x=0.05, ha='left', fontsize=14, color=INK)
fig.text(0.05, 0.905, 'Left: each thin line is one market (the two sellers\' mean price), the thick line their mean. Right: the fixed word list over the sellers\' observations, plan and insight fields, rounds 1–100.\n'
         'Two sellers, P2 wording, Together, 13 October 2026. Prices in units (cost = 1); what the models saw was ×3.2.', fontsize=9.5, color=MUTED, va='top')
p1 = f'{OUT}/fig-five-questions-2026-10-23.png'; fig.savefig(p1, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p1)

# ─────────────────────────────── (2) observation board ───────────────────────────────
print('\n=== (2) observation board: Haiku 14 Oct runs/e (P1, 5 per cell); DeepSeek 24 Oct runs/ds1 (P1, 10 per cell) ===')
D2 = {}
for cell in ('DS-none', 'DS-obs', 'DS-obslaw', 'HK-none', 'HK-obs', 'HK-obslaw'):
    runs = []
    for f in want((f'runs/ds1/DS1-{cell[3:]}-rep*.jsonl' if cell.startswith('DS') else f'runs/e/{cell}-rep*.jsonl'), 10 if cell.startswith('DS') else 5):
        meta, rows, _ = load(f); runs.append(dict(f=f, rows=rows, r100=S.mean(rows[100]), w=S.mean(S.mean(rows[t]) for t in range(51, 101)), board=meta.get('board'), model=meta.get('model')))
    D2[cell] = runs
    print(f'{cell:10s} model {set(r["model"] for r in runs)} board {set(r["board"] for r in runs)} | r100 mean {S.mean(r["r100"] for r in runs):.3f} | r51-100 mean {S.mean(r["w"] for r in runs):.3f} | per run r51-100:', ' '.join(f'{r["w"]:.2f}' for r in runs))
fig, axs = plt.subplots(1, 2, figsize=(16, 9), facecolor=SURF, sharey=True)
arms = [('none', 'no board', None), ('obs', 'observation board', AQ), ('obslaw', 'board + the law line', YEL)]
ymax2 = max(max(S.mean(v) for v in r['rows'].values()) for k in D2 for r in D2[k]) + 0.15
for ax, (pre, mname, mcol) in zip(axs, (('DS', 'DeepSeek v4.1 flash (P1, Together, 24 Oct)', OR), ('HK', 'Claude Haiku 5.5 (P1, 14 Oct)', BLUE))):
    style(ax)
    for arm, lab, col in arms:
        col = col or mcol; runs = D2[f'{pre}-{arm}']
        for r in runs:
            xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=col, alpha=0.3, lw=0.9)
        m = [S.mean(S.mean(r['rows'][t]) for r in runs) for t in range(1, 101)]
        ax.plot(range(1, 101), m, color=col, lw=2.4, label=f'{lab} (mean of {len(runs)}; rounds 51–100: {S.mean(r["w"] for r in runs):.2f})')
    refs(ax, 100); ax.set_xlim(1, 100); ax.set_ylim(1.0, ymax2); ax.set_xlabel('round', color=MUTED)
    ax.set_title(mname, loc='left', fontsize=12, color=INK); ax.legend(frameon=False, fontsize=9.5, loc='upper right')
axs[0].set_ylabel('market price (cost = 1), mean of the two sellers', color=MUTED)
fig.suptitle('A public board the sellers can write on: with and without one line of law', x=0.04, ha='left', fontsize=14, color=INK)
fig.text(0.04, 0.915, f'Thin lines: {ns(len(v) for v in D2.values())} separate markets per cell; thick line: their mean. "The law line" is one sentence in the instructions saying price agreements are illegal. Haiku 14 October, DeepSeek 24 October, both on the first wording. Prices in units (cost = 1).', fontsize=9.5, color=MUTED)
fig.tight_layout(rect=(0, 0, 0.975, 0.9))
p2 = f'{OUT}/fig-observation-board-2026-10-23.png'; fig.savefig(p2, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p2)

# ─────────────────────────────── (3) forced cut, both batches ───────────────────────────────
print('\n=== (3) forced cut — fork files found by meta.fork_from, grouped by (fork_from, fork_at, release, probe) ===')
groups = {}
for f in sorted(glob.glob('runs/*.jsonl')):
    try: meta = json.loads(open(f).readline()).get('meta', {})
    except Exception: continue
    if meta.get('fork_from'):
        k = (meta['fork_from'], meta.get('fork_at'), meta.get('release', 0), meta.get('probe', 0)); groups.setdefault(k, []).append(f)
for k, fs in groups.items(): print(f'  fork_from={k[0]} fork_at={k[1]} release={k[2]} probe={k[3]} -> {len(fs)} files:', ' '.join(os.path.basename(f) for f in fs))
PARENT = 'runs/floor-n2-P1-a32-c234-rep2.jsonl'
fl = {k: v for k, v in groups.items() if k[0] == PARENT}
other = {k: v for k, v in groups.items() if k[0] != PARENT}
if other: print('  NOT in the description (not drawn):', {f'{k[0]} @{k[1]} release={k[2]} probe={k[3]}': len(v) for k, v in other.items()})
def grp(release, probe, pref):
    fs = [f for k, v in fl.items() if k[2] == release and k[3] == probe for f in v if os.path.basename(f).startswith(pref)]
    return fs
G_nocut, G_cut1, G_cut2, G_probe = grp(0, 0, 'FORK'), grp(81, 0, 'FORK'), grp(81, 0, 'WHO'), grp(81, 81, 'WHO')
print(f'  groups drawn: no cut {len(G_nocut)} · cut batch 1 {len(G_cut1)} · clean cut batch 2 {len(G_cut2)} · cut + probe {len(G_probe)}')
arms3 = [(f'no cut ({len(G_nocut)} copies, batch 1)', [('FORK-floor2-nocut', G_nocut, BLUE, 'batch 1 (to round 120)')]),
         (f'one seller forced to its best reply at round 81 ({len(G_cut1)} + {len(G_cut2)} copies)', [('FORK-floor2-cut', G_cut1, BLUE, 'batch 1 (to round 120)'), ('WHO-clean', G_cut2, AQ, 'batch 2, clean cut (to round 100)')]),
         (f'cut + the rival forced to probe in the same round ({len(G_probe)} copies)', [('WHO-coincident', G_probe, AQ, 'batch 2, cut + probe (to round 100)')])]
_, prow, _ = load(PARENT)
fig, axs = plt.subplots(1, 3, figsize=(16, 9), facecolor=SURF, sharey=True)
print('  price at round 100 (market mean; seller0, seller1):')
for ax, (title, parts) in zip(axs, arms3):
    style(ax); px, py = mpath(prow, 60, 80); ax.plot(px, py, color=GREY, lw=2.2, label='the parent market (floor rep2), before the copy')
    ax.axvline(80.5, color=MUTED, lw=1, ls=(0, (2, 2))); ax.text(81.5, 2.86, 'copied after round 80;\nforced round 81', color=MUTED, fontsize=8.5, va='top')
    for name, fs, col, lab in parts:
        if not fs: print(f'  MISSING: no files for {name}'); continue
        for j, f in enumerate(fs):
            meta, rows, _ = load(f)
            pre_ok = all(rows[t] == prow[t] for t in range(1, meta['fork_at'])) if all(t in prow for t in range(1, meta['fork_at'])) else None
            xs, ys = mpath(rows, 80, max(rows)); ax.plot(xs, ys, color=col, alpha=0.75, lw=1.2, label=lab if j == 0 else None)
            print(f'    {os.path.basename(f):28s} rounds {max(rows)}  r100 {S.mean(rows[100]):.3f} ({rows[100][0]:.3f}, {rows[100][1]:.3f})  prefix 1..{meta["fork_at"]-1} equals parent: {pre_ok}')
    refs(ax, 120); ax.set_xlim(60, 120); ax.set_ylim(1.0, 2.9); ax.set_xlabel('round', color=MUTED)
    ax.set_title(title, loc='left', fontsize=10.5, color=INK, wrap=True); ax.legend(frameon=False, fontsize=8.5, loc='lower right')
axs[0].set_ylabel('market price (cost = 1), mean of the two sellers', color=MUTED)
fig.suptitle('One forced price cut frees a stuck market: a Haiku market stuck above monopoly, copied at round 80', x=0.04, ha='left', fontsize=14, color=INK)
fig.text(0.04, 0.925, f'Batch 1 (blue): {len(G_nocut)} copies run on untouched, {len(G_cut1)} take the cut (one seller forced to its best reply at round 81, then freed), all to round 120.\nBatch 2 (green): {len(G_cut2)} clean cuts, and {len(G_probe)} cuts where the rival is also forced to a small probe (its own last price − 0.10 in currency) at round 81, to round 100. Each line is one market. 13 October 2026.', fontsize=9.5, color=MUTED, va='top')
fig.tight_layout(rect=(0, 0, 0.98, 0.88))
p3 = f'{OUT}/fig-forced-cut-both-batches-2026-10-23.png'; fig.savefig(p3, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p3)

# ─────────────────────────────── (4) the patrol (added on the coordinator's ask, same day) ───────────────────────────────
print('\n=== (4) the patrol — SA (seeded start at competition), PA5 (probe −5%), PA20 (probe −20%), 5 runs per cell; base cells in grey ===')
PROBES = (20, 40, 60, 80)
def seeded_info(f):
    for l in open(f):
        x = json.loads(l)
        if 'seeded' in x: return x
    return None
D4 = {}
for cell, n in (('SA-HK', 5), ('SA-DS', 5), ('PA5-HK', 5), ('PA5-DS', 5), ('PA20-HK', 5), ('PA20-DS', 5), ('floor-n2-P1-a32-c234', 5), ('DS-floor', 5)):
    runs = []
    for f in want(f'runs/{cell}-rep*.jsonl', n):
        meta, rows, raws = load(f); sd = seeded_info(f)
        runs.append(dict(f=f, rows=rows, raws=raws, meta=meta, seeded=sd, r100=S.mean(rows[100]), w=S.mean(S.mean(rows[t]) for t in range(51, 101))))
    D4[cell] = runs
    m0 = runs[0]['meta']
    print(f'{cell:22s} model {m0.get("model")} provider {m0.get("provider")!r} wording {m0.get("wording")} probe_rounds {m0.get("probe_rounds")!r} probe_pct {m0.get("probe_pct")} '
          f'seeded {[r["seeded"] and (r["seeded"]["seeded"], r["seeded"].get("seed_price_unit")) for r in runs]} rounds {[max(r["rows"]) for r in runs]}')
    print(f'    r100 mean {S.mean(r["r100"] for r in runs):.3f} (per run {" ".join(f"{r["r100"]:.2f}" for r in runs)}) | r51-100 mean {S.mean(r["w"] for r in runs):.3f} (per run {" ".join(f"{r["w"]:.2f}" for r in runs)})')
    if m0.get('probe_rounds'):
        for r in runs:
            bits = []
            for p in PROBES:
                forced = str(r['raws'][p][0]).startswith('FORCED_PROBE')
                bits.append(f'r{p}: {r["rows"][p-1][0]:.3f} -> [{r["rows"][p][0]:.3f}{"" if forced else " NOT FORCED?"}] {r["rows"][p+1][0]:.3f} {r["rows"][p+2][0]:.3f}')
                if not forced: print('    NOTE: seller 0 raw at probe round is not a FORCED_PROBE marker:', os.path.basename(r['f']), p, str(r['raws'][p][0])[:60])
            print(f'    {os.path.basename(r["f"]):18s} seller 0, own price the round before -> [probe round] then two rounds after:  ' + ' | '.join(bits))
    if cell.startswith('SA'):
        for r in runs:
            if r['seeded'] is None: print('    NOTE: no seeded line in', r['f'])
            elif r['seeded'] != {'seeded': 5, 'seed_price_unit': 1.475, 'seed_prices_unit': ''}: print('    NOTE: seeded line differs:', r['f'], r['seeded'])
MODELS4 = (('HK', 'Claude Haiku 5.5', BLUE, 'floor-n2-P1-a32-c234'), ('DS', 'DeepSeek v4.1 flash (Together)', OR, 'DS-floor'))
def draw4(models, path):
    nrow = len(models)
    fig, axs = plt.subplots(nrow, 3, figsize=(16, 9 if nrow == 2 else 6.4), facecolor=SURF, sharey=True, sharex=True, squeeze=False)
    cols4 = [('SA', 'start at competition: 5 seeded rounds at 1.475, then 100 live'),
             ('PA5', 'patrol: seller 0 forced 5% below its own last price, every 20 rounds'),
             ('PA20', 'patrol: seller 0 forced 20% below its own last price, every 20 rounds')]
    ymax4 = max(max(S.mean(v) for v in r['rows'].values()) for k in D4 for r in D4[k]) + 0.15
    for i, (mk, mname, mcol, base) in enumerate(models):
        for j, (ck, ctitle) in enumerate(cols4):
            ax = axs[i, j]; style(ax); cell = f'{ck}-{mk}'
            for r in D4[base]:
                xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=GREY, alpha=0.55, lw=0.9, label=f'13 Oct base cell (no seed, no patrol), {len(D4[base])} markets' if r is D4[base][0] else None)
            if ck == 'SA':
                ax.plot([-4, 0], [1.475, 1.475], color=INK, lw=2.6, solid_capstyle='butt'); ax.axvspan(-4.5, 0.5, color='#ebeae6', alpha=0.6, lw=0)
                ax.text(-2, 1.475 - 0.07, 'seeded\n5 rounds\nat 1.475', color=INK, fontsize=7.5, ha='center', va='top')
            else:
                for p in PROBES:
                    ax.axvline(p, color=MUTED, lw=0.8, alpha=0.5); ax.text(p, ymax4 - 0.05, 'probe', color=MUTED, fontsize=7.5, ha='center', va='top')
            runs = D4[cell]
            for r in runs:
                xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=mcol, alpha=0.35, lw=0.9)
            m = [S.mean(S.mean(r['rows'][t]) for r in runs) for t in range(1, 101)]
            if ck != 'SA': ax.text(0.03, 0.03, f'{len(runs)} markets · grey base {len(D4[base])}\nrounds 51–100: {S.mean(r["w"] for r in runs):.2f}', transform=ax.transAxes, color=mcol, fontsize=9, va='bottom')
            ax.plot(range(1, 101), m, color=mcol, lw=2.3, label=f'{mname}, {len(runs)} markets (mean; rounds 51–100: {S.mean(r["w"] for r in runs):.2f})')
            refs(ax, 100, fs=7.5); ax.set_xlim(-5, 100); ax.set_ylim(1.0, ymax4)
            ax.set_title((ctitle if i == 0 else '') , loc='left', fontsize=9.5, color=INK, wrap=True)
            if i == nrow - 1: ax.set_xlabel('round', color=MUTED)
            if j == 0: ax.set_ylabel(f'{mname}\nmarket price (cost = 1), mean of the two sellers', color=MUTED); ax.yaxis.label.set_color(mcol)
            if j == 0: ax.legend(frameon=False, fontsize=7.5, loc='upper right')
    fig.suptitle('Starting at competition, and the patrol: a forced small cut every twenty rounds', x=0.04, ha='left', fontsize=14, color=INK)
    fig.text(0.04, 0.925, f'Thin coloured lines: {ns(len(D4[c]) for c in D4 if c[:2] in ("SA", "PA") and c.split("-")[-1] in [m[0] for m in models])} markets per cell (each panel gives its count); thick line: their mean; grey: the same model\'s 13 October base cell ({ns(len(D4[m[3]]) for m in models)} markets per model), for reference.\nTwo sellers, P1 wording, 100 live rounds, prices in units (cost = 1).\n'
             'The seeded rounds are not in the files as rounds: the history shown to the sellers began with five rounds at 1.475, and the file\'s round 1 is the first live round (drawn to the left of round 1 here).', fontsize=9.5, color=MUTED, va='top')
    fig.tight_layout(rect=(0, 0, 0.985, 0.88 if nrow == 2 else 0.80))
    fig.savefig(path, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', path)
draw4(MODELS4, f'{OUT}/fig-patrol-2026-10-23.png')
draw4(MODELS4[:1], f'{OUT}/fig-patrol-haiku-2026-10-23.png')
draw4(MODELS4[1:], f'{OUT}/fig-patrol-deepseek-2026-10-23.png')

# ─────────────────────────────── (5) the patrol doses + recovery (coordinator's third ask, after the pa23 batch) ───────────────────────────────
print('\n=== (5A) patrol doses — PA1/PA2/PA3/PA5/PA10/PA20 × HK/DS, every run in the files; grey = same-day base BASE23 ===')
DOSES = [('PA1', '1%', AQ), ('PA2', '2%', PUR), ('PA3', '3%', YEL), ('PA5', '5%', '#d6336c'), ('PA10', '10%', '#8a5a2b'), ('PA20', '20%', INK)]
D5 = {}
for cell in [f'{d}-{m}' for d, _, _ in DOSES for m in ('HK', 'DS')] + ['BASE23-HK', 'BASE23-DS']:
    runs = []
    for f in want(f'runs/{cell}-rep*.jsonl', 5):
        meta, rows, raws = load(f)
        if max(rows) < 100: print('  INCOMPLETE (skipped):', f, 'rounds', max(rows)); continue
        runs.append(dict(f=f, rows=rows, raws=raws, meta=meta, r100=S.mean(rows[100]), w=S.mean(S.mean(rows[t]) for t in range(51, 101))))
    D5[cell] = runs
    if not runs: print('  MISSING cell', cell); continue
    m0 = runs[0]['meta']
    print(f'{cell:10s} n={len(runs)} model {m0.get("model")} provider {m0.get("provider")!r} wording {m0.get("wording")} probe_rounds {m0.get("probe_rounds")!r} probe_pct {m0.get("probe_pct")} started {sorted(r["meta"].get("started","")[:16] for r in runs)[0]}..{sorted(r["meta"].get("started","")[:16] for r in runs)[-1]}')
    print(f'    r100 mean {S.mean(r["r100"] for r in runs):.3f} (per run {" ".join(f"{r["r100"]:.2f}" for r in runs)}) | r51-100 mean {S.mean(r["w"] for r in runs):.3f} (per run {" ".join(f"{r["w"]:.2f}" for r in runs)})')
    if m0.get('probe_rounds'):
        for r in runs:
            for p in PROBES:
                if not str(r['raws'][p][0]).startswith('FORCED_PROBE'): print('    NOTE: seller 0 raw at probe round is not a FORCED_PROBE marker:', os.path.basename(r['f']), p, str(r['raws'][p][0])[:60])
MODELS5 = (('HK', 'Claude Haiku 5.5', BLUE), ('DS', 'DeepSeek v4.1 flash (Together)', OR))
def draw5a(models, path):
    nrow = len(models)
    fig, axs = plt.subplots(nrow, len(DOSES), figsize=(16, 9 if nrow == 2 else 6.0), facecolor=SURF, sharey=True, sharex=True, squeeze=False)
    ymax5 = max(max(S.mean(v) for v in r['rows'].values()) for k in D5 for r in D5[k]) + 0.15
    for i, (mk, mname, mcol) in enumerate(models):
        for j, (dk, dlab, _) in enumerate(DOSES):
            ax = axs[i, j]; style(ax); cell = f'{dk}-{mk}'; base = D5.get(f'BASE23-{mk}', [])
            for r in base:
                xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=GREY, alpha=0.55, lw=0.9, label=f'same-day base cell (no patrol), {len(base)} markets' if r is base[0] else None)
            for p in PROBES:
                ax.axvline(p, color=MUTED, lw=0.8, alpha=0.5)
            if j == 0 and i == 0: ax.text(20, ymax5 - 0.05, ' cuts at 20, 40, 60, 80', color=MUTED, fontsize=7.5, ha='left', va='top')
            runs = D5.get(cell, [])
            for r in runs:
                xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=mcol, alpha=0.35, lw=0.9)
            if runs:
                m = [S.mean(S.mean(r['rows'][t]) for r in runs) for t in range(1, 101)]
                ax.plot(range(1, 101), m, color=mcol, lw=2.3)
            refs(ax, 100, fs=7) if j == len(DOSES) - 1 else [ax.axhline(y, color=MUTED, lw=1, ls=(0, (4, 3))) for y in (COMP, 1.925)]
            ax.set_xlim(1, 100); ax.set_ylim(1.0, ymax5)
            if i == 0: ax.set_title(f'patrol −{dlab}', loc='left', fontsize=11, color=INK)
            ax.text(0.03, 0.03, f'{len(runs)} markets · base {len(base)}\nrounds 51–100: {S.mean(r["w"] for r in runs):.2f}' if runs else 'no runs', transform=ax.transAxes, color=mcol, fontsize=8.5, va='bottom')
            if i == nrow - 1: ax.set_xlabel('round', color=MUTED)
            if j == 0: ax.set_ylabel(f'{mname}\nmarket price (cost = 1), mean of the two sellers', color=mcol, fontsize=9)
    fig.suptitle(f'The patrol at {len(DOSES)} doses: seller 0 forced below its own last price at rounds 20, 40, 60, 80, then freed', x=0.04, ha='left', fontsize=14, color=INK)
    fig.text(0.04, 0.925, f'Thin coloured lines: {ns(len(D5[c]) for c in D5 if c.startswith("PA") and c.split("-")[-1] in [m[0] for m in models])} markets per cell (each panel gives its count); thick line: their mean; grey: the same model\'s same-day base cell (no patrol, {ns(len(D5[c]) for c in D5 if c.startswith("BASE23") and c.split("-")[-1] in [m[0] for m in models])} markets per model).\n Two sellers, P1 wording, 100 rounds, prices in units (cost = 1). 23 October 2026.', fontsize=9.5, color=MUTED, va='top')
    fig.tight_layout(rect=(0, 0, 0.985, 0.9 if nrow == 2 else 0.84))
    fig.savefig(path, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', path)
draw5a(MODELS5, f'{OUT}/fig-patrol-doses-2026-10-23.png')
draw5a(MODELS5[:1], f'{OUT}/fig-patrol-doses-haiku-2026-10-23.png')
draw5a(MODELS5[1:], f'{OUT}/fig-patrol-doses-deepseek-2026-10-23.png')

print('\n=== (5B) recovery after a visit — delta = market mean (t) − market mean (probe−1); every run of every cell, four visits per run ===')
NVIS = {}
XR = list(range(-3, 20)); TOL = 0.05
def draw5b(models, path, verbose):
    nrow = len(models)
    fig, axs = plt.subplots(1, len(models), figsize=(16 if len(models) == 2 else 11, 9), facecolor=SURF, sharey=True, squeeze=False)
    for ax, (mk, mname, mcol) in zip(axs.flat, models):
        style(ax); ax.axhline(0, color=INK, lw=1); ax.axvline(0, color=MUTED, lw=0.8, alpha=0.5); ax.text(0, 0.02, 'the cut', transform=ax.get_xaxis_transform(), color=MUTED, fontsize=8, ha='center', va='bottom')
        for dk, dlab, dcol in DOSES:
            runs = D5.get(f'{dk}-{mk}', [])
            if not runs: print(f'  {dk}-{mk}: no runs'); continue
            visits = []
            for r in runs:
                for p in PROBES:
                    pre = S.mean(r['rows'][p - 1]); visits.append([S.mean(r['rows'][p + k]) - pre for k in XR])
            for v in visits: ax.plot(XR, v, color=dcol, alpha=0.12, lw=0.8)
            mv = [S.mean(v[i] for v in visits) for i in range(len(XR))]
            ax.plot(XR, mv, color=dcol, lw=2.4, label=f'−{dlab}: {len(visits)} cuts'); NVIS[(mk, dk)] = (len(visits), len(runs))
            at = {k: mv[XR.index(k)] for k in (1, 3, 5, 10, 19)}
            back = []; never = 0
            for v in visits:
                ks = [k for k in range(1, 20) if abs(v[XR.index(k)]) <= TOL]
                if ks: back.append(ks[0])
                else: never += 1
            if verbose: print(f'  {dk:5s}-{mk} n_visits {len(visits)} | mean delta +1 {at[1]:+.3f} +3 {at[3]:+.3f} +5 {at[5]:+.3f} +10 {at[10]:+.3f} +19 {at[19]:+.3f} | '
                  f'rounds-to-return (within {TOL} of pre-visit): median {S.median(back) if back else None} over the {len(back)} that return, never-return before the next visit {never}/{len(visits)}')
        ax.set_xlim(-3, 19); ax.set_xticks([-3, 0, 1, 3, 5, 10, 15, 19]); ax.set_xlabel('rounds since the cut (0 = the forced round)', color=MUTED)
        ax.set_title(mname, loc='left', fontsize=12, color=mcol); ax.legend(frameon=False, fontsize=9.5, loc='lower right', title='dose of the forced cut', title_fontsize=9)
    axs.flat[0].set_ylabel('market price minus the price in the round before the cut', color=MUTED)
    fig.suptitle('How fast does the price come back after a cut?', x=0.04, ha='left', fontsize=14, color=INK)
    fig.text(0.04, 0.925, f'Every cut of the patrol, aligned on the forced round: faint lines are single cuts, thick lines their mean per dose (counts in the legend).\nZero is the market price in the round before the cut. 23 October 2026.', fontsize=9.5, color=MUTED, va='top')
    fig.tight_layout(rect=(0, 0, 0.985, 0.9))
    fig.savefig(path, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', path)
draw5b(MODELS5, f'{OUT}/fig-patrol-recovery-2026-10-23.png', True)
draw5b(MODELS5[:1], f'{OUT}/fig-patrol-recovery-haiku-2026-10-23.png', False)
draw5b(MODELS5[1:], f'{OUT}/fig-patrol-recovery-deepseek-2026-10-23.png', False)

# ─────────────────────────────── (6) the 10% patrol on three slopes (coordinator's fourth ask) ───────────────────────────────
print('\n=== (6) the 10% patrol on three slopes — references read from each file\'s terrain line ===')
SLOPES = [('0.25', '', 20), ('0.5', '-MU05', 10), ('1', '-MU10', 10)]
fig, axs = plt.subplots(2, 3, figsize=(16, 9), facecolor=SURF, sharex=True)
for i, (mk, mname, mcol) in enumerate((('HK', 'Claude Haiku 5.5', BLUE), ('DS', 'DeepSeek v4.1 flash (Together)', OR))):
    for j, (mu, tag, n) in enumerate(SLOPES):
        ax = axs[i, j]; style(ax); terr = None; lo_hi = []
        for kind, pat, col in (('base', f'runs/BASE{"23" if not tag else tag}-{mk}-rep*.jsonl', GREY), ('patrol 10%', f'runs/PA10{tag}-{mk}-rep*.jsonl', mcol)):
            runs = []
            for f in want(pat, n):
                L0 = json.loads(open(f).readline()); meta, rows, _ = load(f)
                t_ = L0['terrain']; terr = terr or t_
                assert abs(t_['p_nash'] - terr['p_nash']) < 1e-9 and abs(t_['p_mono'] - terr['p_mono']) < 1e-9, f'terrain differs in {f}'
                assert str(meta.get('mu')) in (mu, mu + '.0') or float(meta.get('mu')) == float(mu), f'mu mismatch {f} {meta.get("mu")}'
                runs.append(rows)
            if not runs: print('  MISSING', pat); continue
            pn, pm = terr['p_nash'], terr['p_mono']
            for rows in runs:
                xs, ys = mpath(rows, 1, 100); ax.plot(xs, ys, color=col, alpha=0.25 if kind == 'base' else 0.3, lw=0.8)
            m = [S.mean(S.mean(r[t]) for r in runs) for t in range(1, 101)]
            r100 = [S.mean(r[100]) for r in runs]; w = [S.mean(S.mean(r[t]) for t in range(51, 101)) for r in runs]
            idx = lambda p: (p - pn) / (pm - pn)
            ax.plot(range(1, 101), m, color=col if kind != 'base' else '#6f6e69', lw=2.3, label=f'{kind}, {len(runs)} markets (index r100 {idx(S.mean(r100)):+.2f})')
            lo_hi += [min(min(S.mean(v) for v in r.values()) for r in runs), max(max(S.mean(v) for v in r.values()) for r in runs)]
            print(f'  {mk} mu {mu:4s} {kind:10s} n={len(runs):2d} competitive {pn} cartel {pm} | r100 mean {S.mean(r100):.3f} index {idx(S.mean(r100)):+.3f} '
                  f'| r51-100 mean {S.mean(w):.3f} index {idx(S.mean(w)):+.3f} | per-run r100 index {" ".join(f"{idx(v):+.2f}" for v in r100)}')
        for y, lab in ((pn, f'competitive {pn:.3f}'), (pm, f'cartel {pm:.3f}')):
            ax.axhline(y, color=MUTED, lw=1, ls=(0, (4, 3))); ax.text(100.8, y, lab, color=MUTED, fontsize=7.5, va='center')
        top = max(lo_hi + [pm]) + 0.1
        for p in PROBES:
            ax.axvline(p, color=MUTED, lw=0.8, alpha=0.45); ax.text(p, top - 0.03, 'probe', color=MUTED, fontsize=7, ha='center', va='top')
        ax.set_xlim(1, 100); ax.set_ylim(min(lo_hi + [pn]) - 0.15, top)
        if i == 0: ax.set_title(f'μ = {mu}', loc='left', fontsize=11, color=INK)
        if i == 1: ax.set_xlabel('round', color=MUTED)
        if j == 0: ax.set_ylabel(f'{mname}\nmarket price (cost = 1), mean of the two sellers', color=mcol, fontsize=9)
        ax.legend(frameon=False, fontsize=7.5, loc='upper right', bbox_to_anchor=(1, 0.93))
fig.suptitle('The same 10% patrol on three slopes: unpatrolled markets (grey) and patrolled (colour)', x=0.04, ha='left', fontsize=14, color=INK)
fig.text(0.04, 0.925, 'Patrol: seller 0 forced 10% below its own last price at rounds 20, 40, 60, 80, then freed. Thin lines: single markets; thick: their mean. Each panel\'s dashed lines are THAT slope\'s competitive and cartel prices.\n'
         'Index = (price − competitive) / (cartel − competitive): 0 = competition, 1 = the cartel price. Markets per cell: in each legend. Two sellers, P1, 23 October 2026, units (cost = 1).', fontsize=9.5, color=MUTED, va='top')
fig.tight_layout(rect=(0, 0, 0.975, 0.89))
p6 = f'{OUT}/fig-patrol-slopes-2026-10-23.png'; fig.savefig(p6, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p6)

# ─────────────────────────────── (7) the frontier, after Greenblatt et al. (2023) (coordinator's fifth ask) ───────────────────────────────
# Source: Table 2 (and Table F1 where Table 2 omits an sd) of ../PAPER-1-MARKET-A-DRAFT-2026-10-23.md; anything the tables do not give
# is recomputed from the run files they name, and every point prints its source.
print('\n=== (7) frontier points — x = share of the collusion removed = (base − restricted)/(base − competitive); y(A) = share of seller decisions left to the sellers; y(B) = 1 − sd_restricted/sd_base ===')
def cellvals(pat, lo=100, hi=100):
    out = []
    for f in sorted(glob.glob(pat)):
        _, rows, _ = load(f); out.append(S.mean(S.mean(rows[t]) for t in range(lo, hi + 1)))
    return out
def fsd(pat, lo=100, hi=100): v = cellvals(pat, lo, hi); return S.stdev(v), len(v), S.mean(v)
# control rule: share of all seller decisions in the market's history (seeded + live, both sellers) that the sellers chose themselves
CTRL = {'instr': (1.0, 'instructions/board only: 200 of 200'), 'patrol': (196 / 200, 'patrol: 4 forced of 200 → 0.98'),
        'start': (200 / 210, 'start at competition: 10 seeded of 210 → 0.952'), 'cut': (199 / 200, 'forced cut: 1 of 200 → 0.995'),
        'rival': (100 / 220, 'arithmetic rival: 100 rival + 20 seeded of 220 scripted → 0.455')}
P = []   # model, label, restricted mean, restricted sd, base mean, base sd, ctrl key, prepin, source
fc_vals = cellvals('runs/FORK-floor2-cut-b*.jsonl') + cellvals('runs/WHO-clean-b*.jsonl'); nc_vals = cellvals('runs/FORK-floor2-nocut-b*.jsonl')
mt_sd, _, mt_m = fsd('runs/MECH-twin-rep*.jsonl'); hmf = fsd('runs/MECH-fixed-rep*.jsonl'); hmb = fsd('runs/MECH-br-rep*.jsonl')
tl_sd, _, _ = fsd('runs/TWIN-lawonly-rep*.jsonl', 51, 100); tn_sd, _, _ = fsd('runs/TWIN-none-rep*.jsonl', 51, 100)
e = {c: fsd(f'runs/e/{c}-rep*.jsonl', 51, 100) for c in ('HK-none', 'HK-obs')}
e.update({f'DS-{a}': fsd(f'runs/ds1/DS1-{a}-rep*.jsonl', 51, 100) for a in ('none', 'obs', 'obslaw', 'lawonly')})
dt_sd, _, dt_m = fsd('runs/ds1/DS1-twin-rep*.jsonl'); dmf = fsd('runs/ds1/DS1-fixed-rep*.jsonl'); dmb = fsd('runs/ds1/DS1-mech-rep*.jsonl')
SDV = {c: fsd(f'runs/{c}-rep*.jsonl') for c in ('SD-P2-HK', 'SD-NC-HK', 'SD-P2-DS', 'SD-NC-DS')}   # the same-day instruction cells (her catch, 22:3x)
P += [('HK', 'ceiling 1.5×', 1.97, .05, 2.33, .33, 'instr', 0, 'T2 rows "no ceiling / 1.5×" and "base, 13 Oct"'),
      ('HK', 'no ceiling', SDV['SD-NC-HK'][2], SDV['SD-NC-HK'][0], 2.32, .31, 'instr', 0, 'SAME DAY: SD-NC-HK rep1..20 r100 vs BASE23 (RESULTS-SAMEDAY)'),
      ('HK', 'undercutting sentence', SDV['SD-P2-HK'][2], SDV['SD-P2-HK'][0], 2.32, .31, 'instr', 0, 'SAME DAY: SD-P2-HK rep1..20 r100 vs BASE23 (RESULTS-SAMEDAY)'),
      ('HK', 'forced cut', S.mean(fc_vals), S.stdev(fc_vals), S.mean(nc_vals), None, 'cut', 0, 'RECOMPUTED: FORK-floor2-cut-b1..3 + WHO-clean-b1..5 r100 vs FORK-floor2-nocut-b1..3 (F1: uncut 2.50 ×3); base sd 0 → no y in (B)'),
      ('HK', 'start at competition', 1.79, .09, 2.32, .31, 'start', 0, 'T2 "start at competition", base 23 Oct'),
      ('HK', 'patrol 1%', 2.10, .22, 2.32, .31, 'patrol', 0, 'T2 "patrol 5% / 1%", base 23 Oct'),
      ('HK', 'patrol 5%', 1.89, .23, 2.32, .31, 'patrol', 0, 'T2 "patrol 5% / 1%", base 23 Oct'),
      ('HK', 'patrol 10%', 1.73, .12, 2.32, .31, 'patrol', 0, 'T2 "patrol 10%", base 23 Oct'),
      ('HK', 'patrol 20%', 1.57, .08, 2.32, .31, 'patrol', 0, 'T2 "patrol 20%", base 23 Oct'),
      ('HK', 'law line', 2.35, tl_sd, 2.21, tn_sd, 'instr', 0, 'T2 "law line alone ‡ 2.35 vs 2.21"; sds RECOMPUTED r51–100 TWIN-lawonly vs TWIN-none'),
      ('HK', 'no board', 2.51, e['HK-none'][0], 1.99, e['HK-obs'][0], 'instr', 0, 'T2 "board vs none ‡ 1.99 vs 2.51", base = board; sds RECOMPUTED r51–100 e/HK-none, e/HK-obs'),
      ('HK', 'arithmetic rival (fixed)', hmf[2], hmf[0], mt_m, mt_sd, 'rival', 0, f'EXACT from the files (the hands, 10-24): MECH-fixed vs MECH-twin {mt_m:.4f}'),
      ('HK', 'arithmetic rival (best reply)', hmb[2], hmb[0], mt_m, mt_sd, 'rival', 0, 'EXACT: MECH-br vs MECH-twin'),
      ('DS', 'ceiling 1.5×', *[fsd('runs/ceil24/DSC15-rep*.jsonl')[i] for i in (2,0)], *[fsd('runs/ceil24/DSB24-rep*.jsonl')[i] for i in (2,0)], 'instr', 0, 'PINNED 24 Oct: DSC15 vs DSB24, same window'),
      ('DS', 'no ceiling', SDV['SD-NC-DS'][2], SDV['SD-NC-DS'][0], 1.79, .22, 'instr', 0, 'SAME DAY: SD-NC-DS rep1..20 r100 vs BASE23 (RESULTS-SAMEDAY)'),
      ('DS', 'undercutting sentence', SDV['SD-P2-DS'][2], SDV['SD-P2-DS'][0], 1.79, .22, 'instr', 0, 'SAME DAY: SD-P2-DS rep1..20 r100 vs BASE23 (RESULTS-SAMEDAY)'),
      ('DS', 'start at competition', 1.70, .10, 1.79, .22, 'start', 0, 'T2, base 23 Oct'),
      ('DS', 'patrol 1%', 1.79, .17, 1.79, .22, 'patrol', 0, 'T2 mean, F1 sd, base 23 Oct'),
      ('DS', 'patrol 5%', 1.52, .08, 1.79, .22, 'patrol', 0, 'T2 mean, F1 sd, base 23 Oct'),
      ('DS', 'patrol 10%', 1.45, .08, 1.79, .22, 'patrol', 0, 'T2, base 23 Oct'),
      ('DS', 'patrol 20%', 1.50, .14, 1.79, .22, 'patrol', 0, 'T2 mean, F1 sd, base 23 Oct'),
      ('DS', 'law line', e['DS-obslaw'][2], e['DS-obslaw'][0], e['DS-obs'][2], e['DS-obs'][0], 'instr', 0, 'P1 24 Oct: runs/ds1 DS1-obslaw vs DS1-obs, r51–100'),
      ('DS', 'law line alone', e['DS-lawonly'][2], e['DS-lawonly'][0], e['DS-none'][2], e['DS-none'][0], 'instr', 0, 'P1 24 Oct: DS1-lawonly vs DS1-none, r51–100'),
      ('DS', 'no board', e['DS-none'][2], e['DS-none'][0], e['DS-obs'][2], e['DS-obs'][0], 'instr', 0, 'P1 24 Oct: DS1-none vs DS1-obs (base = board), r51–100'),
      ('DS', 'arithmetic rival (fixed)', dmf[2], dmf[0], dt_m, dt_sd, 'rival', 0, 'P1 24 Oct: DS1-fixed vs DS1-twin, r100'),
      ('DS', 'arithmetic rival (best reply)', dmb[2], dmb[0], dt_m, dt_sd, 'rival', 0, 'P1 24 Oct: DS1-mech vs DS1-twin, r100')]
rows7 = []
print(f'  {"model":5s} {"point":30s} {"restr":>6s} {"sd":>5s} {"base":>6s} {"b.sd":>5s} | {"x":>6s} {"x plot":>6s} {"y(A)":>6s} {"y(B)":>6s} | source')
for mk, lab, rm, rs, bm, bs, ck, pre, src in P:
    x = (bm - rm) / (bm - COMP); xp = min(max(x, -0.5), 1.2)
    ya = CTRL[ck][0]; yb = (1 - rs / bs) if bs else None
    rows7.append(dict(mk=mk, lab=lab, x=x, xp=xp, ya=ya, yb=yb, pre=pre, clipped=xp != x))
    print(f'  {mk:5s} {lab:30s} {rm:6.3f} {rs:5.3f} {bm:6.3f} {(bs if bs is not None else float("nan")):5.3f} | {x:+6.3f} {xp:+6.3f} {ya:6.3f} {("%+6.3f" % yb) if yb is not None else "   n/a"} | {src}')
print('  control rule:', ' · '.join(v[1] for v in CTRL.values()))
LABEL_AT = {  # hand placements where the automatic stagger collides (offsets in points)
    ('ya', 'HK', 'forced cut'): (-45, 32), ('ya', 'HK', 'start at competition'): (0, -55), ('ya', 'HK', 'no ceiling'): (-15, 64),
    ('ya', 'HK', 'undercutting sentence'): (45, 46), ('ya', 'HK', 'patrol 10%'): (30, -62), ('ya', 'DS', 'no board'): (35, -62), ('ya', 'DS', 'start at competition'): (-45, -42), ('ya', 'DS', 'arithmetic rival (fixed)'): (75, -10), ('ya', 'DS', 'arithmetic rival (best reply)'): (-60, -22),
    ('ya', 'DS', 'patrol 10%'): (20, -30), ('ya', 'DS', 'undercutting sentence'): (40, 30),
    ('yb', 'HK', 'no ceiling'): (-50, 36), ('yb', 'HK', 'undercutting sentence'): (45, 52), ('yb', 'HK', 'patrol 10%'): (48, -16),
    ('yb', 'HK', 'start at competition'): (-50, 16), ('yb', 'HK', 'patrol 1%'): (0, -20), ('yb', 'DS', 'start at competition'): (0, 18)}
def frontier(ykey, ylabel, title, path, ylim, note):
    fig, ax = plt.subplots(figsize=(16, 9), facecolor=SURF); style(ax); ax.grid(axis='x', color='#ebeae6', lw=0.8)
    ax.axvspan(0.95, 1.05, color=AQ, alpha=0.12, lw=0); ax.text(1.0, ylim[0] + 0.01 * (ylim[1] - ylim[0]), 'back to\ncompetition', color=AQ, fontsize=9, ha='center', va='bottom')
    ax.axvline(0, color=MUTED, lw=1, ls=(0, (4, 3))); ax.text(0.01, ylim[0], ' no change', color=MUTED, fontsize=8.5, va='bottom')
    if ylim[0] < 0 < ylim[1]: ax.axhline(0, color=MUTED, lw=0.8)
    for mk, col, mkr, nm in (('HK', BLUE, 'o', 'Claude Haiku 5.5'), ('DS', OR, '^', 'DeepSeek v4.1 flash')):
        for k, r in enumerate(sorted((x for x in rows7 if x['mk'] == mk and x[ykey] is not None), key=lambda x: x['xp'])):
            y = r[ykey]
            if y is None: continue
            yp = min(max(y, ylim[0] + 0.02), ylim[1] - 0.02)
            ax.scatter([r['xp']], [yp], s=200 if r['pre'] else 90, marker=mkr, facecolors='none' if r['pre'] else col, edgecolors=col, linewidths=1.8, zorder=6 if r['pre'] else 4)
            if r['clipped']: ax.annotate('', xy=(r['xp'] + (0.06 if r['x'] > 1.2 else -0.06), yp), xytext=(r['xp'], yp), arrowprops=dict(arrowstyle='->', color=col, lw=1.6))
            if yp != y: ax.annotate('', xy=(r['xp'], yp - 0.05 if y < yp else yp + 0.05), xytext=(r['xp'], yp), arrowprops=dict(arrowstyle='->', color=col, lw=1.6))
            txt = r['lab'] + (f' (x = {r["x"]:+.2f})' if r['clipped'] else '') + (f' (y = {y:+.2f})' if yp != y else '')
            dy = (16 + 12 * (k % 4)) * (1 if mk == 'HK' else -1); dx = 0
            dx, dy = LABEL_AT.get((ykey, mk, r['lab']), (dx, dy))
            ax.annotate(txt, (r['xp'], yp), xytext=(dx, dy), textcoords='offset points', fontsize=8, color=col, ha='center', va='center',
                        arrowprops=dict(arrowstyle='-', color=col, lw=0.5, alpha=0.5, shrinkA=1, shrinkB=5))
    ax.scatter([], [], s=70, marker='o', color=BLUE, label='Claude Haiku 5.5'); ax.scatter([], [], s=70, marker='^', color=OR, label='DeepSeek v4.1 flash')
    ax.legend(frameon=False, fontsize=9.5, loc='lower left' if ykey == 'ya' else 'lower right', bbox_to_anchor=None if ykey == 'ya' else (0.93, 0.1))
    ax.set_xlim(-0.6, 1.3); ax.set_ylim(*ylim)
    ax.set_xlabel(f'share of the collusion removed  =  (base price − restricted price) / (base price − competitive {COMP}), round 100 (‡ rows: rounds 51–100)', color=MUTED)
    ax.set_ylabel(ylabel, color=MUTED)
    fig.suptitle(title, x=0.04, ha='left', fontsize=14, color=INK)
    fig.text(0.04, 0.925, note + '\nEach point is one restriction on one model, against that restriction\'s own base as Table 2 gives it. Numbers: Table 2 / F1 of the Market A draft;\nDeepSeek board, law and rival cells: first wording, 24 Oct; sds the tables lack are recomputed from the run files. After Greenblatt et al. (2023).', fontsize=9.3, color=MUTED, va='top')
    fig.tight_layout(rect=(0, 0, 0.99, 0.87)); fig.savefig(path, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', path)
frontier('ya', 'share of price decisions left to the sellers', 'Which restriction removes the most collusion at the least cost? (top right is best)',
         f'{OUT}/fig-frontier-control-2026-10-23.png', (0.38, 1.10),
         'Y rule: share of all seller decisions in the market\'s history (seeded and live, both sellers) that the sellers chose themselves. Patrol 4 forced of 200 = 0.98; start at competition 10 seeded of 210 = 0.952;\n'
         'forced cut 1 of 200 = 0.995; arithmetic rival 100 scripted + 20 seeded of 220 = 0.455; instructions, the law line and the board change no decision = 1.0.')
frontier('yb', 'predictability  =  1 − (sd of the restricted runs / sd of the base runs)', 'Removing collusion and making markets predictable',
         f'{OUT}/fig-frontier-predictability-2026-10-23.png', (-1.25, 1.12),
         f'Y: 0 = markets as spread out as without the restriction; 1 = every market lands at the same price; below 0 = more spread out than the base. The forced cut has no point here: its base is {len(nc_vals)} copies of one history, all at {S.mean(nc_vals):.2f} (sd {S.pstdev(nc_vals):.2f}).')

# ─────────────────────────────── (8) Table 2 as a chart, one file per model (coordinator's ask: Results one model at a time) ───────────────────────────────
# Rows in the paper's numbering. Each row: the run files Table 2 / F1 name, its OWN base (Table 2: rows 4 and 7 use the 23 Oct base; 1–2 the 13 Oct base;
# 3 the uncut copies of the same history (F1); 5 and 8 the 'vs' arm of the same batch (‡: rounds 51–100); 6 the Haiku twin with the same seed (F1); 9 no question).
print('\n=== (8) Table 2 charts — per row: mean, n, base used ===')
from matplotlib.transforms import blended_transform_factory
from matplotlib.lines import Line2D
B13H = ('runs/floor-n2-P1-a32-c234-rep*.jsonl', 'base, 13 Oct'); B23H = ('runs/BASE23-HK-rep*.jsonl', 'base, 23 Oct (same day)')
B13D = ('runs/DS-floor-rep*.jsonl', 'base, 13 Oct †'); B23D = ('runs/BASE23-DS-rep*.jsonl', 'base, 23 Oct (same day)')
T2 = {'HK': [  # (number, label, pattern(s), base (pattern, label), dagger-dag ‡, prepin, faint)
        ('1', 'told ceiling 1.5×', ['runs/C1-c15-rep*.jsonl'], B13H, 0, 0, 0),
        ('1', 'told ceiling: none', ['runs/SD-NC-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('2', 'the undercutting sentence', ['runs/SD-P2-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('3', 'one forced cut (copies)', ['runs/FORK-floor2-cut-b*.jsonl', 'runs/WHO-clean-b*.jsonl'], ('runs/FORK-floor2-nocut-b*.jsonl', 'uncut copies of the same history'), 0, 0, 0),
        ('4', 'patrol 5%', ['runs/PA5-HK-rep*.jsonl'], B23H, 0, 0, 1),
        ('4', 'patrol 10%', ['runs/PA10-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('4', 'patrol 20%', ['runs/PA20-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('5', 'the law line alone', ['runs/TWIN-lawonly-rep*.jsonl'], ('runs/TWIN-none-rep*.jsonl', 'same batch, no law line'), 1, 0, 0),
        ('6', 'arithmetic rival: fixed', ['runs/MECH-fixed-rep*.jsonl'], ('runs/MECH-twin-rep*.jsonl', 'Haiku rival, same seed'), 0, 0, 0),
        ('6', 'arithmetic rival: best reply', ['runs/MECH-br-rep*.jsonl'], ('runs/MECH-twin-rep*.jsonl', 'Haiku rival, same seed'), 0, 0, 0),
        ('7', 'start at competition', ['runs/SA-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('8', 'no board (vs the board)', ['runs/e/HK-none-rep*.jsonl'], ('runs/e/HK-obs-rep*.jsonl', 'observation board, 14 Oct'), 1, 0, 0)],
      'DS': [
        ('1', 'told ceiling 1.5×', ['runs/ceil24/DSC15-rep*.jsonl'], ('runs/ceil24/DSB24-rep*.jsonl', 'base, 24 Oct (same window)'), 0, 0, 0),
        ('1', 'told ceiling: none', ['runs/SD-NC-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('2', 'the undercutting sentence', ['runs/SD-P2-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('3', 'one forced cut — not run on DeepSeek', [], None, 0, 0, 0),
        ('4', 'patrol 5%', ['runs/PA5-DS-rep*.jsonl'], B23D, 0, 0, 1),
        ('4', 'patrol 10%', ['runs/PA10-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('4', 'patrol 20%', ['runs/PA20-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('5', 'the law line alone', ['runs/ds1/DS1-lawonly-rep*.jsonl'], ('runs/ds1/DS1-none-rep*.jsonl', 'same batch, no law line'), 1, 0, 0),
        ('5', 'the law line (board + law)', ['runs/ds1/DS1-obslaw-rep*.jsonl'], ('runs/ds1/DS1-obs-rep*.jsonl', 'same board, no law line'), 1, 0, 0),
        ('6', 'arithmetic rival: fixed', ['runs/ds1/DS1-fixed-rep*.jsonl'], ('runs/ds1/DS1-twin-rep*.jsonl', 'DeepSeek rival, same seed'), 0, 0, 0),
        ('6', 'arithmetic rival: best reply', ['runs/ds1/DS1-mech-rep*.jsonl'], ('runs/ds1/DS1-twin-rep*.jsonl', 'DeepSeek rival, same seed'), 0, 0, 0),
        ('7', 'start at competition', ['runs/SA-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('8', 'no board (vs the board)', ['runs/ds1/DS1-none-rep*.jsonl'], ('runs/ds1/DS1-obs-rep*.jsonl', 'observation board, 24 Oct'), 1, 0, 0),
        ('9', 'the watcher: a colour asked first', ['runs/a5p1/A5P1-before-rep[1-8].jsonl'], ('runs/a5p1/A5P1-noask-rep[1-8].jsonl', 'no question, same batch'), 0, 0, 0)]}
def vals(pats, dag):
    v = []
    for pat in pats: v += cellvals(pat, 51, 100) if dag else cellvals(pat)
    return v
for mk, mname, mcol, mkr, fname in (('HK', 'Haiku', BLUE, 'o', 'haiku'), ('DS', 'DeepSeek', OR, 'o', 'deepseek')):
    rows = T2[mk]; nR = len(rows)
    fig, ax = plt.subplots(figsize=(12, 9), facecolor=SURF); style(ax); ax.grid(axis='y', visible=False); ax.grid(axis='x', color='#ebeae6', lw=0.8)
    allx = []; tr = blended_transform_factory(ax.transAxes, ax.transData)
    for k, (num, lab, pats, base, dag, pre, faint) in enumerate(rows):
        y = nR - 1 - k
        if k and rows[k - 1][0] != num: ax.axhline(y + 0.5, color='#dddcd7', lw=0.8)
        if not pats:
            ax.text(1.5, y, 'not run on this model', color=MUTED, fontsize=9, va='center', style='italic'); print(f'  {mk} {num} {lab}'); continue
        v = vals(pats, dag); bv = vals([base[0]], dag); allx += v + bv
        bm, bs = S.mean(bv), (S.stdev(bv) if len(bv) > 1 else 0.0); m = S.mean(v)
        ax.add_patch(plt.Rectangle((bm - bs, y - 0.32), max(2 * bs, 0.004), 0.64, color=GREY, alpha=0.28, lw=0))
        ax.plot([bm, bm], [y - 0.32, y + 0.32], color='#8a8984', lw=1.2)
        ax.text(bm + bs + 0.012, y + 0.2, f'{base[1]}{" ‡" if dag else ""}: {bm:.2f} ± {bs:.2f} (n {len(bv)})', color='#6f6e69', fontsize=7.5, va='center')
        al = 0.35 if faint else 0.85
        js = [((i % 5) - 2) * 0.06 for i in range(len(v))]
        ax.scatter(v, [y + j for j in js], s=26, marker=mkr, facecolors=SURF if pre else mcol, edgecolors=mcol, linewidths=1.2, alpha=al, zorder=3)
        ax.plot([m, m], [y - 0.3, y + 0.3], color=mcol, lw=4 if not faint else 2.5, alpha=1 if not faint else 0.45, zorder=4, solid_capstyle='butt')
        ax.text(1.005, y, f'{m:.2f}   n {len(v)}', transform=tr, color=mcol, fontsize=9, va='center', alpha=1 if not faint else 0.55)
        print(f'  {mk} {num} {lab:38s} mean {m:.3f} (sd {S.stdev(v) if len(v) > 1 else 0:.3f}) n {len(v):2d} {"r51-100" if dag else "r100   "} | base: {base[1]} = {bm:.3f} ± {bs:.3f} n {len(bv)} | files {", ".join(pats)} vs {base[0]}')
    ax.set_yticks(range(nR)); ax.set_yticklabels([f'{r[0]} · {r[1]}{" ‡" if r[4] else ""}{" †" if r[5] else ""}' for r in reversed(rows)], fontsize=10)
    for t, r in zip(ax.get_yticklabels(), reversed(rows)): t.set_color(MUTED if (r[6] or not r[2]) else INK)
    for xv, lb in ((COMP, f'competitive {COMP}'), (1.925, 'cartel 1.925')):
        ax.axvline(xv, color=MUTED, lw=1, ls=(0, (4, 3))); ax.text(xv, nR - 0.35, lb, color=MUTED, fontsize=8.5, ha='center', va='bottom')
    ax.set_xlim(min(allx + [COMP]) - 0.1, max(3.0, max(allx) + 0.05)); ax.set_ylim(-0.6, nR - 0.1)
    ax.set_xlabel('market price (cost = 1), mean of the two sellers: round 100, or the rounds 51–100 mean on ‡ rows', color=MUTED)
    ax.text(1.005, nR - 0.35, 'mean   runs', transform=tr, color=MUTED, fontsize=8.5, va='bottom')
    hand = [Line2D([], [], marker=mkr, ls='', color=mcol, label='one market'), Line2D([], [], color=mcol, lw=4, label='cell mean'),
            plt.Rectangle((0, 0), 1, 1, color=GREY, alpha=0.28, label='its own base: mean ± sd')]
    if mk == 'DS': hand.append(Line2D([], [], marker=mkr, ls='', markerfacecolor=SURF, color=mcol, label='† before the host was pinned'))
    fig.legend(handles=hand, frameon=False, fontsize=9, loc='upper left', bbox_to_anchor=(0.03, 0.885), ncol=len(hand))
    fig.suptitle(f'{mname}: each restriction against its own base', x=0.04, ha='left', fontsize=14, color=INK)
    fig.text(0.04, 0.925, 'Rows in the paper\'s numbering (Table 2). Each dot is one market; the bold tick is the cell mean; the grey band is that row\'s own base (mean ± sd), labelled on the row.\n'
             f'Patrol 5% drawn faint. ‡ rounds 51–100 mean. {"† pre-pin DeepSeek (hollow), against the pre-pin 13 Oct base. Rows 5, 6, 8 and 9: first wording, 24 Oct. " if mk == "DS" else "Row 9 (the watcher) is omitted: Table 2 gives Haiku a talk measure, not a price. "}Counts from the run files.',
             fontsize=9.3, color=MUTED, va='top')
    fig.tight_layout(rect=(0, 0, 0.92, 0.86))
    pp = f'{OUT}/fig-table2-{fname}-2026-10-23.png'; fig.savefig(pp, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', pp)

# ─────────────────────────────── (7c) the frontier for the paper, taller, one continuous y-axis (24 Oct, her notes: readable, and no cut axis — "bigger vertically than look fake") ───────────────────────────────
# Same points as (7) 'ya'. Labels of the 1.0 row sit above it in three levels; labels of the 0.98 row sit below it. 'forced cut' is labelled 'the release' (her vocabulary ruling).
def frontier_tall(path):
    fig, ax = plt.subplots(figsize=(10, 7.4), facecolor=SURF); style(ax); ax.grid(axis='x', color='#ebeae6', lw=0.8)
    lo, hi = 0.40, 1.07
    ax.axvspan(0.95, 1.05, color=AQ, alpha=0.12, lw=0); ax.text(1.0, 0.70, 'back to\ncompetition', color=AQ, fontsize=10, ha='center', va='center')
    ax.axvline(0, color=MUTED, lw=1, ls=(0, (4, 3))); ax.text(0.012, lo + 0.004, 'no change', color=MUTED, fontsize=10, va='bottom')
    rename = {'forced cut': 'the release'}
    L1, L2, L3, B1, B2, B3 = 12, 26, 40, -13, -27, -41
    place = {('HK', 'no board'): (0, L1), ('HK', 'law line'): (0, L2), ('DS', 'law line alone'): (12, L1), ('DS', 'law line'): (0, L3),
             ('DS', 'no ceiling'): (0, L1), ('DS', 'no board'): (-6, L1), ('HK', 'ceiling 1.5×'): (0, L2), ('DS', 'ceiling 1.5×'): (8, L1),
             ('HK', 'no ceiling'): (0, L3), ('HK', 'undercutting sentence'): (0, L2), ('DS', 'undercutting sentence'): (0, L3),
             ('HK', 'the release'): (-60, -95),
             ('DS', 'patrol 1%'): (0, -20), ('HK', 'patrol 1%'): (-28, -20), ('HK', 'patrol 5%'): (0, -20), ('HK', 'patrol 10%'): (2, -20),
             ('DS', 'patrol 5%'): (-20, -45), ('HK', 'patrol 20%'): (14, -20), ('DS', 'patrol 20%'): (10, -65), ('DS', 'patrol 10%'): (15, -20),
             ('HK', 'start at competition'): (0, -45), ('DS', 'start at competition'): (0, -20),
             ('HK', 'arithmetic rival (fixed)'): (-60, 16), ('HK', 'arithmetic rival (best reply)'): (-120, 0), ('DS', 'arithmetic rival (fixed)'): (70, 0), ('DS', 'arithmetic rival (best reply)'): (-40, -16)}
    for mk, col, mkr in (('HK', BLUE, 'o'), ('DS', OR, '^')):
        for r in (x for x in rows7 if x['mk'] == mk):
            y = r['ya']; lab = rename.get(r['lab'], r['lab'])
            ax.scatter([r['xp']], [y], s=70, marker=mkr, facecolors=col, edgecolors=col, linewidths=1.4, zorder=4)
            if r['clipped']: ax.annotate('', xy=(r['xp'] - 0.06, y), xytext=(r['xp'], y), arrowprops=dict(arrowstyle='->', color=col, lw=1.5))
            txt = lab + (f' (x = {r["x"]:+.2f})' if r['clipped'] else '')
            ax.annotate(txt, (r['xp'], y), xytext=place.get((mk, lab), (0, 13)), textcoords='offset points', fontsize=9.5, color=col,
                        ha='center', va='center', arrowprops=dict(arrowstyle='-', color=col, lw=0.5, alpha=0.5, shrinkA=1, shrinkB=4))
    ax.scatter([], [], s=60, marker='o', color=BLUE, label='Claude Haiku 5.5'); ax.scatter([], [], s=60, marker='^', color=OR, label='DeepSeek v4.1 flash')
    ax.legend(frameon=False, fontsize=10.5, loc='center left', bbox_to_anchor=(0.0, 0.42))
    ax.set_xlim(-0.6, 1.3); ax.set_ylim(lo, hi); ax.set_yticks([0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]); ax.tick_params(labelsize=10)
    ax.set_xlabel('share of the collusion removed = (base price − restricted price) / (base price − competitive 1.473)', color=MUTED, fontsize=10.5)
    ax.set_ylabel('share of price decisions left to the sellers', color=MUTED, fontsize=10.5)
    fig.suptitle('Which restriction removes the most collusion at the least cost? (top right is best)', x=0.07, ha='left', fontsize=12.5, color=INK)
    fig.tight_layout(rect=(0, 0, 1, 0.96)); fig.savefig(path, dpi=130, facecolor=SURF); plt.close(fig); print('wrote', path)
frontier_tall(f'{OUT}/fig-frontier-tall-2026-10-24.png')
