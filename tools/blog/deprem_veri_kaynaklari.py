# Blog: son deprem verileri nereden geliyor (uygulamanin gercek kaynaklari: AFAD apiv2 + Kandilli sondepremler.asp)
POST = {"tags": ["earthquake"],'id': 'where-earthquake-data-comes-from',
 'app': 'sondepremler',
 'date': '2026-11-10',
 'en': {'slug': 'where-earthquake-data-comes-from',
        'title': 'Where Does Earthquake Data Come From? AFAD, Kandilli, USGS',
        'desc': 'Why do two agencies report different magnitudes for the same earthquake? How AFAD, Kandilli and others publish, revise '
                'and update recent earthquake lists.',
        'intro': 'Open two earthquake lists right after a quake and you may see two different magnitudes, two slightly different times or '
                 'places. Nothing is broken. Recent earthquake lists come from seismological networks, and each agency runs its own '
                 'stations, its own software and its own review process.',
        'sections': [{'h': 'Seismic networks: the source of every list',
                      'p': ['An earthquake list is not made by an app. It starts at a seismological network: a set of seismometers spread '
                            'across a region, sending their recordings to a processing center. Software and analysts there find the time, '
                            'the location, the depth and the magnitude of each event, and the agency publishes the result.',
                            "Turkey has several such sources. Two public ones are AFAD's Earthquake Department, part of the national "
                            'disaster management authority, and the Kandilli Observatory and Earthquake Research Institute at Boğaziçi '
                            'University. Outside Turkey, global agencies such as the US Geological Survey (USGS) and the '
                            'European-Mediterranean Seismological Centre (EMSC) publish their own solutions, especially for larger '
                            'events.']},
                     {'h': 'What Son Depremler actually uses',
                      'p': ["Son Depremler reads data directly from two public services: AFAD's event service and the Kandilli "
                            "Observatory's last-earthquakes page. You can switch between the two sources with one tap and compare them. "
                            'The app is not affiliated with either institution, and it does not use USGS or EMSC data.',
                            'From AFAD the app requests the last 30 days of events and applies the time and magnitude filters on the '
                            'phone. Kandilli publishes its list of the most recent 500 earthquakes, which covers roughly a week, so a '
                            'longer period is only available from AFAD in the app.']},
                     {'h': 'The first result and later revisions',
                      'p': ['The first solution after an earthquake is usually computed quickly, often automatically, from the stations '
                            'that have already received the waves. Analysts then review the recordings, add more stations, pick the wave '
                            'arrivals more carefully and recompute. Location, depth and magnitude can all change a little in that process.',
                            "You can even see this in Kandilli's list: each line has a solution quality column, which shows a preliminary "
                            'solution (marked as such) or a revised one with a revision number and date. The practical lesson is that a '
                            'number you see a few minutes after an earthquake can still be updated, and a list you open a day later can '
                            'differ from the one you saw first.']},
                     {'h': 'Why magnitudes differ between agencies',
                      'ul': ['Different magnitude types: one agency may report a local magnitude (ML), another a moment magnitude (Mw) or '
                             'a duration magnitude (MD). They are designed to be close but are not identical.',
                             'Different stations: each network uses its own stations and their distance to the earthquake, which affects '
                             'the estimate.',
                             'Different methods and software: calculation details and corrections vary.',
                             'Different timing: one list may show an automatic result and the other a reviewed one.',
                             'Rounding and display: values are reported to one decimal and may be rounded in different ways.'],
                      'p2': ["Kandilli's list contains several magnitude columns. The app shows Kandilli's ML when it exists, and "
                             "otherwise Mw and then MD. AFAD's records also carry a magnitude type, so the number you see is not always "
                             'the same kind of magnitude on both sources.']},
                     {'h': 'How to read the differences',
                      'p': ['A difference of a few tenths between two agencies is common and does not mean either one is wrong. If one '
                            'list says 4.6 and the other says 4.4, both are describing a moderate earthquake. What matters more is the '
                            'order of magnitude, the depth and the location, which usually agree closely.',
                            "Times need attention as well. AFAD's service provides times in UTC, while Kandilli lists local Turkish time, "
                            'and the app converts them for display. If you compare with another source, check which time zone it uses.']},
                     {'h': 'Following one earthquake step by step',
                      'p': ['Imagine a moderate earthquake in the middle of the night. Within a short time, the seismic networks detect it '
                            'and produce a first automatic estimate. If you open a list at that moment you may see a first value, or the '
                            'quake may not appear yet because the service has not published it. Over the following minutes and hours the '
                            'entry may be refreshed with a reviewed location or magnitude, and smaller aftershocks begin to appear as '
                            'separate lines.',
                            'If a list seems behind, the reason is often just timing: the agency has not published yet, or the app is '
                            'showing its last saved copy. Refreshing in the app asks the source again.']},
                     {'h': 'Tips for comparing sources',
                      'ul': ['Look at the time first: if two entries are within a few seconds and a few kilometers of each other, they are '
                             'almost certainly the same earthquake.',
                             'Check which magnitude type each source reports before concluding that they disagree.',
                             'For small earthquakes, expect larger relative differences, because few stations may have recorded them.',
                             'For a strong earthquake, wait for the reviewed values before quoting a number to others.',
                             'Use the official statements of the agency, rather than screenshots, when you need an exact figure.']},
                     {'h': 'What a list can and cannot do',
                      'p': ['A recent earthquake list is a record of what has already happened. The data reaches the agencies after the '
                            'earthquake, usually within minutes, and can be revised afterwards. It cannot predict earthquakes and it is '
                            'not an early warning system.',
                            'Use lists to learn what happened, compare sources and see the pattern of small earthquakes in your region. '
                            'For official statements and safety information after a strong event, follow AFAD.']}],
        'faq': [['Where does Son Depremler get its data?',
                 "From AFAD's public event service and the Kandilli Observatory's public last-earthquakes list. The app is not affiliated "
                 'with either institution.'],
                ['Why do AFAD and Kandilli show different magnitudes?',
                 'They use their own stations and methods, may report different magnitude types (ML, Mw, MD) and may publish at different '
                 'review stages.'],
                ["Can an earthquake's magnitude change after it is published?",
                 'Yes. The first automatic solution can be revised after analysts review the data, so location, depth and magnitude may '
                 'change slightly.'],
                ['Does the app warn me before an earthquake?',
                 'No. It lists earthquakes that have already been recorded and is not an early warning system.']]},
 'tr': {'slug': 'son-deprem-verileri-nereden-geliyor',
        'title': 'Son Deprem Verileri Nereden Geliyor? AFAD, Kandilli, USGS',
        'desc': 'Aynı deprem için neden iki kurum farklı büyüklük verir? AFAD, Kandilli ve diğer kurumların son deprem listelerini nasıl '
                'yayımladığı ve güncellediği.',
        'intro': 'Bir depremden hemen sonra iki farklı listeyi açarsanız iki ayrı büyüklük, biraz farklı saat ya da yer görebilirsiniz. '
                 'Bir şey bozuk değildir. Son deprem listeleri sismoloji ağlarından gelir ve her kurumun kendi istasyonları, kendi '
                 'yazılımı ve kendi inceleme süreci vardır.',
        'sections': [{'h': 'Sismik ağlar: her listenin kaynağı',
                      'p': ['Deprem listesini bir uygulama üretmez. Her şey bir sismoloji ağında başlar: bir bölgeye yayılmış '
                            'sismometrelerin kayıtlarını bir işlem merkezine gönderdiği düzen. Orada yazılımlar ve analistler her olayın '
                            'zamanını, yerini, derinliğini ve büyüklüğünü bulur; kurum da sonucu yayımlar.',
                            "Türkiye'de böyle birkaç kaynak vardır. Kamuya açık iki tanesi, ulusal afet yönetimi kurumunun bünyesindeki "
                            "AFAD Deprem Dairesi ile Boğaziçi Üniversitesi Kandilli Rasathanesi ve Deprem Araştırma Enstitüsü'dür. Türkiye "
                            'dışında, ABD Jeoloji Araştırmaları Kurumu (USGS) ve Avrupa-Akdeniz Sismoloji Merkezi (EMSC) gibi küresel '
                            'kurumlar, özellikle büyük olaylar için kendi çözümlerini yayımlar.']},
                     {'h': 'Son Depremler gerçekte neyi kullanır?',
                      'p': ["Son Depremler verileri doğrudan iki kamuya açık servisten okur: AFAD'ın olay servisi ve Kandilli "
                            "Rasathanesi'nin son depremler sayfası. İki kaynak arasında tek dokunuşla geçip karşılaştırabilirsiniz. "
                            'Uygulama iki kurumla da bağlantılı değildir ve USGS ya da EMSC verisi kullanmaz.',
                            "AFAD'dan uygulama son 30 günün olaylarını ister ve zaman ile büyüklük filtrelerini telefonda uygular. "
                            'Kandilli, son 500 depremin listesini yayımlar; bu kabaca bir haftayı kapsar, bu yüzden uygulamada daha uzun '
                            "bir dönem yalnızca AFAD'dan gelir."]},
                     {'h': 'İlk sonuç ve sonraki revizyonlar',
                      'p': ['Bir depremden sonraki ilk çözüm genellikle hızlıca, çoğu zaman otomatik olarak, dalgaları o ana kadar almış '
                            'istasyonlardan hesaplanır. Sonra analistler kayıtları inceler, daha fazla istasyon ekler, dalga varışlarını '
                            'daha dikkatli seçer ve yeniden hesaplar. Bu süreçte yer, derinlik ve büyüklük biraz değişebilir.',
                            "Bunu Kandilli'nin listesinde bile görebilirsiniz: her satırda bir çözüm niteliği sütunu vardır ve bu sütun ya "
                            'ilksel bir çözümü ya da revizyon numarası ve tarihi olan revize edilmiş bir çözümü gösterir. Pratik ders '
                            'şudur: depremden birkaç dakika sonra gördüğünüz bir sayı hâlâ güncellenebilir ve bir gün sonra açtığınız '
                            'liste ilk gördüğünüzden farklı olabilir.']},
                     {'h': 'Kurumlar arasında büyüklükler neden farklı?',
                      'ul': ['Farklı büyüklük türleri: bir kurum yerel büyüklük (ML), diğeri moment büyüklüğü (Mw) ya da süre büyüklüğü '
                             '(MD) bildirebilir. Birbirine yakın olacak şekilde tasarlanmışlardır ama aynı değildir.',
                             'Farklı istasyonlar: her ağ kendi istasyonlarını ve bunların depreme uzaklığını kullanır; bu da tahmini '
                             'etkiler.',
                             'Farklı yöntem ve yazılım: hesap ayrıntıları ve düzeltmeler değişir.',
                             'Farklı zamanlama: bir liste otomatik sonucu, diğeri incelenmiş sonucu gösteriyor olabilir.',
                             'Yuvarlama ve gösterim: değerler tek ondalıkla bildirilir ve farklı biçimlerde yuvarlanabilir.'],
                      'p2': ["Kandilli'nin listesinde birkaç büyüklük sütunu bulunur. Uygulama, varsa Kandilli'nin ML değerini, yoksa Mw "
                             've sonra MD değerini gösterir. AFAD kayıtları da bir büyüklük türü taşır; yani gördüğünüz sayı iki kaynakta '
                             'her zaman aynı türde bir büyüklük olmayabilir.']},
                     {'h': 'Farkları nasıl okumalı?',
                      'p': ['İki kurum arasında onda birler düzeyinde fark yaygındır ve birinin yanlış olduğu anlamına gelmez. Bir liste '
                            '4,6, diğeri 4,4 diyorsa, ikisi de orta büyüklükte bir depremi anlatıyordur. Daha önemli olan büyüklük '
                            'mertebesi, derinlik ve konumdur; bunlar genellikle birbirine çok yakındır.',
                            "Saatlere de dikkat etmek gerekir. AFAD'ın servisi saatleri UTC olarak verir, Kandilli ise Türkiye yerel "
                            'saatini listeler; uygulama bunları gösterim için dönüştürür. Başka bir kaynakla karşılaştırırsanız hangi saat '
                            'dilimini kullandığına bakın.']},
                     {'h': 'Tek bir depremi adım adım izlemek',
                      'p': ['Gece yarısı olan orta büyüklükte bir depremi düşünün. Kısa sürede sismik ağlar bunu algılar ve ilk otomatik '
                            'tahmini üretir. O anda bir liste açarsanız ilk değeri görebilirsiniz; ya da servis henüz yayımlamadığı için '
                            'deprem listede hiç görünmeyebilir. Sonraki dakika ve saatlerde kayıt, gözden geçirilmiş bir yer ya da '
                            'büyüklükle yenilenebilir ve daha küçük artçılar ayrı satırlar olarak belirmeye başlar.',
                            'Bir liste geride kalmış gibi görünüyorsa sebep çoğu zaman yalnızca zamanlamadır: kurum henüz yayımlamamıştır '
                            'ya da uygulama son kaydettiği kopyayı göstermektedir. Uygulamada yenileme yapmak kaynağa yeniden sorar.']},
                     {'h': 'Kaynakları karşılaştırmak için ipuçları',
                      'ul': ['Önce saate bakın: iki kayıt birkaç saniye ve birkaç kilometre içindeyse, neredeyse kesinlikle aynı '
                             'depremdir.',
                             'Kaynakların uyuşmadığı sonucuna varmadan önce her birinin hangi büyüklük türünü bildirdiğine bakın.',
                             'Küçük depremlerde göreli farkların daha büyük olmasını bekleyin; çünkü onları az sayıda istasyon kaydetmiş '
                             'olabilir.',
                             'Güçlü bir depremde, başkalarına bir sayı aktarmadan önce gözden geçirilmiş değerleri bekleyin.',
                             'Kesin bir rakama ihtiyacınız olduğunda ekran görüntüleri yerine kurumun resmî açıklamalarını kullanın.']},
                     {'h': 'Verinin uygulamaya ulaşma yolu',
                      'p': ['Uygulamanın kullandığı yol kısaca şöyledir: sismometreler kayıtları kurumun merkezine gönderir, kurum sonucu '
                            'bir servis ya da web sayfası olarak yayımlar, uygulama bu yayını okur ve size liste olarak gösterir. Yani '
                            'uygulama kendi başına deprem ölçmez; kurumların yayımladığı sonucu aktarır. Bu yüzden listede ne varsa, '
                            'kaynağın o anda yayımladığıdır.',
                            "Kandilli'nin sayfası sabit genişlikli bir metin olarak yayımlandığı için uygulama onu satır satır okur; AFAD "
                            'ise yapılandırılmış bir veri servisi sunar. Bu iki farklı biçim, iki kaynağın neden her zaman tıpatıp aynı '
                            'görünmediğini de açıklar: biri bir olayı birkaç alanla, diğeri farklı sütunlarla anlatır.']},
                     {'h': 'Kaynağı ve kendi bölgenizi seçmek',
                      'p': ['Hangi kaynağı seçeceğiniz ihtiyacınıza bağlıdır. Daha uzun bir geçmişe, yani son 30 güne bakmak ve il, ilçe '
                            've mahalle bilgisi görmek istiyorsanız AFAD kaydı uygundur. Kandilli listesi ise son bir haftayı kapsar ve '
                            'kendi çözüm niteliği bilgisiyle gelir. İkisini yan yana açıp karşılaştırmak, bir depremin farklı kurumlarca '
                            'nasıl değerlendirildiğini görmenin en kolay yoludur.']},
                     {'h': 'Bir liste ne yapabilir, ne yapamaz?',
                      'p': ['Son deprem listesi, olmuş olanın kaydıdır. Veriler depremden sonra, genellikle dakikalar içinde kurumlara '
                            'ulaşır ve sonradan revize edilebilir. Depremleri tahmin edemez ve erken uyarı sistemi değildir.',
                            'Listeleri ne olduğunu öğrenmek, kaynakları karşılaştırmak ve bölgenizdeki küçük depremlerin düzenini görmek '
                            "için kullanın. Güçlü bir olaydan sonra resmî açıklamalar ve güvenlik bilgisi için AFAD'ı takip edin."]}],
        'faq': [['Son Depremler verileri nereden alıyor?',
                 "AFAD'ın kamuya açık olay servisinden ve Kandilli Rasathanesi'nin kamuya açık son depremler listesinden. Uygulama iki "
                 'kurumla da bağlantılı değildir.'],
                ['AFAD ve Kandilli neden farklı büyüklük gösteriyor?',
                 'Kendi istasyonlarını ve yöntemlerini kullanırlar, farklı büyüklük türleri (ML, Mw, MD) bildirebilirler ve farklı '
                 'inceleme aşamalarında yayın yapabilirler.'],
                ['Bir depremin büyüklüğü yayımlandıktan sonra değişebilir mi?',
                 'Evet. İlk otomatik çözüm, analistler veriyi inceledikten sonra revize edilebilir; yer, derinlik ve büyüklük biraz '
                 'değişebilir.'],
                ['Uygulama beni depremden önce uyarır mı?',
                 'Hayır. Daha önce kaydedilmiş depremleri listeler ve erken uyarı sistemi değildir.']]},
 'es': {'slug': 'de-donde-vienen-los-datos-de-terremotos',
        'title': '¿De dónde vienen los datos de terremotos? AFAD, Kandilli, USGS',
        'desc': '¿Por qué dos instituciones dan magnitudes distintas para el mismo sismo? Cómo publican, revisan y actualizan AFAD, '
                'Kandilli y otros sus listas recientes.',
        'intro': 'Si abres dos listas de terremotos justo después de un sismo, puedes ver dos magnitudes distintas y una hora o un lugar '
                 'ligeramente diferentes. No hay ningún fallo. Las listas de sismos recientes provienen de redes sismológicas, y cada '
                 'institución tiene sus propias estaciones, su propio software y su propio proceso de revisión.',
        'sections': [{'h': 'Redes sísmicas: el origen de cada lista',
                      'p': ['Una lista de terremotos no la crea una aplicación. Todo empieza en una red sismológica: un conjunto de '
                            'sismómetros repartidos por una región que envían sus registros a un centro de procesamiento. Allí, programas '
                            'y analistas determinan la hora, la ubicación, la profundidad y la magnitud de cada evento, y la institución '
                            'publica el resultado.',
                            'Turquía tiene varias fuentes así. Dos públicas son el Departamento de Terremotos de AFAD, dentro de la '
                            'autoridad nacional de gestión de desastres, y el Observatorio Kandilli e Instituto de Investigación de '
                            'Terremotos de la Universidad del Bósforo. Fuera de Turquía, organismos globales como el Servicio Geológico de '
                            'Estados Unidos (USGS) y el Centro Sismológico Euromediterráneo (EMSC) publican sus propias soluciones, sobre '
                            'todo para eventos grandes.']},
                     {'h': 'Qué usa realmente Son Depremler',
                      'p': ['Son Depremler lee los datos directamente de dos servicios públicos: el servicio de eventos de AFAD y la '
                            'página de últimos terremotos del Observatorio Kandilli. Puedes cambiar entre las dos fuentes con un toque y '
                            'compararlas. La app no está afiliada a ninguna de las dos instituciones y no usa datos de USGS ni de EMSC.',
                            'A AFAD la app le pide los eventos de los últimos 30 días y aplica los filtros de tiempo y magnitud en el '
                            'teléfono. Kandilli publica su lista de los 500 terremotos más recientes, que cubre más o menos una semana, '
                            'así que en la app un período más largo solo está disponible desde AFAD.']},
                     {'h': 'El primer resultado y las revisiones posteriores',
                      'p': ['La primera solución tras un terremoto suele calcularse con rapidez, a menudo de forma automática, con las '
                            'estaciones que ya han recibido las ondas. Después los analistas revisan los registros, añaden más estaciones, '
                            'identifican con más cuidado la llegada de las ondas y recalculan. En ese proceso la ubicación, la profundidad '
                            'y la magnitud pueden cambiar un poco.',
                            'Incluso se aprecia en la lista de Kandilli: cada línea tiene una columna de calidad de la solución, que '
                            'indica una solución preliminar o una revisada con número y fecha de revisión. La lección práctica es que una '
                            'cifra que ves unos minutos después del sismo todavía puede actualizarse, y una lista que abras un día más '
                            'tarde puede diferir de la que viste al principio.']},
                     {'h': 'Por qué las magnitudes difieren entre instituciones',
                      'ul': ['Tipos de magnitud distintos: una institución puede informar magnitud local (ML), otra magnitud de momento '
                             '(Mw) o de duración (MD). Están diseñadas para ser cercanas, pero no son idénticas.',
                             'Estaciones distintas: cada red usa sus propias estaciones y su distancia al sismo, lo que afecta a la '
                             'estimación.',
                             'Métodos y software distintos: los detalles del cálculo y las correcciones varían.',
                             'Momento distinto: una lista puede mostrar el resultado automático y otra el revisado.',
                             'Redondeo y presentación: los valores se informan con un decimal y pueden redondearse de formas diferentes.'],
                      'p2': ['La lista de Kandilli contiene varias columnas de magnitud. La app muestra la ML de Kandilli cuando existe y, '
                             'si no, la Mw y después la MD. Los registros de AFAD también llevan un tipo de magnitud, de modo que el '
                             'número que ves no siempre es el mismo tipo de magnitud en ambas fuentes.']},
                     {'h': 'Cómo interpretar las diferencias',
                      'p': ['Una diferencia de unas décimas entre dos instituciones es habitual y no significa que alguna se equivoque. Si '
                            'una lista dice 4,6 y la otra 4,4, las dos describen un sismo moderado. Importa más el orden de magnitud, la '
                            'profundidad y la ubicación, que suelen coincidir bastante.',
                            'También hay que fijarse en las horas. El servicio de AFAD entrega las horas en UTC, mientras que Kandilli '
                            'lista la hora local de Turquía, y la app las convierte para mostrarlas. Si comparas con otra fuente, '
                            'comprueba qué zona horaria usa.']},
                     {'h': 'Seguir un terremoto paso a paso',
                      'p': ['Imagina un sismo moderado en plena noche. En poco tiempo, las redes sísmicas lo detectan y producen una '
                            'primera estimación automática. Si abres una lista en ese momento, puedes ver un primer valor, o puede que el '
                            'sismo todavía no aparezca porque el servicio aún no lo ha publicado. En los minutos y horas siguientes, el '
                            'registro puede actualizarse con una ubicación o magnitud revisadas, y empiezan a aparecer réplicas más '
                            'pequeñas como líneas separadas.',
                            'Si una lista parece ir retrasada, la causa suele ser simplemente el momento: la institución todavía no ha '
                            'publicado, o la app muestra su última copia guardada. Actualizar en la app vuelve a consultar la fuente.']},
                     {'h': 'Consejos para comparar fuentes',
                      'ul': ['Mira primero la hora: si dos registros están a pocos segundos y pocos kilómetros uno del otro, casi seguro '
                             'son el mismo sismo.',
                             'Comprueba qué tipo de magnitud informa cada fuente antes de concluir que no coinciden.',
                             'En los sismos pequeños, espera diferencias relativas mayores, porque pocas estaciones pueden haberlos '
                             'registrado.',
                             'En un sismo fuerte, espera a los valores revisados antes de citar una cifra a otras personas.',
                             'Cuando necesites una cifra exacta, usa los comunicados oficiales de la institución en lugar de capturas de '
                             'pantalla.']},
                     {'h': 'Qué puede y qué no puede hacer una lista',
                      'p': ['Una lista de terremotos recientes es un registro de lo que ya ha ocurrido. Los datos llegan a las '
                            'instituciones después del sismo, normalmente en minutos, y pueden revisarse después. No puede predecir '
                            'terremotos y no es un sistema de alerta temprana.',
                            'Usa las listas para saber qué pasó, comparar fuentes y ver el patrón de los sismos pequeños en tu región. '
                            'Para comunicados oficiales e información de seguridad tras un evento fuerte, sigue a AFAD o a la protección '
                            'civil de tu país.']}],
        'faq': [['¿De dónde obtiene Son Depremler sus datos?',
                 'Del servicio público de eventos de AFAD y de la lista pública de últimos terremotos del Observatorio Kandilli. La app no '
                 'está afiliada a ninguna de las dos instituciones.'],
                ['¿Por qué AFAD y Kandilli muestran magnitudes distintas?',
                 'Usan sus propias estaciones y métodos, pueden informar tipos de magnitud distintos (ML, Mw, MD) y pueden publicar en '
                 'fases de revisión diferentes.'],
                ['¿Puede cambiar la magnitud de un sismo después de publicarse?',
                 'Sí. La primera solución automática puede revisarse cuando los analistas examinan los datos, así que la ubicación, la '
                 'profundidad y la magnitud pueden variar un poco.'],
                ['¿La app me avisa antes de un terremoto?', 'No. Lista sismos ya registrados y no es un sistema de alerta temprana.']]},
 'pt': {'slug': 'de-onde-vem-os-dados-de-terremotos',
        'title': 'De onde vêm os dados de terremotos? AFAD, Kandilli, USGS',
        'desc': 'Por que duas instituições dão magnitudes diferentes para o mesmo terremoto? Como AFAD, Kandilli e outras publicam, '
                'revisam e atualizam suas listas.',
        'intro': 'Se você abrir duas listas de terremotos logo depois de um tremor, poderá ver duas magnitudes diferentes e um horário ou '
                 'local ligeiramente distintos. Não há nada quebrado. As listas de terremotos recentes vêm de redes sismológicas, e cada '
                 'instituição tem as suas estações, o seu software e o seu processo de revisão.',
        'sections': [{'h': 'Redes sísmicas: a origem de cada lista',
                      'p': ['Uma lista de terremotos não é criada por um aplicativo. Tudo começa numa rede sismológica: um conjunto de '
                            'sismômetros espalhados por uma região que enviam seus registros a um centro de processamento. Lá, programas e '
                            'analistas determinam o horário, a localização, a profundidade e a magnitude de cada evento, e a instituição '
                            'publica o resultado.',
                            'A Turquia tem várias fontes assim. Duas públicas são o Departamento de Terremotos da AFAD, ligado à '
                            'autoridade nacional de gestão de desastres, e o Observatório Kandilli e Instituto de Pesquisa de Terremotos '
                            'da Universidade do Bósforo. Fora da Turquia, órgãos globais como o Serviço Geológico dos Estados Unidos '
                            '(USGS) e o Centro Sismológico Euro-Mediterrâneo (EMSC) publicam suas próprias soluções, sobretudo para '
                            'eventos grandes.']},
                     {'h': 'O que o Son Depremler realmente usa',
                      'p': ['O Son Depremler lê os dados diretamente de dois serviços públicos: o serviço de eventos da AFAD e a página de '
                            'últimos terremotos do Observatório Kandilli. Você pode alternar entre as duas fontes com um toque e comparar. '
                            'O app não é afiliado a nenhuma das duas instituições e não usa dados do USGS nem do EMSC.',
                            'Da AFAD o app pede os eventos dos últimos 30 dias e aplica os filtros de tempo e magnitude no próprio '
                            'celular. O Kandilli publica a lista dos 500 terremotos mais recentes, que cobre aproximadamente uma semana; '
                            'por isso, no app, um período mais longo só está disponível pela AFAD.']},
                     {'h': 'O primeiro resultado e as revisões posteriores',
                      'p': ['A primeira solução depois de um terremoto costuma ser calculada rapidamente, muitas vezes de forma '
                            'automática, com as estações que já receberam as ondas. Depois os analistas revisam os registros, acrescentam '
                            'mais estações, marcam com mais cuidado a chegada das ondas e recalculam. Nesse processo a localização, a '
                            'profundidade e a magnitude podem mudar um pouco.',
                            'Isso aparece até na lista do Kandilli: cada linha tem uma coluna de qualidade da solução, que indica uma '
                            'solução preliminar ou uma revisada, com número e data da revisão. A lição prática é que um valor que você vê '
                            'minutos depois do terremoto ainda pode ser atualizado, e uma lista aberta no dia seguinte pode diferir da que '
                            'você viu no início.']},
                     {'h': 'Por que as magnitudes diferem entre instituições',
                      'ul': ['Tipos de magnitude diferentes: uma instituição pode informar magnitude local (ML), outra magnitude de '
                             'momento (Mw) ou de duração (MD). São feitas para ficar próximas, mas não são idênticas.',
                             'Estações diferentes: cada rede usa suas próprias estações e a distância delas ao terremoto, o que afeta a '
                             'estimativa.',
                             'Métodos e software diferentes: detalhes de cálculo e correções variam.',
                             'Momento diferente: uma lista pode mostrar o resultado automático e a outra o revisado.',
                             'Arredondamento e exibição: os valores são informados com uma casa decimal e podem ser arredondados de '
                             'maneiras distintas.'],
                      'p2': ['A lista do Kandilli traz várias colunas de magnitude. O app mostra a ML do Kandilli quando existe e, caso '
                             'contrário, a Mw e depois a MD. Os registros da AFAD também trazem um tipo de magnitude, então o número que '
                             'você vê nem sempre é o mesmo tipo de magnitude nas duas fontes.']},
                     {'h': 'Como interpretar as diferenças',
                      'p': ['Uma diferença de algumas décimas entre duas instituições é comum e não significa que alguma esteja errada. Se '
                            'uma lista diz 4,6 e a outra 4,4, as duas descrevem um terremoto moderado. Importam mais a ordem de grandeza, '
                            'a profundidade e a localização, que costumam coincidir bem.',
                            'Os horários também pedem atenção. O serviço da AFAD fornece os horários em UTC, enquanto o Kandilli lista o '
                            'horário local da Turquia, e o app os converte para exibição. Se comparar com outra fonte, verifique qual fuso '
                            'ela usa.']},
                     {'h': 'Acompanhando um terremoto passo a passo',
                      'p': ['Imagine um terremoto moderado no meio da noite. Em pouco tempo, as redes sísmicas o detectam e produzem uma '
                            'primeira estimativa automática. Se você abrir uma lista nesse momento, poderá ver um primeiro valor, ou o '
                            'terremoto pode ainda nem aparecer porque o serviço ainda não o publicou. Nos minutos e horas seguintes, o '
                            'registro pode ser atualizado com uma localização ou magnitude revisadas, e réplicas menores começam a '
                            'aparecer como linhas separadas.',
                            'Se uma lista parece atrasada, a causa costuma ser apenas o momento: a instituição ainda não publicou, ou o '
                            'app está mostrando a última cópia salva. Atualizar no app consulta a fonte novamente.']},
                     {'h': 'Dicas para comparar fontes',
                      'ul': ['Olhe primeiro o horário: se dois registros estão a poucos segundos e poucos quilômetros um do outro, quase '
                             'certamente são o mesmo terremoto.',
                             'Verifique qual tipo de magnitude cada fonte informa antes de concluir que elas discordam.',
                             'Em terremotos pequenos, espere diferenças relativas maiores, porque poucas estações podem tê-los registrado.',
                             'Em um terremoto forte, espere os valores revisados antes de citar um número a outras pessoas.',
                             'Quando precisar de um número exato, use os comunicados oficiais da instituição em vez de capturas de tela.']},
                     {'h': 'O que uma lista pode e não pode fazer',
                      'p': ['Uma lista de terremotos recentes é um registro do que já aconteceu. Os dados chegam às instituições depois do '
                            'terremoto, normalmente em minutos, e podem ser revisados depois. Ela não prevê terremotos e não é um sistema '
                            'de alerta antecipado.',
                            'Use as listas para saber o que aconteceu, comparar fontes e ver o padrão dos pequenos terremotos na sua '
                            'região. Para comunicados oficiais e informações de segurança depois de um evento forte, acompanhe a AFAD ou a '
                            'defesa civil do seu país.']}],
        'faq': [['De onde o Son Depremler obtém seus dados?',
                 'Do serviço público de eventos da AFAD e da lista pública de últimos terremotos do Observatório Kandilli. O app não é '
                 'afiliado a nenhuma das duas instituições.'],
                ['Por que AFAD e Kandilli mostram magnitudes diferentes?',
                 'Usam suas próprias estações e métodos, podem informar tipos de magnitude distintos (ML, Mw, MD) e podem publicar em '
                 'fases de revisão diferentes.'],
                ['A magnitude de um terremoto pode mudar depois de publicada?',
                 'Sim. A primeira solução automática pode ser revisada quando os analistas examinam os dados, então localização, '
                 'profundidade e magnitude podem variar um pouco.'],
                ['O app me avisa antes de um terremoto?',
                 'Não. Ele lista terremotos já registrados e não é um sistema de alerta antecipado.']]}}
