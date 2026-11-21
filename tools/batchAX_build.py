"""Batch AX (2026-11-20): equilibrium arrows in two Hands-on Lab boxes.
Full (39).pdf printed the plain-text arrow (&#8652;, added in batch AV) as a diamond in 6.10 and 10.9 because the PDF font
lacks it. Both now use the book's standard math arrow, \\(\\rightleftharpoons\\)."""
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


A = r'\(\rightleftharpoons\)'
e('597118', 'H<sub>2</sub>O &#8652; H<sup>+</sup>', 'H<sub>2</sub>O ' + A + ' H<sup>+</sup>', '6.10 lab box: math equilibrium arrow')
e('597162', 'O<sub>2</sub> &#8652; HbO<sub>2</sub>', 'O<sub>2</sub> ' + A + ' HbO<sub>2</sub>', '10.9 lab box: math equilibrium arrow')
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'batch': 'AX', 'date': '2026-11-20', 'uploads': [], 'edits': E}, open('tools/batchAX_2026-11-20.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAX_sha_2026-11-20.json', 'w'))
print(sum(len(v) for v in E.values()), 'edits on', len(E), 'pages')
print(json.dumps(sha))
