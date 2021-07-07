import datetime
import time
import os


def mm():
    file_name = '1.txt'
    file_times_modified = time.localtime(os.path.getmtime(file_name))
    year_modified = file_times_modified.tm_year
    month_modified = file_times_modified.tm_mon
    day_modified = file_times_modified.tm_mday

    hour_modified = file_times_modified.tm_hour
    minute_modified = file_times_modified.tm_min
    second_modified = file_times_modified.tm_sec
    time_jian=str(year_modified)+'-'+str(month_modified)+'-'+str(day_modified)+' '+str(hour_modified)+':'+str(minute_modified)+':'+str(second_modified)
    print(time_jian)
    dd=datetime.datetime.strptime(time_jian,"%Y-%m-%d %H:%M:%S")

    now_time=datetime.datetime.now()

    print(now_time)

    dd_seconds=(now_time-dd).seconds

    if dd_seconds>60:
    #     start_dire=r"C:/Users/admin/PycharmProjects/work/mysql_db/cv3.py"
        r=os.system('python ceshi3.py')
        print(r)
    print(dd_seconds)
if __name__ == '__main__':
    mm()
