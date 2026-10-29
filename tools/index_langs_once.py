# Tek seferlik: ana sayfaya es/pt metinleri ekler (en öğesinin kopyası + çeviri). Zaten uygulandı; yeni karta elle es/pt ekle.
import re
P = "index.html"
s = open(P, encoding="utf-8").read()
T = [  # (en metninin başlangıcı, es, pt)
    ("Android apps and games", "Aplicaciones y juegos de Android de Nesim Razon", "Aplicativos e jogos Android de Nesim Razon"),
    ("Solitaire that makes", "El solitario que te hace sonreír", "Paciência que faz você sorrir"),
    ("NEW GAME", "JUEGO NUEVO", "JOGO NOVO"),
    ("Four classic solitaire", "Cuatro solitarios clásicos en una sola app, con cartas de caritas adorables: Klondike, Spider, FreeCell y TriPeaks. Reto diario, rachas, pistas y temas.", "Quatro paciências clássicas em um só app, com cartas de carinhas fofas: Klondike, Spider, FreeCell e TriPeaks. Desafio diário, sequências, dicas e temas."),
    ("<b>Learn more</b>", "<b>Más información</b>", "<b>Saiba mais</b>"),
    ("Privacy Policy", "Política de privacidad", "Política de privacidade"),
    ("POPULAR", "POPULAR", "POPULAR"),
    ("Results of the Turkish", "Resultados de las loterías turcas (Sayısal Loto, Süper Loto, Şans Topu, On Numara, Milli Piyango), boletos aleatorios y comprobación de boletos.", "Resultados das loterias turcas (Sayısal Loto, Süper Loto, Şans Topu, On Numara, Milli Piyango), bilhetes aleatórios e conferência de bilhetes."),
    ("All", "Todo", "Tudo"), ("Games", "Juegos", "Jogos"), ("Apps", "Apps", "Apps"),
    ("NEW", "NUEVO", "NOVO"),
    ("A block puzzle", "Un puzle de bloques con caritas adorables: arrastra bloques al tablero, completa filas y columnas para limpiarlas y encadena combos. Reto diario, misiones y temas.", "Um quebra-cabeça de blocos com carinhas fofas: arraste blocos para o tabuleiro, complete linhas e colunas para limpá-las e encadeie combos. Desafio diário, missões e temas."),
    ("An arrow puzzle", "Un puzle de flechas: saca las flechas en el orden correcto y despeja el tablero. Cientos de niveles, un Reto diario con clasificación mundial e insignias para coleccionar.", "Um quebra-cabeça de setas: tire as setas na ordem certa e limpe o tabuleiro. Centenas de níveis, um Desafio diário com classificação mundial e emblemas para colecionar."),
    ("The classic number", "El clásico puzle de números: desliza, combina números iguales y llega a la ficha 2048.", "O clássico quebra-cabeça de números: deslize, combine números iguais e chegue à peça 2048."),
    ("Classic Tic-Tac-Toe", "El clásico tres en raya contra el ordenador: Fácil, Medio o Difícil. En Difícil nunca pierde.", "O clássico jogo da velha contra o computador: Fácil, Médio ou Difícil. No Difícil ele nunca perde."),
    ("Where Am I?", "¿Dónde estoy?", "Onde estou?"),
    ("See where you are", "Mira dónde estás en el mapa con tu dirección y coordenadas; cópialas o compártelas.", "Veja onde você está no mapa com seu endereço e coordenadas; copie ou compartilhe."),
    ("Age Calculator", "Calculadora de edad", "Calculadora de idade"),
    ("Calculate exact age", "Calcula tu edad exacta y el tiempo entre fechas, y guarda una lista de cumpleaños y aniversarios.", "Calcule sua idade exata e o tempo entre datas, e mantenha uma lista de aniversários e datas especiais."),
    ("Recent earthquakes", "Terremotos recientes en Turquía y alrededores según AFAD y Kandilli, con mapa y estadísticas.", "Terremotos recentes na Turquia e arredores segundo AFAD e Kandilli, com mapa e estatísticas."),
    ("BMI Calculator", "Calculadora de IMC", "Calculadora de IMC"),
    ("Calculate your BMI", "Calcula tu IMC con las categorías de la OMS y consulta el rango de peso saludable para tu estatura.", "Calcule seu IMC com as categorias da OMS e veja a faixa de peso saudável para sua altura."),
    ("O Canada, the national", "O Canada, el himno nacional de Canadá, con una bandera ondeante; suena en segundo plano y en Chromecast.", "O Canada, o hino nacional do Canadá, com uma bandeira ondulante; toca em segundo plano e no Chromecast."),
    ("Sailing and sea", "Noticias de vela y mar, resultados de regatas y artículos de turksail.com (en turco).", "Notícias de vela e mar, resultados de regatas e artigos de turksail.com (em turco)."),
    ("Media relations", "Relaciones con los medios, comunicación de crisis y formación en oratoria de medyafobi.com (en turco).", "Relações com a mídia, comunicação de crise e treinamentos de oratória de medyafobi.com (em turco)."),
    ("Contact", "Contacto", "Contato"),
]
TURKEY = ("es", "pt")


def tr(text):
    t = text.strip()
    for pre, es, pt in T:
        if (t == pre) if len(pre) <= 12 and not pre.startswith("<") else t.startswith(pre):
            return es, pt
    if t.endswith("the national anthem of Türkiye, with a waving flag; plays in the background and on Chromecast."):
        return ("İstiklal Marşı, el himno nacional de Türkiye, con una bandera ondeante; suena en segundo plano y en Chromecast.",
                "İstiklal Marşı, o hino nacional da Türkiye, com uma bandeira ondulante; toca em segundo plano e no Chromecast.")
    return None


def sub(m):
    el = m.group(0)
    inner = m.group(2) if (m.lastindex or 0) >= 2 else None
    out = el
    for i, l in enumerate(("es", "pt")):
        c = el.replace('lang="en"', f'lang="{l}"', 1)
        if inner is not None:
            r = tr(inner)
            assert r, inner
            c = c.replace(inner, r[i], 1)
        out += c
    return out


s = re.sub(r'<img lang="en"[^>]*>', sub, s)
s = re.sub(r'<(p|span|a|h2)\b[^>]*\blang="en"[^>]*>(.*?)</\1>', sub, s, flags=re.S)
s = s.replace('  html.tr [lang="en"], html.en [lang="tr"] { display:none; }',
              '  html.tr [lang]:not([lang="tr"]):not(html), html.en [lang]:not([lang="en"]):not(html), html.es [lang]:not([lang="es"]):not(html), html.pt [lang]:not([lang="pt"]):not(html) { display:none; }')
s = s.replace('''    if (lang !== "tr" && lang !== "en") lang = (navigator.language || "").toLowerCase().indexOf("tr") === 0 ? "tr" : "en";''',
              '''    if (["tr", "en", "es", "pt"].indexOf(lang) < 0) { var n = (navigator.language || "en").toLowerCase().slice(0, 2); lang = ["tr", "es", "pt"].indexOf(n) >= 0 ? n : "en"; }''')
s = s.replace('''      <button type="button" data-lang="en" onclick="setLang('en')">EN</button>''',
              '''      <button type="button" data-lang="en" onclick="setLang('en')">EN</button>
      <button type="button" data-lang="es" onclick="setLang('es')">ES</button>
      <button type="button" data-lang="pt" onclick="setLang('pt')">PT</button>''')
open(P, "w", encoding="utf-8", newline="\n").write(s)
print("ok")
