/* Clean inline-SVG pathway / flow diagrams for the textbook (no <style>, no <marker>, no foreignObject,
   so LibreTexts keeps every element).  Usage:  node tools/pathway.js spec.json > out.svg
   Spec: {
     title?: "…", colw?: 150, rowh?: 90, pad?: 16, font?: 15,
     nodes: [{id, label (use \n for line breaks), col, row, kind?: "mol"|"energy"|"enzyme"|"note"|"tissue"|"ghost", w?, h?}],
     edges: [{from, to, label?, kind?: "main"|"side"|"dashed"|"both", via?: [[col,row],...], curve?: true, labelPos?: 0..1, labelSide?: "above"|"below"}],
     groups?: [{label, cols:[c0,c1], rows:[r0,r1], fill?}]
   }
   col/row are grid coordinates (floats allowed). Nodes are centred on their grid point. */
const fs=require('fs');
const spec=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const esc=s=>String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;');
const COLW=spec.colw||150,ROWH=spec.rowh||90,PAD=spec.pad||16,FS=spec.font||15;
const FONT='Nunito,Inter,Helvetica,Arial,sans-serif';
const INK='#2d3f4b',MUTED='#4f5a74',LINE='#c9d1dc';
const KIND={mol:{fill:'#ffffff',stroke:'#8fa6b8',text:INK,bold:700},
            energy:{fill:'#fff6e2',stroke:'#e2c77a',text:'#80601a',bold:800},
            enzyme:{fill:'none',stroke:'none',text:'#3b5f7a',bold:700,italic:true},
            note:{fill:'#f3effd',stroke:'#c9b8ea',text:'#4a3a73',bold:600},
            tissue:{fill:'#e8f6ef',stroke:'#a9d9c2',text:'#23704f',bold:800},
            ghost:{fill:'none',stroke:'none',text:MUTED,bold:600},
            start:{fill:'#f2e8f7',stroke:'#b48cc8',text:'#5b3a72',bold:800}};
const allC=spec.nodes.map(n=>n.col).concat(...(spec.edges||[]).map(e=>(e.via||[]).map(v=>v[0]))), allR=spec.nodes.map(n=>n.row).concat(...(spec.edges||[]).map(e=>(e.via||[]).map(v=>v[1])));
const cols=Math.ceil(Math.max(...allC))+1, rows=Math.ceil(Math.max(...allR))+1;
const px=c=>PAD+COLW*(c+0.5), py=r=>PAD+(spec.title?30:0)+ROWH*(r+0.5);
const nodes={};
for(const n of spec.nodes){
  const lines=String(n.label).split('\n');
  const k=KIND[n.kind||'mol'];
  const tw=Math.max(...lines.map(l=>l.length))*FS*0.56+22;
  n.w=n.w||Math.min(Math.max(tw,64),COLW*1.6); n.h=n.h||(lines.length*(FS+4)+14);
  n.x=px(n.col); n.y=py(n.row); n.lines=lines; n.k=k; nodes[n.id]=n;
}
const W=PAD*2+COLW*cols, H=PAD*2+(spec.title?30:0)+ROWH*rows;
let out='',labels='';
if(spec.groups) for(const g of spec.groups){
  const x0=PAD+COLW*g.cols[0], x1=PAD+COLW*(g.cols[1]+1), y0=PAD+(spec.title?30:0)+ROWH*g.rows[0], y1=PAD+(spec.title?30:0)+ROWH*(g.rows[1]+1);
  out+=`<rect x="${x0+4}" y="${y0+4}" width="${x1-x0-8}" height="${y1-y0-8}" rx="16" fill="${g.fill||'#f7f8fb'}" stroke="${LINE}" stroke-dasharray="6 4" stroke-width="1.5"/>`;
  out+=`<text x="${x0+16}" y="${y0+24}" font-size="${FS-2}" font-weight="800" fill="${MUTED}" font-family="${FONT}">${esc(g.label)}</text>`;
}
/* edges */
function anchor(n,tx,ty){ // point on node boundary toward (tx,ty)
  const dx=tx-n.x, dy=ty-n.y; if(!dx&&!dy) return [n.x,n.y];
  const hw=n.w/2+4, hh=n.h/2+4; const sx=Math.abs(dx)>1e-6?hw/Math.abs(dx):1e9, sy=Math.abs(dy)>1e-6?hh/Math.abs(dy):1e9; const s=Math.min(sx,sy);
  return [n.x+dx*s, n.y+dy*s];
}
function arrowHead(x,y,ang,color){const a=Math.PI/7,L=11;const p1=[x-L*Math.cos(ang-a),y-L*Math.sin(ang-a)],p2=[x-L*Math.cos(ang+a),y-L*Math.sin(ang+a)];return `<path d="M${x.toFixed(1)} ${y.toFixed(1)} L${p1[0].toFixed(1)} ${p1[1].toFixed(1)} L${p2[0].toFixed(1)} ${p2[1].toFixed(1)} Z" fill="${color}"/>`}
for(const e of spec.edges||[]){
  const a=nodes[e.from], b=nodes[e.to]; if(!a||!b) throw new Error('edge node missing: '+e.from+'->'+e.to);
  const color=e.kind==='side'?'#8a97a6':INK, sw=e.kind==='side'?1.8:2.4, dash=e.kind==='dashed'||e.kind==='side-dashed'?' stroke-dasharray="7 5"':'';
  const pts=[]; const via=(e.via||[]).map(([c,r])=>[px(c),py(r)]);
  const first=via.length?via[0]:[b.x,b.y]; pts.push(anchor(a,first[0],first[1])); for(const v of via) pts.push(v);
  const last=pts[pts.length-1]; pts.push(anchor(b,last[0],last[1]));
  let d; if(e.curve&&pts.length===2){const [p,q]=pts; const mx=(p[0]+q[0])/2+(q[1]-p[1])*0.25, my=(p[1]+q[1])/2-(q[0]-p[0])*0.25; d=`M${p[0].toFixed(1)} ${p[1].toFixed(1)} Q${mx.toFixed(1)} ${my.toFixed(1)} ${q[0].toFixed(1)} ${q[1].toFixed(1)}`;}
  else d='M'+pts.map(p=>p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' L');
  out+=`<path d="${d}" fill="none" stroke="${color}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round"${dash}/>`;
  const pe=pts[pts.length-1], pp=pts[pts.length-2]; out+=arrowHead(pe[0],pe[1],Math.atan2(pe[1]-pp[1],pe[0]-pp[0]),color);
  if(e.kind==='both'){const p0=pts[0],p1=pts[1]; out+=arrowHead(p0[0],p0[1],Math.atan2(p0[1]-p1[1],p0[0]-p1[0]),color);}
  if(e.label){
    const t=e.labelPos==null?0.5:e.labelPos; let seg=0,len=0,L=[];for(let i=1;i<pts.length;i++){const l=Math.hypot(pts[i][0]-pts[i-1][0],pts[i][1]-pts[i-1][1]);L.push(l);len+=l}
    let s=t*len,i=0;while(i<L.length-1&&s>L[i]){s-=L[i];i++} const f=L[i]?s/L[i]:0; const x=pts[i][0]+(pts[i+1][0]-pts[i][0])*f, y=pts[i][1]+(pts[i+1][1]-pts[i][1])*f;
    const ang=Math.atan2(pts[i+1][1]-pts[i][1],pts[i+1][0]-pts[i][0]); const horiz=Math.abs(Math.cos(ang))>0.7;
    const lines=String(e.label).split('\n'); const lw=Math.max(...lines.map(l=>l.length))*(FS-3)*0.56+10, lh=lines.length*(FS-1);
    let lx=x, ly=y; if(horiz){ly+= (e.labelSide==='below'? lh/2+8 : -(lh/2+6));} else {lx+= (e.labelSide==='below'? -(lw/2+6) : lw/2+6);}
    labels+=`<rect x="${(lx-lw/2).toFixed(1)}" y="${(ly-lh/2-2).toFixed(1)}" width="${lw.toFixed(1)}" height="${(lh+4).toFixed(1)}" rx="6" fill="#ffffff" fill-opacity="0.92"/>`;
    lines.forEach((l,j)=>{labels+=`<text x="${lx.toFixed(1)}" y="${(ly-lh/2+(FS-3)+j*(FS-1)-2).toFixed(1)}" text-anchor="middle" font-size="${FS-3}" font-weight="700" font-style="italic" fill="${e.kind==='side'?'#6b7a85':'#3b5f7a'}" font-family="${FONT}">${esc(l)}</text>`});
  }
}
/* nodes */
for(const n of spec.nodes){
  const k=n.k; if(k.fill!=='none') out+=`<rect x="${(n.x-n.w/2).toFixed(1)}" y="${(n.y-n.h/2).toFixed(1)}" width="${n.w.toFixed(1)}" height="${n.h.toFixed(1)}" rx="${n.kind==='energy'?n.h/2:10}" fill="${k.fill}" stroke="${k.stroke}" stroke-width="2"/>`;
  n.lines.forEach((l,j)=>{const y=n.y-(n.lines.length-1)*(FS+4)/2+j*(FS+4)+FS*0.36; out+=`<text x="${n.x.toFixed(1)}" y="${y.toFixed(1)}" text-anchor="middle" font-size="${FS}" font-weight="${k.bold}"${k.italic?' font-style="italic"':''} fill="${k.text}" font-family="${FONT}">${esc(l)}</text>`});
}
out+=labels;
if(spec.title) out=`<text x="${PAD+4}" y="${PAD+18}" font-size="${FS+2}" font-weight="800" fill="${INK}" font-family="${FONT}">${esc(spec.title)}</text>`+out;
const svg=`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" style="max-width:100%;height:auto;display:block;margin:0 auto" role="img" aria-label="${esc(spec.alt||spec.title||'pathway diagram')}"><rect width="100%" height="100%" rx="14" fill="#ffffff" stroke="#e2dccd" stroke-width="2" stroke-dasharray="6 4"/>${out}</svg>`;
process.stdout.write(svg);
