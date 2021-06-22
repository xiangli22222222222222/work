import cv2
n=0

while n<6:


    cap=cv2.VideoCapture(n,cv2.CAP_DSHOW)

    rep,frame=cap.read()

    if rep:
          n=n+1
    else:
        print(n)
        break

print(n)
