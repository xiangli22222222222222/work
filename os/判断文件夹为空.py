import os


def os_dir(dir):
    if os.listdir(dir):
        print("文件夹里啥也没有")
    else:
        print("好牛逼的文件夹")

path =input('input_path:')
os_dir(path)