from rotas.pasta_manual.manuais_routes import bp_manuais_routes
from rotas.tela_principal import bp_tela_principal

def import_blueprints(app):
    app.register_blueprint(bp_manuais_routes, url_prefix="/manual")
    app.register_blueprint(bp_tela_principal, url_prefix="/inicio")