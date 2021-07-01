import threading
import takevideo
import datetime
def gogogo():

     for i in range(1,10,2):
         print(i)

datetime1=datetime.datetime.now()

t1=threading.Thread(target=takevideo.dogo,args=('4',datetime1))
t1.start()
t2=threading.Thread(target=gogogo)
t2.start()


