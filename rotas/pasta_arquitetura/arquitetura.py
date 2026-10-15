"""Views da página de Arquitetura 2099."""

from flask import render_template, send_from_directory
from rotas.pasta_arquitetura import bp_arquitetura
import os


@bp_arquitetura.route('/')
def ini_arquitetura():
    """Renderiza a página de apresentação do Padrão 2099."""
    return render_template('pasta_arquitetura/tela_arquitetura.html.jinja')


@bp_arquitetura.route('/playbook')
def playbook():
    """Renderiza o playbook completo em HTML."""
    return render_template('pasta_arquitetura/tela_playbook.html.jinja')