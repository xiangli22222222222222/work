import os
import datetime
import time

import shouhu

def shouhu(file_name):
    while 1:
        exitor=os.path.exists(file_name)
        if exitor:
            with open(file_name,'r') as f:
                content=f.read()
                content.replace('\n', '').replace('\r', '')
                now_time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                d = datetime.datetime.strptime(content,'%Y-%m-%d %H:%M:%S')
                miaoshu=(now_time-d).second
                miaoshu=int(miaoshu)

                if miaoshu>10:
                    shouhu.beishouhu(file_name)
                else:
                    os.remove(file_name)
    time.sleep(10)




if __name__=='__main__':
    file_name='shouhu.txt'
    shouhu(file_name)