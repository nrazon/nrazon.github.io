# Yazı: Jetpack Compose'ta oyun hissi (ezilme/gerilme, parçacık, ses, titreşim; oyun motoru yok) - Cubbles kodundan
POST = {
    "id": "compose-game-juice",
    "app": "cubbles",
    "date": "2026-11-12",
    "tags": [
        "compose",
        "game-design",
        "android"
    ],
    "en": {
        "slug": "game-feel-jetpack-compose-without-game-engine",
        "title": "Game Feel in Jetpack Compose Without a Game Engine",
        "desc": "Squash, stretch, particles, synthesized sound and haptics in Jetpack Compose: how a block puzzle gets its game feel with one Canvas and one frame loop.",
        "intro": "Cubbles is a block-placing puzzle with cute faces on the blocks, and almost all of its charm is feedback: a piece that settles with a bounce, a row that melts away in a wave, a sound and a buzz that grow with your streak. None of it needs a game engine. This post walks through how it is done in plain Jetpack Compose, what the numbers are, where the shortcuts are, and how two other games of ours solve the same problem differently.",
        "sections": [
            {
                "h": "Why a puzzle does not need an engine",
                "p": [
                    "An 8 by 8 board, three pieces in a tray and a drag gesture do not need physics, a scene graph or a game loop framework. What they need is a clock and a way to draw. Compose gives you both: a Canvas to paint on, and a frame callback to read time from. Everything below sits on those two things."
                ]
            },
            {
                "h": "One Canvas, one clock",
                "p": [
                    "The game screen draws the board, the tray, the effects and the floating text in a single Canvas. A coroutine started with a launched effect loops forever: it waits for the next frame with withFrameNanos, ignores the frame time it is given, writes the current uptime in milliseconds into a state variable called now, and drops any finished effects from a list.",
                    "The important detail is where now is read. It is read inside the Canvas draw lambda, so each frame invalidates the drawing only, not the composition of the whole screen. The score text and the buttons around the board do not recompose sixty times a second. The board itself is a plain mutable object rather than observable state, so a small counter is bumped after each move to make the Canvas redraw. The cost of this design is honest: the loop never stops, even when no effect is running, because blinking eyes and the gently bobbing tray pieces also need a clock."
                ]
            },
            {
                "h": "Effects are data, not animations",
                "p": [
                    "Instead of one Animatable per block, the game keeps a list of small effect objects. There is a sealed class with a start time and a duration, and subclasses for a placement pop, a line clear, a floating text, a screen shake, a particle burst, a color flash and a sweeping light. They are created at the instant a piece is dropped and appended to the list.",
                    "The drawing code turns each one into a progress value between zero and one, by subtracting the start time from now and dividing by the duration, and derives everything from that number. There is no coroutine per effect, nothing to cancel, and nothing that can drift out of sync with the board. Layering is free: a big clear simply adds several effects to the list."
                ]
            },
            {
                "h": "Squash, stretch and the wave",
                "p": [
                    "A placed piece pops for 480 milliseconds. Its scale is one plus 0.28 times a sine over the first part of the animation, multiplied by one minus the progress, so it swells and settles with a fading amplitude. To be accurate, this is a damped swell rather than a volume-preserving squash and stretch: the blocks are rounded squares scaled uniformly, which is cheap and reads clearly at phone size.",
                    "The clear animation is where the personality is. Each cleared cell waits a delay of 28 milliseconds per step of Manhattan distance from the center of the piece you placed, so the clear spreads outward like a ripple and tells your eye where it began. Then the cell swells to 1.4 times its size during the first 30 percent of 380 milliseconds, shrinks to nothing, mixes toward white and fades its alpha, and wears a happy face until 70 percent of the way through. One smoothstep function, the classic three t squared minus two t cubed, is the only easing curve used anywhere in the file."
                ]
            },
            {
                "h": "Faces are just a few arcs",
                "p": [
                    "Every block has a face drawn from circles, lines and arcs, with a mood chosen per frame: normal, happy, excited or sad. Blinking needs no state. The eyes close when the current time plus the cell index times 911, taken modulo 3700 milliseconds, is under 130, so each block blinks on its own schedule. The eyes also shift by four percent of the block size toward the finger while you drag, which is a small thing that makes the board feel alive."
                ]
            },
            {
                "h": "Particles without a particle system",
                "p": [
                    "A particle here is an immutable object with a start position, a velocity, a size, a color and a spin. Nothing is updated per frame. The draw code computes the position in closed form from the elapsed time: start plus velocity times t, with a gravity term of half g times t squared added to the vertical axis, where g is sixteen cell heights per second squared. There is no pool and no per-particle state to maintain.",
                    "Counts are bounded by design. Each cleared cell emits 2 plus the hype level, capped at 4, particles, where hype is lines cleared plus the combo minus one. A board has 64 cells, so a single burst cannot exceed 384 particles. A perfect clear adds 90 pieces of confetti and a new record adds 70. A burst lives 1.1 seconds, shrinks to 40 percent of its size and fades out. Squares spin and circles do not. All randomness comes from a generator seeded with the event time, so effects are reproducible while debugging."
                ]
            },
            {
                "h": "Floating text that stays readable",
                "p": [
                    "Floating text such as the score, the combo and the praise words rises with the same smoothstep, pops in with a quick overshoot and stays for 1.9 seconds. It used to vanish in one second and players missed it. The words are drawn with a dark outline made of eight shifted copies, because white text on a light bathroom-tile background is unreadable without one. A real bug lives here too: on very small screens a long praise word was wider than the space available, and a clamp call with an inverted range crashed the app. The fix was a small helper that never inverts the range, plus shrinking the text to fit."
                ]
            },
            {
                "h": "Sound without sound files",
                "p": [
                    "There are no audio assets. At first use, a sound is synthesized into a short array of 16-bit samples at 22,050 Hz mono: a sine at the note frequency plus a second harmonic at 20 percent, multiplied by an exponential decay, with a 60-sample attack ramp, about three milliseconds, to avoid the click you get from starting at full amplitude. The arrays are cached by name, and each playback builds a static-mode AudioTrack with that array, tagged as game usage, and releases it from a position marker when it finishes."
                ]
            },
            {
                "h": "Haptics that you can actually feel",
                "p": [
                    "The vibration class drives the vibrator directly. A comment in the code explains why: the standard view haptic call follows the user's touch feedback setting and was barely perceptible on many phones in the first release. Instead the game builds waveforms, with amplitude control where the hardware reports it and plain timings where it does not, and wraps the call so a missing vibrator never crashes anything."
                ]
            },
            {
                "h": "The rule that keeps it honest",
                "p": [
                    "Feedback is cheap to add and easy to overdo, so the project notes set a rule: no effect for its own sake. The puzzle must stay readable and a bad moment must never feel like a punishment. In code that looks like this. A ghost of the piece and a highlight on the rows it would clear appear before you drop. The dragged piece is lifted 1.6 cells above your finger so that your hand does not hide it. Trays are generated so that a legal move always exists. And the game over screen only says how close you were to your best score when you are within 60 percent of it; otherwise it simply shows the best, so a poor run is not followed by a scolding.",
                    "One gap, stated plainly: Cubbles has no reduced-motion switch yet. Our bingo game does, and it shows the pattern. A setting is exposed through a composition local, and the confetti and the looping home screen animations check it and stand down."
                ]
            },
            {
                "h": "The same ideas in two other games",
                "p": [
                    "Where the screen is made of widgets rather than one Canvas, the standard animation API fits better. In the bingo game, a drawn ball pops in with an Animatable and a bouncy spring, scaling from 0.2 to 1 while it rotates. The daub on a bingo card uses an animate-as-state call with a spring of damping 0.42 so it lands with a wobble. A rejected tap increments an integer key, and a launched effect on that key snaps a shake value to one and springs it back to zero, read inside a graphics layer so nothing recomposes.",
                    "In a space puzzle of ours, the frame loop moves each gate a fixed 38 percent of the remaining distance toward its target cell on every frame. It is the simplest possible smoothing and it feels good, with the caveat that the speed depends on the frame rate. A rule of thumb from all three: use the animation API for widgets, and time-derived drawing for free-form scenes."
                ]
            },
            {
                "h": "What to take away",
                "p": [
                    "Keep effects as small data objects with a start time and a duration, derive everything from progress, read your clock inside the draw lambda, cap every effect, and let the game rules run ahead of the animation. You get a surprising amount of life from a few hundred lines of Canvas code and a sine function. If you want to see these numbers at work, Cubbles is the game they were tuned for."
                ]
            }
        ],
        "faq": [
            [
                "Can you build game feel in Jetpack Compose without a game engine?",
                "Yes, for puzzle and casual games. One Canvas, a frame loop with withFrameNanos and time-derived drawing cover squash, particles and screen shake."
            ],
            [
                "How do you avoid recomposing the whole screen every frame?",
                "Read the clock state only inside the Canvas draw lambda. Then each frame invalidates drawing, not composition."
            ],
            [
                "How are the sounds made without audio files?",
                "They are synthesized once into short arrays of samples, cached, and played with a static-mode AudioTrack that is released when playback ends."
            ],
            [
                "Why drive the vibrator directly?",
                "The standard haptic call depends on the user's touch feedback setting and was hardly felt on many phones, so the game builds its own waveforms."
            ],
            [
                "Does more feedback always make a game better?",
                "No. Effects should never hide the puzzle or punish the player, so each one here has a cap and the game over screen avoids discouraging messages."
            ]
        ]
    },
    "tr": {
        "slug": "oyun-motoru-olmadan-jetpack-compose-oyun-hissi",
        "title": "Oyun Motoru Olmadan Jetpack Compose ile Oyun Hissi",
        "desc": "Jetpack Compose'ta ezilme, gerilme, parçacık, üretilen ses ve titreşim: bir blok bulmacası tek Canvas ve tek kare döngüsüyle oyun hissini nasıl kazanır.",
        "intro": "Cubbles, blokların yüzü olan bir blok yerleştirme bulmacası ve cazibesinin neredeyse tamamı geri bildirimden geliyor: yaylanarak oturan bir parça, dalga gibi eriyen bir satır, serinle birlikte büyüyen ses ve titreşim. Bunların hiçbiri oyun motoru istemiyor. Bu yazı işin düz Jetpack Compose ile nasıl yapıldığını, sayıları, kestirme yolları ve başka iki oyunumuzun aynı sorunu nasıl farklı çözdüğünü anlatıyor.",
        "sections": [
            {
                "h": "Bir bulmaca neden motor istemez",
                "p": [
                    "8'e 8'lik bir tahta, tepsideki üç parça ve bir sürükleme hareketi fizik motoru, sahne ağacı ya da oyun döngüsü kütüphanesi istemez. İstediği şey bir saat ve çizim yeteneğidir. Compose ikisini de verir: üzerine boyayacağın bir Canvas ve zamanı okuyacağın bir kare geri çağrısı. Aşağıdakilerin hepsi bu ikisinin üstünde duruyor."
                ]
            },
            {
                "h": "Tek Canvas, tek saat",
                "p": [
                    "Oyun ekranı tahtayı, tepsiyi, efektleri ve yüzen yazıları tek bir Canvas içinde çizer. Bir launched effect ile başlatılan bir eş yordam sonsuza kadar döner: withFrameNanos ile sonraki kareyi bekler, verilen kare zamanını yok sayar, o anki çalışma süresini milisaniye olarak now adlı bir durum değişkenine yazar ve biten efektleri bir listeden atar.",
                    "Önemli olan now'un nerede okunduğu. Canvas'ın çizim lambdası içinde okunuyor; bu yüzden her kare yalnızca çizimi geçersiz kılıyor, ekranın tamamının kompozisyonunu değil. Skor yazısı ve tahtanın çevresindeki düğmeler saniyede altmış kez yeniden oluşmuyor. Tahtanın kendisi gözlemlenebilir durum değil, düz bir değişebilir nesne; bu yüzden her hamleden sonra küçük bir sayaç artırılıp Canvas'ın yeniden çizilmesi sağlanıyor. Bu tasarımın bedeli açık: efekt çalışmıyorken bile döngü durmuyor, çünkü göz kırpan gözler ve hafifçe sallanan tepsi parçaları da bir saate ihtiyaç duyuyor."
                ]
            },
            {
                "h": "Efektler animasyon değil, veridir",
                "p": [
                    "Her blok için bir Animatable yerine oyun küçük efekt nesnelerinden oluşan bir liste tutuyor. Başlangıç zamanı ve süresi olan bir mühürlü sınıf var; alt sınıfları yerleşme sıçraması, satır silme, yüzen yazı, ekran sarsıntısı, parçacık patlaması, renk parlaması ve süpüren ışık. Parça bırakıldığı anda oluşturulup listeye ekleniyorlar.",
                    "Çizim kodu her birini, now'dan başlangıç zamanını çıkarıp süreye bölerek sıfır ile bir arasında bir ilerleme değerine çeviriyor ve her şeyi bu sayıdan türetiyor. Efekt başına eş yordam yok, iptal edilecek bir şey yok ve tahtayla aynı hizadan kayabilecek hiçbir şey yok. Katmanlama bedava: büyük bir silme listeye birkaç efekt daha ekliyor."
                ]
            },
            {
                "h": "Ezilme, gerilme ve dalga",
                "p": [
                    "Yerleştirilen parça 480 milisaniye boyunca sıçrıyor. Ölçeği, animasyonun ilk kısmı üzerinde bir artı 0,28 çarpı bir sinüs, bunun da bir eksi ilerleme ile çarpılmış hâli; yani şişip sönen bir genlikle oturuyor. Doğrusunu söylemek gerekirse bu hacmi koruyan klasik ezilme-gerilme değil, sönümlenen bir şişme: bloklar yuvarlak köşeli kareler ve tek biçimli ölçekleniyor; bu ucuz ve telefon boyutunda net okunuyor.",
                    "Karakter silme animasyonunda. Silinen her hücre, koyduğun parçanın merkezine olan Manhattan uzaklığının her adımı için 28 milisaniye bekliyor; böylece silme dışarı doğru bir dalga gibi yayılıyor ve gözüne nereden başladığını söylüyor. Sonra hücre 380 milisaniyenin ilk yüzde 30'unda boyunun 1,4 katına şişiyor, sonra sıfıra küçülüyor, beyaza doğru karışıyor, saydamlığı sönüyor ve yolun yüzde 70'ine kadar mutlu bir yüz takıyor. Dosyada kullanılan tek yumuşatma eğrisi smoothstep, yani t karenin üç katı eksi t küpünün iki katı."
                ]
            },
            {
                "h": "Yüzler birkaç yaydan ibaret",
                "p": [
                    "Her bloğun yüzü daire, çizgi ve yaylardan çiziliyor ve ruh hâli her karede seçiliyor: normal, mutlu, heyecanlı ya da üzgün. Göz kırpmak için durum gerekmiyor. Şu anki zaman artı hücre numarası çarpı 911'in 3700 milisaniyeye göre modu 130'dan küçükse gözler kapanıyor; böylece her blok kendi takviminde kırpıyor. Sürüklerken gözler bloğun boyunun yüzde dördü kadar parmağa doğru kayıyor; küçük bir şey ama tahtayı canlı hissettiriyor."
                ]
            },
            {
                "h": "Parçacık sistemi olmadan parçacıklar",
                "p": [
                    "Burada bir parçacık; başlangıç konumu, hızı, boyutu, rengi ve dönüşü olan değişmez bir nesne. Kare başına hiçbir şey güncellenmiyor. Çizim kodu konumu geçen süreden kapalı formülle hesaplıyor: başlangıç artı hız çarpı t, dikey eksene de yarım g çarpı t kare eklenerek; g saniye karede on altı hücre boyu. Havuz yok, parçacık başına bakılacak durum yok.",
                    "Sayılar tasarım gereği sınırlı. Her silinen hücre 2 artı heyecan düzeyi kadar, en çok 4 olmak üzere parçacık saçıyor; heyecan düzeyi silinen satır sayısı artı seri eksi bir. Tahtada 64 hücre var, yani tek bir patlama 384 parçacığı geçemez. Mükemmel temizleme 90 konfeti, yeni rekor 70 konfeti ekliyor. Bir patlama 1,1 saniye yaşıyor, boyutunun yüzde 40'ına küçülüyor ve sönüyor. Kareler dönüyor, daireler dönmüyor. Rastgelelik olay zamanıyla tohumlanmış bir üreteçten geliyor; böylece hata ayıklarken efektler yeniden üretilebiliyor."
                ]
            },
            {
                "h": "Okunur kalan yüzen yazılar",
                "p": [
                    "Skor, seri ve övgü gibi yüzen yazılar aynı smoothstep ile yükseliyor, hızlı bir taşmayla beliriyor ve 1,9 saniye kalıyor. Eskiden bir saniyede kayboluyordu ve oyuncular kaçırıyordu. Yazılar sekiz kaydırılmış kopyadan oluşan koyu bir konturla çiziliyor, çünkü açık banyo fayansı zemininde beyaz yazı kontursuz okunmuyor. Burada gerçek bir hata da yaşadı: çok küçük ekranlarda uzun bir övgü sözcüğü kullanılabilir alandan geniş çıkıyordu ve ters aralıklı bir sınırlama çağrısı uygulamayı çökertti. Çözüm aralığı asla ters çevirmeyen küçük bir yardımcı ve yazıyı sığacak kadar küçültmek oldu."
                ]
            },
            {
                "h": "Ses dosyası olmadan ses",
                "p": [
                    "Hiç ses varlığı yok. İlk kullanımda bir ses, 22.050 Hz tek kanallı 16 bitlik kısa bir örnek dizisine üretiliyor: nota frekansında bir sinüs artı yüzde 20 oranında ikinci harmonik, üstel bir sönümle çarpılmış ve tam genlikle başlamaktan doğan tıkırtıyı önlemek için 60 örneklik, yaklaşık üç milisaniyelik bir yükselme rampasıyla. Diziler adıyla önbelleğe alınıyor; her çalmada bu diziyle statik kipte bir AudioTrack kuruluyor, oyun kullanımı olarak etiketleniyor ve bitince bir konum işaretçisinden serbest bırakılıyor."
                ]
            },
            {
                "h": "Gerçekten hissedilen titreşim",
                "p": [
                    "Titreşim sınıfı titreşim motorunu doğrudan sürüyor. Koddaki bir yorum nedenini açıklıyor: standart görünüm dokunsal geri bildirimi kullanıcının dokunma geri bildirimi ayarına bağlı ve ilk sürümde birçok telefonda neredeyse hissedilmiyordu. Bunun yerine oyun kendi dalga biçimlerini kuruyor; donanım bildiriyorsa genlik denetimiyle, bildirmiyorsa yalnızca sürelerle; çağrıyı da sarıyor, böylece titreşim motoru olmayan cihaz hiçbir şeyi çökertmiyor."
                ]
            },
            {
                "h": "Dürüst kalmanın kuralı",
                "p": [
                    "Geri bildirim eklemek ucuz ve abartmak kolay; bu yüzden proje notlarında bir kural var: kendi hatırı için efekt yok. Bulmaca okunur kalmalı ve kötü bir an asla ceza gibi hissettirmemeli. Kodda bu şöyle görünüyor. Bırakmadan önce parçanın hayaleti ve sileceği satırların vurgusu görünüyor. Sürüklenen parça parmağının 1,6 hücre üstünde duruyor ki elin onu gizlemesin. Tepsiler her zaman yasal bir hamle kalacak biçimde üretiliyor. Oyun sonu ekranı da en iyi skoruna ne kadar yaklaştığını yalnızca onun yüzde 60'ı içindeysen söylüyor; değilse yalnızca rekoru gösteriyor, böylece kötü bir oyunun ardından azar işitmiyorsun.",
                    "Açıkça söyleyeyim: Cubbles'ta henüz hareketi azaltma düğmesi yok. Bingo oyunumuzda var ve kalıbı gösteriyor. Ayar bir composition local ile açılıyor; konfeti ve ana ekrandaki döngüsel animasyonlar ona bakıp geri çekiliyor."
                ]
            },
            {
                "h": "Aynı fikirler iki başka oyunda",
                "p": [
                    "Ekran tek bir Canvas yerine bileşenlerden oluştuğunda standart animasyon API'si daha iyi uyuyor. Bingo oyununda çekilen top, bir Animatable ve zıplayan bir yayla beliriyor; dönerken 0,2'den 1'e ölçekleniyor. Bingo kartındaki işaret, sönüm oranı 0,42 olan bir yayla animate-as-state çağrısı kullanıyor ve titreyerek oturuyor. Reddedilen bir dokunuş bir tamsayı anahtarı artırıyor, o anahtardaki bir launched effect sarsıntı değerini bire çekip yayla sıfıra döndürüyor; değer bir graphics layer içinde okunduğu için hiçbir şey yeniden oluşmuyor.",
                    "Bir uzay bulmacamızda ise kare döngüsü her karede her kapıyı hedef hücreye kalan mesafenin sabit yüzde 38'i kadar yaklaştırıyor. Bu mümkün en basit yumuşatma ve iyi hissettiriyor; tek çekincesi hızın kare hızına bağlı olması. Üçünden çıkan pratik kural: bileşenler için animasyon API'si, serbest sahneler için zamandan türetilen çizim."
                ]
            },
            {
                "h": "Akılda kalanlar",
                "p": [
                    "Efektleri başlangıç zamanı ve süresi olan küçük veri nesneleri olarak tut, her şeyi ilerlemeden türet, saatini çizim lambdasında oku, her efekte tavan koy ve oyun kurallarının animasyonun önünde koşmasına izin ver. Birkaç yüz satır Canvas kodu ve bir sinüs fonksiyonundan şaşırtıcı miktarda canlılık çıkıyor. Bu sayıların iş başında nasıl göründüğünü merak edersen Cubbles, hepsinin ayarlandığı oyun."
                ]
            }
        ],
        "faq": [
            [
                "Oyun motoru olmadan Jetpack Compose'ta oyun hissi yapılabilir mi?",
                "Evet, bulmaca ve hafif oyunlar için. Tek Canvas, withFrameNanos ile bir kare döngüsü ve zamandan türetilen çizim ezilmeyi, parçacıkları ve sarsıntıyı karşılıyor."
            ],
            [
                "Her karede tüm ekranın yeniden oluşması nasıl önlenir?",
                "Saat durumunu yalnızca Canvas çizim lambdasında oku. O zaman her kare kompozisyonu değil, çizimi geçersiz kılar."
            ],
            [
                "Ses dosyası olmadan sesler nasıl yapılıyor?",
                "Bir kez kısa örnek dizilerine üretiliyor, önbelleğe alınıyor ve çalma bitince serbest bırakılan statik kipte bir AudioTrack ile çalınıyor."
            ],
            [
                "Titreşim motoru neden doğrudan sürülüyor?",
                "Standart dokunsal çağrı kullanıcının dokunma geri bildirimi ayarına bağlı ve birçok telefonda neredeyse hissedilmedi; bu yüzden oyun kendi dalga biçimlerini kuruyor."
            ],
            [
                "Daha çok geri bildirim oyunu her zaman daha iyi yapar mı?",
                "Hayır. Efektler bulmacayı gizlememeli ya da oyuncuyu cezalandırmamalı; bu yüzden buradaki her efektin bir tavanı var ve oyun sonu ekranı cesaret kırıcı mesajlardan kaçınıyor."
            ]
        ]
    },
    "es": {
        "slug": "sensacion-de-juego-jetpack-compose-sin-motor",
        "title": "Sensación de juego en Jetpack Compose sin motor de juego",
        "desc": "Squash, stretch, partículas, sonido sintetizado y vibración en Jetpack Compose: cómo un puzle de bloques gana sensación de juego con un Canvas y un bucle.",
        "intro": "Cubbles es un puzle de colocar bloques con caras simpáticas, y casi todo su encanto es respuesta al jugador: una pieza que se asienta con un rebote, una fila que se deshace en ola, un sonido y una vibración que crecen con tu racha. Nada de eso necesita un motor de juego. Esta entrada explica cómo se hace con Jetpack Compose a secas, qué números se usan, dónde están los atajos y cómo otros dos juegos nuestros resuelven el mismo problema de otra manera.",
        "sections": [
            {
                "h": "Por qué un puzle no necesita motor",
                "p": [
                    "Un tablero de 8 por 8, tres piezas en una bandeja y un gesto de arrastre no necesitan física, un grafo de escena ni un marco de bucle de juego. Necesitan un reloj y una forma de dibujar. Compose da las dos cosas: un Canvas donde pintar y una llamada por fotograma de la que leer el tiempo. Todo lo que sigue se apoya en esas dos piezas."
                ]
            },
            {
                "h": "Un Canvas, un reloj",
                "p": [
                    "La pantalla de juego dibuja el tablero, la bandeja, los efectos y los textos flotantes en un único Canvas. Una corrutina lanzada con un efecto lanzado da vueltas para siempre: espera el siguiente fotograma con withFrameNanos, ignora el tiempo de fotograma que recibe, escribe el tiempo de actividad actual en milisegundos en una variable de estado llamada now y quita de una lista los efectos terminados.",
                    "Lo importante es dónde se lee now. Se lee dentro de la lambda de dibujo del Canvas, así que cada fotograma invalida solo el dibujo y no la composición de toda la pantalla. El texto de la puntuación y los botones alrededor del tablero no se recomponen sesenta veces por segundo. El coste de este diseño es evidente: el bucle no se detiene nunca, ni siquiera sin efectos activos, porque los ojos que parpadean y las piezas de la bandeja que se mecen suavemente también necesitan un reloj."
                ]
            },
            {
                "h": "Los efectos son datos, no animaciones",
                "p": [
                    "En lugar de un Animatable por bloque, el juego mantiene una lista de pequeños objetos de efecto. Hay una clase sellada con un instante de inicio y una duración, y subclases para el rebote al colocar, la limpieza de línea, el texto flotante, la sacudida de pantalla, la ráfaga de partículas, el destello de color y la luz que barre. Se crean en el instante en que sueltas una pieza y se añaden a la lista.",
                    "El código de dibujo convierte cada uno en un valor de progreso entre cero y uno, restando el inicio a now y dividiendo por la duración, y deriva todo de ese número. No hay una corrutina por efecto, nada que cancelar y nada que pueda desincronizarse del tablero."
                ]
            },
            {
                "h": "Squash, stretch y la ola",
                "p": [
                    "Una pieza colocada rebota durante 480 milisegundos. Su escala es uno más 0,28 por un seno sobre la primera parte de la animación, multiplicado por uno menos el progreso, de modo que se hincha y se asienta con una amplitud que se apaga.",
                    "La personalidad está en la animación de limpieza. Cada celda limpiada espera 28 milisegundos por cada paso de distancia Manhattan desde el centro de la pieza que colocaste, así que la limpieza se extiende hacia fuera como una onda y le dice a tu ojo dónde empezó. Después la celda se hincha hasta 1,4 veces su tamaño durante el primer 30 por ciento de 380 milisegundos, se encoge hasta desaparecer, se mezcla hacia el blanco, pierde opacidad y lleva una cara feliz hasta el 70 por ciento del recorrido. Una sola función smoothstep, tres t al cuadrado menos dos t al cubo, es la única curva de suavizado de todo el archivo."
                ]
            },
            {
                "h": "Las caras son unos pocos arcos",
                "p": [
                    "Cada bloque tiene una cara dibujada con círculos, líneas y arcos, con un estado de ánimo elegido en cada fotograma: normal, feliz, emocionado o triste. Parpadear no necesita estado. Los ojos se cierran cuando el tiempo actual más el índice de la celda por 911, tomado módulo 3700 milisegundos, es menor que 130, así que cada bloque parpadea según su propio calendario. Además los ojos se desplazan un cuatro por ciento del tamaño del bloque hacia el dedo mientras arrastras, un detalle pequeño que hace que el tablero parezca vivo."
                ]
            },
            {
                "h": "Partículas sin sistema de partículas",
                "p": [
                    "Aquí una partícula es un objeto inmutable con posición inicial, velocidad, tamaño, color y giro. No se actualiza nada por fotograma. El código de dibujo calcula la posición en forma cerrada a partir del tiempo transcurrido: inicio más velocidad por t, con un término de gravedad de un medio de g por t al cuadrado en el eje vertical, donde g son dieciséis alturas de celda por segundo al cuadrado. No hay reserva de objetos ni estado por partícula que mantener.",
                    "Las cantidades están acotadas por diseño. Cada celda limpiada emite 2 más el nivel de emoción, con un máximo de 4, partículas, donde la emoción es líneas limpiadas más la racha menos uno. Un tablero tiene 64 celdas, así que una sola ráfaga no puede pasar de 384 partículas. Una limpieza perfecta añade 90 piezas de confeti y un récord nuevo añade 70. Una ráfaga vive 1,1 segundos, se encoge hasta el 40 por ciento de su tamaño y se desvanece."
                ]
            },
            {
                "h": "Texto flotante que sigue siendo legible",
                "p": [
                    "Los textos flotantes, como la puntuación, la racha y las palabras de elogio, suben con el mismo smoothstep, aparecen con un rápido sobrepaso y permanecen 1,9 segundos. Las palabras se dibujan con un contorno oscuro hecho de ocho copias desplazadas, porque el texto blanco sobre un fondo claro de azulejos de baño no se lee sin él. Aquí también vivió un error real: en pantallas muy pequeñas una palabra de elogio larga era más ancha que el espacio disponible, y una llamada de limitación con el rango invertido hacía fallar la aplicación. La solución fue una pequeña función auxiliar que nunca invierte el rango y reducir el texto hasta que cabe."
                ]
            },
            {
                "h": "Sonido sin archivos de sonido",
                "p": [
                    "No hay recursos de audio. En el primer uso, un sonido se sintetiza en una matriz corta de muestras de 16 bits a 22.050 Hz en mono: un seno a la frecuencia de la nota más un segundo armónico al 20 por ciento, multiplicado por una caída exponencial, con una rampa de ataque de 60 muestras, unos tres milisegundos, para evitar el chasquido que produce empezar a plena amplitud. Las matrices se guardan en caché por nombre; cada reproducción crea un AudioTrack en modo estático con esa matriz, marcado como uso de juego, y lo libera desde un marcador de posición al terminar."
                ]
            },
            {
                "h": "Vibración que de verdad se siente",
                "p": [
                    "La clase de vibración maneja el vibrador directamente. Un comentario en el código explica el motivo: la llamada háptica estándar de las vistas depende del ajuste de respuesta táctil del usuario y apenas se notaba en muchos móviles en la primera versión. En su lugar el juego construye sus propias formas de onda, con control de amplitud donde el hardware lo declara y solo con tiempos donde no, y envuelve la llamada para que un dispositivo sin vibrador nunca provoque un fallo."
                ]
            },
            {
                "h": "La regla que mantiene la honestidad",
                "p": [
                    "Añadir respuesta al jugador es barato y es fácil pasarse, así que las notas del proyecto fijan una regla: ningún efecto por el efecto. El puzle debe seguir siendo legible y un mal momento nunca debe sentirse como un castigo. En el código se ve así. Antes de soltar aparecen un fantasma de la pieza y un resaltado de las filas que limpiaría. La pieza arrastrada se levanta 1,6 celdas sobre el dedo para que la mano no la tape. Las bandejas se generan de modo que siempre quede una jugada legal. Y la pantalla de fin de partida solo dice lo cerca que estuviste de tu mejor puntuación cuando estás dentro del 60 por ciento de ella; si no, solo muestra el récord, de modo que una mala partida no va seguida de una regañina.",
                    "Una carencia, dicha sin rodeos: Cubbles todavía no tiene un interruptor para reducir el movimiento. Nuestro juego de bingo sí, y muestra el patrón. El ajuste se expone mediante un composition local, y el confeti y las animaciones en bucle de la pantalla de inicio lo consultan y se retiran."
                ]
            },
            {
                "h": "Las mismas ideas en otros dos juegos",
                "p": [
                    "Cuando la pantalla se compone de widgets en lugar de un solo Canvas, encaja mejor la API de animación estándar. En el juego de bingo, la bola extraída aparece con un Animatable y un muelle rebotón, escalando de 0,2 a 1 mientras gira. La marca sobre un cartón de bingo usa una llamada animate-as-state con un muelle de amortiguación 0,42 para asentarse con un temblor. Un toque rechazado incrementa una clave entera, y un efecto lanzado sobre esa clave fija un valor de sacudida en uno y lo devuelve a cero con un muelle, leído dentro de una graphics layer para que nada se recomponga.",
                    "En un puzle espacial nuestro, el bucle de fotogramas acerca cada puerta, en cada fotograma, un 38 por ciento fijo de la distancia restante hacia su celda de destino. Es el suavizado más simple posible y se siente bien, con la salvedad de que la velocidad depende de la tasa de fotogramas. Una regla práctica de los tres: la API de animación para widgets y dibujo derivado del tiempo para escenas libres."
                ]
            },
            {
                "h": "Lo que conviene llevarse",
                "p": [
                    "Guarda los efectos como pequeños objetos de datos con inicio y duración, deriva todo del progreso, lee tu reloj dentro de la lambda de dibujo, pon un techo a cada efecto y deja que las reglas del juego vayan por delante de la animación. Se obtiene una cantidad sorprendente de vida con unos cientos de líneas de Canvas y una función seno. Si quieres ver estos números en acción, Cubbles es el juego para el que se ajustaron."
                ]
            }
        ],
        "faq": [
            [
                "¿Se puede lograr sensación de juego en Jetpack Compose sin motor de juego?",
                "Sí, en puzles y juegos casuales. Un Canvas, un bucle de fotogramas con withFrameNanos y dibujo derivado del tiempo cubren el squash, las partículas y la sacudida."
            ],
            [
                "¿Cómo se evita recomponer toda la pantalla en cada fotograma?",
                "Leyendo el estado del reloj solo dentro de la lambda de dibujo del Canvas. Así cada fotograma invalida el dibujo y no la composición."
            ],
            [
                "¿Cómo se hacen los sonidos sin archivos de audio?",
                "Se sintetizan una vez en matrices cortas de muestras, se guardan en caché y se reproducen con un AudioTrack en modo estático que se libera al terminar."
            ],
            [
                "¿Por qué se maneja el vibrador directamente?",
                "La llamada háptica estándar depende del ajuste de respuesta táctil del usuario y apenas se sentía en muchos móviles, así que el juego construye sus propias formas de onda."
            ],
            [
                "¿Más respuesta al jugador siempre mejora un juego?",
                "No. Los efectos no deben tapar el puzle ni castigar al jugador, por eso cada efecto aquí tiene un límite y la pantalla final evita mensajes desalentadores."
            ]
        ]
    },
    "pt": {
        "slug": "game-feel-jetpack-compose-sem-motor-de-jogo",
        "title": "Game feel no Jetpack Compose sem motor de jogo",
        "desc": "Squash, stretch, partículas, som sintetizado e vibração no Jetpack Compose: como um quebra-cabeça de blocos ganha game feel com um Canvas e um laço.",
        "intro": "O Cubbles é um quebra-cabeça de encaixar blocos com carinhas simpáticas, e quase todo o seu charme é resposta ao jogador: uma peça que assenta com um quique, uma linha que derrete em onda, um som e uma vibração que crescem com a sua sequência. Nada disso precisa de um motor de jogo. Este texto mostra como se faz com Jetpack Compose puro, quais são os números, onde estão os atalhos e como outros dois jogos nossos resolvem o mesmo problema de outro jeito.",
        "sections": [
            {
                "h": "Por que um quebra-cabeça não precisa de motor",
                "p": [
                    "Um tabuleiro de 8 por 8, três peças numa bandeja e um gesto de arrastar não precisam de física, de grafo de cena nem de um framework de laço de jogo. Precisam de um relógio e de uma forma de desenhar. O Compose oferece as duas coisas: um Canvas para pintar e uma chamada por quadro de onde ler o tempo. Tudo o que vem a seguir se apoia nessas duas peças."
                ]
            },
            {
                "h": "Um Canvas, um relógio",
                "p": [
                    "A tela do jogo desenha o tabuleiro, a bandeja, os efeitos e os textos flutuantes num único Canvas. Uma corrotina iniciada com um efeito lançado roda para sempre: espera o próximo quadro com withFrameNanos, ignora o tempo de quadro recebido, grava o tempo de atividade atual em milissegundos numa variável de estado chamada now e remove de uma lista os efeitos que terminaram.",
                    "O detalhe importante é onde now é lido. Ele é lido dentro da lambda de desenho do Canvas, então cada quadro invalida apenas o desenho e não a composição da tela inteira. O texto da pontuação e os botões em volta do tabuleiro não são recompostos sessenta vezes por segundo. O custo desse desenho é claro: o laço nunca para, mesmo sem efeito em andamento, porque os olhos que piscam e as peças da bandeja que balançam suavemente também precisam de um relógio."
                ]
            },
            {
                "h": "Efeitos são dados, não animações",
                "p": [
                    "Em vez de um Animatable por bloco, o jogo mantém uma lista de pequenos objetos de efeito. Existe uma classe selada com instante de início e duração, e subclasses para o quique ao colocar, a limpeza de linha, o texto flutuante, o tremor de tela, a rajada de partículas, o clarão de cor e a luz que varre. Eles são criados no instante em que você solta a peça e acrescentados à lista.",
                    "O código de desenho transforma cada um num valor de progresso entre zero e um, subtraindo o início de now e dividindo pela duração, e deriva tudo desse número. Não há corrotina por efeito, nada a cancelar e nada que possa sair de sincronia com o tabuleiro."
                ]
            },
            {
                "h": "Squash, stretch e a onda",
                "p": [
                    "Uma peça colocada quica por 480 milissegundos. Sua escala é um mais 0,28 vezes um seno sobre a primeira parte da animação, multiplicado por um menos o progresso, de modo que ela incha e assenta com uma amplitude que vai se apagando. Para ser exato, é um inchaço amortecido e não um squash and stretch que preserva o volume: os blocos são quadrados arredondados escalados de modo uniforme, o que é barato e se lê bem no tamanho de um celular.",
                    "A personalidade está na animação de limpeza. Cada célula limpa espera 28 milissegundos por passo de distância Manhattan a partir do centro da peça que você colocou, então a limpeza se espalha para fora como uma ondulação e diz ao seu olho onde começou. Depois a célula incha até 1,4 vez o seu tamanho nos primeiros 30 por cento de 380 milissegundos, encolhe até sumir, mistura-se ao branco, perde opacidade e usa uma carinha feliz até 70 por cento do caminho. Uma única função smoothstep, três t ao quadrado menos dois t ao cubo, é a única curva de suavização usada em todo o arquivo."
                ]
            },
            {
                "h": "Rostos são só alguns arcos",
                "p": [
                    "Cada bloco tem um rosto desenhado com círculos, linhas e arcos, com um humor escolhido a cada quadro: normal, feliz, empolgado ou triste. Piscar não precisa de estado. Os olhos se fecham quando o tempo atual mais o índice da célula vezes 911, tomado módulo 3700 milissegundos, é menor que 130, então cada bloco pisca no seu próprio ritmo. Os olhos também se deslocam quatro por cento do tamanho do bloco em direção ao dedo enquanto você arrasta, um detalhe pequeno que faz o tabuleiro parecer vivo."
                ]
            },
            {
                "h": "Partículas sem sistema de partículas",
                "p": [
                    "Aqui uma partícula é um objeto imutável com posição inicial, velocidade, tamanho, cor e giro. Nada é atualizado por quadro. O código de desenho calcula a posição em forma fechada a partir do tempo decorrido: início mais velocidade vezes t, com um termo de gravidade de meio g vezes t ao quadrado no eixo vertical, em que g vale dezesseis alturas de célula por segundo ao quadrado. Não há reserva de objetos nem estado por partícula para manter.",
                    "As quantidades são limitadas por projeto. Cada célula limpa emite 2 mais o nível de empolgação, no máximo 4, partículas, em que a empolgação é linhas limpas mais a sequência menos um. Um tabuleiro tem 64 células, então uma única rajada não passa de 384 partículas. Uma limpeza perfeita acrescenta 90 peças de confete e um novo recorde acrescenta 70. Uma rajada vive 1,1 segundo, encolhe até 40 por cento do tamanho e some."
                ]
            },
            {
                "h": "Texto flutuante que continua legível",
                "p": [
                    "Os textos flutuantes, como a pontuação, a sequência e as palavras de elogio, sobem com o mesmo smoothstep, surgem com um rápido excesso e ficam 1,9 segundo. As palavras são desenhadas com um contorno escuro feito de oito cópias deslocadas, porque texto branco sobre um fundo claro de azulejo de banheiro não se lê sem ele. Aqui também morou um erro real: em telas muito pequenas uma palavra de elogio longa era mais larga que o espaço disponível, e uma chamada de limitação com o intervalo invertido derrubava o aplicativo. A correção foi uma pequena função auxiliar que nunca inverte o intervalo, mais reduzir o texto até caber."
                ]
            },
            {
                "h": "Som sem arquivos de som",
                "p": [
                    "Não há recursos de áudio. No primeiro uso, um som é sintetizado numa matriz curta de amostras de 16 bits a 22.050 Hz em mono: um seno na frequência da nota mais um segundo harmônico a 20 por cento, multiplicado por um decaimento exponencial, com uma rampa de ataque de 60 amostras, cerca de três milissegundos, para evitar o estalo de começar em amplitude total. As matrizes ficam em cache por nome; cada reprodução cria um AudioTrack em modo estático com essa matriz, marcado como uso de jogo, e o libera a partir de um marcador de posição quando termina."
                ]
            },
            {
                "h": "Vibração que dá para sentir de verdade",
                "p": [
                    "A classe de vibração controla o vibrador diretamente. Um comentário no código explica o motivo: a chamada háptica padrão das views depende da configuração de resposta ao toque do usuário e quase não era percebida em muitos celulares na primeira versão. Em vez disso o jogo monta suas próprias formas de onda, com controle de amplitude quando o hardware informa e só com tempos quando não, e envolve a chamada para que um aparelho sem vibrador nunca cause uma falha."
                ]
            },
            {
                "h": "A regra que mantém a honestidade",
                "p": [
                    "Adicionar resposta ao jogador é barato e é fácil exagerar, por isso as notas do projeto fixam uma regra: nenhum efeito por si só. O quebra-cabeça tem de continuar legível e um mau momento nunca deve parecer um castigo. No código isso aparece assim. Antes de soltar, surgem um fantasma da peça e um realce das linhas que ela limparia. A peça arrastada fica 1,6 célula acima do dedo para que a mão não a esconda. As bandejas são geradas de modo que sempre exista uma jogada legal. E a tela de fim de jogo só diz o quão perto você ficou da sua melhor pontuação quando está dentro de 60 por cento dela; caso contrário, mostra apenas o recorde, para que uma partida ruim não termine em bronca.",
                    "Uma lacuna, dita sem rodeios: o Cubbles ainda não tem uma chave para reduzir o movimento. Nosso jogo de bingo tem, e mostra o padrão. A configuração é exposta por um composition local, e o confete e as animações em laço da tela inicial a consultam e se retiram."
                ]
            },
            {
                "h": "As mesmas ideias em outros dois jogos",
                "p": [
                    "Quando a tela é feita de widgets em vez de um único Canvas, a API de animação padrão se encaixa melhor. No jogo de bingo, a bola sorteada surge com um Animatable e uma mola saltitante, escalando de 0,2 a 1 enquanto gira. A marca na cartela usa uma chamada animate-as-state com uma mola de amortecimento 0,42 para assentar com um tremor. Um toque rejeitado incrementa uma chave inteira, e um efeito lançado sobre essa chave fixa um valor de tremor em um e o devolve a zero com uma mola, lido dentro de uma graphics layer para que nada seja recomposto.",
                    "Num quebra-cabeça espacial nosso, o laço de quadros aproxima cada portal, a cada quadro, de uma fração fixa de 38 por cento da distância restante até a célula de destino. É a suavização mais simples possível e dá uma boa sensação, com a ressalva de que a velocidade depende da taxa de quadros. Uma regra prática dos três: API de animação para widgets e desenho derivado do tempo para cenas livres."
                ]
            },
            {
                "h": "O que levar daqui",
                "p": [
                    "Guarde os efeitos como pequenos objetos de dados com início e duração, derive tudo do progresso, leia o relógio dentro da lambda de desenho, ponha um teto em cada efeito e deixe as regras do jogo andarem na frente da animação. Sai uma quantidade surpreendente de vida de algumas centenas de linhas de Canvas e uma função seno. Se quiser ver esses números em ação, o Cubbles é o jogo para o qual eles foram ajustados."
                ]
            }
        ],
        "faq": [
            [
                "Dá para criar game feel no Jetpack Compose sem motor de jogo?",
                "Sim, em quebra-cabeças e jogos casuais. Um Canvas, um laço de quadros com withFrameNanos e desenho derivado do tempo cobrem squash, partículas e tremor."
            ],
            [
                "Como evitar recompor a tela inteira a cada quadro?",
                "Lendo o estado do relógio apenas dentro da lambda de desenho do Canvas. Assim cada quadro invalida o desenho e não a composição."
            ],
            [
                "Como os sons são feitos sem arquivos de áudio?",
                "São sintetizados uma vez em matrizes curtas de amostras, guardados em cache e tocados com um AudioTrack em modo estático liberado ao fim da reprodução."
            ],
            [
                "Por que controlar o vibrador diretamente?",
                "A chamada háptica padrão depende da configuração de resposta ao toque do usuário e quase não era sentida em muitos celulares, então o jogo monta suas próprias formas de onda."
            ],
            [
                "Mais resposta ao jogador sempre melhora um jogo?",
                "Não. Os efeitos não devem esconder o quebra-cabeça nem punir o jogador, por isso cada efeito aqui tem um limite e a tela final evita mensagens desanimadoras."
            ]
        ]
    }
}
