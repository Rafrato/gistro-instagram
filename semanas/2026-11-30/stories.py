# Stories da semana 2026-11-30 (3 por dia). python3 semanas/2026-11-30/stories.py
import sys; sys.path.insert(0, 'kit')
from stories_modelos import *
D = 'semanas/2026-11-30/'
S = lambda svg, nome: salvar_story(svg, D + 'story-' + nome + '.png')
# Segunda
S(post_novo(D+'segunda.png', ['A 1ª parcela do 13º vence hoje.', 'Os prazos estão no perfil.']), 'seg-1')
S(enquete('Pergunta rápida', ['Você tem', 'funcionário de', 'carteira assinada?'], 2, ['Tenho', 'Ainda não'],
    ['Queremos entender quem acompanha', 'o perfil para trazer dicas certas.']), 'seg-2')
S(dica('Hoje fecha novembro', ['Mande o mês', 'para o contador', 'esta semana.'], 2,
    ['Quanto antes ele recebe os lançamentos', 'e as notas, menos pergunta chega depois.'], objeto('calendario', 300, 1060, 1.0)), 'seg-3')
# Terça
S(bastidores(['O dia começa pelo', 'que precisa de você.'], 1, 'telas/painel-atencao.png',
    ['Contas vencidas, valores a receber', 'atrasados e produtos zerados, logo', 'na primeira tela.']), 'ter-1')
S(reels_novo(D+'reels-quadro.png', ['O nosso primeiro Reels: um tour', 'pela prévia. Veja no perfil.']), 'ter-2')
S(mito_verdade(['"Estoque parado', 'não custa nada."'], 'Mito',
    ['É dinheiro que já saiu do caixa e', 'ainda não voltou. Às vezes, o boleto', 'dele vence antes da venda.']), 'ter-3')
# Quarta
S(dica('Dica rápida', ['Pagou? Registre', 'na hora.'], 1,
    ['Conta paga e não anotada vira', 'comprovante para caçar no fim do mês.'], objeto('recibo', 300, 1000, 1.0)), 'qua-1')
S(post_novo(D+'quarta.png', ['Onde ficam as contas da sua loja?', 'Responda com o número no post.']), 'qua-2')
S(enquete('Pergunta rápida', ['Você confere o', 'estoque toda', 'semana?'], 2, ['Toda semana', 'Só quando falta']), 'qua-3')
# Quinta
S(post_novo(D+'quinta.png', ['Contar o estoque sem fechar a loja.', 'Veja no perfil.']), 'qui-1')
S(bastidores(['Contagem', 'pelo celular.'], 1, 'telas/contagem-celular.png',
    ['Anda pela prateleira, digita', 'a quantidade e registra.']), 'qui-2')
S(dica('Dica de contagem', ['Comece pelo que', 'está zerado', 'no sistema.'], 2,
    ['É onde mais aparece diferença: às vezes', 'o produto está na prateleira e o', 'controle não sabe.']), 'qui-3')
# Sexta
S(post_novo(D+'sexta.png', ['Comprar para as festas sem', 'encalhar em janeiro. Veja no perfil.']), 'sex-1')
S(enquete('Pergunta rápida', ['Já fez as', 'compras para', 'as festas?'], 2, ['Já fiz', 'Ainda não']), 'sex-2')
S(resumo(['Resumo', 'da semana'], [(D+'segunda.png', 'Seg · Prazos do 13º'), (D+'quarta.png', 'Qua · Onde ficam as contas'),
    (D+'quinta.png', 'Qui · Contagem por partes'), (D+'sexta.png', 'Sex · Compras de fim de ano')]), 'sex-3')
print('ok')
