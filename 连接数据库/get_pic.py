import os

import cv2


def save_image(image, addr, num):
    address = addr + str(num) + '.png'
    cv2.imwrite(address, image)


# 读取视频文件
def getpic(file_name,file_path):

    #设置模块的实例化对象
    videoCapture = cv2.VideoCapture(file_name)

    # 读帧
    success, frame = videoCapture.read()
    i = 0

    # 设置固定帧率
    timeF = 3
    j = 0
    while success:
        i = i + 1
        if (i % timeF == 0):
            j = j + 1
            if j>6:
                save_image(frame,file_path,j)
            # print('save image:', i)
        success, frame = videoCapture.read()
    #干完活把视频删掉

if __name__=='__main__':
    getpic()