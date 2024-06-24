m = [7,5,16,15,99,6,18]
print(m)
def HoanDoi(ds , i , j):
    tg = ds[i]
    ds[i] = ds[j]
    ds[j] = tg

def VunGoc(ds , g , l):
    if(2*g+1 == l):
        if(ds[2*g+1] > ds[g]):
            HoanDoi(ds , g , 2*g+1)
    else:
        if(ds[2*g+1] > ds[2*g+2]):
            j = 2*g+1
        else:
            j = 2 * g +2 
        if ds[g] < ds[j]:
            HoanDoi(ds , g , j)

def VunCay(ds):
    l = len(ds) -1
    g = len(ds) // 2 -1
    while (l >= 0):
        for j in range(g , -1 ,-1):
            VunGoc(ds , j , l)
        HoanDoi(ds , 0 , l)
        l = l-1
        g = (l+1) // 2 -1 


VunCay(m)