/* Push the built pages (pages/*.html + pages/manifest.json on GitHub Pages) into the CHEM 3B LibreTexts book.
   How to run: sign in to chem.libretexts.org, open any page of the book, open the browser console (⌥⌘J in Chrome),
   paste this whole file, press Enter. It updates the 15 Chapter Guides and creates (or updates) a "Practice Games"
   page at the end of each chapter. Re-running is safe: existing pages are updated in place.
   Requires: the ItsDrDan/textbook repo pushed to GitHub with Pages on (raw.githubusercontent.com must serve pages/manifest.json). */
(async () => {
  const RAW = 'https://raw.githubusercontent.com/ItsDrDan/textbook/main/pages/';
  const LIVE_EDIT_CUTOFF = '2026-11-05T06:30:00Z'; // pages changed on LibreTexts after this are skipped
  const api = (p, o) => fetch('/@api/deki/' + p, Object.assign({ credentials: 'include' }, o || {}));
  const j = async (p) => (await api(p + (p.includes('?') ? '&' : '?') + 'dream.out.format=json')).json();
  const me = await j('users/current'); console.log('Signed in as', me.username || me['@id']);
  const man = await (await fetch(RAW + 'manifest.json', { cache: 'no-store' })).json();
  const log = [];
  for (const e of man) {
    const html = await (await fetch(RAW + e.file, { cache: 'no-store' })).text();
    if (!html || html.length < 200) { log.push(['SKIP (empty)', e.what]); continue; }
    let id = e.pageId;
    if (!id && e.create) {
      const parent = await j('pages/' + e.create.parentId);
      const subs = [].concat((await j('pages/' + e.create.parentId + '/subpages'))['page.subpage'] || []);
      const existing = e.create.exactTitle ? subs.find(s => s.title === e.create.exactTitle) : subs.find(s => new RegExp('^\\d+\\.\\d+:\\s*' + e.create.title + '$').test(s.title));
      if (existing) id = existing['@id'];
      else {
        const chapNum = (parent.title.match(/^(\d+):/) || [])[1];
        const nums = subs.map(s => +((s.title.match(/^\d+\.(\d+):/) || [])[1] || 0));
        const title = e.create.exactTitle || `${chapNum}.${Math.max(0, ...nums) + 1}: ${e.create.title}`;
        const path = parent.path['#text'] + '/' + title.replace(/ /g, '_');
        const r = await api('pages/=' + encodeURIComponent(encodeURIComponent(path)) + '/contents?edittime=now&abort=exists&title=' + encodeURIComponent(title),
          { method: 'POST', headers: { 'Content-Type': 'text/plain; charset=utf-8' }, body: html });
        log.push([r.status === 200 ? 'CREATED' : 'CREATE FAILED ' + r.status, e.what, title]);
        continue;
      }
    }
    // Guard (added Nov 5, 2026): pages edited directly on LibreTexts after the last build are NOT overwritten.
    // The November 4-5 polish pass (link fixes, merges, renumbering, Rosa openers, Chapter Summaries) was made live on LibreTexts.
    // To overwrite anyway, run  window.FORCE_SYNC = true  in the console before pasting this script.
    const info = await j('pages/' + id);
    if (!window.FORCE_SYNC && new Date(info['date.modified']) > new Date(LIVE_EDIT_CUTOFF)) { log.push(['SKIP (edited on LibreTexts after build)', e.what, id]); continue; }
    const r = await api('pages/' + id + '/contents?edittime=now', { method: 'POST', headers: { 'Content-Type': 'text/plain; charset=utf-8' }, body: html });
    log.push([r.status === 200 ? 'UPDATED' : 'FAILED ' + r.status, e.what, id]);
  }
  console.table(log);
  console.log('Done. Open a Chapter Guide to check the Try It boxes and figures.');
})();
