INK='#112800'; LIME='#9fe870'; TINT='#eef4e9'; KRAFT='#d9b382'
def ob(nome):
    O={
 'prateleira': f'''<rect x="20" y="40" width="360" height="300" rx="10" fill="{TINT}"/>
  <path d="M20 140 H380 M20 240 H380" stroke="{INK}" stroke-width="10"/>
  <rect x="40" y="70" width="50" height="70" rx="6" fill="{LIME}"/><rect x="100" y="80" width="50" height="60" rx="6" fill="{LIME}"/><rect x="160" y="64" width="42" height="76" rx="18" fill="#ffffff" stroke="{INK}" stroke-width="3"/>
  <rect x="220" y="76" width="60" height="64" rx="6" fill="{KRAFT}"/><rect x="292" y="84" width="40" height="56" rx="16" fill="{INK}"/>
  <rect x="40" y="176" width="70" height="64" rx="6" fill="{KRAFT}"/><rect x="122" y="170" width="44" height="70" rx="18" fill="{LIME}"/>
  <rect x="190" y="186" width="120" height="50" rx="8" fill="none" stroke="{INK}" stroke-width="3" stroke-dasharray="10 8"/><text x="250" y="218" text-anchor="middle" font-family="Inter" font-weight="700" font-size="20" fill="{INK}">zerado</text>
  <rect x="40" y="270" width="44" height="70" rx="6" fill="#ffffff" stroke="{INK}" stroke-width="3"/><rect x="96" y="276" width="44" height="64" rx="6" fill="{LIME}"/><rect x="152" y="286" width="90" height="54" rx="6" fill="{KRAFT}"/><rect x="256" y="270" width="44" height="70" rx="18" fill="{INK}"/>''',
 'caixa': f'''<path d="M60 140 L200 90 L340 140 L340 300 L200 350 L60 300 Z" fill="{KRAFT}"/><path d="M200 190 L200 350 L60 300 L60 140 Z" fill="#c9a06c"/><path d="M60 140 L200 190 L340 140" fill="none" stroke="#b88d59" stroke-width="4"/><path d="M130 115 L270 165" stroke="#eed9b5" stroke-width="26"/>''',
 'recibo': f'''<path d="M110 40 H290 V330 L270 314 L250 330 L230 314 L210 330 L190 314 L170 330 L150 314 L130 330 L110 314 Z" fill="#ffffff" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>
  <path d="M136 90 H264 M136 130 H230 M136 170 H250 M136 210 H214" stroke="{TINT}" stroke-width="12" stroke-linecap="round"/><path d="M136 260 H264" stroke="{INK}" stroke-width="3" stroke-dasharray="6 6"/><rect x="200" y="272" width="64" height="22" rx="6" fill="{LIME}"/>''',
 'calendario': f'''<rect x="60" y="70" width="280" height="250" rx="22" fill="#ffffff" stroke="{INK}" stroke-width="4"/><path d="M60 92 Q60 70 82 70 H318 Q340 70 340 92 V130 H60 Z" fill="{INK}"/>
  <rect x="110" y="50" width="16" height="46" rx="8" fill="{LIME}"/><rect x="274" y="50" width="16" height="46" rx="8" fill="{LIME}"/>''' + ''.join(f'<rect x="{88+c*60}" y="{150+r*52}" width="40" height="34" rx="8" fill="{TINT}"/>' for r in range(3) for c in range(4)) + f'<circle cx="228" cy="219" r="30" fill="none" stroke="{LIME}" stroke-width="8"/>',
 'cofrinho': f'''<ellipse cx="200" cy="210" rx="130" ry="100" fill="{LIME}"/><circle cx="318" cy="200" r="34" fill="{LIME}"/><ellipse cx="336" cy="202" rx="16" ry="12" fill="#86d35a"/>
  <path d="M120 128 L136 92 L164 120 Z" fill="{LIME}"/><rect x="120" y="290" width="34" height="40" rx="10" fill="#86d35a"/><rect x="236" y="290" width="34" height="40" rx="10" fill="#86d35a"/>
  <rect x="168" y="112" width="70" height="12" rx="6" fill="{INK}"/><circle cx="290" cy="178" r="7" fill="{INK}"/><circle cx="210" cy="60" r="30" fill="#ffd166" stroke="{INK}" stroke-width="4"/><text x="210" y="70" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="{INK}">$</text>''',
 'calculadora': f'''<rect x="110" y="40" width="180" height="290" rx="26" fill="{INK}"/><rect x="132" y="66" width="136" height="60" rx="10" fill="{LIME}"/><text x="256" y="110" text-anchor="end" font-family="Inter" font-weight="700" font-size="30" fill="{INK}">2.500</text>''' + ''.join(f'<rect x="{134+c*46}" y="{146+r*44}" width="34" height="32" rx="8" fill="{"#ffffff" if (r,c)!=(3,2) else LIME}" opacity="{1 if (r,c)==(3,2) else .85}"/>' for r in range(4) for c in range(3)),
 'celular': f'''<rect x="120" y="20" width="160" height="320" rx="30" fill="{INK}"/><rect x="132" y="40" width="136" height="280" rx="20" fill="#ffffff"/>
  <rect x="146" y="70" width="108" height="70" rx="14" fill="{TINT}"/><circle cx="168" cy="96" r="12" fill="{LIME}"/><path d="M188 90 H240 M188 110 H226" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>
  <rect x="146" y="156" width="108" height="16" rx="8" fill="{TINT}"/><rect x="146" y="184" width="80" height="16" rx="8" fill="{TINT}"/><rect x="146" y="240" width="108" height="44" rx="12" fill="{LIME}"/>''',
 'notebook': f'''<rect x="70" y="60" width="260" height="180" rx="16" fill="{INK}"/><rect x="84" y="74" width="232" height="152" rx="8" fill="#ffffff"/>
  <path d="M104 196 L150 160 L190 176 L240 120 L296 100" fill="none" stroke="{LIME}" stroke-width="10" stroke-linecap="round" stroke-linejoin="round"/><path d="M104 206 H296" stroke="{TINT}" stroke-width="4"/>
  <path d="M40 250 H360 L340 280 H60 Z" fill="#59634f"/>''',
 'dinheiro': f'''<rect x="70" y="150" width="240" height="120" rx="14" fill="{LIME}" transform="rotate(-8 190 210)"/><circle cx="190" cy="210" r="30" fill="#ffffff" opacity=".7"/>
  <ellipse cx="290" cy="290" rx="56" ry="18" fill="#e8b93c"/><rect x="234" y="256" width="112" height="34" fill="#e8b93c"/><ellipse cx="290" cy="256" rx="56" ry="18" fill="#ffd166"/>
  <ellipse cx="290" cy="240" rx="56" ry="18" fill="#e8b93c"/><rect x="234" y="222" width="112" height="18" fill="#e8b93c"/><ellipse cx="290" cy="222" rx="56" ry="18" fill="#ffd166"/>''',
 'sacola': f'''<path d="M140 120 Q140 60 200 60 Q260 60 260 120" fill="none" stroke="{INK}" stroke-width="12"/><path d="M90 120 H310 L290 330 H110 Z" fill="{LIME}"/><path d="M90 120 H310 L306 160 H94 Z" fill="#86d35a"/><circle cx="200" cy="230" r="34" fill="#ffffff"/><text x="200" y="244" text-anchor="middle" font-family="Inter" font-weight="700" font-size="40" fill="{INK}">G</text>''',
 'etiqueta': f'''<path d="M90 120 L190 60 H320 V180 H190 Z" fill="#ffffff" stroke="{INK}" stroke-width="4" stroke-linejoin="round" transform="rotate(-10 200 120)"/><circle cx="150" cy="128" r="10" fill="{INK}"/><text x="252" y="132" text-anchor="middle" font-family="Inter" font-weight="700" font-size="32" fill="{INK}" transform="rotate(-10 200 120)">R$ 9,90</text>''',
 'alerta': f'''<circle cx="200" cy="180" r="130" fill="{TINT}"/><path d="M140 230 Q140 120 200 116 Q260 120 260 230 L276 252 H124 Z" fill="{LIME}"/><circle cx="200" cy="268" r="18" fill="{LIME}"/><circle cx="262" cy="118" r="30" fill="{INK}"/><text x="262" y="130" text-anchor="middle" font-family="Inter" font-weight="700" font-size="32" fill="#ffffff">3</text>''',
 'balcao': f'''<rect x="10" y="150" width="380" height="190" rx="12" fill="{INK}"/><rect x="0" y="130" width="400" height="30" rx="10" fill="#59634f"/><rect x="40" y="190" width="320" height="16" rx="8" fill="{LIME}" opacity=".5"/>
  <rect x="250" y="60" width="110" height="74" rx="10" fill="#3c4a5c"/><rect x="262" y="72" width="86" height="40" rx="6" fill="{LIME}"/>''',
 'planta': f'''<path d="M200 230 Q150 170 120 100 Q190 120 200 210 Q210 110 280 90 Q260 170 200 230 Z" fill="#86d35a"/><path d="M200 230 Q180 160 200 60 Q220 160 200 230 Z" fill="{LIME}"/><path d="M140 230 H260 L246 330 H154 Z" fill="{KRAFT}"/>''',
 'fala': f'''<path d="M60 70 H340 Q360 70 360 90 V220 Q360 240 340 240 H170 L110 290 L120 240 H60 Q40 240 40 220 V90 Q40 70 60 70 Z" fill="#ffffff" stroke="{INK}" stroke-width="4"/><path d="M80 120 H300 M80 160 H260 M80 200 H200" stroke="{TINT}" stroke-width="14" stroke-linecap="round"/>''',
    }
    return O[nome]
NOMES=['prateleira','caixa','recibo','calendario','cofrinho','calculadora','celular','notebook','dinheiro','sacola','etiqueta','alerta','balcao','planta','fala']
