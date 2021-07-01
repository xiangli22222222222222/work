import threading
import time
import sendmessage
def go1():
         for i in range(0, 20, 2):
            time.sleep(2)
            print(threading.current_thread().name, i)


t1=threading.Thread(target=go1)
t2=threading.Thread(target=sendmessage.dothis,args=('3'))

t1.start()
t2.start()