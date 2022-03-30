# Kieu Vu Hoai Nam
# B1807650
# Cau 1
def cau1():
    num = ""
    char = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isdigit(): 
            num+=i
        else: char+=i
    print("số lượng chữ số trong câu : ", len(num))
    print("số lượng chữ cái trong câu : ", len(char)) 
    
# Kieu Vu Hoai Nam
# B1807650
# Cau 2
def cau2():
    upper = ""
    lower = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isupper():
            upper+=i
        else : lower+=i
    print("số chữ hoa là : ", len(upper))
    print("số chữ thường là : ", len(lower))

# Kieu Vu Hoai Nam
# B1807650
# Cau 3
def cau3():
    char = ""
    s = input("nhập vào câu của bạn : ")
    for i in s:
        if i.isupper():
            char+=i
        else: char+=i.upper()
    print("các chữ cái đã được in hoa : ",char)

# Kieu Vu Hoai Nam
# B1807650
# Cau 4
def cau4():
    values = []
    for i in range(100, 301):
        s = str(i)
        if (int(s[0])%2!=0) and (int(s[1])%2!=0) and (int(s[2])%2!=0):
            values.append(s)
    print (",".join(values))

# Kieu Vu Hoai Nam
# B1807650
# Cau 5
def cau5():
    chan=[]
    items=[x for x in input("Nhập chuỗi cách nhau bởi dấu phẩy: ").split(',')]
    for i in items:
        if int(i)%2!=0:
            chan.append(i)
    print("Các số lẻ trong chuỗi: ",",".join(chan))

# Kieu Vu Hoai Nam
# B1807650
# Cau 6
def cau6():
    for i in range(1,21):
        print(str(i)+"-"+str(i**2))

# Kieu Vu Hoai Nam
# B1807650
# Cau 7
def cau7():
    list=[12,24,35,70,88,120,155]
    del list[0] 
    del list[3]
    del list[3]
    print(list)

# Kieu Vu Hoai Nam
# B1807650
# Cau 8
def cau8():
    list1={12,3,78,35,55,120}
    list2={12,24,35,78,88,120,155}
    print(list1 & list2)

# Kieu Vu Hoai Nam
# B1807650
# Cau 9
def cau9():
    mang=[]
    for i in range (5,21):
        mang.append(str(i**2))
    print(",".join(mang))

# Kieu Vu Hoai Nam
# B1807650
# Cau 10
def cau10():
    mang=[]
    kq=[]
    print("nhập vào tuple gồm 7 số : ")
    for i in range (1,8):
        while True:
            try:
                n = input("số thứ %d : "%i)
                if n.isnumeric() : break
                else : print("vui lòng nhập số")
            except ValueError: print("dữ liệu đầu vào ko hợp lệ")
        tuple[n]
        mang.append(n)
    for a in mang:
        if int(a)%2==0:
            kq.append(a)
            tuple[kq]
    print(kq)

# Kieu Vu Hoai Nam
# B1807650
# Cau 11
def cau11():
    string = input("nhập vào câu của bạn : ")
    count={}
    for i in string:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    for i in sorted(count, key=count.get, reverse=False):
        print(i, count[i])

# Kieu Vu Hoai Nam
# B1807650
# Cau 12
def cau12():
    chuoi=input("Nhập chuỗi : ")
    chuoi = chuoi[::-1]
    print (chuoi)
