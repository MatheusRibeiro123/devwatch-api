import time
import threading
import psutil

def monitor_loop():
    while True:
        #parei aqui----------------------
        time.sleep(5)

def start_monitor():
    thread = threading.Thread(target=monitor_loop, daemon=True)
    thread.start()