import datetime
import pymysql


def mysql_db(i,sqlqure):

    #数据库基本属性
    db = pymysql.connect(host='rm-8vb3v2iodf4hbi2r6fo.mysql.zhangbei.rds.aliyuncs.com', port=3306, user='root',
                         password='instantjuhuicatering@', db='instantjuhuicatering', charset='utf8')

    # 定义游标
    cur = db.cursor()


    # sql语法
    sql =sqlqure
    # 执行查询操作
    cur.execute(sql)
    data = cur.fetchall()

    return(data)

def get_db(i,sqlselect):
    # 取最近24小时以内的数据
    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)

    if sqlselect==1:
        print("这次拿第一个灶眼")
        sql="SELECT * FROM datastreamsonoff WHERE datastreamsonoff.key = '%s' and datastreamsonoff.create_date > '%s' ORDER BY datastreamsonoff.create_date ASC" % (
            'token 0870c9a90075b54639524eae86304a06202787c8',now_time)
    else:
        sql="SELECT * FROM datastreamsonoff WHERE datastreamsonoff.key = '%s' and datastreamsonoff.create_date > '%s' ORDER BY datastreamsonoff.create_date ASC" % (
            'token d254b573257ed1078c30f5fcc8171a31dbc3064d',now_time)
    data=mysql_db(i,sql)
    return (data)
if __name__=='__main__':

     get_db(-32,1)