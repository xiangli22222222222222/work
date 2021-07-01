from PIL  import Image
import getcoor
import os

def cutpic(srcpath,dstpath,y):
    img_all=os.listdir(srcpath)

    for img_1 in img_all:
        srcimg=srcpath+img_1
    # 读取图片
        img_1 = Image.open(srcimg)
        # 设置裁剪的位置
        crop_box = y
        # 裁剪图片
        img_2 = img_1.crop(crop_box)
        img_2.save(dstPath)

if __name__=='__main__':
    srcPath = 'e:\\work\\cutpic\\'
    for i in range(0,5):
        y=getcoor.getcoor(i)
        dstPath = 'e:\\work\\cutpic_resize\\' + str(i) + '.png'
        cutpic(srcPath,dstPath,y)