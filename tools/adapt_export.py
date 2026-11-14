"""Build per-chapter homework question sets from the book's Try It bank for import into LibreTexts ADAPT (QTI 1.2, the
# NOTE: in the Try It bank the correct answer is ALWAYS c[0]; the "k" field is the calculator flag, not the answer key.
same format Canvas exports) plus a review spreadsheet. Text-only questions; items that need drawn structures are left out.
Usage: python3 tools/adapt_export.py  ->  adapt/CHEM3B_ChNN_<name>_QTI.zip, adapt/CHEM3B_ADAPT_question_list.csv"""
import json, re, os, zipfile, csv, html, uuid, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
OUT = os.path.join(ROOT, 'adapt'); os.makedirs(OUT, exist_ok=True)
import ast, types
# Read only the PLAN table from build_pages.py. Importing the module would run the whole page build
# (it rewrites pages/*.html from the stale drafts and needs node), which must never happen here.
_src = open(os.path.join(ROOT, 'tools', 'build_pages.py'), encoding='utf-8').read()
_plan = next(n for n in ast.parse(_src).body if isinstance(n, ast.Assign) and any(getattr(t, 'id', None) == 'PLAN' for t in n.targets))
B = types.SimpleNamespace(PLAN=eval(compile(ast.Expression(_plan.value), 'build_pages.PLAN', 'eval'), {'dict': dict}))

NAMES = {1: 'Bonding Review', 2: 'Alkanes and Cycloalkanes', 3: 'Alkenes, Alkynes and Aromatics', 4: 'Alcohols, Phenols, Ethers and Thiols',
         5: 'Aldehydes, Ketones and Chirality', 6: 'Carboxylic Acids and Esters', 7: 'Amines and Amides', 8: 'Carbohydrates', 9: 'Lipids',
         10: 'Amino Acids and Proteins', 11: 'Enzymes and Vitamins', 12: 'Nucleic Acids and Protein Synthesis', 13: 'Carbohydrate Metabolism',
         14: 'Metabolism and Energy Production', 15: 'Metabolism of Lipids and Proteins'}

bank = {}
for f in os.listdir(os.path.join(ROOT, 'bank')):
    if f.endswith('.json'):
        bank[f[:-5]] = json.load(open(os.path.join(ROOT, 'bank', f)))

def usable(x):
    return not any(k in x for k in ('s', 'f', 'cs')) and x.get('src') != 'canvas-quiz' and len(x.get('c', [])) >= 2

def plain(s):
    # Strip real tags only (a tag name must follow "<"), and do it BEFORE unescaping, so text such as
    # "propane &lt; dimethyl ether &lt; ethanol" is not mistaken for a tag (fb-3B-0225, fixed 2026-11-13).
    return html.unescape(re.sub(r'</?[A-Za-z][A-Za-z0-9]*(?:\s[^<>]*)?/?>', '', s))

used = set(); SETS = {}
# metabolism questions are split by their own keywords so Chapters 13-15 each get the right ones
MET = [(15, re.compile(r'β-oxid|beta.oxid|ketone bod|ketosis|ketoacid|lipogen|fatty acid|urea|transamin|deamin|ammoni|nitrogen balance|glucogenic|ketogenic|carnitine|lipase|triacylglycerol', re.I)),
       (14, re.compile(r'citric|krebs|electron transport|ATP synthase|oxidative phosph|coenzyme Q|cytochrome|chemiosm|proton gradient|oxaloacetate|succin|fumar|isocitr|ketoglut|FADH|kcal|calorie', re.I))]
def met_chapter(x):
    t = plain(x['q']) + ' ' + plain(' '.join(map(str, x['c'])))
    for ch, rx in MET:
        if rx.search(t): return ch
    return 13
for ch in range(1, 16):
    picked = []
    for w in B.PLAN[ch]['widgets']:
        p = w[1]
        if 't' not in p: continue
        rx = re.compile(p['q'], re.I) if p.get('q') else None
        for t in p['t'].split(','):
            for x in bank.get(t, []):
                if x['id'] in used or not usable(x): continue
                if t == 'metabolism':
                    if met_chapter(x) != ch: continue
                elif rx and not rx.search(plain(x['q']) + ' ' + plain(' '.join(map(str, x['c'])))): continue
                picked.append(x); used.add(x['id'])
    SETS[ch] = picked

# Items no widget regex catches (2026-11-12 fresh-eyes review): explicit chapter for each, so none is silently dropped.
# CHEM 3A drill items (strong acid/base, molar mass: 0233-0235, 0409, 0410, 0905, 0906) are left out on purpose.
EXPLICIT = {**{f'fb-3B-{n:04d}': 1 for n in (5, 6, 7, 8, 10, 405, 403, 407, 228, 229)},
            **{f'fb-3B-{n:04d}': 2 for n in (14, 17, 20, 351, 240, 241, 256, 2063, 2065, 2066)},
            **{f'fb-3B-{n:04d}': 3 for n in (21, 22, 23, 347, 242, 346, 25, 27, 32, 211, 396, 921, 2068)},
            'fb-3B-0255': 5, 'fb-3B-0254': 6, 'fb-3B-0221': 6, 'fb-3B-0232': 7,
            **{f'fb-3B-{n:04d}': 12 for n in (139, 287, 938)}}
LEFT_OUT = {f'fb-3B-{n:04d}' for n in (233, 234, 235, 409, 410, 905, 906)}
for t, items in bank.items():
    for x in items:
        if x['id'] in EXPLICIT and x['id'] not in used and usable(x):
            SETS[EXPLICIT[x['id']]].append(x); used.add(x['id'])
# Questions added on 2026-11-13 (fb-3B-2238 and later) carry "sec", the section that teaches them: file each one under
# that chapter, whatever the widget patterns matched.
for t, items in bank.items():
    for x in items:
        if int(x['id'].split('-')[2]) >= 2238 and x.get('sec') and usable(x):
            ch = int(x['sec'].split('.')[0])
            for c in SETS: SETS[c] = [y for y in SETS[c] if y['id'] != x['id']]
            SETS[ch].append(x); used.add(x['id'])
unmatched = [x['id'] for items in bank.values() for x in items if usable(x) and x['id'] not in used and x['id'] not in LEFT_OUT]
if unmatched: print('WARNING: usable bank items in no chapter set:', ', '.join(sorted(unmatched)))

def esc(s): return html.escape(s, quote=False)

def item_xml(x, n):
    ident = 'i' + uuid.uuid5(uuid.NAMESPACE_URL, x['id']).hex
    import random
    order = list(range(len(x['c']))); random.Random(x['id']).shuffle(order)   # deterministic shuffle so the key is not always A
    choices = [x['c'][j] for j in order]; key = order.index(0)
    resp = ''.join(f'<response_label ident="{ident}_{j}"><material><mattext texttype="text/html">{esc(str(c))}</mattext></material></response_label>' for j, c in enumerate(choices))
    fb = esc('Correct! ' + x.get('w', '')); hint = esc('Not quite. Hint: ' + (x.get('h') or 'Review the chapter and try again.'))
    return f'''<item ident="{ident}" title="{esc(x['id'])}">
<itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>question_type</fieldlabel><fieldentry>multiple_choice_question</fieldentry></qtimetadatafield><qtimetadatafield><fieldlabel>points_possible</fieldlabel><fieldentry>1.0</fieldentry></qtimetadatafield></qtimetadata></itemmetadata>
<presentation><material><mattext texttype="text/html">{esc(x['q'])}</mattext></material>
<response_lid ident="response1" rcardinality="Single"><render_choice>{resp}</render_choice></response_lid></presentation>
<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes>
<respcondition continue="No"><conditionvar><varequal respident="response1">{ident}_{key}</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing>
<itemfeedback ident="{ident}_{key}_fb"><flow_mat><material><mattext texttype="text/html">{fb}</mattext></material></flow_mat></itemfeedback>
<itemfeedback ident="general_incorrect_fb"><flow_mat><material><mattext texttype="text/html">{hint}</mattext></material></flow_mat></itemfeedback>
</item>'''

rows = []
for ch, items in SETS.items():
    title = f'CHEM 3B Chapter {ch}: {NAMES[ch]}'
    aid = 'a' + uuid.uuid5(uuid.NAMESPACE_URL, f'chem3b-ch{ch}').hex
    body = '\n'.join(item_xml(x, i) for i, x in enumerate(items, 1))
    qti = f'''<?xml version="1.0" encoding="UTF-8"?>
<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/ims_qtiasiv1p2 http://www.imsglobal.org/xsd/ims_qtiasiv1p2p1.xsd">
<assessment ident="{aid}" title="{esc(title)}"><qtimetadata><qtimetadatafield><fieldlabel>cc_maxattempts</fieldlabel><fieldentry>1</fieldentry></qtimetadatafield></qtimetadata>
<section ident="root_section">
{body}
</section></assessment></questestinterop>'''
    manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="m{aid}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:imsmd="http://www.imsglobal.org/xsd/imsmd_v1p2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/xsd/imscp_v1p1.xsd">
<metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata><organizations/>
<resources><resource identifier="{aid}" type="imsqti_xmlv1p2"><file href="{aid}/{aid}.xml"/><dependency identifierref="{aid}meta"/></resource><resource identifier="{aid}meta" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{aid}/assessment_meta.xml"><file href="{aid}/assessment_meta.xml"/></resource></resources></manifest>'''
    zn = os.path.join(OUT, f'CHEM3B_Ch{ch:02d}_{re.sub(r"[^A-Za-z]+", "_", NAMES[ch]).strip("_")}_QTI.zip')
    with zipfile.ZipFile(zn, 'w', zipfile.ZIP_DEFLATED) as z:
        meta = (f'<?xml version="1.0" encoding="UTF-8"?>\n<quiz identifier="{aid}" xmlns="http://canvas.instructure.com/xsd/cccv1p0"><title>{esc(title)}</title>'
                f'<description>Homework for Chapter {ch} of Introductory Organic and Biological Chemistry for FCC (LibreTexts). Questions by Daniel Kwasniewski, CC BY 4.0.</description>'
                f'<quiz_type>assignment</quiz_type><points_possible>{len(items)}</points_possible></quiz>')
        z.writestr('imsmanifest.xml', manifest); z.writestr(f'{aid}/{aid}.xml', qti); z.writestr(f'{aid}/assessment_meta.xml', meta)
    for x in items:
        rows.append([ch, NAMES[ch], x['id'], x['t'], x.get('d', ''), plain(x['q']), plain(str(x['c'][0])),
                     ' | '.join(plain(str(c)) for j, c in enumerate(x['c']) if j != 0), plain(x.get('w', ''))])
with open(os.path.join(OUT, 'CHEM3B_ADAPT_question_list.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f); w.writerow(['Chapter', 'Chapter title', 'Question ID', 'Topic', 'Difficulty', 'Question', 'Correct answer', 'Distractors', 'Feedback'])
    w.writerows(rows)
print({ch: len(v) for ch, v in SETS.items()}, 'total', sum(len(v) for v in SETS.values()))
