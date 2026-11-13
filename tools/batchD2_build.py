"""Batch D2 (review 2026-11-12): ten plain YouTube iframes -> the house aspect-ratio wrapper used by the other 64
videos (tools/videos.py), with real titles; credits added where missing (BioMan Biology on 13.4, 13.5, 14.3).
Titles/channels from YouTube oEmbed. Output: tools/batchD2_videos_2026-11-12.json"""
import json, re
L = 'pages/live/'
V = {  # id: (title, channel)
 'RNQKJ1hnHes': ('Basic Concepts behind Intermolecular Forces', 'Daniel Kwasniewski (ItsDrDan)'),
 'gSKpPWYVnTU': ('Organic Chemistry: An Introduction (Part 1)', 'Daniel Kwasniewski (ItsDrDan)'),
 'xbsGe976lZ4': ('Organic Chemistry: An Introduction (Part 2)', 'Daniel Kwasniewski (ItsDrDan)'),
 'ckrRl0L3sr4': ('Fischer to Haworth Projections using Mannose', 'Daniel Kwasniewski (ItsDrDan)'),
 'fBVx-i_Ehmc': ('Tips and Tricks for Converting Haworth to Fischer Projections', 'Daniel Kwasniewski (ItsDrDan)'),
 '78YEo1BlhuM': ('The Link Reaction Explained (Aerobic Respiration)', 'BioMan Biology'),
 '7V2kRH0K8QU': ('Glycolysis (and Exploding Sugar Demo!)', 'BioMan Biology'),
 'UZlmm-yzWrQ': ('The Krebs Cycle Explained (Aerobic Respiration)', 'BioMan Biology'),
 '2QllhjZWnnw': ('Beta oxidation', 'Biotech Review'),
 'D--AtATgfyM': ('Obesity: The Little Things', 'NHLBI'),
}
ALLOW = 'accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture'
def wrap(vid):
    t, ch = V[vid]; tt = t.replace("'", '&rsquo;')
    return (f'<div style="max-width:640px"><div style="width:100%;position:relative;aspect-ratio:16/9"><iframe src="https://www.youtube.com/embed/{vid}?rel=0" '
            f'title="{tt} ({ch}, YouTube video)" frameborder="0" style="width:100%;height:100%;position:absolute;left:0;top:0" allow="{ALLOW}" allowfullscreen="true"></iframe></div></div>')
edits = {}
def e(p, old, new, note):
    t = open(L + p + '.html').read(); assert t.count(old) == 1, (p, note, t.count(old))
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})
for p in ('597062', '597074', '597141'):
    t = open(L + p + '.html').read()
    for m in re.finditer(r'<p><iframe width="560" height="315" src="https://www\.youtube\.com/embed/([\w-]+)"[^>]*></iframe></p>', t):
        e(p, m.group(0), wrap(m.group(1)), f'guide video {m.group(1)} -> wrapper')
    # credit on the title lines
    for vid, (title, ch) in V.items():
        for old in (f'<p><strong>{title}</strong></p>',):
            if old in t: e(p, old, f'<p><strong>{title}</strong> (Daniel Kwasniewski (ItsDrDan))</p>', 'add credit')
        m = re.search(r'<p><strong>' + re.escape(title) + r'</strong> \((\d+:\d+)\)</p>', t)
        if m: e(p, m.group(0), f'<p><strong>{title}</strong> ({m.group(1)}, Daniel Kwasniewski (ItsDrDan))</p>', 'add credit')
CREDIT = {'597192': '78YEo1BlhuM', '597193': '7V2kRH0K8QU', '597202': 'UZlmm-yzWrQ'}
for p in ('597192', '597193', '597202', '597209'):
    t = open(L + p + '.html').read()
    for m in re.finditer(r'<div class="mt-video-widget mt-video-width-55"><iframe[^>]*src="https://www\.youtube\.com/embed/([\w-]+)"[^>]*></iframe></div>', t):
        vid = m.group(1); new = wrap(vid)
        if CREDIT.get(p) == vid:
            ttl, ch = V[vid]
            new += f'<p><small>Video: &ldquo;{ttl}&rdquo; ({ch} on YouTube, embedded by link; not covered by this book&rsquo;s license).</small></p>'
        e(p, m.group(0), new, f'widget video {vid} -> wrapper' + (' + credit' if CREDIT.get(p) == vid else ''))
json.dump(edits, open('tools/batchD2_videos_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
for p, es in edits.items():
    for x in es: print(p, x['note'])
print(sum(len(v) for v in edits.values()), 'edits')
