/* Original replacements for CC BY-SA figures (Dr. Dan, CC BY 4.0).
   node tools/oer_figs.js -> figures/pathways/oer/*.svg
   Same visual language as tools/glycolysis.js (plain SVG, no ids/styles/markers). */
const fs = require('fs'), path = require('path');
const G = require('./glycolysis.js'), { label, line, dbl, head, chain, pyranose, shift, svgWrap, textW, firstW, hlRect, esc, r1, CAC_MOL, CAC_STEPS, KEY, sideColor, FONT, INK, BLUE, RED, GREEN, MUTED } = G.H;
const PURPLE = '#5b4790', TITLE = (x, y, s) => label(x, y, s, 19, { weight: 900, color: PURPLE }).svg;
const note = (x, y, s, o = {}) => label(x, y, s, o.fs || 13.5, { color: o.color || MUTED, weight: o.weight || 700, anchor: o.anchor, italic: o.italic }).svg;
const scaled = (m, x, y, s) => `<g transform="translate(${r1(x)} ${r1(y)}) scale(${s})">${m.svg}</g>`;
const rad = d => d * Math.PI / 180;
const out = {};

/* ---------------- 1. Citric acid cycle wheel (14.3) ---------------- */
function cacWheel() {
  const W = 1180, H = 1250, cx = 590, cy = 655, R = 410, Rin = 268, S = 0.7;
  const order = ['oaa', 'cit', 'icit', 'akg', 'scoa', 'suc', 'fum', 'mal'];
  const ang = i => -22.5 + 45 * i;            // 0° = straight up, clockwise
  const pt = (a, r) => [cx + r * Math.sin(rad(a)), cy - r * Math.cos(rad(a))];
  let o = TITLE(20, 30, 'The citric acid cycle (one turn, per acetyl CoA)');
  o += note(20, 54, 'Each arrow is one step; the number matches the step close-ups in this section. Changed groups are highlighted there.');
  // centre label
  o += `<circle cx="${cx}" cy="${cy}" r="84" fill="#f4f1fb" stroke="#c9bfe6" stroke-width="1.6"/>`;
  o += label(cx, cy - 22, 'Citric acid', 17, { anchor: 'middle', weight: 900, color: PURPLE }).svg + label(cx, cy, 'cycle', 17, { anchor: 'middle', weight: 900, color: PURPLE }).svg;
  o += label(cx, cy + 26, 'mitochondrial matrix', 12.5, { anchor: 'middle', color: MUTED, weight: 700, italic: true }).svg;
  // molecules
  order.forEach((id, i) => { const m = CAC_MOL[id].draw([]); const [x, y] = pt(ang(i), R); const w = m.w * S, h = m.h * S;
    o += scaled(m, x - w / 2, y - h / 2 - 8, S) + label(x, y + h / 2 + 4, CAC_MOL[id].name, 15, { anchor: 'middle', weight: 900, color: '#3b4a63' }).svg; });
  // step arcs on the inner circle, clockwise from molecule i to i+1
  const side = { 1: [], 2: [], 3: ['NAD^+', 'NADH'], 4: ['NAD^+', 'NADH'], 5: ['GDP + Ⓟ_i', 'GTP'], 6: ['FAD', 'FADH_2'], 7: [], 8: ['NAD^+', 'NADH'] };
  const extraOut = { 3: 'CO_2', 4: 'CO_2' }, extraIn = { 7: 'H_2O' };
  const enz = { 1: 'citrate synthase', 2: 'aconitase', 3: 'isocitrate dehydrogenase', 4: 'α-ketoglutarate dehydrogenase', 5: 'succinyl CoA synthetase', 6: 'succinate dehydrogenase', 7: 'fumarase', 8: 'malate dehydrogenase' };
  for (let k = 1; k <= 8; k++) {
    const a0 = ang(k - 1) + 7, a1 = ang(k) - 7, am = (a0 + a1) / 2;
    const [x0, y0] = pt(a0, Rin), [x1, y1] = pt(a1, Rin);
    o += `<path d="M${r1(x0)} ${r1(y0)} A ${Rin} ${Rin} 0 0 1 ${r1(x1)} ${r1(y1)}" fill="none" stroke="${INK}" stroke-width="3.4"/>`;
    o += head(x1, y1, a1, INK, 15);
    const na = k === 1 ? am + 9 : am; const [nx, ny] = pt(na, Rin + 26); o += `<circle cx="${r1(nx)}" cy="${r1(ny)}" r="12" fill="#eef2f8" stroke="#9fb0c8" stroke-width="1.4"/>` + label(nx, ny, String(k), 13, { anchor: 'middle', color: MUTED, weight: 900 }).svg;
    if (k !== 1) { const [ex, ey] = pt(am, R + 18); const words = enz[k].split(' ');
      const lines = words.length > 1 && textW(enz[k], 12.5) > 120 ? [words.slice(0, -1).join(' '), words[words.length - 1]] : [enz[k]];
      lines.forEach((t, j) => o += label(ex, ey + (j - (lines.length - 1) / 2) * 15, t, 12.5, { anchor: 'middle', color: MUTED, weight: 700, italic: true }).svg); }
    if (side[k].length) { const d = 10, rr = Rin - 70; const [px, py] = pt(am - d, rr), [qx, qy] = pt(am + d, rr);
      const [c1x, c1y] = pt(am - 7, Rin - 2), [c2x, c2y] = pt(am + 7, Rin - 2);
      o += `<path d="M${r1(px)} ${r1(py)} C ${r1(c1x)} ${r1(c1y)}, ${r1(c2x)} ${r1(c2y)}, ${r1(qx)} ${r1(qy)}" fill="none" stroke="${MUTED}" stroke-width="2.2"/>`;
      o += head(qx, qy, Math.atan2(qy - c2y, qx - c2x) * 180 / Math.PI, MUTED, 9);
      const [lx, ly] = pt(am - d - 1, rr - 26), [ox2, oy2] = pt(am + d + 1, rr - 26);
      o += label(lx, ly, side[k][0], 14.5, { anchor: 'middle', color: sideColor(side[k][0]), weight: 800 }).svg + label(ox2, oy2, side[k][1], 14.5, { anchor: 'middle', color: sideColor(side[k][1]), weight: 800 }).svg; }
    if (extraOut[k]) { const [px, py] = pt(am + 2, Rin + 4), [qx, qy] = pt(am + 4, Rin + 42); o += line(px, py, qx, qy, 2.2, MUTED) + head(qx, qy, Math.atan2(qy - py, qx - px) * 180 / Math.PI, MUTED, 9);
      const [lx, ly] = pt(am + 6, Rin + 60); o += label(lx, ly, extraOut[k], 14.5, { anchor: 'middle', color: sideColor('CO_2'), weight: 800 }).svg; }
    if (extraIn[k]) { const [px, py] = pt(am, Rin - 64), [qx, qy] = pt(am, Rin - 6); o += line(px, py, qx, qy, 2.2, MUTED) + head(qx, qy, Math.atan2(qy - py, qx - px) * 180 / Math.PI, MUTED, 9);
      const [lx, ly] = pt(am, Rin - 82); o += label(lx, ly, extraIn[k], 14.5, { anchor: 'middle', color: sideColor('H_2O'), weight: 800 }).svg; }
  }
  // acetyl CoA (+ H2O) entering step 1 from above; CoA-SH leaving toward the centre
  const ac = chain([{ c: 'C', top: 'O', r: 'S–CoA' }, { lab: 'CH_3' }]); const [tx, ty] = pt(0, Rin);
  o += scaled(ac, cx - 52, 74, 0.72) + label(cx + 104, 118, 'Acetyl CoA (2 C)', 15, { weight: 900, color: '#3b4a63' }).svg;
  o += line(cx, 196, cx, ty - 6, 2.4, MUTED) + head(cx, ty - 2, 90, MUTED, 10);
  o += label(cx + 12, 300, '+ H_2O', 14, { color: sideColor('H_2O'), weight: 800 }).svg;
  o += label(cx - 14, 292, 'citrate', 12.5, { anchor: 'end', color: MUTED, weight: 700, italic: true }).svg + label(cx - 14, 307, 'synthase', 12.5, { anchor: 'end', color: MUTED, weight: 700, italic: true }).svg;
  const [sx0, sy0] = pt(5, Rin - 2), [sx1, sy1] = pt(22, Rin - 70);
  o += `<path d="M${r1(sx0)} ${r1(sy0)} Q ${r1(sx0 + 6)} ${r1(sy1 - 4)} ${r1(sx1)} ${r1(sy1)}" fill="none" stroke="${MUTED}" stroke-width="2.2"/>` + head(sx1 + 2, sy1 + 1, 20, MUTED, 9) + label(sx1 + 6, sy1 + 16, 'CoA–SH', 14.5, { color: sideColor('CoA'), weight: 800 }).svg;
  // totals box
  const bx = 20, by = H - 118; o += `<rect x="${bx}" y="${by}" width="${W - 40}" height="96" rx="12" fill="#f7f9fc" stroke="#d6dde8"/>`;
  o += label(bx + 18, by + 24, 'Per turn (one acetyl CoA):', 15, { weight: 900, color: PURPLE }).svg;
  o += label(bx + 18, by + 52, '2 CO_2  +  3 NADH  +  1 FADH_2  +  1 GTP (≈ ATP)', 16, { weight: 800 }).svg;
  o += label(bx + 18, by + 78, 'Per glucose the cycle turns twice (2 acetyl CoA), so double every number.', 13.5, { color: MUTED, weight: 700 }).svg;
  o += KEY(W - 300, by + 24);
  return svgWrap(W, H, o, 'The citric acid cycle as a wheel of structures. Step 1, citrate synthase: acetyl CoA (2 carbons) and water join oxaloacetate to make citrate, releasing CoA-SH. Step 2, aconitase: citrate is rearranged to isocitrate. Step 3, isocitrate dehydrogenase: NAD+ is reduced to NADH and CO2 leaves, giving alpha-ketoglutarate. Step 4, alpha-ketoglutarate dehydrogenase: NAD+ is reduced to NADH and CO2 leaves, giving succinyl CoA. Step 5, succinyl CoA synthetase: GDP and phosphate make GTP, giving succinate. Step 6, succinate dehydrogenase: FAD is reduced to FADH2, giving fumarate. Step 7, fumarase: water adds, giving malate. Step 8, malate dehydrogenase: NAD+ is reduced to NADH, regenerating oxaloacetate. Per turn: 2 CO2, 3 NADH, 1 FADH2 and 1 GTP.');
}

/* ---------------- 2. Glucose open chain <=> ring (5.3) ---------------- */
function eqArrow(x0, x1, y) { // two half-arrows (equilibrium)
  return line(x0, y - 6, x1 - 2, y - 6, 2.8) + `<path d="M${r1(x1)} ${r1(y - 6)}L${r1(x1 - 14)} ${r1(y - 13)}L${r1(x1 - 14)} ${r1(y - 6)}z" fill="${INK}"/>` +
    line(x0 + 2, y + 6, x1, y + 6, 2.8) + `<path d="M${r1(x0)} ${r1(y + 6)}L${r1(x0 + 14)} ${r1(y + 13)}L${r1(x0 + 14)} ${r1(y + 6)}z" fill="${INK}"/>`;
}
function glucoseRing() {
  const m1 = chain([{ c: 'C', top: 'O', r: 'H', hl: ['top', 'r'] }, { c: 'C', l: 'H', r: 'OH' }, { c: 'C', l: 'HO', r: 'H' }, { c: 'C', l: 'H', r: 'OH' }, { c: 'C', l: 'H', r: 'OH', hl: ['r'] }, { lab: 'CH_2OH' }]);
  const a = pyranose({ c1: 'OH', hl: ['c1'] });
  let o = TITLE(18, 30, 'Glucose: open-chain aldehyde ⇌ cyclic hemiacetal');
  const y0 = 62, gx = 50; o += shift(m1, gx, y0);
  const nums = ['1', '2', '3', '4', '5', '6']; nums.forEach((n, i) => o += label(gx + 70 + 13, y0 + 44 + i * 46 - 13, n, 11, { color: '#8a94a6', weight: 800 }).svg);
  const midY = y0 + m1.h / 2; o += eqArrow(285, 405, midY);
  o += note(345, midY - 30, 'the C-5 –OH adds', { anchor: 'middle' }) + note(345, midY + 34, 'to the C-1 C=O', { anchor: 'middle' });
  const ax = 440, ay = midY - a.h / 2 - 6; o += shift(a, ax, ay);
  o += label(ax + 85, ay - 8, 'C-1 is now a hemiacetal carbon', 13, { anchor: 'middle', color: '#8a4a0e', weight: 800 }).svg;
  o += label(gx + 75, y0 + m1.h + 26, 'Open-chain D-glucose (aldehyde)', 14.5, { anchor: 'middle', weight: 900, color: '#3b4a63' }).svg;
  o += label(ax + 85, ay + a.h + 14, 'α-D-Glucose (six-membered ring)', 14.5, { anchor: 'middle', weight: 900, color: '#3b4a63' }).svg;
  const H = y0 + m1.h + 110, W = 720;
  o += note(18, H - 48, 'In water, over 99% of glucose is in the ring form. The new –OH on C-1 can point down (α, shown)');
  o += note(18, H - 30, 'or up (β). Highlighted: the aldehyde group and the C-5 –OH that react to close the ring.');
  return svgWrap(W, H, o, 'Glucose interconverts between an open-chain aldehyde form, a six-carbon Fischer-style chain with CHO at carbon 1 and OH groups on carbons 2 to 6, and a six-membered cyclic hemiacetal. The OH on carbon 5 adds to the C=O of carbon 1, closing a ring that contains an oxygen; carbon 1 becomes a hemiacetal carbon bearing an OH, drawn here pointing down (alpha). In water over 99 percent of glucose is in the ring form.');
}

/* ---------------- 3. Partial hydrogenation of an oil (5.4) ---------------- */
/* skeletal fatty-acid chain: n carbons after the carbonyl carbon; db = list of {pos, cis} (bond between C pos and pos+1, C1 = carbonyl) */
function fattyChain(x, y, n, dbs, hlDb = []) {
  // n carbons drawn after the carbonyl C (C1); bond k joins C(k+1)–C(k+2). cis C=C at positions in dbs bends the chain by 60°.
  const L = 21; let pts = [[x, y]], D = 0, kinkSign = -1, o = "";
  for (let k = 0; k < n - 1; k++) { const pos = k + 2; const hd = D + (k % 2 === 0 ? -30 : 30); const [px, py] = pts[k];
    pts.push([px + L * Math.cos(rad(hd)), py + L * Math.sin(rad(hd))]);
    if (dbs.includes(pos)) { D += 22 * kinkSign; kinkSign = -kinkSign; } }
  for (let k = 0; k < n - 1; k++) { const pos = k + 2, isDb = dbs.includes(pos); const [x1, y1] = pts[k], [x2, y2] = pts[k + 1];
    if (isDb && hlDb.includes(pos)) o += `<circle cx="${r1((x1 + x2) / 2)}" cy="${r1((y1 + y2) / 2)}" r="15" fill="#fff0a8" stroke="#e8c547" stroke-width="1.2"/>`;
    o += line(x1, y1, x2, y2, 2.2);
    if (isDb) { // second line on the side toward the neighbours (inside of the kink)
      const nb = pts[k + 2] || pts[k - 1]; const dx = x2 - x1, dy = y2 - y1, Ln = Math.hypot(dx, dy); let nx = -dy / Ln * 5, ny = dx / Ln * 5;
      const mx = (x1 + x2) / 2, my = (y1 + y2) / 2; if ((nb[0] - mx) * nx + (nb[1] - my) * ny < 0) { nx = -nx; ny = -ny; }
      o += line(x1 + dx * .18 + nx, y1 + dy * .18 + ny, x2 - dx * .18 + nx, y2 - dy * .18 + ny, 2.2); } }
  const end = pts.reduce((m, p) => p[0] > m[0] ? p : m, pts[0]);
  return { svg: o, end: [end[0], y] };
}
function triglyceride(x, y, chains, title, hl = [[], [], []]) {
  let o = ''; const rows = [0, 84, 168];
  o += label(x, y + rows[0], 'CH_2', 16).svg + label(x + 4, y + rows[1], 'CH', 16).svg + label(x, y + rows[2], 'CH_2', 16).svg;
  o += line(x + 14, y + 13, x + 14, y + rows[1] - 13) + line(x + 14, y + rows[1] + 13, x + 14, y + rows[2] - 13);
  rows.forEach((ry, i) => { const yy = y + ry; o += line(x + 40, yy, x + 56, yy) + label(x + 60, yy, 'O', 16, { color: RED }).svg + line(x + 74, yy, x + 90, yy);
    o += label(x + 94, yy, 'C', 16).svg + dbl(x + 99, yy - 11, x + 99, yy - 28, 3) + label(x + 99, yy - 36, 'O', 15, { anchor: 'middle', color: RED }).svg;
    const ch = chains[i]; const f = fattyChain(x + 112, yy, 17, ch.db, hl[i] || []); o += f.svg;
    o += label(f.end[0] + 14, yy, ch.name, 13.5, { weight: 800, color: ch.color || '#3b4a63' }).svg; });
  o += label(x - 6, y - 96, title, 15, { weight: 900, color: '#3b4a63' }).svg;
  return o;
}
function hydrogenation() {
  const W = 760; let o = TITLE(18, 30, 'Partial hydrogenation of a vegetable oil');
  const LIN = { name: 'linoleate (2 C=C)', db: [9, 12], color: '#2c5f9c' }, OLE = { name: 'oleate (1 C=C)', db: [9], color: '#23704f' }, STE = { name: 'stearate (0 C=C)', db: [], color: '#9c3346' };
  o += triglyceride(30, 170, [LIN, LIN, OLE], 'Vegetable oil (liquid): a triglyceride with unsaturated chains', [[12], [12], [9]]);
  const ay = 410; o += line(240, ay, 240, ay + 70, 3.4) + head(240, ay + 76, 90, INK, 14);
  o += label(256, ay + 22, '+ 3 H_2', 16, { weight: 800, color: '#1f6f8b' }).svg + label(256, ay + 46, 'Ni catalyst, heat', 14, { color: MUTED, weight: 700, italic: true }).svg;
  o += label(256, ay + 68, 'H_2 adds across some C=C bonds', 13.5, { color: MUTED, weight: 700 }).svg;
  o += triglyceride(30, 640, [OLE, OLE, STE], 'Partially hydrogenated oil (soft solid, e.g. margarine)');
  const H = 900; o += note(18, H - 58, 'Fewer C=C double bonds = straighter chains that pack together, so the fat is more solid.');
  o += note(18, H - 40, 'The highlighted C=C bonds are the ones that react. Partial hydrogenation can also flip some');
  o += note(18, H - 22, 'cis C=C bonds to trans, which is where trans fats come from.');
  return svgWrap(W, H, o, 'Partial hydrogenation of a vegetable oil. Top: a liquid triglyceride, a glycerol backbone with three ester-linked 18-carbon chains: two linoleate chains with two C=C double bonds each and one oleate chain with one C=C. Adding 3 H2 with a nickel catalyst and heat saturates some of the double bonds. Bottom: a partially hydrogenated, soft solid fat with two oleate chains and one fully saturated stearate chain. Fewer double bonds make straighter chains that pack together; partial hydrogenation can also convert some cis double bonds to trans.');
}

/* ---------------- 4. Sphingolipid general structure (9.4) ---------------- */
function sphingolipids() {
  const W = 920; let o = TITLE(18, 30, 'Sphingolipids: one backbone, different head groups');
  o += note(18, 54, 'Every sphingolipid is built on sphingosine. Change the two highlighted parts (R and X) to get each class.');
  const x0 = 60, y0 = 110, gap = 56; // vertical three-carbon backbone
  const bx = x0 + 140;
  { const pre = textW('X–O–', 17), sx = bx - 4 - pre - firstW('CH_2', 17) / 2; o += hlRect(sx - 6, y0 - 15, firstW('X', 17) + 12, 30) + label(sx, y0, 'X–O–CH_2', 17).svg; }
  const c2y = y0 + gap, c3y = y0 + 2 * gap;
  o += line(bx - 4, y0 + 12, bx - 4, c2y - 12) + line(bx - 4, c2y + 12, bx - 4, c3y - 12);
  o += label(bx - 4, c2y, 'C', 17, { anchor: 'middle' }).svg + line(bx - 14, c2y, bx - 30, c2y) + label(bx - 34, c2y, 'H', 16, { anchor: 'end' }).svg;
  o += line(bx + 6, c2y, bx + 24, c2y) + label(bx + 28, c2y, 'NH', 16).svg + line(bx + 56, c2y, bx + 72, c2y) + label(bx + 76, c2y, 'C', 16).svg + dbl(bx + 81, c2y - 11, bx + 81, c2y - 28, 3) + label(bx + 81, c2y - 36, 'O', 15, { anchor: 'middle', color: RED }).svg;
  o += hlRect(bx + 92, c2y - 16, 236, 32) + line(bx + 90, c2y, bx + 104, c2y) + label(bx + 108, c2y, 'R  (fatty acid chain)', 16, { weight: 800, color: RED }).svg;
  o += label(bx - 4, c3y, 'C', 17, { anchor: 'middle' }).svg + line(bx - 14, c3y, bx - 30, c3y) + label(bx - 34, c3y, 'H', 16, { anchor: 'end' }).svg + line(bx + 6, c3y, bx + 24, c3y) + label(bx + 28, c3y, 'OH', 16).svg;
  // trans alkene tail drawn as condensed text going down
  const ty = c3y + gap; o += line(bx - 4, c3y + 12, bx - 4, ty - 12) + label(bx - 4, ty, 'CH', 16, { anchor: 'middle' }).svg + dbl(bx - 4, ty + 12, bx - 4, ty + 34, 3) + label(bx - 4, ty + 46, 'CH', 16, { anchor: 'middle' }).svg;
  o += line(bx - 4, ty + 58, bx - 4, ty + 76) + label(bx - 4, ty + 90, '(CH_2)_12', 16, { anchor: 'middle' }).svg + line(bx - 4, ty + 102, bx - 4, ty + 118) + label(bx - 4, ty + 132, 'CH_3', 16, { anchor: 'middle' }).svg;
  o += note(bx + 30, ty + 23, 'trans C=C', { italic: true });
  o += `<path d="M${bx - 60} ${c2y - 30} Q ${bx - 90} ${c2y + 60} ${bx - 60} ${ty + 140}" fill="none" stroke="#c9bfe6" stroke-width="2"/>`;
  o += label(bx - 96, c2y + 120, 'sphingosine', 14, { anchor: 'end', weight: 800, color: PURPLE, italic: true }).svg;
  o += label(bx - 96, c2y + 138, 'backbone', 14, { anchor: 'end', weight: 800, color: PURPLE, italic: true }).svg;
  // table of classes
  const tx = 470, tyy = 230; const rows = [
    ['Class', 'R (on N)', 'X (on O)'],
    ['Sphingosine', 'none (free –NH_2)', 'H'],
    ['Ceramide', 'fatty acid', 'H'],
    ['Sphingomyelin', 'fatty acid', 'phosphocholine'],
    ['Cerebroside', 'fatty acid', 'one sugar'],
    ['Ganglioside', 'fatty acid', 'chain of sugars']];
  const cw = [128, 132, 124], rh = 34;
  rows.forEach((r, i) => { let cx2 = tx; const yy2 = tyy + i * rh; if (i === 0) o += `<rect x="${tx - 8}" y="${yy2 - 20}" width="${cw.reduce((a, b) => a + b) + 8}" height="${rh}" rx="6" fill="#efeaf9"/>`;
    else if (i % 2 === 0) o += `<rect x="${tx - 8}" y="${yy2 - 20}" width="${cw.reduce((a, b) => a + b) + 8}" height="${rh}" fill="#f7f9fc"/>`;
    r.forEach((c, j) => { o += label(cx2, yy2 - 2, c, i === 0 ? 14 : 13.5, { weight: i === 0 || j === 0 ? 900 : 700, color: i === 0 ? PURPLE : j === 1 ? RED : j === 2 ? BLUE : '#3b4a63' }).svg; cx2 += cw[j]; }); });
  o += note(tx - 8, tyy + rows.length * rh + 8, 'Sphingomyelin is a phospholipid; cerebrosides and gangliosides');
  o += note(tx - 8, tyy + rows.length * rh + 26, 'are glycolipids. All have two nonpolar tails and a polar head.');
  const H = 520; return svgWrap(W, H, o, 'General structure of sphingolipids. A sphingosine backbone: carbon 1 carries CH2-O-X, carbon 2 carries an amide N-H bonded to C=O and a fatty acid chain R, carbon 3 carries an OH, followed by a trans CH=CH double bond and a long (CH2)12-CH3 tail. A table lists the classes: sphingosine has a free NH2 and X = H; ceramide has a fatty acid R and X = H; sphingomyelin has a fatty acid and X = phosphocholine; a cerebroside has a fatty acid and one sugar as X; a ganglioside has a fatty acid and a chain of sugars as X.');
}

/* ---------------- 5. Myelin and multiple sclerosis (9.4) ---------------- */
function myelin() {
  const W = 860, H = 430; let o = TITLE(18, 30, 'Myelin and multiple sclerosis');
  const panel = (px, title, damaged) => { let s = label(px + 190, 70, title, 16, { anchor: 'middle', weight: 900, color: damaged ? RED : GREEN }).svg;
    const y = 200; // neuron cell body + axon
    s += `<circle cx="${px + 40}" cy="${y}" r="34" fill="#fde3cf" stroke="#c98b5e" stroke-width="2"/>`;
    for (let k = 0; k < 6; k++) { const a = rad(150 + k * 12 - 30 * (k % 2)); s += line(px + 40 + 30 * Math.cos(a + 1.6), y + 30 * Math.sin(a + 1.6), px + 40 + 58 * Math.cos(a + 1.6), y + 58 * Math.sin(a + 1.6), 3, '#c98b5e'); }
    s += `<rect x="${px + 72}" y="${y - 6}" width="290" height="12" rx="6" fill="#fde3cf" stroke="#c98b5e" stroke-width="1.6"/>`;
    for (let k = 0; k < 5; k++) { const sx = px + 86 + k * 56; const broken = damaged && (k === 1 || k === 3);
      if (!broken) s += `<rect x="${sx}" y="${y - 18}" width="44" height="36" rx="16" fill="#f4f1fb" stroke="${PURPLE}" stroke-width="2"/>`;
      else s += `<path d="M${sx} ${y - 14} q 10 -8 18 0 M${sx + 26} ${y + 12} q 8 8 16 0" fill="none" stroke="${PURPLE}" stroke-width="2" stroke-dasharray="4 4"/>`; }
    if (!damaged) s += note(px + 60, y + 50, 'myelin sheath (wrapped around the axon)', { fs: 13 });
    s += line(px + 362, y, px + 378, y, 3, '#c98b5e') + head(px + 384, y, 0, '#c98b5e', 10);
    // signal arrow
    if (!damaged) s += `<path d="M${px + 86} ${y - 40} H ${px + 340}" stroke="${GREEN}" stroke-width="3" fill="none"/>` + head(px + 348, y - 40, 0, GREEN, 12) + label(px + 216, y - 54, 'fast signal (jumps gap to gap)', 13, { anchor: 'middle', color: GREEN, weight: 800 }).svg;
    else { s += `<path d="M${px + 86} ${y - 40} H ${px + 200}" stroke="${RED}" stroke-width="3" stroke-dasharray="6 6" fill="none"/>` + head(px + 208, y - 40, 0, RED, 12) + label(px + 216, y - 54, 'slow or blocked signal', 13, { anchor: 'middle', color: RED, weight: 800 }).svg;
      [[px + 164, y + 92], [px + 276, y + 100]].forEach(([ix, iy]) => { s += `<circle cx="${ix}" cy="${iy}" r="18" fill="#dff1f7" stroke="#1f6f8b" stroke-width="2"/>` + `<circle cx="${ix - 4}" cy="${iy - 3}" r="6" fill="#1f6f8b"/>` + line(ix, iy - 18, ix, y + 26, 2.2, '#1f6f8b') + head(ix, y + 18, -90, '#1f6f8b', 11); });
      s += note(px + 210, y + 140, 'immune cells attack and strip away the myelin', { fs: 13, anchor: 'middle', color: '#1f6f8b' }); }
    return s; };
  o += panel(20, 'Healthy nerve fiber', false) + panel(440, 'Multiple sclerosis', true);
  o += line(430, 60, 430, 380, 1.2, '#d6dde8');
  o += note(18, H - 34, 'Myelin is rich in sphingomyelin and other sphingolipids. In multiple sclerosis the immune system damages myelin in the brain and');
  o += note(18, H - 16, 'spinal cord, so nerve signals slow down or stop.');
  return svgWrap(W, H, o, 'Two panels. Healthy nerve fiber: a neuron cell body and an axon wrapped in evenly spaced segments of myelin sheath; the signal travels fast, jumping from gap to gap. Multiple sclerosis: the same axon with some myelin segments missing, immune cells attacking the myelin, and a slow or blocked signal. Myelin is rich in sphingomyelin and other sphingolipids.');
}

/* ---------------- 6. Collagen triple helix (10.7) ---------------- */
function collagen() {
  const W = 860, H = 350; let o = TITLE(18, 30, 'Collagen: a triple helix of three protein chains');
  const cols = ['#9c3346', '#2c5f9c', '#23704f'], x0 = 40, x1 = 560, yc = 160, A = 34, per = 150;
  const segs = []; const N = 260;
  for (let c = 0; c < 3; c++) for (let i = 0; i < N; i++) { const t0 = i / N, t1 = (i + 1) / N; const ph = c * 2 * Math.PI / 3;
    const xa = x0 + (x1 - x0) * t0, xb = x0 + (x1 - x0) * t1; const th0 = (xa - x0) / per * 2 * Math.PI + ph, th1 = (xb - x0) / per * 2 * Math.PI + ph;
    segs.push({ c, z: Math.cos((th0 + th1) / 2), d: `M${r1(xa)} ${r1(yc + A * Math.sin(th0))} L${r1(xb)} ${r1(yc + A * Math.sin(th1))}` }); }
  segs.sort((a, b) => a.z - b.z).forEach(s => { const shade = 0.55 + 0.45 * (s.z + 1) / 2; o += `<path d="${s.d}" stroke="${cols[s.c]}" stroke-opacity="${shade.toFixed(2)}" stroke-width="${(9 + 4 * s.z).toFixed(1)}" stroke-linecap="round" fill="none"/>`; });
  o += note(x0, yc + 70, 'Three left-handed chains wind around each other into a right-handed "rope."');
  // repeat unit box
  const bx = 600, by = 80; o += `<rect x="${bx}" y="${by}" width="240" height="190" rx="12" fill="#f7f9fc" stroke="#d6dde8"/>`;
  o += label(bx + 16, by + 26, 'Repeating unit', 15, { weight: 900, color: PURPLE }).svg;
  o += label(bx + 16, by + 60, 'Gly – X – Y', 22, { weight: 900 }).svg;
  o += note(bx + 16, by + 92, 'X is often proline (Pro)'); o += note(bx + 16, by + 112, 'Y is often hydroxyproline (Hyp)');
  o += note(bx + 16, by + 140, 'Every third residue is glycine, the');
  o += note(bx + 16, by + 158, 'smallest amino acid, so it fits in');
  o += note(bx + 16, by + 176, 'the crowded center of the helix.');
  o += note(18, H - 36, 'Hydrogen bonds between the chains hold the triple helix together. Making hydroxyproline needs vitamin C;');
  o += note(18, H - 18, 'without it, collagen is weak (scurvy).');
  return svgWrap(W, H, o, 'Collagen triple helix: three protein chains, drawn in red, blue and green, wind around each other into a rope-like right-handed triple helix. A box explains the repeating unit Gly-X-Y, where X is often proline and Y is often hydroxyproline; every third residue is glycine, small enough to fit in the crowded center. Hydrogen bonds between chains hold the helix together, and making hydroxyproline requires vitamin C.');
}

/* ---------------- 7. ATP synthase (14.4) ---------------- */
const Hion = (x, y, r = 13) => `<circle cx="${r1(x)}" cy="${r1(y)}" r="${r}" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.8"/>` + `<text x="${r1(x - 6.5)}" y="${r1(y + 5)}" font-family="${FONT}" font-size="13" font-weight="900" fill="#1d1d1f">H<tspan font-size="9" dy="-5">+</tspan></text>`;
function atpSynthase() {
  const W = 860, H = 640; let o = TITLE(18, 30, 'ATP synthase: a rotary motor driven by H⁺ flow');
  const my0 = 150, my1 = 230; // membrane band
  o += `<rect x="0" y="54" width="${W}" height="${my0 - 54}" fill="#fdecef"/>` + note(16, 76, 'Intermembrane space (high [H⁺])', { color: RED, weight: 800 });
  o += `<rect x="0" y="${my1}" width="${W}" height="${H - my1 - 60}" fill="#e9f2fb"/>` + note(16, H - 76, 'Mitochondrial matrix (low [H⁺])', { color: BLUE, weight: 800 });
  // lipid bilayer
  for (let x = 6; x < W; x += 16) { o += `<circle cx="${x}" cy="${my0 + 8}" r="6" fill="#f3d9a6" stroke="#c9a15a"/>` + `<circle cx="${x}" cy="${my1 - 8}" r="6" fill="#f3d9a6" stroke="#c9a15a"/>` + line(x - 2, my0 + 14, x - 2, (my0 + my1) / 2 - 3, 1.2, '#c9a15a') + line(x + 2, my0 + 14, x + 2, (my0 + my1) / 2 - 3, 1.2, '#c9a15a') + line(x - 2, my1 - 14, x - 2, (my0 + my1) / 2 + 3, 1.2, '#c9a15a') + line(x + 2, my1 - 14, x + 2, (my0 + my1) / 2 + 3, 1.2, '#c9a15a'); }
  o += note(W - 190, my0 - 10, 'inner membrane', { italic: true });
  const cx = 360, ringY = (my0 + my1) / 2;
  // Fo c-ring (rotor) as a row of c subunits
  o += `<rect x="${cx - 120}" y="${my0 - 6}" width="240" height="${my1 - my0 + 12}" rx="26" fill="#d9cdf2" stroke="${PURPLE}" stroke-width="2.2"/>`;
  for (let k = 0; k < 8; k++) o += `<rect x="${cx - 112 + k * 28}" y="${my0}" width="24" height="${my1 - my0}" rx="10" fill="#ece6fa" stroke="${PURPLE}" stroke-width="1.4"/>`;
  o += label(cx - 24, my1 + 22, 'F_o rotor (ring of c subunits)', 13.5, { anchor: 'end', weight: 800, color: PURPLE }).svg;
  // a subunit (stator) at right of ring
  o += `<rect x="${cx + 124}" y="${my0 - 14}" width="54" height="${my1 - my0 + 28}" rx="14" fill="#cfe8dc" stroke="${GREEN}" stroke-width="2.2"/>` + label(cx + 151, ringY, 'a', 18, { anchor: 'middle', weight: 900, color: GREEN }).svg;
  // b stalk (peripheral stator) from a down to F1 head
  const fy = 430; o += `<rect x="${cx + 160}" y="${my1 + 10}" width="16" height="${fy - my1 - 40}" rx="7" fill="#cfe8dc" stroke="${GREEN}" stroke-width="2"/>`;
  o += `<path d="M${cx + 168} ${fy - 30} Q ${cx + 168} ${fy - 6} ${cx + 120} ${fy - 4}" stroke="${GREEN}" stroke-width="10" fill="none" stroke-linecap="round"/>`;
  o += label(cx + 186, my1 + 70, 'b stalk', 13.5, { weight: 800, color: GREEN }).svg + label(cx + 186, my1 + 88, '(holds F_1 still)', 12.5, { color: MUTED, weight: 700 }).svg;
  // gamma central stalk (rotates with ring)
  o += `<rect x="${cx - 9}" y="${my1 + 6}" width="18" height="${fy - my1 + 30}" rx="8" fill="#d9cdf2" stroke="${PURPLE}" stroke-width="2"/>`;
  o += label(cx - 22, my1 + 62, 'γ stalk', 13.5, { anchor: 'end', weight: 800, color: PURPLE }).svg + label(cx - 22, my1 + 80, '(turns with rotor)', 12.5, { anchor: 'end', color: MUTED, weight: 700 }).svg;
  // F1 head: alternating alpha/beta lobes
  const hy = fy + 40; const lobes = [-90, -54, -18, 18, 54, 90];
  lobes.forEach((dx, i) => o += `<ellipse cx="${cx + dx}" cy="${hy}" rx="26" ry="44" fill="${i % 2 ? '#fbe3c4' : '#f7d2a0'}" stroke="#c07a2c" stroke-width="2"/>`);
  o += label(cx, hy + 64, 'F_1 head (3 α + 3 β subunits)', 13.5, { anchor: 'middle', weight: 800, color: '#8a4a0e' }).svg;
  // rotation arrow around rotor
  o += `<path d="M${cx - 150} ${ringY + 26} C ${cx - 186} ${ringY + 6}, ${cx - 186} ${ringY - 30}, ${cx - 150} ${ringY - 46}" fill="none" stroke="${PURPLE}" stroke-width="3"/>` + head(cx - 146, ringY - 48, -30, PURPLE, 12) + label(cx - 190, ringY - 6, 'rotates', 13.5, { anchor: 'end', weight: 800, color: PURPLE }).svg;
  // H+ path: down through a/c interface
  o += Hion(cx + 118, 104) + Hion(cx + 150, 92) + Hion(cx + 186, 110) + Hion(cx + 80, 88) + Hion(cx + 240, 96);
  o += `<path d="M${cx + 120} ${120} C ${cx + 120} ${150}, ${cx + 122} ${200}, ${cx + 118} ${my1 + 46}" fill="none" stroke="#1d1d1f" stroke-width="2.6" stroke-dasharray="7 5"/>` + head(cx + 118, my1 + 52, 92, '#1d1d1f', 11);
  o += Hion(cx + 116, my1 + 74);
  o += label(cx + 250, my1 + 140, 'H⁺ flows down its gradient', 13.5, { weight: 800 }).svg + label(cx + 250, my1 + 158, 'through F_o, turning the rotor', 13.5, { weight: 800 }).svg;
  // ATP synthesis at head
  o += label(cx - 230, hy - 10, 'ADP + Ⓟ_i', 16, { weight: 800, color: '#8a5a00' }).svg;
  o += `<path d="M${cx - 150} ${hy - 6} C ${cx - 120} ${hy - 4}, ${cx - 120} ${hy + 24}, ${cx - 150} ${hy + 28}" fill="none" stroke="${MUTED}" stroke-width="2.4"/>` + head(cx - 154, hy + 28, 178, MUTED, 10);
  o += label(cx - 230, hy + 32, 'ATP + H_2O', 16, { weight: 800, color: '#8a5a00' }).svg;
  o += note(cx + 130, hy + 4, 'the turning γ stalk changes the shape of', { fs: 12.5 }) + note(cx + 130, hy + 20, 'each β subunit in turn: bind ADP + Ⓟ_i,', { fs: 12.5 }) + note(cx + 130, hy + 36, 'make ATP, release ATP', { fs: 12.5 });
  o += note(16, H - 34, 'About 10 H⁺ pass through for one full turn of the rotor, and one turn makes 3 ATP (about 3 H⁺ per ATP, plus 1 to bring');
  o += note(16, H - 16, 'phosphate into the matrix). Ⓟ_i = inorganic phosphate.');
  return svgWrap(W, H, o, 'ATP synthase in the inner mitochondrial membrane. H+ ions in the intermembrane space, where their concentration is high, flow through the Fo part, between the a subunit (stator) and the ring of c subunits (rotor), into the matrix, where H+ concentration is low. The flow turns the rotor and the attached gamma stalk. A b stalk holds the F1 head still. The turning gamma stalk changes the shape of each beta subunit of the F1 head in turn, so ADP and inorganic phosphate bind, are joined into ATP, and ATP is released. About 10 H+ per turn make 3 ATP.');
}
function atpRotation() {
  const W = 930, H = 340; let o = TITLE(18, 30, 'How H⁺ flow turns the F_o rotor (view from above)');
  const pan = (px, n, title, step, loaded) => { let s = label(px + 135, 66, title, 13.5, { anchor: 'middle', weight: 900, color: '#3b4a63' }).svg;
    const cx = px + 135, cy = 180, R = 74, nsub = 10;
    s += `<circle cx="${cx}" cy="${cy}" r="${R + 22}" fill="#f4f1fb" stroke="#c9bfe6" stroke-width="1.4"/>`;
    // stator a on right
    s += `<rect x="${cx + R + 6}" y="${cy - 30}" width="34" height="60" rx="10" fill="#cfe8dc" stroke="${GREEN}" stroke-width="2"/>` + label(cx + R + 23, cy, 'a', 16, { anchor: 'middle', weight: 900, color: GREEN }).svg;
    for (let k = 0; k < nsub; k++) { const a = rad(k * 36 + step * 36); const x = cx + R * Math.cos(a), y = cy + R * Math.sin(a);
      const loaded = (step === 0 && k === 0) || (step === 1 && (k === 0 || k === 9)) || (step === 2 && k >= 1 && k <= 8 ? false : false);
      s += `<circle cx="${r1(x)}" cy="${r1(y)}" r="17" fill="#ece6fa" stroke="${PURPLE}" stroke-width="1.6"/>`;
      if (k === 0) { if (loaded) s += `<circle cx="${r1(x)}" cy="${r1(y)}" r="11" fill="#ffffff" stroke="#1d1d1f" stroke-width="1.4"/>` + `<text x="${r1(x - 5.5)}" y="${r1(y + 4)}" font-family="${FONT}" font-size="10" font-weight="900" fill="#1d1d1f">H<tspan font-size="7" dy="-4">+</tspan></text>`; else s += label(x, y + 1, 'c', 12, { anchor: 'middle', color: PURPLE, weight: 900 }).svg; } }
    s += `<circle cx="${cx}" cy="${cy}" r="14" fill="#d9cdf2" stroke="${PURPLE}" stroke-width="1.6"/>` + label(cx, cy, 'γ', 13, { anchor: 'middle', weight: 900, color: PURPLE }).svg;
    return s; };
  // panel 1: H+ arrives from IMS at the a/c interface and binds a c subunit
  o += pan(20, 0, '1. H⁺ enters from the intermembrane space', 0);
  o += Hion(20 + 135 + 74 + 4, 180 - 70) + `<path d="M${20 + 135 + 74 + 4} ${180 - 56} L ${20 + 135 + 76} ${180 - 22}" stroke="#1d1d1f" stroke-width="2.2"/>` + head(20 + 135 + 76, 180 - 18, 95, '#1d1d1f', 9);
  o += note(155, 310, 'it binds a c subunit next to a', { anchor: 'middle', fs: 13 });
  // panel 2: ring turns one step
  o += pan(310, 1, '2. The ring turns one step', 1, true);
  o += `<path d="M${310 + 135 + 60} ${180 + 70} A 92 92 0 0 1 ${310 + 135 - 30} ${180 + 88}" fill="none" stroke="${PURPLE}" stroke-width="3"/>` + head(310 + 135 - 36, 180 + 86, 170, PURPLE, 11);
  o += note(445, 310, 'the loaded subunit moves into the membrane', { anchor: 'middle', fs: 13 });
  // panel 3: after almost a full turn, H+ released to matrix
  o += pan(600, 9, '3. H⁺ leaves into the matrix', 0);
  o += Hion(600 + 135 + 60, 180 + 86) + `<path d="M${600 + 135 + 68} ${180 + 50} L ${600 + 135 + 64} ${180 + 72}" stroke="#1d1d1f" stroke-width="2.2"/>`;
  o += note(735, 310, 'after nearly a full turn, at the a subunit', { anchor: 'middle', fs: 13 });
  return svgWrap(W, H, o, 'Three panels viewing the Fo rotor from above: a ring of ten c subunits around the central gamma stalk, with the a subunit (stator) on the right. Panel 1: an H+ ion from the intermembrane space binds a c subunit next to the a subunit. Panel 2: the ring turns one step, carrying the loaded subunit into the membrane. Panel 3: after nearly a full turn the subunit reaches the a subunit again and releases its H+ into the matrix. Each H+ that passes turns the ring and the gamma stalk one step.');
}

/* ---------------- 8. Glucose catabolism overview (14.4) ---------------- */
function respiration() {
  const W = 900, H = 700; let o = TITLE(18, 30, 'What happens to glucose: with and without oxygen');
  const box = (x, y, w, h, fill, stroke, lines, fs = 15) => { let s = `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="12" fill="${fill}" stroke="${stroke}" stroke-width="1.8"/>`;
    lines.forEach((t, i) => s += label(x + w / 2, y + 24 + i * 21, t, i === 0 ? fs + 1 : fs - 1.5, { anchor: 'middle', weight: i === 0 ? 900 : 700, color: i === 0 ? '#2d3f4b' : '#3b4a63' }).svg); return s; };
  const arr = (x0, y0, x1, y1, c = INK, lab, side = 1) => { const a = Math.atan2(y1 - y0, x1 - x0) * 180 / Math.PI; let s = line(x0, y0, x1, y1, 3, c) + head(x1, y1, a, c, 12); if (lab) s += label((x0 + x1) / 2 + 12 * side, (y0 + y1) / 2, lab, 13.5, { color: c, weight: 800, anchor: side < 0 ? 'end' : undefined }).svg; return s; };
  // cytosol region
  o += `<rect x="10" y="50" width="${W - 20}" height="${H - 60}" rx="16" fill="#fffaf0" stroke="#ead9b8"/>` + note(26, 72, 'Cytosol', { color: '#8a6a2a', weight: 900 });
  o += box(330, 84, 240, 54, '#ffffff', '#c9b27f', ['Glucose (6 C)']);
  o += arr(450, 138, 450, 182, INK);
  o += box(250, 186, 400, 76, '#fff3d6', '#d9b45a', ['Glycolysis', 'net 2 ATP  +  2 NADH']);
  o += arr(450, 262, 450, 300, INK);
  o += box(330, 302, 240, 54, '#ffffff', '#c9b27f', ['2 Pyruvate (3 C each)']);
  // anaerobic branch (left)
  o += arr(340, 340, 200, 400, RED) + label(258, 350, 'no O_2', 13.5, { anchor: 'middle', color: RED, weight: 800 }).svg;
  o += box(30, 404, 250, 108, '#fdecef', '#d9a1ad', ['Without oxygen', 'muscle: 2 lactate', 'yeast: 2 ethanol + 2 CO_2', 'NADH → NAD⁺ (recycled)']);
  o += note(155, 532, 'only the 2 ATP from glycolysis', { anchor: 'middle', color: RED });
  // aerobic branch (right): mitochondrion
  o += `<rect x="360" y="390" width="520" height="290" rx="60" fill="#eef5fb" stroke="#9fb7d4" stroke-width="2"/>` + note(392, 416, 'Mitochondrion', { color: BLUE, weight: 900 });
  o += arr(560, 340, 640, 418, GREEN) + label(612, 362, 'O_2 present', 13.5, { color: GREEN, weight: 800 }).svg;
  o += box(430, 424, 420, 54, '#ffffff', '#9fb7d4', ['2 Pyruvate → 2 Acetyl CoA + 2 CO_2 + 2 NADH'], 14.5);
  o += arr(640, 478, 640, 500, INK);
  o += box(430, 502, 420, 74, '#f4f1fb', '#c9bfe6', ['Citric acid cycle (2 turns)', '4 CO_2 + 6 NADH + 2 FADH_2 + 2 GTP']);
  o += arr(640, 576, 640, 598, INK);
  o += box(430, 600, 420, 70, '#e8f4ee', '#9fcfb5', ['Electron transport + ATP synthase', 'NADH, FADH_2 → O_2 → H_2O; makes most of the ATP']);
  o += note(30, 584, 'With O₂: up to about 32 ATP per glucose', { color: '#2d3f4b', weight: 900 });
  o += note(30, 604, '(2.5 ATP per NADH, 1.5 per FADH₂,');
  o += note(30, 622, 'plus 2 ATP and 2 GTP made directly).');
  o += note(30, 652, 'All 6 carbons leave as 6 CO₂.', { color: RED });
  return svgWrap(W, H, o, 'Overview of glucose catabolism. In the cytosol, glycolysis converts glucose (6 carbons) into 2 pyruvate (3 carbons each), with a net 2 ATP and 2 NADH. Without oxygen, pyruvate becomes 2 lactate in muscle or 2 ethanol and 2 CO2 in yeast, recycling NADH to NAD+, so only the 2 ATP from glycolysis are made. With oxygen, pyruvate enters the mitochondrion: 2 pyruvate become 2 acetyl CoA, 2 CO2 and 2 NADH; two turns of the citric acid cycle give 4 CO2, 6 NADH, 2 FADH2 and 2 GTP; electron transport passes electrons from NADH and FADH2 to O2, forming water, and ATP synthase makes most of the ATP, for up to about 32 ATP per glucose. All 6 carbons leave as 6 CO2.');
}

out.cac_wheel = cacWheel(); out.glucose_ring = glucoseRing(); out.hydrogenation = hydrogenation(); out.sphingolipids = sphingolipids();
out.myelin_ms = myelin(); out.collagen = collagen(); out.atp_synthase = atpSynthase(); out.atp_rotation = atpRotation(); out.respiration = respiration();
const dir = path.join(__dirname, '..', 'figures', 'pathways', 'oer'); fs.mkdirSync(dir, { recursive: true });
for (const [k, v] of Object.entries(out)) fs.writeFileSync(path.join(dir, k + '.svg'), v);
console.log(Object.keys(out).join(' '));
