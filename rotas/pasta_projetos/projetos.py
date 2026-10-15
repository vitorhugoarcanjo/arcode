"""Views do módulo Projetos — lista + filtro por stack."""

from flask import render_template, request
from rotas.pasta_projetos import bp_projetos


# ==========================================================
# DADOS DOS PROJETOS
# ==========================================================
PROJETOS = [
    {
        'slug': 'vhorganiza',
        'nome': 'VHORGANIZA',
        'descricao': (
            'Sistema de gestão de tarefas e finanças pessoais. '
            'Backend Flask com PostgreSQL, autenticação de usuários, '
            'auditoria completa de ações e interface reativa com HTMX.'
        ),
        'tech': ['Flask', 'PostgreSQL', 'HTMX', 'Jinja2', 'SQL'],
        'badge': 'Em produção',
        'badge_tipo': 'producao',
        'link': 'https://vhorganiza.com.br',
        'link_texto': 'Acessar',
        'ano': '2025',
        'categoria': 'Sistema Web',
    },
    {
        'slug': 'safa',
        'nome': 'SAFA',
        'descricao': (
            'Sistema de consulta ambiental, florestal e documental. '
            'Centraliza consultas estaduais e federais em uma única plataforma '
            'e gera relatórios em PDF automaticamente.'
        ),
        'tech': ['Flask', 'SQLite', 'PDFKit', 'Jinja2'],
        'badge': 'Em produção',
        'badge_tipo': 'producao',
        'link': 'https://safapf.com.br',
        'link_texto': 'Acessar',
        'ano': '2024/2025',
        'categoria': 'Sistema Web',
    },
    {
        'slug': 'laudo-pericial',
        'nome': 'Laudo Pericial',
        'descricao': (
            'Sistema de emissão de laudos periciais de trânsito usado por peritos oficiais. '
            'Gera documentos forenses com 90+ páginas: análise de vestígios, cálculos de velocidade, '
            'enquadramento legal automático, anexos fotográficos e assinatura eletrônica. '
            'Roda 100% offline por segurança dos dados.'
        ),
        'tech': ['Flask', 'SQLite', 'WeasyPrint', 'python-docx'],
        'badge': 'Cliente',
        'badge_tipo': 'cliente',
        'link': None,
        'link_texto': 'Projeto privado',
        'ano': '2026',
        'categoria': 'Sistema Forense',
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
    },
    {
        'slug': 'meulinks',
        'nome': 'MeuLinks',
        'descricao': (
            'Plataforma de linktree multi-usuário. Cada pessoa cadastra seus links '
            'e compartilha uma única URL. Em desenvolvimento, com admin e CRUD.'
        ),
        'tech': ['Flask', 'SQLite', 'HTMX'],
        'badge': 'Em desenvolvimento',
        'badge_tipo': 'dev',
        'link': 'https://meulinks.com.br',
        'link_texto': 'Ver demo',
        'ano': '2026',
        'categoria': 'SaaS',
    },
]


# ==========================================================
# HELPERS
# ==========================================================
def _todas_as_stacks():
    """Retorna a lista única de todas as stacks usadas nos projetos."""
    stacks = set()
    for p in PROJETOS:
        stacks.update(p['tech'])
    return sorted(stacks)


def _filtrar_projetos(stack=None):
    """Filtra projetos por stack (ou retorna todos)."""
    if not stack or stack == 'todas':
        return PROJETOS
    return [p for p in PROJETOS if stack in p['tech']]


# ==========================================================
# VIEWS
# ==========================================================
@bp_projetos.route('/')
def ini_projetos():
    """Lista todos os projetos."""
    stack_ativa = request.args.get('stack', 'todas')

    return render_template(
        'pasta_projetos/tela_projetos.html.jinja',
        projetos=_filtrar_projetos(stack_ativa),
        stacks=_todas_as_stacks(),
        stack_ativa=stack_ativa,
    )