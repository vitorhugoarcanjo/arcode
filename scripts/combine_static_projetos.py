"""
Build PROJETOS — Combina CSS/JS do módulo.
Gera:
    static/css/modules/pasta_projetos/projetos.min.css
    static/js/modules/pasta_projetos/carrossel.min.js
    static/js/modules/pasta_projetos/modal.min.js

Uso:
    python scripts/combine_static_projetos.py
"""

import os
from datetime import datetime


CSS_FILES = [
    'static/css/modules/pasta_projetos/projetos.css',
]

JS_FILES = [
    'static/js/modules/pasta_projetos/carrossel.js',
    'static/js/modules/pasta_projetos/modal.js',
]


def combinar_css():
    output = 'static/css/modules/pasta_projetos/projetos.min.css'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando CSS de projetos...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'/* PROJETOS — {datetime.now().strftime("%d/%m/%Y %H:%M")} */\n\n')
        for file in CSS_FILES:
            if os.path.exists(file):
                nome = os.path.basename(file)
                out.write(f'/* ===== {nome} ===== */\n')
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
                    out.write('\n\n')
                print(f'  ✅ {nome}')
            else:
                print(f'  ⚠️  {file} não encontrado')


def combinar_js():
    output = 'static/js/modules/pasta_projetos/carrossel.min.js'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando JS de projetos...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'// PROJETOS — {datetime.now().strftime("%d/%m/%Y %H:%M")}\n\n')
        for file in JS_FILES:
            if os.path.exists(file):
                nome = os.path.basename(file)
                out.write(f'// ==== {nome} ====\n')
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
                    out.write('\n\n')
                print(f'  ✅ {nome}')
            else:
                print(f'  ⚠️  {file} não encontrado')


def main():
    print('=' * 60)
    print('🏗️  BUILD PROJETOS — Portfólio 2099')
    print('=' * 60)

    combinar_css()
    combinar_js()

    print('\n' + '=' * 60)
    print('✅ PRONTO! Arquivos gerados:')
    print('   📄 static/css/modules/pasta_projetos/projetos.min.css')
    print('   📄 static/js/modules/pasta_projetos/carrossel.min.js')
    print('=' * 60)


if __name__ == '__main__':
    main()