from flask import Blueprint, render_template, abort

bp_manuais_routes = Blueprint('manual', __name__)

@bp_manuais_routes.route('/<page>')
def ini_manual(page='index_manual'):
    """Página de manuais com menu lateral"""
    
    # Dicionário com todos os manuais
    manuais = {
        'index_manual': {
            'titulo': 'Início - Manuais',
            'arquivo': 'index_manual.html'
        },
        'deploy': {
            'titulo': 'Deploy de Site - Passo a Passo',
            'arquivo': 'deploy.html'
        },
        'github': {
            'titulo': 'GitHub - Comandos e Dicas',
            'arquivo': 'github.html'
        },
        'nginx': {
            'titulo': 'Nginx - Configuração e Comandos',
            'arquivo': 'nginx.html'
        },
        'ssl': {
            'titulo': 'SSL/Certbot - Certificados',
            'arquivo': 'ssl.html'
        },
        'gunicorn': {
            'titulo': 'Gunicorn - Gerenciamento',
            'arquivo': 'gunicorn.html'
        },
        'backup': {
            'titulo': 'Backup e Restauração',
            'arquivo': 'backup.html'
        }
    }
    
    # Se a página não existir, mostra 404
    if page not in manuais:
        abort(404)
    
    # Renderiza o template com o menu lateral
    return render_template('pasta_manual/base_manual.html',
        manuais=manuais,
        pagina_atual=page,
        titulo=manuais[page]['titulo']
    )