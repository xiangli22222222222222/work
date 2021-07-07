import os.path

import datetime

print(__file__)

filename=os.path.dirname( os.path.abspath(__file__) )+'/12345.txt'

print(filename)


get_time=os.path.getmtime(filename)
print(get_time)

get_time=datetime(get_time)

print(get_time)
now_time=datetime.datetime.now()
seconds=(now_time-get_time).seconds

print (seconds)