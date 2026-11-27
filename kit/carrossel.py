"""Peças de carrossel (1080x1350) reaproveitáveis. Use a partir da raiz do repositório."""
from gistro_kit import *

def pagina(n, total):
    return f'<text x="996" y="110" text-anchor="end" font-family="Inter" font-weight="600" font-size="30" fill="{MUT}">{n}/{total}</text>'

def rotulo(t, y=150):
    return texto(84, y, [t.upper()], 32, MUT, 700)

def arraste(y=1180, x=760):
    return (f'<rect x="{x}" y="{y-52}" width="236" height="72" rx="36" fill="{INK}"/>'
            f'<text x="{x+118}" y="{y-5}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="#fff">Arraste  →</text>')

def grande(x, y, txt, tam=150, cor=INK):
    return f'<text x="{x}" y="{y}" font-family="Inter Display, Inter" font-weight="700" font-size="{tam}" letter-spacing="-4" fill="{cor}">{txt}</text>'

def item(y, linhas, larg=912):
    return (f'<rect x="84" y="{y}" width="{larg}" height="130" rx="24" fill="{TINT}"/>'
            f'<rect x="118" y="{y+37}" width="56" height="56" rx="14" fill="{LIME}"/>'
            f'<path d="M132 {y+66} l10 10 l20 -22" fill="none" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>'
            + ''.join(f'<text x="204" y="{y+58+i*40}" font-family="Inter" font-weight="600" font-size="32" fill="{INK}">{l}</text>' for i, l in enumerate(linhas)))

def balao(y, linhas, tam=34, larg=860):
    """Balão de mensagem genérico (sem marca de aplicativo)."""
    h = 60 + len(linhas) * tam * 1.4
    out = (f'<rect x="84" y="{y}" width="{larg}" height="{h}" rx="34" fill="{TINT}"/>'
           f'<path d="M84 {y+h-40} l-26 40 l60 -18 z" fill="{TINT}"/>')
    out += ''.join(f'<text x="124" y="{y+62+i*tam*1.4}" font-family="Inter" font-size="{tam}" fill="{INK}">{l}</text>' for i, l in enumerate(linhas))
    return out, h

def botao(x, y, txt, larg, tam=36, fundo=INK, cor='#fff'):
    return (f'<rect x="{x}" y="{y}" width="{larg}" height="88" rx="44" fill="{fundo}"/>'
            f'<text x="{x+larg/2}" y="{y+58}" text-anchor="middle" font-family="Inter" font-weight="700" font-size="{tam}" fill="{cor}">{txt}</text>')
