import cv2
from datetime import datetime
import time
def capvideo(action,FILE_VIDEO,FILE_PIC):

    action=int(action)
    #初始化摄像头

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    WIDTH = 1280
    HEIGHT = 720
    FPS = 10
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 10)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    out = cv2.VideoWriter(FILE_VIDEO, fourcc=fourcc, fps=FPS, frameSize=(WIDTH, HEIGHT))

    nowtime = datetime.datetime.now()
    # print(nowtime)
    dothisone=False
    i = 10
    while 1:
        rep, frame = cap.read()

        while not cap.isOpened():
            time.sleep(3)
            print("摄像头没打开等5秒")
            dothisone = True
            break
        while not rep:
            time.sleep(3)
            print("摄像头没打开等5秒")
            dothisone = True
            break
        #     print("摄像头被占用，等5秒")
        if dothisone:
            break
        # 摄像过程
        if action==3:
            rep = out.write(frame)
            print("在写")
            nowtime1=datetime.datetime.now()
            if (nowtime1-nowtime).seconds==7:
                cap.release()
                out.release()
                return (nowtime,FILE_VIDEO)
         # 拍照过程
        if action==5:

            cv2.imwrite(FILE_PIC,frame)
            i-=1
            if i<2:
                nowtime = datetime.datetime.now()
                return (nowtime,FILE_PIC)

if __name__=='__main__':
    capvideo(3,'e:/work1/')