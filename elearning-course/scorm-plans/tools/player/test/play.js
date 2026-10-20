// Plays one packaged course end to end on a mock SCORM 1.2 LMS (lms.html) and prints one JSON line.
//   node play.js <base-url> <folder> right|wrong [screenshot-dir] [relaunch-after-N-screens]
// Run it through tools/check_packages.py, which serves the packages over http and checks the results.
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node-tools/node_modules/playwright')); }
(async () => {
  const [,, base, mod, mode='right', shots='', stopAt='0'] = process.argv;
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 800 } });
  const p = await ctx.newPage();
  const errs=[]; p.on('pageerror',e=>errs.push(e.message));
  const url=base+'/lms.html#'+encodeURIComponent(base+'/'+mod+'/index.html');
  await p.goto(url); await p.waitForTimeout(1500);
  let f = p.frames()[1];
  const W = mode==='wrong';
  const seen=[]; let guard=0, step=0;
  while(guard++<200){
    const s = await f.evaluate(()=>{const id=window.__mc.state.c; return COURSE.screens.find(x=>x.id===id);});
    seen.push(s.id); step++;
    if (shots) await p.screenshot({path:`${shots}/${String(step).padStart(2,'0')}-${s.id}-a.png`});
    const T=s.type, q=sel=>f.locator('.screen:not(.leave) '+sel);
    const click=async sel=>{ await q(sel).first().click(); await p.waitForTimeout(250); };
    try{
    if(T==='title_slide'){ await click('.btn-start'); continue; }
    if(T==='branching'){ const n=s.id.endsWith('-ask')?1:0; await q('.opt').nth(n).click(); await p.waitForTimeout(700); continue; }
    if(T==='mcq'||T==='true_false'){
      const opts = T==='true_false'?[{correct:s.correct===true},{correct:s.correct===false}]:s.options;
      for(const [i,o] of opts.entries()) if(!!o.correct!==W) { await q('.opt').nth(i).click(); if(!s.multi_select) break; }
      await click('.actions .btn-primary'); }
    else if(T==='fill_blank'){ for(const bl of s.blanks) await q(`input[data-b="${bl.id}"]`).fill(W?'zzz':(bl.accepted[0]||'x')); await click('.actions .btn-primary'); }
    else if(T==='drag_drop'){ for(const it of s.items){ const tgt = W? s.targets.find(t=>t.id!==it.correct_target_id).id : it.correct_target_id; await q(`.pool .token[data-id="${it.id}"]`).click(); await q(`.target[data-id="${tgt}"]`).click(); await p.waitForTimeout(120);} await click('.actions .btn-primary'); }
    else if(T==='matching'){ const ids=s.pairs.map(x=>x.id); for(const [i,id] of ids.entries()){ await q(`[data-l="${id}"]`).click(); await q(`[data-r="${W?ids[(i+1)%ids.length]:id}"]`).click(); } await click('.actions .btn-primary'); }
    else if(T==='sorting'){ if(!W){ for(const [i,it] of s.items.entries()){ for(let k=0;k<12;k++){ const pos=await f.evaluate(id=>[...document.querySelectorAll('.screen:not(.leave) .sortlist li')].findIndex(l=>l.dataset.id===id),it.id); if(pos<=i) break; await q(`.sortlist li[data-id="${it.id}"] .mv[data-d="-1"]`).click(); } } } await click('.actions .btn-primary'); }
    else if(T==='hotspot'){ const n=await q('.spot').count(); for(let i=0;i<n;i++) await q('.spot').nth(i).click(); }
    else if(T==='labeled_diagram' && s.mode==='quiz'){ for(const [i,l] of s.labels.entries()) await q('.legend select').nth(i).selectOption(W?s.labels[(i+1)%s.labels.length].id:l.id); await click('.actions .btn-primary'); }
    else if(T==='simulation'){ for(const st of s.steps){ if(st.regions&&st.regions.length){ const k=st.regions.findIndex(r=>r.correct); await q('.region').nth(k).click({force:true}); await p.waitForTimeout(650);} else { await q('.sim-input input').fill(st.input_accepted[0]); await q('.sim-input input').press('Enter'); await p.waitForTimeout(550);} } }
    else if(T==='decision_scenario'){ let id=s.start_node_id; for(let k=0;k<12&&id;k++){ const n=s.nodes.find(x=>x.id===id); const sc=n.choices.map(c=>c.score_delta||0); const best=W?sc.indexOf(Math.min(...sc)):sc.indexOf(Math.max(...sc)); await q('.scen-node .opt').nth(best).click(); await q('.scen-node .feedback .btn-primary').first().waitFor({timeout:8000}); await click('.scen-node .feedback .btn-primary'); id=s.nodes.find(x=>x.id===n.choices[best].goto_node_id)?n.choices[best].goto_node_id:null; } }
    else if(T==='game'){ let id=s.start_node_id; for(let k=0;k<12&&id;k++){ const n=s.nodes.find(x=>x.id===id); let best=n.choices.findIndex(c=>(c.on_choose||[]).some(a=>a.do==='score.correct')); if(W) best=n.choices.findIndex(c=>!(c.on_choose||[]).some(a=>a.do==='score.correct')); if(best<0) best=0; await q('.scen-node .opt').nth(best).click(); await p.waitForTimeout(250); await q('.scen-node .feedback .btn-primary').first().waitFor({timeout:8000}).catch(()=>{}); const over=await q('.scen-node .feedback .btn-primary').count(); if(!over) break; await click('.scen-node .feedback .btn-primary'); id=n.choices[best].to; if(!(await q('.scen-node').count())) break; } }
    else if(T==='escape_room'){ for(const pz of s.puzzles){ if(!(await q('.scen-node input').count())) break; await q('.scen-node input').fill(W?'nope':pz.accepted[0]); await q('.scen-node input').press('Enter'); await p.waitForTimeout(650);} }
    else if(T==='adaptive_practice'){ for(let k=0;k<20;k++){ if(!(await q('.scen-node .opt').count())) break; const txt=await q('.scen-node .prompt').innerText(); const it=s.items.find(x=>x.prompt_html.replace(/<[^>]+>/g,'').trim().slice(0,30)===txt.trim().slice(0,30)); let k2=it?it.options.findIndex(o=>!!o.correct!==W):0; await q('.scen-node .opt').nth(Math.max(0,k2)).click(); await q('.scen-node .feedback .btn-primary').first().waitFor({timeout:8000}); await click('.scen-node .feedback .btn-primary'); } }
    }catch(e){ errs.push(s.id+': '+e.message.split('\n')[0]); }
    if (shots) await p.screenshot({path:`${shots}/${String(step).padStart(2,'0')}-${s.id}-b.png`});
    if(+stopAt && step===+stopAt){
      const before = await p.evaluate(()=>DATA['cmi.core.lesson_location']);
      // simulate closing and relaunching: keep DATA, reload the iframe
      await p.evaluate(()=>{ LOG.push(['--relaunch--']); document.getElementById('f').src=document.getElementById('f').src; });
      await p.waitForTimeout(1800); f=p.frames()[1];
      const after = await f.evaluate(()=>window.__mc.state.c);
      errs.push(...(before===after?[]:['resume went to '+after+' instead of '+before]));
    }
    const nb = await f.evaluate(()=>{const n=document.getElementById('nextB'); return {dis:n.disabled, hid:n.hidden};});
    if(nb.hid) break;
    if(nb.dis){ errs.push('Next locked on '+s.id); break; }
    await f.locator('#nextB').click(); await p.waitForTimeout(650);
  }
  const lms = await p.evaluate(()=>{ const sets=LOG.filter(x=>x[0]==='set'); const k=Object.keys(DATA);
    return {status:DATA['cmi.core.lesson_status'], score:DATA['cmi.core.score.raw'], exit:DATA['cmi.core.exit'], time:DATA['cmi.core.session_time'], sd:(DATA['cmi.suspend_data']||'').length,
      interactions:k.filter(x=>/interactions\.\d+\.result/.test(x)).length, wrong:k.filter(x=>/interactions\.\d+\.result/.test(x)&&DATA[x]==='wrong').map(x=>DATA[x.replace('result','id')]),
      objectives:k.filter(x=>/objectives\.\d+\.id/.test(x)).map(x=>DATA[x]+':'+DATA[x.replace('id','status')]+':'+DATA[x.replace('id','score.raw')]), commits:LOG.filter(x=>x[0]==='commit').length, init:LOG.filter(x=>x[0]==='init').length}; });
  await f.evaluate(()=>{ window.dispatchEvent(new Event('pagehide')); });
  const fin = await p.evaluate(()=>({finish:LOG.filter(x=>x[0]==='finish').length, exit:DATA['cmi.core.exit'], time:DATA['cmi.core.session_time']}));
  console.log(JSON.stringify({mod, mode, screens:seen.length, last:seen[seen.length-1], errs, status:lms.status, score:lms.score, interactions:lms.interactions, wrong:lms.wrong.length, sd:lms.sd, exit:fin.exit}));
  await b.close();
})();
