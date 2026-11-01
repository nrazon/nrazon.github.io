// calisan.js hesap motoru testleri:  node tools/calisan.test.js
// Beklenen değerler Android uygulamasının Kotlin testlerinden (MaasHesabiTest, MaasOngorusuTest, TatillerTest) birebir alındı;
// onlar da gerçek bordro ve verginet.net çıktılarından (CalisanAsistani/docs/ALTIN_TEST_VERISI.md).
const assert = require("assert");
const C = require("../calisan.js");
const p = C.P2026;

let n = 0;
function ok(name, fn) { fn(); n++; console.log("  ok  " + name); }
function esit(beklenen, gercek, ad, tol) { assert.ok(Math.abs(beklenen - gercek) <= (tol === undefined ? 0.011 : tol), ad + ": beklenen " + beklenen + " gerçek " + gercek); }
const t = (a, g, y) => C.ld(y || 2026, a, g);
const profil = (o) => Object.assign({ tutar: 0, net: false, emekli: false, giris: null, primAylik: 0, primBaslangicAy: 1, primTaksit: 0, primBirikimli: false, sonBordro: null, maasGunu: 5, maasSonrakiAy: true, zam: null }, o);
const kardes = profil({ tutar: 190000, emekli: true, giris: t(7, 1), primAylik: 8069.68 });

// ------------------------------------------------------------------ MaasHesabi
ok("vergi dilimleri kümülatif", () => {
  esit(25500, C.vergi(p, 170000), "170 bin"); esit(58500, C.vergi(p, 340000), "340 bin"); esit(100200, C.vergi(p, 510000), "510 bin");
});
ok("yuvarla: ondalık kayma 4.211,325 -> 4.211,33; negatif ve tam sayılar", () => {
  assert.strictEqual(C.yuvarla(16845.3 - 12633.975), 4211.33);
  assert.strictEqual(C.yuvarla(1.005), 1.01); assert.strictEqual(C.yuvarla(2.5), 2.5); assert.strictEqual(C.yuvarla(-1.235), -1.24);
});
ok("brütten: 200 bin her ay (Ocak-Aralık) bordro değerleri", () => {
  const s = C.yil(p, Array(12).fill(200000), false);
  const beklenen = [[0, 25500, 142982, 4211.33, 147444.03], [1, 33000, 135482, 4211.33, 139944.03], [2, 41700, 126782, 4211.33, 131244.03],
    [3, 45900, 122582, 4211.33, 127044.03], [5, 45900, 122582, 4211.33, 127044.03], [6, 45900, 122582, 4537.75, 127370.45],
    [7, 45900, 122582, 5615.10, 128447.80], [8, 48300, 120182, 5615.10, 126047.80], [9, 59500, 108982, 5615.10, 114847.80], [11, 59500, 108982, 5615.10, 114847.80]];
  beklenen.forEach((b) => {
    const a = s[b[0]], ad = "ay " + (b[0] + 1);
    esit(28000, a.sgkIsci, ad + " sgk"); esit(2000, a.issizlik, ad + " işsizlik"); esit(1518, a.damgaVergisi, ad + " damga");
    esit(b[1], a.gelirVergisi, ad + " gv"); esit(b[2], a.netOnce, ad + " net"); esit(b[3], a.gvIstisnasi, ad + " gv istisna");
    esit(250.70, a.damgaIstisnasi, ad + " damga istisna"); esit(b[4], a.net, ad + " ele geçen");
  });
  esit(2040000, s[11].devir.gvMatrah, "yıl sonu kümülatif");
  esit(556500, s.reduce((x, a) => x + a.gelirVergisi, 0), "yıllık gv");
  esit(1526173.63, s.reduce((x, a) => x + a.net, 0), "yıllık ele geçen", 0.2);
});
ok("netten brüte 200 bin her ay", () => {
  const s = C.netten(p, 200000, 12, false);
  [[0, 276673.41], [1, 299762.05], [2, 315733.49], [7, 347314.06]].forEach(([i, brut]) => {
    esit(brut, s[i].brut, "brüt ay " + (i + 1), 0.03); esit(200000, s[i].net, "net ay " + (i + 1), 0.02);
  });
  esit(41617.80, s[1].sgkIsci, "sgk tavan"); esit(2972.70, s[1].issizlik, "işsizlik tavan"); esit(490343.95, s[1].devir.gvMatrah, "kümülatif şubat", 0.05);
});
ok("Ağustos 2026 bordrosu: emekli, yıl ortası giriş, kuruşuna", () => {
  const onceki = C.devir(167680.32, C.asgariVergiMatrahi(p));
  const a = C.ay(p, { brut: 190000, emekli: true, ekGvIndirimi: 8069.68, damgaEkMatrah: 2609.39, netEk: 2609.39 - 2589.58 }, onceki);
  esit(14250, a.sgkIsci, "sgdp"); esit(0, a.issizlik, "işsizlik"); esit(167680.32, a.gvMatrah, "gv matrah"); esit(32420.08, a.gelirVergisi, "gelir vergisi");
  esit(1461.91, a.damgaVergisi, "damga"); esit(335360.64, a.devir.gvMatrah, "kümülatif"); esit(4211.33, a.gvIstisnasi, "gv istisna");
  esit(250.70, a.damgaIstisnasi, "damga istisna"); esit(141887.82, a.netOnce, "net istihkak"); esit(146349.85, a.net, "net ödenecek");
});

// ------------------------------------------------------------------ MaasOngorusu
ok("gerçek bordro zinciri Temmuz'dan Aralık'a (kardeşin)", () => {
  const o = C.ongoru(p, kardes, t(10, 12));
  assert.strictEqual(o.ilkAy, 7); assert.deepStrictEqual(o.aylar.map((a) => a.ay), [7, 8, 9, 10, 11, 12]);
  [153617.88, 146349.85, 138021.00, 133496.24, 133496.24, 133496.24].forEach((b, i) => esit(b, o.aylar[i].sonuc.net, o.aylar[i].ay + ". ay net", 0.001));
  o.aylar.forEach((a) => esit(4211.33, a.sonuc.gvIstisnasi, a.ay + ". ay gv istisna", 0.001));
});
ok("dilim geçişleri doğru aylarda işaretlenir", () => {
  const o = C.ongoru(p, kardes, t(7, 20));
  assert.deepStrictEqual(o.aylar.map((a) => a.dilimOrani), [0.15, 0.20, 0.27, 0.27, 0.27, 0.27]);
  assert.deepStrictEqual(o.aylar.map((a) => a.dilimDegisti), [false, true, true, false, false, false]);
  assert.strictEqual(o.siradaki.ay, 7); assert.strictEqual(o.sonrakiGecis.ay, 8);
});
ok("maaş sonraki ayın 5'inde yatar: 31 Ekim'de sıradaki Ekim maaşı", () => {
  const o = C.ongoru(p, kardes, t(10, 31));
  assert.strictEqual(o.siradaki.ay, 10); assert.strictEqual(o.siradakiTarih.getTime(), t(11, 5).getTime()); assert.strictEqual(o.sonraki.ay, 11);
  esit(133496.24, o.siradaki.sonuc.net, "Ekim maaşı"); assert.strictEqual(o.siraIndex, 3); assert.strictEqual(o.seciliIndex, 3);
});
ok("ödeme gününden sonra sıradaki sonraki aya geçer", () => {
  assert.strictEqual(C.ongoru(p, kardes, t(11, 5)).siradaki.ay, 10);
  const o = C.ongoru(p, kardes, t(11, 6));
  assert.strictEqual(o.siradaki.ay, 11); assert.strictEqual(o.siradakiTarih.getTime(), t(12, 5).getTime());
});
ok("maaş aynı ayın sonunda yatıyorsa", () => {
  const pr = Object.assign({}, kardes, { maasSonrakiAy: false, maasGunu: 28 });
  assert.strictEqual(C.ongoru(p, pr, t(10, 20)).siradaki.ay, 10); assert.strictEqual(C.ongoru(p, pr, t(10, 31)).siradaki.ay, 11);
});
ok("ödeme tarihi ayın son gününe sınırlanır", () => {
  const pr = profil({ tutar: 1, maasGunu: 31 });
  assert.strictEqual(C.odemeTarihi(pr, 2026, 1).getTime(), t(2, 28).getTime());
  assert.strictEqual(C.odemeTarihi(Object.assign({}, pr, { maasSonrakiAy: false }), 2026, 2).getTime(), t(2, 28).getTime());
});
ok("Aralık maaşı Ocak'ta yatar; yeni yıl Ocak'ı sonrakidir", () => {
  const o = C.ongoru(p, profil({ tutar: 120000 }), t(12, 20));
  assert.strictEqual(o.siradaki.ay, 12); assert.strictEqual(o.siradakiTarih.getTime(), t(1, 5, 2027).getTime());
  assert.ok(o.yeniYilOcak); assert.strictEqual(o.yeniYilOcak.yil, 2027);
  esit(C.yil(p, Array(12).fill(120000), false)[0].net, o.yeniYilOcak.sonuc.net, "Ocak neti (matrah sıfırdan)");
  assert.ok(o.yeniYilOcak.sonuc.net > o.siradaki.sonuc.net);
});
ok("Ocak'ta yatan maaş geçen yılın Aralık maaşıdır", () => {
  const o = C.ongoru(p, kardes, t(1, 3, 2027), p, p);
  assert.strictEqual(o.siradaki.yil, 2026); assert.strictEqual(o.siradaki.ay, 12); assert.strictEqual(o.siraIndex, -1); assert.strictEqual(o.seciliIndex, 0);
  esit(133496.24, o.siradaki.sonuc.net, "geçen yılın Aralık maaşı"); assert.strictEqual(o.sonraki.ay, 1); assert.strictEqual(o.sonraki.yil, 2027);
});
ok("son bordro: giriş yoksa asgari istisna Ocak'tan sayılır", () => {
  const pr = Object.assign({}, kardes, { giris: null, sonBordro: { yil: 2026, ay: 9, kumulatifGvMatrah: 503040.96 } });
  const o = C.ongoru(p, pr, t(9, 28));
  assert.strictEqual(o.ilkAy, 9); assert.strictEqual(o.siradaki.ay, 9);
  esit(503040.96, o.siradaki.sonuc.devir.gvMatrah, "Eylül sonu KGVM"); esit(40748.93, o.siradaki.sonuc.gelirVergisi, "Eylül gelir vergisi");
  esit(133496.24 - 4211.33 + 5615.10, o.sonraki.sonuc.net, "Ekim neti (giriş yoksa)");
});
ok("son bordro + giriş tarihi bordroyu kuruşuna verir", () => {
  const pr = Object.assign({}, kardes, { sonBordro: { yil: 2026, ay: 9, kumulatifGvMatrah: 503040.96 } });
  const o = C.ongoru(p, pr, t(9, 28));
  esit(138021.00, o.siradaki.sonuc.net, "Eylül neti (bordro)"); esit(133496.24, o.sonraki.sonuc.net, "Ekim neti");
  esit(-4524.76, o.sonraki.sonuc.net - o.siradaki.sonuc.net, "sonraki maaş farkı");
});
ok("yıl başından beri brüt maaş Ocak'tan hesaplanır", () => {
  const o = C.ongoru(p, profil({ tutar: 120000 }), t(3, 15));
  assert.strictEqual(o.ilkAy, 1); assert.strictEqual(o.aylar.length, 12); assert.strictEqual(o.siradaki.ay, 3);
  esit(C.yil(p, Array(12).fill(120000), false)[2].net, o.siradaki.sonuc.net, "Mart neti");
});
ok("net maaş sabit kalır, brüt artar", () => {
  const o = C.ongoru(p, profil({ tutar: 100000, net: true }), t(2, 1));
  o.aylar.forEach((a) => esit(100000, a.sonuc.net, a.ay + ". ay net sabit", 0.02));
  assert.ok(o.aylar[o.aylar.length - 1].sonuc.brut > o.aylar[0].sonuc.brut);
});
ok("prim karşılığında net yüksek olur (ilk ay %15: 1.210,45)", () => {
  const primsiz = C.ongoru(p, Object.assign({}, kardes, { primAylik: 0 }), t(7, 20)), primli = C.ongoru(p, kardes, t(7, 20));
  esit(1210.45, primli.siradaki.sonuc.net - primsiz.siradaki.sonuc.net, "ilk ay prim avantajı"); esit(8069.68, primli.siradaki.primIndirilen, "indirilen prim");
});
ok("geçersiz tutar null döner", () => {
  assert.strictEqual(C.ongoru(p, profil({ tutar: 0 }), t(5, 5)), null); assert.strictEqual(C.ongoru(p, profil({ tutar: NaN }), t(5, 5)), null);
});
ok("dilim yardımcıları", () => {
  assert.strictEqual(C.dilimOrani(p, 0), 0.15); assert.strictEqual(C.dilimOrani(p, 189999.99), 0.15); assert.strictEqual(C.dilimOrani(p, 190000), 0.20);
  assert.strictEqual(C.dilimOrani(p, 400000), 0.27); assert.strictEqual(C.dilimUst(p, 100000), 190000); assert.strictEqual(C.dilimUst(p, 6000000), null);
});
ok("8 taksit yalnız o aylarda uygulanır (Mart-Ekim)", () => {
  const o = C.ongoru(p, profil({ tutar: 190000, primAylik: 6250, primBaslangicAy: 3, primTaksit: 8 }), t(2, 10));
  for (let a = 1; a <= 12; a++) assert.strictEqual(o.aylar.find((x) => x.ay === a).primOdenen, a >= 3 && a <= 10 ? 6250 : 0, "ay " + a);
  assert.strictEqual(o.aylar.filter((a) => a.primIndirilen > 0).length, 8);
  esit(8 * 6250, o.aylar.reduce((x, a) => x + a.primIndirilen, 0), "indirilen toplam", 0.001);
});
ok("tek seferlik büyük ödeme aylık sınırda kesilir (28.500) ve taksit daha avantajlı", () => {
  const pr = profil({ tutar: 190000, primAylik: 50000, primBaslangicAy: 6, primTaksit: 1 });
  const o = C.ongoru(p, pr, t(5, 10)), haz = o.aylar.find((a) => a.ay === 6);
  assert.strictEqual(haz.primOdenen, 50000); assert.strictEqual(haz.primIndirilen, 28500);
  const taksitle = C.ongoru(p, Object.assign({}, pr, { primAylik: 6250, primTaksit: 8 }), t(5, 10));
  assert.ok(taksitle.aylar.reduce((x, a) => x + a.primIndirilen, 0) > o.aylar.reduce((x, a) => x + a.primIndirilen, 0));
});
ok("birikimli hayat sigortasında primin yarısı indirilir", () => {
  const risk = C.ongoru(p, profil({ tutar: 100000, primAylik: 4000 }), t(2, 10)), bir = C.ongoru(p, profil({ tutar: 100000, primAylik: 4000, primBirikimli: true }), t(2, 10));
  assert.strictEqual(risk.aylar[0].primIndirilen, 4000); assert.strictEqual(bir.aylar[0].primIndirilen, 2000); assert.strictEqual(bir.aylar[0].primOdenen, 4000);
});
ok("süresiz prim yeni yılda da sürer, süreli taksit yalnız kalanı taşır", () => {
  const sur = C.ongoru(p, profil({ tutar: 120000, primAylik: 3000, primTaksit: 0 }), t(12, 20));
  assert.strictEqual(sur.yeniYilOcak.primOdenen, 3000);
  const sureli = profil({ tutar: 120000, primAylik: 3000, primBaslangicAy: 6, primTaksit: 8 });
  const o = C.ongoru(p, sureli, t(12, 20));
  assert.strictEqual(o.aylar.filter((a) => a.primOdenen > 0).length, 7); assert.strictEqual(o.yeniYilOcak.primOdenen, 3000);
  const yeni = C.yeniYil(p, p, sureli, t(12, 20), 0.0);
  assert.strictEqual(yeni.aylar.filter((a) => a.primOdenen > 0).length, 1); assert.strictEqual(yeni.aylar[0].primOdenen, 3000);
  assert.strictEqual(C.ongoru(p, Object.assign({}, sureli, { primTaksit: 7 }), t(12, 20)).yeniYilOcak.primOdenen, 0);
});
ok("prim planı sınırları", () => {
  const pr = profil({ tutar: 1, primAylik: 100, primBaslangicAy: 4, primTaksit: 3 });
  assert.deepStrictEqual([1, 2, 3, 4, 5, 6, 7].map((a) => C.primAy(pr, a)), [0, 0, 0, 100, 100, 100, 0]);
  assert.strictEqual(C.primAy(pr, 13), 0); assert.strictEqual(C.primAy(Object.assign({}, pr, { primTaksit: 0 }), 13), 100); assert.strictEqual(C.primAy(Object.assign({}, pr, { primAylik: 0 }), 5), 0);
});
ok("zam seçilen aydan itibaren brütü artırır ve yılbaşına taşınır", () => {
  const pr = profil({ tutar: 100000, zam: { ay: 7, oran: 0.10 } });
  const o = C.ongoru(p, pr, t(5, 10));
  assert.strictEqual(o.aylar[5].sonuc.brut, 100000); assert.ok(Math.abs(o.aylar[6].sonuc.brut - 110000) < 1e-6); assert.ok(Math.abs(o.aylar[11].sonuc.brut - 110000) < 1e-6);
  assert.ok(Math.abs(C.ongoru(p, pr, t(12, 20)).yeniYilOcak.sonuc.brut - 110000) < 1e-6);
});
ok("zamlı net zamsızdan yüksek ama brüt artışından az", () => {
  const z0 = C.ongoru(p, profil({ tutar: 100000 }), t(5, 10)), z1 = C.ongoru(p, profil({ tutar: 100000, zam: { ay: 7, oran: 0.20 } }), t(5, 10));
  const f = z1.aylar[6].sonuc.net - z0.aylar[6].sonuc.net; assert.ok(f > 0 && f < 20000);
});
ok("yeni yıl zammı Ocak'tan, matrah sıfırdan hesaplar", () => {
  const pr = profil({ tutar: 120000 }), o = C.yeniYil(p, p, pr, t(10, 31), 0.30);
  assert.strictEqual(o.siradaki.ay, 1); assert.strictEqual(o.aylar.length, 12); assert.ok(Math.abs(o.aylar[0].sonuc.brut - 156000) < 1e-6);
  esit(C.yil(p, Array(12).fill(156000), false)[0].net, o.aylar[0].sonuc.net, "Ocak neti zamlı");
  assert.ok(o.aylar[0].sonuc.net > C.yeniYil(p, p, pr, t(10, 31), 0.0).aylar[0].sonuc.net);
});

// ------------------------------------------------------------------ Tatiller
ok("2026 tatil günleri (17 gün, bayram tarihleri)", () => {
  const l = C.tatilYil(2026); assert.strictEqual(l.length, 17);
  assert.strictEqual(l.find((x) => x.ad === "Ramazan Bayramı Arefesi").tarih.getTime(), t(3, 19).getTime());
  assert.strictEqual(l.find((x) => x.ad === "Kurban Bayramı 4. gün").tarih.getTime(), t(5, 30).getTime());
  assert.strictEqual(l.find((x) => x.ad === "Cumhuriyet Bayramı").tarih.getTime(), t(10, 29).getTime());
});
ok("2033'te Ramazan iki kez (8 gün)", () => {
  const l = C.tatilYil(2033).filter((x) => x.ad.startsWith("Ramazan")).map((x) => x.tarih.getTime());
  assert.strictEqual(l.length, 8); assert.ok(l.includes(t(12, 25, 2033).getTime())); assert.ok(l.includes(t(1, 2, 2033).getTime()));
});
ok("köprü: 2026 Kurban (23-31 Mayıs, 1,5 izin, 9 gün) ve Cumhuriyet (29 Ekim-1 Kasım, 1 izin)", () => {
  const o = C.kopruOnerileri(2026);
  const k = o.find((x) => x.baslangic.getTime() === t(5, 23).getTime() && x.bitis.getTime() === t(5, 31).getTime());
  assert.ok(k); assert.strictEqual(k.izinGunu, 1.5); assert.strictEqual(k.toplamGun, 9);
  assert.ok(o.some((x) => x.baslangic.getTime() === t(10, 29).getTime() && x.bitis.getTime() === t(11, 1).getTime() && x.izinGunu === 1));
});
ok("sıradaki tatil", () => {
  assert.strictEqual(C.tatilSonraki(t(10, 29)).tarih.getTime(), t(10, 29).getTime());
  assert.strictEqual(C.tatilSonraki(t(10, 30)).tarih.getTime(), t(1, 1, 2027).getTime());
});
ok("ondalık temizleme: virgül ondalık, nokta binlik", () => {
  assert.strictEqual(C.ondalikTemizle("8.069,68"), "8069.68"); assert.strictEqual(C.ondalikTemizle("120.000"), "120000"); assert.strictEqual(C.ondalikTemizle("1.234.567"), "1234567");
  assert.strictEqual(C.ondalikTemizle("190000,5"), "190000.5"); assert.strictEqual(C.ondalikTemizle("12.5"), "12.5"); assert.strictEqual(C.ondalikTemizle("abc12"), "12");
  assert.strictEqual(C.ondalikTemizle("8069,6789"), "8069.67"); assert.strictEqual(C.ondalikTemizle("1234567890123"), "123456789");
});
ok("tl biçimi", () => {
  assert.strictEqual(C.tl(146349.85), "146.349,85 ₺"); assert.strictEqual(C.tl(133496.24, false), "133.496 ₺"); assert.strictEqual(C.tl(-4524.76), "−4.524,76 ₺");
});

console.log("\n" + n + " test geçti");
