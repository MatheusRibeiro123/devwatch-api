from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.metrics_service import get_system_metrics, create_metric
from app.schemas.metrics_schema import MetricsResponse
from app.database import get_db

router = APIRouter(prefix="/metrics", tags=["Metrics"])

#retorna métricas atuais (não salva)

@router.get("/", response_model=MetricsResponse)
def get_metrics():
    return get_system_metrics()


# coleta e salva métricas no banco
@router.post("/")
def create_metric_route(db: Session = Depends(get_db)):
    return create_metric(db)