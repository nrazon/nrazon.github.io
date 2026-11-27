# Çekiliş aracının EN/ES/PT sayfaları (27.11.2026). Tek kaynak: cekilis/index.html (TR; uygulama kodu ve stil orada).
# Çıktı: secret-santa/, amigo-invisible/, amigo-secreto/ (ELLE DÜZENLEME YOK). Kullanım: py -3 -X utf8 tools/gen_cekilis.py (build_site.py çağırır).
# Bu klasörler i18n_split SKIP_DIRS ve seo_fix SKIP içindedir.
import html
import json
import os
import re

G = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = "https://nesimapps.com"
PAGES = {"tr": "cekilis", "en": "secret-santa", "es": "amigo-invisible", "pt": "amigo-secreto"}

L = {
    "en": {
        "title": "Free online Secret Santa draw, no sign-up | Snowlings",
        "og": "Online Secret Santa draw",
        "desc": "Free online Secret Santa generator: type the names, set who must not draw each other and send each match privately on WhatsApp. No sign-up, no server.",
        "ogdesc": "Type the names, run the draw and send each match privately on WhatsApp. Free, no sign-up, data stays in your browser.",
        "currency": "USD",
        "h2": "How does the online Secret Santa draw work?",
        "steps": [("Add the participants:", "one name per line (at least 3, at most 50)."),
                  ("Add rules if you like:", "one pair per line for couples, siblings or anyone who must not draw each other (Anna - Mark)."),
                  ("Add a budget, date and note,", "then press \"Run the draw\"."),
                  ("Share the matches:", "pass the phone around, or send each person a private link on WhatsApp. Everyone sees only their own match.")],
        "faqh": "Frequently asked questions",
        "faq": [("Can someone draw themselves, or can two people draw each other?", "Nobody draws themselves. Whenever possible the matches form one big cycle (A → B → C → … → A), so if A draws B, B does not draw A back."),
                ("How do I stop couples or siblings from drawing each other?", "Write one pair per line in the \"Who must not draw each other\" box, for example Anna - Mark. If the draw is impossible with your rules, the page tells you; remove a few and try again."),
                ("Are the names and matches stored?", "No. The draw runs in your browser; names and matches are not sent to any server and no account is needed. In a private link the match is encoded after the # sign, which is not sent to the server. Send each link only to its owner, because anyone with the link can see that match."),
                ("How many people can join?", "From 3 to 50. Write one name per line; the page warns you if a name appears twice."),
                ("Is it free, and do I need an app?", "It is completely free and needs no app; it works in a phone or computer browser. The Snowlings app by the same developer (Christmas calendar, winter puzzles, greeting cards) is a separate product.")],
        "more": 'Read more: <a href="/blog/how-to-run-an-online-secret-santa-draw-free-no-sign-up/">How to run an online Secret Santa draw</a>. This tool is part of <a href="/snowlings/">Snowlings</a>, a Christmas app with a new door every day in December, 6 winter puzzle games and greeting cards.',
        "others": "Other languages:",
    },
    "es": {
        "title": "Sorteo de amigo invisible online gratis | Snowlings",
        "og": "Sorteo online de amigo invisible",
        "desc": "Sorteo de amigo invisible online y gratis: escribe los nombres, indica quién no puede tocarse y envía cada pareja en privado por WhatsApp. Sin registro.",
        "ogdesc": "Escribe los nombres, haz el sorteo y envía cada pareja en privado por WhatsApp. Gratis, sin registro; los datos se quedan en tu navegador.",
        "currency": "EUR",
        "h2": "¿Cómo funciona el sorteo de amigo invisible online?",
        "steps": [("Escribe los participantes:", "un nombre por línea (mínimo 3, máximo 50)."),
                  ("Añade reglas si quieres:", "una pareja por línea para parejas, hermanos o quienes no deban tocarse (Ana - Marcos)."),
                  ("Añade presupuesto, fecha y nota,", "y pulsa \"Hacer el sorteo\"."),
                  ("Comparte el resultado:", "pasad el teléfono o envía a cada persona su enlace privado por WhatsApp. Cada uno ve solo su pareja.")],
        "faqh": "Preguntas frecuentes",
        "faq": [("¿Puede alguien tocarse a sí mismo o dos personas entre sí?", "Nadie se saca a sí mismo. Siempre que es posible, las parejas forman un solo ciclo grande (A → B → C → … → A), así que si A saca a B, B no saca a A."),
                ("¿Cómo evito que las parejas o los hermanos se toquen?", "Escribe una pareja por línea en la casilla \"Quién no puede tocarse\", por ejemplo Ana - Marcos. Si con tus reglas el sorteo es imposible, la página te avisa; quita algunas y prueba de nuevo."),
                ("¿Se guardan los nombres y las parejas?", "No. El sorteo se hace en tu navegador; no se envía nada a ningún servidor y no hace falta cuenta. En el enlace privado la pareja va codificada después del signo #, parte que no se envía al servidor. Manda cada enlace solo a su destinatario, porque quien lo tenga puede ver esa pareja."),
                ("¿Cuántas personas pueden participar?", "De 3 a 50. Escribe un nombre por línea; la página avisa si un nombre está repetido."),
                ("¿Es gratis? ¿Tengo que instalar una app?", "Es totalmente gratis y no hace falta ninguna app: funciona en el navegador del móvil o del ordenador. La app Snowlings del mismo desarrollador (calendario navideño, puzles de invierno, tarjetas) es un producto aparte.")],
        "more": 'Más información: <a href="/es/blog/como-hacer-un-sorteo-de-amigo-invisible-online-gratis-sin-registro/">Cómo hacer un sorteo de amigo invisible online</a>. Esta herramienta forma parte de <a href="/es/snowlings/">Snowlings</a>, una app navideña con una puerta nueva cada día de diciembre, 6 puzles de invierno y tarjetas de felicitación.',
        "others": "Otros idiomas:",
    },
    "pt": {
        "title": "Sorteio de amigo secreto online grátis | Snowlings",
        "og": "Sorteio online de amigo secreto",
        "desc": "Sorteio de amigo secreto online e grátis: digite os nomes, diga quem não pode se tirar e envie cada par em particular pelo WhatsApp. Sem cadastro.",
        "ogdesc": "Digite os nomes, faça o sorteio e envie cada par em particular pelo WhatsApp. Grátis, sem cadastro; os dados ficam no seu navegador.",
        "currency": "BRL",
        "h2": "Como funciona o sorteio de amigo secreto online?",
        "steps": [("Escreva os participantes:", "um nome por linha (no mínimo 3, no máximo 50)."),
                  ("Adicione regras se quiser:", "um par por linha para casais, irmãos ou quem não deve se tirar (Ana - Marcos)."),
                  ("Informe valor, data e observação,", "e toque em \"Fazer o sorteio\"."),
                  ("Compartilhe o resultado:", "passem o celular ou envie a cada pessoa o link particular pelo WhatsApp. Cada um vê só o próprio par.")],
        "faqh": "Perguntas frequentes",
        "faq": [("Alguém pode tirar a si mesmo, ou duas pessoas se tirarem?", "Ninguém tira a si mesmo. Sempre que possível, os pares formam um único ciclo grande (A → B → C → … → A), então se A tira B, B não tira A."),
                ("Como impedir que casais ou irmãos se tirem?", "Escreva um par por linha na caixa \"Quem não pode se tirar\", por exemplo Ana - Marcos. Se o sorteio for impossível com as suas regras, a página avisa; remova algumas e tente de novo."),
                ("Os nomes e os pares são guardados?", "Não. O sorteio acontece no seu navegador; nada é enviado a servidor algum e não é preciso ter conta. No link particular o par fica codificado depois do sinal #, parte que não é enviada ao servidor. Envie cada link só ao dono, porque quem tiver o link consegue ver aquele par."),
                ("Quantas pessoas podem participar?", "De 3 a 50. Escreva um nome por linha; a página avisa se um nome estiver repetido."),
                ("É grátis? Preciso instalar um app?", "É totalmente grátis e não precisa de app: funciona no navegador do celular ou do computador. O app Snowlings do mesmo desenvolvedor (calendário de Natal, quebra-cabeças de inverno, cartões) é um produto à parte.")],
        "more": 'Saiba mais: <a href="/pt/blog/como-fazer-um-sorteio-de-amigo-secreto-online-gratis-sem-cadastro/">Como fazer um sorteio de amigo secreto online</a>. Esta ferramenta faz parte do <a href="/pt/snowlings/">Snowlings</a>, um app de Natal com uma porta nova por dia em dezembro, 6 quebra-cabeças de inverno e cartões.',
        "others": "Outros idiomas:",
    },
}
NAMES = {"tr": "Yılbaşı çekilişi", "en": "Secret Santa draw", "es": "Amigo invisible", "pt": "Amigo secreto"}


def sub(pattern, repl, s):
    s, n = re.subn(pattern, lambda m: repl, s, flags=re.S)
    if n != 1:
        raise SystemExit(f"gen_cekilis: kaynakta tam 1 kez bulunmalı ({n}): {pattern}")
    return s


def esc(s):
    return html.escape(s, quote=True)


def build(src, lang):
    t = L[lang]
    url = f"{BASE}/{PAGES[lang]}/"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebApplication", "name": t["og"], "url": url, "applicationCategory": "UtilitiesApplication", "operatingSystem": "Any",
         "inLanguage": lang, "offers": {"@type": "Offer", "price": "0", "priceCurrency": t["currency"]}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}]}
    others = " · ".join(f'<a href="/{PAGES[l]}/" hreflang="{l}">{NAMES[l]}</a>' for l in PAGES if l != lang)
    info = ('<section id="info" class="info">\n'
            f'  <h2>{esc(t["h2"])}</h2>\n  <ol>\n'
            + "".join(f"    <li><b>{esc(a)}</b> {esc(b)}</li>\n" for a, b in t["steps"])
            + f'  </ol>\n  <h2>{esc(t["faqh"])}</h2>\n'
            + "".join(f"  <h3>{esc(q)}</h3>\n  <p>{esc(a)}</p>\n" for q, a in t["faq"])
            + f'  <p class="more">{t["more"]}</p>\n  <p>{t["others"]} {others}</p>\n</section>')
    s = sub(r'<html lang="tr">', f'<html lang="{lang}">', src)
    s = sub(r"<title>.*?</title>", f'<title>{esc(t["title"])}</title>', s)
    s = sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{esc(t["desc"])}">', s)
    s = sub(r'<link rel="canonical" href="[^"]*">', f'<link rel="canonical" href="{url}">', s)
    s = sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{esc(t["og"])}">', s)
    s = sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{esc(t["ogdesc"])}">', s)
    s = sub(r'<meta property="og:url" content="[^"]*">', f'<meta property="og:url" content="{url}">', s)
    s = sub(r'<script type="application/ld\+json">.*?</script>', f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>', s)
    return sub(r'<section id="info".*?</section>', info, s)


def main():
    src = open(os.path.join(G, "cekilis", "index.html"), encoding="utf-8").read()
    for lang in L:
        d = os.path.join(G, PAGES[lang])
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "index.html"), "w", encoding="utf-8", newline="\n").write(build(src, lang))
    print("gen_cekilis: 3 sayfa")


if __name__ == "__main__":
    main()
