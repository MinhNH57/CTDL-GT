st = [1,2,3,4,5,6]
st.append(30)
print(st)
st.pop()
print(st)
#VD Tìm giá trị lớn nhất ở trong Stack
import numpy.random as rd
st1 = rd.randint(100 , size = (20))
st1 = list(st1)
print(st1)
m = st.pop() 
while(st1 != []):
    b = st1.pop()
    if(b > m) :
        m = b
print("Giá trị lớn nhất :" , m)