# Rehber: Cubbles ileri düzey (kombo, seri, planlama); temel ipuçları blocks.py'de
GUIDE = {
    "id": "blocks-advanced", "app": "cubbles", "date": "2026-11-10",
    "en": {
        "slug": "block-puzzle-combos-and-high-score-strategy",
        "title": "Block Puzzle High Score: Combos, Streaks and Planning Ahead",
        "desc": "How block puzzle scoring really works, why clearing several lines at once pays so much, how to keep a combo alive and how to plan a whole set of pieces.",
        "intro": "Once you know the basics of a block puzzle, the next jump in score comes from understanding the numbers behind it. Here is how Cubbles counts points, why a combo is worth so much, and how to plan a whole set of three pieces in advance.",
        "sections": [
            {"h": "How the points are counted", "p": [
                "Every piece you place gives one point for each square it covers. That part is small. The real score comes from clearing lines. A clear is worth 10 times the number of lines squared, times your current combo number.",
                "Squaring the lines is what matters. One line is worth 10, two lines at once are worth 40, three lines are worth 90 and four lines are worth 160, all before the combo multiplier. Clearing two lines together is four times better than clearing one, not twice.",
                "If you empty the entire board with a clear, you get a perfect clear bonus of 100 extra points. It is a nice surprise, but it rarely beats steady combos, so do not bend your whole game around it."]},
            {"h": "What a combo really is", "p": [
                "A combo counts how many moves in a row have cleared at least one line. Your first clear is combo 1, the next clearing move is combo 2, and so on. Each time you clear, the number goes up and so does the multiplier.",
                "The streak survives a limited number of quiet moves. You can place two pieces without clearing anything, but if a third move in a row clears nothing, the combo drops back to zero. In Cubbles a set has three pieces, so in practice you need at least one clear in every set to keep the streak going. The game shows how many chances you have left.",
                "Compare two ways to get the same lines. Clearing a single line five moves in a row scores 10, 20, 30, 40 and 50, a total of 150 from clears. The same five single lines cleared one by one with the combo broken in between score only 10 each. The multiplier rewards patience and rhythm more than luck."]},
            {"h": "Two lines beat two combos", "p": [
                "Because lines are squared and the combo is a simple multiplier, a bigger clear usually wins over a longer streak early on. At combo 1, two lines at once score 40. Two separate single lines at combos 1 and 2 score only 30. Three lines at combo 2 score 180.",
                "Late in a long streak the balance changes. At combo 5 a single line is already worth 50, and a double is worth 200. A long streak makes every later clear worth more, so protecting it is worth a small sacrifice in the shape of the board.",
                "A useful habit is to ask before each move: can this piece finish more than one line, and will the next piece still clear something? If the answer to both is yes, that is a strong move."]},
            {"h": "Plan the whole set, not one piece", "p": [
                "You always see three pieces at once, and Cubbles makes sure those three can all be placed in some order. That gives you information. Before you move, look at the three pieces together and imagine where each could go.",
                "Often one piece prepares a line for another. A short piece can leave a gap in a row, and the long piece in your hand fills exactly that gap and clears the line. Placing them in the other order may not work at all.",
                "Because pieces cannot be rotated, the shapes you hold are the shapes you must use. Look for placements that will clear lines with the hardest piece first, keep the easiest piece for the end, and check what the board will look like when you have placed all three and a fresh set arrives.",
                "The pieces are chosen with weights. Small pieces become more common as the board fills up, and also in the first moves of a game. A crowded board is not hopeless, because the game tends to hand you pieces that help."]},
            {"h": "Building lines for a chain", "p": [
                "To keep a combo going you need lines that are nearly done. Aim to leave several rows or columns missing just one block shape each, so that the next set offers something that completes one or two of them.",
                "Work on rows and columns at the same time. A piece that sits in the corner of the board helps one row and one column, so a clear in one direction often brings the other closer. Avoid filling one long strip completely while leaving the rest empty, because it only helps a single clear.",
                "Use quiet moves on purpose. When you must place a piece without clearing, put it where it brings a line closer or tidies an edge, not in the middle of the open space. You have two quiet moves before the combo breaks, so spend them on setup."]},
            {"h": "Daily challenge and revive", "p": [
                "In the daily challenge everyone gets the same sequence of piece sets, built from the date. You can start the daily game again with the same pieces, and your best score of the day is kept. This makes it a good place to practise: you learn which pieces are coming and what to save space for. The first game of the day also gives a bonus of 50 experience points, and daily scores go to their own leaderboard, separate from classic games.",
                "If a game ends, you can watch an optional ad once per game to continue. It clears the two fullest rows and the two fullest columns and gives you a fresh set. Use it when you are already deep in a streak, because the extra moves let you keep earning at a high multiplier.",
                "Finally, the daily quests give you small goals such as reaching a given combo or a given score. A goal like a combo of 3 or 4 is a good reason to practise the habits in this guide."]},
        ],
        "faq": [
            ["How are points calculated in Cubbles?", "Each placed square gives one point. A clear adds 10 times the number of lines squared, times your combo number, and an empty board adds 100."],
            ["How many moves can I make without clearing before the combo ends?", "Two. If a third move in a row clears nothing, the combo resets."],
            ["Is it better to clear two lines at once or build a combo?", "Early on, a double clear usually wins. In a long streak, protecting the combo is worth more because every clear is multiplied."],
            ["Do I get the same pieces in the daily challenge?", "Yes, they come from the date and are normally the same for every player. You can start the daily game again with the same pieces."],
        ],
    },
    "tr": {
        "slug": "blok-bulmaca-kombo-ve-yuksek-skor-stratejisi",
        "title": "Blok Bulmacada Yüksek Skor: Kombo, Seri ve İleri Planlama",
        "desc": "Blok bulmacada puanlama nasıl işler, birkaç satırı birden temizlemek neden çok kazandırır, kombo nasıl sürdürülür ve üç parça nasıl planlanır.",
        "intro": "Blok bulmacanın temellerini öğrendikten sonra skordaki bir sonraki sıçrama, arkadaki sayıları anlamaktan gelir. Cubbles'ın puanı nasıl saydığını, kombonun neden bu kadar değerli olduğunu ve üç parçalık bir takımı önceden nasıl planlayacağını anlatıyoruz.",
        "sections": [
            {"h": "Puanlar nasıl sayılır", "p": [
                "Yerleştirdiğin her parça, kapladığı her kare için bir puan verir. Bu kısım küçüktür. Asıl skor satır temizlemekten gelir. Bir temizleme, satır sayısının karesinin 10 katı çarpı mevcut kombo sayındır.",
                "Önemli olan satır sayısının karesinin alınması. Bir satır 10, aynı anda iki satır 40, üç satır 90, dört satır 160 eder; hepsi kombo çarpanından önce. İki satırı birlikte temizlemek, bir satırı temizlemekten iki kat değil dört kat iyidir.",
                "Bir temizlemeyle tüm tahtayı boşaltırsan 100 puanlık mükemmel temizleme bonusu alırsın. Güzel bir sürprizdir ama düzenli kombolardan nadiren daha iyidir; bütün oyununu onun etrafında kurma."]},
            {"h": "Kombo gerçekte nedir", "p": [
                "Kombo, art arda kaç hamlenin en az bir satır temizlediğini sayar. İlk temizlemen kombo 1, sonraki temizleyen hamle kombo 2 olur ve böyle sürer. Her temizlemede sayı artar, çarpan da artar.",
                "Seri, sınırlı sayıda sessiz hamleyi kaldırır. Hiçbir şey temizlemeden iki parça koyabilirsin; ama art arda üçüncü hamle de bir şey temizlemezse kombo sıfıra düşer. Cubbles'ta bir takım üç parçadır; yani pratikte seriyi sürdürmek için her takımda en az bir temizleme gerekir. Oyun kaç hakkın kaldığını gösterir.",
                "Aynı satırları almanın iki yolunu karşılaştır. Art arda beş hamlede birer satır temizlemek 10, 20, 30, 40 ve 50 puan, temizlemelerden toplam 150 eder. Aynı beş tek satırı arada kombo bozularak tek tek temizlersen her biri yalnızca 10 puandır. Çarpan, şansa göre sabra ve ritme daha çok ödül verir.",
                "Kombo hakları tahtada küçük işaretlerle görünür. Hamle yapmadan önce onlara bakmak seriyi kaybetmemenin en kolay yoludur: tek hakkın kaldığını görürsen bu hamle mutlaka bir satır temizlemeli."]},
            {"h": "İki satır, iki komboyu yener", "p": [
                "Satırlar kare alındığı ve kombo basit bir çarpan olduğu için, erken aşamada daha büyük bir temizleme genelde daha uzun bir seriyi yener. Kombo 1'de aynı anda iki satır 40 eder. Kombo 1 ve 2'de iki ayrı tek satır yalnızca 30 eder. Kombo 2'de üç satır 180 eder.",
                "Uzun bir serinin sonlarında denge değişir. Kombo 5'te tek bir satır zaten 50, çift satır 200 eder. Uzun bir seri sonraki her temizlemeyi daha değerli yapar; bu yüzden onu korumak, tahtanın şeklinden küçük bir ödün vermeye değer. Seri henüz kısaysa (kombo 1 ya da 2) durum tersidir: büyük bir temizleme kurmak seriyi canlı tutmaktan genelde daha çok kazandırır.",
                "Faydalı bir alışkanlık: her hamleden önce sor. Bu parça birden fazla satırı bitirebilir mi ve sıradaki parça yine bir şey temizler mi? İkisinin de cevabı evetse güçlü bir hamledir."]},
            {"h": "Tek parçayı değil, bütün takımı planla", "p": [
                "Her zaman aynı anda üç parça görürsün ve Cubbles bu üçünün de bir sırayla yerleştirilebilmesini sağlar. Bu sana bilgi verir. Hamle yapmadan önce üç parçaya birlikte bak ve her birinin nereye gidebileceğini hayal et.",
                "Çoğunlukla bir parça diğeri için bir satır hazırlar. Kısa bir parça bir satırda boşluk bırakır, elindeki uzun parça tam o boşluğu doldurup satırı temizler. Bunları ters sırayla koymak hiç işe yaramayabilir.",
                "Parçalar döndürülemediği için elindeki şekiller, kullanmak zorunda olduğun şekillerdir. En zor parçayla satır temizleyecek yerleştirmeleri ara, en kolay parçayı sona sakla ve üçünü de koyup yeni bir takım geldiğinde tahtanın nasıl görüneceğine bak.",
                "Parçalar ağırlıklarla seçilir. Tahta doldukça ve oyunun ilk hamlelerinde küçük parçalar daha sık gelir. Kalabalık bir tahta umutsuz değildir, çünkü oyun sana yardımcı olacak parçalar verme eğilimindedir."]},
            {"h": "Zincir için satır hazırlamak", "p": [
                "Komboyu sürdürmek için neredeyse bitmiş satırlara ihtiyacın var. Birkaç satır ya da sütunu birer blok şekli eksik bırakmayı hedefle; böylece sıradaki takım bunlardan birini ya da ikisini tamamlayan bir şey sunar.",
                "Satırlarla sütunlarla aynı anda çalış. Tahtanın köşesine oturan bir parça bir satıra ve bir sütuna yardım eder; yani bir yöndeki temizleme çoğu zaman diğerini de yaklaştırır. Geri kalanı boş bırakıp tek uzun bir şeridi tamamen doldurmaktan kaçın; yalnızca tek bir temizlemeye yarar.",
                "Sessiz hamleleri bilerek kullan. Bir şey temizlemeden parça koymak zorundaysan onu açık alanın ortasına değil, bir satırı yaklaştıran ya da kenarı toparlayan yere koy. Kombo bozulmadan önce iki sessiz hamlen var; onları hazırlığa harca."]},
            {"h": "Günlük meydan okuma ve devam etme", "p": [
                "Günlük meydan okumada herkese tarihten kurulan aynı parça takımı dizisi gelir. Günlük oyunu aynı parçalarla yeniden başlatabilirsin ve günün en iyi skorun saklanır. Bu, alıştırma için iyi bir yer: hangi parçaların geleceğini ve nereye yer ayıracağını öğrenirsin. Günün ilk oyunu 50 deneyim puanı bonusu da verir; günlük skorlar klasik oyunlardan ayrı kendi liderlik tablosuna gider.",
                "Oyun bittiğinde, her oyunda bir kez isteğe bağlı bir reklam izleyip devam edebilirsin. Bu, en dolu iki satırı ve en dolu iki sütunu temizler ve sana yeni bir takım verir. Bunu en çok zaten uzun bir serideysen kullan; ek hamleler yüksek çarpanla puan kazanmaya devam etmeni sağlar.",
                "Son olarak günlük görevler sana belli bir kombo ya da belli bir skora ulaşmak gibi küçük hedefler verir. Kombo 3 ya da 4 gibi bir hedef, bu rehberdeki alışkanlıkları denemek için iyi bir neden."]},
        ],
        "faq": [
            ["Cubbles'ta puanlar nasıl hesaplanır?", "Yerleştirilen her kare bir puan verir. Bir temizleme, satır sayısının karesinin 10 katı çarpı kombo sayısı kadar ekler; boşalan tahta 100 ekler."],
            ["Kombo bitmeden temizleme yapmadan kaç hamle yapabilirim?", "İki. Art arda üçüncü hamle de bir şey temizlemezse kombo sıfırlanır."],
            ["Aynı anda iki satır temizlemek mi, kombo kurmak mı daha iyi?", "Başta çift temizleme genelde kazanır. Uzun bir seride kombo her temizlemeyi çarptığı için onu korumak daha değerlidir."],
            ["Günlük meydan okumada aynı parçalar mı gelir?", "Evet, tarihten gelirler ve normalde her oyuncuda aynıdır. Günlük oyunu aynı parçalarla yeniden başlatabilirsin."],
        ],
    },
    "es": {
        "slug": "puzle-de-bloques-combos-y-estrategia-de-puntuacion",
        "title": "Puzle de bloques: combos, rachas y planificación para puntuar alto",
        "desc": "Cómo funciona la puntuación en un puzle de bloques, por qué compensa limpiar varias líneas a la vez, cómo mantener un combo y planificar tres piezas.",
        "intro": "Cuando ya conoces lo básico de un puzle de bloques, el siguiente salto de puntuación llega al entender los números que hay detrás. Aquí explicamos cómo cuenta los puntos Cubbles, por qué un combo vale tanto y cómo planificar de antemano un grupo de tres piezas.",
        "sections": [
            {"h": "Cómo se cuentan los puntos", "p": [
                "Cada pieza que colocas da un punto por cada casilla que cubre. Eso es poco. La puntuación de verdad viene de limpiar líneas. Una limpieza vale 10 veces el cuadrado del número de líneas, multiplicado por tu número de combo actual.",
                "Lo que importa es que el número de líneas se eleva al cuadrado. Una línea vale 10, dos líneas a la vez valen 40, tres líneas valen 90 y cuatro líneas valen 160, todo ello antes del multiplicador de combo. Limpiar dos líneas juntas es cuatro veces mejor que limpiar una, no el doble.",
                "Si vacías todo el tablero con una limpieza, recibes una bonificación de limpieza perfecta de 100 puntos extra. Es una buena sorpresa, pero pocas veces supera a los combos constantes, así que no organices toda tu partida alrededor de ella."]},
            {"h": "Qué es realmente un combo", "p": [
                "Un combo cuenta cuántos movimientos seguidos han limpiado al menos una línea. Tu primera limpieza es el combo 1, el siguiente movimiento que limpia es el combo 2, y así sucesivamente. Cada vez que limpias, el número sube y el multiplicador también.",
                "La racha aguanta un número limitado de movimientos tranquilos. Puedes colocar dos piezas sin limpiar nada, pero si un tercer movimiento seguido no limpia nada, el combo vuelve a cero. En Cubbles un grupo tiene tres piezas, así que en la práctica necesitas al menos una limpieza en cada grupo para mantener la racha. El juego muestra cuántas oportunidades te quedan.",
                "Compara dos formas de conseguir las mismas líneas. Limpiar una sola línea cinco movimientos seguidos da 10, 20, 30, 40 y 50, un total de 150 por las limpiezas. Esas mismas cinco líneas sueltas, limpiadas una a una con el combo roto entre medias, dan solo 10 cada una. El multiplicador premia la paciencia y el ritmo más que la suerte."]},
            {"h": "Dos líneas a la vez superan a dos combos", "p": [
                "Como las líneas se elevan al cuadrado y el combo es un simple multiplicador, una limpieza mayor suele ganar a una racha más larga al principio. Con combo 1, dos líneas a la vez dan 40. Dos líneas sueltas con combos 1 y 2 dan solo 30. Tres líneas con combo 2 dan 180.",
                "Al final de una racha larga, el equilibrio cambia. Con combo 5, una sola línea ya vale 50 y una doble vale 200. Una racha larga hace que cada limpieza posterior valga más, así que protegerla compensa un pequeño sacrificio en la forma del tablero.",
                "Un hábito útil es preguntarse antes de cada movimiento: ¿puede esta pieza completar más de una línea y la siguiente pieza seguirá limpiando algo? Si la respuesta a ambas es sí, es un movimiento fuerte."]},
            {"h": "Planifica todo el grupo, no una pieza", "p": [
                "Siempre ves tres piezas a la vez, y Cubbles se asegura de que las tres puedan colocarse en algún orden. Eso te da información. Antes de mover, mira las tres piezas juntas e imagina dónde podría ir cada una.",
                "A menudo una pieza prepara una línea para otra. Una pieza corta puede dejar un hueco en una fila, y la pieza larga que tienes en la mano rellena justo ese hueco y limpia la línea. Colocarlas en el orden contrario puede no funcionar en absoluto.",
                "Como las piezas no se pueden girar, las formas que tienes son las que debes usar. Busca colocaciones que limpien líneas con la pieza más difícil primero, deja la más fácil para el final y mira cómo quedará el tablero cuando hayas colocado las tres y llegue un grupo nuevo.",
                "Las piezas se eligen con pesos. Las piezas pequeñas son más frecuentes cuando el tablero se llena y también en los primeros movimientos de una partida. Un tablero lleno no es una causa perdida, porque el juego tiende a darte piezas que ayudan."]},
            {"h": "Preparar líneas para encadenar", "p": [
                "Para mantener un combo necesitas líneas casi terminadas. Procura dejar varias filas o columnas a las que les falte solo una forma de bloque, de modo que el siguiente grupo ofrezca algo que complete una o dos de ellas.",
                "Trabaja con filas y columnas a la vez. Una pieza situada en la esquina del tablero ayuda a una fila y a una columna, así que una limpieza en una dirección suele acercar la otra. Evita rellenar por completo una sola franja larga dejando vacío el resto, porque solo sirve para una limpieza.",
                "Usa los movimientos tranquilos con intención. Cuando tengas que colocar una pieza sin limpiar, ponla donde acerque una línea o ordene un borde, no en medio del espacio abierto. Tienes dos movimientos tranquilos antes de que se rompa el combo; gástalos en preparar."]},
            {"h": "Reto diario y continuar", "p": [
                "En el reto diario todos reciben la misma secuencia de grupos de piezas, construida a partir de la fecha. Puedes empezar de nuevo la partida diaria con las mismas piezas y se conserva tu mejor puntuación del día. Es un buen sitio para practicar: aprendes qué piezas vienen y para qué guardar espacio. La primera partida del día da además una bonificación de 50 puntos de experiencia, y las puntuaciones diarias van a su propia clasificación, separada de las partidas clásicas.",
                "Si una partida termina, puedes ver un anuncio opcional una vez por partida para continuar. Limpia las dos filas más llenas y las dos columnas más llenas, y te da un grupo nuevo. Úsalo cuando ya estés metido en una racha larga, porque los movimientos extra te permiten seguir sumando con un multiplicador alto.",
                "Por último, las misiones diarias te dan pequeños objetivos, como alcanzar cierto combo o cierta puntuación. Un objetivo como un combo de 3 o 4 es una buena razón para practicar los hábitos de esta guía."]},
        ],
        "faq": [
            ["¿Cómo se calculan los puntos en Cubbles?", "Cada casilla colocada da un punto. Una limpieza suma 10 veces el cuadrado del número de líneas por tu número de combo, y un tablero vacío suma 100."],
            ["¿Cuántos movimientos puedo hacer sin limpiar antes de que termine el combo?", "Dos. Si un tercer movimiento seguido no limpia nada, el combo se reinicia."],
            ["¿Es mejor limpiar dos líneas a la vez o construir un combo?", "Al principio suele ganar la limpieza doble. En una racha larga, proteger el combo vale más porque cada limpieza se multiplica."],
            ["¿Recibo las mismas piezas en el reto diario?", "Sí, salen de la fecha y normalmente son iguales para todos los jugadores. Puedes empezar de nuevo la partida diaria con las mismas piezas."],
        ],
    },
    "pt": {
        "slug": "quebra-cabeca-de-blocos-combos-e-estrategia-de-pontuacao",
        "title": "Quebra-cabeça de blocos: combos, sequências e planejamento",
        "desc": "Como funciona a pontuação num quebra-cabeça de blocos, por que limpar várias linhas de uma vez compensa, como manter um combo e planejar três peças.",
        "intro": "Depois que você conhece o básico de um quebra-cabeça de blocos, o próximo salto de pontuação vem de entender os números por trás dele. Aqui explicamos como o Cubbles conta os pontos, por que um combo vale tanto e como planejar com antecedência um conjunto de três peças.",
        "sections": [
            {"h": "Como os pontos são contados", "p": [
                "Cada peça que você coloca dá um ponto por cada quadrado que ela cobre. Isso é pouco. A pontuação de verdade vem de limpar linhas. Uma limpeza vale 10 vezes o quadrado do número de linhas, multiplicado pelo seu número de combo atual.",
                "O que importa é que o número de linhas é elevado ao quadrado. Uma linha vale 10, duas linhas ao mesmo tempo valem 40, três linhas valem 90 e quatro linhas valem 160, tudo isso antes do multiplicador do combo. Limpar duas linhas juntas é quatro vezes melhor do que limpar uma, não o dobro.",
                "Se você esvaziar o tabuleiro inteiro com uma limpeza, ganha um bônus de limpeza perfeita de 100 pontos extras. É uma boa surpresa, mas raramente supera combos constantes, então não organize a partida toda em torno dela."]},
            {"h": "O que um combo realmente é", "p": [
                "Um combo conta quantas jogadas seguidas limparam pelo menos uma linha. Sua primeira limpeza é o combo 1, a próxima jogada que limpa é o combo 2, e assim por diante. Cada vez que você limpa, o número sobe, e o multiplicador também.",
                "A sequência suporta um número limitado de jogadas tranquilas. Você pode colocar duas peças sem limpar nada, mas, se uma terceira jogada seguida não limpar nada, o combo volta a zero. No Cubbles um conjunto tem três peças, então, na prática, você precisa de pelo menos uma limpeza em cada conjunto para manter a sequência. O jogo mostra quantas chances ainda restam.",
                "Compare duas maneiras de conseguir as mesmas linhas. Limpar uma única linha cinco jogadas seguidas dá 10, 20, 30, 40 e 50, um total de 150 pelas limpezas. Essas mesmas cinco linhas isoladas, limpas uma a uma com o combo quebrado no meio, dão só 10 cada uma. O multiplicador recompensa a paciência e o ritmo mais do que a sorte."]},
            {"h": "Duas linhas valem mais do que dois combos", "p": [
                "Como as linhas são elevadas ao quadrado e o combo é um multiplicador simples, uma limpeza maior costuma vencer uma sequência mais longa no início. Com combo 1, duas linhas ao mesmo tempo dão 40. Duas linhas isoladas com combos 1 e 2 dão só 30. Três linhas com combo 2 dão 180.",
                "No fim de uma sequência longa, o equilíbrio muda. Com combo 5, uma única linha já vale 50 e uma dupla vale 200. Uma sequência longa faz cada limpeza seguinte valer mais, então protegê-la compensa um pequeno sacrifício na forma do tabuleiro.",
                "Um hábito útil é perguntar antes de cada jogada: esta peça pode completar mais de uma linha, e a próxima peça ainda vai limpar alguma coisa? Se a resposta às duas for sim, é uma jogada forte."]},
            {"h": "Planeje o conjunto inteiro, não uma peça", "p": [
                "Você sempre vê três peças ao mesmo tempo, e o Cubbles garante que as três possam ser colocadas em alguma ordem. Isso dá informação. Antes de jogar, olhe as três peças juntas e imagine onde cada uma poderia ir.",
                "Muitas vezes uma peça prepara uma linha para outra. Uma peça curta pode deixar um vazio em uma fileira, e a peça longa que você tem na mão preenche exatamente esse vazio e limpa a linha. Colocá-las na ordem contrária pode simplesmente não funcionar.",
                "Como as peças não podem ser giradas, as formas que você tem são as que precisa usar. Procure posições que limpem linhas com a peça mais difícil primeiro, deixe a mais fácil para o fim e veja como o tabuleiro ficará depois de colocar as três e chegar um conjunto novo.",
                "As peças são escolhidas com pesos. As peças pequenas ficam mais frequentes à medida que o tabuleiro enche e também nas primeiras jogadas de uma partida. Um tabuleiro cheio não é uma causa perdida, porque o jogo tende a dar peças que ajudam."]},
            {"h": "Preparar linhas para encadear", "p": [
                "Para manter um combo, você precisa de linhas quase prontas. Procure deixar várias fileiras ou colunas faltando só uma forma de bloco, para que o próximo conjunto ofereça algo que complete uma ou duas delas.",
                "Trabalhe com fileiras e colunas ao mesmo tempo. Uma peça no canto do tabuleiro ajuda uma fileira e uma coluna, então uma limpeza em uma direção muitas vezes aproxima a outra. Evite preencher por completo uma única faixa longa deixando o resto vazio, porque isso só serve para uma limpeza.",
                "Use as jogadas tranquilas de propósito. Quando precisar colocar uma peça sem limpar, coloque-a onde aproxime uma linha ou arrume uma borda, e não no meio do espaço aberto. Você tem duas jogadas tranquilas antes de o combo quebrar; gaste-as na preparação."]},
            {"h": "Desafio diário e continuar", "p": [
                "No desafio diário, todos recebem a mesma sequência de conjuntos de peças, construída a partir da data. Você pode reiniciar a partida diária com as mesmas peças, e a sua melhor pontuação do dia é mantida. É um bom lugar para praticar: você aprende quais peças vêm e para o que guardar espaço. A primeira partida do dia também dá um bônus de 50 pontos de experiência, e as pontuações diárias vão para o seu próprio ranking, separado das partidas clássicas.",
                "Quando uma partida termina, você pode assistir a um anúncio opcional uma vez por partida para continuar. Ele limpa as duas fileiras mais cheias e as duas colunas mais cheias e dá um conjunto novo. Use quando já estiver em uma sequência longa, porque as jogadas extras permitem continuar somando com um multiplicador alto.",
                "Por fim, as missões diárias dão pequenas metas, como alcançar certo combo ou certa pontuação. Uma meta como combo 3 ou 4 é um bom motivo para praticar os hábitos deste guia."]},
        ],
        "faq": [
            ["Como os pontos são calculados no Cubbles?", "Cada quadrado colocado dá um ponto. Uma limpeza soma 10 vezes o quadrado do número de linhas vezes o seu número de combo, e um tabuleiro vazio soma 100."],
            ["Quantas jogadas posso fazer sem limpar antes de o combo acabar?", "Duas. Se uma terceira jogada seguida não limpar nada, o combo é reiniciado."],
            ["É melhor limpar duas linhas de uma vez ou montar um combo?", "No início, a limpeza dupla costuma vencer. Em uma sequência longa, proteger o combo vale mais porque cada limpeza é multiplicada."],
            ["Recebo as mesmas peças no desafio diário?", "Sim, elas vêm da data e normalmente são iguais para todos os jogadores. Você pode reiniciar a partida diária com as mesmas peças."],
        ],
    },
}
