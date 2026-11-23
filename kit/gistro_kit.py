"""Kit visual do Gistro para posts do Instagram.

Uso típico (rodar a partir da raiz do repositório):
    import sys; sys.path.insert(0, 'kit')
    from gistro_kit import *
    c  = titulo(84, 190, ['Acabou na hora', 'da venda?'], destaque=1)
    c += texto(84, 350, ['Contar a prateleira sempre parece', 'coisa para depois. Até faltar.'])
    c += janela(84, 460, 912, 'telas/contagens-sugestoes.png')
    c += personagem('ana', 'pensa', x=880, pe=1268, altura=470)
    c += assinatura()
    salvar(post(c), 'semanas/AAAA-MM-DD/terca.png')

Regras: fundo branco; verde só como destaque; texto em verde-escuro; personagens e objetos
sempre deste kit (nunca redesenhar); telas só da pasta telas/; a palavra Gistro no rodapé.
"""
import base64, os, subprocess, tempfile
from PIL import ImageFont
from elenco import pessoa, ELENCO
from objetos import ob, NOMES as OBJETOS

INK = '#112800'; LIME = '#9fe870'; MUT = '#59634f'; LINE = '#e3e6df'; TINT = '#eef4e9'; BRANCO = '#ffffff'
FONTE_TITULO = '/usr/share/fonts/opentype/inter/InterDisplay-Bold.otf'
POSES = ['normal', 'aponta', 'pensa', 'celular', 'comemora', 'caixa']

def _largura(txt, tam):
    try:
        return ImageFont.truetype(FONTE_TITULO, int(tam)).getlength(txt)
    except Exception:
        return len(txt) * tam * 0.52

def post(conteudo, fundo=BRANCO):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1350" viewBox="0 0 1080 1350"><rect width="1080" height="1350" fill="{fundo}"/>{conteudo}</svg>'

def titulo(x, y, linhas, tam=84, destaque=None):
    """Título forte; a linha `destaque` ganha o marca-texto verde."""
    out = []
    for i, l in enumerate(linhas):
        yy = y + i * tam * 1.12
        if destaque is not None and i == destaque:
            out.append(f'<rect x="{x-10}" y="{yy - tam*0.80}" width="{_largura(l, tam) + 20}" height="{tam*1.0}" rx="12" fill="{LIME}"/>')
        out.append(f'<text x="{x}" y="{yy}" font-family="Inter Display, Inter" font-weight="700" font-size="{tam}" letter-spacing="-1.5" fill="{INK}">{l}</text>')
    return ''.join(out)

def texto(x, y, linhas, tam=34, cor=MUT, peso=400):
    return ''.join(f'<text x="{x}" y="{y + i*tam*1.4}" font-family="Inter" font-size="{tam}" font-weight="{peso}" fill="{cor}">{l}</text>' for i, l in enumerate(linhas))

def _data(caminho):
    return 'data:image/png;base64,' + base64.b64encode(open(caminho, 'rb').read()).decode()

def janela(x, y, largura, imagem):
    """Recorte de tela dentro de uma janela de navegador. Use só arquivos de telas/."""
    from PIL import Image
    iw, ih = Image.open(imagem).size
    h = largura * ih / iw; cid = f'j{int(x)}{int(y)}'
    return (f'<rect x="{x}" y="{y}" width="{largura}" height="{h+44}" rx="18" fill="#fff" stroke="{LINE}" stroke-width="2"/>'
            f'<circle cx="{x+26}" cy="{y+22}" r="6" fill="{LINE}"/><circle cx="{x+46}" cy="{y+22}" r="6" fill="{LINE}"/><circle cx="{x+66}" cy="{y+22}" r="6" fill="{LINE}"/>'
            f'<clipPath id="{cid}"><rect x="{x+2}" y="{y+44}" width="{largura-4}" height="{h-2}" rx="14"/></clipPath>'
            f'<image x="{x}" y="{y+44}" width="{largura}" height="{h}" href="{_data(imagem)}" clip-path="url(#{cid})" preserveAspectRatio="none"/>')

def marcar(x, y, w, h):
    """Contorno verde em volta de um detalhe (coordenadas do post)."""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="none" stroke="{LIME}" stroke-width="6"/>'

def personagem(nome, pose='normal', x=880, pe=1268, altura=460, espelhar=False):
    """Coloca um personagem do elenco com os pés em (x, pe)."""
    k = altura / 830; sx = -k if espelhar else k
    return f'<g transform="translate({x} {pe}) scale({sx} {k}) translate(-200 -830)">{pessoa(nome, pose)}</g>'

def objeto(nome, x, y, escala=1.0):
    """Coloca um objeto do kit (caixa de 400x400) com o canto em (x, y)."""
    return f'<g transform="translate({x} {y}) scale({escala})">{ob(nome)}</g>'

def palavra(x, y, w, cor=INK, check=INK):
    h = w * 50 / 176
    return (f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="-4 4 176 50"><g fill="none" stroke="{cor}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round">'
            f'<path d="M33.73 16.27 A18 18 0 1 0 39 29 H28"/><path d="M51 23 V47"/><circle cx="51" cy="11" r="3.8" fill="{cor}" stroke="none"/>'
            f'<path d="M78 26 C76.3 24 73.8 23 71 23 C67 23 64.2 25.3 64.2 29 C64.2 32.6 67.3 34 71 35.2 C75 36.4 78 38 78 41.6 C78 45 75 47 71 47 C67.9 47 65.5 45.9 64 43.8"/>'
            f'<path d="M96 12 V41"/><path d="M91 23 H105"/><path d="M96 41 L100.5 47 L110 35" stroke="{check}"/><path d="M120 47 V31 C120 26.6 123.6 23 128 23 H131"/><circle cx="153" cy="35" r="12"/></g></svg>')

def assinatura():
    """A palavra Gistro no rodapé, sempre no mesmo lugar."""
    return palavra(84, 1222, 150)

def salvar(svg, destino):
    os.makedirs(os.path.dirname(destino) or '.', exist_ok=True)
    with tempfile.NamedTemporaryFile('w', suffix='.svg', delete=False) as f:
        f.write(svg); tmp = f.name
    subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1350', tmp, '-o', destino], check=True)
    os.unlink(tmp)
    return destino

# ---------- Stories (1080 x 1920) ----------
# Área segura: deixe livres os 250 px de cima e os 340 px de baixo (barra do Instagram e respostas).
def story(conteudo, fundo=BRANCO):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1080" height="1920" viewBox="0 0 1080 1920"><rect width="1080" height="1920" fill="{fundo}"/>{conteudo}</svg>'

def miniatura(caminho_png, x, y, largura):
    """Miniatura de um post do feed (1080x1350) com borda, para o story 'post novo'."""
    h = largura * 1350 / 1080; cid = f'm{int(x)}{int(y)}'
    return (f'<rect x="{x-3}" y="{y-3}" width="{largura+6}" height="{h+6}" rx="30" fill="{LINE}"/>'
            f'<clipPath id="{cid}"><rect x="{x}" y="{y}" width="{largura}" height="{h}" rx="28"/></clipPath>'
            f'<image x="{x}" y="{y}" width="{largura}" height="{h}" href="{_data(caminho_png)}" clip-path="url(#{cid})"/>')

def area_figurinha(x, y, w, h, rotulo='Enquete aqui'):
    """Espaço tracejado onde o proprietário cola a figurinha (enquete, pergunta, caixinha) no app."""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="28" fill="none" stroke="{MUT}" stroke-width="4" stroke-dasharray="16 12" opacity=".6"/>'
            f'<text x="{x+w/2}" y="{y+h/2+12}" text-anchor="middle" font-family="Inter" font-size="34" fill="{MUT}" opacity=".8">{rotulo}</text>')

def assinatura_story():
    return palavra(84, 1500, 170)

def salvar_story(svg, destino):
    os.makedirs(os.path.dirname(destino) or '.', exist_ok=True)
    with tempfile.NamedTemporaryFile('w', suffix='.svg', delete=False) as f:
        f.write(svg); tmp = f.name
    subprocess.run(['rsvg-convert', '-w', '1080', '-h', '1920', tmp, '-o', destino], check=True)
    os.unlink(tmp)
    return destino
