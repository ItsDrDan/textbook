"""Match each ADAPT homework question to one of Dr. Dan's YouTube lessons (shown with the Hint button).
Rules are per chapter; first matching rule wins. python3 tools/adapt_hint_videos.py <out.json>"""
import json, glob, re, html, sys, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
VID = {  # id: (title, length)
 'CGmbd2YwflY': ('How to Draw Lewis Structures', '22:25'), '-WH0D2cWcJc': ('Calculating Formal Charge', '—'),
 'wD3b-7J0Xy0': ('Introduction to VSEPR Theory', '20:20'), 'Wz23sE4KUBE': ('Electronegativity and Polarity (Part 1: Polar Bonds)', '12:30'),
 '0fzuzHnkPAc': ('Electronegativity and Polarity (Part 2: Polar Molecules)', '18:02'), 'CdA3Ov94lw0': ('Dipole-Dipole, Hydrogen Bonding, and Ion-Dipole', '17:14'),
 'vf1I8M32OXQ': ('Dispersion Forces and Polarizability', '—'), 'lAcgVwEmjM8': ('Properties of Intermolecular Forces: Boiling Point, Melting Point', '—'),
 'mvdjSfWFdaU': ('How to Calculate Molar Mass', '—'), 'u_Y1sC58C7M': ('Chemical Bonding: Covalent, Ionic, and Metallic Bonds', '—'),
 'gSKpPWYVnTU': ('Organic Chemistry: An Introduction (Part 1)', '16:41'), 'xbsGe976lZ4': ('Organic Chemistry: An Introduction (Part 2)', '—'),
 '9lxWINhQtUc': ('Naming Alkanes with Branches', '15:16'), 'OxLTA0CZrd4': ('Naming Alkanes with Propyl & Butyl Isomers', '12:22'),
 'kEkvxf6e-Ro': ('Tips and Tricks on Drawing Isomers', '13:51'), 'JutTTWvB2wQ': ('Identifying and Naming Cis and Trans Alkenes', '12:48'),
 'b4DBut72xEI': ('Drawing Cis and Trans Alkenes', '17:34'), 'Dcun-l5jM9w': ('Addition Reactions of Alkenes and Markovnikov’s Rule', '20:39'),
 'l3Sb_GWBano': ('Dehydration Reactions of Alcohols and Zaitsev’s Rule', '10:26'), 'veiUgkx_Dlc': ('Oxidation of Alcohols', '9:27'),
 'nN-RMEEbjLI': ('How to Name Ethers in 3 Easy Steps', '11:47'), '1KPqZ2pp9bg': ('Formation of Hemiacetals and Acetals', '11:53'),
 'whVLjQhx3FI': ('Cyclic Acetals and Ketals', '16:20'), 'K0oEXP7JBZU': ('Reduction Reactions of Aldehydes and Ketones', '11:21'),
 'RudBXy5lTuU': ('Introduction to Chirality, Enantiomers, and Diastereomers', '21:04'), '4Z7_TvNmeR4': ('Tips and Tricks to Finding Chiral Carbons', '22:54'),
 '2pwJ5G0uOtA': ('How to Make Esters through Esterification', '11:29'), 'vfSSUIcgzTY': ('Hydrolysis of Esters: Acid and Base (Saponification)', '17:48'),
 'HU4KHyptdVA': ('Hydrolysis Reactions of Amides with Acids and Bases', '19:05'), '417CUTR3H1E': ('Carbohydrate Basics: Classifying Aldoses and Ketoses', '7:47'),
 '5L0AmyTCyi4': ('How to Draw Haworth Projections from Fischer Projections', '17:29'), 'xMjXa2mliZA': ('How to Draw a Haworth Projection (Ketose Edition)', '7:39'),
 'fBVx-i_Ehmc': ('Tips and Tricks for Converting Haworth to Fischer Projections', '—'), 'pwyW-X99GI8': ('Oxidation and Reduction of Carbohydrates', '10:44'),
 'BQwU9Z7myeg': ('Lipids: Formation of Triacylglycerides', '5:14'), 'Heg74N-mZms': ('Lipids: Hydrolysis of Triacylglycerides', '4:50'),
 'gO3YPk_2lTE': ('Lipids: Saponification of Triacylglycerides', '5:25'), 'M7VkdbGkPXY': ('Lipids: Hydrogenation of Unsaturated Fats', '6:12'),
 'Y_bXmJDoANI': ('Drawing Zwitterions and Amino Acids Made Simple', '14:34'), 'ec1npXqFdDM': ('Understanding Protein Structure', '23:39'),
 'IsypcIC7XqA': ('Introduction to Oxidation and Reduction Reactions: LEO goes GER', '—'), 'T8Uxtqoi1-8': ('Conjugate Acid-Base Pairs', '—'),
 '_3MEHX5yvzQ': ('Properties of Acids and Bases', '—'), 'M5gCzKjb0kA': ('Introduction to the pH Scale', '—'),
}
R = {
 1: [(r'formal charge', '-WH0D2cWcJc'), (r'molar mass|g mol', 'mvdjSfWFdaU'), (r'lewis|lone pair|valence electron|octet', 'CGmbd2YwflY'),
     (r'angle|shape|tetrahedral|trigonal|bent|linear|pyramidal|vsepr|geometry', 'wD3b-7J0Xy0'),
     (r'electronegativ|polar bond|δ\+|bond dipole', 'Wz23sE4KUBE'), (r'nonpolar|polar molecule|dipole moment|polar overall|most polar', '0fzuzHnkPAc'),
     (r'dispersion|london', 'vf1I8M32OXQ'), (r'boiling|melting|soluble|solubility|viscos', 'lAcgVwEmjM8'),
     (r'hydrogen bond|hydrogen-bond|intermolecular|dipole', 'CdA3Ov94lw0'), (r'acid|base|proton', '_3MEHX5yvzQ'),
     (r'ionic|covalent', 'u_Y1sC58C7M'), (r'functional group|organic|skeletal|condensed|line structure|expanded', 'gSKpPWYVnTU')],
 2: [(r'propyl|butyl|isopropyl|sec-|tert-|isobutyl', 'OxLTA0CZrd4'), (r'name|iupac', '9lxWINhQtUc'), (r'isomer', 'kEkvxf6e-Ro'),
     (r'boiling|melting|soluble|dispersion', 'vf1I8M32OXQ'), (r'condensed|skeletal|line|structural formula|organic|alkane', 'gSKpPWYVnTU')],
 3: [(r'cis|trans|geometric', 'JutTTWvB2wQ'), (r'markovnikov|major product|hbr|hcl|h2o|hydration|hydrogenation|br2|cl2|halogen|addition|reacts with', 'Dcun-l5jM9w')],
 4: [(r'dehydrat|zaitsev|h2so4.*heat|alkene', 'l3Sb_GWBano'), (r'oxidi|\[o\]|k2cr2o7|kmno4', 'veiUgkx_Dlc'), (r'ether', 'nN-RMEEbjLI')],
 5: [(r'cyclic|ring form', 'whVLjQhx3FI'), (r'hemiacetal|acetal|hemiketal|ketal', '1KPqZ2pp9bg'), (r'reduc|nabh4|h2, ni|hydrogenat', 'K0oEXP7JBZU'),
     (r'how many chiral|chiral carbon|stereocent', '4Z7_TvNmeR4'), (r'chiral|enantiomer|diastereomer|stereoisomer|meso|mirror', 'RudBXy5lTuU'),
     (r'oxidi|tollens|benedict', 'veiUgkx_Dlc')],
 6: [(r'hydroly|saponif|naoh.*ester|soap', 'vfSSUIcgzTY'), (r'esterif|ester|alcohol and .*acid|acid and .*alcohol', '2pwJ5G0uOtA'),
     (r'conjugate|ioniz|acid|base|neutraliz', 'T8Uxtqoi1-8')],
 7: [(r'hydroly', 'HU4KHyptdVA'), (r'base|acid|ammonium|protonat', '_3MEHX5yvzQ')],
 8: [(r'fructose|ketose.*ring|furanose', 'xMjXa2mliZA'), (r'haworth|ring form|cyclic|anomer|α|β|alpha|beta|pyranose', '5L0AmyTCyi4'),
     (r'fischer|\bd-|\bl-|d or l|chiral', 'fBVx-i_Ehmc'), (r'reducing sugar|oxidi|reduc|benedict|tollens|sugar alcohol|sorbitol|acid', 'pwyW-X99GI8'),
     (r'hemiacetal|acetal|glycosid', '1KPqZ2pp9bg'), (r'aldose|ketose|triose|tetrose|pentose|hexose|classif', '417CUTR3H1E')],
 9: [(r'saponif|soap|naoh|koh', 'gO3YPk_2lTE'), (r'hydrogenat|h2|partially', 'M7VkdbGkPXY'), (r'hydroly|lipase', 'Heg74N-mZms'),
     (r'triacylglycerol|triglyceride|glycerol|ester bond', 'BQwU9Z7myeg')],
 10: [(r'zwitterion|pi\b|isoelectric|charge|ph |ph\b|electrode', 'Y_bXmJDoANI'),
      (r'primary|secondary|tertiary|quaternary|helix|sheet|structure|fold|denatur|disulfide', 'ec1npXqFdDM')],
 11: [(r'nad|fad|oxidi|reduc', 'IsypcIC7XqA')],
 13: [(r'oxidi|reduc|nad|fad', 'IsypcIC7XqA')], 14: [(r'oxidi|reduc|nad|fad', 'IsypcIC7XqA')], 15: [(r'oxidi|reduc|nad|fad', 'IsypcIC7XqA')],
}
def plain(s): return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html.unescape(str(s)))).lower()

def build(ch_of):
    """ch_of: {bank id: chapter}"""
    B = {x['id']: x for f in glob.glob(os.path.join(ROOT, 'bank', '*.json')) for x in json.load(open(f))}
    import adapt_thin as T
    for x in T.NEW13: B[x['id']] = x
    out = {}
    for i, ch in ch_of.items():
        x = B.get(i)
        if not x: continue
        text = plain(x['q']) + ' ' + plain(x.get('h', '')) + ' ' + plain(x.get('t', ''))
        for rx, vid in R.get(ch, []):
            if re.search(rx, text): out[i] = vid; break
    return out

def hint_html(vid):
    t, ln = VID[vid]; e = html.escape
    return (f'<p><strong>Need help? Watch Dr. Dan’s lesson:</strong> {e(t)}' + (f' ({ln})' if ln != '—' else '') + '</p>'
            f'<div style="max-width:560px"><div style="width:100%;height:0px;position:relative;padding-bottom:56.25%"><iframe src="https://www.youtube.com/embed/{vid}?rel=0" '
            f'title="{e(t)} (Dr. Dan, YouTube video)" frameborder="0" style="width:100%;height:100%;position:absolute;left:0;top:0" '
            f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="true"></iframe></div></div>'
            f'<p><small>Captions: use the CC button. Video not loading? <a href="https://www.youtube.com/watch?v={vid}" target="_blank" rel="noopener">Watch it on YouTube</a>.</small></p>')
