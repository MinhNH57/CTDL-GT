# Kiểu dữ liệu số trong python 
# Thư viện Math
a = 4 #Gan gia tri bien la 4 , Voi 4 la kieu so nguyen
# print(a)
# print(type(a))

b = 1.984534543534534545435435435345 
print(b)
print(type(b))

#improt thu vien de lay toan bo noi dung cua thu vien
# Tu thu vien decimal import tat ca moi thu vao
from decimal import*

#lay toi da 30 chu so phan nguyenva phan thap phan
getcontext().prec = 30
Decimal(10)/Decimal(3)
print(Decimal(10)/Decimal(3))

#Phan so 
from fractions import*
a= Fraction(9,6)
print(a)
print(type(a))

#So phuc
# So phuc co cau trc la :<Phan thuc> + <Phan ao>j 
c=complex(2,5)
print(c)
#lay phan thuc
print(c.real)
#Lay phan ao 
print(c.imag)
#Chia lay phan nguyen
d = 10//3
print(d)
#chia lay phan du
e = 10/4
print(e)

#Thu vien Math 
import math