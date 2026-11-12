# Yazı: herkes için aynı günlük bulmaca (sunucusuz, tohumdan)
POST = {
    "tags": ["algorithms", "devlog"],
    "id": "daily-puzzle-same-for-everyone", "app": None, "date": "2026-11-10",
    "en": {
        "slug": "how-daily-puzzles-work-without-a-server",
        "title": "How a Daily Puzzle Can Be the Same for Everyone, No Server",
        "desc": "How a game can give every player the same daily puzzle without a server: date seeds, deterministic randomness, time zones and what cheating looks like.",
        "intro": "Many puzzle games offer a daily challenge that is identical for every player, so you can compare scores with friends. It sounds like it needs a server that hands out the puzzle. It does not. Here is how we do it in our own games, and where the limits are.",
        "sections": [
            {"h": "The idea: the date is the puzzle", "p": [
                "A computer cannot produce truly random numbers on its own. A random number generator is a recipe: you give it a starting number, called a seed, and it produces a long sequence that looks random. The important part is that the same seed always produces exactly the same sequence.",
                "That is the whole trick. If every phone turns today's date into a number and uses that number as the seed, every phone builds the same shuffle, the same pieces or the same layout. Nobody has to send anything. The date works as the shared secret that everyone already has.",
                "In practice the games do not use the raw date as a recipe on its own. They mix it with a few more numbers, such as a puzzle type or a board size, so that different puzzles on the same day do not become copies of each other."]},
            {"h": "What our games actually do", "p": [
                "Cubbles turns the local date into a single number in the form year, month, day, for example 20261110, and uses it as the seed for the pieces. Each set of three pieces is drawn from a generator that is started from that day number, the number of the set, and an attempt counter. So the first set of the day is always the same, and so is the second, and so on.",
                "Cardles uses the day number as the seed for its deals. The shuffling code in the game is its own small, portable random generator, written so that the same seed gives the same deal on every device and every Android version. The type of game also rotates with the calendar, so the daily challenge cycles through four different solitaire games.",
                "Logiclings builds a pack of three puzzles each day. Its seed combines the day count with the puzzle type and size, and the type rotates through the five kinds of puzzle so each one comes around regularly. Pentolings picks its daily fitting puzzle from a fixed pool of medium levels using the day count, and its daily falling-blocks round uses a seed derived from the day."]},
            {"h": "Why deterministic randomness is enough", "p": [
                "The word deterministic means that the result depends only on the inputs. A shuffle that starts from the same seed and goes through the same steps cannot come out differently. As long as the code that builds the puzzle is identical on every phone, the puzzle is identical too.",
                "This also means that a good daily puzzle is mostly about the builder, not the delivery. In Cardles, for example, a deal is not accepted blindly. Some deals are impossible to win, so the game checks the daily deal and, if it is stuck or cannot be won, tries the next nearby seed in a fixed order. Every phone follows the same order, so every phone ends up on the same deal.",
                "Cubbles does something similar. A set of three pieces has to be placeable together, so the game tries up to forty seeded attempts and uses the first one that works. We will come back to what that means for fairness in a moment."]},
            {"h": "Time zones: whose midnight?", "p": [
                "Without a server there is no single clock that decides when a new day starts. Our games use the date on your own phone. When it is already tomorrow in Sydney, a player in Los Angeles is still on today's puzzle. Both are correct for their own calendar.",
                "For a single player this is the friendliest choice. The new puzzle appears at your own midnight, and your streak follows your own days. The cost is that a global daily comparison is slightly fuzzy: two people can be playing different days at the same moment.",
                "A streak is calculated the same way. A streak counts consecutive local days, and the game is forgiving: if you have not played yet today, yesterday still keeps the streak alive until the day is over."]},
            {"h": "Same puzzle, mostly", "p": [
                "In the strictest sense a seeded puzzle is identical only if every step depends on the seed and nothing else. Cubbles is an honest example of where that is not quite true. The check that each set of pieces can be placed depends on the state of your board. If an attempt does not fit your board, the game moves to the next attempt, so two players can occasionally see a different set of pieces. Most of the time the first attempt works and everyone sees the same ones, which is why we describe the daily game as the same for nearly everyone rather than for everyone.",
                "There is another small caveat for puzzles that are picked from a list. If an update changes the list of levels, the pick for a given day can change with it. Players on different versions may then see different puzzles for a few days.",
                "These are the kinds of details worth deciding on purpose. Either the puzzle depends on nothing but the seed, or you accept a small difference and say so."]},
            {"h": "Cheating, clocks and what no server costs you", "p": [
                "The price of skipping a server is trust. The game believes the date on your phone. If you change the clock, you can open another day's puzzle. For a game played for fun, with scores that are shared as a friendly challenge, we think that is an acceptable trade. A server that checks every score would need accounts, storage and care for people's data, and it would be one more thing that can break.",
                "Scores that go to a leaderboard are reported by the app. A determined person can send a number the game did not earn, and the app cannot fully prevent that. That is why we treat leaderboards as a game between friends and not as a contest with prizes.",
                "If you ever build one, decide early what the daily puzzle must never depend on. Keep it to the seed, test that two devices produce the same result, and keep the rule that builds the puzzle frozen. If you must change the builder, change it with a new version of the daily and not silently, or yesterday's puzzle will no longer match."]},
        ],
        "faq": [
            ["Does a daily challenge need an internet connection?", "In our games, no. The puzzle is built on your phone from the date, so it works offline."],
            ["Will my friend in another country get the same puzzle today?", "Usually yes, but a new day starts at each player's own midnight, so someone far away may be a day ahead or behind."],
            ["Can someone cheat by changing the phone's clock?", "They can open another day's puzzle. Without a server the game trusts the phone's date, so we treat the daily as a friendly challenge."],
            ["What is a seed?", "A starting number for a random number generator. The same seed always gives the same sequence, which is how different devices build the same puzzle."],
        ],
    },
    "tr": {
        "slug": "sunucusuz-gunluk-bulmaca-nasil-yapilir",
        "title": "Sunucu Olmadan Herkese Aynı Günlük Bulmaca Nasıl Verilir?",
        "desc": "Sunucu kullanmadan her oyuncuya aynı günlük bulmacayı vermenin yolu: tarihten tohum, belirlenimli rastgelelik, saat dilimi ve hile meselesi.",
        "intro": "Birçok bulmaca oyununda herkese aynı günlük meydan okuma gelir; böylece skorlarını arkadaşlarınla karşılaştırabilirsin. Bunun için bulmacayı dağıtan bir sunucu gerekir gibi görünür. Gerekmiyor. Kendi oyunlarımızda bunu nasıl yaptığımızı ve sınırlarını anlatıyoruz.",
        "sections": [
            {"h": "Fikir: bulmaca tarihin kendisi", "p": [
                "Bilgisayar kendi başına gerçekten rastgele sayı üretemez. Rastgele sayı üreteci aslında bir tariftir: ona tohum denen bir başlangıç sayısı verirsin, o da rastgele görünen uzun bir dizi üretir. Önemli nokta şu: aynı tohum her seferinde birebir aynı diziyi verir.",
                "Bütün hile bundan ibaret. Her telefon bugünün tarihini bir sayıya çevirip tohum olarak kullanırsa, her telefon aynı karıştırmayı, aynı parçaları ya da aynı yerleşimi kurar. Kimsenin bir şey göndermesi gerekmez. Tarih, herkesin zaten elinde olan ortak bir sır gibi çalışır.",
                "Pratikte oyunlar ham tarihi tek başına kullanmaz. Aynı gün içindeki farklı bulmacalar birbirinin kopyası olmasın diye tarihi bulmaca türü ya da tahta boyutu gibi birkaç sayıyla karıştırırlar."]},
            {"h": "Oyunlarımız bunu gerçekte nasıl yapıyor", "p": [
                "Cubbles yerel tarihi yıl, ay, gün biçiminde tek bir sayıya çevirir, örneğin 20261110, ve parçaların tohumu olarak kullanır. Her üçlü parça takımı; gün sayısından, takımın sırasından ve bir deneme sayacından başlayan bir üreteçle çekilir. Böylece günün ilk takımı hep aynıdır, ikincisi de, üçüncüsü de.",
                "Cardles dağıtımlar için gün sayısını tohum alır. Oyundaki karıştırma kodu kendi küçük, taşınabilir rastgele üretecidir; aynı tohum her cihazda ve her Android sürümünde aynı dağıtımı versin diye böyle yazılmıştır. Oyun türü de takvimle döner, yani günlük meydan okuma dört farklı solitaire oyununu sırayla gezer.",
                "Logiclings her gün üç bulmacalık bir paket kurar. Tohumu gün sayısını, bulmaca türünü ve boyutunu birleştirir; tür beş bulmaca çeşidi arasında döner, her çeşit düzenli aralıkla sıra gelir. Pentolings günlük döşeme bulmacasını gün sayısıyla orta zorluktaki sabit bir bölüm havuzundan seçer; günlük düşme turunda ise günden türetilmiş bir tohum kullanır.",
                "Bu ayrıntıların hepsinin ortak noktası şu: günün sayısı bir sır değil, herkesin hesaplayabildiği bir girdi. Cardles bir adım daha gider. FreeCell günlüğü için gün sayısını sabit bir çarpanla karıştırıp numaralı klasik dağıtımlardan birine eşler. Klondike ve Spider dağıtımlarında tohum, günün sayısının on katına küçük bir sabit eklenerek bulunur."]},
            {"h": "Belirlenimli rastgelelik neden yeter", "p": [
                "Belirlenimli demek, sonucun yalnızca girdilere bağlı olması demek. Aynı tohumdan başlayıp aynı adımlardan geçen bir karıştırma farklı çıkamaz. Bulmacayı kuran kod her telefonda aynıysa bulmaca da aynıdır.",
                "Bu, iyi bir günlük bulmacanın işin büyük kısmının dağıtımda değil kurucuda olduğunu da gösterir. Cardles'ta örneğin bir dağıtım körü körüne kabul edilmez. Bazı dağıtımları kazanmak imkânsızdır; oyun günlük dağıtımı kontrol eder, tıkanıksa ya da kazanılamıyorsa sabit bir sırayla yakın bir sonraki tohumu dener. Her telefon aynı sırayı izlediği için hepsi aynı dağıtıma varır.",
                "Cubbles de benzer bir şey yapar. Üç parçanın birlikte yerleştirilebilmesi gerekir; bu yüzden oyun tohumlu en fazla kırk deneme yapar ve işe yarayan ilkini kullanır. Bunun adalet açısından ne anlama geldiğine birazdan döneceğiz.",
                "Bir oyunun günlük görevleri de aynı yoldan gelir. Cubbles her günün üç görevini yine gün sayısından üretir, yani görevler de herkese aynıdır ve hiçbir sunucu onları dağıtmaz."]},
            {"h": "Saat dilimleri: kimin gece yarısı?", "p": [
                "Sunucu olmayınca yeni günün ne zaman başladığına karar veren tek bir saat de yok. Oyunlarımız kendi telefonundaki tarihi kullanır. Sidney'de yarın olmuşken Los Angeles'taki oyuncu hâlâ bugünün bulmacasındadır. İkisi de kendi takvimine göre doğrudur.",
                "Tek bir oyuncu için bu en dostane seçim. Yeni bulmaca kendi gece yarında gelir, serin kendi günlerine göre ilerler. Bedeli, küresel bir günlük karşılaştırmanın biraz bulanık olması: iki kişi aynı anda farklı günlerin bulmacasını oynuyor olabilir.",
                "Seri de aynı mantıkla hesaplanır. Seri, art arda yerel günleri sayar ve oyun bağışlayıcıdır: bugün henüz oynamadıysan gün bitene kadar dün seriyi hayatta tutar."]},
            {"h": "Aynı bulmaca, çoğunlukla", "p": [
                "En katı anlamda tohumlu bir bulmaca ancak her adım yalnızca tohuma bağlıysa herkeste aynıdır. Cubbles bunun tam doğru olmadığı dürüst bir örnek. Her parça takımının yerleştirilebilir olduğunu denetleyen kontrol senin tahtanın durumuna bağlı. Bir deneme tahtana uymuyorsa oyun bir sonrakine geçer; yani iki oyuncu ara sıra farklı parça takımları görebilir. Çoğu zaman ilk deneme tutar ve herkes aynı parçaları görür; bu yüzden günlük oyunu herkes için değil, neredeyse herkes için aynı diye tarif ediyoruz.",
                "Listeden seçilen bulmacalar için küçük bir uyarı daha var. Bir güncelleme bölüm listesini değiştirirse, belli bir günün seçimi de değişebilir. Farklı sürümlerdeki oyuncular birkaç gün farklı bulmaca görebilir.",
                "Bunlar bilerek karar verilmesi gereken ayrıntılar. Ya bulmaca tohumdan başka hiçbir şeye bağlı olmaz ya da küçük bir farkı kabul eder ve bunu açıkça söylersin.",
                "Cardles bu konuda daha sıkıdır: dağıtım yalnızca günün sayısına ve sabit bir deneme sırasına bağlıdır, oyuncunun yaptığı hamlelere bağlı değildir. Bu yüzden iki kişi aynı günün Cardles dağıtımını aynı kartlarla görür; fark ancak oyunu farklı oynamalarından doğar."]},
            {"h": "Hile, saat ve sunucusuzluğun bedeli", "p": [
                "Sunucudan vazgeçmenin bedeli güvendir. Oyun telefondaki tarihe inanır. Saati değiştirirsen başka bir günün bulmacasını açabilirsin. Eğlence için oynanan, skorların dostça meydan okuma olarak paylaşıldığı bir oyunda bunu kabul edilebilir bir takas sayıyoruz. Her skoru denetleyen bir sunucu hesap, depolama ve insanların verisine özen gerektirir; üstelik bozulabilecek bir şey daha olur.",
                "Liderlik tablosuna giden skorları uygulama bildirir. Kararlı biri oyunun kazanmadığı bir sayıyı gönderebilir ve uygulama bunu tamamen engelleyemez. Bu yüzden liderlik tablolarını ödüllü bir yarışma değil, arkadaşlar arasında bir oyun olarak görüyoruz.",
                "Sen de bir tane yapacaksan, günlük bulmacanın hiçbir zaman neye bağlı olmaması gerektiğine baştan karar ver. Onu tohuma bağla, iki cihazın aynı sonucu verdiğini test et ve bulmacayı kuran kuralı dondur. Kurucuyu değiştirmek zorundaysan bunu sessizce değil günlüğün yeni bir sürümüyle yap; yoksa dünkü bulmaca artık tutmaz."]},
        ],
        "faq": [
            ["Günlük meydan okuma için internet gerekir mi?", "Oyunlarımızda gerekmez. Bulmaca telefonunda tarihten kurulur, çevrimdışı çalışır."],
            ["Başka ülkedeki arkadaşım bugün aynı bulmacayı alır mı?", "Genellikle evet; ama yeni gün her oyuncunun kendi gece yarısında başlar, uzaktaki biri bir gün önde ya da geride olabilir."],
            ["Telefonun saatini değiştirerek hile yapılabilir mi?", "Başka bir günün bulmacası açılabilir. Sunucu olmadığı için oyun telefonun tarihine güvenir; günlüğü dostça bir meydan okuma olarak görüyoruz."],
            ["Tohum nedir?", "Rastgele sayı üretecinin başlangıç sayısı. Aynı tohum hep aynı diziyi verir; farklı cihazlar bulmacayı böyle aynı kurar."],
        ],
    },
    "es": {
        "slug": "puzle-diario-igual-para-todos-sin-servidor",
        "title": "Cómo dar el mismo puzle diario a todos sin un servidor",
        "desc": "Cómo un juego puede dar el mismo puzle diario a todos sin servidor: semilla a partir de la fecha, aleatoriedad determinista, husos horarios y trampas.",
        "intro": "Muchos juegos de puzles ofrecen un reto diario idéntico para todos los jugadores, de modo que puedes comparar tu puntuación con tus amigos. Parece que haría falta un servidor que reparta el puzle. No hace falta. Aquí explicamos cómo lo hacemos en nuestros propios juegos y dónde están los límites.",
        "sections": [
            {"h": "La idea: la fecha es el puzle", "p": [
                "Un ordenador no puede producir por sí solo números realmente aleatorios. Un generador de números aleatorios es una receta: le das un número inicial, llamado semilla, y produce una secuencia larga que parece aleatoria. Lo importante es que la misma semilla siempre produce exactamente la misma secuencia.",
                "Ahí está todo el truco. Si cada móvil convierte la fecha de hoy en un número y lo usa como semilla, todos los móviles construyen la misma mezcla, las mismas piezas o la misma disposición. Nadie tiene que enviar nada. La fecha funciona como un secreto compartido que todos ya tienen.",
                "En la práctica, los juegos no usan la fecha sola. La mezclan con algunos números más, como el tipo de puzle o el tamaño del tablero, para que los distintos puzles del mismo día no sean copias unos de otros."]},
            {"h": "Qué hacen realmente nuestros juegos", "p": [
                "Cubbles convierte la fecha local en un solo número con el formato año, mes, día, por ejemplo 20261110, y lo usa como semilla de las piezas. Cada grupo de tres piezas sale de un generador que parte del número del día, el número del grupo y un contador de intentos. Así, el primer grupo del día es siempre el mismo, y también el segundo, y así sucesivamente.",
                "Cardles usa el número del día como semilla de sus repartos. El código que baraja es un pequeño generador aleatorio propio y portátil, escrito para que la misma semilla dé el mismo reparto en cualquier dispositivo y versión de Android. El tipo de juego también rota con el calendario, de modo que el reto diario recorre cuatro solitarios distintos.",
                "Logiclings arma cada día un paquete de tres puzles. Su semilla combina el número del día con el tipo y el tamaño del puzle, y el tipo rota entre las cinco clases de puzle para que cada una vuelva con regularidad. Pentolings elige el puzle diario de encaje entre un grupo fijo de niveles medios según el número del día, y su ronda diaria de bloques que caen usa una semilla derivada del día."]},
            {"h": "Por qué basta la aleatoriedad determinista", "p": [
                "Determinista significa que el resultado depende únicamente de los datos de entrada. Una mezcla que parte de la misma semilla y sigue los mismos pasos no puede salir distinta. Mientras el código que construye el puzle sea idéntico en todos los móviles, el puzle también lo será.",
                "Esto también demuestra que un buen puzle diario depende sobre todo del constructor y no de la entrega. En Cardles, por ejemplo, un reparto no se acepta a ciegas. Algunos repartos son imposibles de ganar, así que el juego comprueba el reparto diario y, si está atascado o no se puede ganar, prueba la siguiente semilla cercana en un orden fijo. Todos los móviles siguen el mismo orden, así que todos acaban en el mismo reparto.",
                "Cubbles hace algo parecido. Las tres piezas deben poder colocarse juntas, así que el juego prueba hasta cuarenta intentos con semilla y usa el primero que funciona. Enseguida veremos qué significa eso para la equidad."]},
            {"h": "Husos horarios: ¿la medianoche de quién?", "p": [
                "Sin servidor no existe un reloj único que decida cuándo empieza un día nuevo. Nuestros juegos usan la fecha de tu propio móvil. Cuando en Sídney ya es mañana, un jugador de Los Ángeles sigue en el puzle de hoy. Ambos tienen razón según su calendario.",
                "Para un jugador individual es la opción más amable. El puzle nuevo aparece en tu medianoche y tu racha sigue tus propios días. El coste es que una comparación diaria global resulta algo difusa: dos personas pueden estar jugando días distintos en el mismo instante.",
                "La racha se calcula igual. Cuenta días locales consecutivos y el juego es indulgente: si hoy todavía no has jugado, el día de ayer mantiene viva la racha hasta que termine el día."]},
            {"h": "El mismo puzle, casi siempre", "p": [
                "En sentido estricto, un puzle con semilla es idéntico solo si cada paso depende de la semilla y de nada más. Cubbles es un ejemplo honesto de que no siempre es así. La comprobación de que cada grupo de piezas se puede colocar depende del estado de tu tablero. Si un intento no encaja en tu tablero, el juego pasa al siguiente, así que dos jugadores pueden ver de vez en cuando grupos de piezas distintos. Casi siempre funciona el primer intento y todos ven las mismas piezas, por eso decimos que el juego diario es igual para casi todos y no para todos.",
                "Hay otra pequeña salvedad en los puzles que se eligen de una lista. Si una actualización cambia la lista de niveles, la elección de un día concreto puede cambiar. Jugadores con versiones distintas podrían ver puzles diferentes durante unos días.",
                "Son detalles que conviene decidir a propósito. O bien el puzle no depende más que de la semilla, o bien se acepta una pequeña diferencia y se dice con claridad."]},
            {"h": "Trampas, relojes y lo que cuesta no tener servidor", "p": [
                "El precio de prescindir del servidor es la confianza. El juego se fía de la fecha de tu móvil. Si cambias el reloj, puedes abrir el puzle de otro día. En un juego para divertirse, donde las puntuaciones se comparten como un reto entre amigos, nos parece un trato aceptable. Un servidor que verificara cada puntuación exigiría cuentas, almacenamiento y cuidado con los datos de las personas, y sería una cosa más que puede fallar.",
                "Las puntuaciones que llegan a una clasificación las comunica la aplicación. Una persona decidida puede enviar una cifra que el juego no ha logrado, y la aplicación no puede impedirlo del todo. Por eso vemos las clasificaciones como un juego entre amigos y no como un concurso con premios.",
                "Si alguna vez haces uno, decide pronto de qué no debe depender nunca el puzle diario. Que dependa solo de la semilla, comprueba que dos dispositivos dan el mismo resultado y mantén congelada la regla que construye el puzle. Si tienes que cambiar el constructor, hazlo con una nueva versión del reto diario y no en silencio, o el puzle de ayer dejará de coincidir."]},
        ],
        "faq": [
            ["¿Un reto diario necesita conexión a internet?", "En nuestros juegos, no. El puzle se construye en tu móvil a partir de la fecha, así que funciona sin conexión."],
            ["¿Mi amigo de otro país recibirá hoy el mismo puzle?", "Normalmente sí, pero el día nuevo empieza en la medianoche de cada jugador, así que alguien lejano puede ir un día por delante o por detrás."],
            ["¿Se puede hacer trampa cambiando el reloj del móvil?", "Se puede abrir el puzle de otro día. Sin servidor, el juego se fía de la fecha del móvil, por eso vemos el reto diario como un desafío entre amigos."],
            ["¿Qué es una semilla?", "Es el número inicial de un generador de números aleatorios. La misma semilla da siempre la misma secuencia, y así distintos dispositivos construyen el mismo puzle."],
        ],
    },
    "pt": {
        "slug": "quebra-cabeca-diario-igual-para-todos-sem-servidor",
        "title": "Como dar o mesmo quebra-cabeça diário a todos sem servidor",
        "desc": "Como um jogo pode dar o mesmo quebra-cabeça diário a todos sem servidor: semente a partir da data, aleatoriedade determinística, fusos horários e trapaça.",
        "intro": "Muitos jogos de quebra-cabeça oferecem um desafio diário idêntico para todos os jogadores, para que você compare sua pontuação com a dos amigos. Parece que seria preciso um servidor para distribuir o quebra-cabeça. Não é preciso. Aqui explicamos como fazemos nos nossos jogos e quais são os limites.",
        "sections": [
            {"h": "A ideia: a data é o quebra-cabeça", "p": [
                "Um computador não consegue produzir sozinho números realmente aleatórios. Um gerador de números aleatórios é uma receita: você dá a ele um número inicial, chamado semente, e ele produz uma sequência longa que parece aleatória. O ponto importante é que a mesma semente sempre produz exatamente a mesma sequência.",
                "Esse é todo o truque. Se cada celular transforma a data de hoje em um número e o usa como semente, todos os celulares montam o mesmo embaralhamento, as mesmas peças ou a mesma disposição. Ninguém precisa enviar nada. A data funciona como um segredo compartilhado que todos já têm.",
                "Na prática, os jogos não usam a data sozinha. Eles a misturam com mais alguns números, como o tipo de quebra-cabeça ou o tamanho do tabuleiro, para que quebra-cabeças diferentes no mesmo dia não sejam cópias uns dos outros."]},
            {"h": "O que nossos jogos realmente fazem", "p": [
                "O Cubbles transforma a data local em um único número no formato ano, mês, dia, por exemplo 20261110, e o usa como semente das peças. Cada conjunto de três peças sai de um gerador que parte do número do dia, do número do conjunto e de um contador de tentativas. Assim, o primeiro conjunto do dia é sempre o mesmo, o segundo também, e assim por diante.",
                "O Cardles usa o número do dia como semente das distribuições. O código que embaralha é um pequeno gerador aleatório próprio e portátil, escrito para que a mesma semente dê a mesma distribuição em qualquer aparelho e versão do Android. O tipo de jogo também gira com o calendário, então o desafio diário percorre quatro paciências diferentes.",
                "O Logiclings monta todo dia um pacote de três quebra-cabeças. A semente combina o número do dia com o tipo e o tamanho do quebra-cabeça, e o tipo gira entre as cinco variedades para que cada uma volte com regularidade. O Pentolings escolhe o quebra-cabeça diário de encaixe em um grupo fixo de fases médias pelo número do dia, e a rodada diária de blocos que caem usa uma semente derivada do dia."]},
            {"h": "Por que a aleatoriedade determinística basta", "p": [
                "Determinístico quer dizer que o resultado depende apenas das entradas. Um embaralhamento que parte da mesma semente e segue os mesmos passos não pode sair diferente. Enquanto o código que monta o quebra-cabeça for idêntico em todos os celulares, o quebra-cabeça também será.",
                "Isso mostra também que um bom quebra-cabeça diário depende mais do construtor do que da entrega. No Cardles, por exemplo, uma distribuição não é aceita às cegas. Algumas distribuições são impossíveis de vencer, então o jogo verifica a distribuição do dia e, se ela estiver travada ou não puder ser vencida, tenta a próxima semente próxima em uma ordem fixa. Todos os celulares seguem a mesma ordem, então todos chegam à mesma distribuição.",
                "O Cubbles faz algo parecido. As três peças precisam poder ser colocadas juntas, então o jogo faz até quarenta tentativas com semente e usa a primeira que funciona. Já vamos ver o que isso significa para a justiça."]},
            {"h": "Fusos horários: a meia-noite de quem?", "p": [
                "Sem servidor, não existe um relógio único que decida quando começa um novo dia. Nossos jogos usam a data do seu próprio celular. Quando já é amanhã em Sydney, um jogador em Los Angeles ainda está no quebra-cabeça de hoje. Os dois estão certos segundo o próprio calendário.",
                "Para um jogador individual, é a escolha mais amigável. O quebra-cabeça novo aparece na sua meia-noite e a sua sequência acompanha os seus dias. O custo é que uma comparação diária global fica um pouco difusa: duas pessoas podem estar jogando dias diferentes ao mesmo tempo.",
                "A sequência é calculada do mesmo jeito. Ela conta dias locais consecutivos e o jogo é tolerante: se você ainda não jogou hoje, o dia de ontem mantém a sequência viva até o dia acabar."]},
            {"h": "O mesmo quebra-cabeça, quase sempre", "p": [
                "No sentido mais estrito, um quebra-cabeça com semente só é idêntico se cada passo depender da semente e de mais nada. O Cubbles é um exemplo honesto de que nem sempre é assim. A verificação de que cada conjunto de peças pode ser colocado depende do estado do seu tabuleiro. Se uma tentativa não cabe no seu tabuleiro, o jogo passa para a próxima, então dois jogadores podem ver, de vez em quando, conjuntos de peças diferentes. Na maior parte das vezes a primeira tentativa funciona e todos veem as mesmas peças, por isso descrevemos o jogo diário como igual para quase todos, e não para todos.",
                "Há outra pequena ressalva para quebra-cabeças escolhidos de uma lista. Se uma atualização muda a lista de fases, a escolha de um dia específico pode mudar. Jogadores em versões diferentes podem ver quebra-cabeças diferentes por alguns dias.",
                "São detalhes que vale decidir de propósito. Ou o quebra-cabeça não depende de nada além da semente, ou se aceita uma pequena diferença e se diz isso com clareza."]},
            {"h": "Trapaça, relógios e o que custa não ter servidor", "p": [
                "O preço de abrir mão do servidor é a confiança. O jogo acredita na data do seu celular. Se você mudar o relógio, poderá abrir o quebra-cabeça de outro dia. Em um jogo feito para se divertir, em que as pontuações são compartilhadas como desafio entre amigos, achamos uma troca aceitável. Um servidor que verificasse cada pontuação exigiria contas, armazenamento e cuidado com os dados das pessoas, e seria mais uma coisa que pode quebrar.",
                "As pontuações que vão para um ranking são informadas pelo aplicativo. Uma pessoa determinada pode enviar um número que o jogo não conquistou, e o aplicativo não consegue impedir isso por completo. Por isso tratamos os rankings como um jogo entre amigos, e não como uma competição com prêmios.",
                "Se você for criar um, decida logo do que o quebra-cabeça diário nunca deve depender. Deixe-o depender só da semente, teste se dois aparelhos produzem o mesmo resultado e mantenha congelada a regra que monta o quebra-cabeça. Se precisar mudar o construtor, faça isso com uma nova versão do desafio diário, e não em silêncio, ou o quebra-cabeça de ontem deixará de coincidir."]},
        ],
        "faq": [
            ["Um desafio diário precisa de conexão com a internet?", "Nos nossos jogos, não. O quebra-cabeça é montado no seu celular a partir da data, então funciona offline."],
            ["Meu amigo em outro país recebe hoje o mesmo quebra-cabeça?", "Normalmente sim, mas o dia novo começa na meia-noite de cada jogador, então alguém distante pode estar um dia à frente ou atrás."],
            ["Dá para trapacear mudando o relógio do celular?", "Dá para abrir o quebra-cabeça de outro dia. Sem servidor, o jogo confia na data do celular, por isso vemos o desafio diário como uma disputa amigável."],
            ["O que é uma semente?", "É o número inicial de um gerador de números aleatórios. A mesma semente sempre dá a mesma sequência, e assim aparelhos diferentes montam o mesmo quebra-cabeça."],
        ],
    },
}
