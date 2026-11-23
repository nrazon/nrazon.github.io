/* Grumblings tarayıcı demosu (nesimapps.com). Uygulamadaki (Grumblings/.../game/Maze.kt) kural motorunun ve BFS çözücünün birebir karşılığı.
   KURAL: kahraman 1 adım (ya da bekle); sonra her canavar sırayla 1 adım, bunu iki tur tekrarlar (A1, B1, A2, B2). Canavar adımı: tercih ettiği
   eksende yaklaşır (engel yoksa); olmazsa diğer eksende; olmazsa yerinde durur. Engel = duvar ya da başka bir canavarın hücresi. Herhangi bir
   canavar kahramanın hücresine girerse yakalanırsın (kalan adımlar atılmaz). Çıkışa varan kahraman kazanır (canavarlar oynamaz).
   Gömülü bölümler uygulamanın assets/levels.txt dosyasının ilk 30 satırıdır (5x5 ve 6x6). Kullanım: <div data-grumblings data-play="<Play adresi>"></div>
   Testler: node tools/grumblings.test.js */
(function () {
  "use strict";

  // Satır: boyut;kahraman;çıkış;eksenler;canavarlar(|);dikey duvarlar;yatay duvarlar;en iyi çözüm
  var LEVELS = [
    "5;4,3;3,0;H;1,4;0001100001001010100110001;0110001010000100011011111;LLUL",
    "5;3,3;1,0;H;0,4;0010100101101010101100001;0010000010000001111011111;LUULL",
    "5;4,4;0,2;H;3,0;0010101001000011000100001;1000001010101000111011111;UUULLU",
    "5;0,4;3,0;H;3,4;0110110011111110100100001;0000000010010000010011111;LDLLULDDD",
    "5;0,3;4,4;H;2,0;0000110011011010111100101;0011001001000000000011111;LLDRRDDDR",
    "5;4,1;0,2;H;0,3;0000100001100011001100001;0001001010011100010011111;RWLLUUUURR",
    "5;0,3;4,2;H;3,4;0000101001110010000100001;1011000011011100010011111;RLLLDLDDDRR",
    "5;2,0;4,4;H;4,2;0000110111001011000101001;0110000001010100001011111;UURRRDDRDD",
    "5;0,3;3,0;H;2,4;0100110101100011001101101;0001001000000100000011111;WLDLULDDD",
    "5;0,3;3,0;H;4,1;0100110111001110010100001;0000001100010100100011111;DULDLULDDD",
    "5;0,2;2,0;H;4,0;0100101011100110011101001;1010000000000000101011111;RDDLLULD",
    "5;2,4;1,0;H;3,0;0000111101011011001100001;0100000000110000010011111;UULLLLD",
    "5;2,4;3,0;H;0,1;1000111011000011111100101;0010000001000000000011111;DULLLLD",
    "5;1,3;4,0;H;3,0;0000100101110010011100001;1100000110010000110011111;ULDLLDDD",
    "5;4,0;0,4;H;4,4;0000100001010011100110101;0110010100010100000011111;UURULURRRR",
    "5;4,3;0,1;H;2,2;0100110101010110000100001;0100100100001011100011111;LULULUUR",
    "5;2,3;3,0;H;0,2;0001100111001011000101001;0110000100011100000011111;RDLLLDLU",
    "5;4,0;2,4;H;4,4;1000101001011010011101001;0001001010000000001011111;UUURURDRRD",
    "5;3,2;0,0;H;1,0;0010100001001011111101011;0100000000010100000011111;DRLUULLUU",
    "5;3,2;3,4;H;0,1;0000101101011110010100001;0001000000001000110011111;WLLDRRRUR",
    "6;0,5;5,2;H;1,2;100001101101010111110101011111000001;000000000000000100001001010000111111;DDDLDDLL",
    "6;3,2;2,5;H;5,4;000001110101000011101001000011000101;001000000100101010011110010000111111;LURRDRRU",
    "6;2,5;5,4;H;0,1;000001001011001101000011000101000011;011000000110011001010010110100111111;LDLDLDRR",
    "6;4,1;1,5;H;2,3;010011010101000111100101010001000001;000100011000111100001000000010111111;URRDRUUUR",
    "6;3,0;1,5;H;5,3;100001000011000101111101010101001001;011000011100000000000100100000111111;UURRRURRD",
    "6;2,0;0,4;H;3,3;010011101001110001111001001101000001;010100001010000100010010000100111111;DDRRUURURU",
    "6;5,3;0,2;H;2,4;100001100111010101000001101111000001;001100000001010010011010001000111111;UUUULLUR",
    "6;0,0;0,5;H;2,2;100001110101010101011001000011000001;000101001001010100010000000100111111;DDRUURRRR",
    "6;4,0;1,0;H;4,3;000011010101100011010001011001000001;101000010010101010100100010010111111;RUURURULLDL",
    "6;0,3;5,1;H;2,2;001001101001110011000001010001000001;001001000010001110000111011100111111;RDRDDLLLLDLDR"
  ];

  // ------------------------------------------------------------ kural motoru (DOM'dan bağımsız)
  function cell(s) { var p = s.split(","); return { r: +p[0], c: +p[1] }; }
  function same(a, b) { return a.r === b.r && a.c === b.c; }

  function decode(line) {
    var p = line.trim().split(";"), n = +p[0], v = [], h = [], r, c;
    for (r = 0; r < n; r++) { v.push([]); h.push([]); for (c = 0; c < n; c++) { v[r].push(p[5][r * n + c] === "1"); h[r].push(p[6][r * n + c] === "1"); } }
    return { n: n, hero: cell(p[1]), exit: cell(p[2]), axes: p[3].split(""), monsters: p[4].split("|").map(cell), v: v, h: h, best: p[7] };
  }

  function inside(L, a) { return a.r >= 0 && a.r < L.n && a.c >= 0 && a.c < L.n; }
  /** a ile komşu b arasında geçiş açık mı. */
  function open(L, a, b) {
    if (!inside(L, a) || !inside(L, b)) return false;
    if (a.r === b.r && b.c === a.c + 1) return !L.v[a.r][a.c];
    if (a.r === b.r && b.c === a.c - 1) return !L.v[a.r][b.c];
    if (a.c === b.c && b.r === a.r + 1) return !L.h[a.r][a.c];
    if (a.c === b.c && b.r === a.r - 1) return !L.h[b.r][a.c];
    return false;
  }
  function blocked(L, from, to, ms, self) {
    if (!open(L, from, to)) return true;
    for (var i = 0; i < ms.length; i++) if (i !== self && same(ms[i], to)) return true;
    return false;
  }
  /** [i]. canavarın tek adımı ([ms] güncel konumlar). */
  function monsterStep(L, hero, ms, i) {
    var mo = ms[i];
    function horizontal() {
      if (hero.c === mo.c) return null;
      var n = { r: mo.r, c: mo.c + (hero.c > mo.c ? 1 : -1) };
      return blocked(L, mo, n, ms, i) ? null : n;
    }
    function vertical() {
      if (hero.r === mo.r) return null;
      var n = { r: mo.r + (hero.r > mo.r ? 1 : -1), c: mo.c };
      return blocked(L, mo, n, ms, i) ? null : n;
    }
    var first = L.axes[i] === "H" ? horizontal() : vertical();
    if (first) return first;
    return (L.axes[i] === "H" ? vertical() : horizontal()) || mo;
  }
  var DIRS = { U: [-1, 0], D: [1, 0], L: [0, -1], R: [0, 1] };
  /** [dir] null ise bekle. Geçersiz hamle (duvar/kenar) null döner. Sonuç: {outcome: GO|WIN|LOSE, hero, monsters, steps:[{i, to}]} */
  function move(L, hero, monsters, dir) {
    var h = hero;
    if (dir) {
      var d = DIRS[dir], n = { r: h.r + d[0], c: h.c + d[1] };
      if (!open(L, h, n)) return null;
      h = n;
    }
    if (same(h, L.exit)) return { outcome: "WIN", hero: h, monsters: monsters, steps: [] };
    var ms = monsters.slice(), steps = [];
    for (var t = 0; t < 2; t++) for (var i = 0; i < ms.length; i++) {
      ms[i] = monsterStep(L, h, ms, i);
      steps.push({ i: i, to: ms[i] });
      if (same(ms[i], h)) return { outcome: "LOSE", hero: h, monsters: ms, steps: steps };
    }
    return { outcome: "GO", hero: h, monsters: ms, steps: steps };
  }

  /** BFS: en kısa çözüm (U D L R W dizisi), yoksa null. Durum = (kahraman, canavarlar). */
  function solve(L, hero, monsters) {
    var n = L.n * L.n, k = monsters.length;
    function id(c) { return c.r * L.n + c.c; }
    function cellOf(i) { return { r: Math.floor(i / L.n), c: i % L.n }; }
    function enc(h, ms) { var key = id(h); for (var i = 0; i < ms.length; i++) key = key * n + id(ms[i]); return key; }
    function dec(key) { var ms = [], kk = key; for (var i = k - 1; i >= 0; i--) { ms[i] = cellOf(kk % n); kk = Math.floor(kk / n); } return { h: cellOf(kk), ms: ms }; }
    var prev = new Map(), start = enc(hero, monsters), queue = [start], qi = 0;
    prev.set(start, null);
    while (qi < queue.length) {
      var st = queue[qi++], s = dec(st);
      for (var a = 0; a < 5; a++) {
        var ch = "UDLRW"[a], r = move(L, s.h, s.ms, ch === "W" ? null : ch);
        if (!r || r.outcome === "LOSE") continue;
        if (r.outcome === "WIN") {
          var out = ch, cur = st;
          while (prev.get(cur)) { out = prev.get(cur).m + out; cur = prev.get(cur).p; }
          return out;
        }
        var ns = enc(r.hero, r.monsters);
        if (!prev.has(ns)) { prev.set(ns, { p: st, m: ch }); queue.push(ns); }
      }
    }
    return null;
  }
  /** Hamle sayısına göre yıldız: en iyi çözüm = 3, biraz fazla = 2, tamamladın = 1. */
  function starsFor(moves, optimal) {
    if (moves <= optimal) return 3;
    if (moves <= optimal + Math.max(2, Math.floor(optimal / 4))) return 2;
    return 1;
  }

  var api = { LEVELS: LEVELS, decode: decode, open: open, monsterStep: monsterStep, move: move, solve: solve, starsFor: starsFor };
  if (typeof module !== "undefined" && module.exports) { module.exports = api; return; }
  if (typeof document === "undefined") return;

  // ------------------------------------------------------------ arayüz
  var D = {
    tr: { level: "Bölüm", moves: "Hamle", best: "En iyi", wait: "Bekle", undo: "Geri al", restart: "Yeniden", hint: "İpucu", preview: "Canavarın yolunu göster", next: "Sonraki bölüm",
      prev: "Önceki bölüm", win: "Kapıya ulaştın!", stars: "yıldız", caught: "Huysuz canavar seni gıdıkladı! Geri al ya da yeniden dene.", nohint: "Bu konumdan çıkış yok: geri al.",
      how: "Ok tuşları, kaydırma ya da yanındaki kareye dokunma ile ilerle. Sen 1 adım atarsın, canavar 2!", cta: "Beğendin mi? 300 bölümün hepsi uygulamada", done: "Demodaki tüm bölümleri bitirdin!", of: "/", hintTxt: "İpucu: bu yöne git", note: "Çizgiler, burada beklersen her canavarın atacağı iki adımı gösterir.", ovNext: "Sonraki bölüm ▶", ovAgain: "Tekrar oyna", ovUndo: "Geri al", ovRestart: "Yeniden", ovWinTitle: "Bölüm geçildi!" },
    en: { level: "Level", moves: "Moves", best: "Best", wait: "Wait", undo: "Undo", restart: "Restart", hint: "Hint", preview: "Show monster path", next: "Next level",
      prev: "Previous level", win: "You reached the door!", stars: "stars", caught: "The grumpy monster tickled you! Undo or try again.", nohint: "No way out from here: undo.",
      how: "Use arrow keys, swipe or tap the next square. You take 1 step, the monster takes 2!", cta: "Like it? All 300 levels are in the app", done: "You finished every level in the demo!", of: "/", hintTxt: "Hint: go this way", note: "The lines show the two steps each monster would take if you waited here.", ovNext: "Next level ▶", ovAgain: "Play again", ovUndo: "Undo", ovRestart: "Restart", ovWinTitle: "Level complete!" },
    es: { level: "Nivel", moves: "Movs.", best: "Mejor", wait: "Esperar", undo: "Deshacer", restart: "Reiniciar", hint: "Pista", preview: "Ver camino del monstruo", next: "Siguiente nivel",
      prev: "Nivel anterior", win: "¡Llegaste a la puerta!", stars: "estrellas", caught: "¡El monstruo gruñón te hizo cosquillas! Deshaz o reintenta.", nohint: "Desde aquí no hay salida: deshaz.",
      how: "Usa las flechas, desliza o toca la casilla de al lado. Tú das 1 paso, ¡el monstruo da 2!", cta: "¿Te gustó? Los 300 niveles están en la app", done: "¡Terminaste todos los niveles de la demo!", of: "/", hintTxt: "Pista: ve por aquí", note: "Las líneas muestran los dos pasos que daría cada monstruo si esperas aquí.", ovNext: "Siguiente nivel ▶", ovAgain: "Jugar de nuevo", ovUndo: "Deshacer", ovRestart: "Reiniciar", ovWinTitle: "¡Nivel superado!" },
    pt: { level: "Nível", moves: "Jogadas", best: "Melhor", wait: "Esperar", undo: "Desfazer", restart: "Reiniciar", hint: "Dica", preview: "Ver caminho do monstro", next: "Próximo nível",
      prev: "Nível anterior", win: "Você chegou à porta!", stars: "estrelas", caught: "O monstro rabugento fez cócegas em você! Desfaça ou tente de novo.", nohint: "Daqui não há saída: desfaça.",
      how: "Use as setas, deslize ou toque no quadrado ao lado. Você dá 1 passo, o monstro dá 2!", cta: "Gostou? Os 300 níveis estão no app", done: "Você terminou todos os níveis da demo!", of: "/", hintTxt: "Dica: vá por aqui", note: "As linhas mostram os dois passos que cada monstro daria se você esperasse aqui.", ovNext: "Próximo nível ▶", ovAgain: "Jogar de novo", ovUndo: "Desfazer", ovRestart: "Reiniciar", ovWinTitle: "Nível concluído!" }
  };
  function lang() {
    var h = document.documentElement;
    var l = (h.getAttribute("data-lang") || h.lang || "en").slice(0, 2);
    return D[l] ? l : "en";
  }

  var CSS = ".gm{--g-ink:#4A2F27;--g-soft:#8A6A58;--g-acc:#E8478B;--g-card:#FFF8EC;--g-edge:#D9BF9A;color:var(--g-ink);font:16px/1.5 system-ui,-apple-system,'Segoe UI',Roboto,sans-serif}" +
    ".gm *{box-sizing:border-box}.gm-box{display:flex;flex-wrap:wrap;gap:18px 26px;align-items:flex-start;justify-content:center}" +
    ".gm-stage{flex:1 1 280px;max-width:380px;width:100%;position:relative}.gm canvas{display:block;width:100%;aspect-ratio:1;border-radius:20px;touch-action:none;outline:none;box-shadow:0 6px 0 rgba(90,58,34,.35)}" +
    ".gm canvas:focus-visible{outline:3px solid var(--g-acc);outline-offset:3px}" +
    ".gm-side{flex:1 1 220px;max-width:340px;display:flex;flex-direction:column;gap:12px;background:var(--g-card);border:2px solid var(--g-edge);border-radius:20px;padding:16px;color:var(--g-ink)}" +
    ".gm-top{display:flex;align-items:center;gap:8px}.gm-top b{flex:1;text-align:center;font-size:18px}" +
    ".gm-nav{border:2px solid var(--g-edge);background:#FFEFD9;color:var(--g-ink);width:36px;height:36px;border-radius:50%;font:inherit;font-weight:800;font-size:18px;cursor:pointer;line-height:1}" +
    ".gm-nav:disabled{opacity:.35;cursor:default}" +
    ".gm-stats{display:flex;gap:8px}.gm-stats div{flex:1;background:#FFEFD9;border-radius:12px;padding:6px;text-align:center}.gm-stats b{display:block;font-size:20px;line-height:1.1}.gm-stats span{font-size:12px;color:var(--g-soft)}" +
    ".gm-status{margin:0;min-height:3.2em;font-weight:800;font-size:15px}.gm-status.win{color:#2C8A83}.gm-status.lose{color:#D8432F}" +
    ".gm-btns{display:flex;flex-wrap:wrap;gap:8px}.gm-btn{border:2px solid var(--g-edge);background:#FFEFD9;color:var(--g-ink);font:inherit;font-weight:800;font-size:14px;padding:8px 14px;border-radius:999px;cursor:pointer}" +
    ".gm-btn[aria-pressed=true],.gm-btn.pri{background:var(--g-acc);border-color:#B02763;color:#fff}.gm-btn:disabled{opacity:.4;cursor:default}" +
    ".gm-note{margin:0;font-size:13px;font-weight:700;color:#B02763}.gm-note[hidden]{display:none}" +
    ".gm-ov{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(74,47,39,.5);border-radius:20px;padding:14px}.gm-ov[hidden]{display:none}" +
    ".gm-ov-card{background:var(--g-card);border:3px solid var(--g-edge);border-radius:20px;padding:18px 20px;text-align:center;box-shadow:0 6px 0 rgba(90,58,34,.35);max-width:260px}" +
    ".gm-ov-stars{font-size:40px;line-height:1;color:#FFC531;letter-spacing:4px;text-shadow:0 2px 0 #B77400}.gm-ov-title{font-weight:800;font-size:18px;margin:8px 0 12px}" +
    ".gm-ov-btns{display:flex;flex-wrap:wrap;gap:8px;justify-content:center}.gm-ov-btns .gm-btn{font-size:15px;padding:10px 16px}" +
    ".gm-how{margin:0;font-size:13px;color:var(--g-soft)}.gm a.gm-cta{font-weight:800;font-size:14px;color:#B02763}" +
    ".gm button:focus-visible,.gm a:focus-visible{outline:3px solid var(--g-acc);outline-offset:2px}";

  function store(key, val) {
    try { if (val === undefined) return JSON.parse(localStorage.getItem(key) || "null"); localStorage.setItem(key, JSON.stringify(val)); } catch (e) { return null; }
  }
  function track(name, params) {
    try { if (typeof window.gtag === "function") window.gtag("event", name, params); } catch (e) {}
  }

  function mount(root) {
    if (root.__gm) return;
    root.__gm = true;
    if (!document.getElementById("gm-css")) {
      var st = document.createElement("style"); st.id = "gm-css"; st.textContent = CSS; document.head.appendChild(st);
    }
    var levels = LEVELS.map(decode);
    var idx = Math.min(Math.max(+store("gm_lv") || 0, 0), levels.length - 1);
    var stars = store("gm_stars") || {};
    var L, hero, ms, moves, history, finished, locked, started, previewOn, hintDir, shake = 0;
    var pos = null, anim = null, raf = 0, W = 0;

    root.classList.add("gm");
    root.innerHTML = '<div class="gm-box"><div class="gm-stage"><canvas tabindex="0" role="img"></canvas><div class="gm-ov" hidden><div class="gm-ov-card"><div class="gm-ov-stars"></div><div class="gm-ov-title" role="status"></div><div class="gm-ov-btns"><button type="button" class="gm-btn pri" data-act="ov1"></button><button type="button" class="gm-btn" data-act="ov2"></button></div></div></div></div><div class="gm-side">' +
      '<div class="gm-top"><button type="button" class="gm-nav" data-act="prev">‹</button><b class="gm-lv"></b><button type="button" class="gm-nav" data-act="next">›</button></div>' +
      '<div class="gm-stats"><div><b class="gm-moves">0</b><span class="gm-l1"></span></div><div><b class="gm-best">0</b><span class="gm-l2"></span></div><div><b class="gm-star">–</b><span class="gm-l3"></span></div></div>' +
      '<p class="gm-status" role="status" aria-live="polite"></p>' +
      '<div class="gm-btns"><button type="button" class="gm-btn" data-act="wait"></button><button type="button" class="gm-btn" data-act="undo"></button>' +
      '<button type="button" class="gm-btn" data-act="restart"></button><button type="button" class="gm-btn" data-act="hint"></button><button type="button" class="gm-btn" data-act="preview" aria-pressed="false"></button></div>' +
      '<p class="gm-note" hidden></p><p class="gm-how"></p>' + (root.getAttribute("data-play") ? '<a class="gm-cta" href="' + root.getAttribute("data-play") + '"></a>' : "") + "</div></div>";
    var cv = root.querySelector("canvas"), ctx = cv.getContext("2d");
    var q = function (s) { return root.querySelector(s); };
    var els = { ov: q(".gm-ov"), ovStars: q(".gm-ov-stars"), ovTitle: q(".gm-ov-title"), note: q(".gm-note"), lv: q(".gm-lv"), moves: q(".gm-moves"), best: q(".gm-best"), star: q(".gm-star"), l1: q(".gm-l1"), l2: q(".gm-l2"), l3: q(".gm-l3"), status: q(".gm-status"), how: q(".gm-how"), cta: q(".gm-cta") };
    var acts = {}; [].forEach.call(root.querySelectorAll("[data-act]"), function (b) { acts[b.getAttribute("data-act")] = b; });
    var status = { key: null, cls: "", extra: "" };

    function text() {
      var t = D[lang()];
      els.lv.textContent = t.level + " " + (idx + 1) + " " + t.of + " " + levels.length;
      els.l1.textContent = t.moves; els.l2.textContent = t.best; els.l3.textContent = "★";
      acts.wait.textContent = t.wait; acts.undo.textContent = t.undo; acts.restart.textContent = t.restart; acts.hint.textContent = t.hint; acts.preview.textContent = t.preview;
      acts.prev.setAttribute("aria-label", t.prev); acts.next.setAttribute("aria-label", t.next);
      els.how.textContent = t.how; if (els.cta) els.cta.textContent = t.cta;
      cv.setAttribute("aria-label", t.level + " " + (idx + 1) + ", " + t.moves + " " + moves);
      els.status.textContent = status.key ? t[status.key] + (status.extra || "") : ""; els.status.className = "gm-status " + status.cls;
      els.note.textContent = t.note; els.note.hidden = !previewOn;
      ovText();
    }
    function ovText() {
      var t = D[lang()], win = finished, lose = !finished && status.cls === "lose";
      if (!win && !lose) return;
      var last = idx >= levels.length - 1;
      if (win) {
        els.ovStars.textContent = "★".repeat(stars[idx] || 1);
        els.ovTitle.textContent = last ? t.done : t.ovWinTitle;
        acts.ov1.textContent = last ? t.ovAgain : t.ovNext; acts.ov2.textContent = last ? t.restart : t.ovAgain;
      } else {
        els.ovStars.textContent = "😖";
        els.ovTitle.textContent = t.caught;
        acts.ov1.textContent = t.ovUndo; acts.ov2.textContent = t.ovRestart;
      }
    }
    function showOv(show) {
      var was = !els.ov.hidden;
      els.ov.hidden = !show;
      if (show) { ovText(); try { acts.ov1.focus({ preventScroll: true }); } catch (e) {} }
      else if (was) { try { cv.focus({ preventScroll: true }); } catch (e) {} }
    }
    function setStatus(key, cls, extra) { status = { key: key, cls: cls || "", extra: extra || "" }; text(); }
    function hud() {
      els.moves.textContent = moves; els.best.textContent = L.best.length;
      els.star.textContent = stars[idx] ? "★".repeat(stars[idx]) : "–";
      acts.prev.disabled = idx === 0; acts.next.disabled = idx >= levels.length - 1 || !stars[idx];
      acts.undo.disabled = !history.length || locked;
      acts.wait.disabled = finished || locked || (status.cls === "lose");
      acts.hint.disabled = finished || locked;
    }

    function load(i) {
      idx = i; store("gm_lv", idx); L = levels[idx];
      hero = L.hero; ms = L.monsters.slice(); moves = 0; history = []; finished = false; locked = false; started = false; hintDir = null;
      pos = { h: { r: hero.r, c: hero.c }, m: ms.map(function (m) { return { r: m.r, c: m.c }; }) };
      showOv(false); setStatus(null); hud(); draw();
    }

    // ---- animasyon: parçalar sırayla (kahraman, A1, B1, A2, B2)
    function runAnim(segs, done) {
      locked = true; hud();
      var k = 0, t0 = 0;
      function frame(now) {
        var s = segs[k];
        if (!t0) t0 = now;
        var u = Math.min(1, (now - t0) / s.dur), e = u < 0.5 ? 2 * u * u : 1 - Math.pow(-2 * u + 2, 2) / 2;
        var o = s.who === "h" ? pos.h : pos.m[s.who];
        o.r = s.from.r + (s.to.r - s.from.r) * e; o.c = s.from.c + (s.to.c - s.from.c) * e;
        draw();
        if (u >= 1) { k++; t0 = 0; if (k >= segs.length) { locked = false; raf = 0; done(); return; } }
        raf = requestAnimationFrame(frame);
      }
      raf = requestAnimationFrame(frame);
    }
    var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

    function act(dir) {
      if (locked || finished || status.cls === "lose") return;
      var r = move(L, hero, ms, dir);
      if (!r) { shake = performance.now(); draw(); return; }
      if (!started) { started = true; track("demo_start", { app: "grumblings", difficulty: L.n + "x" + L.n, level: idx + 1 }); }
      history.push({ hero: hero, ms: ms }); moves++; hintDir = null;
      var segs = [];
      if (dir) segs.push({ who: "h", from: { r: hero.r, c: hero.c }, to: r.hero, dur: reduce ? 1 : 150 });
      var cur = ms.map(function (m) { return { r: m.r, c: m.c }; });
      r.steps.forEach(function (s) { segs.push({ who: s.i, from: cur[s.i], to: s.to, dur: reduce ? 1 : 140 }); cur[s.i] = s.to; });
      if (!segs.length) segs.push({ who: "h", from: { r: hero.r, c: hero.c }, to: r.hero, dur: 1 });
      var prevHero = hero; hero = r.hero; ms = r.monsters;
      runAnim(segs, function () {
        pos = { h: { r: hero.r, c: hero.c }, m: ms.map(function (m) { return { r: m.r, c: m.c }; }) };
        if (r.outcome === "WIN") {
          finished = true; var s = starsFor(moves, L.best.length);
          if (!stars[idx] || s > stars[idx]) { stars[idx] = s; store("gm_stars", stars); }
          setStatus("win", "win", " " + "★".repeat(s) + " " + moves + " / " + L.best.length);
          track("demo_end", { app: "grumblings", difficulty: L.n + "x" + L.n, level: idx + 1, result: "win", moves: moves, stars: s });
          if (idx >= levels.length - 1) setStatus("done", "win", " " + "★".repeat(s));
        } else if (r.outcome === "LOSE") {
          setStatus("caught", "lose");
          track("demo_end", { app: "grumblings", difficulty: L.n + "x" + L.n, level: idx + 1, result: "loss", moves: moves });
        } else setStatus(null);
        hud(); draw();
        showOv(r.outcome === "WIN" || r.outcome === "LOSE");
      });
    }
    function undo() {
      if (locked || !history.length) return;
      var h = history.pop(); hero = h.hero; ms = h.ms; moves = Math.max(0, moves - 1); finished = false; hintDir = null;
      pos = { h: { r: hero.r, c: hero.c }, m: ms.map(function (m) { return { r: m.r, c: m.c }; }) };
      showOv(false); setStatus(null); hud(); draw();
    }
    function hint() {
      if (locked || finished) return;
      var sol = solve(L, hero, ms);
      if (!sol) { setStatus("nohint", "lose"); return; }
      hintDir = sol[0]; setStatus("hintTxt", "", ""); hud(); draw();
    }

    // ---- çizim
    function size() {
      var w = Math.max(220, Math.round(cv.clientWidth || 300)), dpr = Math.min(window.devicePixelRatio || 1, 2);
      if (W !== w * dpr) { W = w * dpr; cv.width = W; cv.height = W; }
      return W;
    }
    function rr(x, y, w, h, r) { ctx.beginPath(); ctx.moveTo(x + r, y); ctx.arcTo(x + w, y, x + w, y + h, r); ctx.arcTo(x + w, y + h, x, y + h, r); ctx.arcTo(x, y + h, x, y, r); ctx.arcTo(x, y, x + w, y, r); ctx.closePath(); }
    function draw() {
      var S = size(), n = L.n, pad = S * 0.025, cs = (S - 2 * pad) / n, r, c, now = performance.now();
      ctx.clearRect(0, 0, S, S);
      ctx.fillStyle = "#EAD3B4"; rr(0, 0, S, S, S * 0.05); ctx.fill();
      var ox = pad, oy = pad;
      for (r = 0; r < n; r++) for (c = 0; c < n; c++) { ctx.fillStyle = (r + c) % 2 ? "#E2C9A6" : "#EAD3B4"; ctx.fillRect(ox + c * cs, oy + r * cs, cs + 0.5, cs + 0.5); }
      // çıkış kapısı
      var ex = ox + (L.exit.c + 0.5) * cs, ey = oy + (L.exit.r + 0.5) * cs, pulse = 1 + 0.06 * Math.sin(now / 260);
      ctx.fillStyle = "#E8478B"; ctx.beginPath(); ctx.arc(ex, ey, cs * 0.36 * pulse, 0, 7); ctx.fill();
      ctx.fillStyle = "#FFC1DA"; ctx.beginPath(); ctx.arc(ex, ey, cs * 0.22 * pulse, 0, 7); ctx.fill();
      ctx.fillStyle = "#FFF8EC"; ctx.beginPath(); ctx.arc(ex, ey, cs * 0.09, 0, 7); ctx.fill();
      // canavar planı: kahraman beklerse canavarların iki adımı
      if (previewOn && !finished && !locked) {
        var sim = ms.map(function (m) { return { r: m.r, c: m.c }; });
        ctx.save(); ctx.globalAlpha = 0.55;
        for (var t = 0; t < 2; t++) for (var i = 0; i < sim.length; i++) {
          var a = sim[i], b = monsterStep(L, hero, sim, i);
          ctx.strokeStyle = L.axes[i] === "H" ? "#E4572E" : "#3E6FB0"; ctx.lineWidth = cs * 0.09; ctx.lineCap = "round";
          ctx.beginPath(); ctx.moveTo(ox + (a.c + 0.5) * cs, oy + (a.r + 0.5) * cs); ctx.lineTo(ox + (b.c + 0.5) * cs, oy + (b.r + 0.5) * cs); ctx.stroke();
          sim[i] = b;
        }
        for (i = 0; i < sim.length; i++) { ctx.fillStyle = L.axes[i] === "H" ? "#E4572E" : "#3E6FB0"; ctx.beginPath(); ctx.arc(ox + (sim[i].c + 0.5) * cs, oy + (sim[i].r + 0.5) * cs, cs * 0.16, 0, 7); ctx.fill(); }
        ctx.restore();
      }
      // duvarlar
      ctx.strokeStyle = "#8A5A3C"; ctx.lineWidth = cs * 0.13; ctx.lineCap = "round";
      ctx.beginPath();
      for (r = 0; r < n; r++) for (c = 0; c < n; c++) {
        if (L.v[r][c] && c < n - 1) { ctx.moveTo(ox + (c + 1) * cs, oy + r * cs); ctx.lineTo(ox + (c + 1) * cs, oy + (r + 1) * cs); }
        if (L.h[r][c] && r < n - 1) { ctx.moveTo(ox + c * cs, oy + (r + 1) * cs); ctx.lineTo(ox + (c + 1) * cs, oy + (r + 1) * cs); }
      }
      ctx.stroke();
      ctx.strokeStyle = "#8A5A3C"; ctx.lineWidth = cs * 0.13; rr(ox, oy, n * cs, n * cs, cs * 0.12); ctx.stroke();
      // canavarlar
      for (var k = 0; k < pos.m.length; k++) monster(ox, oy, cs, pos.m[k], L.axes[k]);
      // kahraman (hafif sarsıntı: geçersiz hamle)
      var sh = shake && now - shake < 220 ? Math.sin((now - shake) / 18) * cs * 0.06 : 0;
      hero_(ox + sh, oy, cs, pos.h, finished);
      // ipucu oku
      if (hintDir) {
        var d = DIRS[hintDir] || [0, 0], hx = ox + (pos.h.c + 0.5) * cs, hy = oy + (pos.h.r + 0.5) * cs, w = Math.sin(now / 160) * cs * 0.05;
        ctx.fillStyle = "#E8478B";
        if (hintDir === "W") { ctx.beginPath(); ctx.arc(hx, hy, cs * 0.46 + w, 0, 7); ctx.lineWidth = cs * 0.07; ctx.strokeStyle = "#E8478B"; ctx.stroke(); }
        else {
          var tx = hx + d[1] * cs * (0.62 + w / cs), ty = hy + d[0] * cs * (0.62 + w / cs);
          ctx.beginPath(); ctx.moveTo(tx + d[1] * cs * 0.22, ty + d[0] * cs * 0.22); ctx.lineTo(tx - d[0] * cs * 0.18 - d[1] * cs * 0.05, ty - d[1] * cs * 0.18 - d[0] * cs * 0.05);
          ctx.lineTo(tx + d[0] * cs * 0.18 - d[1] * cs * 0.05, ty + d[1] * cs * 0.18 - d[0] * cs * 0.05); ctx.closePath(); ctx.fill();
        }
      }
    }
    function hero_(ox, oy, cs, p, happy) {
      var x = ox + (p.c + 0.5) * cs, y = oy + (p.r + 0.5) * cs, rad = cs * 0.3;
      ctx.fillStyle = "rgba(90,58,34,.25)"; ctx.beginPath(); ctx.ellipse(x + rad * 0.15, y + rad * 0.95, rad * 0.9, rad * 0.35, 0, 0, 7); ctx.fill();
      var g = ctx.createRadialGradient(x - rad * 0.3, y - rad * 0.4, rad * 0.1, x, y, rad * 1.2); g.addColorStop(0, "#FFF0A0"); g.addColorStop(1, "#FFD23F");
      ctx.fillStyle = g; ctx.beginPath(); ctx.arc(x, y, rad, 0, 7); ctx.fill();
      ctx.strokeStyle = "#4A2F27"; ctx.lineWidth = rad * 0.1; ctx.lineCap = "round"; ctx.beginPath(); ctx.moveTo(x, y - rad * 0.95); ctx.lineTo(x + rad * 0.15, y - rad * 1.3); ctx.stroke();
      ctx.fillStyle = "#4A2F27"; ctx.beginPath(); ctx.arc(x - rad * 0.35, y - rad * 0.1, rad * 0.12, 0, 7); ctx.arc(x + rad * 0.35, y - rad * 0.1, rad * 0.12, 0, 7); ctx.fill();
      ctx.beginPath(); ctx.arc(x, y + rad * (happy ? 0.12 : 0.2), rad * 0.3, 0.1 * Math.PI, 0.9 * Math.PI); ctx.stroke();
    }
    function monster(ox, oy, cs, p, axis) {
      var x = ox + (p.c + 0.5) * cs, y = oy + (p.r + 0.5) * cs, s = cs * 0.62, col = axis === "H" ? "#E4572E" : "#3E6FB0";
      ctx.fillStyle = "rgba(90,58,34,.25)"; ctx.beginPath(); ctx.ellipse(x + s * 0.08, y + s * 0.5, s * 0.5, s * 0.17, 0, 0, 7); ctx.fill();
      ctx.fillStyle = col; rr(x - s / 2, y - s / 2, s, s, s * 0.3); ctx.fill();
      ctx.fillStyle = "#FFF8EC"; ctx.beginPath(); ctx.arc(x - s * 0.2, y - s * 0.12, s * 0.12, 0, 7); ctx.arc(x + s * 0.2, y - s * 0.12, s * 0.12, 0, 7); ctx.fill();
      ctx.fillStyle = "#4A2F27"; ctx.beginPath(); ctx.arc(x - s * 0.2, y - s * 0.1, s * 0.055, 0, 7); ctx.arc(x + s * 0.2, y - s * 0.1, s * 0.055, 0, 7); ctx.fill();
      ctx.strokeStyle = "#4A2F27"; ctx.lineWidth = s * 0.07; ctx.lineCap = "round";
      ctx.beginPath(); ctx.moveTo(x - s * 0.34, y - s * 0.34); ctx.lineTo(x - s * 0.1, y - s * 0.24); ctx.moveTo(x + s * 0.34, y - s * 0.34); ctx.lineTo(x + s * 0.1, y - s * 0.24); ctx.stroke();
      // karındaki ok: yatay önce / dikey önce
      ctx.fillStyle = "rgba(255,248,236,.9)"; ctx.beginPath();
      if (axis === "H") { ctx.moveTo(x - s * 0.2, y + s * 0.2); ctx.lineTo(x + s * 0.08, y + s * 0.2); ctx.lineTo(x + s * 0.08, y + s * 0.12); ctx.lineTo(x + s * 0.24, y + s * 0.26); ctx.lineTo(x + s * 0.08, y + s * 0.4); ctx.lineTo(x + s * 0.08, y + s * 0.32); ctx.lineTo(x - s * 0.2, y + s * 0.32); }
      else { ctx.moveTo(x - s * 0.06, y + s * 0.14); ctx.lineTo(x + s * 0.06, y + s * 0.14); ctx.lineTo(x + s * 0.06, y + s * 0.3); ctx.lineTo(x + s * 0.14, y + s * 0.3); ctx.lineTo(x, y + s * 0.44); ctx.lineTo(x - s * 0.14, y + s * 0.3); ctx.lineTo(x - s * 0.06, y + s * 0.3); }
      ctx.closePath(); ctx.fill();
    }

    // ---- girdiler
    var KEYS = { ArrowUp: "U", ArrowDown: "D", ArrowLeft: "L", ArrowRight: "R", w: "U", s: "D", a: "L", d: "R", W: "U", S: "D", A: "L", D: "R" };
    cv.addEventListener("keydown", function (e) {
      if (KEYS[e.key]) { e.preventDefault(); act(KEYS[e.key]); } else if (e.key === " " || e.key === "Enter") { e.preventDefault(); act(null); } else if (e.key === "z" || e.key === "Z") undo();
    });
    var tx0 = null, ty0 = null;
    cv.addEventListener("pointerdown", function (e) { tx0 = e.clientX; ty0 = e.clientY; cv.focus({ preventScroll: true }); });
    cv.addEventListener("pointerup", function (e) {
      if (tx0 === null) return;
      var dx = e.clientX - tx0, dy = e.clientY - ty0; tx0 = null;
      if (Math.max(Math.abs(dx), Math.abs(dy)) > 24) { act(Math.abs(dx) > Math.abs(dy) ? (dx > 0 ? "R" : "L") : (dy > 0 ? "D" : "U")); return; }
      var rect = cv.getBoundingClientRect(), n = L.n, cs = rect.width / n;
      var c = Math.floor((e.clientX - rect.left) / cs), r = Math.floor((e.clientY - rect.top) / cs);
      var dr = r - hero.r, dc = c - hero.c;
      if (dr === 0 && dc === 0) act(null);
      else if (Math.abs(dr) + Math.abs(dc) === 1) act(dr === -1 ? "U" : dr === 1 ? "D" : dc === -1 ? "L" : "R");
    });
    root.addEventListener("click", function (e) {
      var b = e.target.closest("[data-act]"); if (!b || b.disabled) return;
      var a = b.getAttribute("data-act");
      if (a === "ov1" || a === "ov2") {
        if (finished) { if (a === "ov1" && idx < levels.length - 1) load(idx + 1); else load(idx); }
        else if (a === "ov1") undo(); else load(idx);
        return;
      }
      if (a === "wait") act(null); else if (a === "undo") undo(); else if (a === "restart") load(idx); else if (a === "hint") hint();
      else if (a === "preview") { previewOn = !previewOn; b.setAttribute("aria-pressed", previewOn); text(); draw(); }
      else if (a === "prev" && idx > 0) load(idx - 1); else if (a === "next" && idx < levels.length - 1 && stars[idx]) load(idx + 1);
    });
    if (window.ResizeObserver) new ResizeObserver(function () { W = 0; draw(); }).observe(cv);
    // kapı nabzı için hafif döngü (yalnız görünürken, hareket azaltma açıksa yok)
    if (!reduce) setInterval(function () { if (!locked && document.visibilityState === "visible" && cv.getBoundingClientRect().width) draw(); }, 120);
    new MutationObserver(text).observe(document.documentElement, { attributes: true, attributeFilter: ["lang", "data-lang", "class"] });
    previewOn = false;
    load(idx);
  }

  api.mount = mount;
  window.GRUMBLINGS = api;
  function auto() { [].forEach.call(document.querySelectorAll("[data-grumblings]"), mount); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto); else auto();
})();
