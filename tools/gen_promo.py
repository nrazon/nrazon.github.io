# "Diger oyunlarim" uzaktan listesi: github-pages/promo/v1/games.json + icons/<anahtar>.png (192px).
# Oyunlar bu dosyayi 48 saatte bir cekip onbellekler; APK icinde yedek kopya (assets/promo_fallback.json) vardir.
# Yeni oyun = GAMES'in basina satir + `py -3 -X utf8 tools/gen_promo.py` + commit/push. Oyunlara surum GEREKMEZ.
# Cardles'in strings.xml'inden mevcut metinler okunur; yenisi/degisen metin DESC_OVERRIDE'a yazilir.
import io, json, os, re, sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(HERE)
ROOT = os.path.dirname(SITE)

# (anahtar, ad, paket, klasor)   en yeni en ustte
GAMES = [
    ('pentolings', 'Pentolings', 'com.pentolings.nesimapps', 'Pentolings'),
    ('nudgelings', 'Nudgelings', 'com.nudgelings.nesimapps', 'Nudgelings'),
    ('grumblings', 'Grumblings', 'com.grumblings.nesimapps', 'Grumblings'),
    ('tilelings', 'Tilelings', 'com.tilelings.nesimapps', 'Tilelings'),
    ('logiclings', 'Logiclings', 'com.logiclings.nesimapps', 'Logiclings'),
    ('beamies', 'Beamies', 'com.beamies.nesimapps', 'Beamies'),
    ('cardles', 'Cardles', 'com.cardles.nesimapps', 'Cardles'),
    ('cubbles', 'Cubbles', 'com.cubbles.nesimapps', 'Cubbles'),
    ('sliplines', 'Sliplines', 'com.sliplines.nesimapps', 'OkKacisi'),
    ('2048', '2048', 'com.game2048.nesimapps', 'Game2048'),
    ('tictactoe', 'Tic-Tac-Toe', 'com.tictactoe.nesimapps', 'TicTacToe'),
]
DESC_OVERRIDE = {  # tr, en, es, pt
    'pentolings': ('Parçaları şekle döşe, renkleri patlat: tek uygulamada iki sevimli bulmaca. 150 bölüm.',
                   'Fit the pieces, pop the colours: two cute puzzle games in one. 150 levels.',
                   'Encaja las piezas, explota los colores: dos puzles adorables en uno. 150 niveles.',
                   'Encaixe as peças, estoure as cores: dois quebra-cabeças fofos em um. 150 níveis.'),
    'nudgelings': ('Araçları kaydır, kristalleri it: tek uygulamada iki sevimli bulmaca. 400 bölüm.',
                   'Slide the pods, push the crystals: two cute puzzle games in one. 400 levels.',
                   'Desliza las cápsulas, empuja los cristales: dos puzles adorables en uno. 400 niveles.',
                   'Deslize as cápsulas, empurre os cristais: dois quebra-cabeças fofos em um. 400 níveis.'),
    'logiclings': ('Her gün yeni mantık bulmacaları: Taç, İkiz, Yol, Uykucu Yüzler ve Kurbağa Zıplatma.',
                   'New logic puzzles every day: Crown, Twin, Path, Sleepy Faces and Frog Hops.',
                   'Puzles de lógica nuevos cada día: Corona, Gemelos, Camino, Caras Dormilonas y Saltos de Ranas.',
                   'Novos quebra-cabeças de lógica todo dia: Coroa, Gêmeos, Caminho, Rostos Sonolentos e Pulos de Sapos.'),
    'cardles': ('Solitaire koleksiyonu: Klondike, Spider, FreeCell, TriPeaks. Günlük meydan okuma.',
                'Solitaire collection: Klondike, Spider, FreeCell, TriPeaks. New daily challenge.',
                'Colección de solitarios: Klondike, Spider, FreeCell, TriPeaks. Reto diario.',
                'Coleção de paciências: Klondike, Spider, FreeCell, TriPeaks. Desafio diário.'),
}
RES = os.path.join(ROOT, 'Cardles', 'app', 'src', 'main', 'res')


def res_text(d, key):
    s = io.open(os.path.join(RES, d, 'strings.xml'), encoding='utf-8').read()
    m = re.search(r'<string name="promo_%s">(.*?)</string>' % re.escape(key), s, re.S)
    return m.group(1).replace("\'", "'").replace('\\"', '"').strip()


def icon_src(key, folder):
    for p in (os.path.join(ROOT, folder, 'market_assets', 'icon-512.png'),
              os.path.join(ROOT, 'Cardles', 'app', 'src', 'main', 'res', 'drawable-nodpi', f'promo_{key}.png')):
        if os.path.exists(p):
            return p
    sys.exit('ikon yok: ' + key)


out = []
os.makedirs(os.path.join(SITE, 'promo', 'v1', 'icons'), exist_ok=True)
for key, name, pkg, folder in GAMES:
    if key in DESC_OVERRIDE:
        tr, en, es, pt = DESC_OVERRIDE[key]
    else:
        tr, en, es, pt = (res_text(d, key) for d in ('values-tr', 'values', 'values-es', 'values-pt'))
    for t in (tr, en, es, pt):
        assert 10 < len(t) < 140, (key, t)
    Image.open(icon_src(key, folder)).convert('RGBA').resize((192, 192), Image.LANCZOS).save(
        os.path.join(SITE, 'promo', 'v1', 'icons', f'{key}.png'), optimize=True)
    out.append({'key': key, 'name': name, 'pkg': pkg, 'icon': f'icons/{key}.png', 'tr': tr, 'en': en, 'es': es, 'pt': pt})
data = json.dumps({'v': 1, 'games': out}, ensure_ascii=False, indent=1) + '\n'
io.open(os.path.join(SITE, 'promo', 'v1', 'games.json'), 'w', encoding='utf-8', newline='\n').write(data)
print(len(out), 'oyun yazildi')
