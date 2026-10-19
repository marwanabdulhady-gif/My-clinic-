const { chromium } = require('playwright');
(async () => {
  const ver = process.argv[2]; const dir = ver === '1.2' ? 's12' : 's2004';
  const b = await chromium.launch(); const p = await (await b.newContext()).newPage();
  await p.goto('http://127.0.0.1:8765/harness.html#' + dir + '/index.html'); await p.waitForTimeout(2500);
  const f = () => p.frames().find(x => x !== p.mainFrame() && x.url().includes('index.html'));
  // answer the mcq correctly and visit every screen
  for (let i = 0; i < 12; i++) {
    await f().evaluate(() => { const s = document.querySelector('.screen:not([aria-hidden="true"])');
      if (s && s.dataset.screenId === 'mcs-023') { s.querySelector('.opt[data-opt="a"]').click(); s.querySelector('.btn-check').click(); }
      const n = document.getElementById('btnNext'); n.disabled = false; n.click(); });
    await p.waitForTimeout(700);
  }
  await p.waitForTimeout(1500);
  await p.evaluate(() => { document.getElementById('c').src = 'about:blank'; }); await p.waitForTimeout(1200);
  const st = JSON.parse(await p.evaluate(() => sessionStorage.getItem('cmi')));
  const pick = Object.fromEntries(Object.entries(st).filter(([k]) => /status|score|exit|location|entry|interactions._count|objectives\.\d\.(id|success|completion|status|score.scaled)/.test(k) && !/suspend/.test(k)));
  const ends = await p.evaluate(() => window.calls.filter(c => /Finish|Terminate|Commit/.test(c[0])).length);
  console.log(JSON.stringify({ version: ver, final: pick, interactions: Object.keys(st).filter(k=>/interactions\.\d+\.id/.test(k)).map(k=>st[k]), commits_and_finish: ends, suspend_chars: (st['cmi.suspend_data']||'').length }, null, 1));
  await b.close();
})();
