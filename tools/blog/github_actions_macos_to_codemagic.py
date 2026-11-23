# Yazi: GitHub Actions macOS kotasi bitince Codemagic'e gecis. Kaynak: Game2048/SansOyunlari/WhereAmI .github/workflows/ios.yml, Slinglings/Astrolings codemagic.yaml, Referans/IOS_PORT_TUZAKLARI.md, Fikirler/Arsiv/ios_port_gunlukleri (IOS_PORT_PLANI, IOS_YENI_UYGULAMALAR_PLANI). Rakamlar: docs.github.com (actions-minute-multipliers, product-billing/github-actions), docs.codemagic.io/billing/pricing.
POST = {'tags': ['ios', 'devlog'],
 'id': 'github-actions-macos-minutes-to-codemagic',
 'app': None,
 'date': '2026-11-23',
 'en': {'slug': 'when-github-actions-macos-minutes-run-out-moving-ios-builds-to-codemagic',
        'title': 'No macOS Minutes Left on GitHub Actions: Moving to Codemagic',
        'desc': 'Building iOS from Windows: what a macOS minute costs on GitHub Actions and Codemagic, how the two pipelines differ, and how to plan the quota.',
        'intro': 'I build my iOS apps from a Windows laptop, so every build runs on a rented Mac. For a while that Mac came from GitHub Actions. Then the free credit got close to empty and I moved '
                 'new work to Codemagic. Here are the real numbers, the differences between the two pipelines, and the habits that keep the minutes from running out.',
        'sections': [{'h': 'Why the quota matters: a minute is not a minute',
                      'p': ["On GitHub Actions the free allowance is money, not minutes. According to GitHub's billing docs, the Free plan includes 12 USD of compute per month for private "
                            'repositories, and a macOS runner costs 0.062 USD per minute. A Linux 2-core runner costs 0.006 USD, so a macOS minute is about ten times more expensive. GitHub also '
                            'rounds each job up to a whole minute.',
                            'Simple arithmetic: 12 divided by 0.062 is about 193 macOS minutes in a month. My first full day of experiments used 54 of them, which is 3.35 USD. By 14 November the '
                            'credit was near 90 percent used, and I decided that new apps would build elsewhere.']},
                     {'h': 'The two pipelines side by side',
                      'ul': ['GitHub Actions: file .github/workflows/ios.yml, runner macos-26, triggered by a push to the ios-kmp branch when iosApp, shared or the Gradle files change. Build number '
                             'comes from github.run_number.',
                             'Codemagic: file codemagic.yaml at the repo root, instance type mac_mini_m2, started by hand from the web page (Start new build, branch main, pick the workflow). Build '
                             'number is 1000 plus the Codemagic build number.',
                             'Both have two jobs: an unsigned simulator build for a quick check, and a TestFlight job that archives, signs and uploads.',
                             'Both have a time limit: 40 minutes for the simulator job and 60 for TestFlight (timeout-minutes in one, max_build_duration in the other).',
                             'Secrets: GitHub repository secrets in one, a Codemagic variable group named apple in the other. Both hold the same App Store Connect key id, issuer id and key text.']},
                     {'h': 'What a build costs on each side',
                      'p': ['A TestFlight run on GitHub took about six minutes in my setup, so roughly 0.37 USD. From 12 USD that is about 32 runs a month, if I did nothing else. On Codemagic my '
                            'notes record builds of about 8 to 10 minutes.',
                            "Codemagic's pricing page says individuals get 500 free minutes per month on macOS M2 machines on a personal account, reset on the first of each month. Beyond that the "
                            'page lists 0.095 USD per minute for the macOS M2 VM. At 8 to 10 minutes a build, 500 minutes is 50 to 60 builds. Slower per build, but a much bigger bucket for this '
                            'workload.',
                            'Prices change. Check the current GitHub and Codemagic pricing pages before you plan around these numbers.',
                            'A worked example helps. Say a new app needs five failed runs before its first good TestFlight build, at about ten minutes each. This is an example, not a record of '
                            'mine.'],
                      'ul': ['Credit on GitHub: 12 USD, about 193 macOS minutes.',
                             'One TestFlight run on GitHub: about 6 minutes, 0.37 USD.',
                             'Five failed runs plus one good run at 10 minutes: 60 minutes. On Codemagic that is 12 percent of the free 500.',
                             'On GitHub the same 60 minutes at 0.062 USD would be 3.72 USD, almost a third of the monthly credit.',
                             'The same 500 free Codemagic minutes at the pay-as-you-go rate of 0.095 USD would be 47.50 USD, so the free bucket is worth real money.'],
                      'p2': ['The point is that failures, not successes, decide how fast the bucket empties.']},
                     {'h': 'Moving a repo over: what changes',
                      'p': ['The simulator job moved almost unchanged: XcodeGen, then xcodebuild with CODE_SIGNING_ALLOWED=NO. The TestFlight job needed real changes, because Codemagic has its own '
                            'signing tools.',
                            'The Codemagic job rebuilds the API key file, creates a keychain and fetches the signing files, then builds the ipa and publishes it:'],
                      'ul': ['keychain initialize',
                             'app-store-connect fetch-signing-files "com.example.app" --type IOS_APP_STORE --create',
                             'keychain add-certificates',
                             'xcode-project use-profiles',
                             'xcode-project build-ipa --project iosApp/iosApp.xcodeproj --scheme iosApp',
                             'app-store-connect publish --path build/ios/ipa/iosApp.ipa'],
                      'p2': ['The build number also needed care. In my setup the number in the package stayed at 1 until I wrote it straight into Info.plist with PlistBuddy after generating the '
                             'project. The signing details have their own post on cloud signing certificates, and the build number has one too.']},
                     {'h': 'Mistakes that burned minutes',
                      'p': ['Most of my wasted minutes came from three mistakes, not from the price. Each one is cheap to avoid once you know it.'],
                      'ul': ['Cloud signing during the archive step created a new Apple Development certificate on every build. After about eleven the account hit its certificate limit and builds '
                             'failed. The fix was one distribution key that I keep, fetched with the signing tools shown above.',
                             'The build number stayed at 1 for three attempts. Three runs, roughly thirty minutes, for one line in Info.plist.',
                             'A wrong Bundle ID chosen in the App Store Connect form made the upload fail with an altool error. You can check the Bundle ID through the App Store Connect API before '
                             'any build, which costs zero macOS minutes.'],
                      'p2': ['The rule I took from this: anything that Windows or a web page can check goes before the Mac. A failed run costs the same as a good one.']},
                     {'h': 'Habits that save minutes',
                      'ul': ['Run the Kotlin iOS compile on Windows first: the simulator target compiles locally and costs no macOS time.',
                             'Run a small pre-check script over the project before sending it, to catch the traps that already cost me runs.',
                             'On GitHub, limit the trigger with paths so a change to a README does not start a Mac.',
                             'Use a commit message marker. A commit containing [testflight] runs only the TestFlight job and skips the simulator job.',
                             'Use concurrency with cancel-in-progress, so a newer push cancels an older run.',
                             'On Codemagic, start builds by hand only. A push never spends minutes by accident.',
                             'Always run the simulator workflow first and the TestFlight one only when it passes.']},
                     {'h': 'Planning the month',
                      'p': ["My plan is simple. GitHub's credit renews at the start of the month, and so do Codemagic's 500 minutes. New apps and long port sessions go to Codemagic. GitHub keeps the "
                            'older repos that already have a working workflow.',
                            'I count in builds, not minutes: about 8 to 10 minutes each, plus a spare allowance for the first run of a new app, when failures are most likely. If a month looks tight, '
                            'I do more work on Windows and send fewer, better prepared builds.',
                            'There is no single winner. GitHub Actions is convenient when the code is already there: the workflow sits in the repo, secrets are in the repo settings and the build can '
                            'start on every push. Its weak point for me is the dollar-based credit, because a macOS minute eats it ten times faster than a Linux one.',
                            'Codemagic suits a repo that builds iOS rarely and by hand. The minutes are a separate bucket of 500, and the signing tools are built for the TestFlight path. Its weak '
                            'point is that you set up one more account, one more variable group and one more place for secrets.',
                            'If you build iOS a few times a week, either works. If you are porting several apps in the same month, count the builds first and choose the cheaper bucket.']}],
        'faq': [['How much does a macOS minute cost on GitHub Actions?',
                 "GitHub's billing page lists 0.062 USD per minute for the macOS runner, against 0.006 USD for a Linux 2-core runner. Check the page for current prices."],
                ['How many free minutes does Codemagic give?',
                 'Its pricing page says individuals receive 500 free minutes per month on macOS M2 machines on a personal account, reset on the first of the month.'],
                ['Are GitHub Actions minutes free for public repositories?',
                 "GitHub's docs say standard GitHub-hosted runners are free in public repositories. The credit I describe applies to private ones."],
                ['Can I keep both services?', 'Yes. I kept GitHub workflows in older repos and used Codemagic for new apps. Each repo uses one of them.']]},
 'tr': {'slug': 'github-actions-macos-dakikalari-bitince-ios-derlemelerini-codemagic-e-tasimak',
        'title': "GitHub Actions macOS Dakikaları Bitince Codemagic'e Geçiş",
        'desc': "Windows'tan iOS derlemesi yapan tek geliştirici: macOS dakikası iki serviste ne kadar tutuyor, iki hat nasıl ayrışıyor ve kota nasıl planlanır.",
        'intro': "iOS uygulamalarımı Windows dizüstünden derliyorum, yani her derleme kiralık bir Mac'te çalışıyor. Bir süre bu Mac GitHub Actions'tan geldi. Sonra ücretsiz kredi bitmeye yaklaştı ve "
                 "yeni işleri Codemagic'e aldım. İşte gerçek rakamlar, iki hattın farkları ve dakikaların tükenmesini önleyen alışkanlıklar.",
        'sections': [{'h': 'Kota neden önemli: her dakika aynı değil',
                      'p': ["GitHub Actions'ta ücretsiz hak dakika değil, para olarak verilir. GitHub'ın faturalandırma belgelerine göre Free planda özel depolar için ayda 12 dolarlık işlem kredisi "
                            'var ve bir macOS makinesi dakikada 0,062 dolar tutuyor. Linux 2 çekirdekli makine 0,006 dolar; yani bir macOS dakikası yaklaşık on kat pahalı. GitHub ayrıca her işi tam '
                            'dakikaya yuvarlıyor.',
                            "Basit hesap: 12'yi 0,062'ye bölünce ayda yaklaşık 193 macOS dakikası çıkıyor. Deneylerin ilk tam günü bunun 54 dakikasını, yani 3,35 doları yedi. 14 Kasım'da kredi "
                            'yaklaşık yüzde 90 dolmuştu ve yeni uygulamaların başka yerde derlenmesine karar verdim.']},
                     {'h': 'İki hat yan yana',
                      'ul': ['GitHub Actions: .github/workflows/ios.yml dosyası, macos-26 makinesi, iosApp, shared veya Gradle dosyaları değişince ios-kmp dalına yapılan gönderimle tetiklenir. '
                             "Derleme numarası github.run_number'dan gelir.",
                             'Codemagic: depo kökünde codemagic.yaml, mac_mini_m2 makine tipi, web sayfasından elle başlatılır (Start new build, dal main, iş akışını seç). Derleme numarası 1000 artı '
                             'Codemagic derleme numarasıdır.',
                             'İkisinde de iki iş var: hızlı kontrol için imzasız simülatör derlemesi ve arşivleyip imzalayan, yükleyen TestFlight işi.',
                             'İkisinde de süre sınırı var: simülatör işi için 40, TestFlight için 60 dakika (birinde timeout-minutes, ötekinde max_build_duration).',
                             'Sırlar: birinde GitHub depo sırları, ötekinde apple adlı bir Codemagic değişken grubu. İkisi de aynı App Store Connect anahtar kimliğini, yayıncı kimliğini ve anahtar '
                             'metnini tutuyor.'],
                      'p2': ['İki dosyanın başındaki yorumlar aynı şeyi söylüyor: macOS dakikaları pahalı, o yüzden iş yalnızca gerektiğinde çalışmalı. GitHub dosyasında bu, iosApp, shared ve Gradle '
                             'yollarına bağlı tetikleyici ve eski çalıştırmayı iptal eden concurrency ayarı. Codemagic dosyasında ise hiç otomatik tetikleyici yok; derleme yalnızca ben düğmeye '
                             'basınca başlıyor.',
                             "Pratikte bu, Codemagic'te dakikanın tamamen benim elimde olduğu anlamına geliyor. Bedeli, her derlemeyi bilerek başlatmam ve sonucu ben izlemem."]},
                     {'h': 'Bir derleme iki tarafta ne tutuyor',
                      'p': ["Benim düzenimde GitHub'da bir TestFlight turu yaklaşık altı dakika sürdü, yani kabaca 0,37 dolar. 12 dolardan başka hiçbir şey yapmasam ayda yaklaşık 32 tur eder. "
                            "Codemagic'te notlarım yaklaşık 8-10 dakikalık derlemeler kaydediyor.",
                            "Codemagic'in fiyat sayfası, bireylerin kişisel hesapta macOS M2 makinelerinde ayda 500 ücretsiz dakika aldığını ve bunun her ayın birinde sıfırlandığını söylüyor. Ötesi "
                            'için sayfa macOS M2 sanal makinesine dakikada 0,095 dolar yazıyor. Derleme başına 8-10 dakikayla 500 dakika, 50-60 derleme demek. Derleme başına daha yavaş ama bu iş '
                            'yükü için çok daha büyük bir kova.',
                            "Fiyatlar değişir. Bu rakamlara göre plan yapmadan önce GitHub ve Codemagic'in güncel fiyat sayfalarına bak.",
                            'Çalışılmış bir örnek yardımcı olur. Diyelim ki yeni bir uygulamanın ilk iyi TestFlight derlemesinden önce her biri yaklaşık on dakikalık beş başarısız çalıştırması var. '
                            'Bu bir örnek, benim kaydım değil.'],
                      'ul': ["GitHub'daki kredi: 12 dolar, yaklaşık 193 macOS dakikası.",
                             "GitHub'da bir TestFlight turu: yaklaşık 6 dakika, 0,37 dolar.",
                             "Beş başarısız artı 10 dakikalık bir iyi çalıştırma: 60 dakika. Codemagic'te bu, ücretsiz 500'ün yüzde 12'si.",
                             "GitHub'da aynı 60 dakika 0,062 dolardan 3,72 dolar eder; aylık kredinin neredeyse üçte biri.",
                             'Aynı 500 ücretsiz Codemagic dakikası, kullandıkça öde fiyatı olan 0,095 dolardan 47,50 dolar eder; yani ücretsiz kova gerçek para değerinde.'],
                      'p2': ['Önemli olan, kovanın ne kadar hızlı boşaldığını başarıların değil başarısızlıkların belirlemesi.']},
                     {'h': 'Bir depoyu taşımak: ne değişiyor',
                      'p': ["Simülatör işi neredeyse aynen taşındı: XcodeGen, ardından CODE_SIGNING_ALLOWED=NO ile xcodebuild. TestFlight işinde gerçek değişiklik gerekti, çünkü Codemagic'in kendi "
                            'imzalama araçları var.',
                            'Codemagic işi API anahtar dosyasını yeniden kurar, bir anahtarlık oluşturur, imzalama dosyalarını çeker, sonra ipa üretir ve yayınlar:'],
                      'ul': ['keychain initialize',
                             'app-store-connect fetch-signing-files "com.example.app" --type IOS_APP_STORE --create',
                             'keychain add-certificates',
                             'xcode-project use-profiles',
                             'xcode-project build-ipa --project iosApp/iosApp.xcodeproj --scheme iosApp',
                             'app-store-connect publish --path build/ios/ipa/iosApp.ipa'],
                      'p2': ["Derleme numarası da dikkat istedi. Benim düzenimde, proje üretildikten sonra numarayı PlistBuddy ile doğrudan Info.plist'e yazana kadar paketteki numara 1'de kaldı. "
                             'İmzalama ayrıntılarının bulut imzalama sertifikaları üzerine, derleme numarasının da kendi yazısı var.']},
                     {'h': 'Dakika yakan hatalar',
                      'p': ['Boşa giden dakikalarımın çoğu fiyattan değil üç hatadan geldi. Bilince her birinden kaçınmak ucuz.',
                            'Bu üç hatayı tek tek anlatmak kolay, ama ders hepsinde aynı: derleme başlamadan önce, ucuz yerde kontrol edilebilecek bir şey vardı. Şimdi her yeni uygulamada '
                            "Codemagic'e gitmeden önce bu kontrolleri yapıyorum ve ilk çalıştırmaya beklentiyle değil, listeyle gidiyorum."],
                      'ul': ['Arşiv adımında bulut imzalama her derlemede yeni bir Apple Development sertifikası üretti. Yaklaşık on birden sonra hesap sertifika sınırına çarptı ve derlemeler '
                             'başarısız oldu. Çözüm, saklayıp yukarıda gösterilen imzalama araçlarıyla çektiğim tek bir dağıtım anahtarıydı.',
                             "Derleme numarası üç denemede 1'de kaldı. Info.plist'teki bir satır için üç çalıştırma, yaklaşık otuz dakika.",
                             "App Store Connect formunda yanlış seçilen Bundle ID, yüklemenin altool hatasıyla başarısız olmasına yol açtı. Bundle ID'yi hiçbir derleme yapmadan App Store Connect "
                             "API'si üzerinden kontrol edebilirsin; bu sıfır macOS dakikası tutar."],
                      'p2': ["Bundan çıkardığım kural: Windows'un ya da bir web sayfasının kontrol edebildiği her şey Mac'ten önce gelir. Başarısız bir çalıştırma, başarılı olanla aynı paraya mal "
                             'olur.']},
                     {'h': 'Dakika kazandıran alışkanlıklar',
                      'ul': ["Önce Kotlin iOS derlemesini Windows'ta çalıştır: simülatör hedefi yerelde derlenir ve macOS zamanı harcamaz.",
                             'Göndermeden önce projeye küçük bir ön kontrol betiği çalıştır; bana şimdiden çalıştırma yediren tuzakları yakalar.',
                             "GitHub'da tetikleyiciyi paths ile sınırla; bir README değişikliği bir Mac başlatmasın.",
                             'Commit iletisinde işaret kullan. İçinde [testflight] geçen commit yalnız TestFlight işini çalıştırır, simülatör işini atlar.',
                             "cancel-in-progress'li concurrency kullan; yeni bir gönderim eski çalıştırmayı iptal eder.",
                             "Codemagic'te derlemeleri yalnız elle başlat. Bir gönderim yanlışlıkla dakika harcamaz.",
                             'Önce simülatör iş akışını, geçince TestFlight olanı çalıştır.']},
                     {'h': 'Ayı planlamak',
                      'p': ["Planım basit. GitHub'ın kredisi ay başında yenileniyor, Codemagic'in 500 dakikası da. Yeni uygulamalar ve uzun taşıma oturumları Codemagic'e gidiyor. GitHub, zaten "
                            'çalışan iş akışı olan eski depolarda kalıyor.',
                            'Dakikayı değil derlemeyi sayıyorum: her biri yaklaşık 8-10 dakika, artı yeni bir uygulamanın başarısızlığın en olası olduğu ilk çalıştırması için yedek pay. Ay sıkışık '
                            "görünürse Windows'ta daha çok iş yapıp daha az ama daha iyi hazırlanmış derleme gönderiyorum.",
                            'Tek bir kazanan yok. Kod zaten oradaysa GitHub Actions rahat: iş akışı depoda durur, sırlar depo ayarlarındadır ve derleme her gönderimde başlayabilir. Benim için zayıf '
                            'yanı dolar bazlı kredi; çünkü bir macOS dakikası onu Linux dakikasından on kat hızlı yiyor.',
                            "Codemagic, iOS'u seyrek ve elle derleyen bir depoya uyuyor. Dakikalar 500'lük ayrı bir kova ve imzalama araçları TestFlight yoluna göre yapılmış. Zayıf yanı bir hesap, "
                            'bir değişken grubu ve sırlar için bir yer daha kurman.',
                            "iOS'u haftada birkaç kez derliyorsan ikisi de olur. Aynı ay birkaç uygulama taşıyorsan önce derlemeleri say ve daha ucuz kovayı seç.",
                            'Son bir not: kotayı bir ay içinde bitirmek felaket değil. Kredi ay başında yenileniyor, yeni derlemeyi bekleyebilirim. Asıl risk, bir App Store gönderimi sıkışmışken '
                            'dakikasız kalmak; bu yüzden ayın son haftasına bir iki derlemelik pay bırakıyorum.']}],
        'faq': [["GitHub Actions'ta bir macOS dakikası ne kadar?",
                 "GitHub'ın faturalandırma sayfası macOS makinesi için dakikada 0,062 dolar, Linux 2 çekirdekli makine için 0,006 dolar yazıyor. Güncel fiyat için sayfaya bak."],
                ['Codemagic kaç ücretsiz dakika veriyor?',
                 'Fiyat sayfası, bireylerin kişisel hesapta macOS M2 makinelerinde ayda 500 ücretsiz dakika aldığını ve ayın birinde sıfırlandığını söylüyor.'],
                ['Herkese açık depolarda GitHub Actions dakikaları ücretsiz mi?',
                 'GitHub belgeleri, standart GitHub barındırmalı makinelerin herkese açık depolarda ücretsiz olduğunu söylüyor. Anlattığım kredi özel depolar için.'],
                ['İki servisi birlikte kullanabilir miyim?', 'Evet. Eski depolarda GitHub iş akışlarını tuttum, yeni uygulamalarda Codemagic kullandım. Her depo ikisinden birini kullanıyor.']]},
 'es': {'slug': 'cuando-se-acaban-los-minutos-de-macos-en-github-actions-pasar-las-compilaciones-ios-a-codemagic',
        'title': 'Sin minutos de macOS en GitHub Actions: paso a Codemagic',
        'desc': 'Compilar iOS desde Windows: cuánto cuesta un minuto de macOS en GitHub Actions y Codemagic, cómo difieren los flujos y cómo planificar la cuota.',
        'intro': 'Compilo mis apps de iOS desde un portátil con Windows, así que cada compilación corre en un Mac alquilado. Durante un tiempo ese Mac vino de GitHub Actions. Luego el crédito '
                 'gratuito se acercó al final y pasé el trabajo nuevo a Codemagic. Aquí van las cifras reales, las diferencias entre los dos flujos y los hábitos que evitan quedarse sin minutos.',
        'sections': [{'h': 'Por qué importa la cuota: un minuto no es un minuto',
                      'p': ['En GitHub Actions lo gratuito es dinero, no minutos. Según la documentación de facturación de GitHub, el plan Free incluye 12 USD de cómputo al mes para repositorios '
                            'privados, y un runner de macOS cuesta 0,062 USD por minuto. Un runner de Linux de 2 núcleos cuesta 0,006 USD, así que un minuto de macOS es unas diez veces más caro. '
                            'Además GitHub redondea cada trabajo al minuto completo.',
                            'Cuenta sencilla: 12 entre 0,062 son unos 193 minutos de macOS al mes. Mi primer día completo de pruebas gastó 54 de ellos, es decir 3,35 USD. El 14 de noviembre el '
                            'crédito estaba casi al 90 por ciento y decidí que las apps nuevas se compilarían en otro sitio.']},
                     {'h': 'Los dos flujos, lado a lado',
                      'ul': ['GitHub Actions: archivo .github/workflows/ios.yml, runner macos-26, se activa con un push a la rama ios-kmp cuando cambian iosApp, shared o los archivos de Gradle. El '
                             'número de compilación sale de github.run_number.',
                             'Codemagic: archivo codemagic.yaml en la raíz del repositorio, tipo de instancia mac_mini_m2, se inicia a mano desde la web (Start new build, rama main, elegir el '
                             'flujo). El número de compilación es 1000 más el número de compilación de Codemagic.',
                             'Ambos tienen dos trabajos: una compilación sin firmar para el simulador como control rápido, y un trabajo de TestFlight que archiva, firma y sube.',
                             'Ambos tienen límite de tiempo: 40 minutos para el simulador y 60 para TestFlight (timeout-minutes en uno, max_build_duration en el otro).',
                             'Secretos: secretos del repositorio en GitHub, y en Codemagic un grupo de variables llamado apple. Los dos guardan el mismo id de clave, el id de emisor y el texto de la '
                             'clave de App Store Connect.']},
                     {'h': 'Lo que cuesta una compilación en cada lado',
                      'p': ['En mi configuración una ejecución de TestFlight en GitHub duró unos seis minutos, o sea unos 0,37 USD. Con 12 USD son unas 32 ejecuciones al mes, si no hiciera nada más. '
                            'En Codemagic mis notas registran compilaciones de unos 8 a 10 minutos.',
                            'La página de precios de Codemagic dice que las personas reciben 500 minutos gratis al mes en máquinas macOS M2 con una cuenta personal, y que se reinician el día uno de '
                            'cada mes. Más allá de eso, la página indica 0,095 USD por minuto para la VM macOS M2. Con 8 a 10 minutos por compilación, 500 minutos son de 50 a 60 compilaciones. Cada '
                            'una es más lenta, pero la bolsa es mucho mayor para esta carga de trabajo.',
                            'Los precios cambian. Revisa las páginas de precios actuales de GitHub y de Codemagic antes de planificar con estas cifras.',
                            'Un ejemplo trabajado ayuda. Supongamos que una app nueva necesita cinco ejecuciones fallidas antes de su primera buena compilación de TestFlight, de unos diez minutos '
                            'cada una. Es un ejemplo, no un registro mío.'],
                      'ul': ['Crédito en GitHub: 12 USD, unos 193 minutos de macOS.',
                             'Una ejecución de TestFlight en GitHub: unos 6 minutos, 0,37 USD.',
                             'Cinco ejecuciones fallidas más una buena de 10 minutos: 60 minutos. En Codemagic es el 12 por ciento de los 500 gratis.',
                             'En GitHub esos mismos 60 minutos a 0,062 USD serían 3,72 USD, casi un tercio del crédito mensual.',
                             'Esos 500 minutos gratis de Codemagic a la tarifa de pago por uso de 0,095 USD serían 47,50 USD, así que la bolsa gratuita vale dinero de verdad.'],
                      'p2': ['Lo importante es que los fallos, no los aciertos, deciden con qué rapidez se vacía la bolsa.']},
                     {'h': 'Pasar un repositorio: qué cambia',
                      'p': ['El trabajo del simulador pasó casi sin cambios: XcodeGen y luego xcodebuild con CODE_SIGNING_ALLOWED=NO. El trabajo de TestFlight sí necesitó cambios reales, porque '
                            'Codemagic tiene sus propias herramientas de firma.',
                            'El trabajo de Codemagic reconstruye el archivo de la clave de API, crea un llavero, descarga los archivos de firma y luego genera el ipa y lo publica:'],
                      'ul': ['keychain initialize',
                             'app-store-connect fetch-signing-files "com.example.app" --type IOS_APP_STORE --create',
                             'keychain add-certificates',
                             'xcode-project use-profiles',
                             'xcode-project build-ipa --project iosApp/iosApp.xcodeproj --scheme iosApp',
                             'app-store-connect publish --path build/ios/ipa/iosApp.ipa'],
                      'p2': ['El número de compilación también pidió cuidado. En mi configuración el número del paquete se quedó en 1 hasta que lo escribí directamente en Info.plist con PlistBuddy '
                             'después de generar el proyecto. Los detalles de la firma tienen su propia entrada sobre certificados de firma en la nube, y el número de compilación también tiene la '
                             'suya.']},
                     {'h': 'Errores que quemaron minutos',
                      'p': ['Casi todos mis minutos perdidos vinieron de tres errores, no del precio. Cada uno es barato de evitar cuando lo conoces.'],
                      'ul': ['La firma en la nube durante el paso de archivado creó un certificado Apple Development nuevo en cada compilación. Tras unos once, la cuenta alcanzó su límite de '
                             'certificados y las compilaciones fallaron. La solución fue una única clave de distribución que conservo, descargada con las herramientas de firma mostradas arriba.',
                             'El número de compilación se quedó en 1 durante tres intentos. Tres ejecuciones, unos treinta minutos, por una línea en Info.plist.',
                             'Un Bundle ID equivocado elegido en el formulario de App Store Connect hizo fallar la subida con un error de altool. Puedes comprobar el Bundle ID con la API de App '
                             'Store Connect antes de cualquier compilación, y eso cuesta cero minutos de macOS.'],
                      'p2': ['La regla que saqué de esto: todo lo que Windows o una página web pueden comprobar va antes que el Mac. Una ejecución fallida cuesta lo mismo que una buena.']},
                     {'h': 'Hábitos que ahorran minutos',
                      'ul': ['Ejecuta primero en Windows la compilación de Kotlin para iOS: el destino del simulador compila en local y no gasta tiempo de macOS.',
                             'Pasa un pequeño script de comprobación al proyecto antes de enviarlo, para cazar las trampas que ya me costaron ejecuciones.',
                             'En GitHub, limita el disparador con paths para que un cambio en un README no arranque un Mac.',
                             'Usa una marca en el mensaje del commit. Un commit con [testflight] ejecuta solo el trabajo de TestFlight y omite el del simulador.',
                             'Usa concurrency con cancel-in-progress, para que un push nuevo cancele la ejecución anterior.',
                             'En Codemagic, inicia las compilaciones solo a mano. Un push nunca gasta minutos por accidente.',
                             'Ejecuta siempre primero el flujo del simulador y el de TestFlight solo cuando pasa.']},
                     {'h': 'Planificar el mes',
                      'p': ['Mi plan es sencillo. El crédito de GitHub se renueva al empezar el mes, y los 500 minutos de Codemagic también. Las apps nuevas y las sesiones largas de portado van a '
                            'Codemagic. GitHub conserva los repositorios antiguos que ya tienen un flujo que funciona.',
                            'Cuento en compilaciones, no en minutos: unos 8 a 10 minutos cada una, más un margen para la primera ejecución de una app nueva, cuando los fallos son más probables. Si '
                            'el mes se ve justo, trabajo más en Windows y envío menos compilaciones, pero mejor preparadas.',
                            'No hay un ganador único. GitHub Actions es cómodo cuando el código ya está ahí: el flujo vive en el repositorio, los secretos están en sus ajustes y la compilación puede '
                            'empezar con cada push. Su punto débil para mí es el crédito en dólares, porque un minuto de macOS lo gasta diez veces más rápido que uno de Linux.',
                            'Codemagic encaja con un repositorio que compila iOS pocas veces y a mano. Los minutos son una bolsa aparte de 500 y las herramientas de firma están pensadas para el '
                            'camino a TestFlight. Su punto débil es que hay que montar una cuenta más, un grupo de variables más y otro sitio para los secretos.',
                            'Si compilas iOS varias veces por semana, sirven los dos. Si portas varias apps en el mismo mes, cuenta primero las compilaciones y elige la bolsa más barata.']}],
        'faq': [['¿Cuánto cuesta un minuto de macOS en GitHub Actions?',
                 'La página de facturación de GitHub indica 0,062 USD por minuto para el runner de macOS, frente a 0,006 USD para un runner de Linux de 2 núcleos. Consulta la página para ver precios '
                 'actuales.'],
                ['¿Cuántos minutos gratis da Codemagic?',
                 'Su página de precios dice que las personas reciben 500 minutos gratis al mes en máquinas macOS M2 con una cuenta personal, y se reinician el día uno del mes.'],
                ['¿Los minutos de GitHub Actions son gratis en repositorios públicos?',
                 'La documentación de GitHub dice que los runners estándar alojados por GitHub son gratuitos en repositorios públicos. El crédito que describo se aplica a los privados.'],
                ['¿Puedo usar los dos servicios a la vez?', 'Sí. Dejé los flujos de GitHub en los repositorios antiguos y usé Codemagic para las apps nuevas. Cada repositorio usa uno de los dos.']]},
 'pt': {'slug': 'quando-os-minutos-de-macos-do-github-actions-acabam-levando-os-builds-ios-para-o-codemagic',
        'title': 'Sem minutos de macOS no GitHub Actions: migrando para o Codemagic',
        'desc': 'Compilar iOS a partir do Windows: quanto custa um minuto de macOS no GitHub Actions e no Codemagic, como os fluxos diferem e como planejar a cota.',
        'intro': 'Compilo meus apps de iOS a partir de um notebook com Windows, então cada build roda em um Mac alugado. Por um tempo esse Mac veio do GitHub Actions. Depois o crédito gratuito '
                 'chegou perto do fim e passei o trabalho novo para o Codemagic. Aqui estão os números reais, as diferenças entre os dois fluxos e os hábitos que evitam ficar sem minutos.',
        'sections': [{'h': 'Por que a cota importa: um minuto não é um minuto',
                      'p': ['No GitHub Actions o que é gratuito é dinheiro, não minutos. Segundo a documentação de cobrança do GitHub, o plano Free inclui 12 USD de computação por mês para '
                            'repositórios privados, e um runner de macOS custa 0,062 USD por minuto. Um runner Linux de 2 núcleos custa 0,006 USD, então um minuto de macOS é cerca de dez vezes mais '
                            'caro. O GitHub também arredonda cada job para o minuto inteiro.',
                            'Conta simples: 12 dividido por 0,062 dá cerca de 193 minutos de macOS por mês. Meu primeiro dia completo de testes gastou 54 deles, ou seja, 3,35 USD. Em 14 de novembro '
                            'o crédito estava perto de 90 por cento usado e decidi que os apps novos seriam compilados em outro lugar.']},
                     {'h': 'Os dois fluxos lado a lado',
                      'ul': ['GitHub Actions: arquivo .github/workflows/ios.yml, runner macos-26, disparado por um push na branch ios-kmp quando iosApp, shared ou os arquivos do Gradle mudam. O '
                             'número do build vem de github.run_number.',
                             'Codemagic: arquivo codemagic.yaml na raiz do repositório, tipo de instância mac_mini_m2, iniciado à mão pela página web (Start new build, branch main, escolher o '
                             'fluxo). O número do build é 1000 mais o número de build do Codemagic.',
                             'Os dois têm dois jobs: um build sem assinatura para o simulador como verificação rápida, e um job de TestFlight que arquiva, assina e envia.',
                             'Os dois têm limite de tempo: 40 minutos para o simulador e 60 para o TestFlight (timeout-minutes em um, max_build_duration no outro).',
                             'Segredos: segredos do repositório no GitHub, e no Codemagic um grupo de variáveis chamado apple. Ambos guardam o mesmo id da chave, o id do emissor e o texto da chave '
                             'do App Store Connect.']},
                     {'h': 'Quanto custa um build em cada lado',
                      'p': ['Na minha configuração, uma execução de TestFlight no GitHub levou cerca de seis minutos, ou seja, uns 0,37 USD. Com 12 USD são cerca de 32 execuções por mês, se eu não '
                            'fizesse mais nada. No Codemagic minhas notas registram builds de uns 8 a 10 minutos.',
                            'A página de preços do Codemagic diz que pessoas físicas recebem 500 minutos grátis por mês em máquinas macOS M2 com uma conta pessoal, zerados no dia um de cada mês. '
                            'Além disso, a página lista 0,095 USD por minuto para a VM macOS M2. Com 8 a 10 minutos por build, 500 minutos são de 50 a 60 builds. Cada um é mais lento, mas o balde é '
                            'bem maior para essa carga de trabalho.',
                            'Os preços mudam. Confira as páginas de preços atuais do GitHub e do Codemagic antes de planejar com esses números.',
                            'Um exemplo ajuda. Suponha que um app novo precise de cinco execuções com falha antes do primeiro bom build de TestFlight, de uns dez minutos cada. É um exemplo, não um '
                            'registro meu.'],
                      'ul': ['Crédito no GitHub: 12 USD, cerca de 193 minutos de macOS.',
                             'Uma execução de TestFlight no GitHub: uns 6 minutos, 0,37 USD.',
                             'Cinco execuções com falha mais uma boa de 10 minutos: 60 minutos. No Codemagic isso é 12 por cento dos 500 grátis.',
                             'No GitHub esses mesmos 60 minutos a 0,062 USD seriam 3,72 USD, quase um terço do crédito mensal.',
                             'Os 500 minutos grátis do Codemagic na tarifa de pagamento por uso de 0,095 USD seriam 47,50 USD, então o balde gratuito vale dinheiro de verdade.'],
                      'p2': ['O ponto é que as falhas, não os acertos, decidem a rapidez com que o balde esvazia.']},
                     {'h': 'Migrando um repositório: o que muda',
                      'p': ['O job do simulador migrou quase sem mudanças: XcodeGen e depois xcodebuild com CODE_SIGNING_ALLOWED=NO. O job de TestFlight precisou de mudanças reais, porque o '
                            'Codemagic tem suas próprias ferramentas de assinatura.',
                            'O job do Codemagic reconstrói o arquivo da chave de API, cria um chaveiro, baixa os arquivos de assinatura e depois gera o ipa e o publica:'],
                      'ul': ['keychain initialize',
                             'app-store-connect fetch-signing-files "com.example.app" --type IOS_APP_STORE --create',
                             'keychain add-certificates',
                             'xcode-project use-profiles',
                             'xcode-project build-ipa --project iosApp/iosApp.xcodeproj --scheme iosApp',
                             'app-store-connect publish --path build/ios/ipa/iosApp.ipa'],
                      'p2': ['O número do build também pediu cuidado. Na minha configuração o número no pacote ficou em 1 até eu escrevê-lo direto no Info.plist com PlistBuddy depois de gerar o '
                             'projeto. Os detalhes da assinatura têm um post próprio sobre certificados de assinatura na nuvem, e o número do build também tem o seu.']},
                     {'h': 'Erros que queimaram minutos',
                      'p': ['A maior parte dos meus minutos perdidos veio de três erros, não do preço. Cada um é barato de evitar quando você o conhece.'],
                      'ul': ['A assinatura na nuvem durante a etapa de arquivamento criou um certificado Apple Development novo a cada build. Depois de uns onze, a conta atingiu o limite de '
                             'certificados e os builds falharam. A solução foi uma única chave de distribuição que eu guardo, baixada com as ferramentas de assinatura mostradas acima.',
                             'O número do build ficou em 1 por três tentativas. Três execuções, uns trinta minutos, por uma linha no Info.plist.',
                             'Um Bundle ID errado escolhido no formulário do App Store Connect fez o envio falhar com um erro do altool. Dá para conferir o Bundle ID pela API do App Store Connect '
                             'antes de qualquer build, e isso custa zero minutos de macOS.'],
                      'p2': ['A regra que tirei disso: tudo que o Windows ou uma página web puder verificar vem antes do Mac. Uma execução que falha custa o mesmo que uma que dá certo.']},
                     {'h': 'Hábitos que economizam minutos',
                      'ul': ['Rode primeiro no Windows a compilação de Kotlin para iOS: o alvo do simulador compila localmente e não gasta tempo de macOS.',
                             'Passe um pequeno script de verificação no projeto antes de enviar, para pegar as armadilhas que já me custaram execuções.',
                             'No GitHub, limite o gatilho com paths para que uma mudança em um README não ligue um Mac.',
                             'Use uma marca na mensagem do commit. Um commit com [testflight] roda só o job de TestFlight e pula o do simulador.',
                             'Use concurrency com cancel-in-progress, para que um push novo cancele a execução anterior.',
                             'No Codemagic, inicie os builds só à mão. Um push nunca gasta minutos por acidente.',
                             'Rode sempre primeiro o fluxo do simulador e o de TestFlight só quando ele passar.']},
                     {'h': 'Planejando o mês',
                      'p': ['Meu plano é simples. O crédito do GitHub renova no começo do mês, e os 500 minutos do Codemagic também. Apps novos e sessões longas de portagem vão para o Codemagic. O '
                            'GitHub fica com os repositórios antigos que já têm um fluxo funcionando.',
                            'Conto em builds, não em minutos: uns 8 a 10 minutos cada, mais uma folga para a primeira execução de um app novo, quando as falhas são mais prováveis. Se o mês parece '
                            'apertado, trabalho mais no Windows e envio menos builds, mas mais bem preparados.',
                            'Não há um vencedor único. O GitHub Actions é cômodo quando o código já está lá: o fluxo fica no repositório, os segredos estão nas configurações dele e o build pode '
                            'começar a cada push. Seu ponto fraco para mim é o crédito em dólares, porque um minuto de macOS o consome dez vezes mais rápido que um de Linux.',
                            'O Codemagic combina com um repositório que compila iOS raramente e à mão. Os minutos são um balde à parte de 500 e as ferramentas de assinatura foram feitas para o '
                            'caminho até o TestFlight. Seu ponto fraco é montar mais uma conta, mais um grupo de variáveis e mais um lugar para os segredos.',
                            'Se você compila iOS algumas vezes por semana, os dois servem. Se está portando vários apps no mesmo mês, conte primeiro os builds e escolha o balde mais barato.']}],
        'faq': [['Quanto custa um minuto de macOS no GitHub Actions?',
                 'A página de cobrança do GitHub lista 0,062 USD por minuto para o runner de macOS, contra 0,006 USD para um runner Linux de 2 núcleos. Consulte a página para ver os preços atuais.'],
                ['Quantos minutos grátis o Codemagic dá?',
                 'A página de preços diz que pessoas físicas recebem 500 minutos grátis por mês em máquinas macOS M2 com uma conta pessoal, zerados no dia um do mês.'],
                ['Os minutos do GitHub Actions são grátis em repositórios públicos?',
                 'A documentação do GitHub diz que os runners padrão hospedados pelo GitHub são gratuitos em repositórios públicos. O crédito que descrevo vale para os privados.'],
                ['Posso usar os dois serviços ao mesmo tempo?', 'Sim. Mantive os fluxos do GitHub nos repositórios antigos e usei o Codemagic nos apps novos. Cada repositório usa um dos dois.']]}}
