"""
Registro central de todos os blueprints da aplicação.
Seguindo o Padrão 2099: um único ponto de registro.
"""
from rotas.pasta_home import bp_home
from rotas.pasta_projetos import bp_projetos
from rotas.pasta_artigos import bp_artigos
from rotas.pasta_arquitetura import bp_arquitetura

def registrar_rotas(app):
    """Registra todos os blueprints da aplicação."""

    # Home
    app.register_blueprint(bp_home)

    # Projetos
    app.register_blueprint(bp_projetos, url_prefix='/projetos')

    # Artigos
    app.register_blueprint(bp_artigos, url_prefix='/artigos')

    # Arquitetura 2099
    app.register_blueprint(bp_arquitetura, url_prefix='/arquitetura-2099')