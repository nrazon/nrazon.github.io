# Ana sayfa (index.html) üretici betiği. Veri: tools/home_data.json (uygulamalar, 4 dilli ad ve açıklamalar), tools/cardles_hero.svg.
# Kullanım:  py -3 tools/gen_home.py            -> yeni.html (önizleme, noindex)
#            py -3 tools/gen_home.py --yayin    -> index.html
# Yeni uygulama = home_data.json'a satır (status: live|soon, cat: games|apps, showcase: true büyük kart). Sayfayı elle düzenleme, betiği düzenle.
# KORUNAN SÖZLEŞMELER (analytics.js ve gen_site.py buna bağlı):
#   - Uygulama Play bağlantıları "play.google.com/store/apps/details?id=<paket>&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dweb" (play_click)
#   - Detay sayfası bağlantıları "<slug>/" (app_open); dil düğmeleri data-lang + setLang(); gen_site.py paket adını data-pkg/data-slug'dan okur
#   - html sınıfı tr|en|es|pt, [lang] gizleme kuralı, data-new-until rozetleri, data-eyes (eyes.js)
import html as H
import json
import os
import sys

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ("tr", "en", "es", "pt")
DATA = json.load(open(os.path.join(G, "tools", "home_data.json"), encoding="utf-8"))
HERO_SVG = open(os.path.join(G, "tools", "cardles_hero.svg"), encoding="utf-8").read()
UTM = "&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dweb"


def esc(s):
    return H.escape(s, quote=True)


def L(d, tag="span", cls=""):
    """4 dilli metin: her dil kendi lang etiketli öğesinde (CSS yalnız seçili dili gösterir)."""
    c = f' class="{cls}"' if cls else ""
    return "".join(f'<{tag} lang="{l}"{c}>{d[l]}</{tag}>' for l in LANGS if l in d)


T = {
    "tagline": {"tr": "Güldüren oyunlar,<br>işe yarayan uygulamalar.", "en": "Games that make you smile,<br>apps that get things done.",
                "es": "Juegos que hacen sonreír,<br>apps que sirven de verdad.", "pt": "Jogos que fazem sorrir,<br>apps que resolvem."},
    "eyebrow": {"tr": "Bağımsız Android geliştiricisi", "en": "Independent Android developer", "es": "Desarrollador Android independiente", "pt": "Desenvolvedor Android independente"},
    "lead": {"tr": "Nesim Razon'un Android oyunları ve uygulamaları", "en": "Android games and apps by Nesim Razon",
             "es": "Juegos y aplicaciones de Android de Nesim Razon", "pt": "Jogos e aplicativos Android de Nesim Razon"},
    "nav_games": {"tr": "Oyunlar", "en": "Games", "es": "Juegos", "pt": "Jogos"},
    "nav_apps": {"tr": "Uygulamalar", "en": "Apps", "es": "Apps", "pt": "Apps"},
    "nav_about": {"tr": "Hakkımda", "en": "About", "es": "Acerca de", "pt": "Sobre"},
    "h_games": {"tr": "Oyunlar", "en": "Games", "es": "Juegos", "pt": "Jogos"},
    "h_games_sub": {"tr": "Kısa molalar için, uzun süre bırakamayacağın oyunlar. Hepsi ücretsiz.", "en": "Games for short breaks you won't want to put down. All free.",
                    "es": "Juegos para pausas cortas que no querrás soltar. Todos gratis.", "pt": "Jogos para pausas curtas que você não vai querer largar. Todos grátis."},
    "h_apps": {"tr": "Uygulamalar", "en": "Apps", "es": "Apps", "pt": "Apps"},
    "h_apps_sub": {"tr": "Gündelik işler için küçük yardımcılar.", "en": "Small helpers for everyday tasks.", "es": "Pequeños ayudantes para el día a día.", "pt": "Pequenos ajudantes para o dia a dia."},
    "h_soon": {"tr": "Çok yakında", "en": "Coming soon", "es": "Próximamente", "pt": "Em breve"},
    "soonchip": {"tr": "YAKINDA", "en": "COMING SOON", "es": "PRÓXIMAMENTE", "pt": "EM BREVE"},
    "new": {"tr": "YENİ", "en": "NEW", "es": "NUEVO", "pt": "NOVO"},
    "newgame": {"tr": "YENİ OYUN", "en": "NEW GAME", "es": "JUEGO NUEVO", "pt": "JOGO NOVO"},
    "popular": {"tr": "POPÜLER", "en": "POPULAR", "es": "POPULAR", "pt": "POPULAR"},
    "more": {"tr": "Daha fazla", "en": "Learn more", "es": "Más información", "pt": "Saiba mais"},
    "play_alt": {"tr": "Google Play'den indir", "en": "Get it on Google Play", "es": "Get it on Google Play", "pt": "Get it on Google Play"},
    "privacy": {"tr": "Gizlilik Politikası", "en": "Privacy Policy", "es": "Política de privacidad", "pt": "Política de privacidade"},
    "h_about": {"tr": "Merhaba, ben Nesim.", "en": "Hi, I'm Nesim.", "es": "Hola, soy Nesim.", "pt": "Olá, eu sou o Nesim."},
    "about": {"tr": "Android için bağımsız bir geliştiriciyim. Oyunlarımı ve uygulamalarımı tek başıma tasarlıyor, yazıyor ve yayınlıyorum. Çoğu ücretsiz ve hiçbiri hesap açmanı istemiyor. Önerin ya da bir hata bildirimin olursa yaz, hepsini okurum.",
              "en": "I'm an independent Android developer. I design, build and publish my games and apps on my own. Most are free and none of them asks you to create an account. If you have a suggestion or a bug report, write to me, I read every message.",
              "es": "Soy un desarrollador Android independiente. Diseño, programo y publico mis juegos y apps yo solo. La mayoría son gratis y ninguna te pide crear una cuenta. Si tienes una sugerencia o un error que contar, escríbeme: leo todos los mensajes.",
              "pt": "Sou um desenvolvedor Android independente. Eu mesmo projeto, programo e publico meus jogos e apps. A maioria é grátis e nenhum pede que você crie uma conta. Se tiver uma sugestão ou um erro para relatar, escreva para mim: leio todas as mensagens."},
    "email": {"tr": "E-posta gönder", "en": "Send an email", "es": "Enviar un correo", "pt": "Enviar e-mail"},
    "contact": {"tr": "İletişim", "en": "Contact", "es": "Contacto", "pt": "Contato"},
    "webprivacy": {"tr": "Site gizliliği", "en": "Website privacy", "es": "Privacidad del sitio", "pt": "Privacidade do site"},
    "allprivacy": {"tr": "Uygulama gizlilik politikaları", "en": "App privacy policies", "es": "Políticas de privacidad de las apps", "pt": "Políticas de privacidade dos apps"},
}
CARDLES = {
    "tr": "Dört klasik solitaire tek uygulamada: sevimli yüzlü kartlarla Klondike, Spider, FreeCell ve TriPeaks. Günlük meydan okuma, seriler, ipuçları ve temalar.",
    "en": "Four classic solitaire games in one app, played with cards that have cute faces: Klondike, Spider, FreeCell and TriPeaks. A daily challenge, streaks, hints and themes.",
    "es": "Cuatro solitarios clásicos en una sola app, con cartas de caritas adorables: Klondike, Spider, FreeCell y TriPeaks. Reto diario, rachas, pistas y temas.",
    "pt": "Quatro paciências clássicas em um só app, com cartas de carinhas fofas: Klondike, Spider, FreeCell e TriPeaks. Desafio diário, sequências, dicas e temas.",
}
CARDLES_TAG = {"tr": "Güldüren solitaire", "en": "Solitaire that makes you smile", "es": "El solitario que te hace sonreír", "pt": "Paciência que faz você sorrir"}
SHOW_TAG = {  # büyük oyun kartlarının kısa sloganı
    "sliplines": {"tr": "Okları doğru sırayla kaydır", "en": "Slide the arrows out in order", "es": "Saca las flechas en orden", "pt": "Deslize as setas na ordem certa"},
    "cubbles": {"tr": "Sevimli yüzlü blok bulmaca", "en": "A block puzzle with cute faces", "es": "Puzle de bloques con caritas", "pt": "Quebra-cabeça de blocos com carinhas"},
}
PLAY_DEV = "https://play.google.com/store/apps/dev?id=4632277715794688965"
SOCIAL = [("LinkedIn", "https://www.linkedin.com/in/nesimrazon/"), ("X", "https://x.com/nrazon"), ("Instagram", "https://www.instagram.com/nesimrazon/")]


def darken(hexc, f):
    r, g, b = (int(hexc[i:i + 2], 16) for i in (1, 3, 5))
    return "#%02X%02X%02X" % (int(r * f), int(g * f), int(b * f))


def play_url(pkg):
    return f"https://play.google.com/store/apps/details?id={pkg}{UTM}"


def badge(pkg):
    imgs = "".join(f'<img lang="{l}" src="badges/google-play-{"tr" if l == "tr" else "en"}.svg" alt="{esc(T["play_alt"][l])}">' for l in LANGS)
    return f'<a class="play" href="{play_url(pkg)}">{imgs}</a>'


def shots_for(slug, lang):
    ext = "jpg" if slug == "sliplines" else "png"
    return f"{slug}/shots/{lang}/%02d.{ext}"


def shot_imgs(slug, picks):
    out = []
    for n in picks:
        for l in LANGS:
            d = "en" if (slug == "cubbles" and l in ("es", "pt")) else l
            out.append(f'<img class="shot" lang="{l}" src="{shots_for(slug, d) % n}" alt="" loading="lazy" width="150" height="267">')
    return "".join(out)


def badge_new(until, key="new"):
    return f' <span class="badge" data-new-until="{until}">{L(T[key])}</span>' if until else ""


def show_card(a):
    s = a["slug"]
    pk = a["pkg"]
    picks = {"sliplines": (1, 2), "cubbles": (1, 2)}[s]
    c1, c2 = darken(a["tint"], .42), darken(a["tint"], .78)
    desc = {l: a["desc"][l] for l in LANGS}
    return f'''    <article class="show" style="--a:{c1};--b:{c2}" data-slug="{s}" data-pkg="{pk}">
      <img class="icon" src="{a["icon"]}" alt="" width="64" height="64" loading="lazy">
      <div class="txt">
        <h3><a class="stretch" href="{s}/">{esc(a["names"]["en"])}</a>{badge_new(a["new"])}</h3>
        <p class="stag">{L(SHOW_TAG[s])}</p>
        {L(desc, "p", "sdesc")}
        <div class="links">{badge(pk)}<a class="small" href="{s}/">{L(T["more"], "b")}</a></div>
      </div>
      <div class="shots" aria-hidden="true">{shot_imgs(s, picks)}</div>
    </article>'''


def tool_card(a):
    s, pk = a["slug"], a["pkg"]
    chip = f' <span class="chip pop">{L(T["popular"])}</span>' if a.get("popular") else ""
    chip += badge_new(a["new"]).replace('class="badge"', 'class="badge"') if a["new"] else ""
    return f'''      <article class="tool" style="--tint:{a["tint"]}" data-slug="{s}" data-pkg="{pk}">
        <img class="icon" src="{a["icon"]}" alt="" width="64" height="64" loading="lazy">
        <div class="tbody">
          <h3><a class="stretch" href="{s}/">{L(a["names"])}</a>{chip}</h3>
          {L(a["desc"], "p")}
          <a class="gp" href="{play_url(pk)}"><svg viewBox="0 0 24 24" width="14" height="14" aria-hidden="true"><path d="M5 3.5v17l15-8.5z" fill="currentColor"/></svg>Google Play</a>
        </div>
      </article>'''


def soon_card(a):
    s = a["slug"]
    return f'''      <article class="tool soon" style="--tint:{a["tint"]}" data-slug="{s}">
        <img class="icon" src="{a["icon"]}" alt="" width="64" height="64" loading="lazy">
        <div class="tbody">
          <h3>{esc(a["names"]["en"])} <span class="chip">{L(T["soonchip"])}</span></h3>
          {L(a["desc"], "p")}
          <a class="small" href="{s}/privacy.html#tr" lang="tr">{T["privacy"]["tr"]}</a><a class="small" href="{s}/privacy.html#en" lang="en">{T["privacy"]["en"]}</a><a class="small" href="{s}/privacy.html#en" lang="es">{T["privacy"]["es"]}</a><a class="small" href="{s}/privacy.html#en" lang="pt">{T["privacy"]["pt"]}</a>
        </div>
      </article>'''


CSS = r'''
  :root { --bg:#141829; --card:#1E2440; --text:#F3F4FA; --dim:#A9B0CF; --link:#6EA8FF; --chip:#252C4D; --shadow:0 6px 20px rgba(0,0,0,.28); --accent:#8E6CF0; --line:rgba(255,255,255,.09); }
  @media (prefers-color-scheme: light) {
    :root { --bg:#F4F5FB; --card:#FFFFFF; --text:#171A2B; --dim:#5B6280; --link:#2F5BD8; --chip:#E6E9F5; --shadow:0 6px 18px rgba(30,40,90,.12); --accent:#6A45D8; --line:rgba(23,26,43,.1); }
  }
  * { box-sizing: border-box; }
  html { scroll-behavior:smooth; scroll-padding-top:16px; }
  body { margin:0; background:var(--bg); color:var(--text); font:16px/1.6 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif; }
  main { max-width:1040px; margin:0 auto; padding:24px 16px 56px; }
  a { color:var(--link); }
  a:focus-visible, button:focus-visible { outline:3px solid var(--accent); outline-offset:2px; }
  .sr { position:absolute; width:1px; height:1px; overflow:hidden; clip:rect(0 0 0 0); white-space:nowrap; }
  /* Üst çubuk */
  .top { display:flex; flex-wrap:wrap; justify-content:space-between; align-items:center; gap:12px 16px; }
  .brand { display:flex; gap:12px; align-items:center; min-width:0; text-decoration:none; color:var(--text); }
  .logo { width:40px; height:40px; border-radius:10px; flex:none; }
  .brand b { font-size:22px; font-weight:900; letter-spacing:-.01em; }
  .topr { display:flex; flex-wrap:wrap; align-items:center; gap:4px 6px; }
  .topr nav { display:flex; gap:2px; }
  .topr nav a { color:var(--dim); text-decoration:none; font-weight:600; font-size:15px; padding:8px 12px; border-radius:999px; }
  .topr nav a:hover { color:var(--text); background:var(--chip); }
  .lang { display:flex; background:var(--card); border-radius:999px; padding:4px; flex:none; box-shadow:var(--shadow); }
  .lang button { border:0; background:none; color:var(--dim); font:inherit; font-weight:700; font-size:14px; padding:6px 14px; border-radius:999px; cursor:pointer; }
  .lang button[aria-pressed="true"] { background:var(--text); color:var(--bg); }
  /* Giriş */
  .intro { padding:36px 4px 26px; }
  .eyebrow { display:inline-block; background:var(--chip); color:var(--dim); font-weight:800; font-size:12px; letter-spacing:.09em; text-transform:uppercase; padding:6px 12px; border-radius:999px; margin:0 0 14px; }
  h1 { font-size:clamp(32px,5.6vw,56px); line-height:1.06; letter-spacing:-.02em; margin:0; font-weight:900; }
  .lead { color:var(--dim); margin:14px 0 0; font-size:18px; max-width:620px; }
  .sec { margin:44px 0 6px; font-size:clamp(24px,3.4vw,32px); letter-spacing:-.01em; line-height:1.2; }
  .sec + .sub { color:var(--dim); margin:0 0 18px; }
  /* Öne çıkan (Cardles) */
  .hero { background:var(--card); border-radius:24px; overflow:hidden; box-shadow:var(--shadow); margin:0 0 16px; }
  .hero .body { padding:20px 22px 24px; display:flex; flex-direction:column; }
  .hero p { margin:0 0 14px; color:var(--dim); }
  @media (min-width:700px) { .hero { display:grid; grid-template-columns:minmax(0,1.1fr) minmax(0,1fr); align-items:center; } .hero .body { padding:24px 28px; } }
  .hero-art { position:relative; background:linear-gradient(135deg,#0F6B52,#16A07F); color:#fff; padding:22px 18px 22px 26px; display:flex; flex-direction:column; justify-content:center; gap:6px; overflow:hidden; min-height:270px; }
  .hero-art .ha-text { display:flex; flex-direction:column; position:relative; z-index:1; }
  .hero-art .ha-title { font-size:clamp(34px,4.6vw,46px); font-weight:900; line-height:1; letter-spacing:-.02em; }
  .hero-art .ha-tag { font-weight:650; font-size:clamp(15px,2.6vw,19px); opacity:.95; margin-top:4px; }
  .hero-art svg { width:100%; max-width:420px; height:auto; overflow:visible; align-self:flex-end; margin-top:-6px; }
  @media (min-width:700px) { .hero-art svg { position:absolute; right:-6px; bottom:-6px; width:56%; max-width:none; margin:0; } .hero-art .ha-text { max-width:40%; } }
  .tag, .badge { display:inline-block; background:var(--accent); color:#fff; font-size:11px; font-weight:800; letter-spacing:.06em; padding:3px 10px; border-radius:999px; }
  .tag { align-self:flex-start; margin-bottom:8px; } .badge { margin-left:6px; position:relative; top:-2px; padding:2px 8px; }
  .chips { display:flex; flex-wrap:wrap; gap:6px; margin:0 0 14px; padding:0; list-style:none; }
  .chips li { background:var(--chip); font-size:13px; font-weight:700; padding:3px 11px; border-radius:999px; }
  .pcard { transition:transform .25s cubic-bezier(.3,1.6,.5,1); transform-box:fill-box; transform-origin:center; }
  .pcard:hover { transform:translateY(-10px); }
  .eye { transform-box:fill-box; transform-origin:center; animation:blink 6s infinite; animation-delay:var(--d,0s); }
  @keyframes blink { 0%,93%,100% { transform:scaleY(1); } 96% { transform:scaleY(.08); } }
  /* Oyun vitrini: Sliplines + Cubbles, gerçek ekran görüntüleriyle */
  .showgrid { display:grid; gap:16px; grid-template-columns:minmax(0,1fr); margin:0 0 16px; }
  @media (min-width:760px) { .showgrid { grid-template-columns:repeat(2,minmax(0,1fr)); } }
  .show { position:relative; overflow:hidden; border-radius:24px; color:#fff; padding:22px 22px 0; background:linear-gradient(150deg,var(--a),var(--b)); box-shadow:var(--shadow); display:flex; flex-direction:column; gap:10px; min-height:420px; }
  .show .icon { width:56px; height:56px; border-radius:14px; box-shadow:0 4px 12px rgba(0,0,0,.35); }
  .show h3 { margin:0; font-size:28px; line-height:1.15; font-weight:900; letter-spacing:-.01em; }
  .show h3 a { color:#fff; text-decoration:none; }
  .show .stag { margin:0; font-weight:700; opacity:.95; }
  .show .sdesc { margin:0; color:rgba(255,255,255,.82); font-size:15px; line-height:1.5; max-width:430px; }
  .show .links { margin-top:6px; position:relative; z-index:2; }
  .show .small { color:#fff; opacity:.9; }
  .show .badge { background:#fff; color:#222; }
  .shots { display:flex; justify-content:center; gap:12px; margin:14px 0 -34px; }
  .shot { width:min(42%,150px); height:auto; border-radius:18px; border:3px solid rgba(255,255,255,.2); box-shadow:0 12px 28px rgba(0,0,0,.4); background:#000; }
  .shot:nth-child(odd) { transform:rotate(-3deg) translateY(6px); } .shot:nth-child(even) { transform:rotate(3deg); }
  @media (min-width:520px) { .show .txt { padding-right:4%; } }
  /* Kompakt kartlar (araçlar ve klasik oyunlar) */
  .tools { display:grid; gap:12px; grid-template-columns:repeat(auto-fill,minmax(min(100%,300px),1fr)); }
  @media (min-width:760px) { .tools.two { grid-template-columns:repeat(2,minmax(0,1fr)); } }
  .tool { position:relative; display:flex; gap:14px; align-items:flex-start; background:linear-gradient(165deg,color-mix(in srgb,var(--tint,var(--card)) 14%,var(--card)) 0%,var(--card) 62%); border-radius:18px; padding:14px 16px; box-shadow:var(--shadow); transition:transform .15s ease; }
  .tool:hover { transform:translateY(-2px); }
  .tool .icon { width:56px; height:56px; border-radius:14px; flex:none; box-shadow:0 3px 10px rgba(0,0,0,.25); }
  .tbody { min-width:0; flex:1; }
  .tool h3 { margin:0 0 2px; font-size:17px; line-height:1.3; }
  .stretch { color:var(--text); text-decoration:none; }
  .stretch::after { content:""; position:absolute; inset:0; border-radius:18px; }
  .show .stretch::after { border-radius:24px; z-index:1; }
  .tool p { margin:0 0 8px; color:var(--dim); font-size:14px; line-height:1.45; display:-webkit-box; -webkit-line-clamp:3; -webkit-box-orient:vertical; overflow:hidden; }
  .chip { display:inline-block; vertical-align:middle; background:var(--chip); color:var(--dim); font-size:10.5px; font-weight:800; letter-spacing:.06em; padding:2px 8px; border-radius:999px; margin-left:4px; position:relative; top:-1px; }
  .chip.pop { background:var(--accent); color:#fff; }
  .gp { position:relative; z-index:2; display:inline-flex; align-items:center; gap:6px; font-size:13px; font-weight:700; color:var(--link); text-decoration:none; padding:5px 11px; border:1.5px solid var(--line); border-radius:999px; }
  .gp:hover { background:var(--chip); }
  .tool.soon { border:1.5px dashed var(--line); box-shadow:none; background:transparent; }
  .tool.soon:hover { transform:none; }
  .tool.soon .small { margin-right:10px; position:relative; z-index:2; }
  .links { display:flex; flex-wrap:wrap; gap:8px 14px; align-items:center; }
  .play img { height:44px; width:auto; display:block; }
  .small { color:var(--link); font-size:14px; }
  /* Hakkımda */
  .about { margin-top:48px; display:flex; flex-wrap:wrap; gap:22px 28px; align-items:center; background:var(--card); border-radius:24px; padding:26px; box-shadow:var(--shadow); }
  .about img { width:96px; height:96px; border-radius:50%; flex:none; object-fit:cover; box-shadow:0 4px 14px rgba(0,0,0,.3); }
  .about .abody { flex:1 1 320px; min-width:0; }
  .about h2 { margin:0 0 8px; font-size:26px; line-height:1.2; }
  .about p { margin:0 0 16px; color:var(--dim); }
  .contacts { display:flex; flex-wrap:wrap; gap:8px; }
  .contacts a { display:inline-block; text-decoration:none; font-weight:700; font-size:14px; padding:9px 16px; border-radius:999px; background:var(--chip); color:var(--text); }
  .contacts a.main { background:var(--accent); color:#fff; }
  .contacts a:hover { filter:brightness(1.1); }
  /* Alt bilgi */
  footer { color:var(--dim); font-size:14px; margin-top:36px; }
  footer .row { display:flex; flex-wrap:wrap; gap:6px 14px; align-items:center; }
  footer details { margin-top:12px; }
  footer summary { cursor:pointer; font-weight:600; }
  footer ul { list-style:none; padding:0; margin:10px 0 0; display:grid; gap:4px 18px; grid-template-columns:repeat(auto-fill,minmax(220px,1fr)); }
  /* Dil: <html class="tr"> ya da "en"; diğer dildeki metinler gizlenir. */
  html.tr [lang]:not([lang="tr"]):not(html), html.en [lang]:not([lang="en"]):not(html), html.es [lang]:not([lang="es"]):not(html), html.pt [lang]:not([lang="pt"]):not(html) { display:none; }
  [hidden] { display:none !important; }
  @media (prefers-reduced-motion: reduce) { html { scroll-behavior:auto; } .eye { animation:none; } .pcard, .tool { transition:none; } .tool:hover { transform:none; } }
  @media (max-width:560px) { .intro { padding-top:24px; } .about { padding:20px; } .topr nav a { padding:8px 9px; font-size:14px; } }
'''

JS = r'''
  // Seçim kaydedildiyse o, yoksa tarayıcının dili (Türkçe değilse İngilizce).
  (function () {
    var lang;
    try { lang = localStorage.getItem("lang"); } catch (e) {}
    if (["tr", "en", "es", "pt"].indexOf(lang) < 0) { var n = (navigator.language || "en").toLowerCase().slice(0, 2); lang = ["tr", "es", "pt"].indexOf(n) >= 0 ? n : "en"; }
    document.documentElement.className = lang;
    document.documentElement.lang = lang;
  })();
  function setLang(lang) {
    document.documentElement.className = lang;
    document.documentElement.lang = lang;
    try { localStorage.setItem("lang", lang); } catch (e) {}
    document.querySelectorAll(".lang button").forEach(function (b) { b.setAttribute("aria-pressed", b.dataset.lang === lang); });
  }
  // "Yeni" rozetleri tarihi geçince kendiliğinden kalkar (data-new-until: yyyy-mm-dd).
  function expireBadges() {
    var today = new Date().toISOString().slice(0, 10);
    document.querySelectorAll("[data-new-until]").forEach(function (el) { if (today > el.dataset.newUntil) el.remove(); });
  }
'''


def build(preview):
    by = {a["slug"]: a for a in DATA}
    live = [a for a in DATA if a["status"] == "live"]
    soon = [a for a in DATA if a["status"] == "soon"]
    games = [a for a in live if a["cat"] == "games" and a["slug"] not in ("cardles", "sliplines", "cubbles")]
    apps = [a for a in live if a["cat"] == "apps"]
    cardles = by["cardles"]
    robots = '<meta name="robots" content="noindex">\n' if preview else ""
    privacy_links = "".join(
        f'<li><a href="{a["slug"]}/privacy.html">{esc(a["names"]["en"])}</a></li>' for a in DATA)
    hero = f'''  <section class="hero" data-slug="cardles" data-pkg="com.cardles.nesimapps">
    <h2 class="sr">Cardles</h2>
    <div class="hero-art">
      <div class="ha-text">
        <span class="ha-title">Cardles</span>
        <span class="ha-tag">{L(CARDLES_TAG)}</span>
      </div>
      {HERO_SVG}
    </div>
    <div class="body">
      <span class="tag" data-new-until="{cardles["new"]}">{L(T["newgame"])}</span>
      {L(CARDLES, "p")}
      <ul class="chips"><li>Klondike</li><li>Spider</li><li>FreeCell</li><li>TriPeaks</li></ul>
      <div class="links">{badge("com.cardles.nesimapps")}<a class="small" href="cardles/">{L(T["more"], "b")}</a></div>
    </div>
  </section>'''
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nesim Apps</title>
{robots}<meta name="description" content="Android games and apps by Nesim Razon: Cardles, Cubbles, Sliplines, 2048, Tic-Tac-Toe, Son Depremler, Age Calculator, BMI Calculator, Where Am I?, National Anthems and more. Android oyunları ve uygulamaları.">
<link rel="canonical" href="https://nrazon.github.io/">
<link rel="icon" href="logo.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<meta name="theme-color" content="#141829" media="(prefers-color-scheme: dark)">
<meta name="theme-color" content="#F4F5FB" media="(prefers-color-scheme: light)">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Nesim Apps">
<meta property="og:title" content="Nesim Apps">
<meta property="og:description" content="Android games and apps by Nesim Razon. Android oyunları ve uygulamaları.">
<meta property="og:url" content="https://nrazon.github.io/">
<meta property="og:image" content="https://nrazon.github.io/og-v3.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<style>{CSS}</style>
<script src="/analytics.js?v=1" defer></script>
<script>{JS}</script>
</head>
<body>
<main>
  <div class="top">
    <a class="brand" href="#top"><img class="logo" src="logo.svg" alt="" width="40" height="40"><b>Nesim Apps</b></a>
    <div class="topr">
      <nav aria-label="Menu"><a href="#games">{L(T["nav_games"])}</a><a href="#apps">{L(T["nav_apps"])}</a><a href="#about">{L(T["nav_about"])}</a></nav>
      <div class="lang" role="group" aria-label="Language / Dil">
        <button type="button" data-lang="tr" onclick="setLang('tr')">TR</button>
        <button type="button" data-lang="en" onclick="setLang('en')">EN</button>
        <button type="button" data-lang="es" onclick="setLang('es')">ES</button>
        <button type="button" data-lang="pt" onclick="setLang('pt')">PT</button>
      </div>
    </div>
  </div>

  <div class="intro" id="top">
    <p class="eyebrow">{L(T["eyebrow"])}</p>
    <h1>{L(T["tagline"], "span")}</h1>
    <p class="lead">{L(T["lead"])}</p>
  </div>

  <section id="games">
{hero}
    <div class="showgrid">
{show_card(by["sliplines"])}
{show_card(by["cubbles"])}
    </div>
    <div class="tools two">
{chr(10).join(tool_card(a) for a in games)}
    </div>
  </section>

  <section id="apps">
    <h2 class="sec">{L(T["h_apps"])}</h2>
    <p class="sub">{L(T["h_apps_sub"])}</p>
    <div class="tools">
{chr(10).join(tool_card(a) for a in apps)}
    </div>
  </section>

  <section id="soon">
    <h2 class="sec">{L(T["h_soon"])}</h2>
    <div class="tools two" style="margin-top:14px">
{chr(10).join(soon_card(a) for a in soon)}
    </div>
  </section>

  <section class="about" id="about">
    <img src="nesim.jpg" alt="Nesim Razon" width="96" height="96">
    <div class="abody">
      <h2>{L(T["h_about"])}</h2>
      {L(T["about"], "p")}
      <div class="contacts">
        <a class="main" href="mailto:nesim.razon@gmail.com">{L(T["email"])}</a>
        <a href="{PLAY_DEV}" rel="noopener">Google Play</a>
        {"".join(f'<a href="{u}" rel="me noopener">{n}</a>' for n, u in SOCIAL)}
      </div>
    </div>
  </section>

  <footer>
    <div class="row"><span>© 2026 Nesim Razon</span><span>·</span><a href="mailto:nesim.razon@gmail.com">nesim.razon@gmail.com</a><span>·</span><a href="/site-privacy.html">{L(T["webprivacy"])}</a></div>
    <details><summary>{L(T["allprivacy"])}</summary><ul>{privacy_links}</ul></details>
  </footer>
</main>
<script src="eyes.js"></script>
<script>
  setLang(document.documentElement.className);
  expireBadges();
</script>
</body>
</html>
'''


if __name__ == "__main__":
    yayin = "--yayin" in sys.argv
    out = os.path.join(G, "index.html" if yayin else "yeni.html")
    open(out, "w", encoding="utf-8", newline="\n").write(build(preview=not yayin))
    print("yazıldı:", out)
