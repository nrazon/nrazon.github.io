# Siteyi baştan üretir: py -3 tools/build_site.py   (github-pages kökünden ya da herhangi yerden)
# Sıra: ana sayfa (4 dilli kaynak) -> detay sayfaları (4 dilli kaynak + _pages.json) -> rehberler -> dil ayırma (i18n_split: kök=İngilizce, /tr /es /pt /fr, hreflang, sitemap, lastmod).
import os
import subprocess
import sys

T = os.path.dirname(os.path.abspath(__file__))
env = dict(os.environ, NO_SPLIT="1", PYTHONIOENCODING="utf-8")


def run(*a):
    r = subprocess.run([sys.executable, "-X", "utf8", *a], env=env)
    if r.returncode:
        sys.exit(r.returncode)


import shutil
for _d in ("tr", "es", "pt", "fr"):  # üretilmiş dil klasörleri her seferinde sıfırdan
    shutil.rmtree(os.path.join(os.path.dirname(T), _d), ignore_errors=True)
run(os.path.join(T, "gen_home.py"), "--yayin")
run(os.path.join(T, "gen_site.py"))
if os.path.exists(os.path.join(T, "gen_guides.py")):
    run(os.path.join(T, "gen_guides.py"))
if os.path.exists(os.path.join(T, "gen_blog.py")):
    run(os.path.join(T, "gen_blog.py"))
run(os.path.join(T, "i18n_split.py"))
