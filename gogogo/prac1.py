import datetime
import time

li=[]
now_time=datetime.datetime.now()
li.append(datetime.datetime(2021, 6, 30, 1, 46, 18))

# li[0]=datetime.datetime.strftime(li[0],'%H:%M:%S')
print(li[0])


now_time=datetime.datetime.now()

# now_time=now_time.strftime('%H:%M:%S')

i=(now_time-li[0]).seconds
print (i)
time.sleep(i)

print(now_time)

