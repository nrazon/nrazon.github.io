# Blog: deprem buyuklugu ile siddeti farki
POST = {"tags": ["earthquake"],'id': 'earthquake-magnitude-vs-intensity',
 'app': 'sondepremler',
 'date': '2026-11-10',
 'en': {'slug': 'earthquake-magnitude-vs-intensity',
        'title': 'Earthquake Magnitude vs Intensity: What Is the Difference?',
        'desc': 'Magnitude measures the energy released by an earthquake, intensity measures the shaking at a place. Learn how Richter, Mw '
                'and Mercalli scales differ.',
        'intro': 'After every earthquake you hear two words: magnitude and intensity. People often use them as if they meant the same '
                 'thing, but they answer different questions. Magnitude asks how big the earthquake was. Intensity asks how strongly it '
                 'was felt in a particular place.',
        'sections': [{'h': 'Magnitude: one number for the earthquake',
                      'p': ['Magnitude describes the size of the earthquake at its source. It is calculated from instrument records, '
                            'called seismograms, and it does not depend on who is standing where. A single earthquake has one true '
                            'magnitude, whether you sit next to the fault or on the other side of the country.',
                            'In practice, each agency computes its own estimate from the stations it has, so you may see slightly '
                            'different values for the same event. That is normal and is explained in a separate article about where '
                            'earthquake data comes from. The important point here is that magnitude is a property of the earthquake, not '
                            'of the place that felt it.']},
                     {'h': 'Richter, ML and moment magnitude',
                      'p': ['The first widely used scale was proposed by Charles Richter in 1935 for earthquakes in southern California. '
                            'It is based on the largest amplitude recorded by a particular type of seismograph, corrected for distance. '
                            "Today it is usually called the local magnitude and written ML. People still say 'Richter scale' in everyday "
                            'speech, even when the number was calculated another way.',
                            'Local magnitude works well for small and moderate earthquakes at short distances, but for very large '
                            'earthquakes it stops growing as fast as the real size of the event. Seismologists call this saturation. For '
                            'that reason the moment magnitude, written Mw, became the standard for larger earthquakes. Mw is calculated '
                            'from the seismic moment, which depends on the area of the fault that slipped, how far it slipped and the '
                            'stiffness of the rock. Because it does not saturate, it describes great earthquakes much more reliably.',
                            'Other magnitude types exist too, for example a duration magnitude (MD) that uses how long the shaking lasts '
                            'on a record, and magnitudes based on body waves or surface waves. All of them are designed to land close to '
                            'each other for typical events, but they can differ by a few tenths.']},
                     {'h': 'The scale is logarithmic',
                      'p': ['Magnitude scales are logarithmic, so each whole step is a multiplication, not an addition. One unit of '
                            'magnitude means the ground motion recorded on a seismogram is about 10 times larger. In terms of released '
                            'energy, one unit is about 32 times more, because energy grows faster than amplitude.',
                            'A magnitude 6.0 earthquake therefore releases about 32 times the energy of a magnitude 5.0, and roughly 1000 '
                            'times the energy of a magnitude 4.0. Two units mean about 100 times the amplitude and about 1000 times the '
                            'energy. This is why a difference of 0.5 or 1.0 in a news report is a very big difference, and why many small '
                            'earthquakes cannot add up to release the energy of one large one.']},
                     {'h': 'Intensity: what people and buildings experience',
                      'p': ['Intensity describes the effects of shaking at a specific location: whether people feel it, whether objects '
                            'fall, whether buildings are damaged. It is not measured by one instrument but assigned by looking at effects, '
                            'using scales such as the Modified Mercalli scale or the MSK and European Macroseismic scales. These use Roman '
                            'numerals, usually from I (not felt) to XII (total destruction).',
                            'Because intensity belongs to a place, one earthquake produces many different intensity values: high near the '
                            'epicenter and lower farther away. Maps that show these values for one event are made from reports and '
                            'observations and are different from a map of epicenters.']},
                     {'h': 'Why the same earthquake feels different',
                      'ul': ['Distance: shaking weakens as seismic waves travel away from the source.',
                             'Depth: a shallow earthquake usually shakes the surface harder than a deep one of the same magnitude.',
                             'Ground: soft soil and sediment can amplify shaking, while hard rock tends to shake less.',
                             'Buildings: the quality of construction and the building height affect how much damage the same shaking '
                             'causes.',
                             'Duration and direction: how long the shaking lasts and how the fault ruptures also change what people '
                             'feel.']},
                     {'h': 'A worked example',
                      'p': ['Compare a magnitude 5.0 earthquake with a magnitude 7.0 one. The difference is two units, so the recorded '
                            'ground motion of the larger one is about 100 times bigger and the energy released is about 1000 times '
                            'greater. The larger earthquake also ruptures a much larger part of the fault, which is why great earthquakes '
                            'shake wide regions for a long time, while a magnitude 3 may be felt only by a few people close to the '
                            'epicenter.',
                            'This also shows why saying that a magnitude 8 is twice a magnitude 4 is wrong. The numbers are exponents of a '
                            'scale, not quantities you can divide.']},
                     {'h': 'Common misunderstandings',
                      'ul': ['The scale has no printed top, but real earthquakes are limited by the size of the faults that exist, so '
                             'there is a practical maximum.',
                             'Very small earthquakes can have magnitudes near zero or even below zero; they are recorded by instruments '
                             'but felt by nobody.',
                             'A high magnitude does not automatically mean heavy damage in a given city, and a moderate magnitude can '
                             'still be damaging if it is shallow and close to buildings that are weak.',
                             'Intensity values are not a second opinion about magnitude; they are measuring something else.']},
                     {'h': 'Reading an earthquake list',
                      'p': ['When you look at a list of recent earthquakes, the number you see is a magnitude, and the list usually shows '
                            'depth too. A magnitude 3.5 at 10 km depth under your town might feel like a short jolt, while a magnitude 5.5 '
                            'far offshore might be barely noticed on land. Magnitude tells you how large the event was; depth, distance '
                            'and local conditions tell you how likely you were to feel it.',
                            'A list in an app such as Son Depremler shows magnitude, depth, time and location for each earthquake, so you '
                            'can compare them side by side. It is a source of information, not a warning system. For official information '
                            'and safety advice after a strong earthquake, follow AFAD.']}],
        'faq': [['Is magnitude the same as Richter scale?',
                 'Not exactly. The Richter scale is the original local magnitude (ML). Many agencies now report moment magnitude (Mw) for '
                 'larger earthquakes, but people still say Richter out of habit.'],
                ['How much more energy does one extra magnitude unit mean?',
                 'About 32 times more energy and about 10 times larger recorded ground motion.'],
                ['Can one earthquake have several intensities?',
                 'Yes. Intensity is assigned per place, so it is high near the source and lower farther away, and it also depends on local '
                 'ground and buildings.'],
                ['Why does a shallow earthquake feel stronger?',
                 'The source is closer to the surface, so the waves travel a shorter way and arrive with more strength.']]},
 'tr': {'slug': 'deprem-buyuklugu-ve-siddeti-arasindaki-fark',
        'title': 'Deprem Büyüklüğü ile Şiddeti Arasındaki Fark Nedir?',
        'desc': 'Büyüklük depremin saldığı enerjiyi, şiddet ise bir yerde hissedilen sarsıntıyı anlatır. Richter, Mw ve Mercalli '
                'ölçeklerinin farkını öğrenin.',
        'intro': 'Her depremden sonra iki kelime duyarız: büyüklük ve şiddet. Çoğu zaman aynı şeymiş gibi kullanılırlar, oysa farklı '
                 'soruların cevabıdırlar. Büyüklük, depremin ne kadar büyük olduğunu söyler. Şiddet ise depremin belli bir yerde ne kadar '
                 'güçlü hissedildiğini anlatır.',
        'sections': [{'h': 'Büyüklük: depremin tek bir sayısı',
                      'p': ['Büyüklük, depremin kaynağındaki boyutunu tarif eder. Sismograf adı verilen cihazların kayıtlarından '
                            'hesaplanır ve kimin nerede durduğuna bağlı değildir. Bir depremin gerçekte tek bir büyüklüğü vardır; ister '
                            'fayın hemen yanında olun, ister ülkenin öbür ucunda.',
                            'Uygulamada her kurum elindeki istasyonlara göre kendi tahminini hesaplar, bu yüzden aynı deprem için '
                            'birbirinden biraz farklı değerler görebilirsiniz. Bu normaldir ve deprem verilerinin nereden geldiğini '
                            'anlatan ayrı bir yazıda ele alınıyor. Burada önemli olan, büyüklüğün depremin bir özelliği olduğu, hissedilen '
                            'yerin bir özelliği olmadığıdır.']},
                     {'h': 'Richter, ML ve moment büyüklüğü',
                      'p': ["Yaygın kullanılan ilk ölçeği Charles Richter 1935'te Güney Kaliforniya depremleri için önerdi. Belirli bir "
                            'tür sismografta kaydedilen en büyük genliğe dayanır ve uzaklık için düzeltilir. Bugün genellikle yerel '
                            "büyüklük denir ve ML yazılır. Sayı başka yolla hesaplanmış olsa bile günlük dilde hâlâ 'Richter ölçeği' "
                            'denir.',
                            'Yerel büyüklük küçük ve orta depremlerde, kısa mesafelerde iyi çalışır; ancak çok büyük depremlerde olayın '
                            'gerçek büyümesi kadar hızlı artmaz. Sismologlar buna doygunluk der. Bu yüzden büyük depremler için moment '
                            'büyüklüğü, yani Mw, standart oldu. Mw, sismik momentten hesaplanır; sismik moment kayan fay alanına, kaymanın '
                            'miktarına ve kayacın sertliğine bağlıdır. Doygunluğa uğramadığı için büyük depremleri çok daha güvenilir '
                            'tarif eder.',
                            'Başka büyüklük türleri de vardır; örneğin kayıtta sarsıntının ne kadar sürdüğünü kullanan süre büyüklüğü (MD) '
                            'ile cisim ya da yüzey dalgalarına dayanan büyüklükler. Hepsi tipik depremlerde birbirine yakın değerler '
                            'verecek şekilde tasarlanmıştır, ama onda birler düzeyinde ayrışabilirler.']},
                     {'h': 'Ölçek logaritmiktir',
                      'p': ['Büyüklük ölçekleri logaritmiktir; yani her tam basamak bir toplama değil, çarpmadır. Büyüklükte bir birim '
                            'artış, sismogramda kaydedilen yer hareketinin yaklaşık 10 kat büyük olması demektir. Açığa çıkan enerji '
                            'bakımından ise bir birim yaklaşık 32 kat fazladır, çünkü enerji genlikten daha hızlı büyür.',
                            'Dolayısıyla 6,0 büyüklüğündeki bir deprem, 5,0 büyüklüğündekinden yaklaşık 32 kat, 4,0 büyüklüğündekinden ise '
                            'kabaca 1000 kat fazla enerji salar. İki birim fark yaklaşık 100 kat genlik ve yaklaşık 1000 kat enerji '
                            "demektir. Haberlerdeki 0,5 ya da 1,0'lık farkın çok büyük bir fark olması ve çok sayıda küçük depremin tek "
                            'bir büyük depremin enerjisini toplayamaması bu yüzdendir.']},
                     {'h': 'Şiddet: insanların ve yapıların yaşadığı',
                      'p': ['Şiddet, belirli bir yerdeki sarsıntının etkilerini anlatır: insanlar hissediyor mu, eşyalar düşüyor mu, '
                            'yapılar hasar görüyor mu. Tek bir cihazla ölçülmez; etkilere bakılarak Değiştirilmiş Mercalli ölçeği ya da '
                            'MSK ve Avrupa Makrosismik Ölçeği gibi ölçeklerle atanır. Bunlar Romen rakamları kullanır, genellikle I '
                            '(hissedilmez) ile XII (tam yıkım) arasındadır.',
                            'Şiddet bir yere ait olduğu için tek bir deprem birçok farklı şiddet değeri üretir: merkez üssü yakınında '
                            'yüksek, uzaklaştıkça düşük. Bir olay için bu değerleri gösteren haritalar bildirimlerden ve gözlemlerden '
                            'hazırlanır ve merkez üssü haritasından farklıdır.']},
                     {'h': 'Aynı deprem neden farklı hissedilir?',
                      'ul': ['Uzaklık: sismik dalgalar kaynaktan uzaklaştıkça sarsıntı zayıflar.',
                             'Derinlik: aynı büyüklükte, sığ bir deprem derin olandan genellikle yüzeyi daha sert sarsar.',
                             'Zemin: yumuşak zemin ve çökeller sarsıntıyı büyütebilir, sert kaya ise genellikle daha az sallanır.',
                             'Yapılar: yapı kalitesi ve bina yüksekliği, aynı sarsıntının ne kadar hasar vereceğini etkiler.',
                             'Süre ve yön: sarsıntının ne kadar sürdüğü ve fayın nasıl koptuğu da hissedileni değiştirir.']},
                     {'h': 'Çözümlü bir örnek',
                      'p': ['5,0 büyüklüğünde bir depremle 7,0 büyüklüğündeki bir depremi karşılaştıralım. Fark iki birimdir; dolayısıyla '
                            'büyük olanın kaydedilen yer hareketi yaklaşık 100 kat büyük, açığa çıkan enerji ise yaklaşık 1000 kat '
                            'fazladır. Büyük deprem fayın çok daha büyük bir bölümünü de kırar; bu yüzden büyük depremler geniş bölgeleri '
                            'uzun süre sarsarken 3 büyüklüğünde bir deprem yalnızca merkez üssüne yakın birkaç kişi tarafından '
                            'hissedilebilir.',
                            'Bu, 8 büyüklüğündeki bir depremin 4 büyüklüğündekinin iki katı olduğunu söylemenin neden yanlış olduğunu da '
                            'gösterir. Bu sayılar bir ölçeğin üsleridir, bölebileceğiniz miktarlar değildir.']},
                     {'h': 'Sık yapılan yanlış anlamalar',
                      'ul': ['Ölçeğin yazılı bir tavanı yoktur, ama gerçek depremler var olan fayların boyutuyla sınırlıdır; yani pratikte '
                             'bir üst sınır vardır.',
                             'Çok küçük depremlerin büyüklüğü sıfıra yakın, hatta sıfırın altında olabilir; cihazlarca kaydedilirler ama '
                             'kimse hissetmez.',
                             'Yüksek büyüklük, belirli bir şehirde ağır hasar anlamına gelmez; orta büyüklükte bir deprem de sığsa ve '
                             'zayıf yapılara yakınsa hasar verebilir.',
                             'Şiddet değerleri büyüklük için ikinci bir görüş değildir; başka bir şeyi ölçerler.']},
                     {'h': 'Sık sorulan bir soru: Hangisi daha önemli?',
                      'p': ['İkisi de önemlidir, ama farklı amaçlara hizmet ederler. Bilim insanları depremleri karşılaştırmak, fay '
                            'davranışını anlamak ve istatistik tutmak için büyüklüğü kullanır; çünkü büyüklük her yerde aynı olan tek bir '
                            'sayıdır. Mühendisler ve afet yöneticileri ise bir bölgede yapıların ne kadar zorlandığını anlamak için '
                            'şiddeti ve yer hareketini kullanır.',
                            'Gündelik hayatta bu ayrımı akılda tutmak işinize yarar: haberlerde okuduğunuz sayı büyüklüktür. Sizin '
                            'evinizde ne kadar sallandığı ise uzaklığa, derinliğe, zemine ve binanın yapısına bağlıdır. Bu yüzden iki '
                            'komşu mahallede aynı deprem çok farklı hissedilebilir.']},
                     {'h': 'Kısaca hatırlamak için',
                      'ul': ['Büyüklük: depremin kendisi, tek sayı, logaritmik ölçek (ML, Mw, MD).',
                             'Şiddet: bir yerdeki etki, Romen rakamları, yere göre değişir (Mercalli, MSK, Avrupa ölçeği).',
                             'Bir birim büyüklük artışı yaklaşık 10 kat genlik ve yaklaşık 32 kat enerji demektir.',
                             'Derinlik, uzaklık, zemin ve yapı kalitesi hissedilen şiddeti belirler.']},
                     {'h': 'Deprem listesini okumak',
                      'p': ['Son depremler listesine baktığınızda gördüğünüz sayı bir büyüklüktür ve liste genellikle derinliği de '
                            'gösterir. Şehrinizin 10 km altındaki 3,5 büyüklüğünde bir deprem kısa bir sarsıntı gibi hissedilebilir; açık '
                            'denizdeki uzak bir 5,5 ise karada neredeyse fark edilmeyebilir. Büyüklük olayın ne kadar büyük olduğunu, '
                            'derinlik, uzaklık ve yerel koşullar ise sizin onu hissetme ihtimalinizi anlatır.',
                            'Son Depremler gibi bir uygulama her deprem için büyüklük, derinlik, saat ve konumu gösterir; böylece '
                            'depremleri yan yana karşılaştırabilirsiniz. Bu bir bilgi kaynağıdır, erken uyarı sistemi değildir. Güçlü bir '
                            "depremden sonra resmî bilgi ve güvenlik önerileri için AFAD'ı takip edin."]}],
        'faq': [['Büyüklük ile Richter ölçeği aynı şey mi?',
                 'Tam olarak değil. Richter ölçeği, ilk yerel büyüklüktür (ML). Birçok kurum artık büyük depremler için moment büyüklüğünü '
                 '(Mw) bildiriyor, ama alışkanlıkla hâlâ Richter denir.'],
                ['Büyüklükte bir birim fazla ne kadar enerji demektir?',
                 'Yaklaşık 32 kat daha fazla enerji ve kaydedilen yer hareketinde yaklaşık 10 kat daha büyük genlik.'],
                ['Bir depremin birden fazla şiddeti olur mu?',
                 'Evet. Şiddet yere göre atanır; kaynağa yakın yerde yüksek, uzakta düşüktür ve yerel zemin ile yapılara da bağlıdır.'],
                ['Sığ deprem neden daha güçlü hissedilir?',
                 'Kaynak yüzeye daha yakın olduğu için dalgalar daha kısa yol alır ve daha güçlü ulaşır.']]},
 'es': {'slug': 'magnitud-e-intensidad-de-un-terremoto',
        'title': 'Magnitud e intensidad de un terremoto: cuál es la diferencia',
        'desc': 'La magnitud mide la energía liberada por un sismo; la intensidad, la sacudida en un lugar. Así se diferencian las escalas '
                'de Richter, Mw y Mercalli.',
        'intro': 'Después de cada terremoto se oyen dos palabras: magnitud e intensidad. Con frecuencia se usan como si fueran sinónimos, '
                 'pero responden a preguntas distintas. La magnitud dice qué tan grande fue el sismo. La intensidad dice con qué fuerza se '
                 'sintió en un lugar concreto.',
        'sections': [{'h': 'Magnitud: un solo número para el sismo',
                      'p': ['La magnitud describe el tamaño del terremoto en su origen. Se calcula a partir de los registros de '
                            'instrumentos llamados sismógrafos y no depende de quién esté dónde. Un sismo tiene una única magnitud real, '
                            'tanto si estás junto a la falla como al otro lado del país.',
                            'En la práctica, cada institución calcula su propia estimación con las estaciones de que dispone, por eso es '
                            'posible ver valores algo distintos para el mismo evento. Es normal y se explica en otro artículo sobre el '
                            'origen de los datos sísmicos. Lo importante aquí es que la magnitud es una propiedad del terremoto, no del '
                            'lugar donde se sintió.']},
                     {'h': 'Richter, ML y magnitud de momento',
                      'p': ['La primera escala de uso amplio la propuso Charles Richter en 1935 para los sismos del sur de California. Se '
                            'basa en la mayor amplitud registrada por un tipo concreto de sismógrafo, corregida por la distancia. Hoy '
                            'suele llamarse magnitud local y se escribe ML. En el lenguaje cotidiano todavía se habla de escala de '
                            'Richter, incluso cuando el número se calculó de otra manera.',
                            'La magnitud local funciona bien para sismos pequeños y moderados a corta distancia, pero en los muy grandes '
                            'deja de crecer tan rápido como el tamaño real del evento. Los sismólogos lo llaman saturación. Por eso la '
                            'magnitud de momento, escrita Mw, se convirtió en el estándar para los grandes sismos. Se calcula a partir del '
                            'momento sísmico, que depende del área de la falla que se desplazó, de cuánto se desplazó y de la rigidez de '
                            'la roca. Como no se satura, describe con mucha más fiabilidad los grandes terremotos.',
                            'Existen otros tipos de magnitud, por ejemplo la magnitud de duración (MD), que usa el tiempo que dura la '
                            'sacudida en el registro, y las basadas en ondas de cuerpo o de superficie. Todas están pensadas para dar '
                            'valores cercanos en sismos típicos, aunque pueden diferir en unas décimas.']},
                     {'h': 'La escala es logarítmica',
                      'p': ['Las escalas de magnitud son logarítmicas: cada paso entero es una multiplicación, no una suma. Una unidad de '
                            'magnitud significa que el movimiento del suelo registrado en el sismograma es unas 10 veces mayor. En '
                            'términos de energía liberada, una unidad equivale a unas 32 veces más, porque la energía crece más deprisa '
                            'que la amplitud.',
                            'Así, un sismo de magnitud 6,0 libera unas 32 veces la energía de uno de 5,0 y aproximadamente 1000 veces la '
                            'de uno de 4,0. Dos unidades suponen unas 100 veces la amplitud y unas 1000 veces la energía. Por eso una '
                            'diferencia de 0,5 o de 1,0 en una noticia es enorme, y por eso muchos sismos pequeños no suman la energía de '
                            'uno grande.']},
                     {'h': 'Intensidad: lo que viven las personas y los edificios',
                      'p': ['La intensidad describe los efectos de la sacudida en un lugar determinado: si la gente la siente, si se caen '
                            'objetos, si los edificios sufren daños. No se mide con un único instrumento, sino que se asigna observando '
                            'los efectos, con escalas como la de Mercalli modificada, la MSK o la Escala Macrosísmica Europea. Usan '
                            'números romanos, normalmente de I (no se siente) a XII (destrucción total).',
                            'Como la intensidad pertenece a un lugar, un mismo terremoto produce muchos valores: altos cerca del epicentro '
                            'y menores a medida que te alejas. Los mapas que muestran esos valores para un evento se elaboran a partir de '
                            'reportes y observaciones, y son distintos de un mapa de epicentros.']},
                     {'h': 'Por qué el mismo sismo se siente distinto',
                      'ul': ['Distancia: la sacudida se debilita a medida que las ondas sísmicas se alejan del origen.',
                             'Profundidad: un sismo superficial suele sacudir la superficie con más fuerza que uno profundo de la misma '
                             'magnitud.',
                             'Terreno: el suelo blando y los sedimentos pueden amplificar la sacudida, mientras que la roca dura suele '
                             'moverse menos.',
                             'Edificios: la calidad de la construcción y la altura influyen en el daño que causa la misma sacudida.',
                             'Duración y dirección: cuánto dura el movimiento y cómo se rompe la falla también cambian lo que se siente.']},
                     {'h': 'Un ejemplo con números',
                      'p': ['Compara un sismo de magnitud 5,0 con uno de magnitud 7,0. La diferencia es de dos unidades, así que el '
                            'movimiento del suelo registrado en el mayor es unas 100 veces más grande y la energía liberada, unas 1000 '
                            'veces mayor. El sismo más grande también rompe una parte mucho mayor de la falla, y por eso los grandes '
                            'terremotos sacuden regiones amplias durante mucho tiempo, mientras que uno de magnitud 3 puede sentirlo solo '
                            'un puñado de personas cerca del epicentro.',
                            'Esto muestra además por qué es incorrecto decir que un sismo de magnitud 8 es el doble que uno de magnitud 4. '
                            'Esos números son exponentes de una escala, no cantidades que se puedan dividir.']},
                     {'h': 'Malentendidos frecuentes',
                      'ul': ['La escala no tiene un tope escrito, pero los terremotos reales están limitados por el tamaño de las fallas '
                             'que existen, así que en la práctica hay un máximo.',
                             'Los sismos muy pequeños pueden tener magnitudes cercanas a cero o incluso negativas; los instrumentos los '
                             'registran, pero nadie los siente.',
                             'Una magnitud alta no implica automáticamente grandes daños en una ciudad concreta, y una magnitud moderada '
                             'puede causar daños si es superficial y está cerca de edificios débiles.',
                             'Los valores de intensidad no son una segunda opinión sobre la magnitud: miden otra cosa.']},
                     {'h': 'Cómo leer una lista de terremotos',
                      'p': ['Cuando miras una lista de sismos recientes, el número que ves es una magnitud, y la lista suele mostrar '
                            'también la profundidad. Un sismo de magnitud 3,5 a 10 km bajo tu ciudad puede sentirse como una sacudida '
                            'breve, mientras que uno de 5,5 lejos de la costa casi no se nota en tierra. La magnitud te dice qué tan '
                            'grande fue el evento; la profundidad, la distancia y las condiciones locales te dicen cuántas probabilidades '
                            'había de sentirlo.',
                            'Una lista en una app como Son Depremler muestra magnitud, profundidad, hora y ubicación de cada sismo, así '
                            'que puedes compararlos uno junto a otro. Es una fuente de información, no un sistema de alerta. Para '
                            'información oficial y recomendaciones de seguridad tras un sismo fuerte, sigue a AFAD o a la protección civil '
                            'de tu país.']}],
        'faq': [['¿Magnitud y escala de Richter son lo mismo?',
                 'No exactamente. La escala de Richter es la magnitud local original (ML). Muchas instituciones informan hoy la magnitud '
                 'de momento (Mw) en los sismos grandes, aunque por costumbre se siga diciendo Richter.'],
                ['¿Cuánta energía más supone una unidad más de magnitud?',
                 'Unas 32 veces más energía y un movimiento del suelo registrado unas 10 veces mayor.'],
                ['¿Un mismo sismo puede tener varias intensidades?',
                 'Sí. La intensidad se asigna por lugar, por lo que es alta cerca del origen y menor lejos, y depende además del terreno y '
                 'de los edificios.'],
                ['¿Por qué un sismo superficial se siente más fuerte?',
                 'Porque el foco está más cerca de la superficie: las ondas recorren menos camino y llegan con más fuerza.']]},
 'pt': {'slug': 'magnitude-e-intensidade-de-um-terremoto',
        'title': 'Magnitude e intensidade de um terremoto: qual é a diferença?',
        'desc': 'A magnitude mede a energia liberada por um terremoto; a intensidade, o tremor em um lugar. Entenda as escalas de Richter, '
                'Mw e Mercalli.',
        'intro': 'Depois de cada terremoto surgem duas palavras: magnitude e intensidade. Muitas vezes são usadas como se fossem a mesma '
                 'coisa, mas respondem a perguntas diferentes. A magnitude diz quão grande foi o terremoto. A intensidade diz com que '
                 'força ele foi sentido em um lugar específico.',
        'sections': [{'h': 'Magnitude: um único número para o terremoto',
                      'p': ['A magnitude descreve o tamanho do terremoto na sua origem. Ela é calculada a partir dos registros de '
                            'instrumentos chamados sismógrafos e não depende de quem está onde. Um terremoto tem uma única magnitude real, '
                            'esteja você ao lado da falha ou do outro lado do país.',
                            'Na prática, cada instituição calcula a própria estimativa com as estações de que dispõe, por isso é possível '
                            'ver valores um pouco diferentes para o mesmo evento. Isso é normal e é explicado em outro artigo sobre a '
                            'origem dos dados sísmicos. O importante aqui é que a magnitude é uma característica do terremoto, não do '
                            'lugar que o sentiu.']},
                     {'h': 'Richter, ML e magnitude de momento',
                      'p': ['A primeira escala amplamente usada foi proposta por Charles Richter em 1935 para os terremotos do sul da '
                            'Califórnia. Ela se baseia na maior amplitude registrada por um tipo específico de sismógrafo, corrigida pela '
                            'distância. Hoje costuma ser chamada de magnitude local e escrita ML. No dia a dia ainda se fala em escala '
                            'Richter, mesmo quando o número foi calculado de outra forma.',
                            'A magnitude local funciona bem para terremotos pequenos e moderados a curta distância, mas nos muito grandes '
                            'ela deixa de crescer tão rápido quanto o tamanho real do evento. Os sismólogos chamam isso de saturação. Por '
                            'isso a magnitude de momento, escrita Mw, tornou-se o padrão para os grandes terremotos. Ela é calculada a '
                            'partir do momento sísmico, que depende da área da falha que deslizou, de quanto deslizou e da rigidez da '
                            'rocha. Como não satura, descreve com muito mais confiança os grandes terremotos.',
                            'Existem ainda outros tipos de magnitude, como a magnitude de duração (MD), que usa o tempo de duração do '
                            'tremor no registro, e as baseadas em ondas de corpo ou de superfície. Todas são concebidas para dar valores '
                            'próximos em eventos típicos, mas podem diferir em algumas décimas.']},
                     {'h': 'A escala é logarítmica',
                      'p': ['As escalas de magnitude são logarítmicas: cada degrau inteiro é uma multiplicação, não uma soma. Uma unidade '
                            'de magnitude significa que o movimento do solo registrado no sismograma é cerca de 10 vezes maior. Em energia '
                            'liberada, uma unidade equivale a cerca de 32 vezes mais, porque a energia cresce mais depressa do que a '
                            'amplitude.',
                            'Assim, um terremoto de magnitude 6,0 libera cerca de 32 vezes a energia de um de 5,0 e aproximadamente 1000 '
                            'vezes a de um de 4,0. Duas unidades significam cerca de 100 vezes a amplitude e cerca de 1000 vezes a '
                            'energia. É por isso que uma diferença de 0,5 ou de 1,0 numa notícia é enorme, e por isso muitos terremotos '
                            'pequenos não somam a energia de um grande.']},
                     {'h': 'Intensidade: o que pessoas e edifícios vivem',
                      'p': ['A intensidade descreve os efeitos do tremor em um local específico: se as pessoas sentem, se objetos caem, se '
                            'os edifícios sofrem danos. Ela não é medida por um único instrumento, mas atribuída observando os efeitos, '
                            'com escalas como a de Mercalli modificada, a MSK ou a Escala Macrossísmica Europeia. Usam algarismos romanos, '
                            'normalmente de I (não sentido) a XII (destruição total).',
                            'Como a intensidade pertence a um lugar, um mesmo terremoto produz muitos valores: altos perto do epicentro e '
                            'menores à medida que você se afasta. Os mapas que mostram esses valores para um evento são feitos a partir de '
                            'relatos e observações e são diferentes de um mapa de epicentros.']},
                     {'h': 'Por que o mesmo terremoto é sentido de formas diferentes',
                      'ul': ['Distância: o tremor enfraquece à medida que as ondas sísmicas se afastam da origem.',
                             'Profundidade: um terremoto raso costuma sacudir a superfície com mais força do que um profundo de mesma '
                             'magnitude.',
                             'Terreno: solo mole e sedimentos podem amplificar o tremor, enquanto rocha dura costuma se mover menos.',
                             'Edifícios: a qualidade da construção e a altura influenciam o dano causado pelo mesmo tremor.',
                             'Duração e direção: quanto tempo o tremor dura e como a falha se rompe também mudam o que se sente.']},
                     {'h': 'Um exemplo com números',
                      'p': ['Compare um terremoto de magnitude 5,0 com um de magnitude 7,0. A diferença é de duas unidades, então o '
                            'movimento do solo registrado no maior é cerca de 100 vezes maior e a energia liberada é cerca de 1000 vezes '
                            'maior. O terremoto maior também rompe uma parte muito maior da falha, e por isso os grandes terremotos '
                            'sacodem regiões amplas por muito tempo, enquanto um de magnitude 3 pode ser sentido só por poucas pessoas '
                            'perto do epicentro.',
                            'Isso mostra ainda por que é errado dizer que um terremoto de magnitude 8 é o dobro de um de magnitude 4. '
                            'Esses números são expoentes de uma escala, não quantidades que se possam dividir.']},
                     {'h': 'Mal-entendidos comuns',
                      'ul': ['A escala não tem um teto escrito, mas os terremotos reais são limitados pelo tamanho das falhas existentes, '
                             'então na prática há um máximo.',
                             'Terremotos muito pequenos podem ter magnitudes próximas de zero ou até negativas; os instrumentos os '
                             'registram, mas ninguém os sente.',
                             'Uma magnitude alta não significa automaticamente grandes danos em uma cidade específica, e uma magnitude '
                             'moderada pode causar danos se for rasa e estiver perto de edifícios frágeis.',
                             'Os valores de intensidade não são uma segunda opinião sobre a magnitude: medem outra coisa.']},
                     {'h': 'Como ler uma lista de terremotos',
                      'p': ['Ao olhar uma lista de terremotos recentes, o número que você vê é uma magnitude, e a lista costuma mostrar '
                            'também a profundidade. Um terremoto de magnitude 3,5 a 10 km sob a sua cidade pode ser sentido como um '
                            'solavanco breve, enquanto um de 5,5 distante da costa quase não é notado em terra. A magnitude diz quão '
                            'grande foi o evento; a profundidade, a distância e as condições locais dizem quão provável era você senti-lo.',
                            'Uma lista em um app como o Son Depremler mostra magnitude, profundidade, horário e local de cada terremoto, '
                            'para que você possa compará-los lado a lado. É uma fonte de informação, não um sistema de alerta. Para '
                            'informações oficiais e orientações de segurança após um terremoto forte, acompanhe a AFAD ou a defesa civil '
                            'do seu país.']}],
        'faq': [['Magnitude e escala Richter são a mesma coisa?',
                 'Não exatamente. A escala Richter é a magnitude local original (ML). Muitas instituições hoje informam a magnitude de '
                 'momento (Mw) nos terremotos grandes, mas por hábito ainda se diz Richter.'],
                ['Quanta energia a mais significa uma unidade de magnitude?',
                 'Cerca de 32 vezes mais energia e um movimento do solo registrado cerca de 10 vezes maior.'],
                ['Um mesmo terremoto pode ter várias intensidades?',
                 'Sim. A intensidade é atribuída por lugar, por isso é alta perto da origem e menor longe, e depende também do terreno e '
                 'dos edifícios.'],
                ['Por que um terremoto raso é sentido com mais força?',
                 'Porque o foco está mais perto da superfície: as ondas percorrem menos caminho e chegam com mais força.']]}}
