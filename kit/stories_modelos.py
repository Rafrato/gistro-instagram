"""Modelos de story do Gistro (1080 x 1920). Use a partir da raiz do repositório.
Área segura: conteúdo entre y=250 e y=1580; a assinatura fica em y=1592.
Tipos: post_novo, dica, enquete (figurinha à mão), bastidores, checklist, mito_verdade, resumo, reels_novo."""
from gistro_kit import *
from gistro_kit import _data

def _fim(s): return story(s + assinatura_story().replace('y="1500"', 'y="1592"'))
def _rot(t): return texto(84, 330, [t.upper()], 34, MUT, 700)

def post_novo(png, frase):
    s = titulo(84, 330, ['Post novo', 'no perfil'], 96, destaque=1)
    s += miniatura(png, 190, 520, 700)
    s += texto(84, 1456, frase, 44, INK, 600)
    return _fim(s)

def reels_novo(frame_png, frase):
    s = titulo(84, 330, ['Reels novo', 'no perfil'], 96, destaque=1)
    from PIL import Image
    w = 520; h = w * 1920 / 1080; x = (1080 - w) / 2; y = 500
    s += (f'<rect x="{x-3}" y="{y-3}" width="{w+6}" height="{h+6}" rx="34" fill="{LINE}"/>'
          f'<clipPath id="rf"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="32"/></clipPath>'
          f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="{_data(frame_png)}" clip-path="url(#rf)"/>'
          f'<circle cx="540" cy="{y+h-120}" r="62" fill="{INK}" opacity=".9"/>'
          f'<path d="M522 {y+h-150} L522 {y+h-90} L568 {y+h-120} Z" fill="#fff"/>')
    s += texto(84, 1500, frase, 40, INK, 600)
    return story(s)          # sem assinatura: o quadro do vídeo já ocupa o espaço

def dica(rotulo, linhas, destaque, apoio=(), extra=''):
    s = _rot(rotulo) + titulo(84, 470, linhas, 92, destaque=destaque)
    y = 470 + len(linhas) * 103 + 40
    s += texto(84, y, list(apoio), 40, MUT) + extra
    return _fim(s)

def enquete(rotulo, linhas, destaque, opcoes, apoio=()):
    s = _rot(rotulo) + titulo(84, 470, linhas, 100, destaque=destaque)
    y = 470 + len(linhas) * 112
    s += area_figurinha(84, y, 760, 280, 'Enquete: ' + ' / '.join(opcoes))
    s += texto(84, y + 380, list(apoio), 40, INK, 500)
    return _fim(s)

def bastidores(linhas, destaque, tela, apoio):
    s = _rot('Bastidores da prévia') + titulo(84, 470, linhas, 88, destaque=destaque)
    y = 470 + len(linhas) * 99 + 10
    from PIL import Image
    iw, ih = Image.open(tela).size; w = 912; h = w * ih / iw
    if h > 600: h = 600; w = h * iw / ih          # tela alta: limita a altura para o texto caber
    s += janela((1080 - w) / 2 if w < 912 else 84, y, w, tela)
    s += texto(84, y + h + 44 + 80, list(apoio), 38, INK, 500)
    return _fim(s)

def checklist(rotulo, linhas, destaque, itens, rodape=()):
    s = _rot(rotulo) + titulo(84, 470, linhas, 92, destaque=destaque)
    y = 470 + len(linhas) * 103 + 30
    for i, it in enumerate(itens):
        yy = y + i * 150
        s += (f'<rect x="84" y="{yy}" width="912" height="122" rx="22" fill="{TINT}"/>'
              f'<rect x="114" y="{yy+33}" width="56" height="56" rx="14" fill="#fff" stroke="{INK}" stroke-width="4"/>')
        s += texto(200, yy + 56, it, 34, INK, 600) if isinstance(it, list) else texto(200, yy + 74, [it], 36, INK, 600)
    s += texto(84, y + len(itens) * 150 + 50, list(rodape), 36, MUT)
    return _fim(s)

def mito_verdade(frase, veredito, explicacao):
    s = _rot('Mito ou verdade?') + titulo(84, 470, frase, 84)
    y = 470 + len(frase) * 94 + 60
    s += (f'<rect x="84" y="{y}" width="360" height="110" rx="55" fill="{LIME}"/>'
          f'<text x="264" y="{y+74}" text-anchor="middle" font-family="Inter Display, Inter" font-weight="700" font-size="60" fill="{INK}">{veredito}</text>')
    s += texto(84, y + 200, explicacao, 40, INK, 500)
    return _fim(s)

def resumo(titulo_linhas, itens):
    """itens: [(png_do_post, 'Seg · 13º salário'), ...] em grade 2 x 2."""
    s = titulo(84, 330, titulo_linhas, 92, destaque=len(titulo_linhas) - 1)
    for i, (png, leg) in enumerate(itens[:4]):
        x = 120 + (i % 2) * 450; y = 480 + (i // 2) * 540
        s += miniatura(png, x, y, 390)
        s += texto(x, y + 488 + 40, [leg], 28, INK, 600)
    return _fim(s)
