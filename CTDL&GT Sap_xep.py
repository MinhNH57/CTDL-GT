m = [6,5,3,1,8,7,2,4]
lap = range(len(m) - 1 , -1 , -1)
for i in lap:
    for j in range(0 , i , 1):
        if(m[j] > m[j+1]):
            temp = m[j]
            m[j] = m[j + 1]
            m[j+1] = temp
print(m)