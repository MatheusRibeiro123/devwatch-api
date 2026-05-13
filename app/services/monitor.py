import time
import threading
import os
from app.services.metrics_service import get_system_metrics,save_metrics
from app.database import SessionLocal
import logging

logger = logging.getLogger(__name__)



disk_path = "C:\\" if os.name == "nt" else "/"

def monitor_loop():
    logger.info("Iniciando monitoramento de métricas do sistema.")
    
    while True:
        db = SessionLocal()

        try:
            metrics = get_system_metrics()
            save_metrics(db , metrics)
           
        
        except Exception as e:
            logger.exception(f"Erro no monitoramento de métricas: {e}")

        finally:
            db.close()

            

        time.sleep(5)

        

def start_monitor():
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()