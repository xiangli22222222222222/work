import datetime
import time

now=datetime.datetime.now()
print(type(now))

date_time=datetime.datetime(2021, 6, 28, 0, 3, 15)

print(type(date_time))

while now < date_time:
    now = datetime.datetime.now()
    time.sleep(5)
    print("wait a monent!")
print(datetime.datetime.now())
