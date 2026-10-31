/* 2048 tarayıcı demosu (nrazon.github.io). Uygulamadaki (Game2048/.../game/Game.kt) kuralların karşılığı: 4x4, satır başına her taş en fazla
   bir kez birleşir, yeni taş %90 "2" / %10 "4", 2048'de "devam et", hamle kalmayınca oyun biter, 1 adım geri alma.
   Kullanım: <div data-g2048 data-play="<Play adresi>"></div>  (g2048.js yüklenince kendiliğinden kurulur). Testler: tools/g2048.test.js */
(function () {
  "use strict";

  var SIZE = 4, WIN = 2048;

  // ------------------------------------------------------------ oyun mantığı (DOM'dan bağımsız)
  /** Hareket yönünde [satır, sütun] hücre sırası (line = satır ya da sütun numarası). */
  function cellsFor(dir, line) {
    var out = [];
    for (var i = 0; i < SIZE; i++) {
      out.push(dir === "left" ? [line, i] : dir === "right" ? [line, SIZE - 1 - i] : dir === "up" ? [i, line] : [SIZE - 1 - i, line]);
    }
    return out;
  }
  function at(tiles, r, c) { for (var i = 0; i < tiles.length; i++) if (tiles[i].r === r && tiles[i].c === c) return tiles[i]; return null; }

  /** Kaydırma ve birleştirme (yeni taş yok). Birleşen iki taş "ghost" olarak hedefe kayar; yerine yeni kimlikli taş doğar. */
  function slide(tiles, dir, nextId) {
    var result = [], ghosts = [], merged = [], gained = 0, moved = false;
    for (var line = 0; line < SIZE; line++) {
      var cells = cellsFor(dir, line), lt = [];
      for (var k = 0; k < SIZE; k++) { var t0 = at(tiles, cells[k][0], cells[k][1]); if (t0) lt.push(t0); }
      var target = 0, i = 0;
      while (i < lt.length) {
        var tc = cells[target], a = lt[i], b = lt[i + 1];
        if (b && a.v === b.v) {
          var nt = { id: nextId++, v: a.v * 2, r: tc[0], c: tc[1] };
          result.push(nt); merged.push(nt.id);
          ghosts.push({ id: a.id, v: a.v, r: tc[0], c: tc[1] }, { id: b.id, v: b.v, r: tc[0], c: tc[1] });
          gained += nt.v; moved = true; i += 2;
        } else {
          if (a.r !== tc[0] || a.c !== tc[1]) moved = true;
          result.push({ id: a.id, v: a.v, r: tc[0], c: tc[1] });
          i += 1;
        }
        target++;
      }
    }
    return { tiles: result, ghosts: ghosts, merged: merged, gained: gained, moved: moved, nextId: nextId };
  }

  function canMove(tiles) {
    if (tiles.length < SIZE * SIZE) return true;
    for (var i = 0; i < tiles.length; i++) {
      var t = tiles[i], right = at(tiles, t.r, t.c + 1), down = at(tiles, t.r + 1, t.c);
      if ((right && right.v === t.v) || (down && down.v === t.v)) return true;
    }
    return false;
  }

  /** Boş bir hücreye %90 2, %10 4 koyar. */
  function spawn(tiles, nextId, rnd) {
    var empty = [];
    for (var r = 0; r < SIZE; r++) for (var c = 0; c < SIZE; c++) if (!at(tiles, r, c)) empty.push([r, c]);
    if (!empty.length) return { tiles: tiles, nextId: nextId, spawned: null };
    var cell = empty[Math.floor(rnd() * empty.length)];
    var t = { id: nextId, v: rnd() < 0.1 ? 4 : 2, r: cell[0], c: cell[1] };
    return { tiles: tiles.concat([t]), nextId: nextId + 1, spawned: t.id };
  }

  function newGame(rnd) {
    var s = { tiles: [], nextId: 1, score: 0, status: "playing", keep: false, moves: 0 };
    for (var i = 0; i < 2; i++) { var sp = spawn(s.tiles, s.nextId, rnd); s.tiles = sp.tiles; s.nextId = sp.nextId; }
    return s;
  }

  /** Hamle: değişmezse null. status: playing | won (2048 ilk kez, devam et denene kadar hamle yok) | over. */
  function move(state, dir, rnd) {
    if (state.status !== "playing") return null;
    var sl = slide(state.tiles, dir, state.nextId);
    if (!sl.moved) return null;
    var sp = spawn(sl.tiles, sl.nextId, rnd);
    var reached = !state.keep && sl.merged.some(function (id) { return sp.tiles.some(function (t) { return t.id === id && t.v >= WIN; }); });
    var status = reached ? "won" : !canMove(sp.tiles) ? "over" : "playing";
    return {
      state: { tiles: sp.tiles, nextId: sp.nextId, score: state.score + sl.gained, status: status, keep: state.keep, moves: state.moves + 1 },
      ghosts: sl.ghosts, merged: sl.merged, spawned: sp.spawned, gained: sl.gained
    };
  }

  var api = { SIZE: SIZE, slide: slide, canMove: canMove, spawn: spawn, move: move, newGame: newGame, at: at };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; return; }
  if (typeof document === "undefined") return;

  // ------------------------------------------------------------ arayüz
  var D = {
    tr: { score: "Skor", best: "Rekor", again: "Yeni oyun", undo: "Geri al", hint: "Ok tuşları ya da kaydırma ile oyna; aynı sayıları birleştir.",
      over: "Oyun bitti", won: "2048'e ulaştın!", keep: "Devam et", cta: "Beğendin mi? Uygulamayı indir", up: "Yukarı", down: "Aşağı", left: "Sol", right: "Sağ",
      board: "2048 tahtası" },
    en: { score: "Score", best: "Best", again: "New game", undo: "Undo", hint: "Use the arrow keys or swipe; merge matching numbers.",
      over: "Game over", won: "You reached 2048!", keep: "Keep going", cta: "Like it? Get the app", up: "Up", down: "Down", left: "Left", right: "Right",
      board: "2048 board" },
    es: { score: "Puntos", best: "Récord", again: "Nueva partida", undo: "Deshacer", hint: "Usa las flechas o desliza; une los números iguales.",
      over: "Fin de la partida", won: "¡Llegaste a 2048!", keep: "Seguir jugando", cta: "¿Te gustó? Descarga la app", up: "Arriba", down: "Abajo", left: "Izquierda", right: "Derecha",
      board: "Tablero de 2048" },
    pt: { score: "Pontos", best: "Recorde", again: "Novo jogo", undo: "Desfazer", hint: "Use as setas ou deslize; junte os números iguais.",
      over: "Fim de jogo", won: "Você chegou a 2048!", keep: "Continuar", cta: "Gostou? Baixe o app", up: "Cima", down: "Baixo", left: "Esquerda", right: "Direita",
      board: "Tabuleiro do 2048" }
  };
  function lang() {
    var h = document.documentElement;
    var l = (h.getAttribute("data-lang") || h.lang || "en").slice(0, 2);
    return D[l] ? l : "en";
  }

  var COLORS = { 2: "#EEE4DA", 4: "#EDE0C8", 8: "#F2B179", 16: "#F59563", 32: "#F67C5F", 64: "#F65E3B", 128: "#EDCF72", 256: "#EDCC61", 512: "#EDC850", 1024: "#EDC53F", 2048: "#EDC22E" };

  var CSS = ".g48{--b-board:#BBADA0;--b-cell:#CDC1B4;--b-text:#776E65;--b-dim:#9A8F84;--b-btn:#8F7A66;--g:8px;color:var(--b-text);font:16px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}" +
    "@media (prefers-color-scheme:dark){.g48{--b-board:#3B3631;--b-cell:#4D4740;--b-text:#EDE4DA;--b-dim:#B3A99F}}" +
    ".g48 *{box-sizing:border-box}.g48-box{display:flex;flex-wrap:wrap;gap:20px 28px;align-items:center;justify-content:center}" +
    ".g48-main{flex:0 1 330px;width:100%;max-width:330px}.g48-side{flex:1 1 200px;max-width:320px;display:flex;flex-direction:column;gap:12px}" +
    ".g48-board{position:relative;background:var(--b-board);border-radius:14px;padding:var(--g);touch-action:none;outline-offset:3px;user-select:none}" +
    ".g48-inner{position:relative;width:100%;aspect-ratio:1}" +
    ".g48-grid{position:absolute;inset:0;display:grid;grid-template-columns:repeat(4,1fr);grid-template-rows:repeat(4,1fr);gap:var(--g)}" +
    ".g48-grid i{background:var(--b-cell);border-radius:8px;opacity:.7}" +
    ".g48-tile{position:absolute;width:calc((100% - 3 * var(--g)) / 4);height:calc((100% - 3 * var(--g)) / 4);left:calc(var(--c) * ((100% - 3 * var(--g)) / 4 + var(--g)));top:calc(var(--r) * ((100% - 3 * var(--g)) / 4 + var(--g)));" +
    "display:flex;align-items:center;justify-content:center;border-radius:8px;font-weight:800;font-size:clamp(22px,7vw,34px);color:#776E65;background:#3C3A32;transition:left .11s ease,top .11s ease}" +
    ".g48-tile.big{font-size:clamp(18px,5.6vw,28px)}.g48-tile.huge{font-size:clamp(14px,4.4vw,22px)}" +
    ".g48-tile.dark{color:#F9F6F2}.g48-tile.pop{animation:g48-pop .16s .11s ease-out backwards}.g48-tile.merge{animation:g48-merge .2s .1s ease-out backwards}" +
    "@keyframes g48-pop{from{transform:scale(0)}to{transform:none}}@keyframes g48-merge{0%{transform:scale(.6)}60%{transform:scale(1.15)}100%{transform:none}}" +
    "@media (prefers-reduced-motion:reduce){.g48-tile{transition:none}.g48-tile.pop,.g48-tile.merge{animation:none}}" +
    ".g48-over{position:absolute;inset:0;border-radius:14px;background:color-mix(in srgb,var(--b-board) 82%,transparent);display:flex;flex-direction:column;gap:12px;align-items:center;justify-content:center;font-weight:800;font-size:24px;text-align:center;padding:12px;color:var(--b-text)}" +
    ".g48-over[hidden]{display:none}" +
    ".g48-stats{display:flex;gap:8px}.g48-stats div{flex:1;background:var(--b-board);border-radius:10px;padding:8px 6px;text-align:center;color:#F9F6F2}" +
    ".g48-stats span{display:block;font-size:11px;letter-spacing:.06em;text-transform:uppercase;opacity:.85}.g48-stats b{font-size:22px;line-height:1.15}" +
    ".g48-row{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}" +
    ".g48-btn{border:0;background:var(--b-btn);color:#F9F6F2;font:inherit;font-weight:800;font-size:14px;padding:9px 16px;border-radius:8px;cursor:pointer}" +
    ".g48-btn:disabled{opacity:.45;cursor:default}" +
    ".g48-pad{display:grid;grid-template-columns:repeat(3,44px);grid-template-rows:repeat(2,40px);gap:6px;justify-content:start}" +
    ".g48-pad button{border:0;border-radius:8px;background:var(--b-board);color:#F9F6F2;font-size:16px;cursor:pointer}" +
    ".g48-pad .u{grid-column:2;grid-row:1}.g48-pad .l{grid-column:1;grid-row:2}.g48-pad .d{grid-column:2;grid-row:2}.g48-pad .r{grid-column:3;grid-row:2}" +
    ".g48-hint{margin:0;font-size:13px;color:var(--b-dim)}.g48 a.g48-cta{font-weight:800;font-size:14px;color:inherit}" +
    ".g48 button:focus-visible,.g48 a:focus-visible,.g48-board:focus-visible{outline:3px solid #EDC22E}";

  function store(key, val) {
    try { if (val === undefined) return JSON.parse(localStorage.getItem(key) || "null"); localStorage.setItem(key, JSON.stringify(val)); } catch (e) { return null; }
  }
  function track(name, params) { try { if (typeof window.gtag === "function") window.gtag("event", name, params); } catch (e) {} }
  var ARROWS = { ArrowUp: "up", ArrowDown: "down", ArrowLeft: "left", ArrowRight: "right", w: "up", s: "down", a: "left", d: "right", W: "up", S: "down", A: "left", D: "right" };

  function mount(root) {
    if (root.__g48) return;
    root.__g48 = true;
    if (!document.getElementById("g48-css")) { var st = document.createElement("style"); st.id = "g48-css"; st.textContent = CSS; document.head.appendChild(st); }
    root.classList.add("g48");
    root.innerHTML = '<div class="g48-box"><div class="g48-main"><div class="g48-board" tabindex="0" role="application"><div class="g48-inner"><div class="g48-grid">' +
      "<i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i></div></div>" +
      '<div class="g48-over" hidden><div class="g48-msg"></div><div class="g48-row" style="justify-content:center"><button type="button" class="g48-btn" data-act="keep"></button><button type="button" class="g48-btn" data-act="again2"></button></div></div></div></div>' +
      '<div class="g48-side"><div class="g48-stats"><div><span data-g="score"></span><b class="g48-score">0</b></div><div><span data-g="best"></span><b class="g48-best">0</b></div></div>' +
      '<div class="g48-row"><button type="button" class="g48-btn" data-act="again"></button><button type="button" class="g48-btn" data-act="undo"></button></div>' +
      '<div class="g48-pad"><button type="button" class="u" data-dir="up">▲</button><button type="button" class="l" data-dir="left">◀</button><button type="button" class="d" data-dir="down">▼</button><button type="button" class="r" data-dir="right">▶</button></div>' +
      '<p class="g48-hint"></p>' + (root.getAttribute("data-play") ? '<a class="g48-cta" href="' + root.getAttribute("data-play") + '"></a>' : "") + "</div></div>";

    var q = function (s) { return root.querySelector(s); };
    var board = q(".g48-board"), inner = q(".g48-inner"), over = q(".g48-over"), msg = q(".g48-msg"), scoreEl = q(".g48-score"), bestEl = q(".g48-best");
    var undoBtn = q("[data-act=undo]"), keepBtn = q("[data-act=keep]"), again2 = q("[data-act=again2]");
    var rnd = Math.random, state, prev = null, best = store("g2048_best") || 0, els = {}, started = false;

    function labels() {
      var t = D[lang()];
      [].forEach.call(root.querySelectorAll("[data-g]"), function (e) { e.textContent = t[e.getAttribute("data-g")]; });
      q("[data-act=again]").textContent = t.again; again2.textContent = t.again; undoBtn.textContent = t.undo; keepBtn.textContent = t.keep;
      q(".g48-hint").textContent = t.hint; board.setAttribute("aria-label", t.board);
      [].forEach.call(root.querySelectorAll("[data-dir]"), function (b) { b.setAttribute("aria-label", t[b.getAttribute("data-dir")]); });
      var cta = q(".g48-cta"); if (cta) cta.textContent = t.cta;
      overText();
    }
    function overText() {
      var t = D[lang()];
      if (state && state.status === "won") { msg.textContent = t.won; keepBtn.hidden = false; }
      else if (state && state.status === "over") { msg.textContent = t.over; keepBtn.hidden = true; }
    }
    function sizeClass(v) { return v >= 1024 ? "huge" : v >= 128 ? "big" : ""; }
    function place(el, t) { el.style.setProperty("--r", t.r); el.style.setProperty("--c", t.c); }
    function makeTile(t, cls) {
      var e = document.createElement("div");
      e.className = "g48-tile " + sizeClass(t.v) + (t.v > 4 ? " dark" : "") + (cls ? " " + cls : "");
      e.textContent = t.v; e.style.background = COLORS[t.v] || "#3C3A32"; place(e, t);
      inner.appendChild(e); els[t.id] = e; return e;
    }
    function rebuild() {
      [].forEach.call(inner.querySelectorAll(".g48-tile"), function (e) { e.remove(); });
      els = {}; state.tiles.forEach(function (t) { makeTile(t); });
    }
    function stats() {
      scoreEl.textContent = state.score; bestEl.textContent = best; undoBtn.disabled = !prev;
      over.hidden = state.status === "playing"; overText();
    }
    function reset() {
      state = newGame(rnd); prev = null; started = false; rebuild(); stats();
    }
    function apply(dir) {
      var mv = move(state, dir, rnd);
      if (!mv) return;
      if (!started) { started = true; track("demo_start", { app: "game2048" }); }
      prev = state; state = mv.state;
      var keepIds = {}; state.tiles.forEach(function (t) { keepIds[t.id] = true; });
      mv.ghosts.forEach(function (g) {
        var e = els[g.id]; if (!e) return;
        place(e, g); delete els[g.id];
        setTimeout(function () { e.remove(); }, 130);
      });
      state.tiles.forEach(function (t) {
        var e = els[t.id];
        if (e) place(e, t);
        else makeTile(t, t.id === mv.spawned ? "pop" : "merge");
      });
      if (state.score > best) { best = state.score; store("g2048_best", best); }
      stats();
      if (state.status !== "playing") {
        var mx = Math.max.apply(null, state.tiles.map(function (t) { return t.v; }));
        track("demo_end", { app: "game2048", result: state.status === "won" ? "win" : "over", score: state.score, max_tile: mx, moves: state.moves });
      }
    }

    board.addEventListener("keydown", function (e) {
      var d = ARROWS[e.key]; if (!d || e.ctrlKey || e.metaKey || e.altKey) return;
      e.preventDefault(); apply(d);
    });
    root.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var d = b.getAttribute("data-dir"), act = b.getAttribute("data-act");
      if (d) { apply(d); return; }
      if (act === "again" || act === "again2") reset();
      else if (act === "keep") { state = { tiles: state.tiles, nextId: state.nextId, score: state.score, status: "playing", keep: true, moves: state.moves }; prev = null; stats(); board.focus(); }
      else if (act === "undo" && prev) { state = prev; prev = null; rebuild(); stats(); }
    });
    // Dokunmatik kaydırma
    var sx, sy;
    board.addEventListener("touchstart", function (e) { var t = e.changedTouches[0]; sx = t.clientX; sy = t.clientY; }, { passive: true });
    board.addEventListener("touchend", function (e) {
      if (sx === undefined) return;
      var t = e.changedTouches[0], dx = t.clientX - sx, dy = t.clientY - sy;
      sx = undefined;
      if (Math.max(Math.abs(dx), Math.abs(dy)) < 24) return;
      apply(Math.abs(dx) > Math.abs(dy) ? (dx > 0 ? "right" : "left") : (dy > 0 ? "down" : "up"));
    }, { passive: true });

    reset(); labels();
    new MutationObserver(labels).observe(document.documentElement, { attributes: true, attributeFilter: ["lang", "data-lang", "class"] });
  }

  api.mount = mount;
  window.G2048 = api;
  function auto() { [].forEach.call(document.querySelectorAll("[data-g2048]"), mount); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto); else auto();
})();
