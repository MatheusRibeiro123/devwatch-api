import psutil
from sqlalchemy.orm import Session
from app.models.metrics_model import Metrics
from fastapi import HTTPException
from datetime import datetime
import os
from sqlalchemy import func

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

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return metric

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
    return(metric)

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
        print("Erro ao salvar metricas", e)

def get_latest_metric(db : Session):

    metric = db.query(Metrics).order_by(Metrics.created_at.desc()).first()

    return metric

def get_metrics_summary(db : Session):
    
    result = db.query(func.avg(Metrics.cpu_percent),func.avg(Metrics.disk_percent),func.avg(Metrics.memory_percent)).first()

    return {
        "cpu_avg":result[0] or 0,
        "disk_avg":result[1] or 0,
        "memory_avg":result[2] or 0  
        }




