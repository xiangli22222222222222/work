import datetime
import time


def beishouhu(file_name):
    while 1:
        with open(file_name, 'a+') as file_object:
            now_time=datetime.datetime.now()
            file_object.write(str(now_time))
        print ("写入完成")
        time.sleep(10)
if __name__=='__main__':
    file_name='shouhu.txt'
    beishouhu(file_name)