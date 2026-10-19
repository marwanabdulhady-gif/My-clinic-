const { chromium } = require('playwright');
(async () => {
  const ver = process.argv[2]; const dir = ver === '1.2' ? 's12' : 's2004';
  const b = await chromium.launch(); const ctx = await b.newContext({ viewport:{width:1300,height:800}}); const p = await ctx.newPage();
  const url = 'http://127.0.0.1:8765/harness.html#' + dir + '/index.html';
  await p.goto(url); await p.waitForTimeout(2500);
  const f = () => p.frames().find(x => x !== p.mainFrame() && x.url().includes('index.html'));
  // go to screen 9 (mcq, index 8)
  for (let i = 0; i < 8; i++) { await f().evaluate(() => { const n = document.getElementById('btnNext'); n.disabled = false; n.click(); }); await p.waitForTimeout(300); }
  await p.waitForTimeout(800);
  await f().evaluate(() => { const s = document.querySelector('.screen[data-screen-id="mcs-023"]');
     s.querySelector('.opt[data-opt="a"]').click();
     s.querySelector('.btn-check').click(); });
  await p.waitForTimeout(1200);
  // leave the course (unload → Finish/Terminate)
  await p.evaluate(() => { document.getElementById('c').src = 'about:blank'; }); await p.waitForTimeout(1200);
  const s1 = await p.evaluate(() => ({ store: JSON.parse(JSON.stringify(window.API && Object.keys(window.calls).length ? null : null)), calls: window.calls }));
  const store1 = await p.evaluate(() => sessionStorage.getItem('cmi'));
  // relaunch
  await p.goto('about:blank'); await p.goto(url); await p.waitForTimeout(3000);
  const where = await f().evaluate(() => { const s = document.querySelector('.screen:not([aria-hidden="true"])'); return s ? s.dataset.screenId : null; });
  const calls2 = await p.evaluate(() => window.calls.filter(c => /entry|suspend|location/.test(c[1]||'')).slice(0,6));
  const st = JSON.parse(store1);
  const keys = Object.keys(st).filter(k => !/suspend_data/.test(k));
  console.log(JSON.stringify({ version: ver,
    api_sequence: s1.calls.filter(c => !/GetValue|LMSGetValue/.test(c[0])).map(c => c[0] + (c[1] && /^cmi/.test(c[1]) ? ' ' + c[1] + '=' + String(c[2]).slice(0,40) : '')).slice(0, 60),
    stored: Object.fromEntries(keys.map(k => [k, st[k].slice(0,60)])), suspend_data_chars: (st['cmi.suspend_data']||'').length,
    resumed_on: where, relaunch_reads: calls2 }, null, 1));
  await b.close();
})();
