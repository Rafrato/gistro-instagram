# Stories da semana 2026-12-07. python3 semanas/2026-12-07/stories.py
import sys; sys.path.insert(0, 'kit')
from stories_modelos import *
D = 'semanas/2026-12-07/'
S = lambda svg, nome: salvar_story(svg, D + 'story-' + nome + '.png')
# Segunda
S(post_novo(D+'segunda-1.png', ['Vendeu bem e o dinheiro sumiu?', 'Os 4 lugares estão no perfil.']), 'seg-1')
S(enquete('Pergunta rápida', ['Você sabe quanto', 'tem a receber', 'hoje?'], 2, ['Sei', 'Não faço ideia']), 'seg-2')
S(mito_verdade(['"Faturou bem,', 'então lucrou', 'bem."'], 'Mito',
    ['Faturamento é o total vendido.', 'Lucro é o que sobra depois de pagar', 'mercadoria, contas e impostos.']), 'seg-3')
# Terça
S(dica('Dica de cobrança', ['Lembre o cliente', 'um dia antes,', 'não um dia depois.'], 2,
    ['O lembrete antes do vencimento evita', 'o atraso e a conversa chata depois.'], objeto('calendario', 300, 1080, 1.0)), 'ter-1')
S(reels_novo(D+'reels-estoque-quadro.png', ['Quantos dias o seu estoque dura?', 'A conta está no Reels.']), 'ter-2')
S(checklist('Fim do expediente', ['Antes de fechar', 'o caixa do dia:'], 1,
    ['Contei o dinheiro da gaveta', 'Anotei as retiradas do dia', 'Conferi as vendas no cartão', 'Separei o troco de amanhã'],
    ['Cinco minutos hoje poupam uma hora', 'de procura no fim do mês.']), 'ter-3')
# Quarta
S(dica('Dica de estoque', ['Estoque mínimo', 'não é chute.'], 1,
    ['Multiplique a venda média por dia pelos', 'dias que o fornecedor leva para entregar.', 'Some uma folga para os dias de movimento.']), 'qua-1')
S(post_novo(D+'quarta.png', ['Na hora ou no fim do dia?', 'Responda com 1 ou 2 no post.']), 'qua-2')
S(enquete('Pergunta rápida', ['Você fecha', 'o caixa', 'todo dia?'], 2, ['Sempre', 'Às vezes']), 'qua-3')
# Quinta
S(post_novo(D+'quinta.png', ['O dia começa pelo que', 'precisa de você. Veja no perfil.']), 'qui-1')
S(dica('Lembrete', ['Faltam 8 dias', 'para a 2ª parcela', 'do 13º.'], 0,
    ['O prazo é sexta, 18/12, porque o dia 20', 'cai num domingo. Já separou o valor?'], objeto('calendario', 300, 1080, 1.0)), 'qui-2')
S(reels_novo(D+'reels-dinheiro-quadro.png', ['Vendeu bem e o dinheiro sumiu?', 'O Reels mostra onde procurar.']), 'qui-3')
# Sexta
S(post_novo(D+'sexta-1.png', ['3 mensagens para cobrar', 'sem climão. Veja no perfil.']), 'sex-1')
S(enquete('Pergunta rápida', ['Já pensou nas', 'contas de', 'janeiro?'], 2, ['Já', 'Ainda não']), 'sex-2')
S(resumo(['Resumo', 'da semana'], [(D+'segunda-1.png', 'Seg · Onde está o dinheiro'), (D+'quarta.png', 'Qua · Na hora ou no fim do dia'),
    (D+'quinta.png', 'Qui · O que precisa de você'), (D+'sexta-1.png', 'Sex · Cobrar sem climão')]), 'sex-3')
print('ok')
