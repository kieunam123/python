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
            n = int (input('nhập vào n (0<n<10): '))
            if 0<n<10:
                break
            else:
                print('n phải lớn hơn 0 và nhỏ hơn 10, nhập lại: ')
        except ValueError:
            print('sai dữ liệu đầu vào! nhập lại : ')
    print('%c + %c%c + %c%c%c + %c%c%c%c ='%(n,n,n,n,n,n,n,n,n,n),n+(n+n)+(n+n+n)+(n+n+n+n))

# cau 3
# Kieu Vu Hoai Nam
# B1807650
def bt3():
    while True:
        try:
            a=float(input('nhập a : '))
            b=float(input('nhập b : '))
            if b!=0: break
            else:
                print('vui lòng nhập b khác 0')
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại : ')
    print(a+' + '+b+' =',a+b)
    print(a+' - '+b+' =',a-b)
    print(a+' x '+b+' =',a*b)
    print(a+' / '+b+' =',a//b)
    print(a+' % '+b+' =',a%b)
    print(a+' ^ '+b+' =',a**b)

# cau 4
# Kieu Vu Hoai Nam
# B1807650
from cmath import pi
from email.policy import default
import math
from tkinter import N
def bt4():
    while True:
        try:
            n = input('nhập bán kính R : ')   
            if n!=float(n) : break
            else : print('vui lòng nhập đúng dữ liệu')     
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại: ')

    print('chu vi hình tròn là : ',round((2*pi*float(n)),2))
    print('diện tích hình tròn là : ',round((round((2*pi*float(n)),2)*pi),2))

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
            n = int(input('nhập số nguyên n : '))
            if n > 0 : break
            else : print('Vui lòng nhập n > 0')
        except ValueError:
            print('sai dữ liệu đầu vào! Nhập lại: ')
    print('n! = ',giaithua(n))

# cau 6
# Kieu Vu Hoai Nam
# B1807650
def bt6():
    try:
        delta = 0
        a=float(input('nhập a : '))
        b=float(input('nhập b : '))
        c=float(input('nhập c : '))
        delta = ((b)**2)-4*(a)*(c)
        if delta > 0 :
            print('phương trình có 2 nghiệm')
            print('x1 = ',(-(b)+math.sqrt(delta))//(2*(a)))
            print('x2 = ',(-(b)-math.sqrt(delta))//(2*(a)))
        elif delta == 0 :
            print('phương trình có nghiệm kép')
            print('x1 = x2 = ',-((b)//2*(a)))
        else : print('phương trình vô nghiệm')
    except ZeroDivisionError as err: 
        print("Math Error")

# cau 7
# Kieu Vu Hoai Nam
# B1807650
def bt7():
    string=''
    for i in range(5000,7000):
        if i%7==0 and i%5!=0 :
            string+=str(i)+" "
    print(string) 
        
# cau 8
# Kieu Vu Hoai Nam
# B1807650      
def decToBin(x):
        return int(bin(x)[2:])
def bt8():
    n=int(input('nhập số cần đổi sang nhị phân : '))
    print('hệ nhị phân của %d là : '%n,decToBin(n))

# cau 9
# Kieu Vu Hoai Nam
# B1807650     
def ucln(a,b):
    if (b == 0):
        return a
    return ucln(b, a % b)
def bcnn(a,b):
     return int((a * b) / ucln(a, b))

def bt9():
    a=int(input('nhập a : '))
    b=int(input('nhập b : '))
    print('ước chung lớn nhất a và b : ',ucln(a,b))
    print('bội chung nhỏ nhất a và b : ',bcnn(a,b))

# cau 10
# Kieu Vu Hoai Nam
# B1807650 
def is_snt(n):
    if (n<2):
        return False
    for i in range(2,int(math.sqrt(n)+1)) :
        if (n%i==0): return False
    return True

def bt10():
    snt=''
    n=int(input("nhập n : "))
    if n>=2:
        snt+="2"+" "
    for i in range(3,n+1):
        if(is_snt(i)):
            snt+=str(i)+" "
        i=i+2
    print(snt)

# cau 11
# Kieu Vu Hoai Nam
# B1807650 
def bt11():
    snt=''
    for i in range(1001,9999):
        if(is_snt(i)):
            snt+=str(i)+" "
        i+=1
    print(snt)

# cau 12
# Kieu Vu Hoai Nam
# B1807650 
def TongChuSo(n):
    tong=0
        tong += n % 10
def bt12():
    while True:
        try:
             n=int(input('nhập số nguyên n : '))
             if n>0: break
             else : print('Vui lòng nhập n > 0 ')
        except ValueError:
            print('Dữ liệu đầu vào không hợp lệ')            
   
    print('tổng của %d là : '%n,TonngChuSo(n))

