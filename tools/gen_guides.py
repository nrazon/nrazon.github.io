# "Nasıl oynanır" rehber sayfaları üretici (5.11.2026, site SEO Faz 2C).
# Veri: tools/guides/*.py (her dosya bir rehber, 4 dil). Çıktı (dil başına ayrı adres):
#   EN /guides/<slug>/   TR /tr/rehber/<slug>/   ES /es/guias/<slug>/   PT /pt/guias/<slug>/   (+ her dilde dizin sayfası)
# Yan ürün: tools/_guides_pages.json (i18n_split.py: oyun detay sayfalarına rehber bağlantısı + sitemap), guides.css.
# Kullanım: py -3 tools/gen_guides.py   (build_site.py çağırır). Yeni rehber = tools/guides/ içine dosya + GUIDE_MODULES listesine ekle.
import hashlib
import html as H
import importlib.util
import json
import os
import re

TOOLS = os.path.dirname(os.path.abspath(__file__))
G = os.path.dirname(TOOLS)
BASE = "https://nrazon.github.io"
LANGS = ["en", "tr", "es", "pt"]
DIRS = {"en": "guides", "tr": "tr/rehber", "es": "es/guias", "pt": "pt/guias"}
HREFLANG = {"en": "en", "tr": "tr", "es": "es", "pt": "pt"}
OGLOC = {"en": "en_US", "tr": "tr_TR", "es": "es_ES", "pt": "pt_BR"}
GUIDE_MODULES = ["mahjong", "solitaire", "blocks", "beamies", "arrows", "logic", "lights", "peg", "g2048", "tictactoe", "maze",
                "freecell", "spider", "tripeaks", "shisen", "mahjong_stuck", "nudge_slide", "nudge_push", "g2048_beyond", "blocks_advanced",
                "mahjong_tiles", "solitaire_types", "pento", "pento_drop"]  # Pentolings rehberleri ("pento", "pento_drop") yayin gunu eklenir  # "maze" (Grumblings): yayin gunu eklenir (tools/guides/maze.py hazir)
SOCIAL = ["https://x.com/nrazon", "https://www.linkedin.com/in/nesimrazon/", "https://play.google.com/store/apps/dev?id=4632277715794688965"]

T = {
    "en": {"back": "← Nesim Apps", "idx_title": "How-to-play guides: rules, tips and strategy", "idx_h1": "How-to-play guides", "idx_desc": "Rules, tips and strategy for Mahjong Solitaire, Klondike, block puzzles, arrow puzzles, logic puzzles, 2048 and Tic-Tac-Toe.",
           "idx_intro": "Short, practical guides to the games in our apps: how they work, how to win more often and where to try them for free.", "cta": "Try it free: {name}", "cta_sub": "Free on Google Play. No account needed.", "about": "About {name}",
           "faq": "Frequently asked questions", "more": "More guides", "by": "By Nesim Razon, independent Android developer", "home": "Nesim Apps", "crumb": "Guides", "read": "Read the guide"},
    "tr": {"back": "← Nesim Apps", "idx_title": "Nasıl oynanır rehberleri: kurallar, ipuçları ve strateji", "idx_h1": "Nasıl oynanır rehberleri", "idx_desc": "Mahjong Solitaire, Klondike, blok bulmaca, ok bulmacası, mantık bulmacaları, 2048 ve XOX için kurallar, ipuçları ve strateji.",
           "idx_intro": "Uygulamalarımızdaki oyunlar için kısa ve pratik rehberler: nasıl çalıştıkları, daha sık nasıl kazanılacağı ve ücretsiz nereden deneneceği.", "cta": "Ücretsiz dene: {name}", "cta_sub": "Google Play'de ücretsiz. Hesap gerekmez.", "about": "{name} hakkında",
           "faq": "Sık sorulan sorular", "more": "Diğer rehberler", "by": "Nesim Razon, bağımsız Android geliştiricisi", "home": "Nesim Apps", "crumb": "Rehberler", "read": "Rehberi oku"},
    "es": {"back": "← Nesim Apps", "idx_title": "Guías de cómo jugar: reglas, consejos y estrategia", "idx_h1": "Guías de cómo jugar", "idx_desc": "Reglas, consejos y estrategia para Mahjong Solitario, Klondike, puzles de bloques, puzles de flechas, puzles de lógica, 2048 y tres en raya.",
           "idx_intro": "Guías breves y prácticas de los juegos de nuestras apps: cómo funcionan, cómo ganar más a menudo y dónde probarlos gratis.", "cta": "Pruébalo gratis: {name}", "cta_sub": "Gratis en Google Play. Sin cuenta.", "about": "Sobre {name}",
           "faq": "Preguntas frecuentes", "more": "Más guías", "by": "Por Nesim Razon, desarrollador Android independiente", "home": "Nesim Apps", "crumb": "Guías", "read": "Leer la guía"},
    "pt": {"back": "← Nesim Apps", "idx_title": "Guias de como jogar: regras, dicas e estratégia", "idx_h1": "Guias de como jogar", "idx_desc": "Regras, dicas e estratégia para Mahjong Paciência, Klondike, quebra-cabeças de blocos, de setas, de lógica, 2048 e jogo da velha.",
           "idx_intro": "Guias curtos e práticos dos jogos dos nossos apps: como funcionam, como vencer mais vezes e onde experimentar de graça.", "cta": "Experimente grátis: {name}", "cta_sub": "Grátis no Google Play. Sem conta.", "about": "Sobre {name}",
           "faq": "Perguntas frequentes", "more": "Mais guias", "by": "Por Nesim Razon, desenvolvedor Android independente", "home": "Nesim Apps", "crumb": "Guias", "read": "Ler o guia"},
}
LABEL = {"en": "EN", "tr": "TR", "es": "ES", "pt": "PT"}

CSS = """/* Rehber sayfaları (gen_guides.py üretir). landing.css üstüne eklenir. */
.guide { max-width:760px; margin:0 auto; }
.guide h1 { font-size:clamp(28px,5.4vw,42px); line-height:1.12; letter-spacing:-.01em; margin:6px 0 10px; }
.guide .by { color:var(--dim); font-size:14px; margin:0 0 18px; }
.guide .lead { font-size:18px; color:var(--text); margin:0 0 26px; }
.guide h2 { font-size:22px; line-height:1.25; margin:34px 0 10px; }
.guide p { margin:0 0 14px; }
.guide ul { margin:0 0 16px; padding-left:22px; }
.guide li { margin:0 0 8px; }
.gcta { display:flex; align-items:center; gap:16px; flex-wrap:wrap; background:var(--card); border-radius:20px; padding:18px 20px; margin:30px 0; box-shadow:var(--shadow); border-left:6px solid var(--accent,#7FB2FF); }
.gcta img.ic { width:64px; height:64px; border-radius:16px; }
.gcta .tx { flex:1 1 220px; }
.gcta .tx b { display:block; font-size:18px; }
.gcta .tx span { color:var(--dim); font-size:14px; }
.gcta .play img { height:46px; width:auto; display:block; }
.gcta a.small { font-size:14px; }
.guide .glist { padding-left:0; }
.glist { display:grid; grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr)); gap:14px; list-style:none; margin:20px 0 0; padding:0; }
.glist li { margin:0; }
.glist a { display:flex; gap:14px; align-items:flex-start; background:var(--card); color:var(--text); text-decoration:none; padding:16px; border-radius:18px; box-shadow:var(--shadow); height:100%; }
.glist a:hover { outline:2px solid var(--accent,#7FB2FF); }
.glist img { width:48px; height:48px; border-radius:12px; flex:none; }
.glist b { display:block; font-size:17px; line-height:1.3; }
.glist span { color:var(--dim); font-size:14px; line-height:1.5; }
.guide .faq { margin-top:30px; }
nav.crumbs { font-size:14px; color:var(--dim); margin:0 0 6px; }
nav.crumbs a { color:var(--dim); }
"""


def load_guides():
    out = []
    for m in GUIDE_MODULES:
        spec = importlib.util.spec_from_file_location("guide_" + m, os.path.join(TOOLS, "guides", m + ".py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.GUIDE)
    return out


def url(lang, slug=""):
    return f"{BASE}/{DIRS[lang]}/" + (f"{slug}/" if slug else "")


def app_url(app, lang):
    return f"/{app}/" if lang == "en" else f"/{lang}/{app}/"


def esc(s):
    return H.escape(s, quote=True)


def head(lang, title, desc, canon, alternates, og_image, ld, accent):
    alts = "".join(f'<link rel="alternate" hreflang="{HREFLANG[l]}" href="{u}">\n' for l, u in alternates.items())
    xdef = f'<link rel="alternate" hreflang="x-default" href="{alternates["en"]}">\n'
    ogalt = "".join(f'<meta property="og:locale:alternate" content="{OGLOC[l]}">\n' for l in alternates if l != lang)
    # <title>: en çok ~60 karakter (Google keser). Uzunsa ilk bölümde (":" "?" "(" öncesi) kes; marka sığarsa ekle. Sayfadaki h1 tam kalır.
    st = title
    if len(st) > 60:
        m = re.search(r"[:?(]", st)
        if m and m.start() >= 14:
            st = st[:m.start()].rstrip() + ("?" if st[m.start()] == "?" else "")
    short = st if len(st) + 14 > 60 else f"{st} | Nesim Apps"
    if len(desc) > 158:
        cut = desc[:158]
        q = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
        desc = cut[:q + 1] if q > 100 else cut[:cut.rfind(" ")].rstrip(",;:") + "…"
    return f"""<!doctype html>
<html lang="{lang}" data-lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(short)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
{alts}{xdef}<link rel="icon" href="/logo.svg" type="image/svg+xml">
<meta name="theme-color" content="{accent}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Nesim Apps">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{OGLOC[lang]}">
{ogalt}<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<style>:root {{ --accent:{accent}; }}</style>
<link rel="stylesheet" href="/landing.css?v=7">
<link rel="stylesheet" href="/guides.css?v=1">
<script src="/analytics.js?v=5" defer></script>
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
</head>
"""


def switcher(lang, alternates):
    links = "".join(
        f'<a href="{u.replace(BASE, "")}" hreflang="{HREFLANG[l]}" data-lang="{l}"' + (' aria-current="page"' if l == lang else "") + f">{LABEL[l]}</a>"
        for l, u in alternates.items())
    return f'<div class="lang" role="navigation" aria-label="Language">{links}</div>'


def home_url(lang):
    return "/" if lang == "en" else f"/{lang}/"


LANGJS = "(function(){[].forEach.call(document.querySelectorAll('.lang a'),function(a){a.addEventListener('click',function(){try{localStorage.setItem('lang_hint','0')}catch(e){}})})})();"


def page_shell(lang, alternates, body):
    t = T[lang]
    return f"""<body>
<main>
  <header class="top">
    <a class="back" href="/">{t['back']}</a>
    {switcher(lang, alternates)}
  </header>
{body}
  <footer><a href="mailto:nesim.razon@gmail.com">nesim.razon@gmail.com</a> · <a href="/site-privacy.html">Privacy</a></footer>
</main>
<script>{LANGJS}</script>
</body>
</html>
"""


def main():
    guides = load_guides()
    home = {a["slug"]: a for a in json.load(open(os.path.join(TOOLS, "home_data.json"), encoding="utf-8"))}
    pages = []
    by_app = {}
    index_urls = {l: "/" + DIRS[l] + "/" for l in LANGS}

    def write(path, content):
        full = os.path.join(G, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8", newline="\n").write(content)

    open(os.path.join(G, "guides.css"), "w", encoding="utf-8", newline="\n").write(CSS)

    for g in guides:
        app = home[g["app"]]
        name = app["names"]["en"]
        accent = app.get("tint", "#7FB2FF")
        by_app.setdefault(g["app"], {})
        alternates = {l: url(l, g[l]["slug"]) for l in LANGS}
        for lang in LANGS:
            c = g[lang]
            t = T[lang]
            canon = alternates[lang]
            feat = os.path.join(G, g["app"], f"feature-{lang}.png")
            og_image = f"{BASE}/{g['app']}/feature-{lang}.png" if os.path.exists(feat) else f"{BASE}/og-v3.png"
            others = [x for x in guides if x["id"] != g["id"]]
            others = sorted(others, key=lambda x: (x["app"] != g["app"]))[:8]  # aynı uygulamanın rehberleri önde, en çok 8
            faq_ld = {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faq"]]}
            art_ld = {"@type": "Article", "headline": c["title"], "description": c["desc"], "inLanguage": lang, "mainEntityOfPage": canon, "image": og_image,
                      "datePublished": g["date"], "dateModified": g["date"],
                      "author": {"@type": "Person", "name": "Nesim Razon", "url": BASE + "/", "sameAs": SOCIAL},
                      "publisher": {"@type": "Person", "name": "Nesim Razon", "url": BASE + "/"},
                      "about": {"@type": "SoftwareApplication", "name": name, "operatingSystem": "Android", "applicationCategory": "GameApplication", "url": BASE + app_url(g["app"], lang)}}
            crumbs_ld = {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": BASE + home_url(lang)},
                {"@type": "ListItem", "position": 2, "name": t["crumb"], "item": url(lang)},
                {"@type": "ListItem", "position": 3, "name": c["title"], "item": canon}]}
            ld = {"@context": "https://schema.org", "@graph": [art_ld, faq_ld, crumbs_ld]}
            sec = []
            for s in c["sections"]:
                sec.append(f'<h2>{esc(s["h"])}</h2>')
                for p in s.get("p", []):
                    sec.append(f"<p>{esc(p)}</p>")
                if s.get("ul"):
                    sec.append("<ul>" + "".join(f"<li>{esc(i)}</li>" for i in s["ul"]) + "</ul>")
                for p in s.get("p2", []):
                    sec.append(f"<p>{esc(p)}</p>")
            play = f"https://play.google.com/store/apps/details?id={app['pkg']}&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dguide%26utm_campaign%3D{g['id']}"
            badge = "tr" if lang == "tr" else "en"
            icon = "/" + app["icon"]
            cta = (f'<aside class="gcta"><img class="ic" src="{icon}" alt="{esc(name)} icon" width="64" height="64">'
                   f'<div class="tx"><b>{esc(t["cta"].format(name=name))}</b><span>{esc(t["cta_sub"])}</span></div>'
                   f'<a class="play" href="{esc(play)}"><img src="/badges/google-play-{badge}.svg" alt="Google Play" width="162" height="48"></a>'
                   f'<a class="small" href="{app_url(g["app"], lang)}">{esc(t["about"].format(name=name))}</a></aside>')
            faq = '<section class="faq"><h2>' + esc(t["faq"]) + "</h2>" + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in c["faq"]) + "</section>"
            more = ('<section><h2>' + esc(t["more"]) + '</h2><ul class="glist">' + "".join(
                f'<li><a href="/{DIRS[lang]}/{o[lang]["slug"]}/"><img src="/{home[o["app"]]["icon"]}" alt="" width="48" height="48"><div><b>{esc(o[lang]["title"])}</b></div></a></li>' for o in others) + "</ul></section>")
            body = (f'  <article class="guide">\n    <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{esc(t["home"])}</a> › <a href="{index_urls[lang]}">{esc(t["crumb"])}</a></nav>\n'
                    f'    <h1>{esc(c["title"])}</h1>\n    <p class="by">{esc(t["by"])}</p>\n    <p class="lead">{esc(c["intro"])}</p>\n    ' + "\n    ".join(sec) + f"\n    {cta}\n    {faq}\n    {more}\n  </article>")
            out = head(lang, c["title"], c["desc"], canon, alternates, og_image, ld, accent) + page_shell(lang, alternates, body)
            write(f"{DIRS[lang]}/{c['slug']}/index.html", out)
            by_app[g["app"]].setdefault(lang, f"/{DIRS[lang]}/{c['slug']}/")  # uygulama sayfasına ilk rehber bağlanır
            pages.append({"url": canon, "loc": alternates, "default": "en", "hash": hashlib.md5(out.encode("utf-8")).hexdigest()})

    # dizin sayfaları
    alternates = {l: url(l) for l in LANGS}
    for lang in LANGS:
        t = T[lang]
        canon = alternates[lang]
        items = "".join(
            f'<li><a href="/{DIRS[lang]}/{g[lang]["slug"]}/"><img src="/{home[g["app"]]["icon"]}" alt="" width="48" height="48"><div><b>{esc(g[lang]["title"])}</b><span>{esc(g[lang]["desc"])}</span></div></a></li>' for g in guides)
        list_ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": t["idx_h1"], "inLanguage": lang, "url": canon, "description": t["idx_desc"],
                   "mainEntity": {"@type": "ItemList", "itemListElement": [{"@type": "ListItem", "position": i + 1, "url": url(lang, g[lang]["slug"]), "name": g[lang]["title"]} for i, g in enumerate(guides)]}}
        body = (f'  <article class="guide">\n    <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{esc(t["home"])}</a> › {esc(t["crumb"])}</nav>\n'
                f'    <h1>{esc(t["idx_h1"])}</h1>\n    <p class="lead">{esc(t["idx_intro"])}</p>\n    <ul class="glist">{items}</ul>\n  </article>')
        out = head(lang, t["idx_title"], t["idx_desc"], canon, alternates, f"{BASE}/og-v3.png", list_ld, "#7FB2FF").replace('content="article"', 'content="website"') + page_shell(lang, alternates, body)
        write(f"{DIRS[lang]}/index.html", out)
        pages.append({"url": canon, "loc": alternates, "default": "en", "hash": hashlib.md5(out.encode("utf-8")).hexdigest()})

    json.dump({"by_app": by_app, "pages": pages, "index": index_urls}, open(os.path.join(TOOLS, "_guides_pages.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"gen_guides: {len(guides)} rehber x {len(LANGS)} dil + dizinler")


if __name__ == "__main__":
    main()
