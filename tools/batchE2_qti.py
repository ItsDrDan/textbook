"""Batch E2 (review 2026-11-12): question-bank licence line.
The author's decision: the question bank is CC BY 4.0, author "Daniel Kwasniewski".
1. Generators (adapt_export.py, adapt_nov5.py, adapt_thin.py) wrote "Dr. Dan (Daniel Kwasniewski), CC BY-NC-SA 4.0"
   into assessment_meta.xml; cumulative.py's docstring said the same. Patched to CC BY 4.0.
2. The 36 QTI zips in adapt/ are rewritten in place: the <description> licence sentence is corrected, and a
   LICENSE.txt (title, author, source, licence) is added so each package describes itself when shared.
   Every other entry is copied byte for byte, in the same order.
"""
import glob, io, re, zipfile

OLD_DESC = [
    ('Questions by Dr. Dan (Daniel Kwasniewski), CC BY-NC-SA 4.0.', 'Questions by Daniel Kwasniewski, CC BY 4.0.'),
    ('Dr. Dan (Daniel Kwasniewski), CC BY-NC-SA 4.0.', 'Questions by Daniel Kwasniewski, CC BY 4.0.'),
]
GEN = ['tools/adapt_export.py', 'tools/adapt_nov5.py', 'tools/adapt_thin.py']
BOOK = 'https://chem.libretexts.org/Workbench/CHEM_3B%3A_Introductory_Organic_and_Biochemistry'

for f in GEN:
    s = open(f, encoding='utf-8').read(); n0 = s
    for a, b in OLD_DESC: s = s.replace(a, b)
    open(f, 'w', encoding='utf-8').write(s); print('patched', f)
f = 'tools/cumulative.py'; s = open(f, encoding='utf-8').read()
s2 = s.replace('All problems written by Daniel Kwasniewski, Fresno City College,\nCC BY-NC-SA 4.0.', 'All problems written by Daniel Kwasniewski, Fresno City College,\nCC BY 4.0.')
open(f, 'w', encoding='utf-8').write(s2); print('patched', f)


def license_txt(title):
    return (f'{title}\n\n'
            'Author: Daniel Kwasniewski, Fresno City College\n'
            'Written for: Introductory Organic and Biological Chemistry for FCC (LibreTexts)\n'
            f'Source: {BOOK}\n'
            'License: Creative Commons Attribution 4.0 International (CC BY 4.0)\n'
            'https://creativecommons.org/licenses/by/4.0/\n\n'
            'Videos linked from question hints are the author\'s YouTube lessons; they are not covered by this license.\n')


n = 0
for z in sorted(glob.glob('adapt/*.zip')):
    zin = zipfile.ZipFile(z)
    items = [(i, zin.read(i.filename)) for i in zin.infolist()]
    zin.close()
    title = None; out = io.BytesIO(); changed = 0
    with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as zo:
        for info, data in items:
            if info.filename == 'LICENSE.txt': continue
            if info.filename.endswith('assessment_meta.xml'):
                t = data.decode('utf-8'); t0 = t
                for a, b in OLD_DESC: t = t.replace(a, b)
                changed += t != t0
                m = re.search(r'<title>(.*?)</title>', t); title = title or (m and m.group(1))
                data = t.encode('utf-8')
            zo.writestr(info, data)
        lic = zipfile.ZipInfo('LICENSE.txt', date_time=items[0][0].date_time)
        lic.compress_type = zipfile.ZIP_DEFLATED
        zo.writestr(lic, license_txt(title or z.split('/')[-1][:-4]))
    open(z, 'wb').write(out.getvalue()); n += 1
print(n, 'zips rewritten')
