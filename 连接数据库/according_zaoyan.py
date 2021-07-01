

def get_po(pozison):
    if pozison==3:
        x_race=94
        y_race=448
    elif pozison==1:
        x_race=57
        y_race=164
    elif pozison==2:
        x_race=321
        y_race=394
    elif pozison==0:
        x_race=57
        y_race=164
    elif pozison==4:
        x_race=321
        y_race=394
    elif pozison==5:
        x_race=57
        y_race=164

    return(int(x_race),int(y_race))
if __name__=='__main__':
    get_po()
