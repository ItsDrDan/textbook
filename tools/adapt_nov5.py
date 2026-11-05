"""Build QTI zips of the Nov 5, 2026 pool-expansion questions (adapt/nov5_new_ids.json), one per chapter (6, 13, 14, 15).
Reuses item_xml() from adapt_export.py without regenerating its zips."""
import os, re, json, zipfile, uuid
HERE=os.path.dirname(os.path.abspath(__file__)); _s=open(os.path.join(HERE,'adapt_export.py')).read(); src=_s.split('used = set()')[0].replace('import build_pages as B','')+'\n'+_s[_s.index('MET = ['):_s.index('for ch in range(1, 16)')]+'\n'+_s[_s.index('def esc'):_s.index('rows = []')]
g={'__file__':os.path.join(HERE,'adapt_export.py')}; exec(src,g)
bank=g['bank']; item_xml=g['item_xml']; esc=g['esc']; plain=g['plain']; met_chapter=g['met_chapter']; OUT=g['OUT']
ids=json.load(open(os.path.join(OUT,'nov5_new_ids.json')))
allq={x['id']:x for v in bank.values() for x in v}
groups={6:[allq[i] for i in ids['acids_esters']]}
for i in ids['metabolism']: groups.setdefault(met_chapter(allq[i]),[]).append(allq[i])
for ch,items in groups.items():
    title=f'CHEM 3B Ch{ch:02d} pool additions (Nov 2026)'; aid='a'+uuid.uuid5(uuid.NAMESPACE_URL,f'chem3b-ch{ch}-nov5').hex
    body='\n'.join(item_xml(x,i) for i,x in enumerate(items,1))
    qti=f'<?xml version="1.0" encoding="UTF-8"?>\n<questestinterop xmlns="http://www.imsglobal.org/xsd/ims_qtiasiv1p2"><assessment ident="{aid}" title="{esc(title)}"><section ident="root_section">\n{body}\n</section></assessment></questestinterop>'
    man=f'<?xml version="1.0" encoding="UTF-8"?>\n<manifest identifier="m{aid}" xmlns="http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"><organizations/><resources><resource identifier="{aid}" type="imsqti_xmlv1p2"><file href="{aid}/{aid}.xml"/><dependency identifierref="{aid}meta"/></resource><resource identifier="{aid}meta" type="associatedcontent/imscc_xmlv1p1/learning-application-resource" href="{aid}/assessment_meta.xml"><file href="{aid}/assessment_meta.xml"/></resource></resources></manifest>'
    meta=f'<?xml version="1.0" encoding="UTF-8"?>\n<quiz identifier="{aid}" xmlns="http://canvas.instructure.com/xsd/cccv1p0"><title>{esc(title)}</title><description>Questions by Dr. Dan (Daniel Kwasniewski), CC BY-NC-SA 4.0.</description><quiz_type>assignment</quiz_type><points_possible>{len(items)}</points_possible></quiz>'
    zn=os.path.join(OUT,f'CHEM3B_Ch{ch:02d}_nov5_QTI.zip')
    with zipfile.ZipFile(zn,'w',zipfile.ZIP_DEFLATED) as z: z.writestr('imsmanifest.xml',man); z.writestr(f'{aid}/{aid}.xml',qti); z.writestr(f'{aid}/assessment_meta.xml',meta)
    print(ch,len(items),os.path.basename(zn))
