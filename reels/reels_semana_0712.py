import sys; sys.path.insert(0, '/home/claude/reels/engine')
from reel_texto import render, quadro
VERM = (192, 57, 43)
# Terça: quantos dias o estoque dura (~16 s)
estoque = [
  dict(t0=0.0, t1=2.4, y=640, linhas=[dict(t='Quantos dias', tam=124), dict(t='o seu estoque', tam=124), dict(t='dura?', tam=124, d=True, at=0.5)]),
  dict(t0=2.4, t1=5.2, rotulo='A conta', y=560, linhas=[dict(t='estoque', tam=120), dict(t='÷ venda', tam=120, at=0.4), dict(t='por dia', tam=120, d=True, at=0.8)]),
  dict(t0=5.2, t1=8.8, rotulo='Exemplo', y=560, linhas=[dict(t='60 latas', tam=120), dict(t='÷ 8 por dia', tam=120, at=0.5), dict(t='= 7 dias e meio', tam=104, d=True, at=1.3)]),
  dict(t0=8.8, t1=12.6, rotulo='Mas atenção', y=560, linhas=[dict(t='O fornecedor', tam=96), dict(t='leva 10 dias', tam=96, at=0.3), dict(t='para entregar?', tam=96, at=0.6), dict(t='Você fica 2 dias', tam=96, d=True, at=1.6), dict(t='e meio sem o produto.', tam=90, d=True, at=1.9)]),
  dict(t0=12.6, t1=15.0, y=640, linhas=[dict(t='Peça antes', tam=124), dict(t='de chegar', tam=124, at=0.3), dict(t='no mínimo.', tam=124, d=True, at=0.7)]),
]
# Quinta: onde está o dinheiro (~17 s)
dinheiro = [
  dict(t0=0.0, t1=2.6, y=640, linhas=[dict(t='Vendeu bem', tam=124), dict(t='e o dinheiro', tam=124), dict(t='sumiu?', tam=124, d=True, at=0.5)]),
  dict(t0=2.6, t1=4.6, y=700, linhas=[dict(t='Ele pode estar', tam=110), dict(t='em 4 lugares.', tam=110, d=True, at=0.4)]),
  dict(t0=4.6, t1=6.8, rotulo='Lugar 1 de 4', y=600, linhas=[dict(t='Na mão', tam=124), dict(t='do cliente.', tam=124, d=True, at=0.3), dict(t='Fiado, prazo, cartão parcelado.', tam=50, at=0.8, passo=1.4)]),
  dict(t0=6.8, t1=9.0, rotulo='Lugar 2 de 4', y=600, linhas=[dict(t='Na', tam=124), dict(t='prateleira.', tam=124, d=True, at=0.3), dict(t='Comprado e ainda não vendido.', tam=50, at=0.8, passo=1.4)]),
  dict(t0=9.0, t1=11.2, rotulo='Lugar 3 de 4', y=600, linhas=[dict(t='Nas', tam=124), dict(t='parcelas.', tam=124, d=True, at=0.3), dict(t='Compras de meses atrás.', tam=50, at=0.8, passo=1.4)]),
  dict(t0=11.2, t1=13.4, rotulo='Lugar 4 de 4', y=600, linhas=[dict(t='No seu', tam=124), dict(t='bolso.', tam=124, d=True, at=0.3), dict(t='Retirada sem controle.', tam=50, at=0.8, passo=1.4)]),
  dict(t0=13.4, t1=16.0, y=640, linhas=[dict(t='Lucro não é', tam=116), dict(t='dinheiro', tam=116, at=0.3), dict(t='no caixa.', tam=116, d=True, at=0.6)]),
]
if __name__ == '__main__':
    if sys.argv[1] == 'quadros':
        for nome, c, f0 in [('e', estoque, 15.0), ('d', dinheiro, 16.0)]:
            for t in [1.5, 4.5, 8.0, 11.8, 14.5, 17.0]:
                quadro(c, t, f0).save(f'/tmp/k{nome}_{t}.png')
    else:
        render(estoque, 15.0, 19.0, '/home/claude/reels/reels-estoque-dias.mp4')
        render(dinheiro, 16.0, 20.0, '/home/claude/reels/reels-onde-esta-o-dinheiro.mp4')
