"""Video hints (Dr. Dan's lessons, with a start time and jump links) for the ADAPT questions added on 2026-11-12.
Uses the per-chapter rules and video list in adapt_hint_videos.py and the chapter markers in video_moments.json.
python3 tools/adapt_hints_new_2026_11_12.py  ->  adapt/adapt_new_hints_2026-11-12.json  {bank id: hint html}"""
import json, re, html, os, sys, ast
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = open(os.path.join(ROOT, 'tools', 'adapt_hint_videos.py'), encoding='utf-8').read()
ns = {}
for node in ast.parse(src).body:   # VID, R and plain() only; do not run the module's build()
    if isinstance(node, (ast.Assign, ast.FunctionDef)) and (getattr(node, 'name', None) == 'plain' or any(getattr(t, 'id', '') in ('VID', 'R') for t in getattr(node, 'targets', []))):
        exec(compile(ast.Module([node], []), 'adapt_hint_videos', 'exec'), {'re': re, 'html': html}, ns)
VID, R, plain = ns['VID'], ns['R'], ns['plain']
MOM = json.load(open(os.path.join(ROOT, 'tools', 'video_moments.json')))
bank = {x['id']: x for f in os.listdir(os.path.join(ROOT, 'bank')) if f.endswith('.json') for x in json.load(open(os.path.join(ROOT, 'bank', f)))}
NEW = json.load(open(os.path.join(ROOT, 'adapt', 'adapt_new_ids_2026-11-12.json')))   # {id: chapter}
STOP = set('the a an of and or to in on for with is are be by as at from that this which what how why does do it its into than more most each your you'.split())
def words(s): return {w for w in re.findall(r'[a-z0-9]+', plain(s)) if w not in STOP and len(w) > 2}
def mmss(t): return f'{t // 60}:{t % 60:02d}'
def hint(vid, x):
    title, ln = VID[vid]; e = html.escape; moms = MOM.get(vid, [])
    qw = words(x['q'] + ' ' + x.get('h', '') + ' ' + str(x['c'][0]))
    best, score = None, 0
    for t, label in moms:
        s = len(qw & words(label))
        if s > score: best, score = (t, label), s
    start = best[0] if best and score >= 1 and best[0] > 0 else 0
    p = f'<p><strong>Need help? Watch Dr. Dan&rsquo;s lesson:</strong> {e(title)}' + (f' ({ln})' if ln != '—' else '')
    if start: p += f'<br>It starts at <strong>{mmss(start)}</strong>, the part about &ldquo;{e(best[1])}.&rdquo; Press play to begin there.'
    p += '</p>'
    q = f'?rel=0&amp;start={start}' if start else '?rel=0'
    out = p + (f'<div style="max-width:560px"><div style="width:100%;height:0px;position:relative;padding-bottom:56.25%"><iframe src="https://www.youtube.com/embed/{vid}{q}" '
               f'title="{e(title)} (Dr. Dan, YouTube video)" frameborder="0" style="width:100%;height:100%;position:absolute;left:0;top:0" '
               f'allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="true"></iframe></div></div>')
    if moms:
        out += '<p><small><strong>Jump to (opens YouTube):</strong> ' + ' &middot; '.join(
            f'<a href="https://www.youtube.com/watch?v={vid}&amp;t={t}s" target="_blank" rel="noopener">{mmss(t)} {e(l)}</a>' for t, l in moms) + '</small></p>'
    tt = f'&amp;t={start}s' if start else ''
    out += f'<p><small>Captions: use the CC button. Video not loading? <a href="https://www.youtube.com/watch?v={vid}{tt}" target="_blank" rel="noopener">Watch it on YouTube</a>.</small></p>'
    return out
# Reviewed by hand: these keyword matches pointed to the wrong lesson.
SKIP = {'fb-3B-2100', 'fb-3B-2101', 'fb-3B-0254', 'fb-3B-2075', 'fb-3B-2077'}
FORCE = {'fb-3B-2088': 'Heg74N-mZms'}   # rancid butter = ester hydrolysis
res = {}
for i, ch in NEW.items():
    if i in SKIP: continue
    if i in FORCE: res[i] = hint(FORCE[i], bank[i]); continue
    x = bank[i]; text = plain(x['q']) + ' ' + plain(x.get('h', '')) + ' ' + plain(x.get('t', ''))
    for rx, vid in R.get(int(ch), []):
        if re.search(rx, text): res[i] = hint(vid, x); break
json.dump(res, open(os.path.join(ROOT, 'adapt', 'adapt_new_hints_2026-11-12.json'), 'w'), ensure_ascii=False, indent=0)
print(len(res), 'of', len(NEW), 'new questions matched a lesson video')
