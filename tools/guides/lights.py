# Rehber: Uykucu Yüzler (Logiclings) - ışıkları kovala yöntemi
GUIDE = {
    "id": "lights", "app": "logiclings", "date": "2026-11-07",
    "en": {
        "slug": "sleepy-faces-strategy-chase-the-lights",
        "title": "Sleepy Faces Strategy: Chase the Lights Method",
        "desc": "How to solve the Sleepy Faces puzzle: the tap rules, why each face needs at most one tap, and the row-by-row “chase the lights” method with a 5x5 cheat sheet.",
        "intro": "Sleepy Faces is a light-toggling puzzle: tapping a face flips it and its four neighbors, and you must wake every sleepy face. It looks random, but a simple method always works.",
        "sections": [
            {"h": "The rules", "p": ["Each face is awake (yellow) or asleep (blue). Tapping a face flips that face and the faces directly above, below, left and right of it. Wake every face to win."], "ul": ["Tapping the same face twice cancels out, so every face needs at most one tap.", "The order of your taps does not matter, only which faces you tap.", "Every board in Logiclings can be solved."]},
            {"h": "Chase the lights, row by row", "p": ["Work from the top row down. Whenever a face in a row is still asleep, tap the face directly below it. That wakes it without touching any row above."], "ul": ["Start at the top left and go left to right, then move to the next row.", "After you finish the second-to-last row, every row except the bottom one is awake.", "If the bottom row is fully awake too, you are done."]},
            {"h": "If the bottom row still has sleepy faces (5x5 cheat sheet)", "p": ["The leftover pattern in the bottom row tells you which top-row faces to tap first. Undo back to the start (or press Reset), tap those top-row faces, then chase the lights again. Write sleepy as 1 and awake as 0, columns from left to right:"], "ul": ["00111: tap column 4 first", "01010: tap columns 1 and 4 first", "01101: tap column 1 first", "10001: tap columns 1 and 2 first", "10110: tap column 5 first", "11011: tap column 3 first", "11100: tap column 2 first"]},
            {"h": "Other board sizes", "p": ["On 6x6 and 7x7 boards every starting position has exactly one solution, so there is only one set of faces to tap. On 4x4 and 5x5 boards there can be several solutions, and Logiclings counts the one with the fewest taps as the best."]},
            {"h": "Hints that teach", "p": ["In Logiclings a hint uses the chase method: it taps the face below the first sleepy face and tells you why, so every hint is also a small lesson."]},
        ],
        "faq": [
            ["Is every Sleepy Faces board solvable?", "In Logiclings, yes. Every puzzle is built so that it can be solved."],
            ["What is the fewest number of taps?", "It depends on the board. The result screen shows your taps next to the fewest possible, so you can aim for it."],
            ["Do I have to use the method?", "No. It is just the most reliable way to solve any board. With practice you will start to see patterns and skip steps."],
        ],
    },
    "tr": {
        "slug": "uykucu-yuzler-stratejisi-isiklari-kovala",
        "title": "Uykucu Yüzler Stratejisi: Işıkları Kovala Yöntemi",
        "desc": "Uykucu Yüzler bulmacasını çözme: dokunma kuralları, her yüze neden en fazla bir kez dokunulduğu ve satır satır “ışıkları kovala” yöntemi, 5x5 kopya kâğıdıyla.",
        "intro": "Uykucu Yüzler bir ışık çevirme bulmacasıdır: bir yüze dokununca o ve dört komşusu durum değiştirir; amaç uyuyan bütün yüzleri uyandırmaktır. Rastgele görünür ama her zaman işe yarayan basit bir yöntem var.",
        "sections": [
            {"h": "Kurallar", "p": ["Her yüz uyanık (sarı) ya da uykuda (mavi). Bir yüze dokununca o yüz ve hemen üstündeki, altındaki, solundaki, sağındaki yüzler durum değiştirir. Hepsini uyandırınca kazanırsın."], "ul": ["Aynı yüze iki kez dokunmak birbirini siler; bu yüzden her yüze en fazla bir kez dokunmak yeter.", "Dokunma sırası önemli değil, yalnızca hangi yüzlere dokunduğun önemli.", "Logiclings'teki her tahta çözülebilir."]},
            {"h": "Işıkları satır satır kovala", "p": ["Üst satırdan başlayıp aşağı doğru ilerle. Bir satırda hâlâ uyuyan bir yüz varsa, hemen ALTINDAKİ yüze dokun. Bu, üstteki satırlara dokunmadan o yüzü uyandırır."], "ul": ["Sol üstten başla, soldan sağa git, sonra bir alt satıra geç.", "Sondan bir önceki satırı bitirince, en alt satır dışındaki tüm satırlar uyanık olur.", "En alt satır da tamamen uyanıksa işin bitti."]},
            {"h": "Son satırda hâlâ uyuyan varsa (5x5 kopya kâğıdı)", "p": ["En alt satırda kalan desen, en başta üst satırdaki hangi yüzlere dokunman gerektiğini söyler. Başa dön (Geri al ya da Sıfırla), o üst satır yüzlerine dokun, sonra ışıkları yeniden kovala. Uyuyanı 1, uyanığı 0 yaz; sütunlar soldan sağa:"], "ul": ["00111: önce 4. sütuna dokun", "01010: önce 1. ve 4. sütunlara dokun", "01101: önce 1. sütuna dokun", "10001: önce 1. ve 2. sütunlara dokun", "10110: önce 5. sütuna dokun", "11011: önce 3. sütuna dokun", "11100: önce 2. sütuna dokun"]},
            {"h": "Diğer tahta boyutları", "p": ["6x6 ve 7x7 tahtalarda her başlangıç durumunun tam olarak bir çözümü vardır; yani dokunulacak tek bir yüz kümesi var. 4x4 ve 5x5 tahtalarda birden çok çözüm olabilir ve Logiclings en az dokunuşlu olanı en iyi sayar."]},
            {"h": "Öğreten ipuçları", "p": ["Logiclings'te ipucu kovalama yöntemini kullanır: ilk uyuyan yüzün altındaki yüze dokunur ve nedenini söyler; yani her ipucu küçük bir derstir."]},
        ],
        "faq": [
            ["Her Uykucu Yüzler tahtası çözülebilir mi?", "Logiclings'te evet. Her bulmaca çözülebilecek şekilde üretilir."],
            ["En az kaç dokunuşla çözülür?", "Tahtaya göre değişir. Sonuç ekranında dokunuş sayını mümkün olan en azla birlikte görürsün; ona yaklaşmaya çalışabilirsin."],
            ["Yöntemi kullanmak zorunda mıyım?", "Hayır. Yalnızca her tahtada en güvenilir yoldur. Pratik yaptıkça desenleri görüp adımları atlamaya başlarsın."],
        ],
    },
    "es": {
        "slug": "caras-dormilonas-estrategia-perseguir-las-luces",
        "title": "Caras Dormilonas: Estrategia de Perseguir las Luces",
        "desc": "Cómo resolver Caras Dormilonas: las reglas, por qué cada cara necesita como mucho un toque y el método de «perseguir las luces» fila por fila, con una tabla para 5x5.",
        "intro": "Caras Dormilonas es un puzzle de interruptores: al tocar una cara, ella y sus cuatro vecinas cambian, y debes despertar todas las caras dormidas. Parece aleatorio, pero hay un método sencillo que siempre funciona.",
        "sections": [
            {"h": "Las reglas", "p": ["Cada cara está despierta (amarilla) o dormida (azul). Al tocar una cara cambian esa cara y las que están justo arriba, abajo, a la izquierda y a la derecha. Gana quien despierta todas."], "ul": ["Tocar la misma cara dos veces se cancela, así que cada cara necesita como mucho un toque.", "El orden de los toques no importa, solo qué caras tocas.", "Todos los tableros de Logiclings se pueden resolver."]},
            {"h": "Perseguir las luces, fila por fila", "p": ["Trabaja de la fila superior hacia abajo. Siempre que una cara de la fila siga dormida, toca la cara que está justo debajo. Así la despiertas sin tocar ninguna fila de arriba."], "ul": ["Empieza arriba a la izquierda y ve de izquierda a derecha; luego pasa a la fila siguiente.", "Al terminar la penúltima fila, todas las filas menos la última están despiertas.", "Si la última fila también está despierta, has terminado."]},
            {"h": "Si en la última fila quedan caras dormidas (tabla para 5x5)", "p": ["El patrón que queda en la última fila te dice qué caras de la primera fila debes tocar al principio. Vuelve al inicio (Deshacer o Reiniciar), toca esas caras y vuelve a perseguir las luces. Escribe dormida como 1 y despierta como 0, columnas de izquierda a derecha:"], "ul": ["00111: toca primero la columna 4", "01010: toca primero las columnas 1 y 4", "01101: toca primero la columna 1", "10001: toca primero las columnas 1 y 2", "10110: toca primero la columna 5", "11011: toca primero la columna 3", "11100: toca primero la columna 2"]},
            {"h": "Otros tamaños", "p": ["En tableros de 6x6 y 7x7 cada posición inicial tiene exactamente una solución, así que solo hay un conjunto de caras que tocar. En 4x4 y 5x5 puede haber varias soluciones, y Logiclings considera mejor la de menos toques."]},
            {"h": "Pistas que enseñan", "p": ["En Logiclings una pista usa el método: toca la cara de debajo de la primera cara dormida y te explica por qué, así que cada pista es también una pequeña lección."]},
        ],
        "faq": [
            ["¿Todos los tableros de Caras Dormilonas se pueden resolver?", "En Logiclings, sí. Cada puzzle se genera para que tenga solución."],
            ["¿Cuál es el mínimo de toques?", "Depende del tablero. En la pantalla de resultado ves tus toques junto al mínimo posible, para que intentes igualarlo."],
            ["¿Tengo que usar el método?", "No. Es solo la forma más fiable de resolver cualquier tablero. Con práctica verás patrones y te saltarás pasos."],
        ],
    },
    "pt": {
        "slug": "rostos-sonolentos-estrategia-perseguir-as-luzes",
        "title": "Rostos Sonolentos: Estratégia de Perseguir as Luzes",
        "desc": "Como resolver Rostos Sonolentos: as regras, por que cada rosto precisa de no máximo um toque e o método de «perseguir as luzes» linha por linha, com uma tabela para 5x5.",
        "intro": "Rostos Sonolentos é um quebra-cabeça de interruptores: ao tocar um rosto, ele e seus quatro vizinhos mudam, e você precisa acordar todos os rostos sonolentos. Parece aleatório, mas existe um método simples que sempre funciona.",
        "sections": [
            {"h": "As regras", "p": ["Cada rosto está acordado (amarelo) ou dormindo (azul). Ao tocar um rosto, ele e os rostos logo acima, abaixo, à esquerda e à direita mudam. Você vence quando todos estiverem acordados."], "ul": ["Tocar o mesmo rosto duas vezes se cancela, então cada rosto precisa de no máximo um toque.", "A ordem dos toques não importa, só quais rostos você toca.", "Todos os tabuleiros do Logiclings podem ser resolvidos."]},
            {"h": "Perseguir as luzes, linha por linha", "p": ["Trabalhe da linha de cima para baixo. Sempre que um rosto da linha ainda estiver dormindo, toque no rosto logo abaixo dele. Assim você o acorda sem mexer em nenhuma linha de cima."], "ul": ["Comece no canto superior esquerdo e vá da esquerda para a direita; depois passe à linha seguinte.", "Ao terminar a penúltima linha, todas as linhas, exceto a última, estarão acordadas.", "Se a última linha também estiver acordada, você terminou."]},
            {"h": "Se a última linha ainda tiver rostos dormindo (tabela para 5x5)", "p": ["O padrão que sobra na última linha diz quais rostos da primeira linha você deve tocar no início. Volte ao começo (Desfazer ou Reiniciar), toque neles e persiga as luzes de novo. Escreva dormindo como 1 e acordado como 0, colunas da esquerda para a direita:"], "ul": ["00111: toque primeiro na coluna 4", "01010: toque primeiro nas colunas 1 e 4", "01101: toque primeiro na coluna 1", "10001: toque primeiro nas colunas 1 e 2", "10110: toque primeiro na coluna 5", "11011: toque primeiro na coluna 3", "11100: toque primeiro na coluna 2"]},
            {"h": "Outros tamanhos", "p": ["Em tabuleiros 6x6 e 7x7 cada posição inicial tem exatamente uma solução, então há um só conjunto de rostos para tocar. Em 4x4 e 5x5 pode haver várias soluções, e o Logiclings considera melhor a de menos toques."]},
            {"h": "Dicas que ensinam", "p": ["No Logiclings uma dica usa o método: toca o rosto abaixo do primeiro rosto dormindo e explica por quê, então cada dica também é uma pequena lição."]},
        ],
        "faq": [
            ["Todo tabuleiro de Rostos Sonolentos tem solução?", "No Logiclings, sim. Cada quebra-cabeça é gerado para poder ser resolvido."],
            ["Qual é o mínimo de toques?", "Depende do tabuleiro. Na tela de resultado você vê seus toques ao lado do mínimo possível, para tentar igualar."],
            ["Preciso usar o método?", "Não. É só a forma mais confiável de resolver qualquer tabuleiro. Com prática você vai enxergar padrões e pular etapas."],
        ],
    },
}
