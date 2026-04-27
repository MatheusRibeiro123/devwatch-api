import psutil
from sqlalchemy.orm import Session
from app.models.metrics_model import Metrics
from fastapi import HTTPException
from datetime import datetime

def get_system_metrics():
    return {
        "cpu":{
            "percent": psutil.cpu_percent(interval=1),
            "cores": psutil.cpu_count()
        },
        "memory":{
            "total": psutil.virtual_memory().total,
            "used": psutil.virtual_memory().used,
            "percent": psutil.virtual_memory().percent
        },
        "disk":{
            "total": psutil.disk_usage("C:\\").total,
            "used": psutil.disk_usage("C:\\").used,
            "percent": psutil.disk_usage("C:\\").percent,
    }
    }

def create_metric(db : Session):
    data = {
        "cpu_percent" : psutil.cpu_percent(interval=1),
        "memory_percent" : psutil.virtual_memory().percent,
        "disk_percent" : psutil.disk_usage("C:\\").percent
    }

    metric = Metrics(**data)

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return(metric)

def get_metrics_history(
        db:Session , limit: int = 50, skip: int = 0, start_date: datetime |None = None,
        end_date: datetime | None = None, min_cpu : float | None = None, max_cpu : float | None = None):
    
    query = db.query(Metrics)

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

def get_metric(db:Session,metric_id):
    metric = db.query(Metrics).filter(Metrics.id == metric_id).first()
    if metric is None:
        raise HTTPException(
            status_code=404,
            detail="Metric not found"
        )
    return(metric)