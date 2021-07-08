import mysql_dbggg
import datetime





def jiashui(start_time):


    i=-16

    before30_start_time=start_time+datetime.timedelta(minutes=-30)

    sqlset = "SELECT * FROM datastreamsonoff WHERE datastreamsonoff.key = '%s' and datastreamsonoff.create_date > '%s' and datastreamsonoff.create_date < '%s'  ORDER BY datastreamsonoff.create_date ASC" % (
        'token b5a0ca4a762fb7cd5c29ee64482e49dc7652db9a',before30_start_time,start_time)


    data=mysql_dbggg.mysql_db(sqlset)
    print(data)
    return (data)


if __name__=='__main__':

    jiashui()