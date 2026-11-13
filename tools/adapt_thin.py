"""Extra ADAPT homework for the thin chapters (3 and 13, plus one Chapter 15 table question).
Adds (1) bank questions that need structures or figures, as PNG images with written alt text, and
(2) new text questions for Chapter 13 (also added to the Try It bank).
Usage: node tools/render_thin.js <ids.json> <imgdir>   then   python3 tools/adapt_thin.py <imgdir>
In the Try It bank the correct answer is ALWAYS c[0]."""
import json, os, sys, zipfile, html, random, re, glob
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'adapt', 'img_thin')  # render images first (see docstring)
OUT = os.path.join(ROOT, 'adapt')

# ---------- new Chapter 13 questions (written for this book; c[0] is correct) ----------
NEW13 = [
 {"id": "fb-3B-1001", "q": "In the first step of glycolysis, glucose + ATP &rarr; glucose 6-phosphate + ADP. Which enzyme class catalyzes this step?",
  "c": ["transferase (a kinase)", "hydrolase", "isomerase", "lyase"],
  "h": "A phosphate group is moved from ATP to glucose.", "w": "Moving a phosphate group from one molecule to another is a group transfer, so hexokinase is a <b>transferase</b> (a kinase)."},
 {"id": "fb-3B-1002", "q": "Where in the cell does glycolysis take place?",
  "c": ["cytosol", "mitochondrial matrix", "inner mitochondrial membrane", "nucleus"],
  "h": "Glycolysis does not need mitochondria at all.", "w": "Glycolysis runs in the <b>cytosol</b>. The citric acid cycle is in the mitochondrial matrix, and the electron transport chain is in the inner mitochondrial membrane."},
 {"id": "fb-3B-1003", "q": "Which step of glycolysis is an isomerization (atoms rearranged within one molecule)?",
  "c": ["glucose 6-phosphate &rarr; fructose 6-phosphate", "fructose 1,6-bisphosphate &rarr; two three-carbon sugars", "glyceraldehyde 3-phosphate &rarr; 1,3-bisphosphoglycerate", "phosphoenolpyruvate &rarr; pyruvate"],
  "h": "Look for a step where the formula stays the same and only the arrangement changes.", "w": "Glucose 6-phosphate (an aldose) is rearranged into fructose 6-phosphate (a ketose) with the same formula, so the enzyme is an <b>isomerase</b>. Splitting into two sugars is a lyase step, and the G3P step is an oxidation."},
 {"id": "fb-3B-1004", "q": "Which two steps of glycolysis use ATP?",
  "c": ["glucose &rarr; glucose 6-phosphate and fructose 6-phosphate &rarr; fructose 1,6-bisphosphate", "1,3-bisphosphoglycerate &rarr; 3-phosphoglycerate and phosphoenolpyruvate &rarr; pyruvate", "glucose &rarr; glucose 6-phosphate and phosphoenolpyruvate &rarr; pyruvate", "glyceraldehyde 3-phosphate &rarr; 1,3-bisphosphoglycerate and 3-phosphoglycerate &rarr; phosphoenolpyruvate"],
  "h": "ATP is invested early, in the six-carbon half of the pathway.", "w": "The two phosphorylations of the six-carbon sugar use ATP: <b>glucose &rarr; glucose 6-phosphate</b> and <b>fructose 6-phosphate &rarr; fructose 1,6-bisphosphate</b>. The two later steps listed in the second choice make ATP."},
 {"id": "fb-3B-1005", "q": "Salivary amylase begins the digestion of which carbohydrate in the mouth?",
  "c": ["starch", "cellulose", "lactose", "sucrose"],
  "h": "Amylase breaks &alpha;(1&rarr;4) glycosidic bonds in a plant polysaccharide.", "w": "Amylase hydrolyzes the &alpha;(1&rarr;4) bonds of <b>starch</b>. Humans have no enzyme for the &beta;(1&rarr;4) bonds of cellulose, and the disaccharides lactose and sucrose are broken down by lactase and sucrase in the small intestine."},
 {"id": "fb-3B-1006", "q": "When oxygen is low, muscle cells reduce pyruvate to lactate. What is the main purpose of this reaction?",
  "c": ["to regenerate NAD<sup>+</sup> so glycolysis can continue", "to make extra ATP from pyruvate", "to release CO<sub>2</sub>", "to convert pyruvate back into glucose"],
  "h": "Glycolysis needs a steady supply of an oxidized coenzyme.", "w": "Reducing pyruvate oxidizes NADH back to <b>NAD<sup>+</sup></b>, which the glyceraldehyde 3-phosphate step of glycolysis needs. The lactate step itself makes no ATP and releases no CO<sub>2</sub>."},
 {"id": "fb-3B-1007", "q": "What are the products of alcoholic fermentation of pyruvate in yeast?",
  "c": ["ethanol and CO<sub>2</sub>", "lactate only", "acetyl CoA and CO<sub>2</sub>", "ethanol and O<sub>2</sub>"],
  "h": "Bread rises and beer bubbles because of a gas.", "w": "Yeast decarboxylates pyruvate to acetaldehyde (releasing CO<sub>2</sub>) and then reduces it to <b>ethanol</b>, regenerating NAD<sup>+</sup>. Acetyl CoA is the aerobic route, and lactate is made by muscle and some bacteria."},
 {"id": "fb-3B-1008", "q": "Which hormone stimulates the liver to break glycogen down to glucose when blood glucose is low?",
  "c": ["glucagon", "insulin", "aldosterone", "oxytocin"],
  "h": "This hormone comes from the pancreas and works opposite to insulin.", "w": "<b>Glucagon</b> (and epinephrine) trigger glycogenolysis in the liver to raise blood glucose. Insulin does the opposite: it promotes glycogen synthesis."},
 {"id": "fb-3B-1009", "q": "Glycogen is highly branched. Which glycosidic bond forms its branch points?",
  "c": ["&alpha;(1&rarr;6)", "&alpha;(1&rarr;4)", "&beta;(1&rarr;4)", "&beta;(1&rarr;6)"],
  "h": "The straight chains use one link; the branches use carbon 6.", "w": "Glycogen chains are joined by &alpha;(1&rarr;4) bonds, and the branches attach through <b>&alpha;(1&rarr;6)</b> bonds, about every 8&ndash;12 glucose units."},
 {"id": "fb-3B-1010", "q": "In the Cori cycle, lactate made by working muscle travels in the blood to which organ, where it is converted back to glucose?",
  "c": ["liver", "brain", "kidney cortex only", "adipose tissue"],
  "h": "This organ is the main site of gluconeogenesis.", "w": "Lactate goes to the <b>liver</b>, which makes glucose from it by gluconeogenesis and sends the glucose back to the muscle."},
 {"id": "fb-3B-1011", "q": "What are the two main products of the pentose phosphate pathway?",
  "c": ["NADPH and ribose 5-phosphate", "NADH and ATP", "pyruvate and lactate", "acetyl CoA and FADH<sub>2</sub>"],
  "h": "One product is used for biosynthesis and protection against oxidation; the other is used to build nucleotides.", "w": "The pathway makes <b>NADPH</b> (for fatty acid synthesis and for keeping glutathione reduced) and <b>ribose 5-phosphate</b> (for nucleotides such as those in DNA, RNA and ATP)."},
 {"id": "fb-3B-1012", "q": "Gluconeogenesis makes new glucose from noncarbohydrate sources. Which of these can NOT be used as a starting material?",
  "c": ["fatty acids with an even number of carbons", "lactate", "glycerol", "alanine"],
  "h": "Think about whether the carbon atoms can end up in pyruvate or oxaloacetate.", "w": "Even-chain <b>fatty acids</b> break down to acetyl CoA, and humans cannot convert acetyl CoA into glucose. Lactate, glycerol (from triacylglycerols) and glucogenic amino acids such as alanine can all be used."},
]
for x in NEW13:
    x.update({"t": "metabolism", "d": 1, "k": 0, "src": "written-for-adapt"})

# ---------- bank questions that need images ----------
CH3 = ["fb-3B-0236", "fb-3B-0239", "fb-3B-0497", "fb-3B-0575", "fb-3B-0576", "fb-3B-0659", "fb-3B-0663", "fb-3B-0914", "fb-3B-0915", "fb-3B-0916",
       "fb-3B-0525", "fb-3B-0526", "fb-3B-0639", "fb-3B-0641", "fb-3B-0644", "fb-3B-0645", "fb-3B-0715", "fb-3B-0716", "fb-3B-0718", "fb-3B-0719",
       "fb-3B-0774", "fb-3B-0919", "fb-3B-0920"]
CH13 = ["fb-3B-0297", "fb-3B-0480", "fb-3B-0482", "fb-3B-0484", "fb-3B-0485", "fb-3B-0967", "fb-3B-0970", "fb-3B-0971"]
CH15 = ["fb-3B-0177"]

BENZ = "Benzene: a six-membered carbon ring drawn with three alternating double bonds."
GLY = ("Flow diagram of glycolysis. Glucose becomes glucose 6-phosphate (ATP used, ADP formed), then fructose 6-phosphate, then fructose 1,6-bisphosphate "
       "(ATP used, ADP formed), which splits into 2 glyceraldehyde 3-phosphate. These become 2 1,3-bisphosphoglycerate (2 NAD+ in, 2 NADH out), "
       "then 2 3-phosphoglycerate (2 ADP in, 2 ATP out), then 2 phosphoenolpyruvate (2 H2O released), then 2 pyruvate (2 ADP in, 2 ATP out).")
ALT = {
 "fb-3B-0497_s": "A six-membered carbon ring with one C=C double bond and a methyl group on the ring carbon across the ring from the double bond.",
 "fb-3B-0497_cs": "Four choices. A: a six-membered ring with only single bonds and one methyl group. B: a benzene ring (three alternating double bonds) with one methyl group. C: a six-membered ring with only single bonds, a methyl group and an OH group on opposite ring carbons. D: an unbranched chain of six carbons with only single bonds.",
 "fb-3B-0575_s": "Zigzag skeletal structure of a five-carbon chain with a C=C double bond between carbons 2 and 3; the chain continues on opposite sides of the double bond.",
 "fb-3B-0576_s": "Skeletal structure of a six-carbon chain with a C=C double bond between carbons 3 and 4; the two ethyl ends are on the same side of the double bond.",
 "fb-3B-0659_s": "A cyclohexane ring with a chlorine atom and an ethyl group both attached to the same ring carbon.",
 "fb-3B-0659_cs": "Four choices. A: a cyclohexene ring with an ethyl group on one of the two double-bond carbons. B: a cyclohexene ring with an ethyl group on a ring carbon that is not part of the double bond. C: a cyclohexane ring with a vinyl group (CH=CH2) attached. D: a cyclohexene ring with an ethyl group on a different ring carbon that is not part of the double bond.",
 "fb-3B-0663_s": "Reaction: trans-2-pentene (a five-carbon chain with a C=C between carbons 2 and 3) reacting with Cl2, shown above the reaction arrow.",
 "fb-3B-0663_cs": "Four choices, each a five-carbon chain with single bonds only. A: Cl on carbons 2 and 3. B: one Cl on carbon 2. C: two Cl atoms on carbon 3. D: Cl on carbons 1 and 2.",
 "fb-3B-0914_s": "Reaction: cyclohexane (a six-membered ring of single bonds) with an arrow labeled 'Pt, heat' and '−H2' below the arrow.",
 "fb-3B-0914_cs": "Four choices. A: a six-membered ring with one C=C double bond. B: a benzene ring with three alternating double bonds. C: an unbranched six-carbon chain with a double bond at one end. D: a six-membered ring of single bonds with an OH group.",
 "fb-3B-0915_s": "Reaction: a central carbon bonded to a Br atom and three methyl groups, with an arrow labeled 'KOH, heat' and '−HBr' below the arrow.",
 "fb-3B-0915_cs": "Four choices. A: a three-carbon chain with a C=C double bond at one end and a methyl group on the central double-bond carbon (four carbons total). B: an unbranched four-carbon chain with a double bond at one end. C: a central carbon bonded to an OH group and three methyl groups. D: a central CH carbon bonded to three methyl groups, single bonds only.",
 "fb-3B-0916_s": "Reaction: a four-carbon chain with Br atoms on carbons 2 and 3, with an arrow labeled 'Zn' and '−Br2' below the arrow.",
 "fb-3B-0916_cs": "Four choices, each four carbons. A: a C=C double bond between carbons 2 and 3. B: a C=C double bond between carbons 1 and 2. C: a double bond at one end and a Br atom on carbon 3. D: a C=O (ketone) group on carbon 2.",
 "fb-3B-0525_s": BENZ,
 "fb-3B-0525_cs": "Four choices. A: a benzene ring bonded to a nitro group (NO2). B: a benzene ring bonded to an amino group (NH2). C: a cyclohexane ring (no double bonds) bonded to a nitro group. D: a benzene ring bonded to an OH group.",
 "fb-3B-0526_s": BENZ,
 "fb-3B-0526_cs": "Four choices. A: a benzene ring with one Br atom. B: a six-membered ring with only two double bonds and Br atoms on two adjacent ring carbons that have single bonds (an addition product, no longer aromatic). C: a benzene ring with Br atoms on two adjacent carbons. D: a cyclohexane ring (no double bonds) with one Br atom.",
 "fb-3B-0639_s": "A benzene ring with two Cl atoms on adjacent ring carbons.",
 "fb-3B-0641_s": "A benzene ring with two OH groups on ring carbons directly across the ring from each other.",
 "fb-3B-0644_s": "Three difluorobenzene isomers. I: F atoms on ring carbons 1 and 3. II: F atoms directly across the ring, on carbons 1 and 4. III: F atoms on adjacent ring carbons 1 and 2.",
 "fb-3B-0645_s": "A benzene ring with two Cl atoms on ring carbons directly across the ring from each other.",
 "fb-3B-0715_s": "Reaction: a benzene ring with two methyl groups across the ring from each other, with Br2 and FeBr3 above the reaction arrow.",
 "fb-3B-0715_cs": "Four choices. A: the benzene ring with its two methyl groups across from each other and one Br on a ring carbon next to a methyl group. B: a non-aromatic six-membered ring with two methyl groups and Br atoms on two adjacent single-bonded ring carbons. C: a benzene ring with a methyl group and a CH2Br group across from each other (Br on the side chain). D: the benzene ring with two methyl groups and two Br atoms.",
 "fb-3B-0716_s": "Reaction: a benzene ring with methyl groups on alternating ring carbons (three methyl groups), with HNO3 and H2SO4 above the reaction arrow.",
 "fb-3B-0716_cs": "Four choices. A: the trimethylbenzene ring with one nitro group (NO2) on a ring carbon between two methyl groups. B: a benzene ring with two methyl groups and a CH2NO2 side chain (nitro group on a side-chain carbon). C: the trimethylbenzene ring with an amino group (NH2) on the ring. D: the trimethylbenzene ring with two nitro groups.",
 "fb-3B-0718_s": "Reaction: a benzene ring with two Cl atoms across the ring from each other, with HNO3 and H2SO4 above the reaction arrow.",
 "fb-3B-0718_cs": "Four choices. A: the benzene ring with Cl atoms across from each other and a nitro group (NO2) on the carbon next to one Cl. B: a benzene ring with one Cl and one nitro group across from each other (a Cl has been replaced). C: the dichlorobenzene ring with an amino group (NH2) on the ring. D: a non-aromatic ring with two Cl atoms, an OH group and a nitro group on single-bonded ring carbons.",
 "fb-3B-0719_s": "Reaction: a benzene ring with four methyl groups, leaving two ring hydrogens across from each other, with Cl2 and FeCl3 above the reaction arrow.",
 "fb-3B-0719_cs": "Four choices. A: the tetramethylbenzene ring with one Cl on one of the two open ring carbons. B: a non-aromatic ring with four methyl groups and two Cl atoms on single-bonded ring carbons. C: a benzene ring with three methyl groups and a CH2Cl side chain (Cl on a side chain). D: the tetramethylbenzene ring with Cl on both open ring carbons.",
 "fb-3B-0774_s": BENZ + " This is one resonance form.",
 "fb-3B-0919_cs": "Four choices. A: a benzene ring bonded to an isopropyl group (a CH carbon attached to two methyl groups). B: a benzene ring bonded to a straight three-carbon propyl chain. C: a benzene ring with a methyl group and an ethyl group on adjacent ring carbons. D: a benzene ring bonded to a tert-butyl group (a carbon attached to three methyl groups).",
 "fb-3B-0920_cs": "Four choices. A: a benzene ring with two methyl groups separated by one ring carbon (1,3 positions). B: a benzene ring with two methyl groups on adjacent carbons (1,2 positions). C: a benzene ring with two methyl groups across from each other (1,4 positions). D: a benzene ring with one ethyl group.",
 "fb-3B-0480_f": GLY, "fb-3B-0482_f": GLY,
 "fb-3B-0484_f": "Flow diagram of pyruvate oxidation: pyruvate becomes acetyl CoA, with NAD+ and CoA going in and NADH and CO2 coming out. Acetyl CoA then enters the citric acid cycle.",
 "fb-3B-0485_f": "Flow diagram from glucose to acetyl CoA. Glycolysis: glucose becomes 2 pyruvate, with 2 NAD+ in and 2 NADH and 2 ATP (net) out. Pyruvate oxidation: 2 pyruvate become 2 acetyl CoA, with 2 NAD+ in and 2 NADH and 2 CO2 out. A table below gives 2.5 ATP per NADH.",
 "fb-3B-0967_s": "Reaction: acetaldehyde (CH3CHO, two carbons with a C=O at the end) is converted to the acetate ion (CH3COO−).",
 "fb-3B-0970_s": "Reaction: pyruvate (CH3–CO–COO−, a ketone next to a carboxylate) is converted to lactate (CH3–CH(OH)–COO−); the arrow is labeled 'NADH → NAD+'.",
 "fb-3B-0971_s": "Reaction: pyruvate (CH3–CO–COO−) is converted to acetaldehyde (CH3CHO); the arrow is labeled '− CO2'.",
}

def cs_perm(x):
    """order of the drawn answer structures in the A-D grid (shuffled so the right one is not always A)"""
    P = list(range(len(x['cs']))); random.Random(x['id'] + 'cs').shuffle(P); return P

def esc(s): return html.escape(s, quote=False)

def fig_html(f):
    out = []
    for fig in f:
        if fig.get('type') == 'eq':
            out.append(f'<p style="text-align:center">{fig["text"]}</p>')
        elif fig.get('type') == 'table':
            head = ''.join(f'<th scope="col">{h}</th>' for h in fig['head'])
            rows = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in fig['rows'])
            out.append(f'<table border="1" cellpadding="4"><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table>')
    return ''.join(out)

def item(x, meta, files):
    ident = 'i' + re.sub(r'[^A-Za-z0-9]', '', x['id'])
    prompt = f"<p>{x['q']}</p>"
    m = meta.get(x['id'], {})
    for key in ('s', 'f', 'cs'):
        fn = m.get(key)
        if fn:
            alt = ALT[f"{x['id']}_{key}"]
            files.append((f'images/{fn}', os.path.join(IMG, fn)))
            prompt += f'<p><img src="$IMS-CC-FILEBASE$/images/{fn}" alt="{html.escape(alt)}" style="max-width:100%"></p>'
    if 'f' in x and not m.get('f'):
        prompt += fig_html(x['f'])
    labels = [c for c in x['c']]
    if x.get('cs'):
        P = cs_perm(x)   # grid cell k shows choice P[k], so choice j is drawn as letter P.index(j)
        labels = [f'Structure {"ABCDEF"[P.index(j)]}' + ('' if str(c).startswith('§') else f': {c}') for j, c in enumerate(x['c'])]
    order = list(range(len(labels))); random.Random(x['id']).shuffle(order)
    key = order.index(0)
    resp = ''.join(f'<response_label ident="{ident}_{j}"><material><mattext texttype="text/html">{esc(labels[o])}</mattext></material></response_label>' for j, o in enumerate(order))
    fb = esc('Correct! ' + x.get('w', '')); hint = esc('Not quite. Hint: ' + (x.get('h') or 'Review the chapter and try again.'))
    return (f'<item ident="{ident}" title="{x["id"]}"><itemmetadata><qtimetadata><qtimetadatafield><fieldlabel>question_type</fieldlabel><fieldentry>multiple_choice_question</fieldentry></qtimetadatafield>'
            f'<qtimetadatafield><fieldlabel>points_possible</fieldlabel><fieldentry>1.0</fieldentry></qtimetadatafield></qtimetadata></itemmetadata>'
            f'<presentation><material><mattext texttype="text/html">{esc(prompt)}</mattext></material><response_lid ident="response1" rcardinality="Single"><render_choice>{resp}</render_choice></response_lid></presentation>'
            f'<resprocessing><outcomes><decvar maxvalue="100" minvalue="0" varname="SCORE" vartype="Decimal"/></outcomes><respcondition continue="No"><conditionvar><varequal respident="response1">{ident}_{key}</varequal></conditionvar><setvar action="Set" varname="SCORE">100</setvar></respcondition></resprocessing>'
            f'<itemfeedback ident="{ident}_{key}_fb"><flow_mat><material><mattext texttype="text/html">{fb}</mattext></material></flow_mat></itemfeedback>'
            f'<itemfeedback ident="general_incorrect_fb"><flow_mat><material><mattext texttype="text/html">{hint}</mattext></material></flow_mat></itemfeedback></item>')

def build(name, title, items, meta):
    aid = 'x' + re.sub(r'[^a-z0-9]', '', name.lower())
    files = []
    body = '\n'.join(item(x, meta, files) for x in items)
    qti = f'<?xml version="1.0" encoding="UTF-8"?>\n<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"><assessment ident="{aid}" title="{esc(title)}"><section ident="root_section">{body}</section></assessment></questestinterop>'
    meta_xml = f'<?xml version="1.0" encoding="UTF-8"?>\n<quiz identifier="{aid}" xmlns="http://canvas.instructure.com/xsd/cccv1p0"><title>{esc(title)}</title><description>Additional CHEM 3B homework questions. Questions by Daniel Kwasniewski, CC BY 4.0.</description><quiz_type>assignment</quiz_type></quiz>'
    man = (f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="m{aid}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"><metadata><schema>IMS Content</schema><schemaversion>1.1.3</schemaversion></metadata><organizations/>'
           f'<resources><resource identifier="{aid}" type="imsqti_xmlv1p2"><file href="{aid}/{aid}.xml"/><dependency identifierref="{aid}meta"/></resource>'
           f'<resource identifier="{aid}meta" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{aid}/assessment_meta.xml"><file href="{aid}/assessment_meta.xml"/></resource></resources></manifest>')
    zn = os.path.join(OUT, f'{name}.zip')
    with zipfile.ZipFile(zn, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('imsmanifest.xml', man); z.writestr(f'{aid}/{aid}.xml', qti); z.writestr(f'{aid}/assessment_meta.xml', meta_xml)
        for arc, path in dict(files).items():
            z.write(path, arc)
    return zn, len(items), len(set(files))

if __name__ == '__main__':
    bank = {x['id']: x for f in glob.glob(os.path.join(ROOT, 'bank', '*.json')) for x in json.load(open(f))}
    for x in NEW13: bank[x['id']] = x
    meta = json.load(open(os.path.join(IMG, 'meta.json')))
    missing = [f"{i}_{k}" for i, m in meta.items() for k in ('s', 'f', 'cs') if m.get(k) and f"{i}_{k}" not in ALT]
    assert not missing, missing
    print(build('CHEM3B_Ch03_extra_QTI', 'CHEM 3B Chapter 3 extra questions', [bank[i] for i in CH3], meta))
    print(build('CHEM3B_Ch13_extra_QTI', 'CHEM 3B Chapter 13 extra questions', [bank[i] for i in CH13] + NEW13, meta))
    print(build('CHEM3B_Ch15_extra_QTI', 'CHEM 3B Chapter 15 extra questions', [bank[i] for i in CH15], meta))
