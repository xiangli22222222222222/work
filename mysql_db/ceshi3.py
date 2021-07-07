import datetime
# str转时间格式：
dd = '2019-03-17 11:00:00'
print(type(dd))
dd = datetime.datetime.strptime(dd, "%Y-%m-%d %H:%M:%S")
print(dd,type(dd))

# 时间格式转str:
dc = dd.strftime("%Y-%m-%d %H:%M:%S")
print(dc,type(dc))