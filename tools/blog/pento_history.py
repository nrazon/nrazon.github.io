# Blog: pentomino nedir, 12 parcanin hikayesi
POST = {"tags": ["history", "game-design"],
    "id": "pentomino-history",
    "app": "pentolings",
    "date": "2026-11-10",
    "en": {
        "slug": "pentominoes-history-golomb-twelve-pieces",
        "title": "Pentominoes: The Story of the 12 Pieces and Golomb",
        "desc": "What a pentomino is, how Solomon Golomb named and studied them in the 1950s, how Martin Gardner made them famous and why a 6x10 board has 2339 solutions.",
        "intro": "Take five squares and glue them edge to edge. You can do it in exactly twelve different ways, and those twelve shapes have kept mathematicians, puzzle makers and bored students busy for more than seventy years. This is the short story of the pentominoes.",
        "sections": [
            {
                "h": "What is a pentomino?",
                "p": [
                    "A pentomino is a flat shape made of five identical squares, where every square shares a full side with at least one other square. Two squares that only touch at a corner do not count as joined. If you turn a shape around or flip it over, it is still the same pentomino, and with that rule there are exactly 12 of them.",
                    "Shapes made of squares joined edge to edge have a general name: polyominoes. One square is a monomino, two squares are the familiar domino, three squares make a tromino (2 kinds), four make a tetromino (5 kinds), five a pentomino (12 kinds) and six a hexomino (35 kinds). The numbers grow quickly after that, which is why the pentominoes are a sweet spot: a small set, easy to hold in your head, but rich enough to make deep puzzles."
                ]
            },
            {
                "h": "Golomb and the invention of the word",
                "p": [
                    "The person who gave these shapes their name was Solomon W. Golomb, an American mathematician. In 1953 he gave a talk at the Harvard Mathematics Club about the shapes you can build from squares, and he called them polyominoes. The word is a joke on the word domino. Golomb read the start of the word domino as if it were the prefix di-, meaning two, and swapped in other number prefixes: tromino, tetromino, pentomino and so on.",
                    "The first full paper on the subject, Checker Boards and Polyominoes, appeared in the American Mathematical Monthly in 1954. In it Golomb asked questions that sound like games. Can you cover a chessboard with certain polyominoes? Which shapes can fill a rectangle? Years later he collected the ideas in a book called Polyominoes (1965), which remains a classic introduction."
                ]
            },
            {
                "h": "The twelve letters",
                "p": [
                    "The twelve pentominoes are known by the letters they look like: F, I, L, N, P, T, U, V, W, X, Y and Z. The set in alphabetical order is FILNPTUVWXYZ, and that is also the order the pieces are listed in the Pentolings app. The letters are shorthand: I is a straight line of five squares, X is a plus, V is a corner with two arms of three, and so on.",
                    "Some letters hide interesting facts. X is the only pentomino that looks the same in every direction you turn it, so it has just one position on a grid. I has two, because it can lie flat or stand up. T, U, V, W and Z have four positions each, and the remaining five (F, L, N, P and Y) have eight, because flipping them over gives new positions. Add them all and you get 63 positions in total. If you do not allow flipping, there are 18 different pieces, because six of the twelve (F, L, N, P, Y and Z) come in two mirror versions."
                ]
            },
            {
                "h": "Martin Gardner and the 1957 spark",
                "p": [
                    "Polyominoes would have stayed a corner of mathematics if Martin Gardner had not noticed them. Gardner wrote the Mathematical Games column in Scientific American, and in 1957 he introduced pentominoes to a wide audience there. Readers loved them. They were simple enough to cut out of paper, and the puzzles that came with them were hard enough to keep people busy for weeks.",
                    "That column helped start a long habit. Puzzle makers began selling sets of the twelve pieces, and the shapes kept turning up in later puzzles and games. Golomb himself went on to write more about polyominoes and other recreational mathematics, and the term he coined in 1953 is the one everybody still uses."
                ]
            },
            {
                "h": "The rectangle puzzles: 2339 ways to fill 6x10",
                "p": [
                    "The classic pentomino challenge is this: put all twelve pieces, each used once, into a rectangle with no gaps. The twelve pieces cover 60 squares, so the rectangle must have area 60. Four shapes are possible: 6x10, 5x12, 4x15 and 3x20. The number of different answers shrinks as the rectangle gets thinner. If we count answers that differ only by turning or mirroring the whole rectangle as one, the numbers are:",
                    "6x10: 2339 solutions. 5x12: 1010. 4x15: 368. 3x20: only 2. These counts were found by exhaustive computer searches, and they make a good sanity check for any pentomino solver. In Pentolings, the last level of the Fit mode is a 6x10 rectangle with the full set, so you are solving a puzzle that has thousands of valid answers in front of you, and the game accepts any one of them."
                ]
            },
            {
                "h": "Beyond five: bigger and smaller families",
                "p": [
                    "The pentominoes are one member of a whole family, and the numbers show why five squares is such a comfortable size. With one turn-and-flip counted as the same shape, there is 1 monomino, 1 domino, 2 trominoes, 5 tetrominoes and 12 pentominoes. Then the count jumps to 35 hexominoes and 108 heptominoes. Past that, nobody can keep the whole set in their head, and the puzzles lose their friendly feel.",
                    "Each size has its own character. Tetrominoes are so few that you can learn them in a minute, but they cannot make interesting rectangle puzzles on their own. Hexominoes need a book to learn. Pentominoes sit in the middle: you can learn all twelve in an afternoon, and you can still spend years on them."
                ]
            },
            {
                "h": "Try it with paper",
                "p": [
                    "You do not need an app to meet the pentominoes. Draw a grid on squared paper, cut out the twelve shapes using the letters as your guide, and try to build a 6x10 rectangle. Beginners often start with the easier 3x20 rectangle in mind and give up, because it has only two true answers and is the hardest of the four. Start with 6x10 or 5x12 instead, where there is more than one way to go right.",
                    "A good first goal is to place the X, which is the only piece that looks the same all round, then the long I, and then work on the pieces that hug the edges. If you get stuck, keep one shape you cannot place and try the others in its absence, because the last two or three pieces usually fall into place together."
                ]
            },
            {
                "h": "Why they make such good puzzles",
                "p": [
                    "Pentominoes sit at a sweet spot. With 12 pieces you can still remember every shape and its name. With 63 positions every piece can face almost any direction, so the puzzles stay flexible. And the idea is easy to explain: fill the shape, no gaps. Beginners can solve small shapes with three or four pieces, and experts can spend an evening on a single 5x12 rectangle.",
                    "That was the reason we built Pentolings around them: a cheerful tile-fitting mode with 150 levels, plus a second mode where the same pieces fall from above and you pop colors. If you want to meet the twelve pieces gradually, the early levels use only three pieces at a time, and each new world adds one more."
                ]
            }
        ],
        "faq": [
            [
                "Who invented the pentominoes?",
                "Solomon W. Golomb named and studied them. He introduced the idea of polyominoes in 1953 and published a paper about them in 1954. The shapes themselves are simple enough that people had probably played with them before."
            ],
            [
                "How many pentominoes are there?",
                "There are exactly 12 if you allow turning and flipping. If you do not allow flipping, there are 18."
            ],
            [
                "How many ways can you fill a 6x10 rectangle with all 12 pieces?",
                "2339, when answers that differ only by turning or mirroring the whole rectangle are counted as one."
            ],
            [
                "Why are they named after letters?",
                "Each of the 12 shapes looks like a letter: F, I, L, N, P, T, U, V, W, X, Y and Z, so the letters became their names."
            ]
        ]
    },
    "tr": {
        "slug": "pentomino-tarihi-golomb-12-parca",
        "title": "Pentominolar: 12 Parçanın ve Golomb'un Hikâyesi",
        "desc": "Pentomino nedir, Solomon Golomb onları 1950'lerde nasıl adlandırıp inceledi, Martin Gardner nasıl ünlü etti ve 6x10 tahtanın neden 2339 çözümü var.",
        "intro": "Beş kareyi kenarlarından yapıştır. Bunu tam on iki farklı biçimde yapabilirsin ve bu on iki şekil yetmiş yılı aşkın süredir matematikçileri, bulmaca yapımcılarını ve canı sıkılan öğrencileri meşgul ediyor. İşte pentominoların kısa hikâyesi.",
        "sections": [
            {
                "h": "Pentomino nedir?",
                "p": [
                    "Pentomino, her karenin en az bir başka kareyle tam bir kenarı paylaştığı, beş özdeş kareden oluşan düz bir şekildir. Yalnızca köşeden değen iki kare birleşik sayılmaz. Bir şekli döndürürsen ya da ters çevirirsen yine aynı pentomino sayılır ve bu kuralla tam 12 tane vardır.",
                    "Karelerin kenarlarından birleşmesiyle oluşan şekillerin genel adı poliomino'dur. Bir kare monomino, iki kare tanıdık domino, üç kare tromino (2 çeşit), dört kare tetromino (5 çeşit), beş kare pentomino (12 çeşit), altı kare heksomino'dur (35 çeşit). Sayılar bundan sonra hızla büyür; pentominoları tatlı bir nokta yapan da budur: aklında tutabileceğin küçük bir takım, ama derin bulmacalar çıkaracak kadar zengin."
                ]
            },
            {
                "h": "Golomb ve sözcüğün icadı",
                "p": [
                    "Bu şekillere adını veren kişi Amerikalı matematikçi Solomon W. Golomb'dur. 1953'te Harvard Matematik Kulübü'nde karelerden kurulabilen şekiller üzerine bir konuşma yaptı ve onlara poliomino dedi. Sözcük, domino sözcüğüne yapılmış bir şakadır. Golomb, domino sözcüğünün başını sanki iki anlamına gelen di- öneki gibi okudu ve yerine başka sayı önekleri koydu: tromino, tetromino, pentomino ve devamı.",
                    "Konuyla ilgili ilk kapsamlı makale, Checker Boards and Polyominoes, 1954'te American Mathematical Monthly dergisinde yayımlandı. Golomb orada oyun gibi duyulan sorular sordu. Bir satranç tahtasını belirli polyominolarla kaplayabilir misin? Hangi şekiller bir dikdörtgeni doldurur? Yıllar sonra fikirlerini Polyominoes (1965) adlı bir kitapta topladı; bu kitap hâlâ klasik bir giriş kaynağıdır."
                ]
            },
            {
                "h": "On iki harf",
                "p": [
                    "On iki pentomino benzedikleri harflerle bilinir: F, I, L, N, P, T, U, V, W, X, Y ve Z. Alfabe sırasıyla takım FILNPTUVWXYZ'dir ve Pentolings uygulamasında parçalar da bu sırayla listelenir. Harfler bir kısaltmadır: I beş karelik düz çizgidir, X artıdır, V üçer karelik iki kolu olan bir köşedir ve böyle gider.",
                    "Bazı harfler ilginç gerçekler saklar. X, hangi yöne çevirirsen çevir aynı görünen tek pentominodur; bu yüzden ızgarada yalnızca bir duruşu vardır. I'nın iki duruşu vardır; yatabilir ya da dikilebilir. T, U, V, W ve Z'nin dörder duruşu, kalan beşinin (F, L, N, P ve Y) ise sekizer duruşu vardır; çünkü onları ters çevirmek yeni duruşlar verir. Hepsini toplarsan toplam 63 duruş çıkar. Ters çevirmeye izin vermezsen 18 farklı parça olur; çünkü on ikinin altısı (F, L, N, P, Y ve Z) iki ayna biçiminde gelir."
                ]
            },
            {
                "h": "Martin Gardner ve 1957 kıvılcımı",
                "p": [
                    "Martin Gardner fark etmeseydi poliominolar matematiğin bir köşesinde kalabilirdi. Gardner, Scientific American dergisinde Mathematical Games köşesini yazıyordu ve 1957'de pentominoları orada geniş bir kitleyle tanıştırdı. Okurlar bayıldı. Kâğıttan kesmek için yeterince basitti, beraberinde gelen bulmacalar ise insanları haftalarca meşgul edecek kadar zordu.",
                    "O yazı uzun bir alışkanlığın başlamasına yardım etti. Bulmaca üreticileri on iki parçalık takımlar satmaya başladı ve şekiller sonraki bulmaca ve oyunlarda tekrar tekrar karşımıza çıktı. Golomb ise poliominolar ve eğlence matematiği üzerine yazmayı sürdürdü; 1953'te ortaya attığı terim hâlâ herkesin kullandığı terimdir."
                ]
            },
            {
                "h": "Dikdörtgen bulmacaları: 6x10'u doldurmanın 2339 yolu",
                "p": [
                    "Klasik pentomino meydan okuması şudur: on iki parçanın hepsini, her birini bir kez kullanarak boşluksuz bir dikdörtgene yerleştir. On iki parça 60 kareyi kapladığından dikdörtgenin alanı 60 olmalıdır. Dört şekil mümkündür: 6x10, 5x12, 4x15 ve 3x20. Dikdörtgen inceldikçe farklı çözüm sayısı azalır. Tüm dikdörtgeni döndürmek ya da aynalamakla birbirinden ayrılan çözümleri bir sayarsak sayılar şöyledir:",
                    "6x10: 2339 çözüm. 5x12: 1010. 4x15: 368. 3x20: yalnızca 2. Bu sayılar bilgisayarla yapılan kapsamlı taramalarla bulundu ve herhangi bir pentomino çözücüsü için iyi bir sağlama oluşturur. Pentolings'te Döşe modunun son bölümü, tam takımla 6x10'luk bir dikdörtgendir; yani binlerce geçerli cevabı olan bir bulmacayı çözüyorsun ve oyun bunlardan herhangi birini kabul ediyor."
                ]
            },
            {
                "h": "Beşin ötesi: daha büyük ve daha küçük aileler",
                "p": [
                    "Pentominolar koca bir ailenin üyelerinden biridir ve sayılar beş karenin neden bu kadar rahat bir boyut olduğunu gösterir. Döndürülüp çevrilmiş bir şekil aynı sayıldığında 1 monomino, 1 domino, 2 tromino, 5 tetromino ve 12 pentomino vardır. Sonra sayı 35 heksomino ve 108 heptomino'ya sıçrar. Bundan sonrasında kimse tüm takımı aklında tutamaz ve bulmacalar dostça havasını kaybeder.",
                    "Her boyutun kendi karakteri var. Tetrominolar o kadar azdır ki bir dakikada öğrenilir, ama tek başlarına ilginç dikdörtgen bulmacaları kuramazlar. Heksominoları öğrenmek için kitap gerekir. Pentominolar ortadadır: on ikisini bir öğleden sonra öğrenebilirsin ve yine de yıllarını onlara verebilirsin."
                ]
            },
            {
                "h": "Kâğıtla dene",
                "p": [
                    "Pentominolarla tanışmak için uygulama gerekmez. Kareli kâğıda bir ızgara çiz, on iki şekli harfleri rehber alarak kes ve 6x10'luk bir dikdörtgen kurmayı dene. Yeni başlayanlar genellikle daha kolay sanıp 3x20'lik dikdörtgenle başlar ve vazgeçer; çünkü yalnızca iki gerçek cevabı vardır ve dördünün en zorudur. Bunun yerine, doğru gitmenin birden fazla yolu olan 6x10 ya da 5x12 ile başla.",
                    "İyi bir ilk hedef, her yönden aynı görünen tek parça olan X'i yerleştirmek, sonra uzun I'yı koymak ve ardından kenarları saran parçalarla uğraşmaktır. Takılırsan yerleştiremediğin bir şekli ayrı tut ve diğerlerini o olmadan dene; çünkü son iki üç parça genellikle birlikte yerine oturur."
                ]
            },
            {
                "h": "Neden bu kadar iyi bulmaca oluyorlar",
                "p": [
                    "Pentominolar tatlı bir noktada durur. 12 parçayla her şekli ve adını hâlâ aklında tutabilirsin. 63 duruşla her parça hemen her yöne bakabilir, bu yüzden bulmacalar esnek kalır. Ve fikir anlatması kolaydır: şekli boşluksuz doldur. Yeni başlayanlar üç dört parçalık küçük şekilleri çözebilir, uzmanlar tek bir 5x12 dikdörtgene bir akşam harcayabilir.",
                    "Pentolings'i onların etrafında kurmamızın nedeni de bu: 150 bölümlü neşeli bir şekil yerleştirme modu ve aynı parçaların yukarıdan düştüğü, renk patlattığın ikinci bir mod. On iki parçayla yavaş yavaş tanışmak istersen ilk bölümler aynı anda yalnızca üç parça kullanır ve her yeni dünya bir parça ekler."
                ]
            }
        ],
        "faq": [
            [
                "Pentominoları kim icat etti?",
                "Onları adlandıran ve inceleyen kişi Solomon W. Golomb'dur. Poliomino fikrini 1953'te ortaya attı ve 1954'te bu konuda bir makale yayımladı. Şekiller o kadar basittir ki insanlar muhtemelen daha önce de onlarla oynamıştı."
            ],
            [
                "Kaç pentomino vardır?",
                "Döndürmeye ve ters çevirmeye izin verirsen tam 12, ters çevirmeye izin vermezsen 18 tane vardır."
            ],
            [
                "6x10'luk dikdörtgen 12 parçayla kaç farklı biçimde doldurulur?",
                "Tüm dikdörtgeni döndürmek ya da aynalamakla birbirinden ayrılan çözümler bir sayıldığında 2339."
            ],
            [
                "Neden harflerle adlandırılmışlar?",
                "12 şeklin her biri bir harfe benzer: F, I, L, N, P, T, U, V, W, X, Y ve Z; harfler de adları oldu."
            ]
        ]
    },
    "es": {
        "slug": "historia-de-los-pentominos-golomb-doce-piezas",
        "title": "Pentominós: la historia de las 12 piezas y de Golomb",
        "desc": "Qué es un pentominó, cómo Solomon Golomb los nombró y estudió en los años 50, cómo Martin Gardner los hizo famosos y por qué un 6x10 tiene 2339 soluciones.",
        "intro": "Toma cinco cuadrados y pégalos por los lados. Puedes hacerlo exactamente de doce maneras distintas, y esas doce formas llevan más de setenta años entreteniendo a matemáticos, fabricantes de puzles y estudiantes aburridos. Esta es la breve historia de los pentominós.",
        "sections": [
            {
                "h": "¿Qué es un pentominó?",
                "p": [
                    "Un pentominó es una forma plana hecha de cinco cuadrados idénticos, en la que cada cuadrado comparte un lado completo con al menos otro cuadrado. Dos cuadrados que solo se tocan por una esquina no cuentan como unidos. Si giras una forma o le das la vuelta, sigue siendo el mismo pentominó, y con esa regla hay exactamente 12.",
                    "Las formas hechas de cuadrados unidos por los lados tienen un nombre general: poliominós. Un cuadrado es un monominó, dos cuadrados son el conocido dominó, tres forman un triominó (2 tipos), cuatro un tetraminó (5 tipos), cinco un pentominó (12 tipos) y seis un hexominó (35 tipos). Los números crecen muy deprisa después, y por eso los pentominós son un punto dulce: un conjunto pequeño, fácil de tener en la cabeza, pero lo bastante rico para crear puzles profundos."
                ]
            },
            {
                "h": "Golomb y la invención de la palabra",
                "p": [
                    "La persona que dio nombre a estas formas fue Solomon W. Golomb, un matemático estadounidense. En 1953 dio una charla en el Club de Matemáticas de Harvard sobre las formas que se pueden construir con cuadrados y las llamó poliominós. La palabra es un juego con dominó. Golomb leyó el comienzo de la palabra dominó como si fuera el prefijo di-, que significa dos, y puso en su lugar otros prefijos numéricos: triominó, tetraminó, pentominó y así sucesivamente.",
                    "El primer artículo completo sobre el tema, Checker Boards and Polyominoes, apareció en la revista American Mathematical Monthly en 1954. En él, Golomb planteaba preguntas que suenan a juegos. ¿Se puede cubrir un tablero de ajedrez con ciertos poliominós? ¿Qué formas llenan un rectángulo? Años después recogió sus ideas en el libro Polyominoes (1965), que sigue siendo una introducción clásica."
                ]
            },
            {
                "h": "Las doce letras",
                "p": [
                    "Los doce pentominós se conocen por las letras a las que se parecen: F, I, L, N, P, T, U, V, W, X, Y y Z. El conjunto en orden alfabético es FILNPTUVWXYZ, y ese es también el orden en que se listan las piezas en la aplicación Pentolings. Las letras son una abreviatura: la I es una línea recta de cinco cuadrados, la X es un más, la V es una esquina con dos brazos de tres, y así sucesivamente.",
                    "Algunas letras esconden datos interesantes. La X es el único pentominó que se ve igual al girarlo en cualquier dirección, así que solo tiene una posición en la cuadrícula. La I tiene dos, porque puede estar tumbada o de pie. La T, la U, la V, la W y la Z tienen cuatro posiciones cada una, y las otras cinco (F, L, N, P e Y) tienen ocho, porque al darles la vuelta aparecen posiciones nuevas. Si las sumas todas, obtienes 63 posiciones. Si no permites voltear, hay 18 piezas distintas, porque seis de las doce (F, L, N, P, Y y Z) vienen en dos versiones simétricas."
                ]
            },
            {
                "h": "Martin Gardner y la chispa de 1957",
                "p": [
                    "Los poliominós habrían seguido siendo un rincón de las matemáticas si Martin Gardner no se hubiera fijado en ellos. Gardner escribía la columna Mathematical Games en Scientific American y en 1957 presentó los pentominós a un público amplio. A los lectores les encantaron. Eran lo bastante sencillos para recortarlos en papel, y los puzles que los acompañaban eran lo bastante difíciles para tener a la gente ocupada durante semanas.",
                    "Aquella columna ayudó a iniciar una larga costumbre. Los fabricantes de puzles empezaron a vender juegos con las doce piezas y las formas siguieron apareciendo en puzles y juegos posteriores. Golomb siguió escribiendo sobre poliominós y matemática recreativa, y el término que acuñó en 1953 es el que todavía usa todo el mundo."
                ]
            },
            {
                "h": "Los rectángulos: 2339 maneras de llenar un 6x10",
                "p": [
                    "El reto clásico de los pentominós es este: colocar las doce piezas, cada una una vez, en un rectángulo sin dejar huecos. Las doce piezas cubren 60 cuadrados, así que el rectángulo debe tener área 60. Son posibles cuatro formas: 6x10, 5x12, 4x15 y 3x20. El número de soluciones distintas se reduce a medida que el rectángulo se hace más delgado. Si contamos como una sola las soluciones que solo se diferencian por girar o reflejar todo el rectángulo, las cifras son:",
                    "6x10: 2339 soluciones. 5x12: 1010. 4x15: 368. 3x20: solo 2. Estas cifras se obtuvieron con búsquedas exhaustivas por ordenador y sirven como buena comprobación para cualquier resolutor de pentominós. En Pentolings, el último nivel del modo Encajar es un rectángulo de 6x10 con el conjunto completo, así que resuelves un puzle que tiene miles de respuestas válidas, y el juego acepta cualquiera de ellas."
                ]
            },
            {
                "h": "Más allá de cinco: familias mayores y menores",
                "p": [
                    "Los pentominós son un miembro de toda una familia, y los números muestran por qué cinco cuadrados es un tamaño tan cómodo. Contando como la misma forma las que se obtienen girando o volteando, hay 1 monominó, 1 dominó, 2 triominós, 5 tetraminós y 12 pentominós. Después la cifra salta a 35 hexominós y 108 heptominós. A partir de ahí, nadie puede tener el conjunto entero en la cabeza y los puzles pierden su carácter amable.",
                    "Cada tamaño tiene su carácter. Los tetraminós son tan pocos que se aprenden en un minuto, pero no sirven por sí solos para puzles de rectángulos interesantes. Los hexominós necesitan un libro para aprenderse. Los pentominós están en el medio: puedes aprender los doce en una tarde y aun así pasar años con ellos."
                ]
            },
            {
                "h": "Pruébalo con papel",
                "p": [
                    "No necesitas una aplicación para conocer los pentominós. Dibuja una cuadrícula en papel cuadriculado, recorta las doce formas guiándote por las letras e intenta construir un rectángulo de 6x10. Muchos principiantes empiezan por el rectángulo de 3x20 pensando que es más fácil y se rinden, porque solo tiene dos respuestas verdaderas y es el más difícil de los cuatro. Empieza mejor con 6x10 o 5x12, donde hay más de un camino correcto.",
                    "Un buen primer objetivo es colocar la X, la única pieza que se ve igual por todos lados, luego la I larga, y después trabajar con las piezas que abrazan los bordes. Si te atascas, deja aparte una forma que no puedas colocar y prueba las demás sin ella, porque las dos o tres últimas piezas suelen encajar juntas."
                ]
            },
            {
                "h": "Por qué son tan buenos puzles",
                "p": [
                    "Los pentominós están en un punto dulce. Con 12 piezas todavía puedes recordar cada forma y su nombre. Con 63 posiciones, cada pieza puede mirar casi en cualquier dirección, así que los puzles siguen siendo flexibles. Y la idea es fácil de explicar: llena la forma, sin huecos. Los principiantes pueden resolver formas pequeñas de tres o cuatro piezas, y los expertos pueden pasar una tarde con un solo rectángulo de 5x12.",
                    "Por eso construimos Pentolings en torno a ellos: un modo alegre de encajar piezas con 150 niveles, más un segundo modo en el que las mismas piezas caen desde arriba y haces explotar colores. Si quieres conocer las doce piezas poco a poco, los primeros niveles usan solo tres piezas a la vez y cada mundo nuevo añade una más."
                ]
            }
        ],
        "faq": [
            [
                "¿Quién inventó los pentominós?",
                "Solomon W. Golomb los nombró y los estudió. Presentó la idea de los poliominós en 1953 y publicó un artículo sobre ellos en 1954. Las formas son tan simples que probablemente la gente ya había jugado con ellas antes."
            ],
            [
                "¿Cuántos pentominós hay?",
                "Hay exactamente 12 si se permite girar y voltear. Si no se permite voltear, hay 18."
            ],
            [
                "¿De cuántas maneras se puede llenar un rectángulo de 6x10 con las 12 piezas?",
                "2339, contando como una sola las soluciones que solo se diferencian por girar o reflejar todo el rectángulo."
            ],
            [
                "¿Por qué tienen nombres de letras?",
                "Cada una de las 12 formas se parece a una letra: F, I, L, N, P, T, U, V, W, X, Y y Z, y las letras acabaron siendo sus nombres."
            ]
        ]
    },
    "pt": {
        "slug": "historia-dos-pentominos-golomb-doze-pecas",
        "title": "Pentominós: a história das 12 peças e de Golomb",
        "desc": "O que é um pentominó, como Solomon Golomb os batizou nos anos 1950, como Martin Gardner os tornou famosos e por que um 6x10 tem 2339 soluções.",
        "intro": "Pegue cinco quadrados e una-os pelos lados. Dá para fazer isso de exatamente doze maneiras diferentes, e essas doze formas ocupam matemáticos, fabricantes de quebra-cabeças e estudantes entediados há mais de setenta anos. Esta é a breve história dos pentominós.",
        "sections": [
            {
                "h": "O que é um pentominó?",
                "p": [
                    "Um pentominó é uma forma plana feita de cinco quadrados idênticos, em que cada quadrado divide um lado inteiro com pelo menos outro quadrado. Dois quadrados que só se tocam pelo canto não contam como unidos. Se você girar uma forma ou virá-la, ela continua sendo o mesmo pentominó, e com essa regra existem exatamente 12.",
                    "As formas feitas de quadrados unidos pelos lados têm um nome geral: poliminós. Um quadrado é um monominó, dois quadrados formam o conhecido dominó, três formam um triminó (2 tipos), quatro um tetraminó (5 tipos), cinco um pentominó (12 tipos) e seis um hexaminó (35 tipos). Os números crescem muito rápido depois disso, e é por isso que os pentominós são um ponto ideal: um conjunto pequeno, fácil de guardar na cabeça, mas rico o bastante para criar quebra-cabeças profundos."
                ]
            },
            {
                "h": "Golomb e a invenção da palavra",
                "p": [
                    "A pessoa que deu nome a essas formas foi Solomon W. Golomb, um matemático americano. Em 1953 ele deu uma palestra no Clube de Matemática de Harvard sobre as formas que podem ser montadas com quadrados e as chamou de poliminós. A palavra é uma brincadeira com dominó. Golomb leu o começo da palavra dominó como se fosse o prefixo di-, que significa dois, e colocou no lugar outros prefixos numéricos: triminó, tetraminó, pentominó e assim por diante.",
                    "O primeiro artigo completo sobre o assunto, Checker Boards and Polyominoes, saiu na revista American Mathematical Monthly em 1954. Nele, Golomb fazia perguntas que parecem jogos. Dá para cobrir um tabuleiro de xadrez com certos poliminós? Quais formas preenchem um retângulo? Anos depois, ele reuniu as ideias no livro Polyominoes (1965), que continua sendo uma introdução clássica."
                ]
            },
            {
                "h": "As doze letras",
                "p": [
                    "Os doze pentominós são conhecidos pelas letras a que se parecem: F, I, L, N, P, T, U, V, W, X, Y e Z. O conjunto em ordem alfabética é FILNPTUVWXYZ, e essa também é a ordem em que as peças aparecem no aplicativo Pentolings. As letras são uma abreviação: o I é uma linha reta de cinco quadrados, o X é um sinal de mais, o V é um canto com dois braços de três, e assim por diante.",
                    "Algumas letras escondem fatos interessantes. O X é o único pentominó que parece igual em qualquer direção em que seja girado, então tem apenas uma posição na grade. O I tem duas, porque pode ficar deitado ou em pé. O T, o U, o V, o W e o Z têm quatro posições cada, e os outros cinco (F, L, N, P e Y) têm oito, porque virá-los dá posições novas. Somando tudo, são 63 posições. Se não for permitido virar, existem 18 peças diferentes, porque seis das doze (F, L, N, P, Y e Z) vêm em duas versões espelhadas."
                ]
            },
            {
                "h": "Martin Gardner e a faísca de 1957",
                "p": [
                    "Os poliminós teriam continuado um cantinho da matemática se Martin Gardner não tivesse reparado neles. Gardner escrevia a coluna Mathematical Games na Scientific American e, em 1957, apresentou os pentominós a um público amplo. Os leitores adoraram. Eram simples o bastante para recortar em papel, e os quebra-cabeças que vinham com eles eram difíceis o bastante para manter as pessoas ocupadas por semanas.",
                    "Aquela coluna ajudou a iniciar um longo hábito. Fabricantes de quebra-cabeças passaram a vender conjuntos com as doze peças e as formas continuaram aparecendo em desafios e jogos posteriores. O próprio Golomb seguiu escrevendo sobre poliminós e matemática recreativa, e o termo que ele criou em 1953 é o que todo mundo ainda usa."
                ]
            },
            {
                "h": "Os retângulos: 2339 maneiras de preencher um 6x10",
                "p": [
                    "O desafio clássico dos pentominós é este: colocar as doze peças, cada uma uma vez, em um retângulo sem deixar vãos. As doze peças cobrem 60 quadrados, então o retângulo precisa ter área 60. Quatro formas são possíveis: 6x10, 5x12, 4x15 e 3x20. O número de soluções diferentes diminui conforme o retângulo fica mais fino. Se contarmos como uma só as soluções que diferem apenas por girar ou espelhar o retângulo inteiro, os números são:",
                    "6x10: 2339 soluções. 5x12: 1010. 4x15: 368. 3x20: apenas 2. Esses números foram obtidos com buscas exaustivas em computador e servem como boa verificação para qualquer resolvedor de pentominós. No Pentolings, o último nível do modo Encaixar é um retângulo 6x10 com o conjunto completo, então você resolve um quebra-cabeça que tem milhares de respostas válidas, e o jogo aceita qualquer uma delas."
                ]
            },
            {
                "h": "Além do cinco: famílias maiores e menores",
                "p": [
                    "Os pentominós são um membro de toda uma família, e os números mostram por que cinco quadrados é um tamanho tão confortável. Contando como a mesma forma as que se obtêm girando ou virando, existem 1 monominó, 1 dominó, 2 triminós, 5 tetraminós e 12 pentominós. Depois a conta salta para 35 hexaminós e 108 heptaminós. A partir daí, ninguém consegue guardar o conjunto inteiro na cabeça e os quebra-cabeças perdem o jeito amigável.",
                    "Cada tamanho tem seu caráter. Os tetraminós são tão poucos que se aprendem em um minuto, mas não dão conta sozinhos de quebra-cabeças de retângulos interessantes. Os hexaminós exigem um livro para aprender. Os pentominós ficam no meio: dá para aprender os doze em uma tarde e ainda passar anos com eles."
                ]
            },
            {
                "h": "Experimente com papel",
                "p": [
                    "Você não precisa de um aplicativo para conhecer os pentominós. Desenhe uma grade em papel quadriculado, recorte as doze formas guiando-se pelas letras e tente montar um retângulo 6x10. Muitos iniciantes começam pelo retângulo 3x20 achando que é mais fácil e desistem, porque ele tem apenas duas respostas verdadeiras e é o mais difícil dos quatro. Comece melhor com 6x10 ou 5x12, onde há mais de um caminho certo.",
                    "Um bom primeiro objetivo é colocar o X, a única peça que parece igual por todos os lados, depois o I comprido, e então trabalhar com as peças que abraçam as bordas. Se travar, separe uma forma que não consegue colocar e teste as outras sem ela, porque as duas ou três últimas peças costumam se encaixar juntas."
                ]
            },
            {
                "h": "Por que são tão bons como quebra-cabeças",
                "p": [
                    "Os pentominós estão em um ponto ideal. Com 12 peças, você ainda consegue lembrar cada forma e seu nome. Com 63 posições, cada peça pode olhar para quase qualquer direção, então os desafios continuam flexíveis. E a ideia é fácil de explicar: preencha a forma, sem vãos. Iniciantes resolvem formas pequenas de três ou quatro peças, e especialistas podem passar uma noite em um único retângulo 5x12.",
                    "Foi por isso que construímos o Pentolings em torno deles: um modo alegre de encaixar peças com 150 níveis, mais um segundo modo em que as mesmas peças caem de cima e você estoura cores. Se quiser conhecer as doze peças aos poucos, os primeiros níveis usam apenas três peças por vez e cada mundo novo acrescenta mais uma."
                ]
            }
        ],
        "faq": [
            [
                "Quem inventou os pentominós?",
                "Solomon W. Golomb os batizou e estudou. Ele apresentou a ideia de poliminós em 1953 e publicou um artigo sobre eles em 1954. As formas são tão simples que provavelmente as pessoas já brincavam com elas antes."
            ],
            [
                "Quantos pentominós existem?",
                "Existem exatamente 12 se for permitido girar e virar. Se não for permitido virar, são 18."
            ],
            [
                "De quantas maneiras dá para preencher um retângulo 6x10 com as 12 peças?",
                "2339, contando como uma só as soluções que diferem apenas por girar ou espelhar o retângulo inteiro."
            ],
            [
                "Por que têm nomes de letras?",
                "Cada uma das 12 formas se parece com uma letra: F, I, L, N, P, T, U, V, W, X, Y e Z, e as letras acabaram virando seus nomes."
            ]
        ]
    }
}
