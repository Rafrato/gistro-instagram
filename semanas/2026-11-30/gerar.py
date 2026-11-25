# Artes da semana 2026-11-30 (quarta). Segunda, quinta e sexta estão em carrosseis.py.
import sys; sys.path.insert(0, 'kit')
from gistro_kit import *
D = 'semanas/2026-11-30/'

def cartoes(y0, itens, larg=700, alt=124, passo=152, verde=None):
    out = ''
    for i, (t, s, v) in enumerate(itens):
        yy = y0 + i * passo
        out += (f'<rect x="84" y="{yy}" width="{larg}" height="{alt}" rx="20" fill="{LIME if i == verde else TINT}"/>'
                f'<text x="118" y="{yy+52}" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{t}</text>'
                f'<text x="118" y="{yy+94}" font-family="Inter" font-size="26" fill="{INK}" opacity=".72">{s}</text>')
        if v: out += f'<text x="{84+larg-34}" y="{yy+74}" text-anchor="end" font-family="Inter" font-weight="700" font-size="32" fill="{INK}">{v}</text>'
    return out

# Quarta 12:00 — engajamento: onde ficam as contas da loja?
b  = titulo(84, 190, ['Onde ficam', 'as contas da', 'sua loja?'], 92, destaque=2)
ops = [('1', 'No caderninho', 'recibo'), ('2', 'Numa planilha', 'notebook'), ('3', 'Num aplicativo', 'celular'), ('4', 'Na cabeça', 'fala')]
for i, (n, t, o) in enumerate(ops):
    x = 84 + (i % 2) * 466; y = 520 + (i // 2) * 300
    b += f'<rect x="{x}' + f'" y="{y}" width="446" height="270" rx="26" fill="{TINT}"/>'
    b += f'<circle cx="{x+62}" cy="{y+62}" r="38" fill="{LIME}"/><text x="{x+62}" y="{y+78}" text-anchor="middle" font-family="Inter Display, Inter" font-weight="700" font-size="44" fill="{INK}">{n}</text>'
    b += f'<text x="{x+34}" y="{y+228}" font-family="Inter" font-weight="700" font-size="36" fill="{INK}">{t}</text>'
    b += objeto(o, x + 250, y + 14, 0.42)
b += texto(84, 1160, ['Responda com o número nos comentários.'], 34, INK, 600) + assinatura()
salvar(post(b), D + 'quarta.png')

print('ok')
