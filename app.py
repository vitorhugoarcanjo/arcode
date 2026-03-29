import os
from flask import Flask, redirect, url_for
from dotenv import load_dotenv
from config.imports_blueprints import import_blueprints

if os.path.exists('.env'):
    load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
ENV = os.environ.get('FLASK_ENV', 'production')
app.config['DEBUG'] = ENV == 'development'

import_blueprints(app)

@app.route('/')
def ini_app():
    return redirect(url_for('inicio.ini_tela_principal'))

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
