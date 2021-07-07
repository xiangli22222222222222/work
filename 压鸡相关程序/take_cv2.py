import time
import datetime
import cv2
import os

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
            if (nowtime1-nowtime).seconds==6:
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

def control_1(action,FILE_VIDEO,FILE_PIC):
    action=int(action)
    #补充完整录制和拍摄的文件名
    dothis_2=False
    while 1:
        # 补充完整录制和拍摄的文件名
        now_time = datetime.datetime.now().strftime('%H-%M-%S')
        FILE_PIC = FILE_PIC + str(now_time) + ".png"
        FILE_VIDEO = FILE_VIDEO + str(now_time) + ".avi"
        # 如果是拍照
        if action == 5:
            take_photo_time,file_name=capvideo(action,FILE_VIDEO,FILE_PIC)
            if  not os.path.exists(FILE_PIC):
                time.sleep(5)
                print("等会再拍照片")
            else:
                dothis_2=True
        if dothis_2:
            break

        if action ==3:
            take_photo_time,file_name=capvideo(action, FILE_VIDEO, FILE_PIC)
            if os.path.getsize(FILE_VIDEO) < 60000:
                time.sleep(5)
                print("等会再去录")
            else:
                dothis_2=True
        if dothis_2:
            break
    return (take_photo_time,file_name)
if __name__=='__main__':
    control_1()