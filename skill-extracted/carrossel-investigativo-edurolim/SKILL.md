---
name: carrossel-investigativo-edurolim
description: Cria carrosséis completos para Instagram no estilo editorial/investigativo de Eduardo Rolim (@oeduardo.1). Recebe o conteúdo de cada slide já pronto e gera o HTML, busca/gera imagens e captura os PNGs. Paleta verde #0E9957 como acento primário. Tipografia IMPACT nos títulos da capa, Inter nos slides internos. Use esta skill sempre que Eduardo enviar o conteúdo dos slides separados e pedir para montar o carrossel, gerar os slides, criar o HTML, ou mencionar "criar carrossel completo", "gerar slides", "montar carrossel", "aqui o conteúdo". NÃO é necessário criar roteiro nem buscar tema — o conteúdo já vem pronto do usuário.
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
- **Fotos de pessoas reais** como fundo na capa/CTA — geradas via Gemini API (ver Passo 2)
- **Overlay com gradiente**: `linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%)`
- **Palavras-chave em verde** `#0E9957` no meio da frase para destaque
- **Texto grande e bold** ocupando a maior parte do slide
- **Numeração do slide** só a partir do slide 2: formato `1/9` no rodapé

---

## Layouts dos Slides — PADRÃO FIXO OBRIGATÓRIO

**Regra absoluta: sempre gerar seguindo exatamente esta sequência de 9 slides, nesta ordem, com estas classes CSS. Nunca inventar layout novo, nunca usar o template genérico antigo (`.slide` / `.slide-editorial`). Este é o padrão validado nos últimos carrosséis de produção (openai-industrial, custo-invisivel, stack-amuleto, saas-sequoia).**

| # | Tipo (classe) | Fundo | Conteúdo |
|---|---|---|---|
| 1 | `slide-capa` | foto full-bleed + overlay gradiente | pretitle + título Impact + botão CTA opcional |
| 2 | `slide-split` | 50% texto preto / 50% foto | tag + título + 3 bullets |
| 3 | `slide-mini-cta` | branco | CTA fixo obrigatório (ver Passo 1) |
| 4 | `slide-tipo-c` | branco | título + fórmula/destaque opcional |
| 5 | `slide-tipo-a` | preto `#0d0d0d`, foto no topo (580px) | título + texto |
| 6 | `slide-tipo-d` | foto full-bleed + overlay | título + texto (1-2 blocos) |
| 7 | `slide-split` | 50/50 (2ª ocorrência) | tag + título + 3 bullets |
| 8 | `slide-tipo-d` | foto full-bleed + overlay (2ª ocorrência) | título + texto |
| 9 | `slide-cta` | branco | nome + CTA final + fonte |

**LIMITES DE CARACTERES — OBRIGATÓRIO (evita overflow/corte de texto):**
- `capa-pretitle`: máx. **110 caracteres** (2-3 linhas em 28px)
- `capa-title`: máx. **70 caracteres**, sempre **1-2 linhas** (Impact 96px é gigante — texto longo estoura o frame e sobrepõe o botão)
- `capa-btn`: máx. **3 palavras** (ex: "Entenda o ponto")
- `split-title` / `td-title` / `tc-title` / `ta-title`: máx. **90 caracteres**, 2-3 linhas
- Se o texto 1 (headline) enviado for mais longo que 70 caracteres, **condensar** para caber na capa — nunca forçar o texto completo no `capa-title`

**Acentuação — OBRIGATÓRIO:** todo texto em português deve manter acentuação, cedilha e til corretos (não → nao é erro, decisões → decisoes é erro). Nunca gerar ou aceitar texto sem acentuação.

**Elementos obrigatórios em todo slide:**
- `.top-header`: `Eduardo Rolim` (esq) — `@oeduardo.1` (centro) — `Mês Ano ®` (dir), Space Grotesk 14px uppercase, opacity 0.50 (ou 0.35 em fundo branco)
- `.progress-bar`: barra fixa no rodapé, `.progress-fill` verde `#0E9957` crescendo por slide: 11.1%, 22.2%, 33.3%... até 100%
- `.slide-arrow`: seta de continuidade no canto inferior direito (exceto capa e CTA final)
- Destaque de palavra-chave sempre com `<span class="hl">`, cor `#0E9957`

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

    /* CAPA */
    .slide-capa {
      width: 1080px; height: 1350px;
      position: relative; overflow: hidden;
      background: #000; page-break-after: always;
    }
    .capa-img {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      object-fit: cover; filter: brightness(0.70); z-index: 0;
    }
    .capa-overlay {
      position: absolute; top: 0; left: 0; width: 100%; height: 100%;
      background: linear-gradient(180deg, rgba(0,0,0,0.00) 0%, rgba(0,0,0,0.08) 35%, rgba(0,0,0,0.45) 62%, rgba(0,0,0,0.72) 100%);
      z-index: 1;
    }
    .capa-content {
      position: absolute; bottom: 90px; left: 0; right: 0;
      padding: 0 60px;
      display: flex; flex-direction: column; align-items: center; text-align: center;
      gap: 22px; z-index: 10;
    }
    .capa-pretitle {
      font-family: 'Inter', sans-serif;
      font-size: 28px; font-weight: 800; line-height: 1.45;
      color: #ffffff; max-width: 860px;
      text-transform: uppercase; letter-spacing: 0.5px;
    }
    .capa-title {
      font-family: Impact, 'Arial Narrow', sans-serif;
      font-size: 96px; font-weight: 400;
      line-height: 0.96; text-transform: uppercase;
      color: #ffffff; text-shadow: 3px 3px 12px rgba(0,0,0,0.95);
    }
    .capa-title .hl { color: #0E9957; }
    .capa-btn {
      font-family: 'Inter', sans-serif;
      font-size: 20px; font-weight: 700;
      text-transform: uppercase; letter-spacing: 1.5px;
      color: #ffffff; background: #0E9957;
      padding: 20px 48px; border-radius: 100px; margin-top: 10px;
      display: flex; align-items: center; gap: 14px;
    }

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
    .cta-text {
      font-family: 'Inter', sans-serif;
      font-size: 30px; font-weight: 700; line-height: 1.45; color: #0f0f0f;
    }
    .cta-text .hl { color: #0E9957; }
    .cta-source {
      font-family: 'Inter', sans-serif;
      font-size: 18px; font-weight: 300; line-height: 1.6;
      color: rgba(0,0,0,0.55); margin-top: 4px;
    }
  </style>
</head>
<body>

<!-- SLIDE 1 — CAPA (textos 1+2) -->
<div class="slide-capa">
  <img class="capa-img" src="img/slide_N.jpg" alt="">
  <div class="capa-overlay"></div>
  <div class="top-header">
    <span>Eduardo Rolim</span><span>@oeduardo.1</span><span>Mês Ano ®</span>
  </div>
  <div class="capa-content">
    <p class="capa-pretitle">[texto 2 — pretitle: frase de contexto/apoio ao título]</p>
    <h1 class="capa-title">[texto 1 — título com <span class="hl">palavra-chave</span> em destaque]</h1>
    <div class="capa-btn">[CTA opcional] <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg></div>
  </div>
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
      <p class="cta-text"><span class="hl">[texto 17 — CTA final]</span></p>
      <p class="cta-source">[texto 18 — fonte/gancho de fechamento]</p>
    </div>
  </div>
  <div class="progress-bar" style="background:rgba(0,0,0,0.08);"><div class="progress-fill" style="width:100%"></div></div>
</div>

</body>
</html>
```

---

## Regras de Design do Conteúdo

O conteúdo de cada slide já vem pronto do Eduardo. Sua função é apenas aplicar o estilo visual correto:

- Título da capa (`capa-title`): CSS já força `text-transform: uppercase` — digitar o texto em caixa normal, o navegador renderiza maiúsculo automaticamente. Impact, com `<span class="hl">` na palavra-chave
- `split-title` também é uppercase por CSS (mesma lógica: digitar normal, renderiza maiúsculo)
- 1-2 palavras em verde `#0E9957` por slide para destaque — identificar as palavras-chave do texto enviado
- `tc-title`/`ta-title`/`td-title`/`cta-text`/`cta-name`: capitalize natural, Inter, SEM uppercase — não forçar caixa alta nesses
- Cada slide com foto deve ter uma **foto diferente**
- `slide-tipo-d` (fundo foto full-bleed) é o slide de maior impacto — reservar para a frase-martelo mais forte do bloco
- Nunca usar o template genérico antigo (`.slide`/`.slide-editorial`) — sempre as 7 classes fixas da seção "Layouts dos Slides"

---

## Fluxo de Trabalho

### Passo 1: Receber o Conteúdo

Eduardo envia **18 textos numerados** (texto 1 a texto 18). Esses textos são **sempre condensados em 9 slides** — NUNCA criar um slide por texto.

**REGRA ABSOLUTA: 18 textos → 9 slides. Sem exceções.**

#### Distribuição fixa dos 18 textos nos 9 slides:

| Slide | Tipo | Textos | Uso no HTML |
|-------|------|--------|-------------|
| 1 | CAPA (`slide-capa`) | texto 1 + texto 2 | texto 2 → `capa-pretitle`; texto 1 → `capa-title` |
| 2 | SPLIT (`slide-split`) | texto 3 + texto 4 | texto 3 → `split-title`; texto 4 → 1º `split-item` (bullets extras podem derivar do mesmo texto) |
| 3 | MINI CTA (`slide-mini-cta`) | fixo — não numerado | CTA fixo obrigatório em `mini-cta-title` |
| 4 | TIPO C (`slide-tipo-c`) | texto 5 + texto 6 + texto 7 | texto 5 → `tc-title`; textos 6+7 → `tc-text` (ou `tc-formula` se for dado/fórmula) |
| 5 | TIPO A (`slide-tipo-a`) | texto 8 + texto 9 | texto 8 → `ta-title`; texto 9 → `ta-text` |
| 6 | TIPO D (`slide-tipo-d`) | texto 10 + texto 11 | texto 10 → `td-title`; texto 11 → `td-text` |
| 7 | SPLIT (`slide-split`) | texto 12 + texto 13 + texto 14 | texto 12 → `split-title`; textos 13+14 → `split-item`s |
| 8 | TIPO D (`slide-tipo-d`) | texto 15 + texto 16 | texto 15 → `td-title`; texto 16 → `td-text` |
| 9 | CTA (`slide-cta`) | texto 17 + texto 18 | texto 17 → `cta-text`; texto 18 → `cta-source` |

**Regras de combinação de textos dentro do slide:**
- `*-title`: o texto mais curto e impactante do grupo — serve como gancho
- `*-text`: os demais textos do grupo combinados — desenvolvem o argumento
- `split-item`: cada bullet é uma frase curta com `<span class="split-bullet">•</span>` na frente
- **Slide 3 (mini-cta)**: SEMPRE o CTA fixo obrigatório (`Quer mais conteúdos como esse? Toca 2 vezes na tela e depois me segue.`), nunca um texto numerado do usuário
- **Slide 9 (CTA)**: `cta-name` é sempre "Eduardo Rolim"; `cta-text` carrega o texto 17 com `<span class="hl">`; `cta-source` é o texto 18

**Imagens: 9 imagens geradas** (slide_01.jpg a slide_09.jpg), uma por slide.

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

- **Capa (slide 1)** — deve parar o scroll imediatamente:
  Rosto dominando 70%+ do frame com expressão extrema + iluminação chiaroscuro.
  Ex: `"Extreme close-up portrait of a 40-year-old woman, one side of face in complete shadow, single harsh side light catching her eye and jaw, expression of quiet fury mixed with certainty, 35mm film grain, cinematic, photorealistic, no text, no words"`

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
