# Identidade Visual — Carrosséis @oeduardo.1

> Arquivo de referência único para todos os parâmetros visuais. Altere aqui e replique no HTML/SKILL.md.

---

## 1. Dimensões

| Item | Valor |
|------|-------|
| Formato do slide | 1080 × 1350 px (Instagram 4:5) |
| Slides por carrossel | 9 slides |
| Textos por carrossel | 18 textos → condensados em 9 slides |

---

## 2. Paleta de Cores

### Cores principais

| Token | Hex / Valor | Uso |
|-------|-------------|-----|
| `verde-primario` | `#0E9957` | Highlights `.hl`, dividers, botão CTA, bordas de caixa |
| `verde-secundario` | `#3CD3A4` | Highlights `.hl2`, textos complementares em verde claro |
| `verde-escuro` | `#2C7050` | Destaques inline secundários (quando necessário) |
| `branco-puro` | `#ffffff` | Títulos principais, texto forte |
| `branco-titulo` | `rgba(255,255,255,0.82)` | Corpo de texto em TIPO B |
| `branco-body` | `rgba(255,255,255,0.78)` | Corpo de texto em TIPO A |
| `branco-pretitle` | `rgba(255,255,255,0.68)` | Pre-título da capa |
| `branco-header` | `rgba(255,255,255,0.50)` | Header/rodapé superior |
| `preto-slide-a` | `#0d0d0d` | Fundo do slide TIPO A |
| `preto-slide-b` | `#000000` | Fundo do slide TIPO B e CAPA |

### Overlays e fundos

| Elemento | Valor |
|----------|-------|
| Filtro da foto na CAPA | `filter: brightness(0.42)` |
| Filtro da foto no TIPO B | `filter: brightness(0.40)` |
| Overlay gradiente da CAPA | `linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.25) 40%, rgba(0,0,0,0.75) 70%, rgba(0,0,0,0.92) 100%)` |
| Overlay gradiente do TIPO B | `linear-gradient(180deg, rgba(0,0,0,0.05) 0%, rgba(0,0,0,0.10) 35%, rgba(0,0,0,0.72) 60%, rgba(0,0,0,0.94) 100%)` |
| Fundo do footer | `rgba(0,0,0,0.55)` |

---

## 3. Tipografia

### Fontes

| Fonte | Fonte-family CSS | Uso |
|-------|-----------------|-----|
| **Impact** | `Impact, 'Arial Narrow', sans-serif` | Título da capa (`capa-title`) |
| **Inter** | `'Inter', sans-serif` | Todo o restante |
| **Space Grotesk** | `'Space Grotesk', sans-serif` | Header e rodapé superior |

### Escala tipográfica — CAPA

| Elemento | Fonte | Tamanho | Peso | Line-height | Outros |
|----------|-------|---------|------|-------------|--------|
| `capa-pretitle` | Inter | 28px | 800 | 1.45 | uppercase, letter-spacing 0.5px, max-width 860px |
| `capa-title` | Impact | 86px | 400 | 0.96 | uppercase, text-shadow 3px 3px 12px rgba(0,0,0,0.95) |
| `capa-btn` | Inter | 20px | 700 | — | uppercase, letter-spacing 1.5px |

### Escala tipográfica — TIPO A

| Elemento | Fonte | Tamanho | Peso | Line-height | Outros |
|----------|-------|---------|------|-------------|--------|
| `ta-title` | Inter | 46px | 800 | 1.12 | capitalize natural |
| `ta-text` | Inter | 27px | 400 | 1.58 | capitalize natural |
| `.hl` inline | Inter | (herda) | 600 | — | cor `#0E9957` |
| `.hl2` inline | Inter | (herda) | 600 | — | cor `#3CD3A4` |
| `strong` inline | Inter | (herda) | 700 | — | cor `#ffffff` |

### Escala tipográfica — TIPO B

| Elemento | Fonte | Tamanho | Peso | Line-height | Outros |
|----------|-------|---------|------|-------------|--------|
| `tb-title` | Inter | 46px | 800 | 1.12 | text-shadow 1px 1px 6px rgba(0,0,0,0.8) |
| `tb-text` | Inter | 27px | 400 | 1.55 | text-shadow 1px 1px 4px rgba(0,0,0,0.7) |
| `tb-text` no slide 9 | Inter | 30px | 400 | 1.65 | texto do autor, sem `tb-title` |
| `.hl` inline | Inter | (herda) | 600 | — | cor `#0E9957` |
| `.hl2` inline | Inter | (herda) | 600 | — | cor `#3CD3A4` |
| `strong` inline | Inter | (herda) | 700 | — | cor `#ffffff` |

### Escala tipográfica — Header / Rodapé

| Elemento | Fonte | Tamanho | Peso | Outros |
|----------|-------|---------|------|--------|
| Texto do header | Space Grotesk | 14px | 400 | uppercase, letter-spacing 1px, cor `rgba(255,255,255,0.50)` |
| Handle do footer | Inter | 17px | 600 | cor `#ffffff` |
| Numeração do footer | Inter | 17px | 400 | cor `rgba(255,255,255,0.45)` |

---

## 4. Header (topo de todos os slides)

```
[ Eduardo Rolim ]    [ @oeduardo.1 ]    [ Mês Ano ® ]
```

| Propriedade | Valor |
|-------------|-------|
| Posição | `position: absolute; top: 0; left: 0; right: 0` |
| Padding | `26px 48px` |
| z-index | `20` |
| Coluna esquerda | `Eduardo Rolim` |
| Coluna central | `@oeduardo.1` |
| Coluna direita | Mês e ano atuais no formato `Abril 2026 ®` |
| Cor do texto | `rgba(255,255,255,0.50)` |
| Fonte | Space Grotesk 400, 14px, uppercase, letter-spacing 1px |

---

## 5. Layouts dos Slides

### Slide 1 — CAPA (`slide-capa`)

```
┌─────────────────────────────┐
│  Eduardo Rolim  @oeduardo.1 │  ← header absoluto
│                             │
│    [foto de fundo           │
│     brightness 0.42         │
│     + gradiente overlay]    │
│                             │
│  ┌─────────────────────┐    │
│  │  capa-pretitle      │    │  ← Inter 28px 800, opacity 0.68
│  │  (texto 2)          │    │
│  │                     │    │
│  │  CAPA-TITLE IMPACT  │    │  ← Impact 86px, uppercase
│  │  (texto 1)          │    │
│  │                     │    │
│  │  [ BOTÃO CTA ]      │    │  ← #0E9957, Inter 20px 700
│  └─────────────────────┘    │
└─────────────────────────────┘
```

| Propriedade | Valor |
|-------------|-------|
| Fundo | `#000` + `<img>` com `brightness(0.42)` |
| Overlay | gradiente CAPA (ver seção 2) |
| `.capa-content` position | `position: absolute; bottom: 90px` |
| `.capa-content` padding | `0 60px` |
| `.capa-content` alinhamento | `align-items: center; text-align: center` |
| `.capa-content` gap | `22px` |
| `.capa-btn` background | `#0E9957` |
| `.capa-btn` padding | `20px 48px` |
| `.capa-btn` border-radius | `100px` |
| `.capa-btn` margin-top | `10px` |

---

### Slides 2, 4, 6, 8 — TIPO A (`slide-tipo-a`)

```
┌─────────────────────────────┐
│  Eduardo Rolim  @oeduardo.1 │  ← header absoluto
│ ┌─────────────────────────┐ │
│ │                         │ │
│ │   FOTO (580px altura)   │ │  ← object-fit: cover
│ │                         │ │
│ └─────────────────────────┘ │
│ ──── (divider verde 60px) ─ │  ← #0E9957, 3px altura
│                             │
│  ta-title                   │  ← Inter 46px 800
│  (texto mais curto/gancho)  │
│                             │
│  ta-text                    │  ← Inter 27px 400, opacity 0.78
│  (texto de desenvolvimento) │
└─────────────────────────────┘
```

| Propriedade | Valor |
|-------------|-------|
| Fundo | `#0d0d0d` |
| Layout | `display: flex; flex-direction: column` |
| `.ta-img` altura | `580px` fixos, `flex-shrink: 0` |
| `.ta-img img` | `object-fit: cover; width: 100%; height: 100%` |
| `.ta-body` padding | `40px 56px 90px` |
| `.ta-body` gap | `22px` |
| `.ta-divider` tamanho | `60px × 3px`, `border-radius: 2px` |
| `.ta-divider` cor | `#0E9957` |

---

### Slides 3, 5, 7, 9 — TIPO B (`slide-tipo-b`)

```
┌─────────────────────────────┐
│  Eduardo Rolim  @oeduardo.1 │  ← header absoluto
│                             │
│    [foto full-bleed         │
│     brightness 0.40         │
│     + gradiente overlay]    │
│                             │
│                             │
│ ── (divider verde 56px) ─── │  ← #0E9957, 3px
│  tb-title                   │  ← Inter 46px 800, text-shadow
│  (texto gancho)             │
│                             │
│  tb-text                    │  ← Inter 27px 400, opacity 0.82
│  (desenvolvimento)          │
└─────────────────────────────┘
```

| Propriedade | Valor |
|-------------|-------|
| Fundo | `#000` |
| `.tb-img` | `position: absolute; top:0; left:0; width:100%; height:100%` + `brightness(0.40)` |
| `.tb-overlay` | gradiente TIPO B (ver seção 2) + `z-index: 1` |
| `.tb-content` position | `position: absolute; bottom: 90px` |
| `.tb-content` padding | `0 56px` |
| `.tb-content` gap | `20px` |
| `.tb-content` z-index | `5` |
| `.tb-divider` tamanho | `56px × 3px`, `border-radius: 2px` |
| `.tb-divider` cor | `#0E9957` |

---

### Slide 9 — Texto 18 do autor (TIPO B especial)

- Usa estrutura TIPO B normalmente
- **Sem `tb-title`** — apenas `tb-divider` + `tb-text`
- `tb-text` com `font-size: 30px` e `line-height: 1.65`
- Exibe o texto exato do autor (texto 18) — sem CTA genérico

---

## 6. Distribuição dos Textos nos Slides

**REGRA ABSOLUTA: 18 textos → 9 slides. Nunca 1 slide por texto.**

| Slide | Tipo HTML | Textos | `ta-title` / `tb-title` | `ta-text` / `tb-text` |
|-------|-----------|--------|--------------------------|----------------------|
| 1 | `slide-capa` | 1 + 2 | texto 1 → `capa-title` | texto 2 → `capa-pretitle` |
| 2 | `slide-tipo-a` | 3 + 4 | texto 3 | texto 4 |
| 3 | `slide-tipo-b` | 5 + 6 + 7 | texto 5 | textos 6 + 7 (separados por `<br><br>`) |
| 4 | `slide-tipo-a` | 8 + 9 | texto 8 | texto 9 |
| 5 | `slide-tipo-b` | 10 + 11 + 12 | texto 10 | textos 11 + 12 (separados por `<br><br>`) |
| 6 | `slide-tipo-a` | 13 + 14 | texto 13 | texto 14 |
| 7 | `slide-tipo-b` | 15 + 16 | texto 15 | texto 16 |
| 8 | `slide-tipo-a` | 17 | texto 17 | desenvolver o argumento |
| 9 | `slide-tipo-b` | 18 | — (sem título) | texto 18 em 30px/1.65 |

---

## 7. Sistema de Destaques Inline

| Classe | Cor | Peso | Quando usar |
|--------|-----|------|-------------|
| `.hl` | `#0E9957` (verde primário) | 600 | Conceito principal, número, palavra-chave central |
| `.hl2` | `#3CD3A4` (verde claro) | 600 | Conceito secundário, contraste com `.hl` na mesma frase |
| `<strong>` | `#ffffff` (branco puro) | 700 | Ênfase em frase sem cor — afirmação direta |

**Regra de uso:** máximo 1–2 destaques por parágrafo. Não acumular `.hl` + `.hl2` + `<strong>` na mesma frase.

---

## 8. Imagens — Geração via Gemini API

### Especificações técnicas

| Parâmetro | Valor |
|-----------|-------|
| API | Gemini Image — `gemini-3.1-flash-image-preview` |
| Quantidade | 9 imagens por carrossel (1 por slide) |
| Formato de saída | `.jpg` em `output/nome-do-carrossel/img/slide_NN.jpg` |
| Aspect ratio solicitado | `portrait orientation, 4:5 aspect ratio` |
| Proibição absoluta | `no text, no words, no letters` em todos os prompts |

### Framework de prompt — 4 camadas obrigatórias

Cada prompt deve ter as 4 camadas a seguir. Prompts genéricos são proibidos.

| Camada | O que descrever | Ruim | Bom |
|--------|----------------|------|-----|
| 1. Sujeito específico | Idade, expressão exata, estado emocional | `"professional person"` | `"52-year-old man, jaw clenched, eyes wide with disbelief"` |
| 2. Momento de clímax | Instante decisivo, não pose estática | `"sitting at desk"` | `"mid-gesture, realization hitting, split second before"` |
| 3. Ambiente narrativo | Cenário que reforça a tensão do slide | `"office"` | `"empty corporate floor, hundreds of abandoned desks stretching to darkness"` |
| 4. Técnica fotográfica | Ângulo e distância focal que ampliam o impacto | (ausente) | `"extreme close-up, 85mm lens"` / `"low-angle wide shot"` / `"Dutch angle"` |

### Templates de prompt por posição do slide

| Slide | Técnica recomendada | Objetivo visual |
|-------|---------------------|-----------------|
| 1 — CAPA | Extreme close-up, iluminação chiaroscuro | Parar o scroll imediatamente |
| 2, 4, 6, 8 — TIPO A | Imagem ambiental com escala ou contraste | Contextualizar o argumento |
| 3, 5, 7 — TIPO B | Ângulo dramático, luz dura, momento de tensão | Amplificar a emoção do texto |
| 9 — Slide 18 autor | Contato visual direto, postura de confiança | Conexão e encerramento |

### Estilo base (sempre incluir)
```
cinematic, photorealistic, high contrast, moody lighting, portrait orientation, 4:5 aspect ratio, no text, no words, no letters
```

---

## 9. Regras de Design — O que é proibido

- **SEM glassmorphism** em nenhum slide
- **SEM cards flutuantes** sobre imagens
- **SEM `text-transform: uppercase`** nos slides TIPO A e TIPO B — apenas na CAPA
- **SEM página genérica de CTA** (`"GOSTOU? SALVE ESTE POST"`) — o slide 9 exibe o texto 18 do autor
- **SEM 1 slide por texto** — sempre condensar 18 textos em 9 slides
- **SEM imagens genéricas** de stock (`"professional person working"`, `"diverse team smiling"`)
- **SEM grandes áreas vazias** nos slides — preencher todo o espaço

---

## 10. Assinatura de Marca

| Elemento | Valor |
|----------|-------|
| Handle principal | `@oeduardo.1` |
| Nome exibido no header | `Eduardo Rolim` |
| Data no header | Mês e ano no formato `Abril 2026 ®` — atualizar a cada carrossel |
| Marca d'água footer | `@oeduardo.1` com ícone Instagram SVG (fill `#ffffff`) |

---

## 11. Como alterar a identidade visual

Para mudar qualquer parâmetro visual, altere neste arquivo e replique nas 3 fontes:

| O que mudar | Onde replicar |
|-------------|---------------|
| Cores, tipografia, tamanhos | `skill-extracted/carrossel-investigativo-edurolim/SKILL.md` → seção "Identidade Visual" |
| CSS dos slides | Template HTML da skill (seção "Template HTML Base") |
| Regras de imagem | SKILL.md → seção "Diretrizes de prompt para imagens" |
| Empacotado na skill | Reempacotar `carrossel-investigativo-edurolim.skill` (ZIP) |
| Versionar | Commit e push em `github.com/edurolim/carrossel-claudecode-skill-edurolim` |
