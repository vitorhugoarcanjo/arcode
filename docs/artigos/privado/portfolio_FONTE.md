# 🌐 PORTFÓLIO VITOR HUGO — FONTE DA VERDADE

**Versão:** 1.0
**Última atualização:** 15/10/2026
**Repositório:** https://github.com/vitorhugoarcanjo/arcode
**Domínio:** https://vitorhugoadp.com.br
**Status:** ⚠️ DOCUMENTO INTERNO — descreve a arquitetura e decisões do portfólio

---

## 📑 ÍNDICE

1. [Visão Geral](#1-visão-geral)
2. [Stack Técnica](#2-stack-técnica)
3. [Estrutura de Pastas](#3-estrutura-de-pastas)
4. [Rotas e Páginas](#4-rotas-e-páginas)
5. [Componentes Globais](#5-componentes-globais)
6. [Sistema de Build](#6-sistema-de-build)
7. [Artigos (Blog Técnico)](#7-artigos-blog-técnico)
8. [Projetos](#8-projetos)
9. [Deploy](#9-deploy)
10. [Roadmap / Próximos Passos](#10-roadmap--próximos-passos)
11. [O Que Nunca Sai do Local](#11-o-que-nunca-sai-do-local)

---

## 1. Visão Geral

Portfólio pessoal de **Vitor Hugo Arcanjo Dias Pereira**, desenvolvedor Python/Flask. O site serve como:

- **Vitrine profissional** — mostra quem é, o que faz, o que construiu
- **Prova técnica** — o próprio código segue o Padrão 2099
- **Blog técnico** — artigos sobre deploy, Flask, Nginx, SSL, etc
- **Documentação pública** — página `/arquitetura-2099` explica o padrão

**Objetivo:** captar recrutadores (CLT remoto) e clientes (freelance remoto).

---

## 2. Stack Técnica

| Camada | Tecnologia |
|--------|-----------|
| **Backend** | Flask + Python 3.12 |
| **Templates** | Jinja2 |
| **Frontend** | HTMX + JS vanilla modular |
| **CSS** | Puro, com design tokens (variáveis) |
| **Markdown** | Biblioteca `markdown` (para artigos) |
| **PDF** | Não usado no portfólio |
| **Build** | Scripts Python (`combine_*.py`) |
| **Deploy** | Git → VPS (Ubuntu 24.04) + systemd + Nginx |
| **Servidor** | Contabo VPS (167.86.116.215) |
| **SSL** | Let's Encrypt / Certbot |

---

## 3. Estrutura de Pastas

```
portfolio_2099/
│
├── app.py                                 # Entry point
├── requirements.txt
├── .env                                   # ⚠️ NUNCA no Git
├── .env.example
├── .gitignore
├── README.md
│
├── config/                                # ⚙️ Ciclo de vida
│   ├── __init__.py
│   └── imports_rotas.py                   # registrar_rotas(app)
│
├── rotas/                                 # 🚦 HTTP
│   ├── __init__.py
│   ├── pasta_home/
│   │   ├── __init__.py                    # bp_home
│   │   └── home.py                        # ini_home
│   ├── pasta_projetos/
│   │   ├── __init__.py                    # bp_projetos
│   │   └── projetos.py                    # PROJETOS + ini_projetos
│   ├── pasta_artigos/
│   │   ├── __init__.py                    # bp_artigos
│   │   └── artigos.py                     # ler .md + renderizar
│   └── pasta_arquitetura/
│       ├── __init__.py                    # bp_arquitetura
│       └── arquitetura.py                 # ini_arquitetura + playbook
│
├── templates/                             # 🎨 Jinja2
│   ├── tela_base_pos_login/
│   │   └── base.html.jinja                # Layout mestre
│   ├── components/
│   │   ├── navbar.html.jinja              # Menu global
│   │   └── footer.html.jinja              # Rodapé global
│   ├── pasta_home/
│   │   └── tela_home.html.jinja
│   ├── pasta_projetos/
│   │   ├── tela_projetos.html.jinja
│   │   └── partials/
│   │       └── _grid_projetos.html.jinja  # Grid com carrossel
│   ├── pasta_artigos/
│   │   ├── tela_artigos.html.jinja        # Lista
│   │   └── tela_artigo.html.jinja         # 1 artigo
│   └── pasta_arquitetura/
│       ├── tela_arquitetura.html.jinja
│       └── tela_playbook.html.jinja
│
├── static/                                # ⚡ Ativos
│   ├── css/
│   │   ├── core/
│   │   │   ├── variaveis.css              # Design tokens
│   │   │   ├── reset.css
│   │   │   └── responsive.css
│   │   ├── components/
│   │   │   ├── navbar.css
│   │   │   ├── footer.css
│   │   │   ├── buttons.css
│   │   │   └── cards.css
│   │   ├── modules/
│   │   │   ├── pasta_home/
│   │   │   │   └── home.min.css
│   │   │   ├── pasta_projetos/
│   │   │   │   └── projetos.min.css
│   │   │   ├── pasta_artigos/
│   │   │   │   └── artigos.min.css
│   │   │   └── pasta_arquitetura/
│   │   │       ├── arquitetura.min.css
│   │   │       └── playbook.min.css
│   │   └── global.min.css                 # Combinado de core+components
│   │
│   ├── js/
│   │   ├── core/
│   │   │   └── eventos.js                 # Helpers globais
│   │   ├── components/
│   │   │   ├── theme-toggle.js
│   │   │   └── menu-hamburger.js
│   │   ├── modules/
│   │   │   ├── pasta_home/
│   │   │   │   └── home.min.js            # scroll-spy
│   │   │   ├── pasta_projetos/
│   │   │   │   └── carrossel.min.js       # carrossel + modal
│   │   │   └── pasta_arquitetura/
│   │   │       └── arquitetura.min.js     # scroll-spy
│   │   └── global.min.js                  # Combinado de core+components
│   │
│   └── images/
│       ├── pasta_home/
│       │   └── home.png                   # Foto profissional
│       └── projetos/
│           ├── vhorganiza/
│           │   ├── 01-inicio.png
│           │   ├── 02-dashboard.png
│           │   ├── 03-financas.png
│           │   ├── 04-tarefas.png
│           │   ├── 05-orcamentos.png
│           │   └── 06-categorias.png
│           ├── safa/
│           │   ├── 01-consulta.png
│           │   ├── 02-crud-usuario.png
│           │   └── 03-pdf.png
│           ├── laudo-pericial/
│           │   ├── 01-tela-inicio.png
│           │   ├── 02-laudo-inicio.png
│           │   ├── 03-laudo-inicio-2.png
│           │   └── 04-word.png
│           ├── conectaprev/
│           │   ├── 01-inicio.png
│           │   ├── 02-login.png
│           │   ├── 03-painel-testes.png
│           │   └── 04-no-teste.png
│           └── meulinks/                  # (vazio por enquanto)
│
├── docs/
│   ├── privado/                           # ⚠️ NUNCA no Git
│   │   └── portfolio_FONTE.md             # Este arquivo
│   └── artigos/                           # ✅ Público (lido pelo Flask)
│       ├── deploy-flask-vps.md
│       ├── nginx-configuracao.md
│       ├── ssl-lets-encrypt.md
│       ├── git-comandos-essenciais.md
│       ├── gunicorn-gerenciamento.md
│       └── backup-restauracao.md
│
└── scripts/
    ├── combine_global.py                  # global.min.css + global.min.js
    ├── combine_static_home.py
    ├── combine_static_artigos.py
    ├── combine_static_projetos.py
    ├── combine_static_arquitetura.py
    └── combine_all.py                     # Roda todos
```

---

## 4. Rotas e Páginas

### Rotas principais

| URL | View | Descrição |
|-----|------|-----------|
| `/` | redirect | Redireciona pra `/inicio` |
| `/inicio` | `home.ini_home` | Home — hero, sobre, stack, projetos destaque, contato |
| `/projetos` | `projetos.ini_projetos` | Lista de projetos com carrossel |
| `/artigos` | `artigos.ini_artigos` | Lista de artigos |
| `/artigos/<slug>` | `artigos.ver_artigo` | 1 artigo específico |
| `/arquitetura-2099` | `arquitetura.ini_arquitetura` | Página do Padrão 2099 |
| `/arquitetura-2099/playbook` | `arquitetura.playbook` | Playbook completo |

### Estrutura de cada página

**Home** (`/inicio`):
- Hero (nome + tagline + CTA)
- Barra de âncoras sticky (Sobre / Stack / Projetos / Contato)
- Seção Sobre (com "o que eu trago")
- Seção Stack (agrupada em 4 cards)
- Seção Projetos em destaque (3 cards)
- Seção Contato (redes + info)
- Footer

**Projetos** (`/projetos`):
- Hero ("Meus projetos")
- Grid de 5 cards com carrossel de imagens
- Modal de imagem em tela cheia (clique na imagem)
- CTA final

**Artigos** (`/artigos`):
- Hero ("Artigos")
- Grid de cards com metadados (data, tempo leitura, tags)
- Clicar → `/artigos/<slug>`

**Arquitetura 2099** (`/arquitetura-2099`):
- Hero
- Âncoras fixas (Problema / Princípios / Árvore / Módulo / Por que funciona / Aprofundar)
- Seção O Problema (4 cards)
- Seção Princípios (20 em 4 grupos)
- Seção A Árvore (bloco de código)
- Seção Como um Módulo Funciona (4 sub-blocos)
- Seção Por que Funciona (3 cards)
- CTA final

**Playbook** (`/arquitetura-2099/playbook`):
- 12 seções de documentação técnica
- Voltar pra página principal

---

## 5. Componentes Globais

### `templates/components/navbar.html.jinja`

Menu fixo no topo, com:
- Logo textual (`VitorHugo`)
- Menu hamburger (mobile)
- 4 links: **Início**, **Projetos**, **Artigos**, **Arquitetura 2099**
- Botão de tema (claro/escuro)

**Estado ativo:** cada link ganha classe `.active` quando `request.endpoint` bate.

### `templates/components/footer.html.jinja`

Rodapé com:
- Copyright © 2026
- "Desenvolvido com ♥ por Vitor Hugo"
- Versão (v2.0.0)

### Tema claro/escuro

- Controlado por `data-theme` no `<html>`
- Persiste em `localStorage` (chave `theme`)
- Detecta preferência do sistema na 1ª visita

---

## 6. Sistema de Build

### Por que existe

Sem build, cada página carrega **8+ arquivos CSS** e **3+ JS**. Com build, carrega **2 CSS** e **1-2 JS**.

### Como funciona

Cada script Python **combina** (concatena) arquivos numa versão `.min.css` / `.min.js` que é carregada no template.

### Scripts

**`combine_global.py`** — gera `global.min.css` + `global.min.js`:
- **CSS:** `variaveis`, `reset`, `responsive`, `navbar`, `footer`, `buttons`, `cards`
- **JS:** `eventos`, `theme-toggle`, `menu-hamburger`
- Carregado **em todas as páginas** (via `base.html.jinja`)

**`combine_static_home.py`** — gera `home.min.css` + `home.min.js`:
- **CSS:** `home.css` (todos os estilos da home)
- **JS:** `scroll-spy.js`

**`combine_static_projetos.py`** — gera `projetos.min.css` + `carrossel.min.js`:
- **CSS:** `projetos.css`
- **JS:** `carrossel.js` + `modal.js`

**`combine_static_artigos.py`** — gera `artigos.min.css`

**`combine_static_arquitetura.py`** — gera `arquitetura.min.css` + `playbook.min.css` + `arquitetura.min.js`

**`combine_all.py`** — roda todos os módulos de uma vez.

### Como rodar

```bash
python scripts/combine_all.py
```

**Sempre que editar CSS/JS**, rodar o build e recarregar a página.

### Padrão de carregamento

**`base.html.jinja`** carrega global:
```jinja
<link rel="stylesheet" href="{{ url_for('static', filename='css/global.min.css') }}">
<script src="{{ url_for('static', filename='js/global.min.js') }}" defer></script>
```

Cada página carrega o seu (via `css_extra` e `js_extra`):
```jinja
{% block css_extra %}
<link rel="stylesheet" href="{{ url_for('static', filename='css/modules/pasta_home/home.min.css') }}">
{% endblock %}
```

---

## 7. Artigos (Blog Técnico)

### Como funciona

Os artigos são arquivos `.md` na pasta `docs/artigos/`. O Flask lê esses arquivos, faz **parse do frontmatter** (cabeçalho `---`) e renderiza o corpo em HTML via biblioteca `markdown`.

### Frontmatter

Cada `.md` começa com:

```yaml
---
titulo: "Título do artigo"
slug: "url-amigavel"
resumo: "Resumo curto que aparece no card."
data: "2026-10-15"
tags: ["tag1", "tag2"]
tempo_leitura: 8
---
```

### Formato da data

- **No `.md`:** formato ISO (`2026-10-15`)
- **Renderizado:** formato PT-BR (`15 de outubro de 2026`)
- **Conversão:** função `formatar_data()` em `artigos.py`

### Artigos publicados

1. `deploy-flask-vps.md` — Deploy Flask em VPS
2. `nginx-configuracao.md` — Nginx para Flask
3. `ssl-lets-encrypt.md` — SSL gratuito
4. `git-comandos-essenciais.md` — Git/GitHub
5. `gunicorn-gerenciamento.md` — Gunicorn
6. `backup-restauracao.md` — Backup

### Como adicionar novo artigo

1. Cria arquivo `.md` em `docs/artigos/`
2. Adiciona frontmatter no topo
3. Escreve conteúdo em Markdown
4. Pronto — aparece automaticamente na lista

### Segurança

- **Filtra arquivos sem `titulo`** no frontmatter (evita "Sem título" na lista)
- **Não executa código** dos `.md` — só converte Markdown pra HTML
- **Não expõe caminho absoluto** — Flask lê relativo

---

## 8. Projetos

### Estrutura de dados

Cada projeto é um dict em `rotas/pasta_projetos/projetos.py`:

```python
{
    'slug': 'vhorganiza',
    'nome': 'VHORGANIZA',
    'descricao': 'Texto longo...',
    'tech': ['Flask', 'PostgreSQL', 'HTMX', 'Jinja2', 'SQL'],
    'badge': 'Em produção',
    'badge_tipo': 'producao',
    'link': 'https://vhorganiza.com.br',
    'link_texto': 'Acessar',
    'ano': '2025',
    'categoria': 'Sistema Web',
    'imagens': [
        {'src': 'images/projetos/vhorganiza/01-inicio.png', 'alt': '...'},
        # ...
    ],
}
```

### Badges disponíveis

| Tipo | Cor | Uso |
|------|-----|-----|
| `producao` | Verde | Sistema em produção |
| `dev` | Amarelo | Em desenvolvimento |
| `cliente` | Azul | Cliente privado |
| `arquivado` | Cinza | Projeto encerrado |

### Projetos atuais

1. **VHORGANIZA** — Tarefas + finanças + orçamentos (em produção)
2. **SAFA** — Consultas ambientais + trabalhistas (em produção)
3. **Laudo Pericial** — Sistema forense (cliente privado)
4. **ConectaPrev** — Saúde digital (arquivado)
5. **MeuLinks** — Linktree multi-usuário (em dev, sem imagens)

### Carrossel + modal

- Cada card tem carrossel com setas ← → e dots
- Clica na imagem ativa → abre **modal em tela cheia**
- Modal: setas navegam, ESC fecha, clica fora fecha
- Meulinks sem imagens → sem carrossel

### Como adicionar imagens a um projeto

1. Coloca os `.png` em `static/images/projetos/<slug>/`
2. Nomeia como `01-nome.png`, `02-nome.png`, etc
3. Adiciona na lista `imagens` do dict
4. Roda build + restart

---

## 9. Deploy

### Repositório

- **GitHub:** https://github.com/vitorhugoarcanjo/arcode
- **Branch:** `main`

### Servidor

- **VPS:** Contabo (167.86.116.215)
- **SO:** Ubuntu 24.04
- **Domínio:** vitorhugoadp.com.br
- **Web server:** Nginx
- **WSGI:** Gunicorn (systemd service `vitorhugoadp`)
- **Socket:** `/var/www/vitorhugoadp/vitorhugoadp.sock`

### Fluxo de deploy

**No PC local:**

```bash
python scripts/combine_all.py
git add .
git commit -m "Descrição"
git push origin main
```

**No servidor (SSH):**

```bash
cd /var/www/vitorhugoadp
git pull origin main
sudo -u www-data venv/bin/pip install -r requirements.txt    # se mudou deps
sudo systemctl restart vitorhugoadp
```

**Testar:**

```bash
curl -I https://vitorhugoadp.com.br
```

### Se der erro

**Ver status do serviço:**

```bash
sudo systemctl status vitorhugoadp
```

**Ver logs:**

```bash
sudo journalctl -u vitorhugoadp -n 50 --no-pager
```

**Erro comum — falta lib:**

Se aparecer `ModuleNotFoundError`, rodar:

```bash
cd /var/www/vitorhugoadp
sudo -u www-data venv/bin/pip install -r requirements.txt
sudo systemctl restart vitorhugoadp
```

**Erro de permissão do Git:**

```bash
git config --global --add safe.directory /var/www/vitorhugoadp
```

---

## 10. Roadmap / Próximos Passos

### Feito

- ✅ Estrutura 2099 aplicada
- ✅ Home refinada
- ✅ Navbar sem Sobre/Contato
- ✅ Barra de âncoras sticky
- ✅ Página `/projetos` com 5 projetos
- ✅ Carrossel + modal de imagens
- ✅ 6 artigos técnicos
- ✅ Página `/arquitetura-2099`
- ✅ Playbook em 12 seções
- ✅ Tema claro/escuro
- ✅ Foto profissional real
- ✅ Deploy no ar

### Pendente

- ⏳ **Imagens do Meulinks** (quando o sistema estiver pronto)
- ⏳ **Instagram profissional** (criar conta + primeiro post)
- ⏳ **Currículo refinado** (1 página)
- ⏳ **LinkedIn atualizado** (link do portfólio)
- ⏳ **Meulinks completo** (admin + CRUD multi-usuário)
- ⏳ **Página de detalhe de projeto** (`/projetos/<slug>`) — fase 2

### Não-essencial

- 🔵 **Bug do Instagram in-app browser** — CSS quebra, mas funciona no Chrome. **Ignorar.**
- 🔵 **Testes automatizados** (pytest)
- 🔵 **Logs estruturados**
- 🔵 **Docker Compose**

---

## 11. O Que Nunca Sai do Local

### ✅ Pode ir pro público (portfólio/GitHub)

- Código do portfólio
- Artigos técnicos
- Descrições genéricas de projeto
- Padrão 2099 (documentação pública)

### ❌ NUNCA pode ir

- `.env` com senhas (`SECRET_KEY`, etc)
- `docs/privado/` (este MD)
- IP do servidor em artigos públicos
- Nome de cliente (usar "Cliente" genérico)
- Dados sensíveis de cliente (Laudo Pericial)
- Credenciais SSH

### Regra de ouro

**No público, trata como open-source. No local, é o teu manual.**

---

## 📥 COMO USAR ESTE MD

1. Salva em `docs/privado/portfolio_FONTE.md`
2. Mantém atualizado quando fizer mudanças grandes
3. Se um dia trocar de IA ou dev, esse arquivo ensina tudo
4. **NUNCA commitar** (garantir que `docs/privado/` tá no `.gitignore`)

---

**Fim do documento.**