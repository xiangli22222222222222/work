import datetime
import mysql_dbggg
import sendmessage_gg
import mifan_wendu


def get_data():

    #从数据拿数据
    i=-32

    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)


    sqlset = "SELECT * FROM steamedricerecord WHERE steamedricerecord.tid = '%s' and steamedricerecord.update_date > '%s' ORDER BY steamedricerecord.create_date ASC" % (
        '201010071',now_time)

    data=mysql_dbggg.mysql_db(sqlset)

    return (data)

def work_data():

    #发消息用的secret和agend_id
    appsecret = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww17c795da4df0c791&corpsecret=USnk3lD9ogaBObZIE3faWxpmsBH8lV7ohbqYjVVPtcA"
    ad_id = 1000005
    li=[]
    data=get_data()

    for data1 in data:
        li1 = []
        for data2 in data1:
            li1.append(data2)
        li.append(li1)
    # print(li)
    # while 1:

    for i in range (len(li)):
        date_time_zf=li[i][4]
        date_time_zf=date_time_zf+datetime.timedelta(hours=8)

        if li[i][10]:

            #判断时间
            date_time1_zfjs = li[i][10]
            date_time1_zfjs = date_time1_zfjs + datetime.timedelta(hours=8)
            zfys=(date_time1_zfjs-date_time_zf).seconds
            zfys= round(zfys / 60, 2)


            time_diff=mifan_wendu.work_data(date_time_zf,date_time1_zfjs,li[i][7])
            print(date_time_zf,date_time1_zfjs)


            for j in range(len(time_diff)):
                print("你们要的温度来拉，，，，，，，，，，，，，，%s"%time_diff[j])



            content = "黄焖鸡人员用第" + str(li[i][7]) + "号蒸箱，蒸饭 " + str(li[i][8]) + " 盘，蒸饭时间为： " + str(date_time_zf)+"蒸好时间为： "+str(date_time1_zfjs)+"蒸饭用时为： "+str(zfys)
        else:
            content = "黄焖鸡人员用第" + str(li[i][7]) + "号蒸箱，蒸饭 " + str(li[i][8]) + " 盘，蒸饭时间为： " + str(date_time_zf) + " 目前饭还没有蒸好！"

        sendmessage_gg.send_message(appsecret,content,ad_id)


if __name__=='__main__':
    work_data()