import re, json, pathlib, datetime

ROOT = pathlib.Path('/home/claude/advogadodoexecutivo')
SITE = 'https://advogadodoexecutivo.com.br'
TODAY = '2026-11-27'
WA_BASE = 'https://wa.me/5561998960202?text='
import urllib.parse

src = (ROOT / 'guias/index.html').read_text()
HEAD = src[:src.index('<main>')]
FOOT = src[src.index('<footer>'):]

ARTICLES = [
 dict(
  slug='acordo-de-saida',
  kicker='Saída da empresa',
  title='Acordo de saída de executivo: o que conferir antes de assinar',
  h1='Acordo de saída: <em>o que conferir</em> antes de assinar',
  desc='Demissão, acordo do art. 484-A, PDV ou homologação na Justiça: o que muda em cada forma de saída e os pontos que o executivo deve conferir antes de assinar.',
  lead='Na saída de um executivo, a negociação costuma ser rápida e a pressão para assinar, grande. Entender a forma de saída e o que está sendo quitado evita surpresas depois.',
  body='''
<h2>As formas de saída mais comuns</h2>
<p><strong>Dispensa sem justa causa.</strong> É a forma que garante mais verbas: aviso prévio proporcional (30 dias mais 3 por ano trabalhado, até 90), saldo de salário, férias com um terço, 13º proporcional, saque do FGTS com multa de 40% e seguro-desemprego.</p>
<p><strong>Acordo entre as partes (CLT, art. 484-A).</strong> Desde 2017, empresa e empregado podem encerrar o contrato de comum acordo. Nesse caso, o aviso prévio indenizado e a multa do FGTS são pagos pela metade (20%), o empregado saca até 80% do saldo do FGTS e não recebe seguro-desemprego.</p>
<p><strong>Programa de desligamento voluntário (PDV).</strong> Quando previsto em acordo ou convenção coletiva, a adesão ao PDV pode dar quitação ampla de todo o contrato (CLT, art. 477-B). Por isso, o valor oferecido precisa ser comparado com tudo o que poderia ser discutido.</p>
<p><strong>Acordo homologado na Justiça (CLT, art. 855-B).</strong> Empresa e empregado podem levar um acordo extrajudicial para homologação. A lei exige que cada parte tenha advogado próprio: o advogado da empresa não representa o executivo.</p>

<h2>O que conferir no documento</h2>
<ul>
<li>Se os valores de PLR, bônus e remuneração variável estão incluídos e como foram calculados.</li>
<li>O que acontece com stock options e ações restritas já adquiridas ou em período de carência.</li>
<li>Se há cláusula de não concorrência, confidencialidade ou não aliciamento, por quanto tempo e com qual contrapartida.</li>
<li>Benefícios que continuam por algum período, como plano de saúde, carro ou outplacement.</li>
<li>O alcance da quitação: quitação "geral e irrestrita" pode impedir discussões futuras.</li>
</ul>

<h2>Pontos de atenção</h2>
<p>As verbas rescisórias devem ser pagas em até 10 dias do fim do contrato (CLT, art. 477, § 6º). Situações como cargo de gestão com controle de jornada, parte da remuneração paga fora da folha ou contratação como PJ na mesma função costumam mudar bastante a conta e merecem análise antes da assinatura.</p>
<p>O prazo para entrar com ação trabalhista é de dois anos após o fim do contrato, alcançando os últimos cinco anos (Constituição, art. 7º, XXIX). Quanto mais cedo a análise, mais espaço há para negociar.</p>
''',
  faq=[('Posso levar o acordo para casa antes de assinar?','Sim. Peça cópia de todos os documentos. Uma proposta séria continua válida depois de alguns dias de análise.'),
       ('Assinar o termo de rescisão impede discutir valores depois?','A assinatura do termo de rescisão, em regra, não impede discutir parcelas não pagas. Já a adesão a PDV com quitação ampla ou um acordo homologado na Justiça podem encerrar a discussão, por isso merecem atenção redobrada.')],
  wa='Olá, Dr. Afonso. Recebi uma proposta de saída da empresa e gostaria de uma análise antes de assinar.'),
 dict(
  slug='clausula-de-nao-concorrencia',
  kicker='Cláusulas do contrato',
  title='Cláusula de não concorrência: quando ela vale para o empregado',
  h1='Cláusula de não concorrência: <em>quando ela vale</em>',
  desc='O que a Justiça do Trabalho costuma exigir para validar a cláusula de não concorrência de executivos: prazo, território, atividade e compensação financeira.',
  lead='Contratos de executivos frequentemente proíbem trabalhar para concorrentes depois da saída. A cláusula pode ser válida, mas precisa respeitar limites.',
  body='''
<h2>O que é</h2>
<p>A cláusula de não concorrência impede o ex-empregado de atuar para concorrentes, ou de abrir negócio concorrente, por um período após o fim do contrato. A CLT não regula o tema de forma específica, e os critérios vêm da jurisprudência e dos princípios do direito do trabalho e da livre iniciativa.</p>

<h2>O que costuma ser exigido para que seja válida</h2>
<ul>
<li><strong>Prazo razoável:</strong> períodos curtos, em geral de até dois anos, tendem a ser aceitos com mais facilidade.</li>
<li><strong>Limite de território e de atividade:</strong> a restrição deve se ligar ao mercado e à função em que o executivo realmente atuava.</li>
<li><strong>Compensação financeira:</strong> o pagamento de indenização pelo período de restrição é o ponto mais observado. Cláusulas sem contrapartida costumam ser questionadas.</li>
<li><strong>Interesse legítimo da empresa:</strong> acesso a informações estratégicas, clientes ou segredos de negócio.</li>
</ul>

<h2>Na negociação e na saída</h2>
<p>Antes de assinar o contrato ou o acordo de saída, vale conferir o valor e a forma de pagamento da compensação, o início do prazo, o que conta como concorrente e se há multa. Na saída, é comum negociar a dispensa da cláusula ou o pagamento da indenização prevista.</p>
<p>Uma cláusula desproporcional pode ser revista judicialmente. Por outro lado, descumprir uma cláusula válida pode gerar multa e indenização. Por isso, a decisão de aceitar uma nova vaga deve vir depois da leitura atenta do que foi assinado.</p>
''',
  faq=[('A empresa pode me impedir de trabalhar sem pagar nada?','A ausência de compensação financeira é um dos principais motivos para questionar a validade da cláusula. Cada contrato precisa ser analisado.'),
       ('Posso negociar a cláusula na saída?','Sim. É comum negociar a redução do prazo, do alcance ou a liberação da cláusula no acordo de desligamento.')],
  wa='Olá, Dr. Afonso. Tenho uma cláusula de não concorrência no contrato e gostaria de entender o meu caso.'),
 dict(
  slug='stock-options-na-demissao',
  kicker='Remuneração de longo prazo',
  title='Stock options na demissão: o que acontece com as opções do executivo',
  h1='Stock options na demissão: <em>o que acontece</em> com as opções',
  desc='Vesting, good leaver, bad leaver e prazo de exercício: como os planos de stock options costumam tratar a saída do executivo e o que conferir.',
  lead='Planos de opções de compra de ações e de ações restritas fazem parte do pacote de muitos executivos. Na saída, as regras do plano definem o que se mantém e o que se perde.',
  body='''
<h2>Como os planos costumam funcionar</h2>
<p>O plano concede o direito de comprar ações por um preço definido, ou de receber ações, após um período de carência (<em>vesting</em>). As regras ficam no regulamento do plano e nos contratos de outorga, que precisam ser lidos em conjunto.</p>

<h2>O que muda com a saída</h2>
<ul>
<li><strong>Opções já adquiridas:</strong> em geral podem ser exercidas, mas dentro de um prazo curto após o desligamento, muitas vezes de 30 a 90 dias.</li>
<li><strong>Opções em carência:</strong> costumam ser perdidas ou antecipadas conforme o motivo da saída.</li>
<li><strong>Good leaver e bad leaver:</strong> muitos planos tratam de forma diferente quem sai por dispensa sem justa causa, aposentadoria ou acordo (good leaver) e quem pede demissão ou é dispensado por justa causa (bad leaver).</li>
</ul>

<h2>Natureza das stock options</h2>
<p>A jurisprudência trabalhista tem entendido, em regra, que planos de stock options com risco para o empregado e pagamento do preço de exercício têm natureza mercantil, e não salarial. Isso significa que, em geral, não geram reflexos em férias, 13º e FGTS. Planos desenhados como forma disfarçada de salário podem receber outro tratamento.</p>

<h2>O que conferir</h2>
<p>Antes de assinar o desligamento, verifique quais lotes já estão adquiridos, o prazo de exercício, a classificação da sua saída no plano, eventuais cláusulas de não concorrência atreladas às ações e a possibilidade de negociar a antecipação de lotes em carência.</p>
''',
  faq=[('Perco as opções se for demitido?','Depende do regulamento do plano e do motivo da saída. Opções já adquiridas costumam ser mantidas por um prazo; as em carência variam conforme o plano.'),
       ('Stock options entram no cálculo da rescisão?','Em regra, quando têm natureza mercantil, não. Mas o desenho do plano precisa ser analisado caso a caso.')],
  wa='Olá, Dr. Afonso. Tenho stock options e estou saindo da empresa. Gostaria de entender o que acontece com elas.'),
 dict(
  slug='plr-proporcional',
  kicker='Remuneração variável',
  title='PLR proporcional na demissão: o executivo tem direito?',
  h1='PLR proporcional: <em>direito de quem sai</em> antes do fim do ano',
  desc='Quem sai da empresa antes do fim do período tem direito à PLR proporcional? O que diz a Súmula 451 do TST e o que conferir no programa de PLR.',
  lead='A participação nos lucros ou resultados costuma ser uma parte relevante da remuneração de executivos. Sair antes do pagamento não significa, necessariamente, perder o valor.',
  body='''
<h2>O que diz a regra</h2>
<p>A PLR é regulada pela Lei 10.101/2000 e definida em acordo ou convenção coletiva, ou em programa negociado com comissão de empregados. O Tribunal Superior do Trabalho firmou entendimento, na Súmula 451, de que é devida a PLR proporcional aos meses trabalhados ao empregado que deixa a empresa antes da data do pagamento, pois ele contribuiu para os resultados do período.</p>

<h2>O que conferir</h2>
<ul>
<li>O acordo ou programa de PLR do ano e as regras para quem sai antes.</li>
<li>As metas individuais e coletivas e o quanto foi atingido até a saída.</li>
<li>A data prevista de pagamento: a PLR proporcional costuma ser paga quando os resultados do período são apurados.</li>
<li>Bônus de retenção ou de contratação com cláusula de devolução proporcional.</li>
<li>Se o termo de rescisão ou o acordo de saída menciona a PLR e de que forma.</li>
</ul>

<h2>PLR, bônus e outras variáveis</h2>
<p>PLR, bônus discricionário e bônus por metas são figuras diferentes. A PLR paga conforme a lei não tem natureza salarial. Já bônus pagos com habitualidade, fora dos requisitos da lei, podem ter natureza salarial e repercutir em outras verbas. Por isso, o nome dado ao pagamento importa menos do que a forma como ele funcionava na prática.</p>
''',
  faq=[('Fui dispensado em outubro. Tenho direito à PLR do ano?','Em regra, a PLR proporcional aos meses trabalhados é devida, conforme a Súmula 451 do TST. O valor depende das regras e dos resultados do programa.'),
       ('E se eu pedir demissão?','A Súmula 451 se aplica à saída antes do pagamento, mas as regras do programa precisam ser analisadas.')],
  wa='Olá, Dr. Afonso. Saí da empresa antes do pagamento da PLR e gostaria de entender o meu caso.'),
 dict(
  slug='empregado-hipersuficiente',
  kicker='Regras especiais',
  title='Empregado hipersuficiente: o que muda para o executivo',
  h1='Empregado hipersuficiente: <em>o que muda</em> para o executivo',
  desc='Quem é o empregado hipersuficiente da CLT, o que ele pode negociar diretamente com a empresa, a cláusula de arbitragem e os limites dessa negociação.',
  lead='A Reforma Trabalhista de 2017 criou regras próprias para empregados com diploma de nível superior e salário mais alto. Elas aumentam a liberdade de negociação, mas não eliminam direitos.',
  body='''
<h2>Quem é</h2>
<p>A CLT (art. 444, parágrafo único) chama de hipersuficiente o empregado que tem diploma de nível superior e recebe salário mensal igual ou superior a duas vezes o limite máximo dos benefícios do INSS. É a situação de boa parte dos executivos e gestores.</p>

<h2>O que muda</h2>
<ul>
<li><strong>Negociação individual:</strong> o hipersuficiente pode negociar diretamente com a empresa os temas que a lei permite negociar em acordo coletivo (CLT, art. 611-A), com a mesma força que teria um acordo coletivo.</li>
<li><strong>Arbitragem:</strong> o contrato pode prever que conflitos sejam resolvidos por arbitragem, desde que por iniciativa do empregado ou com sua concordância expressa (CLT, art. 507-A).</li>
</ul>

<h2>Os limites</h2>
<p>A liberdade de negociação não alcança os direitos que a própria lei protege contra a negociação (CLT, art. 611-B), como FGTS, 13º salário, férias com o adicional de um terço, normas de saúde e segurança e outras garantias constitucionais. Cláusulas que ultrapassem esses limites podem ser questionadas.</p>

<h2>O que conferir</h2>
<p>Se você se enquadra nessa categoria, vale ler com atenção cláusulas sobre jornada, banco de horas, remuneração por produtividade, teletrabalho e arbitragem. Na saída, o enquadramento também influencia a estratégia de negociação e o foro em que eventual conflito será discutido.</p>
''',
  faq=[('Ser hipersuficiente significa perder direitos?','Não. Amplia o que pode ser negociado diretamente, mas direitos como FGTS, férias e 13º continuam garantidos.'),
       ('A cláusula de arbitragem me impede de ir à Justiça do Trabalho?','Ela pode valer para o hipersuficiente quando houve iniciativa ou concordância expressa. A validade de cada cláusula precisa ser analisada.')],
  wa='Olá, Dr. Afonso. Sou executivo e gostaria de entender as cláusulas do meu contrato.'),
]

def rel(h):
    return re.sub(r'((?:href|src)=")\.\./', r'\1../../', h)

def head_for(a):
    h = rel(HEAD)
    h = re.sub(r'<title>.*?</title>', f'<title>{a["title"]} | Advogado do Executivo</title>', h, flags=re.S)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{a["desc"]}">', h)
    h = h.replace(f'{SITE}/guias/', f'{SITE}/artigos/{a["slug"]}/')
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{a["title"]}">', h)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{a["desc"]}">', h)
    h = re.sub(r'<nav aria-label="Seções">.*?</nav>', '<nav aria-label="Seções"><a href="../../">Início</a><a href="../../pj/">Contratados PJ</a><a href="../">Artigos</a><a href="../../guias/">Guias grátis</a></nav>', h, flags=re.S)
    wa = WA_BASE + urllib.parse.quote(a['wa'])
    h = re.sub(r'(<a class="btn" href=")https://wa\.me/[^"]*(")', r'\g<1>' + wa + r'\2', h)
    ld = {"@context": "https://schema.org", "@type": "Article", "headline": a['title'], "description": a['desc'],
          "datePublished": TODAY, "dateModified": TODAY, "inLanguage": "pt-BR",
          "author": {"@type": "Person", "name": "Afonso Henrique Vidigal Botelho de Magalhães", "jobTitle": "Advogado trabalhista"},
          "publisher": {"@type": "Organization", "name": "Advogado do Executivo", "url": SITE},
          "mainEntityOfPage": f'{SITE}/artigos/{a["slug"]}/'}
    faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in a['faq']]}
    css = '''<style>
.article{max-width:760px}
.article h2{font-size:32px;margin:44px 0 14px}
.article p{margin:0 0 16px;font-size:18px;line-height:1.7}
.article ul{margin:0 0 18px;padding-left:22px;font-size:18px;line-height:1.7}
.article li{margin-bottom:8px}
.related{display:flex;flex-wrap:wrap;gap:12px;margin-top:20px}
.related a{border:1px solid var(--line,#e2d9ca);padding:10px 14px;text-decoration:none;color:inherit}
.updated{color:var(--mute,#5d6672);font-size:14px;margin-top:18px}
.alist{display:grid;gap:18px;margin-top:30px}
.alist a{display:block;border:1px solid var(--line,#e2d9ca);background:var(--paper,#fbf8f3);padding:26px 28px;text-decoration:none;color:inherit}
.alist a h3{font-size:26px;margin-bottom:8px}
</style>
'''
    h = h.replace('</head>', f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n<script type="application/ld+json">{json.dumps(faq, ensure_ascii=False)}</script>\n' + css + '</head>')
    return h, wa

def page(a):
    h, wa = head_for(a)
    others = [o for o in ARTICLES if o['slug'] != a['slug']]
    rel_links = ''.join(f'<a href="../{o["slug"]}/">{o["title"].split(":")[0]}</a>' for o in others)
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{r}</p></details>' for q, r in a['faq'])
    main = f'''<main>
<section class="dark band" id="inicio">
  <div class="wrap">
    <p class="crumb"><a href="../../">Advogado do Executivo</a> / <a href="../">Artigos</a></p>
    <span class="kicker">{a["kicker"]}</span>
    <h1>{a["h1"]}</h1>
    <p class="lead" style="margin-top:24px;max-width:760px">{a["lead"]}</p>
    <p class="updated">Atualizado em novembro de 2026 · Afonso Magalhães, advogado trabalhista há mais de 45 anos</p>
  </div>
</section>
<section class="band paperband">
  <div class="wrap article">
{a["body"]}
    <h2>Dúvidas frequentes</h2>
    <div class="faq">{faq_html}</div>
    <p class="note" style="margin-top:30px">Conteúdo informativo. Não substitui a análise individual do seu caso e não constitui promessa de resultado.</p>
    <h2>Material gratuito</h2>
    <p>Baixe os guias "Saída de executivo: o que conferir antes de assinar" e "Contratado como PJ: quando pode haver vínculo", em PDF e sem cadastro.</p>
    <a class="btn" href="../../guias/">Ver os guias gratuitos</a>
    <h2>Leia também</h2>
    <div class="related">{rel_links}<a href="../../pj/">Contratado como PJ</a></div>
  </div>
</section>
<section class="dark band contact" id="contato">
  <div class="wrap">
    <div>
      <span class="kicker">Contato reservado</span>
      <h2>Quer entender o seu caso?</h2>
      <p class="lead">Atendimento on-line em todo o Brasil e presencial em Brasília.</p>
    </div>
    <div>
      <div class="channels">
        <div><small>WhatsApp</small><a href="{wa}" target="_blank" rel="noopener">(61) 99896-0202</a></div>
        <div><small>E-mail</small><a href="mailto:afonsomagalhaesadvogados@gmail.com">afonsomagalhaesadvogados@gmail.com</a></div>
      </div>
      <p class="note" style="margin-top:18px">Todo atendimento é protegido pelo sigilo profissional. O contato inicial não gera obrigação.</p>
    </div>
  </div>
</section>
</main>
'''
    return h + main + rel(FOOT)

def index_page():
    a = dict(slug='', title='Artigos para executivos e contratados PJ', desc='Artigos sobre saída de executivos, não concorrência, stock options, PLR, empregado hipersuficiente e contratação como PJ.', faq=[('O que encontro aqui?', 'Artigos informativos sobre direitos de executivos e contratados PJ.')], wa='Olá, Dr. Afonso. Li os artigos do site e gostaria de conversar sobre o meu caso.')
    h, wa = head_for(a)
    h = h.replace(f'{SITE}/artigos//', f'{SITE}/artigos/').replace('../../', '../')
    h = re.sub(r'<script type="application/ld\+json">\{"@context": "https://schema.org", "@type": "FAQPage".*?</script>\n', '', h, flags=re.S)
    items = ''.join(f'<a href="{o["slug"]}/"><span class="kicker">{o["kicker"]}</span><h3>{o["title"]}</h3><p>{o["desc"]}</p></a>' for o in ARTICLES)
    items += '<a href="../pj/"><span class="kicker">Contratação como PJ</span><h3>Contratado como PJ: quando pode haver vínculo de emprego</h3><p>Os sinais que costumam ser analisados, o que pode ser discutido e o cenário do Tema 1.389 no STF.</p></a>'
    main = f'''<main>
<section class="dark band"><div class="wrap">
<p class="crumb"><a href="../">Advogado do Executivo</a> / Artigos</p>
<span class="kicker">Conteúdo informativo</span>
<h1>Artigos para <em>executivos e PJ</em></h1>
<p class="lead" style="margin-top:24px;max-width:760px">Textos curtos sobre as dúvidas mais comuns na contratação, na negociação e na saída da empresa.</p>
</div></section>
<section class="band paperband"><div class="wrap"><div class="alist">{items}</div>
<p class="note" style="margin-top:28px">Conteúdo informativo. Não substitui a análise individual do seu caso.</p></div></section>
</main>
'''
    h = h.replace('<a href="../">Artigos</a>', '<a href="./">Artigos</a>')
    foot = FOOT
    return h + main + foot

for a in ARTICLES:
    d = ROOT / 'artigos' / a['slug']; d.mkdir(parents=True, exist_ok=True)
    (d / 'index.html').write_text(page(a))
(ROOT / 'artigos' / 'index.html').write_text(index_page())

urls = ['', 'pj/', 'guias/', 'artigos/'] + [f'artigos/{a["slug"]}/' for a in ARTICLES]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + ''.join(f'  <url><loc>{SITE}/{u}</loc><lastmod>{TODAY}</lastmod></url>\n' for u in urls) + '</urlset>\n'
(ROOT / 'sitemap.xml').write_text(sm)
print('ok', len(ARTICLES))
