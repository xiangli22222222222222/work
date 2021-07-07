import multiprocessing
import time
import ceshi2
import main_borad


# 拷贝任务
def work():
    print("复制中...", multiprocessing.current_process().pid)
    # 获取当前进程的守护状态
    # 提示：使用进程池创建的进程是守护主进程的状态，默认自己通过Process创建的进程是不是守住主进程的状态
    # print(multiprocessing.current_process().daemon)
    time.sleep(0.5)


if __name__ == '__main__':
    # 创建进程池
    # 3:进程池中进程的最大个数
    pool = multiprocessing.Pool(3)
    # 模拟大批量的任务，让进程池去执行
    for i in range(5):
        # 循环让进程池执行对应的work任务
        # 同步执行任务，一个任务执行完成以后另外一个任务才能执行
        # pool.apply(work)
        # 异步执行，任务执行不会等待，多个任务一起执行

        pool.apply_async(work)

        pool.apply_async(ceshi2.dayin())

        pool.apply_async(main_borad.dosomething())

    # 关闭进程池，意思告诉主进程以后不会有新的任务添加进来
    pool.close()
    # 主进程等待进程池执行完成以后程序再退出
    pool.join()