import cv2
from datetime import datetime
import time

WIDTH = 1280
HEIGHT = 720
FPS = 10.0

# 必须指定CAP_DSHOW(Direct Show)参数初始化摄像头,否则无法使用更高分辨率
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
# 设置摄像头设备分辨率
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
# 设置摄像头设备帧率,如不指定,默认600
cap.set(cv2.CAP_PROP_FPS, 15)
# 建议使用XVID编码,图像质量和文件大小比较都兼顾的方案
fourcc = cv2.VideoWriter_fourcc(*'XVID')
n=0
FILENAME = 'myvideo.avi'
out = cv2.VideoWriter(FILENAME, fourcc, FPS, (WIDTH, HEIGHT))

start_time = datetime.now()

while n<=100:

    ret, frame = cap.read()

    while True:
        if ret:
            #cv2.imwrite('image2/' + str(n) + '.jpg', frame)
            out.write(frame)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) == ord('q'):
                break
            录制5秒后停止
            if (datetime.now()-start_time).seconds == 10:
                cap.release()
                print("录制结束")
                break
            监测到ESC按键也停止
        else:
            print("摄像头离线了")
            break
    n+=1
    print(n)
    time.sleep(100)
out.release()
cv2.destroyAllWindows()
print("ok")