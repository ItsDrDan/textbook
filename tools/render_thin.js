// Render prompt + choice-structure images for selected bank items. node tools/render_thin.js ids.json outdir
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const ROOT=path.resolve(__dirname,'..');const [,,idsFile,OUT]=process.argv;const ids=JSON.parse(fs.readFileSync(idsFile));fs.mkdirSync(OUT,{recursive:true});
const bank={};for(const f of fs.readdirSync(path.join(ROOT,'bank')).filter(f=>f.endsWith('.json')))for(const q of JSON.parse(fs.readFileSync(path.join(ROOT,'bank',f))))bank[q.id]=q;
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:2,viewport:{width:900,height:700}});
const css=fs.readFileSync(path.join(ROOT,'css/widget-base.css'),'utf8');
await p.setContent(`<html><head><style>${css} body{margin:0;background:#fff;font-family:Helvetica,Arial,sans-serif} #h{display:inline-block;padding:10px;background:#fff;max-width:860px} svg text{font-family:Helvetica,Arial,sans-serif!important} .grid{display:flex;flex-wrap:wrap;gap:18px;align-items:flex-end} .cell{text-align:center} .lab{font:700 20px Helvetica,Arial;margin-top:4px}</style></head><body><div class=fbx><div id=h></div></div></body></html>`);
await p.addScriptTag({content:fs.readFileSync(path.join(ROOT,'js/fbx.js'),'utf8')});
const meta={};
for(const id of ids){const q=bank[id];const r=await p.evaluate(q=>{const F=window.FBX;return {s:F.structBlock(q.s)||'',f:F.figBlock(q.f)||'',cs:q.cs?q.cs.map(m=>m?F.molSVG(m,0.8):''):null}},q);
 const shot=async(html,name)=>{await p.evaluate(h=>{document.getElementById('h').innerHTML=h},html);const el=await p.$('#h');await el.screenshot({path:path.join(OUT,name)});return name};
 const m={};if(r.s&&/<svg/.test(r.s))m.s=await shot(r.s,id+'_s.png');
 if(r.f){m.fhtml=r.f; if(/<svg/.test(r.f))m.f=await shot(r.f,id+'_f.png')}
 if(r.cs){const L='ABCDEF';const cells=r.cs.map((svg,k)=>`<div class=cell>${svg}<div class=lab>${L[k]}</div></div>`).join('');m.cs=await shot(`<div class=grid>${cells}</div>`,id+'_cs.png')}
 meta[id]=m}
fs.writeFileSync(path.join(OUT,'meta.json'),JSON.stringify(meta));await b.close();console.log(Object.keys(meta).length)})();
