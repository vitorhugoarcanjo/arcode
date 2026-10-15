---
titulo: "Git e GitHub: comandos essenciais para deploy em VPS"
slug: "git-comandos-essenciais"
resumo: "Os comandos de Git que eu mais uso no dia a dia pra gerenciar projetos em servidor: clonar, atualizar, resolver conflito e desfazer erro."
data: "2026-10-15"
tags: ["git", "github", "deploy", "vps", "versionamento"]
tempo_leitura: 7
---

# Git e GitHub: comandos essenciais

Quando você trabalha com deploy em VPS, o Git deixa de ser só "aquela
ferramenta que salva o código" e passa a ser o **canal oficial** entre a sua
máquina e o servidor. Esse artigo é o conjunto de comandos que eu uso toda semana.

## Conceitos rápidos

- **Git:** sistema de controle de versão que registra todo histórico do código
- **GitHub:** plataforma online que hospeda repositórios Git (tipo um "Dropbox pra código")
- **Repositório (repo):** a pasta do projeto versionada
- **Commit:** um "ponto de salvamento" com uma mensagem
- **Branch:** uma linha paralela de desenvolvimento

## Clonar um repositório

Baixa o código do GitHub pra máquina local ou pro servidor:

```bash
cd /var/www
git clone https://github.com/seu-usuario/seu-repositorio.git nome-do-site
cd nome-do-site
```

**Explicação:**

- `git clone` — baixa o repositório
- `https://github.com/...` — URL do repo
- `nome-do-site` — nome da pasta local (opcional)

## Atualizar código (pull)

Baixa as últimas alterações do GitHub:

```bash
cd /var/www/nome-do-site
git pull origin main
```

**Explicação:**

- `git pull` — baixa as alterações
- `origin` — nome padrão do repo remoto
- `main` — branch principal

> **Atenção:** se você fez alterações locais, pode dar conflito.
> Use `git status` antes.

## Verificar status

Mostra quais arquivos foram alterados:

```bash
git status
```

**O que cada cor significa:**

- 🟢 Verde — arquivos prontos pra commit
- 🔴 Vermelho — arquivos modificados mas não adicionados
- 🔵 Azul — branch atual e diferenças com o remoto

## Enviar código (commit + push)

```bash
# Adicionar arquivos
git add .

# Criar commit com mensagem
git commit -m "Descrição das alterações"

# Enviar pro GitHub
git push origin main
```

> **Dica:** a mensagem deve ser clara.
> Ex: `"Corrige bug no login"` ou `"Adiciona relatório mensal"`.

## Resolver conflitos

Quando duas pessoas (ou duas máquinas) mexem no mesmo arquivo:

```bash
# 1. Puxar alterações
git pull origin main

# 2. Resolver conflitos manualmente nos arquivos
# Os conflitos aparecem assim:
# <<<<<<< HEAD
# seu código
# =======
# código do GitHub
# >>>>>>> 123abc

# 3. Finalizar
git add .
git commit -m "Resolve conflitos"
git push origin main
```

## Trabalhar com branches

Branches são "ramificações" úteis pra testar novas funcionalidades sem mexer na main:

```bash
# Ver branches
git branch

# Criar e mudar pra nova branch
git checkout -b nova-funcionalidade

# Voltar pra main
git checkout main

# Enviar branch pro GitHub
git push origin nova-funcionalidade
```

## Desfazer alterações

### Desfazer alterações locais (não commitadas)

```bash
# Um arquivo específico
git checkout -- app.py

# Todos os arquivos
git checkout -- .
```

### Desfazer o último commit (mantém alterações)

```bash
git reset --soft HEAD~1
```

### Desfazer o último commit (remove alterações)

```bash
git reset --hard HEAD~1
```

> **Cuidado:** `git reset --hard` remove permanentemente. Use só se tiver certeza.

## Ver histórico

```bash
# Últimos commits
git log

# Forma resumida
git log --oneline

# Últimos 5
git log -5
```

## Fluxo completo de atualização do site

Esse é o passo a passo que eu uso toda vez que subo mudança pro servidor:

```bash
cd /var/www/nome-do-site
git pull origin main
sudo -u www-data venv/bin/pip install -r requirements.txt
sudo pkill -f "nome-do-site.*gunicorn"
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app \
    --daemon
curl -I https://seudominio.com.br
```

**Passo a passo:**

1. Baixa as mudanças
2. Atualiza dependências (se mudou `requirements.txt`)
3. Reinicia o Gunicorn (aplica o novo código)
4. Testa se o site tá no ar

## Comandos úteis

| Comando | O que faz |
|---------|-----------|
| `git fetch --all` | Baixa informações sem aplicar |
| `git reset --hard origin/main` | Força local igual ao remoto |
| `git stash` | Guarda alterações temporariamente |
| `git stash pop` | Recupera alterações guardadas |
| `git remote -v` | Mostra URL do repo remoto |
| `git branch -d nome` | Remove branch local |
| `git push origin --delete nome` | Remove branch remota |

## Problemas comuns

- **`fatal: not a git repository`** → você não está na pasta correta
- **`Permission denied (publickey)`** → use HTTPS em vez de SSH, ou configure chave SSH
- **`refusing to merge unrelated histories`** → `git pull origin main --allow-unrelated-histories`
- **`Your local changes would be overwritten`** → `git stash` antes do pull
- **`failed to push some refs`** → faça `git pull` primeiro

## Dicas

- Sempre faça `git status` antes de qualquer operação
- Mensagens de commit claras ajudam muito
- Nunca faça deploy sem testar localmente
- Mantenha um `.gitignore` cobrindo `venv/`, `__pycache__/`, `.env`
- O arquivo `.env` **NUNCA** deve ir pro Git
- Após `pull`, reinicie o Gunicorn

Se ficou dúvida, me chama no WhatsApp.