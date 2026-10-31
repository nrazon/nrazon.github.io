// ttt.js yapay zekâ testleri:  node tools/ttt.test.js   (uygulamadaki Game.kt ile aynı kurallar)
const assert = require("assert");
const { winnerOf, empties, over, aiMove } = require("../ttt.js");

let n = 0;
function ok(name, fn) { fn(); n++; console.log("  ok  " + name); }

// Küçük, tohumlanabilir rastgele sayı üretici (deterministik testler)
function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

function playGame(diff, starter, humanPick, rnd) {
  const cells = Array(9).fill(null);
  let turn = starter;
  while (!over(cells)) {
    const m = turn === "X" ? humanPick(cells, rnd) : aiMove(cells, diff, rnd);
    assert.strictEqual(cells[m], null, "dolu hücreye oynandı");
    cells[m] = turn;
    turn = turn === "X" ? "O" : "X";
  }
  const w = winnerOf(cells);
  return w ? w.mark : "-";
}
const randomHuman = (cells, rnd) => empties(cells)[Math.floor(rnd() * empties(cells).length)];

ok("winnerOf / over temel", () => {
  assert.strictEqual(winnerOf(["X", "X", "X", null, null, null, null, null, null]).mark, "X");
  assert.deepStrictEqual(winnerOf([null, "O", null, null, "O", null, null, "O", null]).line, [1, 4, 7]);
  assert.strictEqual(winnerOf(Array(9).fill(null)), null);
  assert.strictEqual(over(["X", "O", "X", "X", "O", "O", "O", "X", "X"]), true); // beraberlik
});

ok("orta ve zor kazanma fırsatını kullanır, rakibi engeller", () => {
  const winO = ["O", "O", null, "X", "X", null, null, null, null]; // O 2'de kazanır (X de 5'te kazanabilir)
  for (const d of ["medium", "hard"]) for (let i = 0; i < 50; i++) assert.strictEqual(aiMove(winO, d, rng(i)), 2, d + " kazanmadı");
  const block = ["X", "X", null, null, "O", null, null, null, null]; // X 2'de kazanır, O engellemeli
  for (const d of ["medium", "hard"]) for (let i = 0; i < 50; i++) assert.strictEqual(aiMove(block, d, rng(i)), 2, d + " engellemedi");
});

ok("hamle hep boş hücredir (3 seviye, 2000 rastgele konum)", () => {
  const r = rng(7);
  for (const d of ["easy", "medium", "hard"]) for (let k = 0; k < 2000; k++) {
    const cells = Array(9).fill(null); const moves = Math.floor(r() * 7);
    for (let m = 0; m < moves; m++) { const e = empties(cells); cells[e[Math.floor(r() * e.length)]] = m % 2 ? "O" : "X"; }
    if (over(cells)) continue;
    assert.strictEqual(cells[aiMove(cells, d, r)], null);
  }
});

ok("ZOR yenilmez: rastgele insan, iki başlangıç, 3000 oyun", () => {
  const r = rng(11);
  let humanWins = 0;
  for (const starter of ["X", "O"]) for (let g = 0; g < 1500; g++) if (playGame("hard", starter, randomHuman, r) === "X") humanWins++;
  assert.strictEqual(humanWins, 0, "zor seviyede insan kazandı: " + humanWins);
});

ok("ZOR yenilmez: insanın TÜM olası oyunları (bilgisayarın rastgele eşit hamleleri 5 kez denendi)", () => {
  // Yalnız insan dallanır; bilgisayar rastgele (tohumlu) eşit iyi hamleyi seçer.
  function walk(cells, turn, rnd) {
    if (over(cells)) { const w = winnerOf(cells); assert.notStrictEqual(w && w.mark, "X", "insan kazandı: " + cells.join(",")); return; }
    if (turn === "O") { const c = cells.slice(); c[aiMove(cells, "hard", rnd)] = "O"; walk(c, "X", rnd); return; }
    for (const i of empties(cells)) { const c = cells.slice(); c[i] = "X"; walk(c, "O", rnd); }
  }
  for (let s = 1; s <= 5; s++) { walk(Array(9).fill(null), "X", rng(s)); walk(Array(9).fill(null), "O", rng(100 + s)); }
});

// Akıllı insan: X için kusursuz hamle (zor yapay zekânın aynası: işaretler değiş tokuş edilir).
const swap = (m) => (m === "X" ? "O" : m === "O" ? "X" : null);
const perfectHuman = (cells, rnd) => aiMove(cells.map(swap), "hard", rnd);

ok("ORTA yenilebilir (çatalı bilmez): kusursuz insan 2000 oyunda çok kazanır; rastgele insan da kazanabilir", () => {
  const r = rng(21); let smart = 0, rand = 0;
  for (let g = 0; g < 2000; g++) if (playGame("medium", g % 2 ? "X" : "O", perfectHuman, r) === "X") smart++;
  for (let g = 0; g < 5000; g++) if (playGame("medium", g % 2 ? "X" : "O", randomHuman, r) === "X") rand++;
  assert.ok(smart > 200, "orta seviye akıllı insanı yenemiyor olmalı: " + smart);
  assert.ok(rand > 20, "orta seviyeyi rastgele insan hiç yenemedi: " + rand);
  console.log("        orta: akıllı insan " + smart + "/2000, rastgele insan " + rand + "/5000 kazandı");
});

ok("ZOR: kusursuz insana karşı da yenilmez (hep berabere)", () => {
  const r = rng(41); let humanWins = 0, draws = 0;
  for (let g = 0; g < 400; g++) { const res = playGame("hard", g % 2 ? "X" : "O", perfectHuman, r); if (res === "X") humanWins++; if (res === "-") draws++; }
  assert.strictEqual(humanWins, 0);
  assert.strictEqual(draws, 400, "kusursuz iki oyuncu hep berabere kalmalı: " + draws);
});

ok("KOLAY: rastgele insan sık kazanır, zordan çok", () => {
  const r = rng(31); let easy = 0, med = 0;
  for (let g = 0; g < 4000; g++) { if (playGame("easy", g % 2 ? "X" : "O", randomHuman, r) === "X") easy++; if (playGame("medium", g % 2 ? "X" : "O", randomHuman, r) === "X") med++; }
  assert.ok(easy > med, "kolay (" + easy + ") ortadan (" + med + ") kolay değil");
  assert.ok(easy / 4000 > 0.25, "kolay çok zor: " + easy);
  console.log("        kolay: " + easy + "/4000, orta: " + med + "/4000");
});

console.log(n + " test geçti");
