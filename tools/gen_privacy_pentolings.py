# -*- coding: utf-8 -*-
"""Pentolings gizlilik sayfasini (pentolings/privacy.html) Grumblings'inkinden turetir: ayni hizmetler (AdMob+UMP, Firebase Analytics/Crashlytics,
Play Games + Saved Games, Billing), Pentolings'e ozgu isim, renk ve oyun tanimi; ayrica "Diger oyunlarim" listesinin
nrazon.github.io'dan indirildigi notu. Calistir: py -3 -X utf8 tools/gen_privacy_pentolings.py"""
import io, os

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "grumblings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#1E1A3C; --card:#2E2761; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFD84D; --link:#B7A4FF;",
     "--bg:#1B1838; --card:#2A2350; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFC857; --link:#B7A4FF;"),
    ("Grumblings", "Pentolings"),
    ("Effective date: 7 November 2026", "Effective date: 9 November 2026"),
    ("Yürürlük tarihi: 7 Kasım 2026", "Yürürlük tarihi: 9 Kasım 2026"),
    ("Fecha de entrada en vigor: 7 de noviembre de 2026", "Fecha de entrada en vigor: 9 de noviembre de 2026"),
    ("Data de vigência: 7 de novembro de 2026", "Data de vigência: 9 de novembro de 2026"),
    # oyun tanimi
    ("is a turn-based maze puzzle game in which you escape from grumpy monsters", "is a puzzle app with two cute games, Fit (fill shapes with pentomino pieces) and Drop (falling pieces and colour pops)"),
    ("huysuz canavarlardan kaçtığın sıra tabanlı bir labirent bulmaca oyunudur", "iki sevimli oyunu olan bir bulmaca uygulamasıdır: Döşe (pentomino parçalarıyla şekil doldurma) ve Düşür (düşen parçalar ve renk patlatma)"),
    ("un juego de puzles de laberinto por turnos en el que escapas de monstruos gruñones", "una aplicación de puzles con dos juegos adorables, Encajar (rellenar formas con piezas pentominó) y Caída (piezas que caen y colores que explotan)"),
    ("um jogo de quebra-cabeças de labirinto por turnos em que você escapa de monstros rabugentos", "um aplicativo de quebra-cabeças com dois jogos fofos, Encaixar (preencher formas com peças de pentaminó) e Queda (peças que caem e cores que estouram)"),
    # saklanan veriler
    ("stars, best moves, daily streak, hero outfit, settings", "stars, best times, high scores, daily streak, settings"),
    ("yıldızların, en iyi hamle sayıların, günlük serin, kahraman kıyafetin, ayarların", "yıldızların, en iyi sürelerin, rekor puanların, günlük serin, ayarların"),
    ("tus estrellas, tus mejores movimientos, tu racha diaria, el atuendo de tu héroe, tus ajustes", "tus estrellas, tus mejores tiempos, tus récords, tu racha diaria, tus ajustes"),
    ("suas estrelas, seus melhores movimentos, sua sequência diária, a roupa do seu herói, suas configurações", "suas estrelas, seus melhores tempos, seus recordes, sua sequência diária, suas configurações"),
    ("stars, best moves and daily records", "stars, best times, high scores and daily records"),
    ("yıldızlar, en iyi hamle sayıları ve günlük kayıtlar", "yıldızlar, en iyi süreler, rekor puanlar ve günlük kayıtlar"),
    ("estrellas, mejores movimientos y registros diarios", "estrellas, mejores tiempos, récords y registros diarios"),
    ("estrelas, melhores movimentos e registros diários", "estrelas, melhores tempos, recordes e registros diários"),
    # kendi sunucusu yok + Diger oyunlarim listesi
    ("I do not operate servers for the game.</p>",
     "I do not operate servers for the game. The only thing the game downloads from my website (nrazon.github.io) is the small public list shown in \"More games\" (names, icons and short descriptions of my other games); it contains no personal data and nothing about you is sent besides what any web request includes, such as your IP address.</p>"),
    ("oyun için sunucu kullanmıyorum.</p>",
     "oyun için sunucu kullanmıyorum. Oyunun web sitemden (nrazon.github.io) indirdiği tek şey, \"Diğer oyunlarım\" bölümünde görünen küçük herkese açık listedir (diğer oyunlarımın adları, simgeleri ve kısa açıklamaları); kişisel veri içermez ve herhangi bir web isteğinin içerdiği bilgiler (örneğin IP adresi) dışında hakkında hiçbir şey gönderilmez.</p>"),
    ("no utilizo servidores para el juego.</p>",
     "no utilizo servidores para el juego. Lo único que el juego descarga de mi sitio web (nrazon.github.io) es la pequeña lista pública de «Más juegos» (nombres, iconos y descripciones breves de mis otros juegos); no contiene datos personales y no se envía nada sobre ti aparte de lo que incluye cualquier petición web, como tu dirección IP.</p>"),
    ("não uso servidores para o jogo.</p>",
     "não uso servidores para o jogo. A única coisa que o jogo baixa do meu site (nrazon.github.io) é a pequena lista pública de \"Mais jogos\" (nomes, ícones e descrições curtas dos meus outros jogos); ela não contém dados pessoais e nada sobre você é enviado além do que qualquer requisição web inclui, como seu endereço IP.</p>"),
]
out = src
for a, b in R:
    if a not in out:
        print("UYARI: bulunamadi:", a[:80])
    out = out.replace(a, b)
for bad in ("hero", "kahraman", "héroe", "herói", "labirent", "maze", "monster"):
    if bad in out:
        print("UYARI: kalinti:", bad)

dst = os.path.join(G, "pentolings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"))
