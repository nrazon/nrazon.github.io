# -*- coding: utf-8 -*-
"""Tilelings gizlilik sayfasını (tilelings/privacy.html) Logiclings'inkinden türetir: aynı hizmetler (AdMob, Firebase, Play Games, Billing),
Tilelings'e özgü metinler ve renkler değiştirilir. Çalıştır: py -3 tools/gen_privacy_tilelings.py"""
import io, os, shutil

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "logiclings", "privacy.html"), encoding="utf-8").read()

R = [
    # tema
    ("--bg:#17131F; --card:#241D33; --text:#F3EFFA; --dim:#CFC6E0; --accent:#E8B64C; --link:#B7A4FF;", "--bg:#0E2A20; --card:#17402F; --text:#F3F7F2; --dim:#CFE3D8; --accent:#E8D9A8; --link:#9ED0FF;"),
    ("Logiclings", "Tilelings"),
    # tarih
    ("Effective date: 1 November 2026", "Effective date: 4 November 2026"),
    ("Yürürlük tarihi: 1 Kasım 2026", "Yürürlük tarihi: 4 Kasım 2026"),
    ("Fecha de entrada en vigor: 1 de noviembre de 2026", "Fecha de entrada en vigor: 4 de noviembre de 2026"),
    ("Data de vigência: 1 de novembro de 2026", "Data de vigência: 4 de novembro de 2026"),
    # oyun tanımı
    ("is a daily logic puzzle game", "is a Mahjong puzzle game with Solitaire, Connect and Tile Match modes"),
    ("günlük bir mantık bulmacası oyunudur", "Solitaire, Connect ve Taş Eşleştirme modları olan bir Mahjong bulmaca oyunudur"),
    ("es un juego diario de puzzles de lógica", "es un juego de puzles de Mahjong con los modos Solitario, Connect y Tile Match"),
    ("é um jogo diário de quebra-cabeças de lógica", "é um jogo de quebra-cabeças de Mahjong com os modos Paciência, Connect e Tile Match"),
    # yerel ilerleme
    ("Your puzzle progress, records, best times, daily streak, the puzzle you are currently solving, settings and statistics",
     "Your puzzle progress, stars, best times, daily streak, the game you are currently playing, your chosen tile set and theme, settings and statistics"),
    ("Bulmaca ilerlemen, rekorların, en iyi sürelerin, günlük serin, şu an çözdüğün bulmaca, ayarların ve istatistiklerin",
     "Bulmaca ilerlemen, yıldızların, en iyi sürelerin, günlük serin, şu an oynadığın oyun, seçtiğin taş takımı ve tema, ayarların ve istatistiklerin"),
    ("Tu progreso en los puzzles, tus récords, tus mejores tiempos, tu racha diaria, el puzzle que estás resolviendo, tus ajustes y tus estadísticas",
     "Tu progreso en los puzles, tus estrellas, tus mejores tiempos, tu racha diaria, la partida en curso, el juego de fichas y el tema elegidos, tus ajustes y tus estadísticas"),
    ("Seu progresso nos quebra-cabeças, seus recordes, seus melhores tempos, sua sequência diária, o quebra-cabeça que você está resolvendo, suas configurações e suas estatísticas",
     "Seu progresso nos desafios, suas estrelas, seus melhores tempos, sua sequência diária, o jogo em andamento, o conjunto de peças e o tema escolhidos, suas configurações e suas estatísticas"),
    ("(counters, best times and daily records)", "(counters, stars, best times and daily records)"),
    ("(sayaçlar, en iyi süreler ve günlük kayıtlar)", "(sayaçlar, yıldızlar, en iyi süreler ve günlük kayıtlar)"),
    ("(contadores, mejores tiempos y registros diarios)", "(contadores, estrellas, mejores tiempos y registros diarios)"),
    ("(contadores, melhores tempos e registros diários)", "(contadores, estrelas, melhores tempos e registros diários)"),
    # Play Games puanları
    ("(for example puzzle times, your daily streak and the number of puzzles solved)", "(for example daily puzzle times, Time Attack scores and your total stars)"),
    ("(örneğin bulmaca sürelerin, günlük serin ve çözdüğün bulmaca sayısı)", "(örneğin günlük bulmaca sürelerin, Zamana Karşı puanların ve toplam yıldızların)"),
    ("(por ejemplo los tiempos de los puzzles, tu racha diaria y el número de puzzles resueltos)", "(por ejemplo los tiempos de los puzles diarios, tus puntos de Contrarreloj y tus estrellas totales)"),
    ("(por exemplo os tempos dos quebra-cabeças, sua sequência diária e o número de quebra-cabeças resolvidos)", "(por exemplo os tempos dos desafios diários, seus pontos de Contra o Tempo e suas estrelas totais)"),
    # analitik
    ("such as \"a puzzle started\" or \"a puzzle was solved\" with its type, size, difficulty, time and how many hints you used",
     "such as \"a puzzle started\" or \"a puzzle was solved\" with its mode, level, difficulty, time, number of moves and how many hints you used"),
    ("(tür, boyut, zorluk, süre ve kaç ipucu kullandığınla)", "(mod, seviye, zorluk, süre, hamle sayısı ve kaç ipucu kullandığınla)"),
    ("con su tipo, tamaño, dificultad, tiempo y cuántas pistas usaste", "con su modo, nivel, dificultad, tiempo, número de movimientos y cuántas pistas usaste"),
    ("com o tipo, tamanho, dificuldade, tempo e quantas dicas você usou", "com o modo, nível, dificuldade, tempo, número de jogadas e quantas dicas você usou"),
]
out = src
for a, b in R:
    if a not in out:
        print("UYARI: bulunamadi:", a[:70])
    out = out.replace(a, b)

dst = os.path.join(G, "tilelings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
icon = os.path.join(G, "..", "Tilelings", "market_assets", "icon-512.png")
if os.path.exists(icon):
    from PIL import Image
    Image.open(icon).convert("RGBA").resize((192, 192), Image.LANCZOS).save(os.path.join(dst, "icon.png"))
print("tamam:", os.path.join(dst, "privacy.html"))
