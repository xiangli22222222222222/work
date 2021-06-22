import cv2
from datetime import datetime
import time
def captureVideoFromCamera():
    cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    n=0
    WIDTH = 1280
    HEIGHT = 720


    FPS = 10
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 10)
    # 建议使用XVID编码,图像质量和文件大小比较都兼顾的方案
    fourcc = cv2.VideoWriter_fourcc(*'XVID')


    n=0
    while n<100:
        FILENAME = "e:\work\myvideo" + str(time.strftime("%H-%M-%S")) + ".avi"
        out = cv2.VideoWriter(FILENAME, fourcc=fourcc, fps=FPS, frameSize=(WIDTH, HEIGHT))
        start_time = datetime.now()
        print(time.strftime("%H:%M:%S"))
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # 逐帧捕获
            ret, frame = cap.read()
            # 如果正确读取帧，ret为True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            frame = cv2.flip(frame, 1)  # 水平翻转
            ret = out.write(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # 录制5秒后停止
            if (datetime.now() - start_time).seconds == 5:
                print("录制结束")
                break
        n+=1
        print(n)
        # 监测到ESC按键也停止
    # 完成所有操作后，释放捕获器
    out.release()
    cap.release()
    cv2.destroyAllWindows()

captureVideoFromCamera()
print("zhixignjiehu")