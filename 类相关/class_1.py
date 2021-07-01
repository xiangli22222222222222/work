class Person(): #定义类
    def __init__(self,name,leg=8): #构造函数带参数
        self.name=name
        self.leg=leg
    def run(self):
        print("我会跑")
        print(self.name)
        print(self.leg)
    def fly(self):
        print("我会飞")

zwj=Person("xiaomei") #实例化时需要带参数
zwj.run()