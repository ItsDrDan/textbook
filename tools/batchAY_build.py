"""Batch AY (2026-11-20): name the faculty-review copy version 1.3.
LibreTexts: title page and About This Book. The November 20 history entry takes the same label style as the 1.2 entry.
Repo (goes live on merge): index.html landing page, review/03_OER_LISTING.md checklist."""
import json, hashlib
pages, E, order = {}, {}, []


def e(p, old, new, note):
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == 1, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    E.setdefault(p, []).append({'old': old, 'new': new, 'count': 1, 'note': note})


e('488226', 'Version 1.2, November 2026', 'Version 1.3, November 2026', 'Title page version')
e('597270', '<strong>Version 1.2, November 2026</strong>', '<strong>Version 1.3, November 2026</strong>', 'About: top version line')
e('597270', 'This is version 1.2.', 'This is version 1.3.', 'About: Reviews section')
e('597270', '<strong>Update (November 20, 2026).</strong>', '<strong>1.3 (November 20, 2026).</strong>', 'About: history label')
for f, old, new in [('index.html', 'Version 1.2, November 2026', 'Version 1.3, November 2026'),
                    ('review/03_OER_LISTING.md', '- [ ] Version number decided', '- [x] Version number decided')]:
    t = open(f, encoding='utf-8').read()
    if new not in t:
        assert t.count(old) == 1, f
        open(f, 'w', encoding='utf-8').write(t.replace(old, new))
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AY', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAY_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAY_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
print(json.dumps(sha))
