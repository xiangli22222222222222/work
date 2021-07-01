
import datetime
import cv2

def capvideo(FILE_PIC):
    i = 10
    #初始化摄像头
    while 1:
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        WIDTH = 1280
        HEIGHT = 720
        FPS = 10
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
        cap.set(cv2.CAP_PROP_FPS, 10)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        rep, frame = cap.read()

        nowtime = datetime.datetime.now()
        cv2.imwrite(FILE_PIC, frame)
        i -= 1
        if i < 2:
            nowtime=datetime.datetime.now()
            return (nowtime, FILE_PIC)


if __name__=='__main__':
    FILE_PATH_PIC = 'E:/work/123/pic/123.png'
    capvideo(FILE_PATH_PIC)