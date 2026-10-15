"""
Build PROJETOS — Combina CSS do módulo.
Gera:
    static/css/modules/pasta_projetos/projetos.min.css

Uso:
    python scripts/combine_static_projetos.py
"""

import os
from datetime import datetime


CSS = [
    'static/css/modules/pasta_projetos/projetos.css',
]


def main():
    print('=' * 60)
    print('🏗️  BUILD PROJETOS — Portfólio 2099')
    print('=' * 60)

    output = 'static/css/modules/pasta_projetos/projetos.min.css'
    os.makedirs(os.path.dirname(output), exist_ok=True)

    print('\n📦 Combinando CSS...')
    with open(output, 'w', encoding='utf-8') as out:
        out.write(f'/* PROJETOS — {datetime.now().strftime("%d/%m/%Y %H:%M")} */\n\n')
        for file in CSS:
            if os.path.exists(file):
                nome = os.path.basename(file)
                out.write(f'/* ===== {nome} ===== */\n')
                with open(file, 'r', encoding='utf-8') as f:
                    out.write(f.read())
                    out.write('\n\n')
                print(f'  ✅ {nome}')
            else:
                print(f'  ⚠️  {file} não encontrado')

    print('\n' + '=' * 60)
    print('✅ PRONTO! Arquivo gerado:')
    print('   📄 static/css/modules/pasta_projetos/projetos.min.css')
    print('=' * 60)


if __name__ == '__main__':
    main()