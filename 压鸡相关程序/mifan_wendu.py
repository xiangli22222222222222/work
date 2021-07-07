import datetime
import mysql_dbggg
import sendmessage_gg


def get_data(steam_cooker):

    #从数据拿数据
    i=-32

    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)

    if int(steam_cooker)==3:

        sqlset = "SELECT * FROM at_temperature WHERE at_temperature.rid = '%s' and at_temperature.del_flag = '%s' and (at_temperature.t_array = '%s' or at_temperature.t_array > '%s') and at_temperature.create_date > '%s' ORDER BY at_temperature.create_date ASC" % (
            '201010071','2','100','98',now_time)
    elif int(steam_cooker)==2:

        sqlset = "SELECT * FROM at_temperature WHERE at_temperature.rid = '%s' and at_temperature.del_flag = '%s' and (at_temperature.t_array = '%s' or at_temperature.t_array > '%s') and at_temperature.create_date > '%s' ORDER BY at_temperature.create_date ASC" % (
            '201010071','1','100','98',now_time)

    data=mysql_dbggg.mysql_db(sqlset)

    return (data)


def work_data(date_time_zf,date_time_zfjs,steam_cooker):


    li=[]
    li2=[]

    data=get_data(steam_cooker)
    # print(len(data))

    for data1 in data:
        li1 = []
        for data2 in data1:
            li1.append(data2)
        li.append(li1)
    # while 1:
    # print (li)
    for i in range(len(li)):
        li2_1=[]
        date_time1=li[i][9]
        date_time1=date_time1+datetime.timedelta(hours=8)
        print(date_time_zf,date_time_zfjs)
        if date_time1>date_time_zf and date_time1<date_time_zfjs:
            li2_1.append(li[i][11])
            li2_1.append(date_time1)
        li2.append(li2_1)
    # print(li2)
    return (li2)


        # sendmessage_gg.send_message(appsecret,content,ad_id)


if __name__=='__main__':
    work_data()