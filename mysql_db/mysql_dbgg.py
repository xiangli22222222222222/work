import datetime
import pymysql


def mysql_db(sqlset,i):

    #数据库基本属性
    db = pymysql.connect(host='rm-8vb3v2iodf4hbi2r6fo.mysql.zhangbei.rds.aliyuncs.com', port=3306, user='root',
                         password='instantjuhuicatering@', db='instantjuhuicatering', charset='utf8')

    # 定义游标
    cur = db.cursor()
    # 取最近24小时以内的数据
    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)

    # sql语法
    sql = sqlset
    # 执行查询操作
    cur.execute(sql)
    data = cur.fetchall()

    return(data)



if __name__=='__main__':

     mysql_db()