from rotas.pasta_manual.manuais_routes import bp_manuais_routes

def import_blueprints(app):
    app.register_blueprint(bp_manuais_routes, url_prefix="/manual")