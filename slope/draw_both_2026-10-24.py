#!/usr/bin/env python3
"""draw_both_2026-10-24.py — the three per-model figure pairs of draw_three_2026-10-23.py, each redrawn as ONE figure with both models,
so the Results can be organised by what was tested rather than by model. From the run files alone; nothing imported from draw_three
(importing it would re-run all its drawing); the helpers, file patterns, run selections and Table rows below are copied from it verbatim.
Run from experiments/sprint-2026-10/slope:  uv run --with matplotlib python3 draw_both_2026-10-24.py
  (8) -> lab-book-figs/fig-restrictions-both-2026-10-24.png    (draw_three section 8, both models side by side, shared row labels)
  (5A) -> lab-book-figs/fig-patrol-doses-both-2026-10-24.png   (draw_three draw5a, Haiku block left, DeepSeek block right, one y axis)
  (5B) -> lab-book-figs/fig-patrol-recovery-both-2026-10-24.png (draw_three draw5b, the two models side by side)
Every mean and n drawn is printed, in lines tagged CHECK, for comparison with draw_three's own printout."""
import json, glob, os, statistics as S
import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.transforms import blended_transform_factory
from matplotlib.lines import Line2D
OUT = 'lab-book-figs'; os.makedirs(OUT, exist_ok=True)
BLUE, OR, AQ, YEL, INK, MUTED, SURF = '#2a78d6', '#eb6834', '#1baf7a', '#eda100', '#0b0b0b', '#52514e', '#fcfcfb'
PUR, GREY = '#8a5cd6', '#9a9893'
COMP = 1.473   # competitive (Nash) price, Calvano setting (as draw_three)
FS = 8.5       # smallest font anywhere in these figures

# ───────────── helpers, copied from draw_three_2026-10-23.py ─────────────
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
def style(ax):
    ax.set_facecolor(SURF)
    for s in ('top', 'right'): ax.spines[s].set_visible(False)
    for s in ('left', 'bottom'): ax.spines[s].set_color('#c9c8c3')
    ax.tick_params(colors=MUTED, labelsize=9); ax.grid(axis='y', color='#ebeae6', lw=0.8)
def want(pattern, n=None):
    fs = sorted(glob.glob(pattern)); print(f'  files: {pattern} -> {len(fs)}' + ('' if n is None or len(fs) == n else f' (first expected {n})'))
    return fs
def ns(counts):
    c = sorted(set(counts)); return str(c[0]) if len(c) == 1 else f'{c[0]}–{c[-1]}'
def cellvals(pat, lo=100, hi=100):
    out = []
    for f in sorted(glob.glob(pat)):
        _, rows, _ = load(f); out.append(S.mean(S.mean(rows[t]) for t in range(lo, hi + 1)))
    return out
def vals(pats, dag):
    v = []
    for pat in pats: v += cellvals(pat, 51, 100) if dag else cellvals(pat)
    return v
PROBES = (20, 40, 60, 80)

# ───────────── (8) the restrictions, both models ─────────────
print('=== (8) restrictions, both models — per row: mean, n, base used ===')
# T2: copied verbatim from draw_three section (8) (same patterns, bases, ‡ / † / faint flags)
B13H = ('runs/floor-n2-P1-a32-c234-rep*.jsonl', 'base, 13 Oct'); B23H = ('runs/BASE23-HK-rep*.jsonl', 'base, 23 Oct (same day)')
B13D = ('runs/DS-floor-rep*.jsonl', 'base, 13 Oct †'); B23D = ('runs/BASE23-DS-rep*.jsonl', 'base, 23 Oct (same day)')
T2 = {'HK': [  # (number, label, pattern(s), base (pattern, label), dagger-dag ‡, prepin, faint)
        ('1', 'told ceiling 1.5×', ['runs/C1-c15-rep*.jsonl'], B13H, 0, 0, 0),
        ('1', 'told ceiling: none', ['runs/SD-NC-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('2', 'the undercutting sentence', ['runs/SD-P2-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('3', 'the release (copies)', ['runs/FORK-floor2-cut-b*.jsonl', 'runs/WHO-clean-b*.jsonl'], ('runs/FORK-floor2-nocut-b*.jsonl', 'uncut copies of the same history'), 0, 0, 0),
        ('4', 'patrol 5%', ['runs/PA5-HK-rep*.jsonl'], B23H, 0, 0, 1),
        ('4', 'patrol 10%', ['runs/PA10-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('4', 'patrol 20%', ['runs/PA20-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('5', 'the law line alone', ['runs/TWIN-lawonly-rep*.jsonl'], ('runs/TWIN-none-rep*.jsonl', 'same batch, no law line'), 1, 0, 0),
        ('5', 'the law line (board + law)', ['runs/e/HK-obslaw-rep*.jsonl'], ('runs/e/HK-obs-rep*.jsonl', 'same board, no law line'), 1, 0, 0),
        ('6', 'arithmetic rival: fixed', ['runs/MECH-fixed-rep*.jsonl'], ('runs/MECH-twin-rep*.jsonl', 'Haiku rival, same seed'), 0, 0, 0),
        ('6', 'arithmetic rival: best reply', ['runs/MECH-br-rep*.jsonl'], ('runs/MECH-twin-rep*.jsonl', 'Haiku rival, same seed'), 0, 0, 0),
        ('7', 'start at competition', ['runs/SA-HK-rep*.jsonl'], B23H, 0, 0, 0),
        ('8', 'no board (vs the board)', ['runs/e/HK-none-rep*.jsonl'], ('runs/e/HK-obs-rep*.jsonl', 'observation board, 14 Oct'), 1, 0, 0)],
      'DS': [
        ('1', 'told ceiling 1.5×', ['runs/ceil24/DSC15-rep*.jsonl'], ('runs/ceil24/DSB24-rep*.jsonl', 'base, 24 Oct (same window)'), 0, 0, 0),
        ('1', 'told ceiling: none', ['runs/SD-NC-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('2', 'the undercutting sentence', ['runs/SD-P2-DS-rep*.jsonl'], B23D, 0, 0, 0),
        ('3', 'the release — not run on DeepSeek', [], None, 0, 0, 0),
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
# The shared rows: (number, shared label, ‡, faint, HK entry, DS entry); an entry is an index into T2[model] or a note string.
# The index's label is asserted below, so every drawn cell is exactly a draw_three cell.
UNION = [('1', 'told ceiling 1.5×', 0, 0, 0, 0),
         ('1', 'told ceiling: none', 0, 0, 1, 1),
         ('2', 'the undercutting sentence', 0, 0, 2, 2),
         ('3', 'the release (copies)', 0, 0, 3, 3),            # T2 DS[3] has no files: drawn as 'not run on this model'
         ('4', 'patrol 5%', 0, 1, 4, 4),
         ('4', 'patrol 10%', 0, 0, 5, 5),
         ('4', 'patrol 20%', 0, 0, 6, 6),
         ('5', 'the law line alone', 1, 0, 7, 7),
         ('5', 'the law line (board + law)', 1, 0, 8, 8),
         ('6', 'arithmetic rival: fixed', 0, 0, 9, 9),
         ('6', 'arithmetic rival: best reply', 0, 0, 10, 10),
         ('7', 'start at competition', 0, 0, 11, 11),
         ('8', 'no board (vs the board)', 1, 0, 12, 12),
         ('9', 'the watcher: a colour asked first', 0, 0, 'price not measured; talk only (Appendix F.7)', 13)]
for num, lab, dag, faint, eh, ed in UNION:
    for mk, e in (('HK', eh), ('DS', ed)):
        if isinstance(e, int):
            r = T2[mk][e]; assert r[0] == num and (r[1] == lab or not r[2]), (mk, e, r[1], lab)
            if r[2]: assert r[4] == dag and r[6] == faint, (mk, lab)
assert sorted(e for *_, e, _ in UNION if isinstance(e, int)) == list(range(len(T2['HK']))), 'every Haiku T2 row drawn once'
assert sorted(e for *_, e in UNION if isinstance(e, int)) == list(range(len(T2['DS']))), 'every DeepSeek T2 row drawn once'

# compute every cell once
CELL = {}
for num, lab, dag, faint, eh, ed in UNION:
    for mk, e in (('HK', eh), ('DS', ed)):
        if not isinstance(e, int) or not T2[mk][e][2]: continue
        _, rl, pats, base, dg, pre, fa = T2[mk][e]
        v = vals(pats, dg); bv = vals([base[0]], dg)
        CELL[(mk, num, lab)] = dict(v=v, bv=bv, m=S.mean(v), bm=S.mean(bv), bs=(S.stdev(bv) if len(bv) > 1 else 0.0), base=base, dag=dg, pre=pre, faint=fa, pats=pats)
        c = CELL[(mk, num, lab)]
        print(f'CHECK T2 {mk} {num} {rl:38s} mean {c["m"]:.3f} (sd {S.stdev(v) if len(v) > 1 else 0:.3f}) n {len(v):2d} {"r51-100" if dg else "r100   "} | '
              f'base: {base[1]} = {c["bm"]:.3f} ± {c["bs"]:.3f} n {len(bv)} | files {", ".join(pats)} vs {base[0]}')
allx = [x for c in CELL.values() for x in c['v'] + c['bv']]
XL = (min(allx + [COMP]) - 0.1, max(3.0, max(allx) + 0.05))
nR = len(UNION)
MOD8 = (('HK', 'Claude Haiku 5.5', BLUE, 4), ('DS', 'DeepSeek v4.1 flash', OR, 5))
fig = plt.figure(figsize=(16, 9.4), facecolor=SURF)
gs = fig.add_gridspec(1, 2, left=0.168, right=0.928, top=0.79, bottom=0.075, wspace=0.17)
axs = [fig.add_subplot(gs[0, 0])]; axs.append(fig.add_subplot(gs[0, 1], sharey=axs[0]))
fig.canvas.draw(); rend = fig.canvas.get_renderer()
for ax, (mk, mname, mcol, ei) in zip(axs, MOD8):
    style(ax); ax.grid(axis='y', visible=False); ax.grid(axis='x', color='#ebeae6', lw=0.8)
    ax.set_xlim(*XL); ax.set_ylim(-0.6, nR - 0.05)
    tr = blended_transform_factory(ax.transAxes, ax.transData)
    for xv, lb in ((COMP, f'competitive {COMP}'), (1.925, 'cartel 1.925')):
        ax.axvline(xv, color=MUTED, lw=1, ls=(0, (4, 3)), zorder=1); ax.text(xv, nR - 0.4, lb, color=MUTED, fontsize=FS, ha='center', va='bottom')
    ax.text(1.012, nR - 0.4, 'mean   runs', transform=tr, color=MUTED, fontsize=FS, va='bottom')
    for k, row in enumerate(UNION):
        num, lab, dag, faint, e = row[0], row[1], row[2], row[3], row[ei]; y = nR - 1 - k
        if k and UNION[k - 1][0] != num: ax.axhline(y + 0.5, color='#dddcd7', lw=0.8, zorder=0)
        if not isinstance(e, int) or not T2[mk][e][2]:
            note = e if isinstance(e, str) else 'not run on this model'
            ax.text(COMP + 0.03, y, note, color=MUTED, fontsize=9.5, va='center', style='italic', zorder=5,
                    bbox=dict(boxstyle='square,pad=0.1', facecolor=SURF, edgecolor='none', alpha=0.9)); continue
        c = CELL[(mk, num, lab)]; v, bv, m, bm, bs = c['v'], c['bv'], c['m'], c['bm'], c['bs']
        ax.add_patch(plt.Rectangle((bm - bs, y - 0.22), max(2 * bs, 0.004), 0.44, color=GREY, alpha=0.28, lw=0, zorder=1))
        ax.plot([bm, bm], [y - 0.22, y + 0.22], color='#8a8984', lw=1.2, zorder=2)
        t = ax.text(bm - bs, y + 0.25, f'{c["base"][1]}{" ‡" if c["dag"] else ""}: {bm:.2f} ± {bs:.2f} (n {len(bv)})', color='#5e5d58', fontsize=FS, va='bottom', ha='left', zorder=5,
                    bbox=dict(boxstyle='square,pad=0.08', facecolor=SURF, edgecolor='none', alpha=0.85))
        bb = t.get_window_extent(renderer=rend); axbb = ax.get_window_extent(renderer=rend)
        if bb.x1 > axbb.x1: t.set_ha('right'); t.set_x(XL[1])       # would overflow into the means column: right-align at the axis end
        al = 0.35 if c['faint'] else 0.85
        js = [((i % 5) - 2) * 0.06 for i in range(len(v))]
        ax.scatter(v, [y + j for j in js], s=26, marker='o', facecolors=SURF if c['pre'] else mcol, edgecolors=mcol, linewidths=1.2, alpha=al, zorder=3)
        ax.plot([m, m], [y - 0.24, y + 0.24], color=mcol, lw=4 if not c['faint'] else 2.5, alpha=1 if not c['faint'] else 0.45, zorder=4, solid_capstyle='butt')
        ax.text(1.012, y, f'{m:.2f}   n {len(v)}', transform=tr, color=mcol, fontsize=9.5, va='center', alpha=1 if not c['faint'] else 0.55)
    ax.set_title(mname, loc='left', fontsize=13, color=mcol, pad=20)
    ax.set_xlabel('market price (cost = 1), mean of the two sellers:\nround 100, or the rounds 51–100 mean on ‡ rows', color=MUTED, fontsize=9.5)
axs[0].set_yticks(range(nR))
axs[0].set_yticklabels([f'{r[0]} · {r[1]}{" ‡" if r[2] else ""}{"  († DeepSeek)" if T2["DS"][r[5]][5] else ""}' for r in reversed(UNION)], fontsize=10)
for t, r in zip(axs[0].get_yticklabels(), reversed(UNION)): t.set_color(MUTED if r[3] else INK)
axs[1].tick_params(labelleft=False)
hand = [Line2D([], [], marker='o', ls='', color=BLUE, label='one market (Haiku)'), Line2D([], [], marker='o', ls='', color=OR, label='one market (DeepSeek)'),
        Line2D([], [], color=INK, lw=4, label='cell mean'), plt.Rectangle((0, 0), 1, 1, color=GREY, alpha=0.28, label='its own base: mean ± sd')]
fig.legend(handles=hand, frameon=False, fontsize=9.5, loc='upper left', bbox_to_anchor=(0.03, 0.895), ncol=len(hand))
fig.suptitle('Each restriction against its own base, both models', x=0.03, y=0.985, ha='left', fontsize=14, color=INK)
fig.text(0.03, 0.945, 'Rows in the paper\'s numbering (Table 1). Each dot is one market; the bold tick is the cell mean; the grey band is that row\'s own base (mean ± sd), labelled on the row. Patrol 5% drawn faint.\n'
         '‡ rounds 51–100 mean. DeepSeek rows 1 (1.5 ×), 5, 6, 8 and 9: 24 Oct, pinned host, same window as their base. Counts from the run files.',
         fontsize=9.5, color=MUTED, va='top')
p8 = f'{OUT}/fig-restrictions-both-2026-10-24.png'; fig.savefig(p8, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p8)

# ───────────── (5A) the patrol doses, both models ─────────────
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
    print(f'CHECK 5A {cell:10s} n={len(runs)} r100 mean {S.mean(r["r100"] for r in runs):.3f} | r51-100 mean {S.mean(r["w"] for r in runs):.3f}')
MODELS5 = (('HK', 'Claude Haiku 5.5', BLUE), ('DS', 'DeepSeek v4.1 flash (Together)', OR))
ymax5 = max(max(S.mean(v) for v in r['rows'].values()) for k in D5 for r in D5[k]) + 0.15
fig = plt.figure(figsize=(16, 9.4), facecolor=SURF)
outer = fig.add_gridspec(1, 2, left=0.06, right=0.985, top=0.80, bottom=0.07, wspace=0.12)
first = None
for b, (mk, mname, mcol) in enumerate(MODELS5):
    inner = outer[0, b].subgridspec(3, 2, hspace=0.42, wspace=0.10)
    base = D5.get(f'BASE23-{mk}', [])
    for j, (dk, dlab, _) in enumerate(DOSES):
        ax = fig.add_subplot(inner[j // 2, j % 2], sharex=first, sharey=first); first = first or ax; style(ax)
        cell = f'{dk}-{mk}'
        for r in base:
            xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=GREY, alpha=0.55, lw=0.9)
        for p in PROBES: ax.axvline(p, color=MUTED, lw=0.8, alpha=0.5)
        for y in (COMP, 1.925): ax.axhline(y, color=MUTED, lw=1, ls=(0, (4, 3)))
        if j == 0: ax.text(21, 1.06, 'cuts at 20, 40, 60, 80', color=MUTED, fontsize=FS, ha='left', va='bottom')
        runs = D5.get(cell, [])
        for r in runs:
            xs, ys = mpath(r['rows'], 1, 100); ax.plot(xs, ys, color=mcol, alpha=0.35, lw=0.9)
        if runs:
            m = [S.mean(S.mean(r['rows'][t]) for r in runs) for t in range(1, 101)]
            ax.plot(range(1, 101), m, color=mcol, lw=2.3)
        ax.set_xlim(1, 100); ax.set_ylim(1.0, ymax5)
        ax.set_title(f'patrol −{dlab}', loc='left', fontsize=11, color=INK, pad=3)
        txt = f'{len(runs)} markets · base {len(base)}\nrounds 51–100: {S.mean(r["w"] for r in runs):.2f}' if runs else 'no runs'
        ax.text(0.97, 0.95, txt, transform=ax.transAxes, color=mcol, fontsize=9, va='top', ha='right', linespacing=1.25,
                bbox=dict(boxstyle='square,pad=0.15', facecolor=SURF, edgecolor='none', alpha=0.85))
        if runs: print(f'CHECK 5Apanel {cell:10s} n {len(runs)} base n {len(base)} r51-100 {S.mean(r["w"] for r in runs):.3f}')
        if j // 2 == 2: ax.set_xlabel('round', color=MUTED)
        else: ax.tick_params(labelbottom=False)
        if j % 2 == 1: ax.tick_params(labelleft=False)
        if j == 2: ax.set_ylabel('market price (cost = 1), mean of the two sellers', color=MUTED, fontsize=9.5)
    fig.text(outer[0, b].get_position(fig).x0, 0.835, f'{mname}: same-day base {len(base)} markets (grey)', color=mcol, fontsize=13, ha='left', va='bottom')
fig.suptitle(f'The patrol at {len(DOSES)} doses: seller 0 forced below its own last price at rounds 20, 40, 60, 80, then freed', x=0.03, ha='left', fontsize=14, color=INK)
fig.text(0.03, 0.935, f'Thin coloured lines: {ns(len(D5[c]) for c in D5 if c.startswith("PA"))} markets per cell (each panel gives its count); thick line: their mean; grey: the same model\'s same-day base cell '
         f'(no patrol, {ns(len(D5[c]) for c in D5 if c.startswith("BASE23"))} markets per model).\nTwo sellers, P1 wording, 100 rounds, prices in units (cost = 1); one y axis for both models.\nDashed: cartel 1.925 (upper) and competitive 1.473 (lower). Vertical lines: the four cuts. 23 October 2026.',
         fontsize=9.5, color=MUTED, va='top')
p5a = f'{OUT}/fig-patrol-doses-both-2026-10-24.png'; fig.savefig(p5a, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p5a)

# ───────────── (5B) recovery after each cut, both models ─────────────
print('\n=== (5B) recovery after a visit — delta = market mean (t) − market mean (probe−1); every run of every cell, four visits per run ===')
XR = list(range(-3, 20)); TOL = 0.05
fig, axs = plt.subplots(1, 2, figsize=(16, 9), facecolor=SURF, sharey=True)
for ax, (mk, mname, mcol) in zip(axs, MODELS5):
    style(ax); ax.axhline(0, color=INK, lw=1); ax.axvline(0, color=MUTED, lw=0.8, alpha=0.5)
    ax.text(0.15, 0.015, 'the cut', transform=ax.get_xaxis_transform(), color=MUTED, fontsize=FS, ha='left', va='bottom')
    for dk, dlab, dcol in DOSES:
        runs = D5.get(f'{dk}-{mk}', [])
        if not runs: print(f'  {dk}-{mk}: no runs'); continue
        visits = []
        for r in runs:
            for p in PROBES:
                pre = S.mean(r['rows'][p - 1]); visits.append([S.mean(r['rows'][p + k]) - pre for k in XR])
        for v in visits: ax.plot(XR, v, color=dcol, alpha=0.12, lw=0.8)
        mv = [S.mean(v[i] for v in visits) for i in range(len(XR))]
        ax.plot(XR, mv, color=dcol, lw=2.4, label=f'−{dlab}: {len(visits)} cuts')
        at = {k: mv[XR.index(k)] for k in (1, 3, 5, 10, 19)}
        back = []; never = 0
        for v in visits:
            ks = [k for k in range(1, 20) if abs(v[XR.index(k)]) <= TOL]
            if ks: back.append(ks[0])
            else: never += 1
        print(f'CHECK 5B {dk:5s}-{mk} n_visits {len(visits)} runs {len(runs)} | mean delta +1 {at[1]:+.3f} +3 {at[3]:+.3f} +5 {at[5]:+.3f} +10 {at[10]:+.3f} +19 {at[19]:+.3f} | '
              f'median return {S.median(back) if back else None} over {len(back)}, never {never}/{len(visits)}')
    ax.set_xlim(-3, 19); ax.set_xticks([-3, 0, 1, 3, 5, 10, 15, 19]); ax.set_xlabel('rounds since the cut (0 = the forced round)', color=MUTED)
    ax.set_title(mname, loc='left', fontsize=13, color=mcol); ax.legend(frameon=False, fontsize=9.5, loc='lower right', title='dose of the forced cut', title_fontsize=9.5)
axs[1].tick_params(labelleft=True)
axs[0].set_ylabel('market price minus the price in the round before the cut', color=MUTED)
fig.suptitle('How fast does the price come back after a cut? Both models', x=0.04, ha='left', fontsize=14, color=INK)
fig.text(0.04, 0.925, 'Every cut of the patrol, aligned on the forced round: faint lines are single cuts, thick lines their mean per dose (counts in the legend); one y axis for both models.\n'
         'Zero is the market price in the round before the cut. 23 October 2026.', fontsize=9.5, color=MUTED, va='top')
fig.tight_layout(rect=(0, 0, 0.985, 0.9))
p5b = f'{OUT}/fig-patrol-recovery-both-2026-10-24.png'; fig.savefig(p5b, dpi=100, facecolor=SURF); plt.close(fig); print('wrote', p5b)
