# Yazi: edge-to-edge + 3 tuslu gezinmede kesilen arayuz. Kaynak: CalisanAsistani/PROJE_NOTLARI.md (31.10 alt cubuk hatasi) + Uygulama.kt,
# Pentolings/PROJE_NOTLARI.md + Screens.kt/HelpScreen.kt (navigationBarsPadding sirasi), Slinglings commit 69af29f (Screens.kt SettingsScreen),
# Referans/claude_hafiza/edge-to-edge-nav-bar-padding.md, resmi belge developer.android.com/develop/ui/views/layout/edge-to-edge.
POST = {'tags': ['android', 'compose'],
 'id': 'edge-to-edge-three-button-navigation-clipped-ui',
 'app': None,
 'date': '2026-11-23',
 'en': {'slug': 'edge-to-edge-and-three-button-navigation-fixing-clipped-compose-ui',
        'title': 'Edge-to-Edge and 3-Button Navigation: Fixing Clipped Compose UI',
        'desc': 'Why text hides under the Android navigation bar after edge-to-edge, with three real bugs from my apps, the Compose fixes and a test routine.',
        'intro': 'After your app targets SDK 35, the system draws it behind the status bar and the navigation bar. On a gesture phone it often looks fine. On a phone with three buttons the last row can sit under the bar, or a bottom line can '
                 'vanish. Here are three real bugs from my own apps, the fix for each, and the test routine I now use.',
        'sections': [{'h': 'What edge-to-edge changed',
                      'p': ["Android's documentation says edge-to-edge is enforced once your app targets SDK 35 and runs on Android 15 or higher. The window then spans the whole display and draws behind the system bars. On earlier Android versions "
                            'you get the same look by calling enableEdgeToEdge() in the activity. My apps target SDK 36, so on a current phone this is not optional.'],
                      'ul': ['The system does not move your content. Your layout must read the insets, the areas covered by system UI, and pad itself.',
                             'With enableEdgeToEdge() the gesture bar is transparent, but the three-button bar gets a translucent scrim by default.',
                             'So one screen can look right with gestures and wrong with three buttons: a real bar sits over your last row.'],
                      'p2': ['Think of it as a change of contract. Before, the system reserved the bar areas and your layout lived in what remained. Now your layout owns the whole rectangle and you decide where the safe area starts. Most clipped UI '
                             'bugs are places where nobody decided.',
                             'In Compose the two modifiers you need most are statusBarsPadding() for the top and navigationBarsPadding() for the bottom. All three bugs below are small mistakes around them.']},
                     {'h': 'Bug 1: the bar space belonged to an ad',
                      'p': ['In Calisan Asistani, an Android app, the home and settings screens have no banner ad. They slid under the navigation bar. I added navigationBarsPadding() to the page box and thought it was done.',
                            'A few days later it happened again. The real cause: the bottom space came only from the banner, written as Banner(Modifier.navigationBarsPadding()). When the banner was never drawn, because ads were off, consent was '
                            'missing or nothing had loaded, the padding disappeared with it. The content went under the soft buttons.',
                            'The fix is to take the bar space from something that always exists. I put a box with navigationBarsPadding() at the bottom of the page, and the banner lives inside that box only on the screens that show one.'],
                      'ul': ['Before: Banner(Modifier.navigationBarsPadding())', 'After: Box(Modifier.fillMaxWidth().navigationBarsPadding()) { if (showBanner) Banner() }'],
                      'p2': ['Then I tested every screen with ads on and with ads off. The rule is simple: if a padding is attached to an element that can be absent, move it to its parent. This bug needs a specific state, no ad, so it only shows if '
                             'you test that state on purpose.']},
                     {'h': 'Bug 2: padding in the wrong place',
                      'p': ['In Pentolings, the settings and statistics content flowed under the navigation buttons. The memory note I keep for this says it came back after I had fixed it in other games. The cause was the order of modifiers on a '
                            'scrolling column.'],
                      'ul': ['Wrong: Modifier.weight(1f).verticalScroll(state).navigationBarsPadding()', 'Right: Modifier.weight(1f).navigationBarsPadding().verticalScroll(state)'],
                      'p2': ['My explanation from the notes: when the padding comes after verticalScroll, it is added inside the scrolled content. The visible window of the list still reaches the bottom edge of the screen, so the content shows '
                             'through behind the buttons. When the padding comes first, the window itself ends above the bar. The Pentolings screens now use the second order, for example in HelpScreen.kt and Screens.kt.',
                             'A quick check for this bug: scroll to the very end of the screen. The last item must stop fully above the bar, with a little space. If it stops behind the bar, the order is wrong.']},
                     {'h': 'Bug 3: a weight squeezed to zero',
                      'p': ['The settings screen of Slinglings is a column with a title, switches, buttons, a decorative desk scene and a version line. The desk scene used weight(1f) to take whatever height was left, and the version line sat below '
                            'it.',
                            'When the rows above filled the screen, nothing was left for the weight. The scene shrank to zero height and the version line at the very bottom was cut off. A taller phone hid the problem, so it only showed on a small '
                            'screen.'],
                      'ul': ['Before: DeskScene(Modifier.weight(1f))', 'After: verticalScroll on the column, DeskScene(Modifier.height(150.dp))'],
                      'p2': ['The column is now scrollable and the scene has a fixed height. If the content does not fit, the user scrolls instead of losing a line. The same commit also stopped the version line from being a hard-coded text: it '
                             'reads the real version name now.',
                             'There were two ways out: give flexible items a minimum height, or make the screen scrollable. I chose scrolling plus a fixed height, because on a small phone the decorative scene is the first thing to give up.']},
                     {'h': 'Which inset for which job',
                      'p': ['Compose offers several inset modifiers. You do not need all of them, but it helps to know what each one answers.'],
                      'ul': ['statusBarsPadding(): keeps a top bar below the status bar.',
                             'navigationBarsPadding(): keeps bottom content above the navigation bar, in gesture mode and in button mode.',
                             'systemBarsPadding(): both of the above in one modifier.',
                             'imePadding(): keeps a text field above the on-screen keyboard.',
                             'safeDrawingPadding(): system bars, keyboard and display cutouts together.',
                             'Scaffold: hands you an innerPadding value. If you ignore it, the content is not padded at all.'],
                      'p2': ['The Android documentation also lists display cutout insets and system gesture insets. The gesture insets matter when your own swipes start near the screen edge; the docs mention swiping in games as an example. My '
                             'screens mostly use the first two modifiers. I have not needed more, so I cannot tell you from experience how the others behave in every case.']},
                     {'h': 'Large text and longer languages',
                      'p': ['Fixed heights are risky in the other direction too. A button with a fixed height cuts its label when the user sets a larger font. In Pentolings the shared button uses heightIn(min = ...) so it can grow with the text.',
                            'In my notes for other apps I also planned to test at 1.3x and 1.5x font size, because Spanish and Portuguese labels are longer than English ones. I have not run that test on every app yet, and I do not claim it. I treat '
                            'it as a checklist item, not a result.',
                            'Do the arithmetic: at a 1.3 font scale a 14 sp label is drawn at about 18 sp, so the same words need roughly 30 percent more width. A label that fit on one line may now need two, or be cut.',
                            'In the Tilelings design notes I wrote a rule for long labels: one line only, a measurement test, and a fallback to 11 sp, checked on a small phone with a 1.3x font. That is a plan from the notes, not a measured result. '
                            'The same notes list 48 dp touch targets, so a button never shrinks below a finger-sized area.']},
                     {'h': 'The test routine',
                      'p': ['Gesture navigation hides most of these bugs, so I test with the other mode. This is the routine.'],
                      'ul': ['Use an emulator with three-button navigation (I use an Android 11 image).',
                             'Raise the font size to 1.3 with: adb shell settings put system font_scale 1.3 (set it back to 1.0 afterwards).',
                             'Open every screen, scroll to the very bottom and take a screenshot.',
                             'Repeat with the longest language and with a small screen.',
                             'Turn ads off and on, because optional elements change the layout.'],
                      'p2': ['Before each release I now ask three questions. Is the last item of every scrolling screen fully above the bar? Does any bottom space depend on an optional element? Does any flexible item have a fixed minimum? Each step '
                             'above reproduces one bug: three buttons show bugs 1 and 2, a small screen shows bug 3, a large font shows the cut labels, and ads off shows bug 1 again.']}],
        'faq': [['From which target SDK is edge-to-edge enforced?', 'According to the Android documentation, edge-to-edge is enforced on Android 15 (API level 35) and higher once your app targets SDK 35.'],
                ['Does navigationBarsPadding() go before or after verticalScroll?', 'Before. Placed after, the padding scrolls with the content and the list still shows behind the navigation bar.'],
                ['Why does my UI look fine on gesture navigation but break with three buttons?', 'With three buttons a real, translucent navigation bar covers the bottom of the window, so any content without bottom padding sits under it.'],
                ['Why did my bottom line disappear on a small screen?', 'A weight(1f) item shrinks to zero when the other items fill the screen. Make the screen scrollable and give that item a fixed height.']]},
 'tr': {'slug': 'edge-to-edge-ve-3-tuslu-gezinmede-kesilen-arayuz-nasil-duzelir',
        'title': 'Edge-to-Edge ve 3 Tuşlu Gezinmede Kesilen Arayüz Nasıl Düzelir',
        'desc': 'Edge-to-edge sonrası yazılar neden gezinme çubuğunun altında kalır: kendi uygulamalarımdan üç gerçek hata, Compose çözümleri ve test rutini.',
        'intro': "Uygulaman SDK 35'i hedefleyince sistem onu durum çubuğunun ve gezinme çubuğunun arkasına çizer. Hareketli gezinmede çoğu zaman sorun görünmez. Üç tuşlu bir telefonda son satır çubuğun altında kalabilir ya da alttaki bir satır "
                 'kaybolabilir. Kendi uygulamalarımdan üç gerçek hatayı, her birinin çözümünü ve şimdi kullandığım test rutinini anlatıyorum.',
        'sections': [{'h': 'Edge-to-edge neyi değiştirdi',
                      'p': ["Android belgeleri, uygulama SDK 35'i hedefleyip Android 15 veya üstünde çalıştığında edge-to-edge'in zorunlu olduğunu söylüyor. Pencere bütün ekrana yayılır ve sistem çubuklarının arkasına çizilir. Eski Android "
                            "sürümlerinde aynı görünümü etkinlikte enableEdgeToEdge() çağırarak alırsın. Benim uygulamalarım SDK 36'yı hedefliyor, yani güncel bir telefonda bu seçenek değil.",
                            "Belgeler ayrıca şunu da hatırlatıyor: uygulaman zaten edge-to-edge değilse, SDK 35'e geçince bazı bölümleri örtülebilir ve inset'leri sen ele almak zorunda kalırsın. Yani bu iş, hedef SDK'yı yükselttiğin gün başlayan "
                            'bir bakım işidir.'],
                      'ul': ["Sistem içeriğini senin yerine kaydırmaz. Düzenin, sistem arayüzünün kapladığı alanları yani inset'leri okuyup kendine boşluk bırakmalı.",
                             'enableEdgeToEdge() ile hareket çubuğu saydamdır, ama üç tuşlu çubuk varsayılan olarak yarı saydam bir perde alır.',
                             'Yani aynı ekran hareketli gezinmede doğru, üç tuşta yanlış görünebilir: gerçek bir çubuk son satırının üstünde durur.'],
                      'p2': ['Bunu bir sözleşme değişikliği gibi düşün. Eskiden sistem çubuk alanlarını ayırıyordu ve düzenin kalan yerde yaşıyordu. Şimdi düzenin tüm dikdörtgenin sahibi ve güvenli alanın nerede başlayacağına sen karar veriyorsun. '
                             'Kesilen arayüz hatalarının çoğu, kimsenin karar vermediği yerlerdir.',
                             "Compose'ta en çok iki değiştirici lazım: üst için statusBarsPadding(), alt için navigationBarsPadding(). Aşağıdaki üç hatanın hepsi bunların çevresindeki küçük yanlışlar."]},
                     {'h': 'Hata 1: çubuk boşluğu bir reklama bağlıydı',
                      'p': ['Çalışan Asistanı adlı Android uygulamamda ana ekran ve ayarlar sayfalarında banner reklam yok. Bu sayfalar gezinme çubuğunun altına giriyordu. Sayfa kutusuna navigationBarsPadding() ekledim ve bitti sandım.',
                            "Birkaç gün sonra yine oldu. Asıl neden şuydu: alttaki boşluk yalnızca banner'dan geliyordu, yani Banner(Modifier.navigationBarsPadding()) olarak yazılmıştı. Banner hiç çizilmeyince (reklam kapalı, onay yok ya da hiçbir "
                            'şey yüklenmemiş) boşluk da kayboluyordu. İçerik yazılım düğmelerinin altına giriyordu.',
                            'Çözüm, çubuk boşluğunu her zaman var olan bir şeyden almak. Sayfanın altına navigationBarsPadding() olan bir kutu koydum; banner yalnızca onu gösteren ekranlarda bu kutunun içinde yaşıyor.',
                            'Bu hatayı yalnızca ekran görüntüsüyle yakalamak zor; hangi durumda çıktığını bilmek gerekir. Notlarıma durumları da yazdım: banner çizilmediğinde reklamsız mod, UMP onayının olmaması ve reklam izninin olmaması aynı '
                            'sonucu veriyordu.'],
                      'ul': ['Önce: Banner(Modifier.navigationBarsPadding())', 'Sonra: Box(Modifier.fillMaxWidth().navigationBarsPadding()) { if (bannerVar) Banner() }'],
                      'p2': ['Sonra her ekranı reklam açıkken ve kapalıyken denedim. Kural basit: bir boşluk, yokluğu mümkün bir öğeye bağlıysa onu üst öğesine taşı. Bu hata belirli bir durum ister, yani reklamın olmaması; o durumu bilerek '
                             'denemezsen hiç görünmez.']},
                     {'h': 'Hata 2: boşluk yanlış yerde',
                      'p': ["Pentolings'te ayarlar ve istatistik içeriği gezinme düğmelerinin altına akıyordu. Bunun için tuttuğum hafıza notu, başka oyunlarda düzelttikten sonra yeniden çıktığını yazıyor. Neden, kaydırmalı bir sütundaki "
                            'değiştirici sırasıydı.'],
                      'ul': ['Yanlış: Modifier.weight(1f).verticalScroll(state).navigationBarsPadding()', 'Doğru: Modifier.weight(1f).navigationBarsPadding().verticalScroll(state)'],
                      'p2': ["Notlardaki açıklamam şu: boşluk verticalScroll'dan sonra gelirse kaydırılan içeriğin içine eklenir. Listenin görünür penceresi hâlâ ekranın alt kenarına uzanır, içerik düğmelerin arkasından görünür. Boşluk önce gelirse "
                             'pencerenin kendisi çubuğun üstünde biter. Pentolings ekranları artık ikinci sırayı kullanıyor, örneğin HelpScreen.kt ve Screens.kt içinde.',
                             'Bu hata için hızlı bir kontrol: ekranın en sonuna kadar kaydır. Son öğe çubuğun tamamen üstünde, biraz boşlukla durmalı. Çubuğun arkasında duruyorsa sıra yanlıştır.',
                             'Başka bir deyişle sorun hiçbir zaman ekranın kendisinde değildi. Sorun, kaydırma penceresinin nerede bittiğiydi.']},
                     {'h': 'Hata 3: sıfıra sıkışan weight',
                      'p': ["Slinglings'in ayarlar ekranı bir sütun: başlık, anahtarlar, düğmeler, süs olarak bir masa sahnesi ve bir sürüm satırı. Masa sahnesi kalan yüksekliği almak için weight(1f) kullanıyordu, sürüm satırı da altındaydı.",
                            "Üstteki satırlar ekranı doldurunca weight'e hiçbir şey kalmıyordu. Sahne sıfır yüksekliğe iniyor, en alttaki sürüm satırı kesiliyordu. Daha uzun bir telefon sorunu gizliyordu, o yüzden yalnızca küçük ekranda "
                            'görünüyordu.'],
                      'ul': ['Önce: DeskScene(Modifier.weight(1f))', 'Sonra: sütunda verticalScroll, DeskScene(Modifier.height(150.dp))'],
                      'p2': ['Sütun artık kaydırılabilir ve sahnenin sabit bir yüksekliği var. İçerik sığmazsa kullanıcı kaydırır, bir satırı kaybetmez. Aynı değişiklik sürüm satırını da sabit yazı olmaktan çıkardı: artık gerçek sürüm adını okuyor.',
                             'İki çıkış yolu vardı: esnek öğelere asgari yükseklik vermek ya da ekranı kaydırılabilir yapmak. Kaydırma artı sabit yükseklik seçtim, çünkü küçük telefonda süs sahnesi vazgeçilecek ilk şey.',
                             'Bu hatayı denemek için küçük bir cihaz profili kullan; asıl hata yalnızca ekran yüksekliği içeriğe yetmediğinde görünür.']},
                     {'h': 'Hangi iş için hangi inset',
                      'p': ['Compose birkaç inset değiştiricisi sunar. Hepsine ihtiyacın yok, ama her birinin neyi yanıtladığını bilmek işe yarar.'],
                      'ul': ['statusBarsPadding(): üst çubuğu durum çubuğunun altında tutar.',
                             'navigationBarsPadding(): alttaki içeriği gezinme çubuğunun üstünde tutar; hareket kipinde de düğme kipinde de.',
                             'systemBarsPadding(): yukarıdakilerin ikisi tek değiştiricide.',
                             'imePadding(): bir metin alanını ekran klavyesinin üstünde tutar.',
                             'safeDrawingPadding(): sistem çubukları, klavye ve ekran çentiklerini birlikte kapsar.',
                             'Scaffold: sana bir innerPadding değeri verir. Onu görmezden gelirsen içerik hiç boşluk almaz.'],
                      'p2': ["Android belgeleri ayrıca ekran çentiği inset'lerini ve sistem hareketi inset'lerini sayıyor. Hareket inset'leri, kendi kaydırma hareketlerin ekran kenarına yakın başladığında önemli; belgeler örnek olarak oyunlardaki "
                             'kaydırmayı anıyor. Benim ekranlarım çoğunlukla ilk iki değiştiriciyi kullanıyor. Fazlasına ihtiyaç duymadım, bu yüzden diğerlerinin her durumda nasıl davrandığını deneyimimden söyleyemem.']},
                     {'h': 'Büyük yazı ve uzun diller',
                      'p': ["Sabit yükseklik öbür yönde de risklidir. Sabit yükseklikli bir düğme, kullanıcı daha büyük yazı seçince etiketini keser. Pentolings'te ortak düğme heightIn(min = ...) kullanır, böylece yazıyla birlikte büyüyebilir.",
                            'Diğer uygulamalar için notlarımda 1.3x ve 1.5x yazı boyutunda test de planladım; çünkü İspanyolca ve Portekizce etiketler İngilizceden uzun. Bu testi her uygulamada henüz çalıştırmadım ve yaptım demiyorum. Onu sonuç '
                            'değil, kontrol listesi maddesi sayıyorum.',
                            "Hesabı yap: 1.3 yazı ölçeğinde 14 sp'lik bir etiket yaklaşık 18 sp çizilir, yani aynı kelimeler kabaca yüzde 30 daha fazla genişlik ister. Tek satıra sığan bir etiket artık iki satır isteyebilir ya da kesilebilir.",
                            "Tilelings tasarım notlarında uzun etiketler için bir kural yazdım: yalnızca tek satır, bir ölçü testi ve 11 sp'ye düşme planı; küçük bir telefonda 1.3x yazıyla denenecek. Bu notlardaki bir plan, ölçülmüş bir sonuç "
                            'değil. Aynı notlar 48 dp dokunma hedeflerini de sayıyor; yani bir düğme parmak boyutunun altına inmez.']},
                     {'h': 'Test rutini',
                      'p': ['Hareketli gezinme bu hataların çoğunu gizler, bu yüzden öbür kipte test ediyorum. Rutin şu.',
                            'Hareketli gezinme açıkken bu hataların çoğu görünmez; üç tuş kipini bilerek açmazsan haftalarca fark etmezsin. Emülatörde bu ayarı sistem ayarlarından değiştirebilirsin.'],
                      'ul': ['Üç tuşlu gezinmeli bir emülatör kullan (ben Android 11 imajı kullanıyorum).',
                             "Yazı boyutunu 1.3'e çıkar: adb shell settings put system font_scale 1.3 (sonra 1.0'a geri al).",
                             'Her ekranı aç, en alta kadar kaydır ve ekran görüntüsü al.',
                             'En uzun dille ve küçük bir ekranla tekrarla.',
                             'Reklamı kapatıp aç; isteğe bağlı öğeler düzeni değiştirir.'],
                      'p2': ['Her sürümden önce artık üç soru soruyorum. Kaydırmalı her ekranın son öğesi çubuğun tamamen üstünde mi? Herhangi bir alt boşluk isteğe bağlı bir öğeye bağlı mı? Esnek bir öğenin sabit bir asgarisi var mı? Yukarıdaki '
                             'her adım bir hatayı yeniden üretir: üç tuş 1. ve 2. hatayı, küçük ekran 3. hatayı, büyük yazı kesilen etiketleri, reklamı kapatmak da 1. hatayı yeniden gösterir.']}],
        'faq': [["Edge-to-edge hangi hedef SDK'dan itibaren zorunlu?", "Android belgelerine göre uygulama SDK 35'i hedefleyince Android 15 (API 35) ve üstünde edge-to-edge zorunlu olur."],
                ["navigationBarsPadding() verticalScroll'dan önce mi sonra mı gelmeli?", 'Önce. Sonra gelirse boşluk içerikle birlikte kayar ve liste gezinme çubuğunun arkasında görünmeye devam eder.'],
                ['Arayüzüm hareketli gezinmede düzgün, üç tuşta bozuk görünüyor, neden?', 'Üç tuşta gerçek ve yarı saydam bir gezinme çubuğu pencerenin altını kaplar; alt boşluğu olmayan içerik onun altında kalır.'],
                ['Küçük ekranda alttaki satırım neden kayboldu?', 'Diğer öğeler ekranı doldurunca weight(1f) olan öğe sıfıra iner. Ekranı kaydırılabilir yap ve o öğeye sabit yükseklik ver.']]},
 'es': {'slug': 'edge-to-edge-y-navegacion-de-3-botones-arreglar-la-interfaz-recortada',
        'title': 'Edge-to-edge y 3 botones: arreglar la interfaz recortada',
        'desc': 'Por qué el texto queda bajo la barra de navegación tras edge-to-edge: tres errores reales de mis apps, soluciones en Compose y una rutina de pruebas.',
        'intro': 'Cuando tu app apunta al SDK 35, el sistema la dibuja detrás de la barra de estado y de la barra de navegación. Con gestos suele verse bien. En un móvil con tres botones, la última fila puede quedar bajo la barra o una línea '
                 'inferior puede desaparecer. Aquí van tres errores reales de mis propias apps, la solución de cada uno y la rutina de pruebas que uso ahora.',
        'sections': [{'h': 'Qué cambió con edge-to-edge',
                      'p': ['La documentación de Android dice que edge-to-edge es obligatorio cuando tu app apunta al SDK 35 y se ejecuta en Android 15 o superior. La ventana ocupa toda la pantalla y se dibuja detrás de las barras del sistema. En '
                            'versiones anteriores de Android obtienes el mismo aspecto llamando a enableEdgeToEdge() en la actividad. Mis apps apuntan al SDK 36, así que en un móvil actual esto no es opcional.'],
                      'ul': ['El sistema no mueve tu contenido. Tu diseño debe leer los insets, las zonas que cubre la interfaz del sistema, y dejar su propio margen.',
                             'Con enableEdgeToEdge() la barra de gestos es transparente, pero la barra de tres botones recibe por defecto una capa translúcida.',
                             'Así, una misma pantalla puede verse bien con gestos y mal con tres botones: una barra real queda encima de tu última fila.'],
                      'p2': ['Piénsalo como un cambio de contrato. Antes, el sistema reservaba las zonas de las barras y tu diseño vivía en lo que quedaba. Ahora tu diseño es dueño de todo el rectángulo y tú decides dónde empieza el área segura. La '
                             'mayoría de los errores de interfaz recortada son lugares donde nadie decidió.',
                             'En Compose, los dos modificadores que más necesitas son statusBarsPadding() para arriba y navigationBarsPadding() para abajo. Los tres errores de abajo son pequeños fallos alrededor de ellos.']},
                     {'h': 'Error 1: el espacio de la barra dependía de un anuncio',
                      'p': ['En Calisan Asistani, una app de Android, las pantallas de inicio y ajustes no tienen banner. Se metían bajo la barra de navegación. Añadí navigationBarsPadding() a la caja de la página y creí que estaba listo.',
                            'Unos días después volvió a ocurrir. La causa real: el espacio inferior venía solo del banner, escrito como Banner(Modifier.navigationBarsPadding()). Cuando el banner no se dibujaba, porque los anuncios estaban '
                            'desactivados, faltaba el consentimiento o no se había cargado nada, el margen desaparecía con él. El contenido quedaba bajo los botones virtuales.',
                            'La solución es tomar el espacio de la barra de algo que siempre existe. Puse una caja con navigationBarsPadding() al pie de la página, y el banner vive dentro de esa caja solo en las pantallas que lo muestran.'],
                      'ul': ['Antes: Banner(Modifier.navigationBarsPadding())', 'Después: Box(Modifier.fillMaxWidth().navigationBarsPadding()) { if (hayBanner) Banner() }'],
                      'p2': ['Luego probé cada pantalla con anuncios activados y desactivados. La regla es simple: si un margen está ligado a un elemento que puede faltar, llévalo a su contenedor. Este error necesita un estado concreto, la ausencia '
                             'de anuncio, así que solo aparece si pruebas ese estado a propósito.']},
                     {'h': 'Error 2: el margen en el sitio equivocado',
                      'p': ['En Pentolings, el contenido de ajustes y estadísticas pasaba por debajo de los botones de navegación. La nota que guardo sobre esto dice que volvió a aparecer después de haberlo arreglado en otros juegos. La causa era '
                            'el orden de los modificadores en una columna con desplazamiento.'],
                      'ul': ['Mal: Modifier.weight(1f).verticalScroll(state).navigationBarsPadding()', 'Bien: Modifier.weight(1f).navigationBarsPadding().verticalScroll(state)'],
                      'p2': ['Mi explicación, tomada de las notas: si el margen va después de verticalScroll, se añade dentro del contenido desplazado. La ventana visible de la lista sigue llegando al borde inferior de la pantalla, y el contenido '
                             'se ve por detrás de los botones. Si el margen va primero, la propia ventana termina sobre la barra. Las pantallas de Pentolings usan ahora el segundo orden, por ejemplo en HelpScreen.kt y Screens.kt.',
                             'Una comprobación rápida para este error: desplázate hasta el final de la pantalla. El último elemento debe detenerse por completo sobre la barra, con un poco de espacio. Si se detiene detrás de la barra, el orden es '
                             'incorrecto.']},
                     {'h': 'Error 3: un weight reducido a cero',
                      'p': ['La pantalla de ajustes de Slinglings es una columna con título, interruptores, botones, una escena decorativa de escritorio y una línea de versión. La escena usaba weight(1f) para tomar la altura que sobrara, y la línea '
                            'de versión estaba debajo.',
                            'Cuando las filas de arriba llenaban la pantalla, no quedaba nada para el weight. La escena se reducía a altura cero y la línea de versión, al final, se cortaba. Un móvil más alto escondía el problema, así que solo '
                            'aparecía en pantallas pequeñas.'],
                      'ul': ['Antes: DeskScene(Modifier.weight(1f))', 'Después: verticalScroll en la columna, DeskScene(Modifier.height(150.dp))'],
                      'p2': ['Ahora la columna se desplaza y la escena tiene altura fija. Si el contenido no cabe, el usuario se desplaza en lugar de perder una línea. El mismo cambio hizo que la línea de versión dejara de ser un texto fijo: ahora '
                             'lee el nombre de versión real.',
                             'Había dos salidas: dar una altura mínima a los elementos flexibles o hacer la pantalla desplazable. Elegí desplazamiento más altura fija, porque en un móvil pequeño la escena decorativa es lo primero a lo que se '
                             'renuncia.']},
                     {'h': 'Qué inset para cada tarea',
                      'p': ['Compose ofrece varios modificadores de insets. No necesitas todos, pero conviene saber qué responde cada uno.'],
                      'ul': ['statusBarsPadding(): mantiene una barra superior debajo de la barra de estado.',
                             'navigationBarsPadding(): mantiene el contenido inferior sobre la barra de navegación, tanto con gestos como con botones.',
                             'systemBarsPadding(): los dos anteriores en un solo modificador.',
                             'imePadding(): mantiene un campo de texto sobre el teclado en pantalla.',
                             'safeDrawingPadding(): barras del sistema, teclado y recortes de pantalla a la vez.',
                             'Scaffold: te entrega un valor innerPadding. Si lo ignoras, el contenido no recibe ningún margen.'],
                      'p2': ['La documentación de Android también menciona los insets de recorte de pantalla y los insets de gestos del sistema. Los de gestos importan cuando tus propios deslizamientos empiezan cerca del borde; la documentación '
                             'menciona como ejemplo el deslizamiento en juegos. Mis pantallas usan sobre todo los dos primeros modificadores. No he necesitado más, así que no puedo decirte por experiencia cómo se comportan los demás en cada caso.']},
                     {'h': 'Texto grande e idiomas más largos',
                      'p': ['Las alturas fijas también son un riesgo en el otro sentido. Un botón con altura fija corta su etiqueta cuando el usuario elige una fuente mayor. En Pentolings el botón común usa heightIn(min = ...) para poder crecer con '
                            'el texto.',
                            'En mis notas de otras apps también planeé probar con fuente de 1.3x y 1.5x, porque las etiquetas en español y portugués son más largas que en inglés. Todavía no he hecho esa prueba en todas las apps y no digo que lo '
                            'haya hecho. La trato como un punto de la lista, no como un resultado.',
                            'Haz la cuenta: con una escala de fuente de 1.3, una etiqueta de 14 sp se dibuja a unos 18 sp, así que las mismas palabras necesitan cerca de un 30 por ciento más de ancho. Una etiqueta que cabía en una línea puede '
                            'necesitar dos, o cortarse.',
                            'En las notas de diseño de Tilelings escribí una regla para etiquetas largas: una sola línea, una prueba de medición y una reducción a 11 sp, comprobadas en un móvil pequeño con fuente 1.3x. Es un plan de las notas, no '
                            'un resultado medido. Las mismas notas listan objetivos táctiles de 48 dp, para que un botón nunca baje del tamaño de un dedo.']},
                     {'h': 'La rutina de pruebas',
                      'p': ['La navegación por gestos esconde la mayoría de estos errores, así que pruebo con el otro modo. Esta es la rutina.'],
                      'ul': ['Usa un emulador con navegación de tres botones (yo uso una imagen de Android 11).',
                             'Sube el tamaño de fuente a 1.3 con: adb shell settings put system font_scale 1.3 (después vuelve a 1.0).',
                             'Abre cada pantalla, desplázate hasta el final y haz una captura.',
                             'Repite con el idioma más largo y con una pantalla pequeña.',
                             'Activa y desactiva los anuncios, porque los elementos opcionales cambian el diseño.'],
                      'p2': ['Antes de cada versión me hago ahora tres preguntas. ¿El último elemento de cada pantalla desplazable queda por completo sobre la barra? ¿Algún espacio inferior depende de un elemento opcional? ¿Algún elemento flexible '
                             'tiene un mínimo fijo? Cada paso anterior reproduce un error: tres botones muestran los errores 1 y 2, una pantalla pequeña muestra el 3, una fuente grande muestra las etiquetas cortadas, y desactivar los anuncios '
                             'vuelve a mostrar el 1.']}],
        'faq': [['¿Desde qué SDK de destino es obligatorio edge-to-edge?', 'Según la documentación de Android, edge-to-edge es obligatorio en Android 15 (nivel de API 35) y superior cuando tu app apunta al SDK 35.'],
                ['¿navigationBarsPadding() va antes o después de verticalScroll?', 'Antes. Si va después, el margen se desplaza con el contenido y la lista sigue viéndose detrás de la barra de navegación.'],
                ['¿Por qué mi interfaz se ve bien con gestos pero falla con tres botones?', 'Con tres botones una barra de navegación real y translúcida cubre la parte inferior de la ventana, y el contenido sin margen inferior queda debajo.'],
                ['¿Por qué desapareció mi línea inferior en una pantalla pequeña?', 'Un elemento con weight(1f) se reduce a cero cuando los demás llenan la pantalla. Haz la pantalla desplazable y dale a ese elemento una altura fija.']]},
 'pt': {'slug': 'edge-to-edge-e-navegacao-de-3-botoes-corrigindo-a-interface-cortada',
        'title': 'Edge-to-edge e 3 botões: corrija a interface cortada',
        'desc': 'Por que o texto fica sob a barra de navegação após o edge-to-edge: três bugs reais dos meus apps, correções no Compose e uma rotina de testes.',
        'intro': 'Quando o seu app mira o SDK 35, o sistema o desenha atrás da barra de status e da barra de navegação. Com gestos, quase sempre parece bem. Em um celular com três botões, a última linha pode ficar sob a barra ou uma linha inferior '
                 'pode sumir. Aqui estão três bugs reais dos meus próprios apps, a correção de cada um e a rotina de testes que uso agora.',
        'sections': [{'h': 'O que o edge-to-edge mudou',
                      'p': ['A documentação do Android diz que o edge-to-edge é obrigatório quando o app mira o SDK 35 e roda no Android 15 ou superior. A janela ocupa a tela inteira e é desenhada atrás das barras do sistema. Em versões anteriores '
                            'do Android, você obtém o mesmo visual chamando enableEdgeToEdge() na activity. Meus apps miram o SDK 36, então em um celular atual isso não é opcional.'],
                      'ul': ['O sistema não move o seu conteúdo. Seu layout precisa ler os insets, as áreas cobertas pela interface do sistema, e reservar o próprio espaço.',
                             'Com enableEdgeToEdge() a barra de gestos é transparente, mas a barra de três botões recebe por padrão uma camada translúcida.',
                             'Assim, a mesma tela pode ficar certa com gestos e errada com três botões: uma barra de verdade fica por cima da sua última linha.'],
                      'p2': ['Pense nisso como uma mudança de contrato. Antes, o sistema reservava as áreas das barras e o seu layout vivia no que sobrava. Agora o seu layout é dono de todo o retângulo e você decide onde começa a área segura. A '
                             'maioria dos bugs de interface cortada são lugares onde ninguém decidiu.',
                             'No Compose, os dois modificadores mais usados são statusBarsPadding() para o topo e navigationBarsPadding() para a base. Os três bugs abaixo são pequenos erros em torno deles.']},
                     {'h': 'Bug 1: o espaço da barra dependia de um anúncio',
                      'p': ['No Calisan Asistani, um app Android, as telas inicial e de ajustes não têm banner. Elas entravam sob a barra de navegação. Adicionei navigationBarsPadding() à caixa da página e achei que estava pronto.',
                            'Alguns dias depois aconteceu de novo. A causa real: o espaço inferior vinha só do banner, escrito como Banner(Modifier.navigationBarsPadding()). Quando o banner não era desenhado, porque os anúncios estavam desligados, '
                            'faltava o consentimento ou nada tinha carregado, o espaço sumia junto. O conteúdo ficava sob os botões virtuais.',
                            'A correção é tirar o espaço da barra de algo que sempre existe. Coloquei uma caixa com navigationBarsPadding() no fim da página, e o banner vive dentro dessa caixa só nas telas que o mostram.'],
                      'ul': ['Antes: Banner(Modifier.navigationBarsPadding())', 'Depois: Box(Modifier.fillMaxWidth().navigationBarsPadding()) { if (temBanner) Banner() }'],
                      'p2': ['Depois testei cada tela com anúncios ligados e desligados. A regra é simples: se um espaço está preso a um elemento que pode estar ausente, leve-o para o contêiner dele. Esse bug exige um estado específico, a ausência '
                             'de anúncio, então só aparece se você testar esse estado de propósito.']},
                     {'h': 'Bug 2: o espaço no lugar errado',
                      'p': ['No Pentolings, o conteúdo de ajustes e estatísticas passava por baixo dos botões de navegação. A nota que guardo sobre isso diz que o problema voltou depois de eu o corrigir em outros jogos. A causa era a ordem dos '
                            'modificadores em uma coluna com rolagem.'],
                      'ul': ['Errado: Modifier.weight(1f).verticalScroll(state).navigationBarsPadding()', 'Certo: Modifier.weight(1f).navigationBarsPadding().verticalScroll(state)'],
                      'p2': ['Minha explicação, tirada das notas: se o espaço vem depois de verticalScroll, ele é adicionado dentro do conteúdo rolável. A janela visível da lista continua chegando à borda inferior da tela, e o conteúdo aparece por '
                             'trás dos botões. Se o espaço vem primeiro, a própria janela termina acima da barra. As telas do Pentolings agora usam a segunda ordem, por exemplo em HelpScreen.kt e Screens.kt.',
                             'Uma verificação rápida para esse bug: role até o final da tela. O último item deve parar totalmente acima da barra, com um pouco de espaço. Se parar atrás da barra, a ordem está errada.']},
                     {'h': 'Bug 3: um weight espremido até zero',
                      'p': ['A tela de ajustes do Slinglings é uma coluna com título, chaves, botões, uma cena decorativa de mesa e uma linha de versão. A cena usava weight(1f) para pegar a altura que sobrasse, e a linha de versão ficava embaixo.',
                            'Quando as linhas de cima enchiam a tela, não sobrava nada para o weight. A cena encolhia para altura zero e a linha de versão, no fim, era cortada. Um celular mais alto escondia o problema, então ele só aparecia em '
                            'telas pequenas.'],
                      'ul': ['Antes: DeskScene(Modifier.weight(1f))', 'Depois: verticalScroll na coluna, DeskScene(Modifier.height(150.dp))'],
                      'p2': ['Agora a coluna rola e a cena tem altura fixa. Se o conteúdo não cabe, o usuário rola em vez de perder uma linha. A mesma mudança também fez a linha de versão deixar de ser um texto fixo: agora ela lê o nome de versão '
                             'real.',
                             'Havia duas saídas: dar uma altura mínima aos itens flexíveis ou tornar a tela rolável. Escolhi rolagem mais altura fixa, porque em um celular pequeno a cena decorativa é a primeira coisa a ser sacrificada.']},
                     {'h': 'Qual inset para cada tarefa',
                      'p': ['O Compose oferece vários modificadores de insets. Você não precisa de todos, mas ajuda saber o que cada um responde.'],
                      'ul': ['statusBarsPadding(): mantém uma barra superior abaixo da barra de status.',
                             'navigationBarsPadding(): mantém o conteúdo inferior acima da barra de navegação, tanto com gestos quanto com botões.',
                             'systemBarsPadding(): os dois anteriores em um só modificador.',
                             'imePadding(): mantém um campo de texto acima do teclado na tela.',
                             'safeDrawingPadding(): barras do sistema, teclado e recortes de tela juntos.',
                             'Scaffold: entrega um valor innerPadding. Se você o ignora, o conteúdo não recebe espaço nenhum.'],
                      'p2': ['A documentação do Android também lista os insets de recorte de tela e os insets de gestos do sistema. Os de gestos importam quando os seus próprios deslizes começam perto da borda; a documentação cita como exemplo o '
                             'deslize em jogos. Minhas telas usam principalmente os dois primeiros modificadores. Não precisei de mais, então não posso dizer por experiência como os outros se comportam em cada caso.']},
                     {'h': 'Texto grande e idiomas mais longos',
                      'p': ['Alturas fixas também são arriscadas no outro sentido. Um botão com altura fixa corta o rótulo quando o usuário escolhe uma fonte maior. No Pentolings o botão comum usa heightIn(min = ...) para poder crescer com o texto.',
                            'Nas minhas notas de outros apps também planejei testar com fonte de 1.3x e 1.5x, porque os rótulos em espanhol e português são mais longos que em inglês. Ainda não fiz esse teste em todos os apps e não afirmo que fiz. '
                            'Trato isso como item de checklist, não como resultado.',
                            'Faça a conta: com escala de fonte 1.3, um rótulo de 14 sp é desenhado a cerca de 18 sp, então as mesmas palavras precisam de uns 30 por cento mais de largura. Um rótulo que cabia em uma linha pode precisar de duas, ou '
                            'ser cortado.',
                            'Nas notas de design do Tilelings escrevi uma regra para rótulos longos: uma linha só, um teste de medição e uma redução para 11 sp, verificados em um celular pequeno com fonte 1.3x. É um plano das notas, não um '
                            'resultado medido. As mesmas notas listam alvos de toque de 48 dp, para que um botão nunca fique menor que um dedo.']},
                     {'h': 'A rotina de testes',
                      'p': ['A navegação por gestos esconde a maioria desses bugs, então testo com o outro modo. Esta é a rotina.'],
                      'ul': ['Use um emulador com navegação de três botões (eu uso uma imagem do Android 11).',
                             'Aumente a fonte para 1.3 com: adb shell settings put system font_scale 1.3 (depois volte para 1.0).',
                             'Abra cada tela, role até o final e tire uma captura.',
                             'Repita com o idioma mais longo e com uma tela pequena.',
                             'Ligue e desligue os anúncios, porque elementos opcionais mudam o layout.'],
                      'p2': ['Antes de cada versão faço agora três perguntas. O último item de cada tela rolável fica totalmente acima da barra? Algum espaço inferior depende de um elemento opcional? Algum item flexível tem um mínimo fixo? Cada '
                             'passo acima reproduz um bug: três botões mostram os bugs 1 e 2, uma tela pequena mostra o 3, uma fonte grande mostra os rótulos cortados, e desligar os anúncios mostra o 1 de novo.']}],
        'faq': [['A partir de qual SDK de destino o edge-to-edge é obrigatório?', 'Segundo a documentação do Android, o edge-to-edge é obrigatório no Android 15 (API 35) e superior quando o app mira o SDK 35.'],
                ['O navigationBarsPadding() vai antes ou depois do verticalScroll?', 'Antes. Se vier depois, o espaço rola junto com o conteúdo e a lista continua aparecendo atrás da barra de navegação.'],
                ['Por que minha interface fica boa com gestos mas quebra com três botões?', 'Com três botões uma barra de navegação real e translúcida cobre a base da janela, e o conteúdo sem espaço inferior fica embaixo dela.'],
                ['Por que a minha linha inferior sumiu em uma tela pequena?', 'Um item com weight(1f) encolhe a zero quando os outros enchem a tela. Torne a tela rolável e dê a esse item uma altura fixa.']]}}
