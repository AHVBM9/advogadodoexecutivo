import asyncio, json, pathlib
from playwright.async_api import async_playwright

OUT = pathlib.Path('/home/claude/advogadodoexecutivo/m')
LOGO = 'file:///home/claude/advogadodoexecutivo/img/logo.png'

POSTS = [
 dict(file='Post12_PLR_Proporcional', date='2026-12-05T10:40:00', k='PLR e bônus', h='Saiu antes do pagamento da PLR? Você pode ter direito à parte proporcional',
      items=['O TST (Súmula 451) reconhece a PLR proporcional aos meses trabalhados','Confira as regras do programa do ano','Guarde as metas e os resultados atingidos'],
      foot='Sair antes não significa, necessariamente, perder a PLR.',
      slug='plr-proporcional',
      cap='Foi desligado antes do pagamento da PLR? Isso não significa, necessariamente, perder o valor.\n\nO TST firmou entendimento (Súmula 451) de que é devida a PLR proporcional aos meses trabalhados a quem deixa a empresa antes da data do pagamento.\n\nVale conferir as regras do programa, as metas e o que o termo de rescisão diz sobre a PLR.\n\nArtigo completo no site: advogadodoexecutivo.com.br/artigos\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#PLR #executivos #rescisao #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post13_Nao_Concorrencia', date='2026-12-08T19:10:00', k='Cláusulas do contrato', h='Não concorrência: 4 pontos que a Justiça costuma observar',
      items=['Prazo razoável','Limite de território e de atividade','Compensação financeira pelo período','Interesse legítimo da empresa'],
      foot='Cláusula sem contrapartida costuma ser questionada.',
      slug='clausula-de-nao-concorrencia',
      cap='Seu contrato proíbe trabalhar para concorrentes depois da saída?\n\nA cláusula de não concorrência pode ser válida, mas a Justiça do Trabalho costuma observar quatro pontos: prazo razoável, limite de território e de atividade, compensação financeira pelo período de restrição e interesse legítimo da empresa.\n\nNa saída, é comum negociar o prazo, o alcance ou a liberação da cláusula.\n\nArtigo completo: advogadodoexecutivo.com.br/artigos\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#naoconcorrencia #executivos #contratodetrabalho #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post14_Stock_Options', date='2026-12-11T12:10:00', k='Stock options', h='Saindo da empresa? Confira 3 pontos do seu plano de opções',
      items=['Quais lotes já estão adquiridos (vesting)','O prazo para exercer depois da saída','Se sua saída é good leaver ou bad leaver'],
      foot='Os prazos de exercício costumam ser curtos.',
      slug='stock-options-na-demissao',
      cap='Stock options na saída da empresa: o regulamento do plano decide o que fica e o que se perde.\n\nAntes de assinar o desligamento, confira:\n✔ Quais lotes já estão adquiridos (vesting)\n✔ O prazo para exercer as opções depois da saída, muitas vezes de 30 a 90 dias\n✔ Se a sua saída é tratada como good leaver ou bad leaver\n\nArtigo completo: advogadodoexecutivo.com.br/artigos\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#stockoptions #executivos #rescisao #remuneracao #advogadotrabalhista'),
 dict(file='Post15_Demissao_Dezembro', date='2026-12-15T19:10:00', k='Fim de ano', h='Demitido em dezembro? O aviso prévio conta para o 13º e as férias',
      items=['O aviso prévio indenizado integra o tempo de serviço (CLT, art. 487)','Ele projeta o 13º e as férias proporcionais','Confira se a projeção entrou no cálculo'],
      foot='As verbas devem ser pagas em até 10 dias.',
      slug='acordo-de-saida',
      cap='Desligamentos de fim de ano pedem atenção ao cálculo.\n\nO aviso prévio indenizado integra o tempo de serviço (CLT, art. 487, § 1º). Na prática, ele projeta o contrato e pode aumentar o 13º e as férias proporcionais.\n\nConfira se essa projeção entrou no termo de rescisão. As verbas devem ser pagas em até 10 dias do fim do contrato.\n\nConteúdo informativo. Cada caso exige análise individual.\n📲 Link na bio.\n\n#demissao #13salario #rescisao #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post16_Hipersuficiente', date='2026-12-18T12:10:00', k='Regras especiais', h='Diploma e salário alto? Você pode ser empregado hipersuficiente',
      items=['Diploma de nível superior','Salário de pelo menos 2 vezes o teto do INSS','Mais temas negociáveis direto com a empresa'],
      foot='FGTS, férias e 13º continuam garantidos.',
      slug='empregado-hipersuficiente',
      cap='Você é empregado hipersuficiente?\n\nA CLT (art. 444, parágrafo único) dá esse nome a quem tem diploma de nível superior e salário de pelo menos duas vezes o teto do INSS, situação de muitos executivos.\n\nO hipersuficiente pode negociar mais temas diretamente com a empresa e aceitar cláusula de arbitragem. Mas direitos como FGTS, férias e 13º continuam garantidos.\n\nArtigo completo: advogadodoexecutivo.com.br/artigos\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#hipersuficiente #executivos #CLT #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post17_Acordo_484A', date='2026-12-22T19:10:00', k='Formas de saída', h='Dispensa ou acordo? O que muda no seu bolso',
      items=['Dispensa: multa de 40% do FGTS e seguro-desemprego','Acordo (art. 484-A): multa de 20% e metade do aviso','No acordo, saque de até 80% do FGTS'],
      foot='Compare antes de aceitar a proposta.',
      slug='acordo-de-saida',
      cap='A empresa propôs encerrar o contrato "por acordo"?\n\nNa dispensa sem justa causa, você recebe aviso prévio integral, multa de 40% do FGTS e pode pedir seguro-desemprego.\n\nNo acordo do art. 484-A da CLT, a multa do FGTS cai para 20%, o aviso prévio indenizado é pago pela metade, o saque do FGTS é de até 80% e não há seguro-desemprego.\n\nCompare os números antes de aceitar.\n\nArtigo completo: advogadodoexecutivo.com.br/artigos\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#rescisao #acordo #FGTS #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post18_Bonus_Retencao', date='2026-12-26T12:10:00', k='Remuneração', h='Bônus de retenção: leia a cláusula de devolução',
      items=['Por quanto tempo você precisa ficar','Se a devolução é proporcional','O que acontece se a empresa dispensar você'],
      foot='O nome do pagamento importa menos que a regra.',
      slug='plr-proporcional',
      cap='Recebeu bônus de retenção ou de contratação?\n\nMuitos vêm com cláusula de devolução se você sair antes de um prazo. Antes de aceitar uma nova proposta, confira:\n✔ Por quanto tempo você precisa ficar\n✔ Se a devolução é integral ou proporcional\n✔ O que acontece se for a empresa a dispensar você\n\nConteúdo informativo. Cada caso exige análise individual.\n📲 Link na bio.\n\n#bonus #executivos #carreira #direitotrabalhista #advogadotrabalhista'),
 dict(file='Post19_Proposta_Nova', date='2026-12-29T19:10:00', k='Nova proposta', h='Vai trocar de empresa em 2027? Leia isto na proposta',
      items=['Forma de contratação: CLT ou PJ','Bônus, PLR e metas por escrito','Não concorrência e confidencialidade','Regras de saída e de stock options'],
      foot='Negociar antes de assinar é mais fácil do que depois.',
      slug='',
      cap='Vai trocar de empresa em 2027?\n\nAntes de assinar a proposta, leia com atenção:\n✔ A forma de contratação: CLT ou PJ\n✔ Bônus, PLR e metas por escrito\n✔ Cláusulas de não concorrência e confidencialidade\n✔ Regras de saída e de stock options\n\nNegociar antes de assinar é sempre mais fácil.\n\nGuias gratuitos: advogadodoexecutivo.com.br/guias\n\nConteúdo informativo. Cada caso exige análise individual.\n\n#carreira #executivos #contratodetrabalho #direitotrabalhista #advogadotrabalhista'),
]

TPL = '''<!DOCTYPE html><html><head><meta charset="utf-8"><style>
*{margin:0;padding:0;box-sizing:border-box}
body{width:1080px;height:1350px;background:#f4efe6;font-family:'Poppins',sans-serif;color:#1d2633;padding:110px 80px 0;position:relative}
.k{color:#a87d45;font-size:30px;margin-bottom:26px}
h1{font-family:'Lora',serif;font-weight:500;font-size:68px;line-height:1.1;color:#101a27}
.l{margin-top:56px}
.i{display:flex;gap:30px;align-items:flex-start;padding:30px 0;border-bottom:1px solid #e2d6c3}
.n{flex:0 0 52px;height:52px;border:2px solid #b08d57;border-radius:50%;color:#a87d45;font-size:26px;display:flex;align-items:center;justify-content:center;margin-top:4px}
.t{font-size:38px;line-height:1.3}
.ft{margin-top:40px;font-size:31px;color:#5d6672}
.f{position:absolute;left:80px;right:80px;bottom:56px;border-top:1px solid #d8c9b0;padding-top:28px;display:flex;justify-content:space-between;align-items:flex-end}
.f img{height:72px}
.f .x{text-align:right;font-size:26px;color:#5d6672;line-height:1.35}
.f .x b{color:#101a27;font-weight:500}
</style></head><body>
<div class="k">{k}</div><h1>{h}</h1>
<div class="l">{items}</div>
<p class="ft">{foot}</p>
<div class="f"><img src="{logo}"><div class="x"><b>advogadodoexecutivo.com.br</b><br>WhatsApp (61) 99896-0202 · OAB/DF 42.071</div></div>
</body></html>'''

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1080, 'height': 1350})
        for po in POSTS:
            items = ''.join(f'<div class="i"><div class="n">{i+1}</div><div class="t">{t}</div></div>' for i, t in enumerate(po['items']))
            html = TPL.replace('{k}', po['k']).replace('{h}', po['h']).replace('{items}', items).replace('{foot}', po['foot']).replace('{logo}', LOGO)
            f = pathlib.Path('/tmp/p.html'); f.write_text(html)
            await pg.goto('file:///tmp/p.html'); await pg.wait_for_timeout(300)
            ov = await pg.evaluate("document.querySelector('.ft').getBoundingClientRect().bottom > document.querySelector('.f').getBoundingClientRect().top - 20")
            await pg.screenshot(path=str(OUT / (po['file'] + '.jpg')), type='jpeg', quality=92)
            print(po['file'], 'OVERLAP' if ov else 'ok')
        await b.close()
    json.dump(POSTS, open('/home/claude/advogadodoexecutivo/tools/dez.json', 'w'), ensure_ascii=False, indent=1)

asyncio.run(main())
