INK='#112800'; LIME='#9fe870'; TINT='#eef4e9'
ELENCO = {
 'ana':   dict(nome='Ana · mercearia',            pele='#b5754f', sombra='#9a5f3d', cabelo='#24150d', estilo='coque',   roupa='avental', cor='#112800', avental=LIME,     calca='#2f3a28', sapato='#1a1a1a'),
 'joao':  dict(nome='João · padaria',             pele='#e9b994', sombra='#cf9a74', cabelo='#5a3a22', estilo='curto',   roupa='avental', cor='#d6eac6', avental=INK,      calca='#3c4a5c', sapato='#2a2a2a', bigode=True),
 'bia':   dict(nome='Bia · serviços',             pele='#f2c9a8', sombra='#dba987', cabelo='#1c1c1c', estilo='longo',   roupa='camiseta',cor=LIME,      calca=INK,       sapato='#f4f4f4'),
 'lucia': dict(nome='Dona Lúcia · loja de roupas',pele='#f0c8a4', sombra='#d6a882', cabelo='#c9c9c9', estilo='coque',   roupa='cardigan',cor='#cfe3bf', blusa='#ffffff', calca='#59634f', sapato='#3a2a1f', oculos=True),
 'rafa':  dict(nome='Rafa · entregas',            pele='#6e4429', sombra='#58351f', cabelo='#140c07', estilo='crespo',  roupa='jaqueta', cor=INK,       detalhe=LIME,    calca='#2b3340', sapato='#f4f4f4', bone=LIME),
 'carlos':dict(nome='Carlos · oficina',           pele='#d29a72', sombra='#b47e58', cabelo='#2a2a2a', estilo='curto',   roupa='macacao', cor='#3c4a5c', blusa='#d6eac6', calca='#3c4a5c', sapato='#1a1a1a', barba=True, oculos=True),
 'mari':  dict(nome='Mari · salão de beleza',     pele='#c98d68', sombra='#ad7350', cabelo='#5b2c1a', estilo='rabo',    roupa='camiseta',cor='#3c4a5c', calca='#112800', sapato='#9fe870', faixa=LIME),
}
def tube(d,c,w): return f'<path d="{d}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
def braco(lado,pose,c,pele):
    s=-1 if lado=='e' else 1; X=lambda x: 200+s*(x-200)
    if pose=='baixo':  m,e,h=(264,350),(288,465),(280,552)
    elif pose=='aponta': m,e,h=(262,352),(322,300),(364,214)
    elif pose=='pensa':  m,e,h=(264,352),(292,456),(232,306)
    elif pose=='celular':m,e,h=(264,350),(282,450),(230,410)
    elif pose=='cima':   m,e,h=(262,346),(318,268),(330,170)
    elif pose=='frente': m,e,h=(264,352),(290,420),(272,456)
    o=[tube(f'M{X(m[0])} {m[1]} L{X(e[0])} {e[1]}',c,48), tube(f'M{X(e[0])} {e[1]} L{X(h[0])} {h[1]}',pele,34), f'<circle cx="{X(h[0])}" cy="{h[1]}" r="20" fill="{pele}"/>']
    if pose=='aponta': o.append(tube(f'M{X(370)} 200 L{X(380)} 178',pele,17))
    return o, (X(h[0]),h[1])
def pessoa(k, pose='normal', objeto=None):
    P=dict(ELENCO[k]); pele,sombra,cab,cor=P['pele'],P['sombra'],P['cabelo'],P['cor']
    poses={'normal':('baixo','baixo'),'aponta':('baixo','aponta'),'pensa':('baixo','pensa'),'celular':('baixo','celular'),'comemora':('cima','cima'),'caixa':('frente','frente')}
    pe,pd=poses[pose]
    manga = cor if P['roupa']!='macacao' else P['blusa']
    if P['roupa']=='cardigan': manga=cor
    g=['<ellipse cx="200" cy="812" rx="120" ry="14" fill="#eef4e9"/>']
    g.append(f'<path d="M146 560 L206 560 L196 790 L156 790 Z" fill="{P["calca"]}"/><path d="M194 560 L254 560 L244 790 L204 790 Z" fill="{P["calca"]}"/>')
    ol = 3 if P['sapato'] in ('#f4f4f4','#ffffff') else 0
    g.append(f'<ellipse cx="168" cy="796" rx="38" ry="15" fill="{P["sapato"]}" stroke="{INK}" stroke-width="{ol}"/><ellipse cx="236" cy="796" rx="38" ry="15" fill="{P["sapato"]}" stroke="{INK}" stroke-width="{ol}"/>')
    if P['estilo']=='longo': g.append(f'<path d="M122 230 Q116 340 146 378 L254 378 Q284 340 278 230 Z" fill="{cab}"/>')
    if P['estilo']=='rabo': g.append(f'<path d="M262 190 Q318 230 300 330 Q292 360 276 368 Q296 300 254 226 Z" fill="{cab}"/>')
    be,_=braco('e',pe,manga,pele); g+=be
    # tronco
    g.append(f'<path d="M132 332 Q200 306 268 332 Q290 420 282 500 Q284 540 266 578 L134 578 Q116 540 118 500 Q110 420 132 332 Z" fill="{cor if P["roupa"]!="macacao" else P["blusa"]}"/>')
    r=P['roupa']
    if r=='avental':
        a=P['avental']; g.append(f'<path d="M156 392 L244 392 L262 612 Q200 626 138 612 Z" fill="{a}"/>'+tube('M160 394 L178 330 M240 394 L222 330',a,9))
        g.append(f'<rect x="176" y="470" width="48" height="36" rx="8" fill="{"#ffffff" if a==LIME else LIME}" opacity=".8"/>')
    elif r=='camiseta':
        g.append(f'<path d="M176 336 L200 372 L224 336" fill="none" stroke="{INK}" stroke-width="4" stroke-linejoin="round" opacity=".3"/>')
    elif r=='cardigan':
        g.append(f'<path d="M184 334 L216 334 L214 578 L186 578 Z" fill="{P["blusa"]}"/>')
        g.append(''.join(f'<circle cx="222" cy="{y}" r="5" fill="{INK}" opacity=".5"/>' for y in (400,450,500)))
    elif r=='jaqueta':
        g.append(f'<path d="M198 330 L202 330 L202 578 L198 578 Z" fill="{P["detalhe"]}"/><path d="M134 520 H266" stroke="{P["detalhe"]}" stroke-width="10"/>')
        g.append(f'<rect x="228" y="400" width="30" height="18" rx="4" fill="{P["detalhe"]}"/>')
    elif r=='macacao':
        g.append(f'<path d="M146 420 L254 420 L268 580 L132 580 Z" fill="{cor}"/>'+tube('M156 422 L170 334 M244 422 L230 334',cor,16))
        g.append(f'<rect x="178" y="450" width="44" height="34" rx="6" fill="#ffffff" opacity=".25"/>')
        g.append(f'<path d="M146 560 L206 560 L196 790 L156 790 Z" fill="{cor}"/><path d="M194 560 L254 560 L244 790 L204 790 Z" fill="{cor}"/>')
    # pescoço e cabeça
    g.append(f'<path d="M180 280 H220 V338 Q200 350 180 338 Z" fill="{sombra}"/>')
    g.append(f'<circle cx="128" cy="246" r="14" fill="{pele}"/><circle cx="272" cy="246" r="14" fill="{pele}"/>')
    g.append(f'<ellipse cx="200" cy="236" rx="72" ry="80" fill="{pele}"/>')
    e=P['estilo']
    if e=='coque': g.append(f'<circle cx="200" cy="140" r="42" fill="{cab}"/><path d="M126 236 Q122 154 200 152 Q278 154 274 236 Q254 192 208 188 Q164 188 146 212 Q134 224 126 236 Z" fill="{cab}"/>')
    elif e=='curto': g.append(f'<path d="M128 226 Q126 156 200 154 Q270 154 274 222 Q272 236 268 240 Q260 200 226 192 Q186 210 144 202 Q134 212 128 226 Z" fill="{cab}"/>')
    elif e=='longo': g.append(f'<path d="M124 252 Q116 154 200 150 Q284 154 276 252 Q266 200 234 184 Q206 210 146 206 Q130 224 124 252 Z" fill="{cab}"/>')
    elif e=='rabo': g.append(f'<path d="M126 236 Q122 154 200 152 Q278 154 274 236 Q262 196 220 186 Q170 190 146 214 Q134 224 126 236 Z" fill="{cab}"/>')
    elif e=='crespo': g.append(''.join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{cab}"/>' for x,y,r in [(150,190,34),(180,165,36),(220,165,36),(250,190,34),(136,222,24),(264,222,24),(200,160,30)]))
    if P.get('faixa'): g.append(tube('M134 200 Q200 160 266 200',P['faixa'],14))
    if P.get('bone'):
        g.append(f'<path d="M130 210 Q132 150 200 148 Q268 150 270 210 Z" fill="{P["bone"]}"/><path d="M200 206 Q260 200 300 214 Q262 226 200 220 Z" fill="{INK}"/>')
    # rosto
    g.append(tube('M164 222 Q176 215 188 222 M212 222 Q224 215 236 222',INK,4).replace('fill="none"','fill="none" opacity=".8"'))
    g.append(f'<ellipse cx="176" cy="244" rx="7" ry="8.5" fill="{INK}"/><ellipse cx="224" cy="244" rx="7" ry="8.5" fill="{INK}"/><circle cx="178" cy="241" r="2.2" fill="#fff"/><circle cx="226" cy="241" r="2.2" fill="#fff"/>')
    if P.get('oculos'): g.append(f'<circle cx="176" cy="245" r="19" fill="none" stroke="{INK}" stroke-width="4.5"/><circle cx="224" cy="245" r="19" fill="none" stroke="{INK}" stroke-width="4.5"/><path d="M195 244 H205" stroke="{INK}" stroke-width="4.5"/>')
    g.append(tube('M201 254 Q195 268 202 272',sombra,4))
    if P.get('barba'): g.append(f'<path d="M134 250 Q138 320 200 324 Q262 320 266 250 Q250 296 200 300 Q150 296 134 250 Z" fill="{cab}"/>')
    if P.get('bigode'): g.append(f'<path d="M178 286 Q200 274 222 286 Q214 296 200 292 Q186 296 178 286 Z" fill="{cab}"/>'+tube('M188 298 Q200 306 212 298',INK,4))
    elif pose=='comemora': g.append(f'<path d="M182 282 Q200 306 218 282 Z" fill="{INK}"/>')
    else: g.append(tube('M184 286 Q200 300 216 286',INK,4.5))
    g.append(f'<ellipse cx="156" cy="272" rx="13" ry="8" fill="#e8806a" opacity=".28"/><ellipse cx="244" cy="272" rx="13" ry="8" fill="#e8806a" opacity=".28"/>')
    bd,mao=braco('d',pd,manga,pele); g+=bd
    if pose=='celular':
        g.insert(-1, f'<g transform="rotate(-12 219 409)"><rect x="196" y="370" width="46" height="78" rx="9" fill="{INK}"/><rect x="202" y="378" width="34" height="58" rx="5" fill="{LIME}"/></g>')
    if pose=='caixa':
        g.append(f'<rect x="130" y="400" width="140" height="110" rx="8" fill="#d9b382"/><path d="M130 430 H270" stroke="#c49c68" stroke-width="6"/><rect x="184" y="400" width="32" height="40" fill="#eed9b5"/>')
        g.append(f'<circle cx="128" cy="456" r="20" fill="{pele}"/><circle cx="272" cy="456" r="20" fill="{pele}"/>')
    return '\n'.join(g)
