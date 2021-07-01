import os
import cv2
import getcoor


# 遍历指定目录，显示目录下的所有文件名
def CropImage4File(filepath, destpath,y):
    pathDir = os.listdir(filepath)  # 列出文件路径中的所有路径或文件
    for allDir in pathDir:
        child = os.path.join(filepath, allDir)
        dest = os.path.join(destpath, allDir)
        if os.path.isfile(child):
            image = cv2.imread(child)
        sp = image.shape  # 获取图像形状：返回【行数值，列数值】列表
        sz1 = sp[0]  # 图像的高度（行 范围）
        sz2 = sp[1]  # 图像的宽度（列 范围）
        # sz3 = sp[2]                #像素值由【RGB】三原色组成

        # 你想对文件的操作
        a = int(y[0])  # x start
        print(a)
        b = int(y[2])  # x end
        print(b)
        c = int(y[1])  # y start
        print(c)
        d = int(y[3])  # y end
        print(d)
        cropImg = image[a:b, c:d]  # 裁剪图像
        cv2.imwrite(dest, cropImg)  # 写入图像路径


if __name__ == '__main__':
    filepath = 'e:\\\work\\cutpic\\'  # 源图像
    destpath = 'e:\\work\\cutpic_resize\\'  # resized images saved here
    y=getcoor.getcoor(1)
    CropImage4File(filepath, destpath,y)