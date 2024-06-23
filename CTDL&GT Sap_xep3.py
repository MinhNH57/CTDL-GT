m = [6,5,3,1,8,7,2,4,99,4,2,100]
for i in range(0 , len(m) - 1,1):
    lnn = i
    for j in range(i+1 , len(m), 1):
        if(m[j] < m[lnn]):
            lnn = j
    temp = m[lnn]
    m[lnn] = m[i]
    m[i] = temp
print(m)