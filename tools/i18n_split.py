# Dil başına ayrı adres üretici (5.11.2026, site SEO Faz 1).
#
# Üreticiler (gen_home.py, gen_site.py) hâlâ 4 dilli TEK sayfa üretir (veri ve çeviriler orada). Bu betik onların çıktısını işler:
#   * `data-l="xx"` / `lang="xx"` işaretli öğeleri hedef dil dışında siler -> her sayfada YALNIZ bir dil kalır;
#   * kök adres = İngilizce (ya da sayfada İngilizce yoksa ilk dil, örn. yalnız Türkçe uygulamalar); diğer diller /tr/, /es/, /pt/, /fr/ altında;
#   * <html lang>, canonical, hreflang (+x-default), og:*, anahtar kelimeli <title>/<meta description>, SoftwareApplication JSON-LD (sameAs dahil);
#   * dil düğmesi = diğer dil sayfasına bağlantı (JavaScript ile metin değiştirme kalktı); iç bağlantılar aynı dilin sayfasına gider;
#   * göreli adresler kök-mutlak yapılır (alt klasörde kırılmasın); sitemap.xml: hreflang alternatifleri + lastmod (içerik değişince).
# Idempotent: işlenmiş sayfada `<!--i18n-split-->` işareti vardır, atlanır. Üreticiler her çalışışında kaynağı yeniden yazar, sonra bu betik çalışır.
# Kullanım: py -3 tools/i18n_split.py   (üreticiler sonunda kendisi çağırır)
import copy
import datetime
import hashlib
import html as htmllib
import json
import os
import posixpath
import re
import sys

from bs4 import BeautifulSoup, Comment

TOOLS = os.path.dirname(os.path.abspath(__file__))
G = os.path.dirname(TOOLS)
BASE = "https://nrazon.github.io"
MARK = "<!--i18n-split-->"
LANGS = ["en", "tr", "es", "pt", "fr"]
LABEL = {"tr": "TR", "en": "EN", "es": "ES", "pt": "PT", "fr": "FR"}
OGLOC = {"en": "en_US", "tr": "tr_TR", "es": "es_ES", "pt": "pt_BR", "fr": "fr_CA"}
SKIP_DIRS = {"tools", "qr", "badges", "node_modules", ".git", ".github", "playreports", "tr", "es", "pt", "fr", "guides", "rehber", "guias", "blog", "yazilar"}
SOCIAL = ["https://x.com/nrazon", "https://www.linkedin.com/in/nesimrazon/", "https://play.google.com/store/apps/dev?id=4632277715794688965"]

SUFFIX = {
    "en": {"games": "Free Android Game", "apps": "Free Android App"},
    "tr": {"games": "Ücretsiz Android Oyunu", "apps": "Ücretsiz Android Uygulaması"},
    "es": {"games": "Juego Android gratis", "apps": "App Android gratis"},
    "pt": {"games": "Jogo Android grátis", "apps": "App Android grátis"},
    "fr": {"games": "Jeu Android gratuit", "apps": "Application Android gratuite"},
}
CTA = {"en": "Free on Google Play.", "tr": "Google Play'de ücretsiz.", "es": "Gratis en Google Play.", "pt": "Grátis no Google Play.", "fr": "Gratuit sur Google Play."}
HOWTO = {  # oyun detay sayfasına eklenen rehber bağlantısı bölümü
    "en": ("How to play", "Read the guide: how to play {name}"),
    "tr": ("Nasıl oynanır?", "Rehberi oku: {name} nasıl oynanır"),
    "es": ("Cómo jugar", "Lee la guía: cómo jugar a {name}"),
    "pt": ("Como jogar", "Leia o guia: como jogar {name}"),
    "fr": ("Comment jouer", "Lire le guide : comment jouer à {name}"),
}
HOME = {
    "en": ("Nesim Apps – Free Android Games & Apps",
           "Free Android games and apps: Tilelings Mahjong, Beamies, Cubbles, Cardles, Logiclings and more. Play in your browser or get them on Google Play."),
    "tr": ("Nesim Apps – Ücretsiz Android Oyunları ve Uygulamaları",
           "Ücretsiz Android oyunları ve uygulamaları: Tilelings Mahjong, Beamies, Cubbles, Cardles, Logiclings ve daha fazlası. Tarayıcıda dene, Google Play'den indir."),
    "es": ("Nesim Apps – Juegos y Apps Android gratis",
           "Juegos y apps Android gratis: Tilelings Mahjong, Beamies, Cubbles, Cardles, Logiclings y más. Juega en el navegador o descárgalos en Google Play."),
    "pt": ("Nesim Apps – Jogos e Apps Android grátis",
           "Jogos e apps Android grátis: Tilelings Mahjong, Beamies, Cubbles, Cardles, Logiclings e mais. Jogue no navegador ou baixe no Google Play."),
}


def read(p):
    return open(p, encoding="utf-8").read()


def write(p, s):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8", newline="\n").write(s)


def load_json(p, default):
    try:
        return json.load(open(p, encoding="utf-8"))
    except Exception:
        return default


def page_url(slug, lang, default):
    """slug '' = ana sayfa. Kök dil: /slug/ ; diğer diller: /lang/slug/"""
    pre = "" if lang == default else f"/{lang}"
    return f"{BASE}{pre}/{slug + '/' if slug else ''}"


def langs_in(soup):
    found = set()
    for t in soup.find_all(True):
        if t.name == "html":
            continue
        for v in (t.get("data-l"), t.get("lang")):
            if v in LANGS:
                found.add(v)
    return found


def trim(text, n):
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= n:
        return text
    cut = text[:n]
    p = max(cut.rfind(". "), cut.rfind("! "), cut.rfind("? "))
    if p > n * 0.55:
        return cut[:p + 1]
    return cut[:cut.rfind(" ")].rstrip(",;:") + "…"


def make_desc(tagline, intro, lang):
    base = tagline.strip()
    if intro:
        base = base.rstrip() + " " + intro.strip()
    cta = CTA[lang]
    d = trim(base, 158 - len(cta) - 1)
    return d + " " + cta


def make_title(store_title, lang, cat):
    t = f"{store_title} – {SUFFIX[lang][cat]}"
    if len(t) + 12 <= 60:
        t += " | Nesim Apps"
    return t


def rewrite_url(val, page_dir, lang, plan):
    """Kök dışı dil sayfalarında göreli adresleri kök-mutlak yapar; site sayfalarına aynı dilin sayfası olarak bağlar."""
    if not val or re.match(r"^(https?:|//|mailto:|tel:|#|data:|javascript:)", val):
        return val
    m = re.match(r"^([^?#]*)([?#].*)?$", val)
    path, rest = m.group(1), m.group(2) or ""
    if path.startswith("/"):
        ab = posixpath.normpath(path)
    else:
        ab = posixpath.normpath(posixpath.join("/" + page_dir, path)) if page_dir else posixpath.normpath("/" + path)
    if path.endswith("/") and not ab.endswith("/"):
        ab += "/"
    seg = [s for s in ab.split("/") if s]
    slug = ""
    if not seg:
        slug = ""
    elif len(seg) == 1 and ab.endswith("/") or (len(seg) == 2 and seg[1] == "index.html"):
        slug = seg[0]
    else:
        return ab + rest
    info = plan.get(slug)
    if info and lang in info["langs"] and lang != info["default"]:
        return f"/{lang}/{slug + '/' if slug else ''}" + rest
    return ab + rest if slug else "/" + rest


def process_source(rel, plan, guides, registry, pagedata, lastmod, today, guides_idx=None, blog_idx=None):
    path = os.path.join(G, rel)
    text = read(path)
    if MARK in text:
        return
    soup0 = BeautifulSoup(text, "html.parser")
    slug = "" if rel == "index.html" else rel.split("/")[0]
    info = plan[slug]
    langs, default = info["langs"], info["default"]
    pd = pagedata.get(slug, {})
    cat = info["cat"]
    page_dir = "" if not slug else slug
    noindex = bool(soup0.find("meta", attrs={"name": "robots"}))
    alternates = {l: page_url(slug, l, default) for l in langs}

    for lang in langs:
        soup = copy.copy(soup0) if False else BeautifulSoup(text, "html.parser")
        # 1) dil dışı öğeleri sil
        for t in list(soup.find_all(True)):
            if t.decomposed or t.name == "html":
                continue
            dl = t.get("data-l")
            lg = t.get("lang")
            if (dl in LANGS and dl != lang) or (lg in LANGS and lg != lang):
                t.decompose()
        html_tag = soup.find("html")
        html_tag["lang"] = lang
        if html_tag.has_attr("data-lang") or slug:
            html_tag["data-lang"] = lang
        if not slug:
            html_tag["class"] = [lang]
        # 2) başlık / açıklama / canonical / hreflang / og
        head = soup.find("head")
        url = alternates[lang]
        if slug:
            st = (pd.get("title") or {}).get(lang) or pd.get("name") or slug
            title = make_title(st, lang, cat)
            desc = make_desc((pd.get("tagline") or {}).get(lang, ""), (pd.get("intro") or {}).get(lang, ""), lang)
            og_title = st
        else:
            title, desc = HOME[lang]
            og_title = title
        def set_meta(attr, key, content):
            tag = head.find("meta", attrs={attr: key})
            if tag is None:
                tag = soup.new_tag("meta")
                tag[attr] = key
                head.append(tag)
            tag["content"] = content
        head.find("title").string = title
        set_meta("name", "description", desc)
        for old in head.find_all("link", attrs={"rel": ["canonical", "alternate"]}):
            old.decompose()
        can = soup.new_tag("link", rel="canonical", href=url)
        head.find("title").insert_after(can)
        anchor = can
        for l in langs:
            a = soup.new_tag("link", rel="alternate", hreflang=l, href=alternates[l])
            anchor.insert_after(a)
            anchor = a
        if len(langs) > 1:
            a = soup.new_tag("link", rel="alternate", hreflang="x-default", href=alternates[default])
            anchor.insert_after(a)
        set_meta("property", "og:title", og_title)
        set_meta("property", "og:description", desc)
        set_meta("property", "og:url", url)
        set_meta("property", "og:locale", OGLOC[lang])
        for l in langs:
            if l != lang:
                tag = soup.new_tag("meta", property="og:locale:alternate", content=OGLOC[l])
                head.append(tag)
        img = head.find("meta", attrs={"property": "og:image"})
        if slug and img is not None:
            cand = os.path.join(G, slug, f"feature-{lang}.png")
            if os.path.exists(cand):
                img["content"] = f"{BASE}/{slug}/feature-{lang}.png"
        set_meta("name", "twitter:title", og_title)
        set_meta("name", "twitter:description", desc)
        # 3) JSON-LD
        for s in head.find_all("script", attrs={"type": "application/ld+json"}):
            try:
                ld = json.loads(s.string)
            except Exception:
                continue
            person = {"@type": "Person", "name": "Nesim Razon", "url": BASE + "/", "sameAs": SOCIAL}
            if slug and ld.get("@type") in ("SoftwareApplication", "MobileApplication", "VideoGame"):
                ld["name"] = (pd.get("title") or {}).get(lang) or ld.get("name")
                ld["description"] = desc
                ld["url"] = url
                ld["inLanguage"] = lang
                for cand in (f"{slug}/feature-{lang}.png", f"{slug}/feature-en.png", f"{slug}/shots/{lang}/01.jpg", f"{slug}/shots/en/01.jpg"):
                    if os.path.exists(os.path.join(G, cand)):
                        ld["image"] = f"{BASE}/{cand}"
                        break
                ld["author"] = person
                ld.setdefault("offers", {"@type": "Offer", "price": "0", "priceCurrency": "USD"})
                shots = [f"{BASE}/{slug}/shots/{lang}/{n:02d}.jpg" for n in range(1, 5) if os.path.exists(os.path.join(G, slug, "shots", lang, f"{n:02d}.jpg"))]
                if shots:
                    ld["screenshot"] = shots
            elif not slug and "@graph" in ld:
                for g in ld["@graph"]:
                    if g.get("@type") == "WebSite":
                        g["url"] = url
                        g["inLanguage"] = lang
                    elif g.get("@type") == "Person":
                        g["sameAs"] = SOCIAL
                    elif g.get("@type") == "ItemList":
                        for it in g.get("itemListElement", []):
                            sl = it["url"].strip("/").split("/")[-1]
                            inf = plan.get(sl)
                            it["url"] = page_url(sl, lang if (inf and lang in inf["langs"]) else (inf or {"default": "en"})["default"], (inf or {"default": "en"})["default"])
            s.string = json.dumps(ld, ensure_ascii=False)
        # 4) dil düğmesi: bağlantılar
        for box in soup.find_all(class_="lang"):
            if len(langs) <= 1:
                box.decompose()
                continue
            box.clear()
            box["role"] = "navigation"
            for l in langs:
                a = soup.new_tag("a", href=alternates[l].replace(BASE, ""), hreflang=l)
                a["data-lang"] = l
                if l == lang:
                    a["aria-current"] = "page"
                a.string = LABEL[l]
                box.append(a)
        # 5) gizlilik bağlantıları (dil sabit)
        priv = info.get("priv") or ["en", "tr", "es", "pt"]
        for a in soup.find_all(attrs={"data-l-privacy": True}):
            tgt = lang if lang in priv else ("en" if "en" in priv else priv[0])
            a["href"] = re.sub(r"#.*$", "", a.get("href", "privacy.html")) + "#" + tgt
            del a["data-l-privacy"]
        # 6) betikler: dil seçimi/tespiti kalkar
        for s in soup.find_all("script"):
            code = s.string or ""
            if "setLang" not in code:
                continue
            if "window.setLang" in code:  # detay sayfası: tüm betik
                s.string = ('\n  (function () {\n    var today = new Date().toISOString().slice(0, 10);\n'
                            '    [].forEach.call(document.querySelectorAll("[data-new-until]"), function (el) { if (today > el.dataset.newUntil) el.remove(); });\n  })();\n')
            else:  # ana sayfa: yalnız dil bölümleri çıkarılır
                code = re.sub(r"\s*// Seçim kaydedildiyse.*?\}\)\(\);\n", "\n", code, count=1, flags=re.S)
                code = re.sub(r"\s*function setLang\(lang\) \{.*?\n  \}\n", "\n", code, count=1, flags=re.S)
                code = code.replace("setLang(document.documentElement.className);", "")
                assert "setLang" not in code and "localStorage.getItem(\"lang\")" not in code, rel
                s.string = code
        # 7) göreli adresler (kök dışı diller)
        if lang != default:
            for t in soup.find_all(True):
                if t.name == "a" and t.has_attr("data-lang"):  # dil düğmesi bağlantıları zaten doğru ve mutlak: dokunma
                    continue
                for attr in ("href", "src", "data-demo-src", "poster"):
                    if t.has_attr(attr):
                        t[attr] = rewrite_url(t[attr], page_dir, lang, plan)
            for t in soup.find_all(style=True):
                t["style"] = re.sub(r"url\(([^)]+)\)", lambda m: "url(" + rewrite_url(m.group(1).strip("'\""), page_dir, lang, plan) + ")", t["style"])
        for a in soup.find_all(attrs={"data-guides-index": True}):  # ana sayfa menüsü: rehber dizini (dile göre)
            gi = (guides_idx or {}).get(lang)
            if gi:
                a["href"] = gi
            del a["data-guides-index"]
        for a in soup.find_all(attrs={"data-blog-index": True}):  # ana sayfa menüsü: blog dizini (dile göre)
            bi = (blog_idx or {}).get(lang)
            if bi:
                a["href"] = bi
            del a["data-blog-index"]
        # 7a) marka (Nesim Apps) bağlantıları her zaman kök "/" (varsayılan sayfa)
        for t in soup.find_all("a", class_=["brand", "back"]):
            t["href"] = "/"
        # 7b) olmayan ekran görüntüsü dosyası (ör. Cardles/Cubbles es/pt yalnız en klasörüne sahip) -> İngilizce karşılığı
        for t in soup.find_all("img"):
            src0 = t.get("src") or ""
            if src0.startswith(("http", "data:")):
                continue
            ab = posixpath.normpath(src0 if src0.startswith("/") else posixpath.join("/" + page_dir, src0)) if src0 else ""
            if ab and not os.path.exists(os.path.join(G, ab.lstrip("/").replace("/", os.sep))) and "/shots/" in ab:
                alt = re.sub(r"/shots/[a-z]{2}/", "/shots/en/", ab)
                if os.path.exists(os.path.join(G, alt.lstrip("/").replace("/", os.sep))):
                    t["src"] = alt
        # 8) rehber bağlantısı (oyun detay sayfaları)
        gl = guides.get(slug, {}).get(lang) if slug else None
        if gl:
            h, label = HOWTO[lang]
            sec = BeautifulSoup(f'<section class="block howto"><h2 class="h">{h}</h2><p><a href="{gl}">{htmllib.escape(label.format(name=(pd.get("name") or slug)))}</a></p></section>', "html.parser")
            foot = soup.find("footer")
            if foot is not None:
                foot.insert_before(sec)
        # 8b) kök (varsayılan dil) sayfalarında: tarayıcı dili başka bir mevcut dilse küçük, kapatılabilir öneri çubuğu (otomatik yönlendirme YOK: arama motorları için güvenli)
        if lang == default and len(langs) > 1 and soup.find("body") is not None:
            alt_map = {l: alternates[l].replace(BASE, "") for l in langs if l != lang}
            msgs = {"tr": "Bu sayfayı Türkçe aç", "es": "Ver esta página en español", "pt": "Ver esta página em português", "fr": "Voir cette page en français", "en": "View this page in English"}
            js = ("(function(){try{if(localStorage.getItem('lang_hint')==='0')return;}catch(e){}"
                  "var A=" + json.dumps(alt_map) + ",M=" + json.dumps({l: msgs[l] for l in alt_map}, ensure_ascii=False) + ";"
                  "var c=(navigator.languages&&navigator.languages[0]||navigator.language||'en').toLowerCase().slice(0,2);if(!A[c])return;"
                  "var d=document.createElement('div');d.setAttribute('role','region');d.style.cssText='position:fixed;left:12px;right:12px;bottom:12px;z-index:50;max-width:520px;margin:0 auto;background:#171A2B;color:#fff;border-radius:14px;padding:10px 14px;display:flex;gap:12px;align-items:center;box-shadow:0 8px 24px rgba(0,0,0,.35);font:15px system-ui,sans-serif';"
                  "var a=document.createElement('a');a.href=A[c];a.textContent=M[c]+' →';a.style.cssText='color:#9CC2FF;font-weight:700;flex:1;text-decoration:none';"
                  "var x=document.createElement('button');x.type='button';x.setAttribute('aria-label','Close');x.textContent='✕';x.style.cssText='background:none;border:0;color:#fff;font-size:16px;cursor:pointer';"
                  "x.onclick=function(){d.remove();try{localStorage.setItem('lang_hint','0');}catch(e){}};d.appendChild(a);d.appendChild(x);document.body.appendChild(d);})();")
            sc = soup.new_tag("script")
            sc.string = js
            soup.find("body").append(sc)
        if soup.find(class_="lang") is not None and soup.find("body") is not None:  # dili elle seçen kişiye öneri çubuğu tekrar çıkmasın
            sc2 = soup.new_tag("script")
            sc2.string = "(function(){[].forEach.call(document.querySelectorAll('.lang a'),function(a){a.addEventListener('click',function(){try{localStorage.setItem('lang_hint','0')}catch(e){}})})})();"
            soup.find("body").append(sc2)
        soup.find("head").insert(0, Comment("i18n-split"))
        out = str(soup)
        out = out.replace("<!--i18n-split-->", MARK, 1)
        # 9) yaz
        dest = rel if lang == default else posixpath.join(lang, rel)
        write(os.path.join(G, dest), out)
        if not noindex:
            registry.append({"url": url, "loc": alternates, "lang": lang, "default": default, "hash": hashlib.md5(out.encode("utf-8")).hexdigest(), "slug": slug})


def build_plan(sources, pagedata):
    home = load_json(os.path.join(TOOLS, "home_data.json"), [])
    cats = {a["slug"]: a.get("cat", "apps") for a in home}
    plan = {}
    for rel in sources:
        slug = "" if rel == "index.html" else rel.split("/")[0]
        text = read(os.path.join(G, rel))
        if MARK in text:
            continue
        soup = BeautifulSoup(text, "html.parser")
        h1 = soup.find("h1")
        langs = langs_in(h1) if h1 is not None else set()   # içerik dilleri: başlığın dilleri (yalnız Türkçe uygulamalarda çerçeve metni 4 dilli olabilir)
        if not langs:
            langs = langs_in(soup)
        ordered = [l for l in ["en", "tr", "es", "pt", "fr"] if l in langs]
        if not ordered:
            m = re.search(r'<html[^>]*lang="([a-z]{2})"', text)
            ordered = [m.group(1) if m else "en"]
        default = "en" if "en" in ordered else ordered[0]
        priv = []
        pp = os.path.join(G, slug, "privacy.html") if slug else None
        if pp and os.path.exists(pp):
            priv = re.findall(r'id="([a-z]{2})"', read(pp))
        plan[slug] = {"langs": ordered, "default": default, "cat": cats.get(slug, "games"), "priv": priv}
    return plan


def main():
    today = datetime.date.today().isoformat()
    sources = ["index.html"] + sorted(
        f"{d}/index.html" for d in os.listdir(G)
        if os.path.isdir(os.path.join(G, d)) and d not in SKIP_DIRS and os.path.exists(os.path.join(G, d, "index.html")))
    pagedata = load_json(os.path.join(TOOLS, "_pages.json"), {})
    _gp = load_json(os.path.join(TOOLS, "_guides_pages.json"), {})
    guides = _gp.get("by_app", {})
    guides_idx = _gp.get("index", {})
    blog_idx = load_json(os.path.join(TOOLS, "_blog_pages.json"), {}).get("index", {})
    plan = build_plan(sources, pagedata)
    # işlenmiş sayfaların da planda olması için (idempotent yeniden çalışma): önceki plan kaydı
    prev = load_json(os.path.join(TOOLS, "_plan.json"), {})
    for k, v in prev.items():
        plan.setdefault(k, v)
    registry = []
    lastmod = load_json(os.path.join(TOOLS, "lastmod.json"), {})
    done = 0
    for rel in sources:
        if MARK in read(os.path.join(G, rel)):
            continue
        process_source(rel, plan, guides, registry, pagedata, lastmod, today, guides_idx, blog_idx)
        done += 1
    json.dump(plan, open(os.path.join(TOOLS, "_plan.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    if done:
        # kayıt: bu çalıştırmada üretilenler + önceki kayıt
        reg = load_json(os.path.join(TOOLS, "_registry.json"), {})
        redone = {r["slug"] for r in registry}
        reg = {u: r for u, r in reg.items() if r.get("slug") not in redone}   # yeniden işlenen sayfanın bayat girdileri (eski dil planı) silinir
        for r in registry:
            reg[r["url"]] = r
        for u in list(reg):                                                    # diskte dosyası olmayan adresler sitemap'e girmez
            pth = u.replace(BASE, "").strip("/")
            if not os.path.exists(os.path.join(G, pth, "index.html") if pth else os.path.join(G, "index.html")):
                del reg[u]
        json.dump(reg, open(os.path.join(TOOLS, "_registry.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    write_sitemap(lastmod, today)
    print(f"i18n_split: {done} kaynak sayfa işlendi")


def write_sitemap(lastmod, today):
    reg = load_json(os.path.join(TOOLS, "_registry.json"), {})
    guides = load_json(os.path.join(TOOLS, "_guides_pages.json"), {}).get("pages", [])
    entries = list(reg.values())
    guides = guides + load_json(os.path.join(TOOLS, "_blog_pages.json"), {}).get("pages", [])
    for g in guides:  # {"url","loc":{lang:url},"hash"}
        entries.append(g)
    xml = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    changed = False
    for e in sorted(entries, key=lambda x: x["url"]):
        h = e.get("hash", "")
        rec = lastmod.get(e["url"])
        if not rec or rec["hash"] != h:
            lastmod[e["url"]] = rec = {"hash": h, "date": today}
            changed = True
        xml.append("  <url>")
        xml.append(f"    <loc>{htmllib.escape(e['url'])}</loc>")
        xml.append(f"    <lastmod>{rec['date']}</lastmod>")
        loc = e.get("loc", {})
        if len(loc) > 1:
            for l in sorted(loc, key=lambda x: LANGS.index(x) if x in LANGS else 9):
                xml.append(f'    <xhtml:link rel="alternate" hreflang="{l}" href="{htmllib.escape(loc[l])}"/>')
            xml.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{htmllib.escape(loc[e["default"]])}"/>')
        xml.append("  </url>")
    xml.append("</urlset>")
    write(os.path.join(G, "sitemap.xml"), "\n".join(xml) + "\n")
    if changed:
        json.dump(lastmod, open(os.path.join(TOOLS, "lastmod.json"), "w", encoding="utf-8"), indent=1)


if __name__ == "__main__":
    main()
