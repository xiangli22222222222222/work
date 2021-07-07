
def duiying(zaoyan):
    zaoyan = int(zaoyan)
    zaoyan1 = 0
    zaoyan2 = 0
    if zaoyan == 0:
        zaoyan1 = 1
        zaoyan2 = 1
    elif zaoyan == 1:
        zaoyan1 = 2
        zaoyan2 = 1
    elif zaoyan == 2:
        zaoyan1 = 1
        zaoyan2 = 2
    elif zaoyan == 3:
        zaoyan1 = 2
        zaoyan2 = 2
    elif zaoyan == 4:
        zaoyan1 = 1
        zaoyan2 = 3
    elif zaoyan == 5:
        zaoyan1 = 2
        zaoyan2 = 3
    return (zaoyan1, zaoyan2)

if __name__=='__main__':
    duiying()