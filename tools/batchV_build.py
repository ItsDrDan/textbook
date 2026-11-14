"""Batch V (2026-11-13): labels the 19:32 PDF still printed under 6 pt.
  12.5 tRNA cloverleaf (file 512603, page 597183) and 12.6 elongation cycle (file 512767, page 597179): re-upload
  14.4 rotor steps (GitHub figure atp_rotation.svg): cache-bust on page 597203
  14.3 (page 597202): tag author@Muhammad Arif Malik added so the print footer cannot come out blank
Output: tools/batchV_2026-11-13.json, tools/batchV_sha_2026-11-13.json, audit/preview/597203.html"""
import json, hashlib
p = '597203'; t = open('pages/live/%s.html' % p, encoding='utf-8').read()
old = 'figures/pathways/oer/atp_rotation.svg"'; new = 'figures/pathways/oer/atp_rotation.svg?v=20261113v"'
assert t.count(old) == 1
n = t.replace(old, new)
h = lambda s: hashlib.sha256(s.encode()).hexdigest()
json.dump({'uploads': [{'file': 'figures/pages/batchT/fig-p597183-2.svg', 'fileid': 512603, 'owner': 597183},
                       {'file': 'figures/pages/batchT/fig-p597179-elongation.svg', 'fileid': 512767, 'owner': 597179}],
           'tags': {'597202': {'add': ['author@Muhammad Arif Malik']}},
           'edits': {p: [{'old': old, 'new': new, 'count': 1, 'note': '14.4 rotor figure: cache-bust for enlarged H+ and c labels'}]}},
          open('tools/batchV_2026-11-13.json', 'w'), indent=1)
json.dump({p: {'before': h(t), 'after': h(n)}}, open('tools/batchV_sha_2026-11-13.json', 'w'))
open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(n)
print('1 edit, 2 uploads, 1 tag')
