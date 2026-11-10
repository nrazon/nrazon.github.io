# Blog: gelistirici yazisi - pentomino bolumleri Dancing Links ile nasil cozulur/uretilir
POST = {
    "id": "pentomino-dlx",
    "app": "pentolings",
    "date": "2026-11-10",
    "en": {
        "slug": "pentomino-puzzles-dancing-links-exact-cover",
        "title": "How We Build Pentomino Levels with Dancing Links",
        "desc": "A developer story: how exact cover and Knuth's Dancing Links solve and generate Pentolings levels, from 63 piece positions to unique puzzles and hints.",
        "intro": "Every Fit level in Pentolings is a promise: there is a way to fill this shape with these pieces. To keep that promise in 150 levels, and to give you a hint at any moment, the game contains a small solver based on Donald Knuth's Dancing Links. Here is how it works, using a tiny example anyone can follow.",
        "sections": [
            {
                "h": "A pentomino puzzle is an exact cover problem",
                "p": [
                    "Look at a level as a list of rules. Every piece must be used exactly once. Every square of the shape must be covered exactly once. Nothing may overlap and nothing may be left over. A problem made of rules like these is called an exact cover problem, and a lot of puzzles turn out to be exactly that, from Sudoku to scheduling.",
                    "To get a computer to solve it, we write the problem as a table. Each column is one rule: a column for every piece, and a column for every square of the shape. Each row is one possible move: a specific piece, turned a specific way, placed at a specific spot. A row marks the columns it satisfies: the piece's own column, and the five squares it would cover. The puzzle is solved when you choose rows so that every column is marked exactly once."
                ]
            },
            {
                "h": "63 positions: the rows of the table",
                "p": [
                    "A pentomino can be turned and flipped, so first the game lists every different position of each of the twelve pieces. It rotates and mirrors the shape and keeps only the results that are really new. X gives 1 position, I gives 2, T, U, V, W and Z give 4 each, and F, L, N, P and Y give 8 each. That adds up to 63 positions for the whole set, a number the code checks.",
                    "Then, for the level's shape, it slides each position to every spot where all five squares lie inside the shape. For a 3x20 rectangle with all twelve pieces, that makes 1236 candidate rows. For the biggest level, a 6x10 rectangle, there are 2056. The table has 72 columns: 12 pieces plus 60 squares."
                ]
            },
            {
                "h": "A tiny example",
                "p": [
                    "Take a 3x5 rectangle and the pieces P, U and V. The table has 3 piece columns and 15 square columns, so 18 columns in all. The pieces have 40, 20 and 12 possible placements, which gives 72 rows. Choosing three rows that mark every column exactly once gives the answer: V on the left and bottom edges, U on the right, P in the middle. In text, the three rows of the board read VPPUU, VPPPU and VVVUU. Turning or mirroring the whole rectangle gives four versions of the same answer, so the solver finds four solutions that look the same to a person."
                ]
            },
            {
                "h": "Knuth's Dancing Links, in plain words",
                "p": [
                    "The search is Algorithm X. Pick a column that is not yet covered. Try each row that marks it. Choosing a row means that its other columns are now taken, so every row that conflicts with it can be thrown away. Then repeat with the smaller table. If a column ever has no rows left, you made a wrong choice earlier, so you back up and try the next row.",
                    "The clever part is how the table is stored. Donald Knuth observed that you can keep the marks in linked lists, where every mark points to its left, right, upper and lower neighbor. Removing a row is just re-pointing a few links, and the removed item keeps remembering where it was, so putting it back is a matter of reversing the steps. Because nodes seem to jump out and back in, he called the technique Dancing Links. In Pentolings, Dlx.kt is about eighty lines and works on plain integer arrays for speed.",
                    "One more trick: at each step the solver picks the column with the fewest remaining rows. If a square can be covered in only two ways, the search quickly tests those two instead of wandering around the table. It is the computer version of what we said in the how-to guide: start with the tight spots."
                ]
            },
            {
                "h": "Locked pieces and levels that are fair",
                "p": [
                    "Some Pentolings levels begin with a locked piece. Those pieces come from a real solution: the generator finds one answer, then freezes one or two of its pieces. The solver treats them as already chosen, removes their squares and columns from the table, and counts what is left.",
                    "Making a level involves more than solving. A generator builds an outline by dropping the pieces next to each other at random, so a solution exists by construction. It then scores many outlines, rewarding solid shapes, penalizing holes and rewarding symmetry, and prefers shapes with more answers in early levels. Because outlines made this way usually have exactly one solution, the difficulty mostly comes from the number of pieces and the odd shape of the outline. Each of the 150 levels is solved again by the tests, checked for duplicates (a rotated or mirrored copy counts as the same), and the final level, a 6x10 rectangle, is the one place with a huge number of answers. A test also confirms the classic count for 3x20: eight, which is the two true answers times four ways to turn or mirror the rectangle."
                ]
            },
            {
                "h": "Why not just try everything?",
                "p": [
                    "You could solve a puzzle by trying every piece in every position, one after another, and checking at the end. That does not work, even for a computer. With twelve pieces, 63 positions and dozens of spots, the number of combinations is astronomical, and almost all of them overlap or leave gaps in the first few moves.",
                    "The trick is to stop a bad branch as soon as you can see it is bad. Algorithm X does exactly that. The moment one square has no piece that could still cover it, the search stops going deeper and backs up. Dancing Links makes each back-up cheap. This is why a 6x10 board, with 2056 candidate placements, is solved quickly even on a phone, and why the hint button does not need a server."
                ]
            },
            {
                "h": "What we learned",
                "p": [
                    "The same solver logic exists twice: in Python, where the generator builds and checks the 150-level pack, and in Kotlin, which ships in the app. The Kotlin tests then solve every level of the pack again from scratch. Having two independent implementations means a mistake in one is unlikely to hide from the other.",
                    "The biggest surprise was how rarely a random outline has more than one answer. We expected many puzzles to have several solutions and found the opposite. It turns out that this is fine: players care that a level is solvable and fair, not how many solutions exist, so the game accepts any valid fill. What the solver gives us is the promise that every level, and every hint, can be trusted."
                ]
            },
            {
                "h": "Hints come from the same solver",
                "p": [
                    "The Hint button asks the solver a new question: given the pieces you have already placed, how does the rest fit? It treats your placed pieces as fixed, solves the remainder and highlights the next piece in the answer it finds. If you follow the hint, the next one can come from memory without solving again. The work runs in the background with a time limit so the screen never freezes.",
                    "If your placed pieces make a solution impossible, the solver finds nothing and the game tells you so: no solution from here, take a piece back. That makes hints useful even when you are not stuck but just unsure. And the game accepts any valid way to fill the shape, not only the one the generator found, so you are never forced to guess the author's answer."
                ]
            }
        ],
        "faq": [
            [
                "What is an exact cover problem?",
                "A problem where you must choose some options so that every item is covered exactly once, with no overlaps and no leftovers. A pentomino puzzle is one."
            ],
            [
                "What are Dancing Links?",
                "A way, published by Donald Knuth, to store a search table in linked lists so that rows can be removed and restored very quickly during a backtracking search."
            ],
            [
                "Why do the pieces have 63 positions?",
                "Each of the 12 pieces can be rotated and flipped, and some of those positions look the same. Counting only distinct ones gives 63 across the whole set."
            ],
            [
                "Does the game have only one correct answer per level?",
                "No. The game accepts any valid way to fill the shape, even if it differs from the one the level was built from."
            ]
        ]
    },
    "tr": {
        "slug": "pentomino-bulmacalari-dancing-links-tam-kapsama",
        "title": "Pentomino Bölümlerini Dancing Links ile Nasıl Üretiyoruz",
        "desc": "Geliştirici hikâyesi: tam kapsama ve Knuth'un Dancing Links yöntemi Pentolings bölümlerini nasıl çözüp üretiyor; 63 duruştan tek çözümlü bulmacalara.",
        "intro": "Pentolings'teki her Döşe bölümü bir sözdür: bu şekli bu parçalarla doldurmanın bir yolu var. Bu sözü 150 bölümde tutmak ve istediğin an sana ipucu verebilmek için oyunun içinde Donald Knuth'un Dancing Links yöntemine dayanan küçük bir çözücü var. Herkesin izleyebileceği küçük bir örnekle nasıl çalıştığını anlatıyoruz.",
        "sections": [
            {
                "h": "Pentomino bulmacası bir tam kapsama problemidir",
                "p": [
                    "Bir bölüme kurallar listesi olarak bak. Her parça tam bir kez kullanılmalı. Şeklin her karesi tam bir kez kaplanmalı. Hiçbir şey üst üste binmemeli ve hiçbir şey artmamalı. Böyle kurallardan oluşan probleme tam kapsama (exact cover) problemi denir ve Sudoku'dan çizelgelemeye kadar çok bulmaca tam olarak budur.",
                    "Bilgisayara çözdürmek için problemi bir tablo olarak yazarız. Her sütun bir kuraldır: her parça için bir sütun ve şeklin her karesi için bir sütun. Her satır olası bir hamledir: belirli bir parça, belirli bir yöne çevrilmiş, belirli bir yere konmuş. Satır, sağladığı sütunları işaretler: parçanın kendi sütunu ve kaplayacağı beş kare. Satırları öyle seçersen ki her sütun tam bir kez işaretlenmiş olsun, bulmaca çözülmüştür."
                ]
            },
            {
                "h": "63 duruş: tablonun satırları",
                "p": [
                    "Bir pentomino döndürülüp ters çevrilebilir; bu yüzden oyun önce on iki parçanın her birinin bütün farklı duruşlarını listeler. Şekli döndürür, aynalar ve yalnızca gerçekten yeni olan sonuçları tutar. X 1 duruş, I 2 duruş, T, U, V, W ve Z dörder, F, L, N, P ve Y sekizer duruş verir. Bunlar takım için toplam 63 duruş eder ve kod bu sayıyı denetler.",
                    "Sonra bölümün şekli için her duruşu, beş karesinin de şeklin içinde kaldığı her yere kaydırır. Tüm on iki parçalı 3x20 dikdörtgen için bu 1236 aday satır eder. En büyük bölüm olan 6x10 dikdörtgen için 2056 satır vardır. Tabloda 72 sütun bulunur: 12 parça ve 60 kare."
                ]
            },
            {
                "h": "Küçük bir örnek",
                "p": [
                    "3x5'lik bir dikdörtgen ve P, U, V parçalarını al. Tabloda 3 parça sütunu ve 15 kare sütunu, yani toplam 18 sütun vardır. Parçaların sırasıyla 40, 20 ve 12 olası yerleşimi var; bu da 72 satır eder. Her sütunu tam bir kez işaretleyen üç satır seçince cevap çıkar: V sol ve alt kenarda, U sağda, P ortada. Yazıyla tahtanın üç satırı VPPUU, VPPPU ve VVVUU olarak okunur. Tüm dikdörtgeni döndürmek ya da aynalamak aynı cevabın dört sürümünü verir; yani çözücü, bir insana aynı görünen dört çözüm bulur."
                ]
            },
            {
                "h": "Knuth'un Dancing Links yöntemi, sade sözlerle",
                "p": [
                    "Arama, Algoritma X'tir. Henüz kaplanmamış bir sütun seç. Onu işaretleyen her satırı dene. Bir satırı seçmek, onun diğer sütunlarının artık alındığı anlamına gelir; bu yüzden onunla çakışan her satır atılabilir. Sonra küçülmüş tabloyla aynı işlemi tekrarla. Bir sütunda hiç satır kalmazsa daha önce yanlış seçim yapmışsındır; geri çekilip sıradaki satırı denersin.",
                    "Zekice olan, tablonun saklanış biçimidir. Donald Knuth, işaretleri bağlı listelerde tutabileceğini fark etti: her işaret sol, sağ, üst ve alt komşusunu gösterir. Bir satırı kaldırmak birkaç bağlantıyı yeniden yönlendirmekten ibarettir ve kaldırılan öğe yerini hatırlamaya devam eder; geri koymak adımları tersine yapmak demektir. Düğümler sanki dışarı fırlayıp geri giriyor gibi göründüğünden bu tekniğe Dancing Links (dans eden bağlantılar) adını verdi. Pentolings'te Dlx.kt yaklaşık seksen satırdır ve hız için düz tamsayı dizileriyle çalışır.",
                    "Bir numara daha: çözücü her adımda geriye en az satırı kalan sütunu seçer. Bir kare yalnızca iki yolla kaplanabiliyorsa arama, tabloda gezinmek yerine hemen bu ikisini dener. Bu, rehberde söylediğimizin bilgisayar sürümüdür: önce dar yerlerden başla."
                ]
            },
            {
                "h": "Kilitli parçalar ve adil bölümler",
                "p": [
                    "Bazı Pentolings bölümleri kilitli bir parçayla başlar. Bu parçalar gerçek bir çözümden gelir: üretici bir cevap bulur, sonra onun bir ya da iki parçasını dondurur. Çözücü onları zaten seçilmiş sayar, karelerini ve sütunlarını tablodan çıkarır ve geriye kalanı sayar.",
                    "Bölüm yapmak çözmekten fazlasıdır. Üretici, parçaları rastgele yan yana koyarak bir silüet oluşturur; böylece yapısı gereği bir çözüm vardır. Sonra çok sayıda silüeti puanlar: dolgun şekilleri ödüllendirir, delikleri cezalandırır, simetriyi ödüllendirir ve ilk bölümlerde daha çok cevabı olan şekilleri tercih eder. Bu yolla yapılan silüetlerin çoğunun tam bir çözümü olduğundan, zorluk esas olarak parça sayısı ve silüetin tuhaf biçiminden gelir. 150 bölümün her biri testlerde yeniden çözülür, tekrar var mı diye bakılır (döndürülmüş ya da aynalanmış kopya aynı sayılır) ve son bölüm olan 6x10 dikdörtgen, çok büyük sayıda cevabı olan tek yerdir. Bir test ayrıca 3x20 için klasik sayıyı doğrular: sekiz; bu, iki gerçek cevabın dikdörtgeni döndürme ya da aynalamanın dört yolu ile çarpımıdır."
                ]
            },
            {
                "h": "Neden her şeyi denemiyoruz?",
                "p": [
                    "Bir bulmacayı her parçayı her duruşta sırayla deneyerek ve sonunda kontrol ederek çözebilirsin. Bu, bilgisayar için bile işe yaramaz. On iki parça, 63 duruş ve onlarca yerle kombinasyon sayısı astronomiktir ve neredeyse hepsi ilk birkaç hamlede üst üste biner ya da boşluk bırakır.",
                    "Püf noktası, kötü bir dalın kötü olduğunu görür görmez durdurmaktır. Algoritma X tam olarak bunu yapar. Bir kareyi kaplayabilecek hiçbir parça kalmadığı anda arama daha derine gitmez ve geri çekilir. Dancing Links her geri çekilmeyi ucuzlatır. 2056 aday yerleşimli bir 6x10 tahtanın telefonda bile çabucak çözülmesinin ve ipucu düğmesinin sunucuya ihtiyaç duymamasının nedeni budur."
                ]
            },
            {
                "h": "Ne öğrendik",
                "p": [
                    "Aynı çözücü mantığı iki yerde var: 150 bölümlük paketi üreten ve denetleyen Python'da ve uygulamada yayına giden Kotlin'de. Kotlin testleri paketin her bölümünü sıfırdan yeniden çözer. İki bağımsız uygulama olması, birindeki hatanın ötekinden saklanmasını zorlaştırır.",
                    "En büyük sürpriz, rastgele bir silüetin birden fazla cevabının ne kadar nadir olduğuydu. Birçok bulmacanın birkaç çözümü olmasını bekliyorduk ve tersini bulduk. Bunun sorun olmadığı ortaya çıktı: oyuncular bir bölümün çözülebilir ve adil olmasını önemser, kaç çözümü olduğunu değil; bu yüzden oyun geçerli her doldurmayı kabul eder. Çözücünün bize verdiği, her bölümün ve her ipucunun güvenilebileceği sözüdür."
                ]
            },
            {
                "h": "İpuçları aynı çözücüden gelir",
                "p": [
                    "İpucu düğmesi çözücüye yeni bir soru sorar: şimdiye kadar yerleştirdiğin parçalar verilmişken geri kalanı nasıl sığar? Yerleştirdiğin parçaları sabit sayar, kalanı çözer ve bulduğu cevaptaki sıradaki parçayı parlatır. İpucunu izlersen bir sonraki, yeniden çözmeden bellekten gelebilir. İş arka planda, zaman sınırıyla çalışır; ekran hiç donmaz.",
                    "Yerleştirdiğin parçalar çözümü imkânsız kılıyorsa çözücü hiçbir şey bulamaz ve oyun bunu söyler: buradan çözüm yok, bir parçayı geri al. Bu, ipucunu yalnızca takıldığında değil, emin olmadığında da işe yarar kılar. Oyun, şekli doldurmanın üreticinin bulduğu yolu değil, geçerli herhangi bir yolunu kabul eder; yani yazarın cevabını tahmin etmeye zorlanmazsın."
                ]
            }
        ],
        "faq": [
            [
                "Tam kapsama problemi nedir?",
                "Her öğenin tam bir kez, çakışmasız ve artansız kaplanması için bazı seçenekleri seçmen gereken problemdir. Pentomino bulmacası bunlardan biridir."
            ],
            [
                "Dancing Links nedir?",
                "Donald Knuth'un yayımladığı, bir arama tablosunu bağlı listelerde saklayarak geri izlemeli aramada satırların çok hızlı kaldırılıp geri konmasını sağlayan yöntemdir."
            ],
            [
                "Parçaların neden 63 duruşu var?",
                "12 parçanın her biri döndürülüp ters çevrilebilir ve bu duruşlardan bazıları aynı görünür. Yalnızca farklı olanları sayınca takım için 63 çıkar."
            ],
            [
                "Oyunda her bölümün tek bir doğru cevabı mı var?",
                "Hayır. Oyun, bölümün üretildiği cevaptan farklı olsa bile şekli dolduran geçerli her yolu kabul eder."
            ]
        ]
    },
    "es": {
        "slug": "puzles-de-pentominos-dancing-links-cobertura-exacta",
        "title": "Cómo creamos niveles de pentominós con Dancing Links",
        "desc": "Una historia de desarrollo: cómo la cobertura exacta y los Dancing Links de Knuth resuelven y generan niveles de Pentolings, de 63 posiciones a puzles únicos.",
        "intro": "Cada nivel de Encajar en Pentolings es una promesa: hay una manera de rellenar esta forma con estas piezas. Para cumplirla en 150 niveles, y para darte una pista en cualquier momento, el juego lleva dentro un pequeño resolutor basado en los Dancing Links de Donald Knuth. Aquí explicamos cómo funciona con un ejemplo diminuto que cualquiera puede seguir.",
        "sections": [
            {
                "h": "Un puzle de pentominós es un problema de cobertura exacta",
                "p": [
                    "Mira un nivel como una lista de reglas. Cada pieza debe usarse exactamente una vez. Cada cuadro de la forma debe cubrirse exactamente una vez. Nada puede solaparse y nada puede sobrar. Un problema formado por reglas así se llama problema de cobertura exacta, y muchos puzles resultan ser justo eso, desde el sudoku hasta la planificación de horarios.",
                    "Para que un ordenador lo resuelva, escribimos el problema como una tabla. Cada columna es una regla: una columna por cada pieza y una columna por cada cuadro de la forma. Cada fila es una jugada posible: una pieza concreta, girada de una manera concreta y colocada en un lugar concreto. La fila marca las columnas que cumple: la columna de la propia pieza y los cinco cuadros que cubriría. El puzle está resuelto cuando eliges filas de modo que cada columna quede marcada exactamente una vez."
                ]
            },
            {
                "h": "63 posiciones: las filas de la tabla",
                "p": [
                    "Un pentominó se puede girar y voltear, así que primero el juego lista todas las posiciones distintas de cada una de las doce piezas. Gira y refleja la forma y conserva solo los resultados realmente nuevos. La X da 1 posición, la I da 2, la T, la U, la V, la W y la Z dan 4 cada una, y la F, la L, la N, la P y la Y dan 8 cada una. Eso suma 63 posiciones para todo el conjunto, una cifra que el código comprueba.",
                    "Después, para la forma del nivel, desliza cada posición a todos los lugares en que los cinco cuadros quedan dentro de la forma. Para un rectángulo de 3x20 con las doce piezas, eso da 1236 filas candidatas. Para el nivel más grande, un rectángulo de 6x10, hay 2056. La tabla tiene 72 columnas: 12 piezas más 60 cuadros."
                ]
            },
            {
                "h": "Un ejemplo diminuto",
                "p": [
                    "Toma un rectángulo de 3x5 y las piezas P, U y V. La tabla tiene 3 columnas de pieza y 15 de cuadro, o sea 18 columnas en total. Las piezas tienen 40, 20 y 12 colocaciones posibles, lo que da 72 filas. Al elegir tres filas que marquen cada columna exactamente una vez sale la respuesta: la V en el borde izquierdo e inferior, la U a la derecha y la P en el centro. En texto, las tres filas del tablero se leen VPPUU, VPPPU y VVVUU. Girar o reflejar todo el rectángulo da cuatro versiones de la misma respuesta, así que el resolutor encuentra cuatro soluciones que a una persona le parecen la misma."
                ]
            },
            {
                "h": "Los Dancing Links de Knuth, en palabras sencillas",
                "p": [
                    "La búsqueda es el Algoritmo X. Elige una columna que aún no esté cubierta. Prueba cada fila que la marca. Elegir una fila significa que sus otras columnas ya están ocupadas, así que se puede descartar toda fila que choque con ella. Luego se repite con la tabla más pequeña. Si alguna columna se queda sin filas, es que antes elegiste mal, así que retrocedes y pruebas la siguiente fila.",
                    "Lo ingenioso es cómo se guarda la tabla. Donald Knuth observó que las marcas se pueden guardar en listas enlazadas, donde cada marca apunta a su vecina de la izquierda, la derecha, arriba y abajo. Quitar una fila consiste en redirigir unos pocos enlaces, y el elemento quitado sigue recordando dónde estaba, de modo que devolverlo es deshacer los pasos al revés. Como los nodos parecen saltar fuera y volver a entrar, llamó a la técnica Dancing Links, enlaces que bailan. En Pentolings, Dlx.kt tiene unas ochenta líneas y trabaja con matrices de enteros simples para ir rápido.",
                    "Un truco más: en cada paso el resolutor elige la columna con menos filas restantes. Si un cuadro solo se puede cubrir de dos maneras, la búsqueda prueba enseguida esas dos en lugar de vagar por la tabla. Es la versión informática de lo que dijimos en la guía: empieza por los sitios estrechos."
                ]
            },
            {
                "h": "Piezas con candado y niveles justos",
                "p": [
                    "Algunos niveles de Pentolings empiezan con una pieza con candado. Esas piezas salen de una solución real: el generador encuentra una respuesta y después congela una o dos de sus piezas. El resolutor las trata como ya elegidas, retira sus cuadros y columnas de la tabla y cuenta lo que queda.",
                    "Hacer un nivel es más que resolver. Un generador construye un contorno colocando las piezas junto a otras al azar, así que por construcción existe una solución. Después puntúa muchos contornos: premia las formas compactas, penaliza los agujeros, premia la simetría y prefiere formas con más respuestas en los primeros niveles. Como los contornos hechos así suelen tener exactamente una solución, la dificultad viene sobre todo del número de piezas y de lo extraño del contorno. Cada uno de los 150 niveles se vuelve a resolver en las pruebas, se comprueba que no haya duplicados (una copia girada o reflejada cuenta como la misma) y el último nivel, un rectángulo de 6x10, es el único lugar con una cantidad enorme de respuestas. Una prueba también confirma la cifra clásica para 3x20: ocho, que son las dos respuestas verdaderas por las cuatro maneras de girar o reflejar el rectángulo."
                ]
            },
            {
                "h": "¿Por qué no probar todo sin más?",
                "p": [
                    "Podrías resolver un puzle probando cada pieza en cada posición, una tras otra, y comprobando al final. Eso no funciona, ni siquiera para un ordenador. Con doce piezas, 63 posiciones y decenas de lugares, el número de combinaciones es astronómico, y casi todas se solapan o dejan huecos en las primeras jugadas.",
                    "El truco es detener una rama mala en cuanto se ve que es mala. El Algoritmo X hace exactamente eso. En el momento en que un cuadro se queda sin ninguna pieza que pueda cubrirlo, la búsqueda deja de profundizar y retrocede. Los Dancing Links hacen que cada retroceso salga barato. Por eso un tablero de 6x10, con 2056 colocaciones candidatas, se resuelve deprisa incluso en un teléfono, y por eso el botón de pista no necesita un servidor."
                ]
            },
            {
                "h": "Lo que aprendimos",
                "p": [
                    "La misma lógica del resolutor existe dos veces: en Python, donde el generador construye y comprueba el paquete de 150 niveles, y en Kotlin, que va en la aplicación. Las pruebas de Kotlin vuelven a resolver desde cero cada nivel del paquete. Con dos implementaciones independientes, es poco probable que un error en una se esconda de la otra.",
                    "La mayor sorpresa fue lo raro que es que un contorno aleatorio tenga más de una respuesta. Esperábamos que muchos puzles tuvieran varias soluciones y encontramos lo contrario. Resulta que no pasa nada: a los jugadores les importa que un nivel sea resoluble y justo, no cuántas soluciones tiene, así que el juego acepta cualquier relleno válido. Lo que nos da el resolutor es la promesa de que se puede confiar en cada nivel y en cada pista."
                ]
            },
            {
                "h": "Las pistas salen del mismo resolutor",
                "p": [
                    "El botón Pista le hace al resolutor una pregunta nueva: dadas las piezas que ya colocaste, ¿cómo encaja el resto? Trata tus piezas colocadas como fijas, resuelve lo que falta e ilumina la siguiente pieza de la respuesta que encuentra. Si sigues la pista, la siguiente puede salir de la memoria sin volver a resolver. El trabajo se hace en segundo plano con un límite de tiempo para que la pantalla nunca se congele.",
                    "Si tus piezas colocadas hacen imposible una solución, el resolutor no encuentra nada y el juego te lo dice: no hay solución desde aquí, quita una pieza. Así la pista sirve incluso cuando no estás atascado, solo inseguro. Y el juego acepta cualquier manera válida de rellenar la forma, no solo la que halló el generador, de modo que nunca tienes que adivinar la respuesta del autor."
                ]
            }
        ],
        "faq": [
            [
                "¿Qué es un problema de cobertura exacta?",
                "Un problema en el que hay que elegir opciones para que cada elemento quede cubierto exactamente una vez, sin solapamientos ni sobrantes. Un puzle de pentominós lo es."
            ],
            [
                "¿Qué son los Dancing Links?",
                "Un método publicado por Donald Knuth para guardar una tabla de búsqueda en listas enlazadas, de modo que las filas se puedan quitar y restaurar muy deprisa durante una búsqueda con retroceso."
            ],
            [
                "¿Por qué las piezas tienen 63 posiciones?",
                "Cada una de las 12 piezas se puede girar y voltear, y algunas de esas posiciones se ven iguales. Contando solo las distintas salen 63 en todo el conjunto."
            ],
            [
                "¿El juego tiene una sola respuesta correcta por nivel?",
                "No. El juego acepta cualquier manera válida de rellenar la forma, aunque sea distinta de aquella con la que se creó el nivel."
            ]
        ]
    },
    "pt": {
        "slug": "quebra-cabecas-de-pentominos-dancing-links-cobertura-exata",
        "title": "Como criamos níveis de pentominós com Dancing Links",
        "desc": "Uma história de desenvolvimento: como a cobertura exata e os Dancing Links de Knuth resolvem e geram níveis do Pentolings, de 63 posições a desafios únicos.",
        "intro": "Cada nível de Encaixar no Pentolings é uma promessa: existe um jeito de preencher esta forma com estas peças. Para cumpri-la em 150 níveis, e para dar uma dica a qualquer momento, o jogo traz dentro um pequeno resolvedor baseado nos Dancing Links de Donald Knuth. Aqui explicamos como ele funciona com um exemplo minúsculo que qualquer pessoa consegue acompanhar.",
        "sections": [
            {
                "h": "Um quebra-cabeça de pentominós é um problema de cobertura exata",
                "p": [
                    "Veja um nível como uma lista de regras. Cada peça precisa ser usada exatamente uma vez. Cada quadrado da forma precisa ser coberto exatamente uma vez. Nada pode se sobrepor e nada pode sobrar. Um problema feito de regras assim se chama problema de cobertura exata, e muitos quebra-cabeças acabam sendo exatamente isso, do sudoku ao planejamento de horários.",
                    "Para que um computador o resolva, escrevemos o problema como uma tabela. Cada coluna é uma regra: uma coluna para cada peça e uma coluna para cada quadrado da forma. Cada linha é uma jogada possível: uma peça específica, girada de um jeito específico e colocada em um lugar específico. A linha marca as colunas que cumpre: a coluna da própria peça e os cinco quadrados que ela cobriria. O quebra-cabeça está resolvido quando você escolhe linhas de modo que cada coluna seja marcada exatamente uma vez."
                ]
            },
            {
                "h": "63 posições: as linhas da tabela",
                "p": [
                    "Um pentominó pode ser girado e virado, então primeiro o jogo lista todas as posições diferentes de cada uma das doze peças. Ele gira e espelha a forma e guarda apenas os resultados realmente novos. O X dá 1 posição, o I dá 2, o T, o U, o V, o W e o Z dão 4 cada, e o F, o L, o N, o P e o Y dão 8 cada. Isso soma 63 posições para o conjunto todo, um número que o código confere.",
                    "Depois, para a forma do nível, ele desliza cada posição para todos os lugares em que os cinco quadrados ficam dentro da forma. Para um retângulo 3x20 com as doze peças, isso dá 1236 linhas candidatas. Para o maior nível, um retângulo 6x10, são 2056. A tabela tem 72 colunas: 12 peças mais 60 quadrados."
                ]
            },
            {
                "h": "Um exemplo minúsculo",
                "p": [
                    "Pegue um retângulo 3x5 e as peças P, U e V. A tabela tem 3 colunas de peça e 15 de quadrado, ou seja, 18 colunas ao todo. As peças têm 40, 20 e 12 colocações possíveis, o que dá 72 linhas. Ao escolher três linhas que marquem cada coluna exatamente uma vez, aparece a resposta: o V nas bordas esquerda e inferior, o U à direita e o P no meio. Em texto, as três linhas do tabuleiro ficam VPPUU, VPPPU e VVVUU. Girar ou espelhar o retângulo inteiro dá quatro versões da mesma resposta, então o resolvedor encontra quatro soluções que parecem a mesma para uma pessoa."
                ]
            },
            {
                "h": "Os Dancing Links de Knuth, em palavras simples",
                "p": [
                    "A busca é o Algoritmo X. Escolha uma coluna que ainda não foi coberta. Experimente cada linha que a marca. Escolher uma linha significa que as outras colunas dela já foram usadas, então toda linha que conflita com ela pode ser descartada. Depois, repete-se com a tabela menor. Se alguma coluna ficar sem linhas, você escolheu errado antes, então volta e tenta a próxima linha.",
                    "O truque inteligente é como a tabela é guardada. Donald Knuth percebeu que as marcas podem ficar em listas encadeadas, em que cada marca aponta para a vizinha da esquerda, da direita, de cima e de baixo. Remover uma linha é apenas redirecionar alguns elos, e o item removido continua lembrando onde estava, então recolocá-lo é refazer os passos ao contrário. Como os nós parecem sair e voltar, ele chamou a técnica de Dancing Links, elos dançantes. No Pentolings, o Dlx.kt tem cerca de oitenta linhas e trabalha com vetores de inteiros simples para ganhar velocidade.",
                    "Mais um truque: a cada passo o resolvedor escolhe a coluna com menos linhas restantes. Se um quadrado só pode ser coberto de duas maneiras, a busca testa logo essas duas em vez de vagar pela tabela. É a versão de computador do que dissemos no guia: comece pelos lugares apertados."
                ]
            },
            {
                "h": "Peças com cadeado e níveis justos",
                "p": [
                    "Alguns níveis do Pentolings começam com uma peça com cadeado. Essas peças vêm de uma solução real: o gerador encontra uma resposta e depois congela uma ou duas de suas peças. O resolvedor as trata como já escolhidas, retira seus quadrados e colunas da tabela e conta o que sobra.",
                    "Fazer um nível é mais do que resolver. Um gerador monta um contorno colocando as peças lado a lado ao acaso, então por construção existe uma solução. Depois ele pontua muitos contornos: premia formas compactas, penaliza buracos, premia simetria e prefere formas com mais respostas nos primeiros níveis. Como contornos feitos assim costumam ter exatamente uma solução, a dificuldade vem principalmente do número de peças e do formato estranho do contorno. Cada um dos 150 níveis é resolvido de novo nos testes, verifica-se que não há duplicados (uma cópia girada ou espelhada conta como a mesma) e o último nível, um retângulo 6x10, é o único lugar com uma quantidade enorme de respostas. Um teste também confirma o número clássico para 3x20: oito, que são as duas respostas verdadeiras vezes as quatro maneiras de girar ou espelhar o retângulo."
                ]
            },
            {
                "h": "Por que não tentar tudo de uma vez?",
                "p": [
                    "Você poderia resolver um quebra-cabeça testando cada peça em cada posição, uma após a outra, e conferindo no final. Isso não funciona, nem para um computador. Com doze peças, 63 posições e dezenas de lugares, o número de combinações é astronômico, e quase todas se sobrepõem ou deixam vãos nas primeiras jogadas.",
                    "O truque é parar um ramo ruim assim que se vê que ele é ruim. O Algoritmo X faz exatamente isso. No momento em que um quadrado fica sem nenhuma peça que possa cobri-lo, a busca deixa de aprofundar e volta. Os Dancing Links tornam cada volta barata. É por isso que um tabuleiro 6x10, com 2056 colocações candidatas, é resolvido rápido até em um celular, e é por isso que o botão de dica não precisa de servidor."
                ]
            },
            {
                "h": "O que aprendemos",
                "p": [
                    "A mesma lógica do resolvedor existe duas vezes: em Python, onde o gerador monta e confere o pacote de 150 níveis, e em Kotlin, que vai no aplicativo. Os testes em Kotlin resolvem de novo, do zero, cada nível do pacote. Com duas implementações independentes, é pouco provável que um erro em uma se esconda da outra.",
                    "A maior surpresa foi como é raro um contorno aleatório ter mais de uma resposta. Esperávamos que muitos desafios tivessem várias soluções e encontramos o contrário. Acontece que isso não é problema: os jogadores se importam que um nível seja resolvível e justo, não quantas soluções ele tem, então o jogo aceita qualquer preenchimento válido. O que o resolvedor nos dá é a promessa de que cada nível e cada dica merecem confiança."
                ]
            },
            {
                "h": "As dicas saem do mesmo resolvedor",
                "p": [
                    "O botão Dica faz ao resolvedor uma pergunta nova: dadas as peças que você já colocou, como o resto se encaixa? Ele trata suas peças colocadas como fixas, resolve o que falta e destaca a próxima peça da resposta que encontrou. Se você seguir a dica, a próxima pode vir da memória sem resolver de novo. O trabalho roda em segundo plano com limite de tempo para a tela nunca travar.",
                    "Se as peças que você colocou tornam a solução impossível, o resolvedor não acha nada e o jogo avisa: sem solução daqui, retire uma peça. Assim a dica serve até quando você não está travado, apenas inseguro. E o jogo aceita qualquer jeito válido de preencher a forma, não só o que o gerador encontrou, então você nunca precisa adivinhar a resposta do autor."
                ]
            }
        ],
        "faq": [
            [
                "O que é um problema de cobertura exata?",
                "Um problema em que é preciso escolher opções para que cada item seja coberto exatamente uma vez, sem sobreposições nem sobras. Um quebra-cabeça de pentominós é um deles."
            ],
            [
                "O que são Dancing Links?",
                "Um método publicado por Donald Knuth para guardar uma tabela de busca em listas encadeadas, de modo que as linhas possam ser removidas e restauradas muito rápido em uma busca com retrocesso."
            ],
            [
                "Por que as peças têm 63 posições?",
                "Cada uma das 12 peças pode ser girada e virada, e algumas dessas posições ficam iguais. Contando só as diferentes, são 63 no conjunto todo."
            ],
            [
                "O jogo tem uma única resposta certa por nível?",
                "Não. O jogo aceita qualquer jeito válido de preencher a forma, mesmo que seja diferente daquele com que o nível foi criado."
            ]
        ]
    }
}
