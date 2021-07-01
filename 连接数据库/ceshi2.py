import threading
import takephoto
import sendmessage
import time

def good():
    for i in range(1,10,2):
       print (i)
       time.sleep(1)

def good1():
    for i in range(0,10,2):
        print(i)
    # time.sleep(1)

thread1=threading.Thread(target=sendmessage.dothis(3))
thread1.start()
thread2=threading.Thread(target=good1())
thread2.start()