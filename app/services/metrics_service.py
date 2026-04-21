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
            "total": psutil.disk_usage("/").total,
            "used": psutil.disk_usage("/").used,
            "percent": psutil.disk_usage("/").percent
    }
    }

def create_metric(db : Session):
    data = {
        "cpu_percent" : psutil.cpu_percent(),
        "memory_percent" : psutil.virtual_memory().percent,
        "disk_percent" : psutil.disk_usage("/").percent
    }

    metric = Metrics(**data)

    db.add(metric)
    db.commit()
    db.refresh(metric)

    return(metric)
