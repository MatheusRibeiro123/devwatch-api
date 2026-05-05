import time
import threading
import os
from app.services.metrics_service import get_system_metrics,save_metrics
from app.database import SessionLocal


disk_path = "C:\\" if os.name == "nt" else "/"

def monitor_loop():
    
    while True:
        db = SessionLocal()

        try:
            metrics = get_system_metrics()
            save_metrics(db , metrics)
           
        
        except Exception as e:
            print("erro no loop",e)

        finally:
            db.close

        time.sleep(5)

        

def start_monitor():
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()