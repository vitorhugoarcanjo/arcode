---
titulo: "SSL gratuito com Let's Encrypt: como configurar em Flask"
slug: "ssl-lets-encrypt"
resumo: "Passo a passo pra colocar HTTPS no seu site Flask usando Let's Encrypt e Certbot. Certificado gratuito, renovação automática e zero dor de cabeça."
data: "2026-10-15"
tags: ["ssl", "lets-encrypt", "https", "deploy", "flask"]
tempo_leitura: 6
---

# SSL gratuito com Let's Encrypt

HTTPS não é mais opcional. Navegador moderno marca site HTTP como "não seguro",
e o Google penaliza no ranking. Felizmente, o **Let's Encrypt** oferece SSL
gratuito com renovação automática.

## Pré-requisitos

- Domínio apontando pro IP do servidor
- DNS já propagado (teste com `dig`)
- Site acessível via HTTP (porta 80)
- Nginx configurado e rodando

## Instalar Certbot

```bash
sudo apt update
sudo apt install certbot python3-certbot-nginx -y

# Verificar
certbot --version
```

## Emitir certificado

Domínio único:

```bash
sudo certbot --nginx -d seudominio.com.br
```

Com www:

```bash
sudo certbot --nginx -d seudominio.com.br -d www.seudominio.com.br
```

O Certbot pergunta:

- **E-mail:** pra avisos de expiração
- **Termos:** `A`
- **Compartilhar e-mail:** `N` (recomendado)
- **Redirecionar HTTP → HTTPS:** `2` (recomendado)

Pronto. HTTPS configurado automaticamente.

## Renovação automática

Certificados do Let's Encrypt duram **90 dias**. O Certbot renova sozinho.

```bash
# Ver tarefa automática
sudo systemctl list-timers | grep certbot

# Testar renovação (não renova de verdade)
sudo certbot renew --dry-run

# Forçar renovação manual (se necessário)
sudo certbot renew
```

## Verificar certificados

```bash
# Listar todos
sudo certbot certificates

# Detalhes de 1
sudo certbot certificates --cert-name seudominio.com.br

# Ver expiração via OpenSSL
echo | openssl s_client -servername seudominio.com.br \
    -connect seudominio.com.br:443 2>/dev/null \
    | openssl x509 -noout -dates

# Testar HTTPS
curl -I https://seudominio.com.br
```

## Remover certificado

```bash
# Remover
sudo certbot delete --cert-name seudominio.com.br

# Revogar (se comprometido)
sudo certbot revoke --cert-path /etc/letsencrypt/live/seudominio.com.br/cert.pem
```

> **Atenção:** após remover o certificado, o Nginx pode parar de funcionar.
> Configure novamente para HTTP se necessário.

## Erros comuns

### DNS problem: NXDOMAIN

Domínio não aponta pro servidor. Verifique:

```bash
dig seudominio.com.br
```

Se não resolver, espere propagação (pode levar até 30 min).

### Too many failed authorizations

Rate limit do Let's Encrypt. Aguarde **1 hora** antes de tentar de novo.

### Certificate already exists

Já tem certificado pra esse domínio:

```bash
sudo certbot certificates
sudo certbot renew --force-renewal
```

### Could not bind to port 80

Porta 80 ocupada:

```bash
sudo lsof -i :80
```

## Estrutura dos arquivos

```
/etc/letsencrypt/live/seudominio.com.br/
├── fullchain.pem   # Certificado + cadeia
├── privkey.pem     # Chave privada
├── cert.pem        # Certificado
└── chain.pem       # Cadeia
```

## Dicas

- Configure DNS **antes** do Certbot
- Aguarde propagação (teste com `dig`)
- Faça `renew --dry-run` de vez em quando
- Guarde o e-mail usado (vai receber avisos)
- Se mudar de servidor, precisa emitir certificado novo

Quer saber mais? Me chama no WhatsApp.