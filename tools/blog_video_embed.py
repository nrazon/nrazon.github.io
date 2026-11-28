# Ingilizce blog yazilarina, yazinin anlatimli videosunu "tikla-yukle" kutusu olarak ekler (gen_blog.py cagirir). 28.11.2026.
# Veri: ana depodaki Araclar/blog_video/yayin/<ad>.json varsa oradan tools/blog_videos.json + video-thumbs/<ad>.webp tazelenir;
# yoksa (yalniz site deposu) kayitli tools/blog_videos.json kullanilir. Tiklanmadan YouTube'a istek gitmez.
# Yayin saati gelmemis video gizli uretilir; tarayici saati gelince kendisi gosterir (siteyi yeniden derlemek gerekmez).
import datetime as dt
import html
import json
import os
import struct

TOOLS = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(TOOLS)
DATA = os.path.join(TOOLS, "blog_videos.json")
THUMBS = os.path.join(SITE, "video-thumbs")
YAYIN = os.path.join(SITE, "..", "Araclar", "blog_video", "yayin")
SOURCE = r"C:\Dropbox\BlogVideolari"


def _seconds(mp4):
    d = open(mp4, "rb").read()
    i = d.find(b"mvhd")
    ts, du = struct.unpack(">II", d[i + 16:i + 24]) if d[i + 4] == 0 else struct.unpack(">IQ", d[i + 24:i + 36])
    return round(du / ts)


def refresh(names):
    data = json.load(open(DATA, encoding="utf-8")) if os.path.exists(DATA) else {}
    for n in names:
        rec = os.path.join(YAYIN, n + ".json")
        if not os.path.exists(rec):
            continue
        j = json.load(open(rec, encoding="utf-8"))
        vid = j.get("youtube_id")
        if not vid:
            continue
        old = data.get(n, {})
        thumb = os.path.join(THUMBS, n + ".webp")
        png = os.path.join(SOURCE, n, n + "_thumb.png")
        mp4 = os.path.join(SOURCE, n, n + ".mp4")
        if (old.get("id") != vid or not os.path.exists(thumb)) and os.path.exists(png):
            from PIL import Image
            os.makedirs(THUMBS, exist_ok=True)
            Image.open(png).convert("RGB").resize((960, 540), Image.LANCZOS).save(thumb, quality=80, method=6)
        sec = old.get("sec") if old.get("id") == vid else None
        if not sec and os.path.exists(mp4):
            sec = _seconds(mp4)
        if os.path.exists(thumb):
            data[n] = {"id": vid, "at": j.get("publishAt") or "", "sec": sec or 0}
    with open(DATA, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, indent=1, sort_keys=True)
        f.write("\n")
    return data


CSS = ('<style>.vid{margin:1.4rem auto;max-width:70%}@media(max-width:640px){.vid{max-width:100%}}'
       '.vid a,.vid iframe{display:block;position:relative;width:100%;aspect-ratio:16/9;border:0;border-radius:14px;overflow:hidden}'
       '.vid img{width:100%;height:100%;object-fit:cover;display:block}'
       '.vid-btn{position:absolute;left:50%;top:50%;width:68px;height:48px;margin:-24px 0 0 -34px;border-radius:13px;background:rgba(0,0,0,.75)}'
       '.vid-btn::after{content:"";position:absolute;left:27px;top:13px;border-style:solid;border-width:11px 0 11px 19px;border-color:transparent transparent transparent #fff}'
       '.vid a:hover .vid-btn{background:#e62117}.vid figcaption{font-size:.85rem;opacity:.7;margin-top:.45rem}</style>')
JS = ('<script>(function(){var f=document.querySelector(".vid[data-yt]");if(!f)return;'
      'if(f.hidden&&Date.now()>=Date.parse(f.dataset.at))f.hidden=false;'
      'var a=f.querySelector("a");a.addEventListener("click",function(e){e.preventDefault();var i=document.createElement("iframe");'
      'i.src="https://www.youtube-nocookie.com/embed/"+f.dataset.yt+"?autoplay=1&rel=0";i.allow="autoplay; encrypted-media; picture-in-picture; fullscreen";'
      'i.title="Narrated version";i.referrerPolicy="strict-origin-when-cross-origin";a.replaceWith(i);'
      'if(window.gtag)window.gtag("event","video_play",{video_id:f.dataset.yt,page_path:location.pathname})})})()</script>')


def block(video, name, title):
    if not video:
        return ""
    live = True
    if video["at"]:
        live = dt.datetime.fromisoformat(video["at"].replace("Z", "+00:00")) <= dt.datetime.now(dt.timezone.utc)
    # Yayinda olan videoda "hidden" yok (JS'siz de gorunur). Zamanli video gizli uretilir.
    hidden = "" if live else " hidden"
    length = (", %d:%02d" % divmod(video["sec"], 60)) if video["sec"] else ""
    return ('<figure class="vid" data-yt="%s" data-at="%s"%s>'
            '<a href="https://www.youtube.com/watch?v=%s" aria-label="Play the narrated version: %s">'
            '<img src="/video-thumbs/%s.webp" width="960" height="540" alt="" loading="lazy"><span class="vid-btn"></span></a>'
            '<figcaption>Short narrated version%s (AI voice). Nothing is loaded from YouTube until you press play.</figcaption></figure>\n    %s%s'
            % (video["id"], video["at"], hidden, video["id"], html.escape(title, quote=True), name, length, CSS, JS))
