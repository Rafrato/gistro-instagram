import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
# Apresentação
c  = titulo(84, 180, ['Organizar o negócio', 'não precisa tomar', 'o seu dia.'], 82, destaque=2)
c += texto(84, 470, ['Contas a pagar e a receber, estoque e documentos,', 'num lugar só. Estamos construindo o Gistro.'], 32)
for i,(n,p) in enumerate([('ana','normal'),('joao','aponta'),('bia','celular'),('rafa','caixa'),('lucia','normal')]):
    c += personagem(n, p, x=170+i*185, pe=1150, altura=500, espelhar=(n=='joao'))
c += f'<text x="996" y="1258" text-anchor="end" font-family="Inter" font-weight="600" font-size="30" fill="{INK}">Em construção · acompanhe por aqui</text>'
c += assinatura()
salvar(post(c), 'semanas/apresentacao/apresentacao-branco.png')
# Exemplos de referência
a  = titulo(84, 190, ['Acabou na hora', 'da venda?'], destaque=1)
a += texto(84, 350, ['Contar a prateleira sempre parece', 'coisa para depois. Até faltar.'])
a += janela(84, 460, 912, 'telas/contagens-sugestoes.png')
a += texto(84, 920, ['Na prévia do Gistro, a contagem já sugere', 'por onde começar: o que nunca foi contado', 'e o que está zerado.'], 32, INK, 500)
a += personagem('ana', 'pensa', x=880, pe=1268, altura=470) + assinatura()
salvar(post(a), 'ilustracoes/exemplos/terca-problema-solucao.png')
b  = titulo(84, 190, ['Vender muito', 'não é o mesmo', 'que lucrar.'], destaque=2)
for i,(t,s,v) in enumerate([('Faturamento','Tudo o que entrou','R$ 20.000'),('Custos e despesas','Mercadoria, aluguel, contas','− R$ 17.500'),('Lucro','O que sobrou de verdade','R$ 2.500')]):
    yy=520+i*150; b+=f'<rect x="84" y="{yy}" width="640" height="120" rx="20" fill="{LIME if i==2 else TINT}"/><text x="118" y="{yy+52}" font-family="Inter" font-weight="700" font-size="34" fill="{INK}">{t}</text><text x="118" y="{yy+92}" font-family="Inter" font-size="26" fill="{INK}" opacity=".7">{s}</text><text x="696" y="{yy+72}" text-anchor="end" font-family="Inter" font-weight="700" font-size="34" fill="{INK}">{v}</text>'
b += texto(84, 1030, ['Exemplo ilustrativo. Antes de comemorar', 'o mês, olhe a terceira linha.'], 30)
b += personagem('joao', 'aponta', x=880, pe=1262, altura=470, espelhar=True) + assinatura()
salvar(post(b), 'ilustracoes/exemplos/quarta-educativo.png')
q  = titulo(84, 190, ['Tudo o que entrou', 'e saiu, com o', 'quanto ficou.'], 80, destaque=2)
q += janela(84, 420, 912, 'telas/movimentacoes.png')
k=912/692; q += marcar(84+(764-168)*k-14, 420+44+(372-292)*k-12, 80*k+28, 26*k+24)
q += texto(84, 960, ['Movimentações, na prévia do Gistro:', 'cada entrada e saída com o motivo', 'e o saldo que ficou depois.'], 32, INK, 500)
q += personagem('bia', 'celular', x=930, pe=1268, altura=420) + assinatura()
salvar(post(q), 'ilustracoes/exemplos/quinta-funcionalidade.png')
print('ok')
