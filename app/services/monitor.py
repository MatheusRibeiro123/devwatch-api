import time
import threading
import psutil
import os

disk_path = "C:\\" if os.name == "nt" else "/"

def monitor_loop():
    
    while True:
        try:
            cpu_percent = psutil.cpu_percent()
            disk_percent = psutil.disk_usage(disk_path).percent
            memory_percent = psutil.virtual_memory().percent

            print(f"""
            CPU:{cpu_percent}%
            RAM:{memory_percent}%
            DISK:{disk_percent}%
""",flush=True)
           
        
        except Exception as e:
            print(e)

        time.sleep(5)

        

def start_monitor():
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()