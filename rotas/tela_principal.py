from flask import Blueprint, render_template

bp_tela_principal = Blueprint('inicio', __name__)

@bp_tela_principal.route('/')
def ini_tela_principal():
    return render_template('pasta_tela_principal/tela_principal.html')


@bp_tela_principal.route('/projetos')
def ini_tela_projetos():
    return render_template('pasta_tela_principal/projetos.html')

@bp_tela_principal.route('/menu_links')
def ini_menu_links():
    return render_template('pasta_menu_links/menu_links.html')