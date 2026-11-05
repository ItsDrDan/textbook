/* Build inline-SVG reaction schemes (for the LibreTexts pages) from the Bond Voyage engine.
   node tools/scheme.js  → writes tools/schemes.json  {id: {svg, caption}} */
global.window={};
require('../js/engine.js');
const E=window.ENGINE,L=E.lib,esc=E.esc;
const fs=require('fs');

function panel(part){ // returns {w,h,inner(x,y)}
 if(part.smi){
  const svg=E.molSVG(E.parseSmi(part.smi),{alt:part.name});
  const vb=svg.match(/viewBox="([^"]+)"/)[1],w=+svg.match(/ width="(\d+)"/)[1],h=+svg.match(/ height="(\d+)"/)[1];
  const body=svg.replace(/^<svg[^>]*>/,'').replace(/<\/svg>$/,'');
  const lab=part.name?wrap(part.name,22):[];const lh=lab.length*15;
  const W=Math.max(w,lab.length?Math.max(...lab.map(l=>l.length*7.2)):0)+8,H=h+lh+(lab.length?6:0);
  return {w:W,h:H,draw:(x,y,base)=>{const mx=x+(W-w)/2,my=Math.max(4,h0/2-h/2-lh/2-4);return `<svg x="${mx.toFixed(1)}" y="${my.toFixed(1)}" width="${w}" height="${h}" viewBox="${vb}">${body}</svg>`+lab.map((l,i)=>`<text x="${(x+W/2).toFixed(1)}" y="${(Math.max(4,h0/2-h/2-lh/2-4)+h+15*(i+1)+2).toFixed(1)}" text-anchor="middle" font-size="13" font-weight="700" fill="#3b5f7a" font-family="Nunito,Inter,Helvetica,Arial,sans-serif">${esc(l)}</text>`).join('')}}}
 const t=String(part.t);const W=t.length*13+10;
 return {w:W,h:30,draw:(x,y,base)=>`<text x="${(x+W/2).toFixed(1)}" y="${(base-h0/2+8).toFixed(1)}" text-anchor="middle" font-size="22" font-weight="800" fill="#2d3f4b" font-family="Nunito,Inter,Helvetica,Arial,sans-serif">${esc(t)}</text>`}}
let h0=0;
function wrap(s,n){const out=[];let cur='';s.split(' ').forEach(w=>{if((cur+' '+w).trim().length>n&&cur){out.push(cur);cur=w}else cur=(cur+' '+w).trim()});if(cur)out.push(cur);return out}
function arrow(cond){const parts=String(cond||'').split(/,\s*/).filter(Boolean);const top=parts.length>1?parts.slice(0,-1).join(', '):(parts[0]||''),bot=parts.length>1?parts[parts.length-1]:'';
 const W=Math.max(90,top.length*8+20,bot.length*8+20);
 return {w:W,h:50,draw:(x,y,base)=>{const cy=base-h0/2;return `<text x="${(x+W/2).toFixed(1)}" y="${(cy-9).toFixed(1)}" text-anchor="middle" font-size="13" font-weight="800" fill="#3b5f7a" font-family="Nunito,Inter,Helvetica,Arial,sans-serif">${esc(top)}</text><line x1="${(x+8).toFixed(1)}" y1="${cy.toFixed(1)}" x2="${(x+W-14).toFixed(1)}" y2="${cy.toFixed(1)}" stroke="#2d3f4b" stroke-width="2.6" stroke-linecap="round"/><path d="M${(x+W-16).toFixed(1)} ${(cy-6.5).toFixed(1)} L${(x+W-4).toFixed(1)} ${cy.toFixed(1)} L${(x+W-16).toFixed(1)} ${(cy+6.5).toFixed(1)} Z" fill="#2d3f4b"/><text x="${(x+W/2).toFixed(1)}" y="${(cy+20).toFixed(1)}" text-anchor="middle" font-size="13" font-weight="800" fill="#3b5f7a" font-family="Nunito,Inter,Helvetica,Arial,sans-serif">${esc(bot)}</text>`}}}
const plus={w:28,h:30,draw:(x,y,base)=>`<text x="${(x+14).toFixed(1)}" y="${(base-h0/2+9).toFixed(1)}" text-anchor="middle" font-size="24" font-weight="900" fill="#6b7a85" font-family="Nunito,Inter,Helvetica,Arial,sans-serif">+</text>`};
function scheme(r,alt){
 const seq=[];const put=(p,i)=>{if(i)seq.push(plus);if(p.coef>1&&p.smi)seq.push(panel({t:String(p.coef)}));seq.push(panel(p))};r.reactants.forEach(put);seq.push(arrow(r.cond));r.products.forEach(put); // coefficients drawn for structures (e.g. 2 alcohols in acetal formation)
 const gap=10,W=seq.reduce((a,p)=>a+p.w,0)+gap*(seq.length-1)+24,H=Math.max(...seq.map(p=>p.h))+24;h0=H;
 let x=12;const base=H-12;let body='';seq.forEach(p=>{body+=p.draw(x,0,base);x+=p.w+gap});
 return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W.toFixed(0)} ${H.toFixed(0)}" width="${W.toFixed(0)}" height="${H.toFixed(0)}" style="max-width:100%;height:auto;display:block;margin:0 auto" role="img" aria-label="${esc(alt)}"><rect width="100%" height="100%" rx="14" fill="#ffffff" stroke="#e2dccd" stroke-width="2" stroke-dasharray="6 4"/>${body}</svg>`}

/* deterministic reactions: call the template until the named reactant appears */
function want(key,test,max=400){for(let i=0;i<max;i++){const r=E.TPL[key]();if(test(r))return r}throw new Error('no match '+key)}
const T=t=>({t});
const mol=(smi,name,style)=>{const s=E.structHTML(smi,style||'skeletal');return (/xmlns=/.test(s)?s:s.replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" ')).replace('<svg ','<svg style="max-width:100%;height:auto" ')};
module.exports={scheme,want,mol,E};
if(require.main===module){
const R={};
R.ch2_combustion=want('combustion',r=>r.reactants[0].name==='propane');
R.ch2_substitution=want('substitution',r=>r.reactants[0].name==='ethane'&&/Cl/.test(r.reactants[1].t));
R.ch3_hydrogenation=want('hydrogenation',r=>r.reactants[0].name==='propene');
R.ch3_hydrohalogenation=want('hydrohalogenation',r=>r.reactants[0].name==='propene'&&/HCl/.test(r.reactants[1].t));
R.ch3_hydration=want('hydration',r=>r.reactants[0].name==='1-butene');
R.ch3_halogenAdd=want('halogenAdd',r=>r.reactants[0].name==='ethene (ethylene)'&&/Br/.test(r.reactants[1].t));
R.ch4_dehydration=want('dehydration',r=>/cyclohexanol/.test(r.reactants[0].name));
R.ch4_ox1=want('ox1Ald',r=>r.reactants[0].name==='ethanol');
R.ch4_ox1acid=want('ox1Acid',r=>r.reactants[0].name==='ethanol');
R.ch4_ox2=want('ox2',r=>r.reactants[0].name==='2-propanol (isopropyl alcohol)');
R.ch5_reduction=want('reduction',r=>r.reactants[0].name==='2-butanone');
R.ch5_oxAld=want('oxAldAcid',r=>r.reactants[0].name==='ethanal (acetaldehyde)');
R.ch5_hemiacetal=want('hemiacetal',r=>r.reactants[0].name==='ethanal (acetaldehyde)'&&r.reactants[1].name==='methanol');
R.ch6_esterification=want('esterification',r=>r.reactants[0].name==='ethanoic acid (acetic acid)'&&r.reactants[1].name==='ethanol');
R.ch6_saponification=want('saponification',r=>/ethyl ethanoate|ethyl acetate/.test(r.reactants[0].name));
R.ch6_neutral=want('neutralAcid',r=>r.reactants[0].name==='propanoic acid');
R.ch7_amidation=want('amidation',r=>r.reactants[0].name==='ethanoic acid (acetic acid)'&&r.reactants[1].name==='methylamine');
R.ch7_neutral=want('neutralAmine',r=>r.reactants[0].name==='ethylamine');
R.ch7_amideHyd=want('amideHydrolysis',r=>r.reactants[0].name==='ethanamide (acetamide)');
const out={};
for(const [id,r] of Object.entries(R)){out[id]={svg:scheme(r,r.type+': '+r.reactants.filter(p=>p.smi).map(p=>p.name).join(' + ')+' gives '+r.products.filter(p=>p.smi).map(p=>p.name).join(' + ')),type:r.type,cls:r.cls,rule:r.rule,names:{re:r.reactants.map(p=>p.name||p.t),pr:r.products.map(p=>p.name||p.t)}}}
/* structure-only figures */
out.struct={};
[['CCCCCC','hexane'],['CC(C)CC','2-methylbutane'],['CCO','ethanol'],['CC(=O)C','propanone (acetone)'],['CC(=O)O','ethanoic acid'],['CCN','ethylamine'],['CC(=O)N','ethanamide'],['CCOC','methoxyethane'],['CCS','ethanethiol'],['C1=CC=CC=C1','benzene']].forEach(([s,n])=>out.struct[n]={skeletal:mol(s,n),condensed:E.condensedStr(E.parseSmi(s)),expanded:(E.expandedSVG(E.parseSmi(s),{scale:.8})||'').replace('<svg ','<svg xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto" ')});
fs.writeFileSync(__dirname+'/schemes.json',JSON.stringify(out));
console.log(Object.keys(out).length,'schemes;',Object.values(out).filter(o=>o.svg).map(o=>o.svg.length).reduce((a,b)=>a+b,0),'bytes');
fs.writeFileSync(__dirname+'/preview.html','<!doctype html><meta charset=utf-8><body style="font-family:sans-serif;background:#eee;padding:20px">'+Object.entries(out).filter(([k,v])=>v.svg).map(([k,v])=>`<h3>${k}: ${v.type}</h3>${v.svg}`).join('')+'<h3>structs</h3>'+Object.entries(out.struct).map(([n,v])=>`<p>${n}: ${v.skeletal} ${v.expanded} <code>${v.condensed}</code></p>`).join(''));
}
