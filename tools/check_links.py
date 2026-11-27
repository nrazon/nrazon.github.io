# Kirik ic baglanti taramasi: py -3 -X utf8 tools/check_links.py .   (build_site.py sonrasi; TOTAL 0 olmali)
import os, re, sys, collections
root = sys.argv[1]
bad = collections.defaultdict(set)
for dp, dn, fn in os.walk(root):
    dn[:] = [d for d in dn if d not in ('.git', 'tools', 'node_modules', '__pycache__')]
    for f in fn:
        if not (f.endswith('.html') or f.endswith('.xml') or f == 'llms.txt'):
            continue
        p = os.path.join(dp, f)
        s = open(p, encoding='utf-8', errors='replace').read()
        s = re.sub(r'<script(?![^>]*ld\+json)[^>]*>.*?</script>', '', s, flags=re.S)
        urls = re.findall(r'''(?:href|src)=["']([^"']+)["']''', s) + re.findall(r'''https://nesimapps\.com[^"'<>\s)\]]*''', s)
        for u in urls:
            u = u.replace('https://nesimapps.com', '') or '/'
            if re.match(r'^(https?:|//|mailto:|tel:|#|data:|javascript:|market:)', u):
                continue
            u = u.split('#')[0].split('?')[0]
            if not u:
                continue
            t = os.path.join(root, u.lstrip('/')) if u.startswith('/') else os.path.join(dp, u)
            if os.path.isdir(t):
                t = os.path.join(t, 'index.html')
            if not os.path.exists(t):
                bad[u].add(os.path.relpath(p, root).replace(os.sep, "/"))
for u, ps in sorted(bad.items()):
    print(u, len(ps), sorted(ps)[:3])
print('TOTAL', len(bad))
