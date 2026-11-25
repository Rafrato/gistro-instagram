# Carrosséis da semana 2026-11-30 (1080x1350 cada tela) e a quinta com tela em destaque.
# python3 semanas/2026-11-30/carrosseis.py
import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
D = 'semanas/2026-11-30/'

def pagina(n, total):
    return f'<text x="996" y="110" text-anchor="end" font-family="Inter" font-weight="600" font-size="30" fill="{MUT}">{n}/{total}</text>'

def arraste(y=1180, x=760):
    return (f'<rect x="{x}" y="{y-52}" width="236" height="72" rx="36" fill="{INK}"/>'
            f'<text x="{x+118}" y="{y-5}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#fff">Arraste  →</text>')

def grande(x, y, txt, tam=150, cor=INK):
    return f'<text x="{x}" y="{y}" font-family="Inter Display, Inter" font-weight="700" font-size="{tam}" letter-spacing="-4" fill="{cor}">{txt}</text>'

def item(y, txt):
    return (f'<rect x="84" y="{y}" width="912" height="130" rx="24" fill="{TINT}"/>'
            f'<rect x="118" y="{y+37}" width="56" height="56" rx="14" fill="{LIME}"/>'
            f'<path d="M132 {y+66} l10 10 l20 -22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
            + ''.join(f'<text x="204" y="{y+58+i*40}" font-family="Inter" font-weight="600" font-size="32" fill="{INK}">{l}</text>' for i, l in enumerate(txt)))

# ---------- Segunda: 13º em 5 telas ----------
T = 5
s1  = texto(84, 150, ['13º SALÁRIO · 2026'], 32, MUT, 700) + pagina(1, T)
s1 += titulo(84, 300, ['As 2 datas', 'do 13º que', 'não dá para', 'perder.'], 116, destaque=3)
s1 += objeto('calendario', 560, 760, 0.95) + arraste() + assinatura()
salvar(post(s1), D + 'segunda-1.png')

s2  = texto(84, 150, ['1ª PARCELA'], 32, MUT, 700) + pagina(2, T)
s2 += grande(84, 360, 'até 30/11')
s2 += f'<rect x="84" y="420" width="360" height="76" rx="38" fill="{LIME}"/><text x="264" y="472" text-anchor="middle" font-family="Inter" font-weight="700" font-size="34" fill="{INK}">hoje, segunda</text>'
s2 += texto(84, 620, ['É a metade do salário,', 'sem descontos.'], 52, INK, 600)
s2 += texto(84, 820, ['Vale para quem tem funcionário', 'com carteira assinada.'], 36)
s2 += assinatura()
salvar(post(s2), D + 'segunda-2.png')

s3  = texto(84, 150, ['2ª PARCELA'], 32, MUT, 700) + pagina(3, T)
s3 += grande(84, 360, 'até 18/12')
s3 += f'<rect x="84" y="420" width="430" height="76" rx="38" fill="{LIME}"/><text x="299" y="472" text-anchor="middle" font-family="Inter" font-weight="700" font-size="34" fill="{INK}">sexta, não dia 20</text>'
s3 += texto(84, 620, ['O prazo da lei é 20/12, mas', 'em 2026 o dia 20 é domingo.', 'Por isso, pague até sexta.'], 52, INK, 600)
s3 += texto(84, 900, ['É nesta parcela que saem o INSS e,', 'quando houver, o Imposto de Renda.'], 36)
s3 += assinatura()
salvar(post(s3), D + 'segunda-3.png')

s4  = texto(84, 150, ['PARA DEZEMBRO NÃO APERTAR'], 32, MUT, 700) + pagina(4, T)
s4 += titulo(84, 300, ['Faça isto', 'ainda hoje:'], 104, destaque=1)
s4 += item(480, ['Separe o valor da 2ª parcela', 'numa conta à parte'])
s4 += item(640, ['Anote como conta a pagar', 'com vencimento em 18/12'])
s4 += item(800, ['Some as compras das festas e', 'as contas de janeiro que vêm aí'])
s4 += assinatura()
salvar(post(s4), D + 'segunda-4.png')

s5  = pagina(5, T)
s5 += titulo(84, 330, ['Salve para', 'lembrar do', 'dia 18.'], 120, destaque=2)
s5 += texto(84, 760, ['Comissão, hora extra e outras variáveis', 'mudam a conta. Na dúvida, confirme', 'os valores com o seu contador.'], 36)
s5 += f'<rect x="84" y="960" width="440" height="88" rx="44" fill="{INK}"/><text x="304" y="1018" text-anchor="middle" font-family="Inter" font-weight="700" font-size="36" fill="#fff">Siga @seugistro</text>'
s5 += personagem('mari', 'comemora', x=880, pe=1268, altura=440) + assinatura()
salvar(post(s5), D + 'segunda-5.png')

# ---------- Sexta: compras de fim de ano em 5 telas ----------
c1  = texto(84, 150, ['COMPRAS DE FIM DE ANO'], 32, MUT, 700) + pagina(1, T)
c1 += titulo(84, 300, ['Comprar para', 'as festas sem', 'encalhar em', 'janeiro.'], 108, destaque=3)
c1 += texto(84, 820, ['3 cuidados antes do', 'próximo pedido'], 44, INK, 600)
c1 += personagem('joao', 'caixa', x=860, pe=1268, altura=520, espelhar=True) + arraste(1000, 84) + assinatura()
salvar(post(c1), D + 'sexta-1.png')

def cuidado(n, tit, linhas, obj, nome):
    s  = pagina(n + 1, T) + texto(84, 150, [f'CUIDADO {n} DE 3'], 32, MUT, 700)
    s += grande(84, 360, f'{n}.', 200, LIME)
    s += titulo(84, 520, tit, 96, destaque=len(tit) - 1)
    y = 520 + len(tit) * 108 + 40
    s += texto(84, y, linhas, 40, INK, 500)
    s += objeto(obj, 680, 960, 0.8) + assinatura()
    salvar(post(s), D + nome)

cuidado(1, ['Olhe o que', 'já vendeu.'], ['As vendas das últimas semanas', '(e as de dezembro passado, se', 'houver) dizem mais que o palpite.'], 'calculadora', 'sexta-2.png')
cuidado(2, ['Compre em', 'duas etapas.'], ['Uma parte agora e outra no', 'meio de dezembro, quando você', 'já sabe o que está saindo.'], 'caixa', 'sexta-3.png')
cuidado(3, ['Combine a', 'troca antes.'], ['Pergunte ao fornecedor o que', 'pode voltar se não vender e', 'anote o combinado.'], 'recibo', 'sexta-4.png')

c5  = pagina(5, T)
c5 += titulo(84, 330, ['Produto parado', 'em janeiro é', 'dinheiro que', 'não voltou.'], 104, destaque=3)
c5 += texto(84, 860, ['Saiu do caixa e ainda está', 'na prateleira.'], 44, INK, 600)
c5 += f'<rect x="84" y="1010" width="560" height="88" rx="44" fill="{INK}"/><text x="364" y="1068" text-anchor="middle" font-family="Inter" font-weight="700" font-size="34" fill="#fff">Salve para a próxima compra</text>'
c5 += objeto('dinheiro', 700, 860, 0.7) + assinatura()
salvar(post(c5), D + 'sexta-5.png')

# ---------- Quinta: tela em destaque (sem personagem) ----------
from PIL import Image
q  = titulo(84, 150, ['Contar o estoque', 'sem fechar a loja.'], 80, destaque=1)
q += texto(84, 300, ['Uma categoria por vez, até pelo celular.'], 38, INK, 600)
iw, ih = Image.open('telas/contagem-celular.png').size; w = 820; h = w * ih / iw; x = (1080 - w) / 2; y0 = 350
q += janela(x, y0, w, 'telas/contagem-celular.png')
k = w / 390                       # css -> post (a captura começa em y = 122 css)
q += f'<rect x="{x + 22*k}" y="{y0 + 44 + (198-122)*k}" width="{346*k}" height="{118*k}" rx="22" fill="none" stroke="{LIME}" stroke-width="7"/>'
salvar(post(q), D + 'quinta.png')
print('ok')
