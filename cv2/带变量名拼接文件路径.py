import os

n=1
n=str(n)
file_path=os.path.join('e:/video/',n,'2.avi')

file_size=os.path.getsize(file_path)


f=open(file_path,'r')


print(file_size)

print (f)
