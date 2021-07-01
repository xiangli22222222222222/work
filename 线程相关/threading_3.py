import threading
import time

def go2():
    for i in range(1, 20, 2):
        time.sleep(2)
        print(threading.current_thread().name, i)
