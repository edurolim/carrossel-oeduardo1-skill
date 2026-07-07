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
- **Fotos de pessoas reais** como fundo na capa/CTA — geradas via OpenAI API (ver Passo 2)
- **Overlay com gradiente**: `linear-gradient(180deg, rgba(0,0,0,0.2) 0%, rgba(0,0,0,0.7) 100%)`
- **Palavras-chave em verde** `#0E9957` no meio da frase para destaque
- **Texto grande e bold** ocupando a maior parte do slide
- **Numeração do slide** só a partir do slide 2: formato `1/9` no rodapé

---

## Layouts dos Slides

### Slide 1 — Capa (1080x1350px)
- Foto impactante de pessoa ou cena como fundo (Unsplash)
- Logo do Instagram + @oeduardo.1 centralizado acima do título
- Título em CAIXA ALTA, IMPACT 52-64px, com 1-2 palavras em verde `#0E9957`
- Formato de pergunta provocativa ou afirmação chocante
- Subtítulo em Inter 22-26px, verde `#3CD3A4` ou branco
- SEM numeração — a capa não tem número de slide
- Header topo obrigatório
- Rodapé com @oeduardo.1, SEM número de página

### Slides Internos 2-N (Fundo Sólido + Foto Contida)

Variar entre 4 variantes para criar dinamismo visual:

**Variante A — Foto no MEIO**: texto grande acima (Inter 36-42px) → foto → texto menor abaixo (Inter 26-30px)

**Variante B — Foto na BASE**: textos grandes preenchendo o topo → foto alinhada na base

**Variante C — Foto no TOPO**: foto alinhada no topo → textos preenchendo a parte inferior

**Variante D — Cor Sólida Verde SEM foto**: fundo `#0E9957`, texto branco IMPACT grande, para slides de impacto máximo (usar 1-2 por carrossel)

**Regras dos slides internos:**
- PREENCHER TODO O ESPAÇO — sem grandes áreas vazias
- Hierarquia: texto principal 36-42px, texto secundário 26-30px
- Posição da foto VARIADA entre slides — não repetir
- Fonte Inter (peso 400-700)
- Palavras destacadas: cor `#0E9957` ou `#2C7050` + `font-weight: 700` + `font-style: italic`
- Texto narrativo: storytelling em parágrafos de 3-5 linhas
- `line-height: 1.45-1.55`
- Sem `text-transform: uppercase` nos slides internos — capitalize natural

### Slide Final — CTA
- Foto de fundo impactante (Unsplash)
- IMPACT para o título da chamada para ação
- Destaque do @oeduardo.1
- Ícones de ações (salvar, compartilhar, curtir)
- Acento do @oeduardo.1 em verde `#0E9957`

### Header Topo (todos os slides)
- **Posição**: `position: absolute; top: 0; left: 0; right: 0;`
- **Esquerdo**: `Powered by Postlab` — branco 0.55 opacity, Space Grotesk 400, 14px, uppercase
- **Centro**: `@oeduardo.1` — branco 0.55 opacity, Space Grotesk 400, 14px, uppercase
- **Direito**: Mês e ano no formato `Março 2026 ®` — Space Grotesk 400, 14px, uppercase
- **Padding**: `20px 40px`

### Rodapé (todos os slides)
- **Esquerdo**: Ícone Instagram SVG + `@oeduardo.1`, peso 600
- **Direito**: `N/total` — APENAS a partir do slide 2. Capa não tem número
- Contagem: slide 2 mostra `1/9`, slide 3 mostra `2/9`, até `9/9`
- **Fundo**: `rgba(0,0,0,0.5)`

---

## Template HTML Base

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <title>Carrossel @oeduardo.1</title>
  <link href="https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,700&family=Space+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }

    /* ===== CAPA E CTA — FOTO DE FUNDO ===== */
    .slide {
      width: 1080px;
      height: 1350px;
      position: relative;
      overflow: hidden;
      font-family: 'Inter', sans-serif;
      color: #ffffff;
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 60px 56px 90px;
      page-break-after: always;
    }

    .slide-bg {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background-size: cover;
      background-position: center;
      filter: brightness(0.5);
      z-index: 0;
    }

    .slide-overlay {
      position: absolute;
      top: 0; left: 0;
      width: 100%; height: 100%;
      background: linear-gradient(180deg, rgba(0,0,0,0.1) 0%, rgba(0,0,0,0.7) 100%);
      z-index: 1;
    }

    .slide-content {
      position: relative;
      z-index: 2;
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    /* TÍTULOS CAPA/CTA — IMPACT */
    .title {
      font-family: Impact, 'Arial Narrow', sans-serif;
      font-size: 60px;
      font-weight: 400;
      line-height: 1.05;
      letter-spacing: 0px;
      text-transform: uppercase;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }

    .title .highlight {
      color: #0E9957;
    }

    .title .highlight-secondary {
      color: #3CD3A4;
    }

    /* SUBTÍTULOS CAPA/CTA — Inter */
    .subtitle {
      font-family: 'Inter', sans-serif;
      font-size: 24px;
      font-weight: 500;
      color: rgba(255,255,255,0.85);
      line-height: 1.5;
      text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
      max-width: 900px;
    }

    .subtitle-green {
      font-family: 'Inter', sans-serif;
      font-size: 22px;
      font-weight: 600;
      color: #3CD3A4;
      line-height: 1.5;
      text-shadow: 1px 1px 4px rgba(0,0,0,0.8);
    }

    /* BRANDING CENTRALIZADO — SLIDE 1 APENAS */
    .cover-branding {
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 12px;
      margin-bottom: 16px;
    }

    .cover-branding svg { width: 32px; height: 32px; fill: #ffffff; }

    .cover-branding span {
      font-family: 'Inter', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #ffffff;
      text-shadow: 2px 2px 8px rgba(0,0,0,0.8);
    }

    /* HEADER TOPO — TODOS OS SLIDES */
    .top-header {
      position: absolute;
      top: 0; left: 0; right: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 22px 40px;
      z-index: 10;
      font-family: 'Space Grotesk', sans-serif;
    }

    .top-header span {
      font-size: 14px;
      font-weight: 400;
      color: rgba(255,255,255,0.55);
      letter-spacing: 0.8px;
      text-transform: uppercase;
    }

    /* RODAPÉ — TODOS OS SLIDES */
    .footer {
      position: absolute;
      bottom: 0; left: 0; right: 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 18px 40px;
      background: rgba(0,0,0,0.5);
      z-index: 10;
    }

    .footer-left { display: flex; align-items: center; gap: 10px; }
    .footer-left svg { width: 22px; height: 22px; fill: #ffffff; }
    .footer-left span { font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 600; color: #ffffff; }
    .footer-right { font-family: 'Inter', sans-serif; font-size: 18px; font-weight: 500; color: rgba(255,255,255,0.6); }

    /* ===== SLIDES INTERNOS — FUNDO SÓLIDO ===== */
    .slide-editorial {
      width: 1080px;
      height: 1350px;
      position: relative;
      overflow: hidden;
      font-family: 'Inter', sans-serif;
      color: #ffffff;
      background: #292A25;
      display: flex;
      flex-direction: column;
      justify-content: center;
      padding: 80px 56px 90px;
      page-break-after: always;
    }

    /* Variante cor sólida verde (impacto máximo) */
    .slide-editorial.accent-bg {
      background: #0E9957;
    }

    .slide-editorial .editorial-content {
      display: flex;
      flex-direction: column;
      gap: 28px;
      z-index: 2;
      flex: 1;
      justify-content: center;
    }

    /* Texto principal — GRANDE, impactante — Inter */
    .slide-editorial .narrative-text {
      font-family: 'Inter', sans-serif;
      font-size: 38px;
      font-weight: 400;
      line-height: 1.45;
      color: #ffffff;
    }

    /* Texto secundário — menor, complementar */
    .slide-editorial .narrative-text.secondary {
      font-size: 28px;
      font-weight: 400;
      line-height: 1.5;
    }

    /* Destaques inline — verde primário */
    .slide-editorial .narrative-text .highlight {
      color: #0E9957;
      font-weight: 700;
      font-style: italic;
    }

    .slide-editorial .narrative-text .highlight-secondary {
      color: #2C7050;
      font-weight: 700;
      font-style: italic;
    }

    .slide-editorial .narrative-text strong { font-weight: 700; }

    /* Na variante accent-bg, destaques ficam em branco */
    .slide-editorial.accent-bg .narrative-text .highlight {
      color: #ffffff;
      text-decoration: underline;
      text-decoration-thickness: 3px;
    }

    .slide-editorial.accent-bg .narrative-text .highlight-secondary {
      color: rgba(255,255,255,0.8);
      font-weight: 700;
      font-style: italic;
    }

    /* Foto contida nos slides internos */
    .slide-editorial .editorial-photo-container {
      width: 100%;
      border-radius: 8px;
      overflow: hidden;
    }

    .slide-editorial .editorial-photo-container img {
      width: 100%;
      height: 380px;
      object-fit: cover;
      display: block;
    }

    /* CTA — ícone de ação */
    .cta-actions {
      display: flex;
      gap: 32px;
      margin-top: 20px;
    }

    .cta-action-item {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
    }

    .cta-follow-box {
      margin-top: 40px;
      padding: 24px 48px;
      background: rgba(14,153,87,0.2);
      border: 1px solid rgba(14,153,87,0.5);
      border-radius: 8px;
    }

    .cta-follow-box span {
      font-family: 'Inter', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #3CD3A4;
    }
  </style>
</head>
<body>

  <!-- ===================== SLIDE 1 — CAPA ===================== -->
  <div class="slide">
    <div class="slide-bg" style="background-image: url('URL_UNSPLASH_AQUI')"></div>
    <div class="slide-overlay"></div>
    <div class="top-header">
      <span>Powered by Postlab</span>
      <span>@oeduardo.1</span>
      <span>Março 2026 ®</span>
    </div>
    <div class="slide-content">
      <div class="cover-branding">
        <!-- SVG Instagram inline aqui -->
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        <span>@oeduardo.1</span>
      </div>
      <h1 class="title">
        POR QUE A <span class="highlight">IA</span> ESTÁ MUDANDO TUDO E NINGUÉM TE CONTA?
      </h1>
      <p class="subtitle">Investigamos o impacto real da inteligência artificial no mercado de trabalho e na vida das pessoas</p>
    </div>
    <div class="footer">
      <div class="footer-left">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        <span>@oeduardo.1</span>
      </div>
      <!-- SEM número de página na capa -->
    </div>
  </div>

  <!-- ====== SLIDE INTERNO — VARIANTE A (FOTO NO MEIO) ====== -->
  <div class="slide-editorial">
    <div class="top-header">
      <span>Powered by Postlab</span>
      <span>@oeduardo.1</span>
      <span>Março 2026 ®</span>
    </div>
    <div class="editorial-content">
      <p class="narrative-text" style="font-size: 38px;">
        Texto narrativo GRANDE contando a história. Desenvolva o ponto com <span class="highlight">palavras destacadas em verde</span> inline. Preencha bem o espaço acima da foto.
      </p>
      <div class="editorial-photo-container">
        <img src="URL_UNSPLASH_AQUI" alt="Foto contextual">
      </div>
      <p class="narrative-text secondary">
        Texto menor complementando. <strong>Frases importantes em bold.</strong> Dados como <span class="highlight-secondary">40% de crescimento</span> em destaque.
      </p>
    </div>
    <div class="footer">
      <div class="footer-left">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        <span>@oeduardo.1</span>
      </div>
      <div class="footer-right">1/9</div>
    </div>
  </div>

  <!-- ====== SLIDE IMPACTO — VARIANTE D (COR SÓLIDA VERDE) ====== -->
  <div class="slide-editorial accent-bg">
    <div class="top-header">
      <span>Powered by Postlab</span>
      <span>@oeduardo.1</span>
      <span>Março 2026 ®</span>
    </div>
    <div class="editorial-content">
      <p class="narrative-text" style="font-size: 42px; font-weight: 600; line-height: 1.3; font-family: Impact, sans-serif; text-transform: uppercase;">
        A IA não está substituindo pessoas. Ela está <span class="highlight">substituindo pessoas que não usam IA.</span>
      </p>
      <p class="narrative-text" style="font-size: 28px; font-weight: 400; line-height: 1.5;">
        Texto complementar com mais detalhes, explicando o contexto e adicionando profundidade ao argumento principal do slide.
      </p>
    </div>
    <div class="footer">
      <div class="footer-left">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        <span>@oeduardo.1</span>
      </div>
      <div class="footer-right">5/9</div>
    </div>
  </div>

  <!-- ====== SLIDE FINAL — CTA ====== -->
  <div class="slide">
    <div class="slide-bg" style="background-image: url('URL_UNSPLASH_AQUI')"></div>
    <div class="slide-overlay"></div>
    <div class="top-header">
      <span>Powered by Postlab</span>
      <span>@oeduardo.1</span>
      <span>Março 2026 ®</span>
    </div>
    <span style="position:absolute;top:32px;right:40px;font-size:20px;font-weight:600;color:rgba(255,255,255,0.7);z-index:3;">9/9</span>
    <div class="slide-content">
      <h1 class="title" style="font-size: 52px;">
        GOSTOU? <span class="highlight">SALVE</span> ESTE POST!
      </h1>
      <p class="subtitle">Compartilhe com alguém que precisa entender o impacto da IA</p>
      <div class="cta-actions">
        <div class="cta-action-item">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#0E9957" stroke-width="2"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"/></svg>
          <span style="font-size:16px;color:#0E9957;font-weight:600;font-family:'Inter',sans-serif;">SALVAR</span>
        </div>
        <div class="cta-action-item">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#ffffff" stroke-width="2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          <span style="font-size:16px;color:#ffffff;font-weight:600;font-family:'Inter',sans-serif;">ENVIAR</span>
        </div>
        <div class="cta-action-item">
          <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#3CD3A4" stroke-width="2"><path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"/></svg>
          <span style="font-size:16px;color:#3CD3A4;font-weight:600;font-family:'Inter',sans-serif;">CURTIR</span>
        </div>
      </div>
      <div class="cta-follow-box">
        <span>SIGA @oeduardo.1</span>
      </div>
    </div>
    <div class="footer">
      <div class="footer-left">
        <svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zM12 0C8.741 0 8.333.014 7.053.072 2.695.272.273 2.69.073 7.052.014 8.333 0 8.741 0 12c0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98C8.333 23.986 8.741 24 12 24c3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98C15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 100 12.324 6.162 6.162 0 000-12.324zM12 16a4 4 0 110-8 4 4 0 010 8zm6.406-11.845a1.44 1.44 0 100 2.881 1.44 1.44 0 000-2.881z"/></svg>
        <span>@oeduardo.1</span>
      </div>
      <div class="footer-right">9/9</div>
    </div>
  </div>

</body>
</html>
```

---

## Regras de Design do Conteúdo

O conteúdo de cada slide já vem pronto do Eduardo. Sua função é apenas aplicar o estilo visual correto:

- Texto em **CAIXA ALTA** só nos títulos da capa e CTA (IMPACT)
- **1-2 palavras em verde** `#0E9957` por slide para destaque — identificar as palavras-chave do texto enviado
- Slides internos: capitalize natural, Inter, sem uppercase
- Cada slide deve ter uma **foto diferente**
- **Variante D** (cor sólida verde): usar em 1-2 slides para impacto máximo, idealmente no slide mais "frase de efeito"

---

## Fluxo de Trabalho

### Passo 1: Receber o Conteúdo

Eduardo envia **18 textos numerados** (texto 1 a texto 18). Esses textos são **sempre condensados em 9 slides** — NUNCA criar um slide por texto.

**REGRA ABSOLUTA: 18 textos → 9 slides. Sem exceções.**

#### Distribuição fixa dos 18 textos nos 9 slides:

| Slide | Tipo | Textos | Uso no HTML |
|-------|------|--------|-------------|
| 1 | CAPA (`slide-capa`) | texto 1 + texto 2 | texto 2 → `capa-pretitle`; texto 1 → `capa-title` |
| 2 | TIPO A (`slide-tipo-a`) | texto 3 + texto 4 | texto 3 → `ta-title`; texto 4 → `ta-text` |
| 3 | TIPO B (`slide-tipo-b`) | texto 5 + texto 6 + texto 7 | texto 5 → `tb-title`; textos 6+7 → `tb-text` |
| 4 | TIPO A (`slide-tipo-a`) | texto 8 + texto 9 | texto 8 → `ta-title`; texto 9 → `ta-text` |
| 5 | TIPO B (`slide-tipo-b`) | texto 10 + texto 11 + texto 12 | texto 10 → `tb-title`; textos 11+12 → `tb-text` |
| 6 | TIPO A (`slide-tipo-a`) | texto 13 + texto 14 | texto 13 → `ta-title`; texto 14 → `ta-text` |
| 7 | TIPO B (`slide-tipo-b`) | texto 15 + texto 16 | texto 15 → `tb-title`; texto 16 → `tb-text` |
| 8 | TIPO A (`slide-tipo-a`) | texto 17 | texto 17 → `ta-title` + desenvolver em `ta-text` |
| 9 | TIPO B (`slide-tipo-b`) | texto 18 | texto 18 → `tb-text` direto (sem `tb-title`) |

**Regras de combinação de textos dentro do slide:**
- `tb-title` / `ta-title`: o texto mais curto e impactante do grupo — serve como gancho
- `tb-text` / `ta-text`: os demais textos do grupo combinados — desenvolvem o argumento
- Quando um grupo tem 3 textos, os 2 menores ficam no body/text, separados por `<br><br>`
- **Slide 9 (texto 18)**: SEMPRE TIPO B com o texto exato do autor em `tb-text`, sem `tb-title`, sem CTA genérico

**Imagens: 9 imagens geradas** (slide_01.jpg a slide_09.jpg), uma por slide.

### Passo 2: Gerar Imagens via OpenAI API (gpt-image-1)

Usar o modelo `gpt-image-1` da OpenAI para gerar uma imagem por slide (capa, internos e CTA).

**Endpoint:**
```
POST https://api.openai.com/v1/images/generations
Header: Authorization: Bearer [OPENAI_API_KEY]
```

**Exemplo de chamada:**
```bash
curl -s -X POST \
  "https://api.openai.com/v1/images/generations" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-1",
    "prompt": "Extreme close-up portrait of a 40-year-old man, jaw clenched, eyes wide with sudden realization, harsh single side light casting half his face in shadow, cinematic, photorealistic, 35mm film grain, high contrast, portrait orientation, no text, no words",
    "size": "1024x1536",
    "quality": "high",
    "n": 1
  }'
```

**A resposta retorna a imagem em base64** dentro de `data[0].b64_json`. Salvar como `.jpg` e referenciar no HTML.

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

**Fallback**: se a chamada à OpenAI API falhar (erro de quota, timeout, etc.), interromper e avisar Eduardo — não usar Unsplash.

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

### OpenAI API — Geração de Imagens
- **Modelo**: `gpt-image-1`
- **Endpoint**: `https://api.openai.com/v1/images/generations`
- **Auth**: header `Authorization: Bearer $OPENAI_API_KEY` (variável lida do `.env`, nunca hardcoded)
- **Resposta**: imagem base64 em `data[0].b64_json`
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
    │   ├── slide_01.jpg   ← gerada via OpenAI API
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
2. **Gerar imagens** via OpenAI API (`gpt-image-1`) — 1 por slide
3. **Salvar imagens** em `output/nome-do-carrossel/img/`
4. **Montar o HTML** com os textos exatos recebidos, seguindo o template desta skill
5. **Capturar PNGs** via Playwright MCP
6. **Criar legenda.txt** com caption e hashtags sugeridos
7. **Salvar tudo** em `output/nome-do-carrossel/`
