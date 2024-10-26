# Projeto Backend com FastAPI e PostgreSQL

Este projeto é uma API RESTful criada com **FastAPI** e **PostgreSQL**. O objetivo é fornecer um backend robusto que pode ser consumido por um frontend (por exemplo, um projeto Next.js).

## Sumário

- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Iniciando o Projeto](#iniciando-o-projeto)
- [Criando Migrações com Alembic](#criando-migrações-com-alembic)
- [Deploy em Produção](#deploy-em-produção)

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- **Python 3.8 ou superior**
- **PostgreSQL**
- **Git** (opcional, mas recomendado)

## Instalação

### 1. Clone o Repositório (se aplicável)

```bash
git clone https://github.com/seu-usuario/seu-projeto.git
cd seu-projeto/backend
```

### 2. Crie um Ambiente Virtual

- Windows
```bash
python -m venv venv
```

- macOS/Linux
```bash
python3 -m venv venv
```

### 3. Ative o Ambiente Virtual

- Windows
```bash
venv\Scripts\activate
```

- macOS/Linux
```bash
source venv/bin/activate
```

### 4. Instale as Dependências
```bash
pip install -r requirements.txt
```
Se você ainda não tem um arquivo requirements.txt, crie um com as dependências necessárias:

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary alembic
pip freeze > requirements.txt
```

## Iniciando o Projeto

### 1. Configure o Banco de Dados PostgreSQL

Certifique-se de que o PostgreSQL está instalado e em execução.

**Crie o Banco de Dados**
Abra o terminal ou prompt de comando e execute:

```bash
psql -U seu_usuario
```
No prompt do PostgreSQL:

```sql
CREATE DATABASE pefea WITH ENCODING 'UTF8';
\q
```
Nota: Substitua `seu_usuario` pelo seu nome de usuário do PostgreSQL.

### 2. Configure a URL do Banco de Dados

No arquivo `app/database.py`, verifique se a `DATABASE_URL` está correta:

```python
DATABASE_URL = "postgresql://seu_usuario:sua_senha@localhost:5432/pefea"
```
Substitua `seu_usuario` e `sua_senha` pelas credenciais do seu banco de dados.

### 3. Inicie o Servidor

No diretório raiz do backend, com o ambiente virtual ativado:

```bash
uvicorn app.main:app --reload
```
O servidor estará disponível em `http://127.0.0.1:8000`.

### 4. Teste a API

Acesse a documentação interativa em `http://127.0.0.1:8000/docs`.

## Criando Migrações com Alembic

O Alembic é usado para gerenciar as migrações do banco de dados.

### 1. Inicialize o Alembic
```bash
alembic init alembic
```

### 2. Configure o `alembic.ini`

No arquivo `alembic.ini`, defina a URL do banco de dados:

```ini
sqlalchemy.url = postgresql://seu_usuario:sua_senha@localhost:5432/pefea
```

### 3. Configure o `env.py`

No arquivo `alembic/env.py`, ajuste as importações:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import Base
target_metadata = Base.metadata
```

### 4. Importe os Modelos

No arquivo `app/models/__init__.py`, importe seus modelos:

```python
from app.models.exemplo import Example
# Importe outros modelos conforme necessário
```

### 5. Gerar e Aplicar Migrações

**Gerar uma Migração**
```bash
alembic revision --autogenerate -m "Inicial"
```

**Aplicar a Migração**
```bash
alembic upgrade head
```

### 6. Atualizar Migrações Após Modificações nos Modelos

Sempre que você alterar ou adicionar modelos:

```bash
alembic revision --autogenerate -m "Descrição das alterações"
alembic upgrade head
```

## Deploy em Produção

Para colocar o projeto em produção, siga os passos abaixo:

### 1. Configurar o Ambiente de Produção

- **Servidor**: Escolha um provedor de hospedagem (VPS, cloud, etc.).
- **Python**: Instale a versão adequada do Python no servidor.
- **Banco de Dados**: Configure o PostgreSQL no ambiente de produção. Você pode usar um serviço gerenciado ou instalar diretamente no servidor.

### 2. Configurar Variáveis de Ambiente

Em vez de armazenar credenciais no código, use variáveis de ambiente.

**Exemplo usando python-dotenv**

Instale o pacote:
```bash
pip install python-dotenv
```

Crie um arquivo `.env`:

```
DATABASE_URL=postgresql://usuario_producao:senha_producao@host_producao:5432/pefea
```

No `app/database.py`, ajuste:

```python
from dotenv import load_dotenv
import os

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
```

### 3. Instalar Dependências em Produção

No servidor de produção, crie e ative um ambiente virtual e instale as dependências:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Aplicar Migrações em Produção

No ambiente de produção, execute:

```bash
alembic upgrade head
```

Nota: As migrações geradas em desenvolvimento podem ser aplicadas em produção. Certifique-se de que o diretório `alembic/` e suas subpastas estejam incluídos no deploy.

### 5. Configurar um Servidor ASGI para Produção

Em vez de usar o Uvicorn diretamente, é recomendado usar um gerenciador de processos como o **Gunicorn** com Uvicorn Workers.

Instale o Gunicorn:
```bash
pip install gunicorn
```

Execute o servidor:
```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

### 6. Configurar um Servidor Web (opcional)

Para servir sua aplicação na porta 80 ou 443 (HTTPS), use um servidor web como **Nginx** como proxy reverso.

### 7. Segurança e Otimizações

- **SSL/TLS**: Configure certificados SSL para comunicação segura.
- **Firewall**: Proteja o servidor com regras de firewall apropriadas.
- **Escalabilidade**: Considere usar contêineres Docker e orquestração com Kubernetes para escalar sua aplicação.

## Resumo

- **Ambientes Virtuais**: Use ambientes virtuais para isolar as dependências.
- **Banco de Dados**: Configure o PostgreSQL e conecte-o à sua aplicação.
- **Migrações**: Use o Alembic para gerenciar mudanças no esquema do banco de dados.
- **Variáveis de Ambiente**: Proteja suas credenciais usando variáveis de ambiente.
- **Deploy**: Configure o ambiente de produção cuidadosamente, seguindo as melhores práticas de segurança.

## Contato

Se você tiver dúvidas ou precisar de assistência adicional, sinta-se à vontade para entrar em contato.
