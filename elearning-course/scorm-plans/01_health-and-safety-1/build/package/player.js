/* My Clinic course player — SCORM 1.2 (Oracle Learning). No dependencies.
   Reads window.COURSE (written by tools/build_package.py from build/course-spec.json).
   Scoring rules match the storyboards: one attempt per scored activity, points all-or-nothing,
   score = earned / total x 100, status passed/failed when the last screen is reached. */
(function () {
  "use strict";
  var C = window.COURSE, D = document;
  var SCREENS = C.screens, BY = {};
  SCREENS.forEach(function (s, i) { s._i = i; BY[s.id] = s; });
  var TOTAL = SCREENS.reduce(function (a, s) { return a + (s.points || 0); }, 0);
  var QUIZ = { mcq: 1, true_false: 1, fill_blank: 1, drag_drop: 1, matching: 1, sorting: 1, simulation: 1,
    decision_scenario: 1, game: 1, escape_room: 1, adaptive_practice: 1, labeled_diagram: 1, hotspot: 1 };
  var RM = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ------------------------------------------------------------------ SCORM 1.2 */
  var LMS = (function () {
    function find(w) {
      for (var n = 0; w && n < 500; n++) {
        try { if (w.API) return w.API; } catch (e) { return null; }
        if (w.parent === w) break; w = w.parent;
      }
      return null;
    }
    var api = find(window) || (window.opener ? find(window.opener) : null), on = false, done = false, store = {};
    var key = "mc-preview-" + C.prefix;
    if (api) { try { on = String(api.LMSInitialize("")) === "true"; } catch (e) { on = false; } }
    if (!on) { try { store = JSON.parse(localStorage.getItem(key) || "{}"); } catch (e) { store = {}; } }
    function get(k) {
      if (on) { try { return String(api.LMSGetValue(k) || ""); } catch (e) { return ""; } }
      return store[k] || "";
    }
    function set(k, v) {
      if (done) return;
      if (on) { try { api.LMSSetValue(k, String(v)); } catch (e) { } }
      else store[k] = String(v);
    }
    function commit() {
      if (done) return;
      if (on) { try { api.LMSCommit(""); } catch (e) { } }
      else try { localStorage.setItem(key, JSON.stringify(store)); } catch (e) { }
    }
    function finish() {
      if (done) return; commit(); done = true;
      if (on) try { api.LMSFinish(""); } catch (e) { }
    }
    function reset() { try { localStorage.removeItem(key); } catch (e) { } }
    return { get: get, set: set, commit: commit, finish: finish, live: on, reset: reset };
  })();

  /* ------------------------------------------------------------------ state + resume */
  var S = { c: null, v: {}, r: {}, x: {}, h: [], e: 0, f: {} };
  (C.variables || []).forEach(function (v) { S.x[v.name] = v.default; });
  try {
    var raw = LMS.get("cmi.suspend_data");
    if (raw) { var o = JSON.parse(raw); for (var k in o) S[k] = o[k]; }
  } catch (e) { }
  var t0 = Date.now(), commitT = 0;
  if (!LMS.get("cmi.core.lesson_status") || LMS.get("cmi.core.lesson_status") === "not attempted")
    LMS.set("cmi.core.lesson_status", "incomplete");
  LMS.set("cmi.core.score.min", 0); LMS.set("cmi.core.score.max", 100);

  function save(now) {
    var snap = { c: S.c, v: S.v, r: S.r, x: S.x, h: S.h.slice(-15), e: S.e, f: S.f };
    var str = JSON.stringify(snap);
    if (str.length > 4000) { snap.h = []; snap.f = {}; str = JSON.stringify(snap); }   // SCORM 1.2 limit 4096
    LMS.set("cmi.suspend_data", str);
    LMS.set("cmi.core.lesson_location", S.c || "");
    clearTimeout(commitT);
    if (now) LMS.commit(); else commitT = setTimeout(LMS.commit, 800);
  }

  /* ------------------------------------------------------------------ helpers */
  function esc(t) { return String(t == null ? "" : t).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  function src(id) { return C.assets[id] || ""; }
  function html(t) {
    t = String(t || "");
    t = t.replace(/\{\{asset:([\w-]+)\}\}/g, function (m, id) { return src(id) ? '<img src="' + src(id) + '" alt="">' : ""; });
    t = t.replace(/(<span[^>]*data-exploration-ref="([\w-]+)"[^>]*>)[^<]*(<\/span>)/g, function (m, a, k, b) { var v = S.f[k]; return a + (v != null && v !== "" ? esc(v) : "(not answered yet)") + b; });
    t = t.replace(/\{\{\s*([a-zA-Z0-9_]+)\s*\}\}/g, function (m, k) { return esc(S.x[k] != null ? S.x[k] : ""); });
    return t;
  }
  function el(tag, cls, inner) { var e = D.createElement(tag); if (cls) e.className = cls; if (inner != null) e.innerHTML = inner; return e; }
  function st(e, i) { e.classList.add("st"); e.style.setProperty("--i", i); return e; }
  function shuffle(a, seed) {
    a = a.slice(); var x = 0; for (var i = 0; i < seed.length; i++) x = (x * 31 + seed.charCodeAt(i)) | 0;
    for (var j = a.length - 1; j > 0; j--) { x = (x * 1103515245 + 12345) | 0; var k = Math.abs(x) % (j + 1); var t = a[j]; a[j] = a[k]; a[k] = t; }
    return a;
  }
  function norm(v, cs) { v = String(v == null ? "" : v).trim().replace(/\s+/g, " "); return cs ? v : v.toLowerCase(); }
  var TICK = '<svg class="tick" width="14" height="14" viewBox="0 0 14 14"><path d="M2.5 7.5l3 3 6-7" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>';

  /* ------------------------------------------------------------------ variables, HUD, toasts */
  function cond(c) {
    if (!c) return true; var a = S.x[c.var], b = c.value;
    switch (c.cmp) { case "!=": return a != b; case ">": return +a > +b; case "<": return +a < +b; case ">=": return +a >= +b; case "<=": return +a <= +b; default: return a == b; }
  }
  function visible(s) { return cond(s.visible_if); }
  function act(list, firstOnly) {
    (list || []).forEach(function (a) {
      if (firstOnly && a.op === "add") return;
      var before = S.x[a.var];
      if (a.op === "set") S.x[a.var] = a.value;
      else S.x[a.var] = (+S.x[a.var] || 0) + (+a.value || 0);
      if (a.var === C.lives_var) S.x[a.var] = Math.max(0, Math.min(C.max_lives || 5, S.x[a.var]));
      if (a.var === C.points_var && a.op === "add" && a.value > 0) toast("+" + a.value + " XP");
      if (a.var === C.lives_var && S.x[a.var] !== before) toast(C.meter_label + (S.x[a.var] > before ? " ↑" : " ↓"), S.x[a.var] > before ? "meter-up" : "meter-down");
    });
    hud();
  }
  var lastRank = null;
  function rank() {
    var v = +S.x[C.points_var] || 0, r = null;
    (C.levels || []).forEach(function (l) { if (v >= l.min_points) r = l.name; });
    return r;
  }
  function hud() {
    var xp = D.getElementById("hudXp"), rk = D.getElementById("hudRank"), mt = D.getElementById("hudMeter");
    if (xp && C.points_var) { var nv = "★ " + (S.x[C.points_var] || 0) + " XP"; if (xp.textContent !== nv) { xp.textContent = nv; bump(xp); } }
    var r = rank();
    if (rk && r) { if (rk.textContent !== "◆ " + r) { rk.textContent = "◆ " + r; if (lastRank && lastRank !== r) { toast("New rank: " + r, "rank"); bump(rk); } } lastRank = r; }
    if (mt && C.lives_var) {
      var v = +S.x[C.lives_var] || 0, dots = mt.querySelectorAll(".dots i");
      for (var i = 0; i < dots.length; i++) dots[i].classList.toggle("on", i < v);
      mt.classList.toggle("low", v <= 1); mt.setAttribute("aria-label", C.meter_label + ": " + v + " of " + C.max_lives);
    }
  }
  function bump(e) { e.classList.remove("bump"); void e.offsetWidth; e.classList.add("bump"); }
  function toast(t, cls) {
    var L = D.getElementById("toasts"); if (!L) return;
    var e = el("div", "toast " + (cls || ""), esc(t)); L.appendChild(e);
    setTimeout(function () { e.remove(); }, 2500);
  }

  /* ------------------------------------------------------------------ scoring + tracking */
  function earned() { var e = 0; for (var k in S.r) e += S.r[k][0] || 0; return e; }
  function score() { return TOTAL ? Math.round(earned() / TOTAL * 100) : 100; }
  function passed() { return score() >= C.tracking.passing_score; }
  function ts(ms) {
    var s = Math.max(0, Math.round(ms / 1000)), h = Math.floor(s / 3600), m = Math.floor(s % 3600 / 60), x = s % 60;
    return (h < 10 ? "000" : h < 100 ? "00" : h < 1000 ? "0" : "") + h + ":" + (m < 10 ? "0" : "") + m + ":" + (x < 10 ? "0" : "") + x + ".00";
  }
  var shownAt = 0;
  var SCORED = SCREENS.filter(function (s) { return s.points; });
  function track(s, ok, itype, resp) {
    var n = SCORED.indexOf(s); if (n < 0) return;
    var p = "cmi.interactions." + n + ".", d = new Date();
    LMS.set(p + "id", s.id);
    if (s.objective_ids && s.objective_ids[0]) LMS.set(p + "objectives.0.id", s.objective_ids[0]);
    LMS.set(p + "time", (d.getHours() < 10 ? "0" : "") + d.getHours() + ":" + (d.getMinutes() < 10 ? "0" : "") + d.getMinutes() + ":" + (d.getSeconds() < 10 ? "0" : "") + d.getSeconds());
    LMS.set(p + "type", itype || "performance");
    LMS.set(p + "weighting", s.points);
    LMS.set(p + "student_response", String(resp == null ? "" : resp).slice(0, 255));
    LMS.set(p + "result", ok ? "correct" : "wrong");
    LMS.set(p + "latency", ts(Date.now() - shownAt));
  }
  function objectives() {
    (C.objectives || []).forEach(function (o, i) {
      var got = 0, max = 0, all = true;
      SCORED.forEach(function (s) { if ((s.objective_ids || []).indexOf(o.id) >= 0) { max += s.points; if (S.r[s.id]) got += S.r[s.id][0]; else all = false; } });
      if (!max) return;
      var pct = Math.round(got / max * 100), p = "cmi.objectives." + i + ".";
      LMS.set(p + "id", o.id); LMS.set(p + "score.raw", pct); LMS.set(p + "score.min", 0); LMS.set(p + "score.max", 100);
      LMS.set(p + "status", !all ? "incomplete" : pct >= C.tracking.passing_score ? "passed" : "failed");
    });
  }
  function status() {
    LMS.set("cmi.core.score.raw", score());
    objectives();
    if (S.e) LMS.set("cmi.core.lesson_status", passed() ? "passed" : "failed");
    save(true);
  }
  /* record a finished activity; first scored answer counts */
  function result(s, ok, itype, resp) {
    var first = !S.r[s.id];
    if (s.points) {
      if (!first) return;
      S.r[s.id] = [ok ? s.points : 0, ok ? 1 : 0];
      track(s, ok, itype, resp);
    } else if (first) S.r[s.id] = [0, ok ? 1 : 0];
    if (first || !s.points) act(ok ? s.on_correct : s.on_wrong, !first);
    status(); gate(true);
  }

  /* ------------------------------------------------------------------ shell */
  var app, stage, nextB, backB, countE, progE, missionE, drawer, scrim, cur = null, gateOpen = true;
  function shell() {
    app = el("div", "app");
    var top = el("header", "topbar");
    top.innerHTML =
      '<button class="iconbtn" id="menuB" aria-label="Open the menu" aria-expanded="false"><svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h10"/></svg></button>' +
      (C.logo ? '<img class="logo" src="' + C.logo + '" alt="My Clinic">' : "") +
      '<div style="min-width:0"><div class="course">' + esc(C.short_title || C.title) + '</div><div class="mission" id="mission"></div></div>' +
      '<div class="spacer"></div><div class="hud">' +
      (C.lives_var ? '<span class="chip meter" id="hudMeter" role="img"><span class="lbl">' + esc(C.meter_label) + '</span><span class="dots">' + new Array((C.max_lives || 5) + 1).join("<i></i>") + "</span></span>" : "") +
      (C.points_var ? '<span class="chip" id="hudXp" aria-live="polite">★ 0 XP</span>' : "") +
      (C.levels ? '<span class="chip rank" id="hudRank" aria-live="polite"></span>' : "") +
      (LMS.live ? "" : '<span class="preview-tag" title="No LMS found: progress is saved in this browser only">Preview</span>') +
      '</div><div class="progress" id="prog"></div>';
    stage = el("main", "stage"); stage.id = "stage";
    var bot = el("footer", "bottombar");
    bot.innerHTML = '<button class="btn btn-ghost" id="backB">← Back</button><div class="spacer"></div><span class="count" id="count"></span><div class="spacer"></div><button class="btn btn-primary" id="nextB">Next →</button>';
    app.appendChild(top); app.appendChild(stage); app.appendChild(bot);
    scrim = el("div", "scrim"); drawer = el("nav", "drawer"); drawer.setAttribute("aria-label", "Course menu");
    D.body.appendChild(app); D.body.appendChild(scrim); D.body.appendChild(drawer);
    D.body.appendChild(el("div", "toast-layer")).id = "toasts";
    nextB = D.getElementById("nextB"); backB = D.getElementById("backB"); countE = D.getElementById("count");
    progE = D.getElementById("prog"); missionE = D.getElementById("mission");
    nextB.onclick = next; backB.onclick = back;
    D.getElementById("menuB").onclick = function () { menu(true); };
    scrim.onclick = function () { menu(false); };
    D.addEventListener("keydown", function (e) { if (e.key === "Escape") menu(false); });
  }
  function sections() {
    var out = [], idx = {};
    SCREENS.forEach(function (s) { var k = s.section || ""; if (!(k in idx)) { idx[k] = out.length; out.push({ title: (C.titles && C.titles[k]) || k, first: s.id, ids: [] }); } out[idx[k]].ids.push(s.id); });
    return out;
  }
  function menu(open) {
    if (open) {
      var secs = sections(), here = cur ? (cur.section || "") : "";
      drawer.innerHTML = '<h2>Missions</h2><ol>' + secs.map(function (x, i) {
        var done = x.ids.every(function (id) { return S.v[id] || !visible(BY[id]); });
        var reach = x.ids.some(function (id) { return S.v[id]; });
        return '<li style="--i:' + i + '" class="' + (done ? "done" : "") + '"><button data-go="' + x.first + '"' + ((BY[x.first].section || "") === here ? ' aria-current="true"' : "") +
          (reach ? "" : ' disabled title="Not reached yet"') + '><span class="num">' + (done ? "✓" : i + 1) + "</span><span>" + esc(x.title) + "</span></button></li>";
      }).join("") + "</ol>" + (LMS.live ? "" : '<div style="padding:0 24px 24px"><button class="btn btn-ghost" id="resetB">Restart preview</button></div>');
      drawer.querySelectorAll("[data-go]").forEach(function (b) { b.onclick = function () { menu(false); var s = BY[b.dataset.go]; while (s && !visible(s)) s = SCREENS[s._i + 1]; if (s) go(s.id, 1); }; });
      var rb = D.getElementById("resetB"); if (rb) rb.onclick = function () { LMS.reset(); location.reload(); };
    }
    drawer.classList.toggle("open", open); scrim.classList.toggle("open", open);
    D.getElementById("menuB").setAttribute("aria-expanded", open ? "true" : "false");
    if (open) { var f = drawer.querySelector("button:not(:disabled)"); if (f) f.focus(); }
  }

  /* ------------------------------------------------------------------ navigation */
  function nextVisible(i) { for (var j = i + 1; j < SCREENS.length; j++) if (visible(SCREENS[j])) return SCREENS[j]; return null; }
  function prevVisible(i) { for (var j = i - 1; j >= 0; j--) if (visible(SCREENS[j])) return SCREENS[j]; return null; }
  function next() { if (!cur || !gateOpen) return; var n = cur._goto ? BY[cur._goto] : nextVisible(cur._i); if (n) { S.h.push(cur.id); go(n.id, 1); } }
  function back() { var id = S.h.pop(); var p = id ? BY[id] : prevVisible(cur._i); if (p) go(p.id, -1, true); }
  function gate(open) {
    gateOpen = open; nextB.disabled = !open || !nextVisible(cur._i) && !cur._goto;
    if (open && cur && QUIZ[cur.type]) { nextB.classList.remove("ready"); void nextB.offsetWidth; nextB.classList.add("ready"); }
  }
  function go(id, dir, isBack) {
    var s = BY[id]; if (!s) return;
    var first = !S.v[s.id];
    cur = s; S.c = s.id; S.v[s.id] = 1; shownAt = Date.now();
    act(s.on_enter, !first);
    var old = stage.querySelector(".screen:not(.leave)");
    var scr = el("section", "screen t-" + (s.type === "title_slide" ? "title" : s.type) + (dir < 0 ? " back" : ""));
    scr.setAttribute("aria-label", s.title || "");
    var inner = el("div", "screen-in"); scr.appendChild(inner);
    gateOpen = true;
    try { (R[s.type] || R.content_slide)(s, inner); } catch (e) { inner.innerHTML = '<div class="card">This screen could not be shown (' + esc(e.message) + ").</div>"; if (window.console) console.error(e); }
    if (old) { old.classList.add("leave"); if (dir < 0) old.classList.add("back"); setTimeout(function () { old.remove(); }, RM ? 0 : 330); }
    scr.classList.add("enter"); stage.appendChild(scr);
    scr.scrollTop = 0;
    var last = !nextVisible(s._i);
    if (last) { S.e = 1; status(); }
    var vis = SCREENS.filter(visible), pos = vis.indexOf(s) + 1;
    countE.textContent = pos + " / " + vis.length;
    progE.style.width = (pos / vis.length * 100) + "%";
    missionE.textContent = (C.titles && C.titles[s.section]) || s.section || "";
    backB.disabled = !S.h.length && !prevVisible(s._i);
    nextB.hidden = last; gate(gateOpen);
    app.classList.toggle("on-title", s.type === "title_slide");
    save();
    setTimeout(function () { var h = scr.querySelector("h1"); if (h && D.body.dataset.ready) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); } D.body.dataset.ready = 1; }, 60);
  }

  /* ------------------------------------------------------------------ screen parts */
  function head(s, box, i) {
    var k = el("div"); k.innerHTML = (s.points ? '<span class="kicker">Activity · ' + s.points + " points</span>" : QUIZ[s.type] && s.type !== "hotspot" && s.type !== "labeled_diagram" ? '<span class="kicker">Quick check · not scored</span>' : "") +
      '<h1 class="title">' + esc(s.title) + "</h1>";
    box.appendChild(st(k, i || 0)); return k;
  }
  function rich(h, cls) { return el("div", "rich " + (cls || ""), html(h)); }
  function fbHtml(s, ok, extra) {
    var f = s.feedback || {}, t = (ok ? f.correct_html : f.incorrect_html) || "";
    t = t.replace(/^(<p>)?\s*(<strong>)?\s*(Correct|Not quite|Not yet|Right)[.!:]?\s*(<\/strong>)?\s*[—-]?\s*/i, "$1");   // the header already says it
    return '<div class="fh"><span class="fi">' + (ok ? TICK : "✕") + "</span>" + (ok ? "Correct" : "Not quite") + '</div><div class="rich">' + html(t || "") + (extra || "") + "</div>";
  }
  function feedback(box, s, ok, extra) {
    var old = box.querySelector(".feedback"); if (old) old.remove();
    var f = el("div", "feedback " + (ok ? "ok" : "no"), fbHtml(s, ok, extra)); f.setAttribute("role", "status");
    box.appendChild(f); setTimeout(function () { f.scrollIntoView({ behavior: RM ? "auto" : "smooth", block: "nearest" }); }, 120);
    return f;
  }
  /* answered before (resume / revisit): show the result instead of a fresh attempt */
  function answered(s, box) {
    var r = S.r[s.id]; if (!r || !s.points) return false;
    box.appendChild(st(rich(s.prompt_html || s.intro_html || ""), 1));
    var f = el("div", "feedback " + (r[1] ? "ok" : "no"), fbHtml(s, !!r[1]) + '<p class="note" style="margin:8px 0 0">You have already answered this activity. ' + r[0] + " of " + s.points + " points.</p>");
    box.appendChild(f); return true;
  }
  function checkBtn(label) { var b = el("button", "btn btn-primary", label || "Check"); b.type = "button"; return b; }
  function needAnswer(s) { if (QUIZ[s.type] && s.type !== "hotspot" && s.type !== "labeled_diagram" && !S.r[s.id]) gate(false); }
  function retry(box, s, redo) {
    if (s.points) return;
    var b = el("button", "btn btn-ghost", "Try again"); b.type = "button";
    b.onclick = function () { box.innerHTML = ""; redo(); };
    var a = box.querySelector(".feedback"); if (a) a.appendChild(el("div", "actions")).appendChild(b);
  }
  function media(id, alt, cls) { return id && src(id) ? '<div class="' + (cls || "media-card") + '"><img src="' + src(id) + '" alt="' + esc(alt || "") + '"></div>' : ""; }
  function fit(img, cb) { if (img.complete && img.naturalWidth) cb(); else img.addEventListener("load", cb); }

  /* ------------------------------------------------------------------ renderers */
  var R = {};

  R.title_slide = function (s, box) {
    var guides = [], m, re = /<div class="mc-guide (noor|omar)">\{\{asset:([\w-]+)\}\}<span>([^<]*)<\/span><\/div>/g;
    while ((m = re.exec(s.body_html || ""))) guides.push(m);
    var left = el("div");
    left.innerHTML = '<span class="kicker">My Clinic · ' + (C.module && C.module !== "00" ? "Module " + esc(C.module) : "Sample course") + '</span><h1>' + esc(s.title) + '</h1>' + (s.subtitle && s.title.indexOf(s.subtitle) < 0 ? '<div class="sub">' + esc(s.subtitle) + '</div>' : "") + '<div class="rule"></div>' +

      '<div class="start"><button class="btn btn-start" type="button">' + (S.e || Object.keys(S.v).length > 2 ? "Continue" : "Start") + ' →</button></div>' +
      '<div class="meta">' + esc(C.duration ? C.duration + " minutes · " : "") + "Pass mark " + C.tracking.passing_score + "%</div>";
    [].forEach.call(left.children, function (c, i) { st(c, i); });
    left.querySelector(".btn-start").onclick = next;
    var right = el("div", "guides");
    guides.forEach(function (g, i) {
      var d = el("div", "guide", '<img src="' + src(g[2]) + '" alt="' + esc(g[3]) + ', your course guide"><span>' + esc(g[3]) + "</span>");
      d.style.setProperty("--i", i); d.style.setProperty("--c", g[1] === "noor" ? "#652D8C" : "#008C99"); right.appendChild(d);
    });
    if (C.petal) box.appendChild(el("img", "petal")).src = C.petal;
    var mo = /<div class="mc-motion">\{\{asset:([\w-]+)\}\}<\/div>/.exec(s.body_html || "");
    if (mo && src(mo[1])) { var mi = box.appendChild(el("img", "motion")); mi.src = src(mo[1]); mi.alt = ""; }
    box.appendChild(left); box.appendChild(right);
  };

  R.content_slide = function (s, box) {
    head(s, box);
    var body = el("div");
    if (s.blocks && s.blocks.length) s.blocks.forEach(function (b, i) { var c = el("div", "card rich", html(b.html)); c.style.marginBottom = "12px"; body.appendChild(st(c, i + 1)); });
    else body.appendChild(st(rich(s.body_html), 1));
    var md = s.media_asset_id && src(s.media_asset_id);
    if (md && s.layout === "text_media") {
      var g = el("div", "split"), char = /^char-/.test(s.media_asset_id);
      if (char && !s.blocks && (s.body_html || "").replace(/<[^>]+>/g, "").length < 260) body.firstChild.classList.add("speech");
      g.appendChild(body);
      g.appendChild(st(el("div", char ? "media-char" : "media-card", '<img src="' + md + '" alt="' + esc(s.media_alt || "") + '">'), 2));
      box.appendChild(g);
    } else if (md) { box.appendChild(body); box.appendChild(st(el("div", "figure", '<img src="' + md + '" alt="' + esc(s.media_alt || "") + '">'), 2)); }
    else box.appendChild(body);
  };
  R.summary = function (s, box) {
    head(s, box);
    if (s.show_score) {
      var p = passed(), h = el("div", "result-head");
      h.innerHTML = ring() + '<div><span class="status-pill ' + (p ? "pass" : "fail") + '">' + (p ? "✓ Passed" : "Not passed yet") + "</span><p class=\"note\" style=\"margin-top:10px\">Pass mark " + C.tracking.passing_score + "%. " + earned() + " of " + TOTAL + " points.</p></div>";
      box.appendChild(st(h, 1)); countUp(h); if (p) confetti();
    }
    box.appendChild(st(rich(s.body_html), 2));
    var a = el("div", "actions"); var fin = el("button", "btn btn-primary", "Finish the course"); fin.type = "button";
    fin.onclick = function () { S.e = 1; status(); LMS.finish(); fin.disabled = true; fin.textContent = "Saved. You can close this window."; try { if (window.opener) window.close(); } catch (e) { } };
    a.appendChild(fin); box.appendChild(st(a, 3));
  };
  function ring() { return '<div class="score-ring" style="--p:0"><div><span><b data-to="' + score() + '">0%</b><small>Your score</small></span></div></div>'; }
  function countUp(h) {
    var b = h.querySelector("[data-to]"), r = h.querySelector(".score-ring"), to = +b.dataset.to, t = 0;
    if (RM) { b.textContent = to + "%"; r.style.setProperty("--p", to); return; }
    var iv = setInterval(function () { t += 1 / 40; var v = Math.round(to * (1 - Math.pow(1 - Math.min(t, 1), 3))); b.textContent = v + "%"; r.style.setProperty("--p", v); if (t >= 1) clearInterval(iv); }, 25);
  }
  function confetti() {
    if (RM) return; var c = el("div", "confetti"), cols = ["#003867", C.colour, "#9D3293", "#C0CED9", "#652D8C"];
    for (var i = 0; i < 70; i++) { var p = el("i"); p.style.left = Math.random() * 100 + "%"; p.style.background = cols[i % cols.length]; p.style.animationDelay = Math.random() * .8 + "s"; p.style.transform = "rotate(" + Math.random() * 360 + "deg)"; c.appendChild(p); }
    D.body.appendChild(c); setTimeout(function () { c.remove(); }, 3800);
  }
  R.results_breakdown = function (s, box) {
    head(s, box);
    var p = passed(), h = el("div", "result-head");
    h.innerHTML = (s.show_total ? ring() : "") + '<div><span class="status-pill ' + (p ? "pass" : "fail") + '">' + (p ? "✓ Passed" : "Below the pass mark") + '</span><p class="note" style="margin-top:10px">' + earned() + " of " + TOTAL + " points · pass mark " + C.tracking.passing_score + "%</p></div>";
    box.appendChild(st(h, 1)); if (s.show_total) countUp(h);
    var bars = el("div", "bars"), weakIds = [];
    (s.sections || []).forEach(function (sec, i) {
      var got = 0, max = 0;
      sec.screen_ids.forEach(function (id) { var x = BY[id]; if (x && x.points) { max += x.points; if (S.r[id]) got += S.r[id][0]; } });
      var pct = max ? Math.round(got / max * 100) : 100, weak = pct < (s.weak_threshold || 70);
      if (weak) sec.screen_ids.forEach(function (id) { if (BY[id] && BY[id].points && (!S.r[id] || !S.r[id][1])) weakIds.push(id); });
      var t = sec.title.replace(/^[\w-]+-o\d+\s*·\s*/, "");
      var row = el("div", "bar-row" + (weak ? " weak" : ""), '<div class="bh"><span>' + esc(t) + "</span><span>" + pct + '%</span></div><div class="bar"><i></i></div>' + (weak && sec.advice_html ? '<div class="adv rich">' + html(sec.advice_html) + "</div>" : ""));
      bars.appendChild(st(row, i + 2));
      setTimeout(function () { row.querySelector(".bar i").style.width = pct + "%"; }, 300 + i * 90);
    });
    box.appendChild(bars);
    if (!p && weakIds.length) {
      var a = el("div", "actions"), b = el("button", "btn btn-mod", "Try the activities you missed"); b.type = "button";
      b.onclick = function () { weakIds.forEach(function (id) { delete S.r[id]; }); S.e = 0; save(true); go(weakIds[0], 1); };
      a.appendChild(b); box.appendChild(st(a, 20));
    }
  };

  R.branching = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var g = el("div", "choice-big");
    s.choices.forEach(function (c, i) {
      var b = el("button", "opt", '<span class="rich">' + html(c.text_html) + "</span>"); b.type = "button";
      b.onclick = function () { act(c.set_vars); s._goto = c.goto_screen_id; S.h.push(s.id); var n = BY[c.goto_screen_id] || nextVisible(s._i); go(n.id, 1); };
      g.appendChild(st(b, i + 2));
    });
    box.appendChild(g); gate(false); s._goto = null;
  };

  function choiceQuiz(s, box) {
    head(s, box);
    if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var tf = s.type === "true_false", multi = !!s.multi_select;
    var opts = tf ? [{ id: "true", text_html: "True", correct: s.correct === true }, { id: "false", text_html: "False", correct: s.correct === false }] : s.options;
    var g = el("div", "options" + (tf ? " tf" : "")), btns = [];
    opts.forEach(function (o, i) {
      var b = el("button", "opt" + (multi ? " multi" : ""), (tf ? "" : '<span class="mark">' + String.fromCharCode(65 + i) + "</span>") + '<span><span class="rich">' + html(o.text_html) + "</span></span>");
      b.type = "button"; b.setAttribute("aria-pressed", "false"); b._o = o;
      b.onclick = function () {
        if (!multi) btns.forEach(function (x) { x.setAttribute("aria-pressed", "false"); });
        b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") === "true" ? "false" : "true");
        chk.disabled = !btns.some(function (x) { return x.getAttribute("aria-pressed") === "true"; });
      };
      btns.push(b); g.appendChild(st(b, i + 2));
    });
    box.appendChild(g);
    var a = el("div", "actions"), chk = checkBtn(); chk.disabled = true; a.appendChild(chk); box.appendChild(st(a, opts.length + 2));
    chk.onclick = function () {
      var sel = btns.filter(function (x) { return x.getAttribute("aria-pressed") === "true"; });
      var ok = btns.every(function (x) { return !!x._o.correct === (sel.indexOf(x) >= 0); });
      btns.forEach(function (x) {
        x.disabled = true;
        var picked = sel.indexOf(x) >= 0;
        if (x._o.correct && (s.feedback || {}).show_correct_answer !== false) { x.classList.add("correct"); var mk = x.querySelector(".mark"); if (mk) mk.innerHTML = TICK; }
        else if (picked) x.classList.add("wrong"); else x.classList.add("dim");
        if (picked && x._o.feedback_html) x.lastChild.appendChild(el("span", "ofb rich", html(x._o.feedback_html)));
      });
      a.remove(); feedback(box, s, ok);
      result(s, ok, tf ? "true-false" : "choice", tf ? (sel[0] && sel[0]._o.id === "true" ? "t" : "f") : sel.map(function (x) { return x._o.id; }).join(","));
      retry(box, s, function () { choiceQuiz(s, box); });
    };
    needAnswer(s);
  }
  R.mcq = choiceQuiz; R.true_false = choiceQuiz;

  R.fill_blank = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    var n = 0, used = {}, inp = function (b, k) { used[b.id] = 1; return '<input class="field" style="display:inline-block;width:130px;flex:none;padding:6px 10px" data-b="' + b.id + '" aria-label="Answer ' + k + '" autocomplete="off">'; };
    var p = html(s.prompt_html).replace(/\[([\w-]+)\]/g, function (m, id) { var b = s.blanks.filter(function (x) { return x.id === id; })[0]; return b ? inp(b, ++n) : m; })
      .replace(/_{3,}/g, function () { var b = s.blanks.filter(function (x) { return !used[x.id]; })[0]; return b ? inp(b, ++n) : ""; });
    var pr = rich(p, "prompt"); box.appendChild(st(pr, 1));
    s.blanks.filter(function (x) { return !used[x.id]; }).forEach(function (b) { used[b.id] = 1; pr.appendChild(el("div", "sim-input", '<input class="field" data-b="' + b.id + '" aria-label="Your answer" autocomplete="off">')); });
    var a = el("div", "actions"), chk = checkBtn(); a.appendChild(chk); box.appendChild(st(a, 2));
    var ins = box.querySelectorAll("input[data-b]");
    ins.forEach(function (i) { i.addEventListener("keydown", function (e) { if (e.key === "Enter") chk.click(); }); });
    chk.onclick = function () {
      var ok = true, resp = [];
      ins.forEach(function (i) {
        var b = s.blanks.filter(function (x) { return x.id === i.dataset.b; })[0];
        var hit = b.accepted.some(function (v) { return norm(v, s.case_sensitive) === norm(i.value, s.case_sensitive); });
        i.classList.add(hit ? "ok" : "no"); i.disabled = true; if (!hit) ok = false; resp.push(i.value);
      });
      a.remove(); feedback(box, s, ok); result(s, ok, "fill-in", resp.join(","));
      retry(box, s, function () { R.fill_blank(s, box); });
    };
    needAnswer(s);
  };

  /* pointer drag with click-to-place fallback (keyboard and touch friendly) */
  function dragKit(container, onDrop) {
    var armed = null, ghost = null, from = null;
    function arm(t) {
      container.querySelectorAll(".token").forEach(function (x) { x.setAttribute("aria-pressed", x === t && armed !== t ? "true" : "false"); });
      armed = armed === t ? null : t;
      container.querySelectorAll(".target").forEach(function (z) { z.classList.toggle("armed", !!armed); });
    }
    container.addEventListener("click", function (e) {
      var t = e.target.closest(".token"), z = e.target.closest(".target,.pool");
      if (t && !t.disabled && !(armed && t !== armed && z && !z.classList.contains("pool"))) { arm(t); return; }
      if (z && armed) { onDrop(armed, z); armed.setAttribute("aria-pressed", "false"); armed = null; container.querySelectorAll(".target").forEach(function (q) { q.classList.remove("armed"); }); }
    });
    container.addEventListener("pointerdown", function (e) {
      var t = e.target.closest(".token"); if (!t || t.disabled || e.button > 0) return;
      var sx = e.clientX, sy = e.clientY, moved = false;
      function mv(ev) {
        if (!moved && Math.abs(ev.clientX - sx) + Math.abs(ev.clientY - sy) < 6) return;
        if (!moved) { moved = true; ghost = t.cloneNode(true); ghost.classList.add("ghost"); ghost.style.width = t.offsetWidth + "px"; D.body.appendChild(ghost); t.classList.add("dragging"); from = t; }
        ghost.style.left = ev.clientX - t.offsetWidth / 2 + "px"; ghost.style.top = ev.clientY - 20 + "px";
        var o = D.elementFromPoint(ev.clientX, ev.clientY), z = o && o.closest(".target,.pool");
        container.querySelectorAll(".target,.pool").forEach(function (q) { q.classList.toggle("over", q === z); });
      }
      function up(ev) {
        D.removeEventListener("pointermove", mv); D.removeEventListener("pointerup", up);
        if (!moved) return;
        var o = D.elementFromPoint(ev.clientX, ev.clientY), z = o && o.closest(".target,.pool");
        container.querySelectorAll(".target,.pool").forEach(function (q) { q.classList.remove("over"); });
        ghost.remove(); ghost = null; from.classList.remove("dragging");
        if (z && container.contains(z)) onDrop(from, z);
        container._noclick = true; setTimeout(function () { container._noclick = false; }, 0);
      }
      D.addEventListener("pointermove", mv); D.addEventListener("pointerup", up);
    });
    container.addEventListener("click", function (e) { if (container._noclick) e.stopImmediatePropagation(); }, true);
  }
  R.drag_drop = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var wrap = el("div"), pool = el("div", "pool"); pool.setAttribute("aria-label", "Items to place");
    shuffle(s.items, s.id).forEach(function (it) { var t = el("button", "token", html(it.text_html)); t.type = "button"; t.dataset.id = it.id; pool.appendChild(t); });
    var tg = el("div", "targets");
    s.targets.forEach(function (x) { var z = el("div", "target", '<div class="tl">' + html(x.label_html) + '</div><div class="zone"></div>'); z.dataset.id = x.id; tg.appendChild(z); });
    wrap.appendChild(pool); wrap.appendChild(tg); box.appendChild(st(wrap, 2));
    box.appendChild(st(el("p", "note", "Drag each item to a box, or tap an item and then tap a box."), 3));
    var a = el("div", "actions"), chk = checkBtn(); chk.disabled = true; a.appendChild(chk); box.appendChild(st(a, 4));
    dragKit(wrap, function (t, z) {
      (z.classList.contains("pool") ? z : z.querySelector(".zone")).appendChild(t);
      t.classList.remove("placed"); void t.offsetWidth; t.classList.add("placed");
      chk.disabled = pool.querySelectorAll(".token").length > 0;
    });
    chk.onclick = function () {
      var ok = true, resp = [];
      wrap.querySelectorAll(".target").forEach(function (z) {
        z.querySelectorAll(".token").forEach(function (t) {
          var it = s.items.filter(function (i) { return i.id === t.dataset.id; })[0], hit = it.correct_target_id === z.dataset.id;
          t.classList.add(hit ? "ok" : "no"); t.disabled = true; if (!hit) ok = false; resp.push(t.dataset.id + "." + z.dataset.id);
          if (!hit && (s.feedback || {}).show_correct_answer !== false) { var tgt = s.targets.filter(function (q) { return q.id === it.correct_target_id; })[0]; if (tgt) t.appendChild(el("small", "", '<br>→ ' + html(tgt.label_html).replace(/<[^>]+>/g, ""))); }
        });
      });
      pool.hidden = true; a.remove(); feedback(box, s, ok); result(s, ok, "matching", resp.join(","));
      retry(box, s, function () { R.drag_drop(s, box); });
    };
    needAnswer(s);
  };

  var PAIR = ["#E6F4F5", "#F1EAF6", "#FBEFF9", "#F7E8EE", "#E8EEF5", "#EAF4EE", "#FFF4E5", "#EEF0F2", "#E3F0FA", "#F5EFE6"];
  var PAIRB = ["#008C99", "#652D8C", "#9D3293", "#7C0041", "#003867", "#1E7B4F", "#B26A00", "#5B6B7B", "#0B4C82", "#8A6D3B"];
  R.matching = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var m = el("div", "match"), L = el("div", "col"), Rc = el("div", "col"), pairs = {}, pick = null, colour = 0;
    s.pairs.forEach(function (p) { var b = el("button", "mitem", html(p.left_html)); b.type = "button"; b.dataset.l = p.id; L.appendChild(b); });
    shuffle(s.pairs, s.id).forEach(function (p) { var b = el("button", "mitem", html(p.right_html)); b.type = "button"; b.dataset.r = p.id; Rc.appendChild(b); });
    m.appendChild(L); m.appendChild(Rc); box.appendChild(st(m, 2));
    box.appendChild(st(el("p", "note", "Tap an item on the left, then its match on the right. Tap a matched item to undo it."), 3));
    var a = el("div", "actions"), chk = checkBtn(); chk.disabled = true; a.appendChild(chk); box.appendChild(st(a, 4));
    function paint() {
      m.querySelectorAll(".mitem").forEach(function (b) { b.classList.remove("paired"); b.style.removeProperty("--pc"); var pn = b.querySelector(".pn"); if (pn) pn.remove(); });
      var n = 0; for (var l in pairs) {
        var lb = L.querySelector('[data-l="' + l + '"]'), rb = Rc.querySelector('[data-r="' + pairs[l] + '"]'), c = lb._c;
        n++; [lb, rb].forEach(function (b) { b.classList.add("paired"); b.style.setProperty("--pc", PAIR[c % 10]); b.style.setProperty("--pc-b", PAIRB[c % 10]); b.appendChild(el("span", "pn", String(n))); });
      }
      chk.disabled = Object.keys(pairs).length < s.pairs.length;
    }
    m.addEventListener("click", function (e) {
      var b = e.target.closest(".mitem"); if (!b || b.disabled) return;
      if (b.dataset.l) {
        if (pairs[b.dataset.l]) { delete pairs[b.dataset.l]; pick = null; paint(); return; }
        L.querySelectorAll(".mitem").forEach(function (x) { x.setAttribute("aria-pressed", x === b ? "true" : "false"); }); pick = b; return;
      }
      for (var l in pairs) if (pairs[l] === b.dataset.r) { delete pairs[l]; paint(); return; }
      if (!pick) return;
      pick._c = colour++; pairs[pick.dataset.l] = b.dataset.r; pick.setAttribute("aria-pressed", "false"); pick = null; paint();
    });
    chk.onclick = function () {
      var ok = true, resp = [];
      for (var l in pairs) {
        var hit = l === pairs[l]; if (!hit) ok = false; resp.push(l + "." + pairs[l]);
        L.querySelector('[data-l="' + l + '"]').classList.add(hit ? "ok" : "no"); Rc.querySelector('[data-r="' + pairs[l] + '"]').classList.add(hit ? "ok" : "no");
      }
      m.querySelectorAll(".mitem").forEach(function (b) { b.disabled = true; });
      var extra = ok || (s.feedback || {}).show_correct_answer === false ? "" : "<ul>" + s.pairs.map(function (p) { return "<li><strong>" + html(p.left_html) + "</strong> → " + html(p.right_html) + "</li>"; }).join("") + "</ul>";
      a.remove(); feedback(box, s, ok, extra); result(s, ok, "matching", resp.join(","));
      retry(box, s, function () { R.matching(s, box); });
    };
    needAnswer(s);
  };

  R.sorting = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var ul = el("ol", "sortlist"), order = shuffle(s.items, s.id);
    if (order.every(function (x, i) { return x.id === s.items[i].id; })) order.reverse();
    function draw(moved) {
      ul.innerHTML = "";
      order.forEach(function (it, i) {
        var li = el("li", it.id === moved ? "moved" : "", '<span class="grip" aria-hidden="true">⠿</span><span class="pos">' + (i + 1) + '</span><span class="txt rich">' + html(it.text_html) + '</span><button class="mv" data-d="-1" aria-label="Move up"' + (i ? "" : " disabled") + '>↑</button><button class="mv" data-d="1" aria-label="Move down"' + (i < order.length - 1 ? "" : " disabled") + ">↓</button>");
        li.dataset.id = it.id; ul.appendChild(li);
      });
    }
    draw(); box.appendChild(st(ul, 2));
    box.appendChild(st(el("p", "note", "Drag the rows, or use the arrows."), 3));
    ul.addEventListener("click", function (e) {
      var b = e.target.closest(".mv"); if (!b || ul._done) return;
      var id = b.closest("li").dataset.id, i = order.findIndex(function (x) { return x.id === id; }), j = i + (+b.dataset.d);
      var t = order[i]; order[i] = order[j]; order[j] = t; draw(id);
      var nb = ul.querySelector('[data-id="' + id + '"] .mv[data-d="' + b.dataset.d + '"]'); (nb && !nb.disabled ? nb : ul.querySelector('[data-id="' + id + '"] .mv:not(:disabled)')).focus();
    });
    ul.addEventListener("pointerdown", function (e) {
      var li = e.target.closest("li"); if (!li || e.target.closest(".mv") || ul._done || e.button > 0) return;
      e.preventDefault(); li.classList.add("lift"); var y0 = e.clientY, id = li.dataset.id;
      function mv(ev) {
        li.style.transform = "translateY(" + (ev.clientY - y0) + "px)";
        var rows = [].slice.call(ul.children), i = order.findIndex(function (x) { return x.id === id; });
        rows.forEach(function (r, k) {
          if (r === li) return; var b = r.getBoundingClientRect(), mid = b.top + b.height / 2;
          if ((k > i && ev.clientY > mid) || (k < i && ev.clientY < mid)) {
            var it = order.splice(i, 1)[0]; order.splice(k, 0, it); y0 += (k > i ? 1 : -1) * (li.offsetHeight + 8);
            ul.insertBefore(li, k > i ? r.nextSibling : r); li.style.transform = "translateY(" + (ev.clientY - y0) + "px)";
          }
        });
      }
      function up() { D.removeEventListener("pointermove", mv); D.removeEventListener("pointerup", up); draw(id); }
      D.addEventListener("pointermove", mv); D.addEventListener("pointerup", up);
    });
    var a = el("div", "actions"), chk = checkBtn(); a.appendChild(chk); box.appendChild(st(a, 4));
    chk.onclick = function () {
      ul._done = true; var ok = order.every(function (x, i) { return x.id === s.items[i].id; });
      [].forEach.call(ul.children, function (li, i) { li.classList.add(order[i].id === s.items[i].id ? "ok" : "no"); li.querySelectorAll(".mv").forEach(function (b) { b.disabled = true; }); });
      var extra = ok || (s.feedback || {}).show_correct_answer === false ? "" : "<p><strong>Correct order:</strong></p><ol>" + s.items.map(function (i) { return "<li>" + html(i.text_html) + "</li>"; }).join("") + "</ol>";
      a.remove(); feedback(box, s, ok, extra); result(s, ok, "sequencing", order.map(function (x) { return x.id; }).join(","));
      retry(box, s, function () { R.sorting(s, box); });
    };
    needAnswer(s);
  };

  /* reveal widgets */
  function seenLine(box, n, of) { var p = box.querySelector(".seen-count") || box.appendChild(el("div", "seen-count")); p.innerHTML = "<b>" + n + "</b> of " + of + " opened"; }
  R.accordion = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var a = el("div", "acc"), seen = {};
    s.items.forEach(function (it, i) {
      var d = el("div", "acc-item", '<button class="acc-head" aria-expanded="false"><span class="n">' + (i + 1) + "</span><span>" + esc(it.title) + '</span><span class="chev">▾</span></button><div class="acc-body"><div><div class="rich">' + html(it.body_html) + "</div></div></div>");
      d.firstChild.onclick = function () {
        var open = !d.classList.contains("open");
        a.querySelectorAll(".acc-item.open").forEach(function (x) { x.classList.remove("open"); x.firstChild.setAttribute("aria-expanded", "false"); });
        d.classList.toggle("open", open); d.firstChild.setAttribute("aria-expanded", open);
        if (open) { d.classList.add("seen"); seen[i] = 1; seenLine(box, Object.keys(seen).length, s.items.length); }
      };
      a.appendChild(st(d, i + 2));
    });
    box.appendChild(a); seenLine(box, 0, s.items.length);
  };
  R.timeline = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var t = el("div", "tline");
    s.events.forEach(function (ev, i) {
      var d = el("div", "acc-item ev", '<button class="acc-head" aria-expanded="false"><span class="date">' + esc(ev.date) + "</span><span>" + esc(ev.title) + '</span><span class="chev">▾</span></button><div class="acc-body"><div><div class="rich" style="padding:0 16px 14px">' + html(ev.body_html) + "</div></div></div>");
      d.firstChild.onclick = function () { var o = !d.classList.contains("open"); d.classList.toggle("open", o); d.firstChild.setAttribute("aria-expanded", o); };
      t.appendChild(st(d, i + 2));
    });
    box.appendChild(t);
  };
  R.tabs = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var w = el("div", "tabs"), list = el("div", "tablist"), ink = el("span", "tab-ink"), panel = el("div", "tabpanel");
    list.setAttribute("role", "tablist"); list.appendChild(ink); panel.setAttribute("role", "tabpanel");
    var tabs = s.tabs.map(function (t, i) {
      var b = el("button", "tab", esc(t.label)); b.setAttribute("role", "tab");
      b.onclick = function () { pick(i); }; b.onkeydown = function (e) { if (e.key === "ArrowRight") { pick((i + 1) % tabs.length); tabs[(i + 1) % tabs.length].focus(); } if (e.key === "ArrowLeft") { var j = (i - 1 + tabs.length) % tabs.length; pick(j); tabs[j].focus(); } };
      list.appendChild(b); return b;
    });
    function pick(i) {
      tabs.forEach(function (b, j) { b.setAttribute("aria-selected", i === j); b.tabIndex = i === j ? 0 : -1; });
      tabs[i].classList.add("seen");
      ink.style.left = tabs[i].offsetLeft + "px"; ink.style.width = tabs[i].offsetWidth + "px";
      panel.innerHTML = ""; var p = rich(s.tabs[i].body_html); panel.appendChild(p);
      panel.style.animation = "none"; void panel.offsetWidth; panel.style.animation = "";
    }
    w.appendChild(list); w.appendChild(panel); box.appendChild(st(w, 2));
    requestAnimationFrame(function () { pick(0); });
  };
  R.flashcards = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var g = el("div", "cards"), seen = {};
    s.cards.forEach(function (c, i) {
      var b = el("button", "flip", '<div class="flip-in"><div class="face front rich">' + html(c.front_html) + '</div><div class="face back rich">' + html(c.back_html) + "</div></div>");
      b.type = "button"; b.setAttribute("aria-label", "Flashcard " + (i + 1) + ": " + b.querySelector(".front").textContent.trim() + ". Press to turn over.");
      b.onclick = function () { b.classList.toggle("on"); seen[i] = 1; seenLine(box, Object.keys(seen).length, s.cards.length); };
      g.appendChild(st(b, i + 2));
    });
    box.appendChild(g); seenLine(box, 0, s.cards.length);
  };

  /* pictures with markers */
  function place(img, items, getXY) {
    function go() { var w = img.naturalWidth, h = img.naturalHeight; items.forEach(function (it) { var p = getXY(it.d); it.e.style.left = p[0] / w * 100 + "%"; it.e.style.top = p[1] / h * 100 + "%"; if (p[2]) { it.e.style.width = p[2] / w * 100 + "%"; it.e.style.height = p[3] / h * 100 + "%"; } }); }
    fit(img, go);
  }
  R.hotspot = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var w = el("div", "explore"), pic = el("div", "pic", '<img src="' + src(s.image_asset_id) + '" alt="' + esc(s.image_alt || "") + '">'), panel = el("div", "panel", '<div class="ph">Select a marker on the picture to learn more.</div>');
    var dots = el("div", "found"), seen = {}, items = [];
    panel.setAttribute("aria-live", "polite");
    s.regions.forEach(function (r, i) {
      var m = el("button", "spot", '<span class="badge">' + (i + 1) + "</span>"); m.type = "button"; m.style.setProperty("--i", i);
      m.setAttribute("aria-label", (r.label_html || "").replace(/<[^>]+>/g, "") || "Point " + (i + 1));
      m.onclick = function () {
        pic.querySelectorAll(".spot").forEach(function (x) { x.classList.remove("active"); }); m.classList.add("active", "seen");
        panel.className = "panel"; void panel.offsetWidth; panel.className = "panel swap";
        panel.innerHTML = '<div class="pin-title rich">' + html(r.label_html) + '</div><div class="rich">' + html(r.feedback_html) + "</div>";
        seen[r.id] = 1; dots.children[i].classList.add("on");
        if (Object.keys(seen).length === s.regions.length && !box._all) {
          box._all = 1; if (s.feedback && s.feedback.correct_html) { var f = el("div", "feedback ok", '<div class="fh"><span class="fi">' + TICK + '</span>All found</div><div class="rich">' + html(s.feedback.correct_html) + "</div>"); box.appendChild(f); }
          result(s, true); gate(true);
        }
      };
      pic.appendChild(m); items.push({ e: m, d: r }); dots.appendChild(el("i"));
    });
    place(pic.querySelector("img"), items, function (r) { var c = r.coords; return r.shape === "circle" ? [c[0] - c[2], c[1] - c[2], c[2] * 2, c[2] * 2] : c; });
    var side = el("div"); side.appendChild(panel); side.appendChild(dots);
    w.appendChild(pic); w.appendChild(side); box.appendChild(st(w, 2));
    if (s.require_all && !S.r[s.id]) gate(false);
  };
  R.labeled_diagram = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var quiz = s.mode === "quiz";
    if (quiz && answered(s, box)) return;
    var w = el("div", "explore"), pic = el("div", "pic", '<img src="' + src(s.image_asset_id) + '" alt="' + esc(s.image_alt || "") + '">'), lg = el("ol", "legend"), items = [];
    var opts = shuffle(s.labels, s.id);
    s.labels.forEach(function (l, i) {
      var m = el("button", "marker", String(i + 1)); m.type = "button"; m.style.setProperty("--i", i);
      var li = el("li", "", '<span class="n">' + (i + 1) + "</span>" + (quiz ? '<select aria-label="Label for point ' + (i + 1) + '"><option value="">Choose…</option>' + opts.map(function (o) { return '<option value="' + o.id + '">' + esc(o.text) + "</option>"; }).join("") + "</select>" : "<span>" + esc(l.text) + "</span>"));
      li.dataset.id = l.id;
      function hl() { lg.querySelectorAll("li").forEach(function (x) { x.classList.toggle("active", x === li); }); pic.querySelectorAll(".marker").forEach(function (x) { x.classList.toggle("active", x === m); }); m.classList.add("seen"); }
      m.onclick = function () { hl(); var sel = li.querySelector("select"); if (sel) sel.focus(); li.scrollIntoView({ block: "nearest", behavior: RM ? "auto" : "smooth" }); };
      li.onmouseenter = hl; li.onclick = hl;
      pic.appendChild(m); items.push({ e: m, d: l }); lg.appendChild(st(li, i + 3));
    });
    place(pic.querySelector("img"), items, function (l) { return [l.x, l.y]; });
    w.appendChild(pic); w.appendChild(lg); box.appendChild(st(w, 2));
    if (quiz) {
      var a = el("div", "actions"), chk = checkBtn(); a.appendChild(chk); box.appendChild(st(a, 4));
      chk.onclick = function () {
        var ok = true, resp = [];
        lg.querySelectorAll("li").forEach(function (li) { var sel = li.querySelector("select"), hit = sel.value === li.dataset.id; sel.disabled = true; li.classList.add(hit ? "correct" : "wrong"); if (!hit) ok = false; resp.push(li.dataset.id + "." + (sel.value || "none")); });
        a.remove(); feedback(box, s, ok); result(s, ok, "matching", resp.join(","));
      };
      needAnswer(s);
    }
  };

  R.simulation = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var w = el("div"), i = 0, misses = 0; box.appendChild(st(w, 2));
    function step() {
      var p = s.steps[i]; w.innerHTML = "";
      var hd = el("div", "sim-head", '<span class="chip">Step ' + (i + 1) + " of " + s.steps.length + '</span><span class="steps-dots">' + s.steps.map(function (x, k) { return '<i class="' + (k < i ? "on" : k === i ? "cur" : "") + '"></i>'; }).join("") + "</span>");
      var ins = el("div", "sim-instr rich", html(p.instruction_html));
      var pic = el("div", "pic", '<img src="' + src(p.image_asset_id) + '" alt="' + esc(p.image_alt || "") + '">'), hint = el("div", "sim-hint rich");
      hint.hidden = true; hint.innerHTML = html(p.hint_html);
      var node = el("div", "scen-node"); node.appendChild(hd); node.appendChild(ins); node.appendChild(el("div", "", "")).style.height = "10px"; node.appendChild(pic); node.appendChild(hint); w.appendChild(node);
      if (p.regions && p.regions.length) {
        var items = [];
        p.regions.forEach(function (r) {
          var b = el("button", "region"); b.type = "button"; b.setAttribute("aria-label", (r.label_html || "").replace(/<[^>]+>/g, ""));
          b.onclick = function () {
            if (r.correct) { b.classList.add("hit"); setTimeout(adv, RM ? 0 : 450); }
            else { misses++; b.classList.remove("miss"); void b.offsetWidth; b.classList.add("miss"); hint.hidden = false; }
          };
          pic.appendChild(b); items.push({ e: b, d: r });
        });
        pic.addEventListener("click", function (e) { if (e.target.tagName === "IMG") { misses++; hint.hidden = false; } });
        place(pic.querySelector("img"), items, function (r) { return r.coords; });
        items.forEach(function (it) { it.e.style.transform = "none"; });
      } else {
        var f = el("div", "sim-input", '<input class="field" aria-label="' + esc(p.input_label || "Type here") + '" placeholder="' + esc(p.input_label || "") + '" autocomplete="off"><button class="btn btn-primary" type="button">Enter</button>');
        node.appendChild(f); var inp = f.querySelector("input");
        function sub() { var hit = (p.input_accepted || []).some(function (v) { return norm(v) === norm(inp.value); }); if (hit) { inp.classList.add("ok"); setTimeout(adv, RM ? 0 : 350); } else { misses++; inp.classList.remove("no"); void inp.offsetWidth; inp.classList.add("no"); hint.hidden = false; } }
        f.querySelector("button").onclick = sub; inp.addEventListener("keydown", function (e) { if (e.key === "Enter") sub(); });
        setTimeout(function () { inp.focus(); }, 300);
      }
    }
    function adv() {
      i++; if (i < s.steps.length) return step();
      w.innerHTML = ""; feedback(box, s, true, misses ? '<p class="note">' + misses + " extra click" + (misses > 1 ? "s" : "") + " on the way. In the real system, take your time.</p>" : "");
      result(s, true, "performance", "steps:" + s.steps.length + ";misses:" + misses);
    }
    step(); needAnswer(s);
  };

  R.decision_scenario = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    var sc = el("div", "scen"), score = 0, path = []; box.appendChild(st(rich(s.intro_html), 1)); box.appendChild(st(sc, 2));
    var nodes = {}; s.nodes.forEach(function (n) { nodes[n.id] = n; });
    function show(id) {
      var n = nodes[id]; sc.innerHTML = "";
      var nd = el("div", "scen-node"), k = s.nodes.indexOf(n) + 1;
      var im = n.image_asset_id && src(n.image_asset_id);
      if (im) nd.classList.add("has-img");
      nd.innerHTML = (im ? '<div class="scen-img"><img src="' + im + '" alt="' + esc(n.image_alt || "") + '"></div>' : "") + '<div class="scen-main"><div class="scen-top" style="margin-bottom:12px"><span class="chip">Decision ' + k + " of " + s.nodes.length + '</span></div><div class="rich prompt">' + html(n.prompt_html) + "</div></div>";
      var main = nd.querySelector(".scen-main");
      var g = el("div", "options"), btns = [];
      n.choices.forEach(function (c, i) {
        var b = el("button", "opt", '<span class="mark">' + String.fromCharCode(65 + i) + '</span><span><span class="rich">' + html(c.text_html) + "</span></span>"); b.type = "button";
        b.onclick = function () {
          score += c.score_delta || 0; path.push(n.id + "." + c.id);
          btns.forEach(function (x) { x.disabled = true; if (x !== b) x.classList.add("dim"); });
          b.classList.add((c.score_delta || 0) > 0 ? "correct" : "wrong"); b.querySelector(".mark").innerHTML = (c.score_delta || 0) > 0 ? TICK : "!";
          var f = el("div", "feedback " + ((c.score_delta || 0) > 0 ? "ok" : "no"), '<div class="rich">' + html(c.feedback_html) + "</div>");
          var a = el("div", "actions"), nx = el("button", "btn btn-primary", nodes[c.goto_node_id] ? "Continue →" : "See the outcome →"); nx.type = "button";
          nx.onclick = function () { if (nodes[c.goto_node_id]) show(c.goto_node_id); else end(); };
          a.appendChild(nx); f.appendChild(a); main.appendChild(f); setTimeout(function () { nx.focus({ preventScroll: true }); f.scrollIntoView({ behavior: RM ? "auto" : "smooth", block: "nearest" }); }, 150);
        };
        btns.push(b); g.appendChild(st(b, i + 1));
      });
      main.appendChild(g); sc.appendChild(nd);
    }
    function end() {
      var ok = s.pass_score != null ? score >= s.pass_score : score > 0; sc.innerHTML = "";
      feedback(box, s, ok, '<p class="note">Good decisions: <strong>' + score + "</strong>" + (s.pass_score != null ? " (needed " + s.pass_score + ")" : "") + "</p>");
      result(s, ok, "performance", path.join(","));
    }
    show(s.start_node_id || s.nodes[0].id); needAnswer(s);
  };

  R.game = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    var mech = s.mechanics || {}, sc = 0, lives = mech.lives ? mech.lives.start : null, hints = (mech.hints && mech.hints.hints) || [], hi = 0, path = [];
    box.appendChild(st(rich(s.intro_html), 1));
    var top = el("div", "scen-top"), g = el("div", "scen"); box.appendChild(st(top, 2)); box.appendChild(st(g, 3));
    var nodes = {}; s.nodes.forEach(function (n) { nodes[n.id] = n; });
    function bar() {
      top.innerHTML = '<span class="chip">Score <b style="margin-left:4px">' + sc + "</b></span>" + (lives != null ? '<span class="chip">Lives <span class="lives" style="margin-left:6px">' + new Array(mech.lives.start + 1).join("x").split("").map(function (x, i) { return '<i class="' + (i >= lives ? "lost" : "") + '"></i>'; }).join("") + "</span></span>" : "") +
        (hi < hints.length ? '<button class="btn btn-ghost" type="button" style="padding:6px 14px" id="hintB">💡 Hint</button>' : "");
      var hb = top.querySelector("#hintB"); if (hb) hb.onclick = function () { g.querySelector(".scen-main").appendChild(el("div", "hintbox", "<strong>Hint:</strong> " + esc(hints[hi++].text))); bar(); };
    }
    function show(id) {
      var n = nodes[id]; g.innerHTML = ""; bar();
      var im = n.image_asset_id && src(n.image_asset_id);
      var nd = el("div", "scen-node" + (im ? " has-img" : ""), (im ? '<div class="scen-img"><img src="' + im + '" alt="' + esc(n.image_alt || "") + '"></div>' : "") + '<div class="scen-main"><div class="rich prompt">' + html(n.content_html) + "</div></div>");
      var main = nd.querySelector(".scen-main");
      var o = el("div", "options"), btns = [];
      n.choices.forEach(function (c, i) {
        var good = (c.on_choose || []).some(function (a) { return a.do === "score.correct"; });
        var b = el("button", "opt", '<span class="mark">' + String.fromCharCode(65 + i) + '</span><span class="rich">' + html(c.text_html) + "</span>"); b.type = "button";
        b.onclick = function () {
          (c.on_choose || []).forEach(function (a) { if (a.do === "score.correct") sc += a.points || 1; if (a.do === "lives.lose" && lives != null) lives = Math.max(0, lives - (a.n || 1)); });
          path.push(n.id + "." + c.id); bar();
          btns.forEach(function (x) { x.disabled = true; if (x !== b) x.classList.add("dim"); });
          b.classList.add(good ? "correct" : "wrong"); b.querySelector(".mark").innerHTML = good ? TICK : "!";
          var f = el("div", "feedback " + (good ? "ok" : "no"), '<div class="rich">' + html(c.feedback_html || "") + "</div>");
          var over = lives === 0, nxt = !over && nodes[c.to];
          var a = el("div", "actions"), nx = el("button", "btn btn-primary", nxt ? "Next →" : "See how you did →"); nx.type = "button";
          nx.onclick = function () { if (nxt) show(c.to); else end(); };
          a.appendChild(nx); f.appendChild(a); main.appendChild(f); setTimeout(function () { nx.focus({ preventScroll: true }); f.scrollIntoView({ behavior: RM ? "auto" : "smooth", block: "nearest" }); }, 150);
        };
        btns.push(b); o.appendChild(st(b, i + 1));
      });
      main.appendChild(o); g.appendChild(nd);
    }
    function end() {
      var ok = lives !== 0 && (s.pass_score != null ? sc >= s.pass_score : sc > 0); g.innerHTML = ""; top.innerHTML = "";
      feedback(box, s, ok, '<p class="note">Score <strong>' + sc + "</strong>" + (lives != null ? " · lives left " + lives : "") + "</p>");
      result(s, ok, "performance", path.join(","));
    }
    show(s.start_node_id || s.nodes[0].id); needAnswer(s);
  };

  R.escape_room = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    var lives = s.lives || 3, i = 0; box.appendChild(st(rich(s.intro_html), 1));
    var top = el("div", "scen-top"), g = el("div"); box.appendChild(st(top, 2)); box.appendChild(st(g, 3));
    function bar() { top.innerHTML = '<span class="chip">Lock ' + Math.min(i + 1, s.puzzles.length) + " of " + s.puzzles.length + '</span><span class="chip">Lives <span class="lives" style="margin-left:6px">' + new Array((s.lives || 3) + 1).join("x").split("").map(function (x, k) { return '<i class="' + (k >= lives ? "lost" : "") + '"></i>'; }).join("") + "</span></span>"; }
    function show() {
      var p = s.puzzles[i]; bar(); g.innerHTML = "";
      var nd = el("div", "scen-node card", '<div class="rich prompt">' + html(p.prompt_html) + '</div><div class="sim-input"><input class="field" aria-label="Your answer" autocomplete="off"><button class="btn btn-primary" type="button">Unlock</button></div>');
      g.appendChild(nd); var inp = nd.querySelector("input"); setTimeout(function () { inp.focus({ preventScroll: true }); }, 300);
      function sub() {
        if (!inp.value.trim()) return;
        if (p.accepted.some(function (v) { return norm(v) === norm(inp.value); })) { inp.classList.add("ok"); toast("🔓 Lock " + (i + 1) + " open"); i++; setTimeout(function () { i < s.puzzles.length ? show() : end(true); }, RM ? 0 : 450); }
        else { lives--; bar(); inp.classList.remove("no"); void inp.offsetWidth; inp.classList.add("no"); if (!nd.querySelector(".hintbox") && p.hint_html) nd.appendChild(el("div", "hintbox rich", html(p.hint_html))); if (lives <= 0) end(false); }
      }
      nd.querySelector("button").onclick = sub; inp.addEventListener("keydown", function (e) { if (e.key === "Enter") sub(); });
    }
    function end(win) { g.innerHTML = ""; top.innerHTML = ""; feedback(box, s, win); result(s, win, "performance", "solved:" + i + "/" + s.puzzles.length); }
    show(); needAnswer(s);
  };

  R.adaptive_practice = function (s, box) {
    head(s, box); if (answered(s, box)) return;
    box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var pool = s.items.slice().sort(function (a, b) { return (a.difficulty || 0) - (b.difficulty || 0); });
    var max = Math.min(s.max_items || pool.length, pool.length), n = 0, right = 0, streak = 0, top = el("div", "scen-top"), g = el("div");
    box.appendChild(st(top, 2)); box.appendChild(st(g, 3));
    function show() {
      var it = pool.shift(); n++;
      top.innerHTML = '<span class="chip">Question ' + n + " of up to " + max + '</span><span class="chip">' + right + " right</span>";
      g.innerHTML = ""; var nd = el("div", "scen-node", '<div class="rich prompt">' + html(it.prompt_html) + "</div>"), o = el("div", "options"), btns = [];
      it.options.forEach(function (op, k) {
        var b = el("button", "opt", '<span class="mark">' + String.fromCharCode(65 + k) + '</span><span class="rich">' + html(op.text_html) + "</span>"); b.type = "button";
        b.onclick = function () {
          var ok = !!op.correct; if (ok) { right++; streak++; } else streak = 0;
          btns.forEach(function (x, j) { x.disabled = true; if (it.options[j].correct) { x.classList.add("correct"); x.querySelector(".mark").innerHTML = TICK; } else if (x === b) x.classList.add("wrong"); else x.classList.add("dim"); });
          var f = el("div", "feedback " + (ok ? "ok" : "no"), '<div class="rich">' + html(ok ? it.explain_html : (it.scaffold_html || "") + (it.explain_html || "")) + "</div>");
          var stop = n >= max || !pool.length || (streak >= 3 && right / n >= (s.target_success || .7));
          var a = el("div", "actions"), nx = el("button", "btn btn-primary", stop ? "Finish practice →" : "Next question →"); nx.type = "button";
          nx.onclick = function () { stop ? end() : show(); }; a.appendChild(nx); f.appendChild(a); nd.appendChild(f);
          setTimeout(function () { nx.focus({ preventScroll: true }); }, 150);
        };
        btns.push(b); o.appendChild(st(b, k + 1));
      });
      nd.appendChild(o); g.appendChild(nd);
    }
    function end() { var ok = right / n >= (s.pass_ratio || .6); g.innerHTML = ""; top.innerHTML = ""; feedback(box, s, ok, '<p class="note">' + right + " of " + n + " right.</p>"); result(s, ok, "performance", right + "/" + n); }
    show(); needAnswer(s);
  };

  R.poll = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var g = el("div", "options"), btns = [], key = "poll_" + s.id;
    s.options.forEach(function (o, i) {
      var b = el("button", "opt" + (s.multi ? " multi" : ""), '<span class="mark">' + (i + 1) + '</span><span class="rich">' + html(o.text_html) + "</span>"); b.type = "button"; b.setAttribute("aria-pressed", S.f[key] && S.f[key].indexOf(o.id) >= 0 ? "true" : "false");
      b.onclick = function () { if (!s.multi) btns.forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") === "true" ? "false" : "true"); sub.disabled = false; };
      btns.push(b); g.appendChild(st(b, i + 2));
    });
    box.appendChild(g);
    var a = el("div", "actions"), sub = checkBtn("Submit"); sub.disabled = !S.f[key]; a.appendChild(sub); box.appendChild(st(a, 9));
    sub.onclick = function () {
      S.f[key] = btns.filter(function (x) { return x.getAttribute("aria-pressed") === "true"; }).map(function (x, i) { return s.options[btns.indexOf(x)].id; });
      a.remove(); var f = el("div", "feedback ok", '<div class="fh"><span class="fi">' + TICK + '</span>Thanks</div><div class="rich">' + html(s.reflection_html || "") + "</div>"); box.appendChild(f); save();
    };
  };
  R.exploration = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var key = s.store_key, v = S.f[key];
    if (s.input_kind === "slider") {
      var mid = v != null ? v : Math.round(((s.min_value || 0) + (s.max_value || 10)) / 2);
      var c = el("div", "card", '<div class="range-val" aria-hidden="true">' + mid + '</div><input type="range" class="range" min="' + (s.min_value || 0) + '" max="' + (s.max_value || 10) + '" step="' + (s.step || 1) + '" value="' + mid + '" aria-label="Your estimate"><div style="display:flex;justify-content:space-between" class="note"><span>' + (s.min_value || 0) + "</span><span>" + (s.max_value || 10) + "</span></div>");
      var r = c.querySelector("input"), out = c.querySelector(".range-val");
      r.oninput = function () { out.textContent = r.value; bump(out); S.f[key] = +r.value; }; r.onchange = function () { save(); };
      box.appendChild(st(c, 2));
    } else if (s.choices && s.choices.length) {
      var g = el("div", "options");
      s.choices.forEach(function (ch, i) {
        var t = typeof ch === "string" ? ch : (ch.text_html || ch.label || ch.text || "");
        var b = el("button", "opt", '<span class="mark">' + String.fromCharCode(65 + i) + '</span><span class="rich">' + html(t) + "</span>"); b.type = "button";
        b.setAttribute("aria-pressed", v === t.replace(/<[^>]+>/g, "") ? "true" : "false");
        b.onclick = function () { g.querySelectorAll(".opt").forEach(function (x) { x.setAttribute("aria-pressed", "false"); }); b.setAttribute("aria-pressed", "true"); S.f[key] = t.replace(/<[^>]+>/g, "").slice(0, 200); save(); };
        g.appendChild(st(b, i + 2));
      });
      box.appendChild(g);
    } else {
      var ta = el("textarea", "field"); ta.value = v || ""; ta.setAttribute("aria-label", "Your answer"); ta.oninput = function () { S.f[key] = ta.value.slice(0, 200); }; ta.onchange = function () { save(); };
      box.appendChild(st(ta, 2));
    }
    box.appendChild(st(el("p", "note", "Not scored. We'll come back to your answer later."), 4));
  };
  R.worked_example = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.intro_html, "prompt"), 1));
    var list = el("div", "we-steps"), n = 0; box.appendChild(st(list, 2));
    var a = el("div", "actions"), more = el("button", "btn btn-mod", "Show the first step"); more.type = "button"; a.appendChild(more); box.appendChild(st(a, 3));
    function add() {
      var p = s.steps[n++], d = el("div", "we-step", '<div class="rich">' + html(p.action_html) + "</div>" + (p.artifact_asset_id && src(p.artifact_asset_id) ? '<div class="figure" style="margin-top:10px"><img src="' + src(p.artifact_asset_id) + '" alt="' + esc(p.artifact_caption || "") + '"></div>' : ""));
      if (p.rationale_html) {
        if (s.fading === "partial" && n > 1) { var w = el("button", "linkbtn", "Why? ▸"); w.type = "button"; w.onclick = function () { w.replaceWith(el("div", "we-why rich", html(p.rationale_html))); }; d.appendChild(w); }
        else d.appendChild(el("div", "we-why rich", html(p.rationale_html)));
      }
      list.appendChild(d);
      if (n >= s.steps.length) {
        a.remove();
        if (s.self_explanation_prompt_html) { var c = el("div", "card", '<div class="rich">' + html(s.self_explanation_prompt_html) + "</div>"); var ta = el("textarea", "field"); ta.setAttribute("aria-label", "Your explanation"); c.appendChild(ta); box.appendChild(st(c, 1)); }
      } else more.textContent = "Next step (" + (n + 1) + " of " + s.steps.length + ")";
    }
    more.onclick = add;
  };
  R.image_compare = function (s, box) {
    head(s, box); box.appendChild(st(rich(s.prompt_html, "prompt"), 1));
    var c = el("div", "compare", '<img src="' + src(s.before_asset_id) + '" alt="' + esc(s.before_label) + '"><div class="after"><img src="' + src(s.after_asset_id) + '" alt="' + esc(s.after_label) + '"></div><div class="handle"></div><span class="lab l">' + esc(s.before_label) + '</span><span class="lab r">' + esc(s.after_label) + '</span><input type="range" min="0" max="100" value="50" aria-label="Compare the two pictures">');
    var r = c.querySelector("input"); r.oninput = function () { c.style.setProperty("--x", r.value + "%"); };
    box.appendChild(st(c, 2));
    if (s.caption) box.appendChild(st(el("p", "note", html(s.caption)), 3));
    if (!RM) { var t = 0, iv = setInterval(function () { t += .04; var x = 50 + Math.sin(t * 3) * 18 * Math.max(0, 1 - t); c.style.setProperty("--x", x + "%"); if (t >= 1) { clearInterval(iv); c.style.setProperty("--x", "50%"); } }, 30); }
  };
  R.video = function (s, box) { head(s, box); box.appendChild(st(el("div", "figure", '<video controls preload="metadata" src="' + src(s.video_asset_id) + '"></video>'), 1)); };

  /* ------------------------------------------------------------------ start */
  D.documentElement.style.setProperty("--mod", C.colour);
  if (C.colour_ink) D.documentElement.style.setProperty("--mod-ink", C.colour_ink);
  shell(); hud(); lastRank = rank();
  var start = S.c && BY[S.c] && visible(BY[S.c]) ? S.c : SCREENS.filter(visible)[0].id;
  go(start, 1);
  function leave() {
    LMS.set("cmi.core.session_time", ts(Date.now() - t0));
    var st = LMS.get("cmi.core.lesson_status");
    LMS.set("cmi.core.exit", st === "passed" || st === "failed" ? "" : "suspend");
    save(true); LMS.finish();
  }
  window.addEventListener("pagehide", leave);
  window.addEventListener("beforeunload", leave);
  window.__mc = { go: go, state: S, score: score };   // used by the automated checks
})();
