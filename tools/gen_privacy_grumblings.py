# -*- coding: utf-8 -*-
"""Grumblings gizlilik sayfasini (grumblings/privacy.html) Tilelings'inkinden turetir: ayni hizmetler (AdMob, Firebase, Play Games, Billing),
Grumblings'e ozgu metinler ve renkler degistirilir. Calistir: py -3 tools/gen_privacy_grumblings.py"""
import io, os

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "tilelings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#0E2A20; --card:#17402F; --text:#F3F7F2; --dim:#CFE3D8; --accent:#E8D9A8; --link:#9ED0FF;",
     "--bg:#1E1A3C; --card:#2E2761; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFD84D; --link:#B7A4FF;"),
    ("Tilelings", "Grumblings"),
    ("Effective date: 4 November 2026", "Effective date: 7 November 2026"),
    ("Yürürlük tarihi: 4 Kasım 2026", "Yürürlük tarihi: 7 Kasım 2026"),
    ("Fecha de entrada en vigor: 4 de noviembre de 2026", "Fecha de entrada en vigor: 7 de noviembre de 2026"),
    ("Data de vigência: 4 de novembro de 2026", "Data de vigência: 7 de novembro de 2026"),
    # oyun tanimi
    ("is a Mahjong puzzle game with Solitaire, Connect and Tile Match modes", "is a turn-based maze puzzle game in which you escape from grumpy monsters"),
    ("Solitaire, Connect ve Taş Eşleştirme modları olan bir Mahjong bulmaca oyunudur", "huysuz canavarlardan kaçtığın sıra tabanlı bir labirent bulmaca oyunudur"),
    ("un juego de puzles de Mahjong con los modos Solitario, Connect y Tile Match", "un juego de puzles de laberinto por turnos en el que escapas de monstruos gruñones"),
    ("um jogo de quebra-cabeças de Mahjong com os modos Paciência, Connect e Tile Match", "um jogo de quebra-cabeças de labirinto por turnos em que você escapa de monstros rabugentos"),
    # yerel ilerleme
    ("Your puzzle progress, stars, best times, daily streak, the game you are currently playing, your chosen tile set and theme, settings and statistics",
     "Your level progress, stars, best moves, daily streak, hero outfit, settings, statistics and badges"),
    ("Bulmaca ilerlemen, yıldızların, en iyi sürelerin, günlük serin, şu an oynadığın oyun, seçtiğin taş takımı ve tema, ayarların ve istatistiklerin",
     "Bölüm ilerlemen, yıldızların, en iyi hamle sayıların, günlük serin, kahraman kıyafetin, ayarların, istatistiklerin ve rozetlerin"),
    ("Tu progreso en los puzles, tus estrellas, tus mejores tiempos, tu racha diaria, la partida en curso, el juego de fichas y el tema elegidos, tus ajustes y tus estadísticas",
     "Tu progreso en los niveles, tus estrellas, tus mejores movimientos, tu racha diaria, el atuendo de tu héroe, tus ajustes, tus estadísticas e insignias"),
    ("Seu progresso nos desafios, suas estrelas, seus melhores tempos, sua sequência diária, o jogo em andamento, o conjunto de peças e o tema escolhidos, suas configurações e suas estatísticas",
     "Seu progresso nos níveis, suas estrelas, seus melhores movimentos, sua sequência diária, a roupa do seu herói, suas configurações, suas estatísticas e conquistas"),
    ("(counters, stars, best times and daily records)", "(counters, stars, best moves and daily records)"),
    ("(sayaçlar, yıldızlar, en iyi süreler ve günlük kayıtlar)", "(sayaçlar, yıldızlar, en iyi hamle sayıları ve günlük kayıtlar)"),
    ("(contadores, estrellas, mejores tiempos y registros diarios)", "(contadores, estrellas, mejores movimientos y registros diarios)"),
    ("(contadores, estrelas, melhores tempos e registros diários)", "(contadores, estrelas, melhores movimentos e registros diários)"),
    # reklam siklik cumleleri
    ("an occasional ad between puzzles (never while you are solving a puzzle, and none in your first 3 puzzles)", "an occasional ad between levels (never while you are playing a level)"),
    ("bulmacalar arasında ara sıra bir reklam (bulmaca çözerken asla, ilk 3 bulmacada hiç)", "bölümler arasında ara sıra bir reklam (bölüm oynarken asla)"),
    ("un anuncio ocasional entre puzzles (nunca mientras resuelves y ninguno en tus 3 primeros puzzles)", "un anuncio ocasional entre niveles (nunca mientras juegas un nivel)"),
    ("um anúncio ocasional entre os quebra-cabeças (nunca enquanto você resolve e nenhum nos seus 3 primeiros)", "um anúncio ocasional entre os níveis (nunca enquanto você joga um nível)"),
    # Play Games puanlari
    ("(for example daily puzzle times, Time Attack scores and your total stars)", "(for example your total stars, perfect levels and daily streak)"),
    ("(örneğin günlük bulmaca sürelerin, Zamana Karşı puanların ve toplam yıldızların)", "(örneğin toplam yıldızların, mükemmel bölümlerin ve günlük serin)"),
    ("(por ejemplo los tiempos de los puzles diarios, tus puntos de Contrarreloj y tus estrellas totales)", "(por ejemplo tus estrellas totales, tus niveles perfectos y tu racha diaria)"),
    ("(por exemplo os tempos dos desafios diários, seus pontos de Contra o Tempo e suas estrelas totais)", "(por exemplo suas estrelas totais, seus níveis perfeitos e sua sequência diária)"),
    # analitik
    ("\"a puzzle started\" or \"a puzzle was solved\" with its mode, level, difficulty, time, number of moves and how many hints you used",
     "\"a level started\" or \"a level was solved\" with its level number, number of moves, stars earned and how many hints you used"),
    ("(mod, seviye, zorluk, süre, hamle sayısı ve kaç ipucu kullandığınla)", "(bölüm numarası, hamle sayısı, kazandığın yıldız ve kaç ipucu kullandığınla)"),
    ("con su modo, nivel, dificultad, tiempo, número de movimientos y cuántas pistas usaste", "con su número de nivel, número de movimientos, estrellas ganadas y cuántas pistas usaste"),
    ("com o modo, nível, dificuldade, tempo, número de jogadas e quantas dicas você usou", "com o número do nível, número de jogadas, estrelas ganhas e quantas dicas você usou"),
]
out = src
for a, b in R:
    if a not in out:
        print("UYARI: bulunamadi:", a[:80])
    out = out.replace(a, b)

dst = os.path.join(G, "grumblings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
icon = os.path.join(G, "..", "Grumblings", "market_assets", "icon-512.png")
if os.path.exists(icon):
    from PIL import Image
    Image.open(icon).convert("RGBA").resize((192, 192), Image.LANCZOS).save(os.path.join(dst, "icon.png"))
print("ok", os.path.join(dst, "privacy.html"))
