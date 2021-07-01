import datetime

now=datetime.datetime.now()

now_time=datetime.datetime.strptime(now,'%H,%M,%S')

print(now)