"""Views do módulo Projetos — lista com carrossel + modal de imagens."""

from flask import render_template
from rotas.pasta_projetos import bp_projetos


# ==========================================================
# DADOS DOS PROJETOS
# ==========================================================
PROJETOS = [
    {
        'slug': 'vhorganiza',
        'nome': 'VHORGANIZA',
        'descricao': (
            'Sistema pessoal que centraliza tarefas, finanças, orçamentos e categorias '
            'em um único dashboard. Cada módulo tem CRUD completo, filtros por período '
            'e status, ordenação, auditoria transacional e interface reativa com HTMX. '
            'Categorias podem ser criadas direto nas telas de Tarefas e Finanças, sem sair do fluxo.'
        ),
        'tech': ['Flask', 'PostgreSQL', 'HTMX', 'Jinja2', 'SQL'],
        'badge': 'Em produção',
        'badge_tipo': 'producao',
        'link': 'https://vhorganiza.com.br',
        'link_texto': 'Acessar',
        'ano': '2025',
        'categoria': 'Sistema Web',
        'imagens': [
            {'src': 'images/projetos/vhorganiza/01-inicio.png', 'alt': 'Tela inicial do VHORGANIZA'},
            {'src': 'images/projetos/vhorganiza/02-dashboard.png', 'alt': 'Dashboard com indicadores'},
            {'src': 'images/projetos/vhorganiza/03-financas.png', 'alt': 'Módulo financeiro'},
            {'src': 'images/projetos/vhorganiza/04-tarefas.png', 'alt': 'Módulo de tarefas'},
            {'src': 'images/projetos/vhorganiza/05-orcamentos.png', 'alt': 'Módulo de orçamentos'},
            {'src': 'images/projetos/vhorganiza/06-categorias.png', 'alt': 'Categorias'},
        ],
    },
    {
        'slug': 'safa',
        'nome': 'SAFA',
        'descricao': (
            'Plataforma de consultas ambientais, trabalhistas e fundiárias. '
            'Módulos: Protocolo PRIMI, Programa Boi na Linha, Análise Ambiental de Imóvel Rural, '
            'Trabalho Escravo e Gestão CAR Automático. Consulta propriedades próximas e '
            'reprova CAR de origem quando há restrições. Gestão CAR envia relatórios por email '
            'em periodicidade configurável (semanal, quinzenal ou mensal). Auditoria completa de todas as operações.'
        ),
        'tech': ['Flask', 'SQLite', 'PDFKit', 'Jinja2'],
        'badge': 'Em produção',
        'badge_tipo': 'producao',
        'link': 'https://safapf.com.br',
        'link_texto': 'Acessar',
        'ano': '2024/2025',
        'categoria': 'Sistema Web',
        'imagens': [
            {'src': 'images/projetos/safa/01-consulta.png', 'alt': 'Tela de consulta do SAFA'},
            {'src': 'images/projetos/safa/02-crud-usuario.png', 'alt': 'CRUD de usuários'},
            {'src': 'images/projetos/safa/03-pdf.png', 'alt': 'Relatório em PDF gerado'},
        ],
    },
    {
        'slug': 'laudo-pericial',
        'nome': 'Laudo Pericial',
        'descricao': (
            'Sistema forense usado por peritos oficiais. Gera documentos com 90+ páginas: '
            'análise de vestígios, cálculos de velocidade, enquadramento legal automático, '
            'anexos fotográficos e assinatura eletrônica. Roda 100% offline por segurança dos dados.'
        ),
        'tech': ['Flask', 'SQLite', 'WeasyPrint', 'python-docx'],
        'badge': 'Cliente',
        'badge_tipo': 'cliente',
        'link': None,
        'link_texto': 'Projeto privado',
        'ano': '2026',
        'categoria': 'Sistema Forense',
        'imagens': [
            {'src': 'images/projetos/laudo-pericial/01-tela-inicio.png', 'alt': 'Tela inicial do sistema'},
            {'src': 'images/projetos/laudo-pericial/02-laudo-inicio.png', 'alt': 'Documento gerado — capa'},
            {'src': 'images/projetos/laudo-pericial/03-laudo-inicio-2.png', 'alt': 'Documento — estrutura'},
            {'src': 'images/projetos/laudo-pericial/04-word.png', 'alt': 'Editor Word integrado'},
        ],
    },
    {
        'slug': 'conectaprev',
        'nome': 'ConectaPrev',
        'descricao': (
            'Plataforma de rastreamento precoce de Parkinson e Alzheimer, '
            'desenvolvida como projeto de impacto social. '
            'Arquivado após a fase inicial — case de aprendizado em saúde digital.'
        ),
        'tech': ['Flask', 'SQLite', 'Jinja2'],
        'badge': 'Arquivado',
        'badge_tipo': 'arquivado',
        'link': None,
        'link_texto': 'Projeto encerrado',
        'ano': '2025',
        'categoria': 'Saúde Digital',
        'imagens': [
            {'src': 'images/projetos/conectaprev/01-inicio.png', 'alt': 'Tela inicial do ConectaPrev'},
            {'src': 'images/projetos/conectaprev/02-login.png', 'alt': 'Tela de login'},
            {'src': 'images/projetos/conectaprev/03-painel-testes.png', 'alt': 'Painel de testes'},
            {'src': 'images/projetos/conectaprev/04-no-teste.png', 'alt': 'Tela de teste em execução'},
        ],
    },
    {
        'slug': 'meulinks',
        'nome': 'MeuLinks',
        'descricao': (
            'Plataforma de linktree multi-usuário. Cada pessoa cria sua página de links '
            'e compartilha uma URL única. Em desenvolvimento, com admin e CRUD.'
        ),
        'tech': ['Flask', 'SQLite', 'HTMX'],
        'badge': 'Em desenvolvimento',
        'badge_tipo': 'dev',
        'link': 'https://meulinks.com.br',
        'link_texto': 'Ver demo',
        'ano': '2026',
        'categoria': 'SaaS',
        'imagens': [],
    },
]


# ==========================================================
# VIEWS
# ==========================================================
@bp_projetos.route('/')
def ini_projetos():
    """Lista todos os projetos."""
    return render_template(
        'pasta_projetos/tela_projetos.html.jinja',
        projetos=PROJETOS,
    )