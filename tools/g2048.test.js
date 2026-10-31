// g2048.js kural testleri:  node tools/g2048.test.js   (uygulamadaki Game.kt ile aynı kurallar)
const assert = require("assert");
const G = require("../g2048.js");

let n = 0;
function ok(name, fn) { fn(); n++; console.log("  ok  " + name); }
function rng(seed) { let s = seed >>> 0; return () => ((s = (s * 1664525 + 1013904223) >>> 0) / 4294967296); }

// 4x4 diziden (0 = boş) taş listesi; satır satır kimlik
function fromRows(rows) {
  const tiles = []; let id = 1;
  rows.forEach((row, r) => row.forEach((v, c) => { if (v) tiles.push({ id: id++, v, r, c }); }));
  return { tiles, nextId: id };
}
function toRows(tiles) {
  const rows = [0, 1, 2, 3].map(() => [0, 0, 0, 0]);
  tiles.forEach((t) => { assert.strictEqual(rows[t.r][t.c], 0, "aynı hücrede iki taş"); rows[t.r][t.c] = t.v; });
  return rows;
}
function slideRows(rows, dir) { const s = fromRows(rows); const r = G.slide(s.tiles, dir, s.nextId); return { rows: toRows(r.tiles), gained: r.gained, moved: r.moved }; }

ok("sola: [2,2,2,2] -> [4,4,0,0], kazanç 8", () => {
  const r = slideRows([[2, 2, 2, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left");
  assert.deepStrictEqual(r.rows[0], [4, 4, 0, 0]); assert.strictEqual(r.gained, 8); assert.ok(r.moved);
});
ok("her taş bir hamlede en fazla bir kez birleşir: [2,2,4,0] -> [4,4,0,0]; [4,2,2,0] -> [4,4,0,0]; [2,2,2,0] -> [4,2,0,0]", () => {
  assert.deepStrictEqual(slideRows([[2, 2, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").rows[0], [4, 4, 0, 0]);
  assert.deepStrictEqual(slideRows([[4, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").rows[0], [4, 4, 0, 0]);
  assert.deepStrictEqual(slideRows([[2, 2, 2, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").rows[0], [4, 2, 0, 0]);
  assert.deepStrictEqual(slideRows([[4, 4, 4, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").rows[0], [8, 8, 0, 0]);
});
ok("aralıklı taşlar: [2,0,0,2] -> [4,0,0,0]; sağa [2,0,2,4] -> [0,0,4,4]", () => {
  assert.deepStrictEqual(slideRows([[2, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").rows[0], [4, 0, 0, 0]);
  assert.deepStrictEqual(slideRows([[2, 0, 2, 4], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "right").rows[0], [0, 0, 4, 4]);
});
ok("dört yön simetrik (yukarı/aşağı sütun üzerinde sola/sağa gibi)", () => {
  const rows = [[2, 0, 4, 0], [2, 4, 0, 0], [0, 4, 0, 2], [4, 0, 0, 2]];
  const tr = (m) => m[0].map((_, c) => m.map((row) => row[c]));
  const up = slideRows(rows, "up").rows, leftOfT = slideRows(tr(rows), "left").rows;
  assert.deepStrictEqual(up, tr(leftOfT));
  const down = slideRows(rows, "down").rows, rightOfT = slideRows(tr(rows), "right").rows;
  assert.deepStrictEqual(down, tr(rightOfT));
});
ok("değişmeyen hamle moved=false (hamle sayılmaz)", () => {
  assert.strictEqual(slideRows([[2, 4, 8, 16], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], "left").moved, false);
  const s = fromRows([[2, 4, 8, 16], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]);
  const st = { tiles: s.tiles, nextId: s.nextId, score: 0, status: "playing", keep: false, moves: 0 };
  assert.strictEqual(G.move(st, "left", rng(1)), null);
});
ok("canMove: dolu ve birleşmez tahta oyun bitmiş; yan yana eşit varsa devam", () => {
  const dead = fromRows([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]);
  assert.strictEqual(G.canMove(dead.tiles), false);
  const alive = fromRows([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 4]]);
  assert.strictEqual(G.canMove(alive.tiles), true);
  assert.strictEqual(G.canMove(fromRows([[2, 4, 2, 0], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]).tiles), true);
});
ok("yeni taş: %90 iki, %10 dört (20000 örnek), boş hücreye, hiç çakışmaz", () => {
  const r = rng(5); let fours = 0;
  for (let i = 0; i < 20000; i++) { const sp = G.spawn([], 1, r); assert.strictEqual(sp.tiles.length, 1); if (sp.tiles[0].v === 4) fours++; else assert.strictEqual(sp.tiles[0].v, 2); }
  assert.ok(fours > 1700 && fours < 2300, "%10 dört bekleniyordu: " + fours);
  const full = fromRows([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]]);
  assert.strictEqual(G.spawn(full.tiles, full.nextId, r).spawned, null);
});
ok("yeni oyun iki taşla başlar; 5000 rastgele oyunda kural bozulmaz (çakışma yok, skor artar, bitince hamle yok)", () => {
  const r = rng(9);
  for (let g = 0; g < 300; g++) {
    let s = G.newGame(r); assert.strictEqual(s.tiles.length, 2);
    let guard = 0;
    while (s.status === "playing" && guard++ < 5000) {
      const dirs = ["up", "down", "left", "right"].sort(() => r() - 0.5); let mv = null;
      for (const d of dirs) { mv = G.move(s, d, r); if (mv) break; }
      if (!mv) { assert.strictEqual(G.canMove(s.tiles), false, "hamle yok ama canMove true"); break; }
      assert.ok(mv.state.score >= s.score && mv.state.moves === s.moves + 1);
      toRows(mv.state.tiles); // çakışma kontrolü
      s = mv.state;
      if (s.status === "won") { s = Object.assign({}, s, { status: "playing", keep: true }); }
    }
    assert.notStrictEqual(s.status, "playing", "oyun hiç bitmedi");
  }
});
ok("2048'e ulaşınca 'won' (devam et denene kadar hamle yok); keep ile bir daha çıkmaz", () => {
  const s = fromRows([[1024, 1024, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]);
  const st = { tiles: s.tiles, nextId: s.nextId, score: 0, status: "playing", keep: false, moves: 0 };
  const mv = G.move(st, "left", rng(3));
  assert.strictEqual(mv.state.status, "won");
  assert.strictEqual(G.move(mv.state, "left", rng(3)), null, "won durumunda hamle olmamalı");
  const st2 = Object.assign({}, st, { keep: true });
  assert.strictEqual(G.move(st2, "left", rng(3)).state.status, "playing");
});
ok("birleşen taşlar için ghost üretilir ve yeni taş kimliği ayrıdır", () => {
  const s = fromRows([[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]);
  const r = G.slide(s.tiles, "left", s.nextId);
  assert.strictEqual(r.ghosts.length, 2); assert.strictEqual(r.merged.length, 1);
  assert.ok(r.tiles.every((t) => t.id !== 1 && t.id !== 2), "birleşen taşın kimliği yeni olmalı");
});

console.log(n + " test geçti");
