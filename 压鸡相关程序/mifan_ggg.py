import datetime
import mysql_dbggg
import sendmessage_gg
import mifan_wendu
import mifan_chengzhong
import mifan_jiashui

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
        date_time_meijia=li[i][4]
        date_time_zf=date_time_zf+datetime.timedelta(hours=8)

        if li[i][10]:

            #判断时间
            date_time1_zfjs = li[i][10]
            time_plus30=date_time1_zfjs+datetime.timedelta(minutes=30)
            date_time1_zfjs = date_time1_zfjs + datetime.timedelta(hours=8)
            zfys=(date_time1_zfjs-date_time_zf).seconds
            zfys= round(zfys / 60, 0)


            time_diff=mifan_wendu.work_data(li[i][4],time_plus30,li[i][7])
            print(date_time_zf,date_time1_zfjs)


            for j in range(len(time_diff)):

                if int(time_diff[j][0])>98:
                    orign_time=time_diff[j][1]

                    for k in range(j+1,len(time_diff)):
                        if int(time_diff[k][0])<99:
                            end_time=time_diff[k][1]

                            subtract=(end_time-orign_time).seconds
                            subtract= round(subtract / 60, 0)

                            print("100度维持了%s分钟"%subtract)
                            break
                    break

            content = str(li[i][7]) + "号蒸箱，" + str(li[i][8]) + "盘，开始： " + str(date_time_zf)+"结束： "+str(date_time1_zfjs)+"用时： "+str(zfys)+" 分钟，100度："+str(subtract)+"分钟"
            sendmessage_gg.send_message(appsecret, content, ad_id)

        else:
            now_time2=datetime.datetime.now()

            if (now_time2-date_time_zf).seconds<6600:
            #     print("真有啊！")
                content = str(li[i][7]) + "号蒸箱，" + str(li[i][8]) + "盘，开始： " + str(date_time_zf) + " 目前饭还没有蒸好！"
            #
            else:
                content ="我是一条操作失误的点火记录！"

            sendmessage_gg.send_message(appsecret,content,ad_id)


       #处理称重数据： 把蒸饭前的30分钟的称重信息拿回来

        weight=mifan_chengzhong.chengzhong(date_time_meijia)
        print(len(weight))
        count_265=0
        count_255=0
        count_275=0
        count_26=0
        count_27=0
        len_weigh=len(weight)
        len_weigh-=1
        for l in range(len_weigh):
            print(weight[l+1][10])
            if float(weight[l][10])==2.65 and float(weight[l+1][10])<0:
                print("我拿到了啊，谁说我没拿到")
                count_265+=1
            elif float(weight[l][10])==2.55 and float(weight[l+1][10])<0:
                count_255+=1
            elif float(weight[l][10]) == 2.6 and float(weight[l+1][10])<0:
                count_26 += 1
            elif float(weight[l][10]) == 2.7 and float(weight[l+1][10])<0:
                count_27 += 1
            elif float(weight[l][10]) == 2.75 and float(weight[l+1][10])<0:
                count_275 += 1

        count=count_27+count_265+count_255+count_275+count_265
        content = "本次有效："+str(count)+"标准："+str(count_265)+"2.6和2.7分别："+str(count_26)+str(count_27)+"2.55和2.75分别: "+str(count_255)+str(count_275)
        sendmessage_gg.send_message(appsecret, content, ad_id)

        #处理加水数据：

        jiashui = mifan_jiashui.jiashui(date_time_meijia)
        len_jiashui=len(jiashui)
        len_jiashui-=1
        count_jiashui=0
        for n in range(len_jiashui):
            if int(jiashui[n][8])==1761:
                count_jiashui+=1


        content = "本次加水："+str(count_jiashui)

        sendmessage_gg.send_message(appsecret, content, ad_id)

if __name__=='__main__':
    work_data()