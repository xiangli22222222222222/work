import threading
import time

count = 0

"""注： 可以参考这篇博客https://blog.csdn.net/l835311324/article/details/86608850的示例2，
这个MyThread类继承了threading模块的Thread类，对其下面的run方法进行了重写"""

class MyThread(threading.Thread):
    def __init__(self , threadName):
        super(MyThread,self).__init__(name=threadName)
    """一旦这个MyThread类被调用，自动的就会运行底下的run方法中的代码，
    因为这个run方法所属的的MyThread类继承了threading.Thread"""
    def run(self):
        global count
        for i in range(100):
            count += 1
            time.sleep(0.3)
            print(self.getName() , count)


for i in range(2):
    MyThread("MyThreadName:" + str(i)).start()