# -*- coding: utf-8 -*-
"""Flowlings gizlilik sayfasini (flowlings/privacy.html) Slinglings'inkinden turetir: ayni hizmetler (AdMob+UMP, Firebase Analytics/Crashlytics,
Play Games, Play Billing, uygulama ici guncelleme). Flowlings'e ozgu isim, renk ve oyun tanimi. Calistir: py -3 tools/gen_privacy_flowlings.py
Yururluk tarihi YAYIN GUNUNDE guncellenir (DATE_*)."""
import io, os, re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "slinglings", "privacy.html"), encoding="utf-8").read()

R = [
    ("--bg:#1B2540; --card:#27345A; --text:#F6F1E6; --dim:#D9DFF0; --accent:#FFD84D; --link:#9CC3FF;",
     "--bg:#12433F; --card:#1C5A54; --text:#F6F1E6; --dim:#CFE9E2; --accent:#FFD84D; --link:#8FE0D0;"),
    ("Slinglings", "Flowlings"),
    ("Effective date: 23 November 2026", "Effective date: 26 November 2026"),
    ("Yürürlük tarihi: 23 Kasım 2026", "Yürürlük tarihi: 26 Kasım 2026"),
    ("Fecha de entrada en vigor: 23 de noviembre de 2026", "Fecha de entrada en vigor: 26 de noviembre de 2026"),
    ("Data de vigência: 23 de novembro de 2026", "Data de vigência: 26 de novembro de 2026"),
    ("is a physics puzzle game in which you sling cute mail couriers through space", "is a pipe puzzle in which you lay pipes to bring energy to sleeping plant creatures"),
    ("sevimli postacıları uzayda fırlattığın bir fizik bulmaca oyunudur", "uyuyan sevimli bitki yaratıklarına enerji ulaştırmak için boru döşediğin bir bulmaca oyunudur"),
    ("un juego de puzles de física en el que lanzas carteros adorables por el espacio", "un juego de puzles en el que colocas tuberías para llevar energía a criaturas vegetales dormidas"),
    ("um jogo de quebra-cabeças de física em que você lança carteiros fofos pelo espaço", "um jogo de quebra-cabeças em que você posiciona canos para levar energia a criaturas vegetais adormecidas"),
    ("best shots", "best tap counts"), ("courier accessories", "unlocked plants"),
    ("en iyi atış sayıların", "en iyi dokunuş sayıların"), ("postacı aksesuarların", "uyandırdığın bitkilerin"),
    ("tus mejores tiros", "tus mejores recuentos de toques"), ("los accesorios de tu cartero", "las plantas desbloqueadas"),
    ("seus melhores tiros", "suas melhores contagens de toques"), ("os acessórios do seu carteiro", "as plantas desbloqueadas"),
    ("best shots", "best tap counts"), ("number of shots", "number of taps"),
    ("atış sayısı", "dokunuş sayısı"), ("número de tiros", "número de toques"),
    ("(sayaçlar, yıldızlar, en iyi atış sayıları ve günlük kayıtlar)", "(sayaçlar, yıldızlar, en iyi dokunuş sayıları ve günlük kayıtlar)"),
    ("(counters, stars, best shots and daily records)", "(counters, stars, best tap counts and daily records)"),
    ("mejores tiros", "mejores recuentos de toques"), ("melhores tiros", "melhores contagens de toques"),
    ("stars earned, how many hints you used and how long it took", "stars earned, how many hints you used and how long it took"),
]
out = src
for a, b in R:
    out = out.replace(a, b)
for bad in ("courier", "postacı", "cartero", "carteiro", "shots", "atış", "tiros", "sling", "fırlat", "lanz", "lança"):
    for m in re.finditer(bad, out, flags=re.I):
        print("UYARI: kalan Slinglings ifadesi:", out[max(0, m.start() - 60):m.end() + 60].replace("\n", " "))
# iPhone: Slinglings metni Android'i anlatir; iOS'ta farkli olan hizmetler ayri bir bolumde (her dilde "Cocuklar" basligindan once).
IOS = {
    "en": ("iPhone", "On iPhone the game uses Apple's services instead of the Google Play ones described above. The iPhone version has no in-app purchases. If you are signed in to Game Center, your scores and unlocked achievements are sent to Apple's Game Center. When iCloud is turned on, your progress counters (level stars, badges and daily streak) are also stored in your iCloud key-value storage, tied to your Apple Account, so they come back on your other devices; I cannot see them. Ads (Google AdMob), usage statistics and crash reports work as described above; crash reports contain the iOS version. The game does not ask for the app tracking permission (App Tracking Transparency) and does not track you across other companies' apps and websites."),
    "tr": ("iPhone", "iPhone'da oyun, yukarıda anlatılan Google Play hizmetleri yerine Apple'ın hizmetlerini kullanır. iPhone sürümünde uygulama içi satın alma yoktur. Game Center'da oturum açıksa skorların ve açtığın başarımlar Apple'ın Game Center'ına gönderilir. iCloud açıksa ilerleme sayaçların (bölüm yıldızları, rozetler ve günlük seri) ayrıca Apple Kimliğine bağlı iCloud anahtar-değer deposunda saklanır, böylece diğer cihazlarında geri gelir; bunları ben göremem. Reklamlar (Google AdMob), kullanım istatistikleri ve çökme raporları yukarıda anlatıldığı gibidir; çökme raporları iOS sürümünü içerir. Oyun uygulama izleme iznini (App Tracking Transparency) istemez ve seni diğer şirketlerin uygulama ve sitelerinde takip etmez."),
    "es": ("iPhone", "En iPhone el juego usa los servicios de Apple en lugar de los de Google Play descritos arriba. La versión para iPhone no tiene compras dentro de la app. Si has iniciado sesión en Game Center, tus puntuaciones y los logros desbloqueados se envían a Game Center de Apple. Si iCloud está activado, los contadores de tu progreso (estrellas de nivel, insignias y racha diaria) también se guardan en el almacenamiento clave-valor de iCloud, vinculado a tu cuenta de Apple, así vuelven en tus otros dispositivos; yo no puedo verlos. Los anuncios (Google AdMob), las estadísticas de uso y los informes de fallos funcionan como se describe arriba; los informes de fallos incluyen la versión de iOS. El juego no solicita el permiso de seguimiento (App Tracking Transparency) y no te rastrea en apps y sitios web de otras empresas."),
    "pt": ("iPhone", "No iPhone o jogo usa os serviços da Apple em vez dos do Google Play descritos acima. A versão para iPhone não tem compras no app. Se você estiver conectado ao Game Center, suas pontuações e conquistas desbloqueadas são enviadas ao Game Center da Apple. Com o iCloud ativado, os contadores do seu progresso (estrelas dos níveis, insígnias e sequência diária) também ficam no armazenamento chave-valor do iCloud, vinculado à sua conta Apple, e voltam nos seus outros aparelhos; eu não consigo vê-los. Os anúncios (Google AdMob), as estatísticas de uso e os relatórios de falhas funcionam como descrito acima; os relatórios de falhas incluem a versão do iOS. O jogo não pede a permissão de rastreamento (App Tracking Transparency) e não rastreia você em apps e sites de outras empresas."),
}
for lang, (head, text) in IOS.items():
    a = out.index('<section id="%s"' % lang)
    b = out.index('</section>', a)
    heads = [m.start() for m in re.finditer(r"<h3>", out[a:b])]
    at = a + heads[-3]
    out = out[:at] + "<h3>%s</h3>\n    <p>%s</p>\n    " % (head, text) + out[at:]
dst = os.path.join(G, "flowlings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"))
