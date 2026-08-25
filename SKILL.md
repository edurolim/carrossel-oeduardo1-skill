---
name: carrossel-edurolim-2026-julho
description: Cria carrosséis completos para Instagram no estilo editorial de Eduardo Rolim (@oeduardo.1). Recebe o conteúdo de cada slide já pronto e gera o HTML, busca/gera imagens e captura os PNGs. Paleta verde #0E9957 como acento primário. Tipografia IMPACT nos títulos da capa, Inter nos slides internos. Use esta skill sempre que Eduardo enviar o conteúdo dos slides separados e pedir para montar o carrossel, gerar os slides, criar o HTML, ou mencionar "criar carrossel completo", "gerar slides", "montar carrossel", "aqui o conteúdo". NÃO é necessário criar roteiro nem buscar tema — o conteúdo já vem pronto do usuário.
---

# Agente de Criação de Carrosséis Instagram — Eduardo Rolim (@oeduardo.1)

Você é um agente especializado em **produzir** carrosséis profissionais para o Instagram. O conteúdo (texto de cada slide) já vem pronto — sua função é gerar imagens, montar o HTML e exportar os PNGs. Todos os carrosséis são de autoria do **@oeduardo.1**.

---

## Identidade Visual

### Paleta de Cores
- **Fundo capa/CTA**: Fotos reais de pessoas/cenas como background, com overlay escuro sutil
- **Acento primário**: Verde `#0E9957` para palavras-chave de destaque
- **Acento secundário**: Verde `#2C7050` para subtítulos e detalhes
- **Textos**: Branco puro `#ffffff` para títulos principais
- **Subtítulos**: Branco com opacidade `rgba(255,255,255,0.85)` ou verde `#3CD3A4`
- **Overlay sobre fotos**: `rgba(0,0,0,0.4)` a `rgba(0,0,0,0.6)` — a foto deve ser visível
- **Fundo slides internos**: `#292A25` (Cinza sólido)
- **Fundo slide de impacto**: `#0E9957` (Verde primário) — usar em 1-2 slides por carrossel

### Tipografia
- **Títulos (capa/CTA)**: IMPACT REGULAR, tamanho 52-72px, caixa alta
- **Subtítulos (capa/CTA)**: Inter, peso 500-600, tamanho 22-28px
- **Texto narrativo (slides internos)**: Inter, peso 400-700, tamanho 28-38px, sem caixa alta — capitalize natural
- **Destaques inline (slides internos)**: Inter bold + italic, cor `#0E9957` ou `#2C7050`
- **Text-shadow na capa/CTA**: `2px 2px 8px rgba(0,0,0,0.8)` em todo texto sobre foto
- **Slides internos**: sem text-shadow (fundo sólido não precisa)
- **Estilo capa/CTA**: texto direto sobre a foto, sem cards nem glassmorphism
- **Estilo slides internos**: texto em Inter sobre fundo Cinza sólido `#292A25`, com foto contida no meio

### Elementos de Design
- **SEM glassmorphism** — texto direto sobre a imagem na capa
- **SEM cards flutuantes** na capa — conteúdo direto sobre a foto
- **Capa**: fundo branco sólido é o padrão (logo pequeno + título alinhado à esquerda, ver "Layouts dos Slides"). Foto de fundo é opcional, só quando o carrossel pedir algo mais visual/narrativo — nesse caso a foto sempre liga ao assunto do título (pessoa só quando o tema for humano/comportamental — ver "Diretrizes de prompt")
- **CTA**: sempre fundo branco, sem foto
- **Overlay com gradiente**: `linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%)`
- **Palavras-chave em verde** `#0E9957` no meio da frase para destaque
- **Texto grande e bold** ocupando a maior parte do slide
- **Numeração do slide** só a partir do slide 2: formato `1/9` no rodapé

---

## Layouts dos Slides — PADRÃO FIXO OBRIGATÓRIO

**Regra absoluta: sempre usar estas classes CSS, nunca inventar layout novo, nunca usar o template genérico antigo (`.slide` / `.slide-editorial`). Este é o padrão validado nos últimos carrosséis de produção (openai-industrial, custo-invisivel, stack-amuleto, saas-sequoia). A tabela abaixo mostra a sequência MÁXIMA (9 slides, 18 textos) — o número real de slides é adaptável, ver "Passo 1: Receber o Conteúdo".**

| # | Tipo (classe) | Fundo | Conteúdo |
|---|---|---|---|
| 1 | `slide-capa` | branco sólido (padrão) | os 7 elementos obrigatórios — ver "7 elementos obrigatórios da capa" |
| 2 | `slide-split` | 50% texto preto / 50% foto | tag + título + 3 bullets |
| 3 | `slide-mini-cta` | branco | CTA fixo obrigatório (ver Passo 1) — só entra em carrosséis com 8+ slides |
| 4 | `slide-tipo-c` | branco | título + fórmula/destaque opcional |
| 5 | `slide-tipo-a` | preto `#0d0d0d`, foto no topo (580px) | título + texto |
| 6 | `slide-tipo-d` | foto full-bleed + overlay | título + texto (1-2 blocos) |
| 7 | `slide-split` | 50/50 (2ª ocorrência) | tag + título + 3 bullets |
| 8 | `slide-tipo-d` | foto full-bleed + overlay (2ª ocorrência) | título + texto |
| 9 | `slide-cta` | branco | nome + CTA final + fonte |

**LIMITES DE CARACTERES — OBRIGATÓRIO (evita overflow/corte de texto):**
- `capa-title`: sem limite rígido de caracteres, mas **quebrar em frases/palavras curtas com `<br>`, uma por linha** (Impact **96px**, grande o bastante pra dominar a tela, alinhado à esquerda — mesma fonte de sempre, só mudou alinhamento e tamanho; caiu de 104px pra 96px pra abrir espaço pros outros elementos obrigatórios da capa: linha de atrito, linha de redução, gate em 2 níveis, screenshot) — cada linha deve ser curta o bastante pra ficar 100% legível de relance. Se o texto 1 vier como frase corrida longa, o trabalho é *quebrar em linhas escaneáveis*, não forçar numa linha só
- **Bloco inteiro da capa (logo + título + pretitle) é centralizado verticalmente no frame de 1350px** (`.capa-content` com `justify-content: center`, não ancorado no topo nem embaixo) — nunca deixar sobrando um bloco grande de espaço vazio abaixo do texto
- `capa-friction`: máx. **60 caracteres** (linha curta entre parênteses, cola direto embaixo do título)
- `split-title` / `td-title` / `tc-title` / `ta-title`: máx. **90 caracteres**, 2-3 linhas

**Acentuação — OBRIGATÓRIO:** todo texto em português deve manter acentuação, cedilha e til corretos (não → nao é erro, decisões → decisoes é erro). Nunca gerar ou aceitar texto sem acentuação.

**Elementos obrigatórios em todo slide:**
- `.top-header`: `Eduardo Rolim` (esq) — `@oeduardo.1` (centro) — `Mês Ano ®` (dir), Space Grotesk 14px uppercase, opacity 0.50 (ou 0.35 em fundo branco)
- `.progress-bar`: barra fixa no rodapé, `.progress-fill` verde `#0E9957` crescendo por slide: `(número do slide ÷ total de slides) × 100%` — ex. num carrossel de 7, o slide 3 mostra 42.8%, não um valor fixo de tabela
- `.slide-arrow`: seta de continuidade no canto inferior direito (exceto capa e CTA final)
- Destaque de palavra-chave sempre com `<span class="hl">`, cor `#0E9957`
- **Exceção obrigatória**: toda vez que a palavra "Claude" aparecer em destaque (título, CTA, gate-reminder, em qualquer slide), usar `<span class="hl-claude">`, cor `#D97757` (laranja de marca do Claude/Anthropic) — nunca o verde do projeto nesse caso específico

---

## 7 elementos obrigatórios da capa — REGRA GERAL, TODA CAPA

Toda capa de carrossel precisa ter os 7 elementos abaixo, **nesta ordem vertical**. Sem eles, a capa não para o scroll. **A capa nunca pode ser 100% texto** — precisa de pelo menos um elemento figurativo (asterisco grande de fundo, print de tela, ou foto recortada).

1. **Cabeçalho fino** (`.top-header`, já padrão em todo slide): `Eduardo Rolim · @oeduardo.1 · Mês Ano ®`
2. **Elemento gráfico grande ao fundo** (`capa-bg-asterisk`): o asterisco/logo da marca ocupando boa parte do canto (~660px), **opacidade alta (~0.9)** — precisa ser bem visível, não um watermark apagado — posicionado no espaço vazio da capa (ex: canto superior direito) sem cobrir o texto. É o elemento figurativo obrigatório quando não há foto/print maior
3. **Título** (`capa-title`): **NÚMERO em dígito** (preferir "5" a "cinco") como primeira palavra em destaque (`hl`, verde) + **NOME DA FERRAMENTA/TEMA** + **RESULTADO CONCRETO**. Número seco é mais forte que "mais de X" — nunca usar "mais de" antes do número se o valor exato já é impactante sozinho
4. **Linha de atrito** (`capa-friction`, entre parênteses, direto embaixo do título, preto, corpo médio — maior que a linha de redução, menor que o título) — cria a tensão que faz a pessoa continuar. Benefício puro, sem atrito, NÃO é linha de atrito. Tipos válidos:
   - **Acesso proibido/secreto**: "que quase ninguém ativou", "que deveriam ser proibidas"
   - **Grátis quando deveria ser pago**
   - **Contra a ferramenta querida**: desafia algo que o público já ama/confia
   - **Substituição de trabalho humano**
   - **Tempo ou desempenho absurdo**
5. **Linha de redução de fricção** (`capa-reduction`, corpo pequeno, cinza, uppercase) — remove a objeção prática antes que ela apareça. Ex: "Sem código · 10 minutos pra configurar", "De graça", "Sem programar"
6. **CTA em 2 níveis** (`capa-gate` + `capa-gate-detail`): a palavra do gate isolada, grande, verde, sempre entre aspas (`Comenta "PALAVRA"`) + uma frase de apoio pequena e peso normal embaixo
7. **Print real de tela, pequeno, canto inferior direito** (`capa-screenshot`) — mockup de UI (não precisa ser screenshot 100% real, mas tem que LER como print de produto: interface flat, sem fotografia cinematográfica)

**Se a capa faz uma promessa numérica quantificável** (ex: "10 horas", "3x mais rápido"), o **slide 2** prova de onde vem esse número — nunca é o primeiro item da lista, é contexto/demonstração. Lista curta tipo recibo (`hours-list`/`hours-row`) com cada parte + total batendo com o número da capa. Sem essa prova, o número vira promessa vazia e o comentário que a capa gera é "prova?" em vez da palavra do gate.

**Gate repetido no meio**: em carrosséis com CTA de comentário (gate word) e 7+ slides, repetir a palavra do gate num slide do meio (por volta do slide 5 ou 6, dentro de um `gate-reminder` — pill verde igual ao `capa-gate`, inserido no conteúdo do slide sem atrapalhar o texto principal). Quem sai do carrossel antes do fim precisa ter visto a palavra pelo menos duas vezes.

**Paleta**: verde `#0E9957` + preto sobre branco. Máximo 3 cores por slide.

---

## Template Lista — carrosséis de item numerado (X skills, X erros, X ferramentas, X passos)

Quando o conteúdo é uma **lista de itens** (não uma narrativa/notícia progressiva), usar este padrão em vez do ciclo `split/tipo-c/tipo-a/tipo-d` da seção "Layouts dos Slides". Sequência:

| # | Tipo | Conteúdo |
|---|---|---|
| 1 | `slide-capa` | os 7 elementos acima |
| 2 | `slide-proof` | contexto curto ou demonstração do número prometido na capa (`hours-list`) — nunca o primeiro item da lista |
| 3 a N-1 | `slide-item` | um item por slide |
| N | `slide-cta` | handle grande + CTA reforçado |

**Regras dos `slide-item` (slide 3 até o penúltimo):**
- Um item por slide, sempre dentro de `item-box` (borda preta 3px, cantos arredondados) — nunca dois itens no mesmo slide
- Cada item tem ícone próprio (`item-icon-wrap`, fundo preto ou verde alternando — nunca mais de 2 cores de fundo de ícone no carrossel inteiro) e título (`item-title`)
- **Zero parágrafo corrido** — só `item-bullets` (frases curtas, uma ideia por linha, nunca período com múltiplas orações encadeadas)
- Indicador de progresso numérico no canto superior direito (`page-count`, formato `0X/0N`, substitui o slot de mês/ano no `.top-header` nos slides de item — a capa mantém mês/ano, os demais mostram página) — capa nunca conta como página, a contagem começa do slide 2
- Handle no rodapé (`footer-handle`, ícone do Instagram + `@oeduardo.1`), **mesma posição em todos os slides de item**
- **Pelo menos 2 `slide-item` com print de tela real** (`item-screenshot`) — mockup flat de UI, `object-fit: cover` com altura fixa (~280px) pra não estourar o box (imagens geradas em 4:5 são muito altas pra caber inteiras)
- O item no **meio da sequência de itens** leva o `gate-reminder` (repetição do CTA — ver regra "Gate repetido no meio")

**Último slide** (`slide-cta`): handle grande (`cta-handle-big`, Playfair Display) + `cta-gate` (a palavra do gate, grande e verde) + `cta-detail` + `cta-reinforce` (pill verde reforçando o mesmo CTA, redundância proposital)

**Quando usar Template Lista vs. padrão narrativo**: conteúdo é uma lista numerada de itens (skills, erros, ferramentas, passos) → Template Lista. Conteúdo é uma narrativa/notícia com desenvolvimento progressivo (ex: "Google reconstruiu o modelo do zero") → padrão fixo de 7 classes em "Layouts dos Slides".

---

## Template HTML Base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Carrossel @oeduardo.1</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,600;0,700;0,800;1,400&family=Space+Grotesk:wght@400;500&family=Playfair+Display:wght@400&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { background: #000; }

    .top-header {
      position: absolute; top: 0; left: 0; right: 0;
      display: flex; justify-content: space-between; align-items: center;
      padding: 26px 48px; z-index: 20;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 14px; font-weight: 400;
      color: rgba(255,255,255,0.50);
      letter-spacing: 1px; text-transform: uppercase;
    }
    .progress-bar {
      position: absolute; bottom: 0; left: 0; right: 0;
      height: 7px; background: rgba(255,255,255,0.12); z-index: 30;
    }
    .progress-fill { height: 100%; background: #0E9957; border-radius: 0 3px 3px 0; }
    .slide-arrow {
      position: absolute; right: 32px; bottom: 24px;
      z-index: 25; opacity: 0.55;
    }

    /* CABEÇALHO/RODAPÉ auxiliares — Template Lista */
    .page-count {
      font-family: 'Space Grotesk', sans-serif;
      font-size: 14px; font-weight: 500;
      color: rgba(0,0,0,0.40); letter-spacing: 1px;
    }
    .footer-handle {
      position: absolute; bottom: 32px; left: 48px; z-index: 20;
      display: flex; align-items: center; gap: 8px;
      font-family: 'Inter', sans-serif; font-size: 16px; font-weight: 600;
      color: #0d0d0d;
    }
    .footer-handle svg { width: 20px; height: 20px; fill: #0d0d0d; }

    /* CAPA — 7 elementos obrigatórios, fundo branco (padrão desde ago/2026) */
    .slide-capa {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; page-break-after: always;
    }
    .slide-capa .top-header { color: rgba(0,0,0,0.40); }
    .capa-bg-asterisk {
      position: absolute; top: -50px; right: -70px;
      width: 660px; height: 660px; object-fit: contain;
      opacity: 0.9; z-index: 5;
    }
    .capa-content {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      padding: 0 64px;
      display: flex; flex-direction: column; justify-content: center; align-items: flex-start; text-align: left;
      z-index: 10;
    }
    .capa-logo-small {
      width: 130px; height: 130px; object-fit: contain;
      margin-bottom: 34px;
    }
    .capa-title {
      font-family: Impact, 'Arial Narrow', sans-serif;
      font-size: 96px; font-weight: 400;
      line-height: 1.0; text-transform: uppercase;
      color: #0d0d0d;
    }
    .capa-title .hl { color: #0E9957; }
    .hl-claude { color: #D97757; }
    .capa-friction {
      font-family: 'Inter', sans-serif;
      font-size: 32px; font-weight: 800; line-height: 1.35;
      color: #0d0d0d; max-width: 780px;
      margin-top: 22px;
    }
    .capa-reduction {
      font-family: 'Inter', sans-serif;
      font-size: 20px; font-weight: 600; line-height: 1.4;
      color: rgba(0,0,0,0.48); text-transform: uppercase; letter-spacing: 0.6px;
      margin-top: 14px;
    }
    .capa-gate {
      font-family: 'Inter', sans-serif;
      font-size: 44px; font-weight: 800; color: #0E9957;
      margin-top: 32px; line-height: 1.1;
    }
    .capa-gate-detail {
      font-family: 'Inter', sans-serif;
      font-size: 22px; font-weight: 400; color: #0d0d0d;
      margin-top: 8px;
    }
    .capa-screenshot {
      position: absolute; bottom: 46px; right: 46px;
      width: 190px; border-radius: 14px; overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.18);
      border: 1px solid rgba(0,0,0,0.08);
      z-index: 10;
    }
    .capa-screenshot img { width: 100%; display: block; }
    .gate-reminder {
      display: inline-flex; align-items: center; align-self: flex-start;
      font-family: 'Inter', sans-serif;
      font-size: 17px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1px;
      color: #ffffff; background: #0E9957;
      padding: 14px 24px; border-radius: 100px; margin-top: 4px;
    }

    /* SLIDE 2 — PROVA (demonstração do número prometido na capa) */
    .slide-proof {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .proof-body {
      flex: 1; padding: 130px 64px 100px;
      display: flex; flex-direction: column; justify-content: center; gap: 28px;
    }
    .proof-divider { width: 56px; height: 4px; background: #0E9957; border-radius: 2px; }
    .proof-title {
      font-family: 'Inter', sans-serif;
      font-size: 44px; font-weight: 800; line-height: 1.15; color: #0d0d0d;
    }
    .proof-title .hl { color: #0E9957; }
    .hours-list { display: flex; flex-direction: column; margin-top: 10px; }
    .hours-row {
      display: flex; justify-content: space-between; align-items: center;
      padding: 16px 0; border-bottom: 1px solid rgba(0,0,0,0.10);
      font-family: 'Inter', sans-serif; font-size: 25px; font-weight: 600;
      color: #0d0d0d;
    }
    .hours-row .hours-value { color: #0E9957; font-weight: 800; }
    .hours-row.total {
      border-bottom: none; border-top: 2px solid #0d0d0d;
      margin-top: 6px; padding-top: 22px;
      font-size: 30px; font-weight: 800;
    }
    .hours-row.total .hours-value { font-size: 32px; }

    /* SLIDES 3 A N-1 — ITEM (Template Lista: um item por slide) */
    .slide-item {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .item-body {
      flex: 1; padding: 130px 56px 100px;
      display: flex; flex-direction: column; justify-content: center;
    }
    .item-box {
      border: 3px solid #0d0d0d; border-radius: 20px;
      padding: 44px 40px; display: flex; flex-direction: column; gap: 24px;
    }
    .item-icon-wrap {
      width: 64px; height: 64px; border-radius: 14px;
      background: #0d0d0d;
      display: flex; align-items: center; justify-content: center;
    }
    .item-icon-wrap.accent-bg { background: #0E9957; }
    .item-icon-wrap svg { width: 32px; height: 32px; }
    .item-tag {
      font-family: 'Space Grotesk', sans-serif; font-size: 15px; font-weight: 500;
      color: rgba(0,0,0,0.45); text-transform: uppercase; letter-spacing: 1.5px;
    }
    .item-title {
      font-family: 'Inter', sans-serif; font-size: 40px; font-weight: 800;
      color: #0d0d0d; line-height: 1.15;
    }
    .item-title .hl { color: #0E9957; }
    .item-bullets { display: flex; flex-direction: column; gap: 14px; }
    .item-bullet {
      font-family: 'Inter', sans-serif; font-size: 24px; font-weight: 600;
      color: #0d0d0d; display: flex; gap: 10px; align-items: flex-start;
    }
    .item-bullet .dot { color: #0E9957; flex-shrink: 0; }
    .item-bullet .hl { color: #0E9957; font-weight: 800; }
    .item-screenshot {
      margin-top: 6px; border-radius: 12px; overflow: hidden;
      border: 1px solid rgba(0,0,0,0.08);
    }
    /* imagens geradas em 4:5 são muito altas pra caber no box inteiras — trava altura fixa */
    .item-screenshot img { width: 100%; height: 280px; object-fit: cover; object-position: center 40%; display: block; }

    /* SPLIT */
    .slide-split {
      width: 1080px; height: 1350px;
      display: flex; flex-direction: row;
      position: relative; overflow: hidden;
      page-break-after: always;
    }
    .split-left {
      width: 50%; height: 100%; background: #0d0d0d;
      display: flex; flex-direction: column; justify-content: center;
      padding: 60px 44px; gap: 20px; z-index: 2;
    }
    .split-tag {
      display: inline-block; background: #0E9957; color: #ffffff;
      font-family: 'Inter', sans-serif;
      font-size: 20px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1px;
      padding: 8px 18px; border-radius: 4px; align-self: flex-start;
    }
    .split-title {
      font-family: 'Inter', sans-serif;
      font-size: 54px; font-weight: 800;
      text-transform: uppercase; line-height: 1.0; color: #ffffff;
    }
    .split-title .hl { color: #0E9957; }
    .split-divider { width: 48px; height: 3px; background: #0E9957; border: none; margin: 4px 0; }
    .split-item {
      font-family: 'Inter', sans-serif;
      font-size: 28px; font-weight: 300;
      line-height: 1.45; color: rgba(255,255,255,0.88);
      display: flex; gap: 12px;
    }
    .split-bullet { color: #0E9957; font-weight: 700; flex-shrink: 0; }
    .split-right { width: 50%; height: 100%; position: relative; }
    .split-right img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.85); }

    /* MINI CTA */
    .slide-mini-cta {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .mini-cta-body {
      flex: 1; display: flex; flex-direction: column;
      justify-content: center; padding: 60px 64px; gap: 32px;
    }
    .mini-cta-accent { width: 56px; height: 5px; background: #0E9957; border-radius: 2px; }
    .mini-cta-title {
      font-family: 'Inter', sans-serif;
      font-size: 62px; font-weight: 800; line-height: 1.1; color: #0d0d0d;
    }
    .mini-cta-title .hl { color: #0E9957; }

    /* TIPO C */
    .slide-tipo-c {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .slide-tipo-c .top-header { color: rgba(0,0,0,0.35); }
    .tc-body {
      flex: 1; padding: 56px 64px 80px;
      display: flex; flex-direction: column; justify-content: center; gap: 28px;
    }
    .tc-divider { width: 56px; height: 4px; background: #0E9957; border-radius: 2px; }
    .tc-title {
      font-family: 'Inter', sans-serif;
      font-size: 52px; font-weight: 800; line-height: 1.12; color: #0d0d0d;
    }
    .tc-title .hl { color: #0E9957; }
    .tc-text {
      font-family: 'Inter', sans-serif;
      font-size: 34px; font-weight: 300; line-height: 1.55;
      color: rgba(0,0,0,0.72);
    }
    .tc-text .hl { color: #0E9957; font-weight: 600; }
    .tc-text strong { font-weight: 700; color: #0d0d0d; }
    .tc-formula {
      font-family: 'Inter', sans-serif;
      font-size: 30px; font-weight: 700; line-height: 1.5;
      color: #0d0d0d;
      background: #f5f5f5; border-left: 5px solid #0E9957;
      padding: 20px 24px; border-radius: 0 8px 8px 0;
    }
    .tc-divider-line { border: none; border-top: 1px solid rgba(0,0,0,0.1); margin: 0; }
    .slide-tipo-c .progress-bar { background: rgba(0,0,0,0.08); }

    /* TIPO A */
    .slide-tipo-a {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #0d0d0d; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .ta-img { width: 100%; height: 580px; overflow: hidden; flex-shrink: 0; }
    .ta-img img { width: 100%; height: 100%; object-fit: cover; filter: brightness(0.95); }
    .ta-body {
      flex: 1; padding: 40px 56px 90px;
      display: flex; flex-direction: column; justify-content: flex-start; gap: 22px;
    }
    .ta-divider { width: 60px; height: 3px; background: #0E9957; border-radius: 2px; }
    .slide-divider { border: none; border-top: 1px solid rgba(255,255,255,0.18); margin: 0; }
    .ta-title {
      font-family: 'Inter', sans-serif;
      font-size: 46px; font-weight: 800; line-height: 1.12; color: #ffffff;
    }
    .ta-title .hl { color: #0E9957; }
    .ta-text {
      font-family: 'Inter', sans-serif;
      font-size: 27px; font-weight: 300; line-height: 1.58;
      color: rgba(255,255,255,0.78);
    }
    .ta-text .hl { color: #0E9957; font-weight: 600; }
    .ta-text strong { font-weight: 700; color: #ffffff; }

    /* TIPO D */
    .slide-tipo-d {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #000; page-break-after: always;
    }
    .td-img {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover; filter: brightness(0.58); z-index: 0;
    }
    .td-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(180deg, rgba(0,0,0,0.00) 0%, rgba(0,0,0,0.05) 30%, rgba(0,0,0,0.55) 58%, rgba(0,0,0,0.80) 100%);
      z-index: 1;
    }
    .td-content {
      position: absolute; top: 0; left: 0; right: 0; bottom: 0;
      display: flex; flex-direction: column; justify-content: center;
      padding: 100px 64px 80px; gap: 24px; z-index: 10;
    }
    .td-divider { width: 56px; height: 4px; background: #0E9957; border-radius: 2px; }
    .td-title {
      font-family: 'Inter', sans-serif;
      font-size: 56px; font-weight: 700; line-height: 1.1; color: #ffffff;
      text-shadow: 1px 1px 6px rgba(0,0,0,0.8);
    }
    .td-title .hl { color: #0E9957; }
    .td-text {
      font-family: 'Inter', sans-serif;
      font-size: 33px; font-weight: 300; line-height: 1.55;
      color: rgba(255,255,255,0.82);
      text-shadow: 1px 1px 4px rgba(0,0,0,0.7);
    }
    .td-text .hl { color: #0E9957; font-weight: 600; }
    .td-text strong { font-weight: 700; color: #ffffff; }

    /* CTA */
    .slide-cta {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #ffffff; display: flex; flex-direction: column;
      page-break-after: always;
    }
    .cta-header {
      display: flex; justify-content: space-between; align-items: center;
      padding: 26px 48px;
      font-family: 'Space Grotesk', sans-serif;
      font-size: 14px; font-weight: 400;
      color: rgba(0,0,0,0.35); letter-spacing: 1px; text-transform: uppercase;
    }
    .cta-body {
      flex: 1; display: flex; align-items: center; justify-content: center;
      padding: 0 64px;
    }
    .cta-inner { display: flex; flex-direction: column; gap: 28px; align-items: flex-start; }
    .cta-name {
      font-family: 'Playfair Display', serif;
      font-size: 72px; font-weight: 400; color: #0f0f0f; line-height: 1;
    }
    .cta-gate {
      font-family: 'Inter', sans-serif;
      font-size: 56px; font-weight: 800; line-height: 1.1; color: #0E9957;
    }
    .cta-detail {
      font-family: 'Inter', sans-serif;
      font-size: 26px; font-weight: 400; line-height: 1.5; color: #0d0d0d;
      margin-top: 14px; max-width: 700px;
    }
    .cta-source {
      font-family: 'Inter', sans-serif;
      font-size: 20px; font-weight: 300; line-height: 1.6;
      color: rgba(0,0,0,0.50); margin-top: 24px;
    }

    /* CTA final — Template Lista (handle grande + gate + reforço) */
    .cta-handle-big {
      font-family: 'Playfair Display', serif;
      font-size: 76px; font-weight: 400; color: #0d0d0d; line-height: 1;
    }
    .cta-reinforce {
      display: inline-flex; align-items: center; align-self: flex-start;
      font-family: 'Inter', sans-serif; font-size: 20px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1.5px;
      color: #ffffff; background: #0E9957;
      padding: 20px 44px; border-radius: 100px; margin-top: 34px;
    }
  </style>
</head>
<body>

<!-- SLIDE 1 — CAPA (7 elementos obrigatórios, nesta ordem) -->
<div class="slide-capa">
  <img class="capa-bg-asterisk" src="img/logo_N.png" alt="">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="capa-content">
    <img class="capa-logo-small" src="img/logo_N.png" alt="[logo do tema/ferramenta, se houver — omitir a tag inteira se não houver logo relevante e usar só o capa-bg-asterisk como elemento figurativo]">
    <h1 class="capa-title">[NÚMERO em dígito, ex: <span class="hl">5</span>, primeira palavra + NOME DA FERRAMENTA/TEMA (usar <span class="hl-claude">hl-claude</span> se for "Claude" especificamente) + RESULTADO CONCRETO — quebrar em frases curtas com &lt;br&gt;, uma por linha]</h1>
    <p class="capa-friction">[linha de atrito entre parênteses — ver "7 elementos obrigatórios da capa"]</p>
    <p class="capa-reduction">[linha de redução de fricção — ex: "Sem código · 10 minutos"]</p>
    <p class="capa-gate">[CTA nível 1 — a palavra do gate, ex: Comenta "PALAVRA"]</p>
    <p class="capa-gate-detail">[CTA nível 2 — frase de apoio pequena]</p>
  </div>
  <div class="capa-screenshot"><img src="img/screenshot_N.jpg" alt="[print/mockup de UI, pequeno, canto inferior direito]"></div>
  <div class="progress-bar"><div class="progress-fill" style="width:11.1%"></div></div>
</div>

<!-- SLIDE 2 — SPLIT (textos 3+4) -->
<div class="slide-split">
  <div class="split-left">
    <span class="split-tag">[tag curta]</span>
    <p class="split-title">[texto 3 — título do split com <span class="hl">destaque</span>]</p>
    <hr class="split-divider">
    <div class="split-item"><span class="split-bullet">•</span><span>[texto 4, bullet 1 — pode usar <strong>negrito</strong>]</span></div>
    <div class="split-item"><span class="split-bullet">•</span><span>[bullet 2 — pode usar <span class="hl">destaque</span>]</span></div>
    <div class="split-item"><span class="split-bullet">•</span><span>[bullet 3]</span></div>
  </div>
  <div class="split-right">
    <img src="img/slide_N.jpg" alt="">
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar"><div class="progress-fill" style="width:22.2%"></div></div>
</div>

<!-- SLIDE 3 — MINI CTA (fixo) -->
<div class="slide-mini-cta">
  <div class="top-header" style="color:rgba(0,0,0,0.35);">
    <span style="color:rgba(0,0,0,0.35);">Eduardo Rolim</span><span style="color:rgba(0,0,0,0.35);">@oeduardo.1</span><span style="color:rgba(0,0,0,0.35);">Mês Ano ®</span>
  </div>
  <div class="mini-cta-body">
    <div class="mini-cta-accent"></div>
    <p class="mini-cta-title">Antes de continuar: Quer mais conteúdos como esse? Toca <span class="hl">2 vezes</span> na tela e depois me segue.</p>
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0E9957" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar" style="background:rgba(0,0,0,0.08);"><div class="progress-fill" style="width:33.3%"></div></div>
</div>

<!-- SLIDE 4 — TIPO C (textos 5+6) -->
<div class="slide-tipo-c">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="tc-body">
    <div class="tc-divider"></div>
    <p class="tc-title">[texto 5 — título tipo-c com <span class="hl">destaques</span>]</p>
    <hr class="tc-divider-line">
    <p class="tc-text">[texto 6 — texto de apoio]</p>
    <div class="tc-formula">[opcional — tc-formula: dado/fórmula em destaque, remover a div se não houver]</div>
    <p class="tc-text">[texto 7 — fechamento, pode usar <strong>negrito</strong>]</p>
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#0E9957" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar" style="background:rgba(0,0,0,0.08);"><div class="progress-fill" style="width:44.4%"></div></div>
</div>

<!-- SLIDE 5 — TIPO A (texto 7) -->
<div class="slide-tipo-a">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="ta-img"><img src="img/slide_N.jpg" alt=""></div>
  <div class="ta-body">
    <div class="ta-divider"></div>
    <p class="ta-title">[texto 8 — título tipo-a com <span class="hl">destaque</span>]</p>
    <hr class="slide-divider">
    <p class="ta-text">[texto 9 — texto de apoio, pode usar <strong>negrito</strong>]</p>
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar"><div class="progress-fill" style="width:55.6%"></div></div>
</div>

<!-- SLIDE 6 — TIPO D (texto 8) -->
<div class="slide-tipo-d">
  <img class="td-img" src="img/slide_N.jpg" alt="">
  <div class="td-overlay"></div>
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="td-content">
    <div class="td-divider"></div>
    <p class="td-title">[texto 10 — título tipo-d com <span class="hl">destaque</span>]</p>
    <hr style="border:none;border-top:1px solid rgba(255,255,255,0.18);margin:0;">
    <p class="td-text">[texto 11 — texto de apoio]</p>
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar"><div class="progress-fill" style="width:66.7%"></div></div>
</div>

<!-- SLIDE 7 — TIPO B / SPLIT (texto 9) -->
<div class="slide-split">
  <div class="split-left">
    <span class="split-tag">Solução</span>
    <p class="split-title">[texto 12 — título do 2º split com <span class="hl">destaque</span>]</p>
    <hr class="split-divider">
    <div class="split-item"><span class="split-bullet">•</span><span>[texto 13, bullet 1]</span></div>
    <div class="split-item"><span class="split-bullet">•</span><span>[bullet 2]</span></div>
    <div class="split-item"><span class="split-bullet">•</span><span>[texto 14, bullet 3]</span></div>
  </div>
  <div class="split-right">
    <img src="img/slide_N.jpg" alt="">
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar"><div class="progress-fill" style="width:77.8%"></div></div>
</div>

<!-- SLIDE 8 — TIPO D (texto 10) -->
<div class="slide-tipo-d">
  <img class="td-img" src="img/slide_N.jpg" alt="">
  <div class="td-overlay"></div>
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="td-content">
    <div class="td-divider"></div>
    <p class="td-title">[texto 15 — título do 2º tipo-d]</p>
    <hr style="border:none;border-top:1px solid rgba(255,255,255,0.18);margin:0;">
    <p class="td-text">[texto 16, parte 1]</p>
    <hr style="border:none;border-top:1px solid rgba(255,255,255,0.18);margin:0;">
    <p class="td-text">[texto 16, parte 2 — frase-martelo]</p>
  </div>
  <div class="slide-arrow"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  <div class="progress-bar"><div class="progress-fill" style="width:88.9%"></div></div>
</div>

<!-- SLIDE 9 — CTA (texto 11) -->
<div class="slide-cta">
  <div class="cta-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="cta-body">
    <div class="cta-inner">
      <span class="cta-name">Eduardo Rolim</span>
      <p class="cta-gate">[palavra do gate em destaque — ex: Comenta "PALAVRA"]</p>
      <p class="cta-detail">[complemento do CTA — o que a pessoa recebe/o que acontece depois]</p>
      <p class="cta-source">[texto 18 — fonte/gancho de fechamento, opcional]</p>
    </div>
  </div>
  <div class="progress-bar" style="background:rgba(0,0,0,0.08);"><div class="progress-fill" style="width:100%"></div></div>
</div>

<!-- ===== TEMPLATE LISTA — exemplos alternativos (carrosséis de item numerado) ===== -->

<!-- SLIDE 2 do Template Lista — PROVA (demonstração do número da capa, nunca o 1º item) -->
<div class="slide-proof">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span class="page-count">01/0N</span>
  </div>
  <div class="proof-body">
    <div class="proof-divider"></div>
    <p class="proof-title">De onde vêm as <span class="hl">[número da capa]</span></p>
    <div class="hours-list">
      <div class="hours-row"><span>[item 1]</span><span class="hours-value">[Xh]</span></div>
      <div class="hours-row"><span>[item 2]</span><span class="hours-value">[Xh]</span></div>
      <div class="hours-row total"><span>TOTAL</span><span class="hours-value">[bate com o número da capa]</span></div>
    </div>
  </div>
  <div class="footer-handle"><span>@oeduardo.1</span></div>
</div>

<!-- SLIDE 3 a N-1 do Template Lista — ITEM (um por slide, dentro de item-box) -->
<div class="slide-item">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span class="page-count">0X/0N</span>
  </div>
  <div class="item-body">
    <div class="item-box">
      <div class="item-icon-wrap accent-bg"><svg><!-- ícone do item, 24x24 --></svg></div>
      <span class="item-tag">[Skill/Item N]</span>
      <p class="item-title">[título curto com <span class="hl">palavra-chave</span>]</p>
      <div class="item-bullets">
        <div class="item-bullet"><span class="dot">•</span><span>[frase curta, zero parágrafo corrido]</span></div>
        <div class="item-bullet"><span class="dot">•</span><span>[frase curta]</span></div>
      </div>
      <div class="item-screenshot"><img src="img/screenshot_N.jpg" alt="[só em pelo menos 2 slides de item]"></div>
      <!-- <div class="gate-reminder">[só no item do meio da sequência]</div> -->
    </div>
  </div>
  <div class="footer-handle"><span>@oeduardo.1</span></div>
</div>

<!-- SLIDE N do Template Lista — CTA final (handle grande + gate + reforço) -->
<div class="slide-cta">
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span class="page-count">0N/0N</span>
  </div>
  <div class="cta-body">
    <span class="cta-handle-big">@oeduardo.1</span>
    <p class="cta-gate">[palavra do gate — ex: Comenta "PALAVRA"]</p>
    <p class="cta-detail">[o que a pessoa recebe]</p>
    <div class="cta-reinforce">[mesmo CTA repetido em pill — redundância proposital]</div>
  </div>
</div>

</body>
</html>
```

---

## Regras de Design do Conteúdo

O conteúdo de cada slide já vem pronto do Eduardo. Sua função é apenas aplicar o estilo visual correto:

- **PROIBIDO usar travessão (—) dentro do texto gerado pros slides** (títulos, textos, bullets, CTA, pretitle). Travessão soa robótico/gerado por IA e mata a humanização do texto. Trocar por ponto final, vírgula, dois-pontos, ou reformular a frase em duas orações curtas. Isso vale pra texto criado/parafraseado por quem monta o carrossel — não se aplica a travessão que já vier literal dentro do texto original enviado pelo Eduardo
- **Ordem de impacto — OBRIGATÓRIO em qualquer slide com 2+ blocos de texto**: o texto de maior impacto vem sempre ACIMA do texto de menor impacto/complementar no HTML (topo visual). Na capa: `capa-title` (grande, Impact) sempre ANTES de `capa-friction` (linha de atrito, menor) — nunca a linha de atrito acima do título. No CTA final: `cta-gate` (a palavra do gate, grande e verde) sempre antes de `cta-detail`/`cta-source` (menores)
- Título da capa (`capa-title`): CSS já força `text-transform: uppercase` — digitar o texto em caixa normal, o navegador renderiza maiúsculo automaticamente. Impact (mesma fonte de sempre), alinhado à esquerda, quebrado em linhas curtas com `<br>`, com `<span class="hl">` em 2-3 palavras-chave espalhadas pelas linhas (verde `#0E9957`, cor de marca — nunca usar a cor de outra marca/produto mesmo se o tema for sobre ela)
- Logo no topo da capa (`capa-logo-small`, 130px): incluir só quando o carrossel tem ligação direta com uma marca/produto específico (ex: carrossel sobre Claude usa o logo do Claude). Sem logo relevante, omitir a tag — não forçar um logo genérico
- `split-title` também é uppercase por CSS (mesma lógica: digitar normal, renderiza maiúsculo)
- 1-2 palavras em verde `#0E9957` por slide para destaque — identificar as palavras-chave do texto enviado
- `tc-title`/`ta-title`/`td-title`/`cta-gate`/`cta-detail`/`cta-name`: capitalize natural, Inter, SEM uppercase — não forçar caixa alta nesses
- Cada slide com foto deve ter uma **foto diferente**
- `slide-tipo-d` (fundo foto full-bleed) é o slide de maior impacto — reservar para a frase-martelo mais forte do bloco
- Nunca usar o template genérico antigo (`.slide`/`.slide-editorial`) — sempre as 7 classes fixas da seção "Layouts dos Slides"

---

## Fluxo de Trabalho

### Passo 1: Receber o Conteúdo

Eduardo envia **N textos numerados** (texto 1 a texto N — N é variável, não precisa ser 18). Esses textos são **condensados em slides**, NUNCA um slide por texto — o número final de slides se adapta à quantidade de texto recebida.

**REGRA: número de slides é ADAPTÁVEL. 9 slides (18 textos) é o teto/exemplo completo, não uma obrigação — carrosséis menores (6, 7, 8 slides) são igualmente válidos.**

#### Algoritmo de distribuição (qualquer quantidade de texto):

1. **Slide 1 = sempre CAPA** (`slide-capa`): texto 1 → `capa-title` (número + ferramenta/tema + resultado concreto); texto 2 → `capa-friction` (linha de atrito, ver "7 elementos obrigatórios da capa"); `capa-reduction`, `capa-gate`/`capa-gate-detail` e `capa-screenshot` sempre presentes
2. **Último slide = sempre CTA** (`slide-cta`): penúltimo texto → `cta-gate` (a palavra do gate, isolada e em destaque) + `cta-detail` (complemento); último texto → `cta-source`
3. **MINI-CTA** (`slide-mini-cta`, fixo, não consome texto do usuário): incluir **somente se o total de slides for 8 ou mais**. Carrosséis de 7 slides ou menos pulam esse slide — vai direto de capa pro primeiro slide de conteúdo.
4. **Slides do meio**: todo texto que sobrar entre a capa e o CTA (descontando os 2 já usados em cada) é distribuído nos slides de conteúdo, ciclando pelos 4 tipos "variados" **nesta ordem fixa, repetindo do início se precisar de mais**: `slide-split → slide-tipo-c → slide-tipo-a → slide-tipo-d`
5. Cada slide do meio recebe **1 a 3 textos**: o mais curto e impactante vira `*-title`, o(s) resto vira(m) `*-text` (ou `split-item`s no caso do split). Distribuir o texto restante o mais equilibrado possível entre os slides do meio definidos — não empilhar tudo num slide só e deixar outro vazio.

**Exemplo com 7 slides (menos texto, ex. 10-12 textos):**
`slide-capa → slide-split → slide-tipo-c → slide-tipo-a → slide-tipo-d → slide-split → slide-cta`
(sem mini-cta, porque total < 8)

**Exemplo com 9 slides (18 textos, máximo):**
`slide-capa → slide-split → slide-mini-cta → slide-tipo-c → slide-tipo-a → slide-tipo-d → slide-split → slide-tipo-d → slide-cta`

**Regras de combinação de textos dentro do slide:**
- `*-title`: o texto mais curto e impactante do grupo — serve como gancho
- `*-text`: os demais textos do grupo combinados — desenvolvem o argumento
- `split-item`: cada bullet é uma frase curta com `<span class="split-bullet">•</span>` na frente
- **Mini-cta (quando presente)**: SEMPRE o CTA fixo obrigatório (`Quer mais conteúdos como esse? Toca 2 vezes na tela e depois me segue.`), nunca um texto numerado do usuário
- **CTA final**: `cta-name` é sempre "Eduardo Rolim"; `cta-gate` carrega a palavra do gate isolada (ex: `Comenta "PALAVRA"`), verde, grande; `cta-detail` complementa em corpo normal; `cta-source` é opcional (ordem de impacto: ver "Regras de Design do Conteúdo")

**Imagens: uma por slide gerado** (slide_01.jpg a slide_0N.jpg, N = total real de slides).

### Passo 2: Gerar Imagens via Gemini API (gemini-2.5-flash-image)

Usar o modelo `gemini-2.5-flash-image` do Google para gerar uma imagem por slide (capa, internos e CTA).

**REGRA ABSOLUTA DE CUSTO: modelo é SEMPRE `gemini-2.5-flash-image`. NUNCA usar variantes `-pro` (mais caras) nem depender de tiers `-preview` sem quota garantida.**
- `flash` é o tier de equilíbrio custo/qualidade da família Gemini — nem o mais avançado (`pro`), nem o mais fraco
- Se algum script, exemplo ou template antigo mostrar `gpt-image-1` / OpenAI, é erro — corrigir para `gemini-2.5-flash-image`
- Requer billing habilitado no projeto do Google AI Studio/Cloud — tier free tem quota 0 pra geração de imagem

**Endpoint:**
```
POST https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent
Header: x-goog-api-key: [GEMINI_API_KEY]
```

**Exemplo de chamada:**
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{
        "text": "Extreme close-up portrait of a 40-year-old man, jaw clenched, eyes wide with sudden realization, harsh single side light casting half his face in shadow, cinematic, photorealistic, 35mm film grain, high contrast, portrait orientation, no text, no words"
      }]
    }],
    "generationConfig": {
      "responseModalities": ["IMAGE"],
      "imageConfig": {"aspectRatio": "4:5"}
    }
  }'
```

**A resposta retorna a imagem em base64** dentro de `candidates[0].content.parts[0].inlineData.data`. Salvar como `.jpg` e referenciar no HTML.

**Diretrizes de prompt para imagens — MÁXIMO IMPACTO VIRAL:**

O prompt de cada imagem deve ser construído especificamente para o conteúdo do slide, não de forma genérica. O objetivo é gerar imagens que **PARAM o scroll** — cada uma deve ter tensão visual, emoção extrema ou enquadramento incomum que force o olhar a parar.

**Framework obrigatório — 4 camadas por prompt:**

1. **SUJEITO ESPECÍFICO**: nunca "person" genérico — descrever idade, estado emocional, expressão exata
   - Ruim: `"focused professional"`
   - Bom: `"45-year-old man, jaw tight, eyes narrowed in disbelief, hand pressed flat on desk"`

2. **MOMENTO DE CLÍMAX**: capturar um instante decisivo, não uma pose estática
   - Usar: `"mid-gesture"`, `"split second before"`, `"caught off guard"`, `"realization hitting"`, `"mid-confrontation"`

3. **AMBIENTE NARRATIVO**: o cenário reforça a tensão da história do slide
   - Ruim: `"office"`
   - Bom: `"empty corporate floor, hundreds of abandoned desks stretching to darkness, one lone computer still on"`

4. **TÉCNICA FOTOGRÁFICA QUE AMPLIA O IMPACTO**:
   - Rosto + emoção intensa → `extreme close-up, 85mm portrait lens`
   - Escala/solidão/poder → `low-angle wide shot, environmental portrait`
   - Tensão/confronto → `Dutch angle, shallow depth of field`
   - Revelação/impacto → `silhouette contre-jour, dramatic backlight`
   - Conexão direta → `direct eye contact, slight lean into camera`

**Templates por tipo de slide:**

- **Capa (slide 1)** — deve parar o scroll imediatamente E ter ligação direta com o tema/título/headline. Retrato de rosto NÃO é obrigatório — escolher o sujeito da imagem baseado no que o título 1 realmente fala:
  - **Título centrado em comportamento/decisão/emoção humana** → retrato dramático continua válido: rosto dominando 70%+ do frame, expressão extrema, chiaroscuro.
    Ex: `"Extreme close-up portrait of a 40-year-old woman, one side of face in complete shadow, single harsh side light catching her eye and jaw, expression of quiet fury mixed with certainty, 35mm film grain, cinematic, photorealistic, no text, no words"`
  - **Título centrado em produto/tecnologia/empresa/dado/evento** → a imagem representa **literalmente o assunto do título**, não um rosto genérico. Ex: título fala de um modelo de IA reconstruído do zero → servidor/infraestrutura sendo desmontada, não uma pessoa aleatória.
    Ex: `"Close-up of a massive server rack being stripped down to bare components by robotic arms, sparks and cold blue light, moment of demolition and rebuild, cinematic, photorealistic, no text, no words"`
  - Em qualquer um dos dois casos: manter iluminação dramática, alto contraste, `no text, no words`, `portrait orientation, 4:5 aspect ratio` — a única coisa que muda é o sujeito, não o padrão técnico/fotográfico
  - **Nunca** usar imagem genérica/decorativa desconectada do título (ex: capa sobre "Google reconstruiu modelo" com foto de pessoa sorrindo aleatória) — o teste é: "alguém que só visse a foto entenderia do que o post fala?"

- **Slides de dado chocante / revelação**:
  Contraste de escala ou perspectiva que choca.
  Ex: `"Low angle shot of a single person standing in the center of a massive empty office floor, hundreds of vacant chairs and dark screens extending to the horizon, one overhead fluorescent light cutting through, cinematic noir, photorealistic, no text"`

- **Slides de tensão / conflito / problema**:
  Linguagem corporal de pressão, gestos de confronto, detalhe que implica história.
  Ex: `"Over-the-shoulder shot of hands hovering over a keyboard, out-of-focus screen casting cold blue light on knuckles, tense stillness before a decision, macro lens, cinematic, no text"`

- **Slides de solução / virada / empoderamento**:
  Perspectiva de controle, luz quente surgindo de frente, postura aberta.
  Ex: `"Person standing at floor-to-ceiling window at night overlooking lit city skyline, back slightly turned, arms open at sides, glass reflecting their silhouette, warm amber interior light, photorealistic, cinematic, no text"`

- **Slides de dado numérico / estatística impactante**:
  Imagem abstrata ou metáfora visual que representa escala/impacto.
  Ex: `"Bird's eye view of a single red umbrella in a sea of black umbrellas on a rainy street, aerial drone perspective, sharp contrast, photorealistic, no text"`

- **CTA (slide final)** — olho no olho, convite direto:
  Contato visual direto com a câmera, expressão de cumplicidade intensa.
  Ex: `"Direct eye contact portrait, person smiling with quiet intensity, leaning slightly forward toward camera, warm light from the side, bokeh background, photorealistic, cinematic, no text"`

**Regras absolutas:**
- Sempre em inglês
- NUNCA usar descrições genéricas como `"professional person working"`, `"diverse team smiling"`, `"business meeting"`
- SEMPRE incluir a emoção central do slide no prompt
- SEMPRE especificar técnica fotográfica (ângulo, distância focal)
- Sem texto na imagem: sempre incluir `no text, no words, no letters` no prompt
- Orientação: `portrait orientation, 4:5 aspect ratio`
- Base de estilo: `cinematic, photorealistic, high contrast, moody lighting`

**Fallback**: se a chamada à Gemini API falhar (erro de quota, billing, timeout, etc.), interromper e avisar Eduardo — não usar Unsplash.

### Passo 3: Gerar o HTML Completo

Criar o arquivo `carrossel.html` seguindo o template base desta skill. Substituir todos os `URL_IMAGEM_AQUI` pelas imagens geradas (salvas localmente ou base64 inline).

**Ordem de montagem:**
1. Ler todos os slides enviados pelo Eduardo
2. Atribuir a variante visual correta a cada slide (capa, editorial A/B/C, impacto D, CTA)
3. Identificar as 1-2 palavras-chave por slide para aplicar `.highlight` em verde
4. Montar o HTML completo com os textos exatos enviados

### Passo 4: Capturar Screenshots com Playwright MCP

**IMPORTANTE — Compensar DPR (Device Pixel Ratio):**
O ambiente tem DPR 0.75, viewport CSS de 1440x1800. Solução:

```javascript
async (page) => {
  await page.goto('http://localhost:PORT/output/NOME/carrossel.html');
  await page.waitForTimeout(3000);

  const dpr = await page.evaluate(() => window.devicePixelRatio);
  const cssW = await page.evaluate(() => window.innerWidth);
  const cssH = await page.evaluate(() => window.innerHeight);
  const scale = cssW / 1080;

  const slides = await page.locator('body > div').all();
  const total = slides.length;

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = 'none');

  for (let i = 0; i < total; i++) {
    const num = String(i + 1).padStart(2, '0');
    const path = `/caminho/output/NOME/slide_${num}.png`;

    const classes = await slides[i].evaluate(el => el.className);
    const isAccent = classes.includes('accent-bg');
    const bgColor = isAccent ? '#0E9957' : '#292A25';

    await page.evaluate(c => {
      document.documentElement.style.background = c;
      document.body.style.background = c;
    }, bgColor);

    await slides[i].evaluate((el, s) => {
      el.style.display = 'flex';
      el.style.position = 'fixed';
      el.style.top = '0';
      el.style.left = '0';
      el.style.width = '1080px';
      el.style.height = '1350px';
      el.style.zIndex = '9999';
      el.style.transform = `scale(${s})`;
      el.style.transformOrigin = 'top left';
    }, scale);

    await page.waitForTimeout(300);

    await page.screenshot({
      path,
      clip: { x: 0, y: 0, width: cssW, height: cssH }
    });

    await slides[i].evaluate(el => {
      el.style.display = 'none';
      el.style.position = '';
      el.style.transform = '';
      el.style.transformOrigin = '';
    });
  }

  for (let i = 0; i < total; i++)
    await slides[i].evaluate(el => el.style.display = '');
}
```

**Regras críticas:**
- SEMPRE usar `transform: scale()` para compensar DPR
- SEMPRE setar `html+body background` para a cor do slide antes de capturar
- NUNCA usar `element.screenshot()` — usar `page.screenshot({ clip })`
- Servir o HTML via HTTP server local (`python3 -m http.server PORT`)

### Passo 5: Gerar legenda.txt

```
[LEGENDA]
Caption sugerida para o post do Instagram.
Texto provocativo que complementa o carrossel.

Siga @oeduardo.1 para mais conteúdo sobre IA.

[HASHTAGS]
#ia #inteligenciaartificial #chatgpt #openai #tecnologia #futuro #inovacao #machinelearning #artificialintelligence
```

---

## APIs e Credenciais

### Gemini API — Geração de Imagens
- **Modelo**: `gemini-2.5-flash-image` (tier flash, equilíbrio custo/qualidade — nunca `-pro`)
- **Endpoint**: `https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-image:generateContent`
- **Auth**: header `x-goog-api-key: $GEMINI_API_KEY` (variável lida do `.env`, nunca hardcoded)
- **Resposta**: imagem base64 em `candidates[0].content.parts[0].inlineData.data`
- Salvar como `.jpg` na pasta `output/nome-do-carrossel/img/slide_N.jpg`

### Playwright MCP
- Viewport: 1080x1350 (formato Instagram 4:5)

---

## Organização de Arquivos

```
output/
└── nome-do-carrossel/
    ├── carrossel.html
    ├── img/
    │   ├── slide_01.jpg   ← gerada via Gemini API
    │   ├── slide_02.jpg
    │   └── ...
    ├── slide_01.png       ← screenshot final
    ├── slide_02.png
    ├── ...
    └── legenda.txt
```

---

## Comando Rápido

Quando Eduardo enviar o conteúdo dos slides:

1. **Ler os slides** recebidos — identificar capa, internos e CTA
2. **Gerar imagens** via Gemini API (`gemini-2.5-flash-image`) — 1 por slide
3. **Salvar imagens** em `output/nome-do-carrossel/img/`
4. **Montar o HTML** com os textos exatos recebidos, seguindo o template desta skill
5. **Capturar PNGs** via Playwright MCP
6. **Criar legenda.txt** com caption e hashtags sugeridos
7. **Salvar tudo** em `output/nome-do-carrossel/`
