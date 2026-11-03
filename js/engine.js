/* ItsDrDan textbook engine: structure drawing, compound library, reaction templates and name checking.
   Extracted from Bond Voyage! (ItsDrDan/organicreactions). Edit there first; copy here. */
(function(){"use strict";

/* ================= helpers ================= */
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const rnd=(a,b)=>a+Math.floor(Math.random()*(b-a+1));
const pick=a=>a[Math.floor(Math.random()*a.length)];
const shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.floor(Math.random()*(i+1));[a[i],a[j]]=[a[j],a[i]]}return a};
const deg=Math.PI/180,cosd=a=>Math.cos(a*deg),sind=a=>Math.sin(a*deg);
function bag(list){let b=[],last=null;return ()=>{if(!b.length){b=shuf(list);if(b[b.length-1]===last&&b.length>1)b.unshift(b.pop())}last=b.pop();return last}}
const SUBD={'0':'₀','1':'₁','2':'₂','3':'₃','4':'₄','5':'₅','6':'₆','7':'₇','8':'₈','9':'₉'};
const subU=s=>String(s).replace(/\d/g,d=>SUBD[d]);

/* ================= molecular graph ================= */
const VAL={C:4,N:3,O:2,S:2,F:1,Cl:1,Br:1,I:1};
const valence=(el,ch)=>el==='N'?3+(ch||0):el==='O'||el==='S'?2+(ch||0):VAL[el];
function parseSmi(s){const atoms=[],bonds=[],stack=[],rings={};let i=0,prev=null,ord=1;
 while(i<s.length){const ch=s[i];
  if(ch==='('){stack.push(prev);i++;continue}
  if(ch===')'){prev=stack.pop();i++;continue}
  if(ch==='='){ord=2;i++;continue}
  if(ch==='#'){ord=3;i++;continue}
  if(/\d/.test(ch)){if(rings[ch]){bonds.push({a:rings[ch].at,b:prev,o:Math.max(rings[ch].o,ord)});delete rings[ch]}else rings[ch]={at:prev,o:ord};ord=1;i++;continue}
  let el,charge=0;
  if(ch==='['){const j=s.indexOf(']',i),m=s.slice(i+1,j).match(/^(Cl|Br|[CNOSFI])(H\d?)?([+-])?$/);el=m[1];charge=m[3]==='+'?1:m[3]==='-'?-1:0;i=j+1}
  else if(s.startsWith('Cl',i)){el='Cl';i+=2}else if(s.startsWith('Br',i)){el='Br';i+=2}else{el=ch;i++}
  const id=atoms.length;atoms.push({el,charge});if(prev!==null)bonds.push({a:prev,b:id,o:ord});ord=1;prev=id}
 return {atoms,bonds}}
function adjOf(g){const adj=g.atoms.map(()=>[]);g.bonds.forEach(b=>{adj[b.a].push({n:b.b,o:b.o});adj[b.b].push({n:b.a,o:b.o})});return adj}
const hCount=(g,adj,i)=>valence(g.atoms[i].el,g.atoms[i].charge)-adj[i].reduce((s,x)=>s+x.o,0);
function comps(g){const n=g.atoms.length,adj=adjOf(g),cid=new Array(n).fill(-1),out=[];
 for(let s=0;s<n;s++){if(cid[s]>=0)continue;const k=out.length,list=[],q=[s];cid[s]=k;while(q.length){const x=q.shift();list.push(x);adj[x].forEach(({n:y})=>{if(cid[y]<0){cid[y]=k;q.push(y)}})}
  list.sort((a,b)=>a-b);const map={};list.forEach((x,j)=>map[x]=j);
  out.push({atoms:list.map(x=>g.atoms[x]),bonds:g.bonds.filter(b=>cid[b.a]===k).map(b=>({a:map[b.a],b:map[b.b],o:b.o})),orig:list})}
 return out}
function matrix(g){const n=g.atoms.length,m=Array.from({length:n},()=>new Array(n).fill(0));g.bonds.forEach(b=>{m[b.a][b.b]=b.o;m[b.b][b.a]=b.o});return m}
function iso(A,B){const n=A.atoms.length;if(n!==B.atoms.length||A.bonds.length!==B.bonds.length)return false;
 const aA=adjOf(A),aB=adjOf(B),mA=matrix(A),mB=matrix(B);
 const sg=(g,adj,i)=>g.atoms[i].el+(g.atoms[i].charge||0)+'/'+hCount(g,adj,i)+'/'+adj[i].map(x=>x.o).sort().join('');
 const sA=A.atoms.map((_,i)=>sg(A,aA,i)),sB=B.atoms.map((_,i)=>sg(B,aB,i));
 if(sA.slice().sort().join()!==sB.slice().sort().join())return false;
 const order=[],seen=new Array(n).fill(false);
 for(let s=0;s<n;s++){if(seen[s])continue;const q=[s];seen[s]=true;while(q.length){const x=q.shift();order.push(x);aA[x].forEach(({n:y})=>{if(!seen[y]){seen[y]=true;q.push(y)}})}}
 const map=new Array(n).fill(-1),used=new Array(n).fill(false);
 const rec=k=>{if(k===n)return true;const i=order[k];
  for(let j=0;j<n;j++){if(used[j]||sA[i]!==sB[j])continue;let ok=true;for(let t=0;t<k;t++){const i2=order[t];if(mA[i][i2]!==mB[j][map[i2]]){ok=false;break}}
   if(!ok)continue;map[i]=j;used[j]=true;if(rec(k+1))return true;used[j]=false;map[i]=-1}
  return false};
 return rec(0)}
function formula(g){const adj=adjOf(g),c={};let q=0;g.atoms.forEach((a,i)=>{c[a.el]=(c[a.el]||0)+1;const h=hCount(g,adj,i);if(h>0)c.H=(c.H||0)+h;q+=a.charge||0});
 const keys=['C','H',...Object.keys(c).filter(k=>k!=='C'&&k!=='H').sort()].filter(k=>c[k]);
 return {c,q,text:keys.map(k=>k+(c[k]>1?c[k]:'')).join('')+(q>0?'⁺':q<0?'⁻':'')}}
const fHTML=t=>t.replace(/(\d+)/g,'<sub>$1</sub>');
const isWater=g=>g.atoms.length===1&&g.atoms[0].el==='O'&&!g.atoms[0].charge;
function groupsOf(g){const adj=adjOf(g),out=new Set(),A=g.atoms;
 const isC=i=>A[i].el==='C',dblO=i=>adj[i].some(x=>x.o===2&&A[x.n].el==='O');
 g.bonds.forEach(b=>{if(isC(b.a)&&isC(b.b)){if(b.o===2)out.add('alkene');if(b.o===3)out.add('alkyne')}});
 A.forEach((a,i)=>{
  if(['F','Cl','Br','I'].includes(a.el))out.add('halide');
  if(a.el==='O'){const cn=adj[i].filter(x=>isC(x.n));
   if(adj[i].length===1&&adj[i][0].o===2){const c=adj[i][0].n;if(!isC(c))return;const nb=adj[c].filter(x=>x.n!==i);
    if(nb.some(x=>A[x.n].el==='N'))out.add('amide');
    else if(nb.some(x=>A[x.n].el==='O')){/* acid/ester/carboxylate handled at O–C single */}
    else{const cc=nb.filter(x=>isC(x.n)).length;out.add(cc>=2?'ketone':'aldehyde')}return}
   if(cn.length===1&&a.charge===-1){if(dblO(cn[0].n))out.add('carboxylate');return}
   if(cn.length===1&&hCount(g,adj,i)===1){out.add(dblO(cn[0].n)?'acid':'alcohol');return}
   if(cn.length===2){out.add(cn.some(x=>dblO(x.n))?'ester':'ether')}}
  if(a.el==='N'){if(adj[i].some(x=>isC(x.n)&&dblO(x.n)))return;out.add(a.charge===1?'ammonium':'amine')}});
 A.forEach((a,i)=>{if(a.el!=='C')return;const os=adj[i].filter(x=>x.o===1&&A[x.n].el==='O'&&!A[x.n].charge);if(os.length<2||dblO(i))return;const oh=os.filter(x=>hCount(g,adj,x.n)===1).length;
  out.delete('alcohol');out.delete('ether');out.add(oh?'hemiacetal':'acetal')});
 return [...out]}
const GNAME={alkene:'alkene',alkyne:'alkyne',halide:'alkyl halide',alcohol:'alcohol',ether:'ether',aldehyde:'aldehyde',ketone:'ketone',acid:'carboxylic acid',ester:'ester',carboxylate:'carboxylate ion',amine:'amine',ammonium:'ammonium ion',amide:'amide',alkane:'alkane',hemiacetal:'hemiacetal',acetal:'acetal'};
const gList=g=>{const l=groupsOf(g);return l.length?l:['alkane']};
const an=w=>(/^[aeiou]/i.test(w)?'an ':'a ')+w;

/* ================= 2D layout (skeletal conventions) ================= */
function chainPath(g,adj){const n=g.atoms.length;if(n===1)return [0];
 const leaves=[...Array(n).keys()].filter(i=>adj[i].length<=1);let best=null,bs=-1e9;
 for(const s of leaves){const par=new Array(n).fill(-2);par[s]=-1;const q=[s];while(q.length){const x=q.shift();adj[x].forEach(({n:y})=>{if(par[y]===-2){par[y]=x;q.push(y)}})}
  for(const t of leaves){if(t===s||par[t]===-2)continue;const p=[];let c=t;while(c!==-1){p.push(c);c=par[c]}p.reverse();
   const endD=[p[0],p[p.length-1]].filter(e=>g.atoms[e].el!=='C'&&adj[e][0]&&adj[e][0].o>1).length;
   const sc=p.length*100-endD*60+p.filter(i=>g.atoms[i].el==='C').length*5;if(sc>bs){bs=sc;best=p}}}
 const het=i=>g.atoms[i].el!=='C'||adj[i].some(x=>g.atoms[x.n].el!=='C')?1:0;
 if(het(best[0])>het(best[best.length-1]))best.reverse();
 return best}
function ringOf(g,adj){const n=g.atoms.length,alive=new Array(n).fill(true);let ch=true;
 while(ch){ch=false;for(let i=0;i<n;i++)if(alive[i]&&adj[i].filter(x=>alive[x.n]).length<=1){alive[i]=false;ch=true}}
 const R=[...Array(n).keys()].filter(i=>alive[i]);if(!R.length)return null;
 const order=[R[0]];let prev=-1,cur=R[0];while(true){const nx=adj[cur].find(x=>alive[x.n]&&x.n!==prev&&(order.length<2||x.n!==order[order.length-2]));if(!nx||nx.n===R[0])break;prev=cur;cur=nx.n;if(order.includes(cur))break;order.push(cur)}
 return order}
function layoutComp(g){const n=g.atoms.length,adj=adjOf(g),pos=new Array(n),placed=new Array(n).fill(false);
 if(n===1){pos[0]={x:0,y:0};return pos}
 const P=(i,x,y)=>{pos[i]={x,y};placed[i]=true};
 const bo=(i,j)=>{const e=adj[i].find(x=>x.n===j);return e?e.o:0};
 const turnAt=(a,b,c)=>{const o1=bo(a,b),o2=bo(b,c);return (o1===3||o2===3)?0:180-((o1===2||o2===2)?120:109.5)};
 function grow(c,par,dir,sign){P(c,pos[par].x+cosd(dir),pos[par].y+sind(dir));const kids=adj[c].filter(x=>!placed[x.n]);
  if(kids.length===1){const t=turnAt(par,c,kids[0].n);grow(kids[0].n,c,dir+sign*t,t?-sign:sign)}
  else if(kids.length===2){grow(kids[0].n,c,dir-60,1);grow(kids[1].n,c,dir+60,-1)}
  else kids.forEach((k,i)=>grow(k.n,c,dir-90+90*i,1))}
 const ring=ringOf(g,adj);
 if(ring){const k=ring.length,R=1/(2*Math.sin(Math.PI/k));ring.forEach((r,j)=>{const a=-90+360*j/k;P(r,R*cosd(a),R*sind(a))});
  ring.forEach((r,j)=>{const a=-90+360*j/k,subs=adj[r].filter(x=>!placed[x.n]);if(subs.length===1)grow(subs[0].n,r,a,1);else subs.forEach((s,m)=>grow(s.n,r,a+(m?35:-35),m?-1:1))})}
 else{const p=chainPath(g,adj);const t1=p.length>2?turnAt(p[0],p[1],p[2]):0;let d=-t1/2,sign=1;P(p[0],0,0);
  for(let k=1;k<p.length;k++){if(k>=2){const t=turnAt(p[k-2],p[k-1],p[k]);d+=sign*t;if(t)sign=-sign}P(p[k],pos[p[k-1]].x+cosd(d),pos[p[k-1]].y+sind(d))}
  p.forEach((c,k)=>{const subs=adj[c].filter(x=>!placed[x.n]);if(!subs.length)return;
   let ox=0,oy=0;[p[k-1],p[k+1]].forEach(nb=>{if(nb===undefined)return;const dx=pos[nb].x-pos[c].x,dy=pos[nb].y-pos[c].y,l=Math.hypot(dx,dy);ox-=dx/l;oy-=dy/l});
   let out=Math.hypot(ox,oy)<1e-6?-90:Math.atan2(oy,ox)/deg;
   if(subs.length===1)grow(subs[0].n,c,out,1);else subs.forEach((s,m)=>grow(s.n,c,out+(m?40:-40),m?-1:1))})}
 return pos}
function layoutGraph(g){const cs=comps(g),pos=new Array(g.atoms.length);let x0=0;
 cs.forEach(c=>{const p=layoutComp(c),xs=p.map(q=>q.x),ys=p.map(q=>q.y),mx=Math.min(...xs),Mx=Math.max(...xs),cy=(Math.min(...ys)+Math.max(...ys))/2;
  c.orig.forEach((o,j)=>pos[o]={x:p[j].x-mx+x0,y:p[j].y-cy});x0+=Mx-mx+1.9});
 return pos}

/* ================= SVG rendering ================= */
const ECOL={O:'#c0392b',N:'#2f5fc4',Cl:'#2e8b57',Br:'#8a5a1c',F:'#2e8b57',C:'#2d3f4b'};
const EW={C:12,O:14,N:14,S:12,F:11,Cl:20,Br:22,I:6};
function atomLabel(g,adj,pos,i,force){const a=g.atoms[i];if(a.el==='C'&&!force&&adj[i].length)return '';
 const h=hCount(g,adj,i),x=pos[i].x,y=pos[i].y,col=ECOL[a.el]||'#2d3f4b',w=EW[a.el]||13;
 const T=(tx,anchor,xx,extra)=>`<text x="${xx.toFixed(1)}" y="${(y+6.5).toFixed(1)}" text-anchor="${anchor}" fill="${col}" font-size="19" font-weight="800" font-family="Inter,Helvetica,Arial,sans-serif" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke" ${extra||''}>${tx}</text>`;
 const hs=h>0?'H'+(h>1?`<tspan dy="5" font-size="13">${h}</tspan>`:''):'';
 const left=adj[i].length===1&&pos[adj[i][0].n].x>x+.1&&h>0;
 let s=T(a.el,'middle',x);
 if(hs){s+=left?T(hs,'end',x-w/2-1):T(hs,'start',x+w/2+1)}
 if(a.charge){const cx=left||!hs?x+w/2+1:x+w/2+(h>1?22:14);s+=`<text x="${cx.toFixed(1)}" y="${(y-5).toFixed(1)}" fill="${col}" font-size="15" font-weight="900" font-family="Inter,Helvetica,Arial,sans-serif" stroke="#fff" stroke-width="4" paint-order="stroke">${a.charge>0?'+':'−'}</text>`}
 return s}
function bondsSVG(g,pos,lab,col){let s='';g.bonds.forEach(b=>{let x1=pos[b.a].x,y1=pos[b.a].y,x2=pos[b.b].x,y2=pos[b.b].y;const dx=x2-x1,dy=y2-y1,l=Math.hypot(dx,dy)||1,ux=dx/l,uy=dy/l,px=-uy,py=ux;
  if(lab[b.a]){x1+=ux*11;y1+=uy*11}if(lab[b.b]){x2-=ux*11;y2-=uy*11}
  const offs=b.o===1?[0]:b.o===2?[-3,3]:[-4.6,0,4.6];offs.forEach(o=>s+=`<line x1="${(x1+px*o).toFixed(1)}" y1="${(y1+py*o).toFixed(1)}" x2="${(x2+px*o).toFixed(1)}" y2="${(y2+py*o).toFixed(1)}" stroke="${col||'#2d3f4b'}" stroke-width="2.4" stroke-linecap="round"/>`)});return s}
function molSVG(g,o){o=o||{};const BL=o.bl||36,raw=layoutGraph(g),pos=raw.map(p=>({x:p.x*BL,y:p.y*BL})),adj=adjOf(g);
 const small=new Set();comps(g).forEach(c=>{if(c.atoms.length<=2)c.orig.forEach(o=>small.add(o))});
 const lab=g.atoms.map((a,i)=>a.el!=='C'||!adj[i].length||small.has(i));
 const body=bondsSVG(g,pos,lab)+g.atoms.map((_,i)=>atomLabel(g,adj,pos,i,small.has(i))).join('');
 const xs=pos.map(p=>p.x),ys=pos.map(p=>p.y),pad=o.pad||22;const x0=Math.min(...xs)-pad-14,x1=Math.max(...xs)+pad+20,y0=Math.min(...ys)-pad,y1=Math.max(...ys)+pad;
 const w=x1-x0,h=y1-y0,sc=o.scale||1;
 return `<svg class="mol" viewBox="${x0.toFixed(0)} ${y0.toFixed(0)} ${w.toFixed(0)} ${h.toFixed(0)}" width="${(w*sc).toFixed(0)}" height="${(h*sc).toFixed(0)}" role="img" aria-label="${esc(o.alt||'Skeletal structure')}" xmlns="http://www.w3.org/2000/svg">${body}</svg>`}
/* condensed structural formula */
function condensedStr(g){const adj=adjOf(g);if(ringOf(g,adj))return null;
 const txt=(i,first,more)=>{const a=g.atoms[i],h=hCount(g,adj,i),hs=h?'H'+(h>1?h:''):'';const q=a.charge>0?'⁺':a.charge<0?'⁻':'';
  if(a.el==='C')return 'C'+hs;if(first&&more&&h)return hs+a.el+q;return a.el+hs+q};
 const bs=o=>o===2?'=':o===3?'≡':'';
 function seg(path,parent){let s='';path.forEach((c,k)=>{if(k>0)s+=bs(adj[c].find(x=>x.n===path[k-1]).o);
   s+=txt(c,k===0&&parent===undefined,path.length>1);
   adj[c].filter(x=>x.n!==path[k-1]&&x.n!==path[k+1]&&x.n!==parent).forEach(x=>{s+='('+bs(x.o)+seg(branchPath(x.n,c),c)+')'})});return s}
 function branchPath(start,from){const p=[start];let cur=start,prv=from;while(true){const nx=adj[cur].filter(x=>x.n!==prv);if(nx.length!==1)break;
   const depth=nx.map(x=>x.n);prv=cur;cur=depth[0];p.push(cur)}return p}
 let s=seg(chainPath(g,adj));
 s=s.replace(/CH\(=O\)OH/g,'HCOOH').replace(/CH\(=O\)O/g,'HCOO').replace(/C\(=O\)OH/g,'COOH').replace(/C\(=O\)O⁻/g,'COO⁻').replace(/C\(=O\)O/g,'COO').replace(/C\(=O\)N/g,'CON').replace(/C\(=O\)/g,'CO').replace(/CH=O$/,'CHO').replace(/CH2=O$/,'HCHO');
 const rv=t=>(t.match(/CH\d?|C/g)||[]).reverse().join('');
 s=s.replace(/^O=CHOH$/,'HCOOH').replace(/^O=CHO⁻$/,'HCOO⁻').replace(/^O=CHO(.+)$/,'HCOO$1').replace(/^O=CHNH(.*)$/,'HCONH$1').replace(/^O=CH(.+)$/,'HCO$1').replace(/^(C[CH\d]*)OCHO$/,(m,a)=>'HCOO'+rv(a)).replace(/^(C[CH\d]*)NHCHO$/,(m,a)=>'HCONH'+rv(a));
 return s}
const condHTML=s=>esc(s).replace(/([A-Za-z\)])(\d+)/g,'$1<sub>$2</sub>').replace(/([⁺⁻])/g,'<sup>$1</sup>').replace(/⁺/g,'+').replace(/⁻/g,'−');
function expandedSVG(g,o){o=o||{};const adj=adjOf(g);if(ringOf(g,adj)||comps(g).length>1)return null;
 const n=g.atoms.length,path=chainPath(g,adj),onP=new Set(path),pos=new Array(n),occ=new Map(),Hs=[];let ok=true;
 const K=(x,y)=>x+','+y;const put=(i,x,y)=>{if(occ.has(K(x,y))){ok=false;return false}occ.set(K(x,y),i);pos[i]={x,y};return true};
 const putH=(i,x,y)=>{if(occ.has(K(x,y))){ok=false;return}occ.set(K(x,y),'H');Hs.push({x,y,i})};
 const hb=i=>adj[i].some(e=>!onP.has(e.n));let x=0;
 path.forEach((c,k)=>{if(k)x+=(hb(path[k-1])||hb(c))?2:1;put(c,x,0)});
 function grow(i,par,dx,dy){const kids=adj[i].filter(e=>e.n!==par&&!pos[e.n]);const dirs=[[dx,dy],[dy,dx],[-dy,-dx]];const used=[];
  kids.forEach((e,j)=>{const d=dirs[j];if(!d){ok=false;return}used.push(j);if(put(e.n,pos[i].x+d[0],pos[i].y+d[1]))grow(e.n,i,d[0],d[1])});
  let h=hCount(g,adj,i);dirs.forEach((d,j)=>{if(h>0&&!used.includes(j)){putH(i,pos[i].x+d[0],pos[i].y+d[1]);h--}});if(h>0)ok=false}
 path.forEach((c,k)=>{const last=k===path.length-1;const slots=[[0,-1],[0,1]];const ends=[];if(k===0)ends.push([-1,0]);if(last)ends.push([1,0]);
  const br=adj[c].filter(e=>!onP.has(e.n));br.forEach((e,j)=>{const d=slots[j]||ends[j-2];if(!d){ok=false;return}if(put(e.n,pos[c].x+d[0],d[1]))grow(e.n,c,d[0],d[1])});
  const free=(g.atoms[c].el==='C'?[...slots.slice(br.length),...ends]:[...ends,...slots.slice(br.length)]);let h=hCount(g,adj,c);
  free.forEach(d=>{if(h>0){putH(c,pos[c].x+d[0],pos[c].y+d[1]);h--}});if(h>0)ok=false});
 if(!ok)return null;
 const U=o.u||40,P=q=>({x:q.x*U,y:q.y*U});const line=(a,b,ord)=>{const A=P(a),B=P(b);const dx=B.x-A.x,dy=B.y-A.y,l=Math.hypot(dx,dy),ux=dx/l,uy=dy/l,px=-uy,py=ux;const s1=11,x1=A.x+ux*s1,y1=A.y+uy*s1,x2=B.x-ux*s1,y2=B.y-uy*s1;
  return (ord===1?[0]:ord===2?[-3.2,3.2]:[-4.8,0,4.8]).map(f=>`<line x1="${(x1+px*f).toFixed(1)}" y1="${(y1+py*f).toFixed(1)}" x2="${(x2+px*f).toFixed(1)}" y2="${(y2+py*f).toFixed(1)}" stroke="#2d3f4b" stroke-width="2.2" stroke-linecap="round"/>`).join('')};
 let body='';g.bonds.forEach(b=>body+=line(pos[b.a],pos[b.b],b.o));Hs.forEach(h=>body+=line(pos[h.i],h,1));
 const T=(q,t,col,ch)=>{const c=P(q);return `<text x="${c.x}" y="${c.y+6.5}" text-anchor="middle" font-size="19" font-weight="800" font-family="Inter,Helvetica,Arial,sans-serif" fill="${col}">${t}</text>`+(ch?`<text x="${c.x+9}" y="${c.y-5}" font-size="14" font-weight="900" fill="${col}">${ch>0?'+':'−'}</text>`:'')};
 g.atoms.forEach((a,i)=>body+=T(pos[i],a.el,ECOL[a.el]||'#2d3f4b',a.charge));Hs.forEach(h=>body+=T(h,'H','#55687a'));
 const all=[...pos,...Hs].map(P),xs=all.map(q=>q.x),ys=all.map(q=>q.y),pad=18;const x0=Math.min(...xs)-pad,y0=Math.min(...ys)-pad,w=Math.max(...xs)-x0+pad+6,h=Math.max(...ys)-y0+pad;const sc=o.scale||.85;
 return `<svg class="mol" viewBox="${x0} ${y0} ${w} ${h}" width="${(w*sc).toFixed(0)}" height="${(h*sc).toFixed(0)}" role="img" aria-label="Expanded structural formula" xmlns="http://www.w3.org/2000/svg">${body}</svg>`}
function structHTML(smi,style,scale){const g=parseSmi(smi);if(style==='expanded'){const e=expandedSVG(g,{scale:scale||.8});if(e)return e}if(style==='condensed'){const c=condensedStr(g);if(c)return `<div class="condensed">${condHTML(c)}</div>`}return molSVG(g,{scale:scale||.85})}

/* ================= compound library ================= */
const ST=['','meth','eth','prop','but','pent','hex','hept','oct'];
const XN={Cl:'chloro',Br:'bromo'};
const lin=(n,subs,mult)=>{subs=subs||{};mult=mult||{};let s='';for(let i=1;i<=n;i++){s+='C';(subs[i]||[]).forEach(x=>s+='('+x+')');if(i<n)s+=mult[i]===2?'=':mult[i]===3?'#':''}return s};
const C=(smi,name)=>({smi,name});
const alkane=n=>C(lin(n),ST[n]+'ane');
const alkene=(n,p)=>{p=Math.min(p,n-p);return C(lin(n,{},{[p]:2}),n===2?'ethene (ethylene)':n===3?'propene':`${p}-${ST[n]}ene`)};
const alkyne=(n,p)=>{p=Math.min(p,n-p);return C(lin(n,{},{[p]:3}),n===2?'ethyne (acetylene)':n===3?'propyne':`${p}-${ST[n]}yne`)};
const alcohol=(n,p)=>{p=Math.min(p,n+1-p);return C(lin(n,{[p]:['O']}),n===1?'methanol':n===2?'ethanol':n===3&&p===2?'2-propanol (isopropyl alcohol)':`${p}-${ST[n]}anol`)};
const halo=(n,p,X)=>{p=Math.min(p,n+1-p);return C(lin(n,{[p]:[X]}),n<=2?XN[X]+ST[n]+'ane':`${p}-${XN[X]}${ST[n]}ane`)};
const dihalo=(n,p,X)=>C(lin(n,{[p]:[X],[p+1]:[X]}),n===2?`1,2-di${XN[X]}ethane`:`${p},${p+1}-di${XN[X]}${ST[n]}ane`);
const aldehyde=n=>n===1?C('C=O','methanal (formaldehyde)'):C(lin(n,{[n]:['=O']}),n===2?'ethanal (acetaldehyde)':ST[n]+'anal');
const ketone=(n,p)=>{p=Math.min(p,n+1-p);return C(lin(n,{[p]:['=O']}),n===3?'propanone (acetone)':n===4?'2-butanone':`${p}-${ST[n]}anone`)};
const acid=n=>C(lin(n,{[n]:['=O','O']}),n===1?'methanoic acid (formic acid)':n===2?'ethanoic acid (acetic acid)':ST[n]+'anoic acid');
const carbox=n=>C(lin(n,{[n]:['=O','[O-]']}),n===1?'methanoate (formate) ion':n===2?'ethanoate (acetate) ion':ST[n]+'anoate ion');
const saltName=n=>n===1?'sodium methanoate (sodium formate)':n===2?'sodium ethanoate (sodium acetate)':`sodium ${ST[n]}anoate`;
const ester=(a,b)=>C(lin(a,{[a]:['=O']})+'O'+'C'.repeat(b),`${ST[b]}yl ${ST[a]}anoate`);
const amide=(a,r)=>r==='dm'?C(lin(a,{[a]:['=O']})+'N(C)C',`N,N-dimethyl${ST[a]}anamide`):C(lin(a,{[a]:['=O']})+'N'+'C'.repeat(r),(r?`N-${ST[r]}yl`:'')+(a===2&&!r?'ethanamide (acetamide)':ST[a]+'anamide'));
const AMINES=[{smi:'CN',name:'methylamine',ion:C('C[NH3+]','methylammonium ion'),salt:'methylammonium chloride',r:1},{smi:'CCN',name:'ethylamine',ion:C('CC[NH3+]','ethylammonium ion'),salt:'ethylammonium chloride',r:2},{smi:'CCCN',name:'propylamine',ion:C('CCC[NH3+]','propylammonium ion'),salt:'propylammonium chloride',r:3},{smi:'CNC',name:'dimethylamine',ion:C('C[NH2+]C','dimethylammonium ion'),salt:'dimethylammonium chloride',r:0}];
const CY={ane:C('C1CCCCC1','cyclohexane'),ene:C('C1=CCCCC1','cyclohexene'),ol:C('OC1CCCCC1','cyclohexanol'),one:C('O=C1CCCCC1','cyclohexanone'),Cl:C('ClC1CCCCC1','chlorocyclohexane'),Br:C('BrC1CCCCC1','bromocyclohexane'),di:X=>C(`${X}C1CCCCC1${X}`,`1,2-di${XN[X]}cyclohexane`)};
const IB={ene:C('C=C(C)C','2-methylpropene'),ane:C('CC(C)C','2-methylpropane'),ol:C('CC(C)(C)O','2-methyl-2-propanol (tert-butyl alcohol)'),ol1:C('CC(C)CO','2-methyl-1-propanol'),hx:X=>C(`CC(C)(C)${X}`,`2-${XN[X]}-2-methylpropane`),x2:X=>C(`${X}CC(C)(C)${X}`,`1,2-di${XN[X]}-2-methylpropane`)};
const T=t=>({t});
const ALKOXY=['','methoxy','ethoxy'];
const hemiacetal=(n,m)=>C(lin(n,{[n]:['O','O'+'C'.repeat(m)]}),n===2?`1-${ALKOXY[m]}ethanol`:`1-${ALKOXY[m]}-1-${ST[n]}anol`);
const acetal=(n,m)=>C(lin(n,{[n]:['O'+'C'.repeat(m),'O'+'C'.repeat(m)]}),`1,1-di${ALKOXY[m]}${ST[n]}ane`);
const hemiketal=m=>C(`CC(C)(O)O${'C'.repeat(m)}`,`2-${ALKOXY[m]}-2-propanol`);
const ketal=m=>C(`CC(C)(O${'C'.repeat(m)})O${'C'.repeat(m)}`,`2,2-di${ALKOXY[m]}propane`);
const MB={ol:C('CC(C)(O)CC','2-methyl-2-butanol'),ol3:C('CC(C)C(O)C','3-methyl-2-butanol'),ene:C('CC(C)=CC','2-methyl-2-butene')};
/* alkenes used in addition reactions. mk: Markovnikov product is a single compound; rv: reverse question has a clear answer set */
const ALK=[
 {alk:alkene(2,1),h2:alkane(2),hx:X=>halo(2,1,X),oh:alcohol(2,1),x2:X=>dihalo(2,1,X),mk:1,rv:1,alts:[alkene(2,1)],straight:2},
 {alk:alkene(3,1),h2:alkane(3),hx:X=>halo(3,2,X),oh:alcohol(3,2),x2:X=>dihalo(3,1,X),mk:1,rv:1,alts:[alkene(3,1)],straight:3},
 {alk:alkene(4,1),h2:alkane(4),hx:X=>halo(4,2,X),oh:alcohol(4,2),x2:X=>dihalo(4,1,X),mk:1,rv:1,alts:[alkene(4,1),alkene(4,2)],straight:4},
 {alk:alkene(4,2),h2:alkane(4),hx:X=>halo(4,2,X),oh:alcohol(4,2),x2:X=>dihalo(4,2,X),mk:1,rv:1,alts:[alkene(4,1),alkene(4,2)],straight:4},
 {alk:alkene(5,1),h2:alkane(5),hx:X=>halo(5,2,X),oh:alcohol(5,2),x2:X=>dihalo(5,1,X),mk:1,rv:0,straight:5},
 {alk:alkene(5,2),h2:alkane(5),x2:X=>dihalo(5,2,X),mk:0,straight:5},
 {alk:alkene(6,1),h2:alkane(6),hx:X=>halo(6,2,X),oh:alcohol(6,2),x2:X=>dihalo(6,1,X),mk:1,rv:0,straight:6},
 {alk:alkene(6,2),h2:alkane(6),x2:X=>dihalo(6,2,X),mk:0,straight:6},
 {alk:alkene(6,3),h2:alkane(6),hx:X=>halo(6,3,X),oh:alcohol(6,3),x2:X=>dihalo(6,3,X),mk:1,rv:0,straight:6},
 {alk:CY.ene,h2:CY.ane,hx:X=>CY[X],oh:CY.ol,x2:X=>CY.di(X),mk:1,rv:1,alts:[CY.ene],h2alts:[CY.ene]},
 {alk:IB.ene,h2:IB.ane,hx:X=>IB.hx(X),oh:IB.ol,x2:X=>IB.x2(X),mk:1,rv:1,alts:[IB.ene],h2alts:[IB.ene]}];
const h2Alts=e=>e.straight?Array.from({length:Math.floor(e.straight/2)},(_,k)=>alkene(e.straight,k+1)):e.h2alts;

/* ================= reaction templates ================= */
/* each returns {key,type,cls,set,reactants,cond,products,draw:[idx],rev:{idx,alts,prompt}|null,rule,hint,salt} */
const MK='Markovnikov’s rule: the H adds to the C=C carbon that already has more H atoms, so the new group ends up on the more substituted carbon.';
const TPL={
 combustion(){const u=Math.random();const c=u<.12?{f:C('C1CCCCC1','cyclohexane'),C:6,H:12,O:0}:u<.35?(n=>({f:alcohol(n,1),C:n,H:2*n+2,O:1}))(rnd(1,3)):(n=>({f:alkane(n),C:n,H:2*n+2,O:0}))(rnd(1,8));
  let a=1,o=(2*c.C+c.H/2-c.O)/2,co=c.C,w=c.H/2;if(o%1){a*=2;o*=2;co*=2;w*=2}
  return {type:'Combustion',cls:'Combustion',set:'hydrocarbon',reactants:[{...c.f,coef:a>1?a:''},T(`${o} O₂`)],cond:'spark',products:[T(`${co} CO₂`),T(`${w} H₂O`)],draw:null,rev:null,
   rule:`Combustion: ${c.O?'an alcohol':'a hydrocarbon'} burns in O₂ to make CO₂ and H₂O and releases energy. Every C–H and C–C bond is broken, so the carbon chain does not survive.`,hint:'Look at the products: only CO₂ and H₂O, made from an organic compound and oxygen.'}},
 substitution(){const X=pick(['Cl','Br']);const r=pick([[alkane(1),halo(1,1,X)],[alkane(2),halo(2,1,X)],[CY.ane,CY[X]]]);
  return {type:'Halogenation (substitution)',cls:'Substitution',set:'hydrocarbon',reactants:[r[0],T(X+'₂')],cond:'light (hν)',products:[r[1],T('H'+X)],draw:[0],rev:{idx:[0],prompt:`Draw the alkane that reacted with ${X}₂ in light to give ${r[1].name}.`},
   rule:`Halogenation of an alkane is a substitution: light breaks the ${X}–${X} bond and one H on the alkane is replaced by ${X}. The H that leaves ends up in H${X}.`,hint:`Swap one H on the alkane for a ${X} atom. The carbon skeleton does not change.`}},
 hydrogenation(){if(Math.random()<.25){const r=pick([[2,1],[3,1],[4,1],[4,2],[5,2]]);const yne=alkyne(...r),ane=alkane(r[0]);
   return {type:'Hydrogenation',cls:'Addition',excl:['Reduction'],set:'hydrocarbon',reactants:[yne,T('2 H₂')],cond:'Pt or Ni',products:[ane],draw:[0],rev:null,
    rule:'Hydrogenation of an alkyne: two H₂ molecules add across the C≡C (two H atoms on each carbon), so the alkyne becomes an alkane with the same carbon skeleton.',hint:'H₂ adds across the multiple bond until every carbon is saturated (single bonds only).'}}
  const e=pick(ALK),alts=h2Alts(e);
  return {type:'Hydrogenation',cls:'Addition',excl:['Reduction'],set:'hydrocarbon',reactants:[e.alk,T('H₂')],cond:'Pt or Ni',products:[e.h2],draw:[0],
   rev:{idx:[0],alts:alts.map(a=>[a.smi]),prompt:`Draw an alkene that reacts with H₂ (Pt) to give ${e.h2.name}.${alts.length>1?' Any correct position of the C=C counts.':''}`},
   rule:'Hydrogenation is an addition: H₂ adds across the C=C, one H to each carbon. The double bond becomes a single bond and the alkene becomes an alkane.',hint:'H₂ with a Pt or Ni catalyst adds one H to each carbon of the C=C. Keep the same carbon skeleton.'}},
 halogenAdd(){const e=pick(ALK),X=pick(['Br','Cl']),p=e.x2(X);
  return {type:'Halogenation (addition)',cls:'Addition',set:'hydrocarbon',reactants:[e.alk,T(X+'₂')],cond:'',products:[p],draw:[0],rev:{idx:[0],alts:[[e.alk.smi]],prompt:`Draw the alkene that reacts with ${X}₂ to give ${p.name}.`},
   rule:`Halogenation of an alkene is an addition: the ${X}–${X} bond breaks and one ${X} adds to each carbon of the C=C. The two ${X} atoms end up on neighboring carbons.`,hint:`Erase the second line of the C=C and put one ${X} on each of those two carbons.`}},
 hydrohalogenation(){const e=pick(ALK.filter(a=>a.mk)),X=pick(['Cl','Br']),p=e.hx(X);
  return {type:'Hydrohalogenation',cls:'Addition',set:'hydrocarbon',reactants:[e.alk,T('H'+X)],cond:'',products:[p],draw:[0],
   rev:e.rv?{idx:[0],alts:e.alts.map(a=>[a.smi]),prompt:`Draw an alkene that reacts with H${X} to give ${p.name} as the major product.${e.alts.length>1?' Either correct alkene counts.':''}`}:null,
   rule:`Hydrohalogenation is an addition: H and ${X} add across the C=C. ${MK}`,hint:`H${X} adds H to one C=C carbon and ${X} to the other. Put the ${X} on the carbon with fewer H atoms.`}},
 hydration(){const e=pick(ALK.filter(a=>a.mk)),p=e.oh;
  return {type:'Hydration',cls:'Addition',set:'alcohol',reactants:[e.alk,T('H₂O')],cond:'H⁺ (H₂SO₄)',products:[p],draw:[0],
   rev:e.rv?{idx:[0],alts:e.alts.map(a=>[a.smi]),prompt:`Draw an alkene that reacts with H₂O (H⁺) to give ${p.name} as the major product.${e.alts.length>1?' Either correct alkene counts.':''}`}:null,
   rule:`Hydration is an addition: water adds across the C=C as H and OH, making an alcohol. ${MK}`,hint:'Water adds as H– and –OH across the double bond. The OH goes on the C=C carbon with fewer H atoms.'}},
 dehydration(){const r=pick([{al:alcohol(2,1),ene:alkene(2,1),alts:[alcohol(2,1)]},{al:alcohol(3,1),ene:alkene(3,1),alts:[alcohol(3,1),alcohol(3,2)]},{al:alcohol(3,2),ene:alkene(3,1),alts:[alcohol(3,1),alcohol(3,2)]},{al:CY.ol,ene:CY.ene,alts:[CY.ol]},{al:IB.ol,ene:IB.ene,alts:[IB.ol,IB.ol1]},{al:alcohol(5,3),ene:alkene(5,2),alts:[alcohol(5,3),alcohol(5,2)]},{al:MB.ol,ene:MB.ene,alts:[MB.ol,MB.ol3]}]);
  return {type:'Dehydration',cls:'Elimination',set:'alcohol',reactants:[r.al],cond:'H₂SO₄, heat',products:[r.ene,T('H₂O')],draw:[0],
   rev:{idx:[0],alts:r.alts.map(a=>[a.smi]),prompt:`Draw an alcohol that loses water (H₂SO₄, heat) to give ${r.ene.name} as the major product.${r.alts.length>1?' Any correct alcohol counts.':''}`},
   rule:'Dehydration is an elimination: the –OH and an H from the neighboring carbon leave together as H₂O, and a C=C forms between those two carbons. (When there is a choice, the C=C forms toward the carbon with fewer H atoms.)',hint:'Remove the OH and one H from the carbon next door, then draw a C=C between those two carbons.'}},
 ox1Ald(){const n=rnd(1,6),a=alcohol(n,1),p=aldehyde(n);
  return {type:'Oxidation',cls:'Oxidation',set:'alcohol',reactants:[a],cond:'[O] (mild)',products:[p],draw:[0],rev:{idx:[0],prompt:`Draw the alcohol that was oxidized (mild [O]) to give ${p.name}.`},
   rule:'Oxidation of a primary (1°) alcohol: the carbon bearing –OH loses two H atoms (one from O, one from C) and forms C=O. A mild oxidizing agent stops at the aldehyde.',hint:'A 1° alcohol (–CH₂OH) becomes an aldehyde (–CHO). Keep the same number of carbons.'}},
 ox1Acid(){const n=rnd(1,6),a=alcohol(n,1),p=acid(n);
  return {type:'Oxidation',cls:'Oxidation',set:'alcohol',reactants:[a],cond:'excess [O] (K₂Cr₂O₇)',products:[p],draw:[0],rev:{idx:[0],prompt:`Draw the alcohol that was fully oxidized (excess [O]) to give ${p.name}.`},
   rule:'With excess oxidizing agent a primary (1°) alcohol is oxidized twice: alcohol → aldehyde → carboxylic acid. The end carbon becomes –COOH.',hint:'Excess [O] keeps going past the aldehyde. The –CH₂OH carbon ends up as –COOH.'}},
 oxAldAcid(){const n=rnd(1,6),a=aldehyde(n),p=acid(n);
  return {type:'Oxidation',cls:'Oxidation',set:'alcohol',reactants:[a],cond:'[O]',products:[p],draw:[0],rev:{idx:[0],prompt:`Draw the aldehyde that was oxidized to give ${p.name}.`},
   rule:'Oxidation of an aldehyde: the H on the carbonyl carbon is replaced by OH, so –CHO becomes –COOH (a carboxylic acid). Ketones have no H there and resist oxidation.',hint:'Aldehydes oxidize easily: add an O to the –CHO carbon to make –COOH.'}},
 ox2(){const r=pick([[3,2],[4,2],[5,2],[5,3],[6,2],[6,3],'cy']);const a=r==='cy'?CY.ol:alcohol(...r),p=r==='cy'?CY.one:ketone(...r);
  return {type:'Oxidation',cls:'Oxidation',set:'alcohol',reactants:[a],cond:'[O]',products:[p],draw:[0],rev:{idx:[0],prompt:`Draw the alcohol that was oxidized to give ${p.name}.`},
   rule:'Oxidation of a secondary (2°) alcohol: the carbon bearing –OH loses its H, and the C–OH becomes C=O, giving a ketone. (A 3° alcohol has no H on that carbon and does not oxidize.)',hint:'A 2° alcohol becomes a ketone. Turn the C–OH into C=O on the same carbon.'}},
 reduction(){const ald=Math.random()<.45;let s,p;
  if(ald){const n=rnd(1,5);s=aldehyde(n);p=alcohol(n,1)}else{const r=pick([[3,2],[4,2],[5,2],[5,3],[6,3],'cy']);s=r==='cy'?CY.one:ketone(...r);p=r==='cy'?CY.ol:alcohol(...r)}
  return {type:'Reduction',cls:'Reduction',excl:['Hydrogenation','Addition'],set:'alcohol',reactants:[s,T('H₂')],cond:'Ni',products:[p],draw:[0],rev:{idx:[0],prompt:`Draw the aldehyde or ketone that was reduced (H₂, Ni) to give ${p.name}.`},
   rule:`Reduction of a carbonyl: H₂ adds across the C=O, turning it into C–OH. An aldehyde gives a 1° alcohol and a ketone gives a 2° alcohol. This is the reverse of alcohol oxidation.`,hint:'H₂ adds one H to the C and one H to the O of the C=O. The C=O becomes C–OH on the same carbon.'}},
 esterification(){const a=rnd(1,4),b=rnd(1,4),ac=acid(a),al=alcohol(b,1),es=ester(a,b);
  return {type:'Esterification',cls:'Condensation',set:'acid',reactants:[ac,al],cond:'H⁺, heat',products:[es,T('H₂O')],draw:[0],rev:{idx:[0,1],prompt:`${cap(es.name)} was made by esterification. Draw the carboxylic acid AND the alcohol that were used, as two separate molecules.`},
   rule:`Esterification is a condensation: the acid loses its –OH and the alcohol loses the H from its –OH, together making H₂O. The new C–O bond joins them. In the name, the alcohol part comes first (${ST[b]}yl) and the acid part ends in -oate (${ST[a]}anoate).`,hint:'Remove –OH from the acid and –H from the alcohol, then join the acid’s C=O carbon to the alcohol’s O.'}},
 esterHydrolysis(){const a=rnd(1,4),b=rnd(1,4),es=ester(a,b),ac=acid(a),al=alcohol(b,1);
  return {type:'Hydrolysis',cls:'Hydrolysis',set:'acid',reactants:[es,T('H₂O')],cond:'H⁺, heat',products:[ac,al],draw:[0,1],rev:{idx:[0],prompt:`Acid hydrolysis gave ${ac.name} and ${al.name}. Draw the ester that was hydrolyzed.`},
   rule:'Acid hydrolysis of an ester is the reverse of esterification: water splits the C–O bond next to the C=O. The carbonyl side becomes a carboxylic acid and the O–alkyl side becomes an alcohol.',hint:'Break the single C–O bond next to the C=O. Add OH to the carbonyl carbon and H to the other O.'}},
 saponification(){const a=rnd(1,4),b=rnd(1,4),es=ester(a,b),cx=carbox(a),al=alcohol(b,1);
  return {type:'Saponification',cls:'Hydrolysis',excl:['Hydrolysis'],set:'acid',reactants:[es,T('NaOH')],cond:'heat',products:[cx,T('Na⁺'),al],draw:[0,2],salt:saltName(a),rev:{idx:[0],prompt:`Heating an ester with NaOH gave ${saltName(a)} and ${al.name}. Draw the ester.`},
   rule:`Saponification is the hydrolysis of an ester in base (NaOH). The C–O bond next to the C=O breaks: the acid part comes out as its carboxylate salt (${saltName(a)}) and the O–alkyl part becomes an alcohol. This is how soap is made from fats.`,hint:'Same split as ester hydrolysis, but in base the acid part ends up as –COO⁻ (with Na⁺). Use ± Charge to put a − on the O.'}},
 amidation(){const a=rnd(1,4),am=Math.random()<.4?null:pick([AMINES[0],AMINES[1],AMINES[3]]);const ac=acid(a),pr=amide(a,am?(am.r||'dm'):0);
  return {type:'Amidation',cls:'Condensation',set:'acid',reactants:am?[ac,C(am.smi,am.name)]:[ac,T('NH₃')],cond:'heat',products:[pr,T('H₂O')],draw:[0],
   rev:am?{idx:[0,1],prompt:`${cap(pr.name)} was made from a carboxylic acid and an amine. Draw both, as two separate molecules.`}:{idx:[0],prompt:`${cap(pr.name)} was made by heating a carboxylic acid with NH₃. Draw the carboxylic acid.`},
   rule:`Amidation is a condensation: the acid loses –OH and the ${am?'amine':'ammonia'} loses an H from N, together making H₂O. The new C–N bond makes an amide${am?`; the group on N is named with N- (${pr.name})`:''}.`,hint:'Replace the –OH of the acid with the N of the amine (keeping its other groups). Water is the other product.'}},
 amideHydrolysis(){const a=rnd(1,4),r=Math.random()<.5?0:1,am=amide(a,r),ac=acid(a);
  return {type:'Hydrolysis',cls:'Hydrolysis',set:'acid',reactants:[am,T('H₂O'),T('H⁺')],cond:'heat',products:r?[ac,AMINES[0].ion]:[ac,T('NH₄⁺')],draw:r?[0,1]:[0],
   rev:{idx:[0],prompt:`Acid hydrolysis gave ${ac.name} and ${r?'the methylammonium ion':'NH₄⁺'}. Draw the amide that was hydrolyzed.`},
   rule:`Hydrolysis of an amide: water breaks the C–N bond. The carbonyl side becomes a carboxylic acid; in acid the nitrogen part picks up H⁺ and comes out as ${r?'an ammonium ion (CH₃NH₃⁺)':'NH₄⁺'}.`,hint:`Break the C–N bond next to the C=O. The carbonyl carbon gets an OH${r?'; the N part becomes CH₃NH₃⁺ (use ± Charge on N)':''}.`}},
 amideBase(){const a=rnd(1,4),r=pick([0,1,1,2]),am=amide(a,r),cx=carbox(a),amn=r?C(AMINES[r-1].smi,AMINES[r-1].name):null;
  return {type:'Hydrolysis',cls:'Hydrolysis',excl:['Saponification'],set:'acid',reactants:[am,T('NaOH')],cond:'heat',products:r?[cx,T('Na⁺'),amn]:[cx,T('Na⁺'),T('NH₃')],draw:r?[0,2]:[0],salt:saltName(a),
   rev:{idx:[0],prompt:`Base hydrolysis (NaOH) gave ${saltName(a)} and ${r?amn.name:'NH₃'}. Draw the amide that was hydrolyzed.`},
   rule:`Base hydrolysis of an amide: OH⁻ breaks the C–N bond. The carbonyl side comes out as a carboxylate salt (${saltName(a)}) and the nitrogen side comes out as ${r?'an amine ('+amn.name+')':'ammonia (NH₃)'}. (In acid you get the carboxylic acid and an ammonium salt instead.)`,hint:'Break the C–N bond next to the C=O. In base the acid part becomes –COO⁻ (use ± Charge) and the N part becomes a neutral amine.'}},
 hemiacetal(){const ket=Math.random()<.3,m=rnd(1,2);let c,p,nm;if(ket){c=ketone(3,2);p=hemiketal(m)}else{const n=rnd(2,4);c=aldehyde(n);p=hemiacetal(n,m)}const al=alcohol(m,1);
  return {type:'Hemiacetal formation',cls:'Addition',noClass:true,set:'alcohol',reactants:[c,al],cond:'H⁺',products:[p],draw:[0],rev:{idx:[0,1],prompt:`${cap(p.name)} is a hemiacetal. Draw the ${ket?'ketone':'aldehyde'} AND the alcohol that formed it, as two separate molecules.`},
   rule:'Hemiacetal formation: one alcohol adds across the C=O. The alcohol’s O bonds to the carbonyl carbon and its H goes to the carbonyl O, so that carbon ends up with an –OH and an –OR. Sugars such as glucose form cyclic hemiacetals this way.',hint:'Turn the C=O into C–OH, and attach the alcohol’s –O–R group to that same carbon.'}},
 acetal(){const ket=Math.random()<.3,m=rnd(1,2);let c,p;if(ket){c=ketone(3,2);p=ketal(m)}else{const n=rnd(2,4);c=aldehyde(n);p=acetal(n,m)}const al=alcohol(m,1);
  return {type:'Acetal formation',cls:'Condensation',noClass:true,set:'alcohol',reactants:[c,{...al,coef:2}],cond:'H⁺',products:[p,T('H₂O')],draw:[0],rev:{idx:[0,1],prompt:`${cap(p.name)} is an acetal. Draw the ${ket?'ketone':'aldehyde'} AND the alcohol that formed it, as two separate molecules (draw the alcohol once).`},
   rule:'Acetal formation: TWO alcohol molecules react with the C=O. The first makes a hemiacetal; the second replaces its –OH, releasing H₂O. The carbon ends up with two –OR groups and no –OH.',hint:'Remove the C=O oxygen (it leaves in water) and put two –O–R groups from the alcohol on that carbon.'}},
 neutralAcid(){const n=rnd(1,5),ac=acid(n),cx=carbox(n);
  return {type:'Neutralization',cls:'Acid–base',set:'acid',reactants:[ac,T('NaOH')],cond:'',products:[cx,T('Na⁺'),T('H₂O')],draw:[0],salt:saltName(n),rev:{idx:[0],prompt:`Draw the carboxylic acid that NaOH neutralized to give ${saltName(n)}.`},
   rule:`Neutralization: the base (OH⁻) removes the acidic H from –COOH, giving a carboxylate ion (–COO⁻) and water. With Na⁺ the salt is ${saltName(n)}.`,hint:'Only the H on the –COOH oxygen is removed. That O gets a − charge (use ± Charge).'}},
 neutralAmine(){const am=pick(AMINES);
  return {type:'Neutralization',cls:'Acid–base',set:'acid',reactants:[C(am.smi,am.name),T('HCl')],cond:'',products:[am.ion,T('Cl⁻')],draw:[0],salt:am.salt,rev:{idx:[0],prompt:`Draw the amine that reacted with HCl to give ${am.salt}.`},
   rule:`Amines are weak bases. The lone pair on N picks up H⁺ from HCl, making an ammonium ion (N⁺ with one more H) and Cl⁻. The salt is ${am.salt}.`,hint:'Add an H⁺ to the nitrogen: it now has four bonds and a + charge (use ± Charge on N).'}}
};
const cap=s=>s.charAt(0).toUpperCase()+s.slice(1);
const WEIGHT={combustion:1,substitution:2,hydrogenation:3,halogenAdd:2,hydrohalogenation:3,hydration:3,dehydration:3,ox1Ald:2,ox1Acid:2,oxAldAcid:1,ox2:3,reduction:3,esterification:3,esterHydrolysis:2,saponification:2,amidation:2,amideHydrolysis:2,amideBase:2,hemiacetal:2,acetal:2,neutralAcid:2,neutralAmine:2};
const SETOF={combustion:'hydrocarbon',substitution:'hydrocarbon',hydrogenation:'hydrocarbon',halogenAdd:'hydrocarbon',hydrohalogenation:'hydrocarbon',hydration:'alcohol',dehydration:'alcohol',ox1Ald:'alcohol',ox1Acid:'alcohol',oxAldAcid:'alcohol',ox2:'alcohol',reduction:'alcohol',esterification:'acid',esterHydrolysis:'acid',saponification:'acid',amidation:'acid',amideHydrolysis:'acid',amideBase:'acid',hemiacetal:'alcohol',acetal:'alcohol',neutralAcid:'acid',neutralAmine:'acid'};
function genRxn(filter,only){for(let tries=0;tries<200;tries++){const keys=Object.keys(TPL).filter(k=>!only||only.includes(k));
  const pool=[];keys.forEach(k=>{for(let i=0;i<WEIGHT[k];i++)pool.push(k)});let k=pick(pool);if(k===lastKey&&Math.random()<.8)continue;
  const r=TPL[k]();r.key=k;if(!filter||filter(r)){lastKey=k;return r}}return null}
let lastKey=null;

/* ================= names: accepted variants ================= */
const ACYL={methanoate:'formate',ethanoate:'acetate',propanoate:'propionate',butanoate:'butyrate',methanamide:'formamide',ethanamide:'acetamide',propanamide:'propionamide',butanamide:'butyramide',methanoic:'formic',ethanoic:'acetic',propanoic:'propionic',butanoic:'butyric',pentanoic:'valeric'};
const ALIAS={'methanol':['methyl alcohol','wood alcohol'],'ethanol':['ethyl alcohol','grain alcohol'],'1-propanol':['propyl alcohol','n-propyl alcohol','n-propanol'],'2-propanol':['isopropyl alcohol','isopropanol','rubbing alcohol'],'1-butanol':['butyl alcohol','n-butyl alcohol','n-butanol'],'2-butanol':['sec-butyl alcohol','sec-butanol'],'1-pentanol':['pentyl alcohol','n-pentanol'],'1-hexanol':['hexyl alcohol'],
 '2-methyl-2-propanol':['tert-butyl alcohol','t-butyl alcohol','tert-butanol','t-butanol'],'2-methyl-1-propanol':['isobutyl alcohol','isobutanol'],'2-methylpropene':['isobutylene','isobutene','2-methyl-1-propene'],'2-methylpropane':['isobutane'],'ethene':['ethylene'],'propene':['propylene'],'ethyne':['acetylene'],
 'methanal':['formaldehyde'],'ethanal':['acetaldehyde'],'propanal':['propionaldehyde'],'butanal':['butyraldehyde'],'propanone':['acetone','dimethyl ketone','2-propanone','propan-2-one'],'2-butanone':['butanone','methyl ethyl ketone','ethyl methyl ketone','mek'],'3-pentanone':['diethyl ketone'],'2-pentanone':['methyl propyl ketone'],
 'hexanoic acid':['caproic acid'],'chloromethane':['methyl chloride'],'bromomethane':['methyl bromide'],'chloroethane':['ethyl chloride'],'bromoethane':['ethyl bromide'],'2-chloropropane':['isopropyl chloride'],'2-bromopropane':['isopropyl bromide'],'2-bromo-2-methylpropane':['tert-butyl bromide','t-butyl bromide'],'2-chloro-2-methylpropane':['tert-butyl chloride','t-butyl chloride'],
 'methylamine':['methanamine','aminomethane'],'ethylamine':['ethanamine','aminoethane'],'propylamine':['1-propanamine','propan-1-amine','n-propylamine'],'dimethylamine':['n-methylmethanamine'],'chlorocyclohexane':['cyclohexyl chloride'],'bromocyclohexane':['cyclohexyl bromide'],'1,2-dibromoethane':['ethylene dibromide'],'1,2-dichloroethane':['ethylene dichloride'],'2,2-dimethoxypropane':['acetone dimethyl acetal']};
const normName=t=>String(t).toLowerCase().replace(/[‐‑‒–—―−]/g,'-').replace(/[\s\-,'’()_.]/g,'');
function nameSets(name){const full=new Set(),part=new Set();const prim=name.replace(/\s*\([^)]*\)/g,'').trim();const paren=(name.match(/\(([^)]*)\)/)||[])[1];
 const add=x=>full.add(x);add(prim);if(paren){add(paren);if(/ ion$/.test(prim))add(paren+' ion')}
 const m=prim.match(/^(.*?)(\d+)-(meth|eth|prop|but|pent|hex|hept|oct)(an)?(ol|one|ene|yne|amine)$/);
 if(m){const [,pre,loc,stem,an,suf]=m;add(`${pre.replace(/-$/,'')}${stem}${an||''}-${loc}-${suf}`);if(loc==='1'&&!pre)part.add(`${stem}${an||''}${suf}`)}
 const m2=prim.match(/^(.*)prop(ene|yne)$/);if(m2){add(`${m2[1]}prop-1-${m2[2]}`);if(!m2[1])add(`1-prop${m2[2]}`)}
 (ALIAS[prim]||[]).forEach(add);
 if(/ ion$/.test(prim)){const base=prim.replace(/ ion$/,'');add(base);if(/ate$/.test(base))add('sodium '+base);if(/ammonium$/.test(base))add(base+' chloride')}
 [...full].forEach(x=>{for(const k in ACYL){const re=new RegExp('(^|[^a-z]|yl)'+k);if(re.test(x))add(x.replace(re,'$1'+ACYL[k]))}});
 return {full:new Set([...full].map(normName)),part:new Set([...part].map(normName)),show:[...new Set([prim,...[...full].filter(x=>x!==prim)])].slice(0,5),prim}}
const ENDING={acid:['carboxylic acid','“-oic acid”'],carboxylate:['carboxylate ion','“-oate”'],ester:['ester','“alkyl …-oate”'],amide:['amide','“-amide”'],ammonium:['ammonium ion','“-ammonium”'],amine:['amine','“-amine”'],aldehyde:['aldehyde','“-al”'],ketone:['ketone','“-one”'],hemiacetal:['hemiacetal','“-ol” with an alkoxy prefix'],alcohol:['alcohol','“-ol”'],acetal:['acetal','“dialkoxy…-ane”'],alkene:['alkene','“-ene”'],alkyne:['alkyne','“-yne”'],halide:['alkyl halide','“-ane” with a chloro- or bromo- prefix'],ether:['ether','“-ane” with an alkoxy prefix'],alkane:['alkane','“-ane”']};
const GPRI=['acid','carboxylate','ester','amide','ammonium','amine','aldehyde','ketone','hemiacetal','alcohol','acetal','alkene','alkyne','halide','ether','alkane'];
function inputFamily(t){if(/oicacid$|icacid$/.test(t))return ['acid'];if(/amide$/.test(t))return ['amide'];if(/ammonium(ion|chloride)?$/.test(t))return ['ammonium'];if(/amine$/.test(t))return ['amine'];
 if(/(oate|ate)(ion)?$/.test(t))return ['ester','carboxylate'];if(/one$|ketone$/.test(t))return ['ketone'];if(/ol$|alcohol$/.test(t))return ['alcohol','hemiacetal'];if(/al$|aldehyde$/.test(t))return ['aldehyde'];
 if(/ene$|ylene$/.test(t))return ['alkene'];if(/yne$/.test(t))return ['alkyne'];if(/ane$/.test(t))return ['alkane','halide','ether','acetal'];return null}
function checkName(input,comp){const t=normName(input);if(!t)return {ok:false,msg:'Type a name first.'};const S=nameSets(comp.name);
 // Older 'n-' (normal) names like n-propanol are accepted, with a note. (N-methyl amine names are a different thing and get no note.)
 const typed=String(input).toLowerCase().trim().replace(/[‐‑‒–—―−]/g,'-').replace(/\s+/g,' ');
 const nNormal=/^n ?[- ] ?(propyl|butyl|pentyl|hexyl) ?(alcohol|amine)$|^n ?[- ] ?(propanol|butanol|pentanol|hexanol)$/.test(typed);
 if(S.full.has(t)&&nNormal)return {ok:true,note:`Technically correct: the “n-” (normal, meaning an unbranched chain) name is an older naming style. We don’t use it in CHEM 3B, so write the IUPAC name: <b>${esc(S.prim)}</b>.`};
 if(S.full.has(t))return {ok:true};if(S.part.has(t))return {ok:true,note:`Counted as correct. The complete name includes the locant: <b>${esc(S.prim)}</b>.`};
 const g=parseSmi(comp.smi),gl=gList(g),main=GPRI.find(k=>gl.includes(k))||'alkane',fam=inputFamily(t);
 const nod=x=>x.replace(/\d/g,'');if([...S.full].some(v=>nod(v)===nod(t)&&v!==t))return {ok:false,msg:'Almost! The chain and the ending are right. Check the locant number: which carbon is the group on? Number from the end closest to the group.'};
 if(fam&&!fam.includes(main))return {ok:false,msg:`Check the ending: this compound is ${an(ENDING[main][0])}, so its name should end in ${ENDING[main][1]}.`};
 if(main==='halide'&&!/chloro|bromo/.test(t))return {ok:false,msg:'This compound has a halogen. Name it as a chloro- or bromo- prefix with its locant number.'};
 if(main==='ester')return {ok:false,msg:'Check both parts of the ester name: the alkyl group on the O comes first (methyl, ethyl…), then the acid part ending in -oate. Count the carbons on each side of the –O–.'};
 const st=['meth','eth','prop','but','pent','hex','hept','oct'];const cn=g.atoms.filter(a=>a.el==='C').length;
 return {ok:false,msg:`The ending is right. Now check the parent chain length (meth 1, eth 2, prop 3, but 4, pent 5, hex 6) and the locant number that tells where the group is. This compound has ${cn} carbon${cn>1?'s':''} in total.`}}
function nameHintFor(comp){const g=parseSmi(comp.smi),gl=gList(g),main=GPRI.find(k=>gl.includes(k))||'alkane';const cn=g.atoms.filter(a=>a.el==='C').length;
 return `This compound is ${an(ENDING[main][0])}, so the name ends in ${ENDING[main][1]}. Find the longest chain that holds the group, count its carbons, and number from the end closest to the group. (Total carbons: ${cn}.)`}
const groupWord=p=>{const gl=gList(parseSmi(p.smi));const k=GPRI.find(x=>gl.includes(x))||'alkane';return ENDING[k][0]};

/* ================= question building ================= */
const SPEC=['Combustion','Halogenation (substitution)','Hydrogenation','Halogenation (addition)','Hydrohalogenation','Hydration','Dehydration','Oxidation','Reduction','Esterification','Amidation','Hydrolysis','Saponification','Neutralization','Hemiacetal formation','Acetal formation'];
const CONF={'Hydration':['Dehydration','Hydrolysis','Hydrogenation','Hydrohalogenation'],'Dehydration':['Hydration','Hydrolysis','Oxidation','Hydrogenation'],'Hydrogenation':['Hydration','Halogenation (addition)','Hydrohalogenation','Dehydration'],'Halogenation (addition)':['Halogenation (substitution)','Hydrohalogenation','Hydrogenation','Hydration'],'Halogenation (substitution)':['Halogenation (addition)','Hydrohalogenation','Combustion','Hydrogenation'],'Hydrohalogenation':['Halogenation (addition)','Hydration','Halogenation (substitution)','Hydrogenation'],'Oxidation':['Reduction','Dehydration','Hydration','Combustion'],'Reduction':['Oxidation','Hydration','Dehydration','Hydrolysis'],'Esterification':['Hydrolysis','Saponification','Amidation','Neutralization'],'Amidation':['Esterification','Hydrolysis','Neutralization','Saponification'],'Hydrolysis':['Esterification','Saponification','Hydration','Amidation'],'Saponification':['Neutralization','Esterification','Dehydration','Amidation'],'Neutralization':['Saponification','Esterification','Hydrolysis','Oxidation'],'Combustion':['Halogenation (substitution)','Hydrogenation','Dehydration','Reduction'],'Hemiacetal formation':['Acetal formation','Hydration','Esterification','Reduction'],'Acetal formation':['Hemiacetal formation','Esterification','Dehydration','Hydration']};
const CLS=['Addition','Substitution','Elimination','Oxidation','Reduction','Condensation','Hydrolysis','Acid–base','Combustion'];
const CLSD={Addition:'two reactants combine and atoms add across a double bond, so the C=C (or C=O) becomes a single bond.',Substitution:'one atom or group on the molecule is swapped for another.',Elimination:'a small molecule (here H₂O) is removed and a C=C double bond forms.',Oxidation:'the carbon gains bonds to oxygen and/or loses hydrogen.',Reduction:'the carbon gains hydrogen and/or loses bonds to oxygen.',Condensation:'two molecules join and a small molecule (H₂O) is released.',Hydrolysis:'water (or OH⁻) splits one molecule into two pieces.','Acid–base':'an H⁺ is transferred from an acid to a base, making a salt.',Combustion:'a hydrocarbon burns in O₂ to CO₂ and H₂O.'};
const SPECD={'Halogenation (substitution)':'an H on an alkane is replaced by a halogen.','Hydrogenation':'H₂ adds across C=C or C≡C.','Halogenation (addition)':'X₂ (Br₂ or Cl₂) adds across C=C.','Hydrohalogenation':'HX (HCl or HBr) adds across C=C.','Hydration':'H₂O adds across C=C to make an alcohol.','Dehydration':'an alcohol loses H₂O to make an alkene.','Oxidation':'an alcohol or aldehyde gains O / loses H.','Reduction':'a C=O gains H₂ to become an alcohol.','Esterification':'acid + alcohol → ester + water.','Amidation':'acid + amine (or NH₃) → amide + water.','Hydrolysis':'water splits an ester or amide into two parts.','Saponification':'NaOH splits an ester into a carboxylate salt and an alcohol.','Neutralization':'an acid and a base make a salt.','Combustion':'burning in O₂ gives CO₂ + H₂O.','Hemiacetal formation':'one alcohol adds to an aldehyde or ketone C=O.','Acetal formation':'two alcohols react with an aldehyde or ketone; H₂O is released.'};
const organic=parts=>parts.filter(p=>p.smi);
const namesOf=parts=>parts.filter(p=>p.smi).map(p=>p.name);
function mcType(r){const general=!r.noClass&&Math.random()<.4;const excl=r.excl||[];
 if(general){const ans=r.cls;const pool=shuf(CLS.filter(c=>c!==ans&&!excl.includes(c)));const opts=shuf([ans,...pool.slice(0,3)]);
  return {kind:'mc',prompt:'Which general class of reaction is this?',options:opts.map(o=>({key:o,html:esc(o)})),answer:ans,
   hint:'Compare reactants and products: did something add across a double bond, swap, leave as water, gain O, gain H, split with water, or transfer H⁺?',
   why:`<b>${esc(ans)}</b>: ${CLSD[ans]}${r.type.toLowerCase()!==ans.toLowerCase()?` Specifically, this is <b>${esc(r.type)}</b>.`:''}`}}
 const ans=r.type;const conf=shuf((CONF[ans]||[]).filter(c=>!excl.includes(c)));const rest=shuf(SPEC.filter(s=>s!==ans&&!conf.includes(s)&&!excl.includes(s)));
 const opts=shuf([ans,...conf.slice(0,2),...rest.slice(0,1)]);
 return {kind:'mc',prompt:'What type of reaction is this?',options:opts.map(o=>({key:o,html:esc(o)})),answer:ans,
  hint:'Look at what was added to the reactant, what left, and what happened to any double bonds or the C=O. The reagent above the arrow is a big clue.',
  why:`<b>${esc(ans)}</b> (${esc(r.cls.toLowerCase())}): ${esc(SPECD[ans])}`}}
const nameHint='Decode each name: stem = carbon count (meth 1, eth 2, prop 3, but 4, pent 5, hex 6); ending = group (-ane, -ene, -yne, -ol, -al, -one, -oic acid, -oate, -amine, -amide); the number = which carbon the group is on.';
function drawStepFor(parts,idx,altsOverride,promptText,hint,why){const tgt=idx.map(i=>parts[i]);const accept=altsOverride||[tgt.map(p=>p.smi)];
 const ions=tgt.some(p=>/[+-]\]/.test(p.smi));
 return {kind:'draw',prompt:promptText,accept,hint,why,ionNote:ions}}
function nameStep(comp,promptText,view,label,why){return {kind:'name',comp,prompt:promptText,view,label:label||'Name it',hint:nameHintFor(comp),why:why||''}}
function buildQuestion(mode){
 const canNameRe=r=>r.rev&&!r.rev.alts&&r.rev.idx.length===1;
 const ok=r=>mode==='identify'?true:mode==='reactant'?!!r.rev:mode==='name'?(!!r.draw||canNameRe(r)):!!r.draw;
 const r=genRxn(ok);const steps=[];const struct=Math.random()<.5;
 const orgP=organic(r.products);
 const prodWord=r.draw&&r.draw.length>1?'both organic products (two separate molecules)':'the organic product';
 const prodPrompt=r.draw?`Draw ${prodWord}${r.draw.some(i=>/[+-]\]/.test(r.products[i].smi))?'. It is an ion: use ± Charge.':'.'}`:'';
 const why=r.rule;
 if(mode==='identify'){steps.push(Object.assign(mcType(r),{view:{re:'struct',pr:'struct'}}))}
 else if(mode==='product'){steps.push(Object.assign(drawStepFor(r.products,r.draw,null,(struct?'Use the reactant structures shown. ':'')+prodPrompt,r.hint,why),{view:{re:struct?'bare':'name',pr:'hidden'},hintShow:'re'}))}
 else if(mode==='reactant'){const idx=r.rev.idx;let pr=r.rev.prompt;const canS=!r.salt&&orgP.every(p=>pr.includes(p.name));const useS=struct&&canS;
  if(useS){orgP.forEach((p,k)=>{pr=pr.split(p.name).join(k?'the other product shown':'the product shown')});pr=cap(pr)}
  steps.push(Object.assign(drawStepFor(r.reactants,idx,r.rev.alts,pr,r.hint,why),{view:{re:'hidden',pr:useS?'bare':'name',hideIdx:idx},hintShow:'pr',typeLabel:r.type}))}
 else if(mode==='name'){const doR=canNameRe(r)&&(!r.draw||Math.random()<.3);
  if(doR){const i=r.rev.idx[0];steps.push(Object.assign(nameStep(r.reactants[i],'Name the starting material (the “?”) that formed the '+(orgP.length>1?'products':'product')+' shown.',{re:'hidden',pr:'bare',hideIdx:[i]},'Name reactant',why),{typeLabel:r.type}))}
  else{const i=pick(r.draw),p=r.products[i];steps.push(nameStep(p,`Name the ${orgP.length>1?groupWord(p)+' product':'organic product'} of this reaction.`,{re:'bare',pr:'hidden'},'Name product',why))}}
 else{const orgIdx=r.reactants.map((p,i)=>p.smi?i:-1).filter(i=>i>=0);const nameStart=struct&&orgIdx.length===1;
  if(nameStart)steps.push(nameStep(r.reactants[orgIdx[0]],'Step 1: name the reactant shown.',{re:'bare',pr:'hidden'},'Name reactant','Good. Now decide what kind of reaction this is.'));
  else steps.push(Object.assign(drawStepFor(r.reactants,orgIdx,null,`Step 1: draw ${orgIdx.length>1?'both reactants':'the reactant'} from ${orgIdx.length>1?'their names (two separate molecules)':'its name'}: ${orgIdx.map(i=>'<b>'+esc(r.reactants[i].name)+'</b>').join(' and ')}.`,nameHint,'Nice drawing. Now decide what kind of reaction this is.'),{view:{re:'name',pr:'hidden'},label:'Draw reactant'}));
  steps.push(Object.assign(mcType(r),{view:{re:'struct',pr:'hidden'},label:'Reaction type'}));
  steps.push(Object.assign(drawStepFor(r.products,r.draw,null,'Step 3: '+prodPrompt.charAt(0).toLowerCase()+prodPrompt.slice(1),r.hint,why),{view:{re:'struct',pr:'hidden'},label:'Draw product'}));
  const i=pick(r.draw),p=r.products[i];steps.push(nameStep(p,`Step 4: name the ${r.draw.length>1?groupWord(p)+' product':'product'} you drew.`,{re:'struct',pr:'bare'},'Name product',''))}
 return {r,steps,mode}}

/* reaction display */
function partHTML(p,show,style){if(!p.smi)return `<span class="ptext">${esc(p.t)}</span>`;
 const coef=p.coef?`<span class="coef">${p.coef}</span>`:'';
 if(show==='bare')return `<span class="molitem">${coef?`<span style="display:flex;align-items:center">${coef}${structHTML(p.smi,style)}</span>`:structHTML(p.smi,style)}</span>`;
 if(show==='hidden')return `<span class="qchip" aria-label="unknown">?</span>`;
 if(show==='name')return `${coef}<span class="namechip">${esc(p.name)}</span>`;
 return `<span class="molitem">${coef?`<span style="display:flex;align-items:center">${coef}${structHTML(p.smi,style)}</span>`:structHTML(p.smi,style)}<span class="molname">${esc(p.name)}</span></span>`}
function rxnHTML(r,view,style){view=view||{};const hid=view.hideIdx||[];
 const re=r.reactants.map((p,i)=>partHTML(p,hid.includes(i)?'hidden':(hid.length?'name':view.re),style)).join('<span class="plus">+</span>');
 const pr=view.pr==='hidden'?'<span class="qchip">?</span>':r.products.map(p=>partHTML(p,view.pr,style)).join('<span class="plus">+</span>');
 return `<div class="rxn">${re}${arrowHTML(r.cond)}${pr}</div>`}
function arrowHTML(cond){const parts=String(cond||'').split(/,\s*/).filter(Boolean);const top=parts.length>1?parts.slice(0,-1).join(', '):(parts[0]||''),bot=parts.length>1?parts[parts.length-1]:'';
 return `<span class="rarrow" role="img" aria-label="reaction arrow${cond?', conditions: '+esc(cond):''}"><span class="rlab">${esc(top)||'&nbsp;'}</span><span class="arrline"></span><span class="rlab bot">${esc(bot)||'&nbsp;'}</span></span>`}

window.ENGINE={parseSmi,molSVG,condensedStr,condHTML,expandedSVG,structHTML,formula,fHTML,gList,groupsOf,TPL,SETOF,WEIGHT,genRxn,mcType,checkName,nameHintFor,groupWord,partHTML,rxnHTML,arrowHTML,esc,shuf,pick,rnd,
 lib:{alkane,alkene,alkyne,alcohol,halo,dihalo,aldehyde,ketone,acid,carbox,ester,amide,AMINES,CY,IB,hemiacetal,acetal,hemiketal,ketal,C,lin,ST},CLS,SPEC,CLSD,SPECD,cap};
})();
