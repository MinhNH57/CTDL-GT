#Viết chương trình tính và hiển thị ra màn hình tích của tổng các chữ số chẵn và tổng các chữ số lẻ của một số tự nhiên nhập từ bàn phím.
try:
    n = int(input())
    if n <= 0 :
        print("Vui long nhap mot so nguyen")
    else :
        TongSoLe = 0 
        TongSoChn = 0
        while n > 0 :
            if n % 2 :
                TongSoChn += n % 10
            else :
                TongSoLe += n % 10
            n = n// 10
        Ketqua = TongSoChn * TongSoLe
        print(Ketqua)
except :
        print("Loi")