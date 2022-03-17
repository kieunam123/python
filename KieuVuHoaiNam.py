# Kieu Vu Hoai Nam
# B1807650

# cau 1
def bt1():
    name=input("nhập tên của bạn :")
    print("Hello " + name + ", Welcome to Python")

# cau 2
def bt2():
    while True:
        try:
            n = input('nhập vào n (0<n<10): ')
            if 0<int(n)<10:
                break
            else:
                print('n phải lớn hơn 0 và nhỏ hơn 10, nhập lại: ')
        except ValueError:
            print('sai dữ liệu đầu vào! nhập lại: ')
    print('%c + %c%c + %c%c%c + %c%c%c%c ='%(n,n,n,n,n,n,n,n,n,n),int(n)+int(n+n)+int(n+n+n)+int(n+n+n+n))

# cau 3



