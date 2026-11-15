# Rehber: Uzay Günlüğü ekranları (Türkiye uzaydan, dönen Dünya, ISS, asteroitler, albüm). Yayın gününe kadar gen_guides.py GUIDE_MODULES'e EKLENMEZ.
GUIDE = {
    "id": "space-screens", "app": "uzaygunlugu", "date": "2026-11-16",
    "en": {
        "slug": "what-the-earth-turkey-and-iss-screens-show-in-uzay-gunlugu",
        "title": "What the Turkey, Earth and ISS Screens Show in Uzay Gunlugu",
        "desc": "What am I looking at? A plain guide to the space card, Turkey satellite view, rotating Earth, ISS position and asteroid list in Uzay Gunlugu.",
        "intro": "Uzay Gunlugu (Space Journal) mixes a daily space card with satellite images and live numbers. This guide explains what each screen shows, where the picture or number comes from, how fresh it is and where its limits are. The app's interface is in Turkish, so the Turkish labels are given in brackets where they help.",
        "sections": [
            {"h": "The big picture: one daily file and a few live sources", "p": [
                "The app has five tabs: Today (Bugün), Turkey (Türkiye), Earth (Dünya), ISS and Album. They do not all work the same way. The 61 space cards are bundled inside the app, so they open even without internet. Everything else is fetched online.",
                "Most of the changing information comes from one small data file that the developer publishes once a day. It holds the Earth frames, the asteroid list and a link to the astronomy picture of the day. The app downloads it when you open it and keeps a copy. If the download fails, it shows the last saved copy, so numbers can be older than they look when you are offline. The satellite image of Turkey and the world map come straight from NASA's public GIBS/Worldview service. The ISS position comes from a separate public service, wheretheiss.at.",
                "One important note: Uzay Gunlugu is an independent app. It is not affiliated with or endorsed by NASA. It only uses publicly available images and data, and it names the source on every screen."]},
            {"h": "The card of the day and the album", "p": [
                "The Today screen opens with the card of the day: a space photograph, its category (for example a nebula, a planet or Earth from orbit), a short note in Turkish, the image credit and an Open in archive link to the original page. The notes were written by hand for the set of 61 cards. They are meant as a quick, friendly caption, not a full lesson.",
                "The card is not random on your phone. The 61 cards are put in one fixed shuffled order, and the number of days since a fixed date decides which one is today's. So everyone sees the same card on the same day, and after 61 days the cycle starts again. Tap the picture to open it full screen, zoom in, share it or set it as wallpaper."]},
            {"h": "Streak and album: how the counting works", "ul": [
                "The first time you open the app on a given day, that day's card is added to your album automatically. A box on the Today screen tells you when a new card was added. Opening the app again the same day changes nothing.",
                "The streak counts consecutive days. If you opened the app yesterday and open it today, it grows by one. Skip a full day and it starts again from one. The flame number next to the title shows the current streak, and it disappears when the streak is broken.",
                "The album shows how many of the 61 cards you have collected, with collected ones first. The album and streak are stored on your device, not in an account."]},
            {"h": "Turkey from space", "p": [
                "This screen shows a true-colour satellite picture of Turkey and the sea around it. It comes from the VIIRS instrument on the NOAA-21 satellite, served through NASA's GIBS/Worldview. True colour means it looks roughly like a photograph: land, sea and clouds.",
                "The default image is yesterday's, built from the satellite passes of that day. There is no image for today because it has not been assembled yet. Use the previous day and next buttons to move through earlier days; the date is shown between them. Clouds are the main limit: on a cloudy day you simply see clouds, and parts of the land can be hidden."]},
            {"h": "Night lights: a fixed map, not a live view", "p": [
                "The Night lights button shows how cities glow after dark. It is easy to misread, so note this: it is a fixed map built from satellite images collected over the whole year 2016, and the app labels it as a yearly average. It is not last night's view and it has no date buttons.",
                "Use it to compare regions: big cities, coastlines and highways stand out as bright areas, and sparsely populated regions look dark. Do not use it to judge today's situation anywhere."]},
            {"h": "Earth now: the rotating Earth", "p": [
                "The Earth screen plays a short loop of pictures of the whole planet taken from a camera on the DSCOVR spacecraft (the EPIC instrument), about a million kilometres away. The app takes the frames of the newest day available and plays them one after another, so you can watch the planet turn. Play and Pause control the loop.",
                "Under the image you see the time of the current frame in UTC (not your local time), the date of the frames and the latitude and longitude at the centre of the picture. The frames are not live: the newest set is usually from a day or two earlier, and the date tells you exactly which. The sunlit side of Earth is the part you see, which is why the picture changes through the day. If frames cannot be loaded, the screen asks you to check your connection."]},
            {"h": "ISS now: reading the numbers", "p": [
                "The ISS screen puts a marker on a world map. The position is requested again every five seconds while the screen is open, so you can watch the marker creep along. The map behind it is a still picture of Earth's surface, not a live view with clouds or day and night shading.",
                "Below the map the app lists four rows. Latitude and longitude give the point on the ground directly under the station. Height is the altitude above the surface in kilometres; the station orbits at roughly 400 km. Speed is shown in kilometres per hour. The last row says whether it is day or night on the ground below the station. A button opens a live camera view from the station on YouTube in your browser, if that stream is available at the time.",
                "Remember what this is not: the marker is a position on a map, not a prediction of when the station will pass over your house, and the app does not tell you when to look up."]},
            {"h": "Asteroids this week: a list to read, not an alarm", "p": [
                "The Today screen ends with a short list of near-Earth asteroids. It comes from NASA/JPL's CNEOS and covers close approaches in roughly the coming two weeks, up to a fixed distance limit. The app shows the first five by date. Each row gives the date and time (UTC), the asteroid's designation, how far away it passes, an estimated size and its speed in kilometres per second.",
                "Distance is written in Moon distances, because kilometres are hard to feel. The Moon is about 384,000 km away, so a pass at 8.0 times the Moon's distance is roughly three million kilometres. If an asteroid passes closer than the Moon, the row says so as a percentage of the Moon's distance. Size is only an estimate worked out from the object's brightness, and the app compares it with a car, a bus, an apartment building or a football field to give you a feel for it.",
                "These are routine, scheduled flybys. The list is informational and is not a hazard warning."]},
            {"h": "Quick limits checklist", "ul": [
                "Interface and card notes are in Turkish only for now.",
                "Satellite picture of Turkey: yesterday at the newest, and cloud cover can hide the ground.",
                "Night lights: a fixed 2016 yearly composite, never daily.",
                "Rotating Earth: recent frames, usually not from today; the time shown is UTC.",
                "ISS: position refreshes every five seconds, but the map under it is a still image.",
                "Asteroids: estimated sizes and a short window; not a safety tool."]},
        ],
        "faq": [
            ["Is Uzay Gunlugu made by NASA?", "No. It is an independent app and is not affiliated with or endorsed by NASA. It uses publicly available images and data and names the source of each one."],
            ["Is the Turkey picture live?", "No. It is a true-colour image of yesterday at the newest. You can go back day by day. The Night lights view is a fixed 2016 yearly map."],
            ["How often does the ISS position update?", "About every five seconds while the ISS screen is open. If the connection drops, the last position stays on screen until a new one arrives."],
            ["Are the asteroids dangerous?", "The list is informational. It shows scheduled close approaches with their distance in Moon distances, and it is not a hazard warning."],
            ["How do I keep my streak?", "Open the app at least once every calendar day. Skipping a whole day resets the streak to one, while opening it several times in one day does not add extra."],
        ],
    },
    "tr": {
        "slug": "uzay-gunlugu-turkiye-dunya-ve-iss-ekranlari-ne-gosteriyor",
        "title": "Uzay Günlüğü'nde Türkiye, Dünya ve ISS Ekranları Ne Gösteriyor?",
        "desc": "Ne görüyorum? Uzay Günlüğü'ndeki uzay kartını, Türkiye uydu görüntüsünü, dönen Dünya'yı, canlı ISS konumunu ve asteroit listesini nasıl okuyacağını öğren.",
        "intro": "Uzay Günlüğü, günlük bir uzay kartını uydu görüntüleri ve canlı sayılarla birleştirir. Bu rehber her ekranın ne gösterdiğini, görüntünün ya da sayının nereden geldiğini, ne kadar taze olduğunu ve sınırlarını anlatıyor.",
        "sections": [
            {"h": "Genel yapı: günlük bir dosya ve birkaç canlı kaynak", "p": [
                "Uygulamada beş sekme var: Bugün, Türkiye, Dünya, ISS ve Albüm. Hepsi aynı şekilde çalışmaz. 61 uzay kartı uygulamanın içine gömülüdür; internet olmadan da açılır. Geri kalan her şey internetten çekilir.",
                "Değişen bilgilerin çoğu, geliştiricinin günde bir kez yayımladığı küçük bir veri dosyasından gelir. Bu dosyada Dünya kareleri, asteroit listesi ve günün astronomi fotoğrafının bağlantısı bulunur. Uygulama dosyayı açılışta indirir ve bir kopyasını saklar. İndirme başarısız olursa son kaydedilen kopyayı gösterir; yani çevrimdışıyken sayılar göründüğünden eski olabilir. Türkiye'nin uydu görüntüsü ve dünya haritası doğrudan NASA'nın herkese açık GIBS/Worldview hizmetinden gelir. ISS konumu ise ayrı bir herkese açık hizmetten, wheretheiss.at'ten alınır.",
                "Önemli bir not: Uzay Günlüğü bağımsız bir uygulamadır. NASA ile bağlantısı ya da NASA'nın onayı yoktur. Yalnızca herkese açık görüntü ve verileri kullanır ve her ekranda kaynağı belirtir."]},
            {"h": "Günün kartı ve albüm", "p": [
                "Bugün ekranı günün kartıyla açılır: bir uzay fotoğrafı, kategorisi (örneğin nebula, gezegen ya da yörüngeden Dünya), kısa bir Türkçe not, görüntü kredisi ve özgün sayfaya giden \"Arşivde aç\" bağlantısı. Notlar, 61 kartlık takım için tek tek elle yazıldı. Tam bir ders değil, hızlı ve samimi bir alt yazı olarak düşünüldü.",
                "Kart telefonunda rastgele seçilmez. 61 kart sabit bir karışık sıraya konur ve belirli bir tarihten bu yana geçen gün sayısı bugünün kartını belirler. Yani herkes aynı gün aynı kartı görür ve 61 gün sonra döngü baştan başlar. Görsele dokunarak tam ekran açabilir, yakınlaştırabilir, paylaşabilir ya da duvar kağıdı yapabilirsin."]},
            {"h": "Seri ve albüm nasıl sayılır?", "ul": [
                "Bir günde uygulamayı ilk açışında o günün kartı albümüne otomatik eklenir. Bugün ekranındaki bir kutu yeni kartın eklendiğini söyler. Aynı gün uygulamayı tekrar açmak hiçbir şeyi değiştirmez.",
                "Seri art arda günleri sayar. Dün açtıysan ve bugün de açarsan bir artar. Tam bir günü atlarsan yeniden bire döner. Başlığın yanındaki alev ve sayı güncel seriyi gösterir; seri kopunca kaybolur.",
                "Albüm, 61 kartın kaçını topladığını gösterir; toplananlar öne alınır. Albüm ve seri bir hesapta değil, cihazında saklanır."]},
            {"h": "Türkiye uzaydan", "p": [
                "Bu ekran Türkiye'nin ve çevresindeki denizlerin gerçek renkli bir uydu görüntüsünü gösterir. Görüntü, NOAA-21 uydusundaki VIIRS aygıtından gelir ve NASA'nın GIBS/Worldview hizmetiyle sunulur. Gerçek renk, görüntünün kabaca bir fotoğraf gibi görünmesi demektir: kara, deniz ve bulutlar.",
                "Varsayılan görüntü dünküdür ve o günkü uydu geçişlerinden birleştirilir. Bugün için görüntü yoktur, çünkü henüz oluşturulmamıştır. Önceki günlere gitmek için Önceki gün ve Sonraki düğmelerini kullan; tarih ikisinin arasında yazar. En büyük sınır bulutlardır: bulutlu günde yalnızca bulut görürsün ve karanın bir kısmı gizlenebilir."]},
            {"h": "Gece ışıkları: sabit bir harita, canlı görüntü değil", "p": [
                "Gece ışıkları düğmesi şehirlerin karanlıkta nasıl parladığını gösterir. Yanlış anlaşılması kolay olduğu için şunu bil: bu, 2016 yılı boyunca toplanan uydu görüntülerinden birleştirilmiş sabit bir haritadır ve uygulama bunu yıllık ortalama olarak etiketler. Dünkü gecenin görüntüsü değildir ve tarih düğmeleri yoktur.",
                "Bölgeleri karşılaştırmak için kullan: büyük şehirler, kıyılar ve otoyollar parlak alanlar olarak öne çıkar, seyrek nüfuslu bölgeler karanlık görünür. Bugün herhangi bir yerdeki durumu yorumlamak için kullanma."]},
            {"h": "Dünya şimdi: dönen Dünya", "p": [
                "Dünya ekranı, yaklaşık bir milyon kilometre öteden DSCOVR uzay aracındaki bir kameranın (EPIC aygıtı) çektiği, gezegenin tamamını gösteren fotoğrafları kısa bir döngüyle oynatır. Uygulama, elde olan en yeni günün karelerini alır ve art arda oynatır; böylece gezegenin döndüğünü izlersin. Oynat ve Duraklat döngüyü yönetir.",
                "Görselin altında geçerli karenin saati UTC olarak (yerel saatin değil), karelerin tarihi ve görüntünün ortasındaki enlem ve boylam yazar. Kareler canlı değildir: en yeni set genellikle bir iki gün öncesine aittir ve tarih bunu tam olarak söyler. Gördüğün yüz, Dünya'nın Güneş'e dönük tarafıdır; görüntü gün içinde bu yüzden değişir. Kareler yüklenemezse ekran bağlantını kontrol etmeni ister."]},
            {"h": "ISS şimdi: sayıları okumak", "p": [
                "ISS ekranı bir dünya haritasına işaret koyar. Ekran açıkken konum her beş saniyede bir yeniden istenir; işaretin yavaşça ilerlediğini izleyebilirsin. Arkadaki harita Dünya yüzeyinin durağan bir görüntüsüdür; bulut ya da gece-gündüz gölgesi içeren canlı bir görüntü değildir.",
                "Haritanın altında dört satır var. Enlem ve boylam, istasyonun tam altındaki yer noktasını verir. Yükseklik, yüzeyden kilometre cinsinden irtifadır; istasyon kabaca 400 km yükseklikte döner. Hız saatte kilometre olarak yazılır. Son satır, istasyonun altındaki yerde gün mü gece mi olduğunu söyler. Bir düğme, o sırada yayın varsa, istasyondan canlı kamera görüntüsünü tarayıcında YouTube'da açar.",
                "Bunun ne olmadığını unutma: işaret haritada bir konumdur; istasyonun evinin üzerinden ne zaman geçeceğinin tahmini değildir ve uygulama sana ne zaman gökyüzüne bakacağını söylemez."]},
            {"h": "Bu hafta asteroitler: okunacak bir liste, alarm değil", "p": [
                "Bugün ekranının sonunda Dünya'ya yaklaşan asteroitlerin kısa bir listesi var. Liste NASA/JPL'nin CNEOS hizmetinden gelir ve belirli bir mesafe sınırına kadar, yaklaşık önümüzdeki iki haftadaki yakın geçişleri kapsar. Uygulama tarihe göre ilk beşini gösterir. Her satır tarihi ve saati (UTC), asteroidin adını, ne kadar uzaktan geçtiğini, tahmini boyutunu ve saniyedeki kilometre cinsinden hızını verir.",
                "Mesafe Ay mesafesi cinsinden yazılır, çünkü kilometreyi hissetmek zordur. Ay yaklaşık 384.000 km uzaktadır; yani Ay mesafesinin 8,0 katından geçen bir cisim kabaca üç milyon kilometre uzaktan geçer. Bir asteroit Ay'dan daha yakın geçerse satır bunu Ay mesafesinin yüzdesi olarak söyler. Boyut yalnızca cismin parlaklığından hesaplanan bir tahmindir; uygulama onu bir otomobil, otobüs, apartman ya da futbol sahasıyla kıyaslayarak fikir verir.",
                "Bunlar planlı, sıradan yakın geçişlerdir. Liste bilgilendirme amaçlıdır, tehlike uyarısı değildir."]},
            {"h": "Kısa sınırlar listesi", "ul": [
                "Arayüz ve kart notları şimdilik yalnızca Türkçe.",
                "Türkiye uydu görüntüsü: en yeni haliyle dün; bulutlar yeri gizleyebilir.",
                "Gece ışıkları: sabit 2016 yıllık birleşim, asla günlük değil.",
                "Dönen Dünya: yakın tarihli kareler, çoğunlukla bugünden değil; gösterilen saat UTC.",
                "ISS: konum her beş saniyede yenilenir, ama altındaki harita durağan bir görüntü.",
                "Asteroitler: tahmini boyutlar ve kısa bir pencere; güvenlik aracı değil."],
             "p2": ["Bu sınırları bilmek ekranları daha doğru okumana yardım eder. Uygulamanın amacı gökyüzüne kısa bir pencere açmaktır: günün kartına bakar, Türkiye'nin dünkü görüntüsünü ve dönen gezegeni izler, istasyonun o an nerede olduğunu görür ve asteroit listesine göz atarsın. Her sayının ve görüntünün kaynağı ekranda ya da Hakkında bölümünde yazılıdır; merak ettiğin bir şeyin nereden geldiğini oradan kontrol edebilirsin. Hakkında bölümüne Bugün ekranının sağ üstündeki ⓘ simgesinden ulaşılır."]},
        ],
        "faq": [
            ["Uzay Günlüğü NASA'nın uygulaması mı?", "Hayır. Bağımsız bir uygulamadır; NASA ile bağlantısı ya da NASA'nın onayı yoktur. Herkese açık görüntü ve verileri kullanır, her birinin kaynağını belirtir."],
            ["Türkiye görüntüsü canlı mı?", "Hayır. En yeni haliyle dünün gerçek renkli görüntüsüdür; gün gün geriye gidebilirsin. Gece ışıkları görünümü ise sabit bir 2016 yıllık haritadır."],
            ["ISS konumu ne sıklıkla güncellenir?", "ISS ekranı açıkken yaklaşık her beş saniyede bir. Bağlantı kopsa son konum, yenisi gelene kadar ekranda kalır."],
            ["Asteroitler tehlikeli mi?", "Liste bilgilendirme amaçlıdır. Planlı yakın geçişleri Ay mesafesi cinsinden gösterir ve tehlike uyarısı değildir."],
            ["Serimi nasıl korurum?", "Her takvim günü uygulamayı en az bir kez aç. Tam bir günü atlamak seriyi bire döndürür; aynı gün birkaç kez açmak fazladan sayılmaz."],
        ],
    },
    "es": {
        "slug": "que-muestran-las-pantallas-de-turquia-tierra-e-iss-en-uzay-gunlugu",
        "title": "Qué muestran las pantallas Turquía, Tierra e ISS de Uzay Gunlugu",
        "desc": "¿Qué estoy viendo? Guía de la tarjeta espacial, la vista satelital de Turquía, la Tierra giratoria, la posición de la ISS y los asteroides en Uzay Gunlugu.",
        "intro": "Uzay Gunlugu (Diario Espacial) combina una tarjeta espacial diaria con imágenes de satélite y datos en vivo. Esta guía explica qué muestra cada pantalla, de dónde sale la imagen o el número, cuán reciente es y cuáles son sus límites. La interfaz de la app está en turco, así que damos entre paréntesis los nombres turcos cuando ayudan.",
        "sections": [
            {"h": "Visión general: un archivo diario y algunas fuentes en vivo", "p": [
                "La app tiene cinco pestañas: Hoy (Bugün), Turquía (Türkiye), Tierra (Dünya), ISS y Álbum. No todas funcionan igual. Las 61 tarjetas espaciales vienen incluidas dentro de la app, así que se abren incluso sin internet. Todo lo demás se descarga en línea.",
                "La mayor parte de la información cambiante procede de un pequeño archivo de datos que el desarrollador publica una vez al día. Contiene los fotogramas de la Tierra, la lista de asteroides y un enlace a la foto astronómica del día. La app lo descarga al abrirse y guarda una copia. Si la descarga falla, muestra la última copia guardada, de modo que sin conexión los datos pueden ser más antiguos de lo que parecen. La imagen de satélite de Turquía y el mapamundi llegan directamente del servicio público GIBS/Worldview de la NASA. La posición de la ISS viene de otro servicio público, wheretheiss.at.",
                "Una nota importante: Uzay Gunlugu es una app independiente. No está afiliada a la NASA ni cuenta con su respaldo. Solo usa imágenes y datos de acceso público y cita la fuente en cada pantalla."]},
            {"h": "La tarjeta del día y el álbum", "p": [
                "La pantalla Hoy se abre con la tarjeta del día: una fotografía espacial, su categoría (por ejemplo una nebulosa, un planeta o la Tierra desde la órbita), una nota breve en turco, el crédito de la imagen y un enlace Abrir en el archivo que lleva a la página original. Las notas se escribieron a mano para el conjunto de 61 tarjetas. Son un pie de foto rápido y cercano, no una lección completa.",
                "La tarjeta no se elige al azar en tu móvil. Las 61 tarjetas se ordenan en una mezcla fija y el número de días transcurridos desde una fecha fija decide cuál toca hoy. Así, todo el mundo ve la misma tarjeta el mismo día y, pasados 61 días, el ciclo vuelve a empezar. Toca la imagen para abrirla a pantalla completa, ampliarla, compartirla o ponerla de fondo de pantalla."]},
            {"h": "Racha y álbum: cómo se cuenta", "ul": [
                "La primera vez que abres la app en un día, la tarjeta de ese día se añade sola a tu álbum. Un cuadro en la pantalla Hoy avisa de que se añadió una tarjeta nueva. Volver a abrir la app el mismo día no cambia nada.",
                "La racha cuenta días consecutivos. Si abriste la app ayer y la abres hoy, sube en uno. Si te saltas un día entero, vuelve a empezar desde uno. La llama con el número junto al título muestra la racha actual y desaparece cuando se rompe.",
                "El álbum indica cuántas de las 61 tarjetas has reunido, con las reunidas primero. El álbum y la racha se guardan en tu dispositivo, no en una cuenta."]},
            {"h": "Turquía desde el espacio", "p": [
                "Esta pantalla muestra una imagen de satélite en color real de Turquía y los mares que la rodean. Procede del instrumento VIIRS del satélite NOAA-21 y se sirve a través de GIBS/Worldview de la NASA. Color real significa que se parece más o menos a una fotografía: tierra, mar y nubes.",
                "La imagen predeterminada es la de ayer, construida con los pasos del satélite de ese día. No hay imagen de hoy porque todavía no se ha montado. Usa los botones de día anterior y siguiente para moverte por días pasados; la fecha aparece entre ambos. El gran límite son las nubes: en un día nublado solo ves nubes y parte de la tierra puede quedar oculta."]},
            {"h": "Luces nocturnas: un mapa fijo, no una vista en vivo", "p": [
                "El botón de luces nocturnas muestra cómo brillan las ciudades de noche. Es fácil malinterpretarlo, así que ten esto presente: es un mapa fijo construido con imágenes de satélite reunidas durante todo el año 2016, y la app lo etiqueta como promedio anual. No es la vista de anoche y no tiene botones de fecha.",
                "Úsalo para comparar regiones: las grandes ciudades, las costas y las autopistas destacan como zonas brillantes, y las regiones poco pobladas se ven oscuras. No lo uses para juzgar la situación de hoy en ningún lugar."]},
            {"h": "La Tierra ahora: el planeta girando", "p": [
                "La pantalla Tierra reproduce en bucle fotografías del planeta entero tomadas por una cámara de la nave DSCOVR (el instrumento EPIC), a un millón de kilómetros aproximadamente. La app toma los fotogramas del día más reciente disponible y los pasa uno tras otro, para que veas girar el planeta. Reproducir y Pausa controlan el bucle.",
                "Debajo de la imagen aparecen la hora del fotograma actual en UTC (no tu hora local), la fecha de los fotogramas y la latitud y longitud del centro de la imagen. Los fotogramas no son en vivo: el conjunto más reciente suele ser de uno o dos días antes, y la fecha te dice exactamente de cuál. Lo que ves es la cara de la Tierra iluminada por el Sol, por eso la imagen cambia a lo largo del día. Si no se pueden cargar los fotogramas, la pantalla te pide revisar la conexión."]},
            {"h": "La ISS ahora: cómo leer los números", "p": [
                "La pantalla de la ISS coloca un marcador en un mapamundi. Mientras la pantalla está abierta, la posición se vuelve a pedir cada cinco segundos, así que puedes ver cómo avanza el marcador. El mapa de fondo es una imagen fija de la superficie terrestre, no una vista en vivo con nubes o sombra de día y noche.",
                "Bajo el mapa hay cuatro filas. Latitud y longitud dan el punto del suelo justo debajo de la estación. Altura es la altitud sobre la superficie en kilómetros; la estación orbita a unos 400 km. La velocidad se muestra en kilómetros por hora. La última fila indica si en el suelo bajo la estación es de día o de noche. Un botón abre en el navegador, en YouTube, una vista en directo desde la estación, si esa emisión está disponible en ese momento.",
                "Recuerda lo que no es: el marcador es una posición en un mapa, no una predicción de cuándo pasará la estación sobre tu casa, y la app no te dice cuándo mirar al cielo."]},
            {"h": "Asteroides de esta semana: una lista para leer, no una alarma", "p": [
                "La pantalla Hoy termina con una lista corta de asteroides cercanos a la Tierra. Procede del CNEOS de la NASA/JPL y abarca los acercamientos de aproximadamente las dos semanas siguientes, hasta un límite de distancia fijo. La app muestra los cinco primeros por fecha. Cada fila indica la fecha y hora (UTC), la designación del asteroide, a qué distancia pasa, un tamaño estimado y su velocidad en kilómetros por segundo.",
                "La distancia se expresa en distancias a la Luna, porque los kilómetros cuesta imaginarlos. La Luna está a unos 384.000 km, así que un paso a 8,0 veces la distancia lunar equivale a unos tres millones de kilómetros. Si un asteroide pasa más cerca que la Luna, la fila lo dice como porcentaje de la distancia lunar. El tamaño es solo una estimación calculada a partir del brillo del objeto, y la app lo compara con un coche, un autobús, un edificio de apartamentos o un campo de fútbol para dar una idea.",
                "Son sobrevuelos rutinarios y previstos. La lista es informativa y no es una alerta de peligro."]},
            {"h": "Lista rápida de límites", "ul": [
                "La interfaz y las notas de las tarjetas están solo en turco por ahora.",
                "Imagen satelital de Turquía: como mucho la de ayer, y las nubes pueden ocultar el suelo.",
                "Luces nocturnas: un compuesto anual fijo de 2016, nunca diario.",
                "Tierra giratoria: fotogramas recientes, normalmente no de hoy; la hora mostrada es UTC.",
                "ISS: la posición se actualiza cada cinco segundos, pero el mapa de fondo es una imagen fija.",
                "Asteroides: tamaños estimados y una ventana corta; no es una herramienta de seguridad."]},
        ],
        "faq": [
            ["¿Uzay Gunlugu es de la NASA?", "No. Es una app independiente, sin afiliación ni respaldo de la NASA. Usa imágenes y datos de acceso público y cita la fuente de cada uno."],
            ["¿La imagen de Turquía es en vivo?", "No. Es una imagen en color real de ayer, como mucho. Puedes retroceder día a día. La vista de luces nocturnas es un mapa anual fijo de 2016."],
            ["¿Cada cuánto se actualiza la posición de la ISS?", "Más o menos cada cinco segundos mientras la pantalla de la ISS está abierta. Si se corta la conexión, la última posición se queda en pantalla hasta que llegue una nueva."],
            ["¿Son peligrosos los asteroides?", "La lista es informativa. Muestra acercamientos previstos con su distancia en distancias lunares y no es una alerta de peligro."],
            ["¿Cómo mantengo mi racha?", "Abre la app al menos una vez cada día natural. Saltarte un día entero reinicia la racha en uno, y abrirla varias veces el mismo día no suma de más."],
        ],
    },
    "pt": {
        "slug": "o-que-mostram-as-telas-turquia-terra-e-iss-no-uzay-gunlugu",
        "title": "O que mostram as telas Turquia, Terra e ISS no Uzay Gunlugu",
        "desc": "O que estou vendo? Guia do cartão espacial, da vista de satélite da Turquia, da Terra girando, da posição da ISS e dos asteroides no Uzay Gunlugu.",
        "intro": "O Uzay Gunlugu (Diário Espacial) mistura um cartão espacial diário com imagens de satélite e números ao vivo. Este guia explica o que cada tela mostra, de onde vem a imagem ou o número, quão recente ele é e quais são os limites. A interface do app está em turco, então indicamos os nomes turcos entre parênteses quando ajuda.",
        "sections": [
            {"h": "Visão geral: um arquivo diário e algumas fontes ao vivo", "p": [
                "O app tem cinco abas: Hoje (Bugün), Turquia (Türkiye), Terra (Dünya), ISS e Álbum. Elas não funcionam todas do mesmo jeito. Os 61 cartões espaciais já vêm dentro do app, então abrem mesmo sem internet. Todo o resto é baixado online.",
                "A maior parte das informações que mudam vem de um pequeno arquivo de dados que o desenvolvedor publica uma vez por dia. Ele contém os quadros da Terra, a lista de asteroides e um link para a foto astronômica do dia. O app baixa o arquivo ao abrir e guarda uma cópia. Se o download falhar, mostra a última cópia salva, então offline os números podem ser mais antigos do que parecem. A imagem de satélite da Turquia e o mapa-múndi vêm direto do serviço público GIBS/Worldview da NASA. A posição da ISS vem de outro serviço público, o wheretheiss.at.",
                "Uma observação importante: o Uzay Gunlugu é um app independente. Não é afiliado à NASA nem tem o aval dela. Ele usa apenas imagens e dados de acesso público e cita a fonte em cada tela."]},
            {"h": "O cartão do dia e o álbum", "p": [
                "A tela Hoje abre com o cartão do dia: uma fotografia espacial, sua categoria (por exemplo uma nebulosa, um planeta ou a Terra vista da órbita), uma nota curta em turco, o crédito da imagem e um link Abrir no arquivo que leva à página original. As notas foram escritas à mão para o conjunto de 61 cartões. Servem como uma legenda rápida e simpática, não como uma aula completa.",
                "O cartão não é sorteado no seu celular. Os 61 cartões ficam numa ordem embaralhada fixa, e o número de dias desde uma data fixa define qual é o de hoje. Assim, todo mundo vê o mesmo cartão no mesmo dia e, depois de 61 dias, o ciclo recomeça. Toque na imagem para abri-la em tela cheia, ampliar, compartilhar ou usar como papel de parede."]},
            {"h": "Sequência e álbum: como a contagem funciona", "ul": [
                "Na primeira vez que você abre o app em um dia, o cartão daquele dia entra sozinho no seu álbum. Uma caixa na tela Hoje avisa que um cartão novo foi adicionado. Abrir o app de novo no mesmo dia não muda nada.",
                "A sequência conta dias consecutivos. Se você abriu o app ontem e abre hoje, ela sobe um. Se pular um dia inteiro, recomeça do um. A chama com o número ao lado do título mostra a sequência atual e some quando ela é interrompida.",
                "O álbum mostra quantos dos 61 cartões você reuniu, com os reunidos na frente. O álbum e a sequência ficam guardados no seu aparelho, não em uma conta."]},
            {"h": "Turquia vista do espaço", "p": [
                "Esta tela mostra uma imagem de satélite em cor real da Turquia e dos mares ao redor. Ela vem do instrumento VIIRS do satélite NOAA-21 e é servida pelo GIBS/Worldview da NASA. Cor real significa que a imagem lembra uma fotografia: terra, mar e nuvens.",
                "A imagem padrão é a de ontem, montada com as passagens do satélite daquele dia. Não há imagem de hoje porque ela ainda não foi montada. Use os botões de dia anterior e seguinte para voltar a dias passados; a data aparece entre eles. O maior limite são as nuvens: num dia nublado você só vê nuvens, e parte do solo pode ficar escondida."]},
            {"h": "Luzes noturnas: um mapa fixo, não uma vista ao vivo", "p": [
                "O botão de luzes noturnas mostra como as cidades brilham depois de escurecer. É fácil interpretar errado, então lembre: é um mapa fixo montado com imagens de satélite reunidas ao longo de todo o ano de 2016, e o app o identifica como média anual. Não é a vista da noite passada e não tem botões de data.",
                "Use-o para comparar regiões: grandes cidades, litorais e rodovias aparecem como áreas brilhantes, e regiões pouco povoadas ficam escuras. Não o use para avaliar a situação de hoje em lugar nenhum."]},
            {"h": "Terra agora: o planeta girando", "p": [
                "A tela Terra reproduz em loop fotografias do planeta inteiro tiradas por uma câmera da nave DSCOVR (o instrumento EPIC), a cerca de um milhão de quilômetros. O app pega os quadros do dia mais recente disponível e os passa um após o outro, para você ver o planeta girar. Reproduzir e Pausar controlam o loop.",
                "Abaixo da imagem aparecem o horário do quadro atual em UTC (não o seu horário local), a data dos quadros e a latitude e a longitude do centro da imagem. Os quadros não são ao vivo: o conjunto mais novo costuma ser de um ou dois dias antes, e a data diz exatamente de qual. O que você vê é o lado da Terra iluminado pelo Sol, por isso a imagem muda ao longo do dia. Se os quadros não carregarem, a tela pede que você verifique a conexão."]},
            {"h": "ISS agora: como ler os números", "p": [
                "A tela da ISS põe um marcador em um mapa-múndi. Enquanto a tela está aberta, a posição é pedida de novo a cada cinco segundos, então dá para ver o marcador avançando. O mapa de fundo é uma imagem fixa da superfície da Terra, não uma vista ao vivo com nuvens ou sombra de dia e noite.",
                "Abaixo do mapa há quatro linhas. Latitude e longitude indicam o ponto do solo bem embaixo da estação. Altura é a altitude acima da superfície em quilômetros; a estação orbita a cerca de 400 km. A velocidade aparece em quilômetros por hora. A última linha diz se, no solo abaixo da estação, é dia ou noite. Um botão abre no navegador, no YouTube, uma transmissão ao vivo da estação, se ela estiver disponível naquele momento.",
                "Lembre o que isto não é: o marcador é uma posição num mapa, não uma previsão de quando a estação passará sobre a sua casa, e o app não avisa quando olhar para o céu."]},
            {"h": "Asteroides desta semana: uma lista para ler, não um alarme", "p": [
                "A tela Hoje termina com uma lista curta de asteroides próximos da Terra. Ela vem do CNEOS da NASA/JPL e cobre as aproximações das próximas duas semanas, mais ou menos, até um limite de distância fixo. O app mostra os cinco primeiros por data. Cada linha traz a data e a hora (UTC), a designação do asteroide, a que distância ele passa, um tamanho estimado e a velocidade em quilômetros por segundo.",
                "A distância é escrita em distâncias da Lua, porque quilômetros são difíceis de imaginar. A Lua fica a cerca de 384.000 km, então uma passagem a 8,0 vezes a distância lunar equivale a uns três milhões de quilômetros. Se um asteroide passar mais perto que a Lua, a linha informa isso como porcentagem da distância lunar. O tamanho é apenas uma estimativa calculada a partir do brilho do objeto, e o app o compara com um carro, um ônibus, um prédio de apartamentos ou um campo de futebol para dar uma noção.",
                "São sobrevoos rotineiros e previstos. A lista é informativa e não é um alerta de perigo."]},
            {"h": "Lista rápida de limites", "ul": [
                "A interface e as notas dos cartões estão só em turco por enquanto.",
                "Imagem de satélite da Turquia: no máximo a de ontem, e as nuvens podem esconder o solo.",
                "Luzes noturnas: um composto anual fixo de 2016, nunca diário.",
                "Terra girando: quadros recentes, normalmente não de hoje; o horário mostrado é UTC.",
                "ISS: a posição atualiza a cada cinco segundos, mas o mapa de fundo é uma imagem fixa.",
                "Asteroides: tamanhos estimados e uma janela curta; não é uma ferramenta de segurança."]},
        ],
        "faq": [
            ["O Uzay Gunlugu é da NASA?", "Não. É um app independente, sem afiliação nem aval da NASA. Usa imagens e dados de acesso público e cita a fonte de cada um."],
            ["A imagem da Turquia é ao vivo?", "Não. É uma imagem em cor real de ontem, no máximo. Dá para voltar dia a dia. A vista de luzes noturnas é um mapa anual fixo de 2016."],
            ["Com que frequência a posição da ISS é atualizada?", "Mais ou menos a cada cinco segundos enquanto a tela da ISS está aberta. Se a conexão cair, a última posição fica na tela até chegar uma nova."],
            ["Os asteroides são perigosos?", "A lista é informativa. Ela mostra aproximações previstas com a distância em distâncias da Lua e não é um alerta de perigo."],
            ["Como mantenho minha sequência?", "Abra o app pelo menos uma vez a cada dia do calendário. Pular um dia inteiro reinicia a sequência em um, e abrir várias vezes no mesmo dia não soma a mais."],
        ],
    },
}
