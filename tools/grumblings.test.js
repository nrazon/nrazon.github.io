// grumblings.js kural motoru ve çözücü testleri:  node tools/grumblings.test.js   (uygulamadaki Maze.kt / MazeTest.kt ile aynı kurallar)
const assert = require("assert");
const fs = require("fs");
const path = require("path");
const G = require("../grumblings.js");

let n = 0;
function ok(name, fn) { fn(); n++; console.log("  ok  " + name); }

/** MazeTest.kt'deki yardımcının karşılığı: duvarlar [[r1,c1],[r2,c2]] çiftleri. */
function maze(rows, exit, axes, ...walls) {
  const v = [], h = [];
  for (let r = 0; r < rows; r++) { v.push(Array(rows).fill(false)); h.push(Array(rows).fill(false)); }
  for (const [a, b] of walls) { if (a[0] === b[0]) v[a[0]][Math.min(a[1], b[1])] = true; else h[Math.min(a[0], b[0])][a[1]] = true; }
  return { n: rows, v, h, exit: { r: exit[0], c: exit[1] }, axes, hero: { r: 0, c: 0 }, monsters: [], best: "" };
}
// MazeTest.kt tek satırlı (1xN) labirentler kullanır; JS motoru kare ızgara varsayar: kareye genişletip ek satırları duvarla kapat.
function strip(cols, exit, axes, ...walls) {
  const L = maze(cols, exit, axes, ...walls);
  for (let r = 1; r < cols; r++) for (let c = 0; c < cols; c++) L.h[r - 1][c] = true; // satır 0 dışını kapat
  return L;
}
const C = (r, c) => ({ r, c });

ok("canavar önce yatay gider; dikey eksenli önce dikey", () => {
  const L = strip(5, [0, 4], ["H"]);
  assert.deepStrictEqual(G.monsterStep(L, C(0, 0), [C(0, 4)], 0), C(0, 3));
  const L2 = maze(3, [0, 0], ["V"]);
  assert.deepStrictEqual(G.monsterStep(L2, C(0, 0), [C(2, 2)], 0), C(1, 2));
  const L3 = maze(3, [0, 0], ["H"]);
  assert.deepStrictEqual(G.monsterStep(L3, C(0, 0), [C(2, 2)], 0), C(2, 1));
});

ok("ilk adımda yakalarsa ikinci adım atılmaz", () => {
  const L = strip(5, [0, 4], ["H"]);
  const r = G.move(L, C(0, 1), [C(0, 3)], null);
  assert.strictEqual(r.outcome, "LOSE"); assert.strictEqual(r.steps.length, 2);
  const r2 = G.move(L, C(0, 2), [C(0, 3)], null);
  assert.strictEqual(r2.outcome, "LOSE"); assert.strictEqual(r2.steps.length, 1);
});

ok("çıkışa varan kahraman kazanır, canavar oynamaz", () => {
  const L = strip(5, [0, 4], ["H"]);
  const r = G.move(L, C(0, 3), [C(0, 0)], "R");
  assert.strictEqual(r.outcome, "WIN"); assert.deepStrictEqual(r.monsters, [C(0, 0)]);
});

ok("engellenen yatay adım dikeye düşer; tamamen sıkışan yerinde durur", () => {
  const L3 = maze(3, [1, 2], ["H"], [[0, 1], [0, 2]]);
  assert.deepStrictEqual(G.monsterStep(L3, C(1, 0), [C(0, 2)], 0), C(1, 2));
  const stuck = strip(3, [0, 0], ["H"], [[0, 1], [0, 2]]);
  assert.deepStrictEqual(G.monsterStep(stuck, C(0, 0), [C(0, 2)], 0), C(0, 2));
});

ok("geçersiz hamle (duvar/kenar) null döner", () => {
  const L = strip(3, [0, 2], ["H"]);
  assert.strictEqual(G.move(L, C(0, 0), [C(0, 2)], "U"), null);
  assert.strictEqual(G.move(L, C(0, 0), [C(0, 2)], "L"), null);
});

ok("iki canavar sıralı hareket eder (A1, B1, A2, B2)", () => {
  const L = maze(5, [2, 4], ["H", "V"]); // 5x5: satır 0-2 kullanılır
  const r = G.move(L, C(0, 0), [C(0, 4), C(2, 0)], null);
  assert.strictEqual(r.outcome, "LOSE");
  assert.deepStrictEqual(r.steps.map(s => s.i), [0, 1, 0, 1]);
  assert.deepStrictEqual(r.steps[r.steps.length - 1].to, C(0, 0));
});

ok("canavar başka canavarın hücresine giremez", () => {
  const L = strip(6, [0, 5], ["H", "H"]);
  const r = G.move(L, C(0, 0), [C(0, 4), C(0, 5)], null);
  assert.strictEqual(r.outcome, "GO"); assert.deepStrictEqual(r.monsters, [C(0, 2), C(0, 3)]);
});

ok("yıldız kuralı uygulamayla aynı", () => {
  assert.strictEqual(G.starsFor(7, 7), 3); assert.strictEqual(G.starsFor(8, 7), 2); assert.strictEqual(G.starsFor(9, 7), 2);
  assert.strictEqual(G.starsFor(10, 7), 1); assert.strictEqual(G.starsFor(4, 4), 3); assert.strictEqual(G.starsFor(6, 4), 2); assert.strictEqual(G.starsFor(7, 4), 1);
  assert.strictEqual(G.starsFor(20, 16), 2); assert.strictEqual(G.starsFor(21, 16), 1); // büyük çözümde pay optimal/4
});

ok("gömülü her bölüm: en iyi çözüm kazandırır ve çözücünün en kısasıyla aynı uzunlukta", () => {
  assert.ok(G.LEVELS.length >= 20);
  G.LEVELS.forEach((line, i) => {
    const L = G.decode(line);
    let h = L.hero, ms = L.monsters, out = null;
    for (const ch of L.best) {
      const r = G.move(L, h, ms, ch === "W" ? null : ch);
      assert.ok(r, "bölüm " + (i + 1) + ": geçersiz hamle " + ch);
      assert.notStrictEqual(r.outcome, "LOSE", "bölüm " + (i + 1) + ": yakalandı");
      out = r.outcome; h = r.hero; ms = r.monsters;
    }
    assert.strictEqual(out, "WIN", "bölüm " + (i + 1) + " kazanmadı");
    const sol = G.solve(L, L.hero, L.monsters);
    assert.strictEqual(sol.length, L.best.length, "bölüm " + (i + 1) + ": çözücü " + sol.length + ", paket " + L.best.length);
  });
});

ok("gömülü bölümler uygulamanın levels.txt dosyasının ilk satırlarıyla aynı (dosya varsa)", () => {
  const p = path.join(__dirname, "..", "..", "Grumblings", "app", "src", "main", "assets", "levels.txt");
  if (!fs.existsSync(p)) { console.log("      (levels.txt yok, atlandı)"); return; }
  const lines = fs.readFileSync(p, "utf8").split(/\r?\n/).filter(Boolean);
  G.LEVELS.forEach((l, i) => assert.strictEqual(l, lines[i], "satır " + (i + 1)));
});

console.log(n + " test geçti");
