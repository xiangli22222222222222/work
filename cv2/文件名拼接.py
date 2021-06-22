import os  # 导入os库
url = 'D:\\data\\'
file_list = os.listdir(r'D:\\data') # 读取目录下的所有文件
print(file_list)
print("-------------我是一条分割线-----------------")
for file in file_list:
    dirs = url + file  # 目录与文件名拼接构成完整目录
    print(dirs)

-------------------------------------------------------------------

timepath=time.strftime('%Y/%m/%d/',time.localtime(time.time()))


newpath="/mnt/data/resources/other/"+

filetype=f.name.split(".")[-1]#获取文件类型

