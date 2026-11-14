/* FBX Exam Practice module v1: built by /home/claude/fbx/build_fbx.py; re-run it instead of editing. Drawing code below is extracted verbatim from Final Boss (src.html). */
(function(){"use strict";
const FBX_VERSION="1";
const $=id=>document.getElementById(id),esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const rnd=n=>Math.floor(Math.random()*n),shuf=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=rnd(i+1);[a[i],a[j]]=[a[j],a[i]]}return a},pick=a=>a[rnd(a.length)];
const MOLU=46;
function molSVG(m,sc){if(m.skel)return skelSVG(m,sc);const A=m.a.map(a=>({el:a[0],x:a[1]*MOLU,y:a[2]*MOLU,lp:a[3]||0,ch:a[4]||0,lab:a[5]||''}));
 const xs=A.map(a=>a.x),ys=A.map(a=>a.y),pad=34+(A.some(a=>Math.abs(a.ch)>1)?9:0),minx=Math.min(...xs)-pad-(m.br?14:0),miny=Math.min(...ys)-pad,W=Math.max(...xs)-minx+pad+(m.br?30:0),H=Math.max(...ys)-miny+pad;
 const S='#2d3f4b';let o='';const dirs=A.map(()=>[]);
 (m.b||[]).forEach(([i,j,ord])=>{const a=A[i],b=A[j],dx=b.x-a.x,dy=b.y-a.y,l=Math.hypot(dx,dy),ux=dx/l,uy=dy/l,px=-uy,py=ux;dirs[i].push(Math.atan2(dy,dx));dirs[j].push(Math.atan2(-dy,-dx));
  const x1=a.x+ux*12,y1=a.y+uy*12,x2=b.x-ux*12,y2=b.y-uy*12;(ord===1?[0]:ord===2?[-3.2,3.2]:[-4.8,0,4.8]).forEach(of=>{o+=`<line x1="${(x1+px*of).toFixed(1)}" y1="${(y1+py*of).toFixed(1)}" x2="${(x2+px*of).toFixed(1)}" y2="${(y2+py*of).toFixed(1)}" stroke="${S}" stroke-width="2.4" stroke-linecap="round"/>`})});
 const angDist=(c,t)=>{let x=Math.abs(c-t)%(2*Math.PI);return x>Math.PI?2*Math.PI-x:x};
 A.forEach((a,i)=>{if(!a.ch)return;let best=-Math.PI/4,bs=-1;[-45,-135,45,135].map(d=>d*Math.PI/180).forEach(c=>{if(a.lab&&Math.abs(c-3*Math.PI/4)<.01)return;const d=dirs[i].length?Math.min(...dirs[i].map(t=>angDist(c,t))):9;if(d>bs+1e-6){bs=d;best=c}});a.chA=best});
 A.forEach((a,i)=>{
  if(a.lp){const cand=[270,90,0,180,315,45,135,225].map(d=>d*Math.PI/180);const taken=dirs[i].slice();if(a.lab)taken.push(3*Math.PI/4);if(a.ch)taken.push(a.chA);const pick=[];
   for(let k=0;k<a.lp;k++){let best=null,bs=-1;cand.forEach(c=>{const ad=t=>{let x=Math.abs(c-t)%(2*Math.PI);return x>Math.PI?2*Math.PI-x:x};const d=(taken.length?Math.min(...taken.map(ad)):9)+0.001*pick.reduce((a,p)=>a+ad(p),0);if(d>bs+1e-6){bs=d;best=c}});pick.push(best);taken.push(best)}
   pick.forEach(c=>{const dg=Math.abs(Math.sin(2*c))>0.5,rr=dg?(a.el.length>1?25:22):15,cx=a.x+Math.cos(c)*rr,cy=a.y+Math.sin(c)*rr,px=-Math.sin(c)*4.2,py=Math.cos(c)*4.2;o+=`<circle cx="${(cx+px).toFixed(1)}" cy="${(cy+py).toFixed(1)}" r="2.3" fill="${S}"/><circle cx="${(cx-px).toFixed(1)}" cy="${(cy-py).toFixed(1)}" r="2.3" fill="${S}"/>`})}
  o+=`<text x="${a.x.toFixed(1)}" y="${(a.y+6.3).toFixed(1)}" text-anchor="middle" font-size="18" font-weight="800" font-family="Nunito,Inter,Helvetica,Arial,sans-serif" fill="${a.el==='C'||a.el==='H'?S:'#c0473b'}" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke">${a.el}</text>`;
  if(a.ch){const cr=Math.abs(a.ch)>1?30:21;o+=`<text x="${(a.x+Math.cos(a.chA)*cr).toFixed(1)}" y="${(a.y+Math.sin(a.chA)*cr+5).toFixed(1)}" text-anchor="middle" font-size="14" font-weight="900" fill="${S}" font-family="Inter,Helvetica,Arial,sans-serif">${a.ch>0?(a.ch>1?a.ch:'')+'+':(a.ch<-1?-a.ch:'')+'−'}</text>`;}
  if(a.lab)o+=`<circle cx="${(a.x-15).toFixed(1)}" cy="${(a.y+17).toFixed(1)}" r="8.5" fill="#fff1d6" stroke="#e8973a" stroke-width="1.5"/><text x="${(a.x-15).toFixed(1)}" y="${(a.y+21).toFixed(1)}" text-anchor="middle" font-size="11.5" font-weight="900" fill="#b4691c" font-family="Inter,Helvetica,Arial,sans-serif">${a.lab}</text>`});
 if(m.br){const yb=miny+8,yt=miny+H-8,xl=minx+8,xr=minx+W-24;o+=`<path d="M${xl+7} ${yb}H${xl}V${yt}H${xl+7}M${xr-7} ${yb}H${xr}V${yt}H${xr-7}" fill="none" stroke="${S}" stroke-width="2"/><text x="${xr+3}" y="${miny+20}" font-size="15" font-weight="900" fill="${S}" font-family="Inter,Helvetica,Arial,sans-serif">${esc(m.br)}</text>`}
 return `<svg viewBox="${minx.toFixed(1)} ${miny.toFixed(1)} ${W.toFixed(1)} ${H.toFixed(1)}" width="${W.toFixed(0)}" height="${H.toFixed(0)}" style="max-width:100%;height:auto" role="img" aria-label="${esc(molDesc(m))}">${o}</svg>`}

function skelSVG(m,sc){const U=(sc||1)*30,A=m.a.map(a=>({t:a[0],x:a[1]*U,y:a[2]*U,ch:a[4]||0,lab:a[5]||''})),S='#2d3f4b';
 const xs=A.map(a=>a.x),ys=A.map(a=>a.y),pad=22+(A.some(a=>a.t!=='C'&&a.t.replace(/\d/g,'').length>1)?16:0),minx=Math.min(...xs)-pad,miny=Math.min(...ys)-pad,W=Math.max(...xs)-minx+pad,H=Math.max(...ys)-miny+pad;let o='';
 const cg=[];const show=a=>a.t!=='C';const cen=[xs.reduce((p,c)=>p+c,0)/A.length,ys.reduce((p,c)=>p+c,0)/A.length];const adj=A.map(()=>[]);(m.b||[]).forEach(([i,j,od])=>{if(od){adj[i].push(j);adj[j].push(i)}});
 const ringCen=(s0,t0)=>{const prev={[s0]:-1},q=[s0];while(q.length){const u=q.shift();for(const v of adj[u]){if(u===s0&&v===t0)continue;if(v in prev)continue;prev[v]=u;if(v===t0){const path=[];let w=t0;while(w!==-1){path.push(w);w=prev[w]}if(path.length>8)return null;return [path.reduce((p,k)=>p+A[k].x,0)/path.length,path.reduce((p,k)=>p+A[k].y,0)/path.length]}q.push(v)}}return null};
 const supDir=i=>{const an=[];(m.b||[]).forEach(([p,q,od])=>{if(od===0)return;const n=p===i?A[q]:q===i?A[p]:null;if(n)an.push(Math.atan2(n.y-A[i].y,n.x-A[i].x))});let best=-0.55,bs=-1;[-0.55,-Math.PI+0.55,0.55,Math.PI-0.55].forEach((c,k)=>{const d=an.length?Math.min(...an.map(x=>{let t=Math.abs(x-c)%(2*Math.PI);return t>Math.PI?2*Math.PI-t:t})):9;const sc=Math.min(d,1.2)-k*0.01;if(sc>bs+1e-9){bs=sc;best=c}});return best};
 const gapDir=i=>{const an=[];(m.b||[]).forEach(([p,q,od])=>{if(od===0)return;const n=p===i?A[q]:q===i?A[p]:null;if(n)an.push(Math.atan2(n.y-A[i].y,n.x-A[i].x))});an.sort((x,y)=>x-y);if(!an.length)return -Math.PI/4;if(an.length===1){const d=an[0]+Math.PI;return d+(Math.cos(d)>=0?-0.6:0.6)}let bg=-1,dir=0;an.forEach((x,k)=>{const y=k+1<an.length?an[k+1]:an[0]+2*Math.PI,g=y-x;if(g>bg+1e-6){bg=g;dir=x+g/2}});return dir};
 (m.b||[]).forEach(([i,j,ord])=>{const a=A[i],b=A[j],dx=b.x-a.x,dy=b.y-a.y,l=Math.hypot(dx,dy),ux=dx/l,uy=dy/l;let px=-uy,py=ux;
  const x1=a.x+(show(a)?ux*11:0),y1=a.y+(show(a)?uy*11:0),x2=b.x-(show(b)?ux*11:0),y2=b.y-(show(b)?uy*11:0);
  const ln=(x1,y1,x2,y2)=>`<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="${S}" stroke-width="2.3" stroke-linecap="round"/>`;
  if(ord===4){const w=5.5;o+=`<polygon points="${x1.toFixed(1)},${y1.toFixed(1)} ${(x2+px*w).toFixed(1)},${(y2+py*w).toFixed(1)} ${(x2-px*w).toFixed(1)},${(y2-py*w).toFixed(1)}" fill="${S}" stroke="${S}" stroke-width="1" stroke-linejoin="round"/>`}
  else if(ord===5){const n=7;for(let k=1;k<=n;k++){const f=k/n,w=0.8+5*f,cx=x1+(x2-x1)*f,cy=y1+(y2-y1)*f;o+=`<line x1="${(cx+px*w).toFixed(1)}" y1="${(cy+py*w).toFixed(1)}" x2="${(cx-px*w).toFixed(1)}" y2="${(cy-py*w).toFixed(1)}" stroke="${S}" stroke-width="1.9" stroke-linecap="round"/>`}}
  else if(ord===0){const g=show(a)&&show(b)?0:0;o+=`<line x1="${x1.toFixed(1)}" y1="${y1.toFixed(1)}" x2="${x2.toFixed(1)}" y2="${y2.toFixed(1)}" stroke="#2f7fbf" stroke-width="2.6" stroke-dasharray="2 5" stroke-linecap="round"/>`}
  else if(ord===1)o+=ln(x1,y1,x2,y2);
  else if(ord===3)[-4.4,0,4.4].forEach(f=>{o+=ln(x1+px*f,y1+py*f,x2+px*f,y2+py*f)});
  else{const mx=(a.x+b.x)/2,my=(a.y+b.y)/2,rc=ringCen(i,j)||cen;if((rc[0]-mx)*px+(rc[1]-my)*py<0){px=-px;py=-py}const inner=!show(a)&&!show(b)&&A.length>3;
   if(inner){o+=ln(x1,y1,x2,y2);const s=0.16;o+=ln(x1+px*6+ux*l*s,y1+py*6+uy*l*s,x2+px*6-ux*l*s,y2+py*6-uy*l*s)}else[-3,3].forEach(f=>{o+=ln(x1+px*f,y1+py*f,x2+px*f,y2+py*f)})}});
 A.forEach(a=>{if(!show(a))return;
  /* place multi-letter labels so the bonded atom (O of OH, N of NH2, C of CH2OH) sits on the bond, and write them right-to-left (HO, H2N) when the bond comes from the right */
  let lt=a.t,anc='middle',lx=a.x;const ii=A.indexOf(a);let nx=0;(m.b||[]).forEach(([p,q,od])=>{if(od===0)return;const n=p===ii?A[q]:q===ii?A[p]:null;if(n){const d=Math.hypot(n.x-a.x,n.y-a.y)||1;nx+=(n.x-a.x)/d}});
  const GW=c=>/[OQ]/.test(c)?13.2:/[NCHD]/.test(c)?12.3:/[S]/.test(c)?11.4:/[0-9]/.test(c)?6.7:/[a-z]/.test(c)?9.5:11.5;
  if(/^[A-Z][a-z]?H\d?$/.test(lt)&&nx>0.35)lt='H'+lt.slice(lt.indexOf('H')+1)+lt.slice(0,lt.indexOf('H'));
  else if(/^H\d?[A-Z][a-z]?$/.test(lt)&&nx<-0.35){const k=lt.search(/[A-GI-Z]/);lt=lt.slice(k)+lt.slice(0,k)}
  else if(lt==='HOCH2'&&nx<-0.35)lt='CH2OH';else if(lt==='CH2OH'&&nx>0.35)lt='HOCH2';
  if(lt.length>1&&/^[A-Z]/.test(lt)&&!/^[A-Z][a-z]?$/.test(lt)&&/^[A-Za-z0-9]+$/.test(lt)){
   if(lt[0]!=='H'){anc='start';lx=a.x-GW(lt[0])/2}
   else{const ch=[...lt],hv=ch.map((c,k)=>/[A-GI-Z]/.test(c)?k:-1).filter(k=>k>=0),k=hv[hv.length-1];if(k!=null&&k>=0){anc='end';lx=a.x+GW(lt[k])/2+ch.slice(k+1).reduce((w,c)=>w+GW(c),0)}}}
  const t=lt.replace(/(\d)/g,'<tspan dy="4" font-size="12">$1</tspan><tspan dy="-4"></tspan>');
  o+=`<text x="${lx.toFixed(1)}" y="${(a.y+6.3).toFixed(1)}" text-anchor="${anc}" font-size="17" font-weight="800" font-family="Nunito,Inter,Helvetica,Arial,sans-serif" fill="${/^C(H\d?|\u200b)?$/.test(a.t)?S:'#c0473b'}" stroke="#fff" stroke-width="5" stroke-linejoin="round" paint-order="stroke">${t}</text>`;
  if(a.ch){const g=a.t==='C'?gapDir(A.indexOf(a)):supDir(A.indexOf(a)),lw=a.t==='C'?0:a.t.replace(/\d/g,'').length*10.5,ext=anc==='middle'?lw/2:(anc==='start')===(Math.cos(g)>=0)?lw-6:6,rr=11+ext*Math.abs(Math.cos(g))+(a.t==='C'?6:4)*Math.abs(Math.sin(g))+(Math.sin(g)>0.3&&/\d/.test(lt)?4:0),cx=a.x+Math.cos(g)*rr,cy=a.y+Math.sin(g)*rr;cg.push([cx,cy]);o+=`<text x="${cx.toFixed(1)}" y="${(cy+5).toFixed(1)}" text-anchor="middle" font-size="14" font-weight="900" fill="${S}" font-family="Inter,Helvetica,Arial,sans-serif">${a.ch>0?'+':'−'}</text>`}});
 const ringsOf=i=>{const out=[];const nb=adj[i];for(let u=0;u<nb.length;u++)for(let v=u+1;v<nb.length;v++){const prev={[nb[u]]:i},q=[nb[u]];let found=null;while(q.length&&!found){const x=q.shift();for(const y of adj[x]){if(y===i&&x!==nb[u]&&x===nb[v]){found=x;break}if(y===i||y in prev)continue;prev[y]=x;q.push(y)}}if(found!=null){const path=[i];let w=found;while(w!==i){path.push(w);w=prev[w]}if(path.length<=8)out.push(path.map(k=>[A[k].x,A[k].y]))}}return out};
 const inPoly=(x,y,P)=>{let c=false;for(let i=0,j=P.length-1;i<P.length;j=i++){if(((P[i][1]>y)!==(P[j][1]>y))&&(x<(P[j][0]-P[i][0])*(y-P[i][1])/(P[j][1]-P[i][1])+P[i][0]))c=!c}return c};
 const tg=[];A.forEach((a,i)=>{if(!a.lab)return;const an=[];(m.b||[]).forEach(([p,q,od])=>{if(od===0)return;const n=p===i?A[q]:q===i?A[p]:null;if(n)an.push(Math.atan2(n.y-a.y,n.x-a.x))});an.sort((x,y)=>x-y);const r=show(a)?23:19,rings=ringsOf(i);let cands=[];if(an.length===0)cands=[-Math.PI/2];else if(an.length===1)cands=[an[0]+Math.PI];else an.forEach((x,k)=>{const y=k+1<an.length?an[k+1]:an[0]+2*Math.PI;cands.push([y-x,x+(y-x)/2])});
  if(an.length>1)cands=cands.sort((p,q)=>q[0]-p[0]).map(c=>c[1]);let dir=cands[0];for(const c of cands){const px=a.x+Math.cos(c)*r,py=a.y+Math.sin(c)*r;if(!rings.some(R=>inPoly(px,py,R))){dir=c;break}}const tx=a.x+Math.cos(dir)*r,ty=a.y+Math.sin(dir)*r;tg.push([tx,ty]);
  o+=`<circle cx="${tx.toFixed(1)}" cy="${ty.toFixed(1)}" r="9" fill="#fff3e0" stroke="#e8973a" stroke-width="1.6"/><text x="${tx.toFixed(1)}" y="${(ty+4.6).toFixed(1)}" text-anchor="middle" font-size="13" font-weight="900" font-style="italic" fill="#b4640f" font-family="${'Inter,Helvetica,Arial,sans-serif'}">${a.lab}</text>`});
 let x0=minx,y0=miny,x1=minx+W,y1=miny+H;tg.concat(cg).forEach(([x,y])=>{x0=Math.min(x0,x-12);y0=Math.min(y0,y-12);x1=Math.max(x1,x+12);y1=Math.max(y1,y+12)});const vb=[x0,y0,x1-x0,y1-y0];
 return `<svg viewBox="${vb.map(v=>v.toFixed(1)).join(' ')}" width="${vb[2].toFixed(0)}" height="${vb[3].toFixed(0)}" style="max-width:100%;height:auto" role="img" aria-label="${esc(molDesc(m))}">${o}</svg>`}
const rxLab=t=>esc(t).replace(/&lt;(\/?)(sub|sup)&gt;/g,'<$1$2>');
function structBlock(sp){if(!sp)return '';return `<span class="fbx-mols">${sp.map(p=>typeof p==='string'?`<span class="fbx-mop">${esc(p)}</span>`:p.arrow!=null?`<span class="fbx-mrx"><span class="fbx-mrxt">${rxLab(p.arrow)}</span><span class="fbx-mrxa"></span>${p.below?`<span class="fbx-mrxt">${rxLab(p.below)}</span>`:''}</span>`:`<span class="fbx-mol">${molSVG(p)}${p.cap?`<b class="fbx-mcap">${esc(p.cap)}</b>`:''}</span>`).join('')}</span>`}
/* ---------- figures (field q.f = [fig, ...]) ---------- */
const FS='#2d3f4b',FF='Inter,Helvetica,Arial,sans-serif';
const svgSub=t=>String(t).replace(/<sub>(.*?)<\/sub>/g,'<tspan baseline-shift="sub" font-size="75%">$1</tspan>').replace(/<sup>(.*?)<\/sup>/g,'<tspan baseline-shift="super" font-size="75%">$1</tspan>');
const svgT=(x,y,t,o='')=>`<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" font-family="${FF}" fill="${FS}" ${o}>${svgSub(t)}</text>`;
const PCOL=['#3b82b4','#e0675a','#4fa36a','#9a7fc9','#e8973a','#2f8fd0'];
function fTable(f){return `<table class="fbx-ftab">${f.cap?`<caption>${f.cap}</caption>`:''}${f.head?`<tr>${f.head.map(h=>`<th>${h}</th>`).join('')}</tr>`:''}${f.rows.map(r=>`<tr>${r.map(c=>`<td>${c}</td>`).join('')}</tr>`).join('')}</table>`}
function fEq(f){return `<div class="fbx-feq">${f.text}</div>`}
function niceTicks(lo,hi,n){const span=hi-lo,step0=span/(n||5),mag=Math.pow(10,Math.floor(Math.log10(step0))),err=step0/mag,step=(err>=7.5?10:err>=3.5?5:err>=1.5?2:1)*mag;const t=[];for(let v=Math.ceil(lo/step-1e-9)*step;v<=hi+1e-9;v+=step)t.push(+v.toPrecision(10));return t}
function fPlot(f){const W=420,H=270,L=58,R=16,T=14,B=46,pw=W-L-R,ph=H-T-B,X=f.x,Y=f.y;
 const sx=v=>L+(v-X.min)/(X.max-X.min)*pw,sy=v=>T+ph-(v-Y.min)/(Y.max-Y.min)*ph;let o='';
 o+=`<rect x="${L}" y="${T}" width="${pw}" height="${ph}" fill="#fff" stroke="${FS}" stroke-width="1.6"/>`;
 (X.ticks||niceTicks(X.min,X.max,5)).forEach(v=>{const x=sx(v);o+=`<line x1="${x}" y1="${T+ph}" x2="${x}" y2="${T+ph+5}" stroke="${FS}"/>`+svgT(x,T+ph+19,X.fmt?X.fmt.replace('#',v):v,'font-size="12" text-anchor="middle"');if(f.grid)o+=`<line x1="${x}" y1="${T}" x2="${x}" y2="${T+ph}" stroke="#c9d6e0" stroke-dasharray="3 3"/>`});
 if(!Y.noTicks)(Y.ticks||niceTicks(Y.min,Y.max,5)).forEach(v=>{const y=sy(v);o+=`<line x1="${L-5}" y1="${y}" x2="${L}" y2="${y}" stroke="${FS}"/>`+svgT(L-8,y+4,v,'font-size="12" text-anchor="end"');if(f.grid)o+=`<line x1="${L}" y1="${y}" x2="${L+pw}" y2="${y}" stroke="#c9d6e0" stroke-dasharray="3 3"/>`});
 o+=svgT(L+pw/2,H-8,X.label||'','font-size="13" font-weight="700" text-anchor="middle"')+svgT(16,T+ph/2,Y.label||'',`font-size="13" font-weight="700" text-anchor="middle" transform="rotate(-90 16 ${T+ph/2})"`);
 (f.regions||[]).forEach(r=>{const P=r.pts.map(p=>sx(p[0]).toFixed(1)+','+sy(p[1]).toFixed(1)).join(' ');o+=`<polygon points="${P}" fill="${r.fill||'#eaf2f8'}" stroke="none"/>`;if(r.label)o+=svgT(sx(r.at[0]),sy(r.at[1]),r.label,'font-size="14" font-weight="900" text-anchor="middle"')});
 (f.series||[]).forEach((s,k)=>{const col=s.color||(f.mono?FS:PCOL[k%PCOL.length]);const P=s.pts.map(p=>[sx(p[0]),sy(p[1])]);
  if(s.bars){const bw=s.barW!=null?s.barW*pw/(X.max-X.min):Math.max(4,pw/(s.pts.length*3));P.forEach(p=>{o+=`<rect x="${(p[0]-bw/2).toFixed(1)}" y="${p[1].toFixed(1)}" width="${bw.toFixed(1)}" height="${(T+ph-p[1]).toFixed(1)}" fill="${col}" stroke="${FS}" stroke-width="1"/>`});if(s.barLabels)s.pts.forEach((q,i)=>{o+=svgT(P[i][0],P[i][1]-5,s.barLabels[i]??'','font-size="11.5" font-weight="700" text-anchor="middle"')});return}
  if(s.dots)P.forEach(p=>{o+=`<circle cx="${p[0].toFixed(1)}" cy="${p[1].toFixed(1)}" r="3.6" fill="${col}"/>`});
  if(!s.dotsOnly)o+=`<polyline points="${P.map(p=>p[0].toFixed(1)+','+p[1].toFixed(1)).join(' ')}" fill="none" stroke="${col}" stroke-width="2.4" stroke-linejoin="round"/>`;
  if(s.label){let i=s.labelAt!=null?s.labelAt:P.reduce((m,p,j)=>p[1]<P[m][1]?j:m,0);const p=P[Math.min(P.length-1,i)];const lx=p[0]+(s.dx!=null?s.dx:22),ly=p[1]+(s.dy!=null?s.dy:-14);
   const left=(s.dx!=null?s.dx:22)<0;o+=`<line x1="${p[0].toFixed(1)}" y1="${p[1].toFixed(1)}" x2="${(lx+(left?4:-4)).toFixed(1)}" y2="${(ly+3).toFixed(1)}" stroke="${FS}" stroke-width="1"/>`+svgT(lx,ly+6,s.label,`font-size="15" font-weight="900" fill="${col}" text-anchor="${left?'end':'start'}"`)}});
 (f.hlines||[]).forEach(h=>{const y=sy(h.y);o+=`<line x1="${L}" y1="${y.toFixed(1)}" x2="${L+pw}" y2="${y.toFixed(1)}" stroke="${FS}" stroke-width="1.3" stroke-dasharray="5 4"/>`;if(h.label)o+=svgT(L+pw-4,y-5,h.label,'font-size="12" font-weight="700" text-anchor="end"')});
 (f.vlines||[]).forEach(v=>{const x=sx(v.x);o+=`<line x1="${x.toFixed(1)}" y1="${T}" x2="${x.toFixed(1)}" y2="${T+ph}" stroke="${FS}" stroke-width="1.3" stroke-dasharray="5 4"/>`;if(v.label)o+=svgT(x+4,T+14,v.label,'font-size="12" font-weight="700"')});
 (f.marks||[]).forEach(m=>{o+=svgT(sx(m[0]),sy(m[1]),m[2],'font-size="13" font-weight="800" text-anchor="middle"')});
 (f.points||[]).forEach(p=>{const x=sx(p[0]),y=sy(p[1]);o+=`<circle cx="${x.toFixed(1)}" cy="${y.toFixed(1)}" r="4.2" fill="#fff" stroke="${FS}" stroke-width="2"/>`;if(p[2])o+=svgT(x+(p[3]??8),y+(p[4]??-8),p[2],'font-size="13" font-weight="900"')});
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="graph">${o}</svg>`}
/* MO pictures: kind = sigma_s, sigmastar_s, sigma_p, sigmastar_p, pi_p, pistar_p; f.show='mo' (result only) or 'combine' (AO + AO → MO) */
function moShape(kind,cx,cy){const P='#7fb8e0',N='#fff',st=`stroke="${FS}" stroke-width="1.8"`;let o='';const nuc=(x)=>`<circle cx="${x}" cy="${cy}" r="3" fill="${FS}"/>`;const d=26;
 const ell=(x,y,rx,ry,fill)=>`<ellipse cx="${x}" cy="${y}" rx="${rx}" ry="${ry}" fill="${fill}" ${st}/>`;
 const lobeH=(x,y,dir,fill,len=30,w=17)=>{const tip=x+dir*len;return `<path d="M${x} ${y} C ${x+dir*len*0.35} ${y-w}, ${tip} ${y-w*0.9}, ${tip} ${y} C ${tip} ${y+w*0.9}, ${x+dir*len*0.35} ${y+w}, ${x} ${y} Z" fill="${fill}" ${st}/>`};
 const lobeV=(x,y,dir,fill,len=30,w=15)=>{const tip=y+dir*len;return `<path d="M${x} ${y} C ${x-w} ${y+dir*len*0.35}, ${x-w*0.9} ${tip}, ${x} ${tip} C ${x+w*0.9} ${tip}, ${x+w} ${y+dir*len*0.35}, ${x} ${y} Z" fill="${fill}" ${st}/>`};
 switch(kind){
  case 's':o+=ell(cx,cy,22,22,P)+nuc(cx);break;
  case 'p_x':o+=lobeH(cx,cy,-1,N)+lobeH(cx,cy,1,P)+nuc(cx);break;
  case 'p_y':o+=lobeV(cx,cy,-1,P)+lobeV(cx,cy,1,N)+nuc(cx);break;
  case 'sigma_s':o+=ell(cx,cy,48,24,P)+nuc(cx-d)+nuc(cx+d);break;
  case 'sigmastar_s':o+=ell(cx-36,cy,24,22,P)+ell(cx+36,cy,24,22,N)+`<line x1="${cx}" y1="${cy-30}" x2="${cx}" y2="${cy+30}" stroke="${FS}" stroke-dasharray="4 3"/>`+nuc(cx-d)+nuc(cx+d);break;
  case 'sigma_p':o+=lobeH(cx-d,cy,-1,N,24,13)+lobeH(cx+d,cy,1,N,24,13)+ell(cx,cy,34,19,P)+nuc(cx-d)+nuc(cx+d);break;
  case 'sigmastar_p':o+=lobeH(cx-d-6,cy,-1,P,30,15)+lobeH(cx-d-6,cy,1,N,22,14)+lobeH(cx+d+6,cy,-1,P,22,14)+lobeH(cx+d+6,cy,1,N,30,15)+`<line x1="${cx}" y1="${cy-32}" x2="${cx}" y2="${cy+32}" stroke="${FS}" stroke-dasharray="4 3"/>`+nuc(cx-d)+nuc(cx+d);break;
  case 'pi_p':o+=`<path d="M${cx-d-22} ${cy-3} C ${cx-d-22} ${cy-44}, ${cx+d+22} ${cy-44}, ${cx+d+22} ${cy-3} Z" fill="${P}" ${st}/><path d="M${cx-d-22} ${cy+3} C ${cx-d-22} ${cy+44}, ${cx+d+22} ${cy+44}, ${cx+d+22} ${cy+3} Z" fill="${N}" ${st}/>`+`<line x1="${cx-d-36}" y1="${cy}" x2="${cx+d+36}" y2="${cy}" stroke="${FS}" stroke-dasharray="4 3"/>`+nuc(cx-d)+nuc(cx+d);break;
  case 'pistar_p':o+=lobeV(cx-d-4,cy,-1,P,32,15)+lobeV(cx-d-4,cy,1,N,32,15)+lobeV(cx+d+4,cy,-1,N,32,15)+lobeV(cx+d+4,cy,1,P,32,15)+`<line x1="${cx}" y1="${cy-38}" x2="${cx}" y2="${cy+38}" stroke="${FS}" stroke-dasharray="4 3"/>`+nuc(cx-d-4)+nuc(cx+d+4);break}
 return o}
function fMO(f){const items=f.items||[{kind:f.kind,cap:f.cap}],w=170,H=f.items&&f.items.some(i=>i.cap)?128:104;let o='';
 items.forEach((it,i)=>{const cx=w*i+w/2;o+=moShape(it.kind,cx,52);if(it.cap)o+=svgT(cx,H-6,it.cap,'font-size="15" font-weight="900" text-anchor="middle"')});
 return `<svg class="fbx-fsvg" viewBox="0 0 ${w*items.length} ${H}" width="${w*items.length}" height="${H}" role="img" aria-label="molecular orbital pictures">${o}</svg>`}
/* MO energy diagram for second-row diatomics: f.order = 'N2' (π below σ2p: Li2–N2) or 'O2' (σ2p below π: O2–Ne2); f.e = valence electrons */
function fMODiag(f){const lv=f.order==='O2'?[['σ2s',0,1],['σ*2s',1,1],['σ2p',2,1],['π2p',3,2],['π*2p',4,2],['σ*2p',5,1]]:[['σ2s',0,1],['σ*2s',1,1],['π2p',2,2],['σ2p',3,1],['π*2p',4,2],['σ*2p',5,1]];
 const W=240,H=300,y0=270,dy=46;let o='',e=f.e==null?-1:f.e;const lines=[];
 lv.forEach(([n,k,deg])=>{const y=y0-k*dy,xs=deg===1?[W/2]:[W/2-34,W/2+34];const lab=n.replace(/(2[sp])$/,'<sub>$1</sub>').replace(/\*/,'<tspan baseline-shift="super" font-size="10">*</tspan>');
  xs.forEach(x=>{o+=`<line x1="${x-24}" y1="${y}" x2="${x+24}" y2="${y}" stroke="${FS}" stroke-width="2.4"/>`;lines.push({x,y,k})});o+=svgT(18,y+5,lab,'font-size="14" font-weight="800"')});
 if(e>0){const byK={};lines.forEach(l=>(byK[l.k]=byK[l.k]||[]).push(l));for(let k=0;k<6&&e>0;k++){const ls=byK[k];const n=Math.min(e,ls.length*2);
  const fill=ls.map(()=>0);for(let j=0;j<n;j++)fill[j<ls.length?j:j-ls.length]++;e-=n;ls.forEach((l,j)=>{const up=`<path d="M${l.x-7} ${l.y-4}v-24m-4 6l4-6 4 6" stroke="#c0473b" stroke-width="2" fill="none"/>`,dn=`<path d="M${l.x+7} ${l.y-28}v24m-4-6l4 6 4-6" stroke="#c0473b" stroke-width="2" fill="none"/>`;if(fill[j]>=1)o+=up;if(fill[j]===2)o+=dn})}}
 if(f.title)o+=svgT(W/2,16,f.title,'font-size="15" font-weight="900" text-anchor="middle"');
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="MO diagram">${o}</svg>`}
/* particle diagrams: f.boxes=[{cap, mols:[["A","A"],["B"]...], water:false}], f.key={A:{c:"#e0675a",n:"O"}}, f.arrow=true */
function seedRand(s){return ()=>{s=(s*9301+49297)%233280;return s/233280}}
function molParticle(m,x,y,key,rot,sc){sc=sc||1;const R=m.map(k=>((key[k]&&key[k].r)||11)*sc);let o='';const n=m.length;const pos=[];
 if(n===1)pos.push([0,0]);else if(n===2)pos.push([-R[0]*0.75,0],[R[1]*0.75,0]);else{const c=R[0]*0.95;pos.push([0,0]);for(let i=1;i<n;i++){const a=(n===3&&!key[m[0]]?.lin)?(i===1?-35:215)*Math.PI/180:(i-1)/(n-1)*2*Math.PI-Math.PI/2;pos.push([Math.cos(a)*(c+R[i]*0.7),Math.sin(a)*(c+R[i]*0.7)])}}
 const ca=Math.cos(rot),sa=Math.sin(rot);const order=pos.map((p,i)=>i).sort((a,b)=>(a===0?1:0)-(b===0?1:0));
 order.forEach(i=>{const k=m[i],K=key[k]||{c:'#999'},px=x+pos[i][0]*ca-pos[i][1]*sa,py=y+pos[i][0]*sa+pos[i][1]*ca;o+=`<circle cx="${px.toFixed(1)}" cy="${py.toFixed(1)}" r="${R[i]}" fill="${K.c}" stroke="${FS}" stroke-width="1.4"/>`;if(K.q)o+=svgT(px,py+4.5,K.q,`font-size="${R[i]>9?13:10}" font-weight="900" text-anchor="middle" fill="#fff"`)});return o}
function fParticles(f){if(!f.arrow&&f.boxes.length>2&&!f._one){const parts=f.boxes.map((b,i)=>fParticles(Object.assign({},f,{boxes:[b],_one:1,seed:(f.seed||0)+i*7,_noKey:1})));const key=fParticles(Object.assign({},f,{boxes:[],_one:1,_keyOnly:1}));return `<div class="fbx-fwrap">${parts.join('')}</div>${key}`}
 if(f._keyOnly){const keys=Object.entries(f.key||{}).filter(([k,v])=>v.n);return keys.length?`<div class="fbx-flegend">${keys.map(([k,v])=>`<span><svg width="22" height="22"><circle cx="11" cy="11" r="${Math.min(10,v.r||9)}" fill="${v.c}" stroke="${FS}" stroke-width="1.4"/>${v.q?`<text x="11" y="15" text-anchor="middle" font-size="11" font-weight="900" fill="#fff" font-family="${FF}">${v.q}</text>`:''}</svg><span>= ${v.n}</span></span>`).join('')}</div>`:''}
const bw=180,bh=170,gap=f.arrow?54:22,key=f.key||{};let o='',x=0;
 f.boxes.forEach((b,bi)=>{const rnd=seedRand(17+bi*31+(f.seed||0));o+=`<rect x="${x}" y="2" width="${bw}" height="${bh}" rx="8" fill="${b.water?'#eaf5fd':'#fff'}" stroke="${FS}" stroke-width="2"/>`;
  const N=b.mols.length,cols=Math.ceil(Math.sqrt(N*bw/bh)),rows=Math.ceil(N/cols),cw=bw/cols,ch=bh/rows;const cells=[...Array(cols*rows).keys()];for(let k=cells.length-1;k>0;k--){const j=Math.floor(rnd()*(k+1));[cells[k],cells[j]]=[cells[j],cells[k]]}
  const ext0=m=>{const r0=Math.max(...m.map(k=>(key[k]&&key[k].r)||11));return m.length===1?r0:m.length===2?r0*1.8:r0*2.7};const need=b.mols.reduce((a,m)=>a+Math.PI*ext0(m)**2,0),sc=Math.min(1,Math.sqrt(0.42*bw*bh/need));const ext=m=>ext0(m)*sc;const placed=[];
  b.mols.forEach((m,i)=>{const e=ext(m);let best=null,bd=-1;
   for(let t=0;t<600;t++){const px=x+e+3+rnd()*(bw-2*e-6),py=2+e+3+rnd()*(bh-2*e-6);const d=placed.length?Math.min(...placed.map(p=>Math.hypot(p[0]-px,p[1]-py)-p[2]-e)):99;if(d>bd){bd=d;best=[px,py]}if(d>=5)break}
   if(bd<0){const c=cells[i];best=[x+(c%cols+.5)*cw,2+(Math.floor(c/cols)+.5)*ch]}
   placed.push([best[0],best[1],e]);o+=molParticle(m,best[0],best[1],key,rnd()*Math.PI*2,sc)});
  if(b.cap)o+=svgT(x+bw/2,bh+22,b.cap,'font-size="14" font-weight="900" text-anchor="middle"');
  x+=bw;if(bi<f.boxes.length-1){if(f.arrow)o+=`<path d="M${x+10} ${bh/2+2}h${gap-22}m-8-6l8 6-8 6" stroke="${FS}" stroke-width="2.4" fill="none"/>`;x+=gap}});
 const keys=Object.entries(key).filter(([k,v])=>v.n&&!f._noKey);let lg='';if(keys.length){lg=`<div class="fbx-flegend">${keys.map(([k,v])=>`<span><svg width="22" height="22"><circle cx="11" cy="11" r="${Math.min(10,v.r||9)}" fill="${v.c}" stroke="${FS}" stroke-width="1.4"/>${v.q?`<text x="11" y="15" text-anchor="middle" font-size="11" font-weight="900" fill="#fff" font-family="${FF}">${v.q}</text>`:''}</svg><span>= ${v.n}</span></span>`).join('')}</div>`}
 const H=bh+(f.boxes.some(b=>b.cap)?30:8);return `<div class="fbx-fpart"><svg class="fbx-fsvg" viewBox="-2 0 ${x+4} ${H}" width="${x+4}" height="${H}" role="img" aria-label="particle diagram">${o}</svg>${lg}</div>`}
/* measurement: cylinder (scale up), buret (scale increases downward), ruler; f.lo,f.hi window, f.minor, f.major, f.level */
function fScale(f){const t=f.type;let o='';
 if(t==='ruler'){const W=420,H=110,L=20,pw=W-40,sx=v=>L+(v-f.lo)/(f.hi-f.lo)*pw;o+=`<rect x="${L-8}" y="44" width="${pw+16}" height="52" rx="4" fill="#fff6dc" stroke="${FS}" stroke-width="1.6"/>`;
  for(let v=f.lo;v<=f.hi+1e-9;v+=f.minor){const vv=+v.toFixed(6),maj=Math.abs(vv/f.major-Math.round(vv/f.major))<1e-6,half=f.half&&Math.abs(vv/f.half-Math.round(vv/f.half))<1e-6;const len=maj?22:half?15:9;o+=`<line x1="${sx(vv)}" y1="44" x2="${sx(vv)}" y2="${44+len}" stroke="${FS}" stroke-width="${maj?1.6:1}"/>`;if(maj)o+=svgT(sx(vv),82,+vv.toFixed(6),'font-size="13" text-anchor="middle" font-weight="700"')}
  o+=`<rect x="${sx(f.start||f.lo)}" y="12" width="${sx(f.len)-sx(f.start||f.lo)}" height="26" rx="5" fill="#9a7fc9" stroke="${FS}" stroke-width="1.4"/><line x1="${sx(f.len)}" y1="10" x2="${sx(f.len)}" y2="48" stroke="#c0473b" stroke-width="1.4" stroke-dasharray="3 2"/>`+svgT(W-24,106,f.unit||'cm','font-size="12" text-anchor="end"');
  return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="ruler">${o}</svg>`}
 if(t==='balance'){return `<svg class="fbx-fsvg" viewBox="0 0 260 150" width="260" height="150" role="img" aria-label="balance"><rect x="20" y="58" width="220" height="80" rx="12" fill="#eef3f7" stroke="${FS}" stroke-width="2"/><rect x="60" y="34" width="140" height="10" rx="4" fill="#cfd8df" stroke="${FS}"/><rect x="95" y="44" width="70" height="14" fill="#cfd8df" stroke="${FS}"/><rect x="50" y="82" width="160" height="40" rx="6" fill="#1f2d36"/><text x="196" y="111" text-anchor="end" font-family="'Courier New',monospace" font-size="24" font-weight="700" fill="#8ff0b8">${f.read}</text></svg>`}
 const W=210,H=300,T=20,B=20,ph=H-T-B,down=t==='buret',sy=v=>down?T+(v-f.lo)/(f.hi-f.lo)*ph:T+ph-(v-f.lo)/(f.hi-f.lo)*ph,x0=70,x1=150;
 o+=`<rect x="${x0}" y="${T-12}" width="${x1-x0}" height="${ph+24}" fill="#f4fbff" stroke="${FS}" stroke-width="2"/>`;
 const ly=sy(f.level),dip=9;o+=`<path d="M${x0} ${ly-dip} Q ${(x0+x1)/2} ${ly+dip} ${x1} ${ly-dip} L ${x1} ${down?T+ph+12:T+ph+12} L ${x0} ${T+ph+12} Z" fill="#9fd0f0" opacity=".75"/>`;
 if(down)o=`<rect x="${x0}" y="${T-12}" width="${x1-x0}" height="${ph+24}" fill="#f4fbff" stroke="${FS}" stroke-width="2"/><path d="M${x0} ${ly-dip} Q ${(x0+x1)/2} ${ly+dip} ${x1} ${ly-dip} L ${x1} ${T+ph+12} L ${x0} ${T+ph+12} Z" fill="#9fd0f0" opacity=".75"/>`;
 o+=`<path d="M${x0} ${ly-dip} Q ${(x0+x1)/2} ${ly+dip} ${x1} ${ly-dip}" fill="none" stroke="#2f6f9a" stroke-width="2"/>`;
 for(let v=f.lo;v<=f.hi+1e-9;v+=f.minor){const vv=+v.toFixed(6),maj=Math.abs(vv/f.major-Math.round(vv/f.major))<1e-6;const y=sy(vv);o+=`<line x1="${x0}" y1="${y}" x2="${x0+(maj?34:18)}" y2="${y}" stroke="${FS}" stroke-width="${maj?1.8:1}"/>`;if(maj)o+=svgT(x0-8,y+5,+vv.toFixed(6),'font-size="14" font-weight="700" text-anchor="end"')}
 o+=svgT(x1+10,T+ph/2,f.unit||'mL','font-size="13"');
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="${t} scale">${o}</svg>`}
/* precision/accuracy targets: f.items=[{cap,pts:[[x,y]...]}] with x,y in -1..1 (0,0 = bullseye) */
function fTargets(f){const r=62,w=150;let o='';f.items.forEach((it,i)=>{const cx=w*i+w/2,cy=70;[1,.75,.5,.25].forEach((k,j)=>{o+=`<circle cx="${cx}" cy="${cy}" r="${r*k}" fill="${j%2?'#fff':'#fdeeed'}" stroke="${FS}" stroke-width="1.4"/>`});o+=`<circle cx="${cx}" cy="${cy}" r="4" fill="#e0675a"/>`;
 it.pts.forEach(p=>{const x=cx+p[0]*r,y=cy+p[1]*r;o+=`<path d="M${x-5} ${y-5}l10 10m0-10l-10 10" stroke="#2f4b60" stroke-width="2.6"/>`});if(it.cap)o+=svgT(cx,cy+r+24,it.cap,'font-size="15" font-weight="900" text-anchor="middle"')});
 return `<svg class="fbx-fsvg" viewBox="0 0 ${w*f.items.length} 162" width="${w*f.items.length}" height="162" role="img" aria-label="targets">${o}</svg>`}
/* metabolic pathways: cycle (wheel) and path (vertical). outs[i]/ins[i] belong to the step from node i to node i+1 */
function fCycle(f){const n=f.nodes.length,R=f.r||132,W=440,H=2*R+150,cx=W/2,cy=H/2,ang=i=>-Math.PI/2+i*2*Math.PI/n;let o='';
 const P=i=>[cx+R*Math.cos(ang(i)),cy+R*Math.sin(ang(i))];
 for(let i=0;i<n;i++){const a0=ang(i)+0.2,a1=ang(i+1)-0.2,x0=cx+R*Math.cos(a0),y0=cy+R*Math.sin(a0),x1=cx+R*Math.cos(a1),y1=cy+R*Math.sin(a1);
  o+=`<path d="M${x0.toFixed(1)} ${y0.toFixed(1)} A ${R} ${R} 0 0 1 ${x1.toFixed(1)} ${y1.toFixed(1)}" fill="none" stroke="${FS}" stroke-width="2" marker-end="url(#ah)"/>`;
  const am=(ang(i)+ang(i+1))/2,lab=[...(f.outs&&f.outs[i]||[]).map(t=>'→ '+t),...(f.ins&&f.ins[i]||[]).map(t=>'← '+t)];
  if(lab.length){const rx=cx+(R+30)*Math.cos(am),ry=cy+(R+30)*Math.sin(am),anc=Math.cos(am)>0.25?'start':Math.cos(am)<-0.25?'end':'middle';
   lab.forEach((t,k)=>{o+=svgT(rx,ry+(k-(lab.length-1)/2)*20+6,t,`font-size="17" font-weight="800" text-anchor="${anc}" fill="${t.startsWith('←')?'#2f7fbf':'#c0473b'}"`)})}}
 for(let i=0;i<n;i++){const [x,y]=P(i),t=f.nodes[i],w=Math.max(64,t.length*8.4+16);o+=`<rect x="${(x-w/2).toFixed(1)}" y="${(y-15).toFixed(1)}" width="${w.toFixed(1)}" height="30" rx="15" fill="#fff" stroke="${FS}" stroke-width="1.6"/>`+svgT(x,y+5.5,t,'font-size="15" font-weight="700" text-anchor="middle"')}
 if(f.title)f.title.split('|').forEach((t,k,arr)=>{o+=svgT(cx,cy+5+(k-(arr.length-1)/2)*18,t,'font-size="15" font-weight="900" text-anchor="middle"')});
 if(f.entry){const [x,y]=P(f.entry.at);o+=`<path d="M${(x-120).toFixed(1)} ${(y-40).toFixed(1)} L ${(x-34).toFixed(1)} ${(y-12).toFixed(1)}" stroke="#2f7fbf" stroke-width="2" marker-end="url(#ahb)"/>`+svgT(x-124,y-44,f.entry.label,'font-size="13" font-weight="900" text-anchor="end" fill="#2f7fbf"')}
 const defs=`<defs><marker id="ah" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="${FS}"/></marker><marker id="ahb" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#2f7fbf"/></marker></defs>`;
 return `<svg class="fbx-fsvg" viewBox="-50 0 ${W+100} ${H}" width="${W+100}" height="${H}" role="img" aria-label="metabolic cycle">${defs}${o}</svg>`}
function fPath(f){const n=f.nodes.length,step=f.step||48,W=400,cx=W/2,top=20,H=top+(n-1)*step+30;let o='';
 const defs=`<defs><marker id="ahp" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="${FS}"/></marker></defs>`;
 for(let i=0;i<n-1;i++){const y0=top+i*step+14,y1=top+(i+1)*step-14;o+=`<line x1="${cx}" y1="${y0}" x2="${cx}" y2="${y1}" stroke="${FS}" stroke-width="2" marker-end="url(#ahp)"/>`;const ym=(y0+y1)/2+5;
  (f.outs&&f.outs[i]||[]).forEach((t,k)=>{o+=svgT(cx+18,ym+k*15-((f.outs[i].length-1)*7),'→ '+t,'font-size="13" font-weight="800" fill="#c0473b"')});
  (f.ins&&f.ins[i]||[]).forEach((t,k)=>{o+=svgT(cx-18,ym+k*15-((f.ins[i].length-1)*7),t+' →','font-size="13" font-weight="800" text-anchor="end" fill="#2f7fbf"')});
  if(f.steps&&f.steps[i])o+=svgT(W-6,ym,f.steps[i],'font-size="11.5" text-anchor="end" fill="#5c6a75"')}
 f.nodes.forEach((t,i)=>{const y=top+i*step,w=Math.max(70,t.length*8+16);o+=`<rect x="${(cx-w/2).toFixed(1)}" y="${y-14}" width="${w.toFixed(1)}" height="28" rx="14" fill="#fff" stroke="${FS}" stroke-width="1.6"/>`+svgT(cx,y+5,t,'font-size="14.5" font-weight="700" text-anchor="middle"')});
 if(f.title)o=svgT(8,16,f.title,'font-size="14" font-weight="900"')+o;
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="metabolic pathway">${defs}${o}</svg>`}
/* Fischer projections and Haworth rings (carbohydrates). Text via svgSub; O/N labels red like skeletal parts. */
const fbCol=t=>{const p=String(t).replace(/<[^>]+>/g,'');return /C/.test(p)||!/[ON]/.test(p)?FS:'#c0473b'};
const fbW=(t,cw)=>String(t).replace(/<su[bp]>(.*?)<\/su[bp]>/g,(m,a)=>' '.repeat(Math.ceil(a.length*.7))).replace(/<[^>]+>/g,'').length*cw;
const fbT=(x,y,t,o='')=>`<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" font-family="${FF}" fill="${fbCol(t)}" font-weight="800" stroke="#fff" stroke-width="4" stroke-linejoin="round" paint-order="stroke" ${o}>${svgSub(t)}</text>`;
const fbL=(x1,y1,x2,y2,w=2.4)=>`<line x1="${(+x1).toFixed(1)}" y1="${(+y1).toFixed(1)}" x2="${(+x2).toFixed(1)}" y2="${(+y2).toFixed(1)}" stroke="${FS}" stroke-width="${w}" stroke-linecap="round"/>`;
const fbTag=(x,y,l,z=1)=>`<circle cx="${(+x).toFixed(1)}" cy="${(+y).toFixed(1)}" r="${9.5*z}" fill="#fff3e0" stroke="#e8973a" stroke-width="1.6"/><text x="${(+x).toFixed(1)}" y="${(y+4.6*z).toFixed(1)}" text-anchor="middle" font-size="${13*z}" font-weight="900" font-style="italic" fill="#b4640f" font-family="${FF}">${svgSub(l)}</text>`;
const fbNum=(x,y,n)=>`<text x="${(+x).toFixed(1)}" y="${(+y).toFixed(1)}" text-anchor="middle" font-size="12" font-weight="700" fill="#8a96a0" font-family="${FF}">${svgSub(n)}</text>`;
function fbBox(){const b={x0:1e9,x1:-1e9,y0:1e9,y1:-1e9};b.add=(x,y)=>{b.x0=Math.min(b.x0,x);b.x1=Math.max(b.x1,x);b.y0=Math.min(b.y0,y);b.y1=Math.max(b.y1,y)};return b}
function fbSvg(o,b,cap,aria,pad=8,z=1){if(cap){const cy=b.y1+22*z;o+=svgT((b.x0+b.x1)/2,cy,cap,`font-size="${15*z}" font-weight="900" text-anchor="middle"`);b.add((b.x0+b.x1)/2,cy+4)}
 const x=b.x0-pad,y=b.y0-pad,w=b.x1-b.x0+2*pad,h=b.y1-b.y0+2*pad;return `<svg class="fbx-fsvg" viewBox="${x.toFixed(1)} ${y.toFixed(1)} ${w.toFixed(1)} ${h.toFixed(1)}" width="${w.toFixed(0)}" height="${h.toFixed(0)}" role="img" aria-label="${aria}">${o}</svg>`}
function fbMulti(f,one){const it=f.items;if(it.length===1)return one(Object.assign({},f,it[0],{items:null}));return `<div class="fbx-fwrap">${it.map(x=>`<div class="fbx-fpart">${one(Object.assign({_m:1},f,x,{items:null}))}</div>`).join('')}</div>`}
/* f.top, f.rows=[[left,right] | [left,right,tag] | "C=O"], f.bottom, f.nums (carbon numbers), f.ttag/f.btag, f.cap; or f.items=[{...}] */
function fFischer(f){if(f.items)return fbMulti(f,fFischer);const g=46,cw=10.6,rows=f.rows||[],b=fbBox();let o='',y=0,n=1;
 const lab=(x,y,t,anc)=>{const w=fbW(t,cw);o+=fbT(x,y+6,t,`font-size="17" text-anchor="${anc}"`);const xa=anc==='end'?x-w:anc==='start'?x:x-w/2;b.add(xa,y-11);b.add(xa+w,y+11);return w};
 const endLab=(t,tag,y)=>{const w=lab(-6.5,y,t,'start');if(f.nums){o+=fbNum(-16,y+5,n);b.add(-22,y)}if(tag){o+=fbTag(w+5,y,tag);b.add(w+16,y)}n++};
 endLab(f.top||'CHO',f.ttag,0);let prev=11;
 rows.forEach(r=>{y+=g;if(typeof r==='string'){o+=fbL(0,prev,0,y-11);lab(0,y,'C','middle');o+=fbL(9,y-3.2,25,y-3.2,2.2)+fbL(9,y+3.2,25,y+3.2,2.2);lab(32,y,'O','middle');if(f.nums)o+=fbNum(-13,y+19,n);prev=y+11}
  else{o+=fbL(0,prev,0,y)+fbL(-26,y,26,y);lab(-30,y,r[0],'end');lab(30,y,r[1],'start');if(f.nums)o+=fbNum(-11,y+18,n);if(r[2])o+=fbTag(15,y-15,r[2]);prev=y}n++});
 y+=g;o+=fbL(0,prev,0,y-11);endLab(f.bottom||'CH<sub>2</sub>OH',f.btag,y);
 return fbSvg(o,b,f.cap,'Fischer projection')}
/* Haworth ring: f.size 5|6 and f.subs=[[up,down],...] from the anomeric carbon around the ring, or f.sugar (glucose, galactose, mannose, fructose, ribose, deoxyribose) + f.anomer 'a'|'b'.
   f.nums (true or a list), f.tags {index|'O': letter}, f.noH, f.flip (ring turned over: O in front). Disaccharide: f.rings=[ringA, ringB] + f.link={from:[i,'up'|'down'],to:[j,'up'|'down'],dy,tag}. */
const HW_SUG={glucose:[6,[['H','OH'],['OH','H'],['H','OH'],['CH<sub>2</sub>OH','H']],[1,2,3,4,5]],galactose:[6,[['H','OH'],['OH','H'],['OH','H'],['CH<sub>2</sub>OH','H']],[1,2,3,4,5]],mannose:[6,[['OH','H'],['OH','H'],['H','OH'],['CH<sub>2</sub>OH','H']],[1,2,3,4,5]],
 fructose:[5,[['OH','H'],['H','OH'],['CH<sub>2</sub>OH','H']],[2,3,4,5]],ribose:[5,[['H','OH'],['H','OH'],['CH<sub>2</sub>OH','H']],[1,2,3,4]],deoxyribose:[5,[['H','H'],['H','OH'],['CH<sub>2</sub>OH','H']],[1,2,3,4]]};
const HW_GEO={6:[[118,0],[184,44],[146,94],[40,94],[0,44],[66,0]],5:[[84,0],[166,48],[134,100],[34,100],[0,48]]};
const HW_REV={'OH':'HO','CH<sub>2</sub>OH':'HOCH<sub>2</sub>','NH<sub>2</sub>':'H<sub>2</sub>N','OCH<sub>3</sub>':'H<sub>3</sub>CO','CH<sub>3</sub>':'H<sub>3</sub>C','COOH':'HOOC','CH<sub>2</sub>OPO<sub>3</sub><sup>2−</sup>':'<sup>2−</sup>O<sub>3</sub>POCH<sub>2</sub>'};
function hwRing(r){let size=r.size,subs=r.subs,nums=r.nums;if(r.sugar){const s=HW_SUG[r.sugar];size=s[0];const fr=r.sugar==='fructose',an=r.anomer==='a'?(fr?['CH<sub>2</sub>OH','OH']:['H','OH']):(fr?['OH','CH<sub>2</sub>OH']:['OH','H']);subs=[an].concat(s[1]);if(nums===true)nums=s[2]}
 if(nums===true)nums=subs.map((x,i)=>i+1);return {size:+size,subs,nums,tags:r.tags||{},noH:r.noH,flip:r.flip,fz:r.fz||1}}
function hwDraw(R,ox,oy,b,skip){const P0=HW_GEO[R.size],W=P0.reduce((m,p)=>Math.max(m,p[0]),0),H=P0.reduce((m,p)=>Math.max(m,p[1]),0);
 const P=P0.map(p=>R.flip?[ox+W-p[0],oy+H-p[1]]:[ox+p[0],oy+p[1]]),cx=ox+W/2,cy=oy+H/2,n=P.length;let o='';const fr=new Set(['1,2','2,3','3,4']);
 for(let i=0;i<n;i++){const j=(i+1)%n,k=Math.min(i,j)+','+Math.max(i,j),bold=R.flip?!fr.has(k):fr.has(k);let a=P[i],c=P[j];const d=Math.hypot(c[0]-a[0],c[1]-a[1]);
  if(i===0)a=[a[0]+(c[0]-a[0])*10/d,a[1]+(c[1]-a[1])*10/d];if(j===0)c=[c[0]+(a[0]-c[0])*10/d,c[1]+(a[1]-c[1])*10/d];o+=fbL(a[0],a[1],c[0],c[1],bold?5.5:2.4);b.add(P[i][0],P[i][1])}
 o+=fbT(P[0][0],P[0][1]+6*R.fz,'O',`font-size="${17*R.fz}" text-anchor="middle"`);
 const ends={},mid=H*.2,z=R.fz;
 R.subs.forEach((s,i)=>{const p=P[i+1],pos=p[1]-cy>mid?1:p[1]-cy<-mid?-1:0;['up','down'].forEach((d,k)=>{const t=s[k],dir=k?1:-1,inside=(pos>0&&dir<0)||(pos<0&&dir>0),L=(inside?20:26)*(z>1?1.12:1),ex=p[0],ey=p[1]+dir*L;ends[i+'_'+d]=[ex,ey];if(skip&&skip[i+'_'+d])return;if(!t||(R.noH&&t==='H'))return;o+=fbL(p[0],p[1],ex,ey);
   const ly=ey+dir*(inside?8.5:10)*z,lr=p[0]>cx+4?1:p[0]<cx-4?-1:0,side=t==='H'||!lr?0:inside?-lr:lr,lt=side<0?(HW_REV[t]||t):t,w=fbW(lt,9.8*z);
   /* the bonded atom (O of OH, C of CH2OH) sits directly on the vertical bond; the rest of the label reads away from it */
   const pl=String(lt).replace(/<su[bp]>(.*?)<\/su[bp]>/g,(m,a)=>a.replace(/./g,'\u2080')).replace(/<[^>]+>/g,''),gw=c=>(c==='\u2080'?6.4:/[OQ]/.test(c)?12.5:/[A-Z]/.test(c)?11.6:/[a-z]/.test(c)?9:6.4)*z;
   let anc='middle',lx=ex;if(pl.length>1&&t!=='H'){if(side<0){const hv=[...pl].map((c,k)=>/[A-GI-Z]/.test(c)?k:-1).filter(k=>k>=0),k=hv.length?hv[hv.length-1]:pl.length-1;anc='end';lx=ex+gw(pl[k])/2+[...pl].slice(k+1).reduce((a,c)=>a+gw(c),0)}else{const k=Math.max(0,[...pl].findIndex(c=>/[A-GI-Z]/.test(c)));anc='start';lx=ex-gw(pl[k])/2-[...pl].slice(0,k).reduce((a,c)=>a+gw(c),0)}}
   o+=fbT(lx,ly+5.5*z,lt,`font-size="${16*z}" text-anchor="${anc}"`);const xa=anc==='start'?lx:anc==='end'?lx-w:lx-w/2;b.add(xa,ly-10*z);b.add(xa+w,ly+10*z)})});
 const out=(p,r)=>{const sx=p[0]>=cx?1:-1,pos=p[1]-cy>mid?1:p[1]-cy<-mid?-1:0;return [p[0]+sx*r,p[1]+pos*r*.75]};
 if(R.nums)R.nums.forEach((nm,i)=>{const q=out(P[i+1],12);o+=fbNum(q[0],q[1]+4,nm)});
 Object.entries(R.tags).forEach(([k,l])=>{const q=k==='O'?[P[0][0],P[0][1]+(R.flip?22:-22)*R.fz]:out(P[+k+1],20*R.fz);o+=fbTag(q[0],q[1],l,R.fz);b.add(q[0]-10*R.fz,q[1]-10*R.fz);b.add(q[0]+10*R.fz,q[1]+10*R.fz)});
 return {o,ends,W}}
function fHaworth(f){if(f.items)return fbMulti(f,fHaworth);const b=fbBox();let o='';const fz=f.fz||(f.rings||f._m?1.3:1);
 if(f.rings){const A=hwRing(Object.assign({fz},f.rings[0])),B=hwRing(Object.assign({fz},f.rings[1])),lk=f.link||{},fa=lk.from[0]+'_'+lk.from[1],tb=lk.to[0]+'_'+lk.to[1];
  const a=hwDraw(A,0,0,b,{[fa]:1});const gap=f.gap||58,dy=lk.dy||0;const c=hwDraw(B,a.W+gap,dy,b,{[tb]:1});o+=a.o+c.o;
  const P1=a.ends[fa],P2=c.ends[tb],sA=lk.from[1]==='up'?-1:1,sB=lk.to[1]==='up'?-1:1;
  const cA=[P1[0],P1[1]-sA*26],cB=[P2[0],P2[1]-sB*26],Ox=(P1[0]+P2[0])/2,Oy=(P1[1]+P2[1])/2;
  const sh=(p,q,d)=>{const L=Math.hypot(q[0]-p[0],q[1]-p[1])||1;return [q[0]-(q[0]-p[0])*d/L,q[1]-(q[1]-p[1])*d/L]},Oc=[Ox,Oy],e1=sh(P1,Oc,10),e2=sh(P2,Oc,10);
  o+=fbL(cA[0],cA[1],P1[0],P1[1])+fbL(P1[0],P1[1],e1[0],e1[1])+fbL(P2[0],P2[1],e2[0],e2[1])+fbL(P2[0],P2[1],cB[0],cB[1]);
  o+=fbT(Ox,Oy+6*fz,'O',`font-size="${17*fz}" text-anchor="middle"`);b.add(Ox,Oy+12);if(lk.tag){const ty=Oy+24*fz;o+=fbTag(Ox,ty,lk.tag,fz);b.add(Ox,ty-10);b.add(Ox,ty+10)}}
 else o+=hwDraw(hwRing(Object.assign({fz},f)),0,0,b).o;
 return fbSvg(o,b,f.cap,'Haworth projection',8,fz)}
/* Orbital box diagrams: subs=[{name:'2p',boxes:['ud','u','']}] ; box codes: '' empty, 'u' ↑, 'd' ↓, 'ud' ↑↓, 'uu' ↑↑ (Hund violation), 'dd'. items=[{subs,cap}] draws several side by side. */
function fOrbitals(f){const one=(g,ox,oy)=>{let o='',x=ox;const BW=30,GAP=6;
  if(g.stack){/* energy-stacked: first sub at the bottom */const n=g.subs.length,rowH=58,wmax=Math.max(...g.subs.map(sb=>sb.boxes.length*BW));
   g.subs.forEach((sb,r)=>{const y=oy+(n-1-r)*rowH,w=sb.boxes.length*BW,x0=ox+30+(wmax-w)/2;sb.boxes.forEach((code,i)=>{const bx=x0+i*BW;o+=`<rect x="${bx}" y="${y}" width="${BW}" height="30" fill="#fff" stroke="${FS}" stroke-width="1.6"/>`;
     const arr=(cx,up)=>`<line x1="${cx}" y1="${y+(up?24:6)}" x2="${cx}" y2="${y+(up?6:24)}" stroke="${FS}" stroke-width="2.2" marker-end="url(#oarr)"/>`;
     if(code==='u')o+=arr(bx+15,1);else if(code==='d')o+=arr(bx+15,0);else if(code==='ud')o+=arr(bx+9,1)+arr(bx+21,0);else if(code==='uu')o+=arr(bx+9,1)+arr(bx+21,1);else if(code==='dd')o+=arr(bx+9,0)+arr(bx+21,0)});
    o+=svgT(x0+w+8,y+20,sb.name,'font-size="13" font-weight="800"')});
   o+=`<line x1="${ox+10}" y1="${oy+(n-1)*rowH+30}" x2="${ox+10}" y2="${oy}" stroke="${FS}" stroke-width="1.6" marker-end="url(#oarr)"/>`+svgT(ox+10,oy-4,'E','font-size="12" font-weight="800" text-anchor="middle"');
   return [o,wmax+30+70,n*rowH-28]}const arr=(cx,up,col)=>`<line x1="${cx}" y1="${oy+(up?24:6)}" x2="${cx}" y2="${oy+(up?6:24)}" stroke="${col||FS}" stroke-width="2.2" marker-end="url(#oarr)"/>`;
  (g.subs||[]).forEach(sb=>{const n=sb.boxes.length;sb.boxes.forEach((code,i)=>{const bx=x+i*BW;o+=`<rect x="${bx}" y="${oy}" width="${BW}" height="30" fill="#fff" stroke="${FS}" stroke-width="1.6"/>`;
    if(code==='u')o+=arr(bx+15,1);else if(code==='d')o+=arr(bx+15,0);else if(code==='ud')o+=arr(bx+9,1)+arr(bx+21,0);else if(code==='uu')o+=arr(bx+9,1)+arr(bx+21,1);else if(code==='dd')o+=arr(bx+9,0)+arr(bx+21,0)});
   o+=svgT(x+n*BW/2,oy+46,sb.name,'font-size="13" font-weight="800" text-anchor="middle"');x+=n*BW+14});
  return [o,x-ox-14]};
 const items=f.items||[Object.assign({},f)];let o='',x=10,W=0,hmax=0;const stacked=items.some(it=>it.stack);
 items.forEach(it=>{const [g,w,h]=one(it,x,stacked?16:8);o+=g;const hh=h||30;hmax=Math.max(hmax,hh);if(it.cap)o+=svgT(x+w/2,(stacked?16:8)+hh+(it.stack?26:36),it.cap,'font-size="14" font-weight="900" text-anchor="middle"');x+=w+28});W=x-10;const H=stacked?16+hmax+34:(f.items?84:60);
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="orbital diagram"><defs><marker id="oarr" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="${FS}"/></marker></defs>${o}</svg>`}
/* Blank periodic table with letters: cells={X:[period,group]}; periods 1-6 main layout (no f-block); show: {Na:[3,1]} real symbols. */
function fPtGrid(f){const CW=22,CH=22,W=18*CW+16,per=f.periods||6,H=per*CH+16;let o='';
 const has=(p,g)=>p===1?(g===1||g===18):p<=3?(g<=2||g>=13):true;
 for(let p=1;p<=per;p++)for(let g=1;g<=18;g++){if(!has(p,g))continue;o+=`<rect x="${8+(g-1)*CW}" y="${8+(p-1)*CH}" width="${CW}" height="${CH}" fill="${p>=4&&g>=3&&g<=12?'#f3f6f8':'#fff'}" stroke="${FS}" stroke-width="1"/>`}
 const put=(t,p,g,col)=>{o+=svgT(8+(g-1)*CW+CW/2,8+(p-1)*CH+CH/2+5,t,`font-size="13" font-weight="900" text-anchor="middle" fill="${col}"`)};
 Object.entries(f.show||{}).forEach(([t,[p,g]])=>put(t,p,g,'#5c6a75'));Object.entries(f.cells||{}).forEach(([t,[p,g]])=>{o+=`<rect x="${8+(g-1)*CW}" y="${8+(p-1)*CH}" width="${CW}" height="${CH}" fill="#fff3e0" stroke="#e8973a" stroke-width="1.6"/>`;put(t,p,g,'#b4640f')});
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="periodic table outline">${o}</svg>`}
/* Galvanic cell: left/right = {metal:'Zn', sol:'Zn²⁺(aq)', label:'A'}; opts: volt (text on meter), eflow ('lr'|'rl'|null), ions (true: show + and − ion arrows in salt bridge with 'lr'/'rl' = direction cations move), hide: ['sol'] */
function fCell(f){const W=440,H=240;let o='';const bk=(x,side)=>{const d=f[side]||{};o+=`<path d="M${x} 110 V210 a8 8 0 0 0 8 8 H${x+112} a8 8 0 0 0 8 -8 V110" fill="none" stroke="${FS}" stroke-width="2"/><rect x="${x+2}" y="150" width="${116}" height="66" fill="#dbeefb"/>`;
   o+=`<rect x="${x+48}" y="70" width="24" height="120" fill="${d.color||'#9aa8b2'}" stroke="${FS}" stroke-width="1.5"/>`+svgT(x+(side==='left'?40:80),84,d.metal||'',`font-size="15" font-weight="900" text-anchor="${side==='left'?'end':'start'}"`);
   if(!(f.hide||[]).includes('sol'))o+=svgT(x+60,236,d.sol||'','font-size="13" font-weight="700" text-anchor="middle"');if(d.label)o+=`<circle cx="${side==='left'?x+22:x+98}" cy="138" r="11" fill="#fff3e0" stroke="#e8973a" stroke-width="1.6"/>`+svgT(side==='left'?x+22:x+98,143,d.label,'font-size="13" font-weight="900" font-style="italic" text-anchor="middle" fill="#b4640f"')};
 bk(40,'left');bk(280,'right');
 const vt=f.volt||'V',vw=Math.max(44,vt.length*8.5+16);o+=`<path d="M100 70 V30 H${220-vw/2} M${220+vw/2} 30 H340 V70" fill="none" stroke="${FS}" stroke-width="2"/><rect x="${220-vw/2}" y="14" width="${vw}" height="32" rx="16" fill="#fff" stroke="${FS}" stroke-width="2"/>`+svgT(220,35,vt,'font-size="13" font-weight="900" text-anchor="middle"');
 o+=`<path d="M130 160 V120 a10 10 0 0 1 10 -10 H300 a10 10 0 0 1 10 10 V160" fill="none" stroke="${FS}" stroke-width="12" stroke-linecap="butt"/><path d="M130 160 V120 a10 10 0 0 1 10 -10 H300 a10 10 0 0 1 10 10 V160" fill="none" stroke="#f6e6c3" stroke-width="8"/>`+svgT(220,104,'salt bridge','font-size="11.5" font-weight="700" text-anchor="middle"');
 if(f.eflow){const lr=f.eflow==='lr';o+=`<path d="M${lr?120:320} 8 H${lr?320:120}" stroke="#c0473b" stroke-width="2" marker-end="url(#ahr)"/>`+svgT(lr?108:332,13,'e⁻','font-size="12" font-weight="900" text-anchor="middle" fill="#c0473b"')}
 if(f.ions){const lr=f.ions==='lr';o+=svgT(220,123,`${lr?'cations →':'← cations'}`,'font-size="11" font-weight="800" text-anchor="middle"')+svgT(220,136,`${lr?'← anions':'anions →'}`,'font-size="11" font-weight="800" text-anchor="middle"')}
 const defs=`<defs><marker id="ahr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#c0473b"/></marker></defs>`;
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="electrochemical cell">${defs}${o}</svg>`}
/* Line spectrum: min,max (nm), lines=[[656,'label?'],...], items=[{lines,cap}] for stacked spectra; visible=true colors the band */
function fSpectrum(f){const W=440,L=30,R=14,pw=W-L-R,items=f.items||[{lines:f.lines,cap:f.cap}],rowH=52,H=items.length*rowH+40,mn=f.min||380,mx=f.max||720;let o='';
 const sx=v=>L+(v-mn)/(mx-mn)*pw;const col=v=>{const t=(v-380)/340;const h=Math.max(0,Math.min(270,270-270*t));return `hsl(${h} 90% 50%)`};
 items.forEach((it,k)=>{const y=18+k*rowH;o+=`<rect x="${L}" y="${y}" width="${pw}" height="30" fill="${f.visible?'url(#vis)':'#2d3f4b'}" stroke="${FS}"/>`;
  (it.lines||[]).forEach(([v,lab])=>{o+=`<line x1="${sx(v).toFixed(1)}" y1="${y}" x2="${sx(v).toFixed(1)}" y2="${y+30}" stroke="${f.visible?'#111':col(v)}" stroke-width="2.6"/>`;if(lab)o+=svgT(sx(v),y-5,lab,'font-size="11" font-weight="800" text-anchor="middle"')});
  if(it.cap)o+=svgT(L-4,y+20,it.cap,'font-size="13" font-weight="900" text-anchor="end"')});
 const ticks=f.ticks||niceTicks(mn,mx,6);ticks.forEach(v=>{const x=sx(v);o+=`<line x1="${x.toFixed(1)}" y1="${H-34}" x2="${x.toFixed(1)}" y2="${H-29}" stroke="${FS}"/>`+svgT(x,H-17,v,'font-size="12" text-anchor="middle"')});
 o+=svgT(L+pw/2,H-3,'wavelength ('+(f.unit||'nm')+')','font-size="12" font-weight="700" text-anchor="middle"');
 const defs=`<defs><linearGradient id="vis" x1="0" x2="1"><stop offset="0" stop-color="#7a00c8"/><stop offset=".18" stop-color="#2b3cff"/><stop offset=".35" stop-color="#00c2ff"/><stop offset=".5" stop-color="#00d26a"/><stop offset=".65" stop-color="#f5e300"/><stop offset=".82" stop-color="#ff8a00"/><stop offset="1" stop-color="#e01b1b"/></linearGradient></defs>`;
 return `<svg class="fbx-fsvg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="line spectrum">${defs}${o}</svg>`}
/* Enzyme cartoons: f.panels=[{kind, cap}] kind: 'free' (enzyme with empty active site), 'fit' (substrate bound), 'nofit' (wrong-shaped substrate near site),
   'competitive' (inhibitor in the active site, substrate waiting), 'noncompetitive' (inhibitor on a side site, active site warped, substrate can't bind),
   'induced' (site hugging the substrate), 'product' (two product pieces leaving). Letter labels: site='a', sub='b', inh='c' via f.tags {site:'a',sub:'b',inh:'c'} */
function fEnzyme(f){const P=f.panels||[{kind:f.kind,cap:f.cap}],W=150,H=148;const panels=[];const tg=f.tags||{};const T=(x,y,t)=>t?`<circle cx="${x}" cy="${y}" r="9" fill="#fff3e0" stroke="#e8973a" stroke-width="1.6"/><text x="${x}" y="${y+4.6}" text-anchor="middle" font-size="13" font-weight="900" font-style="italic" fill="#b4640f" font-family="${FF}">${t}</text>`:'';
 P.forEach((p,k)=>{let o='';const ox=0,warp=p.kind==='noncompetitive';
  // enzyme body with a notch (active site) on top; warped notch is shallow/rounded
  const site=warp?`q10 12 20 0 q10 -8 20 0`:(p.kind==='induced'?`l -12 7 l 6 17 l 52 0 l 6 -17 l -12 -7`:`l 0 20 l 40 0 l 0 -20`);
  const sub=(x,y,col)=>`<path d="M${x} ${y} l 0 -22 l 40 0 l 0 22 z" fill="${col||'#f2c35b'}" stroke="${FS}" stroke-width="1.8"/>`;
  const inh=(x,y)=>`<path d="M${x} ${y} l 0 -22 l 40 0 l 0 22 l -10 -8 l -20 0 z" fill="#e0675a" stroke="${FS}" stroke-width="1.8"/>`;
  const side=(x,y)=>`<path d="M${x} ${y} l 20 -12 l 20 12 l -20 12 z" fill="#e0675a" stroke="${FS}" stroke-width="1.8"/>`;
  if(p.kind==='denatured'){o+=`<g transform="translate(0,16)"><path d="M22 40 c 20 -30 40 10 60 -10 s 30 30 46 20 c 10 30 -20 40 -40 36 s -20 -24 -36 -10 c -20 10 -36 -10 -30 -36z" fill="#cfe7f7" stroke="${FS}" stroke-width="2" stroke-dasharray="6 3"/><path d="M40 30 c 15 -20 30 20 45 -5 s 25 25 40 5" fill="none" stroke="${FS}" stroke-width="2"/>`+svgT(75,94,'enzyme (unfolded)','font-size="11" font-weight="800" text-anchor="middle"')+sub(100,30)+T(120,0,tg.sub)+'</g>';if(p.cap)o+=svgT(75,H-4,p.cap,'font-size="15" font-weight="900" text-anchor="middle"');panels.push(`<span class="fbx-fpart"><svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="enzyme diagram">${o}</svg></span>`);return}
  o+=`<g transform="translate(0,16)"><path d="M20 70 q0 -28 35 -28 ${site} q35 0 35 28 q0 40 -55 40 q-55 0 -55 -40z" fill="#cfe7f7" stroke="${FS}" stroke-width="2"/>`;
  o+=svgT(75,94,'enzyme','font-size="11" font-weight="800" text-anchor="middle"');
  if(p.kind==='free'){o+=T(75,55,tg.site)}
  else if(p.kind==='fit'){o+=sub(55,62)+T(75,25,tg.sub)}
  else if(p.kind==='induced'){o+=`<path d="M53 65 l 0 -22 l 44 0 l 0 22 z" fill="#f2c35b" stroke="${FS}" stroke-width="1.8"/>`+T(75,25,tg.sub)}
  else if(p.kind==='nofit'){o+=`<path d="M55 36 l 20 -22 l 20 22 z" fill="#f2c35b" stroke="${FS}" stroke-width="1.8"/>`+T(75,8,tg.sub)}
  else if(p.kind==='competitive'){o+=inh(55,62)+sub(100,30,'#f2c35b')+T(75,25,tg.inh)+T(120,0,tg.sub)}
  else if(p.kind==='noncompetitive'){o+=side(100,92)+sub(55,30)+T(140,92,tg.inh)+T(75,0,tg.sub)}
  else if(p.kind==='product'){o+=`<path d="M48 30 l 0 -16 l 18 0 l 0 16 z" fill="#9fd3a7" stroke="${FS}" stroke-width="1.8"/><path d="M84 30 l 0 -16 l 18 0 l 0 16 z" fill="#9fd3a7" stroke="${FS}" stroke-width="1.8"/>`+svgT(75,12,'→ products','font-size="10" font-weight="800" text-anchor="middle"')}
  o+='</g>';if(p.cap)o+=svgT(75,H-4,p.cap,'font-size="15" font-weight="900" text-anchor="middle"');panels.push(`<span class="fbx-fpart"><svg viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto" role="img" aria-label="enzyme diagram">${o}</svg></span>`)});
 return `<div class="fbx-fwrap">${panels.join('')}</div>`}
const FIG={cycle:fCycle,path:fPath,table:fTable,eq:fEq,plot:fPlot,mo:fMO,modiag:fMODiag,particles:fParticles,cylinder:fScale,buret:fScale,ruler:fScale,balance:fScale,targets:fTargets,fischer:fFischer,haworth:fHaworth,orbitals:fOrbitals,ptgrid:fPtGrid,cell:fCell,spectrum:fSpectrum,enzyme:fEnzyme};
function figBlock(fs){if(!fs)return '';return `<span class="fbx-figs">${fs.map(f=>{try{return `<span class="fbx-fig">${FIG[f.type](f)}</span>`}catch(e){return ''}}).join('')}</span>`}
const qHTML=q=>q.q+structBlock(q.s)+figBlock(q.f);
/* spoken description of a drawn molecule, so structure-only answer choices can be told apart by screen-reader users.
   It says where things are (which kind of carbon carries each atom, what a bridging atom joins, where multiple bonds and
   ring substituents sit) without naming the functional group, so it gives the listener what the drawing gives the eye. */
function molDesc(m){if(!m||!m.a)return 'structure';
 const A=m.a.map(a=>({l:String(a[0]),x:+a[1]||0,y:+a[2]||0,lp:a[3]||0,ch:a[4]||0})),N=A.length,adj=A.map(()=>[]),RB=(m.b||[]).filter(b=>A[b[0]]&&A[b[1]]),B=RB.filter(b=>b[2]!==0).map(b=>[b[0],b[1],b[2]===4||b[2]===5?1:b[2]]); /* 0 = dotted (hydrogen-bond) line, 4 = solid wedge, 5 = dashed wedge */
 B.forEach(b=>{adj[b[0]].push([b[1],b[2]||1]);adj[b[1]].push([b[0],b[2]||1])});
 const isC=i=>A[i].l==='C',isH=i=>A[i].l==='H',plural=(n,w)=>n+' '+w+(n===1?'':'s'),nC=A.filter((a,i)=>isC(i)).length;
 /* shortest path i -> j that does not use the bond i-j: tells us whether that bond is in a ring, and the ring */
 const pathAvoid=(i,j)=>{const prev=new Array(N).fill(-2),q=[i];prev[i]=-1;while(q.length){const u=q.shift();if(u===j)break;
   for(const [v] of adj[u]){if((u===i&&v===j)||prev[v]!==-2)continue;prev[v]=u;q.push(v)}}
  if(prev[j]===-2)return null;const p=[];for(let u=j;u!==-1;u=prev[u])p.push(u);return p};
 const rings={},inRing=new Array(N).fill(false),ringBond={};
 B.forEach(b=>{const p=pathAvoid(b[0],b[1]);if(p){ringBond[Math.min(b[0],b[1])+'-'+Math.max(b[0],b[1])]=1;rings[p.slice().sort((x,y)=>x-y).join(',')]=p}});
 let comp=0;{const seen=new Array(N).fill(false);for(let s=0;s<N;s++){if(seen[s])continue;comp++;const q=[s];seen[s]=true;while(q.length){const u=q.shift();for(const [v] of adj[u])if(!seen[v]){seen[v]=true;q.push(v)}}}}
 const nRings=Math.max(0,B.length-N+comp),R=Object.values(rings).sort((a,b)=>a.length-b.length).slice(0,nRings);
 R.forEach(r=>r.forEach(i=>inRing[i]=true));
 const order=(i,j)=>{const e=adj[i].find(e=>e[0]===j);return e?e[1]:0};
 const aromatic=r=>r.length===6&&r.every(isC)&&r.filter((a,k)=>order(a,r[(k+1)%6])===2).length===3;
 const inArom=new Array(N).fill(false);R.forEach(r=>{if(aromatic(r))r.forEach(i=>inArom[i]=true)});
 const cdeg=i=>adj[i].filter(e=>isC(e[0])).length;
 /* carbons reachable from `from` without passing through `block` (size of the group on that side) */
 const side=(from,block)=>{const seen=new Set([block,from]),q=[from];let c=isC(from)?1:0;while(q.length){const u=q.shift();for(const [v] of adj[u])if(!seen.has(v)){seen.add(v);if(isC(v))c++;q.push(v)}}return c};
 const env=c=>{if(inArom[c])return 'a benzene-ring carbon';if(inRing[c])return 'a ring carbon';const d=cdeg(c);
  if(d===0)return 'a carbon with no carbon neighbors';if(d===1)return 'an end carbon';
  const s=adj[c].filter(e=>isC(e[0])).map(e=>side(e[0],c)).sort((a,b)=>a-b);
  return (d===2?'a chain carbon':'a branch carbon')+' ('+s.join(' and ')+' carbons on its sides)'};
 const chg=a=>a.ch>0?' with a + charge':a.ch<0?' with a − charge':'';
 const hasCO=c=>adj[c].some(e=>e[1]===2&&!isC(e[0])&&!isH(e[0]));
 const parts=[(m.skel?'skeletal':'Lewis')+' structure'];if(nC)parts.push(plural(nC,'carbon'));
 const ph=[];
 R.forEach(r=>{const het=r.filter(i=>!isC(i)).map(i=>A[i].l);ph.push(aromatic(r)?'benzene ring':r.length+'-membered ring'+(het.length?' containing '+het.join(' and '):''))});
 /* longest carbon chain, for open-chain molecules: tells branched isomers apart */
 if(!nRings&&nC>=4){let best=0;const walk=(u,seen,len)=>{if(len>best)best=len;for(const [v] of adj[u])if(isC(v)&&!seen.has(v)){seen.add(v);walk(v,seen,len+1);seen.delete(v)}};
  A.forEach((a,i)=>{if(isC(i)&&cdeg(i)<=1)walk(i,new Set([i]),1)});if(best&&best<nC)ph.push('longest carbon chain '+best)}
 /* atoms other than C and H */
 A.forEach((a,i)=>{if(isC(i)||isH(i))return;const nb=adj[i].filter(e=>!isH(e[0])),cn=nb.filter(e=>isC(e[0])),name=a.l+chg(a);
  if(!nb.length){const h=adj[i].filter(e=>isH(e[0])).length;ph.push(h?'separate molecule: '+name+' with '+h+' H':'separate '+name);return}
  if(inRing[i]){if(cn.length>2||nb.length>2)ph.push(name+' in the ring, also bonded to '+(nb.length-2)+' other atom'+(nb.length-2===1?'':'s'));return}
  if(cn.length===1&&nb.length===1){ph.push(name+(cn[0][1]===2?' double-bonded to ':cn[0][1]===3?' triple-bonded to ':' on ')+env(cn[0][0]));return}
  if(cn.length>=2&&cn.length===nb.length){const g=cn.map(e=>{const c=e[0];return inArom[c]?'a benzene ring':inRing[c]?'a ring':side(c,i)+'-carbon group'+(hasCO(c)?' that starts with a C=O':'')}).sort();
   ph.push(name+' joining '+g.join(' and '));return}
  ph.push(name+' bonded to '+nb.map(e=>isC(e[0])?env(e[0]):A[e[0]].l).sort().join(' and '))});
 /* carbon-carbon multiple bonds (not the benzene ring) */
 B.forEach(b=>{const [i,j,o]=b;if(!(o===2||o===3)||!isC(i)||!isC(j)||(inArom[i]&&inArom[j]))return;const w=o===2?'double':'triple';
  if(ringBond[Math.min(i,j)+'-'+Math.max(i,j)]){ph.push('carbon–carbon '+w+' bond in the ring');return}
  const s=[side(i,j),side(j,i)].sort((a,b)=>a-b);let t='carbon–carbon '+w+' bond with '+s[0]+' and '+s[1]+' carbons on its two sides';
  if(o===2){const si=adj[i].filter(e=>e[0]!==j&&!isH(e[0])),sj=adj[j].filter(e=>e[0]!==i&&!isH(e[0]));
   if(si.length===1&&sj.length===1){const cr=k=>(A[j].x-A[i].x)*(A[k].y-A[i].y)-(A[j].y-A[i].y)*(A[k].x-A[i].x),p=cr(si[0][0])*cr(sj[0][0]);
    if(Math.abs(p)>1e-6)t+=p>0?', groups on the same side':', groups on opposite sides'}}
  ph.push(t)});
 /* where the substituents sit on each ring */
 R.forEach(r=>{const sub=r.map((a,k)=>adj[a].some(e=>!isH(e[0])&&!r.includes(e[0]))?k:-1).filter(k=>k>=0);
  if(sub.length===2){const d=Math.min(Math.abs(sub[0]-sub[1]),r.length-Math.abs(sub[0]-sub[1]));
   ph.push('two ring substituents '+(d===1?'on neighboring ring atoms':d===2?'one ring atom apart':r.length===6&&d===3?'on opposite ring atoms':d-1+' ring atoms apart'))}
  else if(sub.length>2){const gaps=sub.map((k,x)=>((sub[(x+1)%sub.length]-k+r.length)%r.length)||r.length).sort((a,b)=>a-b);ph.push(sub.length+' ring substituents, spaced '+gaps.join('-')+' around the ring')}});
 /* wedges, and dotted lines drawn between molecules */
 const end=i=>isH(i)?'an H on '+(adj[i][0]?A[adj[i][0][0]].l:'nothing'):A[i].l+(adj[i].some(e=>e[1]===2)?' of a C=O':(h=>h?' that has '+h+' H':'')(adj[i].filter(e=>isH(e[0])).length));
 const dir=(i,j)=>{const dx=A[j].x-A[i].x,dy=A[j].y-A[i].y,v=Math.abs(dy)>0.3?(dy<0?'up':'down'):'',h=Math.abs(dx)>0.3?(dx<0?'left':'right'):'';return v&&h?v+' and '+h:v||h||'out'};
 RB.forEach(b=>{if(b[2]===4||b[2]===5)ph.push((isC(b[1])?'a carbon group':A[b[1]].l)+' on a '+(b[2]===4?'solid wedge':'dashed wedge')+' bond pointing '+dir(b[0],b[1]));
  if(b[2]===0)ph.push('dotted line between '+end(b[0])+' and '+end(b[1]))});
 /* Lewis drawings: lone pairs and bond counts are what the question is about */
 if(!m.skel){A.forEach((a,i)=>{if(isH(i))return;const bo=adj[i].reduce((s,e)=>s+e[1],0);ph.push(a.l+' with '+plural(bo,'bond')+' and '+plural(a.lp,'lone pair'))});
  const nH=A.filter((a,i)=>isH(i)).length;if(nH)ph.push(plural(nH,'H atom'))}
 /* a C carrying a charge */
 A.forEach((a,i)=>{if(isC(i)&&a.ch)ph.push('carbon'+chg(a))});
 const cnt={};ph.forEach(p=>cnt[p]=(cnt[p]||0)+1);
 Object.keys(cnt).forEach(p=>parts.push(cnt[p]>1?cnt[p]+' × '+p:p));
 return parts.join(', ')}
/* condensed-formula style walk of the drawing (CH3-CH(OH)-CH3). Used only to tell apart two choices whose
   descriptions above come out the same, e.g. propyl and isopropyl groups on a ring. */
function molWalk(m){if(!m||!m.a)return '';
 const A=m.a.map(a=>({l:String(a[0]),ch:a[4]||0})),N=A.length,adj=A.map(()=>[]);(m.b||[]).forEach(b=>{if(A[b[0]]&&A[b[1]]&&b[2]!==0){const o=b[2]===4||b[2]===5?1:b[2]||1;adj[b[0]].push([b[1],o]);adj[b[1]].push([b[0],o])}});
 const isH=i=>A[i].l==='H',heavy=i=>adj[i].filter(e=>!isH(e[0]));
 const tok=i=>{const a=A[i];let t=a.l;if(t==='C'){const h=m.skel?Math.max(0,4-adj[i].reduce((s,e)=>s+e[1],0)-Math.abs(a.ch)):adj[i].filter(e=>isH(e[0])).length;t='C'+(h?'H'+(h>1?h:''):'')}
  return t+(a.ch>0?'+':a.ch<0?'\u2212':'')};
 const sym=o=>o===2?'=':o===3?'\u2261':'';
 const walk=(u,p,seen)=>{seen.add(u);const kids=[];for(const [v,o] of heavy(u)){if(v===p)continue;if(seen.has(v)){kids.push([sym(o)+'ring',0]);continue}kids.push([sym(o)+walk(v,u,seen),1])}
  kids.sort((a,b)=>a[0].length-b[0].length||(a[0]<b[0]?-1:1));const main=kids.length&&kids[kids.length-1][1]?kids.pop():null;
  return tok(u)+kids.map(k=>'('+k[0]+')').join('')+(main?(/^[=\u2261]/.test(main[0])?'':'-')+main[0]:'')};
 const starts=A.map((a,i)=>i).filter(i=>!isH(i)&&heavy(i).length<=1);if(!starts.length)starts.push(A.findIndex((a,i)=>!isH(i)));
 const out=[];const all=new Set();
 let best=null;starts.forEach(s=>{const seen=new Set(),w=walk(s,-1,seen);if(best===null||w.length<best[0].length||(w.length===best[0].length&&w<best[0]))best=[w,seen]});
 if(best){out.push(best[0]);best[1].forEach(i=>all.add(i))}
 A.forEach((a,i)=>{if(!isH(i)&&!all.has(i)){const seen=new Set();out.push(walk(i,-1,seen));seen.forEach(j=>all.add(j))}});
 return out.join(' and ')}
/* labels for all structure choices of one question; duplicates get the walk appended */
function optLabels(q){const d=q.c.map((c,k)=>String(c).startsWith('\u00a7')?molDesc(q.cs&&q.cs[k]):null),n={};d.forEach(x=>{if(x!==null)n[x]=(n[x]||0)+1});
 return d.map((x,k)=>x!==null&&n[x]>1?x+'; drawn as '+molWalk(q.cs[k]):x)}
const optLabel=(q,k,L)=>{if(!String(q.c[k]).startsWith('§'))return '';const d=q.__lab||(q.__lab=optLabels(q));return `Choice ${L}: ${d[k]}`};
const optHTML=(q,k)=>(String(q.c[k]).startsWith('§')?'':q.c[k])+(q.cs&&q.cs[k]?`<span class="fbx-optmol">${molSVG(q.cs[k],0.8)}</span>`:'');
/* ---------- FBX practice UI (hand-written; the drawing code above is extracted from Final Boss) ---------- */
const FBX_DIFF=['','● Easy','●● Medium','●●● Hard'];
const fbxGet=(k,d)=>{try{const v=localStorage.getItem(k);return v?JSON.parse(v):d}catch(e){return d}};
const fbxSet=(k,v)=>{try{localStorage.setItem(k,JSON.stringify(v))}catch(e){}};
const FBX_REVIEW_GAP=4; // a missed question comes back after this many other answers
function fbxMount(root,items,opts){
 opts=opts||{};items=(items||[]).filter(q=>q&&q.id&&Array.isArray(q.c)&&q.c.length===4);
 if(root.__fbx)root.__fbx.destroy();
 const KEY=opts.storageKey||'fbx-progress',tk=q=>q.g||q.t;
 const TL=(opts.topics||[]).map(t=>Array.isArray(t)?t:[t.id,t.name,t.icon||'']),TN={},TI={};TL.forEach(([id,n,ic])=>{TN[id]=n;TI[id]=ic||''});
 const byId={};items.forEach(q=>byId[q.id]=q);
 const present=[...new Set(items.map(tk))],order=TL.map(t=>t[0]).filter(t=>present.includes(t)).concat(present.filter(t=>!(t in TN)));
 const tname=t=>TN[t]||t,count={};items.forEach(q=>{const t=tk(q);count[t]=(count[t]||0)+1});
 const blank=()=>({v:1,topic:'all',deck:[],miss:[],n:0,first:0,streak:0,best:0,byT:{},cur:null});
 let P=Object.assign(blank(),fbxGet(KEY,{})||{});
 if(!Array.isArray(P.deck))P.deck=[];P.deck=P.deck.filter(id=>byId[id]);
 if(!Array.isArray(P.miss))P.miss=[];P.miss=P.miss.filter(m=>Array.isArray(m)&&byId[m[0]]);
 if(!P.byT||typeof P.byT!=='object')P.byT={};
 if(P.topic!=='all'&&!order.includes(P.topic))P.topic='all';
 const save=()=>fbxSet(KEY,P);
 const S={q:null,order:null,sel:null,tries:0,done:false,hinted:false,again:false,note:''};
 root.classList.add('fbx');
 root.innerHTML=`<div class="fbx-card"><div class="fbx-head"><label class="fbx-tsel"><span>Topic</span><select aria-label="Choose a topic"></select></label><div class="fbx-score" aria-live="polite"></div></div>
<div class="fbx-note" hidden></div><div class="fbx-meta"></div><div class="fbx-q"></div><div class="fbx-opts" role="group" aria-label="Answer choices"></div>
<div class="fbx-btns"><button type="button" class="fbx-btn fbx-check">Check</button><button type="button" class="fbx-btn fbx-hintb">💡 Hint</button><button type="button" class="fbx-btn fbx-next">New Question ▸</button></div>
<div class="fbx-hint" hidden></div><div class="fbx-fb" role="status" aria-live="polite"></div></div>`;
 const E=c=>root.querySelector('.fbx-'+c),sel=E('tsel').querySelector('select');
 const inPool=q=>P.topic==='all'||tk(q)===P.topic,pool=()=>items.filter(inPool);
 function acc(t){const a=P.byT[t];return a&&a[1]?Math.round(100*a[0]/a[1])+'%':''}
 function buildSel(){sel.innerHTML=`<option value="all">📚 All topics (${items.length})</option>`+order.map(t=>{const a=acc(t);return `<option value="${esc(t)}">${TI[t]?TI[t]+' ':''}${esc(tname(t))} (${count[t]})${a?' • '+a+' right':''}</option>`}).join('');sel.value=P.topic}
 function score(){const pl=pool(),ids=new Set(pl.map(q=>q.id)),left=P.deck.filter(id=>ids.has(id)).length,rev=P.miss.filter(m=>ids.has(m[0])).length;
  E('score').innerHTML=`<span class="fbx-pill ok">✅ ${P.first} / ${P.n} first try</span><span class="fbx-pill st">🔥 Streak ${P.streak} • best ${P.best}</span><span class="fbx-pill">🃏 ${left||pl.length} left in deck</span>${rev?`<span class="fbx-pill rv">🔁 ${rev} to review</span>`:''}`}
 function fb(k,h){const f=E('fb');f.className='fbx-fb '+k;f.innerHTML=h}
 function note(t){const n=E('note');n.hidden=!t;n.textContent=t||''}
 function pick(){const pl=pool();if(!pl.length)return null;const ids=new Set(pl.map(q=>q.id)),cur=S.q&&S.q.id;
  let k=P.miss.findIndex(m=>ids.has(m[0])&&m[1]<=P.n&&m[0]!==cur);
  if(k>=0){const id=P.miss.splice(k,1)[0][0];S.again=true;return byId[id]}
  S.again=false;let i=P.deck.findIndex(id=>ids.has(id)&&id!==cur);
  if(i<0){const queued=new Set(P.miss.map(m=>m[0])),fresh=shuf(pl.map(q=>q.id).filter(id=>!queued.has(id)&&id!==cur));
   if(!fresh.length){k=P.miss.findIndex(m=>ids.has(m[0])&&m[0]!==cur);if(k>=0){const id=P.miss.splice(k,1)[0][0];S.again=true;return byId[id]}return byId[cur]||pl[0]}
   if(P.deck.length||P.n)S.note='🎉 You have seen every question'+(P.topic==='all'?'':' in this topic')+'. The deck is reshuffled!';
   P.deck=P.deck.filter(id=>!ids.has(id)).concat(fresh);i=P.deck.findIndex(id=>ids.has(id))}
  return byId[P.deck.splice(i,1)[0]]}
 function show(q){S.q=q;S.order=opts.shuffle===false?[0,1,2,3]:shuf([0,1,2,3]);S.sel=null;S.tries=0;S.done=false;S.hinted=false;S.lastWhy='';P.cur=q?q.id:null;save();
  note(S.note);S.note='';E('hint').hidden=true;E('hint').innerHTML='';fb('','');
  const ck=E('check'),hb=E('hintb'),nx=E('next');nx.classList.remove('go');
  if(!q){E('meta').innerHTML='';E('q').innerHTML='<div class="fbx-empty">No questions for this topic yet.</div>';E('opts').innerHTML='';ck.disabled=hb.disabled=true;score();return}
  ck.disabled=false;hb.disabled=!q.h;const t=tk(q);
  E('meta').innerHTML=`${S.again?'<span class="fbx-chip again">🔁 Review</span>':''}<span class="fbx-chip">${TI[t]?TI[t]+' ':''}${esc(tname(t))}</span>${q.k?'<span class="fbx-chip calc">🧮 Calculator</span>':''}<span class="fbx-chip lvl">${FBX_DIFF[q.d]||''}</span>`;
  E('q').innerHTML=qHTML(q);
  E('opts').innerHTML=S.order.map((k,i)=>{const al=optLabel(q,k,'ABCD'[i]);return `<button type="button" class="fbx-opt" data-k="${k}" aria-pressed="false"${al?` aria-label="${esc(al)}"`:''}><span class="fbx-L">${'ABCD'[i]}</span><span class="fbx-ot">${optHTML(q,k)}</span></button>`}).join('');
  score()}
 function optBtn(k){return E('opts').querySelector(`.fbx-opt[data-k="${k}"]`)}
 function check(){if(S.done||!S.q)return;if(S.sel==null){fb('bad','👆 Tap an answer first, then press Check.');return}
  const b=optBtn(S.sel);
  if(S.sel===0)return finish(true);
  b.classList.remove('sel');b.classList.add('wrong');b.disabled=true;b.setAttribute('aria-pressed','false');S.sel=null;
  const why=whyNot(S.q,+b.dataset.k);S.lastWhy=why;
  if(S.tries===0){S.tries=1;fb('bad','🔎 Not quite. '+(why?why+' ':'')+'Try again!'+(S.hinted?'':' Stuck? Tap 💡 Hint.'));return}
  S.tries=2;finish(false)}
 /* Per-option feedback: optional q.x array, indexed like q.c (q.x[0] unused), explains why a distractor is wrong. */
 function whyNot(q,k){const x=q&&Array.isArray(q.x)?q.x[k]:null;return x?'<span class="fbx-why">'+x+'</span>':''}
 function finish(solved){const q=S.q,t=tk(q),first=solved&&S.tries===0;S.done=true;
  root.querySelectorAll('.fbx-opt').forEach(b=>{b.disabled=true;if(+b.dataset.k===0){b.classList.add('right');b.classList.remove('sel')}});
  P.n++;const a=P.byT[t]||(P.byT[t]=[0,0]);a[1]++;
  if(first){a[0]++;P.first++;P.streak++;P.best=Math.max(P.best,P.streak)}else{P.streak=0;P.miss=P.miss.filter(m=>m[0]!==q.id);P.miss.push([q.id,P.n+FBX_REVIEW_GAP])}
  P.cur=null;save();
  const L='ABCD'[S.order.indexOf(0)],txt=String(q.c[0]).startsWith('§')?'':' ('+q.c[0]+')',later='<small>🔁 This question will come back later for review.</small>';
  fb(solved?'good':'info',first?'✅ <b>Correct!</b> '+q.w:solved?'✅ <b>Got it on the second try.</b> '+q.w+later:`👀 The answer is <b>${L}</b>${txt}. ${S.lastWhy?S.lastWhy+' ':''}${q.w}${later}`);
  E('check').disabled=true;E('hintb').disabled=true;E('next').classList.add('go');buildSel();score();
  try{if(opts.onAnswer)opts.onAnswer(q,first,{solved,revealed:!solved,tries:S.tries+(solved?1:0),hinted:S.hinted,review:S.again,topic:tname(t),topicId:t})}catch(e){console.error(e)}
  const f=E('fb'),r=f.getBoundingClientRect();if(r.bottom>innerHeight&&f.scrollIntoView)f.scrollIntoView({behavior:'smooth',block:'nearest'})}
 function hint(){if(S.done||!S.q||!S.q.h)return;S.hinted=true;const h=E('hint');h.innerHTML='💡 '+S.q.h;h.hidden=false;E('hintb').disabled=true}
 function next(){if(S.q&&!S.done){P.deck=P.deck.filter(id=>id!==S.q.id);P.deck.push(S.q.id)}show(pick());const r=root.getBoundingClientRect();if(r.top<0&&root.scrollIntoView)root.scrollIntoView({behavior:'smooth',block:'start'})}
 function onClick(e){const o=e.target.closest('.fbx-opt');
  if(o&&root.contains(o)){if(S.done||o.disabled)return;S.sel=+o.dataset.k;root.querySelectorAll('.fbx-opt').forEach(x=>{const on=x===o;x.classList.toggle('sel',on);x.setAttribute('aria-pressed',on?'true':'false')});if(E('fb').classList.contains('bad'))fb('','');return}
  if(e.target.closest('.fbx-check'))check();else if(e.target.closest('.fbx-hintb'))hint();else if(e.target.closest('.fbx-next'))next()}
 function onSel(){if(S.q&&!S.done){P.deck=P.deck.filter(id=>id!==S.q.id);P.deck.unshift(S.q.id)}P.topic=sel.value;save();S.q=null;show(pick())}
 root.addEventListener('click',onClick);sel.addEventListener('change',onSel);
 buildSel();const resume=P.cur&&byId[P.cur]&&inPool(byId[P.cur])?byId[P.cur]:null;show(resume||pick());
 const api={next,setTopic(t){sel.value=(t==='all'||order.includes(t))?t:'all';onSel()},get progress(){return JSON.parse(JSON.stringify(P))},
  reset(){P=blank();save();buildSel();S.q=null;show(pick())},
  destroy(){root.removeEventListener('click',onClick);root.innerHTML='';root.classList.remove('fbx');delete root.__fbx}};
 root.__fbx=api;return api}
window.FBX={version:FBX_VERSION,mount:fbxMount,qHTML,optHTML,optLabel,optLabels,molDesc,molWalk,molSVG,figBlock,structBlock};

})();