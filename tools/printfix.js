/* printfix.js — make chemistry figures and charges survive the LibreTexts PDF export (PrinceXML).
   Issue ledger: R01 (atom labels hidden) and R02 (charges printed as a box glyph). See tools/ISSUE_LEDGER.md.

   R01  The structure drawers put a white outline behind each atom label with
        stroke="#fff" + paint-order="stroke". Browsers paint the outline first, but Prince ignores
        paint-order and paints the white outline ON TOP of the letter, so O, N, Cl, OH… vanish.
        Fix: split each such <text> into two: a white halo copy (aria-hidden) and then the coloured
        letter with no stroke. Same look in browsers, correct in every renderer.
   R02  Superscript charge characters (⁺ U+207A, ⁻ U+207B, and ⁴–⁹/⁰) are not in the book's fonts,
        so Prince prints ⯑. Fix: write the charge as an ordinary + or − raised with <sup> (HTML) or a
        shifted <tspan> (SVG). Attribute values (alt text, aria-label) are left unchanged.

   Works in Node (module.exports) and in the browser (window.PrintFix). Pure string functions, idempotent. */
(function (root) {
  const SUP = { '⁰': '0', '¹': '1', '²': '2', '³': '3', '⁴': '4', '⁵': '5', '⁶': '6', '⁷': '7', '⁸': '8', '⁹': '9', '⁺': '+', '⁻': '−' };
  // A run of superscript characters that contains at least one character the fonts lack.
  const RUN = /[⁰¹²³⁴-⁹⁺⁻]*[⁰⁴-⁹⁺⁻][⁰¹²³⁴-⁹⁺⁻]*/g;
  const plain = r => [...r].map(c => SUP[c]).join('');
  const decodeSupEntities = s => s.replace(/&#(8304|185|178|179|830[89]|831[0-5]);|&#x(2070|b9|b2|b3|207[4-9ab]);/gi, (m, d, h) => String.fromCharCode(d ? +d : parseInt(h, 16)))
    .replace(/&sup([123]);/g, (m, n) => ({ 1: '¹', 2: '²', 3: '³' })[n]);

  // --- SVG text content: superscripts → shifted tspans -------------------------------------------
  function svgTextSup(inner) {
    // Only touch character data, never inside tags.
    return inner.replace(/(^|>)([^<]*)/g, (m, gt, txt) => gt + txt.replace(RUN, (run, off, whole) => {
      const rest = whole.slice(off + run.length);
      const up = `<tspan dy="-0.5em" font-size="70%">${plain(run)}</tspan>`;
      // Bring the baseline back down if more text follows inside this node.
      return rest.length ? up + '<tspan dy="0.35em"></tspan>' : up;
    }).replace(/<tspan dy="0\.35em"><\/tspan>([^<]+)/g, '<tspan dy="0.35em">$1</tspan>'));
  }

  // --- one <text> element --------------------------------------------------------------------------
  const attr = (a, n) => { const m = a.match(new RegExp('\\s' + n + '\\s*=\\s*"([^"]*)"')); return m ? m[1] : null; };
  const drop = (a, names) => names.reduce((s, n) => s.replace(new RegExp('\\s' + n + '\\s*=\\s*"[^"]*"', 'g'), ''), a);
  function fixTextEl(attrs, inner) {
    inner = svgTextSup(inner);
    const po = attr(attrs, 'paint-order') || ((attr(attrs, 'style') || '').match(/paint-order\s*:\s*([^;]+)/) || [])[1];
    const stroke = attr(attrs, 'stroke');
    const isWhite = v => /^(#fff|#ffffff|white|rgb\(255,\s*255,\s*255\))$/i.test((v || '').trim());
    const fill = attr(attrs, 'fill');
    // Halo copies we made (aria-hidden) and plain labels are left alone. A white outline is a halo whether or not
    // paint-order is set: without paint-order even browsers paint it on top, and Prince always does (p.555 NH3+).
    const halo = !/aria-hidden="true"/.test(attrs) && stroke && stroke !== 'none' && !isWhite(fill) &&
                 ((po && /^\s*stroke/.test(po)) || isWhite(stroke));
    if (!halo) return `<text${attrs}>${inner}</text>`;
    let base = drop(attrs, ['paint-order']).replace(/\sstyle="([^"]*)"/, (m, st) => {
      const s2 = st.replace(/paint-order\s*:\s*[^;]+;?/g, '').trim(); return s2 ? ` style="${s2}"` : ''; });
    const haloEl = drop(base, ['fill', 'aria-label', 'role', 'id']) + ` fill="${stroke}" aria-hidden="true"`;
    const letter = drop(base, ['stroke', 'stroke-width', 'stroke-linejoin', 'stroke-linecap', 'stroke-opacity']);
    return `<text${haloEl}>${inner}</text><text${letter}>${inner}</text>`;
  }

  function fixSvg(svg) {
    // No early exit on data-printfix: a file fixed by the first version may still have white-outline labels
    // without paint-order. Element-level checks keep this idempotent.
    svg = decodeSupEntities(svg);                              // some files store ⁺ as &#8314;
    let out = svg.replace(/<text\b([^>]*)>([\s\S]*?)<\/text>/g, (m, a, inner) => fixTextEl(a, inner));
    if (out !== svg && !/data-printfix="1"/.test(out)) out = out.replace(/<svg\b/, '<svg data-printfix="1"');
    return out;
  }

  // --- HTML page: fix inline SVGs, and superscripts in ordinary text ------------------------------
  function fixHtml(html) {
    const parts = decodeSupEntities(html).split(/(<svg\b[\s\S]*?<\/svg>|<script\b[\s\S]*?<\/script>|<style\b[\s\S]*?<\/style>)/i);
    return parts.map((p, i) => {
      if (i % 2) return /^<svg/i.test(p) ? fixSvg(p) : p;
      // character data only (between tags); attributes stay as they are
      return p.replace(/(^|>)([^<]*)/g, (m, gt, txt) => gt + txt.replace(RUN, r => '<sup>' + plain(r).replace('−', '&minus;') + '</sup>'));
    }).join('');
  }

  // Quick count for dry runs: how many things would change.
  function audit(text) {
    const s = decodeSupEntities(text);
    return {
      haloLabels: (s.match(/<text\b[^>]*>/g) || []).filter(t => !/aria-hidden="true"/.test(t) && (/paint-order\s*[:=]\s*"?\s*stroke/.test(t) || (/\sstroke="(#fff|#ffffff|white)"/i.test(t) && !/\sfill="(#fff|#ffffff|white)"/i.test(t)))).length,
      superscriptRuns: (s.match(RUN) || []).length,
    };
  }

  const api = { fixSvg, fixHtml, audit };
  if (typeof module !== 'undefined' && module.exports) module.exports = api; else root.PrintFix = api;
})(typeof window !== 'undefined' ? window : globalThis);
