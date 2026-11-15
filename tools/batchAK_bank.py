"""Batch AK (2026-11-15), bank part: the seven carbonyl-reduction questions say [H] instead of H2 + Ni/metal catalyst.
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
 # fb-3B-0683 (found in the ADAPT scan)
 ('when it is treated with H<sub>2</sub> and a Ni catalyst (the benzene ring does not react)?', 'when it is treated with [H] (a reducing agent)? The benzene ring does not react.'),
 ('Styrene has no oxygen, so H<sub>2</sub> just gives ethylbenzene.', 'Styrene has no oxygen, so reducing it cannot create an –OH.'),
 ('This drawing is styrene, which has no oxygen. H<sub>2</sub> would add across its C=C and could not create an –OH.', 'This drawing is styrene, which has no oxygen. Reducing it could not create an –OH.'),
 # fb-3B-0366, 0367, 0512 (found in the second scan)
 ('Catalytic hydrogenation (H<sub>2</sub>, Ni) of pentanal,', 'Reduction ([H]) of pentanal,'),
 ('Reduction is the reverse of oxidation: H<sub>2</sub> adds across the C=O on the same carbon.', 'Reduction is the reverse of oxidation: [H] adds H atoms across the C=O on the same carbon.'),
 ('The carboxylic acid is an oxidation product. H<sub>2</sub> with Ni is a reduction.', 'The carboxylic acid is an oxidation product. [H] is a reduction.'),
 ('An alkene has no oxygen. H<sub>2</sub> adds across the C=O; it does not remove the oxygen.', 'An alkene has no oxygen. [H] adds H atoms across the C=O; it does not remove the oxygen.'),
 ('takes up H<sub>2</sub> over platinum, which product and alcohol class result?', 'is reduced with [H] (a reducing agent), which product and alcohol class result?'),
 ('and a ketone cannot form one. Adding H<sub>2</sub> is reduction.', 'and a ketone cannot form one. Adding [H] is reduction.'),
 ('is reduced with H<sub>2</sub> and a catalyst under conditions that do not affect the benzene ring.', 'is reduced with [H] (a reducing agent); the benzene ring is not affected.'),
 ('Reduction adds H<sub>2</sub> across the C=O. What kind of alcohol does an aldehyde give?', 'Reduction adds H atoms across the C=O. What kind of alcohol does an aldehyde give?'),
 ('H<sub>2</sub> adds across C=O, turning the aldehyde CHO into CH<sub>2</sub>OH:', '[H] adds H atoms across the C=O, turning the aldehyde CHO into CH<sub>2</sub>OH:'),
 ('This drawing is benzoic acid, the oxidation product. H<sub>2</sub> is a reducing agent.', 'This drawing is benzoic acid, the oxidation product. [H] is a reducing agent.'),
 ('This drawing is toluene: the oxygen is gone completely. H<sub>2</sub> adds across the C=O; it does not remove the oxygen.', 'This drawing is toluene: the oxygen is gone completely. [H] adds H atoms across the C=O; it does not remove the oxygen.'),
 # fb-3B-0245, 0681, 0682, 0692 (third scan; these phrases occur only in reduction items)
 ('Adding H<sub>2</sub> across the C=O of 2-pentanone', 'Adding H atoms across the C=O of 2-pentanone'),
 ('H<sub>2</sub> adds to the C=O at C2', 'H atoms add to the C=O at C2'),
 ('H<sub>2</sub> adds one H to the C and one H to the O of the C=O.', '[H] adds one H to the C and one H to the O of the C=O.'),
 ('H<sub>2</sub> adds across the C=O', '[H] adds H atoms across the C=O'),
 ('H<sub>2</sub> is a reducing agent.', '[H] is a reducing agent.'),
 ('is the reduction product (H<sub>2</sub>), the opposite reaction.', 'is the reduction product ([H]), the opposite reaction.'),  # fb-3B-0684
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
