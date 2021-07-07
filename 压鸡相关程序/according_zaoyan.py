

def get_po(pozison):
    if pozison==3:
        x_race=78
        y_race=441
    elif pozison==1:
        x_race=48
        y_race=160
    elif pozison==2:
        x_race=316
        y_race=390
    elif pozison==0:
        x_race=48
        y_race=160
    elif pozison==4:
        x_race=359
        y_race=734
    elif pozison==5:
        x_race=101
        y_race=720

    return(int(x_race),int(y_race))
if __name__=='__main__':
    get_po()
