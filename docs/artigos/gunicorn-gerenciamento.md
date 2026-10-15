---
titulo: "Gunicorn: como gerenciar sua aplicação Flask em produção"
slug: "gunicorn-gerenciamento"
resumo: "Comandos essenciais pra iniciar, parar, reiniciar e monitorar o Gunicorn rodando aplicações Flask em VPS com Nginx."
data: "2026-10-15"
tags: ["gunicorn", "flask", "vps", "deploy", "wsgi"]
tempo_leitura: 7
---

# Gunicorn: como gerenciar sua aplicação Flask

Gunicorn é o **servidor WSGI** que roda sua aplicação Flask de verdade em produção.
O Nginx fica na frente recebendo requisições, mas quem executa o código Python
é o Gunicorn.

## Estrutura padrão do comando

```bash
/var/www/nome-do-site/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app \
    --daemon
```

**Parâmetros:**

| Parâmetro | O que faz |
|-----------|-----------|
| `--workers 3` | Quantos processos paralelos |
| `--bind unix:...sock` | Socket Unix (mais rápido que TCP) |
| `app:app` | Arquivo `app.py` com variável `app` (Flask) |
| `--daemon` | Roda em background |

## Iniciar um site

**Flask:**

```bash
cd /var/www/nome-do-site
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app \
    --daemon
```

**Django:**

```bash
cd /var/www/nome-do-site
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    seu_projeto.wsgi:application \
    --daemon
```

## Parar um site

```bash
# Parar site específico
sudo pkill -f "nome-do-site.*gunicorn"

# Parar todos os sites
sudo pkill -f gunicorn

# Forçar parada (se não parar normalmente)
sudo pkill -9 -f "nome-do-site.*gunicorn"
```

> **Atenção:** o `-9` força a parada imediata. Use só se o normal não funcionar.

## Reiniciar um site

Quando você atualiza o código, precisa reiniciar o Gunicorn:

```bash
# 1. Parar
sudo pkill -f "nome-do-site.*gunicorn"

# 2. Aguardar 2 segundos
sleep 2

# 3. Iniciar de novo
cd /var/www/nome-do-site
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app \
    --daemon

# 4. Verificar
ps aux | grep nome-do-site | grep -v grep
```

## Configuração de workers

A quantidade ideal depende do servidor (CPU + RAM):

```bash
# Regra geral: workers = (2 × CPUs) + 1
# Exemplo: 2 CPUs = 5 workers

# Servidor pequeno (1-2 GB RAM)
--workers 3

# Servidor médio (4 GB RAM)
--workers 5

# Servidor grande (8+ GB RAM)
--workers 7-9
```

> **Dica:** workers demais consomem RAM. Workers de menos deixam o site lento.
> Comece com 3 e ajuste conforme necessidade.

## Verificar se está rodando

```bash
# Ver processos
ps aux | grep gunicorn | grep -v grep

# Verificar socket
ls -la /var/www/nome-do-site/nome-do-site.sock

# Testar comunicação direta com o socket
curl --unix-socket /var/www/nome-do-site/nome-do-site.sock http://localhost/

# Testar via Nginx
curl -I http://seudominio.com.br
curl -I https://seudominio.com.br
```

## Inicialização automática (reboot)

Pra o Gunicorn subir sozinho quando o servidor reiniciar:

```bash
sudo crontab -e
```

Adicione:

```
@reboot sleep 30 && cd /var/www/nome-do-site && sudo -u www-data venv/bin/gunicorn --workers 3 --bind unix:/var/www/nome-do-site/nome-do-site.sock app:app --daemon
```

**Para múltiplos sites**, adicione uma linha por site com `sleep` diferente:

```
@reboot sleep 30 && cd /var/www/site1 && ...
@reboot sleep 45 && cd /var/www/site2 && ...
@reboot sleep 60 && cd /var/www/site3 && ...
```

## Erros comuns

### No such file or directory (gunicorn)

Gunicorn não está instalado no venv:

```bash
sudo -u www-data /var/www/nome-do-site/venv/bin/pip install gunicorn
```

### Address already in use

Socket já existe (outro processo rodando):

```bash
sudo pkill -f "nome-do-site.*gunicorn"
sudo rm -f /var/www/nome-do-site/nome-do-site.sock
# Iniciar novamente
```

### Permission denied (socket)

Permissão errada:

```bash
sudo chown -R www-data:www-data /var/www/nome-do-site
sudo chmod -R 755 /var/www/nome-do-site
```

### ImportError: No module named 'app'

Nome do arquivo ou variável incorreto:

```bash
# Ver o arquivo principal
ls -la /var/www/nome-do-site/*.py

# Para Flask: app:app (arquivo app.py com variável app)
# Para Django: meusite.wsgi:application
```

### Worker timeout (site lento)

Worker demorou mais que o limite:

```bash
gunicorn --workers 3 --timeout 300 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app --daemon
```

### 502 Bad Gateway (Nginx)

Nginx não consegue falar com Gunicorn:

```bash
# Verificar se está rodando
ps aux | grep nome-do-site

# Verificar socket
ls -la /var/www/nome-do-site/nome-do-site.sock
```

## Estrutura de arquivos

```
/var/www/nome-do-site/
├── nome-do-site.sock     # Socket criado automaticamente
├── app.py                # Seu código Flask
├── venv/                 # Ambiente virtual
│   └── bin/gunicorn      # Executável do Gunicorn
└── static/               # Arquivos estáticos
```

## Boas práticas

- Sempre rode o Gunicorn como usuário `www-data`
- Use sockets Unix em vez de portas TCP (mais rápido)
- Após atualizar código, sempre reinicie o Gunicorn
- Configure workers baseado na RAM (monitore com `htop`)
- Mantenha o timeout alto (300s) pra queries SQL demoradas
- Sempre verifique os logs do Nginx depois de reiniciar

Se ficou dúvida, me chama no WhatsApp.