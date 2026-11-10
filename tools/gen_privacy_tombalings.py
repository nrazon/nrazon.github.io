# -*- coding: utf-8 -*-
"""Tombalings gizlilik sayfasini (tombalings/privacy.html) uretir: baslik/stil/gezinme Pentolings sayfasindan, metinler 4 dilde burada.
Hizmetler: AdMob+UMP, Firebase Analytics/Crashlytics, Play Games + Saved Games, Billing, cihazin metin okuma motoru (sesli tellal).
"Diger oyunlarim" listesi YOK (Tombalings capraz tanitima girmez). Calistir: py -3 -X utf8 tools/gen_privacy_tombalings.py"""
import io, os, re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "pentolings", "privacy.html"), encoding="utf-8").read()
head = src[:src.index('  <section id="en"')]
head = head.replace("Pentolings", "Tombalings").replace("pentolings", "tombalings")
head = head.replace("--bg:#1B1838; --card:#2A2350; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFC857; --link:#B7A4FF;",
                    "--bg:#F4E4C6; --card:#FFFBF0; --text:#2B211C; --dim:#4A3C32; --accent:#C8372A; --link:#2B5FA8;")
tail = src[src.rindex("</section>") + len("</section>"):]

GOOGLE_ADS = {
    "en": '<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a>',
    "tr": '<a href="https://policies.google.com/technologies/partner-sites?hl=tr">Google, hizmetlerini kullanan sitelerden veya uygulamalardan gelen bilgileri nasıl kullanır</a> ve <a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a>',
    "es": '<a href="https://policies.google.com/technologies/partner-sites?hl=es">Cómo usa Google la información de sitios o aplicaciones que utilizan sus servicios</a> y la <a href="https://policies.google.com/privacy?hl=es">Política de Privacidad de Google</a>',
    "pt": '<a href="https://policies.google.com/technologies/partner-sites?hl=pt-BR">Como o Google usa informações de sites ou apps que usam seus serviços</a> e a <a href="https://policies.google.com/privacy?hl=pt-BR">Política de Privacidade do Google</a>',
}
GPRIV = {
    "en": '<a href="https://policies.google.com/privacy">Google Privacy Policy</a>',
    "tr": '<a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a>',
    "es": '<a href="https://policies.google.com/privacy?hl=es">Política de Privacidad de Google</a>',
    "pt": '<a href="https://policies.google.com/privacy?hl=pt-BR">Política de Privacidade do Google</a>',
}

T = {
    "en": dict(h="Privacy Policy", eff="Effective date: 10 November 2026", sec=[
        ("", 'Tombalings ("the game") is a number game with Tombala and Bingo against cute computer rivals. It is made by Nesim Razon, an individual developer ("I", "me"). The game has no accounts; I do not sell any data and I do not operate servers for the game. Points in the game are only for fun: there is no real money, no betting and no real prizes.'),
        ("Your game and progress", "Your points, statistics, badges and settings are stored on your phone so you can continue later. If you sign in to Google Play Games, your progress counters (points, rounds, wins) are also saved to Google's cloud with Play Games Saved Games, tied to your Google Play Games profile, so you can continue on another phone; I cannot see it. If Android backup is turned on, Android may also include your data in your device backup to your Google account. Uninstalling the game or clearing its data deletes the data on your phone."),
        ("Voice caller (text-to-speech)", "The optional voice caller reads the drawn numbers aloud using the text-to-speech engine of your device. This happens on your device: the game does not record, send or store any speech or text. The speech engine itself is provided by your device (for example by Google) and is covered by its own privacy policy. You can turn the voice caller off in Settings."),
        ("Advertising (Google AdMob)", "The game is free and shows ads provided by Google AdMob: an occasional ad between rounds (never while you are playing a round). Gambling-related ads are blocked. To serve and measure ads and to prevent fraud, Google may collect and process information such as your device's advertising ID, IP address, approximate location derived from the IP address, device and app information, and how you interact with ads. Learn more in {ADS}. In the European Economic Area, the United Kingdom and Switzerland the game asks for your consent first; you can change your choice in the game under <strong>Settings → Privacy options</strong>."),
        ("Google Play Games", "If you choose to use Google Play Games, the game sends your scores (your total points and the number of Tombalas you won), the achievements you unlock and your saved progress to Google Play Games so that leaderboards, achievements and cloud save work. This is handled by Google under the {GP}. If you do not sign in, none of this is sent."),
        ("Purchases (Google Play Billing)", "The game offers one optional one-time purchase that removes ads. The payment is handled entirely by Google Play; I do not receive your payment details."),
        ("Usage statistics (Google Analytics for Firebase)", 'The game sends anonymous events to Google Analytics for Firebase, such as "a round started" or "a round ended" with the game mode, the number of cards and the points earned. They are linked to a random installation ID, not to you, and the advertising ID is not collected for analytics.'),
        ("Crash reports (Firebase Crashlytics)", "If the game crashes, it sends a technical crash report (error details, device model, Android and app version) linked to a random installation ID. It contains no personal information."),
        ("Children", "The game is not directed to children under 13, and I do not knowingly collect personal information from children. Ads are limited to content suitable for general audiences."),
        ("Your rights and changes", "Depending on where you live (for example under the GDPR, Brazil's LGPD or Turkey's KVKK), you may have rights over your personal data. Because I do not hold personal data about you, requests about advertising data should be made to Google. If this policy changes, the new version will be published on this page with a new effective date."),
    ], contact="Contact"),
    "tr": dict(h="Gizlilik Politikası", eff="Yürürlük tarihi: 10 Kasım 2026", sec=[
        ("", 'Tombalings ("oyun"), sevimli bilgisayar rakiplere karşı Tombala ve Bingo oynadığın bir sayı oyunudur. Bağımsız geliştirici Nesim Razon ("ben") tarafından yapılmıştır. Oyunda hesap yoktur; hiçbir veri satmıyorum ve oyun için sunucu kullanmıyorum. Oyundaki puanlar yalnızca eğlence içindir: gerçek para, bahis ve gerçek ödül yoktur.'),
        ("Oyunun ve ilerlemen", "Puanların, istatistiklerin, rozetlerin ve ayarların sonra devam edebilmen için telefonunda saklanır. Google Play Games'e giriş yaparsan ilerleme sayaçların (puanlar, turlar, kazanmalar) ayrıca Play Games Saved Games ile Google'ın bulutuna, Google Play Games profiline bağlı olarak kaydedilir; böylece başka bir telefonda devam edebilirsin. Bunu ben göremem. Android yedeklemesi açıksa Android verilerini Google hesabındaki cihaz yedeğine de ekleyebilir. Oyunu kaldırmak ya da verilerini silmek telefondaki verileri siler."),
        ("Sesli tellal (metin okuma)", "İsteğe bağlı sesli tellal, çekilen sayıları cihazının metin okuma motoruyla yüksek sesle okur. Bu, cihazında gerçekleşir: oyun hiçbir konuşmayı ya da metni kaydetmez, göndermez veya saklamaz. Metin okuma motorunu cihazın sağlar (örneğin Google) ve kendi gizlilik politikasına tabidir. Sesli tellalı Ayarlar'dan kapatabilirsin."),
        ("Reklamlar (Google AdMob)", "Oyun ücretsizdir ve Google AdMob reklamları gösterir: turlar arasında ara sıra bir reklam (tur oynarken asla). Kumarla ilgili reklamlar engellenir. Reklamları sunmak, ölçmek ve dolandırıcılığı önlemek için Google, cihazının reklam kimliği, IP adresi, IP adresinden çıkarılan yaklaşık konum, cihaz ve uygulama bilgileri ile reklamlarla etkileşimin gibi bilgileri toplayıp işleyebilir. Ayrıntılar: {ADS}. Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre'de oyun önce iznini ister; seçimini oyunda <strong>Ayarlar → Gizlilik seçenekleri</strong> bölümünden değiştirebilirsin."),
        ("Google Play Games", "Google Play Games'i kullanmayı seçersen oyun puanlarını (toplam puanın ve kazandığın tombala sayısı), açtığın başarımları ve kayıtlı ilerlemeni, liderlik tabloları, başarımlar ve bulut kaydı çalışsın diye Google Play Games'e gönderir. Bunu {GP} kapsamında Google yürütür. Giriş yapmazsan bunların hiçbiri gönderilmez."),
        ("Satın almalar (Google Play Faturalandırma)", "Oyun, reklamları kaldıran isteğe bağlı tek seferlik bir satın alma sunar. Ödeme tamamen Google Play tarafından yürütülür; ödeme bilgilerini ben almam."),
        ("Kullanım istatistikleri (Google Analytics for Firebase)", 'Oyun Google Analytics for Firebase\'e "tur başladı" ya da "tur bitti" (oyun modu, kart sayısı ve kazandığın puanla) gibi anonim olaylar gönderir. Olaylar sana değil, rastgele bir kurulum kimliğine bağlıdır; istatistikler için reklam kimliği toplanmaz.'),
        ("Çökme raporları (Firebase Crashlytics)", "Oyun bir hata yüzünden kapanırsa, rastgele bir kurulum kimliğine bağlı teknik bir çökme raporu (hata ayrıntıları, cihaz modeli, Android ve uygulama sürümü) gönderir. Kişisel bilgi içermez."),
        ("Çocuklar", "Oyun 13 yaş altı çocuklara yönelik değildir ve bilerek çocuklardan kişisel bilgi toplamam. Reklamlar genel izleyiciye uygun içerikle sınırlıdır."),
        ("Hakların ve değişiklikler", "Yaşadığın yere göre (örneğin KVKK veya GDPR kapsamında) kişisel verilerin üzerinde hakların olabilir. Sana ait kişisel veri tutmadığım için reklam verileriyle ilgili talepler Google'a yapılmalıdır. Bu politika değişirse yeni sürüm, yeni yürürlük tarihiyle bu sayfada yayınlanır."),
    ], contact="İletişim"),
    "es": dict(h="Política de privacidad", eff="Fecha de entrada en vigor: 10 de noviembre de 2026", sec=[
        ("", 'Tombalings («el juego») es un juego de números con Tómbola y Bingo contra simpáticos rivales controlados por el dispositivo. Lo ha creado Nesim Razon, desarrollador independiente («yo»). El juego no tiene cuentas; no vendo ningún dato y no uso servidores para el juego. Los puntos del juego son solo por diversión: no hay dinero real, apuestas ni premios reales.'),
        ("Tu juego y tu progreso", "Tus puntos, estadísticas, insignias y ajustes se guardan en tu teléfono para que puedas continuar más tarde. Si inicias sesión en Google Play Games, tus contadores de progreso (puntos, rondas, victorias) también se guardan en la nube de Google con Play Games Saved Games, vinculados a tu perfil de Google Play Games, para que puedas continuar en otro teléfono; yo no puedo verlos. Si la copia de seguridad de Android está activada, Android puede incluir tus datos en la copia de tu dispositivo en tu cuenta de Google. Desinstalar el juego o borrar sus datos elimina los datos del teléfono."),
        ("Locutor de voz (texto a voz)", "El locutor de voz opcional lee en voz alta los números sacados con el motor de texto a voz de tu dispositivo. Esto ocurre en tu dispositivo: el juego no graba, envía ni guarda ninguna voz ni texto. El motor de voz lo proporciona tu dispositivo (por ejemplo Google) y se rige por su propia política de privacidad. Puedes desactivar el locutor en Ajustes."),
        ("Publicidad (Google AdMob)", "El juego es gratuito y muestra anuncios de Google AdMob: un anuncio ocasional entre rondas (nunca mientras juegas una ronda). Los anuncios relacionados con juegos de azar están bloqueados. Para mostrar y medir anuncios y prevenir fraudes, Google puede recopilar y procesar información como el ID de publicidad de tu dispositivo, la dirección IP, la ubicación aproximada derivada de la IP, información del dispositivo y de la app, y cómo interactúas con los anuncios. Más información en {ADS}. En el Espacio Económico Europeo, el Reino Unido y Suiza el juego te pide primero tu consentimiento; puedes cambiar tu elección en el juego en <strong>Ajustes → Opciones de privacidad</strong>."),
        ("Google Play Games", "Si decides usar Google Play Games, el juego envía tus puntuaciones (tus puntos totales y el número de Tómbolas ganadas), los logros que desbloqueas y tu progreso guardado a Google Play Games para que funcionen las clasificaciones, los logros y el guardado en la nube. Lo gestiona Google conforme a la {GP}. Si no inicias sesión, no se envía nada de esto."),
        ("Compras (Google Play Billing)", "El juego ofrece una compra única y opcional que elimina los anuncios. El pago lo gestiona por completo Google Play; yo no recibo tus datos de pago."),
        ("Estadísticas de uso (Google Analytics for Firebase)", 'El juego envía eventos anónimos a Google Analytics for Firebase, como «una ronda empezó» o «una ronda terminó» con el modo de juego, el número de cartones y los puntos obtenidos. Están vinculados a un ID de instalación aleatorio, no a ti, y no se recopila el ID de publicidad para analítica.'),
        ("Informes de fallos (Firebase Crashlytics)", "Si el juego falla, envía un informe técnico (detalles del error, modelo del dispositivo, versión de Android y de la app) vinculado a un ID de instalación aleatorio. No contiene información personal."),
        ("Niños", "El juego no está dirigido a menores de 13 años y no recopilo a sabiendas datos personales de niños. Los anuncios se limitan a contenido apto para todos los públicos."),
        ("Tus derechos y cambios", "Según donde vivas (por ejemplo, conforme al RGPD, la LGPD de Brasil o la KVKK de Turquía), puedes tener derechos sobre tus datos personales. Como no conservo datos personales tuyos, las solicitudes sobre datos publicitarios deben dirigirse a Google. Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha de entrada en vigor."),
    ], contact="Contacto"),
    "pt": dict(h="Política de Privacidade", eff="Data de vigência: 10 de novembro de 2026", sec=[
        ("", 'O Tombalings ("o jogo") é um jogo de números com Tômbola e Bingo contra rivais fofos controlados pelo aparelho. Foi criado por Nesim Razon, desenvolvedor independente ("eu"). O jogo não tem contas; não vendo nenhum dado e não uso servidores para o jogo. Os pontos do jogo são apenas para diversão: não há dinheiro real, apostas nem prêmios reais.'),
        ("Seu jogo e seu progresso", "Seus pontos, estatísticas, conquistas e configurações ficam armazenados no seu telefone para você continuar depois. Se você entrar no Google Play Games, seus contadores de progresso (pontos, rodadas, vitórias) também são salvos na nuvem do Google com o Play Games Saved Games, vinculados ao seu perfil do Google Play Games, para você continuar em outro telefone; eu não consigo vê-los. Se o backup do Android estiver ativado, o Android pode incluir seus dados no backup do aparelho na sua conta Google. Desinstalar o jogo ou limpar seus dados apaga os dados do telefone."),
        ("Locutor de voz (texto para fala)", "O locutor de voz opcional lê em voz alta os números sorteados usando o mecanismo de texto para fala do seu aparelho. Isso acontece no seu aparelho: o jogo não grava, envia nem armazena nenhuma fala ou texto. O mecanismo de voz é fornecido pelo seu aparelho (por exemplo, pelo Google) e segue a própria política de privacidade. Você pode desativar o locutor em Configurações."),
        ("Publicidade (Google AdMob)", "O jogo é gratuito e mostra anúncios do Google AdMob: um anúncio ocasional entre rodadas (nunca enquanto você joga uma rodada). Anúncios relacionados a jogos de azar são bloqueados. Para exibir e medir anúncios e prevenir fraudes, o Google pode coletar e processar informações como o ID de publicidade do aparelho, o endereço IP, a localização aproximada derivada do IP, informações do aparelho e do app e como você interage com os anúncios. Saiba mais em {ADS}. No Espaço Econômico Europeu, no Reino Unido e na Suíça, o jogo pede seu consentimento primeiro; você pode mudar sua escolha no jogo em <strong>Configurações → Opções de privacidade</strong>."),
        ("Google Play Games", "Se você optar por usar o Google Play Games, o jogo envia suas pontuações (seus pontos totais e o número de Tômbolas vencidas), as conquistas que você desbloqueia e seu progresso salvo ao Google Play Games para que as classificações, as conquistas e o salvamento na nuvem funcionem. Isso é tratado pelo Google conforme a {GP}. Se você não entrar, nada disso é enviado."),
        ("Compras (Google Play Billing)", "O jogo oferece uma compra única e opcional que remove os anúncios. O pagamento é tratado inteiramente pelo Google Play; eu não recebo seus dados de pagamento."),
        ("Estatísticas de uso (Google Analytics for Firebase)", 'O jogo envia eventos anônimos ao Google Analytics for Firebase, como "uma rodada começou" ou "uma rodada terminou" com o modo de jogo, o número de cartelas e os pontos ganhos. Eles ficam vinculados a um ID de instalação aleatório, não a você, e o ID de publicidade não é coletado para estatísticas.'),
        ("Relatórios de falhas (Firebase Crashlytics)", "Se o jogo travar, ele envia um relatório técnico (detalhes do erro, modelo do aparelho, versão do Android e do app) vinculado a um ID de instalação aleatório. Não contém informações pessoais."),
        ("Crianças", "O jogo não é direcionado a menores de 13 anos e não coleto conscientemente informações pessoais de crianças. Os anúncios são limitados a conteúdo adequado ao público geral."),
        ("Seus direitos e alterações", "Dependendo de onde você mora (por exemplo, pela GDPR, pela LGPD do Brasil ou pela KVKK da Turquia), você pode ter direitos sobre seus dados pessoais. Como não guardo dados pessoais seus, pedidos sobre dados de publicidade devem ser feitos ao Google. Se esta política mudar, a nova versão será publicada nesta página com uma nova data de vigência."),
    ], contact="Contato"),
}

out = [head]
for lang in ("en", "tr", "es", "pt"):
    d = T[lang]
    out.append(f'  <section id="{lang}" lang="{lang}">\n    <h2>{d["h"]}</h2>\n    <p class="meta">{d["eff"]}</p>')
    for title, body in d["sec"]:
        body = body.replace("{ADS}", GOOGLE_ADS[lang]).replace("{GP}", GPRIV[lang])
        if title:
            out.append(f"    <h3>{title}</h3>")
        out.append(f"    <p>{body}</p>")
    out.append(f'    <h3>{d["contact"]}</h3>\n    <p>Nesim Razon · <a href="mailto:nesim.razon@gmail.com">nesim.razon@gmail.com</a></p>\n  </section>')
out.append(tail)
html = "\n".join(out)
for bad in ("pentomino", "Pentolings", "Düşür", "More games", "Diğer oyunlarım", "level", "bölüm", "nivel", "nível"):
    if bad in html:
        print("UYARI: kalinti:", bad)
dst = os.path.join(G, "tombalings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(html)
print("ok", os.path.join(dst, "privacy.html"))
