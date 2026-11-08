# -*- coding: utf-8 -*-
"""Her uygulama/oyun için <slug>/terms.html (Kullanim Sartlari) uretir.
Tema (CSS) ve dil seti uygulamanin kendi privacy.html'inden alinir. Calistir: py -3 tools/gen_terms.py
Calisan/Hafta Sonum/Uzay Gunlugu'nde sartlar zaten privacy.html#kosullar icinde: bunlar atlanir."""
import io, os, re, sys

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATE = {"en": "4 November 2026", "tr": "4 Kasım 2026", "es": "4 de noviembre de 2026", "pt": "4 de novembro de 2026"}
MAIL = "nesim.razon@gmail.com"

# slug: (ad, tur, reklam, uygulama ici satin alma, play games, ozel not anahtari)
APPS = {
    "sliplines": ("Sliplines", "game", True, False, True, None),
    "game2048": ("2048", "game", True, False, True, None),
    "tictactoe": ("Tic-Tac-Toe", "game", True, False, False, None),
    "cubbles": ("Cubbles", "game", True, False, True, None),
    "cardles": ("Cardles", "game", True, False, True, None),
    "beamies": ("Beamies: Beam Home", "game", True, True, True, None),
    "logiclings": ("Logiclings", "game", True, True, True, None),
    "tilelings": ("Tilelings", "game", True, True, True, None),
    "grumblings": ("Grumblings", "game", True, True, True, None),
    "nudgelings": ("Nudgelings", "game", True, True, True, None),
    "astrolings": ("Astrolings", "app", True, True, False, "astro"),
    "nuzzlings": ("Nuzzlings", "game", False, True, True, "pet"),
    "sansoyunlari": ("Şans Oyunları", "app", True, False, False, "lottery"),
    "sondepremler": ("Son Depremler", "app", True, False, False, "quake"),
    "whereami": ("Where Am I?", "app", True, False, False, "location"),
    "agecalculator": ("Age Calculator", "app", True, False, False, None),
    "bmicalculator": ("BMI Calculator", "app", True, False, False, "health"),
    "anthemturkey": ("National Anthem of Turkey", "app", True, False, False, "media"),
    "anthemcanada": ("National Anthem of Canada", "app", True, False, False, "media"),
    "turksail": ("TurkSail", "app", False, False, False, "rss"),
    "medyafobi": ("MedyaFobi", "app", False, False, False, "rss"),
}

T = {}  # metin parcalari: T[anahtar][dil]
T["h"] = {"en": "Terms of Use", "tr": "Kullanım Şartları", "es": "Términos de uso", "pt": "Termos de Uso"}
T["eff"] = {"en": "Effective date", "tr": "Yürürlük tarihi", "es": "Fecha de entrada en vigor", "pt": "Data de vigência"}
T["intro"] = {
    "en": "These terms apply to {name} (\"the {kind}\"), made by Nesim Razon, an individual developer (\"I\", \"me\"). By installing or using the {kind} you accept them. If you do not agree, please do not use it.",
    "tr": "Bu şartlar, bireysel geliştirici Nesim Razon (\"ben\") tarafından yapılan {name} ({kind}) için geçerlidir. {kind_acc} yükleyerek veya kullanarak bu şartları kabul etmiş olursunuz. Kabul etmiyorsanız lütfen kullanmayın.",
    "es": "Estos términos se aplican a {name} («{kind}»), creado por Nesim Razon, desarrollador individual («yo»). Al instalar o usar {kind_def} aceptas estos términos. Si no estás de acuerdo, no lo uses.",
    "pt": "Estes termos se aplicam a {name} (\"{kind}\"), criado por Nesim Razon, desenvolvedor individual (\"eu\"). Ao instalar ou usar {kind_def} você aceita estes termos. Se não concordar, não use.",
}
KIND = {
    "en": {"game": "game", "app": "app"},
    "tr": {"game": "oyun", "app": "uygulama"},
    "es": {"game": "juego", "app": "aplicación"},
    "pt": {"game": "jogo", "app": "aplicativo"},
}
KIND_ACC = {"tr": {"game": "Oyunu", "app": "Uygulamayı"}}
KIND_DEF = {"es": {"game": "el juego", "app": "la aplicación"}, "pt": {"game": "o jogo", "app": "o aplicativo"}}

SEC = []  # (baslik dict, govde dict | callable)
SEC.append(({"en": "Using the {kind}", "tr": "Kullanım", "es": "Uso", "pt": "Uso"},
            {"en": "I grant you a personal, non-exclusive, non-transferable licence to use the {kind} on your own devices for non-commercial purposes. Please do not copy, resell or redistribute it, reverse engineer it (except where the law allows it), or use it to cheat leaderboards, harm other people or break the law.",
             "tr": "Size, {kind_gen} kendi cihazlarınızda ticari olmayan amaçlarla kullanmanız için kişisel, devredilemez ve münhasır olmayan bir kullanım hakkı veriyorum. Lütfen kopyalamayın, yeniden satmayın veya dağıtmayın, (yasaların izin verdiği haller dışında) tersine mühendislik yapmayın; skor tablolarında hile, başkalarına zarar verme ya da yasa dışı amaçlarla kullanmayın.",
             "es": "Te concedo una licencia personal, no exclusiva e intransferible para usar {kind_def} en tus propios dispositivos con fines no comerciales. No lo copies, revendas ni redistribuyas, no hagas ingeniería inversa (salvo donde la ley lo permita) ni lo uses para hacer trampas en clasificaciones, dañar a otras personas o infringir la ley.",
             "pt": "Concedo a você uma licença pessoal, não exclusiva e intransferível para usar {kind_def} nos seus próprios dispositivos para fins não comerciais. Não copie, revenda ou redistribua, não faça engenharia reversa (exceto quando a lei permitir) nem use para trapacear em placares, prejudicar outras pessoas ou violar a lei."}))

ADS = ({"en": "Ads", "tr": "Reklamlar", "es": "Anuncios", "pt": "Anúncios"},
       {"en": "The {kind} is free and is supported by ads from Google AdMob. How ads and your data are handled is described in the Privacy Policy. I do not control which ads are shown; if you see an ad you find inappropriate, you can report it to Google.",
        "tr": "{kind_nom} ücretsizdir ve Google AdMob reklamlarıyla desteklenir. Reklamların ve verilerinizin nasıl işlendiği Gizlilik Politikası'nda anlatılmıştır. Hangi reklamların gösterileceğini ben belirlemiyorum; uygunsuz bir reklam görürseniz Google'a bildirebilirsiniz.",
        "es": "{kind_def_cap} es gratuito y se financia con anuncios de Google AdMob. En la Política de privacidad se describe cómo se tratan los anuncios y tus datos. No controlo qué anuncios se muestran; si ves uno inapropiado, puedes informar a Google.",
        "pt": "{kind_def_cap} é gratuito e é mantido por anúncios do Google AdMob. A Política de Privacidade descreve como os anúncios e seus dados são tratados. Não controlo quais anúncios são exibidos; se vir algum inadequado, você pode denunciá-lo ao Google."})

IAP = ({"en": "In-app purchases", "tr": "Uygulama içi satın alma", "es": "Compras dentro de la aplicación", "pt": "Compras no aplicativo"},
       {"en": "Optional in-app purchases (for example removing ads) are processed by Google Play. Prices are shown in the store in your currency. Purchases are tied to your Google account and can be restored on another device with the same account. Refunds are handled under Google Play's refund policy.",
        "tr": "İsteğe bağlı uygulama içi satın almalar (örneğin reklamları kaldırma) Google Play tarafından işlenir. Fiyatlar mağazada kendi para biriminizde görünür. Satın alımlar Google hesabınıza bağlıdır ve aynı hesapla başka bir cihazda geri yüklenebilir. İadeler Google Play'in iade politikasına göre yapılır.",
        "es": "Las compras opcionales dentro de la aplicación (por ejemplo, quitar los anuncios) las procesa Google Play. Los precios aparecen en la tienda en tu moneda. Las compras están vinculadas a tu cuenta de Google y pueden restaurarse en otro dispositivo con la misma cuenta. Los reembolsos se rigen por la política de reembolsos de Google Play.",
        "pt": "As compras opcionais no aplicativo (por exemplo, remover anúncios) são processadas pelo Google Play. Os preços aparecem na loja na sua moeda. As compras ficam vinculadas à sua conta Google e podem ser restauradas em outro dispositivo com a mesma conta. Os reembolsos seguem a política de reembolso do Google Play."})

PGS = ({"en": "Google Play Games", "tr": "Google Play Games", "es": "Google Play Juegos", "pt": "Google Play Games"},
       {"en": "Leaderboards, achievements and cloud save use Google Play Games and are optional. They are subject to Google's own terms. Progress saved in the cloud depends on Google's service and I cannot guarantee it will always be available or restorable.",
        "tr": "Skor tabloları, başarımlar ve bulut kaydı Google Play Games'i kullanır ve isteğe bağlıdır; Google'ın kendi şartlarına tabidir. Bulutta saklanan ilerleme Google'ın hizmetine bağlıdır; her zaman erişilebilir ya da geri yüklenebilir olacağını garanti edemem.",
        "es": "Las clasificaciones, los logros y el guardado en la nube usan Google Play Juegos y son opcionales; se rigen por los términos de Google. El progreso guardado en la nube depende del servicio de Google y no puedo garantizar que siempre esté disponible o se pueda restaurar.",
        "pt": "Placares, conquistas e salvamento na nuvem usam o Google Play Games e são opcionais; seguem os termos do próprio Google. O progresso salvo na nuvem depende do serviço do Google e não posso garantir que esteja sempre disponível ou possa ser restaurado."})

NOTES = {
    "astro": ({"en": "Entertainment only", "tr": "Yalnızca eğlence amaçlı", "es": "Solo entretenimiento", "pt": "Apenas entretenimento"},
              {"en": "The readings, ratings and texts in the app are written for entertainment. They are not predictions, are not scientifically proven and are not medical, financial, legal or any other professional advice. Please do not base important decisions on them.",
               "tr": "Uygulamadaki yorumlar, puanlar ve metinler eğlence amacıyla yazılmıştır. Öngörü değildir, bilimsel olarak kanıtlanmış değildir; tıbbi, mali, hukuki ya da başka bir profesyonel tavsiye de değildir. Lütfen önemli kararlarını bunlara dayandırma.",
               "es": "Las lecturas, puntuaciones y textos de la app están escritos con fines de entretenimiento. No son predicciones, no están demostrados científicamente y no constituyen asesoramiento médico, financiero, legal ni profesional de ningún tipo. Por favor, no bases decisiones importantes en ellos.",
               "pt": "As leituras, pontuações e textos do app são escritos para entretenimento. Não são previsões, não são comprovados cientificamente e não constituem aconselhamento médico, financeiro, jurídico ou profissional de qualquer tipo. Por favor, não baseie decisões importantes neles."}),
    "lottery": ({"en": "Results information", "tr": "Sonuç bilgisi", "es": "Información de resultados", "pt": "Informação de resultados"},
                {"en": "The app only shows draw results for information. It is not a gambling service, does not sell tickets and is not affiliated with any lottery operator. Results are taken from a third-party source; always check the official operator for the final result.",
                 "tr": "Uygulama yalnızca bilgi amacıyla çekiliş sonuçlarını gösterir. Bir kumar hizmeti değildir, bilet satmaz ve hiçbir şans oyunu işletmecisiyle bağlantılı değildir. Sonuçlar üçüncü taraf bir kaynaktan alınır; kesin sonuç için her zaman resmi işletmeciyi kontrol edin.",
                 "es": "La aplicación solo muestra resultados de sorteos con fines informativos. No es un servicio de juego, no vende boletos ni está afiliada a ningún operador de lotería. Los resultados provienen de una fuente de terceros; consulta siempre al operador oficial para el resultado definitivo.",
                 "pt": "O aplicativo apenas exibe resultados de sorteios para fins informativos. Não é um serviço de apostas, não vende bilhetes e não é afiliado a nenhum operador de loteria. Os resultados vêm de uma fonte de terceiros; consulte sempre o operador oficial para o resultado definitivo."}),
    "quake": ({"en": "Earthquake data", "tr": "Deprem verileri", "es": "Datos de terremotos", "pt": "Dados de terremotos"},
              {"en": "Earthquake information comes from public third-party sources and may be delayed, incomplete or revised. The app is not an official warning or early-warning system and must not be relied on for safety decisions. Follow official institutions (such as AFAD and Kandilli) in an emergency.",
               "tr": "Deprem bilgileri herkese açık üçüncü taraf kaynaklardan gelir; gecikmeli, eksik olabilir veya sonradan düzeltilebilir. Uygulama resmi bir uyarı ya da erken uyarı sistemi değildir; güvenlikle ilgili kararlarda buna güvenilmemelidir. Acil durumda resmi kurumları (AFAD, Kandilli vb.) takip edin.",
               "es": "La información sobre terremotos procede de fuentes públicas de terceros y puede llegar con retraso, estar incompleta o revisarse. La aplicación no es un sistema oficial de alerta y no debe usarse para decisiones de seguridad. En una emergencia, sigue a las instituciones oficiales (como AFAD y Kandilli).",
               "pt": "As informações sobre terremotos vêm de fontes públicas de terceiros e podem atrasar, ficar incompletas ou ser revisadas. O aplicativo não é um sistema oficial de alerta e não deve ser usado para decisões de segurança. Em uma emergência, siga as instituições oficiais (como AFAD e Kandilli)."}),
    "location": ({"en": "Location accuracy", "tr": "Konum doğruluğu", "es": "Precisión de la ubicación", "pt": "Precisão da localização"},
                 {"en": "Location and address results depend on your device, signal and Google's services and can be inaccurate. Do not rely on the app for navigation or in an emergency.",
                  "tr": "Konum ve adres sonuçları cihazınıza, sinyale ve Google hizmetlerine bağlıdır; hatalı olabilir. Uygulamaya navigasyon için ya da acil durumda güvenmeyin.",
                  "es": "Los resultados de ubicación y dirección dependen de tu dispositivo, la señal y los servicios de Google y pueden ser inexactos. No dependas de la aplicación para navegar ni en una emergencia.",
                  "pt": "Os resultados de localização e endereço dependem do seu dispositivo, do sinal e dos serviços do Google e podem ser imprecisos. Não dependa do aplicativo para navegação ou em emergências."}),
    "health": ({"en": "Not medical advice", "tr": "Tıbbi tavsiye değildir", "es": "No es consejo médico", "pt": "Não é aconselhamento médico"},
               {"en": "BMI and related results are general information only and are not medical advice, a diagnosis or a treatment recommendation. Talk to a doctor or dietitian about your health.",
                "tr": "VKİ ve ilgili sonuçlar yalnızca genel bilgidir; tıbbi tavsiye, teşhis ya da tedavi önerisi değildir. Sağlığınızla ilgili olarak bir doktora veya diyetisyene danışın.",
                "es": "El IMC y los resultados relacionados son solo información general y no constituyen consejo médico, diagnóstico ni recomendación de tratamiento. Consulta a un médico o dietista sobre tu salud.",
                "pt": "O IMC e os resultados relacionados são apenas informações gerais e não constituem aconselhamento médico, diagnóstico ou recomendação de tratamento. Consulte um médico ou nutricionista sobre sua saúde."}),
    "media": ({"en": "Third-party material", "tr": "Üçüncü taraf içerik", "es": "Material de terceros", "pt": "Material de terceiros"},
              {"en": "Recordings, flags and other third-party material shown in the app remain the property of their respective owners.",
               "tr": "Uygulamada gösterilen kayıtlar, bayraklar ve diğer üçüncü taraf içerikler ilgili sahiplerinin malıdır.",
               "es": "Las grabaciones, banderas y otro material de terceros que se muestra en la aplicación siguen siendo propiedad de sus respectivos titulares.",
               "pt": "Gravações, bandeiras e outros materiais de terceiros exibidos no aplicativo continuam sendo propriedade de seus respectivos titulares."}),
    "rss": ({"en": "Website content", "tr": "Site içeriği", "es": "Contenido del sitio web", "pt": "Conteúdo do site"},
            {"en": "The app is an independent reader for the website's public news feed. The articles, images and trademarks belong to the website and its authors; I do not edit or endorse them. Links open the original website.",
             "tr": "Uygulama, sitenin herkese açık haber akışı için bağımsız bir okuyucudur. Yazılar, görseller ve markalar siteye ve yazarlarına aittir; bunları düzenlemem veya onaylamam. Bağlantılar özgün siteyi açar.",
             "es": "La aplicación es un lector independiente del canal de noticias público del sitio web. Los artículos, imágenes y marcas pertenecen al sitio y a sus autores; no los edito ni los respaldo. Los enlaces abren el sitio original.",
             "pt": "O aplicativo é um leitor independente do feed público de notícias do site. Os artigos, imagens e marcas pertencem ao site e a seus autores; não os edito nem os endosso. Os links abrem o site original."}),
    "pet": ({"en": "Virtual pet", "tr": "Sanal evcil hayvan", "es": "Mascota virtual", "pt": "Pet virtual"},
            {"en": "The cat is a virtual character. Nothing is lost permanently if you stop playing, and nothing in the game replaces caring for a real animal.",
             "tr": "Kedi sanal bir karakterdir. Oynamayı bırakırsanız kalıcı bir şey kaybolmaz; oyundaki hiçbir şey gerçek bir hayvana bakmanın yerini tutmaz.",
             "es": "El gato es un personaje virtual. No se pierde nada de forma permanente si dejas de jugar, y nada del juego sustituye el cuidado de un animal real.",
             "pt": "O gato é um personagem virtual. Nada é perdido permanentemente se você parar de jogar, e nada no jogo substitui o cuidado com um animal real."}),
}

SEC_TAIL = [
    ({"en": "Availability and changes", "tr": "Erişilebilirlik ve değişiklikler", "es": "Disponibilidad y cambios", "pt": "Disponibilidade e alterações"},
     {"en": "I may update, change or stop offering the {kind}, or any feature, at any time. I try to keep it working but cannot promise it will always be available or free of errors.",
      "tr": "Bu {kind_gen} veya herhangi bir özelliğini istediğim zaman güncelleyebilir, değiştirebilir ya da sunmayı bırakabilirim. Çalışır durumda tutmaya çalışırım, ancak her zaman erişilebilir ya da hatasız olacağına söz veremem.",
      "es": "Puedo actualizar, cambiar o dejar de ofrecer {kind_def} o cualquier función en cualquier momento. Intento que funcione bien, pero no puedo prometer que esté siempre disponible ni libre de errores.",
      "pt": "Posso atualizar, alterar ou deixar de oferecer {kind_def} ou qualquer recurso a qualquer momento. Tento mantê-lo funcionando, mas não posso prometer que estará sempre disponível ou livre de erros."}),
    ({"en": "No warranty and liability", "tr": "Garanti ve sorumluluk", "es": "Sin garantía y responsabilidad", "pt": "Sem garantia e responsabilidade"},
     {"en": "The {kind} is provided \"as is\", without warranties of any kind. To the extent the law allows, I am not liable for indirect or consequential losses arising from its use. This does not limit any rights you have as a consumer under mandatory law in your country.",
      "tr": "{kind_nom} \"olduğu gibi\" sunulur, hiçbir garanti verilmez. Yasaların izin verdiği ölçüde, kullanımından doğan dolaylı veya sonuçsal zararlardan sorumlu değilim. Bu, ülkenizdeki emredici hukuk uyarınca tüketici olarak sahip olduğunuz haklarınızı sınırlamaz.",
      "es": "{kind_def_cap} se ofrece «tal cual», sin garantías de ningún tipo. En la medida que permita la ley, no soy responsable de pérdidas indirectas o consecuentes derivadas de su uso. Esto no limita los derechos que tengas como consumidor según la ley imperativa de tu país.",
      "pt": "{kind_def_cap} é fornecido \"como está\", sem garantias de qualquer tipo. Na medida em que a lei permitir, não sou responsável por perdas indiretas ou consequentes decorrentes do uso. Isso não limita os direitos que você tem como consumidor segundo a lei imperativa do seu país."}),
    ({"en": "Ownership", "tr": "Fikri haklar", "es": "Propiedad", "pt": "Propriedade"},
     {"en": "The {kind}, its name, artwork, sounds and code belong to me, except for third-party material that belongs to its owners. Google Play and Android are trademarks of Google LLC. Use of the {kind} is also subject to the Google Play Terms of Service.",
      "tr": "{kind_nom}, adı, görselleri, sesleri ve kodu; sahiplerine ait üçüncü taraf içerikler hariç, bana aittir. Google Play ve Android, Google LLC'nin ticari markalarıdır. {kind_nom} kullanımı ayrıca Google Play Hizmet Şartları'na tabidir.",
      "es": "{kind_def_cap}, su nombre, sus gráficos, sonidos y código me pertenecen, salvo el material de terceros, que pertenece a sus titulares. Google Play y Android son marcas de Google LLC. El uso también está sujeto a las Condiciones del Servicio de Google Play.",
      "pt": "{kind_def_cap}, seu nome, arte, sons e código pertencem a mim, exceto o material de terceiros, que pertence a seus titulares. Google Play e Android são marcas da Google LLC. O uso também está sujeito aos Termos de Serviço do Google Play."}),
    ({"en": "Changes to these terms and governing law", "tr": "Şartlarda değişiklik ve uygulanacak hukuk", "es": "Cambios en estos términos y ley aplicable", "pt": "Alterações destes termos e lei aplicável"},
     {"en": "If these terms change, the new version is published on this page with a new effective date. Continuing to use the {kind} after that means you accept the changes. To the extent the law allows, these terms are governed by the laws of Türkiye, without affecting mandatory consumer protection rights of your country of residence.",
      "tr": "Bu şartlar değişirse yeni sürüm, yeni yürürlük tarihiyle bu sayfada yayınlanır; sonrasında {kind_gen} kullanmaya devam etmeniz değişiklikleri kabul ettiğiniz anlamına gelir. Yasaların izin verdiği ölçüde bu şartlara Türkiye hukuku uygulanır; yaşadığınız ülkenin emredici tüketici koruma hakları saklıdır.",
      "es": "Si estos términos cambian, la nueva versión se publicará en esta página con una nueva fecha de entrada en vigor; seguir usando {kind_def} después supone aceptar los cambios. En la medida que permita la ley, estos términos se rigen por las leyes de Türkiye, sin perjuicio de los derechos imperativos de protección del consumidor de tu país de residencia.",
      "pt": "Se estes termos mudarem, a nova versão será publicada nesta página com nova data de vigência; continuar usando {kind_def} depois disso significa que você aceita as mudanças. Na medida em que a lei permitir, estes termos são regidos pelas leis da Turquia, sem prejuízo dos direitos imperativos de proteção ao consumidor do seu país de residência."}),
    ({"en": "Contact", "tr": "İletişim", "es": "Contacto", "pt": "Contato"},
     {"en": "Nesim Razon · <a href=\"mailto:" + MAIL + "\">" + MAIL + "</a>",
      "tr": "Nesim Razon · <a href=\"mailto:" + MAIL + "\">" + MAIL + "</a>",
      "es": "Nesim Razon · <a href=\"mailto:" + MAIL + "\">" + MAIL + "</a>",
      "pt": "Nesim Razon · <a href=\"mailto:" + MAIL + "\">" + MAIL + "</a>"}),
]

LANG_NAMES = {"en": "English", "tr": "Türkçe", "es": "Español", "pt": "Português"}
PRIV_WORD = {"en": "Privacy Policy", "tr": "Gizlilik Politikası", "es": "Política de privacidad", "pt": "Política de Privacidade"}


def fill(s, name, kind, lang):
    k = KIND[lang][kind]
    d = {
        "name": name, "kind": k,
        "kind_acc": KIND_ACC.get("tr", {}).get(kind, k),
        "kind_gen": {"game": "oyunu", "app": "uygulamayı"}[kind],
        "kind_nom": {"game": "Oyun", "app": "Uygulama"}[kind],
        "kind_def": KIND_DEF.get(lang, {}).get(kind, k),
        "kind_def_cap": KIND_DEF.get(lang, {}).get(kind, k).capitalize(),
    }
    out = s
    for a, b in d.items():
        out = out.replace("{" + a + "}", b)
    if kind == "app":  # skor tablosu ifadesi yalnizca oyunlarda anlamli
        for a, b in (("to cheat leaderboards, harm other people or", "to harm other people or"),
                     ("skor tablolarında hile, başkalarına zarar verme ya da", "başkalarına zarar vermek ya da"),
                     ("para hacer trampas en clasificaciones, dañar a otras personas o", "para dañar a otras personas o"),
                     ("para trapacear em placares, prejudicar outras pessoas ou", "para prejudicar outras pessoas ou")):
            out = out.replace(a, b)
    return out


def build(slug, spec):
    name, kind, ads, iap, pgs, note = spec
    src = io.open(os.path.join(G, slug, "privacy.html"), encoding="utf-8").read()
    langs = [l for l in re.findall(r'<section id="([a-z]{2})"', src) if l in LANG_NAMES]
    langs = [l for l in ("en", "tr", "es", "pt") if l in langs] or ["en"]
    style = re.search(r"<style>.*?</style>", src, re.S).group(0)
    heading = re.search(r"<h1>(.*?)</h1>", src).group(1)
    secs = [SEC[0]]
    if ads: secs.append(ADS)
    if iap:
        secs.append(IAP if ads else tuple({k: re.sub(r"\s*\((?:for example|örneğin|por ejemplo|por exemplo)[^)]*\)", "", v) for k, v in d.items()} for d in IAP))
    if pgs: secs.append(PGS)
    if note: secs.append(NOTES[note])
    secs += SEC_TAIL
    parts = []
    for l in langs:
        body = []
        for i, (h, p) in enumerate(secs, 1):
            body.append(f"    <h3>{i}. {fill(h[l], name, kind, l)}</h3>\n    <p>{fill(p[l], name, kind, l)}</p>")
        body.append(f'    <p><a href="privacy.html#{l}">{PRIV_WORD[l]}</a></p>')
        parts.append(f'  <section id="{l}" lang="{l}">\n    <h2>{T["h"][l]}</h2>\n    <p class="meta">{T["eff"][l]}: {DATE[l]}</p>\n    <p>{fill(T["intro"][l], name, kind, l)}</p>\n' + "\n".join(body) + "\n  </section>")
    nav = "\n".join(f'    <a href="#{l}">{LANG_NAMES[l]}</a>' for l in langs)
    meta = " · ".join(T["h"][l] for l in langs)
    html = f'''<!doctype html>
<html lang="{langs[0]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} – {T["h"][langs[0]]}</title>
{style}
</head>
<body>
<main>
  <h1>{heading}</h1>
  <p class="meta">{meta}</p>
  <nav>
{nav}
  </nav>

''' + "\n".join(parts) + '''
</main>
</body>
</html>
'''
    io.open(os.path.join(G, slug, "terms.html"), "w", encoding="utf-8", newline="\n").write(html)
    return langs


if __name__ == "__main__":
    for slug, spec in APPS.items():
        print(slug, build(slug, spec))
        import subprocess as _sp
        _sp.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "seo_fix.py")])
