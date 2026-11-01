/* Çalışan Asistanı tarayıcı demosu (nrazon.github.io/calisan/). Android uygulamasındaki hesap motorunun (CalisanAsistani/.../hesap/*.kt:
   Maas, Parametreler, MaasOngorusu, SaglikPrimi, Tatiller) JavaScript karşılığı + uygulamanın Ana ekran / Net maaşım / İzin planı / Ayarlar ekranları.
   Hiçbir veri sunucuya gitmez; girilen bilgiler yalnızca bu tarayıcıda (localStorage) saklanır; Ayarlar > "Tüm verilerimi sil" ile silinir.
   Kullanım: <div data-calisan data-play="<Play adresi>"></div>  (calisan.js yüklenince kendiliğinden kurulur). Testler: node tools/calisan.test.js */
(function () {
  "use strict";
  var api = {};

  // ====================================================================== tarih yardımcıları (UTC gece yarısı = LocalDate)
  function ld(y, m, d) { return new Date(Date.UTC(y, m - 1, d)); }
  function Y(d) { return d.getUTCFullYear(); }
  function M(d) { return d.getUTCMonth() + 1; }
  function D(d) { return d.getUTCDate(); }
  function addDays(d, n) { return new Date(d.getTime() + n * 86400000); }
  function daysBetween(a, b) { return Math.round((b.getTime() - a.getTime()) / 86400000); }
  function lenMonth(y, m) { return new Date(Date.UTC(y, m, 0)).getUTCDate(); }
  function dow(d) { return (d.getUTCDay() + 6) % 7; }                 // 0 = Pazartesi ... 6 = Pazar (java.time.DayOfWeek sırası)
  function isWeekend(d) { return dow(d) >= 5; }
  function today() { var n = new Date(); return ld(n.getFullYear(), n.getMonth() + 1, n.getDate()); }
  var AYLAR = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"];
  var AYLAR_K = ["Oca", "Şub", "Mar", "Nis", "May", "Haz", "Tem", "Ağu", "Eyl", "Eki", "Kas", "Ara"];
  var GUNLER = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"];
  function ayAd(ay, kisa) { var i = Math.min(12, Math.max(1, ay)) - 1; return kisa ? AYLAR_K[i] : AYLAR[i]; }

  // ====================================================================== yuvarlama ve biçim
  /** Kuruşa yarım yukarı; önce 6 haneye (ondalık kayma 4.211,325'i 4.211,32 yapmasın). Kotlin: BigDecimal(x).setScale(6).setScale(2). */
  function yuvarla(x) {
    var neg = x < 0, a = Math.abs(x);
    var s = a.toFixed(6), dot = s.indexOf(".");
    var cents = parseInt(s.slice(0, dot), 10) * 100 + parseInt(s.slice(dot + 1, dot + 3), 10);
    if (s.charCodeAt(dot + 3) >= 53) cents++;
    var r = cents / 100;
    return neg ? -r : r;
  }
  function tl(x, kurus) {
    if (kurus === undefined) kurus = true;
    var neg = x < 0, a = Math.abs(x);
    var s = a.toFixed(kurus ? 2 : 0), p = s.split(".");
    var ip = p[0].replace(/\B(?=(\d{3})+(?!\d))/g, ".");
    return (neg ? "−" : "") + ip + (kurus ? "," + p[1] : "") + " ₺";
  }
  /** Rakam girişi: virgül ondalık ayraçtır, noktalar binlik ayraçtır ("120.000" -> 120000, "8.069,68" -> 8069.68); tek nokta ondalıktır ("12.5").
   *  (Android uygulamasındaki ondalikTemizle yalnız ilk noktayı ondalık sayar; web'de klavyeyle binlik ayraçlı yazmak yaygın olduğu için burada daha akıllı.) */
  function ondalikTemizle(girdi) {
    var s = String(girdi).replace(/[^0-9.,]/g, "");
    if (s.indexOf(",") >= 0) { var v = s.indexOf(","); s = s.slice(0, v).replace(/\./g, "") + "." + s.slice(v + 1).replace(/[.,]/g, ""); }
    else if (/^\d{1,3}(\.\d{3})+$/.test(s)) s = s.replace(/\./g, "");
    var n = s.indexOf(".");
    var duz = n < 0 ? s : s.slice(0, n + 1) + s.slice(n + 1).replace(/\./g, "");
    var b = duz.split(".");
    var tam = b[0].slice(0, 9);
    return b.length < 2 ? tam : tam + "." + b[1].slice(0, 2);
  }

  // ====================================================================== Parametreler (2026; kaynaklar: calisan/params.json)
  var DILIM_SON = Infinity;
  var P2026 = {
    yil: 2026, asgariUcretBrut: 33030.0, sgkTavan: 297270.0, sgkIsciOrani: 0.14, issizlikIsciOrani: 0.01, sgdpIsciOrani: 0.075, damgaOrani: 0.00759,
    dilimler: [{ ust: 190000.0, oran: 0.15 }, { ust: 400000.0, oran: 0.20 }, { ust: 1500000.0, oran: 0.27 }, { ust: 5300000.0, oran: 0.35 }, { ust: DILIM_SON, oran: 0.40 }],
  };
  function vergi(p, kum) {
    var kalan = Math.max(0, kum), alt = 0, toplam = 0;
    for (var i = 0; i < p.dilimler.length; i++) {
      var d = p.dilimler[i], genislik = d.ust - alt, pay = Math.min(kalan, genislik);
      toplam += pay * d.oran; kalan -= pay; alt = d.ust;
      if (kalan <= 0) break;
    }
    return toplam;
  }
  function dilimOrani(p, kum) {
    for (var i = 0; i < p.dilimler.length; i++) if (kum < p.dilimler[i].ust) return p.dilimler[i].oran;
    return p.dilimler[p.dilimler.length - 1].oran;
  }
  function dilimUst(p, kum) {
    for (var i = 0; i < p.dilimler.length; i++) if (kum < p.dilimler[i].ust) return p.dilimler[i].ust === DILIM_SON ? null : p.dilimler[i].ust;
    return null;
  }

  // ====================================================================== MaasHesabi
  function devir(gv, asgari) { return { gvMatrah: gv || 0, asgariMatrah: asgari || 0 }; }
  function clamp(x, lo, hi) { return Math.min(hi, Math.max(lo, x)); }

  function asgariVergiMatrahi(p) {
    return p.asgariUcretBrut - yuvarla(p.asgariUcretBrut * p.sgkIsciOrani) - yuvarla(p.asgariUcretBrut * p.issizlikIsciOrani);
  }

  /** Bir aylık brütten nete. g = {brut, emekli, ekGvIndirimi, damgaEkMatrah, netEk}; onceki = önceki ayın kümülatifleri. */
  function ay(p, g, onceki) {
    var sgkMatrah = clamp(g.brut, p.asgariUcretBrut, p.sgkTavan);
    var emekli = !!g.emekli;
    var sgkIsci = yuvarla(sgkMatrah * (emekli ? p.sgdpIsciOrani : p.sgkIsciOrani));
    var issizlik = emekli ? 0.0 : yuvarla(sgkMatrah * p.issizlikIsciOrani);
    var ekGv = g.ekGvIndirimi || 0, damgaEk = g.damgaEkMatrah || 0, netEk = g.netEk || 0;
    var gvMatrah = yuvarla(g.brut - sgkIsci - issizlik - ekGv);
    var kumGv = onceki.gvMatrah + gvMatrah;
    var gelirVergisi = yuvarla(vergi(p, kumGv) - vergi(p, onceki.gvMatrah));
    var damga = yuvarla((g.brut + damgaEk) * p.damgaOrani);
    var asgariMatrah = asgariVergiMatrahi(p);
    var kumAsgari = onceki.asgariMatrah + asgariMatrah;
    var gvIstisna = yuvarla(vergi(p, kumAsgari) - vergi(p, onceki.asgariMatrah));
    var damgaIstisna = yuvarla(p.asgariUcretBrut * p.damgaOrani);
    var netOnce = yuvarla(g.brut - sgkIsci - issizlik - gelirVergisi - damga + netEk);
    return {
      brut: g.brut, sgkMatrah: sgkMatrah, sgkIsci: sgkIsci, issizlik: issizlik, gvMatrah: gvMatrah, gelirVergisi: gelirVergisi, damgaVergisi: damga,
      gvIstisnasi: gvIstisna, damgaIstisnasi: damgaIstisna, netOnce: netOnce, net: yuvarla(netOnce + gvIstisna + damgaIstisna),
      devir: devir(kumGv, kumAsgari),
    };
  }

  function yil(p, brutlar, emekli, baslangic) {
    var dv = baslangic || devir(), out = [];
    brutlar.forEach(function (b) { var a = ay(p, { brut: b, emekli: emekli }, dv); out.push(a); dv = a.devir; });
    return out;
  }

  /** Netten brüte tek ay (ikili arama, kuruşa yuvarlı; komşu kuruşlardan hedefe en yakını). */
  function brutBul(p, hedefNet, onceki, emekli) {
    var alt = Math.min(p.asgariUcretBrut, hedefNet), ust = hedefNet * 4 + 1.0;
    for (var i = 0; i < 80; i++) {
      var orta = (alt + ust) / 2;
      if (ay(p, { brut: orta, emekli: emekli }, onceki).net < hedefNet) alt = orta; else ust = orta;
    }
    var merkez = yuvarla(ust), best = null;
    [merkez - 0.01, merkez, merkez + 0.01].forEach(function (b) {
      var r = ay(p, { brut: b, emekli: emekli }, onceki), f = Math.abs(r.net - hedefNet);
      if (best === null || f < best.f) best = { r: r, f: f };
    });
    return best.r;
  }
  function netten(p, hedefNet, ayAdedi, emekli) {
    var dv = devir(), out = [];
    for (var i = 0; i < ayAdedi; i++) { var a = brutBul(p, hedefNet, dv, emekli); out.push(a); dv = a.devir; }
    return out;
  }

  // ====================================================================== SaglikPrimi
  var PRIM_ORAN = 0.15;
  function primIndirim(p, brut, prim, yilIcindeIndirilen) {
    if (!isFinite(prim) || prim <= 0 || !isFinite(brut) || brut <= 0) return 0.0;
    var aylikSinir = brut * PRIM_ORAN;
    var kalanYillik = Math.max(0, p.asgariUcretBrut * 12 - Math.max(0, yilIcindeIndirilen));
    return yuvarla(Math.min(prim, aylikSinir, kalanYillik));
  }

  // ====================================================================== MaasProfili / MaasOngorusu
  function primAy(pr, a) {
    var aylik = pr.primAylik || 0, bas = clamp(pr.primBaslangicAy || 1, 1, 12), taksit = pr.primTaksit || 0;
    if (aylik <= 0 || !isFinite(aylik)) return 0.0;
    if (a < bas) return 0.0;
    if (taksit <= 0) return aylik;
    if (a < bas + taksit) return aylik;
    return 0.0;
  }
  function primIndirilebilir(pr, a) { return primAy(pr, a) * (pr.primBirikimli ? 0.5 : 1.0); }
  function odemeTarihi(pr, y, a) {
    var taban = ld(y, a, 1);
    if (pr.maasSonrakiAy) taban = ld(M(taban) === 12 ? Y(taban) + 1 : Y(taban), M(taban) === 12 ? 1 : M(taban) + 1, 1);
    var gun = Math.min(Math.max(pr.maasGunu === undefined ? 5 : pr.maasGunu, 1), lenMonth(Y(taban), M(taban)));
    return ld(Y(taban), M(taban), gun);
  }
  function copy(o, ch) { var r = {}, k; for (k in o) r[k] = o[k]; for (k in ch) r[k] = ch[k]; return r; }
  function carpan(pr, a) { return pr.zam && a >= pr.zam.ay ? 1.0 + pr.zam.oran : 1.0; }

  function gvMatrahi(p, pr, emekli, onceki, sbAy) {
    var brut = pr.net ? brutBul(p, pr.tutar, onceki, emekli).brut : pr.tutar;
    var ind = pr.net ? 0.0 : primIndirim(p, brut, primIndirilebilir(pr, sbAy), 0.0);
    return ay(p, { brut: brut, emekli: emekli, ekGvIndirimi: ind }, devir()).gvMatrah;
  }

  function ongoruWrap(o) {
    o.seciliIndex = clamp(o.siraIndex, 0, o.aylar.length - 1);
    o.sonrakiGecis = null;
    for (var i = o.siraIndex + 1; i < o.aylar.length; i++) if (i >= 0 && o.aylar[i].dilimDegisti) { o.sonrakiGecis = o.aylar[i]; break; }
    o.yeniYilOcak = o.sonraki && o.sonraki.yil > o.aylar[0].yil ? o.sonraki : null;
    return o;
  }

  /** [bugun] itibarıyla sıradaki maaş, sonraki maaş ve yıl boyunca aylık tahmin (Kotlin: MaasOngorusu.hesapla). */
  function ongoru(p, pr, bugun, pGelecek, pOnceki) {
    pGelecek = pGelecek || p; pOnceki = pOnceki || p;
    if (!(pr.tutar > 0) || !isFinite(pr.tutar)) return null;
    var emekli = !!pr.emekli, yl = Y(bugun);
    var sb = pr.sonBordro && pr.sonBordro.yil === yl && pr.sonBordro.ay >= 1 && pr.sonBordro.ay <= 12 && pr.sonBordro.kumulatifGvMatrah > 0 ? pr.sonBordro : null;
    var girisYilda = pr.giris && Y(pr.giris) === yl ? pr.giris : null;
    var asgari = asgariVergiMatrahi(p);
    var ilkAy, devir0;
    if (sb) {
      ilkAy = sb.ay;
      var calisilan = Math.max(sb.ay - (girisYilda ? M(girisYilda) : 1) + 1, 1);
      var bu = gvMatrahi(p, pr, emekli, devir(sb.kumulatifGvMatrah, 0.0), sb.ay);
      var once = Math.max(sb.kumulatifGvMatrah - bu, 0.0);
      devir0 = devir(once, asgari * (calisilan - 1));
    } else {
      ilkAy = girisYilda ? M(girisYilda) : 1;
      devir0 = devir();
    }
    var aylar = [], dv = devir0, indirilen = 0.0, oncekiOran = dilimOrani(p, devir0.gvMatrah);
    for (var a = ilkAy; a <= 12; a++) {
      var hedef = pr.tutar * carpan(pr, a);
      var brut = pr.net ? brutBul(p, hedef, dv, emekli).brut : hedef;
      var ind = pr.net ? 0.0 : primIndirim(p, brut, primIndirilebilir(pr, a), indirilen);
      indirilen += ind;
      var s = ay(p, { brut: brut, emekli: emekli, ekGvIndirimi: ind }, dv);
      var oran = dilimOrani(p, s.devir.gvMatrah);
      aylar.push({ yil: yl, ay: a, sonuc: s, primIndirilen: ind, dilimOrani: oran, dilimDegisti: oran > oncekiOran, primOdenen: pr.net ? 0.0 : primAy(pr, a) });
      oncekiOran = oran; dv = s.devir;
    }
    // Ocak'ta yatan maaş geçen yılın Aralık maaşıdır
    var oncekiAralik = null;
    if (M(bugun) === 1 && odemeTarihi(pr, yl - 1, 12) >= bugun) {
      var oo = ongoru(pOnceki, copy(pr, { sonBordro: null, zam: null }), ld(yl - 1, 12, 15), p, pOnceki);
      oncekiAralik = oo && oo.aylar.length ? oo.aylar[oo.aylar.length - 1] : null;
    }
    // Aralık maaşından sonra gelecek yılın Ocak'ı (matrah sıfırdan)
    var ocakHedef = pr.tutar * carpan(pr, 12);
    var ocakBrut = pr.net ? brutBul(pGelecek, ocakHedef, devir(), emekli).brut : ocakHedef;
    var ocakPrim = pr.net ? 0.0 : primAy(pr, 13);
    var ocakInd = primIndirim(pGelecek, ocakBrut, pr.net ? 0.0 : primIndirilebilir(pr, 13), 0.0);
    var ocakSonuc = ay(pGelecek, { brut: ocakBrut, emekli: emekli, ekGvIndirimi: ocakInd }, devir());
    var gelecekOcak = { yil: yl + 1, ay: 1, sonuc: ocakSonuc, primIndirilen: ocakInd, dilimOrani: dilimOrani(pGelecek, ocakSonuc.devir.gvMatrah), dilimDegisti: false, primOdenen: ocakPrim };

    var zincir = (oncekiAralik ? [oncekiAralik] : []).concat(aylar, [gelecekOcak]);
    var i = -1;
    for (var k = 0; k < zincir.length; k++) if (odemeTarihi(pr, zincir[k].yil, zincir[k].ay) >= bugun) { i = k; break; }
    if (i < 0) i = zincir.length - 1;
    var siradaki = zincir[i];
    return ongoruWrap({
      ilkAy: ilkAy, aylar: aylar, siraIndex: oncekiAralik ? i - 1 : i, siradaki: siradaki,
      siradakiTarih: odemeTarihi(pr, siradaki.yil, siradaki.ay), sonraki: zincir[i + 1] || null, baslangicDevri: devir0,
    });
  }

  /** "Yeni yıl zammı": gelecek yılın 12 aylık tahmini, maaşa [zamOrani] eklenmiş, matrah Ocak'ta sıfırdan. */
  function yeniYil(p, pGelecek, pr, bugun, zamOrani) {
    var kalanTaksit = (pr.primTaksit || 0) <= 0 ? 0 : (clamp(pr.primBaslangicAy || 1, 1, 12) + pr.primTaksit - 13);
    var yeni = copy(pr, {
      tutar: pr.tutar * (1.0 + zamOrani), giris: null, sonBordro: null, zam: null, maasSonrakiAy: false, maasGunu: 31,
      primAylik: ((pr.primTaksit || 0) <= 0 || kalanTaksit > 0) ? pr.primAylik : 0.0,
      primBaslangicAy: 1, primTaksit: (pr.primTaksit || 0) <= 0 ? 0 : Math.max(kalanTaksit, 0),
    });
    return ongoru(pGelecek, yeni, ld(Y(bugun) + 1, 1, 1), pGelecek, p);
  }

  // ====================================================================== Tatiller (2026-2035; Diyanet takvimi)
  var BAYRAM = {
    2026: [["R", 3, 19], ["K", 5, 26]], 2027: [["R", 3, 8], ["K", 5, 15]], 2028: [["R", 2, 25], ["K", 5, 4]],
    2029: [["R", 2, 13], ["K", 4, 23]], 2030: [["R", 2, 3], ["K", 4, 12]], 2031: [["R", 1, 23], ["K", 4, 1]],
    2032: [["R", 1, 13], ["K", 3, 21]], 2033: [["R", 1, 1], ["K", 3, 10], ["R", 12, 22]], 2034: [["K", 2, 28], ["R", 12, 11]],
    2035: [["K", 2, 17], ["R", 11, 30]],
  };
  var ILK_YIL = 2026, SON_YIL = 2035;
  function tatilYil(y) {
    var l = [
      { tarih: ld(y, 1, 1), ad: "Yılbaşı" }, { tarih: ld(y, 4, 23), ad: "Ulusal Egemenlik ve Çocuk Bayramı" },
      { tarih: ld(y, 5, 1), ad: "Emek ve Dayanışma Günü" }, { tarih: ld(y, 5, 19), ad: "Atatürk'ü Anma, Gençlik ve Spor Bayramı" },
      { tarih: ld(y, 7, 15), ad: "Demokrasi ve Milli Birlik Günü" }, { tarih: ld(y, 8, 30), ad: "Zafer Bayramı" },
      { tarih: ld(y, 10, 28), ad: "Cumhuriyet Bayramı Arefesi", yarimGun: true }, { tarih: ld(y, 10, 29), ad: "Cumhuriyet Bayramı" },
    ];
    (BAYRAM[y] || []).forEach(function (b) {
      var ad = b[0] === "R" ? "Ramazan Bayramı" : "Kurban Bayramı", gun = b[0] === "R" ? 3 : 4, arefe = ld(y, b[1], b[2]);
      l.push({ tarih: arefe, ad: ad + " Arefesi", yarimGun: true });
      for (var i = 1; i <= gun; i++) l.push({ tarih: addDays(arefe, i), ad: ad + " " + i + ". gün" });
    });
    return l.filter(function (t) { return Y(t.tarih) === y; }).sort(function (a, b) { return a.tarih - b.tarih; });
  }
  function tatilTumu() { var o = []; for (var y = ILK_YIL; y <= SON_YIL; y++) o = o.concat(tatilYil(y)); return o; }
  function tatilSonraki(bugun) {
    var t = tatilTumu();
    for (var i = 0; i < t.length; i++) if (t[i].tarih >= bugun && !t[i].yarimGun) return t[i];
    return null;
  }
  function kopruOnerileri(y, maxIzin) {
    if (maxIzin === undefined) maxIzin = 5.0;
    var tam = {};
    tatilYil(y - 1).concat(tatilYil(y), tatilYil(y + 1)).forEach(function (t) { if (!t.yarimGun) tam[t.tarih.getTime()] = true; });
    var arefe = {};
    tatilYil(y).forEach(function (t) { if (t.yarimGun) arefe[t.tarih.getTime()] = true; });
    function off(d) { return isWeekend(d) || !!tam[d.getTime()]; }
    function maliyet(d) { return off(d) ? 0.0 : (arefe[d.getTime()] ? 0.5 : 1.0); }
    var bas = ld(y, 1, 1), son = ld(y, 12, 31), sonuc = [], s = bas;
    while (s <= son) {
      if (off(s)) {
        var izin = 0.0, e = s;
        while (e <= son && izin <= maxIzin) {
          izin += maliyet(e);
          if (izin > maxIzin) break;
          var sonraki = addDays(e, 1);
          if (off(e) && izin > 0.0 && !off(sonraki)) {
            var onceki = addDays(s, -1);
            if (!off(onceki)) {
              var icerir = false;
              for (var d = s; d <= e; d = addDays(d, 1)) if (tam[d.getTime()]) { icerir = true; break; }
              if (icerir) sonuc.push({ baslangic: s, bitis: e, izinGunu: izin, toplamGun: daysBetween(s, e) + 1 });
            }
          }
          e = sonraki;
        }
      }
      s = addDays(s, 1);
    }
    function enUzun(liste, anahtar) {
      var g = {}, order = [];
      liste.forEach(function (o) { var k = anahtar(o); if (!(k in g)) { g[k] = o; order.push(k); } else if (o.toplamGun > g[k].toplamGun) g[k] = o; });
      return order.map(function (k) { return g[k]; });
    }
    var bit = enUzun(sonuc, function (o) { return o.bitis.getTime() + "|" + o.izinGunu; });
    var uz = enUzun(bit, function (o) { return o.baslangic.getTime() + "|" + o.izinGunu; });
    uz.forEach(function (o) { o.verim = o.toplamGun / o.izinGunu; });
    return uz.sort(function (a, b) { return b.verim - a.verim || a.baslangic - b.baslangic; });
  }

  api.P2026 = P2026; api.yuvarla = yuvarla; api.tl = tl; api.vergi = vergi; api.dilimOrani = dilimOrani; api.dilimUst = dilimUst;
  api.ay = ay; api.yil = yil; api.brutBul = brutBul; api.netten = netten; api.devir = devir; api.asgariVergiMatrahi = asgariVergiMatrahi;
  api.primIndirim = primIndirim; api.primAy = primAy; api.odemeTarihi = odemeTarihi; api.ongoru = ongoru; api.yeniYil = yeniYil;
  api.tatilYil = tatilYil; api.tatilSonraki = tatilSonraki; api.kopruOnerileri = kopruOnerileri; api.ld = ld;
  api.ondalikTemizle = ondalikTemizle;

  // ====================================================================== ARAYÜZ (yalnız tarayıcıda)
  if (typeof document !== "undefined") (function () {
    var CSS = [
      ".cal-wrap{display:flex;flex-direction:column;align-items:center;gap:14px}",
      ".cal-phone{position:relative;width:min(100%,392px);height:812px;background:#0e1311;border-radius:56px;padding:11px;box-sizing:border-box;box-shadow:0 28px 60px rgba(0,0,0,.3),inset 0 0 0 2px #2b3532}",
      ".cal-screen{position:relative;height:100%;border-radius:45px;overflow:hidden;background:#F7F3EC;color:#1F2A27;font-family:Roboto,system-ui,-apple-system,'Segoe UI',sans-serif;-webkit-font-smoothing:antialiased;text-align:left}",
      ".cal-island{position:absolute;top:9px;left:50%;transform:translateX(-50%);width:104px;height:29px;border-radius:20px;background:#0e1311;z-index:6}",
      ".cal-status{position:absolute;top:0;left:0;right:0;height:46px;display:flex;justify-content:space-between;align-items:center;padding:6px 30px 0;font:600 14px/1 system-ui,sans-serif;z-index:5;pointer-events:none;color:#1F2A27}",
      ".cal-body{position:absolute;top:46px;bottom:0;left:0;right:0;overflow-y:auto;overscroll-behavior:contain;padding:6px 16px 38px;scrollbar-width:none}",
      ".cal-body::-webkit-scrollbar{display:none}",
      ".cal-homebar{position:absolute;bottom:8px;left:50%;transform:translateX(-50%);width:124px;height:5px;border-radius:3px;background:#1F2A27;opacity:.8;z-index:7;pointer-events:none}",
      ".cal-body *{box-sizing:border-box}",
      ".cal-body button,.cal-body input{font-family:inherit}",
      ".cal-col{display:flex;flex-direction:column;gap:13px}",
      ".cal-head{display:flex;align-items:flex-start;padding:6px 2px 0 4px}",
      ".cal-head>div:first-child{flex:1}",
      ".cal-hi{color:#6B7A75;font-size:15px;font-weight:500}",
      ".cal-h1{margin:0;font-size:31px;line-height:1.08;font-weight:900;letter-spacing:-.4px;color:#1F2A27}",
      ".cal-round{width:44px;height:44px;border-radius:50%;border:0;background:#fff;font-size:20px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex:none;color:#1F2A27}",
      ".cal-card{border-radius:28px;display:block;width:100%;border:0;text-align:left;color:inherit;transition:transform .16s cubic-bezier(.3,1.6,.5,1)}",
      ".cal-tap{cursor:pointer}.cal-tap:active{transform:scale(.965)}",
      ".cal-in{padding:20px}",
      ".cal-maas{background:#CDEBD9}.cal-tazminat{background:#FFE2B8}.cal-mesai{background:#D9D4FF}.cal-tatil{background:#FFD0C7}.cal-izin{background:#CFE6F7}.cal-yuzey{background:#fff}",
      ".cal-t-maas{color:#1F6B4A}.cal-t-tazminat{color:#9A5B00}.cal-t-mesai{color:#4B3FB5}.cal-t-tatil{color:#C2432C}.cal-t-izin{color:#1F5F8F}",
      ".cal-soluk{color:#6B7A75}.cal-uyari{color:#B3261E}",
      ".cal-lab{font-size:12px;font-weight:600;letter-spacing:.2px;margin:0}",
      ".cal-big{font-size:46px;line-height:1.05;font-weight:900;letter-spacing:-.5px}",
      ".cal-title{font-size:20px;font-weight:800;margin:0}",
      ".cal-sub{font-size:16px;font-weight:700;margin:0}",
      ".cal-p{font-size:14px;line-height:1.45;margin:0}",
      ".cal-small{font-size:12px;line-height:1.35;margin:0}",
      ".cal-note{font-size:12px;line-height:1.4;color:#6B7A75;margin:0;padding:0 4px}",
      ".cal-row{display:flex;align-items:center}",
      ".cal-grow{flex:1;min-width:0}",
      ".cal-grid2{display:grid;grid-template-columns:1fr 1fr;gap:13px}",
      ".cal-box{padding:16px;height:152px;display:flex;flex-direction:column;justify-content:space-between}",
      ".cal-box .e{font-size:34px;line-height:1}",
      ".cal-box b{display:block;font-size:19px;font-weight:800;margin-bottom:2px}",
      ".cal-box span{font-size:12px;line-height:1.3;color:#6B7A75;display:block}",
      ".cal-tatilkart{padding:16px 6px 14px 20px}",
      ".cal-char{width:112px;height:112px;flex:none;cursor:pointer;-webkit-tap-highlight-color:transparent}",
      ".cal-char svg{width:100%;height:100%;overflow:visible}",
      ".cal-char.bounce svg{animation:cal-bounce .5s cubic-bezier(.3,1.6,.5,1)}",
      "@keyframes cal-bounce{0%{transform:scale(1)}40%{transform:scale(1.14) rotate(-4deg)}100%{transform:scale(1)}}",
      ".cal-balon{margin:6px 14px 0 0;padding:13px;border-radius:18px;background:rgba(247,243,236,.62);display:flex;flex-direction:column;gap:10px;cursor:pointer}",
      ".cal-btns{display:flex;gap:8px;flex-wrap:wrap}",
      ".cal-pill{border:0;border-radius:999px;background:#C2432C;color:#fff;font-weight:700;font-size:14px;padding:8px 14px;cursor:pointer}",
      ".cal-pills{display:flex;background:#fff;border-radius:999px;padding:4px;gap:4px}",
      ".cal-pills button{flex:1;border:0;border-radius:999px;padding:10px 6px;font-weight:700;font-size:14px;background:transparent;color:#6B7A75;cursor:pointer}",
      ".cal-pills button.on{background:#2F6F5E;color:#fff}",
      ".cal-field{display:block;background:var(--fd,#F7F3EC);border-radius:20px;padding:8px 16px 9px}",
      ".cal-field small{display:block;font-size:12px;color:#6B7A75;margin-bottom:1px}",
      ".cal-field .in{display:flex;align-items:center;gap:6px}",
      ".cal-field input{flex:1;min-width:0;border:0;outline:0;background:transparent;font-size:17px;font-weight:600;color:#1F2A27;padding:2px 0}",
      ".cal-field .sf{color:#6B7A75;font-size:15px}",
      ".cal-field:focus-within{box-shadow:inset 0 -2px 0 #2F6F5E}",
      ".cal-clear{border:0;background:transparent;color:#2F6F5E;font-weight:700;font-size:14px;cursor:pointer;padding:4px 0 4px 8px}",
      ".cal-chips{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding:1px 0;position:relative}",
      ".cal-chips::-webkit-scrollbar{display:none}",
      ".cal-chip{border:0;border-radius:999px;padding:9px 15px;background:var(--cb,#fff);color:#6B7A75;font-weight:700;font-size:14px;white-space:nowrap;cursor:pointer;flex:none}",
      ".cal-chip.on{background:var(--co,#1F6B4A);color:#fff}.cal-chip.past{opacity:.6}",
      ".cal-btn{display:block;width:100%;border:0;border-radius:999px;padding:14px;background:#1F6B4A;color:#fff;font-weight:800;font-size:16px;cursor:pointer}",
      ".cal-btn[disabled]{opacity:.45;cursor:default}",
      ".cal-link{display:flex;align-items:center;width:100%;border:0;background:transparent;padding:14px 20px;font-size:16px;font-weight:500;color:#1F2A27;cursor:pointer;text-align:left;text-decoration:none}",
      ".cal-link i{margin-left:auto;font-style:normal;color:#6B7A75;font-size:22px}",
      ".cal-sw{position:relative;width:48px;height:28px;flex:none}",
      ".cal-sw input{position:absolute;inset:0;opacity:0;width:100%;height:100%;margin:0;cursor:pointer;z-index:1}",
      ".cal-sw span{position:absolute;inset:0;border-radius:999px;background:#c9cfcc;transition:background .15s}",
      ".cal-sw span:after{content:'';position:absolute;top:3px;left:3px;width:22px;height:22px;border-radius:50%;background:#fff;transition:transform .15s}",
      ".cal-sw input:checked+span{background:#2F6F5E}.cal-sw input:checked+span:after{transform:translateX(20px)}",
      ".cal-step{display:flex;align-items:center;gap:6px}",
      ".cal-step button{width:36px;height:36px;border-radius:50%;border:0;background:#F7F3EC;font-size:20px;color:#1F2A27;cursor:pointer}",
      ".cal-step button[disabled]{color:#aab3b0;cursor:default}",
      ".cal-top{display:flex;align-items:center;gap:12px;padding:6px 0 4px}",
      ".cal-top h2{margin:0;font-size:20px;font-weight:800}",
      ".cal-sat{display:flex;justify-content:space-between;gap:12px;padding:5px 0;font-size:14px}",
      ".cal-sat span:first-child{color:#6B7A75}.cal-sat b{font-weight:600;text-align:right}.cal-sat.v b{font-size:17px;font-weight:800}",
      ".cal-bars{display:flex;align-items:flex-end;gap:5px;height:110px}",
      ".cal-bars button{flex:1;height:100%;border:0;background:transparent;padding:0;display:flex;align-items:flex-end;cursor:pointer}",
      ".cal-bars i{display:block;width:100%;border-radius:8px 8px 5px 5px;background:#CDEBD9;transition:height .35s cubic-bezier(.3,1.4,.5,1)}",
      ".cal-bars button.on i{background:#1F6B4A}",
      ".cal-tt{display:flex;gap:12px;padding:7px 0;align-items:center}",
      ".cal-tt .d{width:70px;font-weight:800;flex:none}",
      ".cal-tt .n{font-size:14px}.cal-tt .x{font-size:12px;color:#6B7A75}",
      ".cal-kopru{display:flex;align-items:center;padding:16px 18px;gap:10px}",
      ".cal-kopru .g{font-size:38px;font-weight:900;line-height:1;text-align:right}",
      ".cal-kopru small{display:block;font-size:12px;font-weight:600;text-align:right}",
      ".cal-sheet{position:absolute;inset:0;background:rgba(0,0,0,.42);z-index:20;display:flex;align-items:flex-end;opacity:0;pointer-events:none;transition:opacity .2s}",
      ".cal-sheet.open{opacity:1;pointer-events:auto}",
      ".cal-sheet>div{background:#fff;width:100%;border-radius:28px 28px 40px 40px;padding:24px 22px 30px;transform:translateY(30px);transition:transform .25s cubic-bezier(.3,1.3,.5,1)}",
      ".cal-sheet.open>div{transform:none}",
      ".cal-sheet .e{font-size:44px;line-height:1}",
      ".cal-play{display:flex;align-items:center;justify-content:center;gap:8px;border-radius:999px;background:#1F6B4A;color:#fff;font-weight:800;font-size:16px;padding:14px;text-decoration:none}",
      ".cal-ghost{border:0;background:transparent;color:#6B7A75;font-weight:700;font-size:15px;padding:10px;cursor:pointer;width:100%}",
      ".cal-cap{max-width:392px;text-align:center;font-size:13px;color:#6B7A75;margin:0}",
    ].join("\n");

    function e(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
    function upperTr(s) { return s.toLocaleUpperCase("tr-TR"); }
    function track(name, params) { try { if (typeof window.gtag === "function") window.gtag("event", name, params); } catch (x) {} }
    var P = P2026;
    var yuzde = function (o) { return "%" + Math.round(o * 100); };
    var gunAy = function (d) { return D(d) + " " + ayAd(M(d)); };
    var fark = function (f) { return (f > 0 ? "+ " : "− ") + tl(Math.abs(f)); };
    var tarihMetni = function (d) { return D(d) + " " + ayAd(M(d)) + " " + GUNLER[dow(d)]; };
    var kisa = function (d) { return D(d) + " " + ayAd(M(d), true); };

    // ---------------------------------------------------------------- asistan karakteri (bordro)
    function karakter(durum) {
      var zig = "";
      for (var i = 1; i <= 7; i++) zig += " L" + (102 - 12 * i) + " " + (i % 2 ? 118 : 111);
      var govde = "M18 12 H80 L102 34 V111" + zig + " Z";
      var gozler;
      if (durum === "mutlu") gozler = '<path d="M38 57 Q46 47 54 57" stroke="#1d1d1b" stroke-width="4" fill="none" stroke-linecap="round"/><path d="M66 57 Q74 47 82 57" stroke="#1d1d1b" stroke-width="4" fill="none" stroke-linecap="round"/>';
      else if (durum === "gozlukl") gozler = '<rect x="33" y="48" width="28" height="17" rx="7" fill="#1d1d1b"/><rect x="59" y="48" width="28" height="17" rx="7" fill="#1d1d1b"/><rect x="58" y="52" width="4" height="3" fill="#1d1d1b"/><path d="M38 52 L46 52" stroke="#fff" stroke-width="2" opacity=".55"/>';
      else gozler = '<ellipse cx="46" cy="57" rx="5" ry="7" fill="#1d1d1b"/><ellipse cx="74" cy="57" rx="5" ry="7" fill="#1d1d1b"/><circle cx="48" cy="54" r="1.8" fill="#fff"/><circle cx="76" cy="54" r="1.8" fill="#fff"/>';
      var agiz = durum === "mutlu" ? '<path d="M50 74 Q60 88 70 74 Z" fill="#7a2c20" stroke="#1d1d1b" stroke-width="3" stroke-linejoin="round"/>' : '<path d="M51 76 Q60 84 69 76" stroke="#1d1d1b" stroke-width="3.5" fill="none" stroke-linecap="round"/>';
      return '<svg viewBox="0 0 120 124" aria-hidden="true"><path d="' + govde + '" fill="#FFFBF0" stroke="#E4D9BE" stroke-width="3" stroke-linejoin="round"/>' +
        '<path d="M80 12 V34 H102 Z" fill="#E9DFC4" stroke="#E4D9BE" stroke-width="3" stroke-linejoin="round"/>' + gozler +
        '<circle cx="35" cy="73" r="7" fill="#F7B6B6" opacity=".9"/><circle cx="85" cy="73" r="7" fill="#F7B6B6" opacity=".9"/>' + agiz +
        '<rect x="30" y="92" width="38" height="5" rx="2.5" fill="#D9CFB5"/><rect x="30" y="102" width="26" height="5" rx="2.5" fill="#D9CFB5"/>' +
        '<circle cx="86" cy="98" r="11" fill="#fff" stroke="#2E8B57" stroke-width="3"/><text x="86" y="103" text-anchor="middle" font-size="14" font-weight="800" fill="#2E8B57" font-family="system-ui,sans-serif">₺</text></svg>';
    }

    // ---------------------------------------------------------------- uygulama
    function mount(root) {
      if (root.__cal) return root.__cal;
      var bugun = today();
      var S = {
        page: "ana", hist: [], sheet: null, balon: false, mesajSira: 0, tikSay: 0, started: false, endSent: false, yil: Y(bugun), izinSecimi: 1, secili: null,
        ayar: { tutar: "", net: false, giris: null, emekli: false, sonrakiAy: true, gun: "5", sozlesme: "", prim: "", primBas: 1, primTaksit: 0, primBirikimli: false, kgvm: "", kgvmAy: M(bugun), kgvmYil: Y(bugun) },
        zam: { acik: false, yuzde: 20, ozel: "", ayS: 0 },
        basla: { tutar: "" },
      };
      var play = root.getAttribute("data-play") || "https://play.google.com/store/apps/details?id=com.calisanasistani.nesimapps";

      // ------------------------------------------------ kayıt: yalnız bu tarayıcıda (localStorage), sunucuya gitmez; "Tüm verilerimi sil" siler
      var KEY = "calisan_demo_v1";
      function ymd(d) { return Y(d) + "-" + String(M(d)).padStart(2, "0") + "-" + String(D(d)).padStart(2, "0"); }
      function sade(a) { var o = {}; for (var k in a) o[k] = a[k]; o.giris = a.giris ? ymd(a.giris) : null; return o; }
      var VARSAYILAN = JSON.stringify(sade(S.ayar));
      function yukle() {
        try {
          var j = JSON.parse(localStorage.getItem(KEY) || "null"); if (!j || !j.ayar) return;
          var a = j.ayar, A = S.ayar;
          ["tutar", "gun", "sozlesme", "prim", "kgvm"].forEach(function (k) { if (typeof a[k] === "string") A[k] = ondalikTemizle(a[k]).slice(0, 12); });
          ["net", "emekli", "sonrakiAy", "primBirikimli"].forEach(function (k) { if (typeof a[k] === "boolean") A[k] = a[k]; });
          if (a.primBas >= 1 && a.primBas <= 12) A.primBas = Math.floor(a.primBas);
          if (a.primTaksit >= 0 && a.primTaksit <= 12) A.primTaksit = Math.floor(a.primTaksit);
          if (a.kgvmAy >= 1 && a.kgvmAy <= 12) A.kgvmAy = Math.floor(a.kgvmAy);
          if (typeof a.kgvmYil === "number") A.kgvmYil = a.kgvmYil;
          var m = typeof a.giris === "string" ? /^(\d{4})-(\d{2})-(\d{2})$/.exec(a.giris) : null;
          A.giris = m ? ld(+m[1], +m[2], +m[3]) : null;
        } catch (x) {}
      }
      function kaydet() {
        try {
          var s = JSON.stringify(sade(S.ayar));
          if (s === VARSAYILAN) localStorage.removeItem(KEY); else localStorage.setItem(KEY, JSON.stringify({ ayar: JSON.parse(s) }));
        } catch (x) {}
      }
      yukle();

      function profilDolu() { return S.ayar.tutar !== "" || S.ayar.giris !== null; }
      function profil() {
        var a = S.ayar;
        var kg = parseFloat(a.kgvm);
        return {
          tutar: parseFloat(a.tutar) || 0, net: a.net, emekli: a.emekli, giris: a.giris,
          primAylik: parseFloat(a.prim) || 0, primBaslangicAy: clamp(a.primBas, 1, 12), primTaksit: clamp(a.primTaksit, 0, 12), primBirikimli: a.primBirikimli,
          sonBordro: kg > 0 && a.kgvmAy >= 1 && a.kgvmAy <= 12 ? { yil: a.kgvmYil, ay: a.kgvmAy, kumulatifGvMatrah: kg } : null,
          maasGunu: clamp(parseInt(a.gun, 10) || 5, 1, 31), maasSonrakiAy: a.sonrakiAy, zam: null,
        };
      }

      // ------------------------------------------------ bileşen yardımcıları
      function card(cls, inner, extra) { return '<div class="cal-card cal-' + cls + ' ' + (extra || "") + '">' + inner + "</div>"; }
      function tapCard(cls, go, inner, extra) { return '<button type="button" class="cal-card cal-tap cal-' + cls + ' ' + (extra || "") + '" data-go="' + go + '">' + inner + "</button>"; }
      function sat(l, v, o) { o = o || {}; return '<div class="cal-sat' + (o.vurgulu ? " v" : "") + '"><span>' + l + '</span><b' + (o.renk ? ' style="color:' + o.renk + '"' : "") + ">" + v + "</b></div>"; }
      function not(t) { return '<p class="cal-note">' + t + "</p>"; }
      function top(baslik) { return '<div class="cal-top"><button type="button" class="cal-round" data-act="geri" aria-label="Geri">←</button><h2>' + baslik + "</h2></div>"; }
      function pills(list, secili, act) {
        return '<div class="cal-pills">' + list.map(function (n, i) { return '<button type="button" data-act="' + act + '" data-v="' + i + '"' + (i === secili ? ' class="on"' : "") + ">" + n + "</button>"; }).join("") + "</div>";
      }
      function field(id, label, val, o) {
        o = o || {};
        return '<label class="cal-field"' + (o.dolgu ? ' style="--fd:' + o.dolgu + '"' : "") + "><small>" + label + '</small><span class="in"><input id="' + id + '" data-f="' + id + '" inputmode="' + (o.ondalik ? "decimal" : "numeric") + '" autocomplete="off" value="' + e(val) + '"><span class="sf">' + (o.sonek === undefined ? "₺" : o.sonek) + "</span></span></label>";
      }
      function sw(act, on) { return '<span class="cal-sw"><input type="checkbox" data-chg="' + act + '"' + (on ? " checked" : "") + '><span></span></span>'; }
      function chips(items, secili, act, o) {
        o = o || {};
        return '<div class="cal-chips"' + (o.vars ? ' style="' + o.vars + '"' : "") + ">" + items.map(function (it, i) {
          var on = (it.id !== undefined ? it.id : i) === secili;
          return '<button type="button" class="cal-chip' + (on ? " on" : "") + (it.past && !on ? " past" : "") + '" data-act="' + act + '" data-v="' + (it.id !== undefined ? it.id : i) + '">' + it.t + "</button>";
        }).join("") + "</div>";
      }
      function bars(vals, secili) {
        var en = Math.max.apply(null, vals.concat([1])), mn = Math.min.apply(null, vals);
        return '<div class="cal-bars">' + vals.map(function (d, i) {
          var o = clamp((d - mn * 0.4) / (en - mn * 0.4), 0.05, 1);
          return '<button type="button" data-act="sec" data-v="' + i + '"' + (i === secili ? ' class="on"' : "") + ' aria-label="' + tl(d, false) + '"><i style="height:' + (o * 100).toFixed(1) + '%"></i></button>';
        }).join("") + "</div>";
      }

      // ------------------------------------------------ ANA EKRAN
      function maasKalanGun(bugunD) {
        if (S.ayar.tutar === "") return null;
        var g = clamp(parseInt(S.ayar.gun, 10) || 5, 1, 31);
        function ayda(d) { return ld(Y(d), M(d), Math.min(g, lenMonth(Y(d), M(d)))); }
        var bu = ayda(bugunD);
        var hedef = bu >= bugunD ? bu : ayda(ld(M(bugunD) === 12 ? Y(bugunD) + 1 : Y(bugunD), M(bugunD) === 12 ? 1 : M(bugunD) + 1, 1));
        return daysBetween(bugunD, hedef);
      }
      function asistan(sonraki) {
        var maasKalan = maasKalanGun(bugun), tatilKalan = sonraki ? daysBetween(bugun, sonraki.tarih) : null;
        var oneriler = [
          { m: "Net maaşını ve zam senaryolarını görmek ister misin?", k: [["Net maaş", "maas"]] },
          { m: "Sıradaki köprü fırsatlarına bakalım mı?", k: [["İzin planı", "tatil"]] },
          { m: "İşten ayrılırsan kıdem ve ihbar tazminatını hesaplayabilirim.", k: [["Tazminat", "sheet:tazminat"]] },
          { m: "Zam gelirse net maaşın ne kadar artar? Zam kartında deneyebilirsin.", k: [["Zam hesabı", "maas"]] },
          { m: "Sağlık veya hayat sigortan varsa vergi iadesini net maaş ekranında görebilirsin.", k: [["Net maaş", "maas"]] },
          { m: "Fazla mesai saatlerini girersen haftalık toplamını takip ederim.", k: [["Mesai", "sheet:mesai"]] },
          { m: "İzin günlerini kaydedersen kalanını senin için tutarım.", k: [["İzinlerim", "sheet:izinler"]] },
        ];
        if (sonraki && tatilKalan > 7) oneriler.push({ m: "Sıradaki tatil " + sonraki.ad + ": " + tatilKalan + " gün kaldı.", k: [["İzin planı", "tatil"]] });
        var gun = Math.floor((bugun - ld(Y(bugun), 1, 1)) / 86400000) + 1, kay = gun % oneriler.length;
        var sirali = oneriler.slice(kay).concat(oneriler.slice(0, kay));
        if (maasKalan !== null && maasKalan <= 3) {
          var s = maasKalan === 0 ? "Bugün maaş günü!" : maasKalan === 1 ? "Maaşa 1 gün kaldı!" : "Maaşa " + maasKalan + " gün kaldı!";
          return { durum: "mutlu", mesajlar: [{ m: s + " Net tutarına bakalım mı?", k: [["Net maaş", "maas"], ["Zam hesabı", "maas"]] }].concat(sirali) };
        }
        if (sonraki && tatilKalan <= 7) {
          var s2 = tatilKalan === 0 ? "Bugün " + sonraki.ad + "!" : sonraki.ad + " için " + tatilKalan + " gün kaldı!";
          return { durum: "gozlukl", mesajlar: [{ m: s2 + " Köprü fırsatlarına bakalım mı?", k: [["İzin planı", "tatil"], ["İzinlerim", "sheet:izinler"]] }].concat(sirali) };
        }
        return { durum: "normal", mesajlar: sirali };
      }
      function anaHTML() {
        var sonraki = tatilSonraki(bugun), as = asistan(sonraki);
        var h = '<div class="cal-col"><div class="cal-head"><div><div class="cal-hi">Merhaba 👋</div><h1 class="cal-h1">Çalışan Asistanı</h1></div>' +
          '<button type="button" class="cal-round" data-go="ayar" aria-label="Ayarlar">⚙️</button></div>';
        if (!profilDolu()) {
          h += tapCard("maas", "ayar", '<span class="cal-row" style="padding:14px 18px"><span style="font-size:28px">👤</span><span class="cal-grow" style="padding:0 14px"><b class="cal-sub cal-t-maas" style="display:block">Profilini bir kere doldur</b><span class="cal-small cal-soluk" style="display:block">Maaşın ve işe giriş tarihin hesap ekranlarında hazır gelsin.</span></span><span class="cal-t-maas" style="font-size:20px">→</span></span>');
        }
        var kalan = sonraki ? daysBetween(bugun, sonraki.tarih) : 0;
        var tk = '<div class="cal-row"><div class="cal-grow cal-tap" data-go="tatil" style="cursor:pointer"><p class="cal-lab cal-t-tatil">SIRADAKİ TATİL</p>';
        if (sonraki) {
          tk += '<div class="cal-t-tatil" style="display:flex;align-items:flex-end;gap:6px"><span class="cal-big">' + (kalan === 0 ? "Bugün!" : kalan) + "</span>" + (kalan === 0 ? "" : '<span class="cal-sub" style="padding-bottom:8px">gün kaldı</span>') + "</div>" +
            '<p class="cal-sub">' + e(sonraki.ad) + '</p><p class="cal-p cal-soluk">' + tarihMetni(sonraki.tarih) + "</p>";
        }
        tk += '</div><div class="cal-char' + (S.tikSay % 2 ? " bounce" : "") + '" data-act="balon" role="button" aria-label="Asistan">' + karakter(as.durum) + "</div></div>";
        if (S.balon) {
          var ms = as.mesajlar[S.mesajSira % as.mesajlar.length];
          tk += '<div class="cal-balon" data-act="balon-kapat"><p class="cal-p">' + e(ms.m) + '</p><div class="cal-btns">' +
            ms.k.map(function (k) { return '<button type="button" class="cal-pill" data-go="' + k[1] + '">' + k[0] + "</button>"; }).join("") + "</div></div>";
        }
        h += '<div class="cal-card cal-tatil"><div class="cal-tatilkart">' + tk + "</div></div>";
        var ozet = null, o = profilDolu() ? ongoru(P, profil(), bugun, P, P) : null;
        if (o) ozet = ayAd(o.siradaki.ay) + " maaşı: " + tl(o.siradaki.sonuc.net, false);
        function kutu(cls, go, em, bas, alt) { return tapCard(cls, go, '<span class="cal-box"><span class="e">' + em + '</span><span><b class="cal-t-' + cls + '">' + bas + "</b><span>" + alt + "</span></span></span>"); }
        h += '<div class="cal-grid2">' + kutu("maas", "maas", "💸", "Net maaş", ozet || "Sıradaki maaşın ne kadar?") + kutu("tazminat", "sheet:tazminat", "🧳", "Tazminat", "Kıdem ve ihbar") + "</div>";
        h += '<div class="cal-grid2">' + kutu("mesai", "sheet:mesai", "⏱️", "Mesai", "Saat takibi, fazla mesai") + kutu("tatil", "tatil", "🏖️", "İzin planı", "Köprü ve uzun tatiller") + "</div>";
        h += tapCard("izin", "sheet:izinler", '<span class="cal-row" style="padding:18px 20px"><span style="font-size:34px">📒</span><span class="cal-grow" style="padding:0 14px"><b class="cal-title cal-t-izin" style="display:block">İzinlerim</b><span class="cal-small cal-soluk">Kalan izin günlerini takip et</span></span><span class="cal-t-izin" style="font-size:20px">→</span></span>');
        h += '<p class="cal-note" style="padding:6px 6px 0;font-size:11px">Bu uygulamadaki hesaplamalar bilgilendirme amaçlıdır; resmî bordro, hukuki veya mali danışmanlık yerine geçmez.</p></div>';
        return h;
      }

      // ------------------------------------------------ İZİN PLANI (TATİL)
      function tatilHTML() {
        var maxIzin = [1, 2, 3, 5][S.izinSecimi];
        var yl = clamp(S.yil, ILK_YIL, SON_YIL);
        var tatiller = tatilYil(yl);
        var oner = kopruOnerileri(yl, maxIzin).filter(function (o) { return o.bitis >= bugun; }).slice(0, 8);
        var h = '<div class="cal-col">' + top("İzin planı");
        var yillar = []; for (var y = ILK_YIL; y <= SON_YIL; y++) yillar.push({ id: y, t: String(y) });
        h += chips(yillar, yl, "yil", { vars: "--co:#C2432C" });
        h += '<h3 class="cal-title" style="margin:2px 0 0">Köprü fırsatları</h3><p class="cal-small cal-soluk" style="margin-top:-8px">En fazla kaç gün izin kullanmak istersin?</p>';
        h += pills(["1 gün", "2 gün", "3 gün", "5 gün"], S.izinSecimi, "izin");
        if (!oner.length) h += not("Bu seçimle " + yl + " için köprü fırsatı yok; izin gününü artırmayı dene.");
        oner.forEach(function (o) {
          var izin = o.izinGunu % 1 === 0 ? o.izinGunu + " gün izin" : String(o.izinGunu).replace(".", ",") + " gün izin";
          var kalan = daysBetween(bugun, o.baslangic);
          h += card("tatil", '<div class="cal-kopru"><div class="cal-grow"><b class="cal-sub" style="display:block">' + kisa(o.baslangic) + " – " + kisa(o.bitis) + '</b><span class="cal-small cal-soluk" style="display:block;font-size:13px">' + izin + " kullan</span>" +
            (kalan > 0 ? '<span class="cal-small cal-soluk">' + kalan + " gün sonra</span>" : "") + '</div><div class="cal-t-tatil"><div class="g">' + o.toplamGun + "</div><small>gün tatil</small></div></div>");
        });
        h += '<h3 class="cal-title" style="margin:8px 0 0">' + yl + " resmî tatilleri</h3>";
        h += card("yuzey", '<div style="padding:8px 18px">' + tatiller.map(function (t) {
          var gecti = t.tarih < bugun, hs = isWeekend(t.tarih);
          var ek = [GUNLER[dow(t.tarih)]]; if (t.yarimGun) ek.push("yarım gün"); if (hs && !t.yarimGun) ek.push("hafta sonuna denk geliyor");
          return '<div class="cal-tt"><span class="d ' + (gecti ? "cal-soluk" : "cal-t-tatil") + '">' + kisa(t.tarih) + '</span><span><span class="n" style="display:block;' + (gecti ? "color:#6B7A75" : "") + '">' + e(t.ad) + '</span><span class="x">' + ek.join(" · ") + "</span></span></div>";
        }).join("") + "</div>");
        h += not("Dinî bayram tarihleri Diyanet İşleri Başkanlığı takviminden alınmıştır. Hafta sonu Cumartesi-Pazar kabul edilir; yarım gün arefeler izin hesabında 0,5 gün sayılır. İdari izin ve 9 günlük tatil gibi sonradan ilan edilen günler ilan edilince uygulamaya otomatik eklenir.");
        return h + "</div>";
      }

      // ------------------------------------------------ AYARLAR
      function ayarHTML() {
        var a = S.ayar, dolgu = "#F7F3EC";
        var girisDeger = a.giris ? Y(a.giris) + "-" + String(M(a.giris)).padStart(2, "0") + "-" + String(D(a.giris)).padStart(2, "0") : "";
        var h = '<div class="cal-col">' + top("Ayarlar");
        h += card("yuzey", '<div class="cal-in cal-col" style="gap:12px"><h3 class="cal-title">Profilim</h3><p class="cal-small cal-soluk" style="font-size:13px">Bir kez yaz: Net maaş, Tazminat ve Mesai ekranları bu bilgilerle hazır açılır. Bilgiler yalnızca bu tarayıcıda saklanır, sunucuya gönderilmez; aşağıdaki "Tüm verilerimi sil" ile silebilirsin.</p>' +
          pills(["Brüt maaş", "Net maaş"], a.net ? 1 : 0, "net") +
          field("ayar.tutar", a.net ? "Aylık net maaş" : "Aylık brüt maaş", a.tutar, { dolgu: dolgu, ondalik: true }) +
          '<label class="cal-field" style="--fd:' + dolgu + '"><small>İşe giriş tarihi</small><span class="in"><input id="ayar.giris" type="date" data-chg="giris" value="' + girisDeger + '" min="2000-01-01" max="2100-12-31" style="font-size:16px"><button type="button" class="cal-clear" data-act="giris-temizle">Temizle</button></span></label>' +
          '<div class="cal-row"><div class="cal-grow"><b class="cal-sub" style="display:block">Emekli çalışanım</b><span class="cal-small cal-soluk">Sosyal güvenlik destek primi %7,5, işsizlik yok</span></div>' + sw("emekli", a.emekli) + "</div>" +
          '<div class="cal-col" style="gap:8px"><b class="cal-sub">Maaş ne zaman yatıyor?</b><p class="cal-small cal-soluk">Çoğu şirket çalışılan ayı izleyen ayın 1-5\'inde öder. Net maaşım, henüz yatmamış ilk maaşını gösterir.</p>' +
          pills(["Sonraki ayın", "Aynı ayın"], a.sonrakiAy ? 0 : 1, "maaszaman") + field("ayar.gun", "Ayın kaçında yatıyor?", a.gun, { dolgu: dolgu, sonek: "günü" }) + "</div>" +
          field("ayar.sozlesme", "Haftalık çalışma saati (boşsa 45; Mesai hedefi de bu)", a.sozlesme, { dolgu: dolgu, sonek: "sa" }) + "</div>");
        var aylar = []; for (var m = 1; m <= 12; m++) aylar.push({ id: m, t: ayAd(m, true) });
        h += card("yuzey", '<div class="cal-in cal-col" style="gap:12px"><h3 class="cal-title">Daha doğru tahmin için</h3><p class="cal-small cal-soluk" style="font-size:13px">İsteğe bağlı. Bordronda varsa yaz; Net maaşım ekranı bordronla aynı sonucu göstersin.</p>' +
          field("ayar.prim", "Sigorta primi: her taksitte ödediğin tutar", a.prim, { dolgu: dolgu, ondalik: true }) +
          '<div class="cal-col" style="gap:6px"><span class="cal-small cal-soluk">İlk ödeme hangi ayda?</span>' + chips(aylar, a.primBas, "primbas", { vars: "--cb:" + dolgu }) + "</div>" +
          '<div class="cal-row"><span class="cal-p cal-grow">Kaç ay ödeyeceksin?</span><span class="cal-step"><button type="button" data-act="taksit-" ' + (a.primTaksit <= 0 ? "disabled" : "") + '>−</button><span style="font-size:15px;min-width:54px;text-align:center">' + (a.primTaksit === 0 ? "Her ay" : a.primTaksit + " ay") + '</span><button type="button" data-act="taksit+" ' + (a.primTaksit >= 12 ? "disabled" : "") + ">+</button></span></div>" +
          '<div class="cal-row"><div class="cal-grow"><b class="cal-sub" style="display:block">Birikimli hayat sigortası</b><span class="cal-small cal-soluk">Birikimli poliçede primin yalnız %50\'si indirilir</span></div>' + sw("birikimli", a.primBirikimli) + "</div>" +
          not("Bordroda \"vergi indirimi\" olarak görünen hayat (birikimsiz) ya da sağlık sigortası primi; gelir vergisi matrahından düşer. Tek seferde ödediysen 1 ay seç ve ödediğin ayı işaretle. İndirim o ayın brütünün %15'i ve yıllık asgari ücret brütüyle sınırlıdır; aşan kısım indirilmez, bu yüzden taksit genelde daha avantajlıdır.") +
          field("ayar.kgvm", "Son bordromdaki toplam KGVM (kümülatif GV matrahı)", a.kgvm, { dolgu: dolgu, ondalik: true }) +
          '<div id="cal-kgvm-ay" class="cal-col" style="gap:6px;' + (a.kgvm === "" ? "display:none" : "") + '"><span class="cal-small cal-soluk">Bu rakam hangi ayın bordrosunda?</span>' + chips(aylar, a.kgvmAy, "kgvmay", { vars: "--cb:" + dolgu }) + "</div>" +
          not("Bordronda \"Toplam KGVM\" ya da \"Kümülatif GV matrahı\" olarak yazar. İşe giriş tarihin ve bu rakam varsa vergi dilimi geçişin bordroya göre hesaplanır.") + "</div>");
        h += card("maas", '<div class="cal-in cal-col" style="gap:4px"><h3 class="cal-title cal-t-maas">Rakamlar</h3><p class="cal-p">' + P.yil + " yılı rakamları kullanılıyor (asgari ücret, vergi dilimleri, kıdem tavanı).</p>" +
          '<p class="cal-small cal-soluk">Son güncelleme: 30 Ekim 2026. Uygulamada yeni rakamlar internetten gelir; bu demo gömülü ' + P.yil + " rakamlarıyla çalışır.</p></div>");
        h += card("yuzey", '<div style="padding:8px 0"><a class="cal-link" href="/calisan/privacy.html" target="_blank" rel="noopener">Gizlilik politikası<i>›</i></a><button type="button" class="cal-link" data-go="sheet:geri">Geri bildirim gönder<i>›</i></button></div>');
        h += card("yuzey", '<div class="cal-in cal-col" style="gap:6px"><h3 class="cal-title">Hakkında</h3><p class="cal-p">Çalışan Asistanı · web demosu</p><p class="cal-small cal-soluk" style="font-size:13px">Nesim Razon</p><p class="cal-small cal-soluk">Hesaplamalar tahmin ve bilgilendirme amaçlıdır; resmî bordro, mali, vergi veya hukuki danışmanlık yerine geçmez. Tazminat hesapları 4857 sayılı İş Kanunu\'na tabi işçiler içindir.</p></div>');
        h += '<button type="button" class="cal-ghost cal-uyari" data-act="sil">Tüm verilerimi sil</button>';
        return h + "</div>";
      }

      // ------------------------------------------------ NET MAAŞIM
      function profilOzeti() {
        var a = S.ayar, pc = [];
        var tutar = parseFloat(a.tutar) || 0;
        pc.push((a.net ? "Net " : "Brüt ") + tl(tutar, tutar % 1 !== 0));
        if (a.emekli) pc.push("Emekli çalışan");
        if (a.giris) pc.push(ayAd(M(a.giris)) + " " + Y(a.giris) + "'dan beri");
        var pr = parseFloat(a.prim) || 0;
        if (pr > 0) pc.push("Sigorta primi " + tl(pr) + " (" + (a.primTaksit <= 0 ? "her ay" : ayAd(a.primBas, true) + " başlangıç, " + a.primTaksit + " taksit") + (a.primBirikimli ? ", birikimli %50" : "") + ")");
        if (a.kgvm !== "" && a.kgvmAy >= 1 && a.kgvmAy <= 12) pc.push("Son bordro: " + ayAd(a.kgvmAy));
        pc.push("Maaş " + (a.sonrakiAy ? "sonraki ayın " : "ayın ") + clamp(parseInt(a.gun, 10) || 5, 1, 31) + "'inde");
        return pc.join(" · ");
      }
      function ortalamaSatiri(aylar, netler) {
        if (!netler.length) return "";
        var ort = netler.reduce(function (x, y) { return x + y; }, 0) / netler.length;
        return '<div class="cal-row" style="justify-content:space-between;gap:10px"><span class="cal-p">' + ayAd(aylar[0], true) + "–" + ayAd(aylar[aylar.length - 1], true) + ' aylık ortalama net</span><b class="cal-sub">' + tl(ort) + "</b></div>";
      }
      function ort(l) { return l.reduce(function (x, y) { return x + y; }, 0) / l.length; }
      function yuzdeTr(x) { return x.toFixed(1).replace(".", ","); }

      function baslangicHTML() {
        var pr = parseFloat(S.basla.tutar) || 0;
        return card("maas", '<div class="cal-in cal-col" style="gap:12px"><h3 class="cal-title cal-t-maas">Önümüzdeki aylarda ne alacaksın?</h3><p class="cal-p">Maaşını bir kez yaz: sıradaki maaşını ve vergi diliminin maaşına etkisini gösterelim. Bilgi yalnızca bu tarayıcıda saklanır, sunucuya gönderilmez.</p>' +
          pills(["Brüt maaş", "Net maaş"], S.ayar.net ? 1 : 0, "net") + field("basla.tutar", S.ayar.net ? "Aylık net maaş" : "Aylık brüt maaş", S.basla.tutar, { dolgu: "#fff", ondalik: true }) +
          not("Bordrodaki \"SGK matrahı\" ya da sözleşmedeki brüt ücret; kuruşlu yazabilirsin. Örnek: 120000") +
          '<button type="button" class="cal-btn" data-act="goster" id="cal-goster"' + (pr > 0 ? "" : " disabled") + ">Göster</button></div>") + digerButon();
      }
      function digerButon() {
        return tapCard("yuzey", "sheet:hesap", '<span class="cal-row" style="padding:20px"><span class="cal-grow"><b class="cal-sub" style="display:block">Başka bir maaşı dene</b><span class="cal-small cal-soluk">Yeni iş teklifi ya da zam: brütten nete, netten brüte, 12 ay</span></span><span class="cal-soluk" style="font-size:24px">›</span></span>');
      }

      function maasHTML() {
        var pr = profil();
        var temel = ongoru(P, pr, bugun, P, P);
        var h = '<div class="cal-col">' + top("Net maaşım");
        if (!temel) return h + baslangicHTML() + "</div>";
        // zam
        var Z = S.zam;
        var ilkZam = temel.siradaki.yil === Y(bugun) ? temel.siradaki.ay + 1 : 1;
        var zamAy = ilkZam > 12 ? 13 : clamp(Z.ayS === 0 ? ilkZam : Z.ayS, ilkZam, 13);
        var ozel = parseFloat(Z.ozel);
        var oran = (ozel > 0 ? ozel : Z.yuzde) / 100;
        var zam = Z.acik && zamAy >= 1 && zamAy <= 12 ? { ay: zamAy, oran: oran } : null;
        var o = zam ? ongoru(P, copy(pr, { zam: zam }), bugun, P, P) : temel;
        var yeni = Z.acik && zamAy === 13 ? yeniYil(P, P, pr, bugun, oran) : null;
        var yeni0 = Z.acik && zamAy === 13 ? yeniYil(P, P, pr, bugun, 0.0) : null;
        var siz = pr.primAylik > 0 && !pr.net ? ongoru(P, copy(pr, { primAylik: 0.0, zam: zam }), bugun, P, P) : null;
        var idx = clamp(S.secili === null ? temel.seciliIndex : S.secili, 0, o.aylar.length - 1);
        if (!S.endSent) { S.endSent = true; track("demo_end", { app: "calisan", result: "maas" }); }

        var sira = o.siradaki, sonraki = o.sonraki;
        var ilkMaasGelecekte = sira.yil === Y(bugun) && o.siraIndex === 0 && o.siradakiTarih > bugun && M(bugun) < o.ilkAy;
        var yeniYilSira = sira.yil !== Y(bugun) && sira.ay !== 12;
        var etiket = ilkMaasGelecekte ? "İLK MAAŞIN · " + upperTr(ayAd(sira.ay)) + " AYI MAAŞI" : S.ayar.net ? "SIRADAKİ MAAŞIN · " + upperTr(ayAd(sira.ay)) + " AYI (NET SABİT)" : "SIRADAKİ MAAŞIN · " + upperTr(ayAd(sira.ay)) + " AYI MAAŞI";
        var k1 = '<p class="cal-lab cal-t-maas">' + etiket + '</p><div class="cal-t-maas" style="font-size:38px;font-weight:900;letter-spacing:-.5px;line-height:1.15">' + tl(sira.sonuc.net) + '</div><p class="cal-small cal-soluk" style="font-size:13px;margin-top:2px">Yatış tarihi: ' + gunAy(o.siradakiTarih) + " (tahmini)</p>";
        var siraSiz = siz && siz.aylar[o.siraIndex];
        if (siraSiz && sira.primIndirilen > 0) k1 += '<p class="cal-small cal-t-maas" style="font-size:13px">Sigorta vergi iadesi dahil: + ' + tl(sira.sonuc.net - siraSiz.sonuc.net) + " (sigortasız " + tl(siraSiz.sonuc.net) + ")</p>";
        if (sonraki) {
          var f = sonraki.sonuc.net - sira.sonuc.net;
          k1 += '<p class="cal-small cal-soluk" style="font-size:13px">Sonraki maaş (' + ayAd(sonraki.ay) + (sonraki.yil > sira.yil ? ", yeni yıl" : "") + "): " + tl(sonraki.sonuc.net) + " " +
            (Math.abs(f) >= 1 ? '<b style="color:' + (f > 0 ? "#1F6B4A" : "#B3261E") + '">' + fark(f) + "</b>" : "aynı") + "</p>";
        }
        if (S.ayar.net) k1 += '<p class="cal-small cal-soluk">Gereken brüt: ' + tl(sira.sonuc.brut) + " (vergi dilimi yükseldikçe artar)</p>";
        if (yeniYilSira) k1 += '<p class="cal-small cal-soluk">Yeni yıl: vergi matrahı sıfırdan başlar.</p>';
        h += card("maas", '<div class="cal-in cal-col" style="gap:3px;padding:22px">' + k1 + "</div>");

        // vergi dilimi
        var kum = sira.sonuc.devir.gvMatrah, gecis = o.sonrakiGecis;
        var k2 = '<h3 class="cal-sub cal-t-tazminat">Vergi diliminle ilgili</h3><p class="cal-p">Sıradaki maaşın (' + ayAd(sira.ay) + ") gelir vergisi diliminin " + yuzde(sira.dilimOrani) + " oranında hesaplandı. O ay sonunda bu yıl biriken vergi matrahın " + tl(kum, false) + ".</p>";
        if (gecis) {
          var gI = o.aylar.indexOf(gecis), sonrakiAy = o.aylar[gI + 1];
          var tamNet = (sonrakiAy || gecis).sonuc.net, ff = tamNet - sira.sonuc.net;
          var fm = Math.abs(ff) < 1 ? "" : " (sıradaki maaşına göre " + tl(Math.abs(ff), false) + " " + (ff < 0 ? "az" : "fazla") + ")";
          k2 += '<p class="cal-p"><b>' + ayAd(gecis.ay) + " ayında " + yuzde(gecis.dilimOrani) + " dilimine geçiyorsun. " + (sonrakiAy ? "Maaşın " + ayAd(gecis.ay) + "'da " + tl(gecis.sonuc.net, false) + ", " + ayAd(sonrakiAy.ay) + " ayından itibaren " + tl(sonrakiAy.sonuc.net, false) + " olacak" + fm + "." : "O ay maaşın " + tl(gecis.sonuc.net, false) + " olacak" + fm + ".") + "</b></p>";
        } else if (o.yeniYilOcak) {
          k2 += '<p class="cal-p">Yıl sonuna kadar diliminin değişmiyor. Ocak\'ta yeni yıl başlar: matrah sıfırlanır, vergi yeniden %15\'ten başlar ve maaşın ' + tl(o.yeniYilOcak.sonuc.net, false) + " olur (zam hariç).</p>";
        } else k2 += '<p class="cal-p">Yıl sonuna kadar diliminin değişmiyor; maaşın aynı kalıyor.</p>';
        var ust = dilimUst(P, kum);
        if (ust !== null && !gecis && sira.sonuc.gvMatrah > 0) {
          var kalanM = ust - kum, ayN = Math.ceil(kalanM / sira.sonuc.gvMatrah);
          if (ayN >= 1 && ayN <= 12) k2 += '<p class="cal-small cal-soluk">Bir üst dilime ' + tl(kalanM, false) + " matrah kaldı (≈ " + ayN + " ay).</p>";
        }
        h += card("tazminat", '<div class="cal-in cal-col" style="gap:8px">' + k2 + "</div>");

        // sigorta avantajı
        if (siz) {
          var odenen = o.aylar.reduce(function (x, a) { return x + a.primOdenen; }, 0);
          if (odenen > 0) {
            var indirilen = o.aylar.reduce(function (x, a) { return x + a.primIndirilen; }, 0), indirilebilir = pr.primBirikimli ? odenen * 0.5 : odenen;
            var iade = 0; o.aylar.forEach(function (a, i) { iade += a.sonuc.net - siz.aylar[i].sonuc.net; });
            var oa = o.aylar.filter(function (a) { return a.primOdenen > 0; });
            h += card("izin", '<div class="cal-in"><h3 class="cal-sub cal-t-izin">Sigorta vergi avantajı (bu yıl)</h3>' +
              sat("Ödenen prim (" + oa.length + " ay: " + ayAd(oa[0].ay, true) + "–" + ayAd(oa[oa.length - 1].ay, true) + ")", tl(odenen)) + sat("Vergi matrahından indirilen", tl(indirilen)) +
              (indirilebilir - indirilen > 1 ? sat("Sınırı aşan (indirilemez)", tl(indirilebilir - indirilen), { renk: "#B3261E" }) : "") +
              sat("Sigorta vergi iaden", "+ " + tl(iade), { vurgulu: 1, renk: "#1F5F8F" }) + sat("Sigortanın sana net maliyeti", tl(odenen - iade)) +
              not("İade = indirilen prim × o aylardaki gelir vergisi oranın. Sınır: ödediğin ayın brütünün %15'i ve yıllık asgari ücret brütü; tek seferde büyük ödeme yaparsan sınırı aşan kısım için iade alamazsın, taksit genelde daha avantajlıdır.") + "</div>");
          }
        }

        // zam kartı
        var zk = '<div class="cal-row"><div class="cal-grow"><b class="cal-sub" style="display:block">Zam gelirse ne olur?</b><span class="cal-small cal-soluk">Oranı ve ayı seç: net maaşın ve vergi dilimin nasıl değişir gör.</span></div>' + sw("zam", Z.acik) + "</div>";
        if (Z.acik) {
          var yuzdeler = [10, 20, 30, 40, 50].map(function (y) { return { id: y, t: "%" + y }; });
          var seciliY = Z.ozel === "" ? Z.yuzde : -1;
          zk += '<div class="cal-col" style="gap:6px"><span class="cal-small cal-soluk">Zam oranı</span>' + chips(yuzdeler, seciliY, "zamy", { vars: "--cb:#F7F3EC" }) + field("zam.ozel", "Başka oran", Z.ozel, { dolgu: "#F7F3EC", sonek: "%", ondalik: true }) + "</div>";
          var zay = []; for (var m = ilkZam; m <= 13; m++) zay.push({ id: m, t: m === 13 ? "Ocak (" + (Y(bugun) + 1) + ")" : ayAd(m, true) });
          zk += '<div class="cal-col" style="gap:6px"><span class="cal-small cal-soluk">Hangi aydan itibaren?</span>' + chips(zay, zamAy, "zamay", { vars: "--cb:#F7F3EC" }) + "</div>";
          zk += zamAy <= 12 ? zamOzeti(zamAy, oran, temel, o) : (yeni && yeni0 ? yeniYilOzeti(oran, yeni, yeni0, temel) : "");
        }
        h += card("yuzey", '<div class="cal-in cal-col" style="gap:12px">' + zk + "</div>");

        // yılın tamamı
        var ac = o.aylar.map(function (a, i) { return { id: i, t: (i === o.siraIndex ? "● " : "") + ayAd(a.ay, true), past: i < o.siraIndex }; });
        h += chips(ac, idx, "sec", { vars: "--co:#1F6B4A" });
        h += bars(o.aylar.map(function (a) { return a.sonuc.net; }), idx);
        h += ortalamaSatiri(o.aylar.map(function (a) { return a.ay; }), o.aylar.map(function (a) { return a.sonuc.net; }));
        h += not("● sıradaki maaşın ayı. Geçmiş aylar da aynı maaşla hesaplandı; gerçek bordron farklıysa Ayarlar'a son bordro matrahını ekle.");

        // döküm
        var s = o.aylar[idx], a2 = s.sonuc, hs = '<h3 class="cal-sub" style="margin-bottom:4px">' + ayAd(s.ay) + " dökümü</h3>";
        hs += sat("Brüt", tl(a2.brut)) + sat(pr.emekli ? "SGDP (%7,5)" : "SGK işçi payı (%14)", "− " + tl(a2.sgkIsci));
        if (!pr.emekli) hs += sat("İşsizlik (%1)", "− " + tl(a2.issizlik));
        hs += sat("Gelir vergisi (" + yuzde(s.dilimOrani) + " dilimi)", "− " + tl(a2.gelirVergisi)) + sat("Damga vergisi", "− " + tl(a2.damgaVergisi));
        if (s.primIndirilen > 0) hs += sat("Sigorta primi indirimi (matrahtan)", tl(s.primIndirilen), { renk: "#1F6B4A" });
        hs += sat("Asgari ücret gelir vergisi istisnası", "+ " + tl(a2.gvIstisnasi), { renk: "#1F6B4A" }) + sat("Asgari ücret damga istisnası", "+ " + tl(a2.damgaIstisnasi), { renk: "#1F6B4A" }) +
          sat("Elinize geçen", tl(a2.net), { vurgulu: 1 }) + sat("Kümülatif gelir vergisi matrahı", tl(a2.devir.gvMatrah, false));
        var sz = siz && siz.aylar[idx];
        if (sz && s.primOdenen > 0) {
          var iade2 = a2.net - sz.sonuc.net;
          hs += sat("Sigortasız olsaydı net", tl(sz.sonuc.net)) + sat("Sigorta vergi iadesi", "+ " + tl(iade2), { renk: "#1F6B4A" }) + sat("Ödediğin prim", tl(s.primOdenen)) + sat("Sigortanın sana net maliyeti", tl(s.primOdenen - iade2));
          var ib = pr.primBirikimli ? s.primOdenen * 0.5 : s.primOdenen;
          if (ib - s.primIndirilen > 1) hs += not("Ödediğin primin " + tl(ib - s.primIndirilen, false) + " kadarı sınırı (aylık brütün %15'i ya da yıllık asgari ücret) aştığı için indirilemedi.");
        }
        h += card("yuzey", '<div class="cal-in">' + hs + "</div>");

        h += tapCard("yuzey", "ayar", '<span class="cal-col" style="padding:20px;gap:2px"><span class="cal-small cal-soluk">Hesap bu bilgilerle yapıldı</span><span class="cal-p">' + e(profilOzeti()) + '</span><span class="cal-small cal-t-maas">Değiştirmek için dokun (Ayarlar ›)</span></span>');
        h += digerButon();
        h += not("Maaşın her ay aynı varsayılır (zam seçersen o aydan itibaren zamlı); ek ödeme ve fazla mesai hesaba katılmadı. Bordro yerine geçmez, bilgilendirme amaçlıdır. Daha doğru tahmin için Ayarlar'a son bordrondaki \"Toplam KGVM\"i, sigorta primini ve maaş gününü ekleyebilirsin.");
        return h + "</div>";
      }

      function zamOzeti(ay, oran, temel, zamli) {
        var i = -1; zamli.aylar.forEach(function (a, k) { if (a.ay === ay) i = k; });
        if (i < 0) return "";
        var z = zamli.aylar[i], t = temel.aylar[i];
        var artis = z.sonuc.net - t.sonuc.net, brutArtis = z.sonuc.brut - t.sonuc.brut;
        var h = '<div class="cal-col" style="gap:4px">' + sat(ayAd(ay) + " ayı maaşı (zamsız)", tl(t.sonuc.net)) + sat(ayAd(ay) + " ayı maaşı (%" + Math.round(oran * 100) + " zamlı)", tl(z.sonuc.net), { vurgulu: 1 }) + sat("Net artış", fark(artis), { renk: "#1F6B4A" }) +
          not("Brüt " + tl(brutArtis, false) + " artıyor ama net " + tl(artis, false) + " artıyor: farkı SGK payı ve gelir vergisi alıyor (zamlı ay " + yuzde(z.dilimOrani) + " diliminde bitiyor).");
        var g = zamli.sonrakiGecis, g0 = temel.sonrakiGecis;
        if (g && (!g0 || g.ay !== g0.ay)) h += '<p class="cal-small cal-t-tazminat" style="font-size:13px">Zamla birlikte ' + ayAd(g.ay) + " ayında " + yuzde(g.dilimOrani) + " dilimine geçiyorsun" + (g0 ? " (zamsız " + ayAd(g0.ay) + ")" : " (zamsız bu yıl geçmiyordun)") + ".</p>";
        // ortalama karşılaştırma
        var o0 = ort(temel.aylar.map(function (a) { return a.sonuc.net; })), o1 = ort(zamli.aylar.map(function (a) { return a.sonuc.net; }));
        if (o0 > 0) {
          var donem = ayAd(temel.aylar[0].ay, true) + "–" + ayAd(temel.aylar[temel.aylar.length - 1].ay, true), art = (o1 - o0) / o0;
          h += sat(donem + " ort. net (zamsız)", tl(o0)) + sat(donem + " ort. net (zamlı)", tl(o1), { vurgulu: 1 }) + sat("Net ortalama artışı", "%" + yuzdeTr(art * 100), { renk: "#1F6B4A" });
          h += ay > temel.aylar[0].ay ? not("Zam yalnızca yılın bir bölümüne uygulandığı için ortalamaya yansıması küçük görünür. Zammın tam yıllık etkisini görmek için Ocak (sonraki yıl) seçeneğini seç.")
            : not("Brüt maaşa %" + Math.round(oran * 100) + " zam, ortalama net maaşına %" + yuzdeTr(art * 100) + " olarak yansıyor; aradaki fark SGK payı ve (daha yüksek dilimlerde) gelir vergisi.");
        }
        var sonA = zamli.aylar[zamli.aylar.length - 1], sonT = temel.aylar[temel.aylar.length - 1];
        h += not("Aralık maaşı: " + tl(sonA.sonuc.net, false) + " (zamsız " + tl(sonT.sonuc.net, false) + ").");
        return h + "</div>";
      }
      function yeniYilOzeti(oran, y, y0, temel) {
        var si = clamp(S.yny === undefined ? 0 : S.yny, 0, y.aylar.length - 1), a = y.aylar[si];
        var h = '<div class="cal-col" style="gap:8px"><b class="cal-sub" style="font-size:15px">Yeni yıl (%' + Math.round(oran * 100) + " zamla, matrah Ocak'ta sıfırlanır)</b>";
        h += chips(y.aylar.map(function (m, i) { return { id: i, t: ayAd(m.ay, true) }; }), si, "ynysec", { vars: "--cb:#F7F3EC" });
        h += bars(y.aylar.map(function (m) { return m.sonuc.net; }), si).replace(/data-act="sec"/g, 'data-act="ynysec"');
        h += ortalamaSatiri(y.aylar.map(function (m) { return m.ay; }), y.aylar.map(function (m) { return m.sonuc.net; }));
        h += sat(ayAd(a.ay) + " maaşı", tl(a.sonuc.net), { vurgulu: 1 }) + sat("Brüt", tl(a.sonuc.brut));
        var g = y.sonrakiGecis;
        h += '<p class="cal-small cal-t-tazminat" style="font-size:13px">' + (g ? "Yeni yılda " + ayAd(g.ay) + " ayında " + yuzde(g.dilimOrani) + " dilimine geçiyorsun; maaşın düşmeye başlar." : "Yeni yıl boyunca vergi diliminin değişmiyor.") + "</p>";
        var simdi = ort(temel.aylar.map(function (m) { return m.sonuc.net; })), zamli = ort(y.aylar.map(function (m) { return m.sonuc.net; })), zamsiz = ort(y0.aylar.map(function (m) { return m.sonuc.net; }));
        if (simdi > 0 && zamsiz > 0) {
          var artis = (zamli - simdi) / simdi * 100, etki = (zamli - zamsiz) / zamsiz * 100;
          h += sat("Şimdiki ort. net (" + ayAd(temel.aylar[0].ay, true) + "–" + ayAd(temel.aylar[temel.aylar.length - 1].ay, true) + ")", tl(simdi)) + sat("Zamlı ort. net (Oca–Ara)", tl(zamli), { vurgulu: 1 }) + sat("Net ortalama artışı", "%" + yuzdeTr(artis), { renk: "#1F6B4A" }) +
            not("Brüt maaşa %" + Math.round(oran * 100) + " zam, ortalama net maaşına %" + yuzdeTr(artis) + " olarak yansıyor; aradaki fark SGK payı ve (daha yüksek dilimlerde) gelir vergisi.") +
            not("Aynı brütle zamsız Oca–Ara ortalaman " + tl(zamsiz, false) + " olurdu (matrah Ocak'ta sıfırlandığı için); zammın kendi etkisi %" + yuzdeTr(etki) + ".");
        }
        h += not("Şimdiki sıradaki maaşın " + tl(temel.siradaki.sonuc.net, false) + "; Ocak maaşın zamla " + tl(y.aylar[0].sonuc.net, false) + " olur (matrah sıfırlandığı için ilk aylar vergi dilimi düşük).");
        return h + "</div>";
      }

      // ------------------------------------------------ sayfa çatısı ve olaylar
      var SHEETS = {
        tazminat: ["🧳", "Tazminat", "Kıdem ve ihbar tazminatını işe giriş ve çıkış tarihin ile brüt ücretinden hesaplar, kesintilerle birlikte dökümünü gösterir."],
        mesai: ["⏱️", "Mesai", "Günlük çalışma saatlerini kaydet, haftalık hedefini ve fazla mesaini takip et; fazla mesainin maaşına etkisini gör."],
        izinler: ["📒", "İzinlerim", "Yıllık izin hakkını ve kullandığın izinleri kaydet; kalan izin günlerini tek bakışta gör."],
        hesap: ["🧮", "Maaş hesaplayıcı", "Başka bir maaşı dene: brütten nete, netten brüte ve 12 aylık tablo. Yeni iş teklifi ya da zam için ideal."],
        geri: ["✉️", "Geri bildirim", "Bu bir web demosudur. Geri bildirimini Google Play sayfasındaki uygulamadan, ya da nesim.razon@gmail.com adresine yazarak iletebilirsin."],
      };
      root.innerHTML = '<div class="cal-wrap"><div class="cal-phone"><div class="cal-screen"><div class="cal-island"></div><div class="cal-status"><span>9:41</span><span>5G ▮▮▮▯</span></div><div class="cal-body" tabindex="0"></div><div class="cal-sheet" aria-hidden="true"><div></div></div></div><div class="cal-homebar"></div></div>' +
        '<p class="cal-cap">Gerçek uygulamanın ekranları ve hesapları. Ayarlar, Net maaş ve İzin planı çalışır; diğer bölümler Android uygulamasında. Girdiğin bilgiler yalnızca bu tarayıcında saklanır.</p></div>';
      var body = root.querySelector(".cal-body"), sheet = root.querySelector(".cal-sheet"), sheetIn = sheet.firstChild;

      function render(keepScroll) {
        var st = body.scrollTop, ae = document.activeElement, fid = ae && root.contains(ae) && ae.id ? ae.id : null, sel = fid && ae.selectionStart !== undefined ? [ae.selectionStart, ae.selectionEnd] : null;
        body.innerHTML = S.page === "ana" ? anaHTML() : S.page === "tatil" ? tatilHTML() : S.page === "ayar" ? ayarHTML() : maasHTML();
        body.scrollTop = keepScroll ? st : 0;
        [].forEach.call(body.querySelectorAll(".cal-chips"), function (c) { var on = c.querySelector(".on"); if (on) c.scrollLeft = Math.max(0, on.offsetLeft - c.clientWidth / 2 + on.offsetWidth / 2); });
        if (fid) { var el = document.getElementById(fid); if (el && root.contains(el)) { el.focus({ preventScroll: true }); if (sel && el.setSelectionRange && el.type !== "date") try { el.setSelectionRange(sel[0], sel[1]); } catch (x) {} } }
        if (S.sheet) { var sh = SHEETS[S.sheet]; sheetIn.innerHTML = '<div class="cal-col" style="gap:10px"><span class="e">' + sh[0] + '</span><h3 class="cal-title" style="font-size:22px">' + sh[1] + '</h3><p class="cal-p cal-soluk" style="font-size:15px;line-height:1.5">' + sh[2] + '</p><p class="cal-p" style="font-weight:700">Bu bölüm Android uygulamasında.</p><a class="cal-play" href="' + e(play) + '" target="_blank" rel="noopener">▶ Google Play\'de aç</a><button type="button" class="cal-ghost" data-act="sheet-kapat">Kapat</button></div>'; sheet.classList.add("open"); sheet.setAttribute("aria-hidden", "false"); }
        else { sheet.classList.remove("open"); sheet.setAttribute("aria-hidden", "true"); }
        kaydet();
      }
      function start() { if (!S.started) { S.started = true; track("demo_start", { app: "calisan" }); } }
      function go(p) {
        start();
        if (p.indexOf("sheet:") === 0) { S.sheet = p.slice(6); track("demo_sheet", { app: "calisan", section: S.sheet }); render(true); return; }
        S.sheet = null;
        if (p === S.page) { render(true); return; }
        S.hist.push(S.page); S.page = p; S.balon = false; S.secili = null;
        track("demo_screen", { app: "calisan", screen: p });
        render(false);
      }
      function geri() { S.sheet = null; S.page = S.hist.pop() || "ana"; render(false); }

      root.addEventListener("click", function (ev) {
        var t = ev.target.closest && ev.target.closest("[data-go],[data-act]"); if (!t || !root.contains(t)) return;
        var g = t.getAttribute("data-go"), act = t.getAttribute("data-act"), v = t.getAttribute("data-v"), A = S.ayar;
        if (g) { ev.preventDefault(); go(g); return; }
        start();
        switch (act) {
          case "geri": geri(); return;
          case "sheet-kapat": S.sheet = null; render(true); return;
          case "balon": S.tikSay++; if (S.balon) S.mesajSira++; else { S.mesajSira = 0; S.balon = true; } render(true); return;
          case "balon-kapat": S.balon = false; render(true); return;
          case "net": A.net = v === "1"; render(true); return;
          case "maaszaman": A.sonrakiAy = v === "0"; render(true); return;
          case "primbas": A.primBas = +v; render(true); return;
          case "kgvmay": A.kgvmAy = +v; render(true); return;
          case "taksit-": A.primTaksit = Math.max(0, A.primTaksit - 1); render(true); return;
          case "taksit+": A.primTaksit = Math.min(12, A.primTaksit + 1); render(true); return;
          case "goster": if ((parseFloat(S.basla.tutar) || 0) > 0) { A.tutar = S.basla.tutar; render(false); } return;
          case "sil": S.ayar = { tutar: "", net: false, giris: null, emekli: false, sonrakiAy: true, gun: "5", sozlesme: "", prim: "", primBas: 1, primTaksit: 0, primBirikimli: false, kgvm: "", kgvmAy: M(bugun), kgvmYil: Y(bugun) }; S.zam = { acik: false, yuzde: 20, ozel: "", ayS: 0 }; S.basla.tutar = ""; S.secili = null; render(false); return;
          case "giris-temizle": A.giris = null; render(true); return;
          case "zamy": S.zam.yuzde = +v; S.zam.ozel = ""; render(true); return;
          case "zamay": S.zam.ayS = +v; S.yny = 0; render(true); return;
          case "sec": S.secili = +v; render(true); return;
          case "ynysec": S.yny = +v; render(true); return;
          case "yil": S.yil = +v; render(true); return;
          case "izin": S.izinSecimi = +v; render(true); return;
        }
      });
      root.addEventListener("input", function (ev) {
        var t = ev.target, f = t.getAttribute && t.getAttribute("data-f"); if (!f) return;
        start();
        var raw = t.value, A = S.ayar;
        var temiz = f === "ayar.gun" || f === "ayar.sozlesme" ? raw.replace(/\D/g, "").slice(0, 2) : ondalikTemizle(raw);
        if (t.value !== temiz) t.value = temiz;
        if (f === "ayar.tutar") A.tutar = temiz; else if (f === "ayar.gun") A.gun = temiz; else if (f === "ayar.sozlesme") A.sozlesme = temiz; else if (f === "ayar.prim") A.prim = temiz;
        else if (f === "ayar.kgvm") { A.kgvm = temiz; A.kgvmYil = Y(bugun); var box = document.getElementById("cal-kgvm-ay"); if (box) box.style.display = temiz === "" ? "none" : ""; }
        else if (f === "basla.tutar") { S.basla.tutar = temiz; var b = document.getElementById("cal-goster"); if (b) b.disabled = !((parseFloat(temiz) || 0) > 0); }
        else if (f === "zam.ozel") { S.zam.ozel = temiz; render(true); }
        kaydet();
      });
      root.addEventListener("change", function (ev) {
        var t = ev.target, c = t.getAttribute && t.getAttribute("data-chg"); if (!c) return;
        start();
        if (c === "emekli") S.ayar.emekli = t.checked; else if (c === "birikimli") S.ayar.primBirikimli = t.checked;
        else if (c === "zam") { S.zam.acik = t.checked; S.zam.ayS = 0; S.yny = 0; }
        else if (c === "giris") {
          // Elle yazarken tarayıcı yılın her rakamında (0002, 0020, 0202, 2026) "değişti" der: ekranı yeniden çizmek alanı sıfırlayıp odağı güne döndürür.
          // Bu yüzden burada yalnız durumu güncelleriz (geçerli aralık: 2000-2100), yeniden çizmeyiz.
          var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(t.value);
          S.ayar.giris = m && +m[1] >= 2000 && +m[1] <= 2100 ? ld(+m[1], +m[2], +m[3]) : null;
          kaydet();
          return;
        }
        render(true);
      });

      render(false);
      var api2 = { state: S, go: go, render: render, setProfil: function (o) { for (var k in o) S.ayar[k] = o[k]; render(false); }, setBugun: function (d) { bugun = d; render(false); } };
      root.__cal = api2;
      return api2;
    }

    var st = document.createElement("style"); st.textContent = CSS; document.head.appendChild(st);
    api.mount = mount;
    function auto() { [].forEach.call(document.querySelectorAll("[data-calisan]"), mount); }
    if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", auto); else auto();
  })();

  if (typeof module !== "undefined" && module.exports) module.exports = api;
  if (typeof window !== "undefined") window.CalisanDemo = api;
})();
