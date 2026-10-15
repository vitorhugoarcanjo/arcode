---
titulo: "Nginx para Flask: configuração e comandos essenciais"
slug: "nginx-configuracao"
resumo: "Tudo que você precisa sobre Nginx quando trabalha com Flask em VPS: proxy reverso, ativar sites, ver logs e resolver os erros mais comuns."
data: "2026-10-15"
tags: ["nginx", "flask", "vps", "deploy"]
tempo_leitura: 8
---

# Nginx para Flask: guia essencial

Nginx é o servidor que fica **na frente** da sua aplicação Flask. Ele recebe
requisições HTTP/HTTPS, serve arquivos estáticos direto e passa o resto pro
Gunicorn (que roda o Flask de verdade).

## Por que não rodar o Flask direto?

Porque o servidor de desenvolvimento do Flask **não é feito pra produção**.
Ele não aguenta concorrência, não faz SSL e não serve estático de forma eficiente.

Nginx + Gunicorn é o combo padrão:

- **Nginx:** HTTPS, proxy, cache, arquivos estáticos
- **Gunicorn:** roda o Flask, gerencia workers

## Comandos básicos

```bash
# Testar configuração (sempre antes de recarregar!)
sudo nginx -t

# Recarregar config SEM downtime
sudo systemctl reload nginx

# Reiniciar (COM downtime)
sudo systemctl restart nginx

# Ver status
sudo systemctl status nginx

# Ver versão
nginx -v
```

> **Importante:** sempre rode `nginx -t` antes de `reload`.
> Se tiver erro de sintaxe, o Nginx para de funcionar.

## Configuração padrão de um site

Arquivo: `/etc/nginx/sites-available/nome-do-site`

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
        add_header Cache-Control "public, immutable";
    }
}
```

**Pontos importantes:**

- `server_name` — qual domínio esse site responde
- `proxy_pass` — pra onde mandar as requisições (o socket do Gunicorn)
- `proxy_read_timeout 300s` — aguarda até 5 min por resposta
- `location /static` — serve arquivos estáticos direto, sem passar pelo Flask

## Ativar / desativar sites

```bash
# Ativar
sudo ln -s /etc/nginx/sites-available/nome-do-site /etc/nginx/sites-enabled/

# Desativar
sudo unlink /etc/nginx/sites-enabled/nome-do-site

# Ver sites ativos
ls -la /etc/nginx/sites-enabled/

# Recarregar
sudo systemctl reload nginx
```

## Logs

```bash
# Erros (últimos 20)
sudo tail -20 /var/log/nginx/error.log

# Acompanhar em tempo real
sudo tail -f /var/log/nginx/error.log

# Acessos
sudo tail -20 /var/log/nginx/access.log
```

O log de erro é **essencial** pra debugar 502, 403 e afins.

## Erros comuns

### 502 Bad Gateway

Nginx não consegue falar com o Gunicorn. Provavelmente:

- Gunicorn não tá rodando
- Socket sumiu
- Permissão errada no socket

Verifique:

```bash
ps aux | grep gunicorn
ls -la /var/www/nome-do-site/nome-do-site.sock
```

### 403 Forbidden

Permissão errada nos arquivos:

```bash
sudo chown -R www-data:www-data /var/www/nome-do-site
sudo chmod -R 755 /var/www/nome-do-site
```

### nginx: [emerg] server_name directive is not allowed here

Erro de sintaxe no arquivo. Rode `sudo nginx -t` pra ver a linha exata.

## Dicas

- **Sempre** `nginx -t` antes de reload
- Um arquivo por site em `sites-available`
- Use nomes descritivos (`meusite.com.br`, não `site1`)
- Backup das configs antes de mexer
- Teste com `curl -I` depois de qualquer alteração

Se ficou dúvida, me chama no WhatsApp.