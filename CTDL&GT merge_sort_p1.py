a = [1,3,5,7,99]
b = [2,6,100]
c = []
while (a != []) and (b != []) :
    if(a[0] < b[0]):
        c.append(a[0])
        a = a[1:]
    else:
        c.append(b[0])
        b = b[1:]
if (a !=[]): c = c + a
if (b!= []) : c = c +b
print(c)