import os
file_name=os.listdir("e:/work/gogogo")

for i in file_name:
    file_name2="e:/work/gogogo"+"//"+i
    os.remove(file_name2)
