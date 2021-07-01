import datetime
import time
import sendpic
import sendmessage
import mysql_db
import take_cv2
import takevideo
import get_pic
import get_result


def gogogo():
    #两个参数置零
    n=0
    m=0
    i=0
    li=[]
    li1=[]
    li2=[]

    #这个变量用来保存判断是否上汽的东西
    li3=[]
    li4=[]
    while 1:
        # 不停的连接数据库，获取数据
        data=mysql_db.mysql_db(-32)

        #每次获取数据以后，计数器置零
        m=0

        #获取当前时间，并格式化
        now_date= (datetime.datetime.now() + datetime.timedelta(days=0,hours=-8)).date().strftime('%Y-%m-%d')
        print(now_date)

        for data1 in data:

              #判断是否是今天的数据
              if str(data1[3]) > now_date:

                #每拿到一条当天的数据，计数器加1
                m=m+1

                #如果这次拿到的数据比上次的多，那么就打印一下新数据
                if m>n:
                    zaotai_kaiguan={"开关情况":data1[9],"灶眼":data1[10],"时间":data1[3],"序号":data1[11]}
                    print(zaotai_kaiguan)

                #如果这不是运行程序第一次拿数据或者不是今天第一次拿数据，就开干
                    if n>0:
                        # 如果是关火信息
                        FILE_PATH_PIC = 'E:/work/123/pic/'
                        FILE_PATH_VIDEO = 'E:/work/123/video/'

                        FILE_PATH_VIDEO2='E:/work/123/video2/'
                        file_path='E:/work/123/pic2/'

                        if data1[9]==str(0):
                            #先休息15秒
                            time.sleep(15)

                            #调用摄像头拍照
                            get_photo_time,file_name=take_cv2.control_1(5,FILE_PATH_VIDEO,FILE_PATH_PIC)

                            #发送灶眼信息
                            sendmessage.send_message(data1[10])

                            #上传图片到企业微信，并发送企业微信
                            sendpic.send_pic(file_name,data1[3],get_photo_time)


                        elif data1[9]==str(1):

                            # 先把实际的点火时间赋值给变量
                            date_time2=data1[3]
                            date_time2=date_time2+datetime.timedelta(hours=8)

                            # 再把录制时间复制给变量
                            date_time1=data1[3]
                            date_time1=date_time1+datetime.timedelta(days=0,hours=8,minutes=14)
                            print(date_time1)

                            # 把判断是否上汽的时间赋值给列表
                            date_time3=data1[3]
                            date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=13,seconds=-30)
                            li3.append(date_time3)
                            li4.append(data1[10])

                            date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=14, seconds=-30)
                            li3.append(date_time3)
                            li4.append(data1[10])

                            date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=15, seconds=-30)
                            li3.append(date_time3)
                            li4.append(data1[10])

                            date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=16, seconds=-30)
                            li3.append(date_time3)
                            li4.append(data1[10])

                            date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=17, seconds=-30)
                            li3.append(date_time3)
                            li4.append(data1[10])

                            # 把录视频的时间，写入列表
                            li.append(date_time1)

                            # 把灶眼的位置，写入列表
                            li1.append(data1[10])


                            # 把开始压鸡的时间，写入列表
                            li2.append(date_time2)

        #获取当前时间
        now_time=datetime.datetime.now()

        #去拍摄自动化判断上汽视频
        if len(li3)!=0:
            if now_time>li3[0]:
                #拍视频
                get_photo_time, file_name = take_cv2.control_1(3, FILE_PATH_VIDEO2, FILE_PATH_PIC)
                #把视频搞成图片,并去掉黑色图片
                get_pic.getpic(file_name,file_path)

                #通过图片计算结果
                get_result.getresult(file_path,int(li4[0]),li3[0])

                del li3[0]
                del li4[0]

        #去拍摄人工判断上汽视频
        if len(li)!=0:
            if now_time>li[0]:
                #录像
                get_photo_time, file_name = take_cv2.control_1(3, FILE_PATH_VIDEO, FILE_PATH_PIC)
                #上传
                takevideo.take_video(li1[0],li2[0],get_photo_time,file_name)
                #删除列表第一个元素
                del li[0]
                del li1[0]
                del li2[0]


        #把这次取得的数据的值，赋给锚
        n=m
        print(n,"现在的时间是%s"%datetime.datetime.now())
        time.sleep(5)
if __name__=='__main__':
    gogogo()

