# -*- coding: utf-8 -*-
"""Pentolings site gorselleri: simge (192px) + ekran goruntusu kucukleri (360x630 JPG) market_assets'ten.
Calistir: py -3 -X utf8 tools/pentolings_assets.py   (ekran goruntuleri yenilenince tekrar)"""
import os
from PIL import Image

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = os.path.join(os.path.dirname(G), "Pentolings", "market_assets")
dst = os.path.join(G, "pentolings")
os.makedirs(dst, exist_ok=True)
Image.open(os.path.join(M, "icon-512.png")).convert("RGBA").resize((192, 192), Image.LANCZOS).save(os.path.join(dst, "icon.png"), optimize=True)
for lg in ("en", "tr", "es", "pt"):
    src = os.path.join(M, "screenshots", lg)
    out = os.path.join(dst, "shots", lg)
    os.makedirs(out, exist_ok=True)
    files = sorted(f for f in os.listdir(src) if f.endswith(".png"))
    for i, f in enumerate(files, 1):
        Image.open(os.path.join(src, f)).convert("RGB").resize((360, 630), Image.LANCZOS).save(os.path.join(out, f"{i:02d}.jpg"), quality=82, optimize=True)
    print(lg, len(files))
