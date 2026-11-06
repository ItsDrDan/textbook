"""Build a Canvas course export (.imscc) for the CHEM 3B OER (Canvas Commons share)."""
import json, hashlib, zipfile, html, re, datetime

TREE = json.load(open('tree.json'))
GO = 'https://chem.libretexts.org/@go/page/{}'
BOOK = 'https://chem.libretexts.org/@go/page/488223'
ABOUT, ALIGN, GLOSS, ATTRIB = 597270, 597272, 488232, 597271
TITLE = 'CHEM 3B: Introductory Organic and Biological Chemistry (OER)'
gid = lambda s: 'g' + hashlib.md5(s.encode()).hexdigest()
esc = html.escape
CC_BY = '<a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">Creative Commons Attribution 4.0 International License (CC BY 4.0)</a>'

# ---------- chapters ----------
chapters = []
for pid, depth, title in TREE:
    if depth == 1: chapters.append({'id': pid, 'title': title, 'pages': []})
    else: chapters[-1]['pages'].append((pid, title))

def wiki(title, body, front=False):
    ident = gid('page:' + title)
    slug = re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
    doc = (f'<html>\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8">\n<title>{esc(title)}</title>\n'
           f'<meta name="identifier" content="{ident}"/>\n<meta name="editing_roles" content="teachers"/>\n<meta name="workflow_state" content="active"/>\n'
           + ('<meta name="front_page" content="true"/>\n' if front else '') + f'</head>\n<body>\n{body}\n</body>\n</html>\n')
    return ident, f'wiki_content/{slug}.html', doc

link = lambda pid, text: f'<a href="{GO.format(pid)}" target="_blank" rel="noopener">{esc(text)}</a>'

chap_rows = ''.join(f'<li>{link(c["id"], c["title"])}</li>' for c in chapters)
start_body = f'''<h2>Welcome to CHEM 3B</h2>
<p><strong>{esc(TITLE)}</strong> is a free, openly licensed course for introductory organic and biological chemistry, built for CHEM 3B at Fresno City College (C-ID CHEM 102). It is written for students headed into nursing, dental hygiene, radiologic technology, respiratory therapy and other health careers. Students never have to buy a textbook.</p>
<p><a href="{BOOK}" target="_blank" rel="noopener"><strong>Open the free textbook on LibreTexts</strong></a> (works on phones, tablets and computers, and can be downloaded as a PDF).</p>
<h3>What is in this course</h3>
<ul>
<li><strong>15 chapter modules.</strong> Each links to the reading for every section, a Chapter Guide (videos, worked examples and common mistakes), Practice Problems with answers, and Practice Games.</li>
<li><strong>Auto-graded homework.</strong> Each chapter has an auto-graded homework set in LibreTexts ADAPT. All questions are public and openly licensed, so instructors can copy them into their own ADAPT course (see the Instructor Guide).</li>
<li><strong>Interactive study games</strong> at the end of every chapter, free for students to play.</li>
<li><strong>A course outline alignment page</strong> that maps every topic in the CHEM 3B course outline of record to the book sections that teach it.</li>
</ul>
<h3>Chapters</h3>
<ol style="list-style:none;padding-left:0">{chap_rows}</ol>
<h3>License</h3>
<p>Unless otherwise indicated, this work is licensed under a {CC_BY}.</p>
<p>Some content in this work is reproduced or adapted from other sources and is subject to separate licensing terms. Such content is identified individually, with its applicable license and attribution information provided where it appears.</p>
<p>The textbook adapts <em>The Basics of General, Organic, and Biological Chemistry</em> by David W. Ball, John W. Hill and Rhonda J. Scott (CC BY-NC-SA), <em>Introduction to Organic and Biochemistry</em> by Muhammad Arif Malik (public domain) and <em>Fundamentals of General, Organic, and Biological Chemistry</em> (LibreTexts, CC BY-NC-SA). Pages adapted from the CC BY-NC-SA sources are marked CC BY-NC-SA 4.0 on the page. A section-by-section list is on the {link(ATTRIB, "Source Attributions by Section")} page.</p>
<p>The study games linked from this course are &copy; ItsDrDan, all rights reserved. They are free for students to play, but they are not part of the openly licensed material and may not be copied or redistributed without permission.</p>
<p><strong>Suggested attribution:</strong> &ldquo;{esc(TITLE)}&rdquo; by Dr. Dan (Daniel Kwasniewski), Fresno City College, licensed CC BY 4.0 except where otherwise indicated.</p>
<h3>Funding</h3>
<p>Development of this course and textbook was supported by the Fresno City College OER Award Program, funded by the State of California.</p>
<h3>Accessibility</h3>
<p>Every figure in the textbook has a text description, headings are in order for screen readers, and embedded videos have captions (use the CC button). If anything is hard to use, please contact the author so it can be fixed.</p>
<h3>Contact</h3>
<p>Dr. Dan (Daniel Kwasniewski), Department of Chemistry, Fresno City College.</p>'''

guide_body = f'''<h2>Instructor Guide</h2>
<p>This page is for instructors who want to adopt or adapt the course. Students can skip it.</p>
<h3>1. The textbook</h3>
<p>The book is free on LibreTexts: {link(488223, "Introductory Organic and Biological Chemistry for FCC")}. LibreTexts lets you copy the whole book or individual pages into your own LibreTexts space and edit them. Keep the license and attribution notices on any page you reuse.</p>
<h3>2. Alignment to the course outline</h3>
<p>The {link(ALIGN, "Course Outline Alignment")} page maps every objective and lecture topic in the CHEM 3B course outline of record (effective Spring 2027, C-ID CHEM 102) to the book sections that teach it. Chapter-level student learning outcomes are on the {link(ABOUT, "About This Book")} page.</p>
<h3>3. Auto-graded homework (LibreTexts ADAPT)</h3>
<p>Each chapter's Practice Problems page links to its ADAPT homework. All of the questions are public in ADAPT under CC BY 4.0 (author Daniel Kwasniewski). To use them, create a free ADAPT instructor account, search the question bank for the author or for the chapter, and add the questions to your own assignments. ADAPT connects to Canvas through LTI, so scores can go straight into your gradebook.</p>
<h3>4. Study games</h3>
<p>The Practice Games pages link to free browser games (no login). You may link to them or embed them in your course for your students. The games are &copy; ItsDrDan, all rights reserved, so please do not copy, host or modify them without permission.</p>
<h3>5. Suggested 16-week pacing</h3>
<table border="1" cellpadding="6" style="border-collapse:collapse">
<thead><tr><th scope="col">Weeks</th><th scope="col">Chapters</th></tr></thead>
<tbody>
<tr><td>1</td><td>1 Bonding Review</td></tr>
<tr><td>2&ndash;3</td><td>2 Alkanes and Cycloalkanes; 3 Alkenes, Alkynes and Aromatics</td></tr>
<tr><td>4&ndash;5</td><td>4 Alcohols, Phenols, Ethers and Thiols; 5 Aldehydes and Ketones (with chirality)</td></tr>
<tr><td>6&ndash;7</td><td>6 Carboxylic Acids and Esters; 7 Amines and Amides</td></tr>
<tr><td>8&ndash;9</td><td>8 Carbohydrates; 9 Lipids</td></tr>
<tr><td>10&ndash;11</td><td>10 Amino Acids and Proteins; 11 Enzymes and Vitamins</td></tr>
<tr><td>12</td><td>12 Nucleic Acids and Protein Synthesis</td></tr>
<tr><td>13&ndash;15</td><td>13 Carbohydrate Metabolism; 14 Metabolism and Energy Production; 15 Metabolism of Lipids and Proteins</td></tr>
<tr><td>16</td><td>Review and final exam</td></tr>
</tbody></table>
<p>Adjust the pacing to your own exam schedule.</p>
<h3>6. License</h3>
<p>Unless otherwise indicated, this course is licensed CC BY 4.0. Content adapted from CC BY-NC-SA sources is marked as such where it appears; see the {link(ATTRIB, "Source Attributions by Section")} page.</p>'''

pages = [wiki('Start Here', start_body, front=True), wiki('Instructor Guide', guide_body)]

# ---------- weblinks ----------
weblinks = []  # (ident, href, xml)
def weblink(title, url):
    ident = gid('url:' + url + title)
    xml = (f'<?xml version="1.0" encoding="UTF-8"?>\n<webLink xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1" '
           f'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imswl_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imswl_v1p1.xsd">\n'
           f'  <title>{esc(title)}</title>\n  <url href="{esc(url)}" target="_blank"/>\n</webLink>\n')
    weblinks.append((ident, f'{ident}.xml', xml))
    return ident

# module structure: list of (title, [items]) where item = dict(kind, title, ref, url)
modules = []
m0 = [dict(kind='page', title='Start Here', ref=pages[0][0]), dict(kind='page', title='Instructor Guide', ref=pages[1][0])]
for pid, t in [(488223, 'Open the free textbook (LibreTexts)'), (ABOUT, 'About This Book'), (ALIGN, 'Course Outline Alignment'), (GLOSS, 'Glossary (English and Spanish)'), (ATTRIB, 'Source Attributions by Section')]:
    m0.append(dict(kind='url', title=t, url=GO.format(pid), ref=weblink(t, GO.format(pid))))
modules.append(('Start Here', m0))
for c in chapters:
    items = [dict(kind='url', title='Chapter ' + c['title'], url=GO.format(c['id']), ref=weblink('Chapter ' + c['title'], GO.format(c['id']))), dict(kind='sub', title='Read')]
    practice = []
    for pid, t in c['pages']:
        it = dict(kind='url', title=t, url=GO.format(pid), ref=weblink(t, GO.format(pid)))
        (practice if re.search(r'Chapter Guide|Practice Problems|Practice Games', t) else items).append(it)
    items.append(dict(kind='sub', title='Study and practice'))
    items.extend(practice)
    modules.append(('Chapter ' + c['title'], items))

# ---------- manifest ----------
now = datetime.date.today().isoformat()
org_items, mod_meta = [], []
for mi, (mtitle, items) in enumerate(modules, 1):
    mid = gid('mod:' + mtitle)
    inner, meta_items = [], []
    for pos, it in enumerate(items, 1):
        iid = gid(f'item:{mtitle}:{pos}:{it["title"]}')
        if it['kind'] == 'sub':
            meta_items.append(f'<item identifier="{iid}"><content_type>ContextModuleSubHeader</content_type><workflow_state>active</workflow_state><title>{esc(it["title"])}</title><new_tab/><position>{pos}</position><indent>0</indent></item>')
            continue
        inner.append(f'<item identifier="{iid}" identifierref="{it["ref"]}"><title>{esc(it["title"])}</title></item>')
        if it['kind'] == 'page':
            meta_items.append(f'<item identifier="{iid}"><content_type>WikiPage</content_type><workflow_state>active</workflow_state><title>{esc(it["title"])}</title><identifierref>{it["ref"]}</identifierref><position>{pos}</position><new_tab/><indent>0</indent></item>')
        else:
            meta_items.append(f'<item identifier="{iid}"><content_type>ExternalUrl</content_type><workflow_state>active</workflow_state><title>{esc(it["title"])}</title><identifierref>{it["ref"]}</identifierref><url>{esc(it["url"])}</url><position>{pos}</position><new_tab>true</new_tab><indent>{0 if it["title"].startswith("Chapter ") else 1}</indent></item>')
    org_items.append(f'<item identifier="{mid}"><title>{esc(mtitle)}</title>{"".join(inner)}</item>')
    mod_meta.append(f'<module identifier="{mid}"><title>{esc(mtitle)}</title><workflow_state>active</workflow_state><position>{mi}</position><require_sequential_progress>false</require_sequential_progress><locked>false</locked><items>{"".join(meta_items)}</items></module>')

settings_id = gid('settings')
resources = [f'<resource identifier="{settings_id}" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="course_settings/canvas_export.txt"><file href="course_settings/course_settings.xml"/><file href="course_settings/module_meta.xml"/><file href="course_settings/canvas_export.txt"/></resource>']
for ident, href, _ in pages:
    resources.append(f'<resource identifier="{ident}" type="webcontent" href="{href}"><file href="{href}"/></resource>')
for ident, href, _ in weblinks:
    resources.append(f'<resource identifier="{ident}" type="imswl_xmlv1p1"><file href="{href}"/></resource>')

manifest = f'''<?xml version="1.0" encoding="UTF-8"?>
<manifest identifier="{gid('manifest')}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1" xmlns:lom="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource" xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/resource http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lomresource_v1p0.xsd http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest http://www.imsglobal.org/profile/cc/ccv1p1/LOM/ccv1p1_lommanifest_v1p0.xsd">
  <metadata>
    <schema>IMS Common Cartridge</schema>
    <schemaversion>1.1.0</schemaversion>
    <lomimscc:lom>
      <lomimscc:general><lomimscc:title><lomimscc:string>{esc(TITLE)}</lomimscc:string></lomimscc:title></lomimscc:general>
      <lomimscc:lifeCycle><lomimscc:contribute><lomimscc:date><lomimscc:dateTime>{now}</lomimscc:dateTime></lomimscc:date></lomimscc:contribute></lomimscc:lifeCycle>
      <lomimscc:rights><lomimscc:copyrightAndOtherRestrictions><lomimscc:value>yes</lomimscc:value></lomimscc:copyrightAndOtherRestrictions><lomimscc:description><lomimscc:string>Creative Commons Attribution 4.0 International (CC BY 4.0), except where otherwise indicated.</lomimscc:string></lomimscc:description></lomimscc:rights>
    </lomimscc:lom>
  </metadata>
  <organizations>
    <organization identifier="org_1" structure="rooted-hierarchy">
      <item identifier="LearningModules">{"".join(org_items)}</item>
    </organization>
  </organizations>
  <resources>
    {chr(10).join(resources)}
  </resources>
</manifest>
'''
course_settings = f'''<?xml version="1.0" encoding="UTF-8"?>
<course identifier="{settings_id}" xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">
  <title>{esc(TITLE)}</title>
  <course_code>CHEM 3B OER</course_code>
  <license>cc_by</license>
  <is_public>false</is_public>
  <default_view>wiki</default_view>
  <public_description>{esc("Free, openly licensed CHEM 3B (C-ID CHEM 102) course: 15 modules linking a LibreTexts textbook, auto-graded ADAPT homework and study games. CC BY 4.0 except where otherwise indicated. Funded by the Fresno City College OER Award Program.")}</public_description>
</course>
'''
module_meta = f'<?xml version="1.0" encoding="UTF-8"?>\n<modules xmlns="http://canvas.instructure.com/xsd/cccv1p0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://canvas.instructure.com/xsd/cccv1p0 https://canvas.instructure.com/xsd/cccv1p0.xsd">\n{chr(10).join(mod_meta)}\n</modules>\n'

out = 'CHEM3B_OER_Canvas_Commons.imscc'
with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as z:
    z.writestr('imsmanifest.xml', manifest)
    z.writestr('course_settings/course_settings.xml', course_settings)
    z.writestr('course_settings/module_meta.xml', module_meta)
    z.writestr('course_settings/canvas_export.txt', 'Canvas course export marker\n')
    for _, href, doc in pages: z.writestr(href, doc)
    for _, href, xml in weblinks: z.writestr(href, xml)
print(out, len(modules), 'modules,', len(weblinks), 'links,', len(pages), 'pages')
