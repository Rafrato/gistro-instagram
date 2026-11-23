# gistro-instagram

Artes publicadas no Instagram do Gistro (@seugistro).

- `marca/` — logo oficial: o símbolo G (`simbolo.svg`, `simbolo-sem-fundo.svg`, `favicon.svg`) e a palavra Gistro (`palavra.svg`, `palavra-fundo-escuro.svg`), com versões em PNG.
- `semanas/AAAA-MM-DD/` — as 3 artes de cada semana (`terca.png`, `quarta.png`, `quinta.png`) e o `semana.json` com as legendas. A data é a da segunda-feira.
- `teste/` — arte usada para testar a ligação com o Metricool.

As imagens deste repositório são públicas: os links delas são enviados ao Metricool, que agenda os posts como rascunho para aprovação.

Cores: verde #9fe870, verde-escuro #112800, branco #ffffff.
Regra da logo: o símbolo G e a palavra Gistro nunca aparecem lado a lado (o G já é a primeira letra da palavra).

## Kit visual (estilo aprovado em 22/11/2026)
- Fundo branco quase sempre; verde #9fe870 só como destaque (marca-texto no título, detalhes); textos em #112800.
- `kit/gistro_kit.py` — funções para montar os posts (título, texto, janela com recorte de tela, personagem, objeto, assinatura). Exemplos em `kit/exemplos.py` e o resultado em `ilustracoes/exemplos/`.
- `ilustracoes/` — personagens fixos (Ana, João, Bia, Dona Lúcia, Rafa, Carlos, Mari) em 6 poses e 15 objetos. Ver `ilustracoes/LEIA-ME.md`.
- `telas/` — recortes de telas reais da prévia, só com dados de demonstração. Ver `telas/LEIA-ME.md`.
