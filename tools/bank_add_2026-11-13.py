"""Bank update of 2026-11-13 (batch R).
1. Every item gets "sec": the first section that teaches what it asks (tools/bank_sec_tags_2026-11-13.json, from the
   Try It alignment review). The widget's &chmax=N option uses it to keep cumulative mixes inside Chapters 1..N.
2. New questions for the three gaps the review found (audit/edits/r_bank.json): Lewis structures (1.3),
   alkene and alkyne naming (3.1), ketone bodies (15.5). Ids start at fb-3B-2238 (2126-2237 are reserved for the
   IMF deck candidates). Idempotent: running it twice changes nothing.
Usage: python3 tools/bank_add_2026-11-13.py"""
import json, os

SEC = json.load(open('tools/bank_sec_tags_2026-11-13.json'))
NEW = json.load(open('audit/edits/r_bank.json', encoding='utf-8')) if os.path.exists('audit/edits/r_bank.json') else {}
GROUPS = (('lewis', 'structure', '1.3'), ('alkene_naming', 'hydrocarbons', '3.1'), ('ketone_bodies', 'metabolism', '15.5'))
dump = lambda d: json.dumps(d, ensure_ascii=False, separators=(',', ':'))
files = {t: json.load(open(f'bank/{t}.json', encoding='utf-8')) for t in sorted(f[:-5] for f in os.listdir('bank') if f.endswith('.json'))}
have = {q['q'] for d in files.values() for q in d}
nid = max([2237] + [int(q['id'].split('-')[2]) for d in files.values() for q in d])
added = {}
for key, topic, sec in GROUPS:
    for q in NEW.get(key, []):
        if q.get('skip') or q['q'] in have: continue
        assert q['t'] == topic and len(q['c']) == 4 and len(set(q['c'])) == 4 and len(q['x']) == 4 and q['x'][0] is None, q['q'][:50]
        nid += 1
        item = {'t': topic, 'q': q['q'], 'c': q['c'], 'h': q['h'], 'w': q['w'], 'k': 0, 'd': int(q.get('d', 2)), 'id': 'fb-3B-%04d' % nid, 'x': q['x'], 'sec': sec}
        files[topic].append(item); have.add(q['q']); added.setdefault(key, []).append(item['id'])
n = 0
for t, d in files.items():
    for q in d:
        if 'sec' not in q:
            q['sec'] = SEC[q['id']]; n += 1
    open(f'bank/{t}.json', 'w', encoding='utf-8').write(dump(d))
print('sec added to', n, 'items; new questions:', {k: v for k, v in added.items()})
json.dump(added, open('tools/bank_new_ids_2026-11-13.json', 'w'), indent=1) if added else None
