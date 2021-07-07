import sendpic
import datetime
import time
import mysql_dbzaoyan
import sendmessage_wb
import take_cv2
import takevideo
import get_pic
import get_result
import sendmessage


# 对列表进行排序操作
def takeSecond(elem):
    return elem[1]


def panduan(li2, li3, li4, li5):
    # 用来存放拍照时间
    li3_1 = []

    # 存放自动拍摄视频
    li4_1 = []

    # 存放人工拍摄上汽视频的
    li5_1 = []

    zaoyan = 100

    # 去拿第一个六眼灶的数据
    data = mysql_dbzaoyan.get_db(-8.5, 1)
    li1 = []

    if data:
        for data1 in reversed(data):
            print(data1)
            li = []
            for data2 in data1:
                li.append(data2)
            li1.append(li)

    for i in range(len(li1)):

        # 设定循环判定标签
        flag0=True
        if int(li1[i][9]) == 1 and not li1[i][1] in li2:

            #把符合条件的灶眼拿出来
            zaoyan = int(li1[i][10])

            for j in range(i):
                if int(li1[j][9])==1 and int(li1[j][10]) == int(zaoyan):
                    flag0=False

            if flag0==True:

                now_time_li4 = datetime.datetime.now()
                now_time_li4 = now_time_li4 + datetime.timedelta(minutes=1)
                li2.append(li1[i][1])
                # 算出实际时间
                date_time2 = li1[i][3]
                date_time2 = date_time2 + datetime.timedelta(hours=8)

                if (now_time_li4 - date_time2).seconds < 780:

                    # 算人工判断是否上汽的视频
                    li5_1.append(date_time2)

                    date_time1 = li1[i][3]
                    date_time1 = date_time1 + datetime.timedelta(days=0, hours=8, minutes=13)
                    print(date_time1)
                    li5_1.append(date_time1)
                    li5_1.append(li1[i][10])
                    li5_1.append(li1[i][1])

                    li5.append(li5_1)
                    li5_1 = []

                    # 拍自动判断是否上汽的视频，把相应的时间，赋值给一维列表，并给二维列表赋值
                    for k in range(12, 17):
                        li4_1.append(date_time2)
                        date_time3 = li1[i][3]
                        date_time3 = date_time3 + datetime.timedelta(days=0, hours=8, minutes=k, seconds=-30)
                        li4_1.append(date_time3)
                        li4_1.append(li1[i][10])
                        li4_1.append(li1[i][1])

                        # 再把一维列表的值，赋给二维列表，并清空一维列表
                        li4.append(li4_1)
                        li4_1 = []

    for i in range(len(li1)):

        # 判断是否有关火数据

        if int(li1[i][9]) == 0 and not li1[i][1] in li2:

            # 找到系统的关火时间

            date_time4 = li1[i][3]
            date_time4 = date_time4 + datetime.timedelta(hours=8)

            li2.append(li1[i][1])
            # print("进入一级循环")
            plustime = li1[i][3]

            zaoyan = int(li1[i][10])
            print("这次灭火的灶眼是：%s,第几条数据%s" % (zaoyan, i + 1))

            for j in range(i + 1, len(li1)):

                # 这里去拿符合关火数据的点火数据
                if int(li1[j][9]) == 1 and int(li1[j][10]) == int(zaoyan):
                    # print("进入二级循环")
                    # print(li1[j][10])

                    origntime = li1[j][3]

                    # 这里算压鸡的时长
                    short_of = (plustime - origntime).seconds
                    short_of = round(short_of / 60, 2)
                    print("这是时间间隔：%s" % short_of)

                    # 获取压鸡时间
                    do_time = li1[j][3]
                    do_time = do_time + datetime.timedelta(hours=8)


                    # 判断这个数据和现在的时间比是不是过时了
                    now_time_li3 = datetime.datetime.now()
                    now_time_li3=now_time_li3+datetime.timedelta(seconds=40)
                    # if (now_time_li3-do_time).seconds < 100:

                    li3_1.append(date_time4)
                    now_time_15 = li1[i][3]
                    now_time_15 = now_time_15 + datetime.timedelta(hours=8, seconds=15)
                    li3_1.append(now_time_15)
                    li3_1.append(li1[j][10])
                    li3_1.append(li1[j][1])

                    li3.append(li3_1)
                    li3_1 = []

                    if short_of < 13:
                        # 这里是删掉自动判断视频的时间队列
                        if li4 == []:
                            break
                        m = 0
                        while 1:
                            if li4[m][3] == li1[j][1]:
                                print("删掉一条Li4数据%s" % li4[m])
                                del li4[m]
                                m -= 1
                            m += 1
                            if m == len(li4):
                                break

                            # 这里是删掉人工判断是否上汽视频队列
                        n = 0
                        while 1:
                            if li5[n][3] == li1[j][1]:
                                print("删掉一条li5数据%s" % li5[n])
                                del li5[n]
                                n -= 1
                            n += 1
                            if n == len(li5):
                                break

                    # 发送压鸡时长消息
                    do_time = datetime.datetime.strftime(do_time, '%H:%M:%S')
                    sendmessage_wb.send_message(zaoyan, short_of, do_time)

                    # 这里判断如果又碰到一个关火数据就跳出循环了
                if int(li1[j][9]) == 0 and int(li1[j][10]) == int(zaoyan):
                    break

    print("图片队列%s" % li3)
    print("自动视频队列%s" % li4)
    print("人工视频队列%s" % li5)
    print("已经处理的%s" % li2)

    return (li2, li3, li4, li5)


def dosomething():
    # 说明 3,4,5   0位置传的是服务器关火时间，，1位置传的是加8个小时处理过的时间，2位置传的灶眼，3位置传的唯一标识
    li2 = []
    li3 = []
    li4 = []
    li5 = []

    while 1:

        # 路径配置信息
        FILE_PATH_PIC = 'D:/work/123/pic/'
        FILE_PATH_VIDEO = 'D:/work/123/video/'

        FILE_PATH_VIDEO2 = 'D:/work/123/video2/'
        file_path = 'D:/work/123/pic2/'

        # 获取现在的时间
        now_time = datetime.datetime.now()

        # 取回时间数组
        l2, li3, li4, li5 = panduan(li2, li3, li4, li5)
        while 1:
            k = 0
            # 这里是判断是否到了拍照时间
            if len(li3) != 0:
                if now_time > li3[0][1]:
                    print("判断拍照的时限应该是：%s" % li3[0][1])
                    k = 1
                    # 去拍照片
                    get_photo_time, file_name = take_cv2.control_1(5, FILE_PATH_VIDEO, FILE_PATH_PIC)

                    # 发送灶眼信息
                    sendmessage.send_message(li3[0][2])

                    # 上传图片到企业微信，并发送企业微信
                    sendpic.send_pic(file_name, li3[0][0], get_photo_time)

                    # 拍完就把数据删掉
                    del li3[0]

            # 这里判断是否到了拍摄自动判断
            if len(li4) != 0:
                li4.sort(key=takeSecond)
                if now_time > li4[0][1]:
                    k = 1
                    # 拍视频
                    get_photo_time, file_name = take_cv2.control_1(3, FILE_PATH_VIDEO2, FILE_PATH_PIC)
                    # 把视频搞成图片,并去掉黑色图片
                    get_pic.getpic(file_name, file_path)

                    # 通过图片计算结果
                    sum0 = get_result.getresult(file_path, int(li4[0][2]), li4[0][1])

                    time_jian = li4[0][1] - li4[0][0]

                    sendmessage_wb.send_message_about2(sum0, int(li4[0][2]), time_jian)

                    del li4[0]

            # 去拍手动判断是否上汽视频
            if len(li5) != 0:
                li5.sort(key=takeSecond)
                if now_time > li5[0][1]:
                    k = 1
                    # 录像
                    get_photo_time, file_name = take_cv2.control_1(3, FILE_PATH_VIDEO, FILE_PATH_PIC)
                    # 上传
                    takevideo.take_video(li5[0][2], li5[0][0], get_photo_time, file_name)
                    # 删除列表第一个元素

                    del li5[0]

            if k == 0:
                break


        with open('12345.txt', 'w') as file_object:
            file_object.write('本次时间为')

        if len(li2)>49:
            del li2[0]

        print("现在的时间是%s" % datetime.datetime.now())
        time.sleep(5)


if __name__ == '__main__':
    dosomething()