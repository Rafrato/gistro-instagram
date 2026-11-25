"""Reels curto: contagem de estoque pelo celular (~16 s). Reaproveita as cenas do reel_cel."""
import copy, sys
import reel_cel as R

def cena(img, novo_t0, novo_t1, titulo=None):
    c = copy.deepcopy(next(c for c in R.CENAS if c.get('img') == img))
    d = novo_t0 - c['t0']
    for p in c['passos']: p['t'] += d
    c['t0'], c['t1'] = novo_t0, novo_t1
    if titulo: c['titulo'] = titulo
    return c

R.CENAS = [
    dict(tipo='gancho', t0=0.0, t1=1.9),
    cena('16-contagens.png', 1.9, 3.5, 'Escolha a categoria'),
    cena('17-contagem-nova.png', 3.5, 4.9, 'Escolha a categoria'),
    cena('19-contagem-celular-antes.png', 4.9, 5.9, 'Conte a prateleira'),
    cena('20-contagem-produto-1.png', 5.9, 7.2, 'Conte a prateleira'),
    cena('21-contagem-produto-2.png', 7.2, 8.5, 'Conte a prateleira'),
    cena('22-contagem-registrada.png', 8.5, 9.8, 'Confirme'),
    cena('23-contagem-confirmar.png', 9.8, 11.1, 'Confirme'),
    cena('24-contagem-confirmada.png', 11.1, 13.4, 'Estoque ajustado'),
    dict(tipo='fim', t0=13.4, t1=17.4),
]
R.LEGENDAS = [
    (1.9, 4.9, 'Uma categoria por vez, pelo celular.'),
    (4.9, 8.5, 'Digite o que tem na prateleira e registre.'),
    (8.5, 11.1, 'Confirmou?'),
    (11.1, 13.4, 'O estoque se ajusta, com o histórico de cada diferença.'),
]
R.GANCHO = [(0.0, 'Contar o'), (0.0, 'estoque'), (0.7, 'sem fechar'), (0.7, 'a loja?')]

if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == 'quadro': R.render(sys.argv[3], so=float(sys.argv[2]))
    else: R.render(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/reels/reels-contagem-celular.mp4')
