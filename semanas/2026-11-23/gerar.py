# Artes da semana 2026-11-23. Rode a partir da raiz do repositório: python3 semanas/2026-11-23/gerar.py
import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
D = 'semanas/2026-11-23/'

# Terça 15:00 — problema e solução: mercadoria chega e o estoque não fica sabendo (Recebimentos)
a  = titulo(84, 190, ['A mercadoria chegou.', 'O estoque', 'sabe disso?'], destaque=2)
a += texto(84, 462, ['Guardou na prateleira, a nota foi para a gaveta', 'e o boleto só aparece no vencimento.'], 32)
a += janela(84, 560, 912, 'telas/recebimentos-lista.png')
k = 912/1146
a += marcar(84 + 812*k, 560 + 44 + 165*k, 166*k, 46*k)          # "Confirmado"
a += texto(84, 1000, ['Na prévia do Gistro, o recebimento registra', 'o que chegou: ao confirmar, o estoque', 'de cada produto é atualizado.'], 32, INK, 500)
a += personagem('joao', 'caixa', x=890, pe=1268, altura=360, espelhar=True) + assinatura()
salvar(post(a), D + 'terca.png')

# Quarta 12:00 — educativo: desconto x margem na semana da Black Friday (sem tela)
b  = titulo(84, 190, ['Desconto bom', 'é o que cabe', 'na margem.'], destaque=2)
cards = [('Preço cheio', 'Vende a R$ 50, custou R$ 30', 'sobra R$ 20'),
         ('Com 20% de desconto', 'Vende a R$ 40, custou R$ 30', 'sobra R$ 10'),
         ('Para voltar aos R$ 20', 'É preciso vender o dobro de peças', '2 peças')]
for i, (t, s, v) in enumerate(cards):
    yy = 500 + i*150
    b += (f'<rect x="84" y="{yy}" width="660" height="120" rx="20" fill="{LIME if i==2 else TINT}"/>'
          f'<text x="118" y="{yy+52}" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{t}</text>'
          f'<text x="118" y="{yy+92}" font-family="Inter" font-size="26" fill="{INK}" opacity=".7">{s}</text>'
          f'<text x="716" y="{yy+72}" text-anchor="end" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{v}</text>')
b += texto(84, 1010, ['Exemplo ilustrativo, por peça. Antes de anunciar', 'a oferta, refaça a conta com o seu custo real.'], 30)
b += personagem('lucia', 'pensa', x=900, pe=1262, altura=460) + assinatura()
salvar(post(b), D + 'quarta.png')

# Quinta 09:00 — funcionalidade: fechamento do mês para o contador (Integrações)
q  = titulo(84, 190, ['Fechar o mês', 'para o contador,', 'com o que conferir.'], 80, destaque=2)
q += janela(84, 440, 912, 'telas/integracoes-o-que-conferir.png')
q += marcar(84 + 12, 440 + 44 + 64, 888, 152)                 # as duas pendências
q += texto(84, 820, ['Na prévia do Gistro, o fechamento junta', 'os lançamentos e um resumo do mês, e avisa', 'o que ainda está pendente antes de enviar.'], 32, INK, 500)
q += objeto('calendario', 470, 960, 0.6)
q += personagem('carlos', 'aponta', x=880, pe=1268, altura=420, espelhar=True) + assinatura()
salvar(post(q), D + 'quinta-v2.png')
print('ok')
