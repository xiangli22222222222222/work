import datetime
import traceback
import pymysql


def mysql_db(i):

    #数据库基本属性
    db = pymysql.connect(host='rm-8vb3v2iodf4hbi2r6fo.mysql.zhangbei.rds.aliyuncs.com', port=3306, user='root',
                         password='instantjuhuicatering@', db='instantjuhuicatering', charset='utf8')

    # 定义游标
    cur = db.cursor()
    # 取最近24小时以内的数据
    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)
    print(now_time)

    # sql语法
    sql = "SELECT * FROM datastreamsdevice WHERE (datastreamsdevice.key = '%s'  and datastreamsdevice.create_date > '%s') ORDER BY datastreamsdevice.create_date ASC" % (
        'token TCS_Hmj_ChengMi0n8cb81f117897a36880atend', now_time)
    # 执行查询操作
    cur.execute(sql)
    data = cur.fetchall()

    return(data)



if __name__=='__main__':
    data=mysql_db(-24)
    i=0
    for data1 in data:
        print(data1)
        if float(data1[10])==2.65:
            i+=1
    print(i)