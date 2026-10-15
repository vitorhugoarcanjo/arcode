---
titulo: "Deploy Flask em VPS: guia completo com Nginx, Gunicorn e SSL"
slug: "deploy-flask-vps"
resumo: "Do zero ao ar: como subir uma aplicação Flask em VPS com Nginx como proxy reverso, Gunicorn como WSGI e SSL gratuito via Let's Encrypt."
data: "2026-10-15"
tags: ["deploy", "flask", "vps", "nginx", "gunicorn"]
tempo_leitura: 12
---

# Deploy Flask em VPS: guia completo

Quando comecei a fazer deploy das minhas aplicações Flask, perdi muito tempo
juntando pedaços de tutoriais diferentes. Esse artigo é o guia que **eu queria
ter lido** na primeira vez.

## O que você vai precisar

- Uma VPS com Ubuntu
- Um domínio apontando para o IP da VPS
- Código no GitHub (ou pronto pra enviar)
- Acesso SSH ao servidor

> **Dica:** se você ainda não tem domínio, dá pra testar via IP.
> Só não vai poder usar HTTPS (SSL exige domínio).

## Passo 1 — Clonar o repositório

SSH na VPS e clone o projeto:

```bash
cd /var/www
git clone https://github.com/seu-usuario/seu-repositorio.git nome-do-site
cd nome-do-site
```

O diretório `/var/www` é o padrão pra hospedar sites no Linux.

## Passo 2 — Criar ambiente virtual

Sempre use `venv` — nunca instale dependências globais.

```bash
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install -r requirements.txt
```

O usuário `www-data` é o padrão do Nginx no Ubuntu.

## Passo 3 — Configurar Nginx

Crie o arquivo de configuração:

```bash
sudo nano /etc/nginx/sites-available/nome-do-site
```

Cole a configuração (substitua `seudominio.com.br`):

```nginx
server {
    listen 80;
    listen [::]:80;
    server_name seudominio.com.br www.seudominio.com.br;

    location / {
        include proxy_params;
        proxy_pass http://unix:/var/www/nome-do-site/nome-do-site.sock;
        proxy_read_timeout 300s;
        send_timeout 300s;
    }

    location /static {
        alias /var/www/nome-do-site/static;
        expires 30d;
    }
}
```

Ative o site:

```bash
sudo ln -s /etc/nginx/sites-available/nome-do-site /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

> **Importante:** o `nginx -t` testa a configuração antes de aplicar.

## Passo 4 — Iniciar Gunicorn

Gunicorn é o servidor WSGI que roda sua aplicação Flask de verdade.

```bash
cd /var/www/nome-do-site
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/nome-do-site/nome-do-site.sock \
    app:app \
    --daemon
```

| Parâmetro | O que faz |
|-----------|-----------|
| `--workers 3` | Processos paralelos. Regra: `(2 × CPUs) + 1` |
| `--bind unix:...sock` | Socket Unix (mais rápido que TCP) |
| `app:app` | Arquivo `app.py` com variável `app` |
| `--daemon` | Roda em background |

## Passo 5 — Testar HTTP

```bash
curl -I http://seudominio.com.br
```

Se retornar `HTTP/1.1 200 OK` ou `302 FOUND`, tá no ar.

## Passo 6 — SSL gratuito com Certbot

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d seudominio.com.br -d www.seudominio.com.br
```

O Certbot pergunta:

- **E-mail:** pra avisos de expiração
- **Termos:** `A`
- **Compartilhar e-mail:** `N`
- **Redirecionar HTTP → HTTPS:** `2`

Depois disso, HTTPS tá funcionando.

## Passo 7 — Auto-start no reboot

```bash
sudo crontab -e
```

Adicione:

```
@reboot sleep 30 && cd /var/www/nome-do-site && sudo -u www-data venv/bin/gunicorn --workers 3 --bind unix:/var/www/nome-do-site/nome-do-site.sock app:app --daemon
```

## Passo 8 — Verificar

```bash
ps aux | grep gunicorn | grep -v grep
ls -la /var/www/nome-do-site/nome-do-site.sock
curl -I https://seudominio.com.br
```

## Erros comuns

### 502 Bad Gateway

Nginx não consegue falar com Gunicorn. Verifique:

```bash
ps aux | grep gunicorn
ls -la /var/www/nome-do-site/nome-do-site.sock
sudo tail -20 /var/log/nginx/error.log
```

### 403 Forbidden

Permissão errada:

```bash
sudo chown -R www-data:www-data /var/www/nome-do-site
sudo chmod -R 755 /var/www/nome-do-site
```

## Resumo

1. Clonar código
2. Criar venv + instalar deps
3. Configurar Nginx (HTTP)
4. Iniciar Gunicorn
5. Testar HTTP
6. Rodar Certbot (SSL)
7. Configurar auto-start
8. Verificar

Pronto, seu Flask tá em produção.