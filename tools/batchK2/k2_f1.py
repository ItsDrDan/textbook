exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
els = []; RS = 66; G = 22
ROWS = [-RS, 0, RS]
def backbone(x, tails, colors):
    """glycerol-type stack: rows CH2 / CH / CH2, each followed by a drawn bond and a tail cmol"""
    xs = x + cw('CH2') + 16; xe = 0; cxs = x + cw('C') / 2
    for k, (y, g) in enumerate(zip(ROWS, ['CH2', 'CH', 'CH2'])):
        els.append(ct(x, y, g))
        els.append(line(x + cw(g) + 2, y - 7, xs - 2, y - 7, 1.6))
        e, x1, cx = tails(xs, y); els.extend(e); xe = max(xe, x1)
    for y in ROWS[:2]:
        els.append(line(cxs, y + 7, cxs, y + RS - 20, 1.6))
    return xe
def ester(xs, y):
    return cmol(xs, y, ['O', 'C', '(CH2)16CH3'], branches={1: ('O', None)}, dbl={1}, colors={0: RED, (1, 'a'): RED})
def alc(xs, y):
    return cmol(xs, y, ['OH'], colors={0: RED})
NY = RS + 38
x = 0
x1 = backbone(x, ester, None); els.append(label((x + x1) / 2, NY, 'tristearin (a triacylglycerol)', 15)); x = x1 + G
els.append(ct(x, 0, '+', 22)); x += 14 + G
e, x1, _ = cmol(x, 0, ['3 NaOH']); els += e; x = x1 + G
A = 80; els += arrow(x, -7, A, 'heat'); x += A + G
x1 = backbone(x, alc, None); els.append(label((x + x1) / 2, NY, 'glycerol', 15)); x = x1 + G
els.append(ct(x, 0, '+', 22)); x += 14 + G
e, x1, _ = cmol(x, 0, ['3 CH3(CH2)16COO^−', 'Na^+'], bonds=[' ']); els += e
els.append(label((x + x1) / 2, NY, 'sodium stearate (soap)', 15))
W = x1
alt = ('Saponification of a fat. Tristearin, a triacylglycerol, is drawn as a glycerol backbone of three stacked carbons, CH2, CH and CH2, '
       'each bonded through an oxygen to an ester carbonyl group, C double-bond O, that carries a (CH2)16CH3 chain. Tristearin plus 3 NaOH, '
       'heated, gives glycerol, CH2OH–CHOH–CH2OH, plus 3 sodium stearate, CH3(CH2)16COO minus Na plus, which is soap.')
save(wrap(els, -10, -RS - 52, W + 20, 2 * RS + 52 + 38 + 14, alt), 'fig-p597116-saponification-tristearin.svg', 1)
