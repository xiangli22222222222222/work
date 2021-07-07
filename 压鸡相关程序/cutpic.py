from PIL  import Image
import datetime
import os
import according_zaoyan
import sendpic

def cut_pic(file_name,zaoyan):
    #时间戳毫毛级
    now_time=datetime.datetime.now()
    now_time1=now_time+datetime.timedelta(hours=-8)
    print(now_time)

    # 分离文件和路径
    (file_path,file_name1)=os.path.split(file_name)
    file_save=file_path+"/""123444.png"

    # 读取图片
    img_1 = Image.open(file_name)
    x,y=according_zaoyan.get_po(zaoyan)

    # 设置裁剪的位置
    k=[]
    k.append(int(y))
    k.append(int(x))
    k.append(int(y+100))
    k.append(int(x+100))
    k=tuple(k)
    # 裁剪图片
    img_2 = img_1.crop(k)

    #保存图片
    img_2.save(file_save)

    #发送图片
    sendpic.send_pic(file_save,now_time1,now_time)

if __name__=='__main__':
    #测试用数据
    # file_name="e:/work/123/1234.png"
    # zaoyan=1
    cut_pic(file_name,zaoyan)