"""Sticky Molecules (IMF game) -> CHEM 3B Try It bank / ADAPT: candidate list (DRAFT, nothing published).

Reads the game's export in ItsDrDan/questionbank (bank/IMF-practice.json, 680 items, CC BY 4.0,
Daniel Kwasniewski), keeps the 217 items tagged for 3B, and decides for each one:
  keep    -> converted to the Try It bank format (t, q, c, h, w, k, d, x) with the book section it serves
  reword  -> kept, but the stem leans on a lab picture or uses an untaught term; fix before import
  drop    -> reason recorded (2-choice, typed number, lab-only, not taught at GOB level, duplicate)
Output: tools/imf_deck_candidates_2026-11-13.json  {summary, items:[...]}
IDs are provisional (fb-3B-2126 upward, after the last bank id fb-3B-2125); confirm before import.
Run from the textbook repo root:  python3 tools/imf_deck_candidates_build.py [path/to/IMF-practice.json]
"""
import json, re, sys, collections

SRC = sys.argv[1] if len(sys.argv) > 1 else '../github/questionbank/bank/IMF-practice.json'
items = [x for x in json.load(open(SRC, encoding='utf-8')) if '3B' in x['courses']]


def tidy(s):
    return re.sub(r'\s+([.,;:])', r'\1', s or '').strip()


# organic family -> bank file (t) and section, for "strongest force" items
FAMILY = {'alkane': ('hydrocarbons', '2.6'), 'alkene': ('hydrocarbons', '3.3'), 'alcohol': ('alcohols', '4.3'),
          'ether': ('alcohols', '4.8'), 'aldehyde': ('carbonyls', '5.2'), 'ketone': ('carbonyls', '5.2'),
          'carboxylic acid': ('acids_esters', '6.3'), 'amine': ('amines', '7.2'), 'amide': ('amines', '7.5')}

# explicit decisions (everything else falls to the rules below)
DROP = {
    'IMF-f8d11929': 'colloids (milk) are not taught in the book',
    'IMF-9685ef5b': 'Tyndall effect is not taught in the book',
    'IMF-35e29cab': 'solution/colloid/suspension is not taught in the book',
    'IMF-00655f1b': '3 choices incl. "Both equally"; IMF-af7b9432 asks the same idea better',
    'IMF-3366854a': 'needs the H-Bond Lab box on screen',
    'IMF-f8e0fff5': 'needs the H-Bond Lab box on screen',
    'IMF-e5649ad1': 'plant-cell turgor is not taught (9.5 is about red blood cells)',
    'IMF-c55317aa': 'plasmolysis is not taught (9.5 is about red blood cells)',
    'IMF-c1bad740': 'plant-cell turgor is not taught',
    'IMF-184f77df': 'duplicate of IMF-5a8e4aa1 (Val/Ala, order swapped)',
    'IMF-65201690': '"the two cysteines" refers to the Fold Lab chain; IMF-25a73aea covers it',
    'IMF-a84092a4': '"this chain" refers to the Fold Lab chain; the sidechain items cover salt bridges',
    'IMF-e5b5cbb8': '"this short protein chain" refers to the Fold Lab chain; IMF-e4202203 covers it',
}
REWORD = {
    'IMF-ed71f91a': 'distractor "Ion–dipole forces" names a force the book does not teach (CONVENTIONS: IMF = dispersion, dipole–dipole, H bonding); swap for "Ionic bonds"',
    'IMF-07403e27': 'stem says "The folded protein" (the lab chain); reword to "A folded protein is heated gently. Which interactions let go?"',
    'IMF-dc0fd8e8': 'stem says "This protein" (the lab chain); reword to "A small protein unfolds when gently heated…"',
    'IMF-0d14ac35': 'answer singles out salt bridges; 10.10 says pH changes disrupt salt bridges and hydrogen bonds. OK as "most directly", but check wording against 10.10',
}
# tonicity: 36 generated variants of 3 steps x 6 baths x 2 cells; keep one per idea (red blood cell only)
TONICITY_KEEP = {'IMF-b2954f76': 'pure water -> hemolysis', 'IMF-5cf56fb1': '0.45% NaCl -> swells',
                 'IMF-05bf0d50': '5% glucose is isotonic', 'IMF-3df7d559': '3% NaCl -> crenation',
                 'IMF-f1b78d23': '10% glucose is hypertonic', 'IMF-02036531': 'seawater -> water out'}
DNA_KEEP = {'IMF-545ca339', 'IMF-31937730', 'IMF-1f22c80b', 'IMF-62bf5c89', 'IMF-e88a88e7'}

SKILL_HOME = {  # skill -> (t, section)
    'IMF.concept': ('properties', '1.8'), 'IMF.hbond': ('properties', '1.8'), 'IMF.simhb': ('properties', '1.8'),
    'IMF.carbs': ('carbs', '8.7'), 'IMF.colloid': ('lipids', '9.5'), 'IMF.fats': ('lipids', '9.1'),
    'IMF.osmosis': ('lipids', '9.5'), 'IMF.simcell': ('lipids', '9.5'), 'IMF.tonicity': ('lipids', '9.5'),
    'IMF.sidechain': ('proteins', '10.8'), 'IMF.folding': ('proteins', '10.8'), 'IMF.simfold': ('proteins', '10.10'),
    'IMF.dna': ('nucleic', '12.2'), 'IMF.orgbp': ('properties', '1.8'),
}
MIXING_HOME = {'IMF-ef5d66cf': ('lipids', '9.2'), 'IMF-e414f186': ('alcohols', '4.3'), 'IMF-e1f992c9': ('alcohols', '4.3'),
               'IMF-82c8da68': ('carbs', '8.5'), 'IMF-197d54d0': ('alcohols', '4.8')}
FOLD_SEC = {'IMF-3d8b104d': '10.8', 'IMF-f8fd26eb': '10.7', 'IMF-03224324': '10.7', 'IMF-5c30a51f': '10.10',
            'IMF-0d14ac35': '10.10', 'IMF-25a73aea': '10.10'}


def decide(x):
    i, sk, n = x['id'], x['skill'], len(x.get('choices') or [])
    if i in DROP: return 'drop', DROP[i], None, None
    if x['type'] != 'mc': return 'drop', 'typed-number item; the Try It bank and ADAPT decks are multiple choice', None, None
    if sk == 'IMF.tonicity':
        return ('keep', TONICITY_KEEP[i], 'lipids', '9.5') if i in TONICITY_KEEP else ('drop', 'one of 36 generated tonicity variants; 6 kept', None, None)
    if sk == 'IMF.dna':
        return ('keep', '', 'nucleic', '12.2') if i in DNA_KEEP else ('drop', '2-choice or repeat of the "strands warmed" item', None, None)
    if sk in ('IMF.mixing', 'IMF.simmix'):
        if i in MIXING_HOME: return ('keep', '',) + MIXING_HOME[i]
        return 'drop', 'yes/no mixing item (2 choices, 50% guess); stays in the game and its Mixing Beaker', None, None
    if sk == 'IMF.organic':
        if n < 3: return 'drop', 'yes/no "O–H or N–H?" step (2 choices)', None, None
        txt = re.sub(r'<[^>]+>', ' ', x['prompt'])
        fam = next((f for f in FAMILY if re.search(r'\b' + f + r'\b', txt)), None)
        t, sec = FAMILY.get(fam, ('properties', '1.8'))
        return 'keep', f'family: {fam}', t, sec
    if sk in ('IMF.orgbp', 'IMF.fats'):
        if n < 3: return 'drop', '"which is higher" step (2 choices); its "why" step is kept', None, None
    t, sec = SKILL_HOME.get(sk, ('properties', '1.8'))
    if sk in ('IMF.folding', 'IMF.simfold'): sec = FOLD_SEC.get(i, sec)
    if i in REWORD: return 'reword', REWORD[i], t, sec
    return 'keep', '', t, sec


out, nid = [], 2126
for x in sorted(items, key=lambda x: (x['skill'], x['id'])):
    act, why, t, sec = decide(x)
    row = {'imf_id': x['id'], 'skill': x['skill'], 'action': act, 'note': why}
    if act != 'drop':
        ch = x['choices']; k = ch.index(x['answer'])
        xs = [tidy(w) or None for w in (x.get('why') or [''] * len(ch))]; xs[k] = None
        row.update({'section': sec, 'bank': {
            't': t, 'q': x['prompt'], 'c': ch, 'h': tidy(x.get('hint')),
            'w': tidy(x.get('explain')) or tidy((x.get('why') or [''])[k]), 'k': k,
            'd': 1 if x['skill'] in ('IMF.concept', 'IMF.hbond', 'IMF.osmosis') else 2,
            'id': f'fb-3B-{nid}', 'x': xs, 'src': 'imf-game', 'from': x['id']}})
        nid += 1
    out.append(row)

c = collections.Counter(r['action'] for r in out)
by_t = collections.Counter(r['bank']['t'] for r in out if 'bank' in r)
by_sec = collections.Counter(r['section'] for r in out if 'bank' in r)
summary = {'source': SRC, 'licence': 'CC BY 4.0, Daniel Kwasniewski (questionbank export)', 'items_3B': len(items),
           'actions': dict(c), 'by_bank_file': dict(by_t), 'by_section': dict(sorted(by_sec.items(), key=lambda kv: [int(p) for p in kv[0].split('.')])),
           'prompts_with_svg': sum('<svg' in r['bank']['q'] for r in out if 'bank' in r)}
json.dump({'summary': summary, 'items': out}, open('tools/imf_deck_candidates_2026-11-13.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(summary, indent=1))
