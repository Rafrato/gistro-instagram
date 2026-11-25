# Stories extras da semana 23/11 (2 por dia, de quarta a sexta). python3 semanas/2026-11-23/stories_extras.py
import sys; sys.path.insert(0, 'kit')
from stories_modelos import *
D = 'semanas/2026-11-23/'
# Quarta 09:30 — dica para a Black Friday
salvar_story(dica('Dica rápida · Black Friday', ['Antes de sexta,', 'anote o custo', 'de cada produto.'], 2,
    ['Sem o custo na mão, você não sabe', 'até quanto pode dar de desconto', 'sem perder dinheiro.'],
    objeto('calculadora', 300, 1000, 1.1)), D + 'story-extra-qua-1.png')
# Quarta 18:30 — bastidores: lista de compras
salvar_story(bastidores(['A lista de compras', 'se monta sozinha.'], 1, 'telas/lista-de-compras.png',
    ['Para cada produto, o Gistro mostra quanto', 'falta para voltar ao estoque mínimo.']), D + 'story-extra-qua-2.png')
# Quinta 12:30 — checklist de fim de mês
salvar_story(checklist('Fim de mês', ['Antes de fechar', 'novembro, confira:'], 1,
    ['Contas pagas marcadas como pagas', 'As notas das compras estão guardadas', 'O saldo anotado bate com o extrato', 'O que ficou para dezembro está anotado'],
    ['Tire um print e use na segunda, dia 30.']), D + 'story-extra-qui-1.png')
# Quinta 18:30 — mito ou verdade
salvar_story(mito_verdade(['"Se tem dinheiro', 'no caixa, o mês', 'foi bom."'], 'Mito',
    ['O caixa pode estar cheio e ainda ter', 'conta para pagar na semana que vem.', 'O que conta é o que sobra depois', 'de pagar tudo o que é do mês.']), D + 'story-extra-qui-2.png')
# Sexta 08:30 — lembrete da conta da margem
salvar_story(dica('Hoje é Black Friday', ['Lembra da conta?', 'Com 20% de', 'desconto, a sobra', 'caiu pela metade.'], 3,
    ['Peça de R$ 50 que custou R$ 30: a sobra', 'vai de R$ 20 para R$ 10. A conta inteira', 'está no post de quarta, no perfil.']), D + 'story-extra-sex-1.png')
# Sexta 18:30 — reposição
salvar_story(dica('Fim do dia', ['Anote o que', 'mais saiu hoje.'], 1,
    ['É a sua lista de reposição da segunda,', 'antes que o cliente encontre a', 'prateleira vazia.'],
    objeto('prateleira', 300, 1010, 1.1)), D + 'story-extra-sex-2.png')
print('ok')
