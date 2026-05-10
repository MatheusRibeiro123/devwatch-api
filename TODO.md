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

## Melhorias da /summary
 - [x] Arredondar valores (round)
 - [x] Adicionar max() das métricas
 - [x] Adicionar count() de registros
 - [x] Validar parâmetro minutes
 - [x] Adicionar filtros start/end

 ## Melhorar tratamento de erros

- [x] Criar exception handlers globais no FastAPI
- [ ] Tratar erros de conexão com PostgreSQL
- [ ] Adicionar logs de erro no backend
- [ ] Validar parâmetros inválidos nas rotas
- [ ] Retornar mensagens padronizadas na API
- [ ] Evitar quebra da coleta automática de métricas
- [ ] Tratar timeout/conexão perdida no banco


## Dashboard
- [ ] Exibir gráficos de CPU
- [ ] Exibir gráficos de RAM
- [ ] Mostrar histórico de métricas

