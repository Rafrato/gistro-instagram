# Artes da semana 2026-11-30. Rode a partir da raiz do repositório: python3 semanas/2026-11-30/gerar.py
import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
D = 'semanas/2026-11-30/'

def cartoes(y0, itens, larg=700, alt=124, passo=152, verde=None):
    out = ''
    for i, (t, s, v) in enumerate(itens):
        yy = y0 + i * passo
        out += (f'<rect x="84" y="{yy}" width="{larg}" height="{alt}" rx="20" fill="{LIME if i == verde else TINT}"/>'
                f'<text x="118" y="{yy+52}" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{t}</text>'
                f'<text x="118" y="{yy+94}" font-family="Inter" font-size="26" fill="{INK}" opacity=".72">{s}</text>')
        if v: out += f'<text x="{84+larg-34}" y="{yy+74}" text-anchor="end" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{v}</text>'
    return out

# Segunda 09:00 — educativo: prazos do 13º (1ª parcela vence hoje)
a  = texto(84, 140, ['13º SALÁRIO · 2026'], 30, MUT, 700)
a += titulo(84, 250, ['A 1ª parcela', 'vence hoje.'], 96, destaque=1)
a += cartoes(430, [('1ª parcela', 'Metade do salário, sem descontos', 'até 30/11'),
                   ('2ª parcela', '20/12 é domingo, então antecipa', 'até 18/12'),
                   ('Separe agora', 'O valor da 2ª parcela, para dezembro não apertar', '')], larg=760, verde=2)
a += texto(84, 940, ['Vale para quem tem funcionário com', 'carteira assinada. Na 2ª parcela saem', 'o INSS e, quando houver, o IR.'], 30)
a += personagem('mari', 'pensa', x=900, pe=1268, altura=430) + assinatura()
salvar(post(a), D + 'segunda.png')

# Quarta 12:00 — engajamento: onde ficam as contas da loja?
b  = titulo(84, 190, ['Onde ficam', 'as contas da', 'sua loja?'], 92, destaque=2)
ops = [('1', 'No caderninho', 'recibo'), ('2', 'Numa planilha', 'notebook'), ('3', 'Num aplicativo', 'celular'), ('4', 'Na cabeça', 'fala')]
for i, (n, t, o) in enumerate(ops):
    x = 84 + (i % 2) * 466; y = 520 + (i // 2) * 300
    b += f'<rect x="{x}' + f'" y="{y}" width="446" height="270" rx="26" fill="{TINT}"/>'
    b += f'<circle cx="{x+62}" cy="{y+62}" r="38" fill="{LIME}"/><text x="{x+62}" y="{y+78}" text-anchor="middle" font-family="Inter Display, Inter" font-weight="700" font-size="44" fill="{INK}">{n}</text>'
    b += f'<text x="{x+34}" y="{y+228}" font-family="Inter" font-weight="700" font-size="36" fill="{INK}">{t}</text>'
    b += objeto(o, x + 250, y + 14, 0.42)
b += texto(84, 1160, ['Responda com o número nos comentários.'], 34, INK, 600) + assinatura()
salvar(post(b), D + 'quarta.png')

# Quinta 09:00 — funcionalidade: contagem por partes (Estoque > Contagens)
q  = titulo(84, 190, ['Contar o estoque', 'sem fechar', 'a loja.'], 84, destaque=2)
q += janela(84, 440, 600, 'telas/contagem-celular.png')
q += texto(84, 1080, ['Na prévia do Gistro, dá para contar', 'uma categoria por vez, até pelo celular.', 'O que não foi contado continua como estava.'], 30, INK, 500)
q += personagem('ana', 'celular', x=890, pe=1268, altura=430, espelhar=True) + assinatura()
salvar(post(q), D + 'quinta.png')

# Sexta 10:00 — educativo: compras de fim de ano sem encalhe
s  = titulo(84, 190, ['Comprar para', 'as festas sem', 'encalhar em janeiro.'], 80, destaque=2)
s += cartoes(450, [('1. Olhe o que já vendeu', 'As últimas semanas dizem mais que o palpite', ''),
                   ('2. Compre em duas etapas', 'Uma parte agora, outra no meio de dezembro', ''),
                   ('3. Combine a troca antes', 'Pergunte ao fornecedor o que pode voltar', '')], larg=760)
s += texto(84, 960, ['Produto parado em janeiro é dinheiro que', 'saiu do caixa e ainda não voltou.'], 32)
s += personagem('joao', 'caixa', x=900, pe=1268, altura=360, espelhar=True) + assinatura()
salvar(post(s), D + 'sexta.png')
print('ok')
