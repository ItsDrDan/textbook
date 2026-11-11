"""Embedded YouTube videos: an Amoeba Sisters or Dr. Dan "Watch first" video at the top of chapter pages,
and topic videos inside sections (placed right after the Learning Objectives box).
python3 tools/videos.py -> /tmp/.../video_spec.json  {pageId: {"where": "chapter"|"section", "html": "..."}}"""
import json, html, sys
CH = {1: 597039, 2: 597040, 3: 597041, 4: 597042, 5: 597043, 6: 597044, 7: 597045, 8: 597046, 9: 597047, 10: 597048,
      11: 597049, 12: 597050, 13: 597051, 14: 597052, 15: 597053}
AS, DD = 'Amoeba Sisters', 'Dr. Dan (ItsDrDan)'
# id: (title, length, channel, one-line reason)
V = {
 '3jwAGWky98c': ('Properties of Water', '6:51', AS, 'A friendly look at why water is polar and how hydrogen bonds give it its special properties. Keep it in mind for the intermolecular forces in this chapter.'),
 'gSKpPWYVnTU': ('Organic Chemistry: An Introduction (Part 1)', '16:41', DD, 'What makes a compound organic, and how carbon builds chains and rings.'),
 '1Dx7LDwINLU': ('Biomolecules', '7:49', AS, 'The big picture first: carbohydrates, lipids, proteins and nucleic acids, and what each one does in your body.'),
 'ALFE2tNIY5c': ('Dehydration Synthesis and Hydrolysis', '6:08', AS, 'Building molecules by removing water, and breaking them apart by adding it back.'),
 'qBCVVszQQNs': ('Inside the Cell Membrane', '9:09', AS, 'Why phospholipids line up into a bilayer, and what cholesterol and membrane proteins do there.'),
 'Ptmlvtei8hw': ('Cell Transport', '7:50', AS, 'How molecules cross the membrane: diffusion, osmosis, and active transport.'),
 'hok2hyED9go': ('Protein Structure and Folding', '7:46', AS, 'Primary, secondary, tertiary and quaternary structure in plain language.'),
 'qgVFkRn8f10': ('Enzymes', '5:47', AS, 'How an enzyme’s active site speeds up a reaction, and what makes enzymes stop working.'),
 '6EDBlowVST0': ('Enzyme Examples, Cofactors/Coenzymes, Inhibitors, and Feedback Inhibition', '8:16', AS, 'Competitive and noncompetitive inhibitors, cofactors, and feedback inhibition.'),
 'JQByjprj_mA': ('DNA vs RNA', '6:31', AS, 'Side-by-side comparison of the two nucleic acids: sugars, bases and strands.'),
 'Qqe4thU-os8': ('DNA Replication', '8:12', AS, 'How the cell copies DNA, and the enzymes that do the work.'),
 'oefAI2x2CQM': ('Protein Synthesis: Transcription and Translation', '8:47', AS, 'From a gene to mRNA to a protein, step by step.'),
 'LsEYgwuP6ko': ('How to Read a Codon Chart', '7:50', AS, 'Practice reading the genetic code to find the amino acid for each codon.'),
 'vl6Vlf2thvI': ('Mutations', '7:14', AS, 'Substitutions, insertions and deletions, and why a frameshift changes so much.'),
 '8FqlTslU22s': ('Viruses', '6:49', AS, 'What a virus is made of and how it uses a host cell to copy itself.'),
 'CDw4WPng2iE': ('Genetic Engineering', '8:25', AS, 'How scientists insert a gene into another organism, for example to make human insulin.'),
 'a5jmdh9AnS4': ('PCR (Polymerase Chain Reaction)', '7:54', AS, 'How PCR makes millions of copies of a DNA segment, used in medical testing.'),
 '23ZzI6WZS28': ('What is ATP?', '5:52', AS, 'ATP as the cell’s energy currency, and how breaking a phosphate bond releases energy.'),
 '1UvuBYUbFk0': ('Digestive System', '8:43', AS, 'The organs of digestion and where carbohydrates, fats and proteins are broken down.'),
 'YbdkbCU20_M': ('Fermentation', '8:34', AS, 'What happens to pyruvate without oxygen: lactic acid and alcoholic fermentation.'),
 'Iz0Q9nTZCw4': ('Homeostasis and Negative/Positive Feedback', '6:24', AS, 'How the body keeps blood glucose steady with insulin and glucagon.'),
 'eJ9Zjc-jdys': ('Cellular Respiration', '8:47', AS, 'Glycolysis, the citric acid cycle and the electron transport chain in one short overview.'),
 'CGmbd2YwflY': ('How to Draw Lewis Structures', '22:25', DD, 'Step-by-step Lewis structures.'),
 'Wz23sE4KUBE': ('Electronegativity and Polarity (Part 1: Polar Bonds)', '12:30', DD, 'Using electronegativity to decide when a bond is polar.'),
 'wD3b-7J0Xy0': ('Introduction to VSEPR Theory', '20:20', DD, 'Predicting shapes and bond angles from electron groups.'),
 '0fzuzHnkPAc': ('Electronegativity and Polarity (Part 2: Polar Molecules)', '18:02', DD, 'Deciding whether a whole molecule is polar.'),
 'CdA3Ov94lw0': ('Dipole-Dipole, Hydrogen Bonding, and Ion-Dipole', '17:14', DD, 'The intermolecular forces you will use all semester.'),
 'kEkvxf6e-Ro': ('Tips and Tricks on Drawing Isomers: The 18 Isomers of Octane', '13:51', DD, 'A system for finding every branched isomer.'),
 '9lxWINhQtUc': ('Naming Alkanes with Branches', '15:16', DD, 'IUPAC naming with substituents.'),
 'OxLTA0CZrd4': ('Naming Alkanes with Propyl & Butyl Isomers', '12:22', DD, 'Isopropyl, sec-butyl, isobutyl and tert-butyl groups.'),
 'JutTTWvB2wQ': ('Identifying and Naming Cis and Trans Alkenes', '12:48', DD, 'Spotting and naming cis and trans isomers.'),
 'b4DBut72xEI': ('Drawing Cis and Trans Alkenes', '17:34', DD, 'Drawing cis and trans alkenes as expanded, condensed and skeletal formulas.'),
 'Dcun-l5jM9w': ('Addition Reactions of Alkenes and Markovnikov’s Rule', '20:39', DD, 'Hydrogenation, halogenation, hydrohalogenation and hydration.'),
 'l3Sb_GWBano': ('Dehydration Reactions of Alcohols and Zaitsev’s Rule', '10:26', DD, 'Making alkenes from alcohols.'),
 'veiUgkx_Dlc': ('Oxidation of Alcohols', '9:27', DD, 'What 1°, 2° and 3° alcohols give when oxidized.'),
 'nN-RMEEbjLI': ('How to Name Ethers in 3 Easy Steps', '11:47', DD, 'IUPAC and common names for ethers.'),
 '1KPqZ2pp9bg': ('Formation of Hemiacetals and Acetals', '11:53', DD, 'Adding alcohols to aldehydes and ketones.'),
 'whVLjQhx3FI': ('Cyclic Acetals and Ketals', '16:20', DD, 'The same reaction inside one molecule, which is how sugars form rings.'),
 'K0oEXP7JBZU': ('Reduction Reactions of Aldehydes and Ketones', '11:21', DD, 'Reducing carbonyls to alcohols.'),
 'RudBXy5lTuU': ('Introduction to Chirality, Enantiomers, and Diastereomers', '21:04', DD, 'Chiral carbons and the kinds of stereoisomers.'),
 '4Z7_TvNmeR4': ('Tips and Tricks to Finding Chiral Carbons', '22:54', DD, 'A quick way to find every chiral carbon.'),
 '2pwJ5G0uOtA': ('How to Make Esters through Esterification', '11:29', DD, 'Carboxylic acid + alcohol → ester + water.'),
 'vfSSUIcgzTY': ('Hydrolysis of Esters: Acid and Base (Saponification)', '17:48', DD, 'Breaking esters apart with acid or base.'),
 'HU4KHyptdVA': ('Hydrolysis Reactions of Amides with Acids and Bases', '19:05', DD, 'Amide hydrolysis in two steps.'),
 '417CUTR3H1E': ('Carbohydrate Basics: Classifying Aldoses and Ketoses', '7:47', DD, 'Classifying sugars by carbonyl group and number of carbons.'),
 '5L0AmyTCyi4': ('How to Draw Haworth Projections from Fischer Projections', '17:29', DD, 'Turning a Fischer projection of glucose into its ring form.'),
 'xMjXa2mliZA': ('How to Draw a Haworth Projection (Ketose Edition)', '7:39', DD, 'The same method for fructose.'),
 'pwyW-X99GI8': ('Oxidation and Reduction of Carbohydrates', '10:44', DD, 'Reducing sugars, sugar acids and sugar alcohols.'),
 'BQwU9Z7myeg': ('Lipids: Formation of Triacylglycerides', '5:14', DD, 'Glycerol + three fatty acids.'),
 'Heg74N-mZms': ('Lipids: Hydrolysis of Triacylglycerides', '4:50', DD, 'Breaking a triglyceride apart with water.'),
 'gO3YPk_2lTE': ('Lipids: Saponification of Triacylglycerides', '5:25', DD, 'Making soap.'),
 'M7VkdbGkPXY': ('Lipids: Hydrogenation of Unsaturated Fats', '6:12', DD, 'Adding H₂ to C=C bonds in oils.'),
 'Y_bXmJDoANI': ('Drawing Zwitterions and Amino Acids Made Simple', '14:34', DD, 'Amino acid charges at different pH values.'),
 'ec1npXqFdDM': ('Understanding Protein Structure', '23:39', DD, 'Primary, secondary, tertiary and quaternary structure, with examples.'),
}
START = {1: ['3jwAGWky98c'], 2: ['gSKpPWYVnTU'], 8: ['1Dx7LDwINLU'], 9: ['qBCVVszQQNs'], 10: ['hok2hyED9go'], 11: ['qgVFkRn8f10'],
         12: ['JQByjprj_mA'], 13: ['23ZzI6WZS28'], 14: ['eJ9Zjc-jdys']}
SEC = {597056: ['CGmbd2YwflY'], 597057: ['Wz23sE4KUBE'], 597058: ['wD3b-7J0Xy0', '0fzuzHnkPAc'], 597061: ['CdA3Ov94lw0'],
       597067: ['kEkvxf6e-Ro'], 597069: ['9lxWINhQtUc', 'OxLTA0CZrd4'], 597079: ['JutTTWvB2wQ', 'b4DBut72xEI'], 597081: ['Dcun-l5jM9w'],
       597094: ['l3Sb_GWBano', 'veiUgkx_Dlc'], 597097: ['nN-RMEEbjLI'], 597104: ['1KPqZ2pp9bg', 'whVLjQhx3FI'], 597105: ['K0oEXP7JBZU'],
       597106: ['RudBXy5lTuU', '4Z7_TvNmeR4'], 597115: ['2pwJ5G0uOtA'], 597116: ['vfSSUIcgzTY', 'ALFE2tNIY5c'], 597127: ['HU4KHyptdVA'],
       597135: ['417CUTR3H1E'], 597137: ['5L0AmyTCyi4', 'xMjXa2mliZA'], 597138: ['pwyW-X99GI8'], 597139: ['ALFE2tNIY5c'],
       597145: ['BQwU9Z7myeg', 'Heg74N-mZms', 'gO3YPk_2lTE', 'M7VkdbGkPXY'], 597148: ['Ptmlvtei8hw'], 597155: ['Y_bXmJDoANI'],
       597158: ['ec1npXqFdDM'], 597169: ['6EDBlowVST0'], 597177: ['Qqe4thU-os8'], 597179: ['oefAI2x2CQM', 'LsEYgwuP6ko'],
       597180: ['vl6Vlf2thvI'], 597181: ['8FqlTslU22s'], 597182: ['CDw4WPng2iE', 'a5jmdh9AnS4'], 597190: ['1UvuBYUbFk0'],
       597193: ['YbdkbCU20_M'], 597195: ['Iz0Q9nTZCw4']}

# key moments (timestamps) for Dr. Dan's videos, from the study hub (ItsDrDan/games data/hub.js)
MOM = json.load(open(__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)), 'video_moments.json')))

def frame(vid):
    t, ln, ch, why = V[vid]
    e = html.escape
    note = ('Video by the Amoeba Sisters on YouTube, embedded here. It is not covered by this book’s Creative Commons license.'
            if ch == AS else 'Video by Dr. Dan on the ItsDrDan YouTube channel.')
    M = MOM.get(vid, []) if ch != AS else []
    fmt = lambda x: f'{x // 60}:{x % 60:02d}'
    jump = ('<p><small><strong>Jump to (opens YouTube):</strong> ' + ' &middot; '.join(
        f'<a style="text-decoration:underline" href="https://www.youtube.com/watch?v={vid}&amp;t={s}s" target="_blank" rel="noopener">{fmt(s)} {e(l)}</a>' for s, l in M)
        + '</small></p>') if len(M) > 1 else ''
    return (f'<p><strong>{e(t)}</strong> ({ln}, {e(ch)})<br />{e(why)}</p>'
            f'<div style="max-width:640px"><div style="width:100%;height:0px;position:relative;padding-bottom:56.25%"><iframe src="https://www.youtube.com/embed/{vid}?rel=0" '
            f'title="{e(t)} ({e(ch)}, YouTube video)" frameborder="0" style="width:100%;height:100%;position:absolute;left:0;top:0" '
            f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="true"></iframe></div></div>' + jump +
            f'<p><small>{note} Turn on captions with the CC button. Video not loading? <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">Watch it on YouTube</a>.</small></p>')

def block(vids, where):
    title = 'Watch first' if where == 'chapter' else ('Video' if len(vids) == 1 else 'Videos')
    lead = ('<p>Start here: an overview of the big ideas before the details in this chapter.</p>' if where == 'chapter' else '')
    return (f'<div class="box-note video-embeds" data-videos="{" ".join(vids)}"><p class="boxtitle">{title}</p>{lead}'
            + ''.join(frame(v) for v in vids) + '</div>')

def spec():
    out = {}
    for ch, vids in START.items(): out[CH[ch]] = {'where': 'chapter', 'html': block(vids, 'chapter')}
    for pid, vids in SEC.items(): out[pid] = {'where': 'section', 'html': block(vids, 'section')}
    return out

if __name__ == '__main__':
    s = spec(); json.dump(s, open(sys.argv[1], 'w'), ensure_ascii=False)
    print(len(s), 'pages,', sum(len(v) for v in START.values()) + sum(len(v) for v in SEC.values()), 'embeds')

def insert(body, where, blk):
    """same placement as on LibreTexts: chapter pages after the opener figure, sections after the objectives box"""
    import re
    s = body.find('<div class="box-note video-embeds"')
    if s >= 0:   # replace an old block
        n = len(re.search(r'data-videos="([^"]*)"', body[s:]).group(1).split())
        e = s
        END = 'Watch it on YouTube</a>.</small></p>'
        for _ in range(n): e = body.index(END, e) + len(END)
        body = body[:s] + body[body.index('</div>', e) + 6:].lstrip('\n')
    if where == 'chapter':
        k = body.find('</figure>'); i = k + 9 if k >= 0 else 0
    else:
        head = body[:4000]; i = -1
        k = head.find('class="box-objectives"')
        if k >= 0:
            c = body.find('</section>', k); i = c + 10 if c >= 0 else -1
        else:
            k = head.find('class="skills"')
            if k >= 0:
                c = body.find('</div>', k); i = c + 6 if c >= 0 else -1
        if i < 0: i = 0
    return body[:i] + '\n' + blk + '\n' + body[i:]

def apply_local(root):
    import os
    done = []
    for pid, vids in SEC.items():
        for f in (f'pages/sec_{pid}.html', f'sections/src_{pid}.html'):
            p = os.path.join(root, f)
            if os.path.exists(p):
                b = open(p, encoding='utf-8').read()
                open(p, 'w', encoding='utf-8').write(insert(b, 'section', block(vids, 'section'))); done.append(f)
    return done
