# -*- coding: utf-8 -*-
"""Astrolings gizlilik sayfasini (astrolings/privacy.html) Nudgelings'inkinden turetir: ortak hizmet bolumleri (AdMob, Billing, Analytics, Crashlytics,
Cocuklar, Haklar, Iletisim) aynen kalir; oyuna ozgu bolumler (ilerleme, Play Games, reklam sikligi, analitik olaylari) Astrolings'e gore degistirilir,
bildirim ve haftalik icerik bolumleri eklenir. Calistir: py -3 tools/gen_privacy_astrolings.py"""
import io, os, re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "nudgelings", "privacy.html"), encoding="utf-8").read()

DATE = {"en": "Effective date: 9 November 2026", "tr": "Yürürlük tarihi: 9 Kasım 2026", "es": "Fecha de entrada en vigor: 9 de noviembre de 2026", "pt": "Data de vigência: 9 de novembro de 2026"}

NEW = {
 "en": {
  "intro": 'Astrolings ("the app") is a Turkish-language astrology and sky app for entertainment: daily sign readings, a Moon calendar and information about the zodiac signs. It is made by Nesim Razon, an individual developer ("I", "me"). The app has no accounts; I do not sell any data. Readings are for entertainment only and are not predictions or advice.',
  "mine": ("Your choices and settings", "Your zodiac sign, the birthday (day and month only; the year is never asked for the zodiac sign) you entered to find it, your text size, notification choice and similar settings are stored only on your phone. The sky positions (Moon, planets) and the readings are calculated on your phone, offline. If Android backup is turned on, Android may include this data in your device backup to your Google account. Uninstalling the app or clearing its data deletes it."),
  "notif": ("Notifications", "If you turn on the daily notification, the app asks for Android's notification permission and then shows a short summary of your sign's reading at the time you choose. The notification is created on your phone; nothing about it is sent anywhere. You can turn it off in the app or in Android settings."),
  "weekly": ("Weekly content from the internet", "Once a day at most, when you open the app, it downloads small content files (the weekly themes) from this website, which is hosted on GitHub Pages. No account or personal information is sent; like any web request, the hosting provider (GitHub) receives your IP address and standard request details, under the <a href=\"https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Privacy Statement</a>. Old files are deleted from your phone automatically."),
  "ads": ("Advertising (Google AdMob)", None),
  "stats": ("Usage statistics (Google Analytics for Firebase)", "The app sends anonymous events to Google Analytics for Firebase, such as which screens or features are used. They are linked to a random installation ID, not to you, and the advertising ID is not collected for analytics."),
  "ads_intro": "The app is free and shows ads provided by Google AdMob. To serve and measure ads and to prevent fraud, Google may collect and process information such as your device's advertising ID, IP address, approximate location derived from the IP address, device and app information, and how you interact with ads. Learn more in",
 },
 "tr": {
  "intro": 'Astrolings ("uygulama") eğlence amaçlı Türkçe bir astroloji ve gökyüzü uygulamasıdır: günlük burç yorumları, Ay takvimi ve burç bilgileri. Bağımsız geliştirici Nesim Razon ("ben") tarafından yapılmıştır. Uygulamada hesap yoktur; hiçbir veri satmıyorum. Yorumlar yalnızca eğlence içindir, öngörü ya da tavsiye değildir.',
  "mine": ("Seçimlerin ve ayarların", "Burcun, burcunu bulmak için girdiğin doğum günü (yalnızca gün ve ay; burç için yıl hiç sorulmaz), yazı boyutu, bildirim tercihin ve benzeri ayarlar yalnızca telefonunda saklanır. Gökyüzü konumları (Ay, gezegenler) ve yorumlar telefonunda, internetsiz hesaplanır. Android yedeklemesi açıksa Android bu verileri Google hesabındaki cihaz yedeğine de ekleyebilir. Uygulamayı kaldırmak ya da verilerini temizlemek bunları siler."),
  "notif": ("Bildirimler", "Günlük bildirimi açarsan uygulama Android'in bildirim iznini ister ve seçtiğin saatte burcunun yorumunun kısa bir özetini gösterir. Bildirim telefonunda oluşturulur; bununla ilgili hiçbir şey bir yere gönderilmez. Uygulamadan ya da Android ayarlarından kapatabilirsin."),
  "weekly": ("İnternetten haftalık içerik", "Uygulama, günde en fazla bir kez, açtığında küçük içerik dosyalarını (haftalık temalar) GitHub Pages üzerinde barındırılan bu web sitesinden indirir. Hesap ya da kişisel bilgi gönderilmez; her web isteğinde olduğu gibi barındırma sağlayıcısı (GitHub), <a href=\"https://docs.github.com/tr/site-policy/privacy-policies/github-general-privacy-statement\">GitHub Gizlilik Beyanı</a> kapsamında IP adresini ve olağan istek bilgilerini alır. Eski dosyalar telefonundan kendiliğinden silinir."),
  "ads": ("Reklamlar (Google AdMob)", None),
  "stats": ("Kullanım istatistikleri (Google Analytics for Firebase)", "Uygulama Google Analytics for Firebase'e hangi ekranların ya da özelliklerin kullanıldığı gibi anonim olaylar gönderir. Olaylar sana değil, rastgele bir kurulum kimliğine bağlıdır; istatistikler için reklam kimliği toplanmaz."),
  "ads_intro": "Uygulama ücretsizdir ve Google AdMob reklamları gösterir. Reklamları sunmak, ölçmek ve dolandırıcılığı önlemek için Google, cihazının reklam kimliği, IP adresi, IP adresinden çıkarılan yaklaşık konum, cihaz ve uygulama bilgileri ile reklamlarla etkileşimin gibi bilgileri toplayıp işleyebilir. Ayrıntılar:",
 },
 "es": {
  "intro": 'Astrolings («la app») es una aplicación de astrología y cielo en turco, con fines de entretenimiento: lecturas diarias por signo, calendario lunar e información sobre los signos del zodiaco. La ha creado Nesim Razon, desarrollador independiente. La app no tiene cuentas; no vendo ningún dato. Las lecturas son solo para entretenimiento y no son predicciones ni consejos.',
  "mine": ("Tus elecciones y ajustes", "Tu signo, el cumpleaños (solo día y mes; el año nunca se pide para el signo) que introdujiste para encontrarlo, el tamaño del texto, tu elección de notificaciones y ajustes similares se guardan solo en tu teléfono. Las posiciones del cielo (Luna, planetas) y las lecturas se calculan en tu teléfono, sin conexión. Si la copia de seguridad de Android está activada, Android puede incluir estos datos en la copia de tu dispositivo en tu cuenta de Google. Desinstalar la app o borrar sus datos los elimina."),
  "notif": ("Notificaciones", "Si activas la notificación diaria, la app solicita el permiso de notificaciones de Android y muestra un breve resumen de la lectura de tu signo a la hora que elijas. La notificación se crea en tu teléfono; no se envía nada a ningún sitio. Puedes desactivarla en la app o en los ajustes de Android."),
  "weekly": ("Contenido semanal desde internet", "Como máximo una vez al día, al abrir la app, descarga pequeños archivos de contenido (los temas semanales) de este sitio web, alojado en GitHub Pages. No se envía ninguna cuenta ni información personal; como en cualquier petición web, el proveedor de alojamiento (GitHub) recibe tu dirección IP y los datos habituales de la petición, según la <a href=\"https://docs.github.com/es/site-policy/privacy-policies/github-general-privacy-statement\">Declaración de privacidad de GitHub</a>. Los archivos antiguos se borran automáticamente de tu teléfono."),
  "ads": ("Publicidad (Google AdMob)", None),
  "stats": ("Estadísticas de uso (Google Analytics para Firebase)", "La app envía eventos anónimos a Google Analytics para Firebase, por ejemplo qué pantallas o funciones se usan. Se vinculan a un ID de instalación aleatorio y no se recopila el ID de publicidad para las estadísticas."),
  "ads_intro": "La app es gratuita y muestra anuncios de Google AdMob. Para mostrar y medir anuncios y prevenir el fraude, Google puede recopilar y tratar información como el ID de publicidad, la dirección IP, la ubicación aproximada derivada de la IP, datos del dispositivo y de la app, y tu interacción con los anuncios. Más información:",
 },
 "pt": {
  "intro": 'Astrolings ("o app") é um aplicativo de astrologia e céu em turco, para entretenimento: leituras diárias por signo, calendário lunar e informações sobre os signos do zodíaco. Foi criado por Nesim Razon, desenvolvedor independente. O app não tem contas; eu não vendo nenhum dado. As leituras são apenas para entretenimento e não são previsões nem conselhos.',
  "mine": ("Suas escolhas e configurações", "Seu signo, o aniversário (apenas dia e mês; o ano nunca é pedido para o signo) que você informou para encontrá-lo, o tamanho do texto, sua escolha de notificações e configurações semelhantes ficam apenas no seu celular. As posições do céu (Lua, planetas) e as leituras são calculadas no seu celular, sem internet. Se o backup do Android estiver ativado, o Android pode incluir esses dados no backup do aparelho na sua conta Google. Desinstalar o app ou limpar seus dados os apaga."),
  "notif": ("Notificações", "Se você ativar a notificação diária, o app pede a permissão de notificações do Android e mostra um breve resumo da leitura do seu signo no horário que você escolher. A notificação é criada no seu celular; nada sobre ela é enviado a lugar nenhum. Você pode desativá-la no app ou nas configurações do Android."),
  "weekly": ("Conteúdo semanal da internet", "No máximo uma vez por dia, ao abrir o app, ele baixa pequenos arquivos de conteúdo (os temas semanais) deste site, hospedado no GitHub Pages. Nenhuma conta ou informação pessoal é enviada; como em qualquer requisição web, o provedor de hospedagem (GitHub) recebe seu endereço IP e dados comuns da requisição, conforme a <a href=\"https://docs.github.com/pt/site-policy/privacy-policies/github-general-privacy-statement\">Declaração de Privacidade do GitHub</a>. Arquivos antigos são apagados do seu celular automaticamente."),
  "ads": ("Publicidade (Google AdMob)", None),
  "stats": ("Estatísticas de uso (Google Analytics para Firebase)", "O app envia eventos anônimos ao Google Analytics para Firebase, por exemplo quais telas ou recursos são usados. Eles ficam ligados a um ID de instalação aleatório e o ID de publicidade não é coletado para as estatísticas."),
  "ads_intro": "O app é gratuito e mostra anúncios do Google AdMob. Para exibir e medir anúncios e evitar fraudes, o Google pode coletar e processar informações como o ID de publicidade, o endereço IP, a localização aproximada obtida do IP, dados do aparelho e do app e sua interação com os anúncios. Saiba mais em",
 },
}

HEAD_PLAY = {"en": "Google Play Games", "tr": "Google Play Games", "es": "Google Play Games", "pt": "Google Play Games"}


def convert(sec, lang):
    n = NEW[lang]
    # bolumleri ayir
    m = re.match(r'(.*?<p class="meta">.*?</p>\s*)<p>(.*?)</p>(.*?)(\n  </section>)?$', sec, re.S)
    head, intro, rest = m.group(1), m.group(2), m.group(3)
    blocks = re.findall(r'(<h3>(.*?)</h3>\s*(?:<p>.*?</p>\s*)+)', rest, re.S)
    out = []
    for html, title in blocks:
        if title == HEAD_PLAY[lang]:
            continue  # Astrolings'te Play Games yok
        low = title.lower()
        if low.startswith(("your game", "oyunun", "tu partida", "seu jogo")):
            for key in ("mine", "notif", "weekly"):
                t, body = n[key]
                out.append("<h3>%s</h3>\n    <p>%s</p>" % (t, body))
            continue
        if title.startswith(("Advertising", "Reklamlar", "Publicidad", "Publicidade")):
            # reklam bolumu: ilk cumleler Astrolings'e gore, baglantilar korunur
            link_part = re.search(r'(<a href.*?)</p>', html, re.S).group(1)
            out.append("<h3>%s</h3>\n    <p>%s %s</p>" % (n["ads"][0], n["ads_intro"], link_part))
            continue
        if title.startswith(("Usage statistics", "Kullanım istatistikleri", "Estadísticas de uso", "Estatísticas de uso")):
            t, body = n["stats"]
            out.append("<h3>%s</h3>\n    <p>%s</p>" % (t, body))
            continue
        out.append(html.strip())
    return head + "<p>%s</p>\n    " % n["intro"] + "\n    ".join(out) + "\n  </section>"


secs = re.findall(r'  <section id="(\w\w)" lang="\w\w">\n(.*?)  </section>', src, re.S)
parts = []
for lang, body in secs:
    parts.append('  <section id="%s" lang="%s">\n%s' % (lang, lang, convert(body, lang)))

out = src
a = out.index('  <section id="en"')
b = out.index('</main>')
out = out[:a] + "\n".join(parts) + "\n" + out[b:]
out = out.replace("Nudgelings", "Astrolings")
out = out.replace("--bg:#0F2F28; --card:#184A3E; --text:#F1FAF6; --dim:#C9E8DC; --accent:#FFD84D; --link:#8FDCC0;",
                  "--bg:#1A1B4B; --card:#2B2766; --text:#F3EFFA; --dim:#D4D2F5; --accent:#FFC21A; --link:#B7B2FF;")
out = re.sub(r'<img src="icon.png" alt="Astrolings">', '', out)
out = out.replace('.brand img { width:64px; height:64px; border-radius:14px; }', '')
out = out.replace("Astrolings privacy policy: what data the Android app uses and how it is protected.", "Astrolings privacy policy: what data the Android app uses and how it is protected.")
for lang, d in DATE.items():
    pass
for old in ("Effective date: 9 November 2026",):
    pass
dst = os.path.join(G, "astrolings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(out)
print("ok", os.path.join(dst, "privacy.html"), len(out))
