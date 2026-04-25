from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.metrics_service import get_system_metrics, create_metric,get_metrics_history,get_metric
from app.schemas.metrics_schema import MetricsResponse
from app.database import get_db
from app.schemas.metrics_schema import MetricsHistoryResponse,MetricResponse

router = APIRouter(prefix="/metrics", tags=["Metrics"])

#retorna métricas atuais (não salva)

@router.get("/", response_model=MetricsResponse)
def get_metrics():
    return get_system_metrics()


# coleta e salva métricas no banco
@router.post("/",response_model=MetricsHistoryResponse)
def create_metric_route(db: Session = Depends(get_db)):
    return create_metric(db)

# lista as ultimas metricas 

@router.get("/history",response_model=list[MetricsHistoryResponse])
def metrics_history(
    limit : int = 50,
    skip : int = 0,
    db : Session = Depends(get_db)):
    return get_metrics_history(db , limit, skip)

#listar apenas um metrica

@router.get("/{metric_id}",response_model=MetricResponse)
def metric(metric_id : int,db:Session = Depends(get_db)):
    return get_metric(db , metric_id )