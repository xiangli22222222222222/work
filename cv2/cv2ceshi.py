import time
import datetime
import cv2
def capvideo(action,FILENAME):
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    WIDTH = 1280
    HEIGHT = 720
    FILENAME_PIC='E:\work\mypic.png'
    FPS = 10
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 10)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(FILENAME, fourcc=fourcc, fps=FPS, frameSize=(WIDTH, HEIGHT))

    nowtime = datetime.datetime.now()
    print(nowtime)
    while 1:
        rep, frame = cap.read()
        # rep = out.write(frame)
        if action==3:
            rep = out.write(frame)
            print("在写")
        #     print(action)
        #     nowtime=datetime.datetime.now()
        #     while 1:
        nowtime1=datetime.datetime.now()
        print(nowtime1)
        if (nowtime1-nowtime).seconds==50:
            cap.release()
            break
        if action==5:
             cv2.imwrite(FILENAME_PIC,frame)
             break
        # else:
        #      break

if __name__=='__main__':
    capvideo()