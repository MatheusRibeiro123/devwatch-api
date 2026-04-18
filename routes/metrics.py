from fastapi import APIRouter
from services.metrics_service import get_system_metrics

router = APIRouter(prefix="/metrics")



#rota que chama função que retorna as metricas do sistema
@router.get("/")
def metrics():
    return get_system_metrics()