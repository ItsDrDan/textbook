"""Batch AN (2026-11-18): author decisions on batch AM.
1. Pentyl acetate smells like pear (the book's convention); 6.6 box follows it (manual Exp 6 to be changed to match).
2. Digestion of foods = the HCl hydrolysis of starch and sucrose in Experiment 8 Part E (plus the amylase work in Exp 13):
   13.3 box, Course Outline Alignment table/sentence, For Instructors.
3. Keep the chromate test in 4.5 (common oxidizing agent); say why the lab uses the Lucas test (safety).
Output: tools/batchAN_2026-11-18.json, tools/batchAN_sha_2026-11-18.json, audit/preview/<id>.html
Run from the repo root: python3 tools/batchAN_build.py"""
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


PDF = 'https://itsdrdan.github.io/chem3b-lab-manual/pdf/experiments/'
A = lambda f, t: '<a href="%s%s" target="_blank" rel="noopener">%s (PDF)</a>' % (PDF, f, t)

e('597114', 'propyl acetate (pear), pentyl acetate (banana), octyl acetate (orange)',
  'propyl acetate and pentyl acetate (both pear; the banana ester is isopentyl acetate, its branched isomer), octyl acetate (orange)',
  '6.6 In the Lab: pentyl acetate = pear', 'Author decision 2026-11-18: keep the book\'s pear (6.5 tip, 6.6 table, 6.11 Example 2); the manual changes to match.')

e('597094', 'the 3&deg; alcohol that chromate cannot oxidize reacts fastest with the Lucas reagent.</p>',
  'the 3&deg; alcohol that chromate cannot oxidize reacts fastest with the Lucas reagent.</p>\n'
  '<p>Why the switch? Chromium(VI) compounds are toxic and cause cancer, and their waste needs special handling, so the teaching '
  'lab avoids them. Dichromate is still one of the most common oxidizing agents in chemistry, so know the chromate test and its '
  'orange-to-green color change for exams.</p>',
  '4.5 In the Lab: why the lab uses Lucas instead of chromate', 'Author decision 2026-11-18: keep the chromate chemistry; the lab dropped it only for safety.')

OLD133 = ('<p><strong>Digestion of starch:</strong> in <strong>Experiment 13 &ndash; Enzymes</strong> you mix starch with amylase')
NEW133 = ('<p><strong>Digestion of starch and sucrose:</strong> in <strong>Experiment 8 &ndash; Tests for Carbohydrates</strong> (Part E) '
          'you model digestion by heating starch and sucrose with dilute HCl. The acid hydrolyzes the glycosidic bonds, just as '
          'digestive enzymes do: the iodine test shows the starch is gone, and Benedict&rsquo;s test turns positive because '
          'reducing sugars (glucose, and fructose from sucrose) appear. The tubes heated with water alone do not change.</p>\n'
          '<p>In <strong>Experiment 13 &ndash; Enzymes</strong> you mix starch with amylase')
e('597191', OLD133, NEW133, '13.3 In the Lab: digestion modeled by Exp 8 Part E acid hydrolysis',
  'Author decision 2026-11-18: the digestion-of-foods lab topic is the HCl hydrolysis in the carbohydrates lab (exp08.js E.1-E.4).')
e('597191', '<p style="font-size:0.95em;"><strong>Lab manual:</strong> ' + A('Exp13_Enzymes.pdf', 'Experiment 13 &ndash; Enzymes') + '</p>',
  '<p style="font-size:0.95em;"><strong>Lab manual:</strong> ' + A('Exp08_TestsForCarbohydrates.pdf', 'Experiment 8 &ndash; Tests for Carbohydrates')
  + '; ' + A('Exp13_Enzymes.pdf', 'Experiment 13 &ndash; Enzymes') + '</p>',
  '13.3 In the Lab: link Exp 8 too', 'Same.')

e('597272', '<a href="/@go/page/597138">8.5</a>, <a href="/@go/page/597140">8.7</a>',
  '<a href="/@go/page/597138">8.5</a>, <a href="/@go/page/597140">8.7</a>, <a href="/@go/page/597191">13.3</a>',
  'Course Outline Alignment table: Exp 8 also 13.3', 'Same.')
e('597272', '<p>Two outline lab topics are not yet in the manual: digestion of foods (Section 13.3 ties it to the amylase work in '
  'Experiment 13) and analysis of simulated urine',
  '<p>Digestion of foods is modeled by the acid hydrolysis of starch and sucrose in Experiment 8 (Part E) and by the amylase work '
  'in Experiment 13 (Section 13.3). One outline lab topic is not yet in the manual: analysis of simulated urine',
  'Course Outline Alignment: digestion covered by Exp 8', 'Same.')
e('597396', 'Digestion of foods and simulated-urine analysis (outline lab topics) are not yet in the manual.',
  'The outline&rsquo;s digestion-of-foods topic is the acid hydrolysis of starch and sucrose in Experiment 8 (with amylase in '
  'Experiment 13); simulated-urine analysis is not yet in the manual.',
  'For Instructors: digestion covered by Exp 8', 'Same.')

h = lambda x: hashlib.sha256(x.encode()).hexdigest()
sha = {p: {'before': h(pages[p][0]), 'after': h(pages[p][1])} for p in order}
for p in order:
    open('audit/preview/%s.html' % p, 'w', encoding='utf-8').write(pages[p][1])
json.dump({'uploads': [], 'edits': edits}, open('tools/batchAN_2026-11-18.json', 'w'), ensure_ascii=False, indent=1)
json.dump(sha, open('tools/batchAN_sha_2026-11-18.json', 'w'))
print(sum(len(v) for v in edits.values()), 'edits on', len(edits), 'pages')
