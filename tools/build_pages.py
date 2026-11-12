#!/usr/bin/env python3
"""Build the LibreTexts page HTML for the CHEM 3B book from the Chapter Guide drafts:
   - figure placeholders -> GitHub Pages URLs
   - game-drawn reaction schemes (inline SVG) after the relevant Key Ideas section
   - "Try It" practice widgets (iframes to practice.html) at key skills and before the Practice section
   - a "Practice Games" page per chapter
Writes pages/*.html and pages/manifest.json (used by tools/sync-libretexts.js)."""
import sys, json, re, os, html, urllib.parse as up

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DRAFTS = '/mnt/user-data/outputs/CHEM3B_LibreTexts_Drafts'
BASE = 'https://itsdrdan.github.io/textbook/'
SCH = json.load(open(os.path.join(ROOT, 'tools/schemes.json')))

GUIDE_IDS = {1:597062,2:597074,3:597086,4:597100,5:597107,6:597119,7:597132,8:597141,9:597150,10:597164,11:597173,12:597184,13:597198,14:597205,15:597218}
CHAPTER_IDS = {1:597039,2:597040,3:597041,4:597042,5:597043,6:597044,7:597045,8:597046,9:597047,10:597048,11:597049,12:597050,13:597051,14:597052,15:597053}
GUIDE_FILES = {int(f[2:4]): f for f in os.listdir(DRAFTS) if 'Chapter_Guide' in f}
TITLES = {1:'Bonding Review - Lewis Structures and Intermolecular Forces',2:'Alkanes and Cycloalkanes',3:'Alkenes, Alkynes, and Aromatic Compounds',4:'Alcohols, Phenols, Ethers, and Thiols',5:'Aldehydes and Ketones',6:'Carboxylic Acids and Esters',7:'Amines and Amides',8:'Carbohydrates',9:'Lipids',10:'Amino Acids and Proteins',11:'Enzymes and Vitamins',12:'Nucleic Acids and Protein Synthesis',13:'Carbohydrate Metabolism',14:'Metabolism and Energy Production',15:'Metabolism of Lipids and Proteins'}

GAMES = {
 'orgrxn':   ('Bond Voyage! Organic Reactions', 'https://itsdrdan.github.io/organicreactions/', 'Identify reaction types, draw products and reactants, and name what you drew.'),
 'origins':  ('Organic Origins', 'https://itsdrdan.github.io/functionalgroups/', 'Spot functional groups, classify 1°/2°/3° carbons, name and draw compounds, predict products.'),
 'flash':    ('Functional Group Flashcards', 'https://itsdrdan.github.io/organic/', 'Flip through the 16 functional groups with a real example and where you meet each one in health care.'),
 'carbs':    ('Sweet Structures', 'https://itsdrdan.github.io/carbohydrates/', 'Classify sugars, read Fischer projections and Haworth rings, and work sugar reactions.'),
 'peptides': ('Peptide Party', 'https://itsdrdan.github.io/aminoacids/', 'Amino acids and R groups, condense and hydrolyze peptides, decode codons, protein structure.'),
 'finalboss':('Final Boss', 'https://itsdrdan.github.io/finalexam/?course=3B', 'Final-exam style multiple choice for every CHEM 3B topic. Pick Topic Training and choose this chapter\'s topic.'),
 'lewis':    ('Lewis Structure Studio', 'https://itsdrdan.github.io/lewisstructures/?course=3B', 'Draw Lewis structures, predict VSEPR shapes and polarity.'),
 'hub':      ('CHEM 3B Daily 5', 'https://itsdrdan.github.io/games/3b.html', 'Five quick questions a day from all the CHEM 3B games (Organic and Biochemistry panels).'),
 'lipidlab': ('Lipid Lab', 'https://itsdrdan.github.io/lipids/', 'Read fatty-acid chains (saturation, shorthand, omega, melting point), build and break triacylglycerols, classify lipids, and work membrane and clinical questions.'),
 'enzyme':   ('Enzyme Engine', 'https://itsdrdan.github.io/enzymes/', 'Classify enzymes, spot the inhibitor from active-site pictures, read activity graphs, and match vitamins to coenzymes.'),
 'helix':    ('Helix Hustle', 'https://itsdrdan.github.io/nucleicacids/', 'DNA and RNA structure, base pairing, replication, transcription and translation.'),
 'metab':    ('Metabolic Marathon', 'https://itsdrdan.github.io/metabolism/', 'Order the pathways, count NADH, FADH\u2082 and ATP, name the reaction type, follow fuel through fed and fasting states, and match enzymes to vitamins.'),
}

def widget(params, title, blurb, height=620, game=None):
    q = dict(params); q['title'] = title
    if game: q['game'] = game
    url = BASE + 'practice.html?' + up.urlencode(q, safe=',|')
    return (f'<div class="box-note" style="border-left:6px solid #86509b;">\n<p class="boxtitle">Try It: {html.escape(title)}</p>\n'
            f'<p>{blurb} Your progress is saved in this browser.</p>\n'
            f'<p><iframe src="{html.escape(url)}" width="100%" height="{height}" style="border:0;border-radius:12px;background:#f5f6fb;" title="Try It: {html.escape(title)}" loading="lazy"></iframe></p>\n'
            f'<p style="font-size:0.9em;">Not loading? <a href="{html.escape(url)}" target="_blank" rel="noopener">Open this practice in a new tab</a>.</p>\n</div>\n')

def scheme_fig(ids, num, caption):
    parts = []
    for i in ids:
        s = SCH[i]
        parts.append(f'<div style="margin:6px 0;">{s["svg"]}<p style="font-size:0.9em;margin:2px 0 8px;text-align:center;"><strong>{html.escape(s["type"])}</strong> ({html.escape(s["cls"].lower())}): {html.escape(s["rule"])}</p></div>')
    return (f'<figure class="figure" style="margin:12px 0;">{"".join(parts)}<figcaption>Figure {num}: {caption} (Structures drawn by the Bond Voyage! reaction engine.)</figcaption></figure>\n')

def games_box(ch):
    return (f'<div class="box-note" style="border-left:6px solid #86509b;">\n<p class="boxtitle">Keep Practicing</p>\n'
            f'<p>Every question above is one of many. For unlimited practice on this chapter, open <strong>Practice Games</strong>, the last page of Chapter {ch}' + (' (and <strong>Practice Game - Lewis Structures</strong>, the page before it)' if ch == 1 else '') + ', or go straight to '
            f'<a href="https://itsdrdan.github.io/games/3b.html" target="_blank" rel="noopener">the CHEM 3B game hub</a>.</p>\n</div>\n')

# ---- per-chapter plan ---------------------------------------------------------------
# schemes: (h3 regex, [scheme ids], caption)   widgets: (h3 regex or 'PRACTICE', params, title, blurb, height, game)
PLAN = {
 1: dict(schemes=[], widgets=[
     ('PRACTICE', {'t':'structure','q':'bond|shape|angle|polar|lewis|tetrahedral|trigonal|octet','n':'10'}, 'Bonding and shape', 'Ten exam-style questions on bonds, Lewis structures, VSEPR shapes and polarity.', 620, 'lewis'),
     ('PRACTICE', {'t':'properties','q':'hydrogen bond|dispersion|dipole|boiling|solub|polar','n':'10'}, 'Intermolecular forces', 'Which force is strongest? Which compound boils higher or dissolves in water? Reason it out.', 620, 'finalboss')],
    games=['lewis','finalboss'],
    gametips={'lewis':'Draw the molecules from Chapter 1, then check shape and polarity.','finalboss':'Topic Training → “Structure & Functional Groups” and “IMFs, Polarity & Acid–Base”.'}),
 2: dict(schemes=[(r'reaction types', ['ch2_combustion','ch2_substitution'], 'The two alkane reactions you must recognize: combustion and halogenation (a substitution).')],
    widgets=[(r'reaction types', {'rxn':'combustion,substitution','mode':'mix'}, 'Alkane reactions', 'Identify the reaction, pick the product, or name it. A new reaction every time.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'hydrocarbons,isomers','q':'alkane|cycloalk|conform|combust|halogenation|substitution|saturated|isomer|branch|IUPAC','n':'12'}, 'Alkanes and isomers', 'Naming, formulas, isomers and properties of alkanes.', 620, 'origins')],
    games=['origins','flash','orgrxn'],
    gametips={'origins':'Start with Spot the Group, then 1°/2°/3° and Name It (alkanes and cycloalkanes). Draw It checks your condensed and skeletal drawings.','flash':'Study mode: flip the alkane, alkene, alkyne and haloalkane cards.','orgrxn':'Identify the Reaction: watch for combustion and halogenation (substitution).'}),
 3: dict(schemes=[(r'Addition reactions', ['ch3_hydrogenation','ch3_halogenAdd','ch3_hydrohalogenation','ch3_hydration'], 'The four addition reactions of alkenes. In the last two, Markovnikov\'s rule puts the H on the carbon that already has more H atoms.')],
    widgets=[(r'Addition reactions', {'rxn':'hydrogenation,halogenAdd,hydrohalogenation,hydration','mode':'product'}, 'Addition to alkenes', 'Pick the product of each addition reaction. Watch the Markovnikov cases.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'hydrocarbons,aromatic','q':'alkene|alkyne|addition|markov|hydrogenat|hydration|double bond|triple bond|cis|trans|aromatic|benzene','n':'12'}, 'Alkenes, alkynes and aromatics', 'Naming, cis/trans, addition reactions and benzene.', 620, 'finalboss')],
    games=['orgrxn','origins','finalboss'],
    gametips={'orgrxn':'Draw the Product with the hydrocarbon set: hydrogenation, halogenation, hydrohalogenation and hydration.','origins':'Name It and Draw It for alkenes and alkynes.','finalboss':'Topic Training → “Alkanes, Alkenes & Alkynes” and “Aromatic Compounds”.'}),
 4: dict(schemes=[(r'^4\. Reactions', ['ch4_dehydration','ch4_ox1','ch4_ox1acid','ch4_ox2'], 'Alcohol reactions: dehydration (elimination) and oxidation. A 1° alcohol oxidizes to an aldehyde, then to a carboxylic acid; a 2° alcohol oxidizes to a ketone; a 3° alcohol does not oxidize.')],
    widgets=[(r'^4\. Reactions', {'rxn':'dehydration,ox1Ald,ox1Acid,ox2','mode':'mix'}, 'Alcohol reactions', 'Dehydration and oxidation of 1° and 2° alcohols: identify, predict and name.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'alcohols','n':'12'}, 'Alcohols, phenols, ethers and thiols', 'Classification, naming, properties and reactions.', 620, 'origins')],
    games=['orgrxn','origins','finalboss'],
    gametips={'orgrxn':'Choose the alcohol set: dehydration, oxidation and reduction.','origins':'Properties mode (boiling point, solubility) and Predict the Product for alcohols.','finalboss':'Topic Training → “Alcohols, Phenols, Thiols & Ethers”.'}),
 5: dict(schemes=[(r'^3\. Reactions', ['ch5_oxAld','ch5_reduction','ch5_hemiacetal'], 'Carbonyl reactions: aldehydes oxidize to acids, aldehydes and ketones are reduced to alcohols, and an alcohol adds to a carbonyl to make a hemiacetal (the first step of sugar ring formation).')],
    widgets=[(r'^3\. Reactions', {'rxn':'oxAldAcid,reduction,hemiacetal,acetal','mode':'mix'}, 'Aldehyde and ketone reactions', 'Oxidation, reduction, hemiacetals and acetals.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'carbonyls,chirality','n':'12'}, 'Carbonyls and chirality', 'Naming aldehydes and ketones, their reactions, and spotting chiral carbons.', 620, 'finalboss')],
    games=['orgrxn','origins','finalboss'],
    gametips={'orgrxn':'Alcohol set: reduction and hemiacetal/acetal formation.','origins':'Med Molecules: find the carbonyls in real drugs.','finalboss':'Topic Training → “Aldehydes & Ketones” and “Chirality”.'}),
 6: dict(schemes=[(r'^3\. Reactions', ['ch6_neutral','ch6_esterification','ch6_saponification'], 'Carboxylic acid and ester reactions: neutralization, esterification (a condensation) and saponification (hydrolysis in base).')],
    widgets=[(r'^3\. Reactions', {'rxn':'esterification,esterHydrolysis,saponification,neutralAcid','mode':'mix'}, 'Acid and ester reactions', 'Esterification, ester hydrolysis, saponification and neutralization.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'acids_esters','n':'12'}, 'Carboxylic acids and esters', 'Naming, acidity, salts and ester chemistry.', 620, 'finalboss')],
    games=['orgrxn','origins','finalboss'],
    gametips={'orgrxn':'Acid set: esterification, hydrolysis, saponification and neutralization. Try Full Reaction mode.','origins':'Name It for carboxylic acids and esters.','finalboss':'Topic Training → “Carboxylic Acids & Esters”.'}),
 7: dict(schemes=[(r'Amines are bases', ['ch7_neutral'], 'An amine accepts H⁺ from an acid to form an ammonium salt.'),
                  (r'^4\. Amides', ['ch7_amidation','ch7_amideHyd'], 'Amide formation (a condensation) and acid hydrolysis of an amide.')],
    widgets=[(r'^4\. Amides', {'rxn':'amidation,amideHydrolysis,amideBase,neutralAmine','mode':'mix'}, 'Amine and amide reactions', 'Amine neutralization, amidation and amide hydrolysis in acid or base.', 600, 'orgrxn'),
             ('PRACTICE', {'t':'amines','n':'12'}, 'Amines and amides', 'Classification, naming, basicity and amide chemistry.', 620, 'finalboss')],
    games=['orgrxn','origins','finalboss'],
    gametips={'orgrxn':'Acid set: amidation and amide hydrolysis.','origins':'1°/2°/3° mode for amines (count the carbons on N).','finalboss':'Topic Training → “Amines & Amides”.'}),
 8: dict(schemes=[], widgets=[(r'^2\. Rings', {'t':'carbs','q':'haworth|anomer|fischer|chiral|hemiacetal|classif|aldo|keto','n':'10'}, 'Sugar structures', 'Fischer projections, Haworth rings, anomers and classification.', 640, 'carbs'),
             ('PRACTICE', {'t':'carbs','n':'14'}, 'Carbohydrates', 'Everything in this chapter, from monosaccharides to polysaccharides.', 640, 'carbs')],
    games=['carbs','finalboss'],
    gametips={'carbs':'Work the modes in order: Classify Sugars, Fischer Projections, Haworth Rings, Stereochemistry, Di- & Polysaccharides, Sugar Reactions.','finalboss':'Topic Training → “Carbohydrates”.'}),
 9: dict(schemes=[], widgets=[(r'Triacylglycerols', {'t':'lipids','q':'fatty acid|triacyl|triglycer|saturated|hydrogenation|saponif|soap|omega','n':'10'}, 'Fatty acids and triacylglycerols', 'Saturated vs. unsaturated, melting points, hydrogenation and saponification.', 620, 'lipidlab'),
             ('PRACTICE', {'t':'lipids','n':'14'}, 'Lipids', 'Fatty acids, fats and oils, membrane lipids and steroids.', 640, 'lipidlab')],
    games=['lipidlab','finalboss','hub'],
    gametips={'lipidlab':'Fatty Acid ID first, then Build & Break (hydrolysis and saponification), Lipid Line-up and Membranes.','finalboss':'Topic Training → “Lipids”.','hub':'The Biochemistry Daily 5 mixes in lipid questions.'}),
 10: dict(schemes=[], widgets=[(r'Zwitterions', {'t':'proteins','q':'amino acid|R group|side chain|zwitter|isoelectric|pI|nonpolar|polar','n':'10'}, 'Amino acids and charge', 'R-group classes, zwitterions and charge at different pH.', 620, 'peptides'),
             ('PRACTICE', {'t':'proteins','n':'14'}, 'Amino acids and proteins', 'Peptide bonds, naming peptides and the four levels of protein structure.', 640, 'peptides')],
    games=['peptides','finalboss'],
    gametips={'peptides':'Amino Acids & R Groups first, then Condense & Hydrolyze (remove the water yourself), Name That Peptide and Protein Structure.','finalboss':'Topic Training → “Amino Acids & Proteins”.'}),
 11: dict(schemes=[], widgets=[(r'^4\. Inhibition', {'t':'enzymes','q':'inhibit|active site|substrate|activation energy|denatur|optimum|rate|temperature|pH','n':'10'}, 'Enzyme activity and inhibition', 'Read activity plots, spot the inhibitor type and predict what temperature and pH do.', 640, 'enzyme'),
             ('PRACTICE', {'t':'enzymes','n':'14'}, 'Enzymes and vitamins', 'Enzyme classes, cofactors, vitamins and regulation.', 640, 'enzyme')],
    games=['enzyme','finalboss','hub'],
    gametips={'enzyme':'Classify the Enzyme, then Spot the Inhibitor and Read the Plot; finish with Cofactors & Vitamins.','finalboss':'Topic Training → “Enzymes & Vitamins”.','hub':'The Biochemistry Daily 5 includes enzyme plots.'}),
 12: dict(schemes=[], widgets=[(r'^2\. Structure', {'t':'nucleic','q':'DNA|base pair|nucleotide|purine|pyrimidine|replication|double helix|complement','n':'10'}, 'DNA structure and replication', 'Nucleotides, base pairing, antiparallel strands and replication.', 620, 'helix'),
             ('PRACTICE', {'t':'nucleic','q':'codon|translation|transcription|mRNA|tRNA|ribosome|mutation|genetic code','n':'10'}, 'From gene to protein', 'Transcription, translation, codons and mutations.', 620, 'peptides')],
    games=['helix','peptides','finalboss'],
    gametips={'helix':'Every mode fits this chapter. Start with base pairing, then replication, transcription and translation.','peptides':'Codon Decoder mode: translate mRNA with the codon chart.','finalboss':'Topic Training → “Nucleic Acids”.'}),
 13: dict(schemes=[], widgets=[(r'^4\. Fates of pyruvate', {'t':'metabolism','q':'glycoly|pyruvate|lactate|acetyl CoA|NAD|ATP|cori|fermentation','n':'10'}, 'Glycolysis and pyruvate', 'Net ATP and NADH, coenzymes, and what happens to pyruvate with and without oxygen.', 620, 'marathon'),
             ('PRACTICE', {'t':'metabolism','q':'glycogen|gluconeo|insulin|glucagon|digest|amylase|blood glucose|pentose|catabol|anabol','n':'10'}, 'Carbohydrate metabolism', 'Digestion, glycogen, gluconeogenesis and blood-glucose control.', 620, 'marathon')],
    games=['metab','finalboss','hub'],
    gametips={'metab':'Pathway Order (glycolysis, fates of pyruvate, Cori cycle), Count the Coenzymes (glycolysis and fermentation) and Fuel Fates (fed versus fasting).','finalboss':'Topic Training → “Metabolism”.','hub':'Biochemistry Daily 5.'}),
 14: dict(schemes=[], widgets=[(r'^3\. ATP from one glucose', {'t':'metabolism','q':'citric|krebs|electron transport|ATP synthase|oxidative phosph|NADH|FADH|coenzyme Q|cytochrome|mitochondri','n':'12'}, 'Citric acid cycle and electron transport', 'Count the NADH, FADH₂ and ATP, and follow the electrons to O₂.', 620, 'marathon'),
             ('PRACTICE', {'t':'metabolism','q':'kcal|Calorie|energy|oxidized|reduced|oxidation|LEO|GER','n':'8'}, 'Energy and redox', 'Food energy and keeping oxidation and reduction straight.', 620, 'marathon')],
    games=['metab','finalboss','hub'],
    gametips={'metab':'Pathway Order (citric acid cycle, electron transport), Count the Coenzymes (ATP per acetyl CoA and per glucose) and Name the Reaction (succinate → fumarate → malate → oxaloacetate).','finalboss':'Topic Training → “Metabolism”.','hub':'Biochemistry Daily 5.'}),
 15: dict(schemes=[], widgets=[(r'Oxidation \(in the mitochondria\)', {'t':'metabolism','q':'fatty acid|β-oxid|beta-oxid|beta oxid|acetyl CoA|ketone bod|ketosis|ketoacid|lipogen','n':'10'}, 'β-Oxidation and ketone bodies', 'Count the cycles, acetyl CoA and ATP from a fatty acid; know when ketone bodies form.', 620, 'marathon'),
             ('PRACTICE', {'t':'metabolism','q':'urea|transamin|deamin|ammoni|nitrogen|amino acid|glucogenic|ketogenic|essential','n':'10'}, 'Amino acid metabolism', 'Transamination, deamination, the urea cycle and nitrogen balance.', 620, 'marathon')],
    games=['metab','finalboss','hub'],
    gametips={'metab':'Pathway Order (β-oxidation, ketone bodies, the fate of nitrogen), Count the Coenzymes for any fatty acid, Name the Reaction (transamination, deamination) and Fuel Fates (fasting, diabetes).','finalboss':'Topic Training → “Metabolism” (and “Amino Acids & Proteins”).','hub':'Biochemistry Daily 5.'}),
}

def insert_after_section(src, h3_regex, block):
    """Insert block at the end of the <h3> section whose text matches h3_regex (before the next <h3>/<h2>/<div class=\"box-note\"...Health)."""
    m = None
    for mm in re.finditer(r'<h3>(.*?)</h3>', src):
        if re.search(h3_regex, html.unescape(mm.group(1))):
            m = mm; break
    if not m:
        raise SystemExit(f'anchor not found: {h3_regex}')
    nxt = re.search(r'\n(?=<h3>|<h2>|<div class="box-note">\s*<p class="boxtitle">Health Career)', src[m.end():])
    pos = m.end() + (nxt.start() if nxt else 0)
    return src[:pos] + '\n' + block + src[pos:]

def build_guide(ch):
    src = open(os.path.join(DRAFTS, GUIDE_FILES[ch])).read()
    src = re.sub(r'^\s*<!--.*?-->\s*', '', src, count=1, flags=re.S)
    # figures -> GitHub Pages
    src = re.sub(r'<!-- IMAGE:[^>]*-->\s*', '', src)
    src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', lambda m: f'src="{BASE}figures/{m.group(1)}"', src)
    plan = PLAN[ch]
    fig_n = len(re.findall(r'<figcaption>', src)) + 1
    for (rx, ids, cap) in plan['schemes']:
        src = insert_after_section(src, rx, scheme_fig(ids, f'{ch}.{fig_n}', cap)); fig_n += 1
    before_practice = []
    for (rx, params, title, blurb, h, game) in plan['widgets']:
        w = widget(params, title, blurb, h, game)
        if rx == 'PRACTICE': before_practice.append(w)
        else: src = insert_after_section(src, rx, w)
    if before_practice:
        src = src.replace('<h2>Practice</h2>', ''.join(before_practice) + '<h2>Practice</h2>', 1)
    from patient_case import case_block
    assert src.count('<h2>Practice</h2>') == 1
    src = src.replace('<h2>Practice</h2>', case_block(ch) + '<h2>Practice</h2>', 1)
    src = src.rstrip() + '\n' + games_box(ch)
    # renumber figures in document order
    k = [0]
    def ren(m):
        k[0] += 1; return f'<figcaption>Figure {ch}.{k[0]}:'
    src = re.sub(rf'<figcaption>Figure {ch}\.\d+:', ren, src)
    return src

def build_games_page(ch):
    plan = PLAN[ch]
    parts = [f'<div class="box-note"><p class="boxtitle">How to use this page</p><p>These games are free, work on your phone, and keep score in your browser. Play a few rounds after each lecture; a short session every day beats one long one before the exam. Each game opens in a new tab if you prefer a bigger screen.</p></div>\n']
    for g in plan['games']:
        if ch == 1 and g == 'lewis': continue   # chapter 1 has its own 1.11 Lewis Structures page
        name, url, blurb = GAMES[g]; tip = plan['gametips'].get(g, '')
        parts.append(f'<h2>{html.escape(name)}</h2>\n<p>{html.escape(blurb)}</p>\n' + (f'<p><strong>For this chapter:</strong> {html.escape(tip)}</p>\n' if tip else '') +
                     f'<p><iframe src="{html.escape(url)}" width="100%" height="900" style="border:0;border-radius:12px;" title="{html.escape(name)}" loading="lazy" allowfullscreen="allowfullscreen"></iframe></p>\n'
                     f'<p style="font-size:0.9em;"><a href="{html.escape(url)}" target="_blank" rel="noopener">Open {html.escape(name)} in a new tab</a></p>\n')
    # the chapter's Try It widgets, collected
    parts.append('<h2>Quick Checks from This Chapter</h2>\n<p>The same short practice sets that appear in the Chapter Guide, in one place.</p>\n')
    for (rx, params, title, blurb, h, game) in plan['widgets']:
        parts.append(widget(params, title, blurb, h, game))
    parts.append('<p style="font-size:0.9em;color:#555;">Games and practice sets by ItsDrDan (Daniel Kwasniewski, Fresno City College): <a href="https://itsdrdan.github.io/games/" target="_blank" rel="noopener">Dr. Dan\'s Chemistry Study Hub</a>. Game design and chemistry by ItsDrDan; code written with AI assistance and checked by the author.</p>\n')
    return ''.join(parts)

LEWIS_PAGE = """<div class="box-objectives"><p class="boxtitle">What this page is for</p><p>Drawing Lewis structures is the one skill from this chapter that every later chapter leans on: functional groups (Chapter 2 onward), polarity and hydrogen bonding (Section 1.8), acid&ndash;base behavior of amines and carboxylic acids, and the shapes of biomolecules all start from a correct Lewis structure. This page gives you unlimited practice with instant checking.</p></div>
<h2>Lewis Structure Studio</h2>
<p>Draw a Lewis structure atom by atom, then let the game check your electron count, octets, formal charges, VSEPR shape and polarity. It is free, works on a phone, and keeps your streak in this browser. The method it checks is exactly the one in <strong>Section 1.3</strong> (count valence electrons, connect atoms, complete octets, convert lone pairs to multiple bonds if needed) and <strong>Section 1.5</strong> (shape and polarity).</p>
<div class="box-note"><p class="boxtitle">Suggested order</p><ol>
<li><strong>Warm up (octet rule):</strong> CH<sub>4</sub>, NH<sub>3</sub>, H<sub>2</sub>O, HF, CCl<sub>4</sub>.</li>
<li><strong>Multiple bonds:</strong> O<sub>2</sub>, N<sub>2</sub>, CO<sub>2</sub>, HCN, H<sub>2</sub>CO (formaldehyde), C<sub>2</sub>H<sub>4</sub>, C<sub>2</sub>H<sub>2</sub>.</li>
<li><strong>Organic molecules you will see all semester:</strong> CH<sub>3</sub>OH, CH<sub>3</sub>NH<sub>2</sub>, CH<sub>3</sub>CHO, CH<sub>3</sub>COOH, CH<sub>3</sub>OCH<sub>3</sub>.</li>
<li><strong>Then predict</strong> the shape around each central atom (tetrahedral, trigonal pyramidal, bent, trigonal planar, linear) and whether the molecule is polar. If your answer and the game&rsquo;s disagree, redraw before looking at the explanation.</li></ol></div>
<p><iframe src="https://itsdrdan.github.io/lewisstructures/?course=3B" width="100%" height="900" style="border:0;border-radius:12px;" title="Lewis Structure Studio" loading="lazy" allowfullscreen="allowfullscreen"></iframe></p>
<p style="font-size:0.9em;"><a href="https://itsdrdan.github.io/lewisstructures/?course=3B" target="_blank" rel="noopener">Open Lewis Structure Studio in a new tab</a> (recommended on a phone or small screen).</p>
<div class="box-note" style="border-left:6px solid #0e6ea8;"><p class="boxtitle">Professor Tip</p><p>On the exam you will draw structures on paper with no checker. After each game round, redraw the same molecule from memory on paper, including lone pairs, and only then compare. Students who practice this way stop losing points for missing lone pairs on O and N, which is the most common Lewis-structure error in CHEM 3B.</p></div>
<p>The other games and quick checks for this chapter are on the <strong>Practice Games</strong> page that follows.</p>
<p style="font-size:0.9em;color:#555;">Lewis Structure Studio by ItsDrDan (Daniel Kwasniewski, Fresno City College): <a href="https://itsdrdan.github.io/games/" target="_blank" rel="noopener">Dr. Dan\'s Chemistry Study Hub</a>. Game design and chemistry by ItsDrDan; code written with AI assistance and checked by the author. The game is a free tool embedded by link and is not part of the licensed text.</p>
"""

if __name__ == '__main__':
    out = os.path.join(ROOT, 'pages'); os.makedirs(out, exist_ok=True)
    manifest = []
    open(os.path.join(out, 'ch01_lewis.html'), 'w').write(LEWIS_PAGE)
    manifest.append({'file': 'ch01_lewis.html', 'pageId': 597064, 'what': '1.11 Practice Game - Lewis Structures'})
    for ch in range(1, 16):
        g = build_guide(ch); fn = f'ch{ch:02d}_guide.html'; open(os.path.join(out, fn), 'w').write(g)
        manifest.append({'file': fn, 'pageId': GUIDE_IDS[ch], 'what': f'Chapter Guide {ch}'})
        p = build_games_page(ch); fn2 = f'ch{ch:02d}_games.html'; open(os.path.join(out, fn2), 'w').write(p)
        manifest.append({'file': fn2, 'create': {'parentId': CHAPTER_IDS[ch], 'title': 'Practice Games'}, 'what': f'Practice Games page, chapter {ch}'})
        print(ch, len(g), len(p))
    # practice-problem pages (drafts, figures rewritten to GitHub Pages)
    PROB_IDS = {1:597063,2:597075,3:597087,4:597101,5:597108,6:597120,7:597133,8:597142,9:597151,10:597165,11:597174,12:597185,13:597199,14:597206,15:597219}
    import glob
    for ch in range(1, 16):
        f = glob.glob(os.path.join(DRAFTS, f'Ch{ch:02d}_Practice_Problems_*.html'))[0]
        src = open(f).read(); src = re.sub(r'^\s*<!--.*?-->\s*', '', src, count=1, flags=re.S)
        src = re.sub(r'<!-- IMAGE:[^>]*-->\s*', '', src)
        src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', lambda m: f'src="{BASE}figures/{m.group(1)}"', src)
        k = [0]
        def ren3(mm):
            k[0] += 1; return f'<figcaption>Problem figure {ch}.{k[0]}:'
        src = re.sub(rf'<figcaption>Figure {ch}\.\d+:', ren3, src)
        if ch >= 2:
            sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
            from cumulative import cumulative_block
            src = src.rstrip() + '\n\n' + cumulative_block(ch, BASE)
        fn = f'ch{ch:02d}_problems.html'; open(os.path.join(out, fn), 'w').write(src)
        manifest.append({'file': fn, 'pageId': PROB_IDS[ch], 'what': f'Practice Problems {ch}'})
    # full section pages that replace empty placeholders
    SECTION_TITLES = {597099:'4.10: Acidity of Alcohols and Phenols',597131:'7.11: Neurotransmitters',597172:'11.7: Enzyme Regulation - Covalent Modification and Genetic Control',597183:'12.9: Structure and Function of RNA',597194:'13.7: Entry of Other Sugars into Glycolysis',597195:'13.8: Regulation of Glucose Metabolism and Metabolism During Stress',597196:'13.9: Glycogen Metabolism- Glycogenesis and Glycogenolysis',597197:'13.10: Gluconeogenesis- Glucose Synthesis from Noncarbohydrates',597204:'14.5: Energy Output in Complete Glucose Catabolism',597212:'15.6: Storage and Mobilization of Triacylglycerols'}
    for f in sorted(glob.glob('/home/claude/textbook/sections/*.html')):
        if os.path.basename(f).startswith(('add_', 'ext_', 'src_')): continue
        src = open(f).read(); src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', lambda m: f'src="{BASE}figures/{m.group(1)}"', src)
        fn = os.path.basename(f); open(os.path.join(out, fn), 'w').write(src)
        m = re.search(r'_(\d+)\.html$', f)
        if m:
            pid = int(m.group(1))
            sec = SECTION_TITLES.get(pid, '').split(':')[0]
            if sec:
                k = [0]
                def ren2(mm):
                    k[0] += 1; return f'<figcaption>Figure {sec}.{k[0]}:'
                src = re.sub(r'<figcaption>Figure \d+\.\d+:', ren2, src); open(os.path.join(out, fn), 'w').write(src)
            manifest.append({'file': fn, 'pageId': pid, 'what': 'Section ' + SECTION_TITLES.get(pid, str(pid))})
        elif fn == 'front_about.html':
            manifest.append({'file': fn, 'create': {'parentId': 488225, 'exactTitle': 'About This Book'}, 'what': 'Front matter: About This Book'})
        elif fn == 'front_alignment.html':
            manifest.append({'file': fn, 'pageId': 597272, 'what': 'Front matter: Course Outline Alignment'})
        elif fn == 'back_sources.html':
            manifest.append({'file': fn, 'create': {'parentId': 488230, 'exactTitle': 'Source Attributions by Section'}, 'what': 'Back matter: Source Attributions by Section'})
    # Lecture Connection blocks appended to transcluded section pages
    TR = json.load(open('/home/claude/textbook/tools/transclusions.json'))
    titles = dict(l.split(' ', 1) for l in open('/home/claude/textbook/tools/section_ids.txt').read().splitlines() if l.strip())
    for f in sorted(glob.glob('/home/claude/textbook/sections/add_*.html')):
        pid = re.search(r'add_(\d+)\.html$', f).group(1)
        if pid not in TR: raise SystemExit('no transclusion for ' + pid)
        src = open(f).read()
        src = re.sub(r'<!-- IMAGE:[^>]*-->\s*', '', src)
        src = re.sub(r'src="(?:/)?(Slide\d+\.png)"', lambda m: f'src="{BASE}figures/{m.group(1)}"', src)
        sec = titles.get(pid, '').split(':')[0]
        k = [0]
        def ren4(mm):
            k[0] += 1; return f'<figcaption>Figure {sec}.{k[0]}:'
        src = re.sub(r'<figcaption>Figure \d+\.\d+:', ren4, src)
        # Sections whose source text has been copied in (with rewritten alt text) live in sections/src_<pid>.html;
        # the rest are still transcluded from the source book.
        srcf = f'/home/claude/textbook/sections/src_{pid}.html'
        head = open(srcf).read().rstrip() if os.path.exists(srcf) else TR[pid].rstrip()
        body = head + '\n' + src.strip() + '\n'
        import videos   # embedded Amoeba Sisters / Daniel Kwasniewski videos (tools/videos.py); insert() replaces any old block
        if int(pid) in videos.SEC: body = videos.insert(body, 'section', videos.block(videos.SEC[int(pid)], 'section'))
        fn = f'sec_{pid}.html'; open(os.path.join(out, fn), 'w').write(body)
        manifest.append({'file': fn, 'pageId': int(pid), 'what': 'Section ' + titles.get(pid, pid) + ' (+ Lecture Connection)'})
    json.dump(manifest, open(os.path.join(out, 'manifest.json'), 'w'), indent=1)

# R04: print-friendly answers. Answers stay click-to-reveal online; in the PDF they move to an "Answers"
# list at the end of each page (tools/answerkey.js). Runs on every built page so the key never drifts.
import subprocess, glob as _glob
_pages = sorted(_glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'pages', '*.html')))
if _pages:
    subprocess.run(['node', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'answerkey.js')] + _pages, check=False)
