"""Batch D5 addendum: the 6.9 exercise box uses <h4> in the <header> form (the D5 pattern matched <h5> only).
Output: tools/batchD5b_fixes_2026-11-12.json"""
import json, re
p = '597117'; t = open(f'pages/live/{p}.html', encoding='utf-8').read()
BOX = re.compile(r'<section class="box-exercise">\s*<header>\s*(<span id="[^"]*"></span>)<div class="mt-section"><h(\d) class="editable">(.*?)</h\2>\s*</div></header>(.*?)</section>', re.S)
ms = list(BOX.finditer(t)); assert len(ms) == 1 and '<section' not in ms[0].group(4)
m = ms[0]
new = f'<section class="box-exercise">\n{m.group(1)}<div class="mt-section"><h{m.group(2)} class="box-legend editable">{m.group(3)}</h{m.group(2)}>{m.group(4)}</div></section>'
assert t.count(m.group(0)) == 1
json.dump({p: [{'old': m.group(0), 'new': new, 'count': 1, 'note': f'exercise box heading form ({m.group(3)})'}]},
          open('tools/batchD5b_fixes_2026-11-12.json', 'w'), ensure_ascii=False, indent=1)
print('ok')
