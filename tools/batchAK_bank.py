"""Batch AK (2026-11-15), bank part: the six carbonyl-reduction questions say [H] instead of H2 + Ni/metal catalyst.
Exact-phrase replacements, applied to every copy of the 3B bank (textbook bank, Final Boss, Bond Voyage exam mode,
shared questionbank). fb-3B-0498 (sorbic acid + excess H2/Ni) and fb-3B-0702 (H2, Ni as a hydrogenation distractor)
are true hydrogenation items and stay. Run from the folder holding the repos:  python3 textbook/tools/batchAK_bank.py"""
import json, sys
R = [
 # fb-3B-0056
 ('is reduced with H<sub>2</sub> and a nickel catalyst?', 'is reduced with [H] (a reducing agent)?'),
 ('Adding H<sub>2</sub> across the C=O gives CH<sub>3</sub>CH(OH)', 'Adding H atoms across the C=O gives CH<sub>3</sub>CH(OH)'),
 ('Butanal is an aldehyde isomer, not a reduction product. Adding H<sub>2</sub> converts the C=O into C–OH.', 'Butanal is an aldehyde isomer, not a reduction product. Reduction ([H]) converts the C=O into C–OH.'),
 ('and a ketone cannot form it. H<sub>2</sub> is a reducing agent.', 'and a ketone cannot form it. [H] is a reducing agent.'),
 # fb-3B-0246
 ('by H<sub>2</sub> and a Ni catalyst?', 'by [H] (a reducing agent)?'),
 ('nor reduced by H<sub>2</sub>.', 'nor reduced by [H].'),
 # fb-3B-0513
 ('is reduced with H<sub>2</sub> and a nickel catalyst. What is the product?', 'is reduced with [H] (a reducing agent). What is the product?'),
 ('the oxygen is gone. H<sub>2</sub> adds across the C=O; it does not remove the oxygen.', 'the oxygen is gone. [H] adds H atoms across the C=O; it does not remove the oxygen.'),
 ('an oxidation product. H<sub>2</sub> is a reducing agent, and a ketone cannot give an acid.', 'an oxidation product. [H] is a reducing agent, and a ketone cannot give an acid.'),
 # fb-3B-0926
 ('are each reduced with H<sub>2</sub> and a Ni catalyst.', 'are each reduced with [H] (a reducing agent).'),
 ('Reduction adds H<sub>2</sub> across the C=O, so the –OH ends up', 'Reduction adds two H atoms across the C=O, so the –OH ends up'),
 ('H<sub>2</sub> with a Ni catalyst reduces both aldehydes and ketones.', '[H] reduces both aldehydes and ketones.'),
 # fb-3B-2287
 ('Sorbitol comes from reducing glucose with H<sub>2</sub> and a metal catalyst.', 'Sorbitol comes from reducing glucose with [H].'),
 # fb-3B-2289
 ('by reaction with H<sub>2</sub> and a metal catalyst. What change takes place?', 'by reaction with [H] (a reducing agent). What change takes place?'),
 ('Is H<sub>2</sub> with a metal catalyst an oxidation or a reduction?', 'Is [H] an oxidation or a reduction?'),
 ('H<sub>2</sub> with a metal catalyst is a reduction. It turns the aldehyde C=O', '[H] stands for a reducing agent. It turns the aldehyde C=O'),
 ("such as Benedict's reagent, not H<sub>2</sub>.", "such as Benedict's reagent, not [H]."),
 ('Adding H<sub>2</sub> never makes a –COOH group.', 'Adding H atoms never makes a –COOH group.'),
]
FILES = [*sys.argv[1:]] or ['textbook/bank/carbonyls.json', 'textbook/bank/carbs.json', 'finalexam/index.html', 'organicreactions/index.html', 'questionbank/bank/final-exam-3b.json']
def variants(s):  # as written in a file: raw, JSON-escaped (–, \"), apostrophe escaped
    v = {s, json.dumps(s)[1:-1], s.replace("'", "\\'"), json.dumps(s, ensure_ascii=True)[1:-1], s.replace('–', '&ndash;'), json.dumps(s, ensure_ascii=False)[1:-1].replace('<', '\\u003c')}
    return [x for x in v if x]
tot = {}
for f in FILES:
    t = open(f, encoding='utf-8').read(); n0 = t
    for a, b in R:
        for va in variants(a):
            if va in t:
                vb = va.replace(a, b) if va == a else variants(b)[[*variants(a)].index(va)] if False else None
                # map the same escaping onto the new text
                for enc in (lambda x: x, lambda x: json.dumps(x)[1:-1], lambda x: x.replace("'", "\\'"), lambda x: json.dumps(x, ensure_ascii=True)[1:-1], lambda x: x.replace('–', '&ndash;'), lambda x: json.dumps(x, ensure_ascii=False)[1:-1].replace('<', '\\u003c')):
                    if enc(a) == va: vb = enc(b); break
                c = t.count(va); t = t.replace(va, vb); tot[(f, a[:40])] = tot.get((f, a[:40]), 0) + c
    if t != n0: open(f, 'w', encoding='utf-8').write(t)
from collections import Counter
per = Counter(); [per.update({k[0]: v}) for k, v in tot.items()]
print(dict(per))
for a, _ in R:
    hit = [f.split('/')[0] for f in FILES if tot.get((f, a[:40]))]
    print(len(hit), a[:60])
