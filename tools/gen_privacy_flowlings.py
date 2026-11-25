# -*- coding: utf-8 -*-
"""Flowlings gizlilik sayfasini (flowlings/privacy.html) Slinglings'inkinden turetir: ayni hizmetler (AdMob+UMP, Firebase Analytics/Crashlytics,
Play Games, Play Billing, uygulama ici guncelleme). Flowlings'e ozgu isim, renk ve oyun tanimi. Calistir: py -3 tools/gen_privacy_flowlings.py
Yururluk tarihi YAYIN GUNUNDE guncellenir (DATE_*)."""
import io, os, re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "slinglings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#1B2540; --card:#27345A; --text:#F6F1E6; --dim:#D9DFF0; --accent:#FFD84D; --link:#9CC3FF;",
     "--bg:#12433F; --card:#1C5A54; --text:#F6F1E6; --dim:#CFE9E2; --accent:#FFD84D; --link:#8FE0D0;"),
    ("Slinglings", "Flowlings"),
    ("Effective date: 23 November 2026", "Effective date: 26 November 2026"),
    ("Yürürlük tarihi: 23 Kasım 2026", "Yürürlük tarihi: 26 Kasım 2026"),
    ("Fecha de entrada en vigor: 23 de noviembre de 2026", "Fecha de entrada en vigor: 26 de noviembre de 2026"),
    ("Data de vigência: 23 de novembro de 2026", "Data de vigência: 26 de novembro de 2026"),
    ("is a physics puzzle game in which you sling cute mail couriers through space", "is a pipe puzzle in which you lay pipes to bring energy to sleeping plant creatures"),
    ("sevimli postacıları uzayda fırlattığın bir fizik bulmaca oyunudur", "uyuyan sevimli bitki yaratıklarına enerji ulaştırmak için boru döşediğin bir bulmaca oyunudur"),
    ("un juego de puzles de física en el que lanzas carteros adorables por el espacio", "un juego de puzles en el que colocas tuberías para llevar energía a criaturas vegetales dormidas"),
    ("um jogo de quebra-cabeças de física em que você lança carteiros fofos pelo espaço", "um jogo de quebra-cabeças em que você posiciona canos para levar energia a criaturas vegetais adormecidas"),
    ("best shots", "best tap counts"), ("courier accessories", "unlocked plants"),
    ("en iyi atış sayıların", "en iyi dokunuş sayıların"), ("postacı aksesuarların", "uyandırdığın bitkilerin"),
    ("tus mejores tiros", "tus mejores recuentos de toques"), ("los accesorios de tu cartero", "las plantas desbloqueadas"),
    ("seus melhores tiros", "suas melhores contagens de toques"), ("os acessórios do seu carteiro", "as plantas desbloqueadas"),
    ("best shots", "best tap counts"), ("number of shots", "number of taps"),
    ("atış sayısı", "dokunuş sayısı"), ("número de tiros", "número de toques"),
    ("(sayaçlar, yıldızlar, en iyi atış sayıları ve günlük kayıtlar)", "(sayaçlar, yıldızlar, en iyi dokunuş sayıları ve günlük kayıtlar)"),
    ("(counters, stars, best shots and daily records)", "(counters, stars, best tap counts and daily records)"),
    ("mejores tiros", "mejores recuentos de toques"), ("melhores tiros", "melhores contagens de toques"),
    ("stars earned, how many hints you used and how long it took", "stars earned, how many hints you used and how long it took"),
]
out = src
for a, b in R:
    out = out.replace(a, b)
for bad in ("courier", "postacı", "cartero", "carteiro", "shots", "atış", "tiros", "sling", "fırlat", "lanz", "lança"):
    for m in re.finditer(bad, out, flags=re.I):
        print("UYARI: kalan Slinglings ifadesi:", out[max(0, m.start() - 60):m.end() + 60].replace("\n", " "))
dst = os.path.join(G, "flowlings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"))
