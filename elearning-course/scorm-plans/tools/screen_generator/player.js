'use strict';
// Review-only state. Nothing is persisted or sent to an LMS or a remote service.
const DATA = JSON.parse(document.getElementById('course-data').textContent);
const $ = id => document.getElementById(id);
const cache = new Map();
let moduleIndex = 0, screenIndex = 0;
const el = (tag, cls, text) => {const n = document.createElement(tag); if (cls) n.className = cls; if (text !== undefined) n.textContent = text; return n;};
Object.entries({primary:'primary', ink:'dark', light:'light', success:'success', error:'error'}).forEach(([variable, color]) => document.documentElement.style.setProperty('--' + variable, DATA.brand.colors[color]));
// Only pre-sanitized *_html / block.html fields from the generator are inserted as HTML.
const rich = (value, cls = '') => {const n = el('div', cls); n.innerHTML = value || ''; return n;};
const button = (text, fn, cls = '') => {const b = el('button', cls, text); b.type = 'button'; b.addEventListener('click', fn); return b;};
const plainHTML = html => rich(html).textContent;
const assetKey = id => (id || '').replace(/^<|>$/g, '');
const assetURL = id => DATA.assets[assetKey(id)] || DATA.preview_assets[assetKey(id)];

/* --- Motion -------------------------------------------------------------
   Applies the structured motion spec that tools/build_motion_spec.py writes into
   every screen (vocabulary in tools/motion_spec.py, presets in style.css).
   motion.reduced_motion = "static" and the OS prefers-reduced-motion setting both
   land every element in its final state with no animation and no hidden layer.  */
const MO_EASING = {standard: 'var(--mo-ease-standard)', decelerate: 'var(--mo-ease-decelerate)',
                   accelerate: 'var(--mo-ease-accelerate)', spring: 'var(--mo-ease-spring)'};
const prefersReducedMotion = () =>
  Boolean(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);

function motionHosts(root) {
  // Layers are applied in authored order to the screen's top-level content blocks.
  const host = root.querySelector('.screen-body') || root.querySelector('.title-copy') ||
               root.querySelector('.section-copy') || root;
  return [...host.children];
}

function applyMotion(root, s) {
  const spec = s._motion;
  if (!spec || typeof spec !== 'object') {root.dataset.motion = 'no-spec'; return;}
  root.dataset.motion = spec.spec_version || 'unspecified';
  root.dataset.motionIntent = spec.intent || '';
  if (prefersReducedMotion()) {
    // OS setting wins over the spec; .mo-static is the runtime form of reduced_motion: "static".
    root.classList.add('mo-static');
    return;
  }
  const entry = spec.entry || {};
  root.classList.add('mo-entry-' + (entry.preset || 'none'));
  root.style.setProperty('--mo-entry-duration', (entry.duration_ms || 0) + 'ms');
  root.style.setProperty('--mo-entry-delay', (entry.delay_ms || 0) + 'ms');
  root.style.setProperty('--mo-easing', MO_EASING[entry.easing] || MO_EASING.standard);
  const hosts = motionHosts(root);
  (spec.layers || []).forEach((layer, index) => {
    const node = hosts[index];
    if (!node) return;
    node.classList.add('mo-layer', 'mo-layer-' + (layer.preset || 'fade-up'));
    node.dataset.moLayer = layer.id;
    node.dataset.moTrigger = layer.trigger || 'enter';
    node.style.setProperty('--mo-layer-duration', (layer.duration_ms || 360) + 'ms');
    node.style.setProperty('--mo-layer-delay', (layer.delay_ms || 0) + 'ms');
    node.style.setProperty('--mo-easing', MO_EASING[layer.easing] || MO_EASING.standard);
  });
  const emphasis = spec.emphasis || {};
  if (emphasis.preset && emphasis.preset !== 'none' && hosts.length) {
    const target = hosts.find(node =>
      (node.textContent || '').toLowerCase().includes(String(emphasis.target || '').toLowerCase())) || hosts[0];
    target.classList.add('mo-emphasis-' + emphasis.preset);
  }
}

function replayCueLayers(root) {
  // Review aid only: fires the cue-bound layers in authored order, the way the narration
  // [[cue:…]] marks will fire them in the built course. No learner state is involved.
  const cueLayers = [...root.querySelectorAll('.mo-layer[data-mo-trigger="cue"]')];
  cueLayers.forEach(node => node.classList.remove('is-cued'));
  cueLayers.forEach((node, index) =>
    setTimeout(() => node.classList.add('is-cued'), 120 + index * 260));
  return cueLayers.length;
}

function media(id, alt) {
  const url = assetURL(id);
  if (url && /\.(png|jpe?g|webp|svg)$/i.test(url)) {
    const img = el('img'); img.src = url; img.alt = alt || '';
    if (!DATA.assets[assetKey(id)] && DATA.preview_assets[assetKey(id)]) img.dataset.reviewArt = 'true';
    return img;
  }
  const box = el('div', 'asset-placeholder');
  box.append(el('strong', '', 'Asset pending'), el('div', '', id || 'No asset assigned'), el('p', '', alt || 'Production visual is not yet supplied.'));
  return box;
}

function feedbackBox() {const box = el('div', 'feedback'); box.setAttribute('role', 'status'); box.hidden = true; return box;}
function feedback(box, screen, correct, custom) {
  box.hidden = false; box.classList.toggle('positive', correct); box.classList.toggle('negative', !correct);
  // Feedback motion comes from motion_spec.feedback_for: settle for a safe choice, a short
  // nudge for one to review. It is cosmetic — the text carries the result (no colour-only cue).
  const spec = (screen.motion || {}).feedback || {};
  const preset = correct ? spec.correct : spec.incorrect;
  box.classList.remove('mo-feedback-settle-once', 'mo-feedback-nudge-once', 'mo-feedback-pulse-once');
  if (preset && preset !== 'none' && !prefersReducedMotion()) {
    box.style.setProperty('--mo-feedback-duration', (spec.duration_ms || 420) + 'ms');
    void box.offsetWidth; // restart the animation when the same box is reused
    box.classList.add('mo-feedback-' + preset);
  }
  box.replaceChildren(el('strong', '', correct ? '✓ Correct for this draft' : '↻ Review this choice'));
  box.append(rich(custom || (screen.feedback || {})[correct ? 'correct_html' : 'incorrect_html'] || '<p>No authored feedback supplied.</p>'));
  box.append(el('small', 'result-note', 'Draft answer check only — no completion or LMS score is recorded.'));
}

function choiceQuestion(s) {
  const form = el('form');
  const options = s.type === 'true_false' ? [{id:'true', text_html:'True', correct:s.correct === true}, {id:'false', text_html:'False', correct:s.correct === false}] : s.options || [];
  const multi = s.multi_select || s.multi;
  const field = el('fieldset', 'options'); field.style.border = '0'; field.style.padding = '0';
  const legend = el('legend', 'result-note', s.type === 'poll' ? 'Reflection · unscored' : multi ? 'Select all that apply' : 'Choose one answer');
  field.append(legend);
  options.forEach((o, i) => {
    const label = el('label', 'option'); const input = el('input'); input.type = multi ? 'checkbox' : 'radio'; input.name = s.id; input.value = String(i);
    label.append(input, rich(o.text_html)); field.append(label);
  });
  form.append(field);
  if (s.type === 'poll' && s.allow_text && !options.length) form.append(rich(s.reflection_html, 'review-only'));
  if (s.allow_text) {const label = el('label', '', 'Optional reflection'); const text = el('textarea'); text.setAttribute('aria-label', 'Optional reflection'); label.append(text); form.append(label);}
  const box = feedbackBox(); const submit = el('button', 'submit', s.type === 'poll' ? 'Reflect' : 'Check draft answer'); submit.type = 'submit';
  form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); const chosen = [...field.querySelectorAll('input:checked')].map(i => Number(i.value));
    if (!chosen.length && options.length) {box.hidden = false; box.textContent = 'Choose an option first.'; return;}
    if (s.type === 'poll') {box.hidden = false; box.replaceChildren(rich(s.reflection_html || '<p>Reflection selected. This poll is unscored.</p>')); return;}
    const correct = options.every((o, i) => Boolean(o.correct) === chosen.includes(i));
    const custom = chosen.length === 1 ? options[chosen[0]].feedback_html : null;
    feedback(box, s, correct, custom);
  });
  return form;
}

function pairedQuestion(s) {
  const form = el('form'); const rows = s.type === 'matching' ? s.pairs : s.items;
  const choices = s.type === 'matching' ? [...new Set(s.pairs.map(p => p.right_html))].sort().map(text => ({id:text, label_html:text})) : s.targets;
  const controls = [];
  rows.forEach((item, i) => {
    const row = el('div', 'answer-row'); const label = el('label'); label.htmlFor = `answer-${s.id}-${i}`; label.append(rich(item.left_html || item.text_html));
    const select = el('select'); select.id = label.htmlFor;
    const placeholder = el('option', '', 'Choose a match'); placeholder.value = ''; select.append(placeholder);
    choices.forEach(c => {const option = el('option', '', plainHTML(c.label_html)); option.value = c.id; select.append(option);});
    row.append(label, select); form.append(row); controls.push(select);
  });
  const box = feedbackBox(); const submit = el('button', 'submit', 'Check draft answer'); submit.type = 'submit'; form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); if (controls.some(c => !c.value)) {box.hidden = false; box.textContent = 'Complete every match first.'; return;}
    feedback(box, s, rows.every((r, i) => controls[i].value === (s.type === 'matching' ? r.right_html : r.correct_target_id)));
  });
  return form;
}

function fillQuestion(s) {
  const form = el('form'); const controls = [];
  s.blanks.forEach(b => {const label = el('label', 'answer-row'); label.append(el('span', '', `Answer · ${b.id}`)); const input = el('input'); input.type = 'text'; input.autocomplete = 'off'; label.append(input); controls.push(input); form.append(label);});
  const box = feedbackBox(); const submit = el('button', 'submit', 'Check draft answer'); submit.type = 'submit'; form.append(submit, box);
  form.addEventListener('submit', event => {
    event.preventDefault(); const norm = value => s.case_sensitive ? value.trim() : value.trim().toLowerCase();
    if (controls.some(c => !c.value.trim())) {box.hidden = false; box.textContent = 'Complete every answer first.'; return;}
    feedback(box, s, s.blanks.every((b, i) => b.accepted.some(a => norm(String(a)) === norm(controls[i].value))));
  });
  return form;
}

function decisionScenario(s) {
  const root = el('div', 'scenario-player');
  let engine;
  try {engine = MyClinicScenario.create(s);} catch (error) {
    root.append(el('div', 'review-only', 'Scenario wiring pending: ' + error.message), reviewContent(s));
    return root;
  }
  const banner = el('div', 'review-only', 'Fictional draft scenario · SME approval pending · no LMS score or pass is recorded.');
  const content = el('div'); root.append(banner, content);
  function draw(focus = false) {
    const state = engine.snapshot(); content.replaceChildren();
    const heading = el('h3', '', state.finished ? 'Draft scenario review complete' : `Decision ${state.trace.length + (state.selected ? 0 : 1)} · ${state.node.id}`);
    heading.tabIndex = -1;
    if (state.finished) {
      content.append(heading, el('p', 'result-note', `Authored branch total: ${state.total}${Number.isFinite(s.pass_score) ? ' · authored scenario threshold: ' + s.pass_score : ''}. This is not a course score or approval.`));
      const log = el('ol'); state.trace.forEach(t => log.append(el('li', '', `${t.node_id} → ${t.choice_id} · authored delta ${t.score_delta}`))); content.append(log);
      content.append(button('Reset draft scenario', () => {engine.reset(); draw(true);}));
    } else {
      const grid = el('div', 'scenario-layout'); const scene = el('div', 'scenario-scene');
      if (state.node.image_asset_id) scene.append(media(state.node.image_asset_id, state.node.image_alt));
      else scene.append(el('div', 'asset-placeholder', 'No scene image is supplied for this authored decision.'));
      const decision = el('div', 'scenario-decision');
      const host = companionAssets(s).find(id => id.includes('avatar'));
      if (host) {
        let pose = host;
        if (state.selected && /after (?:a|each) choice|reacts|feedback/i.test(s.notes || '')) {
          const best = Math.max(...state.node.choices.map(c => c.score_delta));
          const who = host.includes('noor') ? 'noor' : 'omar';
          const target = `char-${who}-avatar-${state.selected.score_delta === best ? 'happy' : 'concern'}`;
          if (assetURL(target)) pose = target;
        }
        decision.append(companionCard(pose, true));
      }
      decision.append(heading, rich(state.node.prompt_html, 'prompt'));
      const choices = el('div', 'options');
      state.node.choices.forEach(choice => {
        const b = button('', () => {engine.choose(choice.id); draw(true);}, 'scenario-choice');
        b.append(rich(choice.text_html)); b.disabled = Boolean(state.selected);
        if (state.selected && state.selected.id === choice.id) b.setAttribute('aria-pressed', 'true');
        choices.append(b);
      }); decision.append(choices);
      if (state.selected) {
        const box = feedbackBox(); box.hidden = false;
        box.append(el('strong', '', 'Authored draft feedback'), rich(state.selected.feedback_html));
        decision.append(box, button(state.selected.goto_node_id === null ? 'Review draft outcome' : 'Continue scenario', () => {engine.advance(); draw(true);}, 'submit'));
      }
      decision.append(button('Reset draft scenario', () => {engine.reset(); draw(true);}, 'scenario-reset'));
      grid.append(scene, decision); content.append(grid);
    }
    if (focus) heading.focus();
  }
  draw(); return root;
}

function panel(item) {
  const box = el('div', 'panel');
  if (item.image_asset_id) box.append(media(item.image_asset_id, item.image_alt));
  box.append(rich(item.body_html)); return box;
}

function tabs(s) {
  const root = el('div'); const row = el('div', 'tabs-row'); const content = el('div');
  const buttons = s.tabs.map((tab, i) => button(tab.label, () => activate(i)));
  function activate(i) {buttons.forEach((b, j) => b.setAttribute('aria-pressed', String(i === j))); content.replaceChildren(panel(s.tabs[i]));}
  row.append(...buttons); root.append(row, content); activate(0); return root;
}

function accordion(s) {
  const root = el('div'); s.items.forEach(item => {const d = el('details', 'accordion-item'); d.append(el('summary', '', item.title), panel(item)); root.append(d);}); return root;
}

function flashcards(s) {
  const root = el('div', 'card-grid'); s.cards.forEach(c => {
    let back = false; const b = button('', () => {back = !back; update();}, 'flashcard');
    function update() {b.setAttribute('aria-pressed', String(back)); b.replaceChildren(el('small', '', back ? 'BACK · select to return' : 'FRONT · select to reveal'), rich(back ? c.back_html : c.front_html));}
    update(); root.append(b);
  }); return root;
}

// Complex production interactions are shown as structured authored content, never
// silently replaced with an invented working assessment or inferred answer key.
function reviewContent(s) {
  const root = el('div'); root.append(el('div', 'review-only', 'Interaction storyboard preview — production logic, scoring and media alignment are not implemented.'));
  function itemCard(item, index) {
    const box = el('div', 'step');
    box.append(el('h3', '', item.title || item.id || `Step ${index + 1}`));
    if (item.text) box.append(el('p', '', item.text));
    for (const key of ['prompt_html', 'instruction_html', 'action_html', 'text_html', 'label_html', 'body_html', 'rationale_html', 'hint_html', 'explain_html', 'scaffold_html']) if (item[key]) box.append(rich(item[key]));
    if (item.image_asset_id) box.append(media(item.image_asset_id, item.image_alt));
    for (const key of ['choices', 'options', 'regions']) {
      if (Array.isArray(item[key])) {
        const list = el('ul'); item[key].forEach(c => {const li = el('li'); li.append(rich(c.text_html || c.label_html || c.id)); if (c.feedback_html) {const d = el('details'); d.append(el('summary', '', 'Authored feedback'), rich(c.feedback_html)); li.append(d);} list.append(li);}); box.append(list);
      }
    }
    return box;
  }
  for (const key of ['nodes', 'steps', 'items', 'regions', 'labels', 'rounds']) {
    if (Array.isArray(s[key])) s[key].forEach((item, i) => root.append(itemCard(item, i)));
  }
  if (s.image_asset_id) root.append(media(s.image_asset_id, s.image_alt));
  if (root.children.length === 1) root.append(el('p', '', s._brief || 'No production interaction detail supplied. Review the source JSON below.'));
  return root;
}

function authoredBlocks(s) {
  const root = el('div', 'content-blocks');
  (s.blocks || []).forEach(block => {
    if (block.html) root.append(rich(block.html, 'content'));
    if (block.asset_id) {
      const withheld = /pending consent/i.test(block.caption || '');
      const consent = (block.caption || '').match(/pending consent\s+([BD]\d+)/i);
      const caption = withheld ? `Portrait and identifying caption withheld · consent ${consent ? consent[1] : 'decision'} pending.` : block.caption || '';
      const figure = el('figure', 'asset-block');
      if (withheld) {
        const placeholder = el('div', 'asset-placeholder');
        placeholder.append(el('strong', '', 'Consent-dependent portrait pending'), el('span', '', assetKey(block.asset_id)), el('p', '', 'No real staff portrait or identifying caption is shown in this draft.'));
        figure.append(placeholder);
      } else figure.append(media(block.asset_id, caption));
      figure.append(el('figcaption', '', caption)); root.append(figure);
    }
  });
  return root;
}

function screenContent(s) {
  const body = el('div');
  if (s.prompt_html || s.intro_html) body.append(rich(s.prompt_html || s.intro_html, 'prompt'));
  if (s._mode === 'brief') {
    body.append(el('div', 'review-only', 'Build detail pending — this is an authored visual brief, not a functional interaction.'));
    if (s.body_html) body.append(rich(s.body_html, 'content'));
    body.append(el('div', 'brief', s._brief || 'No on-screen content supplied.'));
    if (s._planned_visuals && s._planned_visuals.length) {
      const list = el('div', 'planned-scene-list');
      list.append(el('h3', '', 'Planned scene / capture placements'));
      s._planned_visuals.forEach(image => {
        const card = el('div', 'panel'); card.append(el('h4', '', image.asset_id),
          media(image.asset_id, image.alt), el('p', 'result-note', image.brief)); list.append(card);
      }); body.append(list);
    }
    return body;
  }
  switch (s.type) {
    case 'content_slide': case 'summary': {
      const content = s.body_html ? rich(s.body_html, 'content') : authoredBlocks(s); const id = s.media_asset_id || s.image_asset_id;
      if (id) {if (s.layout === 'text_media') content.prepend(el('h2', '', s.title)); const layout = el('div', 'media-layout'); const image = el('div', 'media'); image.append(media(id, s.media_alt || s.image_alt)); layout.append(content, image); body.append(layout);} else body.append(content);
      break;
    }
    case 'mcq': case 'true_false': case 'poll': body.append(choiceQuestion(s)); break;
    case 'matching': case 'drag_drop': body.append(pairedQuestion(s)); break;
    case 'fill_blank': body.append(fillQuestion(s)); break;
    case 'decision_scenario': body.append(decisionScenario(s)); break;
    case 'tabs': body.append(tabs(s)); break;
    case 'accordion': body.append(accordion(s)); break;
    case 'flashcards': body.append(flashcards(s)); break;
    case 'timeline': s.events.forEach(e => {const box = el('div', 'timeline-event'); box.append(el('small', '', e.date), el('h3', '', e.title), rich(e.body_html)); body.append(box);}); break;
    case 'worked_example':
      s.steps.forEach((step, i) => {const box = el('div', 'step'); box.append(el('small', 'eyebrow', `STEP ${i + 1}`), rich(step.action_html)); const d = el('details'); d.append(el('summary', '', 'Why this step?'), rich(step.rationale_html)); box.append(d);
        if (step.artifact_asset_id) {const artifact = el('figure', 'worked-artifact'); artifact.append(media(step.artifact_asset_id, step.artifact_caption), el('figcaption', '', step.artifact_caption || 'Authored example artifact')); box.append(artifact);}
        body.append(box);});
      if (s.self_explanation_prompt_html) {body.append(rich(s.self_explanation_prompt_html)); const text = el('textarea'); text.setAttribute('aria-label', 'Unscored reflection'); body.append(text);} break;
    case 'labeled_diagram':
      if (s.mode === 'display') body.append(displayDiagram(s));
      else body.append(reviewContent(s));
      break;
    case 'results_breakdown':
      body.append(el('div', 'review-only', 'Results layout only. This preview does not calculate a course score or grant a pass.'), rich(s.body_html));
      s.sections.forEach(section => {const d = el('details', 'accordion-item'); d.append(el('summary', '', section.title), el('p', 'result-note', `Evidence: ${(section.screen_ids || []).join(', ')}`), rich(section.advice_html)); body.append(d);}); break;
    default: body.append(reviewContent(s));
  }
  return body;
}

// Companion placements come from each package's Phase 3 table, not arbitrary decoration.
function companionIdentity(id) {
  const noor = id.includes('noor');
  return {name: noor ? 'Noor' : 'Dr. Omar', role: noor ? 'Senior nurse · Safety liaison' : 'Family physician',
          color: noor ? '#652D8C' : '#006E78'};
}
function companionCard(id, avatar = false) {
  const who = companionIdentity(id); const box = el('div', avatar ? 'companion-avatar-row' : 'companion-card');
  box.style.setProperty('--character', who.color);
  const frame = el('div', avatar ? 'avatar-frame' : 'portrait-frame');
  frame.append(media(id, `${who.name}, ${who.role.toLowerCase()}, in the planned companion pose.`));
  const caption = el('div', 'companion-caption');
  caption.append(el('strong', '', who.name), el('small', '', who.role));
  if (!avatar && !DATA.assets[id]) caption.append(el('small', 'review-art-note', 'Review art · full-size G6 pending'));
  box.append(frame, caption); return box;
}
function companionAssets(s) {return (s._companion.assets || []).filter(id => id !== 'char-duo-welcome');}
function displayDiagram(s) {
  const root = el('div', 'diagram-layout'); const labels = el('div', 'diagram-labels');
  (s.labels || []).forEach((label, i) => {
    const row = el('div', 'diagram-label'); row.append(el('span', 'label-number', String(i + 1)), el('p', '', label.text || label.id)); labels.append(row);
  });
  const figure = el('figure', 'diagram-figure'); figure.append(media(s.image_asset_id, s.image_alt));
  figure.append(el('figcaption', '', 'Current authored SVG · labels repeated as readable text'));
  root.append(labels, figure); return root;
}
function tipCard(s) {
  // Only the exact tip written in the card is used. Do not shorten/invent dialogue.
  const match = (s.notes || '').match(/label ["“]([^"”]+)["”]:\s*(.*?)(?:\s*Speaker:|$)/);
  const id = companionAssets(s).find(a => a.includes('avatar'));
  if (!match || !id) return null;
  const who = companionIdentity(id), tip = el('div', 'companion-tip');
  tip.style.setProperty('--character', who.color);
  const avatar = el('div', 'avatar-frame'); avatar.append(media(id, `${who.name}, companion guide.`));
  const text = el('div', 'tip-copy'); text.append(el('strong', '', match[1]), el('p', '', match[2].trim()));
  tip.append(avatar, text); return tip;
}
function resultsContent(m, s) {
  const root = el('div', 'results-layout'); const total = el('div', 'result-total');
  const ring = el('div', 'empty-score-ring'); ring.append(el('strong', '', '—'), el('span', '', 'NOT SCORED'));
  total.append(ring, el('p', '', 'Layout preview only'), el('small', '', 'No pass or completion is awarded.'));
  total.append(el('p', 'planned-pass', 'Planned settings: ' + m.contract.identity['SCORM/completion/pass mark']));
  const sections = el('div', 'objective-results'); sections.append(rich(s.body_html));
  (s.sections || []).forEach(section => {
    const row = el('details', 'objective-row'); const summary = el('summary');
    const heading = el('div', 'objective-heading'); heading.append(el('span', '', section.title), el('small', '', 'NOT RUN'));
    summary.append(heading, el('div', 'unscored-bar'));
    row.append(summary, el('p', 'result-note', `Evidence: ${(section.screen_ids || []).join(', ')}`), rich(section.advice_html)); sections.append(row);
  });
  root.append(total, sections); return root;
}
function buildScreen(m, s) {
  const root = buildSlide(m, s);
  applyMotion(root, s);
  return root;
}

function buildSlide(m, s) {
  const root = el('div', `slide layout-${s._layout.id}`);
  root.dataset.screenId = s.id; root.dataset.layout = s._layout.id;
  root.dataset.reference = s._layout.reference_id;
  const hosts = companionAssets(s);
  const progress = el('div', 'slide-progress'); progress.style.width = ((m.screens.indexOf(s) + 1) / m.screens.length * 100) + '%';
  if (s._layout.id === 'L1') {
    root.classList.add('title-screen'); if (hosts.length > 1) root.classList.add('with-duo');
    const logo = media('brand-logo-horizontal-white', 'My Clinic'); logo.className = 'logo';
    const copy = el('div', 'title-copy');
    copy.append(el('span', 'module-chip', `Module ${m.id.slice(0, 2)} · ${m.contract.identity['Commercial course group']}`), el('h2', '', s.title), el('p', 'subtitle', s.subtitle || s._brief || ''));
    root.append(logo, copy);
    if (hosts.length) {const portraits = el('div', 'title-companions'); hosts.forEach(id => portraits.append(companionCard(id))); root.append(portraits);}
    root.append(el('p', 'tagline', DATA.brand.logo.tagline), el('span', 'title-draft', `DRAFT · ${s.id}`)); return root;
  }
  if (s._layout.id === 'L2') {
    root.classList.add('section-opener');
    const tile = el('div', 'section-tile');
    if (s.media_asset_id) tile.append(media(s.media_asset_id, s.media_alt));
    else tile.append(el('span', '', m.id.slice(0, 2)));
    const text = el('div', 'section-copy'), quote = rich(s.body_html || '', 'section-quote');
    const marker = quote.querySelector('p');
    if (marker && /^SECTION \d/.test(marker.textContent)) {text.append(el('span', 'section-marker', marker.textContent)); marker.remove();}
    text.append(el('h2', '', s.title), quote);
    if (!s.body_html && s._brief) text.append(el('p', '', s._brief));
    const logo = media('brand-logo-horizontal-navy', 'My Clinic'); logo.className = 'section-logo';
    root.append(tile, text, logo, el('span', 'section-id', `DRAFT · ${s.id}`), progress); return root;
  }
  const header = el('div', 'screen-header'); const logo = media('brand-logo-horizontal-navy', 'My Clinic');
  header.append(logo, el('span', 'breadcrumb', s.section || ''), el('span', 'slide-context', s.type.replaceAll('_', ' ')));
  const content = el('div', 'screen-body');
  if (!(s.type === 'content_slide' && s.layout === 'text_media' && (s.media_asset_id || s.image_asset_id))) content.append(el('h2', '', s.title));
  if (['L4', 'L5'].includes(s._layout.id)) content.append(el('div', 'screen-instruction', s.points ? `DRAFT PRACTICE · ${s.points} PLANNED POINTS · NO LMS SCORE` : 'UNSCORED REFLECTION'));
  let body = s.type === 'results_breakdown' && s._mode !== 'brief' ? resultsContent(m, s) : screenContent(s);
  const placement = (s._companion.placement || '').toLowerCase();
  const alreadyPlaced = s.media_asset_id && hosts.includes(assetKey(s.media_asset_id));
  if (hosts.length && !alreadyPlaced && !placement.includes('avatar') && !placement.includes('tip') && !['L5'].includes(s._layout.id)) {
    const layout = el('div', `host-layout${s.type === 'poll' ? ' poll-host' : ''}`); const hostsBox = el('div', 'inline-hosts');
    hosts.forEach(id => hostsBox.append(companionCard(id, id.includes('avatar')))); layout.append(body, hostsBox); body = layout;
  }
  content.append(body);
  if (placement.includes('tip') && !placement.includes('feedback')) {const tip = tipCard(s); if (tip) content.append(tip);}
  const foot = el('div', 'screen-footer'); foot.append(el('span', '', m.title), el('span', '', `DRAFT · ${s.id}`));
  root.append(header, content, foot, progress); return root;
}

function outline() {
  const m = DATA.modules[moduleIndex]; const query = $('search').value.toLowerCase(); const nav = $('outline'); nav.replaceChildren(); let section = null;
  m.screens.forEach((s, i) => {
    if (!`${s.id} ${s.title}`.toLowerCase().includes(query)) return;
    if (s.section !== section) {section = s.section; nav.append(el('div', 'section-label', section || 'Screens'));}
    const b = button('', () => navigate(moduleIndex, i), 'screen-link');
    b.append(el('span', '', s.title), el('small', '', `${s.id} · ${s.type}${s.points ? ' · scored draft' : ''}`));
    if (i === screenIndex) b.setAttribute('aria-current', 'page'); nav.append(b);
  });
  if (!nav.children.length) nav.append(el('p', '', 'No matching screens.'));
}

function render() {
  const m = DATA.modules[moduleIndex], s = m.screens[screenIndex];
  document.documentElement.style.setProperty('--secondary', m.color);
  document.documentElement.style.setProperty('--secondary-text', m.color.toUpperCase() === '#008C99' ? DATA.brand.value_colors.ambitious_dark : m.color);
  $('module').value = String(moduleIndex); $('module-name').textContent = m.title; $('screen-name').textContent = s.title;
  $('mode').textContent = ({rendered:'RENDERED DRAFT', brief:'BUILD DETAIL PENDING', review:'INTERACTION REVIEW'})[s._mode];
  const key = `${m.id}/${s.id}`; if (!cache.has(key)) cache.set(key, buildScreen(m, s));
  $('stage').replaceChildren(cache.get(key));
  $('position').textContent = `${screenIndex + 1} / ${m.screens.length} · ${s.id}`;
  $('prev').disabled = screenIndex === 0; $('next').disabled = screenIndex === m.screens.length - 1;
  const warnings = [];
  const pending = $('pending-facts');
  pending.textContent = s._pending.length ? '⚠ Content awaiting confirmation: ' + s._pending.join(', ') + '. Current wording is retained for kickoff review, not approved policy.' : '';
  pending.hidden = !s._pending.length;
  if (s._withheld.length) warnings.push('Consent-dependent portraits/captions withheld: ' + s._withheld.map(item => item.asset_id).join(', '));
  if (s._missing.length) warnings.push('Missing build fields: ' + s._missing.join(', '));
  if (s._unresolved.length) warnings.push('Assets pending: ' + s._unresolved.join(', '));
  if (s.notes && /char-/.test(s.notes)) warnings.push('Planned companion placement uses existing review-resolution art. Full-size artwork and G6 handoff remain pending.');
  $('warnings').textContent = warnings.join('\n');
  $('transcript').textContent = s.narration_text || 'No narration supplied.';
  $('audio').replaceChildren(); const url = assetURL(s.narration_asset_id);
  if (url && /\.(mp3|wav|ogg)$/i.test(url)) {const a = el('audio'); a.controls = true; a.preload = 'none'; a.src = url; $('audio').append(a);}
  $('metadata').textContent = `${m.source}\nScreen: ${s.id} · Type: ${s.type} · Planned points: ${s.points || 0}\nObjectives: ${(s.objective_ids || []).join(', ') || 'none'}\nEvidence: ${(s.evidence_screen_ids || []).join(', ') || 'none'}\n${s.notes || ''}`;
  $('visual').textContent = s._visual;
  $('layout-source').textContent = `${s._layout.description} · Reference ${s._layout.reference_image} · Geometry compiled from supplied mockups.html. Dense slides expand vertically rather than hiding content.`;
  const contract = m.contract;
  $('alignment-status').textContent = contract.alignment === 'matched' ? 'COUNTS & ORDER MATCHED · NOT APPROVAL' : 'ALIGNMENT NEEDS REVIEW';
  $('worksheet-meta').textContent = `${contract.worksheet}\n${contract.identity.Audience} · ${contract.identity['Seat-time estimate']}\n${contract.actual.screens} screens · ${contract.actual.scored} scored drafts · ${contract.actual.points} planned points\n${contract.issues.join('\n')}`;
  $('template-gates').replaceChildren(...contract.gates.map(g => el('li', '', (g.checked ? '☑ ' : '☐ ') + g.text)));
  $('input-links').replaceChildren(...contract.inputs.map(input => {const li = el('li'); const a = el('a', '', input.path.replace('elearning-course/scorm-plans/', '')); a.href = 'reference/inputs/' + input.path; a.target = '_blank'; a.rel = 'noopener'; li.append(a, el('small', '', ` · SHA256 ${input.sha256.slice(0, 12)}`)); return li;}));
  $('spec').textContent = JSON.stringify(Object.fromEntries(Object.entries(s).filter(([key]) => !key.startsWith('_'))), null, 2);
  motionPanel(s);
  document.title = `${s.id} · My Clinic screen review`; outline();
}

function motionPanel(s) {
  // Reviewer-facing summary of the structured motion spec for the current screen.
  const spec = s._motion;
  const slide = $('stage').firstElementChild;
  if (!spec || typeof spec !== 'object') {
    $('motion-status').textContent = 'NO MOTION SPEC';
    $('motion-summary').textContent = 'This screen has no motion object. Rerun tools/build_motion_spec.py.';
    $('replay-motion').hidden = true; $('motion-reduced').textContent = '';
    return;
  }
  const entry = spec.entry || {}, emphasis = spec.emphasis || {}, exitBlock = spec.exit || {};
  const feedbackBlock = spec.feedback || {};
  const layers = spec.layers || [];
  const cueCount = layers.filter(l => l.trigger === 'cue').length;
  $('motion-status').textContent = `SPEC v${spec.spec_version} · ${String(spec.intent || '').toUpperCase()}`;
  $('motion-summary').innerHTML = '';
  const rows = [
    ['Intent', spec.intent],
    ['Entrance', `${entry.preset} · ${entry.duration_ms} ms · ${entry.easing}`],
    ['Layers', layers.length ? `${layers.length} (${cueCount} bound to narration cues): ` +
      layers.map(l => `${l.id} ${l.preset}@${l.delay_ms}ms`).join(' · ') : 'none'],
    ['Emphasis', emphasis.preset === 'none' ? 'none' : `${emphasis.preset} on ${emphasis.target}`],
    ['Answer feedback', `safe: ${feedbackBlock.correct} · review: ${feedbackBlock.incorrect}`],
    ['Exit', `${exitBlock.preset} · ${exitBlock.duration_ms} ms`],
    ['Entrance budget', `${spec.budget_ms} ms · loop ${spec.loop ? 'yes' : 'no'}`],
  ];
  rows.forEach(([label, value]) => {
    const line = el('span'); line.append(el('strong', '', label + ': '), document.createTextNode(String(value)));
    $('motion-summary').append(line, el('br'));
  });
  $('motion-reduced').textContent = prefersReducedMotion()
    ? 'prefers-reduced-motion is ON in this browser: every preset is disabled and all layers are shown (motion.reduced_motion = "static").'
    : `Reduced-motion fallback: "${spec.reduced_motion}" — with the OS setting on, nothing animates and no cue layer stays hidden.`;
  $('replay-motion').hidden = false;
  $('replay-motion').onclick = () => {
    if (!slide) return;
    slide.classList.remove(...[...slide.classList].filter(c => c.startsWith('mo-entry-')));
    void slide.offsetWidth;
    applyMotion(slide, s);
    replayCueLayers(slide);
  };
}

function navigate(mi, si) {
  moduleIndex = mi; screenIndex = si;
  const hash = '#' + DATA.modules[mi].id + '/' + DATA.modules[mi].screens[si].id;
  // Hash links support deep-linking and browser back/forward without storing learner data.
  if (location.hash !== hash) {location.hash = hash;} else render();
}
function route() {
  const [mid, sid] = location.hash.slice(1).split('/');
  const mi = DATA.modules.findIndex(m => m.id === mid);
  moduleIndex = mi >= 0 ? mi : 0;
  const si = DATA.modules[moduleIndex].screens.findIndex(s => s.id === sid); screenIndex = si >= 0 ? si : 0;
  render();
}
const phase = DATA.report.phase;
$('batch-counter').textContent = phase ? `0${phase.id} / 04` : `${DATA.modules.length} PACKAGES`;
$('batch-title').textContent = phase ? `Phase ${phase.id} · ${phase.title}` : 'Current-content slide review';
$('batch-description').textContent = `${DATA.report.screen_count} current-content slides · ${DATA.modules.length} packages · Storyboards, phase plans and production worksheets required. ${phase ? phase.review_focus : 'Unresolved production gates remain open.'}`;
DATA.report.phase_plan.phases.forEach(p => {const item = el('div', `phase-item${phase && p.id === phase.id ? ' active' : ''}`); item.append(el('strong', '', `0${p.id}`), el('span', '', p.title), el('small', '', phase && p.id === phase.id ? 'CURRENT BATCH' : 'QUEUED')); $('phases').append(item);});
DATA.modules.forEach((m, i) => {const o = el('option', '', m.title); o.value = String(i); $('module').append(o);});
$('module').addEventListener('change', () => {$('search').value = ''; navigate(Number($('module').value), 0);});
$('search').addEventListener('input', outline);
$('prev').addEventListener('click', () => navigate(moduleIndex, Math.max(0, screenIndex - 1)));
$('next').addEventListener('click', () => navigate(moduleIndex, Math.min(DATA.modules[moduleIndex].screens.length - 1, screenIndex + 1)));
window.addEventListener('hashchange', () => {document.querySelectorAll('audio').forEach(a => a.pause()); route();});
route();
