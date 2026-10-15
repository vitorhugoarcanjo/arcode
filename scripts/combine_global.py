"""
Build GLOBAL — Combina CSS/JS compartilhados por TODAS as páginas.
Gera:
    static/css/global.min.css
    static/js/global.min.js

Uso:
    python scripts/combine_global.py
"""

import os
from datetime import datetime


# ==========================================================
# ARQUIVOS QUE TODA PÁGINA USA
# ==========================================================

CSS_FILES = [
    # CORE
    'static/css/core/variaveis.css',
    'static/css/core/reset.css',
    'static/css/core/responsive.css',

    # COMPONENTS
    'static/css/components/navbar.css',
    'static/css/components/footer.css',
    'static/css/components/buttons.css',
    'static/css/components/cards.css',
]

JS_FILES = [
    # CORE
    'static/js/core/eventos.js',

    # COMPONENTS
    'static/js/components/theme-toggle.js',
    'static/js/components/menu-hamburger.js',
]


# ==========================================================
# COMBINAR
# ==========================================================

def combinar_css():
    output = 'static/css/global.min.css'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando CSS global...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'/* GLOBAL — {datetime.now().strftime("%d/%m/%Y %H:%M")} */\n\n')
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
    output = 'static/js/global.min.js'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando JS global...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'// GLOBAL — {datetime.now().strftime("%d/%m/%Y %H:%M")}\n\n')
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
    print('🏗️  BUILD GLOBAL — Portfólio 2099')
    print('=' * 60)

    combinar_css()
    combinar_js()

    print('\n' + '=' * 60)
    print('✅ PRONTO! Arquivos gerados:')
    print('   📄 static/css/global.min.css')
    print('   📄 static/js/global.min.js')
    print('=' * 60)


if __name__ == '__main__':
    main()