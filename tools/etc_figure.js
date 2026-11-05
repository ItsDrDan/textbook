/* Electron transport chain figure in the classic textbook-cartoon style (phospholipid bilayers, oval complexes,
   red electron path, H+ circles, ATP synthase lollipop). Plain SVG: no <style>, <marker> or ids.
   node tools/etc_figure.js  ->  figures/pathways/etc/etc.svg  (+ etc_game.svg, same drawing without the outer membrane) */
const fs = require('fs'), path = require('path');
const FONT = 'Nunito,Helvetica,Arial,sans-serif', INK = '#2d3f4b', MUTED = '#5a6478';
const PINK = '#f6d7e3', PINK_S = '#8a4d63', HEAD = '#c9c3ec', HEAD_S = '#4b4a8a', TAIL = '#4b4a8a', RED = '#a3262b';
const r1 = n => Math.round(n * 10) / 10, esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;');
/* text with _sub and ^sup */
function T(x, y, s, o = {}) {
  const fs_ = o.fs || 16; let body = '';
  String(s).split(/(_[0-9a-z]+|\^[0-9+\-−]+)/).forEach(p => {
    if (!p) return;
    if (p[0] === '_') body += `<tspan font-size="${r1(fs_ * .72)}" dy="${r1(fs_ * .28)}">${esc(p.slice(1))}</tspan><tspan dy="${r1(-fs_ * .28)}">&#8203;</tspan>`;
    else if (p[0] === '^') body += `<tspan font-size="${r1(fs_ * .72)}" dy="${r1(-fs_ * .42)}">${esc(p.slice(1).replace('-', '−'))}</tspan><tspan dy="${r1(fs_ * .42)}">&#8203;</tspan>`;
    else body += esc(p);
  });
  return `<text x="${r1(x)}" y="${r1(y)}" font-family="${FONT}" font-size="${fs_}" font-weight="${o.w || 800}" fill="${o.c || INK}" text-anchor="${o.a || 'middle'}"${o.it ? ' font-style="italic"' : ''}>${body}</text>`;
}
const head = (x, y, ang, c, s = 11) => { const a = ang * Math.PI / 180, p = t => [x - s * Math.cos(a + t), y - s * Math.sin(a + t)]; const [x1, y1] = p(.42), [x2, y2] = p(-.42); return `<path d="M${r1(x)} ${r1(y)}L${r1(x1)} ${r1(y1)}L${r1(x2)} ${r1(y2)}z" fill="${c}"/>`; };
/* membrane along y = y0 + k*(x - cx)^2 ; heads on both faces, wavy tails between */
function bilayer(x0, x1, y0, k, cx, gap, skip = []) {
  const Y = x => y0 + k * (x - cx) ** 2; let o = '';
  const band = `M${x0} ${r1(Y(x0) - gap / 2 - 7)} ` + Array.from({ length: 41 }, (_, i) => { const x = x0 + (x1 - x0) * i / 40; return `L${r1(x)} ${r1(Y(x) - gap / 2 - 7)}`; }).join(' ') + ' ' + Array.from({ length: 41 }, (_, i) => { const x = x1 - (x1 - x0) * i / 40; return `L${r1(x)} ${r1(Y(x) + gap / 2 + 7)}`; }).join(' ') + 'z';
  o += `<path d="${band}" fill="#eef0fb"/>`;
  for (let x = x0 + 6; x < x1 - 4; x += 13) {
    if (skip.some(([a, b]) => x > a && x < b)) continue;
    const y = Y(x), ytop = y - gap / 2, ybot = y + gap / 2;
    o += `<path d="M${r1(x - 2)} ${r1(ytop + 5)} l3 4 l-3 4 l3 4 M${r1(x + 2)} ${r1(ytop + 5)} l3 4 l-3 4 l3 4" fill="none" stroke="${TAIL}" stroke-width="1.1" opacity=".75"/>`;
    o += `<path d="M${r1(x - 2)} ${r1(ybot - 5)} l3 -4 l-3 -4 l3 -4 M${r1(x + 2)} ${r1(ybot - 5)} l3 -4 l-3 -4 l3 -4" fill="none" stroke="${TAIL}" stroke-width="1.1" opacity=".75"/>`;
    o += `<circle cx="${r1(x)}" cy="${r1(ytop)}" r="5.2" fill="${HEAD}" stroke="${HEAD_S}" stroke-width="1"/><circle cx="${r1(x)}" cy="${r1(ybot)}" r="5.2" fill="${HEAD}" stroke="${HEAD_S}" stroke-width="1"/>`;
  }
  return { svg: o, Y };
}
const ell = (cx, cy, rx, ry, lab, fsz = 22) => `<ellipse cx="${cx}" cy="${cy}" rx="${rx}" ry="${ry}" fill="${PINK}" fill-opacity=".92" stroke="${PINK_S}" stroke-width="2"/>` + (lab ? T(cx, cy + fsz * .35, lab, { fs: fsz, w: 900, c: '#5b2a3c' }) : '');
const hion = (x, y) => `<circle cx="${x}" cy="${y}" r="15" fill="#f7e3ec" stroke="${PINK_S}" stroke-width="1.6"/>` + T(x - 2, y + 5, 'H^+', { fs: 14, w: 800, c: '#5b2a3c' });
const box = (x, y, w, h, lab, fill, stroke) => `<rect x="${x - w / 2}" y="${y - h / 2}" width="${w}" height="${h}" rx="7" fill="${fill}" stroke="${stroke}" stroke-width="1.8"/>` + T(x, y + 6, lab, { fs: 16 });
const curve = (d, c = MUTED, w = 2.4) => `<path d="${d}" fill="none" stroke="${c}" stroke-width="${w}" stroke-linecap="round"/>`;

function build({ outer = true } = {}) {
  const W = 1040, cx = 450; let o = '';
  const topPad = outer ? 0 : -150; // shift everything up when no outer membrane
  const g = s => `<g transform="translate(0 ${topPad})">${s}</g>`;
  let body = '';
  if (outer) {
    body += T(20, 30, 'Cytoplasm', { a: 'start', fs: 16, c: MUTED, w: 700 });
    const om = bilayer(10, 900, 70, 0.00012, cx, 22); body += om.svg;
    body += curve('M912 50 q8 0 8 10 v20 q0 6 6 6 q-6 0 -6 6 v20 q0 10 -8 10', MUTED, 1.6) + T(934, 84, 'Outer', { a: 'start', fs: 14, w: 700, c: MUTED }) + T(934, 101, 'membrane', { a: 'start', fs: 14, w: 700, c: MUTED });
  }
  body += T(outer ? 20 : 20, outer ? 158 : 168, 'Intermembrane space (high H^+)', { a: 'start', fs: 16, c: '#8a4d63', w: 800 });
  // H+ crowd in intermembrane space
  [[120, 190], [210, 172], [300, 196], [380, 168], [560, 172], [650, 196], [720, 168], [870, 196]].forEach(([x, y]) => body += hion(x, y));
  const IMy = 300; // inner membrane centre
  const im = bilayer(10, 900, IMy, 0.0001, cx, 30, [[105, 205], [262, 302], [335, 410], [530, 615], [742, 788]]); body += im.svg;
  body += curve('M912 262 q8 0 8 10 v18 q0 6 6 6 q-6 0 -6 6 v18 q0 10 -8 10', MUTED, 1.6) + T(934, 292, 'Inner', { a: 'start', fs: 14, w: 700, c: MUTED }) + T(934, 309, 'membrane', { a: 'start', fs: 14, w: 700, c: MUTED });
  
  const Y = im.Y;
  // complexes
  const cI = [155, Y(155) + 8], cII = [255, Y(255) + 70], cQ = [282, Y(282) - 4], cIII = [372, Y(372)], cC = [455, Y(455) - 62], cIV = [572, Y(572)];
  let cplx = ell(cI[0], cI[1], 46, 72, 'I');
  cplx += `<ellipse cx="${cII[0]}" cy="${cII[1] + 4}" rx="38" ry="56" fill="${PINK}" stroke="${PINK_S}" stroke-width="2"/>` + T(cII[0], cII[1] - 12, 'II', { fs: 20, w: 900, c: '#5b2a3c' }) + T(cII[0], cII[1] + 22, 'FADH_2', { fs: 14, w: 800, c: '#23704f' });
  cplx += ell(cIII[0], cIII[1], 36, 64, 'III');
  cplx += ell(cIV[0] - 20, cIV[1], 22, 60, '') + ell(cIV[0] + 20, cIV[1], 22, 60, '') + T(cIV[0], cIV[1] + 8, 'IV', { fs: 22, w: 900, c: '#5b2a3c' });
  cplx += ell(cQ[0], cQ[1], 30, 15, 'Q', 15) + T(cQ[0], cQ[1] - 22, 'CoQ', { fs: 13, w: 800, c: MUTED });
  cplx += ell(cC[0], cC[1], 38, 20, 'Cyt c', 15);
  // ATP synthase: membrane channel + stalk + head in matrix
  const sx = 765, sy = Y(sx);
  body += `<rect x="${sx - 22}" y="${sy - 44}" width="44" height="88" rx="16" fill="${PINK}" stroke="${PINK_S}" stroke-width="2"/>`;
  body += `<rect x="${sx - 8}" y="${sy + 40}" width="16" height="40" fill="${PINK}" stroke="${PINK_S}" stroke-width="2"/>` + `<circle cx="${sx}" cy="${sy + 118}" r="46" fill="${PINK}" stroke="${PINK_S}" stroke-width="2"/>`;
  body += `<line x1="${sx - 6}" y1="${sy - 40}" x2="${sx - 6}" y2="${sy + 120}" stroke="${RED}" stroke-width="2"/><line x1="${sx + 6}" y1="${sy - 40}" x2="${sx + 6}" y2="${sy + 120}" stroke="${RED}" stroke-width="2"/>`;
  // H+ flowing back through ATP synthase
  body += hion(sx - 44, sy - 92) + curve(`M${sx - 32} ${sy - 80} Q ${sx} ${sy - 80} ${sx} ${sy - 50}`, '#8a4d63', 2.6) + `<line x1="${sx}" y1="${sy - 40}" x2="${sx}" y2="${sy + 150}" stroke="#8a4d63" stroke-width="2.6"/>` + head(sx, sy + 158, 90, '#8a4d63', 12);
  body += T(sx + 36, sy - 66, 'H^+ flows back', { a: 'start', fs: 14, w: 800, c: '#8a4d63' }) + T(sx + 36, sy - 49, 'into the matrix', { a: 'start', fs: 14, w: 800, c: '#8a4d63' });
  body += T(sx, sy + 190, 'ATP synthase', { fs: 15, w: 900, c: '#5b2a3c' });
  body += box(sx + 120, sy + 98, 104, 30, 'ADP + P_i', '#fff6e2', '#c9a24a') + `<ellipse cx="${sx + 120}" cy="${sy + 160}" rx="40" ry="18" fill="#ffd36b" stroke="#b7791f" stroke-width="2"/>` + T(sx + 120, sy + 166, 'ATP', { fs: 17, w: 900 });
  body += curve(`M${sx + 88} ${sy + 110} Q ${sx + 66} ${sy + 132} ${sx + 84} ${sy + 152}`, '#8a5a00', 2.4) + head(sx + 86, sy + 155, 50, '#8a5a00', 10);
  // electron path (thick red): NADH -> I -> Q -> III -> cyt c -> IV -> O2 ; FADH2 at II -> Q
  const ePath = `M90 ${Y(90) + 118} C 120 ${Y(120) + 112}, ${cI[0]} ${cI[1] + 60}, ${cI[0]} ${cI[1] + 10} S ${cQ[0] - 30} ${cQ[1] - 10}, ${cQ[0]} ${cQ[1]} S ${cIII[0] - 10} ${cIII[1] - 40}, ${cIII[0]} ${cIII[1] - 30} S ${cC[0] - 20} ${cC[1]}, ${cC[0]} ${cC[1]} S ${cIV[0] - 10} ${cIV[1] - 40}, ${cIV[0]} ${cIV[1]} S ${cIV[0] + 10} ${cIV[1] + 70}, ${cIV[0] + 30} ${cIV[1] + 92}`;
  body += `<path d="${ePath}" fill="none" stroke="${RED}" stroke-width="5" stroke-linecap="round" opacity=".9"/>` + head(cIV[0] + 36, cIV[1] + 98, 50, RED, 14);
  body += `<path d="M${cII[0] - 4} ${cII[1] + 26} C ${cII[0] - 6} ${cII[1]}, ${cQ[0] - 10} ${cQ[1] + 30}, ${cQ[0] - 2} ${cQ[1] + 8}" fill="none" stroke="${RED}" stroke-width="5" stroke-linecap="round" opacity=".9"/>`;
  body += cplx + T(cC[0] + 50, cC[1] + 4, 'e^−', { fs: 18, w: 900, c: RED, a: 'start' }) + T(118, Y(118) + 112, 'e^−', { fs: 18, w: 900, c: RED, a: 'start' });
  // matrix side: NADH -> NAD+, succinate -> fumarate (FAD/FADH2), O2 -> H2O
  const mY = Y(155) + 140;
  body += box(78, mY, 84, 30, 'NADH', '#eaf4fb', '#2c5f9c') + box(78, mY + 64, 84, 30, 'NAD^+', '#eaf4fb', '#2c5f9c');
  body += curve(`M102 ${mY + 15} Q 132 ${mY + 32} 106 ${mY + 48}`, '#2c5f9c', 2.4) + head(104, mY + 50, 150, '#2c5f9c', 10);
  body += T(cII[0] - 4, cII[1] + 6, '', {}) + T(cII[0] - 40, cII[1] + 86, 'Succinate', { fs: 15, w: 800, a: 'end' }) + T(cII[0] + 44, cII[1] + 86, 'Fumarate', { fs: 15, w: 800, a: 'start' });
  body += curve(`M${cII[0] - 44} ${cII[1] + 78} Q ${cII[0]} ${cII[1] + 54} ${cII[0] + 40} ${cII[1] + 78}`, MUTED, 2.4) + head(cII[0] + 42, cII[1] + 80, 35, MUTED, 10);

  const oX = cIV[0] + 62, oY = cIV[1] + 120;
  body += T(oX, oY, '½ O_2 + 2 H^+', { fs: 16, w: 800, a: 'start' }) + head(oX + 52, oY + 32, 90, MUTED, 10) + `<line x1="${oX + 52}" y1="${oY + 8}" x2="${oX + 52}" y2="${oY + 24}" stroke="${MUTED}" stroke-width="2.4"/>`;
  body += `<ellipse cx="${oX + 52}" cy="${oY + 52}" rx="30" ry="16" fill="#e2f1f8" stroke="#1f6f8b" stroke-width="1.8"/>` + T(oX + 52, oY + 58, 'H_2O', { fs: 16, w: 900, c: '#1f6f8b' });
  // H+ pumping at I, III, IV (matrix -> intermembrane space)
  for (const [x, top, bot] of [[cI[0] + 18, cI[1] - 72, cI[1] + 72], [cIII[0] + 14, cIII[1] - 64, cIII[1] + 64], [cIV[0] - 22, cIV[1] - 60, cIV[1] + 60]]) {
    body += hion(x + 4, bot + 34) + curve(`M${x + 2} ${bot + 18} L${x} ${top - 22}`, '#8a4d63', 2.6) + head(x, top - 28, -90, '#8a4d63', 12);
  }
  body += T(470, IMy - 108 + 0, '', {});
  body += T(470, outer ? 132 : 140, 'H^+ is pumped out by complexes I, III and IV', { fs: 14, w: 700, c: '#8a4d63', it: true });
  body += T(20, outer ? 576 : 566, 'Matrix (low H^+)', { a: 'start', fs: 16, c: '#2c5f9c', w: 800 });
  const H = (outer ? 596 : 446);
  o = g(body);
  return `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}" role="img" aria-label="The electron transport chain in the inner mitochondrial membrane. NADH gives electrons to complex I and FADH2 (from succinate turning into fumarate) gives electrons to complex II. A red line traces the electrons through coenzyme Q, complex III, cytochrome c and complex IV to oxygen, which forms water. Complexes I, III and IV pump H+ from the matrix into the intermembrane space; H+ flows back through ATP synthase, which makes ATP from ADP and phosphate."><rect width="100%" height="100%" fill="#ffffff"/>${o}</svg>`;
}
if (require.main === module) {
  const dir = path.join(__dirname, '..', 'figures', 'pathways', 'etc'); fs.mkdirSync(dir, { recursive: true });
  fs.writeFileSync(path.join(dir, 'etc.svg'), build({ outer: true }));
  fs.writeFileSync(path.join(dir, 'etc_game.svg'), build({ outer: false }));
  console.log('ok');
}
module.exports = { build };
