"""
Portfólio Vitor Hugo — Padrão 2099
Entry point da aplicação Flask.
"""

import os
from flask import Flask, redirect, url_for
from dotenv import load_dotenv

# Carrega variáveis de ambiente (se existir .env)
if os.path.exists('.env'):
    load_dotenv()


def create_app():
    """Factory da aplicação Flask."""
    app = Flask(__name__)

    # Configurações
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-only-change-me')
    ENV = os.environ.get('FLASK_ENV', 'production')
    app.config['DEBUG'] = ENV == 'development'

    # Registra blueprints
    from config.imports_rotas import registrar_rotas
    registrar_rotas(app)

    # Rota raiz — redireciona pra home
    @app.route('/')
    def ini_app():
        return redirect(url_for('home.ini_home'))

    return app


app = create_app()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])