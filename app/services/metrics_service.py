import psutil
from sqlalchemy.orm import Session
from app.models.metrics_model import Metrics


def get_system_metrics():
    return {
        "cpu":{
            "percent": psutil.cpu_percent(),
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
            "percent": psutil.disk_usage("C:\\").percent
    }
    }

def create_metric(db : Session):
    data = {
        "cpu_percent" : psutil.cpu_percent(),
        "memory_percent" : psutil.virtual_memory().percent,
        "disk_percent" : psutil.disk_usage("C:\\").percent
    }

    metric = Metrics(**data)

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return(metric)

def get_metrics_history(db:Session , limit: int = 50, skip: int = 0 ):
    return(
        db.query(Metrics)
        .order_by(Metrics.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )