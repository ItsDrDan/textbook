exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
from rdkit import Chem
import math, sys
ROT = float(sys.argv[1]) if len(sys.argv) > 1 else 0
PW = 330; els = []
specs = [('CC(=O)Oc1ccccc1C(=O)O', BLUE, ['stomach (strong acid):', '–COOH keeps its H'], ['neutral: crosses membranes']),
         ('CC(=O)Oc1ccccc1C(=O)[O-]', RED, ['blood (pH 7.4):', '–COO^− (lost its H)'], ['charged: stays in water'])]
mols = []
for smi, col, top, bot in specs:
    m = Mol(smi, rotate=ROT); mols.append(m)
    print(Chem.rdMolDescriptors.CalcMolFormula(m.m), Chem.GetFormalCharge(m.m))
    acid = [10, 11, 12]
    xs = [m.p[a][0] for a in acid]; ys = [m.p[a][1] for a in acid]
    x0, x1, y0, y1 = min(xs) - 16, max(xs) + 22, min(ys) - 16, max(ys) + 16
    m.els.insert(0, f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1-x0:.1f}" height="{y1-y0:.1f}" rx="12" fill="{col}" fill-opacity="0.08" stroke="{col}" stroke-width="2" stroke-dasharray="6 4"/>')
    m.box = [min(m.box[0], x0), min(m.box[1], y0), max(m.box[2], x1), max(m.box[3], y1)]
H = max(m.box[3] - m.box[1] for m in mols)
TOP = 52
for k, ((smi, col, top, bot), m) in enumerate(zip(specs, mols)):
    ox = k * PW; cx = ox + PW / 2
    b = m.box; dx = cx - (b[0] + b[2]) / 2; dy = TOP + H / 2 - (b[1] + b[3]) / 2
    els += m.shifted(dx, dy)
    els.append(label(cx, 18, top[0], 16, col, weight=800))
    els.append(ct(cx, 40, top[1], 16, col, anchor='middle', weight=700))
    els.append(label(cx, TOP + H + 24, bot[0], 15, INK, weight=600))
els.append(line(PW, 4, PW, TOP + H + 30, 1.2, GREY, '5 5'))
alt = 'Aspirin in two places in the body. Left panel, labeled stomach (strong acid): –COOH keeps its H. Skeletal aspirin, a benzene ring carrying an acetate ester group, O–C(=O)–CH3, and next to it a carboxylic acid group, C(=O)OH, which is boxed in blue; note under it: neutral, crosses membranes. Right panel, labeled blood (pH 7.4): –COO minus, lost its H. The same structure with the acid group drawn as the carboxylate ion, C(=O)O minus, boxed in red; note under it: charged, stays in water.'
save(wrap(els, 0, 0, 2 * PW, TOP + H + 36, alt, 1), 'fig-p597118-aspirin-stomach-blood.svg', 7)
