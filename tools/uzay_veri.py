"""Uzay Gunlugu gunluk veri hatti: NASA/JPL kaynaklarindan uzay/bugun.json uretir.

Hepsi anahtarsiz (APOD yeni API, EPIC, CNEOS, EONET, CelesTrak, GIBS). Bir kaynak
cokerse onceki bugun.json'daki degeri korunur (tek kaynak kesintisi uygulamayi bozmaz).
Calistirma: py -3 -I tools/uzay_veri.py   (cikti: uzay/bugun.json)
"""
import datetime
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CIKTI = os.path.join(KOK, "uzay", "bugun.json")
UA = {"User-Agent": "UzayGunlugu-veri/1.0 (+https://nrazon.github.io/uzay/)"}
AU_KM = 149597870.7
AY_KM = 384400.0


def getir(url, deneme=5, bekle=3):
    """GET + yeniden deneme (images-api ve bazi NASA sunuculari aralikli baglanti sifirlar)."""
    son = None
    for i in range(deneme):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            son = e
            if e.code in (404, 400):
                break
        except Exception as e:  # ConnectionReset, timeout...
            son = e
        time.sleep(bekle * (i + 1))
    raise RuntimeError(f"{url}: {son}")


def json_getir(url):
    return json.loads(getir(url).decode("utf-8"))


def temiz(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]*>", "", s or "")).strip()


def ilk_cumleler(s, sinir=320):
    s = temiz(s)
    if len(s) <= sinir:
        return s
    kes = s[:sinir]
    nokta = kes.rfind(". ")
    return (kes[: nokta + 1] if nokta > 80 else kes.rstrip() + "…")


# NASA kaynakli (kamu malina yakin) kredi kalibi: ucuncu taraf ad iceren kayitlar False.
NASA_KREDI = re.compile(r"^(image credit:?\s*)?((nasa|esa|jpl|caltech|stsci|cxc|jaxa|csa|usgs|noaa|gsfc|jhuapl|swri|msss|ssi|arizona|isro)[\s,;&/\-()]*)+$", re.I)


def apod():
    veri = json_getir("https://science.nasa.gov/wp-json/wp/v2/apod-basic?per_page=10"
                      "&_fields=date,title,media_type,permalink,explanation,copyright,credit")
    cikti = []
    for x in veri:
        kredi = temiz(x.get("credit"))
        telif = temiz(x.get("copyright"))
        sade = re.sub(r"(image\s+)?credit:?|&amp;|\band\b", " ", kredi, flags=re.I).strip()
        nasa = not telif and bool(sade) and bool(NASA_KREDI.match(sade))
        cikti.append({
            "tarih": x["date"], "baslik": temiz(x["title"]), "tur": x.get("media_type"),
            "baglanti": x.get("permalink"), "ozet_en": ilk_cumleler(x.get("explanation")),
            "kredi": kredi, "nasa_kaynakli": nasa,
        })
    return cikti


def epic():
    liste = json_getir("https://epic.gsfc.nasa.gov/api/natural")
    if not liste:
        raise RuntimeError("epic bos")
    gun = liste[0]["date"][:10]
    y, a, g = gun.split("-")
    kareler = []
    for k in liste:
        if k["date"][:10] != gun:
            continue
        kareler.append({
            "zaman": k["date"],
            "enlem": round(k["centroid_coordinates"]["lat"], 2),
            "boylam": round(k["centroid_coordinates"]["lon"], 2),
            "url": f"https://epic.gsfc.nasa.gov/archive/natural/{y}/{a}/{g}/jpg/{k['image']}.jpg",
            "kucuk": f"https://epic.gsfc.nasa.gov/archive/natural/{y}/{a}/{g}/thumbs/{k['image']}.jpg",
        })
    return {"gun": gun, "kareler": kareler, "kredi": "NASA EPIC / DSCOVR"}


def asteroitler(bugun):
    d1 = bugun.isoformat()
    d2 = (bugun + datetime.timedelta(days=14)).isoformat()
    v = json_getir(f"https://ssd-api.jpl.nasa.gov/cad.api?date-min={d1}&date-max={d2}"
                   "&dist-max=0.05&sort=date&fullname=true")
    alanlar = v["fields"]
    cikti = []
    for satir in v.get("data", []):
        r = dict(zip(alanlar, satir))
        h = float(r["h"]) if r.get("h") else None
        # Parlaklik (H) -> cap tahmini (albedo 0.14): 1329/sqrt(p) * 10^(-H/5) km
        cap_m = round(1329 / math.sqrt(0.14) * 10 ** (-h / 5) * 1000) if h is not None else None
        cikti.append({
            "ad": temiz(r.get("fullname")), "tarih": r["cd"],
            "mesafe_ay": round(float(r["dist"]) * AU_KM / AY_KM, 1),  # Ay mesafesi cinsinden
            "hiz_kms": round(float(r["v_rel"]), 1), "cap_m": cap_m,
        })
    return {"aralik": [d1, d2], "liste": cikti[:12], "kredi": "NASA/JPL CNEOS"}


def eonet():
    v = json_getir("https://eonet.gsfc.nasa.gov/api/v3/events?status=open&limit=15")
    cikti = []
    for e in v.get("events", []):
        g = (e.get("geometry") or [{}])[-1]
        koor = g.get("coordinates") or []
        cikti.append({
            "baslik": temiz(e["title"]), "tur": (e.get("categories") or [{}])[0].get("title"),
            "tarih": (g.get("date") or "")[:10],
            "boylam": koor[0] if len(koor) == 2 and isinstance(koor[0], (int, float)) else None,
            "enlem": koor[1] if len(koor) == 2 and isinstance(koor[1], (int, float)) else None,
        })
    return {"liste": cikti, "kredi": "NASA EONET"}


def iss_tle():
    v = json_getir("https://celestrak.org/NORAD/elements/gp.php?CATNR=25544&FORMAT=json")
    return v[0] if v else None


def gibs(bugun):
    dun = (bugun - datetime.timedelta(days=1)).isoformat()
    sablon = ("https://wvs.earthdata.nasa.gov/api/v1/snapshot?REQUEST=GetSnapshot&LAYERS={k}"
              "&CRS=EPSG:4326&TIME={t}&WRAP=DAY&BBOX=34.0,25.0,43.0,45.5&FORMAT=image/jpeg"
              "&WIDTH=1230&HEIGHT=540&AUTOSCALE=FALSE")
    return {
        "tarih": dun,
        "turkiye": sablon.format(k="VIIRS_SNPP_CorrectedReflectance_TrueColor", t=dun),
        "kredi": "NASA GIBS / Worldview",
    }


def main():
    simdi = datetime.datetime.now(datetime.timezone.utc)
    bugun = simdi.date()
    eski = {}
    if os.path.exists(CIKTI):
        try:
            with open(CIKTI, encoding="utf-8") as f:
                eski = json.load(f)
        except Exception:
            pass
    sonuc = {"uretim": simdi.strftime("%Y-%m-%dT%H:%M:%SZ"), "surum": 1}
    hatalar = []
    for ad, fn in (("apod", apod), ("epic", epic), ("asteroitler", lambda: asteroitler(bugun)),
                   ("eonet", eonet), ("iss_tle", iss_tle), ("gibs", lambda: gibs(bugun))):
        try:
            sonuc[ad] = fn()
        except Exception as e:
            hatalar.append(f"{ad}: {e}")
            if ad in eski:
                sonuc[ad] = eski[ad]
    if hatalar:
        print("UYARI:\n  " + "\n  ".join(hatalar), file=sys.stderr)
    eksik = [k for k in ("apod", "epic", "asteroitler") if k not in sonuc]
    if eksik:
        print("HATA: zorunlu kaynak yok:", eksik, file=sys.stderr)
        sys.exit(1)
    os.makedirs(os.path.dirname(CIKTI), exist_ok=True)
    with open(CIKTI, "w", encoding="utf-8", newline="\n") as f:
        json.dump(sonuc, f, ensure_ascii=False, indent=1)
        f.write("\n")
    print("yazildi:", CIKTI, os.path.getsize(CIKTI), "bayt;",
          "epic kare:", len(sonuc["epic"]["kareler"]), "| asteroit:", len(sonuc["asteroitler"]["liste"]),
          "| apod nasa-kaynakli:", sum(a["nasa_kaynakli"] for a in sonuc["apod"]), "/", len(sonuc["apod"]))


if __name__ == "__main__":
    main()
