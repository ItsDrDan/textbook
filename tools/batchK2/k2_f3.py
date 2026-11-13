exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
from rdkit import Chem
import math, sys
def starred(smi, rot=0, flip=False, dist=17):
    m = Mol(smi, rotate=rot, flip=flip)
    cc = [i for i, _ in Chem.FindMolChiralCenters(m.m, includeUnassigned=True, useLegacyImplementation=False)]
    ri = m.m.GetRingInfo().AtomRings()
    for i in cc:
        x, y = m.p[i]
        angs = sorted(math.atan2(m.p[n.GetIdx()][1] - y, m.p[n.GetIdx()][0] - x) for n in m.m.GetAtomWithIdx(i).GetNeighbors())
        ring = [r for r in ri if i in r][0]
        rcx = sum(m.p[k][0] for k in ring) / len(ring); rcy = sum(m.p[k][1] for k in ring) / len(ring)
        best = None
        for k in range(len(angs)):
            a1 = angs[k]; a2 = angs[(k + 1) % len(angs)] + (2 * math.pi if k == len(angs) - 1 else 0)
            gap = a2 - a1; mid = (a1 + a2) / 2
            ux, uy = math.cos(mid), math.sin(mid)
            inward = ux * (rcx - x) + uy * (rcy - y) > 0
            score = gap - (10 if inward else 0)
            if best is None or score > best[0]: best = (score, ux, uy)
        _, ux, uy = best
        m.els.append(text(x + ux * dist, y + uy * dist + 9, '*', RED, 26, 800, fmt=False))
    print(smi, 'chiral atoms', cc, 'formula', Chem.rdMolDescriptors.CalcMolFormula(m.m))
    return m, cc
RC = float(sys.argv[1]) if len(sys.argv) > 1 else 0
mm, c1 = starred('CC(C)C1CCC(C)CC1O')
mc, c2 = starred('CC1=CCC(CC1=O)C(C)=C', rot=RC)
els = []; x = 0; G = 60
H = max(m.box[3] - m.box[1] for m in (mm, mc))
for m, nm, sub in ((mm, 'menthol', '3 chiral carbons'), (mc, 'carvone', '1 chiral carbon')):
    b = m.box; dx = x - b[0]; dy = -(b[1] + b[3]) / 2
    els += m.shifted(dx, dy)
    cxm = x + (b[2] - b[0]) / 2
    els.append(label(cxm, H / 2 + 22, nm, 16, weight=700)); els.append(label(cxm, H / 2 + 42, sub + ' (*)', 14, weight=500))
    x += b[2] - b[0] + G
W = x - G
alt = 'Skeletal structures of menthol and carvone with their chiral carbons marked by red asterisks. Left, menthol: a cyclohexane ring carrying an OH group, an isopropyl group on the neighboring ring carbon, and a methyl group on the ring carbon two positions away from the OH carbon on the other side; the three ring carbons that hold the OH, the isopropyl group and the methyl group are starred, so menthol has 3 chiral carbons. Right, carvone: a six-membered ring containing a ketone C=O and a C=C double bond, with a methyl group on the double-bond carbon next to the C=O and an isopropenyl group, C(CH3)=CH2, on the ring; only the ring carbon holding the isopropenyl group is starred, so carvone has 1 chiral carbon.'
save(wrap(els, -10, -H / 2 - 8, W + 20, H + 58, alt, 0.85), 'fig-p597106-menthol-carvone.svg', 3)
