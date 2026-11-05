# SEO son rötuşu (idempotent): meta description'ı olmayan sayfalara (gizlilik / şartlar / 404 / site gizliliği) description ekler,
# alt="" olan kapak/ikon görsellerine anlamlı alt koyar. Üreticiler (gen_site, gen_terms, gen_privacy_tilelings) sonunda bunu çağırır;
# elle yazılı gizlilik sayfaları için de tek başına çalıştırılabilir: py -3 tools/seo_fix.py
import glob
import html
import os
import re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKIP = ("tools", "node_modules", "google6b7f0191d81507b3.html")


def describe(path, title):
    name = re.split(r"\s+[–·-]\s+", title)[0].strip()
    base = os.path.basename(path)
    if base == "404.html":
        return "Page not found. Nesim Apps: small Android games and apps on Google Play – Sayfa bulunamadı · Página no encontrada · Página não encontrada."
    if base == "site-privacy.html":
        return "Privacy notice for the Nesim Apps website (nrazon.github.io): anonymous analytics, no accounts, no ads. Gizlilik · Privacidad · Privacidade."
    tr_only = "Gizlilik Politikası" in title and "Privacy" not in title
    if base == "terms.html":
        return f"{name} terms of use: license, acceptable use and liability for the Android app by Nesim Apps. Kullanım şartları · Términos de uso · Termos de uso."
    if "Kullanım Koşulları" in title:
        return f"{name}: gizlilik politikası ve kullanım koşulları. Hangi veriler işlenir, nasıl korunur. Nesim Apps Android uygulaması."
    if tr_only:
        return f"{name}: gizlilik politikası. Uygulamanın hangi verileri işlediği ve nasıl korunduğu. Privacy policy of the Nesim Apps Android app."
    return f"{name} privacy policy: what data the Android app uses and how it is protected. Gizlilik politikası · Política de privacidad · Política de privacidade."


def fix(path):
    s = open(path, encoding="utf-8").read()
    o = s
    if not re.search(r'<meta[^>]+name=["\']description', s):
        m = re.search(r"<title>([^<]*)</title>", s)
        if m:
            d = html.escape(describe(path, html.unescape(m.group(1))), quote=True)
            s = s.replace(m.group(0), m.group(0) + f'\n<meta name="description" content="{d}">', 1)

    def alt_for(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag)
        if not src or not re.search(r'alt=""', tag):
            return tag
        mm = re.search(r"/?([a-z0-9]+)/icon\.", src.group(1))
        label = (mm.group(1) + " icon") if mm else "Nesim Apps"
        return tag.replace('alt=""', f'alt="{label}"')

    s = re.sub(r"<img\b[^>]*>", alt_for, s)
    if s != o:
        open(path, "w", encoding="utf-8", newline="\n").write(s)
        return True
    return False


def main():
    n = 0
    for f in glob.glob(os.path.join(G, "**", "*.html"), recursive=True):
        rel = os.path.relpath(f, G).replace("\\", "/")
        if rel.startswith(SKIP) or rel in SKIP:
            continue
        if fix(f):
            n += 1
    print("seo_fix: değişen sayfa", n)


if __name__ == "__main__":
    main()
