import psutil

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