"""
Build MASTER — Roda todos os combine_static_* de uma vez.
Uso:
    python scripts/combine_all.py           # roda global + todos os módulos
    python scripts/combine_all.py home      # roda só a home
"""

import os
import sys
import subprocess
from datetime import datetime


# ==========================================================
# MÓDULOS QUE TÊM BUILD PRÓPRIO
# ==========================================================
MODULOS = [
    'home',
    'arquitetura',
    'artigos',
    'projetos',
    # quando criar os próximos, adiciona aqui:
]


def rodar_script(script_path):
    """Roda um script python e captura erros."""
    if not os.path.exists(script_path):
        print(f'  ⚠️  {script_path} não existe — pulando')
        return False

    try:
        subprocess.run([sys.executable, script_path], check=True)
        return True
    except subprocess.CalledProcessError as e:
        print(f'  ❌ Erro: {e}')
        return False


def main():
    print('=' * 60)
    print(f'🏗️  BUILD MASTER — {datetime.now().strftime("%d/%m/%Y %H:%M")}')
    print('=' * 60)

    sucessos = []
    falhas = []

    # 1. GLOBAL primeiro
    if len(sys.argv) == 1 or 'global' in sys.argv:
        print('\n📦 Rodando GLOBAL...')
        ok = rodar_script('scripts/combine_global.py')
        (sucessos if ok else falhas).append('global')

    # 2. Módulos específicos
    if len(sys.argv) > 1:
        modulos = [m for m in sys.argv[1:] if m != 'global']
    else:
        modulos = MODULOS

    for modulo in modulos:
        print(f'\n📦 Rodando módulo: {modulo}')
        ok = rodar_script(f'scripts/combine_static_{modulo}.py')
        (sucessos if ok else falhas).append(modulo)

    # 3. Resumo
    print('\n' + '=' * 60)
    print('📊 RESUMO FINAL')
    print('=' * 60)

    if sucessos:
        print(f'\n✅ Sucesso ({len(sucessos)}):')
        for m in sucessos:
            print(f'   • {m}')

    if falhas:
        print(f'\n❌ Falhas ({len(falhas)}):')
        for m in falhas:
            print(f'   • {m}')

    print('\n' + '=' * 60)
    if not falhas:
        print('✅ TUDO PRONTO!')
    else:
        print(f'⚠️  {len(falhas)} módulo(s) falharam.')
    print('=' * 60)

    sys.exit(1 if falhas else 0)


if __name__ == '__main__':
    main()