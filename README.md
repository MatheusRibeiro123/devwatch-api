# 🧭 DevWatch

API de monitoramento de sistema desenvolvida com **FastAPI**, com foco em coleta, armazenamento e análise de métricas da máquina em tempo real.

---

# 🚧 Status do Projeto

Projeto em desenvolvimento utilizado para prática de:

* Backend com FastAPI
* Arquitetura REST
* Integração com PostgreSQL
* Docker
* Tratamento de erros
* Logging
* Organização de projetos Python

---

# 🎯 Objetivo

Construir uma API capaz de:

* Monitorar uso de CPU
* Monitorar uso de memória RAM
* Monitorar uso de disco
* Salvar métricas automaticamente no PostgreSQL
* Consultar histórico de métricas
* Aplicar paginação e filtros dinâmicos
* Gerar resumos estatísticos das métricas
* Executar monitoramento contínuo em background
* Rodar em ambiente local e Docker
* Evoluir futuramente para dashboard e alertas em tempo real

---

# ⚙️ Tecnologias Utilizadas

* Python
* FastAPI
* SQLAlchemy
* PostgreSQL
* Pydantic
* Uvicorn
* psutil
* python-dotenv
* Docker

---

# 🧠 Aprendizados

Este projeto está sendo desenvolvido com foco em:

* Estruturação de APIs com FastAPI
* Arquitetura backend organizada
* Separação de responsabilidades
* Integração com PostgreSQL via SQLAlchemy
* Persistência de dados
* Dependency Injection no FastAPI
* Validação com Pydantic
* Paginação (`limit` e `skip`)
* Filtros dinâmicos em queries
* Tratamento global de erros
* Logging no backend
* Coleta automática de métricas
* Threads/background tasks
* Variáveis de ambiente (`.env`)
* Containerização com Docker
* Compatibilidade entre Windows e Linux

---

# 📂 Estrutura do Projeto

```bash
app/
├── database/
├── exceptions/
├── handlers/
├── models/
├── routes/
├── schemas/
├── services/
└── main.py
```

---

# 📌 Funcionalidades

## 🔹 `GET /metrics`

Retorna métricas atuais do sistema em tempo real.

---

## 🔹 `POST /metrics`

Coleta e salva métricas manualmente no banco de dados.

---

## 🔹 `GET /metrics/history`

Retorna histórico de métricas com suporte a:

* Paginação
* Filtros dinâmicos
* Intervalo de datas
* Filtro de CPU mínima/máxima

### Exemplo

```bash
/metrics/history?limit=10&skip=0
```

---

## 🔹 `GET /metrics/latest`

Retorna a métrica mais recente registrada.

---

## 🔹 `GET /metrics/summary`

Retorna um resumo estatístico das métricas contendo:

* Média de CPU/RAM/Disco
* Valor máximo de CPU/RAM/Disco
* Quantidade de registros
* Filtros por período

---

## 🔹 `GET /metrics/{metric_id}`

Retorna uma métrica específica pelo ID.

---

# 🛡️ Tratamento de Erros

O projeto possui:

* Exception handlers globais
* Logs de erro com `logging`
* Rollback automático em falhas no banco
* Respostas padronizadas da API
* Proteção contra quebra do monitoramento automático

---

# 🐳 Execução com Docker

## Subir o projeto

```bash
docker compose up --build
```

Isso irá:

* Subir a API FastAPI
* Subir o PostgreSQL
* Conectar automaticamente os containers

---

# 🐘 Banco de Dados

O banco é criado automaticamente pelo Docker Compose.

Caso precise criar manualmente:

```sql
CREATE DATABASE devwatch;
```

---

# 🔐 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=db
DB_PORT=5432
DB_NAME=devwatch
DB_USER=postgres
DB_PASSWORD=postgres
```

---

# ⚙️ Instalação

Clone o repositório:

```bash
git clone https://github.com/MatheusRibeiro123/devwatch-api.git
cd DevWatch
```

---

# ▶️ Executando a Aplicação

⚠️ O projeto atualmente roda via Docker Compose.

```bash
docker compose up --build
```

---

# 📚 Documentação da API

Após subir o projeto:

* Swagger: http://localhost:8000/docs
* Redoc: http://localhost:8000/redoc

---

# 📈 Próximos Passos

* Dashboard com gráficos
* Visualização em tempo real
* Sistema de alertas
* Autenticação
* Melhorias de observabilidade

---

# 👨‍💻 Autor

**Matheus Ribeiro**
Desenvolvedor em formação, focado em backend com Python e construção de APIs.

Projeto desenvolvido para prática de FastAPI, Docker, PostgreSQL e arquitetura backend.
