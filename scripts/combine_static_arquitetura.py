"""
Build ARQUITETURA 2099 — Combina CSS/JS específicos do módulo.
Gera:
    static/css/modules/pasta_arquitetura/arquitetura.min.css
    static/css/modules/pasta_arquitetura/playbook.min.css
    static/js/modules/pasta_arquitetura/arquitetura.min.js

Uso:
    python scripts/combine_static_arquitetura.py
"""

import os
from datetime import datetime


CSS_ARQUITETURA = [
    'static/css/modules/pasta_arquitetura/arquitetura.css',
]

CSS_PLAYBOOK = [
    'static/css/modules/pasta_arquitetura/playbook.css',
]

JS_ARQUITETURA = [
    'static/js/modules/pasta_arquitetura/scroll-spy.js',
]


def combinar_css(arquivos, output, label):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print(f'\n📦 Combinando CSS — {label}...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'/* {label.upper()} — {datetime.now().strftime("%d/%m/%Y %H:%M")} */\n\n')
        for file in arquivos:
            if os.path.exists(file):
                nome = os.path.basename(file)
                out.write(f'/* ===== {nome} ===== */\n')
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
                    out.write('\n\n')
                print(f'  ✅ {nome}')
            else:
                print(f'  ⚠️  {file} não encontrado')


def combinar_js(arquivos, output, label):
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print(f'\n📦 Combinando JS — {label}...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'// {label.upper()} — {datetime.now().strftime("%d/%m/%Y %H:%M")}\n\n')
        for file in arquivos:
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
    print('🏗️  BUILD ARQUITETURA 2099 — Portfólio 2099')
    print('=' * 60)

    combinar_css(
        CSS_ARQUITETURA,
        'static/css/modules/pasta_arquitetura/arquitetura.min.css',
        'arquitetura'
    )

    combinar_css(
        CSS_PLAYBOOK,
        'static/css/modules/pasta_arquitetura/playbook.min.css',
        'playbook'
    )

    combinar_js(
        JS_ARQUITETURA,
        'static/js/modules/pasta_arquitetura/arquitetura.min.js',
        'arquitetura'
    )

    print('\n' + '=' * 60)
    print('✅ PRONTO! Arquivos gerados:')
    print('   📄 static/css/modules/pasta_arquitetura/arquitetura.min.css')
    print('   📄 static/css/modules/pasta_arquitetura/playbook.min.css')
    print('   📄 static/js/modules/pasta_arquitetura/arquitetura.min.js')
    print('=' * 60)


if __name__ == '__main__':
    main()