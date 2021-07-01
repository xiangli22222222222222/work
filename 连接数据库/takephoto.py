import cv2
from datetime import datetime
import time
import sendpic


def capturephoto(FILE_PATH):

    time.sleep(1)
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

    WIDTH = 1280
    HEIGHT = 720


    FPS = 10
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 10)
    # 建议使用XVID编码,图像质量和文件大小比较都兼顾的方案
    # fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # while 1:
    FILENAME = FILE_PATH + str(time.strftime("%H-%M-%S")) + ".png"
    # print(time.strftime("%H:%M:%S"))
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
        # 逐帧捕获
    else:
        print("camera is ok")
        i=12
        while i>0:
            ret, frame = cap.read()
            # 如果正确读取帧，ret为True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
            # frame = cv2.flip(frame, 1)  # 水平翻转
            else:
                cv2.imwrite(FILENAME, frame)
                i=i-1
                print("拍摄完成，%d"%i)
    cap.release()
    cv2.destroyAllWindows()
    now=datetime.now()
    return (now)
    # 完成所有操作后，释放捕获器
if __name__=='__main__':
    capturephoto(FILE_PATH)
    print("zhixignjiehu")