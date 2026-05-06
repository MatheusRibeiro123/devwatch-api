# 🧭 DevWatch

API de monitoramento de sistema desenvolvida com **FastAPI**, com o objetivo de coletar, armazenar e consultar métricas da máquina em tempo real.

---

## 🚧 Status do Projeto

Projeto em desenvolvimento, utilizado para prática de backend com FastAPI, arquitetura de APIs REST, integração com banco de dados relacional, Docker e boas práticas de organização de projetos Python.

---

## 🎯 Objetivo

Construir uma API capaz de:

- Monitorar uso de CPU
- Monitorar uso de memória RAM
- Monitorar uso de disco
- Salvar métricas em banco PostgreSQL
- Consultar histórico de métricas
- Aplicar paginação de resultados
- Aplicar filtros dinâmicos
- Rodar em ambiente local e Docker
- Evoluir futuramente para alertas e monitoramento em tempo real

---

## ⚙️ Tecnologias utilizadas

- Python
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Uvicorn
- psutil
- python-dotenv
- Docker

---

## 🧠 Aprendizados

Este projeto está sendo desenvolvido com foco em:

- Estruturação de APIs com FastAPI
- Arquitetura backend organizada
- Separação de responsabilidades (routes, services, models, schemas)
- Integração com PostgreSQL via SQLAlchemy
- Persistência de dados
- Dependency Injection no FastAPI
- Validação com Pydantic
- Paginação (limit e skip)
- Filtros dinâmicos em queries
- Tratamento de erros
- Variáveis de ambiente (.env)
- Coleta de métricas com psutil
- Containerização com Docker
- Compatibilidade entre ambientes (Windows/Linux)

---

## 📂 Estrutura do projeto


app/
├── models/
├── routes/
├── schemas/
├── services/


---

## 📌 Funcionalidades

### 🔹 `GET /metrics`
Retorna métricas atuais do sistema em tempo real.

### 🔹 `POST /metrics`
Coleta e salva métricas no banco de dados.

### 🔹 `GET /metrics/history`
Retorna histórico de métricas com suporte a:
- paginação
- filtros dinâmicos

Exemplo:

/metrics/history?limit=10&skip=0


### 🔹 `GET /metrics/{metric_id}`
Retorna uma métrica específica pelo ID.

---

## 🐳 Execução com Docker

### Subir o projeto (API + Banco de Dados)

```bash
docker compose up --build

Isso irá:

subir a API (FastAPI)
subir o PostgreSQL
conectar automaticamente os serviços via Docker network

---

## 🐘 Banco de dados

O banco já é criado automaticamente pelo Docker Compose.

Caso precise recriar manualmente:

```sql id="p8m2qp"
CREATE DATABASE devwatch;
🔐 Variáveis de ambiente (.env)

Crie um arquivo .env na raiz do projeto:

DB_HOST=db
DB_PORT=5432
DB_NAME=devwatch
DB_USER=postgres
DB_PASSWORD=postgres
⚙️ Instalação

Clone o repositório:

git clone <https://github.com/MatheusRibeiro123/devwatch-api.git>
cd DevWatch
▶️ Executando a aplicação

⚠️ O projeto roda apenas via Docker Compose

docker compose up --build
📚 Documentação da API

Após subir o projeto:

Swagger: http://localhost:8000/docs
Redoc: http://localhost:8000/redoc
 
 ## 👨‍💻 Autor

**Matheus Ribeiro**  
Desenvolvedor em formação, focado em backend com Python e construção de APIs.  
Este projeto foi desenvolvido como prática de estudos em FastAPI, Docker e arquitetura de sistemas.