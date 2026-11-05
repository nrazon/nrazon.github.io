# Rehber: Logiclings (Taç, İkiz, Yol)
GUIDE = {
    "id": "logic", "app": "logiclings", "date": "2026-11-05",
    "en": {
        "slug": "how-to-solve-crown-twin-path-puzzles",
        "title": "How to Solve Crown, Twin and Path Logic Puzzles",
        "desc": "Rules and solving techniques for three logic puzzles: Crown (one crown per row, column and region), Twin (balanced blue and orange faces) and Path (one line through every cell).",
        "intro": "Logiclings has three kinds of logic puzzles, and every puzzle has exactly one solution, so you never need to guess. Each one rewards a different way of thinking. Here are the rules and the first techniques to try.",
        "sections": [
            {"h": "Crown", "p": ["Place exactly one crown in every row, every column and every colored region, and never let two crowns touch, not even diagonally."], "ul": ["Start with the smallest colored region: it has the fewest places for its crown.", "When a region is confined to one row or column, no other region can put its crown in that row or column.", "Every crown rules out its neighbors, including the diagonal ones. Cross those cells off.", "When one cell is the only option left for a row, column or region, that is where the crown goes."]},
            {"h": "Twin", "p": ["Fill the grid with blue and orange faces. Every row and column must contain the same number of each color, no three faces in a row may be alike, and the = and × signs between neighbors tell you whether the two faces are the same (=) or different (×)."], "ul": ["If two neighbors are alike, the face next to them must be the other color, so you never get three in a row.", "Count each row and column: once one color has reached its half, every remaining cell is the other color.", "Use = and × signs as free information and spread it along the row."]},
            {"h": "Path", "p": ["Start at number 1, pass through the numbers in order and fill every single cell with one unbroken path."], "ul": ["Corners and cells with only one open neighbor are dead ends: a path can only enter or leave them in one way, so the line is forced there.", "Think about where the highest number sits: the path must end there after covering everything.", "If a move would leave a cell you can never reach, undo it. Numbers must be reached in the correct order."]},
            {"h": "Hints that explain", "p": ["If you are stuck, a hint in Logiclings does not just fill a cell. It explains the logic step by step and highlights the cell, so every hint is also a small lesson."]},
        ],
        "faq": [
            ["Do I ever have to guess?", "No. Every puzzle has exactly one solution that can be found by logic alone."],
            ["Do the puzzles get harder?", "Yes. Sizes go from 4x4 up to 10x10 grids, from easy to hard."],
            ["Is there a time limit?", "No. There is no timer pressure and no lives. Your best times are tracked for fun."],
        ],
    },
    "tr": {
        "slug": "tac-ikiz-yol-bulmacalari-nasil-cozulur",
        "title": "Taç, İkiz ve Yol Mantık Bulmacaları Nasıl Çözülür?",
        "desc": "Üç mantık bulmacasının kuralları ve çözüm teknikleri: Taç (her satır, sütun ve bölgeye bir taç), İkiz (dengeli mavi ve turuncu yüzler) ve Yol (her hücreden geçen tek çizgi).",
        "intro": "Logiclings'te üç tür mantık bulmacası var ve her bulmacanın tam olarak bir çözümü olduğu için asla tahmin etmen gerekmez. Her biri farklı bir düşünme biçimini ödüllendirir. İşte kurallar ve deneyeceğin ilk teknikler.",
        "sections": [
            {"h": "Taç", "p": ["Her satıra, her sütuna ve her renkli bölgeye tam olarak bir taç koy; iki taç çapraz da olsa birbirine değmesin."], "ul": ["En küçük renkli bölgeyle başla: tacını koyacak en az yeri var.", "Bir bölge tek bir satır ya da sütunla sınırlıysa, başka hiçbir bölge o satıra ya da sütuna tacını koyamaz.", "Her taç komşularını eler, çapraz olanlar dahil. O hücreleri işaretle.", "Bir hücre bir satır, sütun ya da bölge için kalan tek seçenekse, taç oraya gider."]},
            {"h": "İkiz", "p": ["Izgarayı mavi ve turuncu yüzlerle doldur. Her satırda ve sütunda iki rengin sayısı eşit olmalı, yan yana üç yüz aynı olmamalı ve komşular arasındaki = ve × işaretleri iki yüzün aynı (=) mı farklı (×) mı olduğunu söyler."], "ul": ["İki komşu aynıysa, yanlarındaki yüz diğer renk olmalı; böylece üç yan yana olmaz.", "Her satırı ve sütunu say: bir renk yarısına ulaştığında kalan tüm hücreler diğer renktir.", "= ve × işaretlerini bedava bilgi olarak kullan ve satır boyunca yay."]},
            {"h": "Yol", "p": ["1 numaradan başla, sayılardan sırayla geç ve her hücreyi tek kopmayan bir yolla doldur."], "ul": ["Köşeler ve yalnızca bir açık komşusu olan hücreler çıkmaz sokaktır: yol oraya ya da oradan tek yoldan girip çıkabilir, bu yüzden çizgi orada zorunludur.", "En büyük sayının nerede durduğunu düşün: yol her şeyi kapladıktan sonra orada bitmelidir.", "Bir hamle hiçbir zaman ulaşamayacağın bir hücre bırakacaksa geri al. Sayılara doğru sırayla ulaşılmalı."]},
            {"h": "Açıklayan ipuçları", "p": ["Takılırsan Logiclings'te ipucu yalnızca bir hücreyi doldurmaz. Mantığı adım adım açıklar ve hücreyi vurgular; yani her ipucu aynı zamanda küçük bir derstir."]},
        ],
        "faq": [
            ["Hiç tahmin etmem gerekir mi?", "Hayır. Her bulmacanın yalnızca mantıkla bulunabilen tam bir çözümü vardır."],
            ["Bulmacalar zorlaşır mı?", "Evet. Boyutlar 4x4'ten 10x10 ızgaraya, kolaydan zora doğru gider."],
            ["Süre sınırı var mı?", "Hayır. Süre baskısı ve can yoktur. En iyi sürelerin eğlence için tutulur."],
        ],
    },
    "es": {
        "slug": "como-resolver-corona-gemelos-camino",
        "title": "Cómo resolver los puzles de lógica Corona, Gemelos y Camino",
        "desc": "Reglas y técnicas para tres puzles de lógica: Corona (una corona por fila, columna y región), Gemelos (caras azules y naranjas equilibradas) y Camino (una línea por todas las casillas).",
        "intro": "Logiclings tiene tres tipos de puzles de lógica y cada puzle tiene exactamente una solución, así que nunca tienes que adivinar. Cada uno premia una forma distinta de pensar. Aquí tienes las reglas y las primeras técnicas que probar.",
        "sections": [
            {"h": "Corona", "p": ["Coloca exactamente una corona en cada fila, cada columna y cada región de color, y nunca dejes que dos coronas se toquen, ni siquiera en diagonal."], "ul": ["Empieza por la región de color más pequeña: es la que tiene menos sitios para su corona.", "Cuando una región queda limitada a una sola fila o columna, ninguna otra región puede poner su corona en esa fila o columna.", "Cada corona descarta a sus vecinas, también las diagonales. Tacha esas casillas.", "Cuando una casilla es la única opción que queda para una fila, columna o región, ahí va la corona."]},
            {"h": "Gemelos", "p": ["Llena la cuadrícula con caras azules y naranjas. Cada fila y columna debe tener el mismo número de cada color, no puede haber tres caras iguales seguidas y los signos = y × entre vecinas indican si las dos caras son iguales (=) o distintas (×)."], "ul": ["Si dos vecinas son iguales, la cara de al lado debe ser del otro color, así nunca hay tres seguidas.", "Cuenta cada fila y columna: cuando un color llega a su mitad, todas las casillas restantes son del otro color.", "Usa los signos = y × como información gratis y extiéndela por la fila."]},
            {"h": "Camino", "p": ["Empieza en el número 1, pasa por los números en orden y llena todas las casillas con una línea sin cortes."], "ul": ["Las esquinas y las casillas con un solo vecino libre son callejones sin salida: el camino solo puede entrar o salir de una forma, así que la línea está forzada ahí.", "Piensa dónde está el número más alto: el camino debe terminar allí después de cubrirlo todo.", "Si un movimiento deja una casilla que nunca podrás alcanzar, deshazlo. Los números deben alcanzarse en el orden correcto."]},
            {"h": "Pistas que explican", "p": ["Si te atascas, una pista de Logiclings no rellena solo una casilla. Explica la lógica paso a paso y resalta la casilla, así que cada pista es también una pequeña lección."]},
        ],
        "faq": [
            ["¿Tengo que adivinar alguna vez?", "No. Cada puzle tiene exactamente una solución que se encuentra solo con lógica."],
            ["¿Los puzles se vuelven más difíciles?", "Sí. Los tamaños van de cuadrículas de 4x4 hasta 10x10, de fácil a difícil."],
            ["¿Hay límite de tiempo?", "No. No hay presión de tiempo ni vidas. Tus mejores tiempos se registran por diversión."],
        ],
    },
    "pt": {
        "slug": "como-resolver-coroa-gemeos-caminho",
        "title": "Como resolver os quebra-cabeças de lógica Coroa, Gêmeos e Caminho",
        "desc": "Regras e técnicas para três quebra-cabeças de lógica: Coroa (uma coroa por linha, coluna e região), Gêmeos (rostos azuis e laranjas equilibrados) e Caminho (uma linha por todas as casas).",
        "intro": "O Logiclings tem três tipos de quebra-cabeças de lógica e cada quebra-cabeça tem exatamente uma solução, então você nunca precisa chutar. Cada um premia uma forma diferente de pensar. Aqui estão as regras e as primeiras técnicas para experimentar.",
        "sections": [
            {"h": "Coroa", "p": ["Coloque exatamente uma coroa em cada linha, cada coluna e cada região colorida, e nunca deixe duas coroas se tocarem, nem na diagonal."], "ul": ["Comece pela menor região colorida: é a que tem menos lugares para a coroa.", "Quando uma região fica limitada a uma única linha ou coluna, nenhuma outra região pode pôr a coroa nessa linha ou coluna.", "Cada coroa elimina as vizinhas, inclusive as diagonais. Risque essas casas.", "Quando uma casa é a única opção que resta para uma linha, coluna ou região, a coroa vai ali."]},
            {"h": "Gêmeos", "p": ["Preencha a grade com rostos azuis e laranjas. Cada linha e coluna deve ter o mesmo número de cada cor, não pode haver três rostos iguais seguidos e os sinais = e × entre vizinhos dizem se os dois rostos são iguais (=) ou diferentes (×)."], "ul": ["Se dois vizinhos são iguais, o rosto ao lado deve ser da outra cor, assim nunca há três seguidos.", "Conte cada linha e coluna: quando uma cor chega à metade, todas as casas restantes são da outra cor.", "Use os sinais = e × como informação de graça e espalhe pela linha."]},
            {"h": "Caminho", "p": ["Comece no número 1, passe pelos números em ordem e preencha todas as casas com uma linha sem cortes."], "ul": ["Cantos e casas com apenas um vizinho livre são becos sem saída: o caminho só pode entrar ou sair de uma forma, então a linha é forçada ali.", "Pense onde está o maior número: o caminho deve terminar ali depois de cobrir tudo.", "Se uma jogada deixar uma casa que você nunca vai alcançar, desfaça. Os números devem ser alcançados na ordem certa."]},
            {"h": "Dicas que explicam", "p": ["Se travar, uma dica do Logiclings não preenche só uma casa. Ela explica a lógica passo a passo e destaca a casa, então cada dica também é uma pequena lição."]},
        ],
        "faq": [
            ["Eu preciso chutar alguma vez?", "Não. Cada quebra-cabeça tem exatamente uma solução que se encontra só com lógica."],
            ["Os quebra-cabeças ficam mais difíceis?", "Sim. Os tamanhos vão de grades 4x4 até 10x10, do fácil ao difícil."],
            ["Existe limite de tempo?", "Não. Não há pressão de tempo nem vidas. Seus melhores tempos são registrados por diversão."],
        ],
    },
}
