# 🧭 DevWatch

API de monitoramento de sistema desenvolvida com **FastAPI**, com o objetivo de coletar, armazenar e consultar métricas da máquina em tempo real.

## 🚧 Status do Projeto

Este projeto ainda está em desenvolvimento.

Está sendo utilizado como prática para aprendizado de desenvolvimento backend com **FastAPI**, arquitetura de APIs REST e organização profissional de projetos Python.

## 🎯 Objetivo

Desenvolver uma API capaz de:

* Monitorar uso de CPU
* Monitorar uso de memória RAM
* Monitorar uso de disco
* Salvar métricas em banco de dados
* Consultar histórico de métricas
* Trabalhar com paginação de resultados
* Evoluir futuramente para filtros avançados e geração de alertas

## ⚙️ Tecnologias utilizadas

* Python
* FastAPI
* SQLAlchemy
* SQLite
* Pydantic
* Uvicorn
* psutil

## 🧠 Aprendizados

Este projeto está sendo desenvolvido com foco em:

* Estruturação de APIs com FastAPI
* Separação de responsabilidades (`routes`, `services`, `models`, `schemas`)
* Organização de projetos backend
* Integração com banco de dados usando SQLAlchemy
* Persistência de dados
* Dependency Injection com FastAPI
* Validação de dados com Pydantic
* Paginação de resultados (`limit` e `skip`)
* Coleta de dados do sistema com psutil

## 📌 Funcionalidades atuais

### `GET /metrics`

Retorna métricas atuais do sistema em tempo real.

### `POST /metrics`

Coleta e salva métricas no banco de dados.

### `GET /metrics/history`

Retorna histórico de métricas salvas com suporte a paginação.

Exemplo:

```http id="n8mx48"
/metrics/history?limit=10&skip=0
```
