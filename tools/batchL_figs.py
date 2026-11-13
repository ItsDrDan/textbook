"""Batch L figures (PDF check 2026-11-12 23:50), house style of tools/batchF_figs.py. Run from repo root.
14.3.1 citric acid cycle as a landscape loop (the square wheel printed at ~2 pt)."""
import sys, os
sys.path.insert(0, 'tools')
from batchF_figs import T, svg, INK, MUTED, RED, BLUE, GREEN, PURPLE, _fc_box, _fc_arrow, _fc_pill

OUT = 'figures/pages/batchL/'
os.makedirs(OUT, exist_ok=True)
SUP = lambda s: f'<tspan baseline-shift="super" font-size="10">{s}</tspan>'
SB = lambda s: f'<tspan baseline-shift="sub" font-size="10">{s}</tspan>'
NADH = f'NAD{SUP("+")} &#8594; NADH'
CO2 = f'CO{SB("2")} out'


def cac_flow():
    W, H = 1220, 480
    b = []
    def en(x, y, s, anchor='middle'): return T(x, y, s, 13.5, 700, MUTED, anchor, 'font-style="italic"')
    blue = dict(fill='#e3ecfb', stroke='#7d9bd6', col=BLUE)
    grey = dict(fill='#eef1f5', stroke='#a9b4c2', col='#4f5a74')
    y1, y2 = 140, 392
    top = [(150, 300, ['Citrate', '(6 C)']), (420, 580, ['Isocitrate', '(6 C)']), (720, 900, ['&#945;-Ketoglutarate', '(5 C)']), (1040, 1200, ['Succinyl CoA', '(4 C)'])]
    bot = [(1040, 1200, ['Succinate', '(4 C)']), (740, 880, ['Fumarate', '(4 C)']), (440, 580, ['Malate', '(4 C)']), (150, 300, ['Oxaloacetate', '(4 C)'])]
    for x0, x1, ln in top + bot: b.append(_fc_box(x0, x1, y1 if (x0, x1, ln) in top else y2, ln, size=16, h=62))
    b.append(T(20, 32, 'One turn of the citric acid cycle (in the mitochondrial matrix)', 16, 900, PURPLE))
    # top row steps 2-4
    tl = [('2 aconitase', '', []), ('3 isocitrate', 'dehydrogenase', [NADH, CO2]), ('4 &#945;-ketoglutarate', 'dehydrogenase', [NADH, CO2])]
    for i, (l1, l2, pills) in enumerate(tl):
        xa, xb = top[i][1] + 6, top[i + 1][0] - 6; xc = (xa + xb) / 2
        b.append(_fc_arrow(xa, y1, xb, y1))
        b.append(en(xc, y1 - (28 if l2 else 12), l1))
        if l2: b.append(en(xc, y1 - 12, l2))
        for k, p in enumerate(pills): b.append(_fc_pill(xc, y1 + 34 + 30 * k, p, w=128, **(blue if 'NAD' in p else grey)))
    # step 4 also takes in CoA
    # right side: step 5
    b.append(_fc_arrow(1120, y1 + 33, 1120, y2 - 33))
    b.append(en(1106, 236, '5 succinyl CoA', 'end')); b.append(en(1106, 252, 'synthetase', 'end'))
    b.append(_fc_pill(1022, 286, f'GDP + P{SB("i")} &#8594; GTP', w=168))
    # bottom row steps 6-8 (right to left)
    bl = [('6 succinate', 'dehydrogenase', [f'FAD &#8594; FADH{SB("2")}']), ('7 fumarase', '', [f'+ H{SB("2")}O']), ('8 malate', 'dehydrogenase', [NADH])]
    for i, (l1, l2, pills) in enumerate(bl):
        xa, xb = bot[i][0] - 6, bot[i + 1][1] + 6; xc = (xa + xb) / 2
        b.append(_fc_arrow(xa, y2, xb, y2))
        b.append(en(xc, y2 - (44 if l2 else 28), l1))
        if l2: b.append(en(xc, y2 - 28, l2))
        for p in pills: b.append(_fc_pill(xc, y2 + 50, p, w=142, **(blue if ('NAD' in p or 'FAD' in p) else grey)))
    # left side: step 1, acetyl CoA joins oxaloacetate
    b.append(_fc_arrow(225, y2 - 33, 225, y1 + 33))
    b.append(_fc_box(14, 124, 266, ['Acetyl CoA', '(2 C)'], fill='#fff6e2', stroke='#e2c77a', col='#80601a', size=15, h=58))
    b.append(_fc_arrow(126, 266, 219, 266))
    b.append(en(238, 236, '1 citrate synthase', 'start'))
    b.append(_fc_pill(320, 272, f'+ H{SB("2")}O, CoA&#8211;SH out', w=170, **grey))
    # net box
    b.append(f'<rect x="470" y="232" width="330" height="96" rx="12" fill="#efeaf8" stroke="{PURPLE}" stroke-width="2"/>')
    b.append(T(635, 260, 'Per acetyl CoA (one turn):', 15, 900, PURPLE, 'middle'))
    b.append(T(635, 286, f'2 CO{SB("2")} + 3 NADH', 16, 900, PURPLE, 'middle'))
    b.append(T(635, 312, f'+ 1 FADH{SB("2")} + 1 GTP', 16, 900, PURPLE, 'middle'))
    alt = ('The citric acid cycle as a loop. Step 1, citrate synthase: acetyl CoA (2 carbons) and water join oxaloacetate (4 carbons) to make citrate (6 carbons), releasing CoA-SH. '
           'Step 2, aconitase: citrate is rearranged to isocitrate. Step 3, isocitrate dehydrogenase: NAD+ is reduced to NADH and CO2 leaves, giving alpha-ketoglutarate (5 carbons). '
           'Step 4, alpha-ketoglutarate dehydrogenase: NAD+ is reduced to NADH and CO2 leaves, giving succinyl CoA (4 carbons). Step 5, succinyl CoA synthetase: GDP and phosphate make GTP, giving succinate. '
           'Step 6, succinate dehydrogenase: FAD is reduced to FADH2, giving fumarate. Step 7, fumarase: water adds, giving malate. Step 8, malate dehydrogenase: NAD+ is reduced to NADH, '
           'regenerating oxaloacetate. Per turn: 2 CO2, 3 NADH, 1 FADH2 and 1 GTP.')
    open(OUT + 'fig-p597202-cac-flow.svg', 'w').write(svg(W, H, alt, ''.join(b)))


cac_flow()
print('cac ok')
