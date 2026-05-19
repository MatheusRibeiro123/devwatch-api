# TODO - DevWatch

## Docker
- [x] Finalizar Dockerfile
- [x] Criar docker-compose
- [x] Configurar PostgreSQL no Docker
- [x] Testar conexão entre containers

## Backend
- [x] Automatizar coleta de métricas
- [x] Criar serviço de monitoramento contínuo
- [x] Criar rota /metrics/latest
- [x] Criar rota /metrics/summary

## Melhorias da /metrics/summary
 - [x] Arredondar valores (round)
 - [x] Adicionar max() das métricas
 - [x] Adicionar count() de registros
 - [x] Validar parâmetro minutes
 - [x] Adicionar filtros start/end

 ## Melhorar tratamento de erros e resiliencia

- [x] Criar exception handlers globais no FastAPI
- [x] Tratar erros de conexão com PostgreSQL
- [x] Adicionar logs de erro no backend
- [x] Validar parâmetros inválidos nas rotas
- [x] Retornar mensagens padronizadas na API
- [x] Evitar quebra da coleta automática de métricas

## Dashboard
- [x] Criar dashboard web
- [x] Integrar frontend com API FastAPI
- [x] Exibir métricas em tempo real
- [x] Exibir gráficos de CPU
- [x] Exibir gráficos de RAM
- [x] Mostrar histórico de métricas
- [x] Mostrar resumo das métricas
- [x] Mostrar última métrica registrada
- [x] Dockerizar frontend
- [x] Melhorar responsividade do dashboard

