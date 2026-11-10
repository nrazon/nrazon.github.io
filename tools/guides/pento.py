# Rehber: Pentolings Dose (Fit) modu - pentomino doldurma bulmacasi
GUIDE = {
    "id": "pento-tile",
    "app": "pentolings",
    "date": "2026-11-10",
    "en": {
        "slug": "how-to-solve-pentomino-puzzles",
        "title": "How to Solve Pentomino Puzzles: The 12 Pieces and Tips",
        "desc": "Learn the 12 pentomino pieces (F I L N P T U V W X Y Z) and how to fill a shape with no gaps: where to start, what goes first and how to avoid dead ends.",
        "intro": "A pentomino puzzle gives you a shape and a handful of pieces, each made of five squares. Your job is to fill the shape completely, with no gaps and no overlaps. Here are the 12 pieces and a way of thinking that makes the puzzles much easier.",
        "sections": [
            {
                "h": "Meet the 12 pentominoes",
                "p": [
                    "A pentomino is a piece made of five squares joined edge to edge. There are exactly 12 different ones, and they are named after the letters they look like: F, I, L, N, P, T, U, V, W, X, Y and Z. In alphabetical order the set is FILNPTUVWXYZ, which is also the easiest way to remember the full list.",
                    "Some are easy to picture. I is a straight line of five. X is a plus sign. T is a T with a long stem. U is a cup, V is a big corner with arms of three, and W is a small staircase. L and Y are long pieces with one extra square (at the end for L, second from the end for Y). N looks like two short lines shifted by one step. P is a 2x2 block with one square sticking out. F and Z are the twisty ones, and F is the hardest to spot at first."
                ]
            },
            {
                "h": "How the pieces move",
                "p": [
                    "In Pentolings you play this mode as Fit. Drag a piece from the tray into the shape. As you get close, a ghost shows where it will land, and when you let go it snaps into place. If the spot is not valid, the piece goes back to the tray.",
                    "Pieces can be turned and mirrored, so one piece can face the shape in many ways. Tap a piece to rotate it. Press and hold to flip it over like a mirror. If a piece refuses to fit, flip it before you give up on it: the mirrored version is a different position, and it is the most common reason for a piece that looks right but will not go in. In total the 12 pieces have 63 distinct positions on the grid, which is why the same piece can solve so many different shapes."
                ]
            },
            {
                "h": "Where to start: the tight spots first",
                "ul": [
                    "Begin at the narrowest or most awkward part of the shape: a corner, a one-square-wide dead end, a thin bridge. Those places have the fewest ways to be filled.",
                    "A dead end that is one square wide can only be filled by the tip of a piece. The long, thin pieces (I, L, Y, N) can reach into it, so look at these first.",
                    "X needs a spot where one cell has all four neighbors free, so it is easy to place or rule out. Do it early.",
                    "I needs a straight line of five free cells. If the shape has only one such line, that is where I belongs.",
                    "If an empty pocket has a size that cannot be reached by whole pieces (for example a closed hole of 1, 2 or 3 cells), you have made a mistake earlier: take that piece back."
                ]
            },
            {
                "h": "Count squares like a chessboard",
                "p": [
                    "Here is a trick for harder shapes. Imagine the shape colored like a chessboard. Every pentomino covers either three light and two dark squares or the other way round, with one exception: X covers four of one color and one of the other. So if the shape has a big difference between light and dark squares, X must be part of the answer, and exactly the right side of the board decides where it goes.",
                    "You do not have to do this on every level. It is a useful check when you are stuck on a shape with an odd outline, because it tells you early whether your plan can work."
                ]
            },
            {
                "h": "Locked pieces, hints and undo",
                "ul": [
                    "Some levels begin with a locked piece already in place. It is marked with a lock, it cannot be moved, and it is part of the final answer. Use it as an anchor and build around it.",
                    "If you place a piece you are not sure about, tap it to send it back to the tray, or drag it to move it. The Undo button takes back your last placements (up to 40 steps) and Restart clears the board after a confirmation.",
                    "Stuck? The Hint button highlights where one piece belongs. You get 3 free hints every day, and when they run out you can watch an optional short ad for 2 more.",
                    "Stars depend on hints: 3 stars with no hints, 2 stars with one or two hints, and 1 star with more. A hint is never a failure, it just costs a star, and you can replay the level."
                ]
            },
            {
                "h": "A worked example: 3x5 with P, U and V",
                "p": [
                    "Take a 3x5 rectangle and three pieces: P, U and V. That is 15 squares for 15 squares of pieces, so it should fit. Where do you start? Look at the corners. The V is the only one of the three with a long corner shape, so put it in a corner, with one arm along the left edge and the other along the bottom edge.",
                    "Now look at what is left. The U has a notch, a square it does not cover, and that notch must be filled by something. In this puzzle the only piece that can poke a square into the notch is the P, so the U goes on the right edge with its opening facing the middle, and the P slides in with its extra square in the notch. The finished board reads VPPUU, VPPPU and VVVUU from top to bottom. The steps you used are the same as in a hard level: corner first, awkward piece second, the flexible piece last."
                ]
            },
            {
                "h": "Common mistakes",
                "ul": [
                    "Forcing a piece that almost fits. If it does not go in after a flip and two or three rotations, it does not belong there.",
                    "Leaving a single square on its own. A lone empty square, or a pocket of two or three, can never be filled, so undo before you go further.",
                    "Saving the corners for last. Corners and dead ends are the first places to settle, not the last.",
                    "Forgetting the lock. A locked piece is part of the answer, so build around it instead of trying to use its space.",
                    "Reaching for a hint at once. A hint only costs a star, but if you look at the shape for one more minute you will often see it yourself, and that is how the pieces become familiar."
                ]
            },
            {
                "h": "A routine that works",
                "p": [
                    "First look at the shape and name the awkward spots. Place the pieces that have only one or two possible homes. Then fill the remaining area from the edge inward, leaving the open middle for last, because open space gives you the most freedom to fit the last pieces. If you reach a point where a small gap cannot be filled, back up two or three pieces rather than forcing one.",
                    "Pentolings has 150 levels in 15 worlds, starting with tiny three-piece shapes and growing to the full set of 12 pentominoes, so you can learn the pieces gradually."
                ]
            }
        ],
        "faq": [
            [
                "What is a pentomino?",
                "A pentomino is a shape made of five squares joined edge to edge. There are exactly 12 of them, named F, I, L, N, P, T, U, V, W, X, Y and Z."
            ],
            [
                "Do I need to use every piece?",
                "Each level lists the pieces you get. Every piece is used exactly once, and the number of squares in the shape is five times the number of pieces."
            ],
            [
                "Can I flip and rotate pieces?",
                "Yes. Tap a piece to rotate it and press and hold to flip it. Flipping is often the missing step."
            ],
            [
                "What does the lock on a piece mean?",
                "It is a helper piece that is already placed correctly. It cannot be moved and it belongs to the final solution."
            ],
            [
                "How do the stars work?",
                "3 stars if you finish without hints, 2 stars with one or two hints, 1 star with more. You can always replay a level."
            ]
        ]
    },
    "tr": {
        "slug": "pentomino-bulmacasi-nasil-cozulur",
        "title": "Pentomino Bulmacası Nasıl Çözülür? 12 Parça ve İpuçları",
        "desc": "12 pentomino parçasını (F I L N P T U V W X Y Z) ve bir şekli boşluksuz doldurmayı öğren: nereden başlanır, ne önce konur, çıkmazdan nasıl kaçılır.",
        "intro": "Pentomino bulmacasında sana bir şekil ve her biri beş kareden oluşan birkaç parça verilir. Amaç, şekli boşluk ve çakışma kalmadan tamamen doldurmaktır. İşte 12 parça ve bulmacaları çok kolaylaştıran bir düşünme yolu.",
        "sections": [
            {
                "h": "12 pentomino ile tanış",
                "p": [
                    "Pentomino, beş karenin kenarlarından birleşmesiyle oluşan bir parçadır. Tam 12 farklı pentomino vardır ve benzedikleri harflerle anılırlar: F, I, L, N, P, T, U, V, W, X, Y ve Z. Alfabe sırasıyla takım FILNPTUVWXYZ diye yazılır; bütün listeyi akılda tutmanın en kolay yolu da budur.",
                    "Bazılarını gözünde canlandırmak kolaydır. I beş karelik düz çizgidir. X artı işaretidir. T, uzun saplı bir T'dir. U bir fincan, V üçer karelik kolları olan büyük bir köşe, W ise küçük bir merdivendir. L ve Y, fazladan bir karesi olan uzun parçalardır (L'de uçta, Y'de uçtan ikinci sırada). N, bir basamak kaymış iki kısa çizgiye benzer. P, bir karesi dışarı çıkan 2x2'lik bir bloktur. F ve Z kıvrımlı olanlardır; F ilk başta en zor tanınanıdır."
                ]
            },
            {
                "h": "Parçalar nasıl oynatılır",
                "p": [
                    "Pentolings'te bu mod Döşe adını taşır. Parçayı tepsiden şeklin içine sürükle. Yaklaştıkça nereye oturacağını bir hayalet gösterir, bıraktığında yerine yapışır. Yer geçerli değilse parça tepsiye döner.",
                    "Parçalar döndürülüp aynalanabilir, yani tek bir parça şekle birçok biçimde bakabilir. Parçaya dokun: döner. Basılı tut: ayna gibi çevrilir. Bir parça sığmıyorsa vazgeçmeden önce çevirmeyi dene: aynalanmış hali farklı bir duruştur ve doğru görünen ama girmeyen parçanın en sık nedeni budur. 12 parçanın ızgara üzerinde toplam 63 ayrı duruşu vardır; aynı parçanın bu kadar çok farklı şekli çözebilmesinin nedeni de bu."
                ]
            },
            {
                "h": "Nereden başlamalı: önce dar yerler",
                "ul": [
                    "Şeklin en dar ya da en sıkıntılı yerinden başla: bir köşe, bir kare genişliğinde çıkmaz, ince bir köprü. Buraları doldurmanın en az yolu vardır.",
                    "Bir kare genişliğindeki çıkmaz yalnızca bir parçanın ucuyla dolabilir. Uzun ve ince parçalar (I, L, Y, N) oraya girebilir; önce bunlara bak.",
                    "X, bir hücrenin dört komşusunun da boş olduğu bir yer ister; bu yüzden yerleştirmek ya da elemek kolaydır. Erken yerleştir.",
                    "I için beş boş hücrelik düz bir çizgi gerekir. Şekilde böyle tek bir çizgi varsa I oradadır.",
                    "Boş bir cep, tam parçalarla dolamayacak büyüklükteyse (örneğin 1, 2 ya da 3 hücrelik kapalı bir delik) daha önce hata yapmışsındır: o parçayı geri al."
                ]
            },
            {
                "h": "Satranç tahtası gibi say",
                "p": [
                    "Zor şekiller için bir numara: şekli satranç tahtası gibi boyalı hayal et. Her pentomino ya üç açık ve iki koyu kareyi ya da tersini kaplar; tek istisna X'tir, o bir renkten dört, diğerinden bir kare kaplar. Yani şekilde açık ve koyu kareler arasında büyük bir fark varsa X mutlaka çözümün parçasıdır ve fark hangi tarafta olduğuna bakılarak yerini bulur.",
                    "Her bölümde buna gerek yok. Ama düzensiz çizgili bir şekilde takıldığında, planının tutup tutmayacağını erkenden söyleyen faydalı bir kontroldür."
                ]
            },
            {
                "h": "Kilitli parçalar, ipucu ve geri al",
                "ul": [
                    "Bazı bölümler yerinde duran kilitli bir parçayla başlar. Kilit simgesi taşır, oynatılamaz ve nihai çözümün parçasıdır. Onu çapa olarak kullan ve çevresini doldur.",
                    "Emin olmadığın bir parçayı yerleştirdiysen dokun, tepsiye geri döner; ya da sürükleyip yerini değiştir. Geri al düğmesi son yerleştirmelerini geri alır (en çok 40 adım), Baştan ise onaydan sonra tahtayı temizler.",
                    "Takıldın mı? İpucu düğmesi bir parçanın nereye ait olduğunu parlatır. Her gün 3 ücretsiz ipucun yenilenir; bitince isteğe bağlı kısa bir reklamla 2 ipucu daha kazanırsın.",
                    "Yıldızlar ipucuna bağlıdır: ipucusuz 3, bir-iki ipucuyla 2, daha fazlasıyla 1 yıldız. İpucu hata değildir, yalnızca bir yıldıza mal olur; bölümü yeniden oynayabilirsin."
                ]
            },
            {
                "h": "Çalışılmış bir örnek: P, U ve V ile 3x5",
                "p": [
                    "3x5'lik bir dikdörtgen ve üç parça al: P, U ve V. Bu, 15 kare için 15 karelik parça demektir; yani sığmalı. Nereden başlarsın? Köşelere bak. Üçü arasında uzun köşe şekli olan tek parça V'dir; onu bir köşeye koy, bir kolu sol kenar, diğeri alt kenar boyunca olsun.",
                    "Şimdi geriye ne kaldığına bak. U'nun bir girintisi var, kaplamadığı bir kare ve o girinti başka bir parçayla dolmalı. Bu bulmacada girintiye bir kare sokabilecek tek parça P'dir; bu yüzden U sağ kenara, açıklığı ortaya bakacak biçimde gider ve P fazladan karesiyle girintiye kayar. Biten tahta yukarıdan aşağıya VPPUU, VPPPU ve VVVUU diye okunur. Kullandığın adımlar zor bir bölümdekilerle aynıdır: önce köşe, sonra sıkıntılı parça, esnek parça en son."
                ]
            },
            {
                "h": "Sık yapılan hatalar",
                "ul": [
                    "Neredeyse sığan bir parçayı zorlamak. Bir çevirme ve iki üç döndürmeden sonra girmiyorsa oraya ait değildir.",
                    "Tek bir kareyi yalnız bırakmak. Tek başına boş bir kare ya da iki üç karelik bir cep asla dolmaz; bu yüzden ilerlemeden önce geri al.",
                    "Köşeleri sona saklamak. Köşeler ve çıkmazlar ilk halledilecek yerlerdir, son değil.",
                    "Kilidi unutmak. Kilitli parça cevabın bir parçasıdır; onun yerini kullanmaya çalışmak yerine çevresini doldur.",
                    "Hemen ipucuna uzanmak. İpucu yalnızca bir yıldıza mal olur, ama şekle bir dakika daha bakarsan çoğu zaman kendin görürsün ve parçalar işte böyle tanıdık gelmeye başlar."
                ]
            },
            {
                "h": "İşe yarayan bir rutin",
                "p": [
                    "Önce şekle bak ve sıkıntılı yerlere ad ver. Yalnızca bir ya da iki olası yuvası olan parçaları yerleştir. Sonra kalan alanı kenardan içeri doğru doldur, açık ortayı en sona bırak; çünkü açık alan son parçaları yerleştirirken sana en çok serbestlik verir. Küçük bir boşluğun doldurulamayacağı bir noktaya gelirsen, bir parçayı zorlamak yerine iki üç parça geri git.",
                    "Pentolings'te 15 dünyada 150 bölüm vardır; üç parçalık küçük şekillerle başlar ve 12 pentominonun tamamına kadar büyür, böylece parçaları yavaş yavaş öğrenebilirsin."
                ]
            }
        ],
        "faq": [
            [
                "Pentomino nedir?",
                "Pentomino, beş karenin kenarlarından birleşmesiyle oluşan şekildir. Tam 12 tanedir ve F, I, L, N, P, T, U, V, W, X, Y, Z adlarını taşırlar."
            ],
            [
                "Her parçayı kullanmak zorunda mıyım?",
                "Her bölüm sana verilen parçaları listeler. Her parça tam bir kez kullanılır ve şekildeki kare sayısı parça sayısının beş katıdır."
            ],
            [
                "Parçaları çevirip döndürebilir miyim?",
                "Evet. Dokununca döner, basılı tutunca çevrilir. Eksik adım çoğu zaman çevirmektir."
            ],
            [
                "Parçadaki kilit ne demek?",
                "Zaten doğru yerleştirilmiş bir yardımcı parçadır. Oynatılamaz ve nihai çözümün parçasıdır."
            ],
            [
                "Yıldızlar nasıl çalışır?",
                "İpucusuz bitirirsen 3, bir-iki ipucuyla 2, daha fazlasıyla 1 yıldız. Bölümü her zaman yeniden oynayabilirsin."
            ]
        ]
    },
    "es": {
        "slug": "como-resolver-puzles-de-pentominos",
        "title": "Cómo resolver puzles de pentominós: las 12 piezas y consejos",
        "desc": "Aprende las 12 piezas de pentominó (F I L N P T U V W X Y Z) y a rellenar una forma sin huecos: por dónde empezar, qué va primero y cómo evitar callejones.",
        "intro": "Un puzle de pentominós te da una forma y unas cuantas piezas, cada una hecha de cinco cuadrados. Tu tarea es rellenar la forma por completo, sin huecos ni solapamientos. Aquí tienes las 12 piezas y una manera de pensar que facilita mucho los puzles.",
        "sections": [
            {
                "h": "Conoce los 12 pentominós",
                "p": [
                    "Un pentominó es una pieza formada por cinco cuadrados unidos por sus lados. Hay exactamente 12 distintos y se nombran por la letra a la que se parecen: F, I, L, N, P, T, U, V, W, X, Y y Z. En orden alfabético el conjunto es FILNPTUVWXYZ, que además es la forma más fácil de recordar la lista completa.",
                    "Algunos son fáciles de imaginar. La I es una línea recta de cinco. La X es un signo más. La T es una T con un palo largo. La U es una taza, la V es una esquina grande con brazos de tres y la W es una pequeña escalera. La L y la Y son piezas largas con un cuadrado extra (en el extremo en la L, en la segunda posición desde el extremo en la Y). La N parece dos líneas cortas desplazadas un paso. La P es un bloque de 2x2 con un cuadrado que sobresale. La F y la Z son las retorcidas, y la F es la más difícil de reconocer al principio."
                ]
            },
            {
                "h": "Cómo se mueven las piezas",
                "p": [
                    "En Pentolings este modo se llama Encajar. Arrastra una pieza desde la bandeja hasta la forma. Al acercarte, un fantasma muestra dónde caerá y, al soltar, se fija en su sitio. Si el lugar no es válido, la pieza vuelve a la bandeja.",
                    "Las piezas se pueden girar y voltear como en un espejo, así que una misma pieza puede encarar la forma de muchas maneras. Toca una pieza para girarla. Mantenla pulsada para voltearla. Si una pieza no cabe, voltéala antes de rendirte: la versión en espejo es otra posición y es la causa más frecuente de que una pieza parezca correcta pero no entre. En total, las 12 piezas tienen 63 posiciones distintas en la cuadrícula, y por eso la misma pieza sirve para tantas formas diferentes."
                ]
            },
            {
                "h": "Por dónde empezar: primero los sitios estrechos",
                "ul": [
                    "Empieza por la parte más estrecha o incómoda de la forma: una esquina, un callejón sin salida de un cuadrado de ancho, un puente fino. Esos lugares tienen menos formas de rellenarse.",
                    "Un callejón de un cuadrado de ancho solo se puede llenar con la punta de una pieza. Las piezas largas y delgadas (I, L, Y, N) pueden entrar, así que mira primero esas.",
                    "La X necesita un lugar donde una casilla tenga libres sus cuatro vecinas, así que es fácil colocarla o descartarla. Hazlo pronto.",
                    "La I necesita una línea recta de cinco casillas libres. Si la forma tiene una sola línea así, ahí va la I.",
                    "Si un hueco vacío tiene un tamaño que las piezas enteras no pueden cubrir (por ejemplo, un agujero cerrado de 1, 2 o 3 casillas), cometiste un error antes: retira esa pieza."
                ]
            },
            {
                "h": "Cuenta como en un tablero de ajedrez",
                "p": [
                    "Un truco para formas difíciles: imagina la forma pintada como un tablero de ajedrez. Cada pentominó cubre tres casillas claras y dos oscuras, o al revés, con una excepción: la X cubre cuatro de un color y una del otro. Así que, si la forma tiene mucha diferencia entre casillas claras y oscuras, la X tiene que formar parte de la solución, y el color que sobra indica dónde puede ir.",
                    "No hace falta hacerlo en todos los niveles. Es una buena comprobación cuando te atascas en una forma de contorno extraño, porque te dice pronto si tu plan puede funcionar."
                ]
            },
            {
                "h": "Piezas con candado, pistas y deshacer",
                "ul": [
                    "Algunos niveles empiezan con una pieza con candado ya colocada. Lleva un candado, no se puede mover y forma parte de la solución final. Úsala como ancla y construye a su alrededor.",
                    "Si colocas una pieza de la que no estás seguro, tócala para devolverla a la bandeja, o arrástrala para moverla. El botón Deshacer revierte tus últimas colocaciones (hasta 40 pasos) y Reiniciar vacía el tablero tras una confirmación.",
                    "¿Atascado? El botón Pista ilumina dónde va una pieza. Tienes 3 pistas gratis al día y, cuando se acaban, puedes ver un anuncio corto opcional para conseguir 2 más.",
                    "Las estrellas dependen de las pistas: 3 estrellas sin pistas, 2 con una o dos pistas y 1 con más. Una pista no es un fracaso, solo cuesta una estrella, y puedes repetir el nivel."
                ]
            },
            {
                "h": "Un ejemplo resuelto: 3x5 con P, U y V",
                "p": [
                    "Toma un rectángulo de 3x5 y tres piezas: P, U y V. Son 15 cuadros para 15 cuadros de piezas, así que debe encajar. ¿Por dónde empiezas? Mira las esquinas. La V es la única de las tres con forma de esquina larga, así que ponla en una esquina, con un brazo a lo largo del borde izquierdo y el otro a lo largo del borde inferior.",
                    "Ahora mira lo que queda. La U tiene una muesca, un cuadro que no cubre, y esa muesca tiene que llenarla otra pieza. En este puzle la única pieza que puede meter un cuadro en la muesca es la P, así que la U va en el borde derecho con su abertura hacia el centro, y la P entra deslizándose con su cuadro extra en la muesca. El tablero terminado se lee VPPUU, VPPPU y VVVUU de arriba abajo. Los pasos que usaste son los mismos que en un nivel difícil: primero la esquina, después la pieza incómoda y, al final, la flexible."
                ]
            },
            {
                "h": "Errores frecuentes",
                "ul": [
                    "Forzar una pieza que casi encaja. Si no entra tras voltearla y girarla dos o tres veces, no va ahí.",
                    "Dejar un cuadro suelto. Un cuadro vacío solo, o un hueco de dos o tres, no se podrá llenar nunca, así que deshaz antes de seguir.",
                    "Dejar las esquinas para el final. Las esquinas y los callejones sin salida son los primeros sitios que hay que resolver, no los últimos.",
                    "Olvidar el candado. Una pieza con candado forma parte de la respuesta, así que construye a su alrededor en lugar de intentar usar su espacio.",
                    "Recurrir a la pista enseguida. Una pista solo cuesta una estrella, pero si miras la forma un minuto más, muchas veces lo verás tú mismo, y así es como las piezas se vuelven familiares."
                ]
            },
            {
                "h": "Una rutina que funciona",
                "p": [
                    "Primero mira la forma y localiza los puntos incómodos. Coloca las piezas que solo tienen uno o dos sitios posibles. Después rellena la zona restante desde el borde hacia dentro y deja el centro abierto para el final, porque el espacio abierto te da más libertad para encajar las últimas piezas. Si llegas a un punto en que un hueco pequeño no se puede llenar, retrocede dos o tres piezas en lugar de forzar una.",
                    "Pentolings tiene 150 niveles en 15 mundos, desde formas diminutas de tres piezas hasta el conjunto completo de 12 pentominós, de modo que puedes aprender las piezas poco a poco."
                ]
            }
        ],
        "faq": [
            [
                "¿Qué es un pentominó?",
                "Un pentominó es una forma hecha de cinco cuadrados unidos por sus lados. Hay exactamente 12 y se llaman F, I, L, N, P, T, U, V, W, X, Y y Z."
            ],
            [
                "¿Tengo que usar todas las piezas?",
                "Cada nivel indica las piezas que recibes. Cada pieza se usa exactamente una vez y el número de cuadrados de la forma es cinco veces el número de piezas."
            ],
            [
                "¿Puedo voltear y girar las piezas?",
                "Sí. Toca una pieza para girarla y mantenla pulsada para voltearla. Voltear suele ser el paso que falta."
            ],
            [
                "¿Qué significa el candado de una pieza?",
                "Es una pieza de ayuda ya colocada correctamente. No se puede mover y pertenece a la solución final."
            ],
            [
                "¿Cómo funcionan las estrellas?",
                "3 estrellas si terminas sin pistas, 2 con una o dos pistas y 1 con más. Siempre puedes repetir un nivel."
            ]
        ]
    },
    "pt": {
        "slug": "como-resolver-quebra-cabecas-de-pentominos",
        "title": "Como resolver quebra-cabeças de pentominós: as 12 peças e dicas",
        "desc": "Aprenda as 12 peças de pentominó (F I L N P T U V W X Y Z) e a preencher uma forma sem vãos: por onde começar, o que vai primeiro e como evitar becos.",
        "intro": "Um quebra-cabeça de pentominós dá a você uma forma e algumas peças, cada uma feita de cinco quadradinhos. Sua tarefa é preencher a forma por completo, sem vãos nem sobreposições. Aqui estão as 12 peças e um jeito de pensar que facilita muito os desafios.",
        "sections": [
            {
                "h": "Conheça os 12 pentominós",
                "p": [
                    "Um pentominó é uma peça formada por cinco quadrados unidos pelos lados. Existem exatamente 12 diferentes, e eles são chamados pela letra com que se parecem: F, I, L, N, P, T, U, V, W, X, Y e Z. Em ordem alfabética o conjunto é FILNPTUVWXYZ, que também é a maneira mais fácil de lembrar a lista inteira.",
                    "Alguns são fáceis de imaginar. O I é uma linha reta de cinco. O X é um sinal de mais. O T é um T com haste longa. O U é uma xícara, o V é um canto grande com braços de três e o W é uma pequena escada. O L e o Y são peças compridas com um quadrado a mais (na ponta no L, na segunda posição a partir da ponta no Y). O N parece duas linhas curtas deslocadas um passo. O P é um bloco 2x2 com um quadrado saindo. O F e o Z são os tortuosos, e o F é o mais difícil de reconhecer no começo."
                ]
            },
            {
                "h": "Como as peças se movem",
                "p": [
                    "No Pentolings este modo se chama Encaixar. Arraste uma peça da bandeja até a forma. Ao se aproximar, um fantasma mostra onde ela vai cair e, ao soltar, ela se fixa no lugar. Se o local não for válido, a peça volta para a bandeja.",
                    "As peças podem ser giradas e viradas como em um espelho, então uma mesma peça pode encarar a forma de muitas maneiras. Toque em uma peça para girá-la. Segure para virá-la. Se uma peça não couber, vire-a antes de desistir: a versão espelhada é outra posição e é o motivo mais comum de uma peça parecer certa mas não entrar. No total, as 12 peças têm 63 posições diferentes na grade, e é por isso que a mesma peça serve para tantas formas diferentes."
                ]
            },
            {
                "h": "Por onde começar: primeiro os lugares apertados",
                "ul": [
                    "Comece pela parte mais estreita ou incômoda da forma: um canto, um beco sem saída de um quadrado de largura, uma ponte fina. Esses lugares têm menos maneiras de ser preenchidos.",
                    "Um beco de um quadrado de largura só pode ser preenchido pela ponta de uma peça. As peças longas e finas (I, L, Y, N) conseguem entrar, então olhe primeiro para elas.",
                    "O X precisa de um lugar em que uma casa tenha os quatro vizinhos livres, então é fácil colocá-lo ou descartá-lo. Faça isso cedo.",
                    "O I precisa de uma linha reta de cinco casas livres. Se a forma tem apenas uma linha assim, é ali que o I vai.",
                    "Se um espaço vazio tem um tamanho que peças inteiras não conseguem cobrir (por exemplo, um buraco fechado de 1, 2 ou 3 casas), você errou antes: retire essa peça."
                ]
            },
            {
                "h": "Conte como em um tabuleiro de xadrez",
                "p": [
                    "Um truque para formas difíceis: imagine a forma pintada como um tabuleiro de xadrez. Cada pentominó cobre três casas claras e duas escuras, ou o contrário, com uma exceção: o X cobre quatro de uma cor e uma da outra. Portanto, se a forma tem uma grande diferença entre casas claras e escuras, o X precisa fazer parte da resposta, e a cor em excesso mostra onde ele pode ficar.",
                    "Não é preciso fazer isso em todo nível. É uma boa verificação quando você trava em uma forma de contorno estranho, porque mostra cedo se o seu plano pode funcionar."
                ]
            },
            {
                "h": "Peças com cadeado, dicas e desfazer",
                "ul": [
                    "Alguns níveis começam com uma peça com cadeado já colocada. Ela tem um cadeado, não pode ser movida e faz parte da solução final. Use-a como âncora e construa ao redor.",
                    "Se você colocar uma peça sobre a qual não tem certeza, toque nela para devolvê-la à bandeja, ou arraste para movê-la. O botão Desfazer volta suas últimas colocações (até 40 passos) e Recomeçar limpa o tabuleiro depois de uma confirmação.",
                    "Travou? O botão Dica destaca onde uma peça vai. Você ganha 3 dicas grátis por dia e, quando elas acabam, pode assistir a um anúncio curto opcional para ganhar mais 2.",
                    "As estrelas dependem das dicas: 3 estrelas sem dicas, 2 com uma ou duas dicas e 1 com mais. Uma dica não é um fracasso, só custa uma estrela, e você pode repetir o nível."
                ]
            },
            {
                "h": "Um exemplo resolvido: 3x5 com P, U e V",
                "p": [
                    "Pegue um retângulo 3x5 e três peças: P, U e V. São 15 quadrados para 15 quadrados de peças, então deve caber. Por onde começar? Olhe os cantos. O V é a única das três com formato de canto longo, então coloque-o em um canto, com um braço ao longo da borda esquerda e o outro ao longo da borda inferior.",
                    "Agora veja o que sobra. O U tem uma reentrância, um quadrado que ele não cobre, e essa reentrância precisa ser preenchida por outra peça. Neste quebra-cabeça a única peça que consegue enfiar um quadrado na reentrância é o P, então o U vai na borda direita com a abertura voltada para o meio, e o P desliza com o quadrado extra para dentro da reentrância. O tabuleiro pronto se lê VPPUU, VPPPU e VVVUU de cima para baixo. Os passos que você usou são os mesmos de um nível difícil: primeiro o canto, depois a peça incômoda e, por último, a flexível."
                ]
            },
            {
                "h": "Erros comuns",
                "ul": [
                    "Forçar uma peça que quase encaixa. Se ela não entra depois de virar e girar duas ou três vezes, não é ali o lugar dela.",
                    "Deixar um quadrado isolado. Um quadrado vazio sozinho, ou um vão de dois ou três, nunca poderá ser preenchido, então desfaça antes de continuar.",
                    "Deixar os cantos para o fim. Os cantos e os becos sem saída são os primeiros lugares a resolver, não os últimos.",
                    "Esquecer o cadeado. Uma peça com cadeado faz parte da resposta, então construa ao redor dela em vez de tentar usar o espaço dela.",
                    "Apelar logo para a dica. Uma dica só custa uma estrela, mas se você olhar a forma por mais um minuto, muitas vezes vai enxergar sozinho, e é assim que as peças ficam familiares."
                ]
            },
            {
                "h": "Uma rotina que funciona",
                "p": [
                    "Primeiro olhe a forma e identifique os pontos incômodos. Coloque as peças que só têm um ou dois lugares possíveis. Depois preencha a área restante da borda para dentro e deixe o meio aberto para o final, porque o espaço aberto dá mais liberdade para encaixar as últimas peças. Se chegar a um ponto em que um vão pequeno não pode ser preenchido, volte duas ou três peças em vez de forçar uma.",
                    "O Pentolings tem 150 níveis em 15 mundos, começando com formas pequenas de três peças e crescendo até o conjunto completo de 12 pentominós, para que você aprenda as peças aos poucos."
                ]
            }
        ],
        "faq": [
            [
                "O que é um pentominó?",
                "Um pentominó é uma forma feita de cinco quadrados unidos pelos lados. Existem exatamente 12, chamados F, I, L, N, P, T, U, V, W, X, Y e Z."
            ],
            [
                "Preciso usar todas as peças?",
                "Cada nível informa as peças que você recebe. Cada peça é usada exatamente uma vez e o número de quadrados da forma é cinco vezes o número de peças."
            ],
            [
                "Posso virar e girar as peças?",
                "Sim. Toque em uma peça para girá-la e segure para virá-la. Virar costuma ser o passo que falta."
            ],
            [
                "O que significa o cadeado em uma peça?",
                "É uma peça de ajuda já colocada corretamente. Ela não pode ser movida e pertence à solução final."
            ],
            [
                "Como funcionam as estrelas?",
                "3 estrelas se terminar sem dicas, 2 com uma ou duas dicas e 1 com mais. Você sempre pode repetir um nível."
            ]
        ]
    }
}
