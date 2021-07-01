import cv2
import datetime
import os


file_path='E:/work/123/322/'
r=[]
g=[]
b=[]
m = 0
data=os.listdir(file_path)
for data1 in data:
    print(data1)
    i = 0
    j = 0
    k = 57
    p = 164
    file_path1=file_path+data1
    img = cv2.imread(file_path1)  #读取图像
    while i <100:
        while j<100:

            j+=1
            get_color=img[k,p]

            r.append(get_color[2])
            g.append(get_color[1])
            b.append(get_color[0])
            p+=1
        j=0
        p=164
        i+=1
        k+=1
        print(len(r))
        print(i)
    m+=1
print(m)
print(datetime.datetime.now())
print(len(r))
sum=0

for p in range(m-1):
    sum=0
    for o in range(10000):
        # print(g[o*p],g[o+10000])
        sum=sum+(abs(int(g[10000+o+p*10000])-int(g[o+p*10000])))
    print(sum)
    sum=sum/10000
    print(sum)
    p+=1

