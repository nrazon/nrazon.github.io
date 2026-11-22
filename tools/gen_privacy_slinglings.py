# -*- coding: utf-8 -*-
"""Slinglings gizlilik sayfasini (slinglings/privacy.html) Nudgelings'inkinden turetir: ayni hizmetler (AdMob, Firebase, Play Games, Billing),
Slinglings'e ozgu isim, renk ve oyun tanimi. Calistir: py -3 tools/gen_privacy_slinglings.py
Yurur luk tarihi YAYIN GUNUNDE guncellenir (asagidaki DATE_*)."""
import io, os

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "nudgelings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#0F2F28; --card:#184A3E; --text:#F1FAF6; --dim:#C9E8DC; --accent:#FFD84D; --link:#8FDCC0;",
     "--bg:#1B2540; --card:#27345A; --text:#F6F1E6; --dim:#D9DFF0; --accent:#FFD84D; --link:#9CC3FF;"),
    ("Nudgelings", "Slinglings"),
    ("Effective date: 9 November 2026", "Effective date: 23 November 2026"),
    ("Yürürlük tarihi: 9 Kasım 2026", "Yürürlük tarihi: 23 Kasım 2026"),
    ("Fecha de entrada en vigor: 9 de noviembre de 2026", "Fecha de entrada en vigor: 23 de noviembre de 2026"),
    ("Data de vigência: 9 de novembro de 2026", "Data de vigência: 23 de novembro de 2026"),
    ("is a puzzle game with two modes, Slide and Push, starring cute little creatures", "is a physics puzzle game in which you sling cute mail couriers through space"),
    ("sevimli minik yaratıkların başrolde olduğu, Kaydır ve İt modlu bir bulmaca oyunudur", "sevimli postacıları uzayda fırlattığın bir fizik bulmaca oyunudur"),
    ("un juego de puzles con dos modos, Deslizar y Empujar, protagonizado por criaturitas adorables", "un juego de puzles de física en el que lanzas carteros adorables por el espacio"),
    ("um jogo de quebra-cabeças com dois modos, Deslizar e Empurrar, estrelado por criaturinhas fofas", "um jogo de quebra-cabeças de física em que você lança carteiros fofos pelo espaço"),
    ("best moves, daily streak, Nudgeling outfit, settings, statistics and badges", "best shots, daily streak, courier accessories, settings, statistics and badges"),
    ("(counters, stars, best moves and daily records)", "(counters, stars, best shots and daily records)"),
    ("en iyi hamle sayıların, günlük serin, Nudgeling kıyafetin, ayarların, istatistiklerin ve rozetlerin", "en iyi atış sayıların, günlük serin, postacı aksesuarların, ayarların, istatistiklerin ve rozetlerin"),
    ("(sayaçlar, yıldızlar, en iyi hamle sayıları ve günlük kayıtlar)", "(sayaçlar, yıldızlar, en iyi atış sayıları ve günlük kayıtlar)"),
    ("tus mejores movimientos, tu racha diaria, el disfraz de tu Slinglings", "tus mejores tiros, tu racha diaria, los accesorios de tu cartero"),
    ("tus mejores movimientos, tu racha diaria, el disfraz de tu Nudgeling", "tus mejores tiros, tu racha diaria, los accesorios de tu cartero"),
    ("(contadores, estrellas, mejores movimientos y registros diarios)", "(contadores, estrellas, mejores tiros y registros diarios)"),
    ("seus melhores movimentos, sua sequência diária, a fantasia do seu Slinglings", "seus melhores tiros, sua sequência diária, os acessórios do seu carteiro"),
    ("seus melhores movimentos, sua sequência diária, a fantasia do seu Nudgeling", "seus melhores tiros, sua sequência diária, os acessórios do seu carteiro"),
    ("(contadores, estrelas, melhores movimentos e registros diários)", "(contadores, estrelas, melhores tiros e registros diários)"),
    ("with its level number, number of moves, stars earned", "with its level number, number of shots, stars earned"),
    ("(bölüm numarası, hamle sayısı, kazandığın yıldız", "(bölüm numarası, atış sayısı, kazandığın yıldız"),
    ("con su número de nivel, número de movimientos, estrellas ganadas", "con su número de nivel, número de tiros, estrellas ganadas"),
    ("com o número do nível, número de jogadas, estrelas ganhas", "com o número do nível, número de tiros, estrelas ganhas"),
    ("«puzzle iniciado» o «puzzle resuelto»", "«nivel iniciado» o «nivel resuelto»"),
    ("\"quebra-cabeça iniciado\" ou \"quebra-cabeça resolvido\"", "\"nível iniciado\" ou \"nível resolvido\""),
    ("\"bulmaca başladı\" ya da \"bulmaca çözüldü\"", "\"bölüm başladı\" ya da \"bölüm çözüldü\""),
]
out = src
for a, b in R:
    out = out.replace(a, b)
# Nudgelings -> Slinglings degisiminden sonra kalan "Slinglings outfit" kaliplari icin son kontrol
for bad in ("outfit", "kıyafet", "disfraz", "fantasia", "hamle", "movimientos", "jogadas", "Slide", "Kaydır"):
    if bad in out:
        print("UYARI: kalan Nudgelings ifadesi:", bad)

dst = os.path.join(G, "slinglings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"))
