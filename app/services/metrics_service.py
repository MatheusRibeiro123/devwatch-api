import psutil
from sqlalchemy.orm import Session
from app.models.metrics_model import Metrics
from fastapi import HTTPException
from datetime import datetime, timedelta
import os
from sqlalchemy import func
import logging

logger = logging.getLogger(__name__)

disk_path = "C:\\" if os.name == "nt" else "/"

def get_system_metrics():
    cpu_percent = psutil.cpu_percent()
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage(disk_path)

    return {
        "cpu": {
            "percent": cpu_percent,
            "cores": psutil.cpu_count()
        },
        "memory": {
            "total": memory.total,
            "used": memory.used,
            "percent": memory.percent
        },
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "percent": disk.percent,
        }
    }

def create_metric(db: Session):
    data = {
        "cpu_percent" : psutil.cpu_percent(interval=1),
        "memory_percent" : psutil.virtual_memory().percent,
        "disk_percent" : psutil.disk_usage(disk_path).percent
    }

    metric = Metrics(**data)

    try:
        db.add(metric)
        db.commit()
        db.refresh(metric)
        
        return metric
    
    except Exception as e:
        db.rollback()
        logger.exception(f"Erro ao criar métrica: {e}")

    

def get_metrics_history(
        db:Session , limit: int = 50, skip: int = 0, start_date: datetime |None = None,
        end_date: datetime | None = None, min_cpu : float | None = None, max_cpu : float | None = None):
    
    query = db.query(Metrics).filter(True)

    if min_cpu is not None:
        query = query.filter(Metrics.cpu_percent >= min_cpu)

    if max_cpu is not None:
        query = query.filter(Metrics.cpu_percent <= max_cpu)

    if start_date:
        query = query.filter(Metrics.created_at >= start_date)

    if end_date:
        query = query.filter(Metrics.created_at <= end_date)
    return(
        query
        .order_by(Metrics.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_metric(db: Session, metric_id: int):
    metric = db.query(Metrics).filter(Metrics.id == metric_id).first()
    if metric is None:
        raise HTTPException(
            status_code=404,
            detail="Metric not found"
        )
    return metric

def save_metrics(db:Session , metrics):
   
    novo = Metrics(
        cpu_percent=metrics["cpu"]["percent"],
        memory_percent=metrics["memory"]["percent"],
        disk_percent=metrics["disk"]["percent"],
        created_at=datetime.utcnow()
    )
    try:
        db.add(novo)
        db.commit()
        db.refresh(novo)
    except Exception as e:
        db.rollback()
        logger.exception(f"Erro ao salvar métricas: {e}")

def get_latest_metric(db : Session):

    metric = db.query(Metrics).order_by(Metrics.created_at.desc()).first()

    if metric is None:
        raise HTTPException(status_code=404, detail="Nenhuma métrica encontrada.")

    return metric

def get_metrics_summary(db : Session,minutes: int | None = None, start_date: datetime | None = None, end_date: datetime | None = None):
    
    query = db.query(
        func.avg(Metrics.cpu_percent),
        func.avg(Metrics.memory_percent),
        func.avg(Metrics.disk_percent),
        func.max(Metrics.cpu_percent),
        func.max(Metrics.memory_percent),
        func.max(Metrics.disk_percent),
        func.count(Metrics.id)
        ) 
    
    if minutes is not None and (start_date or end_date):
        raise HTTPException(status_code=400, detail="Os parâmetros 'minutes' e 'start_date/end_date' não podem ser usados juntos.")

    if start_date is not None and end_date is not None and start_date > end_date:
        raise HTTPException(status_code=400, detail="O parâmetro 'start_date' deve ser anterior a 'end_date'.")

    if start_date is not None:
        query = query.filter(Metrics.created_at >= start_date)

    if end_date is not None:
        query = query.filter(Metrics.created_at <= end_date)

    if minutes is not None:
        
        if minutes <= 0:
            raise HTTPException(status_code=400, detail="O parâmetro 'minutes' deve ser um número positivo.")
        
        if minutes > 10080:
            raise HTTPException(status_code=400, detail="O parâmetro 'minutes' não pode ser maior que 10080 (7 dias).")
        
        
        time_limit= datetime.utcnow() - timedelta(minutes=minutes)

        query = query.filter(Metrics.created_at >= time_limit)

    result = query.first()

    if result is None:
        raise HTTPException(status_code=404, detail="Nenhuma métrica encontrada.")

    return {
        "cpu_avg": round(result[0] or 0, 2),
        "memory_avg": round(result[1] or 0, 2),
        "disk_avg": round(result[2] or 0, 2),
        "cpu_max": round(result[3] or 0, 2),
        "memory_max": round(result[4] or 0, 2),
        "disk_max": round(result[5] or 0, 2),
        "count": result[6] or 0
    }




