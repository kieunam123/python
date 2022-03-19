# Kieu Vu Hoai Nam
# B1807650

# cau 1
# Kieu Vu Hoai Nam
# B1807650
def bt1():
    name=input("nhập tên của bạn :")
    print("Hello " + name + ", Welcome to Python")

# cau 2
# Kieu Vu Hoai Nam
# B1807650
def bt2():
    while True:
        try:
            n = input('nhập vào n (0<n<10): ')
            if 0<int(n)<10:
                break
            else:
                print('n phải lớn hơn 0 và nhỏ hơn 10, nhập lại: ')
        except ValueError:
            print('sai dữ liệu đầu vào! nhập lại : ')
    print('%c + %c%c + %c%c%c + %c%c%c%c ='%(n,n,n,n,n,n,n,n,n,n),int(n)+int(n+n)+int(n+n+n)+int(n+n+n+n))

# cau 3
# Kieu Vu Hoai Nam
# B1807650
def bt3():
    while True:
        try:
            a=input('nhập a : ')
            b=input('nhập b : ')
            if int(b)!=0: break
            else:
                print('vui lòng nhập b khác 0')
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại : ')
    print(a+' + '+b+' =',int(a)+int(b))
    print(a+' - '+b+' =',int(a)-int(b))
    print(a+' x '+b+' =',int(a)*int(b))
    print(a+' / '+b+' =',int(a)//int(b))
    print(a+' % '+b+' =',int(a)%int(b))
    print(a+' ^ '+b+' =',int(a)**int(b))

# cau 4
# Kieu Vu Hoai Nam
# B1807650
from cmath import pi
from tkinter import N
def bt4():
    while True:
        try:
            n = input('nhập bán kính R : ')   
            if n!=int(n) : break
            else : print('vui lòng nhập đúng dữ liệu')     
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại: ')

    print('chu vi hình tròn là : ',round((2*pi*int(n)),2))
    print('diện tích hình tròn là : ',round((round((2*pi*int(n)),2)*pi),2))

# cau 5
# Kieu Vu Hoai Nam
# B1807650
def giaithua(n):
    if n == 0:
        return 1
    return n * giaithua(n-1)
def bt5():
    while True:
        try:
            n = input('nhập số nguyên n : ')
            if int(n) > 0 : break
            else : print('Vui lòng nhập n > 0')
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại: ')
    print('n! = ',giaithua(int(n)))

