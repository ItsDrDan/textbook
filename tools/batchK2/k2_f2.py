exec(open('/private/tmp/claude-501/-Users-dan--claude-spares-spare-pFNKGe/6d7de96c-bd21-4c02-8348-92b6983ada5b/scratchpad/k2_common.py').read())
els = []; NY = 46; G = 20
def name(x0, x1, t, k=0): els.append(label((x0 + x1) / 2, NY + 19 * k, t, 15))
x = 0
e, x1, _ = cmol(x, 0, ['CH3', 'C', 'OH'], branches={1: ('O', None)}, dbl={1}, colors={2: RED, (1, 'a'): RED}); els += e; name(x, x1, 'acetic acid'); x = x1 + G
els.append(ct(x, 0, '+', 22)); x += 14 + G
e, x1, _ = cmol(x, 0, ['NH3'], colors={0: BLUE}); els += e; name(x, x1, 'ammonia'); x = x1 + G
A1 = 150; els += arrow(x, -7, A1, 'mix (acid–base)', 'room temperature'); x += A1 + G
x0 = x
e, x1, _ = cmol(x, 0, ['CH3', 'C', 'O^−'], branches={1: ('O', None)}, dbl={1}, colors={2: RED, (1, 'a'): RED}); els += e; x = x1 + 10
e, x1, _ = cmol(x, 0, ['NH4^+'], colors={0: BLUE}); els += e; name(x0, x1, 'ammonium acetate'); name(x0, x1, '(a salt)', 1); x = x1 + G
A2 = 130; els += arrow(x, -7, A2, 'heat (–H' + SUB2 + ')'); x += A2 + G
x0 = x
e, x1, _ = cmol(x, 0, ['CH3', 'C', 'NH2'], branches={1: ('O', None)}, dbl={1}, colors={2: BLUE, (1, 'a'): RED}); els += e; name(x, x1, 'acetamide'); x = x1 + G
els.append(ct(x, 0, '+', 22)); x += 14 + G
e, x1, _ = cmol(x, 0, ['H2O'], colors={0: RED}); els += e; name(x, x1, 'water')
W = x1
alt = ('Amide formation in two steps. Acetic acid, CH3–C(=O)–OH, plus ammonia, NH3, mixed at room temperature undergo an acid–base reaction '
       'to give the salt ammonium acetate, CH3–C(=O)–O minus with NH4 plus. Heating the salt drives off water: the arrow labeled heat, minus H2O, '
       'leads to acetamide, CH3–C(=O)–NH2, plus H2O.')
save(wrap(els, -10, -58, W + 20, NY + 19 + 14 + 58, alt), 'fig-p597126-amide-two-step.svg', 2)
