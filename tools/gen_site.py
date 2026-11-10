# github-pages üretici betiği: oyun/uygulama detay sayfalarını (<slug>/index.html), landing.css, eyes.js, sitemap.xml ve robots.txt'yi üretir.
# Kullanım: py -3 tools/gen_site.py   (github-pages kökünden). Kaynaklar: ../<Uygulama>/market_assets/listing.md + screenshots.
# Yeni uygulama: APPDEFS'e satır ekle (ana sayfada kartı da olmalı; "Daha fazla" bağlantısını betik ekler). Cardles/Cubbles içeriği aşağıda elle yazılı.
# Ekran görüntüsü küçükleri <slug>/shots/ altına Chrome ile üretilir (yoksa); tools/thumbs_manifest.json boyutları tutar (commit edilir).
import glob
import os
import re
import json

G = r"C:\@Development\PersonalAndroidApps\github-pages"
BASE = "https://nrazon.github.io"
# Yayına henüz çıkmamış uygulamaların detay sayfaları: URL'den açılır ama ana sayfa kartı, "Diğer uygulamalarım" listeleri ve sitemap'e GİRMEZ,
# sayfada noindex var. Uygulama Play'de yayınlanınca slug buradan silinir (ve home_data.json'da status=live yapılır).
HIDDEN = {"tombalings"}  # yayinda olmayan uygulama onceden buraya eklenir, yayin gunu silinir
# Ana sayfada kartında data-pkg olmayan (henüz "yakında" kartı olan) uygulamaların paket adları.
VIDEOS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "videos.json"), encoding="utf-8"))
VIDEO_LABEL = {"tr": "Tanıtım videosu", "en": "Promo video", "es": "Vídeo de presentación", "pt": "Vídeo de apresentação"}
VIDEO_PLAY = {"tr": "Tanıtım videosunu oynat", "en": "Play promo video", "es": "Reproducir el vídeo", "pt": "Reproduzir o vídeo"}
PKG_FALLBACK = {"calisan": "com.calisanasistani.nesimapps", "uzaygunlugu": "com.uzaygunlugu.nesimapps", "haftasonum": "com.haftasonum.nesimapps", "beamies": "com.beamies.nesimapps", "logiclings": "com.logiclings.nesimapps", "grumblings": "com.grumblings.nesimapps", "nudgelings": "com.nudgelings.nesimapps", "pentolings": "com.pentolings.nesimapps", "tombalings": "com.tombalings.nesimapps", "astrolings": "com.astrolings.nesimapps", "nuzzlings": "com.nuzzlingscat.nesimapps"}
REF = "&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dweb"

# ------------------------------------------------------------------ ortak: göz takip betiği
EYES_JS = r'''/* Sevimli kartlar: gözler imleci (ya da parmağı) izler; imleç yokken ara sıra etrafa bakar. Hareketsizlik tercihinde durur. */
(function () {
  var reduce = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (reduce) return;
  var groups = [].slice.call(document.querySelectorAll("[data-eyes]"));
  if (!groups.length) return;
  var idleTimer = null;
  function look(x, y) {
    groups.forEach(function (g) {
      var r = g.getBoundingClientRect();
      if (!r.width) return;
      var cx = r.left + r.width / 2, cy = r.top + r.height / 2;
      var dx = x - cx, dy = y - cy, d = Math.hypot(dx, dy) || 1, k = Math.min(1, d / 260);
      var mx = (dx / d) * k * 0.034, my = (dy / d) * k * 0.034;
      [].forEach.call(g.querySelectorAll(".pupil"), function (p) { p.setAttribute("transform", "translate(" + mx.toFixed(4) + " " + my.toFixed(4) + ")"); });
    });
  }
  function wander() {
    var w = window.innerWidth, h = window.innerHeight;
    look(Math.random() * w, Math.random() * h * 0.6);
  }
  function pointer(e) {
    var t = e.touches ? e.touches[0] : e;
    look(t.clientX, t.clientY);
    clearInterval(idleTimer);
    idleTimer = setInterval(wander, 3200);
  }
  window.addEventListener("pointermove", pointer, { passive: true });
  window.addEventListener("touchmove", pointer, { passive: true });
  idleTimer = setInterval(wander, 3200);
  wander();
})();
'''

# ------------------------------------------------------------------ ortak CSS (landing sayfaları)
LANDING_CSS = r'''/* Oyun tanıtım sayfaları. Koyu varsayılan, açık tema sistem tercihine göre. Her sayfa --accent ve --hero-a/--hero-b verir. */
:root { --bg:#141829; --card:#1E2440; --text:#F3F4FA; --dim:#A9B0CF; --link:#7FB2FF; --chip:#252C4D; --line:#2C345A; --shadow:0 8px 24px rgba(0,0,0,.30); }
@media (prefers-color-scheme: light) {
  :root { --bg:#F4F5FB; --card:#FFFFFF; --text:#171A2B; --dim:#5B6280; --link:#2F5BD8; --chip:#E6E9F5; --line:#DCE0F0; --shadow:0 8px 22px rgba(30,40,90,.12); }
}
* { box-sizing:border-box; }
html { scroll-behavior:smooth; }
body { margin:0; background:var(--bg); color:var(--text); font:16px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
main { max-width:1040px; margin:0 auto; padding:28px 16px 64px; }
a { color:var(--link); }
a:focus-visible, button:focus-visible, summary:focus-visible { outline:3px solid var(--accent); outline-offset:3px; }
.top { display:flex; justify-content:space-between; align-items:center; gap:12px; margin-bottom:22px; }
.back { text-decoration:none; font-weight:700; color:var(--dim); }
.back:hover { color:var(--text); }
.lang { display:flex; gap:2px; background:var(--card); border-radius:999px; padding:4px; box-shadow:var(--shadow); }
.lang button { border:0; background:none; color:var(--dim); font:inherit; font-weight:700; font-size:13px; padding:5px 11px; border-radius:999px; cursor:pointer; }
.lang button[aria-pressed="true"] { background:var(--text); color:var(--bg); }
.lang a { color:var(--dim); font-weight:700; font-size:13px; padding:5px 11px; border-radius:999px; text-decoration:none; }
.lang a[aria-current] { background:var(--text); color:var(--bg); }
/* Hero */
.lhero { display:grid; grid-template-columns:minmax(0,1fr); background:linear-gradient(135deg,var(--hero-a),var(--hero-b)); color:#fff; border-radius:26px; overflow:hidden; box-shadow:var(--shadow); }
.lhero .copy { padding:30px 26px 8px; display:flex; flex-direction:column; align-items:flex-start; gap:12px; }
.lhero .art { padding:8px 12px 22px; display:flex; justify-content:center; }
.lhero .art svg { width:100%; max-width:480px; height:auto; overflow:visible; }
.tag { display:inline-block; background:#FFD166; color:#3A2A00; font-size:12px; font-weight:800; letter-spacing:.07em; padding:3px 11px; border-radius:999px; }
h1 { font-size:clamp(44px,9vw,72px); line-height:1; margin:0; letter-spacing:-.02em; font-weight:900; }
.tagline { font-size:clamp(18px,3.4vw,24px); font-weight:650; margin:0; color:rgba(255,255,255,.92); }
.intro { margin:0; max-width:46ch; color:rgba(255,255,255,.86); }
.chips { display:flex; flex-wrap:wrap; gap:6px; margin:2px 0 0; padding:0; list-style:none; }
.chips li { background:rgba(255,255,255,.16); font-size:13px; font-weight:700; padding:3px 11px; border-radius:999px; }
.cta { display:flex; flex-wrap:wrap; gap:10px 16px; align-items:center; margin-top:8px; }
.cta .play img { height:48px; width:auto; display:block; }
.cta a.small { color:#fff; font-size:14px; opacity:.9; }
@media (min-width:820px) {
  .lhero { grid-template-columns:minmax(0,1.05fr) minmax(0,1fr); align-items:center; }
  .lhero .copy { padding:44px 14px 44px 44px; }
  .lhero .art { padding:24px 34px 24px 0; }
}
/* Bölümler */
section.block { margin-top:46px; }
h2.h { font-size:13px; font-weight:800; letter-spacing:.09em; text-transform:uppercase; color:var(--dim); margin:0 0 16px; }
/* Ekran görüntüleri */
.strip { display:flex; gap:16px; overflow-x:auto; scroll-snap-type:x proximity; padding:6px 4px 18px; margin:0 -4px; }
.strip figure { margin:0; flex:none; scroll-snap-align:start; }
.phone { width:200px; border-radius:26px; border:5px solid #0b0d18; background:#0b0d18; box-shadow:var(--shadow); overflow:hidden; }
.phone img { display:block; width:100%; height:auto; }
@media (min-width:700px) { .phone { width:224px; } }
/* Özellikler */
.fgrid { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,300px),1fr)); gap:14px; }
.feat { background:var(--card); border-radius:18px; padding:18px 20px; box-shadow:var(--shadow); display:grid; grid-template-columns:44px minmax(0,1fr); gap:4px 14px; align-items:start; }
.feat svg { width:44px; height:44px; grid-row:1 / span 2; }
.feat h3 { margin:0; font-size:17px; line-height:1.3; }
.feat p { margin:0; color:var(--dim); font-size:15px; line-height:1.55; }
/* SSS */
.faq details { background:var(--card); border-radius:14px; padding:2px 18px; margin-bottom:10px; box-shadow:var(--shadow); }
.faq summary { cursor:pointer; font-weight:700; padding:14px 0; }
.faq details p { margin:0 0 14px; color:var(--dim); }
/* Diğer oyunlar */
.more { display:flex; flex-wrap:wrap; gap:10px; }
.more a { display:flex; align-items:center; gap:10px; background:var(--card); color:var(--text); text-decoration:none; font-weight:700; padding:8px 16px 8px 8px; border-radius:16px; box-shadow:var(--shadow); }
.more img { width:40px; height:40px; border-radius:10px; }
footer { color:var(--dim); font-size:14px; margin-top:44px; }
/* Dil: data-l="tr|en|es|pt" olan her şey yalnız seçili dilde görünür. */
html[data-lang="tr"] [data-l]:not([data-l="tr"]), html[data-lang="en"] [data-l]:not([data-l="en"]),
html[data-lang="es"] [data-l]:not([data-l="es"]), html[data-lang="pt"] [data-l]:not([data-l="pt"]),
html[data-lang="fr"] [data-l]:not([data-l="fr"]) { display:none; }
/* Kart yüzleri */
.pcard { transition:transform .25s cubic-bezier(.3,1.6,.5,1); transform-box:fill-box; transform-origin:center; }
.pcard:hover { transform:translateY(-10px); }
.eye { transform-box:fill-box; transform-origin:center; animation:blink 6s infinite; animation-delay:var(--d,0s); }
@keyframes blink { 0%,93%,100% { transform:scaleY(1); } 96% { transform:scaleY(.08); } }
@media (prefers-reduced-motion: reduce) { .eye { animation:none; } .pcard { transition:none; } html { scroll-behavior:auto; } }

/* QR ile yükle: yalnız fare olan geniş ekranlarda (masaüstü); telefonda Play rozeti yeterli */
.qr { display:none; position:relative; z-index:2; }
@media (hover:hover) and (pointer:fine) and (min-width:900px) { .qr { display:inline-block; } }
.qr summary { list-style:none; cursor:pointer; display:inline-flex; align-items:center; gap:6px; font-size:13px; font-weight:700; padding:6px 12px; border-radius:999px; border:1.5px solid color-mix(in srgb, currentColor 35%, transparent); color:inherit; user-select:none; }
.qr summary::-webkit-details-marker { display:none; }
.qr summary svg { width:14px; height:14px; flex:none; }
.qr summary:hover, .qr[open] summary { background:color-mix(in srgb, currentColor 14%, transparent); }
.qrpop { position:absolute; left:0; bottom:calc(100% + 10px); z-index:30; width:211px; padding:14px 14px 10px; background:#fff; color:#171A2B; border-radius:16px; box-shadow:0 10px 32px rgba(0,0,0,.4); text-align:center; }
.qrpop img { display:block; width:183px; height:183px; margin:0 auto 6px; }
.qrpop p { margin:0; font-size:13px; font-weight:700; line-height:1.3; }
.demo-wrap { background:var(--card); border-radius:22px; padding:22px; box-shadow:var(--shadow); }
.demo-open { display:inline-flex; align-items:center; gap:10px; font:inherit; font-weight:800; font-size:16px; padding:13px 22px; border:2px solid var(--accent); border-radius:999px; background:var(--card); color:var(--accent); cursor:pointer; }
.demo-open:hover, .demo-open[aria-expanded=true] { background:var(--accent); color:#fff; }
.demo-open + .demo-wrap { margin-top:16px; }
'''

# ------------------------------------------------------------------ SVG parçaları
SPADE = "M.5,.03 C.56,.28 1,.4 1,.65 C1,.9 .62,.92 .52,.72 L.62,.98 L.38,.98 L.48,.72 C.38,.92 0,.9 0,.65 C0,.4 .44,.28 .5,.03 Z"
HEART = "M.5,.28 C.5,.08 0,.04 0,.36 C0,.62 .4,.78 .5,.97 C.6,.78 1,.62 1,.36 C1,.04 .5,.08 .5,.28 Z"
DIAMOND = "M.5,0 Q.56,.4 .96,.5 Q.56,.6 .5,1 Q.44,.6 .04,.5 Q.44,.4 .5,0 Z"


def circ(cx, cy, r):
    return f"M{cx - r},{cy} a{r},{r} 0 1 0 {2 * r},0 a{r},{r} 0 1 0 {-2 * r},0 Z"


CLUB = circ(.5, .27, .24) + " " + circ(.26, .58, .24) + " " + circ(.74, .58, .24) + " M.5,.5 L.62,.98 L.38,.98 Z"
SUIT = {"S": SPADE, "H": HEART, "D": DIAMOND, "C": CLUB}
COLOR = {"S": "#16161C", "H": "#E0192F", "D": "#E0192F", "C": "#16161C"}
CROWN = "M.25,0 L.2,-.3 L.38,-.16 L.5,-.34 L.62,-.16 L.8,-.3 L.75,0 Z"
HAT = "M.34,0 L.5,-.38 L.66,0 Z"


def face(ey, delay, white="#fff", mood="smile"):
    return (
        f'<g class="eye" style="--d:{delay}s"><path d="{circ(.36, ey, .085)}" fill="{white}"/><path class="pupil" d="{circ(.37, ey + .01, .045)}" fill="#1B1B2B"/></g>'
        f'<g class="eye" style="--d:{delay}s"><path d="{circ(.64, ey, .085)}" fill="{white}"/><path class="pupil" d="{circ(.65, ey + .01, .045)}" fill="#1B1B2B"/></g>'
        f'<path d="M.4,{ey + .15} Q.5,{ey + .26} .6,{ey + .15}" fill="none" stroke="{white}" stroke-width=".04" stroke-linecap="round"/>'
    )


def card(x, y, rot, scale, rank, suit, acc=None, delay=0.0):
    w, h = 190, 270
    c = COLOR[suit]
    ey = .58 if suit == "C" else .5
    acc_svg = ""
    if acc == "crown":
        acc_svg = f'<path d="{CROWN}" fill="#FFC83D"/><path d="{CROWN}" fill="none" stroke="#000" stroke-opacity=".3" stroke-width=".02"/><circle cx=".5" cy="-.06" r=".04" fill="#fff"/>'
    elif acc == "hat":
        acc_svg = f'<path d="{HAT}" fill="#4DA3FF"/><path d="{HAT}" fill="none" stroke="#000" stroke-opacity=".3" stroke-width=".02"/><circle cx=".5" cy="-.38" r=".055" fill="#FFE066"/>'
    size = 112
    return f'''<g transform="translate({x} {y}) scale({scale}) rotate({rot} {w / 2} {h / 2})"><g class="pcard" data-eyes>
  <rect x="5" y="9" width="{w}" height="{h}" rx="20" fill="#000" opacity=".25"/>
  <rect width="{w}" height="{h}" rx="20" fill="#FFFCF4"/>
  <text x="15" y="62" font-family="system-ui,Segoe UI,Arial" font-weight="900" font-size="58" fill="{c}">{rank}</text>
  <g transform="translate({w - 56} 24) scale(34)"><path d="{SUIT[suit]}" fill="{c}"/></g>
  <g transform="translate({w / 2 - size / 2} {h / 2 - size / 2 + 22}) scale({size})"><path d="{SUIT[suit]}" fill="{c}"/>{face(ey, delay)}{acc_svg}</g>
</g></g>'''


def sparkle(x, y, s, color="#FFD166"):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0,-1 Q.12,-.12 1,0 Q.12,.12 0,1 Q-.12,.12 -1,0 Q-.12,-.12 0,-1Z" fill="{color}"/>'


def cards_art():
    return ('<svg viewBox="0 0 640 400" role="img" aria-label="Cards with faces">'
            + card(20, 60, -12, 1.08, "A", "H", None, 0.0)
            + card(170, 14, -4, 1.08, "K", "S", "crown", 1.1)
            + card(325, 40, 6, 1.08, "Q", "D", "crown", 2.3)
            + card(470, 92, 14, 1.08, "J", "C", "hat", 3.4)
            + sparkle(60, 30, 20) + sparkle(600, 40, 14, "#fff") + sparkle(40, 380, 13, "#fff") + sparkle(610, 370, 21) + sparkle(330, 12, 11, "#fff")
            + "</svg>")


def cube(x, y, size, rot, color, delay, mood="smile", brows=False):
    r = size * .22
    c = size / 2
    e = size * .17
    ex = size * .19
    pr = size * .075
    pupil_move = ""
    brows_svg = ""
    if brows:
        brows_svg = (f'<path d="M{c - ex - e},{c - e * 1.5} L{c - ex + e * .9},{c - e * 1.05}" stroke="#1B1B2B" stroke-width="{size * .035}" stroke-linecap="round"/>'
                     f'<path d="M{c + ex + e},{c - e * 1.5} L{c + ex - e * .9},{c - e * 1.05}" stroke="#1B1B2B" stroke-width="{size * .035}" stroke-linecap="round"/>')
    return (f'<g transform="translate({x} {y}) rotate({rot} {c} {c})"><g class="pcard" data-eyes>'
            f'<rect x="{size * .02}" y="{size * .04}" width="{size}" height="{size}" rx="{r}" fill="#000" opacity=".22"/>'
            f'<rect width="{size}" height="{size}" rx="{r}" fill="{color}"/>'
            f'<g transform="scale({size})">'
            f'<g class="eye" style="--d:{delay}s"><circle cx=".31" cy=".42" r=".105" fill="#fff"/><g class="pupil"><circle cx=".32" cy=".43" r=".055" fill="#1B1B2B"/></g></g>'
            f'<g class="eye" style="--d:{delay}s"><circle cx=".69" cy=".42" r=".105" fill="#fff"/><g class="pupil"><circle cx=".70" cy=".43" r=".055" fill="#1B1B2B"/></g></g>'
            f'<path d="M.38,.62 Q.5,.74 .62,.62" fill="none" stroke="#1B1B2B" stroke-width=".045" stroke-linecap="round"/>'
            f'<circle cx=".19" cy=".6" r=".06" fill="#fff" opacity=".28"/><circle cx=".81" cy=".6" r=".06" fill="#fff" opacity=".28"/>'
            f'</g>{brows_svg if False else ""}</g></g>')


def cubes_art():
    return ('<svg viewBox="0 0 640 400" role="img" aria-label="Cute blocks">'
            + cube(215, 90, 210, -3, "#7C5CC9", 0.0)
            + cube(60, 40, 120, -10, "#FFE45C", 1.4)
            + cube(470, 30, 120, 12, "#F0447C", 2.2)
            + cube(70, 245, 125, 8, "#EF5350", 3.1)
            + cube(490, 235, 125, -8, "#66BB6A", 0.7)
            + cube(300, 300, 85, 4, "#29B6F6", 1.9)
            + sparkle(190, 50, 20) + sparkle(600, 190, 13, "#fff") + sparkle(40, 360, 13, "#FFD166") + sparkle(430, 20, 12, "#fff") + sparkle(620, 360, 18)
            + "</svg>")


def suit_icon(suit, tint):
    c = tint
    return f'<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="12" fill="{c}" opacity=".16"/><g transform="translate(11 10) scale(22)"><path d="{SUIT[suit]}" fill="{c}"/></g></svg>'


def cube_icon(color):
    return (f'<svg viewBox="0 0 44 44" aria-hidden="true"><rect width="44" height="44" rx="12" fill="{color}" opacity=".16"/>'
            f'<rect x="9" y="9" width="26" height="26" rx="7" fill="{color}"/><circle cx="17" cy="21" r="3" fill="#fff"/><circle cx="27" cy="21" r="3" fill="#fff"/>'
            f'<circle cx="17.7" cy="21.6" r="1.5" fill="#1B1B2B"/><circle cx="27.7" cy="21.6" r="1.5" fill="#1B1B2B"/>'
            f'<path d="M17,27 Q22,31 27,27" fill="none" stroke="#1B1B2B" stroke-width="1.6" stroke-linecap="round"/></svg>')


# ------------------------------------------------------------------ sayfa içerikleri
LANGS_ALL = ["tr", "en", "es", "pt"]

SEC = {
    "shots": {"fr": "Captures d'écran", "tr": "Ekran görüntüleri", "en": "Screenshots", "es": "Capturas de pantalla", "pt": "Capturas de tela"},
    "features": {"fr": "Fonctionnalités", "tr": "Özellikler", "en": "Features", "es": "Características", "pt": "Recursos"},
    "faq": {"fr": "Questions fréquentes", "tr": "Sık sorulanlar", "en": "Frequently asked questions", "es": "Preguntas frecuentes", "pt": "Perguntas frequentes"},
    "more": {"fr": "Autres applis", "tr": "Diğer uygulamalarım", "en": "More from me", "es": "Más apps", "pt": "Mais apps"},
    "privacy": {"fr": "Politique de confidentialité", "tr": "Gizlilik Politikası", "en": "Privacy Policy", "es": "Política de privacidad", "pt": "Política de privacidade"},
    "webprivacy": {"fr": "Confidentialité du site", "tr": "Site gizliliği", "en": "Website privacy", "es": "Privacidad del sitio", "pt": "Privacidade do site"},
    "try": {"fr": "Essayer dans le navigateur", "tr": "Tarayıcıda dene", "en": "Try it in your browser", "es": "Pruébalo en el navegador", "pt": "Experimente no navegador"},
    "qr": {"fr": "Installer via QR", "tr": "QR ile yükle", "en": "Install via QR", "es": "Instalar con QR", "pt": "Instalar com QR"},
    "qrscan": {"fr": "Scannez avec votre téléphone", "tr": "Telefonunla tara", "en": "Scan with your phone", "es": "Escanea con tu móvil", "pt": "Escaneie com o celular"},
    "contact": {"fr": "Contact", "tr": "İletişim", "en": "Contact", "es": "Contacto", "pt": "Contato"},
    "back": {"fr": "← Nesim Apps", "tr": "← Nesim Apps", "en": "← Nesim Apps", "es": "← Nesim Apps", "pt": "← Nesim Apps"},
    "new": {"fr": "NOUVEAU JEU", "tr": "YENİ OYUN", "en": "NEW GAME", "es": "JUEGO NUEVO", "pt": "JOGO NOVO"},
    "newapp": {"fr": "NOUVEAU", "tr": "YENİ", "en": "NEW", "es": "NUEVO", "pt": "NOVO"},
}

CARDLES = dict(
    slug="cardles", name="Cardles", pkg="com.cardles.nesimapps", icon="cardles/icon.svg", tint="#2FA37F", hero=("#0F6B52", "#16A07F"),
    accent="#1F8A68", langs=LANGS_ALL, shots=8, art=cards_art, new_until="2026-12-15",
    title={"tr": "Cardles: Klasik Solitaire", "en": "Cardles: Solitaire Classics", "es": "Cardles: Solitario Clásico", "pt": "Cardles: Paciência Clássica"},
    tagline={"tr": "Güldüren solitaire", "en": "Solitaire that makes you smile", "es": "El solitario que te hace sonreír", "pt": "Paciência que faz você sorrir"},
    intro={
        "tr": "Dört klasik solitaire tek uygulamada: Klondike, Spider, FreeCell ve TriPeaks. Kartların yüzü var: göz kırpar, gözleriyle parmağını izler ve iyi oynayınca sevinir.",
        "en": "Four classic solitaire games in one app: Klondike, Spider, FreeCell and TriPeaks. The cards have faces: they blink, follow your finger with their eyes and cheer when you play well.",
        "es": "Cuatro solitarios clásicos en una sola app: Klondike, Spider, FreeCell y TriPeaks. Las cartas tienen cara: parpadean, siguen tu dedo con los ojos y celebran tus buenas jugadas.",
        "pt": "Quatro paciências clássicas em um só app: Klondike, Spider, FreeCell e TriPeaks. As cartas têm carinha: piscam, seguem seu dedo com os olhos e comemoram suas boas jogadas.",
    },
    chips=["Klondike", "Spider", "FreeCell", "TriPeaks"],
    desc="Four classic solitaire games in one app: Klondike, Spider, FreeCell and TriPeaks, with cards that have cute faces, a daily challenge, streaks and themes.",
    features=[
        ("S", {"tr": "Dört klasik", "en": "Four classics", "es": "Cuatro clásicos", "pt": "Quatro clássicos"},
         {"tr": "Klondike (1 ya da 3 kart), Spider (1, 2 ya da 4 takım), FreeCell ve TriPeaks. Her biri için kısa bir \"nasıl oynanır\" rehberi var.",
          "en": "Klondike (draw 1 or 3), Spider (1, 2 or 4 suits), FreeCell and TriPeaks. Every game has a short how-to-play guide.",
          "es": "Klondike (1 o 3 cartas), Spider (1, 2 o 4 palos), FreeCell y TriPeaks. Cada juego tiene una guía corta de cómo jugar.",
          "pt": "Klondike (1 ou 3 cartas), Spider (1, 2 ou 4 naipes), FreeCell e TriPeaks. Cada jogo tem um guia curto de como jogar."}),
        ("H", {"tr": "Yüzlü kartlar", "en": "Cards with faces", "es": "Cartas con cara", "pt": "Cartas com carinha"},
         {"tr": "Göz kırpan, parmağını izleyen ve kazanınca sevinen kartlar. Uzun süre dokunmazsan uyurlar.",
          "en": "Cards that blink, follow your finger and cheer when you win. Leave them alone for a while and they fall asleep.",
          "es": "Cartas que parpadean, siguen tu dedo y celebran cuando ganas. Si las dejas un rato, se duermen.",
          "pt": "Cartas que piscam, seguem seu dedo e comemoram quando você vence. Se você as deixar um tempo, elas dormem."}),
        ("D", {"tr": "Günlük meydan okuma", "en": "Daily challenge", "es": "Reto diario", "pt": "Desafio diário"},
         {"tr": "Her gün herkese aynı dağıtım, oyun türü her gün değişir. Seriyi koru, isteğe bağlı akşam hatırlatması al.",
          "en": "Everyone gets the same deal each day and the game changes daily. Keep your streak and get an optional evening reminder.",
          "es": "Todos reciben la misma partida cada día y el juego cambia a diario. Mantén tu racha y activa un recordatorio opcional por la tarde.",
          "pt": "Todos recebem o mesmo jogo a cada dia e o jogo muda todo dia. Mantenha sua sequência e ative um lembrete opcional à noite."}),
        ("C", {"tr": "Akıllı ipuçları", "en": "Smart hints", "es": "Pistas inteligentes", "pt": "Dicas inteligentes"},
         {"tr": "İpuçları gerçek bir çözümü izler. Geri al sınırsız ve her zaman ücretsiz; hamle kalmayınca oyun söyler.",
          "en": "Hints follow a real solution. Undo is unlimited and always free, and the game tells you when no moves are left.",
          "es": "Las pistas siguen una solución real. Deshacer es ilimitado y siempre gratis, y el juego avisa cuando no quedan movimientos.",
          "pt": "As dicas seguem uma solução real. Desfazer é ilimitado e sempre grátis, e o jogo avisa quando não há mais movimentos."}),
        ("S", {"tr": "Başarımlar ve sıralamalar", "en": "Achievements and leaderboards", "es": "Logros y clasificaciones", "pt": "Conquistas e classificações"},
         {"tr": "Google Play Oyunlar ile 30 başarım ve 10 liderlik tablosu: en hızlı galibiyetler, en az hamle, en uzun seri.",
          "en": "30 achievements and 10 leaderboards with Google Play Games: fastest wins, fewest moves, longest streaks.",
          "es": "30 logros y 10 clasificaciones con Google Play Juegos: victorias más rápidas, menos movimientos, rachas más largas.",
          "pt": "30 conquistas e 10 classificações com o Google Play Games: vitórias mais rápidas, menos movimentos, maiores sequências."}),
        ("H", {"tr": "Temalar, çevrimdışı, hesapsız", "en": "Themes, offline, no account", "es": "Temas, sin conexión, sin cuenta", "pt": "Temas, offline, sem conta"},
         {"tr": "Kazandıkça açılan dört masa teması ve 4 renkli deste seçeneği. Çevrimdışı oynanır, hesap gerekmez. Arayüz Türkçe, İngilizce, İspanyolca ve Portekizce.",
          "en": "Four table themes that unlock as you win and an optional 4-colour deck. Plays offline, no account needed. Available in English, Turkish, Spanish and Portuguese.",
          "es": "Cuatro temas de mesa que se desbloquean al ganar y una baraja opcional de 4 colores. Funciona sin conexión y sin cuenta. Disponible en inglés, turco, español y portugués.",
          "pt": "Quatro temas de mesa que se desbloqueiam ao vencer e um baralho opcional de 4 cores. Funciona offline e sem conta. Disponível em inglês, turco, espanhol e português."}),
    ],
    faq=[
        ({"tr": "Ücretsiz mi?", "en": "Is it free?", "es": "¿Es gratis?", "pt": "É grátis?"},
         {"tr": "Evet. Oyun bitince yeni oyuna geçerken ara sıra bir reklam gösterilir; isteğe bağlı bir video izleyerek ek ipucu kazanabilirsin. Geri al her zaman ücretsiz.",
          "en": "Yes. An ad is shown now and then between games, and you can optionally watch a video for extra hints. Undo is always free.",
          "es": "Sí. De vez en cuando se muestra un anuncio entre partidas, y puedes ver un vídeo opcional para conseguir pistas extra. Deshacer siempre es gratis.",
          "pt": "Sim. Um anúncio aparece de vez em quando entre os jogos, e você pode assistir a um vídeo opcional para ganhar dicas extras. Desfazer é sempre grátis."}),
        ({"tr": "İnternet gerekir mi?", "en": "Do I need internet?", "es": "¿Necesito internet?", "pt": "Preciso de internet?"},
         {"tr": "Hayır, oyunlar çevrimdışı oynanır. Reklamlar, liderlik tabloları ve başarımlar için bağlantı gerekir.",
          "en": "No, the games work offline. Ads, leaderboards and achievements need a connection.",
          "es": "No, los juegos funcionan sin conexión. Los anuncios, las clasificaciones y los logros necesitan conexión.",
          "pt": "Não, os jogos funcionam offline. Anúncios, classificações e conquistas precisam de conexão."}),
        ({"tr": "Her dağıtım çözülebilir mi?", "en": "Is every deal solvable?", "es": "¿Todas las partidas tienen solución?", "pt": "Todo jogo tem solução?"},
         {"tr": "FreeCell ve TriPeaks'te evet. Klondike ve Spider'da hamle kalmazsa oyun bunu söyler ve aynı dağıtımı yeniden oynayabilirsin.",
          "en": "In FreeCell and TriPeaks, yes. In Klondike and Spider the game tells you when no moves are left and you can replay the same deal.",
          "es": "En FreeCell y TriPeaks, sí. En Klondike y Spider el juego avisa cuando no quedan movimientos y puedes repetir la misma partida.",
          "pt": "No FreeCell e no TriPeaks, sim. No Klondike e no Spider o jogo avisa quando não há mais movimentos e você pode repetir o mesmo jogo."}),
        ({"tr": "Google Play Oyunlar zorunlu mu?", "en": "Do I need Google Play Games?", "es": "¿Necesito Google Play Juegos?", "pt": "Preciso do Google Play Games?"},
         {"tr": "Hayır, isteğe bağlı. Giriş yapmazsan oyun aynen çalışır; sadece sıralamalara ve başarımlara katılamazsın.",
          "en": "No, it is optional. Without signing in the game works the same; you just won't appear on leaderboards or earn achievements.",
          "es": "No, es opcional. Sin iniciar sesión el juego funciona igual; solo no aparecerás en las clasificaciones ni obtendrás logros.",
          "pt": "Não, é opcional. Sem entrar o jogo funciona igual; você só não aparece nas classificações nem ganha conquistas."}),
    ],
)

CUBBLES = dict(
    slug="cubbles", name="Cubbles", pkg="com.cubbles.nesimapps", icon="cubbles/icon.svg", tint="#7C5CC9", hero=("#2A1F5E", "#6C4BC4"),
    accent="#6A45D8", langs=["tr", "en"], shots=6, art=cubes_art, new_until="2026-11-30",
    title={"tr": "Cubbles: Sevimli Blok Bulmaca", "en": "Cubbles: Cute Block Puzzle"},
    tagline={"tr": "Sevimli bloklar, büyük kombolar", "en": "Cute blocks, big combos"},
    intro={
        "tr": "Başlaması kolay, bırakması zor sevimli bir blok bulmacası. Blokları tahtaya sürükle, tam satır ve sütunları temizle, kombo yap. Blokların yüzü var: göz kırpar, parmağını izler ve sevinir.",
        "en": "A cute block puzzle that's easy to start and hard to put down. Drag blocks onto the board, clear full rows and columns and chain combos. The blocks have faces: they blink, follow your finger and cheer.",
    },
    chips=["Combos", "Daily challenge", "Themes"],
    desc="A cute block puzzle: drag blocks onto the board, clear rows and columns and chain combos. Daily challenge, quests and themes.",
    features=[
        ("S", {"tr": "Tatmin edici kombolar", "en": "Satisfying combos"},
         {"tr": "3 hamle içinde yine temizle, serini büyüt ve tahtanın parlamasını izle.",
          "en": "Keep clearing within 3 moves to build your streak and watch the board glow."}),
        ("D", {"tr": "Günlük meydan okuma", "en": "Daily challenge"},
         {"tr": "Her gün herkese aynı parçalar gelir. Skorunu paylaş, serini koru.",
          "en": "Everyone gets the same pieces each day. Share your score and keep your streak alive."}),
        ("H", {"tr": "Görevler ve seviyeler", "en": "Quests and levels"},
         {"tr": "XP kazan, seviye atla ve yeni tahta temalarını aç. Play Oyunlar ile liderlik ve başarımlar.",
          "en": "Earn XP, level up and unlock new board themes. Leaderboards and achievements with Play Games."}),
        ("C", {"tr": "Adil oyun", "en": "Fair play"},
         {"tr": "Her parça seti hepsini yerleştirebileceğin şekilde seçilir; oyun ancak yerin bitince biter.",
          "en": "Each set of pieces is chosen so you can place all of them, so a game ends only when you run out of space."}),
    ],
    faq=[
        ({"tr": "Ücretsiz mi?", "en": "Is it free?"},
         {"tr": "Evet. Oyunlar arasında reklam gösterilir; oyun bitince isteğe bağlı bir reklam izleyip yer açarak devam edebilirsin.",
          "en": "Yes. Ads are shown between games, and after a game over you can optionally watch an ad to clear space and keep going."}),
        ({"tr": "İnternet gerekir mi?", "en": "Do I need internet?"},
         {"tr": "Hayır, oyun çevrimdışı oynanır. Reklamlar ve liderlik tabloları için bağlantı gerekir.",
          "en": "No, the game works offline. Ads and leaderboards need a connection."}),
        ({"tr": "Hangi dillerde?", "en": "Which languages?"},
         {"tr": "Oyun Türkçe ve İngilizce.", "en": "The game is available in English and Turkish."}),
    ],
)



def t(d, lang):
    return d.get(lang) or d.get("en") or next(iter(d.values()))


def multi(dct, langs, tag="span"):
    return "".join(f'<{tag} data-l="{l}">{t(dct, l)}</{tag}>' for l in langs)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


GLYPH = '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3 3h8v8H3zm2 2v4h4V5zm8-2h8v8h-8zm2 2v4h4V5zM3 13h8v8H3zm2 2v4h4v-4zm10-2h2v2h-2zm-2 2h2v2h-2zm4 0h2v2h-2zm-2 2h2v2h-2zm4 0h2v2h-2zm-4 2h2v2h-2z"/></svg>'


def page(cfg):
    L = cfg["langs"]
    slug = cfg["slug"]
    url = f"{BASE}/{slug}/"
    play = f"https://play.google.com/store/apps/details?id={cfg['pkg']}{REF}"
    feats = ""
    for b in cfg.get("bullets", []):
        feats += f'<div class="feat b">{tick_icon(cfg["tint"])}<h3>{multi(b, L, "span")}</h3></div>\n'
    for suit, title, text in cfg.get("features", []):
        icon = cube_icon(cfg["tint"] if suit in "SH" else {"D": "#F0A33A", "C": "#3AA0E0"}[suit]) if slug == "cubbles" else suit_icon(suit, {"S": "#2B2F45", "H": "#E0192F", "D": "#E0192F", "C": "#2B2F45"}[suit] if False else {"S": "#3B4260", "H": "#E0192F", "D": "#E0192F", "C": "#3B4260"}[suit])
        feats += f'<div class="feat">{icon}<h3>{multi(title, L, "span")}</h3><p>{multi(text, L, "span")}</p></div>\n'
    faqs = ""
    for q, a in cfg.get("faq", []):
        faqs += f'<details><summary>{multi(q, L)}</summary><p>{multi(a, L)}</p></details>\n'
    shots = ""
    sf = cfg.get("shotfiles")
    if sf is None:
        sf = {l: [f"shots/{l if os.path.isdir(os.path.join(G, slug, 'shots', l)) else 'en'}/{n:02d}.png" for n in range(1, cfg["shots"] + 1)] for l in L}
    vids = VIDEOS.get(cfg["slug"], {})
    for l in L:
        if l in vids:
            shots += (f'<figure class="vid" data-l="{l}"><button type="button" class="vidbtn" data-yt="{vids[l]}" data-app="{cfg["slug"]}" aria-label="{esc(VIDEO_PLAY[l])}">'
                      f'<img src="shots/{l}/video.jpg" alt="{esc(cfg["name"])} video" width="640" height="360" loading="lazy"><span class="pl"><i></i></span><span class="vl">{esc(VIDEO_LABEL[l])}</span></button></figure>\n')
        files = sf.get(l) or sf.get("en") or next(iter(sf.values()))
        for n, f in enumerate(files, 1):
            dim = cfg.get("dims", {}).get(f)
            wh = f' width="{dim[0]}" height="{dim[1]}"' if dim else ' width="360"'
            shots += f'<figure data-l="{l}"><div class="phone"><img src="{f}" alt="{esc(cfg["name"])} screenshot {n}"{wh} loading="lazy"></div></figure>\n'
    langbtn = "".join(f'<button type="button" data-lang="{l}" onclick="setLang(\'{l}\')">{l.upper()}</button>' for l in L)
    more = "".join(f'<a href="{href}"><img src="../{icon}" alt="{esc(name)} icon" width="40" height="40">{name}</a>' for href, name, icon in OTHERS if name != cfg["name"])
    faq_block = f'''  <section class="block faq" aria-labelledby="h-faq">
    <h2 class="h" id="h-faq">{multi(SEC['faq'], L)}</h2>
{faqs}  </section>
''' if faqs else ""
    note_block = f'<p class="note">{multi(cfg["note"], L, "span")}</p>' if cfg.get("note") else ""
    tag_html = f'<span class="tag" data-new-until="{cfg["new_until"]}">{multi(SEC["new"] if cfg["slug"] in GAME_SLUGS else SEC["newapp"], L)}</span>' if cfg.get("new_until") else ""
    chips = "".join(f"<li>{c}</li>" for c in cfg["chips"])
    video_dialog = ""
    if vids:
        video_dialog = (
            '<dialog class="vmodal" id="vmodal" aria-label="Video"><div class="vframe" id="vframe"></div><button type="button" class="vclose" aria-label="Close">\u2715</button></dialog>\n'
            '<script>(function(){var d=document.getElementById("vmodal");if(!d||!d.showModal)return;var f=document.getElementById("vframe");'
            'document.addEventListener("click",function(e){var b=e.target.closest&&e.target.closest(".vidbtn");'
            'if(b){f.innerHTML=\'<iframe src="https://www.youtube-nocookie.com/embed/\'+b.getAttribute("data-yt")+\'?autoplay=1&rel=0&playsinline=1" title="Video" '
            'allow="autoplay; encrypted-media; picture-in-picture; fullscreen" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>\';d.showModal();return;}'
            'if(e.target===d||(e.target.classList&&e.target.classList.contains("vclose")))d.close();});'
            'd.addEventListener("close",function(){f.innerHTML="";});})();</script>\n')
    jsonld = json.dumps({
        "@context": "https://schema.org", "@type": "SoftwareApplication", "name": cfg["name"], "operatingSystem": "Android",
        "applicationCategory": "GameApplication", "description": cfg["desc"], "url": url, "image": f"{BASE}/{slug}/icon.svg",
        "author": {"@type": "Person", "name": "Nesim Razon"}, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"},
        "installUrl": f"https://play.google.com/store/apps/details?id={cfg['pkg']}",
    }, ensure_ascii=False)
    title_main = t(cfg["title"], "en")
    qr_html = "" if cfg["slug"] in HIDDEN else (
        f'<details class="qr" data-qr="{cfg["slug"]}"><summary>' + GLYPH + multi(SEC["qr"], L) + '</summary><div class="qrpop">'
        f'<img src="../qr/{cfg["slug"]}.svg" alt="QR code: install {esc(cfg["name"])}" width="183" height="183" loading="lazy">' + multi(SEC["qrscan"], L, "p") + '</div></details>')
    demo_attr = {"tictactoe": ("data-ttt", "ttt.js?v=2"), "game2048": ("data-g2048", "g2048.js?v=1"), "calisan": ("data-calisan", "calisan.js?v=3")}.get(cfg["slug"])
    demo_block = (f'  <section class="block" aria-labelledby="h-demo">\n    <h2 class="h" id="h-demo">{multi(SEC["try"], L)}</h2>\n'
                  f'    <div class="demo-wrap"><div {demo_attr[0]} data-play="{play}"></div></div>\n  </section>\n\n') if demo_attr else ""
    ttt_script = f'\n<script src="../{demo_attr[1]}" defer></script>' if demo_attr else ""
    if cfg["slug"] == "calisan":
        # Uzun telefon demosu: kapalı gelir, düğmeye basınca açılır ve betik o zaman yüklenir (sayfa kısa kalsın, gereksiz indirme olmasın).
        demo_block = (f'  <section class="block" id="demo">\n    <button type="button" class="demo-open" data-demo-toggle="calisan" aria-expanded="false" aria-controls="demo-body"><span class="ar">▶</span> <span>{multi(SEC["try"], L)}</span></button>\n'
                      f'    <div class="demo-wrap" id="demo-body" hidden><div data-calisan data-play="{play}"></div></div>\n  </section>\n\n')
        ttt_script = ("\n<script>(function(){var b=document.querySelector('.demo-open');if(!b)return;b.addEventListener('click',function(){var w=document.getElementById('demo-body'),o=w.hidden;"
                      "w.hidden=!o;b.setAttribute('aria-expanded',o);b.querySelector('.ar').textContent=o?'▼':'▶';"
                      "if(o&&!document.getElementById('demo-js')){var s=document.createElement('script');s.id='demo-js';s.src='../calisan.js?v=3';document.head.appendChild(s);}"
                      "if(o)setTimeout(function(){w.scrollIntoView({behavior:'smooth',block:'start'});},50);});})();</script>")
    noindex = '\n<meta name="robots" content="noindex">' if cfg["slug"] in HIDDEN else ""
    return f'''<!doctype html>
<html lang="en" data-lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_main)}</title>
<meta name="description" content="{esc(cfg['desc'])}">
<link rel="canonical" href="{url}">{noindex}
<link rel="icon" href="../logo.svg" type="image/svg+xml">
<meta name="theme-color" content="{cfg['hero'][0]}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nesim Apps">
<meta property="og:title" content="{esc(title_main)}">
<meta property="og:description" content="{esc(cfg['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/{slug}/feature-en.png">
<meta name="twitter:card" content="summary_large_image">
<style>
:root {{ --accent:{cfg['accent']}; --hero-a:{cfg['hero'][0]}; --hero-b:{cfg['hero'][1]}; }}
</style>
<link rel="stylesheet" href="../landing.css?v=7">
<script src="/analytics.js?v=5" defer></script>
<script type="application/ld+json">{jsonld}</script>
</head>
<body>
<main>
  <header class="top">
    <a class="back" href="../">{SEC['back']['en']}</a>
    {('<div class="lang" role="group" aria-label="Language">' + langbtn + '</div>') if len(L) > 1 else ''}
  </header>

  <section class="lhero">
    <div class="copy">
      {tag_html}
      <h1{' class="long"' if max(len(v) for v in (cfg.get('names') or {'x': cfg['name']}).values()) > 14 else ''}>{multi(cfg['names'], L) if cfg.get('names') else cfg['name']}</h1>
      <p class="tagline">{multi(cfg['tagline'], L)}</p>
      <p class="intro">{multi(cfg['intro'], L)}</p>
      {('<ul class="chips">' + chips + '</ul>') if chips else ""}
      <div class="cta">
        <a class="play" href="{play}"><img src="../badges/google-play-tr.svg" alt="Google Play" data-l="tr"><img src="../badges/google-play-en.svg" alt="Get it on Google Play" data-l="en">{"".join(f'<img src="../badges/google-play-en.svg" alt="Google Play" data-l="{l}">' for l in L if l not in ("tr", "en"))}</a>
        {qr_html}
        <a class="small" href="privacy.html#{ 'tr' if False else 'en'}" data-l-privacy>{multi(SEC['privacy'], L)}</a>
      </div>
    </div>
    <div class="art">{cfg['art']()}</div>
  </section>

{demo_block}  <section class="block" aria-labelledby="h-shots">
    <h2 class="h" id="h-shots">{multi(SEC['shots'], L)}</h2>
    <div class="strip">
{shots}    </div>
  </section>

  <section class="block" aria-labelledby="h-feat">
    <h2 class="h" id="h-feat">{multi(SEC['features'], L)}</h2>
    <div class="fgrid">
{feats}    </div>
    {note_block}
  </section>

{faq_block}
  <section class="block" aria-labelledby="h-more">
    <h2 class="h" id="h-more">{multi(SEC['more'], L)}</h2>
    <div class="more">{more}</div>
  </section>

  <footer>{multi(SEC['contact'], L)}: <a href="mailto:nesim.razon@gmail.com">nesim.razon@gmail.com</a> · <a href="privacy.html">{multi(SEC['privacy'], L)}</a> · <a href="/site-privacy.html">{multi(SEC['webprivacy'], L)}</a></footer>
</main>
{video_dialog}<script>
  (function () {{
    var supported = {json.dumps(L)};
    var priv = {json.dumps(cfg.get("priv", ["tr", "en", "es", "pt"]))};
    var lang;
    try {{ lang = localStorage.getItem("lang"); }} catch (e) {{}}
    if (supported.indexOf(lang) < 0) {{
      var n = (navigator.language || "en").toLowerCase().slice(0, 2);
      lang = supported.indexOf(n) >= 0 ? n : (supported.indexOf("en") >= 0 ? "en" : supported[0]);
    }}
    window.setLang = function (l) {{
      document.documentElement.setAttribute("data-lang", l);
      document.documentElement.lang = l;
      try {{ localStorage.setItem("lang", l); }} catch (e) {{}}
      [].forEach.call(document.querySelectorAll(".lang button"), function (b) {{ b.setAttribute("aria-pressed", b.dataset.lang === l); }});
      [].forEach.call(document.querySelectorAll("[data-l-privacy]"), function (a) {{ a.href = "privacy.html#" + (priv.indexOf(l) >= 0 ? l : (priv.indexOf("en") >= 0 ? "en" : priv[0])); }});
    }};
    setLang(lang);
    var today = new Date().toISOString().slice(0, 10);
    [].forEach.call(document.querySelectorAll("[data-new-until]"), function (el) {{ if (today > el.dataset.newUntil) el.remove(); }});
  }})();
</script>
<script src="../eyes.js?v=3"></script>{ttt_script}
<script>
  // QR açılırken: dışarı tıklayınca ya da Esc ile kapanır (aynı anda yalnız biri açık).
  document.addEventListener("click", function (e) {{ document.querySelectorAll("details.qr[open]").forEach(function (d) {{ if (!d.contains(e.target)) d.removeAttribute("open"); }}); }});
  document.addEventListener("keydown", function (e) {{ if (e.key === "Escape") document.querySelectorAll("details.qr[open]").forEach(function (d) {{ d.removeAttribute("open"); }}); }});
</script>
</body>
</html>
'''



CUBBLES["langs"] = ["tr", "en", "es", "pt"]
_cx = {
    "title": ("Cubbles: Puzle de Bloques Adorable", "Cubbles: Quebra-cabeça de Blocos Fofo"),
    "tagline": ("Bloques adorables, grandes combos", "Blocos fofos, grandes combos"),
    "intro": ("Un rompecabezas de bloques adorable, fácil de empezar y difícil de soltar. Arrastra bloques al tablero, completa filas y columnas y encadena combos. Los bloques tienen cara: parpadean, siguen tu dedo con los ojos y celebran.",
              "Um quebra-cabeça de blocos fofo, fácil de começar e difícil de largar. Arraste blocos para o tabuleiro, complete linhas e colunas e encadeie combos. Os blocos têm carinha: piscam, seguem seu dedo com os olhos e comemoram."),
}
for _k, (_es, _pt) in _cx.items():
    CUBBLES[_k]["es"], CUBBLES[_k]["pt"] = _es, _pt
_cf = [
    (("Combos satisfactorios", "Combos satisfatórios"), ("Sigue limpiando en un máximo de 3 movimientos para aumentar tu racha y ver cómo brilla el tablero.", "Continue limpando em até 3 jogadas para aumentar sua sequência e ver o tabuleiro brilhar.")),
    (("Reto diario", "Desafio diário"), ("Todos reciben las mismas piezas cada día. Comparte tu puntuación y mantén tu racha.", "Todos recebem as mesmas peças a cada dia. Compartilhe sua pontuação e mantenha sua sequência.")),
    (("Misiones y niveles", "Missões e níveis"), ("Gana XP, sube de nivel y desbloquea nuevos temas de tablero. Clasificaciones y logros con Google Play Juegos.", "Ganhe XP, suba de nível e desbloqueie novos temas de tabuleiro. Classificações e conquistas com o Google Play Games.")),
    (("Juego limpio", "Jogo justo"), ("Cada conjunto de piezas se elige para que puedas colocarlas todas, así que la partida solo termina cuando te quedas sin espacio.", "Cada conjunto de peças é escolhido para que você consiga colocar todas, então a partida só termina quando acabar o espaço.")),
]
for (_s, _t, _x), ((_te, _tp), (_xe, _xp)) in zip(CUBBLES["features"], _cf):
    _t["es"], _t["pt"], _x["es"], _x["pt"] = _te, _tp, _xe, _xp
_cq = [
    (("¿Es gratis?", "É grátis?"), ("Sí. Se muestran anuncios entre partidas y, tras perder, puedes ver un anuncio opcional para liberar espacio y seguir jugando.", "Sim. Anúncios aparecem entre as partidas e, após perder, você pode assistir a um anúncio opcional para liberar espaço e continuar.")),
    (("¿Necesito internet?", "Preciso de internet?"), ("No, el juego funciona sin conexión. Los anuncios y las clasificaciones necesitan conexión.", "Não, o jogo funciona offline. Anúncios e classificações precisam de conexão.")),
    (("¿En qué idiomas está?", "Em quais idiomas?"), ("El juego está disponible en inglés y turco.", "O jogo está disponível em inglês e turco.")),
]
for (_q, _a), ((_qe, _qp), (_ae, _ap)) in zip(CUBBLES["faq"], _cq):
    _q["es"], _q["pt"], _a["es"], _a["pt"] = _qe, _qp, _ae, _ap
# ------------------------------------------------------------------ diğer oyun/uygulamalar: listing.md'den otomatik
import sys
import subprocess
import shutil

ROOT = r"C:\@Development\PersonalAndroidApps"
CSS_EXTRA = '''
.feat.b { grid-template-columns:30px minmax(0,1fr); align-items:center; padding:14px 18px; }
.feat.b svg { width:30px; height:30px; grid-row:auto; }
.feat.b h3 { font-size:15.5px; font-weight:600; line-height:1.45; }
.lhero h1.long { font-size:clamp(30px,5.4vw,50px); line-height:1.08; }
.note { color:var(--dim); margin:16px 0 0; max-width:70ch; }
.iconart { display:flex; align-items:center; justify-content:center; padding:10px 0 26px; }
.iconart img { width:min(46vw,200px); height:auto; border-radius:23%; box-shadow:0 14px 34px rgba(0,0,0,.35); }
'''
VIDEO_CSS = r'''
/* Mağaza videosu kutusu (ekran görüntüleri şeridinin ilki) ve modal */
.strip figure.vid { display:flex; align-items:center; }
.vidbtn { position:relative; display:block; width:min(80vw,440px); aspect-ratio:16/9; border:0; padding:0; border-radius:22px; overflow:hidden; cursor:pointer; background:#0b0d18; box-shadow:var(--shadow); }
.vidbtn img { display:block; width:100%; height:100%; object-fit:cover; }
.vidbtn .pl { position:absolute; inset:0; display:flex; align-items:center; justify-content:center; background:linear-gradient(180deg,rgba(0,0,0,0) 40%,rgba(0,0,0,.35)); }
.vidbtn .pl i { width:74px; height:74px; border-radius:50%; background:rgba(255,255,255,.93); display:flex; align-items:center; justify-content:center; box-shadow:0 8px 24px rgba(0,0,0,.45); transition:transform .15s; }
.vidbtn:hover .pl i, .vidbtn:focus-visible .pl i { transform:scale(1.1); }
.vidbtn .pl i::after { content:""; margin-left:6px; border-style:solid; border-width:15px 0 15px 25px; border-color:transparent transparent transparent #1B1030; }
.vidbtn .vl { position:absolute; left:12px; bottom:10px; background:rgba(0,0,0,.62); color:#fff; font-size:12px; font-weight:700; padding:4px 11px; border-radius:999px; }
.vidbtn:focus-visible { outline:3px solid var(--accent,#fff); outline-offset:3px; }
dialog.vmodal { border:0; padding:0; background:transparent; max-width:none; width:min(94vw,960px); overflow:visible; }
dialog.vmodal::backdrop { background:rgba(8,6,20,.84); }
.vframe { position:relative; aspect-ratio:16/9; background:#000; border-radius:16px; overflow:hidden; box-shadow:0 20px 60px rgba(0,0,0,.6); }
.vframe iframe { position:absolute; inset:0; width:100%; height:100%; border:0; }
.vclose { position:absolute; top:-48px; right:0; width:40px; height:40px; border-radius:50%; border:0; background:rgba(255,255,255,.92); color:#1B1030; font-size:18px; font-weight:800; cursor:pointer; }
'''
LANDING_CSS += CSS_EXTRA
LANDING_CSS += VIDEO_CSS

# slug, klasör, ad(tr), ad(en), simge, tint, ekran görüntüsü kaynakları {dil: klasör}, yeni-rozet
APPDEFS = [
    ("astrolings", "Astrolings", "Astrolings", "Astrolings", "icon.png", "#6A5ACD", {"tr": "tr"}, "2026-11-24"),
    ("tombalings", "Tombalings", "Tombalings", "Tombalings", "icon.png", "#FFC94D", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-10"),
    ("pentolings", "Pentolings", "Pentolings", "Pentolings", "icon.png", "#8E6BFF", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2027-01-05"),
    ("nudgelings", "Nudgelings", "Nudgelings", "Nudgelings", "icon.png", "#2FBF8A", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-20"),
    ("grumblings", "Grumblings", "Grumblings", "Grumblings", "icon.png", "#9B6BFF", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-10"),
    ("tilelings", "Tilelings", "Tilelings", "Tilelings", "icon.png", "#2E9E73", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-05"),
    ("nuzzlings", "Nuzzlings", "Nuzzlings", "Nuzzlings", "icon.png", "#F4A15B", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-31"),
    ("logiclings", "Logiclings", "Logiclings", "Logiclings", "icon.png", "#E8B64C", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-15"),
    ("beamies", "Beamies", "Beamies", "Beamies", "icon.svg", "#F2C14E", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, "2026-12-03"),
    ("haftasonum", "Etkinlik", "Hafta Sonum", "Hafta Sonum", "icon.png", "#FFC857", {"tr": "tr"}, "2026-12-02"),
    ("calisan", "CalisanAsistani", "Çalışan Asistanı", "Çalışan Asistanı", "icon.svg", "#2F6F5E", {"tr": "tr"}, "2026-12-15"),
    ("uzaygunlugu", "UzayGunlugu", "Uzay Günlüğü", "Uzay Günlüğü", "icon.png", "#3A5BC7", {"tr": "tr"}, "2026-12-15"),
    ("sliplines", "OkKacisi", "Sliplines", "Sliplines", "icon.png", "#F08A4B", {"en": "en-US", "tr": "tr-TR", "es": "es-ES", "pt": "pt-BR"}, "2026-11-30"),
    ("game2048", "Game2048", "2048", "2048", "icon.svg", "#EDC22E", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, None),
    ("tictactoe", "TicTacToe", "Tic-Tac-Toe", "Tic-Tac-Toe", "icon.svg", "#4CC9C0", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, None),
    ("sansoyunlari", "SansOyunlari", "Şans Oyunları", "Şans Oyunları", "icon.svg", "#F2B23A", {"tr": "tr"}, None),
    ("whereami", "WhereAmI", "Neredeyim?", "Where Am I?", "icon.svg", "#E5544B", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, None),
    ("agecalculator", "AgeCalculator", "Yaş Hesaplama", "Age Calculator", "icon.svg", "#5AB8D8", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, None),
    ("sondepremler", "SonDepremler", "Son Depremler", "Son Depremler", "icon.svg", "#E04F5F", {"en": "en", "tr": "tr"}, None),
    ("bmicalculator", "BMICalculator", "Vücut Kitle İndeksi", "BMI Calculator", "icon.svg", "#5BB27A", {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}, None),
    ("anthemturkey", "NationalAnthemofTurkey", "National Anthem of Turkey", "National Anthem of Turkey", "icon.svg", "#E30A17", {"en": "en", "tr": "tr"}, None),
    ("anthemcanada", "NationalAnthemofCanada", "National Anthem of Canada", "National Anthem of Canada", "icon.svg", "#D52B1E", {"en": "en", "fr": "fr"}, None),
    ("turksail", "TurkSail", "TurkSail", "TurkSail", "icon.svg", "#2E6FBF", {"tr": "."}, None),
    ("medyafobi", "MedyaFobi", "MedyaFobi", "MedyaFobi", "icon.svg", "#D9302C", {"tr": "."}, None),
]
GAME_SLUGS = ["cardles", "cubbles", "sliplines", "game2048", "tictactoe"]
SLIP_TEXT = {
    "tr": ("Okları doğru sırayla kaydır, tahtayı boşalt", "Okları doğru sırayla kaydırıp tahtayı boşalttığın bir bulmaca oyunu. Yüzlerce seviye, dünya sıralamalı Günün Bulmacası ve toplanacak rozetler."),
    "en": ("Slide the arrows out in the right order", "An arrow puzzle game: slide the arrows out in the right order and clear the board. Hundreds of levels, a Daily Puzzle with a global leaderboard, and badges to collect."),
}
MD = r"C:\@Development\PersonalAndroidApps"


def parse_okk():
    d = os.path.join(MD, "OkKacisi", "market_assets", "listing")
    out = {}
    for fn in os.listdir(d):
        m = re.match(r"([a-z]{2})-[A-Z]{2}\.txt$", fn)
        if not m:
            continue
        txt = open(os.path.join(d, fn), encoding="utf-8").read()
        parts = re.split(r"=== [^\n]*===\n", txt)
        out[m.group(1)] = dict(name=parts[1].strip(), short=parts[2].strip(), full=parts[3].strip())
    return out


def parse_listing(folder):
    if folder == "OkKacisi":
        return parse_okk()
    p = os.path.join(MD, folder, "market_assets", "listing.md")
    if not os.path.exists(p):
        return {}
    txt = open(p, encoding="utf-8").read()
    out = {}
    for sec in re.split(r"\n## ", txt)[1:]:
        m = re.match(r"[^\n]*\(([a-z]{2})-[A-Za-z0-9]+", sec)
        if not m:
            continue
        lang = m.group(1)

        def block(title):
            mm = re.search(r"### (?:" + title + r")[^\n]*\n\s*```[^\n]*\n(.*?)\n```", sec, re.S)
            return mm.group(1).strip() if mm else ""
        name = block("Uygulama adı|Başlık|Title")
        short = block("Kısa açıklama|Short description")
        full = block("Tam açıklama|Full description")
        if not (name or short or full):
            continue
        out[lang] = dict(name=name, short=short, full=full)
    return out


def split_full(full):
    lines = full.split("\n")
    intro, bullets, tail = [], [], []
    state = "intro"
    for ln in lines:
        if ln.startswith("•"):
            bullets.append(ln.lstrip("• ").strip())
            state = "tail"
            continue
        if not ln.strip() or (ln.isupper() and len(ln) < 60):
            continue
        if state == "intro":
            if not ln.rstrip().endswith(":"):
                intro.append(ln.strip())
        elif ln[:1].isspace() and ln.lstrip()[:1] in ("\u2013", "-"):
            tail.append("\u00a7" + ln.strip())   # alt madde işareti
        else:
            tail.append(ln.strip())
    return intro, bullets, tail


def format_note(tail):
    """Girintili alt maddeleri satır satır, diğer cümleleri paragraf olarak birleştirir."""
    subs = [x[1:] for x in tail if x.startswith("\u00a7")]
    rest = [x for x in tail if not x.startswith("\u00a7")]
    out = "<br>".join(subs)
    if subs and rest:
        out += "<br><br>"
    return out + " ".join(rest)


def darken(hexc, f):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % (int(r * f), int(g * f), int(b * f))


def tick_icon(color):
    return (f'<svg viewBox="0 0 30 30" aria-hidden="true"><circle cx="15" cy="15" r="15" fill="{color}" opacity=".18"/>'
            f'<path d="M8.5 15.5 L13 20 L21.5 10.5" fill="none" stroke="{color}" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def index_pkgs():
    s = open(os.path.join(G, "index.html"), encoding="utf-8").read()
    out = {}
    # Yeni ana sayfa (tools/gen_home.py): her kartta data-slug + data-pkg
    for m in re.finditer(r'data-slug="([a-z0-9]+)" data-pkg="([A-Za-z0-9_.]+)"', s):
        out.setdefault(m.group(1), m.group(2))
    # Eski düzen (yedek): ikon + Play bağlantısındaki id=
    for m in re.finditer(r'<img (?:class="icon" )?src="([^/"]+)/icon[^>]*>.*?details\?id=([A-Za-z0-9_.]+)', s, re.S):
        out.setdefault(m.group(1), m.group(2))
    return out


def shot_list(folder, srcdir):
    base = os.path.join(MD, folder, "market_assets")
    newer = sorted(glob.glob(os.path.join(base, "screenshots_*", srcdir)))  # örn. screenshots_1.1.0: varsa en yenisi kullanılır
    d = newer[-1] if newer else os.path.join(base, "screenshots", srcdir)
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.lower().endswith(".png")]


def build_apps():
    pk = index_pkgs()
    cfgs = []
    for slug, folder, ntr, nen, icon, tint, shotsrc, new in APPDEFS:
        lst = parse_listing(folder)
        langs = list(shotsrc.keys())
        langs = [l for l in (["tr", "en", "es", "pt", "fr"]) if l in langs]
        cfg = dict(slug=slug, name=nen, names={"tr": ntr, "en": nen, "es": nen, "pt": nen, "fr": nen}, pkg=(PKG_FALLBACK.get(slug) or pk[slug]), icon=f"{slug}/{icon}", tint=tint,
                   hero=(darken(tint, .38), darken(tint, .72)), accent=darken(tint, .66), langs=langs, new_until=new,
                   title={}, tagline={}, intro={}, chips=[], bullets=[], note=None,
                   art=(lambda s=slug, i=icon, nen=nen: f'<div class="iconart"><img src="{i}" alt="{nen} icon" width="200" height="200"></div>'))
        if True:
            bullets, notes = {}, {}
            for l in langs:
                e = lst.get(l) or lst.get("en") or lst["tr"]
                intro, bl, tail = split_full(e["full"])
                cfg["title"][l] = e["name"]
                cfg["tagline"][l] = e["short"]
                cfg["intro"][l] = " ".join(intro[:2])
                bullets[l] = bl
                notes[l] = format_note(tail)
            cfg["desc"] = (lst.get("en") or lst["tr"])["short"]
            n = max(len(v) for v in bullets.values())
            cfg["bullets"] = [{l: (bullets[l][i] if i < len(bullets[l]) else bullets[langs[0]][i]) for l in langs} for i in range(n)]
            if any(notes.values()):
                cfg["note"] = {l: notes[l] for l in langs}
            cfg["shotfiles_src"] = {l: shot_list(folder, shotsrc[l]) for l in langs}
        cfg["priv"] = re.findall(r'id="([a-z]{2})"', open(os.path.join(G, slug, "privacy.html"), encoding="utf-8").read())
        cfgs.append(cfg)
    return cfgs


APPCFGS = build_apps()
ALL = [CARDLES, CUBBLES] + APPCFGS
for _c in (CARDLES, CUBBLES):
    _c["priv"] = re.findall(r'id="([a-z]{2})"', open(os.path.join(G, _c["slug"], "privacy.html"), encoding="utf-8").read())
NAME_EN = {c["slug"]: c["name"] for c in ALL}
ICON = {c["slug"]: c["icon"] for c in ALL}
VISIBLE = [c for c in ALL if c["slug"] not in HIDDEN]
ORDER = GAME_SLUGS + [c["slug"] for c in VISIBLE if c["slug"] not in GAME_SLUGS]
OTHERS = [(f"../{sl}/", NAME_EN[sl], ICON[sl]) for sl in ORDER]
# i18n_split.py için sayfa verisi (dil başına başlık/slogan/giriş): anahtar kelimeli <title>/<meta description> buradan üretilir
json.dump({c["slug"]: {"name": c["name"], "title": c.get("title", {}), "tagline": c.get("tagline", {}), "intro": c.get("intro", {})} for c in ALL},
          open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "_pages.json"), "w", encoding="utf-8"), ensure_ascii=False)

import base64
import html as _html

SCR = os.path.dirname(os.path.abspath(__file__))


def make_thumbs():
    jobs = []  # (src, out relative to G)
    for cfg in APPCFGS:
        cfg["shotfiles"] = {}
        for l, files in cfg["shotfiles_src"].items():
            rels = []
            for n, src in enumerate(files, 1):
                rel = f"{cfg['slug']}/shots/{l}/{n:02d}.jpg"
                rels.append(f"shots/{l}/{n:02d}.jpg")
                jobs.append((src, rel))
            cfg["shotfiles"][l] = rels
    manifest_p = os.path.join(SCR, "thumbs_manifest.json")
    manifest = json.load(open(manifest_p)) if os.path.exists(manifest_p) else {}
    todo = [(s_, r) for s_, r in jobs if r not in manifest or not os.path.exists(os.path.join(G, r))]
    if todo:
        page_p = os.path.join(SCR, "thumbs.html")
        js_jobs = json.dumps([[("file:///" + s_.replace("\\", "/")), r] for s_, r in todo])
        import threading
        import http.server
        got = []

        class H(http.server.BaseHTTPRequestHandler):
            def do_POST(self):
                n = int(self.headers.get("Content-Length", 0))
                got.append(json.loads(self.rfile.read(n).decode("utf-8")))
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()

            def do_OPTIONS(self):
                self.send_response(200)
                self.send_header("Access-Control-Allow-Origin", "*")
                self.send_header("Access-Control-Allow-Headers", "*")
                self.end_headers()

            def log_message(self, *a):
                pass
        srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), H)
        port = srv.server_address[1]
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        imgs = "".join(f'<img src="file:///{s_.replace(chr(92), "/")}" data-rel="{r}">' for s_, r in todo)
        open(page_p, "w", encoding="utf-8").write("""<!doctype html><meta charset="utf-8">""" + imgs + """<script>
window.addEventListener("load", function () {
  [].forEach.call(document.querySelectorAll("img"), function (im) {
    var o;
    try {
      var w = 360, h = Math.round(w * im.naturalHeight / im.naturalWidth);
      var c = document.createElement("canvas"); c.width = w; c.height = h;
      var x = c.getContext("2d"); x.imageSmoothingQuality = "high"; x.drawImage(im, 0, 0, w, h);
      o = {rel: im.dataset.rel, w: w, h: h, d: c.toDataURL("image/jpeg", 0.82).split(",")[1]};
    } catch (e) { o = {rel: im.dataset.rel, err: String(e)}; }
    fetch("http://127.0.0.1:%d/", {method: "POST", mode: "cors", headers: {"Content-Type": "text/plain"}, body: JSON.stringify(o)});
  });
});
</script>""" % port)
        chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        if not os.path.exists(chrome):
            chrome = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
        prof = os.path.join(SCR, "vb_thumbs")
        proc = subprocess.Popen([chrome, "--headless=new", "--disable-gpu", "--allow-file-access-from-files", f"--user-data-dir={prof}", "file:///" + page_p.replace("\\", "/")],
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        import time
        for _ in range(240):
            if len(got) >= len(todo):
                break
            time.sleep(1)
        proc.kill()
        srv.shutdown()
        if len(got) < len(todo):
            # Chrome küçük resim üretemediyse (ör. başsız Chrome açılmadı) Pillow ile aynı boyut/kalitede üret (5.11.2026 yedek yol)
            from PIL import Image
            done = {it["rel"] for it in got if "err" not in it}
            for s_, r in todo:
                if r in done:
                    continue
                im = Image.open(s_).convert("RGB")
                w = 360; h = round(w * im.height / im.width)
                out = os.path.join(G, r)
                os.makedirs(os.path.dirname(out), exist_ok=True)
                im.resize((w, h), Image.LANCZOS).save(out, "JPEG", quality=82)
                manifest[r] = [w, h]
        assert True
        for it in got:
            assert "err" not in it, it
            out = os.path.join(G, it["rel"])
            os.makedirs(os.path.dirname(out), exist_ok=True)
            open(out, "wb").write(base64.b64decode(it["d"]))
            manifest[it["rel"]] = [it["w"], it["h"]]
        json.dump(manifest, open(manifest_p, "w"))
    for cfg in APPCFGS:
        cfg["dims"] = {f: manifest[f"{cfg['slug']}/{f}"] for fl in cfg["shotfiles"].values() for f in fl}


make_thumbs()

# ------------------------------------------------------------------ yaz
open(os.path.join(G, "eyes.js"), "w", encoding="utf-8", newline="\n").write(EYES_JS)
open(os.path.join(G, "landing.css"), "w", encoding="utf-8", newline="\n").write(LANDING_CSS)
for cfg in ALL:
    open(os.path.join(G, cfg["slug"], "index.html"), "w", encoding="utf-8", newline="\n").write(page(cfg))

# robots + sitemap
pages = ["", "site-privacy.html"] + [f"{c['slug']}/{x}" for c in VISIBLE for x in ("", "privacy.html")]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{BASE}/{p}</loc></url>\n" for p in pages) + "</urlset>\n"
open(os.path.join(G, "sitemap.xml"), "w", encoding="utf-8", newline="\n").write(sm)
open(os.path.join(G, "robots.txt"), "w", encoding="utf-8", newline="\n").write(
    "User-agent: *\nAllow: /\n\n# Yapay zeka arama/asistan tarayicilari serbest (5.11.2026)\n"
    + "".join(f"User-agent: {b}\nAllow: /\n" for b in ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-SearchBot", "Claude-User", "PerplexityBot", "Google-Extended"])
    + f"\nSitemap: {BASE}/sitemap.xml\n")

# her karta "Detaylar / Learn more"
_ip = os.path.join(G, "index.html")
_s = open(_ip, encoding="utf-8").read()
for _c in APPCFGS:
    _sl = _c["slug"]
    if _sl in HIDDEN or f'href="{_sl}/"' in _s:
        continue
    _a = f'<a class="small" href="{_sl}/privacy.html#tr" lang="tr">'
    assert _s.count(_a) >= 1, _sl
    _s = _s.replace(_a, f'<a class="small" href="{_sl}/" lang="tr"><b>Daha fazla</b></a>\n            <a class="small" href="{_sl}/" lang="en"><b>Learn more</b></a>\n            <a class="small" href="{_sl}/" lang="es"><b>Más información</b></a>\n            <a class="small" href="{_sl}/" lang="pt"><b>Saiba mais</b></a>\n            ' + _a)
open(_ip, "w", encoding="utf-8", newline="\n").write(_s)


print("ok")

import subprocess as _sp, sys as _sys
_sp.run([_sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "seo_fix.py")])
if not os.environ.get("NO_SPLIT"):
    _sp.run([_sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "i18n_split.py")])
