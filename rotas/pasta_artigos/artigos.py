# rotas\pasta_artigos\artigos.py
"""Views do módulo Artigos — lê .md da pasta docs/artigos/."""

import os
import markdown
from flask import render_template, abort
from rotas.pasta_artigos import bp_artigos


# ==========================================================
# CONFIGURAÇÃO
# ==========================================================
ARTIGOS_DIR = os.path.join('docs', 'artigos')

# ==========================================================
# FORMATAR DATA
# ==========================================================
def formatar_data(data_iso):
    """Converte '2026-10-15' em '15 de outubro de 2026'."""
    if not data_iso or '-' not in data_iso:
        return data_iso

    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]

    try:
        ano, mes, dia = data_iso.split('-')
        mes_nome = meses[int(mes) - 1]
        return f"{int(dia)} de {mes_nome} de {ano}"
    except (ValueError, IndexError):
        return data_iso

# ==========================================================
# PARSE DO CABEÇALHO (frontmatter simples)
# ==========================================================
def parse_frontmatter(conteudo_md):
    """Extrai o cabeçalho YAML simples (---) do começo do .md."""
    if not conteudo_md.startswith('---'):
        return {}, conteudo_md

    partes = conteudo_md.split('---', 2)
    if len(partes) < 3:
        return {}, conteudo_md

    frontmatter = {}
    for linha in partes[1].strip().split('\n'):
        if ':' not in linha:
            continue
        chave, valor = linha.split(':', 1)
        chave = chave.strip()
        valor = valor.strip().strip('"').strip("'")

        # Tags: ["a", "b"] -> lista
        if valor.startswith('[') and valor.endswith(']'):
            valor = [
                v.strip().strip('"').strip("'")
                for v in valor[1:-1].split(',')
                if v.strip()
            ]

        frontmatter[chave] = valor

    return frontmatter, partes[2].strip()


# ==========================================================
# LISTAR ARTIGOS
# ==========================================================
def listar_artigos():
    """Lê todos os .md e retorna uma lista de metadados."""
    artigos = []

    if not os.path.isdir(ARTIGOS_DIR):
        return artigos

    for nome_arquivo in os.listdir(ARTIGOS_DIR):
        if not nome_arquivo.endswith('.md'):
            continue

        caminho = os.path.join(ARTIGOS_DIR, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        frontmatter, _ = parse_frontmatter(conteudo)

        # Pula arquivos sem título (evita "Sem título")
        titulo = frontmatter.get('titulo', '').strip()
        if not titulo:
            continue

        artigos.append({
            'slug': frontmatter.get('slug', nome_arquivo.replace('.md', '')),
            'titulo': titulo,
            'resumo': frontmatter.get('resumo', ''),
            'data': formatar_data(frontmatter.get('data', '')),
            'tags': frontmatter.get('tags', []),
            'tempo_leitura': frontmatter.get('tempo_leitura', 0),
        })

    # Ordena por data (mais recente primeiro)
    artigos.sort(key=lambda a: a['data'], reverse=True)
    return artigos


# ==========================================================
# BUSCAR 1 ARTIGO POR SLUG
# ==========================================================
def buscar_artigo(slug):
    """Lê 1 .md específico e retorna o conteúdo em HTML."""
    if not os.path.isdir(ARTIGOS_DIR):
        return None

    for nome_arquivo in os.listdir(ARTIGOS_DIR):
        if not nome_arquivo.endswith('.md'):
            continue

        caminho = os.path.join(ARTIGOS_DIR, nome_arquivo)
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()

        frontmatter, corpo_md = parse_frontmatter(conteudo)

        slug_arquivo = frontmatter.get('slug', nome_arquivo.replace('.md', ''))
        if slug_arquivo != slug:
            continue

        # Converte markdown -> HTML
        html = markdown.markdown(
            corpo_md,
            extensions=['fenced_code', 'tables', 'toc'],
        )

        return {
            'slug': slug,
            'titulo': frontmatter.get('titulo', 'Sem título'),
            'resumo': frontmatter.get('resumo', ''),
            'data': formatar_data(frontmatter.get('data', '')),
            'tags': frontmatter.get('tags', []),
            'tempo_leitura': frontmatter.get('tempo_leitura', 0),
            'conteudo_html': html,
        }

    return None


# ==========================================================
# VIEWS
# ==========================================================
@bp_artigos.route('/')
def ini_artigos():
    """Lista todos os artigos."""
    artigos = listar_artigos()
    return render_template(
        'pasta_artigos/tela_artigos.html.jinja',
        artigos=artigos,
    )


@bp_artigos.route('/<slug>')
def ver_artigo(slug):
    """Renderiza 1 artigo específico."""
    artigo = buscar_artigo(slug)
    if not artigo:
        abort(404)

    return render_template(
        'pasta_artigos/tela_artigo.html.jinja',
        artigo=artigo,
    )