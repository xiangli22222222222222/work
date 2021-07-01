import time
import threading
import cv2ceshi

file_path="e:/work/123/ceshi2.avi"
def ceshi1():
    for i in range(1,10):
        print(i)
        if i == 3:
            t1=threading.Thread(target=cv2ceshi.capvideo(i,file_path))
            t1.start()
        time.sleep(1)
        print(i)

if __name__=='__main__':
    ceshi1()
