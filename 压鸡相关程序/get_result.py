import cv2
import datetime
import os
import according_zaoyan
import sendmessage_bz
import cutpic
import get_zaoyan

def getresult(file_path,zaoyan,get_time):

    #把时间写入文件
    zaoyan1,zaoyan2=get_zaoyan.duiying(zaoyan)
    with open('12194548.txt', 'a') as file_object:
        file_object.write('本次时间为:' + str(get_time)+"  "+"第"+str(zaoyan1)+"排"+"第"+str(zaoyan2)+"个灶眼"+"\n")
    sum0 = 0  # 用来判断综合分数
    # 初始化列表
    r=[]
    g=[]
    b=[]
    # m是个计数器，看看一共有多少文件
    m=0
    #通过灶眼信息，获得坐标
    data=os.listdir(file_path)
    for data2 in data:
        file_path2=file_path+data2
        cutpic.cut_pic(file_path2,zaoyan)
        break
    for data1 in data:

        i = 0
        j = 0
        k,p=according_zaoyan.get_po(zaoyan)
        print(k,p)
        q=p
        file_path1=file_path+data1
        img = cv2.imread(file_path1)  #读取图像
        while i <100:
            while j<100:

                j+=1
                get_color=img[k,p]

                r.append(get_color[2])
                g.append(get_color[1])
                b.append(get_color[0])
                p+=1
            j=0
            p=q
            i+=1
            k+=1
        m+=1
        os.remove(file_path1)
        #把处理过的文件删除
        print(m)
        sum=0

        #定义一个存储数据的列表
        li=[]

        #拿到上汽与否的判断数值，并存入列表
    for p in range(m-1):
        sum=0
        for o in range(10000):
            # print(g[o*p],g[o+10000])
            sum=sum+(abs(int(r[10000+o+p*10000])-int(r[o+p*10000])))
        # print(sum)
        sum=sum/10000
        with open('12194548.txt', 'a') as file_object:
            file_object.write(str(sum) + '\n')
        print("这里是偏差值%s"%sum)
        p+=1
        li.append(sum)
        sum0+=sum

    with open('12194548.txt', 'a') as file_object:
        file_object.write("本次综合分数为："+str(sum0) + '\n')
    #如果上汽的数据多余2个

    s=0
    for r in li:
        if r>3:
            s+=1
    print(s)
    if sum0>55:
        t="判断已经上汽"
    else:
        t="判断没有上汽"
    sendmessage_bz.send_message(zaoyan,get_time,s,t)

    return(sum0)

if __name__=='__main__':
    #测试用
    # file_path='E:/work/123/pic/'
    # zaoyan=1
    # get_time=datetime.datetime.now()
    getresult(file_path,zaoyan,get_time)
