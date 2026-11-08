# -*- coding: utf-8 -*-
"""Astrolings haftalik tema paketi uretici ve denetleyici.
  py -3 -X utf8 tools/astrolings_paket.py build   -> ../Astrolings/banka/hafta_*.json dosyalarini birlestirir, astrolings/v1/<yil-ay>.json + surum.json yazar
  py -3 -X utf8 tools/astrolings_paket.py kontrol -> surum.json'da gelecek 2 ay icin paket var mi (GitHub Action kullanir); eksikse cikis kodu 1 ve eksik aylari yazar
Paket bicimi: {"ay": "2026-11", "haftalar": [{"hafta": "2026-W45", "burclar": {"koc": {"tema": "..."}, ...}}, ...]}
Bir ISO haftasi, en az bir gunu o ayda olan HER ay dosyasina girer (uygulama gunun ayina gore dosya acar)."""
import datetime, glob, hashlib, json, os, sys

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
V1 = os.path.join(G, "astrolings", "v1")
BANKA = os.path.join(os.path.dirname(G), "Astrolings", "banka")


def week_days(week):
    y, w = week.split("-W")
    mon = datetime.date.fromisocalendar(int(y), int(w), 1)
    return [mon + datetime.timedelta(days=i) for i in range(7)]


def build():
    merged = {}  # kod -> hafta -> metin
    for f in sorted(glob.glob(os.path.join(BANKA, "hafta_*.json"))):
        if os.path.basename(f).startswith("hafta_olaylari"):
            continue
        for code, weeks in json.load(open(f, encoding="utf-8")).items():
            merged.setdefault(code, {}).update(weeks)
    weeks = sorted({w for v in merged.values() for w in v})
    months = {}
    for w in weeks:
        for d in week_days(w):
            months.setdefault("%04d-%02d" % (d.year, d.month), set()).add(w)
    os.makedirs(V1, exist_ok=True)
    index = {"paketler": {}}
    for ay, ws in sorted(months.items()):
        # yalniz tamamen yazilmis haftalar (12 burc) paketlenir
        done = [w for w in sorted(ws) if all(w in merged.get(c, {}) for c in ("koc", "boga", "ikizler", "yengec", "aslan", "basak", "terazi", "akrep", "yay", "oglak", "kova", "balik"))]
        if not done:
            continue
        pack = {"ay": ay, "haftalar": [{"hafta": w, "burclar": {c: {"tema": merged[c][w]} for c in merged if w in merged[c]}} for w in done]}
        data = json.dumps(pack, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        open(os.path.join(V1, ay + ".json"), "wb").write(data)
        index["paketler"][ay] = {"boyut": len(data), "sha": hashlib.sha256(data).hexdigest()}
    index["son"] = max(index["paketler"]) if index["paketler"] else ""
    open(os.path.join(V1, "surum.json"), "w", encoding="utf-8", newline="\n").write(json.dumps(index, ensure_ascii=False, indent=1))
    print("yazildi:", ", ".join("%s (%d bayt)" % (k, v["boyut"]) for k, v in index["paketler"].items()))


def kontrol():
    today = datetime.date.today()
    need = []
    for k in (1, 2):
        m = today.month - 1 + k
        need.append("%04d-%02d" % (today.year + m // 12, m % 12 + 1))
    try:
        have = set(json.load(open(os.path.join(V1, "surum.json"), encoding="utf-8"))["paketler"])
    except Exception:
        have = set()
    missing = [n for n in need if n not in have]
    if missing:
        print("EKSIK: " + ", ".join(missing))
        sys.exit(1)
    print("TAMAM: " + ", ".join(need))


if __name__ == "__main__":
    {"build": build, "kontrol": kontrol}[sys.argv[1]]()
