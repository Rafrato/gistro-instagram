"""Reels de texto animado (1080x1920, 30 fps), sem telas: frases que entram uma a uma."""
import subprocess, sys
from PIL import Image, ImageDraw
sys.path.insert(0, '/home/claude/reels/engine')
from reel2 import F, faixa, ease, INK, LIME, MUT, BG, W, H, FPS, fim

def quadro(cenas, t, fim_t0):
    fr = Image.new('RGB', (W, H), BG); d = ImageDraw.Draw(fr, 'RGBA')
    if t >= fim_t0:
        fim(fr, d, t - fim_t0); return fr
    cena = next(c for c in cenas if c['t0'] <= t < c['t1'])
    lt = t - cena['t0']
    if cena.get('rotulo'):
        d.text((84, 330), cena['rotulo'].upper(), font=F('Inter-SemiBold.otf', 40), fill=MUT)
    y = cena.get('y', 620)
    for ln in cena['linhas']:
        txt, tam, dest, atraso = ln['t'], ln.get('tam', 110), ln.get('d', False), ln.get('at', 0)
        f = F('InterDisplay-Bold.otf', tam)
        if lt >= atraso:
            k = ease((lt - atraso) / 0.22); yy = y + 36 * (1 - k)
            cor = ln.get('cor', INK)
            if dest:
                tw = d.textlength(txt, font=f)
                d.rounded_rectangle((64, yy + tam * 0.12, 64 + 36 + tw * k, yy + tam * 1.12), radius=18, fill=LIME + (int(255 * k),))
            d.text((82, yy), txt, font=f, fill=(cor if isinstance(cor, tuple) else INK) + (int(255 * k),))
        y += int(tam * ln.get('passo', 1.28))
    return fr

def render(cenas, fim_t0, total, saida):
    cmd = ['ffmpeg', '-y', '-loglevel', 'error', '-f', 'rawvideo', '-pix_fmt', 'rgb24', '-s', f'{W}x{H}', '-r', str(FPS), '-i', '-',
           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', saida]
    p = subprocess.Popen(cmd, stdin=subprocess.PIPE); prev = None; prev_c = None; n = 0
    for i in range(int(total * FPS)):
        t = i / FPS; f = quadro(cenas, t, fim_t0)
        c = 'fim' if t >= fim_t0 else next(k for k, cc in enumerate(cenas) if cc['t0'] <= t < cc['t1'])
        if prev_c is not None and c != prev_c: n, base = 5, prev
        if n > 0: f = Image.blend(base, f, 1 - n / 6); n -= 1
        p.stdin.write(f.tobytes()); prev_c = c
        if n == 0: prev = f
    p.stdin.close(); p.wait()
