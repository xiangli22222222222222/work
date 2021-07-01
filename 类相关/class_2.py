class Person(): #定义类
    def __init__(self): #构造函数不带参数
       print("jjj")
    def run(self,name,leg=8): #实例方法带参数
        print("我会跑")
        print(name)
        print(leg)
    def fly(self):
        print("我会飞")

zwj=Person() #实例化时不需要带参数
zwj.run("xiaomei") #调取方法需要带参数