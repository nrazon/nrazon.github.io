# Rehber: Koyun Ağılları (Logiclings) - dikdörtgen bölme bulmacası
GUIDE = {
    "id": "pens", "app": "logiclings", "date": "2026-11-24",
    "en": {
        "slug": "sheep-pens-rectangle-puzzle-guide",
        "title": "Sheep Pens: How to Solve Rectangle Division Puzzles",
        "desc": "How to play Sheep Pens, a logic puzzle where you split a grid into rectangular pens: the rules, the first moves to look for and how hints explain the logic.",
        "intro": "Sheep Pens is a rectangle puzzle. Some squares hold a sheep with a number, and you split the whole grid into rectangular pens so that every pen holds exactly one sheep and covers as many squares as its number. It is calm, visual and fully solvable by logic.",
        "sections": [
            {"h": "The rules", "ul": [
                "Drag your finger from one square to another to draw a rectangle. Tap a pen to erase it.",
                "Every pen must contain exactly one sheep, and its area (the number of squares it covers) must equal the number on that sheep.",
                "Pens cannot overlap and must be rectangles. When every square belongs to a correct pen, the puzzle is solved.",
                "Every puzzle has exactly one solution, so you never need to guess."]},
            {"h": "Where to start", "ul": [
                "A sheep with a 1 is its own pen. Draw it first.",
                "Look at the biggest numbers. A 6, for example, can only be a 1x6, 2x3, 3x2 or 6x1 rectangle, and walls and other sheep rule most of those out.",
                "Squares that only one sheep can reach are forced: if just one pen can possibly cover a square, it belongs to that pen.",
                "Two sheep close together split the space between them. Count how many squares each one needs and see where the border has to fall."]},
            {"h": "Keep every square in play", "p": ["The trick that solves harder grids is to ask, for each empty square, which sheep could still reach it. A pen cannot swallow another sheep and cannot leave the grid, and its size is fixed by the number. When only one option is left for a square, the pen is decided. When none is left, an earlier pen was wrong, so use Undo."]},
            {"h": "Sheep Pens in Logiclings", "p": ["Logiclings offers grids from 5x5 to 9x9 in three levels. Every puzzle is checked by a solver, so it always has one answer. The hint button explains the exact reason a pen is forced, in words, instead of just drawing it for you. Sheep Pens is one of the seven puzzle types in the app and one of the daily puzzles."]},
        ],
        "faq": [
            ["Can a pen have two sheep?", "No. Every pen holds exactly one sheep, and its size must match the number on it."],
            ["Do I have to guess?", "No. Every puzzle has a single solution that can be found by logic alone."],
            ["How do I remove a pen I drew?", "Tap the pen. You can also use Undo or Reset."],
            ["Which grid sizes are there?", "From 5x5 to 9x9, in Easy, Medium and Hard."],
        ],
    },
    "tr": {
        "slug": "koyun-agillari-dikdortgen-bulmacasi-rehberi",
        "title": "Koyun Ağılları: Dikdörtgen Bölme Bulmacası Nasıl Çözülür",
        "desc": "Tahtayı dikdörtgen ağıllara böldüğün mantık bulmacası Koyun Ağılları nasıl oynanır: kurallar, ilk hamleler ve ipuçlarının mantığı nasıl açıkladığı.",
        "intro": "Koyun Ağılları bir dikdörtgen bulmacasıdır. Bazı karelerde sayılı bir koyun durur; tahtanın tamamını, her ağılda tam bir koyun olacak ve ağılın alanı koyunun üstündeki sayıya eşit olacak şekilde dikdörtgen ağıllara bölersin. Sakin, görsel ve tamamen mantıkla çözülür.",
        "sections": [
            {"h": "Kurallar", "ul": [
                "Parmağını bir kareden diğerine sürükleyerek dikdörtgen çiz. Bir ağıla dokunursan silinir.",
                "Her ağılda tam bir koyun olmalı ve ağılın alanı (kapladığı kare sayısı) koyunun üstündeki sayıya eşit olmalı.",
                "Ağıllar üst üste binemez ve dikdörtgen olmalıdır. Her kare doğru bir ağılın parçası olunca bulmaca çözülmüş olur.",
                "Her bulmacanın tek çözümü vardır, yani tahmin etmen gerekmez."]},
            {"h": "Nereden başlamalı", "ul": [
                "1 yazan koyun kendi başına bir ağıldır. Önce onu çiz.",
                "En büyük sayılara bak. Örneğin 6, yalnız 1x6, 2x3, 3x2 ya da 6x1 dikdörtgeni olabilir; duvarlar ve diğer koyunlar çoğunu eler.",
                "Yalnız tek koyunun ulaşabildiği kareler zorunludur: bir kareyi kapsayabilecek tek ağıl varsa kare o ağıla aittir.",
                "Birbirine yakın iki koyun aradaki boşluğu paylaşır. Her birinin kaç kareye ihtiyacı olduğunu say ve sınırın nereye düşmesi gerektiğini bul."]},
            {"h": "Her kareyi hesaba kat", "p": ["Zor tahtaları çözen püf nokta şudur: her boş kare için hangi koyunun hâlâ ona ulaşabileceğini sor. Ağıl başka bir koyunu yutamaz, tahtadan taşamaz ve büyüklüğü sayıyla sabittir. Bir kare için tek seçenek kalınca ağıl belli olur. Hiç seçenek kalmadıysa önceki bir ağıl yanlıştır; Geri al'ı kullan."]},
            {"h": "Logiclings'te Koyun Ağılları", "p": ["Logiclings 5x5'ten 9x9'a kadar üç seviyede tahta sunar. Her bulmaca bir çözücüyle denetlenir, yani tek cevabı vardır. İpucu düğmesi bir ağılın neden zorunlu olduğunu çizmekle kalmaz, sözle açıklar. Koyun Ağılları uygulamadaki yedi bulmaca türünden biridir ve günlük bulmacalara girer."]},
        ],
        "faq": [
            ["Bir ağılda iki koyun olabilir mi?", "Hayır. Her ağılda tam bir koyun olmalı ve büyüklüğü üstündeki sayıyla eşleşmeli."],
            ["Tahmin etmem gerekir mi?", "Hayır. Her bulmacanın yalnızca mantıkla bulunan tek bir çözümü vardır."],
            ["Çizdiğim ağılı nasıl silerim?", "Ağıla dokun. Geri al ya da Sıfırla da kullanabilirsin."],
            ["Hangi tahta boyutları var?", "5x5'ten 9x9'a kadar; Kolay, Orta ve Zor seviyeleriyle."],
        ],
    },
    "es": {
        "slug": "corrales-puzzle-de-rectangulos-guia",
        "title": "Corrales: Cómo resolver puzzles de dividir en rectángulos",
        "desc": "Cómo jugar Corrales, un puzzle de lógica donde divides la cuadrícula en corrales rectangulares: reglas, primeros movimientos y cómo las pistas explican la lógica.",
        "intro": "Corrales es un puzzle de rectángulos. Algunas casillas tienen una oveja con un número, y debes dividir toda la cuadrícula en corrales rectangulares de modo que cada corral tenga exactamente una oveja y cubra tantas casillas como indica su número. Es tranquilo, visual y se resuelve solo con lógica.",
        "sections": [
            {"h": "Las reglas", "ul": [
                "Arrastra el dedo de una casilla a otra para dibujar un rectángulo. Toca un corral para borrarlo.",
                "Cada corral debe tener exactamente una oveja y su área (las casillas que cubre) debe ser igual al número de esa oveja.",
                "Los corrales no pueden solaparse y deben ser rectángulos. Cuando cada casilla pertenece a un corral correcto, el puzzle está resuelto.",
                "Cada puzzle tiene una única solución, así que nunca hace falta adivinar."]},
            {"h": "Por dónde empezar", "ul": [
                "Una oveja con un 1 es su propio corral. Dibújala primero.",
                "Mira los números más grandes. Un 6, por ejemplo, solo puede ser un rectángulo de 1x6, 2x3, 3x2 o 6x1, y los bordes y otras ovejas descartan casi todos.",
                "Las casillas que solo una oveja puede alcanzar son forzadas: si un único corral puede cubrir una casilla, esa casilla es suya.",
                "Dos ovejas cercanas se reparten el espacio entre ellas. Cuenta cuántas casillas necesita cada una y averigua dónde debe caer el límite."]},
            {"h": "Ten en cuenta cada casilla", "p": ["El truco para las cuadrículas difíciles es preguntarse, para cada casilla vacía, qué ovejas aún pueden alcanzarla. Un corral no puede tragarse otra oveja, no puede salirse de la cuadrícula y su tamaño lo fija el número. Cuando solo queda una opción para una casilla, el corral está decidido. Si no queda ninguna, algún corral anterior era incorrecto; usa Deshacer."]},
            {"h": "Corrales en Logiclings", "p": ["Logiclings ofrece cuadrículas de 5x5 a 9x9 en tres niveles. Cada puzzle se comprueba con un solucionador, así que siempre tiene una sola respuesta. El botón de pista explica con palabras por qué un corral es forzado, en lugar de dibujarlo sin más. Corrales es uno de los siete tipos de puzzle de la app y entra en los puzzles diarios."]},
        ],
        "faq": [
            ["¿Puede un corral tener dos ovejas?", "No. Cada corral tiene exactamente una oveja y su tamaño debe coincidir con el número."],
            ["¿Tengo que adivinar?", "No. Cada puzzle tiene una única solución que se encuentra solo con lógica."],
            ["¿Cómo borro un corral que dibujé?", "Toca el corral. También puedes usar Deshacer o Reiniciar."],
            ["¿Qué tamaños de cuadrícula hay?", "De 5x5 a 9x9, en Fácil, Medio y Difícil."],
        ],
    },
    "pt": {
        "slug": "currais-quebra-cabeca-de-retangulos-guia",
        "title": "Currais: Como resolver quebra-cabeças de dividir em retângulos",
        "desc": "Como jogar Currais, um quebra-cabeça de lógica em que você divide a grade em currais retangulares: regras, primeiras jogadas e como as dicas explicam a lógica.",
        "intro": "Currais é um quebra-cabeça de retângulos. Algumas casas têm uma ovelha com um número, e você divide toda a grade em currais retangulares de modo que cada curral tenha exatamente uma ovelha e cubra tantas casas quanto indica o número dela. É calmo, visual e se resolve só com lógica.",
        "sections": [
            {"h": "As regras", "ul": [
                "Arraste o dedo de uma casa para outra para desenhar um retângulo. Toque em um curral para apagá-lo.",
                "Cada curral deve ter exatamente uma ovelha, e sua área (as casas que cobre) deve ser igual ao número dessa ovelha.",
                "Os currais não podem se sobrepor e precisam ser retângulos. Quando toda casa pertence a um curral correto, o quebra-cabeça está resolvido.",
                "Cada quebra-cabeça tem uma única solução, então você nunca precisa adivinhar."]},
            {"h": "Por onde começar", "ul": [
                "Uma ovelha com 1 é o próprio curral. Desenhe-a primeiro.",
                "Olhe os maiores números. Um 6, por exemplo, só pode ser um retângulo de 1x6, 2x3, 3x2 ou 6x1, e as bordas e outras ovelhas descartam quase todos.",
                "Casas que só uma ovelha alcança são forçadas: se um único curral pode cobrir uma casa, ela pertence a ele.",
                "Duas ovelhas próximas dividem o espaço entre elas. Conte quantas casas cada uma precisa e descubra onde a divisa deve ficar."]},
            {"h": "Leve em conta cada casa", "p": ["O truque para as grades difíceis é perguntar, para cada casa vazia, quais ovelhas ainda podem alcançá-la. Um curral não pode engolir outra ovelha, não pode sair da grade e seu tamanho é fixado pelo número. Quando só resta uma opção para uma casa, o curral está decidido. Se não resta nenhuma, algum curral anterior estava errado; use Desfazer."]},
            {"h": "Currais no Logiclings", "p": ["O Logiclings oferece grades de 5x5 a 9x9 em três níveis. Cada quebra-cabeça é verificado por um solucionador, então sempre tem uma única resposta. O botão de dica explica com palavras por que um curral é forçado, em vez de apenas desenhá-lo. Currais é um dos sete tipos de quebra-cabeça do app e entra nos quebra-cabeças diários."]},
        ],
        "faq": [
            ["Um curral pode ter duas ovelhas?", "Não. Cada curral tem exatamente uma ovelha e seu tamanho deve coincidir com o número."],
            ["Preciso adivinhar?", "Não. Cada quebra-cabeça tem uma única solução, encontrada só com lógica."],
            ["Como apago um curral que desenhei?", "Toque no curral. Você também pode usar Desfazer ou Reiniciar."],
            ["Quais tamanhos de grade existem?", "De 5x5 a 9x9, em Fácil, Médio e Difícil."],
        ],
    },
}
