# -*- coding: utf-8 -*-
# Blog / "Yazılar" üreticisi: tools/blog/*.py (POST sözlüğü, rehberlerle aynı biçim, app None olabilir, faq isteğe bağlı).
# Kullanım: py -3 tools/gen_blog.py (build_site.py gen_guides'tan sonra çağırır). Yeni yazı = tools/blog/ içine dosya + BLOG_MODULES listesine ekle.
import hashlib
import importlib.util
import json
import os

TOOLS = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("gen_guides", os.path.join(TOOLS, "gen_guides.py"))
GG = importlib.util.module_from_spec(_s)
_s.loader.exec_module(GG)

G, BASE, LANGS, esc, head, page_shell, home_url, app_url = GG.G, GG.BASE, GG.LANGS, GG.esc, GG.head, GG.page_shell, GG.home_url, GG.app_url
T = GG.T
DIRS = {"en": "blog", "tr": "tr/yazilar", "es": "es/blog", "pt": "pt/blog"}
# Yayın günü eklenenler (Pentolings yayına çıkınca): "pento_history", "pento_dlx"
BLOG_MODULES = ["mahjong_solvable", "mahjong_history", "daily_seed", "generated_levels", "ttt_history",
                "deprem_buyukluk", "deprem_oncesi_sonrasi", "deprem_veri_kaynaklari", "bmi_nedir", "bmi_hatalar", "yas_hesaplama", "artik_yil_dogum_gunu", "pento_history", "pento_dlx", "tombala_cards",
                "merkur_retrosu", "burclar_takimyildiz", "ay_evreleri"]  # son 3: yalnız Türkçe (Astrolings)

BT = {
    "en": {"idx_title": "Blog: puzzle design, game history and dev notes", "idx_h1": "Blog", "idx_desc": "Notes from an independent Android developer: how puzzles are generated and checked, the history of classic puzzle games and behind-the-scenes dev stories.",
           "idx_intro": "Notes from behind the scenes: how our puzzle games are built, where classic puzzles come from and what we learn while making them.", "crumb": "Blog", "more": "More from the blog", "read": "Read"},
    "tr": {"idx_title": "Yazılar: bulmaca tasarımı, oyun tarihi ve geliştirici notları", "idx_h1": "Yazılar", "idx_desc": "Bağımsız bir Android geliştiricisinden notlar: bulmacalar nasıl üretilip doğrulanır, klasik bulmaca oyunlarının tarihi ve perde arkası hikâyeleri.",
           "idx_intro": "Perde arkasından notlar: bulmaca oyunlarımız nasıl yapılıyor, klasik bulmacalar nereden geliyor ve yaparken neler öğreniyoruz.", "crumb": "Yazılar", "more": "Diğer yazılar", "read": "Oku"},
    "es": {"idx_title": "Blog: diseño de puzles, historia de juegos y notas de desarrollo", "idx_h1": "Blog", "idx_desc": "Notas de un desarrollador Android independiente: cómo se generan y comprueban los puzles, la historia de los juegos clásicos y anécdotas del desarrollo.",
           "idx_intro": "Notas entre bastidores: cómo se construyen nuestros juegos de puzles, de dónde vienen los puzles clásicos y qué aprendemos al hacerlos.", "crumb": "Blog", "more": "Más del blog", "read": "Leer"},
    "pt": {"idx_title": "Blog: design de quebra-cabeças, história dos jogos e notas de desenvolvimento", "idx_h1": "Blog", "idx_desc": "Notas de um desenvolvedor Android independente: como os quebra-cabeças são gerados e verificados, a história dos jogos clássicos e bastidores do desenvolvimento.",
           "idx_intro": "Notas dos bastidores: como nossos jogos de quebra-cabeça são feitos, de onde vêm os quebra-cabeças clássicos e o que aprendemos ao criá-los.", "crumb": "Blog", "more": "Mais do blog", "read": "Ler"},
}


def url(lang, slug=""):
    return f"{BASE}/{DIRS[lang]}/" + (f"{slug}/" if slug else "")


def load_posts():
    out = []
    for m in BLOG_MODULES:
        spec = importlib.util.spec_from_file_location("post_" + m, os.path.join(TOOLS, "blog", m + ".py"))
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        out.append(mod.POST)
    return out


def main():
    posts = load_posts()
    home = {a["slug"]: a for a in json.load(open(os.path.join(TOOLS, "home_data.json"), encoding="utf-8"))}
    pages = []
    index_urls = {l: "/" + DIRS[l] + "/" for l in LANGS}

    def write(path, content):
        full = os.path.join(G, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        open(full, "w", encoding="utf-8", newline="\n").write(content)

    def icon_of(q):
        return home[q["app"]]["icon"] if q.get("app") else "logo.svg"

    def alt_of(q):
        return esc(home[q["app"]]["names"]["en"] + " icon") if q.get("app") else "Nesim Apps"

    for p in posts:
        app = home.get(p.get("app")) if p.get("app") else None
        accent = app.get("tint", "#7FB2FF") if app else "#7FB2FF"
        plangs = [l for l in LANGS if l in p]  # yalnız Türkçe yazılar olabilir
        alternates = {l: url(l, p[l]["slug"]) for l in plangs}
        for lang in plangs:
            c, t, b = p[lang], T[lang], BT[lang]
            canon = alternates[lang]
            feat = os.path.join(G, p["app"], f"feature-{lang}.png") if app else ""
            og_image = f"{BASE}/{p['app']}/feature-{lang}.png" if app and os.path.exists(feat) else f"{BASE}/og-v3.png"
            art = {"@type": "BlogPosting", "headline": c["title"], "description": c["desc"], "inLanguage": lang, "mainEntityOfPage": canon, "image": og_image,
                   "datePublished": p["date"], "dateModified": p["date"],
                   "author": {"@type": "Person", "name": "Nesim Razon", "url": BASE + "/", "sameAs": GG.SOCIAL},
                   "publisher": {"@type": "Person", "name": "Nesim Razon", "url": BASE + "/"}}
            if app:
                art["about"] = {"@type": "SoftwareApplication", "name": app["names"]["en"], "operatingSystem": "Android", "applicationCategory": "GameApplication", "url": BASE + app_url(p["app"], lang)}
            crumbs = {"@type": "BreadcrumbList", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": t["home"], "item": BASE + home_url(lang)},
                {"@type": "ListItem", "position": 2, "name": b["crumb"], "item": url(lang)},
                {"@type": "ListItem", "position": 3, "name": c["title"], "item": canon}]}
            graph = [art, crumbs]
            faq = c.get("faq") or []
            if faq:
                graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]})
            ld = {"@context": "https://schema.org", "@graph": graph}
            sec = []
            for s in c["sections"]:
                sec.append(f'<h2>{esc(s["h"])}</h2>')
                for x in s.get("p", []):
                    sec.append(f"<p>{esc(x)}</p>")
                if s.get("ul"):
                    sec.append("<ul>" + "".join(f"<li>{esc(i)}</li>" for i in s["ul"]) + "</ul>")
                for x in s.get("p2", []):
                    sec.append(f"<p>{esc(x)}</p>")
            cta = ""
            if app:
                name = app["names"]["en"]
                play = f"https://play.google.com/store/apps/details?id={app['pkg']}&referrer=utm_source%3Dnrazon.github.io%26utm_medium%3Dblog%26utm_campaign%3D{p['id']}"
                badge = "tr" if lang == "tr" else "en"
                cta = (f'<aside class="gcta"><img class="ic" src="/{app["icon"]}" alt="{esc(name)} icon" width="64" height="64">'
                       f'<div class="tx"><b>{esc(t["cta"].format(name=name))}</b><span>{esc(t["cta_sub"])}</span></div>'
                       f'<a class="play" href="{esc(play)}"><img src="/badges/google-play-{badge}.svg" alt="Google Play" width="162" height="48"></a>'
                       f'<a class="small" href="{app_url(p["app"], lang)}">{esc(t["about"].format(name=name))}</a></aside>')
            faqh = ('<section class="faq"><h2>' + esc(t["faq"]) + "</h2>" + "".join(f"<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>" for q, a in faq) + "</section>") if faq else ""
            others = sorted([x for x in posts if x["id"] != p["id"] and lang in x], key=lambda x: (x.get("app") != p.get("app")))[:6]  # aynı uygulamanınkiler önde, en çok 6
            more = ""
            if others:
                more = ('<section><h2>' + esc(b["more"]) + '</h2><ul class="glist">' + "".join(
                    f'<li><a href="/{DIRS[lang]}/{o[lang]["slug"]}/"><img src="/{icon_of(o)}" alt="{alt_of(o)}" width="48" height="48"><div><b>{esc(o[lang]["title"])}</b></div></a></li>' for o in others) + "</ul></section>")
            body = (f'  <article class="guide">\n    <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{esc(t["home"])}</a> › <a href="{index_urls[lang]}">{esc(b["crumb"])}</a></nav>\n'
                    f'    <h1>{esc(c["title"])}</h1>\n    <p class="by">{esc(t["by"])} · {p["date"]}</p>\n    <p class="lead">{esc(c["intro"])}</p>\n    ' + "\n    ".join(sec) + f"\n    {cta}\n    {faqh}\n    {more}\n  </article>")
            out = head(lang, c["title"], c["desc"], canon, alternates, og_image, ld, accent) + page_shell(lang, alternates, body)
            write(f"{DIRS[lang]}/{c['slug']}/index.html", out)
            pages.append({"url": canon, "loc": alternates, "default": "en" if "en" in alternates else plangs[0], "hash": hashlib.md5(out.encode("utf-8")).hexdigest()})

    alternates = {l: url(l) for l in LANGS}
    for lang in LANGS:
        t, b = T[lang], BT[lang]
        canon = alternates[lang]
        items = "".join(
            f'<li><a href="/{DIRS[lang]}/{q[lang]["slug"]}/"><img src="/{icon_of(q)}" alt="{alt_of(q)}" width="48" height="48"><div><b>{esc(q[lang]["title"])}</b><span>{esc(q[lang]["desc"])}</span></div></a></li>' for q in posts if lang in q)
        list_ld = {"@context": "https://schema.org", "@type": "Blog", "name": b["idx_h1"], "inLanguage": lang, "url": canon, "description": b["idx_desc"],
                   "blogPost": [{"@type": "BlogPosting", "headline": q[lang]["title"], "url": url(lang, q[lang]["slug"]), "datePublished": q["date"]} for q in posts if lang in q]}
        body = (f'  <article class="guide">\n    <nav class="crumbs" aria-label="breadcrumb"><a href="{home_url(lang)}">{esc(t["home"])}</a> › {esc(b["crumb"])}</nav>\n'
                f'    <h1>{esc(b["idx_h1"])}</h1>\n    <p class="lead">{esc(b["idx_intro"])}</p>\n    <ul class="glist">{items}</ul>\n  </article>')
        out = head(lang, b["idx_title"], b["idx_desc"], canon, alternates, f"{BASE}/og-v3.png", list_ld, "#7FB2FF").replace('content="article"', 'content="website"') + page_shell(lang, alternates, body)
        write(f"{DIRS[lang]}/index.html", out)
        pages.append({"url": canon, "loc": alternates, "default": "en", "hash": hashlib.md5(out.encode("utf-8")).hexdigest()})

    json.dump({"pages": pages, "index": index_urls}, open(os.path.join(TOOLS, "_blog_pages.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"gen_blog: {len(posts)} yazı x {len(LANGS)} dil + dizinler")


if __name__ == "__main__":
    main()
