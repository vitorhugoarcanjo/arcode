---
titulo: "Backup e restauração de sites Flask: guia completo"
slug: "backup-restauracao"
resumo: "Como fazer backup dos seus sites Python, do banco de dados e restaurar tudo quando der problema. Inclui automação via crontab."
data: "2026-10-15"
tags: ["backup", "deploy", "vps", "crontab", "flask"]
tempo_leitura: 9
---

# Backup e restauração de sites Flask

Se você já perdeu dados por não ter backup, sabe o desespero. Se nunca perdeu,
uma hora vai perder. Esse guia é o processo que eu uso pra **nunca ficar na mão**.

## O que precisa ser salvo

Em um site Python (Flask/Django), você precisa salvar:

- **Código fonte** — pasta inteira do site: `/var/www/meusite/`
- **Banco de dados** — se for SQLite, o arquivo `.db`
- **Arquivos de mídia** — uploads de usuários: `media/`
- **`.env`** — variáveis de ambiente (senhas, chaves)

> **⚠️ Importante:** NÃO faça backup da pasta `venv/`.
> Ela pode ser recriada facilmente e ocupa muito espaço.

## Backup do site completo

Backup de um site específico (excluindo `venv`):

```bash
cd /var/www
tar -czf /backup/meusite_$(date +%Y%m%d_%H%M%S).tar.gz \
    --exclude=meusite/venv \
    --exclude=meusite/__pycache__ \
    meusite/
```

Backup só do código (sem arquivos grandes):

```bash
cd /var/www
tar -czf /backup/meusite_code_$(date +%Y%m%d).tar.gz \
    --exclude=meusite/venv \
    --exclude=meusite/__pycache__ \
    --exclude=meusite/static \
    --exclude=meusite/media \
    meusite/
```

Backup completo de TODOS os sites:

```bash
sudo tar -czf /backup/todos_sites_$(date +%Y%m%d).tar.gz \
    --exclude=*/venv \
    --exclude=*/__pycache__ \
    /var/www/
```

**Explicação:**

- `tar -czf` — cria arquivo compactado (`.tar.gz`)
- `$(date +%Y%m%d_%H%M%S)` — adiciona data e hora no nome
- `--exclude` — exclui pastas desnecessárias

## Backup do banco de dados

### SQLite

```bash
# Cópia simples
cp /var/www/meusite/banco_de_dados.db /backup/banco_$(date +%Y%m%d).db

# Com compactação
tar -czf /backup/banco_$(date +%Y%m%d).tar.gz \
    /var/www/meusite/banco_de_dados.db
```

### PostgreSQL

```bash
# Backup
sudo -u postgres pg_dump nome_do_banco > /backup/banco_$(date +%Y%m%d).sql

# Comprimir
gzip /backup/banco_$(date +%Y%m%d).sql
```

### MySQL / MariaDB

```bash
mysqldump -u usuario -p nome_banco > /backup/banco_$(date +%Y%m%d).sql
```

## Restaurar backup

### Restaurar site completo

```bash
# 1. Parar o site
sudo pkill -f "meusite.*gunicorn"

# 2. Guardar estado atual (opcional)
mv /var/www/meusite /var/www/meusite_old

# 3. Extrair backup
cd /var/www
tar -xzf /backup/meusite_20260328.tar.gz

# 4. Ajustar permissões
sudo chown -R www-data:www-data /var/www/meusite
sudo chmod -R 755 /var/www/meusite

# 5. Recriar ambiente virtual (se necessário)
cd /var/www/meusite
sudo -u www-data python3 -m venv venv
sudo -u www-data venv/bin/pip install -r requirements.txt

# 6. Iniciar o site
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/meusite/meusite.sock \
    app:app --daemon
```

### Restaurar banco SQLite

```bash
# 1. Parar o site
sudo pkill -f "meusite.*gunicorn"

# 2. Restaurar o banco
cp /backup/banco_20260328.db /var/www/meusite/banco_de_dados.db

# 3. Ajustar permissão
sudo chown www-data:www-data /var/www/meusite/banco_de_dados.db

# 4. Reiniciar
cd /var/www/meusite
sudo -u www-data venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/var/www/meusite/meusite.sock \
    app:app --daemon
```

## Backup automático (crontab)

Pra fazer backup todo dia às 3 da manhã:

```bash
sudo crontab -e
```

Adicione:

```
# Backup diário dos sites às 3:00
0 3 * * * tar -czf /backup/todos_sites_$(date +\%Y\%m\%d).tar.gz --exclude=*/venv --exclude=*/__pycache__ /var/www/

# Backup diário do banco SQLite às 3:30
30 3 * * * cp /var/www/meusite/banco.db /backup/banco_$(date +\%Y\%m\%d).db

# Backup semanal completo (domingo às 4:00)
0 4 * * 0 tar -czf /backup/backup_completo_$(date +\%Y\%m\%d).tar.gz /var/www/ /etc/nginx/sites-available/ /etc/letsencrypt/
```

**Explicação do crontab:**

- `0 3 * * *` — minuto 0, hora 3, todo dia, todo mês, todo dia da semana
- `\%Y\%m\%d` — data no nome do arquivo (ano-mês-dia)
- `0 4 * * 0` — domingo às 4:00

## Limpar backups antigos

Backups acumulam. Remova os com mais de 30 dias:

```bash
find /backup -name "*.tar.gz" -mtime +30 -delete
find /backup -name "*.db" -mtime +30 -delete
find /backup -name "*.sql" -mtime +30 -delete
```

Automatize no crontab:

```
# Limpar backups antigos todo dia às 2:00
0 2 * * * find /backup -name "*.tar.gz" -mtime +30 -delete
0 2 * * * find /backup -name "*.db" -mtime +30 -delete
```

## Estrutura recomendada de backups

```
/backup/
├── sites/
│   ├── meusite_20260328.tar.gz
│   └── meusite_20260329.tar.gz
├── bancos/
│   ├── banco_20260328.db
│   └── banco_20260329.db
├── completo/
│   └── completo_20260328.tar.gz
└── logs/
    └── backup_20260328.log
```

## Backup fora do servidor (rclone)

Backup no mesmo servidor não protege contra falha do disco. Envie pra fora:

```bash
# Instalar rclone
curl https://rclone.org/install.sh | sudo bash

# Configurar (seguir instruções)
rclone config

# Enviar backup
rclone copy /backup/meusite.tar.gz gdrive:backups/
```

Funciona com Google Drive, Dropbox, S3, OneDrive, etc.

## Dicas importantes

- **Backup fora do servidor** — Google Drive, AWS S3, outro servidor
- **Teste seus backups** — periodicamente tente restaurar num ambiente de teste
- **Documente** — anote onde estão os backups e como restaurar
- **Mantenha camadas** — diários (7 dias), semanais (4 semanas), mensais (6 meses)
- **`.env` não esqueça** — backup separado (contém senhas)
- **Antes de atualizar** — sempre faça backup antes de mexer em código ou deps

## Resumo rápido

```bash
# Backup rápido de um site
tar -czf /backup/meusite_$(date +%Y%m%d).tar.gz \
    --exclude=meusite/venv \
    /var/www/meusite

# Listar backups
ls -la /backup/

# Restaurar
tar -xzf /backup/meusite_20260328.tar.gz -C /var/www/
```

Se ficou dúvida, me chama no WhatsApp.