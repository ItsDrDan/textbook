// Render the structure/figure parts of Try It bank questions to PNG for the ADAPT/QTI export.
// node tools/render_bank_images.js  -> adapt/img/<id>_q.png, <id>_c<k>.png, adapt/img/index.json
const {chromium}=require('playwright');const fs=require('fs');const path=require('path');
const ROOT=path.resolve(__dirname,'..');const OUT=path.join(ROOT,'adapt','img');
(async()=>{const b=await chromium.launch();const p=await b.newPage({deviceScaleFactor:2,viewport:{width:900,height:700}});
const css=fs.readFileSync(path.join(ROOT,'css/widget-base.css'),'utf8');
await p.setContent(`<html><head><style>${css} body{margin:0;background:#fff;font-family:Helvetica,Arial,sans-serif} #h{display:inline-block;padding:8px;background:#fff} svg text{font-family:Helvetica,Arial,sans-serif!important}</style></head><body><div id=h></div></body></html>`);
await p.addScriptTag({content:fs.readFileSync(path.join(ROOT,'js/fbx.js'),'utf8')});
const idx={};let n=0;
for(const f of fs.readdirSync(path.join(ROOT,'bank')).filter(f=>f.endsWith('.json'))){
 for(const q of JSON.parse(fs.readFileSync(path.join(ROOT,'bank',f),'utf8'))){
  if(!(q.s||q.f||q.cs)||q.src==='canvas-quiz')continue;
  const rec={q:null,c:[]};
  const parts=await p.evaluate(q=>({q:(window.FBX.structBlock(q.s)||'')+(window.FBX.figBlock(q.f)||''),c:(q.c||[]).map((_,k)=>q.cs&&q.cs[k]?window.FBX.molSVG(q.cs[k],0.8):'')}),q);
  const shot=async(html,name)=>{if(!html||!/<svg|<table|<img/.test(html))return null;await p.evaluate(h=>{document.getElementById('h').innerHTML=h},html);
   const el=await p.$('#h');const bb=await el.boundingBox();if(!bb||bb.width<4||bb.height<4)return null;await el.screenshot({path:path.join(OUT,name)});n++;return {file:name,w:Math.round(bb.width),h:Math.round(bb.height)}};
  try{rec.q=await shot(parts.q,`${q.id}_q.png`);for(let k=0;k<parts.c.length;k++)rec.c.push(await shot(parts.c[k],`${q.id}_c${k}.png`))}catch(e){rec.err=String(e).slice(0,200)}
  idx[q.id]=rec}}
fs.writeFileSync(path.join(OUT,'index.json'),JSON.stringify(idx));console.log('items',Object.keys(idx).length,'images',n);await b.close()})();
