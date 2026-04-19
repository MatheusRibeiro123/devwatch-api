from fastapi import APIRouter
from app.services.metrics_service import get_system_metrics
from app.schemas.metrics_schema import MetricsResponse
router = APIRouter(prefix="/metrics")



#rota que chama função que retorna as metricas do sistema
@router.get("/",response_model=MetricsResponse )
def metrics():
    return get_system_metrics()