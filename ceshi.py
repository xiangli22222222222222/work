import os
f=os.listdir("C:/Users/admin/Desktop/m")

for f1 in f:
    print(f1)
    (f2,f3)=os.path.splitext(f1)
    print (f2)