"""View principal da Home."""

from flask import render_template
from rotas.pasta_home import bp_home


@bp_home.route('/inicio')
def ini_home():
    """Renderiza a página inicial do portfólio."""
    return render_template('pasta_home/tela_home.html.jinja')