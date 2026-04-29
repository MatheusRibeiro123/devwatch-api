🧭 DevWatch

API de monitoramento de sistema desenvolvida com **FastAPI**, com o objetivo de coletar, armazenar e consultar métricas da máquina em tempo real.

---

## 🚧 Status do Projeto

> Este projeto ainda está em desenvolvimento. Está sendo utilizado como prática para aprendizado de desenvolvimento backend com FastAPI, arquitetura de APIs REST, integração com banco de dados relacionais, containerização com Docker e organização profissional de projetos Python.

---

## 🎯 Objetivo

Desenvolver uma API capaz de:

- Monitorar uso de CPU
- Monitorar uso de memória RAM
- Monitorar uso de disco
- Salvar métricas em banco de dados PostgreSQL
- Consultar histórico de métricas
- Trabalhar com paginação de resultados
- Aplicar filtros dinâmicos
- Funcionar em ambiente local e Docker
- Evoluir futuramente para geração de alertas e monitoramento em tempo real

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
- Integração com PostgreSQL usando SQLAlchemy
- Persistência de dados
- Dependency Injection no FastAPI
- Validação de dados com Pydantic
- Paginação de resultados (limit e skip)
- Filtros dinâmicos em queries
- Tratamento de erros
- Variáveis de ambiente com `.env`
- Coleta de dados do sistema com `psutil`
- Containerização com Docker
- Compatibilidade entre Windows e Linux (cross-platform)

---

## 📂 Estrutura do Projeto
app/
├── models/
├── routes/
├── schemas/
├── services/

text

---

## 📌 Funcionalidades atuais

### 🔹 `GET /metrics`
Retorna métricas atuais do sistema em tempo real.

### 🔹 `POST /metrics`
Coleta e salva métricas no banco de dados.

### 🔹 `GET /metrics/history`
Retorna histórico de métricas com suporte a:
- Paginação
- Filtros dinâmicos

**Exemplo:**  
`/metrics/history?limit=10&skip=0`

### 🔹 `GET /metrics/{metric_id}`
Retorna uma métrica específica pelo ID.

---

## 🐳 Execução com Docker

1. **Build da imagem**
   ```bash
   docker build -t devwatch .
Executar container

bash
docker run -p 8000:8000 \
  -e DB_HOST=host.docker.internal \
  devwatch
🐘 Configuração do PostgreSQL
Crie o banco:

sql
CREATE DATABASE devwatch;
🔐 Configuração do .env
Crie um arquivo .env na raiz do projeto:

text
DB_HOST=localhost
⚙️ Instalação
Clone o repositório

bash
git clone <https://github.com/MatheusRibeiro123/devwatch-api.git>
Acesse o projeto

bash
cd DevWatch
Crie o ambiente virtual

bash
python -m venv venv
Ative o ambiente virtual

Windows:

bash
venv\Scripts\activate
Linux/macOS:

bash
source venv/bin/activate
Instale as dependências

bash
pip install -r requirements.txt
▶️ Executando a API (local)
bash
uvicorn app.main:app --reload
📚 Documentação
Swagger: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

🚀 Próximas melhorias
Sistema de autenticação

Geração de alertas

Dashboard frontend

Monitoramento em tempo real

docker-compose (API + PostgreSQL juntos)

Testes automatizados

Deploy da aplicação

👨‍💻 Autor
Matheus Ribeiro
Projeto desenvolvido como prática de estudos em desenvolvimento backend com Python.