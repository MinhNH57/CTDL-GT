print("Nhập vào sso thập phân cần chuyển đổi:")
tp = int(input())
st = []
while (tp != 0):
    sd = tp % 2 
    st.append(sd)
    tp = tp//2
print(st)
b = ""
while(st != []):
    b = b + str(st.pop())
print("Nhi phan :" ,b)