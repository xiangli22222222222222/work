import mysql_dbggg
import datetime





def chengzhong(start_time):


    i=-16

    before30_start_time=start_time+datetime.timedelta(minutes=-30)

    sqlset = "SELECT * FROM datastreamsdevice WHERE datastreamsdevice.key = '%s' and datastreamsdevice.create_date > '%s' and datastreamsdevice.create_date < '%s'  ORDER BY datastreamsdevice.create_date ASC" % (
        'token TCS_Hmj_ChengMi0n8cb81f117897a36880atend',before30_start_time,start_time)


    data=mysql_dbggg.mysql_db(sqlset)
    print(data)
    return (data)


if __name__=='__main__':

    chengzhong()