/* Yilbasi cekilisi (gizli hediye arkadasi) algoritmasi: kimse kendini cekmez, "birbirini cekmesin" kisitlarina uyar,
   mumkunse TEK BUYUK DONGU kurar (A->B->C->...->A; boylece A->B, B->A gibi karsilikli eslesme olmaz).
   Tarayicida ve node'da calisir (tools/cekilis.test.js). Hicbir sunucuya veri gitmez. */
(function (root) {
  "use strict";

  function shuffle(a, rnd) {
    a = a.slice();
    for (var i = a.length - 1; i > 0; i--) {
      var j = Math.floor(rnd() * (i + 1));
      var t = a[i]; a[i] = a[j]; a[j] = t;
    }
    return a;
  }

  /* names: ["Ayse", ...]; excl: [["Ayse","Mehmet"], ...] (iki yonlu: ikisi birbirini cekmez) */
  function draw(names, excl, rnd) {
    rnd = rnd || Math.random;
    var n = names.length;
    var ban = {};
    names.forEach(function (x) { ban[x] = {}; ban[x][x] = true; });
    (excl || []).forEach(function (p) {
      if (ban[p[0]] && ban[p[1]]) { ban[p[0]][p[1]] = true; ban[p[1]][p[0]] = true; }
    });
    var tries = 0;
    // 1) tek buyuk dongu (geri izleme)
    while (tries++ < 60) {
      var order = shuffle(names, rnd), cycle = [order[0]], used = {}; used[order[0]] = true;
      if (cyc(order[0], cycle, used, ban, names, rnd, n, { n: 0 })) {
        var res = {};
        for (var i = 0; i < n; i++) res[cycle[i]] = cycle[(i + 1) % n];
        return { map: res, cycle: true };
      }
    }
    // 2) genel (dongu sart degil): rastgele geri izleme
    var res2 = {}, taken = {};
    var order2 = shuffle(names, rnd);
    var nodes = { n: 0 };
    if (assign(order2, 0, res2, taken, ban, rnd, nodes)) return { map: res2, cycle: false };
    return null;
  }

  function cyc(cur, cycle, used, ban, names, rnd, n, nodes) {
    if (cycle.length === n) return !ban[cur][cycle[0]];
    var cand = shuffle(names, rnd);
    for (var i = 0; i < cand.length; i++) {
      var c = cand[i];
      if (used[c] || ban[cur][c]) continue;
      if (++nodes.n > 4000) return false;
      used[c] = true; cycle.push(c);
      if (cyc(c, cycle, used, ban, names, rnd, n, nodes)) return true;
      used[c] = false; cycle.pop();
    }
    return false;
  }

  function assign(order, k, res, taken, ban, rnd, nodes) {
    if (k === order.length) return true;
    if (++nodes.n > 50000) return false;
    var giver = order[k], cand = shuffle(order, rnd);
    for (var i = 0; i < cand.length; i++) {
      var c = cand[i];
      if (taken[c] || ban[giver][c]) continue;
      taken[c] = true; res[giver] = c;
      if (assign(order, k + 1, res, taken, ban, rnd, nodes)) return true;
      taken[c] = false; delete res[giver];
    }
    return false;
  }

  /* Hizli olasilik kontrolu: her kisinin aday sayisi > 0 ve (n>=3) */
  function feasible(names, excl) {
    if (names.length < 3) return false;
    var r = draw(names, excl);
    return !!r;
  }

  /* Baglanti verisi: URL '#' kisminda (sunucuya gitmez) base64url JSON. Sifreleme DEGIL: baglantiyi acan gorur. */
  function encode(obj) {
    var json = JSON.stringify(obj);
    var b = (typeof Buffer !== "undefined") ? Buffer.from(json, "utf8").toString("base64")
      : btoa(unescape(encodeURIComponent(json)));
    return b.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  }
  function decode(s) {
    s = s.replace(/-/g, "+").replace(/_/g, "/");
    while (s.length % 4) s += "=";
    var json = (typeof Buffer !== "undefined") ? Buffer.from(s, "base64").toString("utf8")
      : decodeURIComponent(escape(atob(s)));
    return JSON.parse(json);
  }

  var api = { draw: draw, feasible: feasible, encode: encode, decode: decode };
  if (typeof module !== "undefined" && module.exports) module.exports = api; else root.CekilisDraw = api;
})(typeof self !== "undefined" ? self : this);
