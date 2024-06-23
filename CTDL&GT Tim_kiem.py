#Tim kiem tuan tu
m = [3,5,8,13,28,19,21,27,32]
def tktt(dx , x):
    lapds = range(0 , len(dx) , 1)
    dc = -1 
    for i in lapds:
        if(dx[i] == x):
            dc = i
    return(dc)
print(tktt(m , 32))

def  tmnp(ds , x):
    l = 0
    r=len(ds) - 1 
    while (l <= r):
        c = (l + r) //2
        if(ds[c] == x):
            return(x,"Có địa chỉ là " , c)
        elif (ds[c] > x):
            r = c -1 
        else : 
            l = c + 1 
print(tmnp(m , 32))