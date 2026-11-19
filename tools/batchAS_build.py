"""Batch AS (2026-11-19): 14.4 Wikipedia credit corrected (found in the Full (32).pdf check after batch AR).
The sentence said the equations and figures were "taken from the public domain source via Wikipedia". The section text is
already the book's own wording (Malik CC0 base, edited), the overall equations are standard facts, and the Complex I, II and IV
diagrams are Wikimedia Commons files File:Complex_I.svg, File:Complex_II.svg, File:Complex_IV.svg by Fvasconcellos, each marked
public domain on Commons (checked 2026-11-19 with the Commons API; the book's PNGs have the same aspect ratios:
366x310 vs 500x426, 242x239 vs 500x493, 221x252 vs 500x569). So the credit names the real source and license.
Output: tools/batchAS_2026-11-19.json, tools/batchAS_sha_2026-11-19.json, audit/preview/<id>.html
Run from the repo root: python3 tools/batchAS_build.py"""
import json, hashlib

pages, edits, order = {}, {}, []


def e(p, old, new, note, why, count=1):
    p = str(p)
    if p not in pages:
        pages[p] = [open('pages/live/%s.html' % p, encoding='utf-8').read()] * 2
        order.append(p)
    t = pages[p][1]
    assert t.count(old) == count, (p, note, t.count(old))
    pages[p][1] = t.replace(old, new)
    edits.setdefault(p, []).append({'old': old, 'new': new, 'count': count, 'note': note, 'why': why})


L = lambda f, n: '<a style="text-decoration:underline" href="https://commons.wikimedia.org/wiki/File:%s" rel="noopener" target="_blank">%s</a>' % (f, n)

e('597203',
  'are described in the following sub-sections, where the chemical equations and figures are taken from the public domain source via Wikipedia.</p>',
  'are described in the following sub-sections. (Diagrams of ' + L('Complex_I.svg', 'Complex I') + ', ' + L('Complex_II.svg', 'Complex II')
  + ' and ' + L('Complex_IV.svg', 'Complex IV') + ': Fvasconcellos, public domain, via Wikimedia Commons.)</p>',
  '14.4: Wikipedia credit corrected to the actual Commons figures',
  'The old sentence called Wikipedia a "public domain source"; Wikipedia text is CC BY-SA 4.0. The section text is the book\'s own '
  'edited wording and the equations are standard facts, so only the three figures need credit: Commons files by Fvasconcellos, '
  'public domain (Commons API, 2026-11-19). Same fix as 13.5 and 14.3 in batch AR.')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAS_2026-11-19.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAS_sha_2026-11-19.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
