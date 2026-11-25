"""Reels 2 do Gistro — usando pelo celular (1080x1920, 30 fps). Toques no lugar do mouse."""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFilter
from reel2 import F, faixa, wrap, ease, lerp, suave, img_rgba, INK, LIME, MUT, BG, LINE, W, H, FPS, AS

CAP = '/mnt/user-data/uploads/gistro-reels-celular/'
CSS_W, CSS_H, ESC = 390, 844, 3
MAXW, MAXH, CX, CY = 760, 1000, 540, 860       # moldura máxima do "celular" no quadro
ASP = MAXW / MAXH
TUDO = (0, 0, 390, 844)

def cx(x, y, w, h): return (x + w / 2, y + h / 2)
def tq(x, y, w, h): return (x + w - 2, y + h - 1)   # toque no canto do botão, sem cobrir o texto

CENAS = [
  dict(tipo='gancho', t0=0.0, t1=2.8),
  dict(tipo='tela', t0=2.8, t1=4.4, img='01-painel.png', titulo='Seu dia, num olhar', passos=[
      dict(t=2.8, vista=TUDO)]),
  dict(tipo='tela', t0=4.4, t1=7.0, img='02-painel-atencao.png', titulo='Seu dia, num olhar', passos=[
      dict(t=4.4, vista=TUDO),
      dict(t=4.6, vista=(52, 60, 390, 560), mov=1.0, caixa=(66, 140, 312, 115))]),
  dict(tipo='tela', t0=7.0, t1=8.6, img='05-financeiro-antes.png', titulo='Conta vencida', passos=[
      dict(t=7.0, vista=TUDO),
      dict(t=7.2, vista=(52, 50, 390, 560), mov=0.8, toque=tq(173.64, 80.89, 95.42, 34))]),
  dict(tipo='tela', t0=8.6, t1=10.6, img='06-financeiro-vencidos.png', titulo='Conta vencida', passos=[
      dict(t=8.6, vista=(52, 50, 390, 560)),
      dict(t=8.7, vista=(52, 290, 390, 720), mov=0.8, caixa=(60, 532, 325, 162)),
      dict(t=9.6, toque=tq(261.5, 662.95, 62.5, 32), mov=0.5)]),
  dict(tipo='tela', t0=10.6, t1=11.9, img='07-financeiro-pagar.png', titulo='Conta vencida', passos=[
      dict(t=10.6, vista=(52, 290, 390, 720)),
      dict(t=10.65, vista=(0, 230, 390, 610), mov=0.6, toque=tq(37, 542.94, 175.75, 37))]),
  dict(tipo='tela', t0=11.9, t1=14.0, img='09-financeiro-pago.png', titulo='Pago e registrado', passos=[
      dict(t=11.9, vista=(0, 230, 390, 610)),
      dict(t=12.0, vista=(52, 240, 390, 740), mov=0.7, caixa=(60, 565, 325, 165))]),
  dict(tipo='tela', t0=14.0, t1=15.6, img='10-lancamento-antes.png', titulo='Conta nova', passos=[
      dict(t=14.0, vista=TUDO),
      dict(t=14.2, vista=(52, 40, 390, 450), mov=0.8, toque=tq(64, 206.39, 152.3, 38))]),
  dict(tipo='tela', t0=15.6, t1=17.8, img='12-lancamento-preenchido.png', titulo='Conta nova', passos=[
      dict(t=15.6, vista=(52, 60, 390, 720)),
      dict(t=16.8, toque=tq(114, 674.39, 174.03, 35), mov=0.5)]),
  dict(tipo='tela', t0=17.8, t1=20.0, img='14-lancamento-na-lista.png', titulo='Lançada', passos=[
      dict(t=17.8, vista=TUDO),
      dict(t=18.0, vista=(52, 40, 390, 520), mov=0.8, caixa=(60, 95, 325, 180))]),
  dict(tipo='tela', t0=20.0, t1=21.6, img='16-contagens.png', titulo='Contagem no celular', passos=[
      dict(t=20.0, vista=TUDO),
      dict(t=20.2, vista=(52, 180, 390, 700), mov=0.8, toque=tq(103, 621.19, 149.08, 32))]),
  dict(tipo='tela', t0=21.6, t1=23.0, img='17-contagem-nova.png', titulo='Contagem no celular', passos=[
      dict(t=21.6, vista=(52, 180, 390, 700)),
      dict(t=21.7, vista=(52, 440, 390, 760), mov=0.7, toque=tq(88, 706.19, 178.66, 38))]),
  dict(tipo='tela', t0=23.0, t1=24.0, img='19-contagem-celular-antes.png', titulo='Contagem no celular', passos=[
      dict(t=23.0, vista=TUDO),
      dict(t=23.1, vista=(0, 0, 390, 470), mov=0.5, toque=tq(104, 206, 159.44, 56))]),
  dict(tipo='tela', t0=24.0, t1=25.3, img='20-contagem-produto-1.png', titulo='Contagem no celular', passos=[
      dict(t=24.0, vista=(0, 0, 390, 470)),
      dict(t=24.4, toque=tq(30, 272, 330, 38), mov=0.5)]),
  dict(tipo='tela', t0=25.3, t1=26.6, img='21-contagem-produto-2.png', titulo='Contagem no celular', passos=[
      dict(t=25.3, vista=(0, 0, 390, 470)),
      dict(t=25.7, toque=tq(30, 420.5, 330, 38), mov=0.5)]),
  dict(tipo='tela', t0=26.6, t1=27.9, img='22-contagem-registrada.png', titulo='Contagem no celular', passos=[
      dict(t=26.6, vista=(0, 0, 390, 470)),
      dict(t=26.65, vista=TUDO, mov=0.6, toque=tq(139.13, 780.75, 234.88, 38))]),
  dict(tipo='tela', t0=27.9, t1=29.2, img='23-contagem-confirmar.png', titulo='Contagem no celular', passos=[
      dict(t=27.9, vista=TUDO),
      dict(t=27.95, vista=(0, 220, 390, 580), mov=0.6, toque=tq(37, 470.25, 234.88, 38))]),
  dict(tipo='tela', t0=29.2, t1=31.2, img='24-contagem-confirmada.png', titulo='Estoque ajustado', passos=[
      dict(t=29.2, vista=TUDO),
      dict(t=29.4, vista=(52, 260, 390, 800), mov=0.8, caixa=(60, 640, 325, 150))]),
  dict(tipo='fim', t0=31.2, t1=36.2),
]
LEGENDAS = [
  (2.8, 4.6, 'O painel já abre mostrando'), (4.6, 7.0, 'o que precisa de atenção.'),
  (7.0, 8.6, 'Conta vencida?'), (8.6, 10.6, 'Toca em pagar,'), (10.6, 11.9, 'confirma…'),
  (11.9, 14.0, 'e pronto: tá registrado.'),
  (14.0, 15.6, 'Chegou uma conta nova?'), (15.6, 20.0, 'Lança na hora, de onde estiver.'),
  (20.0, 21.8, 'E a contagem de estoque?'), (21.8, 23.6, 'Anda pela prateleira'),
  (23.6, 27.4, 'e conta direto no celular.'), (27.4, 31.2, 'Confirmou, o estoque se ajusta.'),
  (31.2, 33.2, 'O Gistro está em construção.'), (33.2, 36.2, 'Segue o perfil pra acompanhar.'),
]
GANCHO = [(0.0, 'Longe do'), (0.0, 'computador?'), (1.2, 'Resolve pelo'), (1.2, 'celular.')]

_img = {}
def img(p):
    if p not in _img: _img[p] = Image.open(p).convert('RGB')
    return _img[p]

def enquadra(v):
    x0, y0, x1, y1 = v
    vw = min(max(x1 - x0, (y1 - y0) * ASP), CSS_W)
    vh = min(max(y1 - y0, vw / ASP), CSS_H)
    cxv = min(max((x0 + x1) / 2, vw / 2), CSS_W - vw / 2)
    cyv = min(max((y0 + y1) / 2, vh / 2), CSS_H - vh / 2)
    return (cxv, cyv, vw, vh)

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

_sm = {}
def moldura(bw, bh):
    k = (bw, bh)
    if k not in _sm:
        if len(_sm) > 400: _sm.clear()
        sh = Image.new('RGBA', (bw + 80, bh + 80), (0, 0, 0, 0))
        ImageDraw.Draw(sh).rounded_rectangle((40, 50, bw + 40, bh + 50), radius=46, fill=(17, 40, 0, 50))
        mk = Image.new('L', (bw, bh), 0); ImageDraw.Draw(mk).rounded_rectangle((0, 0, bw - 1, bh - 1), radius=44, fill=255)
        _sm[k] = (sh.filter(ImageFilter.GaussianBlur(18)), mk)
    return _sm[k]

def tela(fr, d, cena, t):
    ps = cena['passos']; src = img(CAP + cena['img'])
    cxv, cyv, vw, vh = trilha(ps, t, 'vista', enquadra)
    l = min(max(cxv - vw / 2, 0), CSS_W - vw); tp = min(max(cyv - vh / 2, 0), CSS_H - vh)
    s = min(MAXW / vw, MAXH / vh); bw, bh = int(round(vw * s)), int(round(vh * s))
    x0, y0 = CX - bw // 2, CY - bh // 2; box = (x0, y0, x0 + bw, y0 + bh)
    crop = src.resize((bw, bh), Image.BICUBIC, box=(l * ESC, tp * ESC, (l + vw) * ESC, (tp + vh) * ESC))
    sh, mk = moldura(bw, bh)
    fr.paste(sh, (x0 - 40, y0 - 40), sh); fr.paste(crop, (x0, y0), mk)
    d.rounded_rectangle(box, radius=44, outline=LINE, width=3)
    def xy(x, y): return x0 + (x - l) * s, y0 + (y - tp) * s
    for i, p in enumerate(ps):
        if 'caixa' in p:
            chega = p['t'] + p.get('mov', 0.8) * 0.8
            if t >= chega:
                a = int(255 * ease((t - chega) / 0.25))
                x, y, w, h = p['caixa']; a0, b0 = xy(x - 3, y - 3); a1, b1 = xy(x + w + 3, y + h + 3)
                a0, a1 = max(a0, box[0] + 6), min(a1, box[2] - 6); b0, b1 = max(b0, box[1] + 6), min(b1, box[3] - 6)
                d.rounded_rectangle((a0, b0, a1, b1), radius=16, fill=LIME + (int(a * 0.18),))
                d.rounded_rectangle((a0, b0, a1, b1), radius=16, outline=LIME + (a,), width=6)
        if 'toque' in p:
            tt = p['t'] + p.get('mov', 0.8) + 0.05          # instante do toque
            dt = t - tt
            if -0.3 <= dt < 0.5:
                px, py = xy(*p['toque'])
                ap = ease((dt + 0.3) / 0.2) if dt < 0 else (1 - ease((dt - 0.25) / 0.25))
                r = 34 if dt < 0 else 34 - 8 * ease(min(dt, 0.12) / 0.12) + 8 * ease(max(0, dt - 0.12) / 0.2)
                d.ellipse((px - r, py - r, px + r, py + r), fill=INK + (int(28 * ap),), outline=INK + (int(150 * ap),), width=4)
                if 0 <= dt < 0.5:
                    k = dt / 0.5; rr = 30 + 70 * ease(k)
                    d.ellipse((px - rr, py - rr, px + rr, py + rr), outline=LIME + (int(230 * (1 - k)),), width=8)
    if cena.get('titulo'):
        faixa(d, cena['titulo'], 262, F('InterDisplay-Bold.otf', 66), x=48)

def gancho(fr, d, t):
    f = F('InterDisplay-Bold.otf', 118); y = 640
    for i, (t0, txt) in enumerate(GANCHO):
        if t >= t0:
            k = ease((t - t0) / 0.22); yy = y + 30 * (1 - k)
            destaque = i >= 2
            tw = d.textlength(txt, font=f)
            if destaque:
                d.rounded_rectangle((60, yy + 14, 60 + 40 + tw * k, yy + f.size + 28), radius=18, fill=LIME + (int(255 * k),))
            d.text((80, yy), txt, font=f, fill=INK + (int(255 * k),))
        y += 150 if i != 1 else 190

def fim(fr, d, t):
    pal = img_rgba(AS + 'palavra-720.png'); k = ease(t / 0.5)
    m = pal.copy(); m.putalpha(m.getchannel('A').point(lambda v: int(v * k)))
    fr.paste(m, ((W - pal.width) // 2, int(640 + 40 * (1 - k))), m)
    k2 = ease((t - 0.5) / 0.3)
    if k2 > 0: faixa(d, 'Em construção', int(1000 + 20 * (1 - k2)), F('InterDisplay-Bold.otf', 76), bg=LIME)
    k3 = ease((t - 2.0) / 0.3)
    if k3 > 0:
        f = F('InterDisplay-Bold.otf', 64); txt = 'Siga @seugistro'; tw = d.textlength(txt, font=f)
        x = (W - tw) / 2; y = 1150
        d.rounded_rectangle((x - 40, y - 14, x + tw + 40, y + f.size + 26), radius=60, fill=INK + (int(255 * k3),))
        d.text((x, y), txt, font=f, fill=(255, 255, 255, int(255 * k3)))

def legenda(d, t):
    for t0, t1, txt in LEGENDAS:
        if t0 <= t < t1 and t < CENAS[-1]['t0']:
            f = F('Inter-SemiBold.otf', 50); y = 1398
            for ln in wrap(d, txt, f, 920):
                tw = d.textlength(ln, font=f); x = (W - tw) / 2
                d.rounded_rectangle((x - 20, y - 8, x + tw + 20, y + f.size + 16), radius=14, fill=INK + (240,))
                d.text((x, y), ln, font=f, fill=(255, 255, 255)); y += f.size + 30

def quadro(t):
    fr = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(fr, 'RGBA')
    cena = next((c for c in CENAS if c['t0'] <= t < c['t1']), CENAS[-1]); lt = t - cena['t0']
    if cena['tipo'] == 'gancho': gancho(fr, d, lt)
    elif cena['tipo'] == 'tela': tela(fr, d, dict(cena, passos=[dict(p, t=p['t'] - cena['t0']) for p in cena['passos']]), lt)
    else: fim(fr, d, lt)
    legenda(d, t)
    return fr, cena

def conferir():
    for c in CENAS:
        if c['tipo'] != 'tela': continue
        ps = [dict(p, t=p['t'] - c['t0']) for p in c['passos']]
        for i, p in enumerate(ps):
            alvo = p.get('toque') or (p.get('caixa') and cx(*p['caixa']))
            if not alvo: continue
            t = p['t'] + p.get('mov', 0) + 0.06
            cxv, cyv, vw, vh = trilha(ps, t, 'vista', enquadra)
            l = cxv - vw / 2; tp = cyv - vh / 2
            ok = l + 10 < alvo[0] < l + vw - 10 and tp + 10 < alvo[1] < tp + vh - 10
            print(f"{c['img']:30} passo {i}  escala {min(MAXW / vw, MAXH / vh):4.2f}  {'ok' if ok else 'FORA DO QUADRO'}")

def render(saida, audio=None, so=None):
    if so is not None: quadro(so)[0].save(saida); return
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-']
    if audio: cmd += ['-i', audio, '-c:a', 'aac', '-b:a', '192k', '-af', 'apad', '-shortest']
    cmd += ['-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    prev_c = prev_f = None; n = 0
    for i in range(int(CENAS[-1]['t1'] * FPS)):
        f, cena = quadro(i / FPS)
        if prev_c is not None and cena is not prev_c: n, base = 5, prev_f
        if n > 0: f = Image.blend(base, f, 1 - n / 6); n -= 1
        p.stdin.write(f.tobytes()); prev_c = cena
        if n == 0: prev_f = f
    p.stdin.close(); p.wait()

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'conferir': conferir()
    elif len(sys.argv) > 2 and sys.argv[1] == 'quadro': render(sys.argv[3], so=float(sys.argv[2]))
    else: render(sys.argv[1] if len(sys.argv) > 1 else '/home/claude/reels/reels2-celular-sem-voz.mp4')
