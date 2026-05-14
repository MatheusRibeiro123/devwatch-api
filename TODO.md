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
- [ ] Criar dashboard React
- [ ] Integrar frontend com API FastAPI
- [ ] Exibir métricas em tempo real
- [ ] Exibir gráficos de CPU
- [ ] Exibir gráficos de RAM
- [ ] Mostrar histórico de métricas
- [ ] Mostrar resumo das métricas
- [ ] Mostrar última métrica registrada
- [ ] Dockerizar frontend
- [ ] Melhorar responsividade do dashboard

