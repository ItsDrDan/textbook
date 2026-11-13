exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
from rdkit import Chem
import math, sys
ROT = float(sys.argv[1]) if len(sys.argv) > 1 else 0
m = Mol('BrC1C(CC)CCC1', rotate=ROT)
print(Chem.rdMolDescriptors.CalcMolFormula(m.m))
ring = [1, 2, 5, 6, 7]  # C1..C5
rcx = sum(m.p[k][0] for k in ring) / 5; rcy = sum(m.p[k][1] for k in ring) / 5
for n, k in enumerate(ring, 1):
    x, y = m.p[k]
    angs = sorted(math.atan2(m.p[q.GetIdx()][1] - y, m.p[q.GetIdx()][0] - x) for q in m.m.GetAtomWithIdx(k).GetNeighbors())
    best = None
    for j in range(len(angs)):
        a1 = angs[j]; a2 = angs[(j + 1) % len(angs)] + (2 * math.pi if j == len(angs) - 1 else 0)
        mid = (a1 + a2) / 2; ux, uy = math.cos(mid), math.sin(mid)
        inward = ux * (rcx - x) + uy * (rcy - y) > 0
        sc = (a2 - a1) - (10 if inward else 0)
        if best is None or sc > best[0]: best = (sc, ux, uy)
    _, ux, uy = best
    m.els.append(text(x + ux * 16, y + uy * 16 + 5.5, str(n), BLUE, 15, 800, halo=False, fmt=False))
m.box = [m.box[0] - 6, m.box[1] - 4, m.box[2] + 8, m.box[3] + 8]
els = []
b = m.box; dx = -b[0]; dy = -(b[1] + b[3]) / 2; els += m.shifted(dx, dy)
W = b[2] - b[0]; H = b[3] - b[1]
cx = W / 2
els.append(label(cx, H / 2 + 22, '1-bromo-2-ethylcyclopentane', 16, weight=700))
els.append(label(cx, H / 2 + 42, 'bromo gets C1 (b comes before e)', 14, weight=500))
half = 125
x0 = min(-10, cx - half); x1 = max(W + 10, cx + half)
save(wrap(els, x0, -H / 2 - 8, x1 - x0, H + 58, 'Skeletal structure of 1-bromo-2-ethylcyclopentane: a five-membered ring with a bromine on one carbon and an ethyl group on the neighboring carbon. Blue numbers label the ring carbons: 1 at the carbon bearing Br, 2 at the carbon bearing the ethyl group, then 3, 4 and 5 continuing around the ring. Text under the drawing: 1-bromo-2-ethylcyclopentane; bromo gets C1 because b comes before e.', 0.85), 'fig-p597073-ring-numbering.svg', 5)
