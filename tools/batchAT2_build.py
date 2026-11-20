"""Batch AT2 (2026-11-20): follow-up from the post-publish rescan of batch AT.
1. landmark-unique (axe best practice): pages with several wide figures had several regions all named "Wide figure: scroll
   sideways". Each region is now named after its own figure ("Scroll sideways: " + the start of the image's alt text).
2. scrollable-region-focusable: 32 side-scrolling figure boxes are <span class="fig-scroll"> (13.4, 13.5, 14.2, 14.3, 15.4, 15.8),
   which batch AT (div only) missed; and the 3.7 bromination reaction row (<div style="text-align:center;overflow-x:auto">).
Output: tools/batchAT2_2026-11-20.json, tools/batchAT2_sha_2026-11-20.json, audit/preview/<id>.html"""
import json, hashlib, re, os, html

pages, E, order = {}, {}, []


def e(p, old, new, note, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old), old[:120])
    pages[p][1] = t.replace(old, new)
    E.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note})


def label(alt):
    a = html.unescape(alt or '').strip().rstrip('.')
    words = a.split()
    s = ' '.join(words[:9]) + ('…' if len(words) > 9 else '')
    return html.escape('Scroll sideways: ' + (s or 'wide figure'), quote=True)


DIVTAG = '<div class="fig-scroll" tabindex="0" role="region" aria-label="Wide figure: scroll sideways">'
for f in sorted(os.listdir('pages/live')):
    p = f[:-5]
    t = open('pages/live/' + f, encoding='utf-8').read()
    seen = {}
    for tag, kind in [(DIVTAG, 'div'), ('<span class="fig-scroll">', 'span')]:
        for m in re.finditer(re.escape(tag), t):
            # the old string runs from the tag to the end of the first src="..." after it (unique per figure)
            sm = re.search(r'src="[^"]*"', t[m.end():])
            old = t[m.start(): m.end() + sm.end()]
            if t.count(old) != 1:
                continue
            alt = re.search(r'alt="([^"]*)"', t[m.end(): m.end() + sm.end() + 2000])
            lab = label(alt.group(1) if alt else '')
            seen[lab] = seen.get(lab, 0) + 1
            if seen[lab] > 1:
                lab += ' (%d)' % seen[lab]
            newtag = '<%s class="fig-scroll" tabindex="0" role="region" aria-label="%s">' % (kind, lab)
            e(p, old, newtag + old[len(tag):], 'side-scrolling figure box: focusable, named after its figure')
    t2 = pages.get(p, [t, t])[1]
    left = t2.count(DIVTAG) + t2.count('<span class="fig-scroll">')
    assert left == 0, (p, 'unconverted fig-scroll', left)

e('597084', '<div style="text-align:center;overflow-x:auto">',
  '<div style="text-align:center;overflow-x:auto" tabindex="0" role="region" aria-label="Scroll sideways: bromination of benzene, benzene to bromobenzene">',
  '3.7: bromination reaction row is a focusable, named region')

# labels must be unique on each page
for p in order:
    labs = re.findall(r'role="region" aria-label="([^"]*)"', pages[p][1])
    assert len(labs) == len(set(labs)), (p, 'duplicate region labels')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AT2', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAT2_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAT2_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
