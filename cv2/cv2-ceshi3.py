import cv2
import numpy as np
import time
import os


def anaoshots():
    # print(time.strftime('%M:%S',time.localtime(time.time())))
    vc = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # 笔记本内置摄像头一般为 0
    # vc = cv2.VideoCapture('Test2.mp4') #读入视频文件
    c = 1
    if vc.isOpened():  # 判断是否正常打开
        rval, frame = vc.read()
        print("read ok")
    else:
        rval = False
        print("read error")
    timeF = 2  # 视频帧计数间隔频率
    while rval:  # 循环读取视频帧
        rval, frame = vc.read()
        if (c % timeF == 0):  # 每隔timeF帧进行存储操作
            cv2.imwrite('image2/' + str(c) + '.jpg', frame)  # 存储为图像

            img = cv2.imread('image2/' + str(c) + '.jpg')
            GrayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # 中值滤波
            GrayImage = cv2.medianBlur(GrayImage, 5)
            ret, th1 = cv2.threshold(GrayImage, 100, 255, cv2.THRESH_BINARY)
            # 3 为Block size, 5为param1值
            th2 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                        cv2.THRESH_BINARY, 3, 5)
            th3 = cv2.adaptiveThreshold(GrayImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                        cv2.THRESH_BINARY, 3, 5)
            titles = ['Gray Image', 'Global Thresholding (v = 107)',
                      'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
            cv2.imwrite('image2/GrayImage' + str(c) + '.jpg', GrayImage)  # 存储为图像
            cv2.imwrite('image2/th1-' + str(c) + '.jpg', th1)  # 存储为图像
            cv2.imwrite('image2/th2-' + str(c) + '.jpg', th2)  # 存储为图像
            cv2.imwrite('image2/th3-' + str(c) + '.jpg', th3)  # 存储为图像
        # images = [GrayImage, th1, th2, th3]
        # for i in range(4):
        #  plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
        #   plt.title(titles[i])
        #   plt.xticks([]),plt.yticks([])
        # plt.show()
        if (c <= (20 * timeF)):
            c = c + 1
        else:
            vc.release()
        cv2.waitKey(1)


# print("Input 'q' to quit!")

def start_video():
    while True:
        value = input("Input 's' start video:")
        if value == 's':
            anaoshots()
        elif value == 'q':
            break


start_video()