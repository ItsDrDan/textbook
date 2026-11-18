"""Batch AO (2026-11-18): lab manual authorship and title in the front matter.
The manual (chem3b-lab-manual main 1322dc2) now lists Alexandra Aloia first and is titled "CHEM 3B Laboratory Manual".
Pages: book home 488223, About 597270, Course Outline Alignment 597272, For Instructors 597396.
Output: tools/batchAO_2026-11-18.json, tools/batchAO_sha_2026-11-18.json, audit/preview/<id>.html"""
import json, hashlib
REPL = [('Daniel Kwasniewski and Alexandra Aloia', 'Alexandra Aloia and Daniel Kwasniewski'),
        ('CHEM 3B Lab Manual', 'CHEM 3B Laboratory Manual')]
h = lambda x: hashlib.sha256(x.encode()).hexdigest()
edits, sha = {}, {}
for p in ['488223', '597270', '597272', '597396']:
    t0 = t = open('pages/live/%s.html' % p, encoding='utf-8').read()
    for old, new in REPL:
        n = t.count(old)
        if n:
            edits.setdefault(p, []).append({'old': old, 'new': new, 'count': n, 'note': 'manual author order / title', 'why': 'Author decision 2026-11-18: Alexandra Aloia is first author; manual title is CHEM 3B Laboratory Manual.'})
            t = t.replace(old, new)
    assert 'Daniel Kwasniewski and Alexandra Aloia' not in t
    sha[p] = {'before': h(t0), 'after': h(t)}
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(t)
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAO_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAO_sha_2026-11-18.json', 'w'))
print({p: [(e['old'][:20], e['count']) for e in es] for p, es in edits.items()})
