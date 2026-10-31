/* Tic-Tac-Toe tarayıcı demosu (nrazon.github.io). Uygulamadaki (TicTacToe/.../game/Game.kt) yapay zekânın birebir karşılığı:
   Kolay: yarı yarıya kazanma fırsatını görür, çoğunlukla rastgele. Orta: kazanır/engeller, çatalı bilmez (yenilebilir).
   Zor: minimax, yenilmez (eşit iyi hamlelerden rastgele). Oyuncu hep X, bilgisayar O; başlayan her oyunda değişir.
   Kullanım: <div data-ttt data-play="<Play adresi>"></div>  (ttt.js yüklenince kendiliğinden kurulur). Testler: tools/ttt.test.js */
(function () {
  "use strict";

  var LINES = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]];

  // ------------------------------------------------------------ oyun mantığı (DOM'dan bağımsız)
  function winnerOf(cells) {
    for (var i = 0; i < LINES.length; i++) {
      var l = LINES[i];
      if (cells[l[0]] && cells[l[0]] === cells[l[1]] && cells[l[0]] === cells[l[2]]) return { mark: cells[l[0]], line: l };
    }
    return null;
  }
  function empties(cells) { var e = []; for (var i = 0; i < 9; i++) if (!cells[i]) e.push(i); return e; }
  function over(cells) { return !!winnerOf(cells) || empties(cells).length === 0; }
  function pick(arr, rnd) { return arr[Math.floor(rnd() * arr.length)]; }

  /** [mark] bu hamlede kazanabiliyorsa o hücre (ilk bulunan). */
  function winning(cells, mark) {
    var e = empties(cells);
    for (var k = 0; k < e.length; k++) {
      var c = cells.slice(); c[e[k]] = mark;
      var w = winnerOf(c);
      if (w && w.mark === mark) return e[k];
    }
    return null;
  }

  function preferred(e, rnd) {
    if (e.indexOf(4) >= 0 && Math.floor(rnd() * 3) > 0) return 4;
    var corners = e.filter(function (i) { return i === 0 || i === 2 || i === 6 || i === 8; });
    if (corners.length && rnd() < 0.5) return pick(corners, rnd);
    return pick(e, rnd);
  }

  /** O'nun gözünden puan: O kazanırsa 10 - derinlik, X kazanırsa derinlik - 10, beraberlik 0.
      [memo]: aynı kökten (bestMove çağrısı) gelen konumlarda derinlik konumdan türediği için tahta anahtarıyla önbelleğe alınır. */
  function minimax(cells, turn, depth, memo) {
    var key = cells.map(function (c) { return c || "-"; }).join("") + turn;
    if (memo[key] !== undefined) return memo[key];
    var w = winnerOf(cells), res;
    if (w) res = w.mark === "O" ? 10 - depth : depth - 10;
    else {
      var e = empties(cells);
      if (!e.length) res = 0;
      else {
        var best = turn === "O" ? -Infinity : Infinity;
        for (var k = 0; k < e.length; k++) {
          var c = cells.slice(); c[e[k]] = turn;
          var s = minimax(c, turn === "O" ? "X" : "O", depth + 1, memo);
          best = turn === "O" ? Math.max(best, s) : Math.min(best, s);
        }
        res = best;
      }
    }
    memo[key] = res;
    return res;
  }

  function bestMove(cells, rnd) {
    var e = empties(cells), scored = [], top = -Infinity, memo = {};
    for (var k = 0; k < e.length; k++) {
      var c = cells.slice(); c[e[k]] = "O";
      var s = minimax(c, "X", 1, memo);
      scored.push([e[k], s]);
      if (s > top) top = s;
    }
    return pick(scored.filter(function (x) { return x[1] === top; }).map(function (x) { return x[0]; }), rnd);
  }

  /** Bilgisayarın (O) hamlesi. [diff]: easy | medium | hard. */
  function aiMove(cells, diff, rnd) {
    rnd = rnd || Math.random;
    var e = empties(cells);
    if (diff === "easy") {
      var win = winning(cells, "O");
      return win !== null && rnd() < 0.5 ? win : pick(e, rnd);
    }
    if (diff === "medium") {
      var w = winning(cells, "O");
      if (w !== null) return w;
      var b = winning(cells, "X");
      return b !== null ? b : preferred(e, rnd);
    }
    return bestMove(cells, rnd);
  }

  var api = { LINES: LINES, winnerOf: winnerOf, empties: empties, over: over, aiMove: aiMove };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; return; }
  if (typeof document === "undefined") return;

  // ------------------------------------------------------------ arayüz
  var D = {
    tr: { easy: "Kolay", medium: "Orta", hard: "Zor", level: "Seviye", you: "Sen", draw: "Berabere", cpu: "Bilgisayar", again: "Yeni oyun", reset: "Skoru sıfırla",
      yours: "Sıra sende (X)", cpuTurn: "Bilgisayar düşünüyor…", won: "Kazandın!", lost: "Bilgisayar kazandı", tie: "Berabere", empty: "boş", row: "satır", col: "sütun",
      cta: "Beğendin mi? Uygulamayı indir", hint: "Zor seviyede bilgisayar hiç kaybetmez." },
    en: { easy: "Easy", medium: "Medium", hard: "Hard", level: "Level", you: "You", draw: "Draw", cpu: "Computer", again: "New game", reset: "Reset score",
      yours: "Your turn (X)", cpuTurn: "Computer is thinking…", won: "You win!", lost: "Computer wins", tie: "It's a draw", empty: "empty", row: "row", col: "column",
      cta: "Like it? Get the app", hint: "On Hard the computer never loses." },
    es: { easy: "Fácil", medium: "Medio", hard: "Difícil", level: "Nivel", you: "Tú", draw: "Empate", cpu: "Máquina", again: "Nueva partida", reset: "Reiniciar marcador",
      yours: "Tu turno (X)", cpuTurn: "La máquina piensa…", won: "¡Ganaste!", lost: "Gana la máquina", tie: "Empate", empty: "vacía", row: "fila", col: "columna",
      cta: "¿Te gustó? Descarga la app", hint: "En Difícil la máquina nunca pierde." },
    pt: { easy: "Fácil", medium: "Médio", hard: "Difícil", level: "Nível", you: "Você", draw: "Empate", cpu: "Computador", again: "Novo jogo", reset: "Zerar placar",
      yours: "Sua vez (X)", cpuTurn: "O computador está pensando…", won: "Você venceu!", lost: "O computador venceu", tie: "Empate", empty: "vazia", row: "linha", col: "coluna",
      cta: "Gostou? Baixe o app", hint: "No Difícil o computador nunca perde." }
  };
  function lang() {
    var h = document.documentElement;
    var l = (h.getAttribute("data-lang") || h.lang || "en").slice(0, 2);
    return D[l] ? l : "en";
  }

  var CSS = ".ttt{--t-card:#1C1F2A;--t-cell:#262B3A;--t-grid:#30364A;--t-text:#EEF0F7;--t-dim:#A3A9BC;--t-x:#EF5B5B;--t-o:#1FA39A;--t-acc:#8E6CF0;color:var(--t-text);font:16px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}" +
    "@media (prefers-color-scheme:light){.ttt{--t-card:#FFFFFF;--t-cell:#F3F5FA;--t-grid:#D9DEEA;--t-text:#1E2230;--t-dim:#6B7285}}" +
    ".ttt *{box-sizing:border-box}.ttt-box{display:flex;flex-wrap:wrap;gap:20px 28px;align-items:center;justify-content:center}" +
    ".ttt-side{flex:1 1 220px;max-width:340px;display:flex;flex-direction:column;gap:12px}" +
    ".ttt-seg{display:flex;background:var(--t-cell);border-radius:999px;padding:4px;gap:2px}" +
    ".ttt-seg button{flex:1;border:0;background:none;color:var(--t-dim);font:inherit;font-weight:700;font-size:14px;padding:8px 10px;border-radius:999px;cursor:pointer}" +
    ".ttt-seg button[aria-pressed=true]{background:var(--t-text);color:var(--t-card)}" +
    ".ttt-board{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;width:min(100%,288px);margin:0 auto;padding:10px;background:var(--t-grid);border-radius:20px}" +
    ".ttt-cell{aspect-ratio:1;border:0;border-radius:14px;background:var(--t-cell);cursor:pointer;display:flex;align-items:center;justify-content:center;padding:14%}" +
    ".ttt-cell:disabled{cursor:default}.ttt-cell:not(:disabled):hover{filter:brightness(1.12)}" +
    ".ttt-cell svg{width:100%;height:100%;overflow:visible}.ttt-cell path,.ttt-cell circle{fill:none;stroke-width:11;stroke-linecap:round}" +
    ".ttt-cell .x{stroke:var(--t-x)}.ttt-cell .o{stroke:var(--t-o)}.ttt-cell.win{background:color-mix(in srgb,var(--t-acc) 28%,var(--t-cell))}" +
    ".ttt-cell.pop svg{animation:ttt-pop .22s ease-out}@keyframes ttt-pop{from{transform:scale(.4);opacity:0}to{transform:none;opacity:1}}" +
    "@media (prefers-reduced-motion:reduce){.ttt-cell.pop svg{animation:none}}" +
    ".ttt-status{margin:0;font-weight:800;font-size:18px;min-height:1.6em}.ttt-status.won{color:var(--t-o)}.ttt-status.lost{color:var(--t-x)}" +
    ".ttt-score{display:flex;gap:8px}.ttt-score div{flex:1;background:var(--t-cell);border-radius:12px;padding:8px 6px;text-align:center}" +
    ".ttt-score b{display:block;font-size:22px;line-height:1.1}.ttt-score span{font-size:12px;color:var(--t-dim)}" +
    ".ttt-row{display:flex;flex-wrap:wrap;gap:8px 14px;align-items:center}" +
    ".ttt-btn{border:0;background:var(--t-acc);color:#fff;font:inherit;font-weight:800;font-size:14px;padding:9px 18px;border-radius:999px;cursor:pointer}" +
    ".ttt-link{background:none;border:0;color:var(--t-dim);font:inherit;font-size:13px;text-decoration:underline;cursor:pointer;padding:4px}" +
    ".ttt-hint{margin:0;font-size:13px;color:var(--t-dim)}.ttt a.ttt-cta{font-weight:800;font-size:14px}" +
    ".ttt button:focus-visible,.ttt a:focus-visible{outline:3px solid var(--t-acc);outline-offset:2px}";

  var X_SVG = '<svg viewBox="0 0 100 100" aria-hidden="true"><path class="x" d="M18 18L82 82M82 18L18 82"/></svg>';
  var O_SVG = '<svg viewBox="0 0 100 100" aria-hidden="true"><circle class="o" cx="50" cy="50" r="33"/></svg>';

  function store(key, val) {
    try { if (val === undefined) return JSON.parse(localStorage.getItem(key) || "null"); localStorage.setItem(key, JSON.stringify(val)); } catch (e) { return null; }
  }
  function track(name, params) {
    try { if (typeof window.gtag === "function") window.gtag("event", name, params); } catch (e) {}
  }

  function mount(root) {
    if (root.__ttt) return;
    root.__ttt = true;
    if (!document.getElementById("ttt-css")) {
      var st = document.createElement("style"); st.id = "ttt-css"; st.textContent = CSS; document.head.appendChild(st);
    }
    var diff = store("ttt_diff") || "hard";
    if (["easy", "medium", "hard"].indexOf(diff) < 0) diff = "hard";
    var scores = store("ttt_scores") || {};
    var starter = "X", cells, ended, started, timer;
    var els = {};

    root.classList.add("ttt");
    root.innerHTML = '<div class="ttt-box"><div class="ttt-board" role="group"></div><div class="ttt-side">' +
      '<div class="ttt-seg" role="group"></div><p class="ttt-status" role="status" aria-live="polite"></p>' +
      '<div class="ttt-score"></div><div class="ttt-row"><button type="button" class="ttt-btn" data-act="again"></button>' +
      '<button type="button" class="ttt-link" data-act="reset"></button></div><p class="ttt-hint"></p>' +
      (root.getAttribute("data-play") ? '<a class="ttt-cta" href="' + root.getAttribute("data-play") + '"></a>' : "") + "</div></div>";
    els.board = root.querySelector(".ttt-board"); els.seg = root.querySelector(".ttt-seg"); els.status = root.querySelector(".ttt-status");
    els.score = root.querySelector(".ttt-score"); els.again = root.querySelector("[data-act=again]"); els.reset = root.querySelector("[data-act=reset]");
    els.hint = root.querySelector(".ttt-hint"); els.cta = root.querySelector(".ttt-cta");

    function sc() { return scores[diff] || (scores[diff] = { w: 0, d: 0, l: 0 }); }

    function labels() {
      var t = D[lang()];
      els.seg.setAttribute("aria-label", t.level);
      [].forEach.call(els.seg.children, function (b) { b.textContent = t[b.getAttribute("data-d")]; });
      els.again.textContent = t.again; els.reset.textContent = t.reset; els.hint.textContent = t.hint;
      if (els.cta) els.cta.textContent = t.cta;
      var s = sc();
      els.score.innerHTML = '<div><b>' + s.w + '</b><span>' + t.you + '</span></div><div><b>' + s.d + '</b><span>' + t.draw + '</span></div><div><b>' + s.l + '</b><span>' + t.cpu + '</span></div>';
      cellLabels();
      statusText();
    }
    function cellLabels() {
      var t = D[lang()];
      [].forEach.call(els.board.children, function (b, i) {
        var m = cells[i];
        b.setAttribute("aria-label", t.row + " " + (Math.floor(i / 3) + 1) + ", " + t.col + " " + (i % 3 + 1) + ", " + (m || t.empty));
      });
    }
    var status = { key: "yours", cls: "" };
    function statusText() {
      var t = D[lang()];
      els.status.textContent = t[status.key]; els.status.className = "ttt-status " + status.cls;
    }
    function setStatus(key, cls) { status = { key: key, cls: cls || "" }; statusText(); }

    function build() {
      els.board.innerHTML = "";
      for (var i = 0; i < 9; i++) {
        var b = document.createElement("button"); b.type = "button"; b.className = "ttt-cell"; b.setAttribute("data-i", i);
        els.board.appendChild(b);
      }
      els.seg.innerHTML = "";
      ["easy", "medium", "hard"].forEach(function (d) {
        var b = document.createElement("button"); b.type = "button"; b.setAttribute("data-d", d); b.setAttribute("aria-pressed", d === diff);
        els.seg.appendChild(b);
      });
    }
    function isHumanTurn() { var moves = 9 - empties(cells).length; return (moves % 2 === 0 ? starter : (starter === "X" ? "O" : "X")) === "X"; }
    function refresh() {
      for (var i = 0; i < 9; i++) {
        var b = els.board.children[i];
        b.disabled = ended || !!cells[i] || !isHumanTurn();
      }
    }

    function finish() {
      ended = true;
      var w = winnerOf(cells), s = sc(), res;
      if (w) {
        w.line.forEach(function (i) { els.board.children[i].classList.add("win"); });
        res = w.mark === "X" ? "w" : "l";
      } else res = "d";
      s[res]++; scores[diff] = s; store("ttt_scores", scores);
      setStatus(res === "w" ? "won" : res === "l" ? "lost" : "tie", res === "w" ? "won" : res === "l" ? "lost" : "");
      var t = D[lang()];
      var sa = els.score.querySelectorAll("b"); sa[0].textContent = s.w; sa[1].textContent = s.d; sa[2].textContent = s.l;
      track("demo_end", { app: "tictactoe", difficulty: diff, result: res === "w" ? "win" : res === "l" ? "loss" : "draw", moves: 9 - empties(cells).length });
      refresh();
    }

    function place(i, mark) {
      cells[i] = mark;
      var b = els.board.children[i]; b.innerHTML = mark === "X" ? X_SVG : O_SVG; b.classList.add("pop");
      if (over(cells)) { finish(); return true; }
      return false;
    }
    function cpuTurn() {
      setStatus("cpuTurn"); refresh();
      timer = setTimeout(function () {
        if (ended) return;
        var done = place(aiMove(cells, diff), "O");
        cellLabels();
        if (!done) { setStatus("yours"); refresh(); }
      }, 420);
    }

    function newGame(keepStarter) {
      clearTimeout(timer);
      if (!keepStarter) starter = starter === "X" ? "O" : "X";
      cells = [null, null, null, null, null, null, null, null, null]; ended = false; started = false;
      [].forEach.call(els.board.children, function (b) { b.innerHTML = ""; b.className = "ttt-cell"; });
      cellLabels();
      if (starter === "O") cpuTurn(); else { setStatus("yours"); refresh(); }
    }

    els.board.addEventListener("click", function (e) {
      var b = e.target.closest(".ttt-cell");
      if (!b || b.disabled || ended) return;
      if (!started) { started = true; track("demo_start", { app: "tictactoe", difficulty: diff }); }
      var i = +b.getAttribute("data-i");
      if (place(i, "X")) { cellLabels(); return; }
      cellLabels();
      cpuTurn();
    });
    els.seg.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      diff = b.getAttribute("data-d"); store("ttt_diff", diff);
      [].forEach.call(els.seg.children, function (x) { x.setAttribute("aria-pressed", x === b); });
      labels(); newGame(true);
    });
    els.again.addEventListener("click", function () { newGame(false); });
    els.reset.addEventListener("click", function () { scores[diff] = { w: 0, d: 0, l: 0 }; store("ttt_scores", scores); labels(); });

    build(); cells = [null, null, null, null, null, null, null, null, null]; ended = false; started = false;
    labels(); newGame(true);
    // dil değişince (html lang / data-lang / class) etiketleri yenile
    new MutationObserver(labels).observe(document.documentElement, { attributes: true, attributeFilter: ["lang", "data-lang", "class"] });
  }

  api.mount = mount;
  window.TTT = api;
  function auto() { [].forEach.call(document.querySelectorAll("[data-ttt]"), mount); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto); else auto();
})();
