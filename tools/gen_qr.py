# Masaüstü ziyaretçiler için "QR ile yükle" görselleri: qr/<slug>.svg (Play sayfasının adresi, utm_medium=qr).
# SVG'ler depoya konur (commit); gen_home.py / gen_site.py yalnızca bu dosyalara bağlanır, bu betik yeni uygulama eklenince ya da
# paket adı değişince çalıştırılır:  py -3 -m pip install --user segno   (bir kez)   ve   py -3 tools/gen_qr.py
# Play Console > Mağaza girişi edinimi > UTM kırılımında utm_medium=qr "QR'dan gelen yüklemeler"dir.
import json
import os

import segno

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = json.load(open(os.path.join(G, "tools", "home_data.json"), encoding="utf-8"))
OUT = os.path.join(G, "qr")
UTM = "&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dqr"
os.makedirs(OUT, exist_ok=True)
n = 0
for a in DATA:
    pkg = a.get("pkg")
    if not pkg:
        print("pkg yok, atlandı:", a["slug"])
        continue
    url = f"https://play.google.com/store/apps/details?id={pkg}{UTM}"
    # hata düzeltme M: ekranda taranırken yeterli, kod çok yoğunlaşmaz. Koyu desen + beyaz zemin (koyu temada da okunur).
    q = segno.make(url, error="m", micro=False)
    q.save(os.path.join(OUT, a["slug"] + ".svg"), kind="svg", scale=4, border=2, dark="#111111", light="#ffffff", xmldecl=False, nl=False)
    n += 1
print(n, "QR üretildi ->", OUT)

# iOS uygulamaları (tools/ios_apps.json: slug -> Apple ID): TEK evrensel QR = https://nrazon.github.io/go/<slug>/ ; sayfa telefonun
# işletim sistemine göre Play'e (utm_medium=qr, Play Console QR kırılımı korunur) ya da App Store'a yönlendirir; masaüstünde/JS yoksa iki rozet.
IOS = json.load(open(os.path.join(G, "tools", "ios_apps.json"), encoding="utf-8"))
def apple_url(v):
    """tools/ios_apps.json değeri: "<Apple ID>" (genel bağlantı, ziyaretçinin mağazasına yönlenir) ya da "<ülke>:<Apple ID>" (yalnız o mağazada yayında olan uygulama: örn. Şans Oyunları "tr:1438867538"; genel bağlantı başka ülkelerde 404 verir)."""
    if ":" in str(v):
        c, i = str(v).split(":", 1)
        return f"https://apps.apple.com/{c}/app/id{i}"
    return f"https://apps.apple.com/app/id{v}"
NAMES = {a["slug"]: a["names"] for a in DATA}
PKGS = {a["slug"]: a.get("pkg") for a in DATA}
GO_PAGE = """<!doctype html>
<html lang="tr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>__NAME__</title>
<style>
  body { margin:0; min-height:100vh; display:flex; align-items:center; justify-content:center; background:#12141C; color:#F3F4FA; font:16px/1.5 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; text-align:center; }
  main { padding:24px; max-width:420px; }
  h1 { font-size:26px; margin:0 0 6px; }
  p { color:#B4B9CC; margin:0 0 20px; }
  .b { display:flex; flex-wrap:wrap; gap:12px; justify-content:center; }
  .b img { height:52px; width:auto; display:block; }
  a.s { color:#B9C3FF; font-size:14px; display:inline-block; margin-top:18px; }
</style>
</head>
<body>
<main>
  <h1>__NAME__</h1>
  <p id="m"><span lang="tr">Telefonunuza uygun mağaza açılıyor…</span><span lang="en" hidden>Opening the right store for your phone…</span></p>
  <div class="b">
    <a href="__PLAY__"><img src="../../badges/google-play-tr.svg" alt="Google Play"></a>
    <a href="__APPLE__"><img src="../../badges/app-store-tr.svg" alt="App Store"></a>
  </div>
  <a class="s" href="../../__SLUG__/">__NAME__ · nrazon.github.io</a>
</main>
<script>
(function () {
  var ua = navigator.userAgent || "";
  var touch = navigator.maxTouchPoints > 1;
  var ios = /iPhone|iPad|iPod/.test(ua) || (/Macintosh/.test(ua) && touch); // iPadOS 13+ Mac gibi görünür
  var android = /Android/.test(ua);
  var m = document.getElementById("m");
  if (!ios && !android) {
    // Masaüstü ya da bilinmeyen: yönlendirme yok, iki rozet kalır.
    m.innerHTML = (/^tr/i.test(navigator.language) ? "Mağaza seçin:" : "Choose a store:");
    return;
  }
  if (!/^tr/i.test(navigator.language)) { var sp = m.children; sp[0].hidden = true; sp[1].hidden = false; }
  location.replace(ios ? "__APPLE__" : "__PLAY__");
})();
</script>
</body>
</html>
"""
for slug, apple_id in IOS.items():
    go_url = f"https://nrazon.github.io/go/{slug}/"
    q = segno.make(go_url, error="m", micro=False)
    q.save(os.path.join(OUT, slug + ".svg"), kind="svg", scale=4, border=2, dark="#111111", light="#ffffff", xmldecl=False, nl=False)
    stale = os.path.join(OUT, slug + "-ios.svg")
    if os.path.exists(stale):
        os.remove(stale)
    play = f"https://play.google.com/store/apps/details?id={PKGS[slug]}{UTM}"
    apple = apple_url(apple_id)
    d = os.path.join(G, "go", slug)
    os.makedirs(d, exist_ok=True)
    page = GO_PAGE.replace("__NAME__", NAMES[slug].get("tr") or NAMES[slug]["en"]).replace("__PLAY__", play.replace("&", "&amp;") if False else play).replace("__APPLE__", apple).replace("__SLUG__", slug)
    open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(page)
    print("iOS evrensel QR + go sayfası:", slug)
