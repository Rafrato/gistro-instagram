"""Reels 1 do Gistro — montagem estilo Screen Studio (1080x1920, 30 fps).
Tempos em segundos absolutos; ajustar TEMPOS quando a narração chegar."""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
INK = (17, 40, 0); LIME = (159, 232, 112); MUT = (89, 99, 79); BG = (255, 255, 255); LINE = (227, 230, 223)
FD = '/usr/share/fonts/opentype/inter/'
def F(n, s): return ImageFont.truetype(FD + n, s)
CAP = '/mnt/user-data/uploads/gistro-reels-capturas/'
AS = '/home/claude/reels/assets/'
BOX = (30, 370, 1050, 1350)            # janela da tela do sistema
BW, BH = BOX[2] - BOX[0], BOX[3] - BOX[1]
CSS_W, CSS_H, ESC = 1440, 900, 2

def ease(t): t = max(0, min(1, t)); return t * t * (3 - 2 * t)
def lerp(a, b, k): return a + (b - a) * k
def c(x, y, w, h): return (x + w / 2, y + h / 2)

# ---------------- cenas ----------------
# passo: t (início do movimento, abs), alvo (css), zoom, cam (opcional), mov, clique, caixa (destaque)
TUDO = (0, 0, 1440, 900)
# passo: t (início), alvo (cursor, css), vista (retângulo que precisa ficar legível), mov (duração),
#        clique, caixa (destaque). A câmera enquadra a "vista"; o cursor e a câmera chegam juntos.
CENAS = [
  dict(tipo='gancho', t0=0.0, t1=3.4),
  dict(tipo='tela', t0=3.4, t1=8.0, img='painel.png', titulo='Seu dia, num olhar', passos=[
      dict(t=3.4, alvo=(760, 420), vista=TUDO),
      dict(t=4.1, alvo=(450, 720), vista=(176, 640, 910, 890), mov=1.2, caixa=(192, 680, 1112, 65)),
      dict(t=6.2, alvo=(850, 838), mov=0.9, caixa=(192, 810, 1112, 69.5)),
  ]),
  dict(tipo='tela', t0=8.0, t1=10.0, img='financeiro-antes.png', titulo='Financeiro', passos=[
      dict(t=8.0, alvo=(760, 420), vista=TUDO),
      dict(t=8.5, alvo=(538, 569), vista=(176, 210, 830, 600), mov=1.1, clique=True),
  ]),
  dict(tipo='tela', t0=10.0, t1=12.6, img='financeiro-vencidos.png', titulo='Financeiro', passos=[
      dict(t=10.0, alvo=(538, 569), vista=(176, 210, 830, 600)),
      dict(t=10.2, alvo=(600, 846), vista=(176, 520, 830, 890), mov=0.8, caixa=(168, 815, 1160, 75)),
      dict(t=11.2, alvo=(1268, 867), vista=(676, 520, 1330, 890), mov=0.9, clique=True),
  ]),
  dict(tipo='tela', t0=12.6, t1=13.9, img='financeiro-pagar.png', titulo='Financeiro', passos=[
      dict(t=12.6, alvo=(1268, 867), vista=(676, 520, 1330, 890)),
      dict(t=12.65, alvo=(652, 600), vista=(440, 260, 1000, 640), mov=0.75, clique=True),
  ]),
  dict(tipo='tela', t0=13.9, t1=15.2, img='financeiro-pago.png', titulo='Pago e registrado', passos=[
      dict(t=13.9, alvo=(652, 600), vista=(440, 260, 1000, 640)),
      dict(t=14.0, alvo=(610, 772), vista=(176, 520, 940, 830), mov=0.7, caixa=(168, 737.94, 1160, 82)),
  ]),
  dict(tipo='tela', t0=15.2, t1=21.2, img='estoque-compras.png', titulo='Lista de compras pronta', passos=[
      dict(t=15.2, alvo=(1000, 300), vista=TUDO),
      dict(t=15.8, alvo=(420, 246), vista=(176, 80, 830, 345), mov=1.2, caixa=(192, 221.19, 624.33, 37.5)),
      dict(t=17.8, alvo=(420, 322), mov=0.7, caixa=(192, 296.69, 624.33, 38)),
      dict(t=19.3, alvo=(760, 328), mov=0.8),
  ]),
  dict(tipo='tela', t0=21.2, t1=24.6, img='recebimento-rascunho.png', titulo='Chegou mercadoria?', passos=[
      dict(t=21.2, alvo=(560, 500), vista=TUDO),
      dict(t=21.9, alvo=(1110, 850), vista=(940, 380, 1330, 900), mov=1.3, clique=True),
  ]),
  dict(tipo='tela', t0=24.6, t1=29.2, img='recebimento-confirmado.png', titulo='Estoque atualizado', passos=[
      dict(t=24.6, alvo=(1110, 754), vista=(940, 284, 1330, 804)),
      dict(t=24.8, alvo=(1172, 306), vista=(940, 280, 1330, 880), mov=0.9, caixa=(972, 292.19, 187.61, 22)),
      dict(t=26.3, alvo=(1150, 746), mov=0.8, caixa=(986, 731.19, 304, 34.48)),
      dict(t=27.5, alvo=(1180, 802), mov=0.6, caixa=(986, 775.67, 304, 87.48)),
  ]),
  dict(tipo='tela', t0=29.2, t1=35.0, img='integracoes.png', titulo='Fechamento do mês', passos=[
      dict(t=29.2, alvo=(700, 600), vista=TUDO),
      dict(t=29.8, alvo=(422, 322), vista=(160, 80, 810, 400), mov=1.2, clique=True),
      dict(t=32.0, alvo=(1180, 205), vista=(674, 80, 1324, 400), mov=1.1, caixa=(829.2, 179.69, 476.8, 196)),
  ]),
  dict(tipo='fim', t0=35.0, t1=40.0),
]
LEGENDAS = [
  (3.4, 5.6, 'O Gistro abre o seu dia'), (5.6, 8.0, 'mostrando o que precisa de atenção.'),
  (8.0, 10.2, 'No financeiro, o que entra e sai'), (10.2, 11.9, 'fica em ordem de urgência.'),
  (11.9, 12.6, 'Pagou?'), (12.6, 15.2, 'Um clique e está registrado.'),
  (15.2, 18.2, 'No estoque, ele já monta a lista do que comprar'), (18.2, 21.2, 'pra cada produto voltar ao mínimo.'),
  (21.2, 22.3, 'Chegou mercadoria?'), (22.3, 25.4, 'Confirma o recebimento e o estoque se atualiza,'),
  (25.4, 29.2, 'com a nota e a conta a pagar no mesmo lugar.'),
  (29.2, 32.2, 'No fim do mês, você baixa tudo pro contador,'), (32.2, 35.0, 'sabendo o que ainda falta conferir.'),
  (35.0, 37.0, 'O Gistro está em construção.'), (37.0, 40.0, 'Segue o perfil pra acompanhar.'),
]
GANCHO = [(0.0, 'Conta vencendo,'), (0.9, 'produto acabando,'), (1.9, 'nota perdida…')]

# ---------------- desenho ----------------
_img = {}
def img(p):
    if p not in _img: _img[p] = Image.open(p).convert('RGB')
    return _img[p]
CUR = [(0, 0), (0, 34), (9, 26), (15, 40), (21, 37), (15, 24), (27, 24)]
def cursor(d, x, y, s=1.7):
    pts = [(x + px * s, y + py * s) for px, py in CUR]
    d.polygon([(px + 3, py + 4) for px, py in pts], fill=(0, 0, 0, 60))
    d.polygon(pts, fill=INK); d.line(pts + [pts[0]], fill=(255, 255, 255), width=4, joint='curve')
def wrap(d, txt, f, maxw):
    out, cur = [], ''
    for w in txt.split():
        t = (cur + ' ' + w).strip()
        if d.textlength(t, font=f) <= maxw: cur = t
        else: out.append(cur); cur = w
    return out + [cur] if cur else out
def faixa(d, txt, y, f, fg=INK, bg=LIME, x=None, pad=(22, 10)):
    tw = d.textlength(txt, font=f); x = (W - tw) / 2 if x is None else x
    d.rounded_rectangle((x - pad[0], y - pad[1] + 4, x + tw + pad[0], y + f.size + pad[1] + 8), radius=16, fill=bg)
    d.text((x, y), txt, font=f, fill=fg)

SOMBRA = Image.new('RGBA', (BW + 80, BH + 80), (0, 0, 0, 0))
ImageDraw.Draw(SOMBRA).rounded_rectangle((40, 50, BW + 40, BH + 50), radius=30, fill=(17, 40, 0, 45))
SOMBRA = SOMBRA.filter(ImageFilter.GaussianBlur(18))
MASK = Image.new('L', (BW, BH), 0); ImageDraw.Draw(MASK).rounded_rectangle((0, 0, BW - 1, BH - 1), radius=28, fill=255)

CY = (BOX[1] + BOX[3]) // 2
_sm = {}
def sombra_mask(bh):
    if bh not in _sm:
        sh = Image.new('RGBA', (BW + 80, bh + 80), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((40, 50, BW + 40, bh + 50), radius=30, fill=(17, 40, 0, 45))
        mk = Image.new('L', (BW, bh), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, BW - 1, bh - 1), radius=28, fill=255)
        _sm[bh] = (sh.filter(ImageFilter.GaussianBlur(18)), mk)
    return _sm[bh]

def suave(t): t = max(0.0, min(1.0, t)); return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2

def enquadra(v):
    """retângulo de leitura -> (cx, cy, vw) que o contém inteiro, dentro da imagem."""
    x0, y0, x1, y1 = v
    vw = max(x1 - x0, (y1 - y0) * BW / BH, CSS_W / 2.6)   # zoom máximo 2,6x
    vw = min(vw, CSS_W); vh = min(vw * BH / BW, CSS_H)
    cx = min(max((x0 + x1) / 2, vw / 2), CSS_W - vw / 2)
    cy = min(max((y0 + y1) / 2, vh / 2), CSS_H - vh / 2)
    return (cx, cy, vw)

def trilha(ps, t, chave, conv=lambda v: v):
    v = None
    for p in ps:
        if chave not in p: continue
        alvo = conv(p[chave])
        if v is None: v = alvo; continue
        if t <= p['t']: break
        k = suave((t - p['t']) / p.get('mov', 0.8))
        v = tuple(lerp(a, b, k) for a, b in zip(v, alvo))
    return v

def tela(fr, d, cena, t):
    ps = cena['passos']; src = img(CAP + cena['img'])
    cx, cy = trilha(ps, t, 'alvo')
    camx, camy, vw = trilha(ps, t, 'vista', enquadra)
    vh = min(vw * BH / BW, CSS_H)
    l = min(max(camx - vw / 2, 0), CSS_W - vw); tp = min(max(camy - vh / 2, 0), CSS_H - vh)
    bh = int(round(vh * BW / vw)); top = int(CY - bh / 2); box = (BOX[0], top, BOX[2], top + bh)
    crop = src.resize((BW, bh), Image.BICUBIC, box=(l * ESC, tp * ESC, (l + vw) * ESC, (tp + vh) * ESC))
    sh, mk = sombra_mask(bh)
    fr.paste(sh, (box[0] - 40, top - 40), sh)
    fr.paste(crop, (box[0], top), mk)
    d.rounded_rectangle(box, radius=28, outline=LINE, width=3)
    sc = BW / vw
    def tela_xy(x, y): return box[0] + (x - l) * sc, top + (y - tp) * sc
    for i, p in enumerate(ps):
        if 'caixa' in p:
            chega = p['t'] + p.get('mov', 0.8) * 0.8
            sai = ps[i + 1]['t'] + 0.15 if i + 1 < len(ps) else 99
            if chega <= t < sai:
                a = int(255 * ease((t - chega) / 0.25))
                x, y, w, h = p['caixa']; x0, y0 = tela_xy(x - 4, y - 4); x1, y1 = tela_xy(x + w + 4, y + h + 4)
                x0, x1 = max(x0, box[0] + 6), min(x1, box[2] - 6); y0, y1 = max(y0, box[1] + 6), min(y1, box[3] - 6)
                d.rounded_rectangle((x0, y0, x1, y1), radius=14, fill=LIME + (int(a * 0.18),))
                d.rounded_rectangle((x0, y0, x1, y1), radius=14, outline=LIME + (a,), width=6)
    px, py = tela_xy(cx, cy); s = 1.7
    for p in ps:
        if p.get('clique'):
            tc = p['t'] + p.get('mov', 0.8) + 0.05
            if 0 <= t - tc < 0.55:
                k = (t - tc) / 0.55; r = 16 + 80 * ease(k)
                d.ellipse((px - r, py - r, px + r, py + r), outline=LIME + (int(230 * (1 - k)),), width=9)
            if 0 <= t - tc < 0.18: s = 1.45
    if box[0] < px < box[2] - 10 and box[1] < py < box[3] - 10: cursor(d, px, py, s)
    if cena.get('titulo'):
        faixa(d, cena['titulo'], 262, F('InterDisplay-Bold.otf', 66), x=48)

def conferir():
    """No instante de cada clique/destaque: a vista inteira está no quadro? cursor dentro? escala do texto?"""
    for c in CENAS:
        if c['tipo'] != 'tela': continue
        ps = [dict(p, t=p['t'] - c['t0']) for p in c['passos']]
        for i, p in enumerate(ps):
            t = p['t'] + p.get('mov', 0) + 0.06
            camx, camy, vw = trilha(ps, t, 'vista', enquadra); vh = min(vw * BH / BW, CSS_H)
            l = min(max(camx - vw / 2, 0), CSS_W - vw); tp = min(max(camy - vh / 2, 0), CSS_H - vh)
            v = trilha(ps[:i + 1], t, 'vista'); cx, cy = trilha(ps, t, 'alvo')
            ok_v = v[0] >= l - 1 and v[2] <= l + vw + 1 and v[1] >= tp - 1 and v[3] <= tp + vh + 1
            ok_c = l + 10 < cx < l + vw - 25 and tp + 10 < cy < tp + vh - 30
            print(f"{c['img']:28} passo {i}  escala {BW / vw:4.2f}  vista {'ok' if ok_v else 'CORTADA'}  cursor {'ok' if ok_c else 'FORA'}")

def gancho(fr, d, t):
    f = F('InterDisplay-Bold.otf', 108); y = 620
    for t0, txt in GANCHO:
        if t >= t0:
            k = ease((t - t0) / 0.22); yy = y + 30 * (1 - k)
            tw = d.textlength(txt, font=f)
            d.rounded_rectangle((60, yy + 12, 60 + 36 + tw * k, yy + f.size + 26), radius=18, fill=LIME + (int(255 * k),))
            d.text((78, yy), txt, font=f, fill=INK + (int(255 * k),))
        y += 160
    if t >= 2.85:
        k = ease((t - 2.85) / 0.2)
        d.text((80, y + 30), 'olha só.', font=F('InterDisplay-Bold.otf', 84), fill=MUT + (int(255 * k),))

_rgba = {}
def img_rgba(p):
    if p not in _rgba: _rgba[p] = Image.open(p).convert('RGBA')
    return _rgba[p]

def fim(fr, d, t):
    pal = img_rgba(AS + 'palavra-720.png'); k = ease(t / 0.5)
    m = pal.copy(); m.putalpha(m.getchannel('A').point(lambda v: int(v * k)))
    fr.paste(m, ((W - pal.width) // 2, int(640 + 40 * (1 - k))), m)
    k2 = ease((t - 0.5) / 0.3)
    if k2 > 0:
        faixa(d, 'Em construção', int(1000 + 20 * (1 - k2)), F('InterDisplay-Bold.otf', 76), bg=LIME)
    k3 = ease((t - 2.0) / 0.3)
    if k3 > 0:
        f = F('InterDisplay-Bold.otf', 64); txt = 'Siga @seugistro'; tw = d.textlength(txt, font=f)
        x = (W - tw) / 2; y = 1150
        d.rounded_rectangle((x - 40, y - 14, x + tw + 40, y + f.size + 26), radius=60, fill=INK + (int(255 * k3),))
        d.text((x, y), txt, font=f, fill=(255, 255, 255, int(255 * k3)))

def legenda(d, t, em_fim):
    if em_fim: return
    for t0, t1, txt in LEGENDAS:
        if t0 <= t < t1:
            f = F('Inter-SemiBold.otf', 50); y = 1398
            for ln in wrap(d, txt, f, 920):
                tw = d.textlength(ln, font=f); x = (W - tw) / 2
                d.rounded_rectangle((x - 20, y - 8, x + tw + 20, y + f.size + 16), radius=14, fill=INK + (240,))
                d.text((x, y), ln, font=f, fill=(255, 255, 255)); y += f.size + 30

def quadro(t):
    fr = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(fr, 'RGBA')
    cena = next(c for c in CENAS if c['t0'] <= t < c['t1']) if t < CENAS[-1]['t1'] else CENAS[-1]
    lt = t - cena['t0']
    if cena['tipo'] == 'gancho': gancho(fr, d, lt)
    elif cena['tipo'] == 'tela': tela(fr, d, dict(cena, passos=[dict(p, t=p['t'] - cena['t0']) for p in cena['passos']]), lt)
    else: fim(fr, d, lt)
    legenda(d, t, cena['tipo'] == 'fim')
    return fr, cena

def render(saida, audio=None, ate=None, so=None):
    fim_t = ate or CENAS[-1]['t1']
    if so is not None:
        quadro(so)[0].save(saida); return
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
    if audio: cmd += ['-i', audio, '-c:a', 'aac', '-b:a', '192k', '-af', 'apad', '-shortest']
    cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_c, prev_f, n_trans = None, None, 0
    for i in range(int(fim_t * FPS)):
        t = i / FPS; f, cena = quadro(t)
        if prev_c is not None and cena is not prev_c: n_trans, base = 5, prev_f
        if n_trans > 0:
            f = Image.blend(base, f, 1 - n_trans / 6); n_trans -= 1
        p.stdin.write(f.tobytes()); prev_c = cena
        if n_trans == 0: prev_f = f
    p.stdin.close(); p.wait()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'conferir':
        conferir()
    elif len(sys.argv) > 2 and sys.argv[1] == 'quadro':
        render(sys.argv[3] if len(sys.argv) > 3 else '/tmp/q.png', so=float(sys.argv[2]))
    else:
        render(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/reels/reels1-sem-voz.mp4')
