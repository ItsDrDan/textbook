"""List every SVG figure on the live pages with the size its labels would have on a 370 px phone screen.
Usage: python3 tools/phone_inventory.py [--json out.json]"""
import re, glob, os, json, sys, collections
PHONE = 354   # content width on an iPhone 17 in Safari (points)
loc = collections.defaultdict(list)
for f in glob.glob('figures/**/*.svg', recursive=True): loc[os.path.basename(f)].append(f)
def pick(name):
    c = loc.get(name, [])
    c.sort(key=lambda f: (('batchT' in f) * 2 + ('/print/' in f or '/phone/' in f or '/pathways/' in f or '/conceptmaps/' in f), os.path.getmtime(f)))
    return c[-1] if c else None
rows = []
for pf in sorted(glob.glob('pages/live/*.html')):
    t = open(pf, encoding='utf-8').read(); pid = os.path.basename(pf)[:-5]
    title = ''
    for m in re.finditer(r'<img\b[^>]*>', t):
        tag = m.group(0); s = re.search(r'src="([^"]+\.svg)[^"]*"', tag)
        if not s or 'fig-phone' in tag: continue
        name = s.group(1).split('/')[-1]; f = pick(name)
        if not f: rows.append({'page': pid, 'name': name, 'missing': True}); continue
        x = open(f, encoding='utf-8', errors='ignore').read()
        vb = re.search(r'viewBox="([-0-9.]+) ([-0-9.]+) ([0-9.]+) ([0-9.]+)"', x)
        if not vb: continue
        W, H = float(vb.group(3)), float(vb.group(4))
        dw = re.search(r'width[=:]"?\s*([0-9.]+)(px)?', tag); dw = float(dw.group(1)) if dw else W
        shown = min(PHONE, dw)
        fs = collections.Counter()
        for mm in re.finditer(r'<text[^>]*?font-size="([0-9.]+)"[^>]*>([^<]*)', x):
            if len(mm.group(2).strip()) > 3: fs[float(mm.group(1))] += 1
        if not fs: continue
        small = min(fs); common = fs.most_common(1)[0][0]
        k = shown / W
        rows.append({'page': pid, 'name': name, 'file': f, 'W': W, 'H': H, 'disp': dw, 'small_px': round(small * k, 1), 'common_px': round(common * k, 1), 'wide': 'fig-wide' in tag})
if '--json' in sys.argv: json.dump(rows, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=0)
bad = [r for r in rows if not r.get('missing') and r['common_px'] < 9]
print(len(rows), 'svg figures on live pages;', len(bad), 'have typical labels under 9 px on a phone;', sum(1 for r in rows if r.get('missing')), 'without a local copy')
for r in sorted(bad, key=lambda r: (r['page'], r['name'])): print(r['page'], r['name'].ljust(40), int(r['W']), 'x', int(r['H']), ' typical', r['common_px'], 'smallest', r['small_px'])
