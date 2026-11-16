// node tools/cekilis.test.js  (github-pages kokunden)
const assert = require("assert");
const { draw, encode, decode } = require("../cekilis/draw.js");

function check(names, excl, label) {
  for (let t = 0; t < 400; t++) {
    const r = draw(names, excl);
    assert(r, label + ": cekilis bulunamadi");
    const seen = new Set();
    for (const g of names) {
      const a = r.map[g];
      assert(a && a !== g, label + ": kendini cekti");
      assert(!seen.has(a), label + ": ayni kisi iki kez cekildi");
      seen.add(a);
    }
    for (const [x, y] of excl) { assert(r.map[x] !== y && r.map[y] !== x, label + ": yasakli eslesme"); }
    if (r.cycle) { // tek dongu: baslangictan n adimda donmeli ve karsilikli eslesme olmamali (n>2)
      let cur = names[0], steps = 0;
      do { cur = r.map[cur]; steps++; } while (cur !== names[0] && steps <= names.length);
      assert.strictEqual(steps, names.length, label + ": tek dongu degil");
    }
  }
}

const mk = (n) => Array.from({ length: n }, (_, i) => "K" + i);
check(mk(3), [], "3 kisi");
check(mk(4), [["K0", "K1"]], "4 kisi, 1 kisit");
check(mk(10), [["K0", "K1"], ["K2", "K3"], ["K4", "K5"]], "10 kisi, ciftler");
check(mk(50), [["K0", "K1"], ["K2", "K3"]], "50 kisi");
// imkansiz: 3 kisi, A herkesle yasak
assert.strictEqual(draw(["A", "B", "C"], [["A", "B"], ["A", "C"]]), null, "imkansiz durum null olmali");
// baglanti verisi (Turkce karakterler)
const obj = { d: "Ofis çekilişi", g: "Şule", a: "Çağlar", b: "500 ₺", t: "24.12.2026", n: "Güzel bir hediye ✨" };
assert.deepStrictEqual(decode(encode(obj)), obj);
console.log("cekilis testleri OK");
