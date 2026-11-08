# -*- coding: utf-8 -*-
"""Nudgelings gizlilik sayfasini (nudgelings/privacy.html) Grumblings'inkinden turetir: ayni hizmetler (AdMob, Firebase, Play Games, Billing),
Nudgelings'e ozgu isim, renk ve oyun tanimi. Calistir: py -3 tools/gen_privacy_nudgelings.py"""
import io, os

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "grumblings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#1E1A3C; --card:#2E2761; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFD84D; --link:#B7A4FF;",
     "--bg:#0F2F28; --card:#184A3E; --text:#F1FAF6; --dim:#C9E8DC; --accent:#FFD84D; --link:#8FDCC0;"),
    ("Grumblings", "Nudgelings"),
    ("Effective date: 7 November 2026", "Effective date: 9 November 2026"),
    ("Yürürlük tarihi: 7 Kasım 2026", "Yürürlük tarihi: 9 Kasım 2026"),
    ("Fecha de entrada en vigor: 7 de noviembre de 2026", "Fecha de entrada en vigor: 9 de noviembre de 2026"),
    ("Data de vigência: 7 de novembro de 2026", "Data de vigência: 9 de novembro de 2026"),
    ("is a turn-based maze puzzle game in which you escape from grumpy monsters", "is a puzzle game with two modes, Slide and Push, starring cute little creatures"),
    ("huysuz canavarlardan kaçtığın sıra tabanlı bir labirent bulmaca oyunudur", "sevimli minik yaratıkların başrolde olduğu, Kaydır ve İt modlu bir bulmaca oyunudur"),
    ("un juego de puzles de laberinto por turnos en el que escapas de monstruos gruñones", "un juego de puzles con dos modos, Deslizar y Empujar, protagonizado por criaturitas adorables"),
    ("um jogo de quebra-cabeças de labirinto por turnos em que você escapa de monstros rabugentos", "um jogo de quebra-cabeças com dois modos, Deslizar e Empurrar, estrelado por criaturinhas fofas"),
    ("hero outfit", "Nudgeling outfit"),
    ("kahraman kıyafetin", "Nudgeling kıyafetin"),
    ("el atuendo de tu héroe", "el disfraz de tu Nudgeling"),
    ("a roupa do seu herói", "a fantasia do seu Nudgeling"),
]
out = src
for a, b in R:
    if a not in out:
        print("UYARI: bulunamadi:", a[:80])
    out = out.replace(a, b)

dst = os.path.join(G, "nudgelings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"))
