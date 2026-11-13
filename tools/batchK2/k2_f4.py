exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
els = []; NY = 70
e, x, cx = cmol(0, 0, ['CH2', 'CH', 'CH3'], bonds=['=', '–']); els += e
els.append(label(cx[0], -26, '2 H', 13, BLUE, weight=700)); els.append(label(cx[1], -26, '1 H', 13, BLUE, weight=700))
els.append(label(x / 2, NY, 'propene', 15)); x1 = x
x += 22; els.append(ct(x, 0, '+', 22)); x += 36
e, x2, _ = cmol(x, 0, ['H', 'Cl'], colors={0: RED, 1: RED}); els += e
els.append(label((x + x2) / 2, NY, 'hydrogen chloride', 15)); x = x2 + 26
els += arrow(x, -7, 80); x += 80 + 26
e, x3, cx = cmol(x, 0, ['CH2', 'CH', 'CH3'], branches={0: (None, 'H'), 1: (None, 'Cl')}, colors={(0, 'b'): RED, (1, 'b'): RED}); els += e
els.append(label((x + x3) / 2, NY, '2-chloropropane (major)', 15))
els.append(ct((x + x3) / 2, NY + 21, 'minor product: 1-chloropropane, CH3CH2CH2Cl', 14, GREY, anchor='middle'))
half = max(cw('minor product: 1-chloropropane, CH3CH2CH2Cl', 14), 15*0.6*23) / 2
W = max(x3, (x + x3) / 2 + half + 4)
alt = ('Markovnikov addition of HCl to propene. Propene, CH2=CH–CH3, in which the end CH2 carbon of the double bond has 2 H and the middle CH carbon has 1 H, '
       'plus hydrogen chloride, H–Cl, gives 2-chloropropane as the major product: the H (red) adds to the CH2 carbon, which already had more hydrogens, making it CH3, '
       'and the Cl (red) adds to the middle carbon, giving CH3–CHCl–CH3. A note says the minor product is 1-chloropropane, CH3CH2CH2Cl.')
save(wrap(els, -12, -48, W + 24, NY + 34 + 48, alt), 'fig-p597081-propene-hcl.svg', 4)
print(len(alt))
