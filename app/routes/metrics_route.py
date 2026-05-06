from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.metrics_service import get_system_metrics, create_metric,get_metrics_history,get_metric,get_latest_metric,get_metrics_summary
from app.schemas.metrics_schema import MetricsResponse
from app.database import get_db
from app.schemas.metrics_schema import MetricsHistoryResponse,MetricResponse
from datetime import datetime

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
    start_date: datetime | None = None,
    end_date : datetime | None = None,
    min_cpu : float | None = None,
    max_cpu : float | None = None,
    db : Session = Depends(get_db)):
    return get_metrics_history(db , limit, skip, start_date, end_date, max_cpu, min_cpu)

#listar a ultima metrica registrada no sistema

@router.get("/latest",response_model= MetricResponse)
def latest_metric(db:Session = Depends(get_db)):
    metric = get_latest_metric(db)

    if not metric:
        raise HTTPException(status_code= 404, detail= "nenhuma metrica encontrada!")
    
    return metric

#listar a media das metricas salvas
@router.get("/summary")
def avg_metrics(db:Session =Depends(get_db)):
    
    average = get_metrics_summary(db)
    
    return average



#listar apenas um metrica

@router.get("/{metric_id}",response_model=MetricResponse)
def metric(metric_id : int,db:Session = Depends(get_db)):
    return get_metric(db , metric_id )







