# Artes da semana 2026-12-07. python3 semanas/2026-12-07/gerar.py
import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
from carrossel import *
from PIL import Image
D = 'semanas/2026-12-07/'

# ---------- Segunda 09:00 · carrossel: onde está o dinheiro (6 telas) ----------
T = 6
s = rotulo('Fluxo de caixa') + pagina(1, T)
s += titulo(84, 300, ['Vendeu bem', 'e o dinheiro', 'sumiu?'], 124, destaque=2)
s += texto(84, 760, ['4 lugares onde ele', 'costuma estar'], 48, INK, 600)
s += objeto('dinheiro', 640, 820, 0.9) + arraste(1040, 84) + assinatura()
salvar(post(s), D + 'segunda-1.png')

def lugar(n, tit, linhas, obj, nome):
    s = pagina(n + 1, T) + rotulo(f'Lugar {n} de 4')
    s += grande(84, 360, f'{n}.', 200, LIME)
    s += titulo(84, 520, tit, 100, destaque=len(tit) - 1)
    y = 520 + len(tit) * 112 + 40
    s += texto(84, y, linhas, 40, INK, 500)
    s += objeto(obj, 680, 960, 0.8) + assinatura()
    salvar(post(s), D + nome)

lugar(1, ['Na mão', 'do cliente.'], ['Venda a prazo, parcelado no cartão', 'e fiado entram na venda, mas', 'ainda não entraram no caixa.'], 'recibo', 'segunda-2.png')
lugar(2, ['Na', 'prateleira.'], ['Mercadoria comprada e ainda', 'não vendida é dinheiro que', 'saiu e ainda não voltou.'], 'caixa', 'segunda-3.png')
lugar(3, ['Nas', 'parcelas.'], ['A compra parcelada de meses atrás', 'continua tirando dinheiro do', 'caixa, mesmo sem venda nova.'], 'calendario', 'segunda-4.png')
lugar(4, ['No seu', 'bolso.'], ['Retirada sem controle para as', 'contas de casa mistura o dinheiro', 'da loja com o seu.'], 'calculadora', 'segunda-5.png')

s = pagina(6, T)
s += titulo(84, 330, ['Lucro não é', 'o mesmo que', 'dinheiro no caixa.'], 104, destaque=2)
s += texto(84, 760, ['Acompanhe os dois: o que sobrou no mês', 'e o que de fato entrou na conta.'], 40, INK, 500)
s += botao(84, 960, 'Salve para revisar no fim do mês', 640, 34)
s += assinatura()
salvar(post(s), D + 'segunda-6.png')

# ---------- Quarta 12:00 · engajamento: isso ou aquilo ----------
q = rotulo('Isso ou aquilo?')
q += titulo(84, 300, ['Na sua loja,', 'a conta paga é', 'anotada…'], 92, destaque=2)
for i, (n, t, o) in enumerate([('1', ['Na hora,', 'no balcão'], 'celular'), ('2', ['No fim do dia,', 'de uma vez'], 'recibo')]):
    x = 84 + i * 466
    q += f'<rect x="{x}" y="620" width="446" height="440" rx="30" fill="{LIME if i == 0 else TINT}"/>'
    q += f'<circle cx="{x+70}" cy="690" r="44" fill="#fff"/><text x="{x+70}" y="708" text-anchor="middle" font-family="Inter Display, Inter" font-weight="700" font-size="52" fill="{INK}">{n}</text>'
    q += objeto(o, x + 250, 650, 0.55)
    q += titulo(x + 36, 940, t, 46)
q += texto(84, 1150, ['Responda com 1 ou 2 nos comentários.'], 36, INK, 600) + assinatura()
salvar(post(q), D + 'quarta.png')

# ---------- Quinta 09:00 · tela em destaque: Precisa da sua atenção (celular) ----------
crop = Image.open('/mnt/user-data/uploads/gistro-reels-celular/02-painel-atencao.png').crop((150, 150, 1150, 1505))
crop.save('telas/celular-precisa-da-sua-atencao.png')
r = titulo(84, 150, ['O dia começa pelo', 'que precisa de você.'], 76, destaque=1)
r += texto(84, 290, ['Contas vencidas, valores atrasados e produtos zerados.'], 32, INK, 600)
iw, ih = crop.size; w = 620; x = (1080 - w) / 2 + 40
r += janela(x, 320, w, 'telas/celular-precisa-da-sua-atencao.png')
r += assinatura()
salvar(post(r), D + 'quinta.png')

# ---------- Sexta 10:00 · carrossel: cobrar sem climão (5 telas) ----------
T = 5
c = rotulo('Contas a receber') + pagina(1, T)
c += titulo(84, 300, ['Cliente atrasou?', 'Como cobrar', 'sem climão.'], 112, destaque=2)
c += texto(84, 740, ['3 mensagens prontas', 'para copiar e adaptar'], 48, INK, 600)
c += personagem('lucia', 'celular', x=860, pe=1268, altura=480, espelhar=True) + arraste(1000, 84) + assinatura()
salvar(post(c), D + 'sexta-1.png')

def mensagem(n, quando, linhas, nome):
    m = pagina(n + 1, T) + rotulo(f'Mensagem {n} de 3')
    m += titulo(84, 300, quando, 88, destaque=len(quando) - 1)
    b, h = balao(300 + len(quando) * 99 + 60, linhas, 38)
    m += b + assinatura()
    salvar(post(m), D + nome)

mensagem(1, ['1 dia antes', 'do vencimento'], ['Oi, [nome]! Passando para lembrar', 'que a parcela de R$ [valor] vence', 'amanhã. Qualquer dúvida, estou', 'por aqui.'], 'sexta-2.png')
mensagem(2, ['No dia seguinte', 'ao vencimento'], ['Oi, [nome], tudo bem? Não encontrei', 'o pagamento de R$ [valor], que', 'venceu ontem. Consegue verificar', 'para mim?'], 'sexta-3.png')
mensagem(3, ['Uma semana', 'depois'], ['Oi, [nome]. O valor de R$ [valor]', 'segue em aberto desde [data].', 'Podemos combinar uma data para', 'o pagamento?'], 'sexta-4.png')

c = pagina(5, T)
c += titulo(84, 300, ['3 cuidados que', 'evitam o atraso'], 96, destaque=1)
c += item(520, ['Combine o prazo por escrito', 'antes de vender'])
c += item(680, ['Cobre sempre pelo mesmo canal', 'e no mesmo tom'])
c += item(840, ['Anote cada contato: quando', 'cobrou e o que foi combinado'])
c += botao(84, 1030, 'Salve para a próxima cobrança', 600, 34) + assinatura()
salvar(post(c), D + 'sexta-5.png')
print('ok')
