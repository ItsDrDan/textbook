"""Bank update of 2026-11-13 (batch T): 60 text-only questions for the twelve thin sections
(2.3, 2.5, 4.2, 4.9, 6.1, 6.5, 8.5, 8.7, 10.1, 13.3, 15.3, 15.9), five each, from audit/edits/t_bank.json.
Every key was solved by the writer and read again in review. Ids continue after the highest id in the bank.
Idempotent: a stem already in the bank is skipped.  Usage: python3 tools/bank_add_thin_2026-11-13.py"""
import json, os
NEW = json.load(open('audit/edits/t_bank.json', encoding='utf-8'))
dump = lambda d: json.dumps(d, ensure_ascii=False, separators=(',', ':'))
files = {f[:-5]: json.load(open('bank/' + f, encoding='utf-8')) for f in sorted(os.listdir('bank')) if f.endswith('.json')}
have = {q['q'] for d in files.values() for q in d}
nid = max(int(q['id'].split('-')[2]) for d in files.values() for q in d)
added = {}
for q in NEW['organic'] + NEW['bio']:
    if q['q'] in have: continue
    assert q['t'] in files and len(q['c']) == 4 and len(set(q['c'])) == 4 and len(q['x']) == 4 and q['x'][0] is None and q.get('sec'), q['q'][:50]
    nid += 1
    files[q['t']].append({'t': q['t'], 'q': q['q'], 'c': q['c'], 'h': q['h'], 'w': q['w'], 'k': 0, 'd': int(q.get('d', 2)), 'id': 'fb-3B-%04d' % nid, 'x': q['x'], 'sec': q['sec']})
    have.add(q['q']); added.setdefault(q['sec'], []).append('fb-3B-%04d' % nid)
for t, d in files.items(): open(f'bank/{t}.json', 'w', encoding='utf-8').write(dump(d))
print('added', sum(len(v) for v in added.values()), added)
if added: json.dump(added, open('tools/bank_new_ids_thin_2026-11-13.json', 'w'), indent=1)
