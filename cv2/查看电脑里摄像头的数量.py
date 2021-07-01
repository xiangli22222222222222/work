import cv2
n=0

while n<6:


    cap=cv2.VideoCapture(n,cv2.CAP_DSHOW)

    rep,frame=cap.read()

    if rep:
          print("电脑里有%s个摄像头"%n)
          n=n+1
    else:
          break

print(n)
