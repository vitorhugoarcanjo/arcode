"""
Build HOME — Combina CSS/JS específicos da home.
Gera:
    static/css/modules/pasta_home/home.min.css
    static/js/modules/pasta_home/home.min.js

Uso:
    python scripts/combine_static_home.py
"""

import os
from datetime import datetime


CSS_FILES = [
    'static/css/modules/pasta_home/home.css',
]

JS_FILES = [
    'static/js/modules/pasta_home/scroll-spy.js',
]


def combinar_css():
    output = 'static/css/modules/pasta_home/home.min.css'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando CSS da home...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'/* HOME — {datetime.now().strftime("%d/%m/%Y %H:%M")} */\n\n')
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
    output = 'static/js/modules/pasta_home/home.min.js'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando JS da home...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'// HOME — {datetime.now().strftime("%d/%m/%Y %H:%M")}\n\n')
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
    print('🏗️  BUILD HOME — Portfólio 2099')
    print('=' * 60)

    combinar_css()
    combinar_js()

    print('\n' + '=' * 60)
    print('✅ PRONTO! Arquivos gerados:')
    print('   📄 static/css/modules/pasta_home/home.min.css')
    print('   📄 static/js/modules/pasta_home/home.min.js')
    print('=' * 60)


if __name__ == '__main__':
    main()