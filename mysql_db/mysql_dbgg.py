import datetime
import pymysql


def mysql_db(sqlset,i):

    #���ݿ��������
    db = pymysql.connect(host='rm-8vb3v2iodf4hbi2r6fo.mysql.zhangbei.rds.aliyuncs.com', port=3306, user='root',
                         password='instantjuhuicatering@', db='instantjuhuicatering', charset='utf8')

    # �����α�
    cur = db.cursor()
    # ȡ���24Сʱ���ڵ�����
    now_time=datetime.datetime.now() + datetime.timedelta(days=0,hours=i)

    # sql�﷨
    sql = sqlset
    # ִ�в�ѯ����
    cur.execute(sql)
    data = cur.fetchall()

    return(data)



if __name__=='__main__':

     mysql_db()