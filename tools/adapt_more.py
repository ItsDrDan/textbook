"""Extra ADAPT homework for Chapters 1-15: Try It bank questions that need drawn structures or figures.
Each drawing becomes a PNG with written alt text (tools/struct_alt.py; hand-written text in adapt_thin.ALT wins).
Chapters 3, 13 and 15 already got their first extra sets from tools/adapt_thin.py; this adds the rest.
Usage: python3 tools/adapt_more.py ids  -> writes <imgdir>/ids.json (all chapters)
       node tools/render_thin.js <imgdir>/ids.json <imgdir>
       python3 tools/adapt_more.py build <imgdir>  -> adapt/CHEM3B_ChNN_more_QTI.zip
In the Try It bank the correct answer is ALWAYS c[0]."""
import json, os, sys, glob, re, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import struct_alt as S

# questions the topic regexes in adapt_export did not place, assigned by hand
HAND = {1: ['fb-3B-0635', 'fb-3B-0636', 'fb-3B-0642', 'fb-3B-0643'] + [f'fb-3B-0{n}' for n in range(535, 555)] + [f'fb-3B-0{n}' for n in range(581, 589)],
        2: ['fb-3B-0019', 'fb-3B-0621', 'fb-3B-0918'],
        3: ['fb-3B-0573', 'fb-3B-0574', 'fb-3B-0578', 'fb-3B-0354', 'fb-3B-0498', 'fb-3B-0499', 'fb-3B-0500', 'fb-3B-0501', 'fb-3B-0502', 'fb-3B-0503',
            'fb-3B-0504', 'fb-3B-0655', 'fb-3B-0656', 'fb-3B-0657', 'fb-3B-0658', 'fb-3B-0660', 'fb-3B-0661', 'fb-3B-0662', 'fb-3B-0664', 'fb-3B-0665',
            'fb-3B-0666', 'fb-3B-0667', 'fb-3B-0668', 'fb-3B-0717'],
        4: ['fb-3B-0527', 'fb-3B-0640'],
        5: ['fb-3B-0900'],
        6: ['fb-3B-0904', 'fb-3B-0908'],
        7: ['fb-3B-0231', 'fb-3B-0528', 'fb-3B-0896', 'fb-3B-0897', 'fb-3B-0898']}
# Chapter 3 extra-set questions whose drawn choices were imported unshuffled (right answer always "Structure A");
# they are re-imported here with a shuffled grid and replace the old copies in the Chapter 3 assignment
RESHUFFLE = {3: ['fb-3B-0497', 'fb-3B-0659', 'fb-3B-0663', 'fb-3B-0914', 'fb-3B-0915', 'fb-3B-0916', 'fb-3B-0525', 'fb-3B-0526',
                 'fb-3B-0715', 'fb-3B-0716', 'fb-3B-0718', 'fb-3B-0719', 'fb-3B-0919', 'fb-3B-0920']}
REST = os.path.join(ROOT, 'adapt', 'more_by_chapter.json')   # chapter -> ids placed by the adapt_export topic regexes

def bank():
    return {x['id']: x for f in glob.glob(os.path.join(ROOT, 'bank', '*.json')) for x in json.load(open(f))}

def chapters():
    rest = json.load(open(REST))
    out = {}
    for ch in range(1, 16):
        ids = list(rest.get(str(ch), [])) + [i for i in HAND.get(ch, []) + RESHUFFLE.get(ch, []) if i not in rest.get(str(ch), [])]
        out[ch] = ids
    seen = {}
    for ch, ids in out.items():
        for i in ids:
            assert i not in seen, (i, ch, seen[i])
            seen[i] = ch
    return out

def alt_for(x, key):
    import adapt_thin as T
    k = f"{x['id']}_{key}"
    if k in T.ALT and key != 'cs': return T.ALT[k]   # the old hand-written choice text assumed the unshuffled order
    if key == 's': return S.describe_struct(x['s'])
    if key == 'cs':
        P = T.cs_perm(x)
        return S.describe_choices([x['cs'][j] for j in P])
    if key == 'f':
        def tab(f):
            if f.get('type') == 'table':
                return 'Table with columns ' + ', '.join(S.plain(h) for h in f['head'] if S.plain(h)) + '. Rows: ' + '; '.join(', '.join(S.plain(c) for c in r) for r in f['rows']) + '.'
            if f.get('type') == 'eq': return 'Equation: ' + S.plain(f['text'].replace('<br>', '; ')) + '.'
        parts = [S.describe_fig(f) or tab(f) for f in x['f'] if isinstance(f, dict)]
        return ' '.join(p for p in parts if p)
    raise KeyError(key)

if __name__ == '__main__':
    B = bank(); CH = chapters()
    if sys.argv[1] == 'ids':
        d = sys.argv[2]; os.makedirs(d, exist_ok=True)
        ids = [i for ch in CH for i in CH[ch]]
        assert all(i in B for i in ids), [i for i in ids if i not in B]
        import adapt_thin as T
        json.dump([{'id': i, 'perm': T.cs_perm(B[i])} if B[i].get('cs') else i for i in ids], open(os.path.join(d, 'ids.json'), 'w'))
        print({ch: len(v) for ch, v in CH.items()}, len(ids))
    elif sys.argv[1] in ('build', 'alts'):
        IMG = sys.argv[2]
        import adapt_thin as T
        T.IMG = IMG
        meta = json.load(open(os.path.join(IMG, 'meta.json')))
        alts = {}
        for ch, ids in CH.items():
            for i in ids:
                for key in ('s', 'f', 'cs'):
                    if meta.get(i, {}).get(key):
                        a = alt_for(B[i], key)
                        assert a and len(a) > 20, (i, key, a)
                        alts[f'{i}_{key}'] = a
        json.dump(alts, open(os.path.join(IMG, 'alts.json'), 'w'), ensure_ascii=False, indent=0)
        if sys.argv[1] == 'alts':
            print(len(alts), 'alt texts'); sys.exit()
        T.ALT = alts
        for ch, ids in CH.items():
            if not ids: continue
            print(ch, T.build(f'CHEM3B_Ch{ch:02d}_more_QTI', f'CHEM 3B Chapter {ch} more questions', [B[i] for i in ids], meta))
