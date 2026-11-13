# -*- coding: utf-8 -*-
"""Pulselings gizlilik sayfasini (pulselings/privacy.html) uretir: baslik/stil/gezinme Pentolings sayfasindan, metinler 4 dilde burada.
Hizmetler: AdMob (yalniz banner) + UMP, Firebase Analytics/Crashlytics (saglik verisi GONDERILMEZ), Play uygulama ici guncelleme.
Play Games, Billing, "Diger oyunlarim" YOK. Calistir: py -3 -X utf8 tools/gen_privacy_pulselings.py"""
import io, os

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
src = io.open(os.path.join(G, "pentolings", "privacy.html"), encoding="utf-8").read()
head = src[:src.index('  <section id="en"')]
head = head.replace("Pentolings", "Pulselings").replace("pentolings", "pulselings")
head = head.replace("--bg:#1B1838; --card:#2A2350; --text:#F3EFFA; --dim:#D9CCFF; --accent:#FFC857; --link:#B7A4FF;",
                    "--bg:#FFF7F3; --card:#FFFFFF; --text:#3B2740; --dim:#7A6A80; --accent:#E0405F; --link:#C2304F;")
tail = src[src.rindex("</section>") + len("</section>"):]

GOOGLE_ADS = {
    "en": '<a href="https://policies.google.com/technologies/partner-sites">How Google uses information from sites or apps that use its services</a> and the <a href="https://policies.google.com/privacy">Google Privacy Policy</a> explain more.',
    "tr": '<a href="https://policies.google.com/technologies/partner-sites?hl=tr">Google, hizmetlerini kullanan sitelerden veya uygulamalardan gelen bilgileri nasıl kullanır</a> ve <a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a> daha fazlasını anlatır.',
    "es": '<a href="https://policies.google.com/technologies/partner-sites?hl=es">Cómo usa Google la información de sitios o aplicaciones que utilizan sus servicios</a> y la <a href="https://policies.google.com/privacy?hl=es">Política de Privacidad de Google</a> lo explican con más detalle.',
    "pt": '<a href="https://policies.google.com/technologies/partner-sites?hl=pt-BR">Como o Google usa informações de sites ou apps que usam seus serviços</a> e a <a href="https://policies.google.com/privacy?hl=pt-BR">Política de Privacidade do Google</a> explicam mais.',
}

T = {
    "en": dict(h="Privacy Policy", eff="Effective date: 13 November 2026", sec=[
        ("", 'Pulselings ("the app") lets you check your resting pulse with your phone\'s camera and flash. It is made by Nesim Razon, an individual developer ("I", "me"). The app has no accounts; I do not sell any data and I do not run servers that store your measurements. This page explains what the app does with information.'),
        ("Camera and flash", "The app uses the camera and the flash only while you measure, to see tiny colour changes in your fingertip. The camera images are analysed on your phone in real time and are never saved, recorded or sent anywhere."),
        ("Your measurements", "Your pulse measurements, tags and history are stored only on your phone, so I cannot see them. Your personal baseline and the balance label are calculated on your phone. You can delete one measurement (History) or all your data (Settings) at any time; uninstalling the app also removes them. Your measurements and health information are not shared with Google, advertisers or analytics."),
        ("Advertising (Google AdMob)", "The app is free and shows a small banner ad provided by Google AdMob, only on the home and history screens. There are no ads while you measure, see your result or breathe. To serve and measure ads, AdMob may use your device's advertising identifier and similar technologies. In regions such as the European Economic Area, the UK and Switzerland, you are first asked for consent with Google's consent form, and you can change your choice later in Settings (Ad choices). Your measurements and health information are never used or shared for advertising. Ad content is limited to material suitable for general audiences. {ADS}"),
        ("Usage statistics (Google Analytics for Firebase)", 'The app sends anonymous usage events to Google Analytics for Firebase, such as "a measurement started, finished or failed", how long it took, the signal quality as a percentage, and whether the how-to or the breathing exercise was opened. These events never include your pulse value, your history, your tags or any other health information. They are linked to a random installation ID, not to your identity, and the advertising ID is not collected by Analytics. {GP}'),
        ("Crash reports (Firebase Crashlytics)", "If the app crashes, it sends a technical crash report (error details, device model, Android and app version) linked to a random installation ID. It contains no measurements and no personal information."),
        ("App updates (Google Play)", "The app may ask Google Play whether a new version is available and offer to install it. This is handled by Google Play."),
        ("Not a medical device", "Pulselings is a general wellness app. Its results are estimates, not medical measurements, and it does not diagnose, treat, cure or prevent any condition. For medical advice, talk to a healthcare professional."),
        ("Children", "The app is not directed to children under 13, and I do not knowingly collect personal information from children."),
        ("Your rights and changes", "Depending on where you live (for example under the GDPR, Brazil's LGPD or Turkey's KVKK), you may have rights over your personal data. Because I do not hold personal data about you, requests about advertising data are best made to Google. If this policy changes, the new version will be published on this page with a new effective date."),
    ], contact="Contact"),
    "tr": dict(h="Gizlilik Politikası", eff="Yürürlük tarihi: 13 Kasım 2026", sec=[
        ("", 'Pulselings ("uygulama"), telefonunun kamerası ve flaşıyla dinlenik nabzını kontrol etmeni sağlar. Bağımsız geliştirici Nesim Razon ("ben") tarafından yapılmıştır. Uygulamada hesap yoktur; hiçbir veriyi satmam ve ölçümlerini saklayan sunucu işletmem. Bu sayfa, uygulamanın bilgilerle ne yaptığını anlatır.'),
        ("Kamera ve flaş", "Uygulama kamerayı ve flaşı yalnızca ölçüm yaparken, parmak ucundaki küçük renk değişimlerini görmek için kullanır. Kamera görüntüleri telefonunda anlık olarak işlenir; hiçbir zaman kaydedilmez, saklanmaz ya da bir yere gönderilmez."),
        ("Ölçümlerin", "Nabız ölçümlerin, etiketlerin ve geçmişin yalnızca telefonunda saklanır; bu yüzden onları göremem. Kişisel baz çizgin ve denge etiketi telefonunda hesaplanır. Bir ölçümü (Geçmiş) ya da tüm verilerini (Ayarlar) istediğin an silebilirsin; uygulamayı kaldırmak da onları siler. Ölçümlerin ve sağlık bilgilerin Google'la, reklam verenlerle ya da analizle paylaşılmaz."),
        ("Reklamlar (Google AdMob)", "Uygulama ücretsizdir ve yalnızca ana ekranda ve geçmişte Google AdMob'un sunduğu küçük bir banner reklam gösterir. Ölçüm yaparken, sonucu görürken ya da nefes alırken reklam yoktur. Reklamları sunmak ve ölçmek için AdMob cihazının reklam kimliğini ve benzer teknolojileri kullanabilir. Avrupa Ekonomik Alanı, Birleşik Krallık ve İsviçre gibi bölgelerde önce Google'ın onay formuyla izin istenir; seçimini sonra Ayarlar'dan (Reklam tercihleri) değiştirebilirsin. Ölçümlerin ve sağlık bilgilerin reklam için asla kullanılmaz ya da paylaşılmaz. Reklam içeriği genel izleyiciye uygun materyalle sınırlıdır. {ADS}"),
        ("Kullanım istatistikleri (Google Analytics for Firebase)", 'Uygulama Google Analytics for Firebase\'e "ölçüm başladı, bitti ya da başarısız oldu", ne kadar sürdüğü, sinyal kalitesi (yüzde olarak) ve rehberin ya da nefes egzersizinin açılıp açılmadığı gibi anonim kullanım olayları gönderir. Bu olaylar nabız değerini, geçmişini, etiketlerini ya da başka hiçbir sağlık bilgisini içermez. Kimliğine değil, rastgele bir kurulum kimliğine bağlıdır; reklam kimliği Analytics tarafından toplanmaz. {GP}'),
        ("Çökme raporları (Firebase Crashlytics)", "Uygulama bir hata yüzünden kapanırsa, rastgele bir kurulum kimliğine bağlı teknik bir çökme raporu (hata ayrıntıları, cihaz modeli, Android ve uygulama sürümü) gönderir. Ölçüm ya da kişisel bilgi içermez."),
        ("Uygulama güncellemeleri (Google Play)", "Uygulama, Google Play'e yeni sürüm olup olmadığını sorabilir ve kurmayı önerebilir. Bunu Google Play yürütür."),
        ("Tıbbi cihaz değildir", "Pulselings genel bir sağlıklı yaşam uygulamasıdır. Sonuçları tahmindir, tıbbi ölçüm değildir; hiçbir durumu teşhis etmez, tedavi etmez, iyileştirmez ve önlemez. Tıbbi tavsiye için bir sağlık uzmanına danışın."),
        ("Çocuklar", "Uygulama 13 yaş altı çocuklara yönelik değildir ve bilerek çocuklardan kişisel bilgi toplamam."),
        ("Hakların ve değişiklikler", "Yaşadığın yere göre (örneğin KVKK veya GDPR kapsamında) kişisel verilerin üzerinde hakların olabilir. Sana ait kişisel veri tutmadığım için reklam verileriyle ilgili talepleri en iyi Google'a iletebilirsin. Bu politika değişirse yeni sürüm bu sayfada yeni bir yürürlük tarihiyle yayımlanır."),
    ], contact="İletişim"),
    "es": dict(h="Política de privacidad", eff="Fecha de entrada en vigor: 13 de noviembre de 2026", sec=[
        ("", 'Pulselings («la app») te permite revisar tu pulso en reposo con la cámara y el flash de tu teléfono. Lo ha creado Nesim Razon, desarrollador independiente («yo»). La app no tiene cuentas; no vendo ningún dato y no gestiono servidores que guarden tus mediciones. Esta página explica qué hace la app con la información.'),
        ("Cámara y flash", "La app usa la cámara y el flash solo mientras mides, para ver pequeños cambios de color en la yema del dedo. Las imágenes de la cámara se analizan en tu teléfono en tiempo real y nunca se guardan, graban ni envían a ningún sitio."),
        ("Tus mediciones", "Tus mediciones de pulso, etiquetas e historial se guardan solo en tu teléfono, así que no puedo verlos. Tu referencia personal y la etiqueta de equilibrio se calculan en tu teléfono. Puedes eliminar una medición (Historial) o todos tus datos (Ajustes) cuando quieras; al desinstalar la app también se eliminan. Tus mediciones y tu información de salud no se comparten con Google, anunciantes ni analítica."),
        ("Publicidad (Google AdMob)", "La app es gratuita y muestra un pequeño banner de Google AdMob, solo en la pantalla de inicio y en el historial. No hay anuncios mientras mides, ves tu resultado o respiras. Para mostrar y medir anuncios, AdMob puede usar el identificador publicitario de tu dispositivo y tecnologías similares. En regiones como el Espacio Económico Europeo, el Reino Unido y Suiza, primero se te pide consentimiento con el formulario de Google, y puedes cambiar tu elección más tarde en Ajustes (Preferencias de anuncios). Tus mediciones y tu información de salud nunca se usan ni se comparten con fines publicitarios. El contenido de los anuncios se limita a material apto para todos los públicos. {ADS}"),
        ("Estadísticas de uso (Google Analytics for Firebase)", 'La app envía eventos de uso anónimos a Google Analytics for Firebase, como «una medición empezó, terminó o falló», cuánto tardó, la calidad de la señal en porcentaje y si se abrió la guía o el ejercicio de respiración. Estos eventos nunca incluyen tu valor de pulso, tu historial, tus etiquetas ni ninguna otra información de salud. Están vinculados a un ID de instalación aleatorio, no a tu identidad, y Analytics no recopila el ID de publicidad. {GP}'),
        ("Informes de fallos (Firebase Crashlytics)", "Si la app falla, envía un informe técnico (detalles del error, modelo del dispositivo, versión de Android y de la app) vinculado a un ID de instalación aleatorio. No contiene mediciones ni información personal."),
        ("Actualizaciones de la app (Google Play)", "La app puede preguntar a Google Play si hay una versión nueva y ofrecer instalarla. Lo gestiona Google Play."),
        ("No es un dispositivo médico", "Pulselings es una app general de bienestar. Sus resultados son estimaciones, no mediciones médicas, y no diagnostica, trata, cura ni previene ninguna afección. Para consejo médico, consulta a un profesional de la salud."),
        ("Niños", "La app no está dirigida a menores de 13 años y no recopilo a sabiendas datos personales de niños."),
        ("Tus derechos y cambios", "Según donde vivas (por ejemplo, conforme al RGPD, la LGPD de Brasil o la KVKK de Turquía), puedes tener derechos sobre tus datos personales. Como no conservo datos personales tuyos, las solicitudes sobre datos publicitarios es mejor dirigirlas a Google. Si esta política cambia, la nueva versión se publicará en esta página con una nueva fecha de entrada en vigor."),
    ], contact="Contacto"),
    "pt": dict(h="Política de Privacidade", eff="Data de vigência: 13 de novembro de 2026", sec=[
        ("", 'O Pulselings ("o app") permite verificar sua pulsação em repouso com a câmera e o flash do celular. Foi criado por Nesim Razon, desenvolvedor independente ("eu"). O app não tem contas; não vendo nenhum dado e não mantenho servidores que armazenem suas medições. Esta página explica o que o app faz com as informações.'),
        ("Câmera e flash", "O app usa a câmera e o flash apenas enquanto você mede, para ver pequenas mudanças de cor na ponta do dedo. As imagens da câmera são analisadas no seu celular em tempo real e nunca são salvas, gravadas nem enviadas a lugar nenhum."),
        ("Suas medições", "Suas medições de pulsação, etiquetas e histórico ficam armazenados apenas no seu celular, então não posso vê-los. Sua referência pessoal e o rótulo de equilíbrio são calculados no seu celular. Você pode excluir uma medição (Histórico) ou todos os seus dados (Configurações) a qualquer momento; desinstalar o app também os remove. Suas medições e informações de saúde não são compartilhadas com o Google, anunciantes nem análises."),
        ("Publicidade (Google AdMob)", "O app é gratuito e mostra um pequeno banner do Google AdMob, apenas na tela inicial e no histórico. Não há anúncios enquanto você mede, vê o resultado ou respira. Para exibir e medir anúncios, o AdMob pode usar o identificador de publicidade do seu aparelho e tecnologias semelhantes. Em regiões como o Espaço Econômico Europeu, o Reino Unido e a Suíça, primeiro é pedido consentimento com o formulário do Google, e você pode mudar sua escolha depois em Configurações (Preferências de anúncios). Suas medições e informações de saúde nunca são usadas nem compartilhadas para publicidade. O conteúdo dos anúncios é limitado a material adequado ao público geral. {ADS}"),
        ("Estatísticas de uso (Google Analytics for Firebase)", 'O app envia eventos de uso anônimos ao Google Analytics for Firebase, como "uma medição começou, terminou ou falhou", quanto tempo levou, a qualidade do sinal em porcentagem e se o guia ou o exercício de respiração foi aberto. Esses eventos nunca incluem seu valor de pulsação, seu histórico, suas etiquetas nem qualquer outra informação de saúde. Ficam vinculados a um ID de instalação aleatório, não à sua identidade, e o ID de publicidade não é coletado pelo Analytics. {GP}'),
        ("Relatórios de falhas (Firebase Crashlytics)", "Se o app travar, ele envia um relatório técnico (detalhes do erro, modelo do aparelho, versão do Android e do app) vinculado a um ID de instalação aleatório. Não contém medições nem informações pessoais."),
        ("Atualizações do app (Google Play)", "O app pode perguntar ao Google Play se há uma nova versão e oferecer a instalação. Isso é tratado pelo Google Play."),
        ("Não é um dispositivo médico", "O Pulselings é um app geral de bem-estar. Seus resultados são estimativas, não medições médicas, e ele não diagnostica, trata, cura nem previne nenhuma condição. Para orientação médica, consulte um profissional de saúde."),
        ("Crianças", "O app não é direcionado a menores de 13 anos e não coleto conscientemente informações pessoais de crianças."),
        ("Seus direitos e alterações", "Dependendo de onde você mora (por exemplo, pela GDPR, pela LGPD do Brasil ou pela KVKK da Turquia), você pode ter direitos sobre seus dados pessoais. Como não guardo dados pessoais seus, pedidos sobre dados de publicidade são mais bem feitos ao Google. Se esta política mudar, a nova versão será publicada nesta página com uma nova data de vigência."),
    ], contact="Contato"),
}

GPRIV = {
    "en": '<a href="https://policies.google.com/privacy">Google Privacy Policy</a>',
    "tr": '<a href="https://policies.google.com/privacy?hl=tr">Google Gizlilik Politikası</a>',
    "es": '<a href="https://policies.google.com/privacy?hl=es">Política de Privacidad de Google</a>',
    "pt": '<a href="https://policies.google.com/privacy?hl=pt-BR">Política de Privacidade do Google</a>',
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
for bad in ("pentomino", "Pentolings", "Düşür", "More games", "Diğer oyunlarım", "level", "bölüm", "nivel", "nível", "Play Games", "Billing"):
    if bad in html:
        print("UYARI: kalinti:", bad)
dst = os.path.join(G, "pulselings")
os.makedirs(dst, exist_ok=True)
io.open(os.path.join(dst, "privacy.html"), "w", encoding="utf-8", newline="\n").write(html)
print("ok", os.path.join(dst, "privacy.html"))
