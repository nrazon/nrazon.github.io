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
